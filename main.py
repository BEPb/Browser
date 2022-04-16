from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtCore import *
import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.showMaximized()
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl("https://google.com"))
        self.setCentralWidget(self.browser)
        self.setWindowIcon(QIcon('images/chrome.png'))
        navbar = QToolBar()
        navbar.setStyleSheet('''
            background-color: white;
            min-height: 10%;
            padding: 10px;
        ''')
        self.addToolBar(navbar)

        # Back button
        backbutton = QAction(QIcon("images/back.png"), "Back", self)
        backbutton.triggered.connect(self.browser.back)
        navbar.addAction(backbutton)

        # Forward button
        forwardbutton = QAction(QIcon("images/forward.png"), "Forward", self)
        forwardbutton.triggered.connect(self.browser.forward)
        navbar.addAction(forwardbutton)

        # reload button
        reloadbutton = QAction(QIcon('images/reload.png'),"Reload", self)
        reloadbutton.triggered.connect(self.browser.reload)
        navbar.addAction(reloadbutton)

        # home button
        home = QAction(QIcon('images/home.png'),"Home", self)
        home.triggered.connect(self.navigate_home)
        navbar.addAction(home)

        self.url_bar = QLineEdit()
        self.url_bar.returnPressed.connect(self.navigate_url)
        self.url_bar.setStyleSheet('''
            border-radius: 10px;
            border:2px solid violet;
        ''')
        navbar.addWidget(self.url_bar)

        self.browser.urlChanged.connect(self.update_url)

    def navigate_home(self):
        self.browser.setUrl(QUrl("https://google.com"))

    def navigate_url(self):
        url = self.url_bar.text()
        self.browser.setUrl(QUrl(url))

    def update_url(self, q):
        self.url_bar.setText(q.toString())


app = QApplication(sys.argv)
app.setApplicationName("Browser")
app.setStyleSheet('''
    QWidget{
        font-size: 15px;
    }
''')
window = MainWindow()
window.show()
app.exec_()