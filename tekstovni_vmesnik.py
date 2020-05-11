import model 

trenutna_igra = model.nova_igra()

def izpis_poraza(igra):
    return f"Izgubil si, geslo je bilo: {igra.geslo}"

def izpis_zmage(igra):
    return f'Zmagal si, geslo je bilo: {igra.geslo}, potreboval si {len(igra.napacne_crke())} ugibov'

def izpis_igre(igra):
    text = (
        f"Stanje gesla: {igra.pravilni_del_gesla()} \n"
        f"imaš še {model.STEVILO_DOVOLJENIH_NAPAK - igra.stevilo_napak()} možnosti za napako"
    )
    return text

def zahtevaj_vnos():
    return input('Vpiši naslednjo črko:')

def pozeni_vmesnik():
    # Naredimo novo igro:

    trenutna_igra = model.nova_igra()

    while True:
        # Pokažemo mu stanje
        print(izpis_igre(trenutna_igra))

        crka = zahtevaj_vnos()

        trenutna_igra.ugibaj(crka)

        if trenutna_igra.zmaga():
            print(izpis_zmage(trenutna_igra))
            return 
        if trenutna_igra.poraz():
            print(izpis_poraza(trenutna_igra))
            return

pozeni_vmesnik()