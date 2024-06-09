import os
from qgis.PyQt.QtWidgets import QAction, QMessageBox, QDialog, QVBoxLayout, QLabel, QPushButton
from qgis.core import QgsProject, QgsWkbTypes, QgsField
from PyQt5.QtGui import QIcon
from geopy.geocoders import Nominatim
import time
from PyQt5.QtCore import QVariant


class ReverseGeocoder:
    def __init__(self, iface):
        self.iface = iface
        self.plugin_dir = os.path.dirname(__file__)
        self.geolocator = Nominatim(user_agent="qgis_reverse_geocoder")
        
    def initGui(self):
        # Pfad zum Icon erstellen
        icon_path = os.path.join(self.plugin_dir, 'icon.png')
        # QAction mit dem Icon erstellen
        self.action = QAction(QIcon(icon_path), "Reverse Geocode", self.iface.mainWindow())
        self.action.triggered.connect(self.show_dialog)
        self.iface.addToolBarIcon(self.action)
        self.iface.addPluginToMenu("&Reverse Geocoder", self.action)

    def unload(self):
        self.iface.removeToolBarIcon(self.action)
        self.iface.removePluginMenu("&Reverse Geocoder", self.action)

    def show_dialog(self):
        dialog = QDialog()
        dialog.setWindowTitle("Reverse Geocoder Anleitung")
        
        layout = QVBoxLayout()
        
        instructions = QLabel("Bitte wählen Sie eine Punkt-Shapefile-Ebene aus und klicken Sie auf 'Start', um die umgekehrte Geokodierung durchzuführen.")
        layout.addWidget(instructions)
        
        start_button = QPushButton("Start")
        start_button.clicked.connect(self.run)
        layout.addWidget(start_button)
        
        dialog.setLayout(layout)
        dialog.exec_()

    def run(self):
        layer = self.iface.activeLayer()
        if not layer:
            QMessageBox.critical(None, "Reverse Geocoder", "Bitte wählen Sie eine Punkt-Shapefile-Ebene aus.")
            return

        if layer.geometryType() != QgsWkbTypes.PointGeometry:
            QMessageBox.critical(None, "Reverse Geocoder", "Die ausgewählte Ebene ist keine Punkt-Ebene.")
            return

        # Überprüfen, ob das Attributfeld 'Adresse' existiert, andernfalls hinzufügen
        if 'Adresse' not in [field.name() for field in layer.fields()]:
            layer.dataProvider().addAttributes([QgsField("Adresse", QVariant.String)])
            layer.updateFields()

        # Beginne eine Bearbeitungssitzung
        layer.startEditing()

        for feature in layer.getFeatures():
            geom = feature.geometry()
            if geom.isNull():
                continue
            point = geom.asPoint()
            address = self.reverse_geocode(point.y(), point.x())
            feature['Adresse'] = address

            # Update das Feature mit der neuen Adresse
            layer.updateFeature(feature)
            # Warte kurz, um die Serverlast zu verringern (Nominatim-Limit von 1 Anfrage pro Sekunde)
            time.sleep(1)

        # Bearbeitungssitzung beenden und Änderungen speichern
        layer.commitChanges()
        layer.updateFields()

        QMessageBox.information(None, "Reverse Geocoder", "Die umgekehrte Geokodierung ist abgeschlossen und die Adressen wurden gespeichert.")

    def reverse_geocode(self, latitude, longitude):
        location = self.geolocator.reverse((latitude, longitude), timeout=10)
        return location.address if location else "Keine Adresse gefunden"
