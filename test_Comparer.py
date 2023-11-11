from Comparer import Comparer
from unittest import TestCase
from unittest import mock
import pytest
import io


class TestComparer(TestCase):
    comparer = Comparer()

    def test_compare_equal(self):
        assert self.comparer.compare([100, 200], [99, 201]) == -1

    def test_compare_max_a(self):
        assert self.comparer.compare([1.9, 10, -1], [1, -1, -0.5]) == 0

    def test_compare_empty(self):
        assert self.comparer.compare([], [1]) == 1

    def test_find_avg_empty(self):
        assert self.comparer.find_avg([], [5, 15, 10]) == [0, 10]

    def test_find_avg_type_error(self):
        with pytest.raises(TypeError):
            self.comparer.find_avg({1, 2, 3}, [5, 15])

    def test_compare_type_error_a(self):
        with pytest.raises(TypeError):
            self.comparer.compare([1, 2, (3, 4)], [1, 2, 3, 4.5])

    def test_compare_type_error_b(self):
        with pytest.raises(TypeError):
            self.comparer.compare([1, 2, 3, 10.999], [1, 2, 'a'])

    def test_print_result_b(self):
        with mock.patch('sys.stdout', new=io.StringIO()) as stdout:
            self.comparer.print_compare_result([0, -100, 0.777], [1, 2, 100, 1000])
        assert stdout.getvalue() == 'Второй список имеет большее среднее значение\n'

    def test_print_result_eqquals(self):
        with mock.patch('sys.stdout', new=io.StringIO()) as stdout:
            self.comparer.print_compare_result([0], [])
        assert stdout.getvalue() == 'Средние значения равны\n'
