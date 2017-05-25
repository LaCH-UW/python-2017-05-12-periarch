from matplotlib import pyplot as plt
from przyklad_liniowy import count_freq as count_freq
from przyklad_liniowy import return_values as return_values
import numpy as np

filenames = {"Lalka Tom I": "lalka-tom-pierwszy.txt", "Lalka Tom II": "lalka-tom-drugi.txt"}
words = ['Wokulski', 'Rzecki', 'subiekt', 'handel', 'sklep']

def bar_chart(title1, title2, words):

    freqs_1 = return_values(count_freq(filenames[title1]), words)
    freqs_2 = return_values(count_freq(filenames[title2]), words)

    fig, ax = plt.subplots()

    index = np.arange(len(words))
    bar_width = 0.35

    plt.bar(index, freqs_1, bar_width,
            color='r',
            label=title1)

    plt.bar(index + bar_width, freqs_2, bar_width,
            color='b',
            label=title2)

    plt.xticks(index + bar_width / 2, words)
    plt.title('Liczba wystąpień słów w I i II tomie "Lalki"')
    plt.xlabel("Utwory")
    plt.ylabel("Liczba wystąpień")
    plt.tight_layout()

    plt.savefig('plot.png')
    plt.show()

if __name__ == '__main__':
    bar_chart("Lalka Tom I", "Lalka Tom II", words)