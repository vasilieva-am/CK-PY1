class Potion:

    def __init__(self, name: str, toxicity: int, fight_application: bool):
        """
        Базовый класс "Зелье"

        :param name: Название зелья
        :param toxicity: Токсичность зелья
        :param fight_application: Возможность применения в бою
        """
        if not isinstance(name, str):
            raise TypeError('Название зелья должно быть типа "str"')
        self._name = name
        if not isinstance(toxicity, int):
            raise TypeError('Токсичность должна быть типа "int"')
        self._toxicity = toxicity
        if not isinstance(fight_application, bool):
            raise TypeError('Возможность применения зелья в бою должна быть типа "bool"')
        self._fight_application = fight_application

    @property
    def name(self) -> str:
        """ Возвращает название зелья. Название зелий не меняется, параметр инкапсулируется"""
        return self._name

    @property
    def toxicity(self) -> int:
        """ Возвращает показатель токсичности зелья, которая не меняется, параметр инкапсулируется"""
        return self._toxicity

    @property
    def fight_application(self) -> bool:
        """ Возвращает возможность применения в бою зелья, которая не меняется, параметр инкапсулируется"""
        return self._fight_application

    def __str__(self):
        return f'Название зелья "{self.name}". Токсичность: {self.toxicity}. Применение в бою: {self.fight_application}'

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self._name!r}, toxicity={self._toxicity!r}, " \
               f"fight_application={self._fight_application!r})"

    def increase_toxicity(self, toxic_level) -> str:
        """Вычислить уровень интоксикации персонажа после принятия зелья

        :param toxic_level: Текущий уровень интоксикации ведьмака
        :raise TypeError: Вызывается ошибка, если тип данных отличен от заданного
        :raise ValueError: Вызывается ошибка, если уровень интоксикации отрицателен
        :return: Уровень интоксикации
        """
        if not isinstance(toxic_level, int):
            raise TypeError('Показатель уровня интоксикации должен быть типа "int"')
        if toxic_level < 0:
            raise ValueError('Значение уровня интоксикации ведьмака не должно быть отрицательным')

        return f"Уровень интоксикации ведьмака: {toxic_level + self._toxicity}"

    def use_in_fight(self) -> str:
        """Описывает возможность применения зелья во время боя

        :return: Возможно/невозможно использование в бою
        """

        if self._fight_application is True:
            return f'Зелье "{self._name}" возможно использовать во время боя'
        else:
            return f'Зелье "{self._name}" невозможно использовать во время боя'


lastochka = Potion("Ласточка", 50, True)
print(lastochka.increase_toxicity(50))
print(lastochka.use_in_fight())


class HealthImprovement(Potion):
    def __init__(self, name: str, toxicity: int, fight_application: bool,  recovery: int):
        """
        Дочерний класс "Зелье для восстановления здоровья"

        :param name: Название эликсира
        :param toxicity: Токсичность зелья
        :param fight_application: Возможность применения в бою
        :param recovery: Очки восстановления здоровья ведьмака
        """
        super().__init__(name, toxicity, fight_application)
        if not isinstance(recovery, int):
            raise TypeError('Показатель очков здоровья от применения зелья должен быть типа "int"')
        if recovery < 0:
            raise ValueError('Значение показателя очков здоровья от применения зелья не должно быть отрицательным')
        self._recovery = recovery

    @property
    def recovery(self) -> int:
        """ Возвращает показатель очков здоровья после применения зелья.
            Очки здоровья не меняются, параметр инкапсулируется"""
        return self._recovery

    def __repr__(self):  # перегружаем метод, добавляя показатель очков здоровья.
        return f"{self.__class__.__name__}(name={self.name!r}, toxicity={self.toxicity!r}, " \
               f"fight_application={self.fight_application!r}, recovery={self.recovery!r})"

    def increase_toxicity(self, toxic_level) -> str:
        """Вычислить уровень интоксикации персонажа после принятия зелья
        Перегружаем метод, так как для "Зелья для восстановления здоровья" имеют особенность снижения интоксикации на
        четверть от значения показателя очков здоровья.

        :param toxic_level: Текущий уровень интоксикации ведьмака
        :raise TypeError: Вызывается ошибка, если тип данных отличен от заданного
        :raise ValueError: Вызывается ошибка, если уровень интоксикации отрицателен
        :return: Уровень интоксикации
        """

        return f"Уровень интоксикации ведьмака: {toxic_level + self._toxicity - self._recovery//4}"


Ivolga = HealthImprovement("Ласточка", 500, True, 250)
print(Ivolga.increase_toxicity(50))
print(Ivolga.use_in_fight())

if __name__ == "__main__":
    pass

