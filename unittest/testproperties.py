class Clase:
    __myprivate="DOS"
    def __init__(self, mi_atributo):
        self.__mi_atributo = mi_atributo
        print(self.__myprivate)
        print(self.__getprivate())

    @property
    def mi_atributo(self):
        return self.__mi_atributo

    def __getprivate(self):
        return "Hola mi perro"

    @staticmethod
    def hablar(s):
        return "hola --"+str(s)

print(Clase.hablar("will1"))
mi_clase = Clase("valo por defecto")
print(mi_clase.mi_atributo)
print(mi_clase._Clase__getprivate()) # colocanco la palabra._Clase seguido del metodo se accede
print(mi_clase.hablar("will2"))
#print(mi_clase.__myprivate)