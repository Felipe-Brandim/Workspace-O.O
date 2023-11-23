# Aluno: Felipe Fernandes Brandim 
# Matricula: 202016201
# Aqui irei desenvolver o código do primeiro projeto de Orientação a objetos:
# Projeto 2

import math

class Ponto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Linha:
    def __init__(self, pontoA, pontoB):
        self.pontoA = pontoA
        self.pontoB = pontoB

class Circulo:
    def __init__(self, centro, raio):
        self.centro = centro
        self.raio = raio

class Retangulo:
    def __init__(self, cantoSuperiorEsquerdo, cantoInferiorDireito):
        self.cantoSuperiorEsquerdo = cantoSuperiorEsquerdo
        self.cantoInferiorDireito = cantoInferiorDireito

class Quadrado:
    def __init__(self, cantoSuperiorEsquerdo, lado):
        self.cantoSuperiorEsquerdo = cantoSuperiorEsquerdo
        self.lado = lado

def calcular_distancia(pontoA, pontoB):
    dx = pontoA.x - pontoB.x
    dy = pontoA.y - pontoB.y
    return math.sqrt(dx * dx + dy * dy)

def calcular_area_circulo(circulo):
    return math.pi * circulo.raio * circulo.raio

def calcular_area_retangulo(retangulo):
    largura = retangulo.cantoInferiorDireito.x - retangulo.cantoSuperiorEsquerdo.x
    altura = retangulo.cantoSuperiorEsquerdo.y - retangulo.cantoInferiorDireito.y
    return largura * altura

def calcular_area_quadrado(quadrado):
    return quadrado.lado * quadrado.lado

class UniversoInterativo:
    def __init__(self):
        self.iniciar()

    def iniciar(self):
        print("Digite as coordenadas do ponto1 (x y): ")
        x1, y1 = map(float, input().split())
        ponto1 = Ponto(x1, y1)

        print("Digite as coordenadas do ponto2 (x y): ")
        x2, y2 = map(float, input().split())
        ponto2 = Ponto(x2, y2)

        print("Distância entre ponto1 e ponto2:", calcular_distancia(ponto1, ponto2))

        linha1 = Linha(ponto1, ponto2)

        print("Digite as coordenadas do canto superior esquerdo do retângulo (x y): ")
        xs, ys = map(float, input().split())
        canto_superior_esquerdo = Ponto(xs, ys)

        print("Digite as coordenadas do canto inferior direito do retângulo (x y): ")
        xi, yi = map(float, input().split())
        canto_inferior_direito = Ponto(xi, yi)

        retangulo1 = Retangulo(canto_superior_esquerdo, canto_inferior_direito)

        print("Área do retângulo:", calcular_area_retangulo(retangulo1))

        print("Digite as coordenadas do canto superior esquerdo do quadrado (x y): ")
        xq, yq = map(float, input().split())
        canto_superior_esquerdo_quadrado = Ponto(xq, yq)

        print("Digite o tamanho do lado do quadrado: ")
        lado_quadrado = float(input())
        quadrado1 = Quadrado(canto_superior_esquerdo_quadrado, lado_quadrado)

        print("Área do quadrado:", calcular_area_quadrado(quadrado1))

        print("Digite as coordenadas do centro do círculo (x y): ")
        xc, yc = map(float, input().split())
        centro_circulo = Ponto(xc, yc)

        print("Digite o raio do círculo: ")
        raio_circulo = float(input())
        circulo1 = Circulo(centro_circulo, raio_circulo)

        print("Área do círculo:", calcular_area_circulo(circulo1))

# Criando uma instância da classe UniversoInterativo
universo_interativo = UniversoInterativo()

