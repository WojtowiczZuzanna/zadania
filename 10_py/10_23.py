class C():
    def __init__(self, name, surname, age, seniority):
        self.name = name
        self.surname = surname
        self.age = age
        self.seniority = seniority

    def create(self):
        nick = ""
        if self.age < 18:
            nick += self.surname.lower()
            nick += self.name[0].lower()
        else:
            nick += self.surname.upper()
            nick += self.name[0]
        nick += str(self.seniority)
        print(nick)

nickname = C("Anna","May",17,7)
nickname2 = C("George","Brown",21,4) 

nickname.create()
nickname2.create()