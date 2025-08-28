# homeworks/distance.py

class Distance:
    # словарь для конвертации всего в метры
    _unit_to_meters = {
        "cm": 0.01,
        "m": 1,
        "km": 1000
    }

    def __init__(self, value: float, unit: str):
        if unit not in self._unit_to_meters:
            raise ValueError(f"Неподдерживаемая единица измерения: {unit}")
        self.value = value
        self.unit = unit

    def __str__(self):
        return f"{self.value} {self.unit}"

    def to_meters(self):
        """Переводим значение в метры"""
        return self.value * self._unit_to_meters[self.unit]

    @staticmethod
    def from_meters(meters: float, unit: str):
        """Создать Distance из метров в нужной единице"""
        return Distance(meters / Distance._unit_to_meters[unit], unit)

    def __add__(self, other):
        if not isinstance(other, Distance):
            return NotImplemented
        total_meters = self.to_meters() + other.to_meters()
        # результат в единицах левого операнда
        return Distance.from_meters(total_meters, self.unit)

    def __sub__(self, other):
        if not isinstance(other, Distance):
            return NotImplemented
        diff_meters = self.to_meters() - other.to_meters()
        if diff_meters < 0:
            raise ValueError("Результат не может быть отрицательным!")
        return Distance.from_meters(diff_meters, self.unit)

    # Доп методы для сравнения
    def __eq__(self, other):
        return self.to_meters() == other.to_meters()

    def __lt__(self, other):
        return self.to_meters() < other.to_meters()

    def __le__(self, other):
        return self.to_meters() <= other.to_meters()

    def __gt__(self, other):
        return self.to_meters() > other.to_meters()

    def __ge__(self, other):
        return self.to_meters() >= other.to_meters()
