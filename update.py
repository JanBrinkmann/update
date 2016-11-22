from PySide.QtGui import *
from PySide.QtCore import *
import sys

class WindowStart(QWidget):
    def __init__(self):
        super(WindowStart, self).__init__()
        self.makeWindow()
        self.timerInstall = QTimer(self)
        self.timerInstall.setSingleShot(True)
        self.timerInstall.timeout.connect(self.goback)
        self.timerReminder = QTimer(self)
        self.timerReminder.setSingleShot(True)
        self.timerReminder.timeout.connect(self.nextround)
        self.setStyleSheet("color: white;" "background-color:#313031")

    def makeWindow(self):
        self.setWindowTitle("Update Adobe Flash Player")
        self.setGeometry(500, 500, 700, 400)
        self.introtext = QLabel(self)
        self.introtext.setText("An update for Adobe Flash Player is available. This update enhances usability, online-security and stability and new features were added, that make work for Content Users easier.")
        self.introtext.setFixedSize(400, 100)
        self.introtext.setWordWrap(True)
        self.introtext.move(150,0)
        self.butInstall = QPushButton("INSTALL", self)
        self.butInstall.setStyleSheet("background-color: #5e5e5e")
        self.butInstall.resize(150,40)
        self.butInstall.move(150, 300)
        self.butInstall.clicked.connect(self.install)
        self.butReminder = QPushButton("REMIND ME LATER", self)
        self.butReminder.setStyleSheet("background-color: #5e5e5e")
        self.butReminder.resize(150,40)
        self.butReminder.move(400, 300)
        self.butReminder.clicked.connect(self.reminder)
        pix1 = QPixmap("img/upperleft2.png")
        self.img1 = QLabel(self) # put an image label inside
        self.img1.setPixmap(pix1)
        self.img1.move(30,0)

    def install(self):
        mywin.hide()
        myProgress.show()

    def reminder(self):
        mywin.hide()
        self.timerReminder.start(2000)

    def goback(self):
        mywin.show()

    def nextround(self):
        myError.show()

class WindowError(QWidget):
    def __init__(self):
        super(WindowError, self).__init__()
        self.makeWindow()
        self.timerInstall = QTimer(self)
        self.timerInstall.setSingleShot(True)
        self.timerInstall.timeout.connect(self.goback)
        self.timerReminder = QTimer(self)
        self.timerReminder.setSingleShot(True)
        self.timerReminder.timeout.connect(self.nextround)
        self.setStyleSheet("color: white;" "background-color:#313031")

    def makeWindow(self):
        self.setWindowTitle("Update Adobe Flash Player")
        self.setGeometry(500, 500, 700, 400)
        self.introtext = QLabel(self)
        self.introtext.setText("I am really sorry, but to see this project you need to run the latest version of Flash.")
        self.introtext.setFixedSize(400, 300)
        self.introtext.setWordWrap(True)
        self.introtext.move(150,-100)
        self.butInstall = QPushButton("INSTALL", self)
        self.butInstall.setStyleSheet("background-color: #5e5e5e")
        self.butInstall.resize(150,40)
        self.butInstall.move(150, 300)
        self.butInstall.clicked.connect(self.install)
        self.butReminder = QPushButton("REMIND ME LATER", self)
        self.butReminder.setStyleSheet("background-color: #5e5e5e")
        self.butReminder.resize(150,40)
        self.butReminder.move(400, 300)
        self.butReminder.clicked.connect(self.reminder)
        pix1 = QPixmap("img/upperleft2.png")
        self.img1 = QLabel(self) # put an image label inside
        self.img1.setPixmap(pix1)
        self.img1.move(30,0)

    def install(self):
        myError.hide()
        myProgress.show()

    def reminder(self):
        myError.hide()
        self.timerReminder.start(2000)

    def goback(self):
        mywin.show()

    def nextround(self):
        myFun.show()

class WindowFun(QWidget):
    def __init__(self):
        super(WindowFun, self).__init__()
        self.makeWindow()
        self.setStyleSheet("color: white;" "background-color:#313031")

    def makeWindow(self):
        self.setWindowTitle("Am I too old for you?")
        self.setGeometry(500, 500, 400, 100)
        self.introtext = QLabel(self)
        self.introtext.setText("Have fun with HTML5 then...")
        self.introtext.setFixedSize(300, 50)
        self.introtext.setWordWrap(True)
        self.introtext.move(100,0)
        self.butReminder = QPushButton("Thanks!", self)
        self.butReminder.setStyleSheet("background-color: #5e5e5e")
        self.butReminder.move(100, 50)
        self.butReminder.clicked.connect(self.nextround)

    def nextround(self):
        myPussy.show()
        myFun.hide()

class WindowPussy(QWidget):
    def __init__(self):
        super(WindowPussy, self).__init__()
        self.makeWindow()
        self.timerInstall = QTimer(self)
        self.timerInstall.setSingleShot(True)
        self.timerInstall.timeout.connect(self.nextround)
        self.setStyleSheet("color: white;" "background-color:#313031")

    def makeWindow(self):
        self.setWindowTitle("Nice p0rn is just around the corner!")
        self.setGeometry(500, 500, 759, 500)
        pix1 = QPixmap("img/popup_small.png")
        self.img1 = QLabel(self) # put an image label inside
        self.img1.setPixmap(pix1)
        self.img1.move(0,0)
        self.but = QPushButton("http://www.pussyparadise.rocks", self)
        self.but.clicked.connect(self.nextround)
        self.but.move(300,425)

    def nextround(self):
        myNoPussy.show()



