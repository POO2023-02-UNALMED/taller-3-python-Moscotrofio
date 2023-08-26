class Marca:
    nombre = None
    def __init__(self, nombre):
        self.nombre = nombre
    
    def getNombre():
        return Marca.nombre
    
    def setNombre(nombre):
        Marca.nombre = nombre
    
class TV:
    _numTV = 0
    def __init__(self, marca, estado):
        self._marca = marca
        self._estado = estado
        self._canal = 1
        self._volumen = 1
        self._precio = 500
        self._control = None
        TV._numTV += 1

    def setMarca(self, marca):
        self._marca = marca
    
    def getMarca(self):
        return self._marca
    
    def setCanal(self, canal):
        self._canal = canal

    def getCanal(self):
        return self._canal

    def setPrecio(self, precio):
        self._precio = precio

    def getPrecio(self):
        return self._precio

    def setVolumen(self, volumen):
        self._volumen = volumen

    def getVolumen(self):
        return self._volumen
    
    def setControl(self, control):
        self._control = control

    def getControl(self):
        return self._control
    
    def setNumTV(numTV):
        TV._numTV = numTV
    
    def getNumTV():
        return TV._numTV
    
    def turnOn(self):
        self._estado = True

    def turnOff(self):
        self._estado = False

    def getEstado(self):
        return self._estado
    
    def canalUp(self):
        if self._estado:
            if self._canal < 120:
                self._canal +=1

    def canalDown(self):
        if self._estado:
            if self._canal > 1:
                self.canal -= 1 

    def volumenUp(self):
        if self._estado:
            if self._volumen < 7:
                self._volumen += 1

    def voluemnDown(self):
        if self._estado:
            if self._volumen > 0:
                self._volumen -= 1

class Control:
    _tv = None
    def enlazar(self, tv):
        self._tv = tv
        tv._control = self

    def getTv():
        return Control._tv
    
    def setTv(tv):
        Control._tv = tv

    def turnOn(self):
        self._tv.turnOn()

    def turnOff(self):
        self._tv.turnOff()

    def canalUp(self):
        self._tv.canalUp()

    def canalDown(self):
        self._tv.canalDown()

    def volumenUp(self):
        self._tv.volumenUp()

    def volumenDown(self):
        self._tv.volumenDown()









