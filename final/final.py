from __future__ import annotations

import csv
from dataclasses import dataclass
from datetime import date, datetime
from decimal import Decimal, InvalidOperation
from pathlib import Path
from typing import Iterable, List, Sequence


CSV_HEADERS: Sequence[str] = ("date", "category", "product", "amount")


@dataclass(frozen=True)
class Purchase:
    date: date
    category: str
    product: str
    amount: Decimal

    @staticmethod
    def from_csv_row(row: dict) -> "Purchase":
        d = parse_date((row.get("date") or "").strip())
        category = (row.get("category") or "").strip()
        product = (row.get("product") or "").strip()
        amount = parse_amount(row.get("amount", ""))

        if not category:
            raise ValueError("Категория не может быть пустой.")
        if not product:
            raise ValueError("Название продукта не может быть пустым.")

        return Purchase(date=d, category=category, product=product, amount=amount)

    def to_csv_row(self) -> dict:
        return {
            "date": self.date.isoformat(),
            "category": self.category,
            "product": self.product,
            "amount": str(self.amount),
        }


def parse_date(value: str) -> date:
    value = (value or "").strip()
    try:
        return datetime.strptime(value, "%Y-%m-%d").date()
    except Exception:
        raise ValueError("Неверная дата. Формат должен быть YYYY-MM-DD, например 2026-05-27.")


def parse_amount(value: str) -> Decimal:
    s = (value or "").strip().replace(",", ".")
    try:
        amount = Decimal(s)
    except (InvalidOperation, ValueError):
        raise ValueError("Неверная стоимость. Введите число (например 199.99).")

    if amount < 0:
        raise ValueError("Стоимость не может быть отрицательной.")
    if not (Decimal("2") <= amount <= Decimal("1000")):
        raise ValueError("Стоимость должна быть в диапазоне от 2 до 1000.")

    return amount.quantize(Decimal("0.01"))


