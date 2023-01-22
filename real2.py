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

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, *args, **kwargs):


        super(MainWindow, self).__init__(*args, **kwargs)
        self.window_width, self.window_height=1200,1000
        self.setMinimumSize(self.window_width, self.window_height)
        self.setStyleSheet('''
            QWidget {
                font-size:15px;
            }
        ''')
        #logowidget
        self.logo = QLabel()
        logo_image = QPixmap('./image2.jpg')
        logo_image = logo_image.scaled(300, 300, QtCore.Qt.KeepAspectRatio)
        self.logo.setPixmap(logo_image)
        logo_layout = QVBoxLayout()
        logo_layout.addWidget(self.logo, stretch=1)


        self.logo_widget = QtWidgets.QWidget()
        self.logo_widget.setLayout(logo_layout)
        #self.logo_widget.setStyleSheet("{background-color: rgb(73,73,73)}" )

        #teamwidget
        self.team_label = QLabel('    TEAM ID:1020')
        #self.team_label.setStyleSheet("QLabel{color: #f5fcff; font: 25pt  'Oswald'; background-color: rgb(73,73,73); }")

        team_layout = QVBoxLayout()
        team_layout.addWidget(self.logo, stretch=1)
        team_layout.addWidget(self.team_label)

        self.team_widget = QtWidgets.QWidget()
        self.team_widget.setLayout(team_layout)
        #self.team_widget.setFixedWidth(320)
        #self.team_widget.setStyleSheet("QLabel{color: #f5fcff; font: 25pt  'Oswald'; background-color: rgb(0,0,0); }")
        #self.team_widget.setFixedHeight(70)



        #team+logowidget

        MENU1_layout = QVBoxLayout()
        MENU1_layout.addWidget(self.logo_widget)
        MENU1_layout.addWidget(self.team_widget)

        self.MENU1_widget = QtWidgets.QWidget()
        self.MENU1_widget.setLayout(MENU1_layout)
        self.MENU1_widget.setFixedWidth(330)
        self.MENU1_widget.setFixedHeight(230)
        self.MENU1_widget.setStyleSheet("QLabel{color: #f5fcff; font: 25pt  'Oswald'; background-color: rgb(0,0,0); }")

        #missiontime widgets
        self.MENU2_mission_time = QLabel('Mission Time:')
        MENU2_layout = QVBoxLayout()
        MENU2_layout.addWidget(self.MENU2_mission_time)
        self.MENU2_widget = QtWidgets.QWidget()
        self.MENU2_widget.setLayout(MENU2_layout)
        self.MENU2_widget.setFixedWidth(1050)
        self.MENU2_widget.setFixedHeight(70)
        self.MENU2_widget.setStyleSheet("QLabel{color: #f5fcff; font: 20pt  'Oswald';background-color: rgb(31,31,31); } ")

        #simulation file widgets
        self.SIMULATION_FILE = QLabel('SIMULATION_FILE:')
        SIMULATION_FILE_layout = QHBoxLayout()
        SIMULATION_FILE_layout.addWidget(self.SIMULATION_FILE)
        self.SIMULATION_FILE_widget = QtWidgets.QWidget()
        self.SIMULATION_FILE_widget.setLayout(SIMULATION_FILE_layout)
        self.SIMULATION_FILE_widget.setFixedWidth(170)
        self.SIMULATION_FILE_widget.setFixedHeight(50)
        self.SIMULATION_FILE_widget.setStyleSheet("QLabel{color: #f5fcff; font: 10pt  'Oswald';background-color: rgb(20,20,20); } ")


        #simulation file uploadwidgets
        self.upload =  QtWidgets.QPushButton("UPLOAD")
        self.upload.setStyleSheet("QPushButton{ background-color: white ; color: black; font: 5pt  'Oswald';}")
        upload_layout = QHBoxLayout()
        upload_layout.addWidget(self.upload)

        self.upload_widget = QtWidgets.QWidget()
        self.upload_widget.setLayout(upload_layout)
        self.upload_widget.setFixedWidth(60)
        self.upload_widget.setFixedHeight(40)

        #menu4
        MENU4_layout = QHBoxLayout()
        MENU4_layout.addWidget(self.SIMULATION_FILE_widget)
        MENU4_layout.addWidget(self.upload_widget)

        self.MENU4_widget = QtWidgets.QWidget()
        self.MENU4_widget.setLayout(MENU4_layout)
        self.MENU4_widget.setStyleSheet("QWidget{background-color:rgb(30,30,30)}")

        #spee port widgets
        self.XBEEPORT = QLabel('XBEEPORT:')
        XBEEPORT_layout = QHBoxLayout()
        XBEEPORT_layout.addWidget(self.XBEEPORT)
        self.XBEEPORT_widget = QtWidgets.QWidget()
        self.XBEEPORT_widget.setLayout(XBEEPORT_layout)
        self.XBEEPORT_widget.setFixedWidth(170)
        self.XBEEPORT_widget.setFixedHeight(50)
        self.XBEEPORT_widget.setStyleSheet("QLabel{color: #f5fcff; font: 10pt  'Oswald';background-color: rgb(20,20,20); } ")


        #spee port combo box widgets
        self.XBEEPORT_combo_box = QComboBox()
        XBEEPORT_combo_box_list = ["COM3", "COM5"]
        self.XBEEPORT_combo_box.addItems(XBEEPORT_combo_box_list)
        self.XBEEPORT_combo_box.setEditable(True)
        self.XBEEPORT_combo_box.setInsertPolicy(QComboBox.NoInsert)
        self.XBEEPORT_combo_box.setStyleSheet("QComboBox{ background-color: white ; color: black;}")
        XBEEPORT_combo_box_layout = QHBoxLayout()
        XBEEPORT_combo_box_layout.addWidget(self.XBEEPORT_combo_box)


        self.XBEEPORT_combo_box_widget = QtWidgets.QWidget()
        self.XBEEPORT_combo_box_widget.setLayout(XBEEPORT_combo_box_layout)
        self.XBEEPORT_combo_box_widget.setFixedWidth(100)
        self.XBEEPORT_combo_box_widget.setFixedHeight(50)


        #menu3
        MENU3_layout = QHBoxLayout()
        MENU3_layout.addWidget(self.XBEEPORT_widget)
        MENU3_layout.addWidget(self.XBEEPORT_combo_box_widget)


        self.MENU3_widget = QtWidgets.QWidget()
        self.MENU3_widget.setLayout(MENU3_layout)
        self.MENU3_widget.setStyleSheet("QWidget{background-color:rgb(30,30,30)}")


        #state widgets
        self.state = QLabel('State:')
        #self.state.setStyleSheet("QLabel{color: #f5fcff; font: 13pt  'Oswald';background-color: rgb(73,73,73); }")
        state_layout = QHBoxLayout()
        state_layout.addWidget(self.state)
        self.state_widget = QtWidgets.QWidget()
        self.state_widget.setFixedWidth(100)
        self.state_widget.setStyleSheet("QLabel{color: #f5fcff; font: 13pt  'Oswald';background-color: rgb(20,20,20); }")
        self.state_widget.setLayout(state_layout)
        #mode widgets
        self.mode = QLabel('Mode:')
        #self.mode.setStyleSheet("QLabel{color: #f5fcff; font: 13pt  'Oswald';background-color: rgb(73,73,73); }")
        mode_layout = QHBoxLayout()
        mode_layout.addWidget(self.mode)
        self.mode_widget = QtWidgets.QWidget()
        self.mode_widget.setFixedWidth(100)
        self.mode_widget.setStyleSheet("QLabel{color: #f5fcff; font: 13pt  'Oswald';background-color: rgb(20,20,20); }")
        self.mode_widget.setLayout(mode_layout)

        #simulationfile h xbee portwidgets
        MENU6_layout = QHBoxLayout()
        MENU6_layout.addWidget(self.MENU4_widget)
        MENU6_layout.addWidget(self.MENU3_widget)


        self.MENU6_widget = QtWidgets.QWidget()
        self.MENU6_widget.setLayout(MENU6_layout)

        #state port h mode widgets

        MENU5_layout = QHBoxLayout()
        MENU5_layout.addWidget(self.state_widget)
        MENU5_layout.addWidget(self.mode_widget)


        self.MENU5_widget = QtWidgets.QWidget()
        self.MENU5_widget.setLayout(MENU5_layout)
        self.MENU5_widget.setStyleSheet("QWidget{background-color:rgb(30,30,30)}")

        #sfhs v xphm widgets
        MENU7_layout = QVBoxLayout()
        MENU7_layout.addWidget(self.MENU6_widget)
        MENU7_layout.addWidget(self.MENU5_widget)


        self.MENU7_widget = QtWidgets.QWidget()
        self.MENU7_widget.setLayout(MENU7_layout)

        #combination of all these QtWidgets
        MENU8_layout = QVBoxLayout()
        MENU8_layout.addWidget(self.MENU2_widget)
        MENU8_layout.addWidget(self.MENU7_widget)


        self.MENU8_widget = QtWidgets.QWidget()
        self.MENU8_widget.setLayout(MENU8_layout)
        self.MENU8_widget.setStyleSheet("QWidget{background-color:rgb(20,20,20)}")


        MENU9_layout = QHBoxLayout()
        MENU9_layout.addWidget(self.MENU1_widget)
        MENU9_layout.addWidget(self.MENU8_widget)


        self.MENU9_widget = QtWidgets.QWidget()
        self.MENU9_widget.setLayout(MENU9_layout)
        self.MENU9_widget.setFixedHeight(300)

        #button widgets
        #heaat shield widgets
        self.dot1= QLabel('                                        •')
        self.HS=QLabel('Heat Shield deployed')
        self.dot1.setStyleSheet("QLabel{color: rgb(255,0,13)}")
        self.HS.setStyleSheet("QLabel{color: #f5fcff; font: 11pt  'Oswald';background-color: rgb(31,31,31); }")

        HS_layout=QHBoxLayout()
        HS_layout.addWidget(self.dot1)
        HS_layout.addWidget(self.HS)
        self.HS_layout_widget = QtWidgets.QWidget()
        self.HS_layout_widget.setLayout(HS_layout)
        self.HS_layout_widget.setFixedHeight(60)
        #parachute widgets
        self.PC=QLabel('Parachute deployed')
        self.dot2= QLabel('                                        •')
        self.dot2.setStyleSheet("QLabel{color: rgb(255,0,13)}")
        self.PC.setStyleSheet("QLabel{color: #f5fcff; font: 11pt  'Oswald';background-color: rgb(31,31,31); }")

        PC_layout=QHBoxLayout()
        PC_layout.addWidget(self.dot2)
        PC_layout.addWidget(self.PC)
        self.PC_layout_widget = QtWidgets.QWidget()
        self.PC_layout_widget.setLayout(PC_layout)
        self.PC_layout_widget.setFixedHeight(60)


        #mast raised widgets
        self.mast=QLabel('Mast raised')
        self.dot3= QLabel('                                        •')
        self.dot3.setStyleSheet("QLabel{color: rgb(255,0,13)}")
        self.mast.setStyleSheet("QLabel{color: #f5fcff; font: 11pt  'Oswald';background-color: rgb(31,31,31); }")

        mast_layout=QHBoxLayout()
        mast_layout.addWidget(self.dot3)
        mast_layout.addWidget(self.mast)
        self.mast_layout_widget = QtWidgets.QWidget()
        self.mast_layout_widget.setLayout(mast_layout)
        self.mast_layout_widget.setFixedHeight(60)


        #all three widget
        states_layout=QHBoxLayout()

        states_layout.addWidget(self.HS_layout_widget)
        states_layout.addWidget(self.PC_layout_widget)
        states_layout.addWidget(self.mast_layout_widget)

        self.states_widget = QtWidgets.QWidget()
        self.states_widget.setLayout(states_layout)
        self.states_widget.setStyleSheet("QWidget{background-color: rgb(20,20,20); }")
        self.states_widget.setFixedHeight(70)
        #telemtry button widget
        self.telemetry= QtWidgets.QPushButton("Telemetry")
        self.telemetry.setText("Telemetry")
        self.telemetry.setStyleSheet("QPushButton{color: #f5fcff; font: 10pt  'Oswald';background-color: rgb(3,0,13); }")

        telemetry_layout=QHBoxLayout()

        telemetry_layout.addWidget(self.telemetry)

        self.telemetry_widget = QtWidgets.QWidget()
        self.telemetry_widget.setLayout(telemetry_layout)
        self.telemetry_widget.setFixedHeight(60)
        #cal button widgets
        self.cal= QtWidgets.QPushButton("cal")
        self.cal.setText("cal")
        self.cal.setStyleSheet("QPushButton{color: #f5fcff; font: 10pt  'Oswald';background-color: rgb(3,0,13); }")

        cal_layout=QHBoxLayout()

        cal_layout.addWidget(self.cal)

        self.cal_widget = QtWidgets.QWidget()
        self.cal_widget.setLayout(cal_layout)
        self.cal_widget.setFixedHeight(60)

        #set itme widget

        self.set_time= QtWidgets.QPushButton("set_time")
        self.set_time.setText("set_time")
        self.set_time.setStyleSheet("QPushButton{color: #f5fcff; font: 10pt  'Oswald';background-color: rgb(3,0,13); }")

        set_time_layout=QHBoxLayout()

        set_time_layout.addWidget(self.set_time)

        self.set_time_widget = QtWidgets.QWidget()
        self.set_time_widget.setLayout(set_time_layout)
        self.set_time_widget.setFixedHeight(60)

        #wiget for top three
        button_layout=QHBoxLayout()
        button_layout.addWidget(self.telemetry_widget)
        button_layout.addWidget(self.cal_widget)
        button_layout.addWidget(self.set_time_widget)

        self.button_widget = QtWidgets.QWidget()
        self.button_widget.setLayout(button_layout)
        self.button_widget.setFixedHeight(70)
        self.button_widget.setStyleSheet("QWidget{background-color: rgb(20,20,20); }")

        #graph widgets
        # graph1
        self.graphPressure_name= QLabel('    Pressure')
        self.graphPressure_name.setStyleSheet("QLabel{color: #f5fcff; font: 10pt  'Oswald';background-color: rgb(20,20,20); }")
        self.line1= QLabel('  ')
        self.line1.setFixedWidth(7)
        self.line1.setFixedHeight(30)
        self.line1.setStyleSheet("QLabel{background-color: rgb(59, 146, 184)}")
        graphPressure_name_layout = QHBoxLayout()
        graphPressure_name_layout.addWidget(self.line1)
        graphPressure_name_layout.addWidget(self.graphPressure_name)
        self.graphPressure_name_widget = QtWidgets.QWidget()
        self.graphPressure_name_widget.setLayout(graphPressure_name_layout)

        self.graphPressure1 = graph([
        	{
        		"color": (0, 0, 255),
        		"name": "Pressure"
        	}], True, 200, "", "Pressure ")

        graphPressure_Layout = QVBoxLayout()
        graphPressure_Layout.addWidget(self.graphPressure_name_widget)
        graphPressure_Layout.addWidget(self.graphPressure1.graphWidget)
        self.graphPressure = QtWidgets.QWidget()
        self.graphPressure.setLayout(graphPressure_Layout)
        self.graphPressure.setStyleSheet("QLabel{color: #f5fcff; font: 10pt  'Oswald';background-color: rgb(3,0,13); }")




        self.graphTemperature_name= QLabel('    Temperature')
        self.graphTemperature_name.setStyleSheet("QLabel{color: #f5fcff; font: 10pt  'Oswald';background-color: rgb(20,20,20); }")
        self.line2= QLabel('  ')
        self.line2.setFixedWidth(7)
        self.line2.setFixedHeight(30)
        self.line2.setStyleSheet("QLabel{background-color: rgb(59, 146, 184)}")
        graphTemperature_name_layout = QHBoxLayout()
        graphTemperature_name_layout.addWidget(self.line2)
        graphTemperature_name_layout.addWidget(self.graphTemperature_name)
        self.graphTemperature_name_widget = QtWidgets.QWidget()
        self.graphTemperature_name_widget.setLayout(graphTemperature_name_layout)

        self.graphTemperature1 = graph([
        	{
        		"color": (0, 0, 255),
        		"name": "Temperature"
        	}], True, 200, "", "Temperature ")

        graphTemperature_Layout = QVBoxLayout()
        graphTemperature_Layout.addWidget(self.graphTemperature_name_widget)
        graphTemperature_Layout.addWidget(self.graphTemperature1.graphWidget)
        self.graphTemperature = QtWidgets.QWidget()
        self.graphTemperature.setLayout(graphTemperature_Layout)
        self.graphTemperature.setStyleSheet("QLabel{color: #f5fcff; font: 10pt  'Oswald';background-color: rgb(3,0,13); }")

        self.graphAltitude_name= QLabel('    Altitude')
        self.graphAltitude_name.setStyleSheet("QLabel{color: #f5fcff; font: 10pt  'Oswald';background-color: rgb(20,20,20); }")
        self.line3= QLabel('  ')
        self.line3.setFixedWidth(7)
        self.line3.setFixedHeight(30)
        self.line3.setStyleSheet("QLabel{background-color: rgb(59, 146, 184)}")
        graphAltitude_name_layout = QHBoxLayout()
        graphAltitude_name_layout.addWidget(self.line3)
        graphAltitude_name_layout.addWidget(self.graphAltitude_name)
        self.graphAltitude_name_widget = QtWidgets.QWidget()
        self.graphAltitude_name_widget.setLayout(graphAltitude_name_layout)

        self.graphAltitude1 = graph([
        	{
        		"color": (0, 0, 255),
        		"name": "Altitude"
        	}], True, 200, "", "Altitude ")

        graphAltitude_Layout = QVBoxLayout()
        graphAltitude_Layout.addWidget(self.graphAltitude_name_widget)
        graphAltitude_Layout.addWidget(self.graphAltitude1.graphWidget)
        self.graphAltitude = QtWidgets.QWidget()
        self.graphAltitude.setLayout(graphAltitude_Layout)
        self.graphAltitude.setStyleSheet("QLabel{color: #f5fcff; font: 12pt  'Oswald';background-color: rgb(3,0,13); }")
        GRAPH1_layout = QHBoxLayout()
        #PAYLOAD_layout.addWidget(self.PAYLOAD_label)
        GRAPH1_layout.addWidget(self.graphPressure)
        GRAPH1_layout.addWidget(self.graphTemperature)
        GRAPH1_layout.addWidget(self.graphAltitude)



        self.GRAPH1_widget = QtWidgets.QWidget()
        self.GRAPH1_widget.setLayout(GRAPH1_layout)


        self.GRAPH1_widget.setStyleSheet("background-color: rgb(30,30,30)")
        #self.GRAPH1_widget.setStyleSheet("background-color: white")