class WindowNoPussy(QWidget):
    def __init__(self):
        super(WindowNoPussy, self).__init__()
        self.makeWindow()
        self.setStyleSheet("color: white;" "background-color:#313031")

    def makeWindow(self):
        self.setWindowTitle("Ooops, something went wrong...")
        self.setGeometry(700, 700, 400, 100)
        self.introtext = QLabel(self)
        self.introtext.setText("You need the newest Flash to watch nice porn...")
        self.introtext.setFixedSize(300, 50)
        self.introtext.setWordWrap(True)
        self.introtext.move(100,0)
        self.but = QPushButton("But I hate Flash!", self)
        self.but.clicked.connect(self.nextround)
        self.but.move(100,50)
        pix1 = QPixmap("img/errorred.png")
        self.img1 = QLabel(self) # put an image label inside
        self.img1.setPixmap(pix1)
        self.img1.move(30,0)

    def nextround(self):
        myCry.show()
        myNoPussy.hide()
        myPussy.hide()

class WindowCry(QWidget):
    def __init__(self):
        super(WindowCry, self).__init__()
        self.makeWindow()
        self.setStyleSheet("color: white;" "background-color:#313031")

    def makeWindow(self):
        self.setWindowTitle("Do you really hate me?")
        self.setGeometry(500, 500, 400, 100)
        self.introtext = QLabel(self)
        self.introtext.setText("I feel unwanted now...")
        self.introtext.setFixedSize(300, 50)
        self.introtext.setWordWrap(True)
        self.introtext.move(100,0)
        self.but = QPushButton("I'm sorry, bro.", self)
        self.but.clicked.connect(self.nextround)
        self.but.move(100,50)

    def nextround(self):
        myImprovement.show()
        myCry.hide()

class WindowImprovement(QWidget):
    def __init__(self):
        super(WindowImprovement, self).__init__()
        self.makeWindow()
        self.setStyleSheet("color: white;" "background-color:#313031")

    def makeWindow(self):
        self.setWindowTitle("I can improve!")
        self.setGeometry(500, 500, 400, 100)
        self.introtext = QLabel(self)
        self.introtext.setText("I will try 11 amazingly easy ways to be better...")
        self.introtext.setFixedSize(300, 50)
        self.introtext.setWordWrap(True)
        self.introtext.move(100,0)
        self.but = QPushButton("Buzzfeed won't help you :/", self)
        self.but.clicked.connect(self.nextround)
        self.but.move(100,50)

    def nextround(self):
        myHelp.show()
        myImprovement.hide()

class WindowHelp(QWidget):
    def __init__(self):
        super(WindowHelp, self).__init__()
        self.makeWindow()
        self.setStyleSheet("color: white;" "background-color:#313031")

    def makeWindow(self):
        self.setWindowTitle("Can you help me?")
        self.setGeometry(500, 500, 400, 100)
        self.introtext = QLabel(self)
        self.introtext.setText("Improving myself is hard. Can you help me?")
        self.introtext.setFixedSize(300, 50)
        self.introtext.setWordWrap(True)
        self.introtext.move(100,0)
        self.but = QPushButton("Just be better.", self)
        self.but.clicked.connect(self.nextround)
        self.but.move(100,50)

    def nextround(self):
        myDead.show()
        myHelp.hide()

class WindowDead(QWidget):
    def __init__(self):
        super(WindowDead, self).__init__()
        self.makeWindow()
        self.setStyleSheet("color: white;" "background-color:#313031")

    def makeWindow(self):
        self.setWindowTitle("You are cruel.")
        self.setGeometry(500, 500, 400, 100)
        self.introtext = QLabel(self)
        self.introtext.setText("I don't know how. Kill me, please.")
        self.introtext.setFixedSize(300, 50)
        self.introtext.setWordWrap(True)
        self.introtext.move(100,0)
        self.but = QPushButton("Uninstall.", self)
        self.but.clicked.connect(self.uninstall)
        self.but.move(100,50)

    def uninstall(self):
        myDead.close()

class ProgressWindow(QWidget):
    def __init__(self):
        super(ProgressWindow, self).__init__()
        self.timerProgress = QTimer(self)
        self.timerProgress.timeout.connect(self.animateFrame)
        self.timerProgress.setSingleShot(True)
        self.makeWindow()
        self.setStyleSheet("color: white;" "background-color:#313031")


    def makeWindow(self):
        self.timerProgress.start(1000)
        self.setWindowTitle("Updating Adobe Flash Player")
        self.setGeometry(500, 500, 400, 100)
        self.progress = QProgressBar(self)
        self.progress.setFixedSize(200,20)
        self.progress.move(100,50)

    def animateFrame(self):

       if self.progress.value() > 90:
           myProgress.hide()
           self.progress.setValue(0)
           mywin.show()

       else:
            x = self.progress.value()
            x = x+20
            self.progress.setValue(x)
            self.timerProgress.start(1000)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mywin = WindowStart()
    myProgress = ProgressWindow()
    myError = WindowError()
    myFun = WindowFun()
    myPussy = WindowPussy()
    myNoPussy = WindowNoPussy()
    myCry = WindowCry()
    myImprovement = WindowImprovement()
    myHelp = WindowHelp()
    myDead = WindowDead()
    mywin.show()
    sys.exit(app.exec_())
