import sys
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtWebEngineWidgets import QWebEngineView
from PyQt6.QtCore import QUrl

class BrowserWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("AntennaDesk")
        self.setGeometry(100, 100, 1200, 800)
        
        self.browser = QWebEngineView()
        self.setCentralWidget(self.browser)
        self.browser.load(QUrl("https://www.antennasearch.com/"))
        self.show()

def main():
    app = QApplication(sys.argv)
    window = BrowserWindow()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()