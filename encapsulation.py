class People:
    def __init__(self, name, age, cpf):
        self.name = name
        self.age = age
        self.__cpf = cpf

    def print_cpf(self):
        print(self.__cpf)

    def drink(self):
        if self.age >= 18:
            self._present_document()
            print('drink ...')
        else:
            print('No drink...')

    def _present_document(self):
        print(self.__cpf)

joe = People('Joe', 18, '34689409390')
joe.drink()
