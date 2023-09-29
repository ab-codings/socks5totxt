# add socks5 to TXT
def add_to_txt():
    # Dateipfad abfragen
    eingabe_dateipfad = input("Geben Sie den Pfad zur Eingabe-Textdatei ein: ")
    ausgabe_dateipfad = input("Geben Sie den Pfad zur Ausgabe-Textdatei ein: ")

    try:
        # Eingabe-Datei öffnen und Ausgabe-Datei erstellen
        with open(eingabe_dateipfad, 'r') as eingabe_datei, open(ausgabe_dateipfad, 'w') as ausgabe_datei:
            for zeile in eingabe_datei:
                # Zeile modifizieren und in Ausgabe-Datei schreiben
                modifizierte_zeile = "SOCKS5\t" + zeile.strip() + '\n'
                ausgabe_datei.write(modifizierte_zeile)

        print("Die Datei wurde erfolgreich modifiziert und gespeichert.")

    except FileNotFoundError:
        print("Die angegebene Eingabe-Datei wurde nicht gefunden.")
    except Exception as e:
        print(f"Ein Fehler ist aufgetreten: {e}")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    add_to_txt()