import time #For random seed

class LinearCongruential:
    _a=1664525
    _c=1013904223
    _modulus=2**32
    _x_0=time.time()

    def __init__(self,a=0.0,b=1.0):
        self.a=a
        self.b=b

    def random(self,N=1):
        if (N==1):
            self._x_0=(self._a*self._x_0+self._c)%self._modulus
            return (self.b-self.a)*(self._x_0/(self._modulus-1.0))+self.a
        elif (N>1):
            rans=[]
            for i in range(0,N):
                self._x_0=(self._a*self._x_0+self._c)%self._modulus
                rans.append((self.b-self.a)*(self._x_0/(self._modulus-1.0))
                +self.a)
            return rans
        else:
            raise Exception("N must be an integer greater than zero")