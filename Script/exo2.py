class ExoFor:
    jours = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    mois = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October",
            "November", "December"]
    jours_semaine = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

    def mjList(self):
        mj = []
        for i in range(12):
            li = [self.mois[i], self.jours[i]]
            mj.append(li)
        print(mj)

    def yearList(self):
        i = 0
        annee = []
        for jour in self.jours:
            for d in range(jour):
                annee.append(str(d + 1) + " " + self.mois[i])
            i += 1
        print(annee)
        print(len(annee))
        return annee

    def dayYearList(self, annee):
        annee2 = []
        for i in range(len(annee)):
            annee2.append(self.jours_semaine[i % 7] + " " + annee[i])
        print(annee2)
        print(len(annee2))

    def dico(self, annee):
        dico_annee = {}
        for i in range(len(annee)):
            dico_annee[annee[i]] = self.jours_semaine[i % 7]
        print(dico_annee)
        return dico_annee

    def findDay(self, dico_annee):
        find = input("Enter date : <number> <month>").title()
        print(dico_annee[find])
