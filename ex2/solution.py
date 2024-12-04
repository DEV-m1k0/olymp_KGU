from io import TextIOWrapper
import math, asyncio

async def get_coordinates(file: TextIOWrapper) -> list[int, int]:
    """
    Функция для получения координат
    """
    return list(map(int, file.readline().split()))

async def calculate_distance_between_circles(x1: int, y1: int, x2: int, y2: int) -> int:
    """
    Функция для высчитывания расстояния между кругами по координатам
    """
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

async def is_better(s1: int, s2) -> str:
    """
    Проверка на то, что площадь сделанного фонарика больше,
    чем площадь первого фонарика
    """
    return "YES" if s2 > s1 else "NO"

async def write_to_file(answer: str):
    """
    Запись результата в файл
    """
    with open('OUTPUT.TXT', 'w') as file:
        file.write(answer)

async def calculate_area(d: int, r: int) -> int:
    """
    Высчитываение площади для сделанного фонарика
    """
    # Если круги не пересекаются, то общая площадь равна сумме площадей обоих кругов
    if d >= 2*r:
        return 2*math.pi*(r**2)
    else:
        # Угол α/2, который соответствует половине угла пересечения
        alpha_half = math.acos((d / 2) / r)
        
        # Площадь пересечения двух кругов
        intersection_area = 2 * r**2 * (alpha_half - math.sin(alpha_half))
        
        # Площадь, освещённая двумя кругами
        return 2*math.pi*(r**2) - intersection_area

async def main():
    # Чтение данных из файла
    with open('INPUT1.TXT', 'r') as file:
        # Читаем координаты центров кругов
        x1, y1 = await get_coordinates(file)
        x2, y2 = await get_coordinates(file)
        
        # Читаем радиус и площадь круга первого фонарика
        r = int(file.readline())
        s_first_flashlight = float(file.readline())

    # Вычисляем расстояние между центрами кругов
    d = await calculate_distance_between_circles(x1, y1, x2, y2)

    # Высчитываем площадь второго фонарика
    s_second_flashlight = await calculate_area(d, r)

    # Проверка на то, что 2ой сделанный фонарик лучше первого
    answer = await is_better(s_first_flashlight, s_second_flashlight)

    # Записываем результат в файл
    await write_to_file(answer)


if __name__ == "__main__":
    asyncio.run(main())