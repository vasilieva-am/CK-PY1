class Runner:
    def __init__(self, runners_number: int, place: int, reward_for_win: int):
        """
        Создание и подготовка к работе объекта "Бегун"

        :param runners_number: Количество бегунов, участвующих в забеге
        :param place: Место, которое занял бегун по окончанию забега
        :param reward_for_win: Награда за победу

         Примеры:
        >>> runner_1 = Runner(8,3,1000)
        """
        if not isinstance(runners_number, int):
            raise TypeError("Количество участников должно быть целым числом")
        if runners_number <= 0:
            raise ValueError("Количество участников должно быть положительным числом")
        self.runners_number = runners_number
        if not isinstance(place, int):
            raise TypeError("Место должно быть целым числом")
        if place <= 0:
            raise ValueError("Место быть положительным числом")
        self.place = place
        if not isinstance(reward_for_win, int):
            raise TypeError("Награда за победу должна быть целым числом")
        if reward_for_win <= 0:
            raise ValueError("Награда за победу должна быть положительным числом")
        self.reward_for_win = reward_for_win

    def probability_of_getting_prizes(self) -> float:
        """
        Функция, которая определяет вероятность победы в забеге и получение главного приза
        :return: Вероятность победы
        
        Примеры:
        >>> runner_1 = Runner(8,3,1000)
        >>> runner_1.probability_of_getting_prizes()
        """
        ...

    def getting_reward(self) -> int:
        """
        Функция, которая определяет какой выигрыш получит бегун
        :return: Сумма выигрыша
       
       Примеры:
        >>> runner_1 = Runner(8,3,1000)
        >>> runner_1.getting_reward()
        """
        ...


class CourseWork:
    def __init__(self, work_amount: int, work_time: (int, float)):
        """
        Создание и подготовка к работе объекта "Курсовая работа"

        :param work_amount: Объем курсовой работы в страницах
        :param work_time: Время написания курсовой работы в часах

        Примеры:
        >>> work_1 = CourseWork(60,16)
        """
        if not isinstance(work_amount, int):
            raise TypeError("Количество страниц в работе должно быть целым числом")
        if work_amount <= 0:
            raise ValueError("Количество страниц в работе должно быть положительным числом")
        self.work_amount = work_amount
        if not isinstance(work_time, (int, float)):
            raise TypeError("Время написания работы должно быть целым числом или числом с плавающей запятой")
        if work_time <= 0:
            raise ValueError("Время написания работы должно быть положительным числом")
        self.work_time = work_time

    def writing_speeed(self) -> (int, float):
        """
        Функция, которая определяет скорость написания курсовой работы
        :return: Скорость напиания (страниц/час)

        Примеры:
        >>> work_1 = CourseWork(60,16)
        >>> work_1.writing_speeed()
        """
        ...

    def turn_work_on_time(self, planned_work_time: (int, float)) -> str:
        """
        Функция, которая определяет успеет ли студент сдать работу во время
        :param planned_work_time: Планируемый срок выполнения работы
        :return: Студент выполнил/не выполнил задание в срок

        Примеры:
        >>> work_1 = CourseWork(60,16)
        >>> work_1.turn_work_on_time(15)
        """
        ...


class Draw:
    def __init__(self, participants_number: int, groups_number: int):
        """
        Создание и подготовка к работе объекта "Жеребьевка"

        :param participants_number: Количество участников жеребьевки
        :param groups_number: Количество групп

        Примеры:
        >>> draw_1 = Draw(10, 2)
        """
        if not isinstance(participants_number, int):
            raise TypeError("Количество участников должно быть целым числом")
        if participants_number <= 0:
            raise ValueError("Количество участников должно быть положительным числом")
        self.participants_number = participants_number
        if not isinstance(groups_number, int):
            raise TypeError("Количество участников должно быть целым числом")
        if groups_number <= 0:
            raise ValueError("Количество участников должно быть положительным числом")
        if participants_number % groups_number > 0:
            raise ValueError("Количество участников должно быть пропорционально числу групп")
        self.groups_number = groups_number

    def number_participants_in_group(self) -> int:
        """
        Функция, которая определяет количество участников в каждой группе
        :return: Количество участников в каждой группе

        Примеры:
        >>> draw_1 = Draw(20,10)
        >>> draw_1.number_participants_in_group()
        """
        ...

    def probability_of_even_group(self) -> float:
        """
        Функция, которая определяет ероятность попадания в четную группу
        :return: Вероятность попадания в четную группу

        Примеры:
        >>> draw_1 = Draw(20,10)
        >>> draw_1.probability_of_even_group()
        """
        ...


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    pass


