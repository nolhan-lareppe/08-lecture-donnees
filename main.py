#### Imports et définition des variables globales

FILENAME = "listes.csv"

#### Fonctions secondaires

def read_data(filename):
    """retourne le contenu du fichier <filename>

    Args:
        filename (str): nom du fichier à lire

    Returns:
        list: le contenu du fichier (1 list par ligne)
    """
    l = []
    with open(filename, mode='r', encoding='utf8') as f:
        for elt in f:
            if elt != "\n":
                s = [int(x) for x in elt.replace("\n", "").split(';') if x != ""]
                l.append(s)
    return l


def get_list_k(data, k):
    """l = []
    for i in range(len(data)):
        l.append(data[i])"""""
    
    return data[k]

def get_first(l):
    return l[0]

def get_last(l):
    return l[-1]

def get_max(l):
    max = l[0]
    for i in range(len(l)):
        "for i in l[1:]:"
        if max < l[i]:
            max = l[i]

    return max

def get_min(l):
    min = l[0]
    for i in range(len(l)):
        "for i in l[1:]:"
        if min > l[i]:
            min = l[i]
    return min

def get_sum(l):
    sum = 0
    "for i in l[0:]:"
    for i in range(len(l)):
        sum += l[i]
    return sum


#### Fonction principale


def main():
    pass
    data = read_data(FILENAME)
    for i, l in enumerate(data):
        print(i, l)
    k = 37
    print(k, get_list_k(data, 37))


if __name__ == "__main__":
    main()
