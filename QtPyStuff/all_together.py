import sys
from PyQt5.QtWidgets import QMainWindow, QTextEdit, QAction
from PyQt5.QtWidgets import QApplication, QWidget, QDesktopWidget
from PyQt5.QtGui import QIcon

class Example(QMainWindow):	
	
	def __init__(self):
		super().__init__()
		self.initUI()
		
	def initUI(self):               
		textEdit = QTextEdit()
		self.setCentralWidget(textEdit)
		exitAction = QAction(QIcon('exit_button.png'), 'Exit', self)
		exitAction.setShortcut('Ctrl+Q')
		exitAction.setStatusTip('Exit application')
		exitAction.triggered.connect(self.close)
		self.statusBar()
		menubar = self.menuBar()
		fileMenu = menubar.addMenu('&File')
		fileMenu.addAction(exitAction)
		menubar.setNativeMenuBar(False) # required for Mac OS
		toolbar = self.addToolBar('Exit')
		toolbar.addAction(exitAction)
		self.setGeometry(300, 300, 350, 250)
		self.setWindowTitle('Main window')
		self.center()    
		self.show()		
		
	def center(self):
		qr = self.frameGeometry()
		cp = QDesktopWidget().availableGeometry().center()
		qr.moveCenter(cp)
		self.move(qr.topLeft())				
		
if __name__ == '__main__':
	app = QApplication(sys.argv)
	ex = Example()
	sys.exit(app.exec_())