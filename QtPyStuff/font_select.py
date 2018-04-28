import sys
from PyQt5.QtWidgets import (QWidget, QVBoxLayout, QPushButton, 
	QSizePolicy, QLabel, QFontDialog, QApplication)


class Example(QWidget):
	
	def __init__(self):
		super().__init__()
		
		self.initUI()
		
		
	def initUI(self):      

		vbox = QVBoxLayout()

		btn = QPushButton('Dialog', self)
		btn.setSizePolicy(QSizePolicy.Fixed,
			QSizePolicy.Fixed)
		
		btn.move(20, 20)

		vbox.addWidget(btn)

		btn.clicked.connect(self.showDialog)
		
		self.lbl = QLabel('Knowledge only matters', self)
		self.lbl.move(130, 20)

		vbox.addWidget(self.lbl)
		self.setLayout(vbox)          
		
		self.setGeometry(300, 300, 250, 180)
		self.setWindowTitle('Font dialog')
		self.show()
		
		
	def showDialog(self):

		font, ok = QFontDialog.getFont()
		if ok:
			self.lbl.setFont(font)
		
		
if __name__ == '__main__':
	
	app = QApplication(sys.argv)
	ex = Example()
	sys.exit(app.exec_())