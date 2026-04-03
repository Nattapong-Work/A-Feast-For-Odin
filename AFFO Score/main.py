import sys
from PyQt6 import QtWidgets
from AFFO_main_ui import MyWindow
from AFFO_Logic import FinalScore


class AppController(MyWindow):
    def __init__(self):
        super().__init__()


        self.pb_done.clicked.connect(self.get_final_score)
        self.pb_reset.clicked.connect(self.reset)


    def get_island(self, state, points):
        pass


    def get_final_score(self):
        # โค้ดส่วนที่รวมรวมค่าจาก สปินบ็อกอื่นๆ มา
        data = {
            "whale" : self.spb_whale.value(),
            "knarr" : self.spb_knarr.value(),
            "long ship" : self.spb_long.value(),
            "knarr emi" : self.spb_knarr_emi.value(),
            "long emi" : self.spb_long_emi.value(),
            "silver" : self.spb_sil.value(),
            "income" : self.spb_inc.value(),
            "occupation" : self.spb_occu.value(),
            "shed" : self.spb_shed_num.value(),
            "shed minus" : self.spb_shed_mi.value(),
            "house" : self.spb_hou_num.value(),
            "house minus" : self.spb_hou_mi.value(),
            "long house" : self.spb_lng_num.value(),
            "long house minus" : self.spb_lng_mi.value(),
            "sheep" : self.spb_shp.value(),
            "preg sheep" : self.spb_preg_shp.value(),
            "cattle" : self.spb_cattle.value(),
            "preg cattle" : self.spb_preg_cattle.value(),
            "exploration minus" : self.spb_mi_expl.value(),
            "main village minus" : self.spb_vill_mi.value(),
        }

        # เรียกใช้ฟังก์ชั่นที่อยู่ในลอจิก พร้อมค่าพรารามิเตอร์ ที่เปนค่าที่ต้องคำนวณเช่น goo(ship = 20, house = 30,...) return กลับมาในตัวแปร
        total_score = FinalScore.get_final_score(
            data["whale"],
            data["knarr"],
            data["long ship"],
            data["knarr emi"],
            data["long emi"],
            data["silver"],
            data["income"],
            data["occupation"],
            data["shed"],
            data["shed minus"],
            data["house"],
            data["house minus"],
            data["long house"],
            data["long house minus"],
            data["sheep"],
            data["preg sheep"],
            data["cattle"],
            data["preg cattle"],
            data["exploration minus"],
            data["main village minus"]
        )
        # ใช้ self.lb_total_scr.set text เปนตัวแปรที่โค้แถวบนคนืนค่ามา
        self.lb_total_scr.setText(str(total_score))

    def reset(self):
        self.spb_whale.setValue(0)
        self.spb_knarr.setValue(0)
        self.spb_long.setValue(0)
        self.spb_knarr_emi.setValue(0)
        self.spb_long_emi.setValue(0)
        self.spb_sil.setValue(0)
        self.spb_inc.setValue(0)
        self.spb_occu.setValue(0)
        self.spb_shed_num.setValue(0)
        self.spb_shed_mi.setValue(0)
        self.spb_hou_num.setValue(0)
        self.spb_hou_mi.setValue(0)
        self.spb_lng_num.setValue(0)
        self.spb_lng_mi.setValue(0)
        self.spb_shp.setValue(0)
        self.spb_preg_shp.setValue(0)
        self.spb_cattle.setValue(0)
        self.spb_preg_cattle.setValue(0)
        self.spb_mi_expl.setValue(0)
        self.spb_vill_mi.setValue(0),




if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    controller = AppController()
    controller.show()
    sys.exit(app.exec())