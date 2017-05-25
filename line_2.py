from matplotlib import pyplot as plt
from przyklad_liniowy import count_freq as count_freq
from przyklad_liniowy import return_values as return_values

filenames = ["lord-jim.txt", "przedwiosnie.txt", "sklepy-cynamonowe.txt", "szewcy.txt",
             "ziemia-obiecana-tom-pierwszy.txt"]
titles = ["Lord Jim", "Przedwiośnie", "Sklepy cynamonowe", "Szewcy", "Ziemia obiecana Tom I"]
word = 'morze'

def one_word(results, texts_titles, word):

    plt.plot(results, color='r')

    plt.xticks(range(len(texts_titles)), texts_titles, rotation=90)

    plt.title('Liczba wystąpień słowa "' + word + '"')
    plt.xlabel("Słowa")
    plt.ylabel("Liczba wystąpień")
    plt.tight_layout()

    plt.savefig('plot.png')
    plt.show()

if __name__ == '__main__':
    results = []
    for fname in filenames:
        results.append(return_values(count_freq(fname), [word])[0])

    one_word(results, titles, word)