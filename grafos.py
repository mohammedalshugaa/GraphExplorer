import color_palettes as clrs
import pygame
import nodos as no
import arcos as ar
import numpy as np

class GrafoNoDirigido:
    
    # atributos de clase
    numero_de_grafos = 0   # util 
    lista_de_grafos =[] # util 
    
    def __init__(self, nombre):
        
        self._indice = GrafoNoDirigido.numero_de_grafos # util 
        
        # Validar valores críticos
        self._validar_valores_iniciales(nombre)
        
        
        # atributos básicos:
        self._nombre:str = nombre
        self._lista_nodos:list = []
        self._lista_arcos:list = []
        self.m_adyacencia:np.array = None






        GrafoNoDirigido.numero_de_grafos+=1 # util 
        GrafoNoDirigido.lista_de_grafos.append(self) # util 
        


    def _validar_valores_iniciales(self, nombre):
        if not isinstance(nombre, str):
            raise ValueError(f"Nombre no es un valor válido: {nombre}")
        """
        if not isinstance(lista_nodos, list) or len(lista_nodos) == 0:
            raise ValueError("Los nodos se deben introducir en una lista no vacia")
        if not isinstance(lista_arcos, list) or len(lista_arcos) == 0:
            raise ValueError("Los arcos se deben introducir en una lista no vacia")
        """
    
     
    # Properties para validación continua
    @property
    def nombre(self):
        return self._nombre
    @nombre.setter
    def nombre(self, valor):
        if not isinstance(valor, str):
            raise ValueError(f"Nombre no es un valor válido: {valor}")
        self._nombre = valor
    
    """
    @property
    def lista_nodos(self):
        return self._lista_nodos
    @lista_nodos.setter
    def lista_nodos(self, valor):
        if not isinstance(valor, list) or len(valor) == 0:
            raise ValueError("Los nodos se deben introducir en una lista no vacia")
        self._lista_nodos = valor
    
    @property
    def lista_arcos(self):
        return self._lista_arcos
    @lista_arcos.setter
    def lista_arcos(self, valor):
        if not isinstance(valor, list) or len(valor) == 0:
            raise ValueError("Los arcos se deben introducir en una lista no vacia")
        self._lista_arcos = valor
    """
    
    
    
    # Método de instancia
    def agregar_nodo(self, nodo_nuevo:no.Nodo):
        if not isinstance(nodo_nuevo, no.Nodo):
            raise ValueError(f"Has intentado agregar un objeto que no es un nodo")
        self._lista_nodos.append(nodo_nuevo) 
        print( f"Nodo agregado correctamente al grafo {self._nombre}" )
        
    def agregar_arco(self, nuevo_arco:ar.ArcoNoDirigido, nodo_origen:no.Nodo, nodo_destino:no.Nodo):
        if not isinstance(nuevo_arco, ar.ArcoNoDirigido):
            raise ValueError(f"Has intentado agregar un objeto que no es un arco")
        if not isinstance(nodo_origen, no.Nodo) or not isinstance(nodo_destino, no.Nodo):
            raise ValueError(f"Has intentado inroducir un objeto que no es un nodo")
        if (nodo_origen not in self._lista_nodos) or (nodo_destino not in self._lista_nodos):
            raise ValueError(f"Has intentado conectar nodos inexistentes")
        self._lista_arcos.append(nuevo_arco) 
        print( f"Arco agregado correctamente al grafo {self._nombre}" )
        
        
    def dibujar_grafo(self, pantalla):
        for nodo in self._lista_nodos:
            nodo.dibujar_nodo_borde(pantalla)
     
     
     
        





    def __repr__(self):
        return ( f"[Grafo; indice:{self._indice}, nombre:{self.nombre}]") # nodos:{self.lista_nodos}, arcos:{self.lista_arcos}
    
    def __str__(self):
        return (
        "\nGrafo no dirigido (\n"
        f"  indice={self._indice},\n"
        f"  nombre='{self.nombre}',\n"
        f"  nodos:{self._lista_nodos},\n"
        f"  arcos:{self._lista_arcos} )\n"
    )






