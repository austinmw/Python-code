import sys
from PyQt5.QtWidgets import QApplication, QWidget

# if __name__ == '__main__':
	
app = QApplication(sys.argv)

w = QWidget()
w.resize(250, 150)
w.move(850, 400)
w.setWindowTitle('Simple')
w.show()

sys.exit(app.exec_())  # The event handling starts from this point