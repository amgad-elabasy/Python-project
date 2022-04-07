def est_base(str):
    """
    vérifier si un caractère est un ADN
    :param str: un caractère
    :return:bool
    """
    return str=="A" or str=="T" or str=="G" or str=="C"


def est_adn(chaine):
    """
    vérifier si une chaîne correspond à un ADN (est constituée uniquement des caractères A, T, G, C)
    :param chaine:
    :return: bool
    """
    i = 0
    while i < len(chaine) and (chaine[i]=="A" or chaine[i]=="T" or chaine[i]=="G" or chaine[i]=="C"):
        i+=1
    return i == len(chaine)

def arn(str):
    """
    L'ARN est construit à partir de l'ADN en remplaçant la thymine T par l'uracile codé par la lettre U
    :param str: une séquence d'ADN
    :return: une séquence ARN
    """
    if est_adn(str) == False:
        print("la chîne de caractère n'est pas un ADN")
    else:
        valeur = str.replace("T","U")
        return valeur


def arn_to_codons(ch):
    """
    :param ch: une chaîne de caractères correspondant à de l'ARN
    :return: un tableau contenant la liste des codons
    """
    tab_codons = []
    i = 0
    while i < len(ch) and len(ch) % 3 == 0 :
        tab_codons.append(ch[i:i+3])
        i+=3
    j = 0
    while j < len(ch) and len(ch) % 3 != 0:
        tab_codons.append(ch[j:j+3])
        j+=3
    if j > len(ch):
        tab_codons.pop()
    return tab_codons


def load_dico_codons_aa(file):
    """
    :param file: un fichier au format JSON
    :return: la structure de données chargée en mémoire à partir du JSON.
    """
    fichier = open(file,"r")
    strjson = fichier.read()
    fichier.close()
    codons = loads(strjson)
    return codons


def codons_stop(dico):
    stop = []
    bases = "AUGC"
    i = 0
    while i < 4:
        j = 0
        while j < 4:
            k = 0
            while k < 4:
                if bases[i] + bases[j] + bases[k] not in dico:
                    stop.append(bases[i] + bases[j] + bases[k])
                k += 1
            j += 1
        i += 1
    return stop


def codons_to_aa(codons, dico):
    aa = []
    i = 0
    while i < len(codons) and codons[i] in dico:
        aa.append(dico[codons[i]])
        i += 1
    return aa




def nextIndice(tab,ind,elements):
    """

    :param tab: une liste
    :param ind: un indice de tab
    :param elements: une deuxième liste elements
    :return:  l'indice de la première case du tableau tab contenant une valeur de elements
    """
    i = ind
    while i < len(tab) and tab[i] not in elements :
        i+=1
    return i



def decoupe_sequence(seq, start, stop):
    """

        :param seq:
        :param start:
        :param stop:
        :return: un tableau contenant les différents morceaux
        """
    g_tab = []
    tab = []
    decoupe = False
    i = 0
    while i < len(seq):
        if seq[i] in stop:
            decoupe = False
            if not tab==[]:
                g_tab.append(tab)
            tab = []
        if decoupe == True:
            tab.append(seq[i])
        if seq[i] in start:
            decoupe = True
        i+=1
    if g_tab == []:
        return "Il n'y a aucune séquence codante"
    return g_tab


def codons_to_seq_codantes(seq_codons,dico):
    tab_decoupe = decoupe_sequence(seq_codons,["AUG"],codons_stop(dico))
    return tab_decoupe


def seq_codantes_to_seq_aas(tab_seq_codante,dico):
    aa = []

    j = 0
    while j < len(tab_seq_codante):
        tab1 = tab_seq_codante[j]
        aa.append(codons_to_aa(tab1, dico))
        j+=1
    return aa


def adn_encode_molecule(b_adn,dico,molecule):
    arn_correspond_adn = arn(b_adn)
    arn_correspond_adn_decoupe = arn_to_codons(arn_correspond_adn)
    return codons_to_aa(arn_correspond_adn_decoupe, dico) == molecule
