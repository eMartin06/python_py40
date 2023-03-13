def nagy(self):
    if len(self) == 0:
        return self
    elif self[0].islower():
        return self.capitalize()
    else:
        return self.lower()

lista = ['alma', 'Korte', 'barack', 'Dinnye', 'eper','Pap']

for i in lista:
    print(i)
    print(nagy(i))
