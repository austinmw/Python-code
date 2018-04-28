# Objects created from a QObject can emit signals. In the following example we will see how we can emit custom signals.
# (clicking in window will close program)
import sys
from PyQt5.QtCore import pyqtSignal, QObject
from PyQt5.QtWidgets import QMainWindow, QApplication


class Communicate(QObject):
	
	closeApp = pyqtSignal() 
	

class Example(QMainWindow):
	
	def __init__(self):
		super().__init__()
		
		self.initUI()
		
		
	def initUI(self):      

		self.c = Communicate()
		self.c.closeApp.connect(self.close)       
		
		self.setGeometry(300, 300, 290, 150)
		self.setWindowTitle('Emit signal')
		self.show()
		
		
	def mousePressEvent(self, event):
		
		self.c.closeApp.emit()
		
		
if __name__ == '__main__':
	
	app = QApplication(sys.argv)
	ex = Example()
	sys.exit(app.exec_())