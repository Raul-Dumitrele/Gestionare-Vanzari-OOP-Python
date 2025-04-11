import json
from datetime import datetime
from produs import Produs
from client import Client
from comanda import Comanda
from vanzari import Vanzari

vanzari = Vanzari()

while True:
    print("\n--- Meniu ---")
    print("1. Adaugă produs")
    print("2. Adaugă client")
    print("3. Adaugă comandă")
    print("4. Afișează produse")
    print("5. Afișează clienți")
    print("6. Afișează comenzi")
    print("7. Șterge produs")
    print("8. Șterge client")
    print("9. Șterge comandă")
    print("10. Caută produs după nume")
    print("11. Caută comenzi după client")
    print("12. Filtrează comenzi după dată")
    print("13. Raport produse cu stoc scăzut")
    print("14. Top clienți")
    print("15. Top produse")
    print("16. Salvează datele")
    print("17. Încarcă datele")
    print("0. Ieșire")
    
    alegere = input("Alege o opțiune: ")
    
    if alegere == "1":
        id = input("ID produs: ")
        nume = input("Nume produs: ")
        pret = float(input("Preț: "))
        stoc = int(input("Stoc: "))
        vanzari.adauga_produs(Produs(id, nume, pret, stoc))
        print("✅ Produs adăugat.")
        
    elif alegere == "2":
        id = input("ID client: ")
        nume = input("Nume client: ")
        vanzari.adauga_client(Client(id, nume))
        print("✅ Client adăugat.")
        
    elif alegere == "3":
        id = input("ID comandă: ")
        id_client = input("ID client: ")
        client = next((c for c in vanzari.clienti if c.id == id_client), None)
        if not client:
            print("❌ Client inexistent.")
            continue

        produse = []

        while True:
            id_produs = input("ID produs (sau enter pentru a termina): ")
            if not id_produs:
                break
            produs = next((p for p in vanzari.produse if p.id == id_produs), None)
            if not produs:
                print("❌ Produs inexistent.")
                continue
            cantitate = int(input("Cantitate: "))
            produse.append((produs, cantitate))

        try:
            vanzari.plaseaza_comanda(id, produse)
            print("✅ Comandă adăugată.")
        except ValueError as e:
            print(f"❌ Eroare: {e}")

            
    elif alegere == "4":
        vanzari.afiseaza_produse()

    elif alegere == "5":
        vanzari.afiseaza_clienti()

    elif alegere == "6":
        vanzari.afiseaza_comenzi()

    elif alegere == "7":
        id_produs = input("ID produs de șters: ")
        vanzari.sterge_produs(id_produs)

    elif alegere == "8":
        id_client = input("ID client de șters: ")
        vanzari.sterge_client(id_client)

    elif alegere == "9":
        id_comanda = input("ID comandă de șters: ")
        vanzari.sterge_comanda(id_comanda)
        
    elif alegere == "10":
        nume_produs = input("Introduceți numele produsului de căutat: ")
        produse_gasite = vanzari.cauta_produs_dupa_nume(nume_produs)
        for produs in produse_gasite:
            print(produs)

    elif alegere == "11":
        nume_client = input("Introduceți numele clientului: ")
        comenzi_gasite = vanzari.cauta_comenzi_dupa_client(nume_client)
        for comanda in comenzi_gasite:
            print(comanda)

    elif alegere == "12":
        data_start = input("Introduceți data de început (YYYY-MM-DD): ")
        data_end = input("Introduceți data de sfârșit (YYYY-MM-DD): ")
        data_start = datetime.strptime(data_start, "%Y-%m-%d")
        data_end = datetime.strptime(data_end, "%Y-%m-%d")
        comenzi_filtrate = vanzari.filtreaza_comenzi_dupa_data(data_start, data_end)
        for comanda in comenzi_filtrate:
            print(comanda)

    elif alegere == "13":
        prag = int(input("Introduceți pragul pentru stocuri scăzute: "))
        vanzari.raporteaza_stocuri_scazute(prag)

    elif alegere == "14":
        top_clienti = vanzari.top_clienti()
        for client in top_clienti:
            print(client)

    elif alegere == "15":
        top_produse = vanzari.top_produse()
        for produs, cantitate in top_produse:
            print(f"{produs}: {cantitate} vândute")

    elif alegere == "16":
        fisier = input("Introduceți numele fișierului pentru salvare: ")
        vanzari.salveaza_date(fisier)
        print("✅ Datele au fost salvate.")

    elif alegere == "17":
        fisier = input("Introduceți numele fișierului pentru încărcare: ")
        vanzari.incarca_date(fisier)
        print("✅ Datele au fost încărcate.")

    elif alegere == "0":
        print("👋 La revedere!")
        break

    else:
        print("⚠️ Opțiune invalidă.")
