from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3

from PyQt5.QtWidgets import QMessageBox

class ViewBillsAdmin( object ):
    
    def loadingData(self):
        db = sqlite3.connect( "project.db" )
        result = db.execute( "select * from Bills" )
        
        self.tableWidget.setRowCount( 0 )
        
        for RowNum, RowDATA in enumerate( result ):
            self.tableWidget.insertRow( RowNum )
            for ColumnNum, ColumnData in enumerate( RowDATA ):
                self.tableWidget.setItem( RowNum, ColumnNum, QtWidgets.QTableWidgetItem( str( ColumnData ) ) )
        db.close()
        self.BillNumber.clear()
    
    def SearchClicked(self):
        
        BillNumber = self.BillNumber.text()
        db = sqlite3.connect("project.db")
        result = db.execute("select * from Bills where BillNum="+ "'"+BillNumber+"'")
        self.tableWidget.setRowCount( 0 )
        
        for RowNum, RowDATA in enumerate( result ):
            self.tableWidget.insertRow( RowNum )
            for ColumnNum, ColumnData in enumerate( RowDATA ):
                self.tableWidget.setItem( RowNum, ColumnNum, QtWidgets.QTableWidgetItem( str( ColumnData ) ) )
        db.close()
    
    def DeleteClicked(self):
        
        BillNumber = self.BillNumber.text()
        db = sqlite3.connect( "project.db" )
        message1 = QMessageBox()
        message1.setWindowTitle( "Successfull" )
        message1.setInformativeText( "Vous avez supprimé le numéro de facture:  " + BillNumber )
        x = message1.exec_()
        db.execute( "delete from Bills where BillNum=" + "'" + BillNumber + "'" ) 
        db.commit()
        result = db.execute("select * from Bills")
        self.tableWidget.setRowCount( 0 )
        
        for RowNum, RowDATA in enumerate( result ):
            self.tableWidget.insertRow( RowNum )
            for ColumnNum, ColumnData in enumerate( RowDATA ):
                self.tableWidget.setItem( RowNum, ColumnNum, QtWidgets.QTableWidgetItem( str( ColumnData ) ) )

        db.close()
        self.BillNumber.clear()


    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindowAdmin")
        MainWindow.resize(800, 411)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.SearchButton = QtWidgets.QPushButton(self.centralwidget)
        self.SearchButton.setGeometry(QtCore.QRect(260, 20, 91, 31))
        self.SearchButton.setObjectName("SearchB")

        self.SearchButton.clicked.connect(self.SearchClicked)
        self.ViewBills = QtWidgets.QPushButton( self.centralwidget )
        self.ViewBills.setGeometry( QtCore.QRect( 534, 20, 111, 31 ) )
        font = QtGui.QFont()
        font.setPointSize(8)
        self.ViewBills.setFont( font )
        self.ViewBills.setObjectName( "ViewBills" )
        self.ViewBills.clicked.connect(self.loadingData)
        self.BillNumber = QtWidgets.QLineEdit(self.centralwidget)
        self.BillNumber.setGeometry(QtCore.QRect(100, 20, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.BillNumber.setFont(font)
        self.BillNumber.setObjectName("BillNumber")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 20, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.DeleteButton = QtWidgets.QPushButton(self.centralwidget)
        self.DeleteButton.setGeometry(QtCore.QRect(370, 20, 91, 31))
        self.DeleteButton.setObjectName("DeleteRecordB")
        self.DeleteButton.clicked.connect(self.DeleteClicked)
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(0, 60, 1300, 331))
        self.tableWidget.setStyleSheet("background-color: rgb(235, 235, 255);\n"
"\n"
"")
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(18)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(11, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(12, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(13, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(14, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(15, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(16, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(17, item)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindowAdmin", "MainWindowAdmin"))
        self.SearchButton.setText(_translate("MainWindowAdmin", "Recherche"))
        self.ViewBills.setText( _translate( "MainWindowAdmin", "Les factures" ) )
        self.label.setText(_translate("MainWindowAdmin", "N° facture"))
        self.DeleteButton.setText(_translate("MainWindowAdmin", "Supprimer"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindowAdmin", "N° facture"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindowAdmin", "Nom du Patient"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindowAdmin", "Date Entrée"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindowAdmin", "Date Sortir"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindowAdmin", "Services"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("MainWindowAdmin", "Chambre"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("MainWindowAdmin", "Médecine"))
        item = self.tableWidget.horizontalHeaderItem(7)
        item.setText(_translate("MainWindowAdmin", "L'infirmière"))
        item = self.tableWidget.horizontalHeaderItem(8)
        item.setText(_translate("MainWindowAdmin", "Intensive care unit"))
        item = self.tableWidget.horizontalHeaderItem(9)
        item.setText(_translate("MainWindowAdmin", "Soins à domicile"))
        item = self.tableWidget.horizontalHeaderItem(10)
        item.setText(_translate("MainWindowAdmin", "Les analyses"))
        item = self.tableWidget.horizontalHeaderItem(11)
        item.setText(_translate("MainWindowAdmin", "Ambulance"))
        item = self.tableWidget.horizontalHeaderItem(12)
        item.setText(_translate("MainWindowAdmin", "Soins"))
        item = self.tableWidget.horizontalHeaderItem(13)
        item.setText(_translate("MainWindowAdmin", "Médicaments"))
        item = self.tableWidget.horizontalHeaderItem(14)
        item.setText(_translate("MainWindowAdmin", "Autre"))
        item = self.tableWidget.horizontalHeaderItem(15)
        item.setText(_translate("MainWindowAdmin", "Total"))
        item = self.tableWidget.horizontalHeaderItem(16)
        item.setText(_translate("MainWindowAdmin", "Reçu par"))
        item = self.tableWidget.horizontalHeaderItem(17)
        item.setText(_translate("MainWindowAdmin", "Date"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = ViewBillsAdmin()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
