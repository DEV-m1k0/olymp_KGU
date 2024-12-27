import heapq, os, asyncio


class ProgramSolution:
    def __init__(self, file_name: str):
        self.file_name = file_name
        self.path = os.path.dirname(__file__)


    def distribute_candies(self, n, m, gifts) -> int:
        """
        Метод, который возвращает наименьшее кол-во конфет в подарках
        """
        heapq.heapify(gifts)
        
        for _ in range(m):
            min_candies = heapq.heappop(gifts)
            min_candies += 1
            heapq.heappush(gifts, min_candies)
        
        # Возвращаем минимальное количество конфет в подарках после распределения
        return min(gifts)


    def read(self) -> tuple[int, int, list[int]]:
        """
        Метод для чтения файлов
        """
        with open(f"{self.path}/{self.file_name}") as file:
            n, m = map(int, file.readline().strip().split())
            gifts = [int(file.readline().strip()) for _ in range(n)]

        return n, m, gifts
    

    def write(self, result: int) -> None:
        """
        Метод для записи ответа в файл
        """
        with open(f'{self.path}/OUTPUT.TXT', 'w') as file:
            file.write(str(result))
    

    async def main(self, file_name: str) -> None:
        """
        Запуск программы
        """
        n, m, gifts = self.read()
        result = self.distribute_candies(n, m, gifts)
        self.write(result=result)



if __name__ == "__main__":
    file_name = "INPUT.TXT"
    solution = ProgramSolution(file_name=file_name)
    asyncio.run(solution.main(file_name=file_name))