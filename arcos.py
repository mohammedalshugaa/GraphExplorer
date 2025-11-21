import color_palettes as clrs
from nodos import Nodo as no

class ArcoNoDirigido:
    
    # atributos de clase
    numero_de_arcos = 0  # sin utilidad
    lista_de_arcos =[] ### lista compartida? # sin utilidad
    
    def __init__(self, nodos, id, nombre, origen, destino, peso=0, grosor=3, color=clrs.NEGRO, curvatura=0):
        
        # Validar valores críticos
        self._validar_valores_iniciales(nodos, id, nombre, origen, destino, peso, grosor, color, curvatura)
        
        # atributos básicos:
        self._id = id
        self.nombre:str = nombre ###
        self.nodos:list = nodos ###
        self.origen:no = origen ###
        self.destino:no = destino ###
        self.peso:float = peso
        self.grosor:int = grosor
        self.color:tuple = color
        self.curvatura:float = curvatura
        
        # atributos relacionados con ... :
        # no necesarios actualmente

            
        # atributos para algoritmos y visualización:
        # vacio por problemas estructurales de temporalidad y estado compartido entre algoritmos
        
        ArcoNoDirigido.numero_de_arcos+=1
        ArcoNoDirigido.lista_de_arcos.append(self)
        

    def _validar_valores_iniciales(self, nodos, id, nombre, origen, destino, peso, grosor, color, curvatura):
        if not isinstance(id, int):
            raise ValueError(f"Indice no es un valor válido: {id}")
        if not isinstance(nombre, str):
            raise ValueError(f"Nombre no es un valor válido: {nombre}")
        if (origen not in nodos) or (not isinstance(origen, no)) :
            raise ValueError(f"El nodo origen no existe")
        if (destino not in nodos) or (not isinstance(destino, no)):
            raise ValueError(f"El nodo destino no existe")
        if not isinstance(peso, (float,int)):
            raise ValueError(f"Peso debe ser un numero real: {peso}")
        if not isinstance(grosor, int) or not (1 <= grosor <= 10):
            raise ValueError(f"Grosor debe ser un entero entre 1 y 10: {grosor}")
        if not isinstance(color, tuple) or len(color) != 3: ###?
            raise ValueError("Color debe ser tupla (R, G, B)") ###?
        if not isinstance(curvatura, (float, int)) or not (0 <= curvatura <= 10): ### limite?
            raise ValueError(f"Curvatura debe ser un numero real entre 0 y 10: {curvatura}") ### limite?

     
    # Properties para validación continua
    @property
    def id(self):
        return self._id
    @id.setter
    def id(self, valor):
        if not isinstance(valor, int):
            raise ValueError(f"Indice no es un valor válido: {valor}")
        self._id = valor
        
    @property
    def nombre(self):
        return self._nombre
    @nombre.setter
    def nombre(self, valor):
        if not isinstance(valor, str):
            raise ValueError(f"Nombre no es un valor válido: {valor}")
        self._nombre = valor
    
    @property
    def origen(self):
        return self._origen
    @origen.setter
    def origen(self, valor):
        if (valor not in self.nodos) or (not isinstance(valor, no)):
            raise ValueError(f"El nodo origen no existe")
        self._origen = valor
        
        
    @property
    def destino(self):
        return self._destino
    @destino.setter
    def destino(self, valor):
        if (valor not in self.nodos) or (not isinstance(valor, no)):
            raise ValueError(f"El nodo destino no existe")
        self._destino = valor
    
    @property
    def peso(self):
        return self._peso
    @peso.setter
    def peso(self, valor):
        if not isinstance(valor, (float, int)):
            raise ValueError(f"Peso debe ser un numero real: {valor}")
        self._peso = valor
    
    @property
    def grosor(self):
        return self._grosor
    @grosor.setter
    def grosor(self, valor):
        if not isinstance(valor, int) or not (1 <= valor <= 10):
            raise ValueError(f"Grosor debe ser un entero entre 1 y 10: {valor}")
        self._grosor = valor
    
    @property
    def color(self):
        return self._color
    @color.setter
    def color(self, valor):
        if not isinstance(valor, tuple) or len(valor) != 3: ###?
            raise ValueError("Color debe ser tupla (R, G, B)") ###?
        self._color = valor
        
        
    @property
    def curvatura(self):
        return self._curvatura
    @curvatura.setter
    def curvatura(self, valor):
        if not isinstance(valor, (float, int)) or not (0 <= valor <= 10): ### limite?
            raise ValueError(f"Curvatura debe ser un numero real entre 0 y 10: {valor}") ### limite?
        self._curvatura = valor
        

    
    def __repr__(self):
        return ( f"[Arco no dirigido; indice:{self._id}, nombre:{self.nombre}, origen:{self.origen.id}, destino:{self.destino.id}, " 
                f"peso:{self.peso}, grosor:{self.grosor}, color:{self.color}, curvatura:{self.curvatura}]" )
    
    def __str__(self):
        return (
        "Arco(\n"
        f"  indice={self._id},\n"
        f"  nombre='{self.nombre}',\n"
        f"  origen={self.origen.id},\n"
        f"  destino={self.destino.id},\n"
        f"  peso={self.peso},\n"
        f"  grosor={self.grosor},\n"
        f"  color={self.color},\n"
        f"  curvatura={self.curvatura})\n"
    )

    





