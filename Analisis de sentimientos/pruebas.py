import random
from typing import Callable, Dict, List, Tuple, TypeVar, DefaultDict

FeatureVector = Dict[str, int]
WeightVector = Dict[str, float]
Example = Tuple[FeatureVector, int]

def kmeans(examples: List[Dict[str, float]], K: int,
           maxEpochs: int) -> Tuple[List, List, float]:


    def ReconstructionRoss():
        suma =0
        for i,puntos in enumerate(examples):
            suma += Distancia(punto, pCentroides[pertenencias[i]] )
        return suma

    def Distancia(punto : Dict[str,float] , centro : Dict[str,float]):
        res = 0
        for key in punto:
            res += (centro.get(key,0) - punto[key]) ** 2
        for key in centro:
            if key not in punto:
                res += (centro[key] - punto.get(key,0)) ** 2
        return res

    def PuntPertCentro(punto:Dict[str,float]):
        distMinima = Distancia(punto,pCentroides[0])
        iMinima = 0
        for i in range(1,K):
            distAux = Distancia(punto,pCentroides[i]) 
            if(distAux < distMinima):
                distMinima = distAux
                iMinima = i
        return iMinima

    def PuntoIgual(idCentro): 
        for i in range(tamMuestra):
            if( (pertenencias[i] == idCentro or pertPasadas[i] == idCentro)
                 and pertPasadas[i] != pertenencias[i]):
                return False
        return True

    def RecalcularPunto(idPunto):
        res =  dict()
        numPuntos=0
        for i in range(tamMuestra):
            if(pertenencias[i] == idPunto):
                numPuntos+=1
                for key in examples[i]:
                    res[key] = (examples[i][key] if key not in res else (res[key]+examples[i][key]) )
        
        for key in res :
            res[key] = res[key]/numPuntos
        return res

    def Convergio():
        for i in range(tamMuestra):
            if(pertenencias[i] != pertPasadas[i]):
                return False

        return True

    tamMuestra = len(examples)
    pertenencias = [-1]*(tamMuestra+1)
    #pCentroides = random.sample( examples , K) 
    pCentroides = [ {'x':20,'y':30} , {'x':20,'y':-10} ]


    for posPunto,punto in enumerate(examples):
            pertenencias[posPunto]=PuntPertCentro(punto)

    for idCentro,centro in enumerate(pCentroides):
        pCentroides[idCentro] = RecalcularPunto(idCentro)
    pertPasadas = pertenencias.copy()
    print(pCentroides)

    for i in range(1,maxEpochs):
        for posPunto,punto in enumerate(examples):
            pertenencias[posPunto]=PuntPertCentro(punto)

        if(Convergio()):
            break

        for idCentro,centro in enumerate(pCentroides):
            if not PuntoIgual(idCentro):
                pCentroides[idCentro] = RecalcularPunto(idCentro)
                
        pertPasadas = pertenencias.copy()
        print(pCentroides)


puntos = [{'x':10},{'x':30},{'x':10,'y':20},{'x':20,'y':20}]
kmeans(puntos,2,10)