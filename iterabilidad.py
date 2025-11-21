class Contador:
    def __init__(self, limite):
        self.limite = limite
        self.valor_actual = 0  # Estado inicial para la iteración

    # 1. El método __iter__
    # Retorna el objeto iterador (en este caso, 'self').
    def __iter__(self):
        self.valor_actual = 0  # Reinicia la cuenta cada vez que se pide un iterador
        return self

    # 2. El método __next__
    # Retorna el siguiente elemento de la secuencia.
    def __next__(self):
        # Avanza el valor
        self.valor_actual += 1
        
        # Comprueba si se ha alcanzado el final de la iteración
        if self.valor_actual > self.limite:
            # Si se supera el límite, se lanza la excepción para detener el bucle 'for'
            raise StopIteration
        
        # Retorna el valor actual
        return self.valor_actual

# Uso
print("--- Usando el Contador como Iterador ---")
mi_contador = Contador(3) 

for numero in mi_contador:
    print(numero)