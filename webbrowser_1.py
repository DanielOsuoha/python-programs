from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWebEngineWidgets import *
class MyWebBrowser(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MyWebBrowser, self).__init__(*args, **kwargs)
        
        self.window = QWidget()
        self.window.setWindowTitle("My Web Browser")
        self.layout = QVBoxLayout()
        self.horizontal = QHBoxLayout()
        
        self.url_bar = QTextEdit()
        self.url_bar.setMaximumHeight(28)
        self.forward_btn = QPushButton("Go")
        self.forward_btn.setMinimumHeight(28)
        
        
        self.back_btn = QPushButton("Go")
        self.back_btn.setMinimumHeight(28)
        
        
        self.go_btn = QPushButton("Go")
        self.go_btn.setMinimumHeight(28)
        
        self.horizontal.addWidget(self.back_btn)
        self.horizontal.addWidget(self.forward_btn)
        self.horizontal.addWidget(self.go_btn)
        
        self.layout.addWidget(self.url_bar)
        
        self.browser = QWebEngineView()
        self.layout.addLayout(self.horizontal)
        self.layout.addWidget(self.browser)
        
        self.browser.setUrl(QUrl("https://www.google.com"))
        self.window.setLayout(self.layout)
        self.window.show()
        
app = QApplication([])
window = MyWebBrowser()
app.exec_()