class Persona:
    def __init__(self, nombre, edad):
        self.__nombre = nombre
        self.__edad = edad

    def nombre(self):
        return self.__nombre

    def edad(self):
        return self.__edad

    def compara_edad(self, persona):
        if self.edad() < persona.edad():
            print(f'{persona.nombre()} es más viejo que yo.')
        if self.edad() > persona.edad():
            print(f'{persona.nombre()} es más joven que yo.')
        if self.edad() == persona.edad():
            print(f'{persona.nombre()} tiene la misma edad que yo.')


p1 = Persona('Samuel', 24)
p2 = Persona('Jael', 36)
p3 = Persona('Liliana', 24)

p1.compara_edad(p2)
p2.compara_edad(p1)
p1.compara_edad(p3)
