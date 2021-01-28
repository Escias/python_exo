class ExoWhile:

    def calcul(self, notes):
        i = 0
        print("minimum : " + str(min(notes)))
        print("maximum : " + str(max(notes)))
        for note in notes:
            i += note
        print("moyenne : " + str(round(i / len(notes), 2)))



    def threeNote(self):
        i = 0
        notes = []
        #note_1, note_2, note_3 = input("Enter 3 number between 0 and 20 ").split()
        while i < 3:
            number = int(input("note " + str(i+1) + " = "))
            if 0 <= number <= 20:
                notes.append(number)
            else:
                print("Must be between 0 and 20")
                continue
            i += 1
        #notes = [int(note_1), int(note_2), int(note_3)]
        self.calcul(notes)

    def note(self):
        i = 0
        notes = []
        n = int(input("Number of notes "))
        while i < n:
            number = int(input("note " + str(i + 1) + " = "))
            if 0 <= number <= 20:
                notes.append(number)
            else:
                print("Must be between 0 and 20")
                continue
            i += 1
        print(notes)
        self.calcul(notes)

    def noEnd(self):
        notes = []
        number = input("Enter a note or type 'fin' ")
        while number != "fin":
            n = int(number)
            if 0 <= n <= 20:
                notes.append(n)
            else:
                print("Must be between 0 and 20")
            number = input("Enter a new note or type 'fin' ")
        self.calcul(notes)
