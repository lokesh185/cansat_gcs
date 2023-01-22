# this file as telemetry widget and stuff
from QSwitchControl import SwitchControl
from PyQt5 import *
import sys
import os
from random import randint
from plot import graph
from map_plot import mapWidget

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class telemetry_widget(QMainWindow):
    def __init__(self, parent=None):
        super(telemetry_widget, self).__init__(parent)
#gpswidget
    #mapwidget
        self.map = mapWidget()
        self.map.update(17,78)
    #----------------------------------------------------------------------------------
    #telemetry widget
        #cmd
        tele_layout = QGridLayout() 
        self.tele_cmd_textbox =  QLineEdit()
        self.tele_cmd_textbox.setStyleSheet("background-color: black ;border: 0px ;color: white")
        
        
        self.tele_cmd_textbox.returnPressed.connect(self.OnReturnPressed)

        self.tele_widget = QWidget()
        self.tele_widget.setStyleSheet("background-color: #222222")
        tele_layout.addWidget(self.tele_cmd_textbox,1,1,1,4)
        

        self.logOutput = QTextEdit()
        self.logOutput.setReadOnly(True)
        self.logOutput.setStyleSheet("background-color: black ;border: 0px ;color: white")
        self.logOutput.setLineWrapMode(QTextEdit.NoWrap)

        font = self.logOutput.font()
        font.setFamily("Courier")
        font.setPointSize(10)
        tele_layout.addWidget(self.logOutput,2,1,9,5)
        
        self.tele_widget.setLayout(tele_layout)
  


        #twends----------------
        gps_layout = QVBoxLayout()

        # add widgets
        gps_layout.addWidget(self.map)

        gps_layout.addWidget(self.tele_widget)

        self.gps_widget = QWidget()
        self.gps_widget.setLayout(gps_layout)
        self.gps_widget.setMinimumSize(500,400)
        self.gps_widget.setStyleSheet("background-color: black")

        all_layout = QHBoxLayout()

        # add widgets
        all_layout.addWidget(self.MAIN_widget)
        #MAIN_layout.addWidget(self.CONTAINER_widget)``
        all_layout.addWidget(self.gps_widget)
        self.all_widget = QWidget()
        self.all_widget.setLayout(all_layout)
        self.all_widget.setStyleSheet("background-color: black")
        self.setCentralWidget(self.all_widget)




        self.packet_count = 0
        self.number = 0
        self.timer = QTimer()
        self.timer.setInterval(250)
        self.timer.timeout.connect(self.update)
        self.timer.start()

    
    def OnReturnPressed(self):
            """ the text is retrieved from tele_cmd_textbox """
            text = self.tele_cmd_textbox.text()
            # do some thing withit
            self.log_output(text+"\n")

    def log_output(self,text):
            self.logOutput.moveCursor(QTextCursor.End)
            self.logOutput.insertPlainText(text)
            sb = self.logOutput.verticalScrollBar()
            sb.setValue(sb.maximum())

app = QtWidgets.QApplication(sys.argv)
w = MainWindow()
w.show()
sys.exit(app.exec_())