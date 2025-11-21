import random as rd
import classes   # Asegúrate de que Grafo.py contiene la clase Grafo
import color_palettes



# [x, y, numero, color, radio, tiene_borde, grosor_borde]
def gen_nodos(x_canvas, y_canvas, n_nodos=rd.randint(4, 9),
              radio=30, min_dist=100, max_intentos_por_nodo=100,
              paleta=color_palettes.GRIS):
    
    # Como mínimo, que no se toquen los bordes de los nodos
    min_dist = max(min_dist, 2 * radio)
    min_dist2 = min_dist * min_dist

    coor = []
    for i in range(n_nodos):
        colocado = False
        for _ in range(max_intentos_por_nodo):
            x = rd.randint(radio, x_canvas - radio)
            y = rd.randint(radio, y_canvas - radio)

            # Comprobar distancia a todos los ya colocados
            ok = True
            for nx, ny, *_ in coor:
                dx = x - nx
                dy = y - ny
                if dx*dx + dy*dy < min_dist2:
                    ok = False
                    break

            if ok:
                #color_nodo = algorithms.colorear()
                paleta = rd.choice(color_palettes.lista_colores_pastel)
                color_nodo = paleta
                coor.append([x, y, i, color_nodo, radio, False, 0])
                colocado = True
                break

        if not colocado:
            raise RuntimeError(
                f"No se pudo colocar el nodo {i} tras {max_intentos_por_nodo} intentos. "
                f"Prueba a reducir min_dist ({min_dist}), disminuir n_nodos o aumentar el canvas."
            )
    return coor
   
   

 
# [primer_nodo, segundo_nodo, direccionalidad, peso, color_arco, repeticion]
def gen_arcos(n_nodos, color_arco, dirigido, es_simple, x_canvas, y_canvas):
    arcos = []
    n_arcos = rd.randint(4, 2*n_nodos)
    
    for i in range(n_arcos):
        x = rd.randint(0, n_nodos-1)
        y = rd.randint(0, n_nodos-1)
        peso = rd.randint(10, 100)
        color_rd = color_arco
        repeticion = 1
        
        # impedir la creacion de nodos reflexivos
        #while y == x: 
        #    y = rd.randint(0, n_nodos - 1)
        
        
        # determinar la direccionalidad
        if dirigido == True: 
            di = rd.choices(["un", "bi"], weights=[0.7, 0.32], k=1)[0]
        else:
            di = "bi"
        
        
        

        # Bucle para que no haya arcos curvas sin arcos lineas
        for a, b, _, _, _, _ in arcos:
                if (a == x and b == y) or (b == x and a == y):
                    if es_simple == False:
                        repeticion += 1
                    else:
                        continue
        
        arcos.append([x, y, di, peso, color_rd, repeticion])
        
    return arcos
