#importa��o da biblioteca DEAP dos recursos necess�rios
from deap import base, creator

#para um problema de minimiza��o
creator.create("FitnessMin", base.Fitness, weights=(-1.0,))
#deriva de uma lista de fitness do recurso acima
creator.create("Individual", list, fitness=creator.FitnessMin)
