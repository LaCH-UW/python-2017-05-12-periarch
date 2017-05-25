from matplotlib import pyplot as plt
from matplotlib import rc
from nltk import FreqDist

# ustawiamy czcionkę wspierającą unicode - w domyślnej są tylko znaki ASCII
rc('font', family='DejaVu Sans')

words = ['do', 'ma', 'jest', 'kot', 'zrobił']
title1 = 'lalka-tom-pierwszy.txt'
title2 = 'lalka-tom-drugi.txt'

nazwy_plikow = [ "lord-jim.txt", "przedwiosnie.txt", "sklepy-cynamonowe.txt", "szewcy.txt", "ziemia-obiecana-tom-pierwszy.txt" ]
tytuly = [ "Lord Jim", "Przedwiośnie", "Sklepy cynamonowe", "Szewcy", "Ziemia obiecana, Tom I"]

def heatmap_plot(ress, titles, words):
    plt.title("Liczba wystąpień słów")
#    plt.xlabel("Próbki")
#    plt.ylabel("Liczba wystąpień")

#    plt.plot(data1, color='r', label="Dane 1")
#    plt.scatter(range(len(names)), data1)
#    plt.plot(data2, color='b', label="Dane 2")
#    plt.scatter(range(len(names)), data2)

    plt.pcolor(ress)

#    plt.legend()

#    plt.grid()

    plt.yticks(range(len(titles)), titles)
    plt.xticks(range(len(words)), words, rotation = 90)

#    plt.tight_layout()
    plt.savefig('plot.png')
    plt.show()

def count_freq(fname):
    with open(fname) as fp:
        split_words = fp.read().split()
        freq_dist = FreqDist(split_words)
    return freq_dist

def return_values(freq, words):
    result = []
    for s in words:
        result.append(freq[s] if s in freq else 0)
    return result


def make_plot(files, titles, words):
    ress = []

    for file1 in files:
        freq1 = count_freq(file1)
        ress.append(return_values(freq1, words))

    heatmap_plot(ress, titles, words)

if __name__ == '__main__':
    make_plot(nazwy_plikow, tytuly, words)


# teraz dopisz kod tworzący wykres punktowy zawierający liczbę wystąpień słów z listy
# z punktami różnych kolorów dla pierwszego i drugiego tomu "Lalki"
# dostosuj legendę itp.

# podpowiedź: funkcję plt.plot(y) zastępuje funkcja plt.scatter(x, y)

