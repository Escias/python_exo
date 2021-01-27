class ExoWhile:

    def calcul(self, notes):
        i = 0
        print("minimum : " + str(min(notes)))
        print("maximum : " + str(max(notes)))
        for note in notes:
            i += note
        print("moyenne : " + str(round(i / len(notes), 2)))

    def threeNote(self):
        note_1, note_2, note_3 = input("Enter 3 number between 0 and 20 ").split()
        notes = [int(note_1), int(note_2), int(note_3)]
        self.calcul(notes)

    def note(self):
        i = 0
        notes = []
        n = int(input("Number of notes "))
        while i < n:
            notes.append(int(input("note " + str(i+1) + " = ")))
            i += 1
        print(notes)
        self.calcul(notes)

    def noEnd(self):
        notes = []
        inp = input("Enter a note or type 'fin' ")
        while inp != "fin":
            notes.append(int(inp))
            inp = input("Enter a new note or type 'fin' ")
        self.calcul(notes)