#----------------------------------------------------------------------------------------
#GRAPH2

        self.graphVoltage_name= QLabel('    Voltage')
        self.graphVoltage_name.setStyleSheet("QLabel{color: #f5fcff; font: 10pt  'Oswald';background-color: rgb(20,20,20); }")
        self.line1= QLabel('  ')
        self.line1.setFixedWidth(7)
        self.line1.setFixedHeight(30)
        self.line1.setStyleSheet("QLabel{background-color: rgb(59, 146, 184)}")
        graphVoltage_name_layout = QHBoxLayout()
        graphVoltage_name_layout.addWidget(self.line1)
        graphVoltage_name_layout.addWidget(self.graphVoltage_name)
        self.graphVoltage_name_widget = QtWidgets.QWidget()
        self.graphVoltage_name_widget.setLayout(graphVoltage_name_layout)

        self.graphVoltage1 = graph([
        	{
        		"color": (0, 0, 255),
        		"name": "Voltage"
        	}], True, 200, "", "Voltage ")

        graphVoltage_Layout = QVBoxLayout()
        graphVoltage_Layout.addWidget(self.graphVoltage_name_widget)
        graphVoltage_Layout.addWidget(self.graphVoltage1.graphWidget)
        self.graphVoltage = QtWidgets.QWidget()
        self.graphVoltage.setLayout(graphVoltage_Layout)
        self.graphVoltage.setStyleSheet("QLabel{color: #f5fcff; font: 10pt  'Oswald';background-color: rgb(3,0,13); }")




        self.graphGPS_Altitude_name= QLabel('    GPS_Altitude')
        self.graphGPS_Altitude_name.setStyleSheet("QLabel{color: #f5fcff; font: 10pt  'Oswald';background-color: rgb(20,20,20); }")
        self.line2= QLabel('  ')
        self.line2.setFixedWidth(7)
        self.line2.setFixedHeight(30)
        self.line2.setStyleSheet("QLabel{background-color: rgb(59, 146, 184)}")
        graphGPS_Altitude_name_layout = QHBoxLayout()
        graphGPS_Altitude_name_layout.addWidget(self.line2)
        graphGPS_Altitude_name_layout.addWidget(self.graphGPS_Altitude_name)
        self.graphGPS_Altitude_name_widget = QtWidgets.QWidget()
        self.graphGPS_Altitude_name_widget.setLayout(graphGPS_Altitude_name_layout)

        self.graphGPS_Altitude1 = graph([
        	{
        		"color": (0, 0, 255),
        		"name": "GPS_Altitude"
        	}], True, 200, "", "GPS_Altitude ")

        graphGPS_Altitude_Layout = QVBoxLayout()
        graphGPS_Altitude_Layout.addWidget(self.graphGPS_Altitude_name_widget)
        graphGPS_Altitude_Layout.addWidget(self.graphGPS_Altitude1.graphWidget)
        self.graphGPS_Altitude = QtWidgets.QWidget()
        self.graphGPS_Altitude.setLayout(graphGPS_Altitude_Layout)
        self.graphGPS_Altitude.setStyleSheet("QLabel{color: #f5fcff; font: 10pt  'Oswald';background-color: rgb(3,0,13); }")

        self.graphTilt_XY_name= QLabel('    Tilt_XY')
        self.graphTilt_XY_name.setStyleSheet("QLabel{color: #f5fcff; font: 10pt  'Oswald';background-color: rgb(20,20,20); }")
        self.line3= QLabel('  ')
        self.line3.setFixedWidth(7)
        self.line3.setFixedHeight(30)
        self.line3.setStyleSheet("QLabel{background-color: rgb(59, 146, 184)}")
        graphTilt_XY_name_layout = QHBoxLayout()
        graphTilt_XY_name_layout.addWidget(self.line3)
        graphTilt_XY_name_layout.addWidget(self.graphTilt_XY_name)
        self.graphTilt_XY_name_widget = QtWidgets.QWidget()
        self.graphTilt_XY_name_widget.setLayout(graphTilt_XY_name_layout)

        self.graphTilt_XY1 = graph([
        	{
        		"color": (0, 0, 255),
        		"name": "Tilt_XY"
        	}], True, 200, "", "Tilt_XY ")

        graphTilt_XY_Layout = QVBoxLayout()
        graphTilt_XY_Layout.addWidget(self.graphTilt_XY_name_widget)
        graphTilt_XY_Layout.addWidget(self.graphTilt_XY1.graphWidget)
        self.graphTilt_XY = QtWidgets.QWidget()
        self.graphTilt_XY.setLayout(graphTilt_XY_Layout)
        self.graphTilt_XY.setStyleSheet("QLabel{color: #f5fcff; font: 10pt  'Oswald';background-color: rgb(3,0,13); }")


        GRAPH2_layout = QHBoxLayout()
        #PAYLOAD_layout.addWidget(self.PAYLOAD_label)
        GRAPH2_layout.addWidget(self.graphVoltage)
        GRAPH2_layout.addWidget(self.graphGPS_Altitude)
        GRAPH2_layout.addWidget(self.graphTilt_XY)



        self.GRAPH2_widget = QtWidgets.QWidget()
        self.GRAPH2_widget.setLayout(GRAPH2_layout)
        self.GRAPH2_widget.setStyleSheet("background-color: rgb(30,30,30)")

        graph_layout = QVBoxLayout()
        graph_layout.addWidget(self.GRAPH2_widget)
        graph_layout.addWidget(self.GRAPH1_widget)

        self.graph_widget = QtWidgets.QWidget()
        self.graph_widget.setLayout(graph_layout)

        #gps widgets
        self.map = mapWidget()
        self.map.update(17,78)

        #telemtry widget
        self.tele_cmd = QLabel('tele_cmd:')
        self.tele_text= QLabel('tele_text')
        tele_layout = QVBoxLayout()
        tele_layout.addWidget(self.tele_cmd)
        tele_layout.addWidget(self.tele_text)


        self.tele_widget = QtWidgets.QWidget()
        self.tele_widget.setLayout(tele_layout)
        self.tele_widget.setStyleSheet("background-color: #005975")

        #twends
        gps_layout = QVBoxLayout()

        # add widgets
        gps_layout.addWidget(self.map)

        gps_layout.addWidget(self.tele_widget)

        self.gps_widget = QtWidgets.QWidget()
        self.gps_widget.setLayout(gps_layout)
        self.gps_widget.setMinimumSize(500,400)
        self.gps_widget.setStyleSheet("background-color: black")


        #main window
        MAIN_layout = QVBoxLayout()

        # add widgets
        MAIN_layout.addWidget(self.MENU9_widget)
        MAIN_layout.addWidget(self.states_widget)
        MAIN_layout.addWidget(self.button_widget)
        #MAIN_layout.addWidget(self.CONTAINER_widget)``
        MAIN_layout.addWidget(self.graph_widget)
        self.MAIN_widget = QtWidgets.QWidget()
        self.MAIN_widget.setLayout(MAIN_layout)


        #all layout
        all_layout = QHBoxLayout()

        # add widgets
        all_layout.addWidget(self.MAIN_widget)
        #MAIN_layout.addWidget(self.CONTAINER_widget)``
        all_layout.addWidget(self.gps_widget)
        self.all_widget = QtWidgets.QWidget()
        self.all_widget.setLayout(all_layout)
        self.all_widget.setStyleSheet("background-color: black")
        self.setCentralWidget(self.all_widget)


app = QtWidgets.QApplication(sys.argv)
w = MainWindow()
w.show()
sys.exit(app.exec_())