class GrafoDirigido:
    
    # atributos de clase
    numero_de_grafos = 0   # util 
    lista_de_grafos =[] # util 
    
    def __init__(self, nombre):
        
        self._indice = GrafoDirigido.numero_de_grafos # util 
        
        # Validar valores críticos
        self._validar_valores_iniciales(nombre)
        
        
        # atributos básicos:
        self._nombre:str = nombre
        self._lista_nodos:list = []
        self._lista_arcos:list = []
        self.m_adyacencia:np.array = None






        GrafoDirigido.numero_de_grafos+=1 # util 
        GrafoDirigido.lista_de_grafos.append(self) # util 
        


    def _validar_valores_iniciales(self, nombre):
        if not isinstance(nombre, str):
            raise ValueError(f"Nombre no es un valor válido: {nombre}")
        """
        if not isinstance(lista_nodos, list) or len(lista_nodos) == 0:
            raise ValueError("Los nodos se deben introducir en una lista no vacia")
        if not isinstance(lista_arcos, list) or len(lista_arcos) == 0:
            raise ValueError("Los arcos se deben introducir en una lista no vacia")
        """
    
     
    # Properties para validación continua
    @property
    def nombre(self):
        return self._nombre
    @nombre.setter
    def nombre(self, valor):
        if not isinstance(valor, str):
            raise ValueError(f"Nombre no es un valor válido: {valor}")
        self._nombre = valor
    
    
    
    
    # Método de instancia
    def agregar_nodo(self, nodo_nuevo:no.Nodo):
        if not isinstance(nodo_nuevo, no.Nodo):
            raise ValueError(f"Has intentado agregar un objeto que no es un nodo")
        self._lista_nodos.append(nodo_nuevo) 
        print( f"Nodo agregado correctamente al grafo {self._nombre}" )
        
    def agregar_arco(self, nuevo_arco:ar.ArcoDirigido, nodo_origen:no.Nodo, nodo_destino:no.Nodo):
        if not isinstance(nuevo_arco, ar.ArcoDirigido):
            raise ValueError(f"Has intentado agregar un objeto que no es un arco")
        if not isinstance(nodo_origen, no.Nodo) or not isinstance(nodo_destino, no.Nodo):
            raise ValueError(f"Has intentado inroducir un objeto que no es un nodo")
        if (nodo_origen not in self._lista_nodos) or (nodo_destino not in self._lista_nodos):
            raise ValueError(f"Has intentado conectar nodos inexistentes")
        self._lista_arcos.append(nuevo_arco) 
        print( f"Arco agregado correctamente al grafo {self._nombre}" )
     
     
     
        





    def __repr__(self):
        return ( f"[Grafo; indice:{self._indice}, nombre:{self.nombre}]") # nodos:{self.lista_nodos}, arcos:{self.lista_arcos}
    
    def __str__(self):
        return (
        "\nGrafo no dirigido (\n"
        f"  indice={self._indice},\n"
        f"  nombre='{self.nombre}',\n"
        f"  nodos:{self._lista_nodos},\n"
        f"  arcos:{self._lista_arcos} )\n"
    )
















    
"""
# pruebas no dirigido
nodo0 = no.Nodo(1, "cacho", 100, 200)
nodo1 = no.Nodo(2, "cacho", 150, 250)
nodo2 = no.Nodo(3, "cacho", 170, 270)
nodos_1 = [nodo0, nodo1, nodo2]  

arco_1 = ar.ArcoNoDirigido(nodos_1, 1, "archi", nodo0, nodo1, peso=12)

miprg = GrafoNoDirigido("mi_primer_grafo")
print(miprg)

miprg.agregar_nodo(nodo0)
miprg.agregar_nodo(nodo1)
miprg.agregar_nodo(nodo2)
print(miprg)

miprg.agregar_arco(arco_1, nodo0, nodo1)
print(miprg)


#print("numero de grafos: ", GrafoNoDirigido.numero_de_grafos)
#print("lista de grafos: ", GrafoNoDirigido.lista_de_grafos)
"""
    
    
            

        
