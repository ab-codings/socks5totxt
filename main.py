# add socks5 to TXT
def add_to_txt():
    import locale

    # check systemlanguage
    systemlanguage = locale.getlocale()[0]

    # Translate
    translations = {
        'de_DE': {
            'eingabe_mitteilung': "Geben Sie den Pfad zur Eingabe-Textdatei ein: ",
            'ausgabe_mitteilung': "Geben Sie den Pfad zur Ausgabe-Textdatei ein: ",
            'erfolgreiche_modifikation': "Die Datei wurde erfolgreich modifiziert und gespeichert.",
            'fehler_mitteilung': "Ein Fehler ist aufgetreten: {}",
        },
        'en_US': {
            'eingabe_mitteilung': "Enter the path to the input text file: ",
            'ausgabe_mitteilung': "Enter the path to the output text file: ",
            'erfolgreiche_modifikation': "The file has been successfully modified and saved.",
            'fehler_mitteilung': "An error occurred: {}",
        }
    }

    # Use system language, if available, else german
    if systemlanguage in translations:
        translations = translations[systemlanguage]
    else:
        translations = translations['en_US']

    # check data paths
    input_filepath = input(translations['eingabe_mitteilung'])
    output_filepath = input(translations['ausgabe_mitteilung'])

    try:
        # open input file and create output file
        with open(input_filepath, 'r') as input_file, open(output_filepath, 'w') as output_file:
            for line in input_file:
                # modify line and write in output file
                modified_line = "socks\t" + line.strip() + '\n'
                output_file.write(modified_line)

        print(translations['erfolgreiche_modifikation'])

    except FileNotFoundError:
        print("Die angegebene Eingabe-Datei wurde nicht gefunden.")
    except Exception as e:
        print(translations['fehler_mitteilung'].format(e))


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    add_to_txt()