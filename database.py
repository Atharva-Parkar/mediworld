import datetime


class DataBase:
    def __init__(self, filename):
        self.filename1 = filename
        self.users1 = None
        self.file1 = None
        self.load()

    def load(self):
        self.file1 = open(self.filename1, "r")
        self.users1 = {}

        for line in self.file1:
            name, age, gender, city, area, emai, passwor, created = line.strip().split(";")
            self.users1[name] = (age, gender, city, area, emai, passwor, created)

        self.file1.close()

    def get_user1(self, name):
        if name in self.users1:
            return self.users1[name]
        else:
            return -1

    def add_user1(self, name, age, gender, city, area, emai, passwor):
        if name.strip() not in self.users1:
            self.users1[name.strip()] = (age.strip(), gender.strip(), city.strip(), area.strip(), emai.strip(), passwor.strip(), DataBase.get_date())
            self.save()
            return 1
        else:
            print("name exists already")
            return -1


    def save(self):
        with open(self.filename1, "w") as f:
            for user in self.users1:
                f.write(user  + ";" + self.users1[user][0] + ";" + self.users1[user][1] + ";" + self.users1[user][2] + self.users1[user][3] + ";" + self.users1[user][4] + ";" + self.users1[user][5] + ";" + self.users1[user][6] + ";" + self.users1[user][7] + ";"  "\n")

    @staticmethod
    def get_date():
        return str(datetime.datetime.now()).split(" ")[0]


