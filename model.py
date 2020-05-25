
import json
STEVILO_DOVOLJENIH_NAPAK = 10

ZACETEK = 'Z'

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
        self.geslo = geslo.lower()
        if crke is None:
            self.crke = []
        else:
            self.crke = [c.lower() for c in crke]

    def pravilne_crke(self):
        return [crka for crka in self.crke if crka in self.geslo]
    
    def napacne_crke(self):
        return [crka for crka in self.crke if crka not in self.geslo]
    
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
        mala_crka = crka.lower()
        if mala_crka in self.crke:
            return PONOVLJENA_CRKA
        self.crke.append(mala_crka)
        if mala_crka in self.geslo:
            if self.zmaga():
                return ZMAGA
            else:
                return PRAVILNA_CRKA
        else:
            if self.poraz():
                return PORAZ
            else:
                return NAPACNA_CRKA

def nova_igra():
    import random
    izbrana_beseda = random.choice(bazen_besed)
    return Igra(izbrana_beseda)

class Vislice:
    def __init__(self,):
        # slovar, ki ima ID-ju priredi objekt njegove igre
        self.igre = {} # int -> Igra

    def prosti_id_igre(self):
        # vrne nek ID ki ga ne uporablja nobena igra
        if len(self.igre) == 0:
            return 0
        else:
            return max(self.igre.keys()) + 1
    
    def nova_igra(self):
        self.preberi_iz_datoteke()
        # dobimo svež ID

        nov_id = self.prosti_id_igre()

        # naredimo novo igro

        sveza_igra = nova_igra()

        # vse to shranimo v self.igre

        self.igre[nov_id] = (sveza_igra, ZACETEK)
        self.shrani_v_datoteko()

        # vrnemo nov ID
        return nov_id
    
    def ugibaj(self, id_igre, crka):
        # dobimo staro igro ven
        self.preberi_iz_datoteke()
        trenutna_igra, _ = self.igre[id_igre]
        # ugibamo crko, dobimo novo stanje
        novo_stanje = trenutna_igra.ugibaj(crka)
        # zapišemo posodobljeno stanje in igro nazaj v 'bazo'
        self.igre[id_igre] = (trenutna_igra, novo_stanje)
        self.shrani_v_datoteko()

    def shrani_v_datoteko(self):

        igre = {}
        for id_igre, (igra, stanje) in self.igre.items():
            igre[id_igre] = ((igra.geslo, igra.crke), stanje)
        
        with open('Vislice/stanje_iger.json', 'w') as out_file:
            json.dump(igre, out_file)

    def preberi_iz_datoteke(self):
        with open('Vislice/stanje_iger.json', 'r') as in_file:
            igre = json.load(in_file)

        self.igre = {}

        for id_igre , ((geslo, crke), stanje) in igre.items():
            (geslo, crke), stanje = igre[id_igre]
            self.igre[int(id_igre)] = Igra(geslo, crke), stanje