class Comparer:
    @staticmethod
    def check_types(numbers_a: list, numbers_b: list):
        if not isinstance(numbers_a, list) or not isinstance(numbers_b, list):
            return False
        for i in numbers_a:
            if not isinstance(i, (int, float)):
                return False
        for i in numbers_b:
            if not isinstance(i, (int, float)):
                return False
        return True

    def find_avg(self, numbers_a: list, numbers_b: list) -> list:
        if self.check_types(numbers_a, numbers_b):
            avg_list = [0] if not numbers_a else [sum(numbers_a) / len(numbers_a)]
            avg_list.append(0) if not numbers_b else avg_list.append(sum(numbers_b) / len(numbers_b))
            return avg_list
        else:
            raise TypeError('Некорректный ввод данных!')

    def compare(self, numbers_a: list, numbers_b: list) -> int:
        if self.check_types(numbers_a, numbers_b):
            avg_list = self.find_avg(numbers_a, numbers_b)
            if avg_list.count(max(avg_list)) == 1:
                return avg_list.index(max(avg_list))
            else:
                return -1
        else:
            raise TypeError('Некорректный ввод данных!')

    def print_compare_result(self, numbers_a: list, numbers_b: list):
        result = self.compare(numbers_a, numbers_b)
        if result == -1:
            print('Средние значения равны')
        else:
            print(['Первый список имеет большее среднее значение',
                   'Второй список имеет большее среднее значение'][result])
