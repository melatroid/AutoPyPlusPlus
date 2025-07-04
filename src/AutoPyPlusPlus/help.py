import tkinter as tk
from tkinter import scrolledtext

def show_help_window(parent, text, title="Hilfe"):
    help_window = tk.Toplevel(parent)
    help_window.title(title)
    help_window.geometry("900x600")  # Du kannst die Größe hier anpassen
    help_window.transient(parent)
    help_window.grab_set()  # Modal-Fenster

    # Überschrift
    header_label = tk.Label(help_window, text=title, font=("Arial", 14, "bold"), anchor="w")
    header_label.pack(fill="x", padx=10, pady=5)

    # Scrollbarer Textbereich
    text_area = scrolledtext.ScrolledText(help_window, wrap=tk.WORD, font=("Courier", 10))
    text_area.insert(tk.END, text)
    text_area.configure(state="disabled")  # Nur lesbar
    text_area.pack(expand=True, fill="both", padx=10, pady=5)

    # Schließen-Button
    close_button = tk.Button(help_window, text="Schließen", command=help_window.destroy)
    close_button.pack(pady=10)

def show_edit_helper(parent_window):
    help_text = (
        "=== Hilfe – Funktionsbeschreibung mit Beispielen ===\n\n"
        "🚀 **Allgemeine Optionen**\n"
        "• **Onefile**\n"
        "  Alles in einer einzigen ausführbaren EXE-Datei bündeln (praktisch für einfache Verteilung).\n"
        "• **Konsole**\n"
        "  Lässt beim Ausführen das Konsolenfenster sichtbar (gut für Debug-Ausgaben).\n"
        "• **Fenster-Modus**\n"
        "  Anwendung ohne sichtbares Konsolenfenster starten (z.B. für grafische Benutzeroberflächen).\n"
        "• **Use PyArmor**\n"
        "  Aktiviert Code-Verschleierung für zusätzlichen Schutz (optional).\n\n"
        "📦 **Felder:**\n"
        "• **Name**\n"
        "  Name des Projekts oder der ausführbaren Datei.\n"
        "  Eingabebeispiel:\n"
        "  MeinBackupTool\n\n"
        "• **Script**\n"
        "  Pfad zum Python-Skript, das kompiliert werden soll.\n"
        "  Eingabebeispiel:\n"
        "  C:/Projekte/backupTool/backupWizard.py\n\n"
        "• **Ausgabeordner**\n"
        "  Zielordner für die erstellte EXE-Datei.\n"
        "  Eingabebeispiel:\n"
        "  C:/Projekte/backupTool/dist\n\n"
        "• **Iconpfad**\n"
        "  Pfad zu einer .ico-Datei als Programmsymbol.\n"
        "  Eingabebeispiel:\n"
        "  C:/Projekte/backupTool/assets/appicon.ico\n\n"
        "• **Add-Data**\n"
        "  Zusätzliche Dateien oder Ordner, die mit der EXE gebündelt werden sollen.\n"
        "  Format: Quellpfad:Zielpfad (bei mehreren Einträgen mit Semikolon trennen).\n"
        "  Eingabebeispiel:\n"
        "  C:/Daten/config.ini:config;C:/Daten/bilder:assets/bilder\n\n"
        "• **Hidden Imports**\n"
        "  Python-Module, die PyInstaller eventuell nicht automatisch erkennt.\n"
        "  Eingabebeispiel:\n"
        "  requests,lxml,custom_module\n\n"
        "• **Version-Datei**\n"
        "  Pfad zu einer Datei mit Versionsinformationen.\n"
        "  Eingabebeispiel:\n"
        "  C:/Projekte/backupTool/version.txt\n\n"
        "• **Runtime Hook**\n"
        "  Pfad zu einem Python-Skript, das beim Start der Anwendung ausgeführt wird.\n"
        "  Eingabebeispiel:\n"
        "  C:/Projekte/backupTool/startup_hook.py\n\n"
        "• **Splash-Bild**\n"
        "  Pfad zu einem Bild, das beim Start angezeigt wird.\n"
        "  Eingabebeispiel:\n"
        "  C:/Projekte/backupTool/splashscreen.png\n\n"
        "• **Spec-Datei**\n"
        "  Pfad zu einer .spec-Datei für individuelle PyInstaller-Build-Konfigurationen.\n"
        "  Eingabebeispiel:\n"
        "  C:/Projekte/backupTool/backupWizard.spec\n\n"
        "⚙️ **Erweiterte Optionen:**\n"
        "• **UPX**: Aktiviert Komprimierung der EXE (verkleinert die Dateigröße).\n"
        "• **Debug**: Aktiviert Debug-Modus (hilfreich für Fehlersuche).\n"
        "• **Clean**: Alte Build-Dateien vor dem Erstellen löschen.\n"
        "• **Strip**: Entfernt Debug-Symbole, verkleinert die EXE.\n"
        "• **Ohne Runtime Key**: Erstellt die EXE ohne Laufzeit-Schlüssel.\n"
        "• **Tcl deaktivieren**: Deaktiviert Tcl/Tk-Support (z.B. wenn nicht benötigt).\n\n"
        "📝 **Weitere Optionen:**\n"
        "Hier können zusätzliche PyInstaller-Parameter direkt eingetragen werden.\n"
        "Eingabebeispiel:\n"
        "--add-binary=\"C:/libs/extra.dll;extra.dll\" --hidden-import=asyncio\n\n"
        "✅ **Tipps für erfolgreiche Eingaben:**\n"
        "• **Add-Data**: Absolute Pfade verwenden und sicherstellen, dass Dateien/Ordner existieren.\n"
        "• **Hidden Imports**: Module ohne Leerzeichen, nur durch Kommas trennen.\n"
        "  Beispiel:\n"
        "  numpy,requests,flask\n"
        "• **Icon, Version, Splash**: Dateien müssen existieren und korrekt angegeben werden.\n"
        "• **Ausgabeordner**: Ordner muss existieren oder automatisch erstellt werden können.\n"
        "• **Script**: Muss ein gültiges Python-Skript sein.\n\n"
        "🖱️ **Schaltflächen:**\n"
        "• **Speichern**: Speichert die aktuellen Einstellungen des Projekts.\n"
        "• **Abbrechen**: Schließt das Editor-Fenster ohne Speichern.\n\n\n"
        
        "🔒 **PyArmor-Optionen (Schutz & Verschleierung)**\n"
        "• **--obf-code <0|1|2>**: Steuert die Obfuskationsebene des Codes (0=keine, 1=normal, 2=hoch).\n"
        "• **--obf-module <0|1>**: Obfuskiert das gesamte Modul (1=aktiviert).\n"
        "• **--mix-str**: Verschlüsselt Zeichenketten im Code.\n"
        "• **--no-wrap**: Deaktiviert den Standard-Wrap-Modus.\n"
        "• **--private**: Aktiviert den privaten Modus (Einschränkung interner Einblicke).\n"
        "• **--restrict**: Aktiviert restriktiven Modus für das Paket.\n"
        "• **--assert-import**: Sicherstellt, dass importierte Module obfuskiert sind.\n"
        "• **--assert-call**: Sicherstellt, dass aufgerufene Funktionen obfuskiert sind.\n"
        "• **--platform NAME**: Zielplattform angeben (z.B. windows.x86_64).\n"
        "• **--use-runtime PATH**: Laufzeitpaket von angegebenem Pfad verwenden.\n"
        "• **--outer**: Verwendet externen Laufzeitschlüssel für mehr Sicherheit.\n"
        "• **--expired DATE**: Ablaufdatum setzen (z.B. 2025-12-31).\n"
        "• **--period N**: Überprüfungsintervall für Laufzeitschlüssel.\n"
        "• **--bind-device DEV**: Bindet das Skript an bestimmte Geräte (z.B. MAC-Adresse).\n"
        "• **--pack <onefile|onedir|NAME.spec>**: Verpackt das obfuskierte Projekt.\n"
        "• **-r, --recursive**: Verschlüsselt Dateien in Unterordnern rekursiv.\n"
        "• **-O PATH**: Ausgabeverzeichnis festlegen.\n"
        "• **--exclude PATTERN**: Dateien oder Pfade von Obfuskation ausschließen.\n\n"
        "Diese Optionen können in den **PyArmor-Optionen** im Editor direkt angegeben werden.\n\n"
          "💡 **Beispiel-Eingabe:**\n"
        " --platform windows.x86_64 --pack onefile --expired 2025-12-31 --bind-device 08:00:27:12:34:56\n"
        "🖱️ **Schaltflächen:**\n"
        "• **Speichern**: Speichert die aktuellen Einstellungen des Projekts.\n"
        "• **Abbrechen**: Schließt das Editor-Fenster ohne Speichern.\n"
    )

    show_help_window(parent_window, help_text, title="Hilfe – Editor")

