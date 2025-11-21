
"""
import svgwrite

# Crear un documento SVG
dwg = svgwrite.Drawing("example.svg", profile="tiny")

# Dibujar un círculo rojo
dwg.add(dwg.circle(center=(100, 100), r=50, fill="red"))

# Dibujar un rectángulo azul
dwg.add(dwg.rect(insert=(150, 50), size=(100, 80), fill="blue"))

# Guardar archivo
dwg.save()

"""

import cv2
import svgwrite

# Leer imagen en escala de grises
img = cv2.imread("grafo.png", cv2.IMREAD_GRAYSCALE)

# Binarizar (necesario para contornos claros)
_, thresh = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)

# Encontrar contornos
contours, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# Crear archivo SVG
dwg = svgwrite.Drawing("output.svg")

# Dibujar cada contorno en el SVG
for contour in contours:
    points = [(int(pt[0][0]), int(pt[0][1])) for pt in contour]
    dwg.add(dwg.polyline(points, stroke="black", fill="none"))

dwg.save()