class CsvPurchaseRepository:
    def __init__(self, csv_path: Path):
        self.csv_path = csv_path

    def ensure_exists(self) -> None:
        self.csv_path.parent.mkdir(parents=True, exist_ok=True)
        if not self.csv_path.exists():
            with self.csv_path.open("w", newline="", encoding="utf-8") as f:
                writer = csv.DictWriter(f, fieldnames=list(CSV_HEADERS))
                writer.writeheader()

    def load_all(self) -> List[Purchase]:
        self.ensure_exists()
        with self.csv_path.open("r", newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            if reader.fieldnames is None:
                raise ValueError("CSV файл повреждён: отсутствуют заголовки.")
            missing = [h for h in CSV_HEADERS if h not in reader.fieldnames]
            if missing:
                raise ValueError(f"CSV файл повреждён: нет колонок {missing}.")

            purchases: List[Purchase] = []
            for row in reader:
                if not any((row.get("date"), row.get("category"), row.get("product"), row.get("amount"))):
                    continue
                purchases.append(Purchase.from_csv_row(row))
            return purchases

    def append(self, purchase: Purchase) -> None:
        self.ensure_exists()
        with self.csv_path.open("a", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=list(CSV_HEADERS))
            writer.writerow(purchase.to_csv_row())

    def overwrite_all(self, purchases: Iterable[Purchase]) -> None:
        self.ensure_exists()
        with self.csv_path.open("w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=list(CSV_HEADERS))
            writer.writeheader()
            for p in purchases:
                writer.writerow(p.to_csv_row())

    def clear(self) -> None:
        self.overwrite_all([])


class MoneyTrackerApp:
    def __init__(self, repo: CsvPurchaseRepository):
        self.repo = repo

    def run(self) -> None:
        while True:
            print("\n=== Контроль денежных средств ===")
            print("1) Добавить покупку")
            print("2) Показать все покупки")
            print("3) Показать покупки по дате")
            print("4) Показать покупки по категории")
            print("5) Показать покупки по дате и категории")
            print("6) Сортировка по стоимости")
            print("7) Удалить запись по ID")
            print("8) Очистить все записи")
            print("0) Exit")
            choice = input("Выберите пункт меню: ").strip()

            try:
                if choice == "1":
                    self.add_purchase()
                elif choice == "2":
                    self.show_all()
                elif choice == "3":
                    self.show_by_date()
                elif choice == "4":
                    self.show_by_category()
                elif choice == "5":
                    self.show_by_date_and_category()
                elif choice == "6":
                    self.sort_by_amount()
                elif choice == "7":
                    self.delete_by_id()
                elif choice == "8":
                    self.clear_all()
                elif choice == "0":
                    print("Выход из программы.")
                    return
                else:
                    print("Неизвестный пункт меню.")
            except Exception as e:
                print(f"Ошибка: {e}")

    def add_purchase(self) -> None:
        print("\nДобавление покупки (формат даты: YYYY-MM-DD)")
        d = parse_date(input("Дата: ").strip())
        category = input("Категория: ").strip()
        product = input("Продукт: ").strip()
        amount = parse_amount(input("Стоимость (2..1000): ").strip())

        if not category:
            raise ValueError("Категория не может быть пустой.")
        if not product:
            raise ValueError("Название продукта не может быть пустым.")

        self.repo.append(Purchase(date=d, category=category, product=product, amount=amount))
        print("Покупка добавлена.")

    def show_all(self) -> None:
        purchases = self.repo.load_all()
        self._print_table(purchases, title="Все покупки")

    def show_by_date(self) -> None:
        d = parse_date(input("Введите дату (YYYY-MM-DD): ").strip())
        purchases = [p for p in self.repo.load_all() if p.date == d]
        self._print_table(purchases, title=f"Покупки за дату {d.isoformat()}")

    def show_by_category(self) -> None:
        category = input("Введите категорию: ").strip()
        if not category:
            raise ValueError("Категория не может быть пустой.")
        purchases = [p for p in self.repo.load_all() if p.category.lower() == category.lower()]
        self._print_table(purchases, title=f"Покупки по категории '{category}'")

    def show_by_date_and_category(self) -> None:
        d = parse_date(input("Введите дату (YYYY-MM-DD): ").strip())
        category = input("Введите категорию: ").strip()
        if not category:
            raise ValueError("Категория не может быть пустой.")
        purchases = [
            p
            for p in self.repo.load_all()
            if p.date == d and p.category.lower() == category.lower()
        ]
        self._print_table(purchases, title=f"Покупки за {d.isoformat()} в категории '{category}'")

    def sort_by_amount(self) -> None:
        purchases = self.repo.load_all()
        if not purchases:
            self._print_table([], title="Сортировка по стоимости")
            return

        order = input("Сортировка: 1) по возрастанию  2) по убыванию: ").strip()
        if order == "1":
            purchases_sorted = sorted(purchases, key=lambda p: p.amount)
            self._print_table(purchases_sorted, title="Сортировка по возрастанию стоимости")
        elif order == "2":
            purchases_sorted = sorted(purchases, key=lambda p: p.amount, reverse=True)
            self._print_table(purchases_sorted, title="Сортировка по убыванию стоимости")
        else:
            print("Неизвестный вариант сортировки.")

    def delete_by_id(self) -> None:
        purchases = self.repo.load_all()
        self._print_table(purchases, title="Удаление записи (список покупок)")
        if not purchases:
            return

        raw = input("Введите ID (номер строки) для удаления: ").strip()
        try:
            idx = int(raw)
        except ValueError:
            raise ValueError("ID должен быть целым числом.")

        if not (1 <= idx <= len(purchases)):
            raise ValueError("ID вне диапазона.")

        removed = purchases.pop(idx - 1)
        self.repo.overwrite_all(purchases)
        print(
            "Удалено: {0} | {1} | {2} | {3}".format(
                removed.date.isoformat(),
                removed.category,
                removed.product,
                f"{removed.amount:.2f}",
            )
        )

    def clear_all(self) -> None:
        confirm = input("Точно очистить ВСЕ записи? (yes/no): ").strip().lower()
        if confirm == "yes":
            self.repo.clear()
            print("Все записи очищены.")
        else:
            print("Отмена.")

    def _print_table(self, purchases: Sequence[Purchase], title: str) -> None:
        print("\n" + title)
        if not purchases:
            print("(нет данных)")
            return

        rows = []
        for i, p in enumerate(purchases, start=1):
            rows.append((str(i), p.date.isoformat(), p.category, p.product, f"{p.amount:.2f}"))

        headers = ("ID", "Дата", "Категория", "Продукт", "Стоимость")
        widths = [len(h) for h in headers]
        for r in rows:
            for j, val in enumerate(r):
                widths[j] = max(widths[j], len(val))

        fmt = "  ".join("{:<" + str(w) + "}" for w in widths)
        print(fmt.format(*headers))
        print(fmt.format(*("-" * w for w in widths)))
        for r in rows:
            print(fmt.format(*r))


def main() -> None:
    data_path = Path(__file__).parent / "data" / "purchases.csv"
    repo = CsvPurchaseRepository(data_path)
    MoneyTrackerApp(repo).run()


if __name__ == "__main__":
    main()
