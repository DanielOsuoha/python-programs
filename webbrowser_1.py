from PyQt5.QtWidgets import *
# from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWebEngineWidgets import *
class MyWebBrowser(QMainWindow):
    def __init__(self): 
        super(MyWebBrowser, self).__init__()       
        self.window = QWidget()
        self.window.setWindowTitle("My Web Browser")
        self.layout = QVBoxLayout()
        self.horizontal = QHBoxLayout()
        
        self.url_bar = QTextEdit()
        self.url_bar.setMaximumHeight(28)
        self.forward_btn = QPushButton("Forward")
        self.forward_btn.setMinimumHeight(28)
        
        
        self.back_btn = QPushButton("Back")
        self.back_btn.setMinimumHeight(28)
        
        
        self.go_btn = QPushButton("Go")
        self.go_btn.setMinimumHeight(28)
        
        self.horizontal.addWidget(self.back_btn)
        self.horizontal.addWidget(self.forward_btn)
        self.horizontal.addWidget(self.go_btn)
        
        self.horizontal.addWidget(self.url_bar)
        
        self.browser = QWebEngineView()
        
        self.go_btn.clicked.connect(lambda: self.navigate(self.url_bar.toPlainText()))
        self.back_btn.clicked.connect(self.browser.back)
        self.forward_btn.clicked.connect(self.browser.forward)
        
        self.layout.addLayout(self.horizontal)
        self.layout.addWidget(self.browser)
    
        self.browser.setUrl(QUrl("https://www.google.com"))
        self.setCentralWidget(self.browser)
        self.window.setLayout(self.layout)
        self.window.showMaximized()
        self.window.show()
        
    def navigate(self, url):
        if not url.startswith("https"):
            url = "https://" + url
       
        self.url_bar.setText(url)
        self.browser.setUrl(QUrl(url))
        
        
app = QApplication([])
window = MyWebBrowser()
app.exec_()