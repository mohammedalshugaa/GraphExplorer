import color_palettes as clrs
import pygame

class Nodo:
    
    # atributos de clase
    numero_de_nodos = 0  # sin utilidad
    lista_de_nodos =[] # sin utilidad
    
    def __init__(self, id, nombre, pos_x, pos_y, es_grafo_dirigido=False, color=clrs.GRIS, 
                 radio=50, borde=0, color_borde=clrs.NEGRO):
        
        
        # Validar valores críticos
        self._validar_valores_iniciales(id, nombre, pos_x, pos_y, radio, borde, color, color_borde)
        
        # atributos básicos:
        self._id = id
        self._nombre:str = nombre ###
        self._pos_x:int = pos_x
        self._pos_y:int = pos_y
        self._color:tuple = color
        self._radio:int = radio
        self._borde:int = borde
        self._color_borde:tuple = color_borde 
        
        # atributos relacionados con arcos y otros nodos:
        self._nodos_vecinos:list = []  # calculado
        self._grado:int = None # calculado
        self._n_bucles:int = None # calculado
        if es_grafo_dirigido: # calculado
            self._grado_entrada:int = None # calculado
            self._grado_salida:int = None # calculado
            
        # atributos para algoritmos y visualización:
        self._visitado:bool = None # calculado
        self._activo:bool = None # calculado
        self._seleccionado:bool = None # calculado
        
        Nodo.numero_de_nodos+=1
        Nodo.lista_de_nodos.append(self)
        

    def _validar_valores_iniciales(self, id, nombre, pos_x, pos_y, radio, borde, color, color_borde):
        if not isinstance(id, int):
            raise ValueError(f"Indice no es un valor válido: {id}")
        if not isinstance(nombre, str):
            raise ValueError(f"Nombre no es un valor válido: {nombre}")
        if pos_x < 0 or pos_y < 0:
            raise ValueError(f"Posiciones deben ser >= 0: ({pos_x}, {pos_y})")
        if radio <= 0:
            raise ValueError(f"Radio debe ser > 0: {radio}")
        if borde < 0:
            raise ValueError(f"Borde debe ser >= 0: {borde}")
        if not isinstance(color, tuple) or len(color) != 3: ###?
            raise ValueError("Color debe ser tupla (R, G, B)") ###?
        if not isinstance(color_borde, tuple) or len(color_borde) != 3: ###?
            raise ValueError("Color debe ser tupla (R, G, B)") ###?
    
     
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
    def pos_x(self):
        return self._pos_x
    @pos_x.setter
    def pos_x(self, valor):
        if valor < 0:
            raise ValueError(f"pos_x no puede ser negativo: {valor}")
        self._pos_x = valor
    
    @property
    def pos_y(self):
        return self._pos_y
    @pos_y.setter
    def pos_y(self, valor):
        if valor < 0:
            raise ValueError(f"pos_y no puede ser negativo: {valor}")
        self._pos_y = valor
    
    @property
    def radio(self):
        return self._radio
    @radio.setter
    def radio(self, valor):
        if valor <= 0:
            raise ValueError(f"Radio debe ser > 0: {valor}")
        self._radio = valor
    
    @property
    def borde(self):
        return self._borde
    @borde.setter
    def borde(self, valor):
        if valor < 0:
            raise ValueError(f"Borde debe ser >= 0: {valor}")
        self._borde = valor
        
    @property
    def color(self):
        return self._color
    @color.setter
    def color(self, valor):
        if not isinstance(valor, tuple) or len(valor) != 3: ###?
            raise ValueError("Color debe ser tupla (R, G, B)") ###?
        self._color = valor
        
    @property
    def color_borde(self):
        return self._color_borde
    @color_borde.setter
    def color_borde(self, valor):
        if not isinstance(valor, tuple) or len(valor) != 3: ###?
            raise ValueError("Color debe ser tupla (R, G, B)") ###?
        self._color_borde = valor
    
    
    
    # metodos de instancia
    def dibujar_nodo(self, pantalla):
        pygame.draw.circle(pantalla, self.color, (self.pos_x, self.pos_y), self.radio)
        
    def dibujar_nodo_borde(self, pantalla):
        pygame.draw.circle(pantalla, self.color_borde, (self.pos_x, self.pos_y), self.radio+self.borde)
        pygame.draw.circle(pantalla, self.color, (self.pos_x, self.pos_y), self.radio)
                
    
    
    def __repr__(self):
        return ( f"[Nodo; indice:{self._id}, nombre:{self.nombre}, radio:{self.radio}, " 
                f"pos_x:{self.pos_x}, pos_y:{self.pos_y}, color:{self.color}]" )
    
    def __str__(self):
        return (
        "Nodo(\n"
        f"  indice={self._id},\n"
        f"  nombre='{self.nombre}',\n"
        f"  radio={self.radio},\n"
        f"  color={self.color},\n"
        f"  borde={self.borde},\n"
        f"  color_borde={self.color_borde})\n"
    )
    
    

# pruebas     
#nodo_1 = Nodo(1, "cacho", 100, 200)
#print(nodo_1)

#nodo_2 = Nodo(2, "paco", 500, 300, True, (17,17,17), 25, 2, clrs.BLANCO)
#print(nodo_2)

#print("numero de nodos: ", Nodo.numero_de_nodos)
#print("lista de nodos: ", Nodo.lista_de_nodos)

        
#print(120+50+200+200+100 + 250 + 500 + 250 + 100 + 50)
