# use for Qt
import sys
import random
from PySide6 import QtCore, QtWidgets, QtGui

# use for file
import os
import zipfile
import shutil

# in screen widgets
class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        
        self.directory = ""
        
        self.text = QtWidgets.QLabel("Please select path font folder.")
        self.folder = QtWidgets.QPushButton("Select Folder")
        self.extract = QtWidgets.QPushButton("Extract All")
        self.textbox = QtWidgets.QTextEdit("None")

        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.addWidget(self.text)
        self.layout.addWidget(self.folder)
        self.layout.addWidget(self.textbox)
        self.layout.addWidget(self.extract)

        self.folder.clicked.connect(self.selectFolder)
        self.extract.clicked.connect(self.extractFolder)

    @QtCore.Slot()
    # select a folder for extrack all font (require!!!) 
    def selectFolder(self):
        respon = QtWidgets.QFileDialog.getExistingDirectory(
            self,
            caption="select folder"
        )
        self.textbox.setText(str(respon))
        self.directory = str(respon)

    # extrack all file out of folder to folder font (require selectFile first !!!).
    def extractFolder(self) :
        if self.directory == "" :
            self.textbox.setText(str("Please select folder!!!"))
            return
        
        if not os.path.exists(self.directory + "/font") :
            os.mkdir(self.directory + "/font")
        
        # loop get file on dir.
        for filename in os.listdir(self.directory ):

            # check only .zip file.
            if filename.endswith('.zip'):
                file_path = os.path.join(self.directory , filename)

                # extract file in folder font
                if os.path.isfile(file_path):
                    with zipfile.ZipFile(file_path , "r") as zip_ref :
                        zip_ref.extractall(self.directory + "/font")

        # create folder for pull font file
        if not os.path.exists(self.directory + "/font/font_for_install") :
            os.mkdir(self.directory + "/font/font_for_install")
        
        # clear textBox for use detail
        self.textbox.setText("")

        # use os walk to find font on folder and cut them out to main font folder
        for root , dirs , files in os.walk(self.directory + "/font") :

            # move all font file to main font folder
            for file_name in files :
                if file_name.endswith((".otf" , ".ttf")) :
                    if not os.path.exists(os.path.join(self.directory , "font/font_for_install" , file_name)) :
                        shutil.move(os.path.join(root , file_name) , self.directory + "/font/font_for_install")
                        self.textbox.setText(str(str(self.textbox.toPlainText()) + "\n add font to " + self.directory + "/font/font_for_install/" + file_name))
                else :
                    os.remove(os.path.join(root , file_name))

        # use again
        for root , dirs , files in os.walk(self.directory + "/font") : 
            # delete a directory not use
            for dir_name in dirs :
                if dir_name != "font_for_install" :
                    shutil.rmtree(os.path.join(root, dir_name))

# setup and show screen
if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    widget = MyWidget()
    widget.resize(500, 100)
    widget.show()

    sys.exit(app.exec())
