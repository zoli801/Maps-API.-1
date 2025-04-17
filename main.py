import sys
import requests
from PyQt6.QtWidgets import QApplication, QLabel, QMainWindow
from PyQt6.QtGui import QPixmap


# from PyQt6.QtCore import Qt
# from io import BytesIO


class MapViewer(QMainWindow):
    def __init__(self, lon=37.620070, lat=55.753630, zoom=10):
        super().__init__()
        self.setWindowTitle("Yandex Map Viewer")
        map_image = self.get_map_image(lon, lat, zoom)
        label = QLabel(self)
        pixmap = QPixmap()
        pixmap.loadFromData(map_image)
        label.setPixmap(pixmap)
        self.setCentralWidget(label)
        self.resize(pixmap.width(), pixmap.height())

    def get_map_image(self, lon, lat, zoom):
        url = f"https://static-maps.yandex.ru/1.x/"
        params = {"ll": f"{lon},{lat}", "z": str(zoom), "l": "map", "size": "600,450"}
        response = requests.get(url, params=params)
        return response.content


if __name__ == "__main__":
    app = QApplication(sys.argv)
    viewer = MapViewer(lon=30.31413, lat=59.93863, zoom=12)  # там, где я сейчас)))
    viewer.show()
    sys.exit(app.exec())
