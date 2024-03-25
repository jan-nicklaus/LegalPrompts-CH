# LegalPrompts
Grosse Sprachmodelle wie ChatGPT von OpenAI oder Googles Gemini erobern die juristische Arbeitswelt. Bei einfachen Anfragen wie «Fasse BGE 149 V 57 zusammen!», helfen die Antworten häufig kaum weiter, da die relevanten (rechtlichen) Aspekte oft nicht wiedergegeben werden oder Erwägungen und Sachverhaltsaspekte erfunden werden (sog. Halluzinationen).

Um die Modelle gewinnbringend einsetzen zu können, ist es zentral, eine gut formulierte Aufforderung (sog. «Prompt») in das Sprachmodell einzugeben. Der «Prompt Builder» nimmt die Nutzerin und den Nutzer an die Hand, indem diese ihre verschiedenen Bedürfnis

## Mögliche Roadmap für die Challenge
+ Fragebogen zu wichtigen Prompt-Bestandteilen
+ Texterkennung aus Dateien und URLs und Einbindung in Prompt
+ Token Counting für gängige LLMs
+ Automatische Übersetzung mit DeepL
+ Datenbank für Prompt-Bestandteile
+ Automatische Einbindung von Gerichtsentscheiden (z.B. BGEs anhand der Nummer)
+ Optionale Einbindung z.B. des OpenAI API für sofortige Ausführung des Prompts
+ etc. etc.


## Vorraussetzungen

installiere die requirements um das Projekt zu starten
$ pip install -r requirements.txt

starte den web server
$ python -m flask run

Der Server läuft auf dem Port 5001 http://localhost:5001/


## Anleitung für unsere Anwendung
+ Auswahl des Sprachmodells (oder ohne nutzen)
+ Bei Benutzung mit Sprachmodell im  Feld "OpenAI Key" den Key eingeben
+ Fundstelle im Freitextfeld angeben (Entscheidnummer)
+ Stil auswählen (juristisch/nicht juristisch)
+ Ggf. Länge des Entscheids regulieren
+ Auswahl, ob die Entscheidzusammenfassung in Bulletpoints oder in einem Fliesstext erscheinen soll
+ Bedürfnisse für die Entscheidzusammenfassung in der Checkbox auswählen
+ Entscheid laden
+ Die Entscheidzusammenfassung erscheint (falls mit API Key in einem Pop-Up Fenster)

## Umsetzung
Die Umsetzung erfolgte im Rahmen des Open Legal Lab 2024 (https://opendata.ch/de/events/open-legal-lab-2024/).

## Kontakt
Ich freue mich über jeden Input hier oder unter https://linkedin.com/in/jan-nicklaus

