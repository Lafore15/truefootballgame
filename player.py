class Player:
    def __init__(self, surname, number, position, default_score):
        self.surname = surname
        self.number = number
        self.position = position
        self.default_score = default_score

    def __repr__(self):
        return f'{self.surname} - {self.number}'

    def __str__(self):
        return f'{self.surname} - {self.number}'

    def set_score(self):
        score = int(input('Введите рейтинг: '))
        self.default_score = score

    def get_score(self):
        return self.default_score

    def get_info(self):
        return self.surname, f'Number is {self.number}', f"Rating is {self.default_score}"
