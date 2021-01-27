from Script.exo2 import ExoFor
from Script.exo3 import ExoWhile


def choice(exo):
    exo_2 = ExoFor()
    exo_3 = ExoWhile()
    if exo == "2":
        exo_2.mjList()
        annee = exo_2.yearList()
        exo_2.dayYearList(annee)
        dico_annee = exo_2.dico(annee)
        exo_2.findDay(dico_annee)
    elif exo == "3":
        exo_3.threeNote()
        exo_3.note()
        exo_3.noEnd()


if __name__ == '__main__':
    exo = input("Choose an exercise :\n"
                "[2] exo2 'for'\n"
                "[3] exo3 'while'")
    choice(exo)
