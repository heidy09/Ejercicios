class Personaje:
    #nombre = "Default"
    #fuerza = 0
    #inteligencia = 0
    #denfensa = 0
    #vida = 0
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida):
        self.nombre = nombre
        self.fuerza = fuerza
        self.inteligencia = inteligencia
        self.defensa = defensa
        self.vida = vida

    def atributos(self):
        print(self.nombre, ":", sep="")
        print("*Fuerza:", self.fuerza)
        print("*Inteligencia:", self.inteligencia)
        print("*Defensa:", self.defensa)
        print("*Vida:", self.vida)

    def subir_nivel(self, fuerza, inteligencia, defensa):
        self.fuerza = self.fuerza + fuerza
        self.inteligencia = self.inteligencia + inteligencia
        self.defensa = self.defensa + defensa

    def esta_vivo(self):
        return self.vida > 0
        
    def morir(self):
        self.vida = 0
        print(self.nombre, "ha muerto")
    
    def daño(self, enemigo):
        return self.fuerza - enemigo.defensa
        
    def atacar(self, enemigo):
        daño = self.daño(enemigo)
        enemigo.vida = enemigo.vida - daño
        print(self.nombre, "ha realizado", daño, "puntos de daño a", enemigo.nombre)
        if enemigo.esta_vivo():
            print("la vida de", enemigo.nombre, "es", enemigo.vida)
        else:
            enemigo.morir()

class Guerrero(Personaje):
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida, espada):
        #Personaje.__init__(self, nombre, fuerza, inteligencia, defensa, vida)
        super().__init__(nombre, fuerza, inteligencia, defensa, vida)
        self.espada = espada

    def cambiar_arma(self):
        opcion = int(input("elige un arma: (1) Acero Valyrio, daño 8. (2) Matadragones, daño 10 "))
        if opcion == 1:
            self.espada = 8 
        elif opcion == 2:
            self.espada = 10
        else:
            print("Numero de arma incorrecto")

    def atributos(self):
        super().atributos()
        print("*Espada:", self.espada)

    def daño(self, enemigo):
        return self.fuerza*self.espada - enemigo.defensa
    
class Mago(Personaje):

    def __init__(self, nombre, fuerza, inteligencia, defensa, vida, libro):
        super().__init__(nombre, fuerza, inteligencia, defensa, vida)
        self.libro = libro

    def atributos(self):
        super().atributos()
        print("*Libro", self.libro)

    def daño(self, enemigo):
        return self.inteligencia*self.libro - enemigo.defensa
    
Personaje_1 = Guerrero("Guts", 20, 10, 4, 100, 4)#cambiamos guerrero por personaje quitamos el argumento 4 y ejecutamos 
Personaje_2 = Mago("Vanessa", 5, 15, 4, 100, 3)

def combate(jugador_1, jugador_2):
    turno = 0
    while jugador_1.esta_vivo() and jugador_2.esta_vivo():
        print("\nTurno", turno)
        jugador_1.atacar(jugador_2)
        print(">>> Acción de", jugador_1.nombre, ":", sep="")
        print(">>> Acción de", jugador_2.nombre, ":", sep="")
        jugador_2.atacar(jugador_1)
        turno = turno + 1
    if jugador_1.esta_vivo():
        print("\nHa ganado", jugador_1.nombre)
    elif jugador_2.esta_vivo():
        print("\nHa ganado", jugador_2.nombre)
    else:
        print("\nEmpate")

combate(Personaje_1, Personaje_2)
#goku = Personaje("Goku", 20, 15, 10, 100)
#guts = Guerrero("Gust", 20, 10, 10, 100, 5)
#vanessa = Mago("vanessa", 20, 15, 10, 100, 5)
#guts.cambiar_arma()
#goku.atacar(guts)
#guts.atacar(vanessa)
#vanessa.atacar(goku)
#goku.atributos()
#guts.atributos()
#vanessa.atributos()
#print(guts.espada)
    #def get_fuerza(self):
    #   return self.fuerza

    #def set_fuerza(self, fuerza):
    #if fuerza < 0:
    #       print("Error, has introducido valor negativo")
    #   else:
    #      self.fuerza = fuerza
    
#mi_personaje = Personaje("BisBoss", 10, 1, 5, 100)
#mi_enemigo = Personaje("Enemy Stando", 8, 5, 3, 100)
#mi_personaje.nombre = "BitBoss"
#mi_personaje.fuerza = 10
#print("El nombre del jugador es", mi_personaje.nombre)
#print("la fuerza del jugador es", mi_personaje.fuerza)
#print(mi_personaje.esta_vivo())
#mi_personaje.morir()
#mi_personaje.subir_nivel(1, 2, 0)
#mi_personaje.atacar(mi_enemigo)
#mi_personaje.atacar(mi_enemigo)
#mi_personaje.set_fuerza(5)
#mi_personaje.get_fuerza()
#mi_enemigo.atributos()
#mi_personaje.atacar(mi_enemigo)

