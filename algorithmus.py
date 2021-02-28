import itertools
import more_itertools


def minverschnitt(lager, eingabe):

    verschnitt = []
    for i in range(len(eingabe)):
        verschnitt.append([])
        for j in range(len(lager)):
            if lager[j] - eingabe[i] >= 0:
                verschnitt[i].append(lager[j] - eingabe[i])
            else:
                verschnitt[i].append(15000)

    return verschnitt

def fullstack(lager, eingabe, verbose, add):
    subsubsets = list(more_itertools.set_partitions(set(eingabe)))

    verschnitt = []
    for i in range(len(subsubsets)):
        verschnitt.append([])
        for k in range(len(lager)):
            verschnitt[i].append([])
            for j in range(len(subsubsets[i])):
                verschnitt[i][k].append(lager[k]-sum(subsubsets[i][j]))
    print(subsubsets)
    print(verschnitt)


def kombinierterverschnitt(lager, eingabe, verbose, add):

    subsets = []

    for i in range(len(eingabe)):
        for j in itertools.combinations(eingabe, i):
            subsets.append(j)
    verschnitt = []
    verschnittsäge = []
    for i in range(len(subsets)):
        verschnitt.append([])
        verschnittsäge.append([])
        for j in range(len(lager)):
            if lager[j] - sum(subsets[i]) >= 0:
                if add != 0:
                    verschnittsäge[i].append(lager[j] - sum(subsets[i])+(add*len(subsets[i])))
                verschnitt[i].append(lager[j] - sum(subsets[i]))
            else:
                verschnitt[i].append(15000)

    return subsets, verschnitt, verschnittsäge



def getminverschnitt(lager, eingabe, verschnitt):
    for i in range(len(verschnitt)):
        print("der minimale Verschnitt für das Stück der länge: " + str(eingabe[i]) + " beträgt: " + str(min(verschnitt[i])) + " Das ausgelagerte Stück hat eine Länge von: " + str(lager[verschnitt[i].index(min(verschnitt[i]))]))