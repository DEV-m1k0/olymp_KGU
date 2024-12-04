import asyncio

async def main(file):
    """
    Функция для запуска программы
    """
    try:
        open(file).close()
    except:
        raise FileNotFoundError("Ошибка при чтении файла. Скорее всего, данного файла не существует или в названии файла допущена ошибка.")
    try:
        with open(file) as file_in, open("OUTPUT.TXT", mode="w") as file_out:
            # Итерируемся по строке и преобразуем строчные элементы списка в численные
            row = list(map(int, file_in.readlines()[1].strip().split()))
            
            # Находим минимальное и максимальное число
            min_num = min(row)
            max_num = max(row)
            
            # Сохраняем минимальное и максимальное число в файле OUTPUT.TXT
            file_out.write(f"{min_num} {max_num}")
    except:
        raise ValueError("Ошибка при чтении файла. Скорее всего, файл, который вы пытаетесь причесть, не соотвествует требованиям задачи.")

if __name__ == "__main__":
    file_name = "INPUT.TXT"
    asyncio.run(main(file_name))