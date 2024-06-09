# Reverse-Geocoder
QGIS Plugin
Umgekehrte Geokodierung: Die Geokodierung wird für jeden Punkt in der ausgewählten Ebene durchgeführt und die Adressen werden in einem neuen Attributfeld "Adresse" gespeichert.
API-Rate-Limitierung: Das Plugin berücksichtigt die API-Beschränkungen von Nominatim durch eine kurze Wartezeit zwischen den Anfragen.

Die Schritte, um das Plugin zu verwenden:

1. geopy in der QGIS-Python-Umgebung installieren
Windows
Öffne die OSGeo4W Shell:

2.Suche im Startmenü nach OSGeo4W Shell und öffne sie.
Installiere geopy in der QGIS-Python-Umgebung:
python3 -m pip install geopy

3. Plugin in QGIS installieren
Öffne QGIS.
Gehe zu Erweiterung > Erweiterung Verwalten und Installieren Plugins.
Klicke auf die Schaltfläche Install from ZIP.
Wähle die ZIP-Datei aus (reverse_geocoder.zip), und klicke auf Install Plugin.

4. Plugin aktivieren und verwenden
Nach der Installation sollte das Plugin in der Liste der installierten Plugins erscheinen.
Aktiviere das Plugin indem du das Kontrollkästchen neben dem Plugin-Namen aktivierst.

5. Plugin verwenden
Wähle eine Punkt-Layer aus, die du umgekehrt geokodieren möchtest.
Klicke auf das Plugin-Symbol oder wähle das Plugin aus dem Menü Erweiterung > Reverse Geocoder. Klicke dann auf Start. Warte anschließend je nach Anzahl der Punkte. Jeder AP dauert 1 Sekunde, das heißt, 100 AP dauern mindestens 100 Sekunden.
Das Plugin führt die umgekehrte Geokodierung durch und zeigt (Die umgekehrte Geokodierung ist abgeschlossen und die Adressen wurden gespeichert) in einem Dialogfeld an.
Die Adresse wurden in neue Spalte (Address) gespeichert.


linkedin: (https://www.linkedin.com/in/homayoon-afsharpoor/)