class ArcoDirigido:
    
    # atributos de clase
    numero_de_arcos = 0  # sin utilidad
    lista_de_arcos =[] ### lista compartida? # sin utilidad
    
    def __init__(self, nodos, id, nombre, origen, destino, peso=0, grosor=3, color=clrs.NEGRO, curvatura=0):
        
        # Validar valores críticos
        self._validar_valores_iniciales(nodos, id, nombre, origen, destino, peso, grosor, color, curvatura)
        
        # atributos básicos:
        self._id = id
        self.nombre:str = nombre ###
        self.nodos:list = nodos ###
        self.origen:no = origen ###
        self.destino:no = destino ###
        self.peso:float = peso
        self.grosor:int = grosor
        self.color:tuple = color
        self.curvatura:float = curvatura
        
        # atributos relacionados con ... :
        # no necesarios actualmente

            
        # atributos para algoritmos y visualización:
        # vacio por problemas estructurales de temporalidad y estado compartido entre algoritmos
        
        ArcoDirigido.numero_de_arcos+=1
        ArcoDirigido.lista_de_arcos.append(self)
        

    def _validar_valores_iniciales(self, nodos, id, nombre, origen, destino, peso, grosor, color, curvatura):
        if not isinstance(id, int):
            raise ValueError(f"Indice no es un valor válido: {id}")
        if not isinstance(nombre, str):
            raise ValueError(f"Nombre no es un valor válido: {nombre}")
        if (origen not in nodos) or (not isinstance(origen, no)) :
            raise ValueError(f"El nodo origen no existe")
        if (destino not in nodos) or (not isinstance(destino, no)):
            raise ValueError(f"El nodo destino no existe")
        if not isinstance(peso, (float,int)):
            raise ValueError(f"Peso debe ser un numero real: {peso}")
        if not isinstance(grosor, int) or not (1 <= grosor <= 10):
            raise ValueError(f"Grosor debe ser un entero entre 1 y 10: {grosor}")
        if not isinstance(color, tuple) or len(color) != 3: ###?
            raise ValueError("Color debe ser tupla (R, G, B)") ###?
        if not isinstance(curvatura, (float, int)) or not (0 <= curvatura <= 10): ### limite?
            raise ValueError(f"Curvatura debe ser un numero real entre 0 y 10: {curvatura}") ### limite?

     
    # Properties para validación continua
    @property
    def id(self):
        return self._id
    @id.setter
    def id(self, valor):
        if not isinstance(valor, int):
            raise ValueError(f"Indice no es un valor válido: {valor}")
        self._id = valor
        
    @property
    def nombre(self):
        return self._nombre
    @nombre.setter
    def nombre(self, valor):
        if not isinstance(valor, str):
            raise ValueError(f"Nombre no es un valor válido: {valor}")
        self._nombre = valor
    
    @property
    def origen(self):
        return self._origen
    @origen.setter
    def origen(self, valor):
        if (valor not in self.nodos) or (not isinstance(valor, no)):
            raise ValueError(f"El nodo origen no existe")
        self._origen = valor
        
        
    @property
    def destino(self):
        return self._destino
    @destino.setter
    def destino(self, valor):
        if (valor not in self.nodos) or (not isinstance(valor, no)):
            raise ValueError(f"El nodo destino no existe")
        self._destino = valor
    
    @property
    def peso(self):
        return self._peso
    @peso.setter
    def peso(self, valor):
        if not isinstance(valor, (float, int)):
            raise ValueError(f"Peso debe ser un numero real: {valor}")
        self._peso = valor
    
    @property
    def grosor(self):
        return self._grosor
    @grosor.setter
    def grosor(self, valor):
        if not isinstance(valor, int) or not (1 <= valor <= 10):
            raise ValueError(f"Grosor debe ser un entero entre 1 y 10: {valor}")
        self._grosor = valor
    
    @property
    def color(self):
        return self._color
    @color.setter
    def color(self, valor):
        if not isinstance(valor, tuple) or len(valor) != 3: ###?
            raise ValueError("Color debe ser tupla (R, G, B)") ###?
        self._color = valor
        
        
    @property
    def curvatura(self):
        return self._curvatura
    @curvatura.setter
    def curvatura(self, valor):
        if not isinstance(valor, (float, int)) or not (0 <= valor <= 10): ### limite?
            raise ValueError(f"Curvatura debe ser un numero real entre 0 y 10: {valor}") ### limite?
        self._curvatura = valor
        

    
    def __repr__(self):
        return ( f"[Arco no dirigido; indice:{self._id}, nombre:{self.nombre}, origen:{self.origen.id}, destino:{self.destino.id}, " 
                f"peso:{self.peso}, grosor:{self.grosor}, color:{self.color}, curvatura:{self.curvatura}]" )
    
    def __str__(self):
        return (
        "Arco(\n"
        f"  indice={self._id},\n"
        f"  nombre='{self.nombre}',\n"
        f"  origen={self.origen.id},\n"
        f"  destino={self.destino.id},\n"
        f"  peso={self.peso},\n"
        f"  grosor={self.grosor},\n"
        f"  color={self.color},\n"
        f"  curvatura={self.curvatura})\n"
    )











            
# pruebas
#nodo0 = Nodo("cacho", 100, 200)
#nodo1 = Nodo("cacho", 150, 250)
#nodo2 = Nodo("cacho", 170, 270)
##nodos = [nodo0, nodo1, nodo2]  

#arco_1 = ArcoNoDirigido(nodos, 1, "archi", nodo0, nodo1, peso=12)
#print(arco_1)

# (self, nodos ,nombre, origen, destino, peso, grosor=3, color=color_palettes.NEGRO, curvatura=0):

#arco_2 = ArcoNoDirigido([0,1,2,3,4], 2, "archi2", 0, 3, 33.77, 2, (25,25,25), 0.5)
#print(arco_2)

#print("numero de arcos no dirigidos: ", ArcoNoDirigido.numero_de_arcos)
#print("lista de arcos no dirigidos: ", ArcoNoDirigido.lista_de_arcos)
