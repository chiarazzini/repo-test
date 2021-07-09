class Persona:
    def __init__(self, nome, cognome, annoNascita, residenza):
        self.nome = nome
        self.cognome = cognome
        self.annoNascita = annoNascita
        self.residenza = residenza

    def profilo(self):
        return "Nome: " + str(self.nome) + '\n' + "Cognome: " + str(self.cognome) + '\n' + "Anno:" + str(self.annoNascita) + '\n' + "Residenza: " + str(self.residenza)


    def __str__(self):
        return str(self.nome) + " " + str(self.cognome) + '\n'

class Sviluppatore(Persona):
    def __init__(self,nome, cognome, annoNascita, residenza, posizione, pagaAnnua):
        super().__init__(nome, cognome, annoNascita, residenza)
        self.posizione = posizione
        self.pagaAnnua = pagaAnnua

    def profilo(self):
        profilo = f"""
        Posizione: {self.posizione}
        Paga Annua: {self.pagaAnnua}"""

        return super().profilo() + profilo

    def __str__(self):
        return self.posizione + " " + self.nome + " " + self.cognome

per1 = Persona('Sara', 'Rossi', 24, 'Milano')
developer = Sviluppatore('Giorgio', 'Rossi', 30, 'Roma', 'dipendente', 1200)
print(per1.profilo())
print(per1.__str__())
print(developer.profilo())
print(developer.__str__())
