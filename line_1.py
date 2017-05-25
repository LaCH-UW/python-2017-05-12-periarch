from matplotlib import pyplot as plt
from przyklad_liniowy import count_freq as count_freq
from przyklad_liniowy import return_values as return_values

words = ['morze', 'Polska', 'sklep', 'wiosna', 'dziecko'] # usunięto powtarzający się wyraz "morze"
filenames = ["lord-jim.txt", "przedwiosnie.txt", "sklepy-cynamonowe.txt", "szewcy.txt",
             "ziemia-obiecana-tom-pierwszy.txt"]
titles = ["Lord Jim", "Przedwiośnie", "Sklepy cynamonowe", "Szewcy", "Ziemia obiecana Tom I"]

def color_lines(texts):

    color_iterator = 0
    for fname, title in zip(texts, titles):
        data = return_values(count_freq(fname), words)
        plt.plot(data, color='C'+str(color_iterator), label=title)
        color_iterator += 1

    plt.xticks(range(len(words)), words)

    plt.title("Liczba wystąpień słów")
    plt.xlabel("Słowa")
    plt.ylabel("Liczba wystąpień")
    plt.legend()

    plt.savefig('plot.png')
    plt.show()

if __name__ == '__main__':
    color_lines(filenames)