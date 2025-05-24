import sys
from PyQt5.QtWidgets import QApplication,QMainWindow,QLabel
from PyQt5.QtGui import QIcon,QFont
from PyQt5.QtCore import Qt
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My Cool First GUI💓")
        self.setGeometry(700,300,500,500)
        self.setWindowIcon(QIcon("moon.jpg"))
        label=QLabel("Hello",self)
        label.setFont(QFont("Arial",30))
        label.setGeometry(0,0,500,100)
        label.setStyleSheet("color:#42e9f5;"
                            "background-color:#f542da;"
                            "font-weight:bold;"
                            "font-style:italic;"
                            "text-decoration:underline;")
        label.setAlignment(Qt.AlignCenter)
def main():
    app=QApplication(sys.argv)
    window=MainWindow()
    window.show()
    sys.exit(app.exec_())
    
if __name__=="__main__":
    main()  
        
        
        