from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWebEngineWidgets import *

class MyWebBrowser(QMainWindow):
    def __init__(self): 
        super(MyWebBrowser, self).__init__()       
        
        self.window = QWidget()
        self.window.setWindowTitle("My Web Browser")
        self.layout = QVBoxLayout()
        self.horizontal = QHBoxLayout()
        
        #create the url bar and use it QLineEdit instead of QTextEdit()
        self.url_bar =  QLineEdit()
        self.url_bar.setMaximumHeight(28)  
        
        # Apply style to the QTextEdit
        self.url_bar.setStyleSheet(
            "QTextEdit { border: 1px solid #ccc; border-radius: 8px; padding: 4px; font-size: 14px; }"
        )
        
        #create the forward button
        self.forward_btn = QPushButton(" --> ")
        self.forward_btn.setMinimumHeight(28)
        self.forward_btn.setStyleSheet(
            "QPushButton { border-radius: 5px; background-color: rgb(200,223,223); }"
            "QPushButton:hover { background-color: #bbb; }"
        )
      
        #create the back button
        self.back_btn = QPushButton(" <-- ")
        self.back_btn.setMinimumHeight(28)
        self.back_btn.setStyleSheet(
            "QPushButton { border-radius: 5px; background-color: rgb(200,223,223); }"
            "QPushButton:hover { background-color: #bbb; }"
        )
        #improve the functionality of the forward and back button by making sure they are disabled when there is no history
        self.browser.pageChanged.connect(self.update_navigation_buttons)

        
        search_icon_path = "images.png"

        # Create a search button
        self.go_btn = QPushButton()
        self.go_btn.setIcon(QIcon(search_icon_path))
        self.go_btn.setMinimumHeight(28)
        self.go_btn.setStyleSheet(
            "QPushButton { border-radius: 5px; background-color: rgb(250,250,250); }"
            "QPushButton:hover { background-color: rgb(170,134,200); }"
        )
        
        #add the refresh button
        self.refresh_btn = QPushButton("Refresh")
        self.refresh_btn.setMinimumHeight(28)
        self.refresh_btn.setStyleSheet(
            "QPushButton { border-radius: 5px; background-color: rgb(200,223,223); }"
            "QPushButton:hover { background-color: #bbb; }"
        )
        self.refresh_btn.clicked.connect(self.browser.reload)
        self.horizontal.addWidget(self.refresh_btn)
        
        
        # Connect returnPressed signal of QTextEdit to slot for go_btn click
        # self.url_bar.returnPressed.connect(self.go_btn.click)
        
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
        
    def update_navigation_buttons(self):
        self.back_btn.setEnabled(self.browser.history().canGoBack())
        self.forward_btn.setEnabled(self.browser.history().canGoForward())
        
           
app = QApplication([])
window = MyWebBrowser()
app.exec_()


# Created by Daniel Osuoha