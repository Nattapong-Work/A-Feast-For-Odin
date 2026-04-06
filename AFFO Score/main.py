import sys
from PyQt6 import QtWidgets
from AFFO_main_ui import MyWindow
from AFFO_Logic import *

class AppController(MyWindow):
    def __init__(self):
        super().__init__()

        # ปุ่ม done และ reset
        self.pb_done.clicked.connect(self.get_final_score)
        self.pb_reset.clicked.connect(self.reset)

        # เช็คบ็อกชื่อเกาะ
        self.chb_shet.stateChanged.connect(self.add_island)
        self.chb_faroe.stateChanged.connect(self.add_island)
        self.chb_ice.stateChanged.connect(self.add_island)
        self.chb_green.stateChanged.connect(self.add_island)
        self.chb_bear.stateChanged.connect(self.add_island)
        self.chb_baffin.stateChanged.connect(self.add_island)
        self.chb_labrador.stateChanged.connect(self.add_island)
        self.chb_newf.stateChanged.connect(self.add_island)

        self.chb_english_cr.stateChanged.connect(self.add_island)



    def add_island(self, state):
        if state == 2:
            ise = self.sender().text()
            global checkbox_point
            checkbox_point = add_point(ise)

        else:
            ise = self.sender().text()
            checkbox_point = sub_point(ise)

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
        total_score = get_final_score(
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

        ship = ship_score(self.spb_whale.value(),
                          self.spb_knarr.value(),
                          self.spb_long.value(),
                          self.spb_knarr_emi.value(),
                          self.spb_long_emi.value())

        island = checkbox_point

        building = building_score(self.spb_shed_num.value(),
                                  self.spb_hou_num.value(),
                                  self.spb_lng_num.value())

        animal = animal_score(self.spb_shp.value(),
                              self.spb_preg_shp.value(),
                              self.spb_cattle.value(),
                              self.spb_preg_cattle.value())




        # ใช้ self.lb_total_scr.set text เปนตัวแปรที่โค้แถวบนคนืนค่ามา
        self.lb_total_scr.setText(str(total_score))

        self.lb_ship_scr.setText(str(ship))
        self.lb_explo_scr.setText(str(island))
        self.lb_build_scr.setText(str(building))
        self.lb_ani_scr.setText(str(animal))

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

        self.chb_shet.setChecked(False)
        self.chb_faroe.setChecked(False)
        self.chb_ice.setChecked(False)
        self.chb_green.setChecked(False)
        self.chb_bear.setChecked(False)
        self.chb_baffin.setChecked(False)
        self.chb_labrador.setChecked(False)
        self.chb_newf.setChecked(False)

checkbox_point = 0


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    controller = AppController()
    controller.show()
    sys.exit(app.exec())