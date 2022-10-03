class Nodo:
    __item = None
    __izq = None
    __der = None
    __car = None

    def __init__(self, item, car):
        self.__item = item
        self.__car = car
        self.__izq = None
        self.__der = None
        
    def setItem(self, x):
        self.__item = x
    
    def setIzq(self,izq):
        self.__izq = izq
    
    def setDer(self, der):
        self.__der = der
    
    def setCar(self, car):
        self.__car = car
    
    def getItem(self):
        return self.__item
    
    def getIzq(self):
        return self.__izq
    
    def getDer(self):
        return self.__der

    def getCar(self):
        return self.__car

class Arbol:
    __raiz = None

    def __init__(self):
        self.__raiz = None
    
    def getRaiz(self):
        return self.__raiz
    
    def vacio(self):
        return self.__raiz == None

    def Insertar(self, subarbol, x, caracter):
        if self.__raiz == None:
            unNodo = Nodo(x, caracter)
            if self.vacio():
                self.__raiz = unNodo
        else:
            if x == subarbol.getItem():
                print("\nNo se puede ya existe el item")
            elif x < subarbol.getItem():
                if subarbol.getIzq() == None:
                    unNodo = Nodo(x, caracter)
                    subarbol.setIzq(unNodo)
                else:
                    self.Insertar(subarbol.getIzq(), x, caracter)
            elif x > subarbol.getItem():
                if subarbol.getDer() == None:
                    unNodo = Nodo(x, caracter)
                    subarbol.setDer(unNodo)
                else:
                    self.Insertar(subarbol.getDer(), x, caracter)

    def grado(self, subarbol):
        grado = 0
        if (subarbol.getDer() != None and subarbol.getIzq() == None) or (subarbol.getDer() == None and subarbol.getIzq() != None):
            grado = 1
        elif subarbol.getDer() != None and subarbol.getIzq() != None:
            grado = 2
        return grado

    def padre(self, subarbol, x):
        if (self.__raiz != None) and (self.__raiz.getItem() != x):
            if (subarbol.getIzq() != None) and (subarbol.getIzq().getItem() == x):
                return subarbol
            elif (subarbol.getDer() != None) and (subarbol.getDer().getItem() == x):
                return subarbol
            elif subarbol.getItem() > x:
                return self.padre(subarbol.getIzq(),x)
            elif subarbol.getItem() < x:
                return self.padre(subarbol.getDer(),x)
        else:
            return None
            

    def suprimir(self, subarbol, x):
        if self.vacio():
            print("\nEl arbol se encuentra vacio")
        else:
            if subarbol.getItem() == x:
                
                #Busca el grado
                grado = self.grado(subarbol)
                
                #Si es de grado 0
                if grado == 0:
                    if self.__raiz == x:
                        self.__raiz = None
                    else:
                        padre = self.padre(self.getRaiz(),x)
                        if padre.getDer() != None:
                            padre.setDer(None)
                        else:
                            padre.setIzq(None)
                
                #Si es de grado 1
                elif grado == 1:
                    padre = self.padre(subarbol,x)
                    if subarbol.getIzq() != None:
                        padre.setIzq(subarbol.getIzq())
                    else:
                        padre.setDer(subarbol.getDer())
                
                #Si es de grado 2
                elif grado == 2:
                    NuevoNodo = self.maximo(subarbol.getDer())
                    NuevoNodoPadre = self.padre(self.getRaiz(), NuevoNodo.getItem())
                    NuevoNodoGrado = self.grado(NuevoNodo)
                    subarbol.setItem(NuevoNodo.getItem())
                    if NuevoNodoGrado == 0:
                        if NuevoNodoPadre.getDer().getItem() == NuevoNodo.getItem():
                            NuevoNodoPadre.setDer(None)
                        else:
                            NuevoNodoPadre.setIzq(None)
                    else:
                        if NuevoNodoPadre.getDer().getItem() == NuevoNodo.getItem():
                            NuevoNodoPadre.setDer(NuevoNodo.getDer())
                        else:
                            NuevoNodoPadre.setIzq(NuevoNodo.getDer())

            #Pasa al siguien por derecha o por izquierda
            elif subarbol.getItem() > x:
                self.suprimir(subarbol.getIzq(),x)
            elif subarbol.getItem() < x:
                self.suprimir(subarbol.getDer(),x)

    def maximo(self,subarbol):
        while subarbol.getIzq() != None:
            subarbol = subarbol.getIzq()
        return subarbol

    def minimo(self,subarbol):
        while subarbol.getDer() != None:
            subarbol = subarbol.getDer()
        return subarbol

    def Inorder(self,subarbol):
        if subarbol != None:
            self.Inorder(subarbol.getIzq())
            print(subarbol.getItem())
            self.Inorder(subarbol.getDer())

    def Preorder(self,subarbol):
        if not self.vacio():
            print(subarbol.getItem())
            self.Preorder(subarbol.getIzq())
            self.Preorder(subarbol.getDer())

    def Postorder(self,subarbol):
        if not self.vacio():
            self.Postorder(subarbol.getIzq())
            self.Postorder(subarbol.getDer())
            print(subarbol.getItem())

    def buscar(self, subarbol, x):
        if subarbol.getItem() == x:
            return subarbol
        else:
            if x < subarbol.getItem():
                return self.buscar(subarbol.getIzq(),x)
            elif x > subarbol.getItem():
                return self.buscar(subarbol.getDer(),x)

    def Nivel(self, x):
        aux = self.__raiz
        Nivel = 0
        bol = True
        while aux != None and bol:
            if x < aux.getItem():
                aux = aux.getIzq()
            elif x > aux.getItem():
                aux = aux.getDer()
            if aux.getItem() == x:
                bol = False
            Nivel += 1
        return Nivel
    
    def Hoja(self, x):
        aux = self.__raiz
        Nivel = 0
        bol = False
        while aux != None and not bol:
            if aux.getItem() == x:
                bol = True
            elif x < aux.getItem():
                aux = aux.getIzq()
            elif x > aux.getItem():
                aux = aux.getDer()
        if self.grado(aux) == 0:
            print('\nEs Hoja')
        else:
            print('\nNo es Hoja')
    
    def Hijo(self, subarbolHijo, subarbolPadre):
        bol = False
        if subarbolPadre.getDer() == subarbolHijo or subarbolPadre.getIzq() == subarbolHijo:
            bol = True
        if bol:
            print('\nSi es hijo')
        else:
            print('\nNo es hijo')
    
    def aprobarCamino(self, subarbolInicio, subarbolFin):
        bol = False
        if subarbolInicio != None:
            if subarbolFin != None:
                subarbolFin = self.buscar(subarbolInicio, subarbolFin)
                if subarbolFin != None:
                    bol = True
        return bol

    def Camino(self, subarbolInicio, subarbolFin):
        NodoInicio = self.buscar(self.__raiz, subarbolInicio)
        NodoFin = self.buscar(self.__raiz, subarbolFin)
        if aprobarCamino:
            while NodoInicio != None:
                if NodoInicio == NodoFin:
                    NodoInicio = None
                else:
                    print(NodoInicio.getItem())
                    if NodoFin.getItem() < NodoInicio.getItem():
                        NodoInicio = NodoInicio,getIzq()
                    else:
                        NodoInicio = NodoInicio,getDer()
        else:
            print('\nNo son camino')

    def Altura(self, subarbol, max = 1):
        if subarbol != None:
            nivel = self.Nivel(subarbol.getItem())
            if max < nivel:
                max = nivel
            max = self.Altura(subarbol.getIzq(), max)
            max = self.Altura(subarbol.getDer(), max)
        return max