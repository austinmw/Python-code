import sys
import os
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QIcon

class Example(QWidget):
	
	# constructor (sorta)
	def __init__(self): 
		super().__init__()
		self.initUI()
		
	# Create the GUI	
	def initUI(self):
		self.setGeometry(300, 300, 300, 220) # combines resize() and move() methods
		self.setWindowTitle('Icon')
		path = os.path.join(os.path.dirname(sys.modules[__name__].__file__), 'web.png')
		app.setWindowIcon(QIcon(path))        
		self.show()
		
		
if __name__ == '__main__':
	app = QApplication(sys.argv)
	ex = Example()
	sys.exit(app.exec_())  

	