def show_main_helper(parent_window):
    help_text = (
        "=== Hilfe – Hauptfenster ===\n\n"
        "Dieses Fenster dient zur Verwaltung und zum Kompilieren von Projekten.\n"
        "Hier eine Übersicht aller Funktionen:\n\n"
        "🟩 Hotkeys:\n Use Caps Lock for best use \n\n"
        "• Shift+C: Alle Projekte kompilieren.\n"
        "• Shift+A: Neues Projekt hinzufügen.\n"
        "• Shift+D: Ausgewähltes Projekt löschen.\n"
        "• Shift+Y: Kompiliermodus A/B umschalten.\n"
        "• Shift+L: Projektdatei (.apyscript) laden.\n"
        "• Shift+S: Projektdatei (.apyscript) speichern als.\n"
        "• Shift+E: Arbeitsverzeichnis leeren.\n"
        "• Shift+T: Design-Theme wechseln.\n"
        "• Shift+Q: Programm beenden.\n"
        "• Shift+F: Vollbild Modus.\n"
        "• Enter: Projekt bearbeiten.\n\n"
        "🟩 Skripte Bereich:\n"
        "• Hinzufügen (Shift+A): Ein neues Python- oder Spec-Projekt zur Liste hinzufügen.\n"
        "• Bearbeiten (Enter): Das ausgewählte Projekt bearbeiten (z.B. Pfade oder Optionen ändern).\n"
        "• Löschen: Entfernt das aktuell ausgewählte Projekt aus der Liste.\n\n"
         "🟩 Projekte Bereich:\n"       
        "• Leeren: Löscht alle Projekte aus der Liste.\n"
        "• Laden: Lädt eine .apyscript-Datei und lädt die gespeicherten Projekte.\n"
        "• Speichern als: Speichert die aktuelle Projektliste als .apyscript oder .spec.\n\n"
        "🟩 Projektbereich:\n"
        "• Inspector: Öffnet den Debug-Inspector für die zuletzt erstellte Logdatei.\n"
        "• Alle kompilieren (Shift+C): Startet die Kompilierung aller ausgewählten Projekte.\n"
        "• Arbeitsverzeichnis leeren: Löscht alle compile_*.log-Dateien und den build-Ordner.\n\n"
        "🟩 Header:\n"
        "• Sprache auswählen: Wechselt die Sprache der Benutzeroberfläche.\n"
        "• INI laden: Lädt eine neue INI-Konfigurationsdatei.\n"
        "• About: Zeigt Informationen über dieses Programm.\n"
        "• 🎨 Colors: Ändert die Farben für Modus A/B.\n"
        "• 🖌️ Design: Wechselt das Design-Theme.\n\n"
        "🟩 Treeview:\n"
        "• Zeigt alle Projekte in der Liste an.\n"
        "• Checkboxen für Modus A/B zur Auswahl, welcher Modus verwendet wird.\n"
        "• Mit Doppelklick oder Enter das Projekt bearbeiten.\n\n"
    )
    show_help_window(parent_window, help_text, title="Hilfe – AutoPy++")

