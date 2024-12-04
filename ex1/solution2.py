import asyncio

async def main():
    """
    Функция для запуска программы
    """
    with open("INPUT.TXT") as file_in, open("OUTPUT.TXT", mode="w") as file_out:
        # Итерируемся по строке и преобразуем строчные элементы списка в численные
        row = list(map(int, file_in.readlines()[1].strip().split()))
        # Находим минимальное число
        min_num = min(row)
        # Находим максимальное число
        max_num = max(row)
        # Сохраняем минимальное и максимальное число в файле OUTPUT.TXT
        file_out.write(f"{min_num} {max_num}")

if __name__ == "__main__":
    asyncio.run(main())