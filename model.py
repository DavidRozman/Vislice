STEVILO_DOVOLJENIH_NAPAK = 10

PRAVILNA_CRKA = '+'
PONOVLJENA_CRKA = 'o'
NAPACNA_CRKA = '-'

ZMAGA = 'W'
PORAZ = 'X'

bazen_besed = []
with open('Vislice/besede.txt') as datoteka_bazena:
    for beseda in datoteka_bazena:
        bazen_besed.append(beseda.strip().lower())


class Igra:
    
    def __init__(self, geslo, crke=None):
        self.geslo = geslo
        if crke is None:
            self.crke = []
        else:
            self.crke = crke

    def pravilne_crke(self):
        return [crka for crka in self.crke if crka in self.geslo]
    
    def napacne_crke(self):
        return [crka for crka in self.crke if crka not in self.crke]
    
    def stevilo_napak(self):
        return len(self.napacne_crke())
    
    def zmaga(self):
        for crka in self.geslo:
            if crka not in self.crke:
                return False
        return True

    def poraz(self):
        return self.stevilo_napak() > STEVILO_DOVOLJENIH_NAPAK
    
    def pravilni_del_gesla(self):
        izpis = ''
        for crka in self.geslo:
            if crka in self.crke:
                izpis += crka
            else:
                izpis += '_'
        return izpis
    
    def nepravilni_ugibi(self):
        return ' '.join(self.napacne_crke())

    def ugibaj(self, crka):
        velika_crka = crka.upper
        if self.zmaga():
            return ZMAGA
        elif self.poraz():
            return PORAZ
        else:
            if velika_crka in self.pravilne_crke():
                return PRAVILNA_CRKA
            elif velika_crka in self.napacne_crke():
                return NAPACNA_CRKA
        

def nova_igra():
    import random
    izbrana_beseda = random.choice(bazen_besed)
    return Igra(izbrana_beseda)