def show_spec_helper(parent_window):
    help_text = (
        "=== Hilfe – Spec-Editor Beschreibung mit Beispielen ===\n\n"
        "🚀 **Allgemeine Optionen**\n"
        "• **Onefile**\n"
        "  Bündelt die Anwendung in einer einzigen ausführbaren EXE-Datei (ideal für einfache Verteilung).\n"
        "• **Konsole**\n"
        "  Zeigt ein Konsolenfenster beim Ausführen der Anwendung an (nützlich für Debugging).\n"
        "• **Windowed**\n"
        "  Startet die Anwendung ohne ein sichtbares Konsolenfenster (z.B. für GUI-Anwendungen).\n\n"
        "📦 **Felder:**\n"
        "• **Name**\n"
        "  Der Name der ausführbaren Datei oder des Projekts.\n"
        "  Eingabebeispiel:\n"
        "  backupWizard\n\n"
        "• **Icon**\n"
        "  Pfad zu einer .ico-Datei, die als Symbol für die EXE verwendet wird.\n"
        "  Eingabebeispiel:\n"
        "  C:/xampp/htdocs/cebterOS/engineering/icon_services.ico\n\n"
        "• **Spec-Datei**\n"
        "  Pfad zu einer .spec-Datei, die PyInstaller-Build-Konfigurationen enthält.\n"
        "  Eingabebeispiel:\n"
        "  C:/xampp/htdocs/cebterOS/engineering/backupWizard.spec\n\n"
        "• **Runtime Hook**\n"
        "  Pfad zu einem Python-Skript, das beim Start der Anwendung ausgeführt wird.\n"
        "  Eingabebeispiel:\n"
        "  C:/Projekte/backupTool/startup_hook.py\n\n"
        "• **Hidden Imports**\n"
        "  Python-Module, die PyInstaller möglicherweise nicht automatisch erkennt.\n"
        "  Eingabebeispiel:\n"
        "  requests\nlxml\ncustom_module\n"
        "  (Ein Modul pro Zeile oder durch Kommas getrennt)\n\n"
        "• **Binaries (add_data)**\n"
        "  Zusätzliche Dateien oder Ordner, die in die EXE eingebunden werden sollen.\n"
        "  Format: Quellpfad:Zielpfad (mehrere Einträge in neuen Zeilen).\n"
        "  Eingabebeispiel:\n"
        "  C:/Daten/config.ini:config\nC:/Daten/bilder:assets/bilder\n\n"
        "⚙️ **Erweiterte Optionen:**\n"
        "• **UPX aktivieren**: Komprimiert die EXE-Datei mit UPX, um die Dateigröße zu reduzieren.\n"
        "• **Debug aktiv**: Aktiviert den Debug-Modus für detaillierte Ausgaben während des Build-Prozesses.\n"
        "• **Clean aktiv**: Löscht alte Build-Dateien vor einem neuen Build.\n"
        "• **Strip aktiv**: Entfernt Debug-Symbole aus der EXE, um die Dateigröße zu verringern.\n\n"
        "✅ **Tipps für erfolgreiche Eingaben:**\n"
        "• **Binaries (add_data)**: Verwende absolute Pfade und stelle sicher, dass die Dateien/Ordner existieren.\n"
        "• **Hidden Imports**: Gib Module ohne Leerzeichen an, entweder in neuen Zeilen oder durch Kommas getrennt.\n"
        "  Beispiel:\n"
        "  numpy\nrequests\nflask\n"
        "• **Icon und Spec-Datei**: Die Dateien müssen existieren und korrekt angegeben werden.\n"
        "• Überprüfe Pfade auf Tippfehler, insbesondere bei Groß-/Kleinschreibung.\n\n"
        "🖱️ **Schaltflächen:**\n"
        "• **Datei hinzufügen**: Fügt eine Daterosenkrantz-Dateien einbinden (z.B. Bilder, DLLs).\n"
        "• **Speichern**: Speichert die aktuellen Einstellungen des Spec-Editors.\n"
        "• **Abbrechen**: Schließt das Spec-Editor-Fenster ohne Speichern.\n"
        "• **Help**: Öffnet dieses Hilfefenster mit Anleitungen.\n"
    )
    show_help_window(parent_window, help_text, title="Hilfe – Spec-Editor")

