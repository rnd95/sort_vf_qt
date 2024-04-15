import sys, os, shutil, zipfile #default
from PyQt5 import QtWidgets
from MainWindow import Ui_Sort_VF_Window

class SortVFWindow (QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Sort_VF_Window()
        self.ui.setupUi(self)
        self.ui.ButtonExit.setEnabled(False)  # Disable exit button initially
        self.months = ['01','02','03','04', '05', '06', '07', '08', '09', '10', '11', '12']
        self.output_folder = 'SORTED_VF'
        self.district_folders = [folder for folder in os.listdir('.') if os.path.isdir(folder)]
        if not self.district_folders:
            self.ui.ListLog.addItem(f"Каталог порожній")
            self.ui.ButtonExit.setEnabled(True)
        else:
            self.ui.ListLog.addItem(f"Виявлено районів (папки): {self.district_folders}")

    def sort_files(self):
        for district_folder in self.district_folders:
            try:
                self.district_number = os.path.basename(district_folder)

                zip_files = [f for f in os.listdir(district_folder) if      
                     os.path.isfile(os.path.join(district_folder, f)) and f.endswith('.zip')]
                if not zip_files:       
                    print("Zip files not detected.")
                    self.ui.ListLog.addItem(f"Попередження: Не виявлено ZIP-файли в {self.district_number}")

                for zip_file in zip_files:
                    temp_folder = os.path.join(district_folder, 'temp')
                    os.makedirs(temp_folder, exist_ok=True)
                    with zipfile.ZipFile(os.path.join(district_folder, zip_file), 'r') as zip_ref:      
                        zip_ref.extractall(temp_folder)
                        print("Unpacked zip: ", zip_file)
                        self.ui.ListLog.addItem(f"Розпаковано : {zip_file}")
                    for self.month in self.months:
                        for bank_folder_number in range(100):
                            SheetType = str(self.month) + "TP" + str(bank_folder_number) + "P1_VF" 
                            bank_folder = os.path.join(temp_folder, 'verifikacia', 'DO', SheetType)
                            if not os.path.exists(bank_folder):     
                                continue

                            bank_folders = [f for f in os.listdir(bank_folder) if os.path.isdir(os.path.join(bank_folder, f))]

                            for bank_code in bank_folders:
                                output_bank_folder = os.path.join(self.output_folder, SheetType, bank_code)
                                if not os.path.exists(output_bank_folder):
                                    os.makedirs(output_bank_folder)
                                for item in os.listdir(os.path.join(bank_folder, bank_code)):
                                    s = os.path.join(bank_folder, bank_code, item)
                                    d = os.path.join(output_bank_folder, item)
                                    if os.path.isdir(s):
                                        shutil.copytree(s, d)
                                    else:
                                        shutil.copy2(s, d)
                    shutil.rmtree(temp_folder)

            except Exception as e:
                self.ui.ListLog.addItem(f"Помилка: {e}")
                self.setWindowTitle("Сортування по верифікації - Помилка у виконанні!")
        self.ui.ListLog.addItem("Done!")
        self.ui.ButtonExit.setEnabled(True)
    def showEvent(self, event):
        super().showEvent(event)
        self.sort_files()

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle("Fusion")
    window = SortVFWindow()
    window.show()  # Call window
    sys.exit(app.exec_())

