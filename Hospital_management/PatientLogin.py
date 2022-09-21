from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3
from PyQt5.QtWidgets import QMessageBox

class Patient_Login( object ):
    
    def ShowAppointments(self):
        db = sqlite3.connect( "project.db" )
        
        r = db.execute( "select Email from SaveEmails" )
        list = [] 
        
        for RowNum, RowData in enumerate( r ):
            for columnNum, columnData in enumerate( RowData ):
                list.append( columnData )
        
        result = db.execute( "select * from Appointments where Email= " + "'" + list[0] + "'" )
        
        self.tableWidgetAppointment.setRowCount( 0 )
        for RowNum, RowData in enumerate( result ):
            self.tableWidgetAppointment.insertRow( RowNum )
            for columnNum, columnData in enumerate( RowData ):
                self.tableWidgetAppointment.setItem( RowNum, columnNum, QtWidgets.QTableWidgetItem( str( columnData ) ) )


        db.close()
    
    def DeleteAppointment(self):
        
        FullName = self.FullName.text()
        db = sqlite3.connect( "project.db" )
        db.execute(
            "delete from Appointments where FullName=" + "'" + FullName + "'")
        db.commit()
        message1 = QMessageBox()
        message1.setWindowTitle( "Successfull" )
        message1.setInformativeText( "Vous avez réussi à supprimer votre rendez-vous" )
        x = message1.exec_()
        
        result = db.execute( "select * from Appointments where FullName= " + "'" + FullName + "'" )
        self.tableWidgetAppointment.setRowCount( 0 )
        
        for RowNum, RowDATA in enumerate( result ):
            self.tableWidgetAppointment.insertRow( RowNum )
            for ColumnNum, ColumnData in enumerate( RowDATA ):
                self.tableWidgetAppointment.setItem( RowNum, ColumnNum,
                                                     QtWidgets.QTableWidgetItem( str( ColumnData ) ) )
        
        db.close()
        self.FullName.clear()
        self.Age.clear()
        self.Phone.clear()
        self.Gender.setCurrentText("")
        self.MedicalCondition.clear()
        self.Email.clear()
        self.PreferDay.setCurrentText("")
    
    def UpdateAppointment(self):
        
        FullName = self.FullName.text()
        Age = self.Age.text()
        Phone = self.Phone.text()
        Gender = self.Gender.currentText()
        MedicalCondition = self.MedicalCondition.text()
        Email = self.Email.text()
        Day = self.PreferDay.currentText()
        Time = self.timeEdit.text()
        db = sqlite3.connect( "project.db" )
        
        db.execute( "update Appointments set FullName =?, Age =?, Phone =?, Gender =?, MedicalCondition =?, Day =?, Time =?, Email =? where FullName="+"'"+FullName+"'",
                    (FullName, Age, Phone, Gender, MedicalCondition, Day, Time, Email) )
        db.commit()
        message1 = QMessageBox()
        message1.setWindowTitle( "Successfull" )
        message1.setInformativeText( "Vous avez mis à jour votre rendez-vous avec succès")
        x = message1.exec_()
    
    def MakeAppointment(self):
        
        AppStatus = ""
        FullName = self.FullName.text()
        Age = self.Age.text()
        Phone = self.Phone.text()
        Gender = self.Gender.currentText()
        MedicalCondition = self.MedicalCondition.text()
        Email = self.Email.text()
        Day = self.PreferDay.currentText()
        Time = self.timeEdit.text()
        db = sqlite3.connect("project.db")
        db.execute("create table if not exists Appointments (AppStatus text, FullName text, Age int, Phone int, Gender text, MedicalCondition text, Day text, Time text, Email text)")
        db.execute("insert into Appointments values(?,?,?,?,?,?,?,?,?)", (AppStatus, FullName, Age, Phone, Gender, MedicalCondition, Day, Time, Email))
        db.commit()
        message1 = QMessageBox()
        message1.setWindowTitle( "Successfull" )
        message1.setInformativeText( "Vous avez réussi à créer un rendez-vous pour " + Day )
        x = message1.exec_()
    
    def ViewPatientInfo(self):
        db = sqlite3.connect("project.db")
        
        r= db.execute("select Email from SaveEmails")
        list = [] 
        for RowNum, RowDATA in enumerate( r ):
            for ColumnNum, ColumnData in enumerate( RowDATA ):
                list.append(ColumnData)
        
        result = db.execute( "select * from PatientInformation where email="+"'"+list[0]+"'" )
        self.tableWidgetPatientInfo.setRowCount( 0 )
        
        for RowNum, RowDATA in enumerate( result ):
            self.tableWidgetPatientInfo.insertRow( RowNum )
            for ColumnNum, ColumnData in enumerate( RowDATA ):
                self.tableWidgetPatientInfo.setItem( RowNum, ColumnNum, QtWidgets.QTableWidgetItem( str( ColumnData ) ) )
        db.close()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName( "MainWindowAdmin" )
        MainWindow.resize( 702, 566 )
        self.centralwidget = QtWidgets.QWidget( MainWindow )
        self.centralwidget.setObjectName( "centralwidget" )
        self.AppointmentButton = QtWidgets.QPushButton( self.centralwidget )
        self.AppointmentButton.setGeometry( QtCore.QRect( 470, 460, 131, 31 ) )
        font = QtGui.QFont()
        font.setFamily( "Segoe UI Semibold" )
        font.setPointSize( 9 )
        font.setBold( True )
        font.setWeight( 75 )
        self.AppointmentButton.setFont( font )
        self.AppointmentButton.setStyleSheet( "background-color: rgb(85, 170, 255);" )
        self.AppointmentButton.setObjectName( "AppointmentButton" )
        self.AppointmentButton.clicked.connect( self.MakeAppointment )

        self.label_2 = QtWidgets.QLabel( self.centralwidget )
        self.label_2.setGeometry( QtCore.QRect(270, 0, 311, 160) )
        self.label_2.setText( "" )
        self.label_2.setPixmap( QtGui.QPixmap( "Logo.png" ) )
        self.label_2.setObjectName( "label_2" )
        self.label_3 = QtWidgets.QLabel( self.centralwidget )
        self.label_3.setGeometry( QtCore.QRect( 10, 139, 131, 20 ) )
        font = QtGui.QFont()
        font.setFamily( "Segoe Print" )
        font.setPointSize( 10 )
        self.label_3.setFont( font )
        self.label_3.setObjectName( "label_3" )
        self.label_4 = QtWidgets.QLabel( self.centralwidget )
        self.label_4.setGeometry( QtCore.QRect( 8, 280, 141, 20 ) )
        font = QtGui.QFont()
        font.setFamily( "Segoe Print" )
        font.setPointSize( 10 )
        self.label_4.setFont( font )
        self.label_4.setObjectName( "label_4" )
        self.tableWidgetPatientInfo = QtWidgets.QTableWidget( self.centralwidget )
        self.tableWidgetPatientInfo.setGeometry( QtCore.QRect( 0, 170, 701, 91 ) )
        self.tableWidgetPatientInfo.setObjectName( "tableWidgetPatientInfo" )
        self.tableWidgetPatientInfo.setColumnCount( 8 )
        self.tableWidgetPatientInfo.setRowCount( 0 )
        item = QtWidgets.QTableWidgetItem()
        item.setBackground( QtGui.QColor( 85, 170, 255 ) )
        self.tableWidgetPatientInfo.setHorizontalHeaderItem( 0, item )
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetPatientInfo.setHorizontalHeaderItem( 1, item )
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetPatientInfo.setHorizontalHeaderItem( 2, item )
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetPatientInfo.setHorizontalHeaderItem( 3, item )
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetPatientInfo.setHorizontalHeaderItem( 4, item )
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetPatientInfo.setHorizontalHeaderItem( 5, item )
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetPatientInfo.setHorizontalHeaderItem( 6, item )
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetPatientInfo.setHorizontalHeaderItem( 7, item )
        self.tableWidgetAppointment = QtWidgets.QTableWidget( self.centralwidget )
        self.tableWidgetAppointment.setGeometry( QtCore.QRect( 0, 310, 701, 91 ) )
        self.tableWidgetAppointment.setObjectName( "tableWidgetAppointment" )
        self.tableWidgetAppointment.setColumnCount( 9 )
        self.tableWidgetAppointment.setRowCount( 0 )
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetAppointment.setHorizontalHeaderItem( 0, item )
        item = QtWidgets.QTableWidgetItem()
        item.setBackground( QtGui.QColor( 85, 170, 255 ) )
        self.tableWidgetAppointment.setHorizontalHeaderItem( 1, item )
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetAppointment.setHorizontalHeaderItem( 2, item )
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetAppointment.setHorizontalHeaderItem( 3, item )
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetAppointment.setHorizontalHeaderItem( 4, item )
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetAppointment.setHorizontalHeaderItem( 5, item )
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetAppointment.setHorizontalHeaderItem( 6, item )
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetAppointment.setHorizontalHeaderItem( 7, item )
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetAppointment.setHorizontalHeaderItem( 8, item )

        self.ShowApButton = QtWidgets.QPushButton( self.centralwidget )
        self.ShowApButton.setGeometry( QtCore.QRect( 568, 270, 131, 31 ) )
        font = QtGui.QFont()
        font.setFamily( "Segoe UI Semibold" )
        font.setPointSize( 9 )
        font.setBold( True )
        font.setWeight( 75 )
        self.ShowApButton.setFont( font )
        self.ShowApButton.setStyleSheet( "background-color: rgb(85, 170, 255);" )
        self.ShowApButton.setObjectName( "ShowApButton" )
        self.ShowApButton.clicked.connect(self.ShowAppointments)

        self.ShowInfoButton = QtWidgets.QPushButton( self.centralwidget )
        self.ShowInfoButton.setGeometry( QtCore.QRect( 550, 131, 140, 31 ) )
        font = QtGui.QFont()
        font.setFamily( "Segoe UI Semibold" )
        font.setPointSize( 9 )
        font.setBold( True )
        font.setWeight( 75 )
        self.ShowInfoButton.setFont( font )
        self.ShowInfoButton.setStyleSheet( "background-color: rgb(85, 170, 255);" )
        self.ShowInfoButton.setObjectName( "ShowInfoButton" )
        self.ShowInfoButton.clicked.connect( self.ViewPatientInfo )
        self.LogOutButton = QtWidgets.QPushButton( self.centralwidget )
        self.LogOutButton.setGeometry( QtCore.QRect( 15, 15, 91, 31 ) )
        font = QtGui.QFont()
        font.setFamily( "Segoe UI Semibold" )
        font.setPointSize( 9 )
        font.setBold( True )
        font.setWeight( 75 )
        self.LogOutButton.setFont( font )
        self.LogOutButton.setStyleSheet( "background-color: rgb(85, 170, 255);" )
        self.LogOutButton.setObjectName( "LogOutB" )
        self.LogOutButton.clicked.connect(QtWidgets.qApp.quit)
        self.label = QtWidgets.QLabel( self.centralwidget )
        self.label.setGeometry( QtCore.QRect( 10, 420 , 91, 16 ) )
        font = QtGui.QFont()
        font.setFamily( "Segoe Print" )
        font.setPointSize( 8 )
        self.label.setFont( font )
        self.label.setObjectName( "label" )
        self.label_5 = QtWidgets.QLabel( self.centralwidget )
        self.label_5.setGeometry( QtCore.QRect( 10, 455, 31, 16 ) )
        font = QtGui.QFont()
        font.setFamily( "Segoe Print" )
        self.label_5.setFont( font )
        self.label_5.setObjectName( "label_5" )
        self.label_6 = QtWidgets.QLabel( self.centralwidget )
        self.label_6.setGeometry( QtCore.QRect( 10, 490, 61, 16 ) )
        font = QtGui.QFont()
        font.setFamily( "Segoe Print" )
        self.label_6.setFont( font )
        self.label_6.setObjectName( "label_6" )
        self.label_7 = QtWidgets.QLabel( self.centralwidget )
        self.label_7.setGeometry( QtCore.QRect( 10, 525, 47, 13 ) )
        font = QtGui.QFont()
        font.setFamily( "Segoe Print" )
        self.label_7.setFont( font )
        self.label_7.setObjectName( "label_7" )
        self.label_8 = QtWidgets.QLabel( self.centralwidget )
        self.label_8.setGeometry( QtCore.QRect( 225, 420, 101, 16 ) )
        font = QtGui.QFont()
        font.setFamily( "Segoe Print" )
        self.label_8.setFont( font )
        self.label_8.setObjectName( "label_1" )
        self.label_9 = QtWidgets.QLabel( self.centralwidget )
        self.label_9.setGeometry( QtCore.QRect( 225, 490, 81, 20 ) )
        font = QtGui.QFont()
        font.setFamily( "Segoe Print" )
        self.label_9.setFont( font )
        self.label_9.setObjectName( "label_2" )
        self.label_10 = QtWidgets.QLabel( self.centralwidget )
        self.label_10.setGeometry( QtCore.QRect( 225, 525, 91, 20 ) )
        font = QtGui.QFont()
        font.setFamily( "Segoe Print" )
        self.label_10.setFont( font )
        self.label_10.setObjectName( "label_6" )
        self.label_11 = QtWidgets.QLabel( self.centralwidget )
        self.label_11.setGeometry( QtCore.QRect( 225, 455, 47, 13 ) )
        font = QtGui.QFont()
        font.setFamily( "Segoe Print" )
        self.label_11.setFont( font )
        self.label_11.setObjectName( "label_7" )
        self.FullName = QtWidgets.QLineEdit( self.centralwidget )
        self.FullName.setGeometry( QtCore.QRect( 96, 415, 113, 20 ) )
        self.FullName.setObjectName( "FullName" )
        self.Age = QtWidgets.QLineEdit( self.centralwidget )
        self.Age.setGeometry( QtCore.QRect( 96, 450, 113, 20 ) )
        self.Age.setObjectName( "Age" )
        self.Phone = QtWidgets.QLineEdit( self.centralwidget )
        self.Phone.setGeometry( QtCore.QRect( 96, 485, 113, 20 ) )
        self.Phone.setObjectName( "Phone" )
        self.Email = QtWidgets.QLineEdit( self.centralwidget )
        self.Email.setGeometry( QtCore.QRect( 324, 417, 113, 20 ) )
        self.Email.setObjectName( "Email" )
        self.MedicalCondition = QtWidgets.QLineEdit( self.centralwidget )
        self.MedicalCondition.setGeometry( QtCore.QRect( 324, 450, 113, 20 ) )
        self.MedicalCondition.setObjectName( "MedicalCondition" )
        self.Gender = QtWidgets.QComboBox( self.centralwidget )
        self.Gender.setGeometry( QtCore.QRect( 96, 520, 81, 22 ) )
        self.Gender.setObjectName( "Get_Geneder" )
        self.Gender.addItem( "" )
        self.Gender.setItemText( 0, "" )
        self.Gender.addItem( "" )
        self.Gender.addItem( "" )
        self.Gender.addItem( "" )
        self.PreferDay = QtWidgets.QComboBox( self.centralwidget )
        self.PreferDay.setGeometry( QtCore.QRect( 324, 485, 111, 22 ) )
        self.PreferDay.setObjectName( "PreferDay" )
        self.PreferDay.addItem( "" )
        self.PreferDay.setItemText( 0, "" )
        self.PreferDay.addItem( "" )
        self.PreferDay.addItem( "" )
        self.PreferDay.addItem( "" )
        self.PreferDay.addItem( "" )
        self.PreferDay.addItem( "" )
        self.PreferDay.addItem( "" )
        self.PreferDay.addItem( "" )
        self.timeEdit = QtWidgets.QTimeEdit( self.centralwidget )
        self.timeEdit.setGeometry( QtCore.QRect( 324, 520, 71, 22 ) )
        self.timeEdit.setObjectName( "timeEdit" )
        self.UpdateButton = QtWidgets.QPushButton( self.centralwidget )
        self.UpdateButton.setGeometry( QtCore.QRect( 470, 505, 61, 31 ) )
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize( 9 )
        font.setBold( True )
        font.setWeight( 75 )
        self.UpdateButton.setFont( font )
        self.UpdateButton.setStyleSheet( "background-color: rgb(85, 170, 255);" )
        self.UpdateButton.setObjectName( "UpdateRecordB" )
        self.UpdateButton.clicked.connect(self.UpdateAppointment)
        self.DeleteButton = QtWidgets.QPushButton( self.centralwidget )
        self.DeleteButton.setGeometry( QtCore.QRect( 541, 505, 61, 31 ) )
        font = QtGui.QFont()
        font.setFamily( "Segoe UI Semibold" )
        font.setPointSize( 9 )
        font.setBold( True )
        font.setWeight( 75 )
        self.DeleteButton.setFont( font )
        self.DeleteButton.setStyleSheet( "background-color: rgb(85, 170, 255);" )
        self.DeleteButton.setObjectName( "DeleteRecordB" )
        self.DeleteButton.clicked.connect(self.DeleteAppointment)
        MainWindow.setCentralWidget( self.centralwidget )
        self.menubar = QtWidgets.QMenuBar( MainWindow )
        self.menubar.setGeometry( QtCore.QRect( 0, 0, 702, 21 ) )
        self.menubar.setObjectName( "menubar" )
        MainWindow.setMenuBar( self.menubar )
        self.statusbar = QtWidgets.QStatusBar( MainWindow )
        self.statusbar.setObjectName( "statusbar" )
        MainWindow.setStatusBar( self.statusbar )

        self.retranslateUi( MainWindow )
        QtCore.QMetaObject.connectSlotsByName( MainWindow )

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle( _translate( "MainWindowAdmin", "MainWindowAdmin" ) )
        self.AppointmentButton.setText( _translate( "MainWindowAdmin", "Prendre rendez-vous" ) )
        self.label_3.setText( _translate( "MainWindowAdmin", "Vos informations" ) )
        self.label_4.setText( _translate( "MainWindowAdmin", "votre rendez-vous" ) )
        item = self.tableWidgetPatientInfo.horizontalHeaderItem( 0 )
        item.setText( _translate( "MainWindowAdmin", "Nom complet" ) )
        item = self.tableWidgetPatientInfo.horizontalHeaderItem( 1 )
        item.setText( _translate( "MainWindowAdmin", "Date de naissance" ) )
        item = self.tableWidgetPatientInfo.horizontalHeaderItem( 2 )
        item.setText( _translate( "MainWindowAdmin", "Adresse" ) )
        item = self.tableWidgetPatientInfo.horizontalHeaderItem( 3 )
        item.setText( _translate( "MainWindowAdmin", "Phone" ) )
        item = self.tableWidgetPatientInfo.horizontalHeaderItem( 4 )
        item.setText( _translate( "MainWindowAdmin", "Etat de santé" ) )
        item = self.tableWidgetPatientInfo.horizontalHeaderItem( 5 )
        item.setText( _translate( "MainWindowAdmin", "Genre" ) )
        item = self.tableWidgetPatientInfo.horizontalHeaderItem( 6 )
        item.setText( _translate( "MainWindowAdmin", "Maladie" ) )
        item = self.tableWidgetPatientInfo.horizontalHeaderItem( 7 )
        item.setText( _translate( "MainWindowAdmin", "E-mail" ) )
        item = self.tableWidgetAppointment.horizontalHeaderItem( 0 )
        item.setText( _translate( "MainWindowAdmin", "État" ) )
        item = self.tableWidgetAppointment.horizontalHeaderItem( 1 )
        item.setText( _translate( "MainWindowAdmin", "Nom complet" ) )
        item = self.tableWidgetAppointment.horizontalHeaderItem( 2 )
        item.setText( _translate( "MainWindowAdmin", "Âge" ) )
        item = self.tableWidgetAppointment.horizontalHeaderItem( 3 )
        item.setText( _translate( "MainWindowAdmin", "Téléphone" ) )
        item = self.tableWidgetAppointment.horizontalHeaderItem( 4 )
        item.setText( _translate( "MainWindowAdmin", "Genre" ) )
        item = self.tableWidgetAppointment.horizontalHeaderItem( 5 )
        item.setText( _translate( "MainWindowAdmin", "Patient Medical Condition" ) )
        item = self.tableWidgetAppointment.horizontalHeaderItem( 6 )
        item.setText( _translate( "MainWindowAdmin", "Jour" ) )
        item = self.tableWidgetAppointment.horizontalHeaderItem( 7 )
        item.setText( _translate( "MainWindowAdmin", "Heure" ) )
        item = self.tableWidgetAppointment.horizontalHeaderItem( 8 )
        item.setText( _translate( "MainWindowAdmin", "E-mail" ) )
        self.ShowApButton.setText( _translate( "MainWindowAdmin", "Rendez-vous" ) )
        self.ShowInfoButton.setText( _translate( "MainWindowAdmin", "Afficher des informations" ) )
        self.LogOutButton.setText( _translate( "MainWindowAdmin", "Se déconnecter" ) )
        self.label.setText( _translate( "MainWindowAdmin", "Nom complet" ) )
        self.label_5.setText( _translate( "MainWindowAdmin", "Âge" ) )
        self.label_6.setText( _translate( "MainWindowAdmin", "Téléphone" ) )
        self.label_7.setText( _translate( "MainWindowAdmin", "Genre" ) )
        self.label_8.setText( _translate( "MainWindowAdmin", "Etat de santé" ) )
        self.label_9.setText( _translate( "MainWindowAdmin", "Jour" ) )
        self.label_10.setText( _translate( "MainWindowAdmin", "Heure" ) )
        self.label_11.setText( _translate( "MainWindowAdmin", "E-mail" ) )
        self.Gender.setItemText( 1, _translate( "MainWindowAdmin", "Homme" ) )
        self.Gender.setItemText( 2, _translate( "MainWindowAdmin", "Femelle" ) )
        
        self.PreferDay.setItemText( 1, _translate( "MainWindowAdmin", "Samedi " ) )
        self.PreferDay.setItemText( 2, _translate( "MainWindowAdmin", "Dimanche " ) )
        self.PreferDay.setItemText( 3, _translate( "MainWindowAdmin", "Lundi" ) )
        self.PreferDay.setItemText( 4, _translate( "MainWindowAdmin", "Mardi " ) )
        self.PreferDay.setItemText( 5, _translate( "MainWindowAdmin", "Mercredi " ) )
        self.PreferDay.setItemText( 6, _translate( "MainWindowAdmin", "Jeudi " ) )
        self.PreferDay.setItemText( 7, _translate( "MainWindowAdmin", "Vendredi " ) )
        self.UpdateButton.setText( _translate( "MainWindowAdmin", "Mise à jour" ) )
        self.DeleteButton.setText( _translate( "MainWindowAdmin", "Supprimer" ) )


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Patient_Login()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
