#importação da biblioteca DEAP dos recursos necessários
from deap import base, creator

#para um problema de minimização
creator.create("FitnessMin", base.Fitness, weights=(-1.0,))
#deriva de uma lista de fitness do recurso acima
creator.create("Individual", list, fitness=creator.FitnessMin)