def show_nuitka_helper(parent_window):
    help_text = (
        "=== Hilfe – Nuitka Compilation Editor ===\n\n"
        "🚀 **Allgemeine Optionen**\n"
        "• **Use Nuitka**\n"
        "  Aktiviert die Kompilierung mit Nuitka, um Python-Skripte in ausführbare Programme umzuwandeln. Deaktiviert bleibt das Skript ein normales Python-Programm, das Python benötigt.\n"
        "• **Standalone**\n"
        "  Erstellt eine eigenständige Anwendung mit allen Abhängigkeiten (z. B. Module, Bibliotheken) in einem Ordner. Ideal für die Verteilung auf Systeme ohne Python. Erzeugt größere Dateien (oft 100 MB+).\n"
        "• **Onefile**\n"
        "  Packt die gesamte Anwendung in eine einzige .exe-Datei (Windows) oder ein Programm (Linux/macOS). Beim Start wird die Datei temporär entpackt, was die Startzeit verlängern kann.\n"
        "• **Console**\n"
        "  Öffnet ein Konsolenfenster beim Programmstart, das Ausgaben (z. B. print oder Fehlermeldungen) anzeigt. Nützlich für Debugging, für Endnutzer oft deaktivieren.\n\n"
        "📦 **Weitere Optionen**\n"
        "• **Follow Imports**\n"
        "  Erkennt und bindet alle importierten Module automatisch ein (z. B. numpy, requests). Spart manuelle Konfiguration, kann aber die Dateigröße erhöhen. Deaktivieren, wenn du Module gezielt einbinden willst.\n"
        "• **Follow Stdlib**\n"
        "  Bindet Python-Standardbibliotheken (z. B. os, sys) ein, falls nicht automatisch erkannt. Selten nötig, nur bei obskuren Modulen wie ctypes aktivieren.\n"
        "• **Plugins**\n"
        "  Aktiviert Unterstützung für spezielle Bibliotheken (z. B. --plugin-enable=pyqt6 für PyQt6). Ohne passende Plugins können GUI- oder Datenbibliotheken fehlerhaft kompiliert werden.\n"
        "• **Extra Options**\n"
        "  Freitextfeld für zusätzliche Nuitka-Parameter, z. B. --include-module=mein_modul oder --noinclude-pandas. Falsche Eingaben führen zu Fehlern, siehe Nuitka-Dokumentation.\n"
        "• **Output Dir**\n"
        "  Der Ordner, in den die kompilierten Dateien geschrieben werden. Muss existieren und beschreibbar sein, z. B. C:\\MeinProjekt\\output.\n\n"
        "⚙️ **Leistungsoptionen**\n"
        "• **LTO (Link Time Optimization)**\n"
        "  Optimiert die Binärdatei für kleinere Größe und schnellere Ausführung. Optionen:\n"
        "  - **auto**: Nuitka wählt basierend auf Projektgröße (Standard).\n"
        "  - **yes**: Maximale Optimierung, aber längere Kompilierungszeit und höherer RAM-Verbrauch (8 GB+).\n"
        "  - **no**: Schnellere Kompilierung, größere Datei. Bei Fehlern no testen.\n"
        "• **Jobs**\n"
        "  Anzahl paralleler Kompilierungsprozesse (1, 2, 4, 8). Mehr Jobs beschleunigen, verbrauchen aber mehr RAM. Für moderne PCs: 4 oder 8, bei wenig RAM: 1 oder 2.\n"
        "• **Show Progress / Memory / Scons**\n"
        "  Zeigt Details während der Kompilierung:\n"
        "  - **Progress**: Fortschritt (z. B. 'Modul X wird kompiliert').\n"
        "  - **Memory**: Speicherverbrauch, hilfreich bei LTO.\n"
        "  - **Scons**: Details des Build-Systems, für fortgeschrittene Nutzer.\n"
        "• **Windows UAC Admin**\n"
        "  Fordert Admin-Rechte beim Programmstart (UAC-Abfrage). Nur aktivieren, wenn die Anwendung Systemzugriffe benötigt (z. B. Schreiben in C:\\Program Files).\n\n"
        "🎨 **Windows-spezifische Optionen**\n"
        "• **Windows Icon**\n"
        "  Pfad zu einer .ico-Datei (z. B. C:\\icon.ico) für das Programmsymbol in Taskleiste/Explorer. Muss mehrere Auflösungen (16x16, 32x32) enthalten.\n"
        "• **Windows Splash**\n"
        "  Pfad zu einem Bild (z. B. C:\\splash.png), das beim Programmstart angezeigt wird. Nützlich bei langer Ladezeit, niedrige Auflösung bevorzugen.\n\n"
        "✅ **Tipps**\n"
        "• Überprüfe Script-Pfad und Output-Ordner vor der Kompilierung.\n"
        "• Nutze nur Plugins, die mit deinen Bibliotheken kompatibel sind (siehe Nuitka-Dokumentation).\n"
        "• Security Level Buttons wählen vordefinierte Einstellungen (z. B. schnell oder sicher). Mit Analyse prüfen.\n"
        "• Aktiviere Show Progress/Memory bei Fehlern, um Probleme zu finden.\n\n"
        "🖱️ **Schaltflächen**\n"
        "• **Analyse**: Prüft Pfade, Plugins und Einstellungen auf Fehler vor der Kompilierung.\n"
        "• **Save**: Speichert die Einstellungen und schließt den Editor.\n"
        "• **Cancel**: Schließt ohne Speichern.\n"
        "• **Help**: Öffnet dieses Hilfefenster.\n"
    )
    show_help_window(parent_window, help_text, title="Hilfe – Nuitka Compilation Editor")    
    