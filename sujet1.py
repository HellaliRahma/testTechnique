import statistics
from random import *

def moyenne(tableau):
    return sum(tableau, 0.0) / len(tableau)

def variance(tableau):
    m=moyenne(tableau)
    return moyenne([(x-m)**2 for x in tableau])

def ecartype(tableau):
    return variance(tableau)**0.5

def statistic(echantillon):
    print(moyenne(echantillon))
    print(ecartype(echantillon))
    print(variance(echantillon))
    print(statistics.mean(echantillon))
    print(statistics.harmonic_mean(echantillon))
    print(statistics.median(echantillon))
    print(statistics.median_low(echantillon))
    print(statistics.median_high(echantillon))
    print(statistics.median_grouped(echantillon))
    print(statistics.mode(echantillon))


