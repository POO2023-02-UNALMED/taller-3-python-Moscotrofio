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