
def find():
    a = 4  # количество баллов за совпадение интересов
    b = 1  # количество баллов за совпадение компаний
    c = 0.4  # количество баллов за разницу в возрасте
    d = 5  # максимальное количество балов за разницу в возрасте
    e = 3  # количество пользователей которое будет найденно

    persons = []


    class Person:
        def __init__(self, first_name, last_name, age, company, interest):
            self.first_name = first_name
            self.last_name = last_name
            self.age = int(age)
            self.company = company
            self.interest = interest.lower().split()

        def __str__(self):
            return " ".join([self.first_name, self.last_name, str(self.age), self.company]) + " " + " ".join(self.interest)

        def search_for_person(self):
            ret = []
            for i in range(len(persons)):
                pers = persons[i]
                if pers != self:

                    count = 0
                    for j in (self.interest):
                        if j in pers.interest:
                            count += a
                    if self.company == pers.company:
                        count += b
                    if abs(self.age - pers.age) < d:
                        count += (d - abs(self.age - pers.age)) * c

                    if len(ret) == 0:
                        ret.append([count, persons[i]])
                    elif ret[-1][0] < count or len(ret) < e:
                        ret.append([count, persons[i]])
                        ret.sort(key=lambda x: x[0], reverse=True)
                        del ret[e:]
            return ret


    person1 = Person("Алексей", "Алексеев", 18, "Моджанг", "Котики майнкрафт фнаф")
    persons.append(person1)
    person2 = Person("Борис", "Быков", 50, "Яндекс", "Шахматы")
    persons.append(person2)
    person3 = Person("Виктор", "Вран", 20, "Haemimont Games", "Вороны видеоигры")
    persons.append(person3)
    person4 = Person("Гриша", "Гоголев", 19, "Моджанк", "Майнкрафт литература")
    persons.append(person4)
    person5 = Person("Денис", "Демонов", 19, "Майкрософт", "Майнкрафт акультизм виндовс")
    persons.append(person5)
    person6 = Person("Епифаний", "Емельянов", 54, "Яндекс", "Шахматы шашки кросворды")
    persons.append(person6)
    person7 = Person("Ёжик", "Соник", 12, "Сега", "Спорт кросворды шахматы шашки")
    persons.append(person7)

    for pers in persons:
        print()
        print(list(map(lambda x: list(map(str, x)), pers.search_for_person())))
