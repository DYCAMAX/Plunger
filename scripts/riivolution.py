import os
import sys
import os
import shutil
from PyQt5.QtWidgets import QWidget, QTextEdit
from compile import compiler

class riivolution(QWidget):
     def __init__(self):
        super().__init__()

        Project_Folders = QWidget
        riivolution_ecriture = QTextEdit

        shutil.copy('mods/riivolution files/Rayman Raving Rabbids.xml', (Project_Folders))

     def Project_Folders(self):
          self

     def modify_file_RRR1(self):
        filename = "mods/riivolution files/Rayman Raving Rabbids.xml" 
        line_id = 5
        new_text = '<option name="{NameProject}" id="{IdProject}" default="1">'
        line_folders = 12
        new_text = '<patch id="{IdProject}">'
        line_folders = 13
        new_text = '<folder external="/{IdProject}/HomeButton2"/>'
        line_folders = 14
        new_text = '<folder external="/{IdProject}/sound"/>'
        line_folders = 15
        new_text = '<folder external="/{IdProject}/TUTO"/>'
        line_file = 16
        new_text = '<file disc="banner.tpl" external="/{IdProject}/banner.tpl"/>'
        line_file = 17
        new_text = '<file disc="bannericons.tpl" external="/{IdProject}/bannericons.tpl"/>'
        line_file = 18
        new_text = '<file disc="Bonus_0.bik" external="/{IdProject}/Bonus_0.bik"/>'
        line_file = 19
        new_text = '<file disc="Bonus_1.bik" external="/{IdProject}/Bonus_1.bik"/>'
        line_file = 20
        new_text = '<file disc="Bonus_2.bik" external="/{IdProject}/Bonus_2.bik"/>'
        line_file = 21
        new_text = '<file disc="Bonus_9.bik" external="/{IdProject}/Bonus_9.bik"/>'
        line_file = 22
        new_text = '<file disc="Bonus_10.bik" external="/{IdProject}/Bonus_10.bik"/>'
        line_file = 23
        new_text = '<file disc="Bonus_11.bik" external="/{IdProject}/Bonus_11.bik"/>'
        line_file = 24
        new_text = '<file disc="Bonus_11.bik" external="/{IdProject}/Bonus_11.bik"/>'
        line_file = 25
        new_text = '<file disc="Bonus_20.bik" external="/{IdProject}/Bonus_20.bik"/>'
        line_file = 26
        new_text = '<file disc="Bonus_21.bik" external="/{IdProject}/Bonus_21.bik"/>'
        line_file = 27
        new_text = '<file disc="Bonus_22.bik" external="/{IdProject}/Bonus_22.bik"/>'
        line_file = 28
        new_text = '<file disc="Bonus_23.bik" external="/{IdProject}/Bonus_23.bik"/>'
        line_file = 29
        new_text = '<file disc="Bonus_24.bik" external="/{IdProject}/Bonus_24.bik"/>'
        line_file = 30
        new_text = '<file disc="Bonus_25.bik" external="/{IdProject}/Bonus_25.bik"/>'
        line_file = 31
        new_text = '<file disc="Bonus_26.bik" external="/{IdProject}/Bonus_26.bik"/>'
        line_file = 32
        new_text = '<file disc="Bonus_27.bik" external="/{IdProject}/Bonus_27.bik"/>'
        line_file = 33
        new_text = '<file disc="Bonus_28.bik" external="/{IdProject}/Bonus_28.bik"/>'
        line_file = 34
        new_text = '<file disc="Bonus_29.bik" external="/{IdProject}/Bonus_29.bik"/>'
        line_file = 35
        new_text ='<file disc="Bonus_30.bik" external="/{IdProject}/Bonus_30.bik"/>'
        line_file = 36
        new_text = '<file disc="Bonus_31.bik" external="/{IdProject}/Bonus_31.bik"/>'
        line_file = 37
        new_text = '<file disc="Default.bik" external="/{IdProject}/Default.bik"/>'
        line_file = 38
        new_text = '<file disc="icon.tpl" external="/{IdProject}/icon.tpl"/>'
        line_file = 39
        new_text = '<file disc="INTRO.BIK" external="/{IdProject}/INTRO.BIK"/>'
        line_file = 40
        new_text = '<file disc="jaderevo_r.elf" external="/{IdProject}/jaderevo_r.elf"/>'
        line_file = 41
        new_text = '<file disc="Licensed_By_Nintendo.bik" external="/{IdProject}/Licensed_By_Nintendo.bik"/>'
        line_file = 42
        new_text = '<file disc="load_0.bik" external="/{IdProject}/load_0.bik"/>'
        line_file = 43
        new_text = '<file disc="load_1.bik" external="/{IdProject}/load_1.bik"/>'
        line_file = 44
        new_text = '<file disc="load_2.bik" external="/{IdProject}/load_2.bik"/>'
        line_file = 45
        new_text = '<file disc="load_3.bik" external="/{IdProject}/load_3.bik"/>'
        line_file = 46
        new_text = '<file disc="load_5.bik" external="/{IdProject}/load_5.bik"/>'
        line_file = 47
        new_text = '<file disc="load_6.bik" external="/{IdProject}/load_6.bik"/>'
        line_file = 48
        new_text = '<file disc="load_7.bik" external="/{IdProject}/load_7.bik"/>'
        line_file = 49
        new_text = '<file disc="nunchunk_0.bik" external="/{IdProject}/nunchunk_0.bik"/>' 
        line_file = 50
        new_text = '<file disc="nunchunk_1.bik" external="/{IdProject}/nunchunk_1.bik"/>' 
        line_file = 51
        new_text = '<file disc="nunchunk_2.bik" external="/{IdProject}/nunchunk_2.bik"/>'
        line_file = 52
        new_text = '<file disc="nunchunk_3.bik" external="/{IdProject}/nunchunk_3.bik"/>'
        line_file = 53
        new_text = '<file disc="nunchunk_5.bik" external="/{IdProject}/nunchunk_5.bik"/>'
        line_file = 54
        new_text = '<file disc="nunchunk_6.bik" external="/{IdProject}/nunchunk_6.bik"/>'
        line_file = 55
        new_text = '<file disc="nunchunk_7.bik" external="/{IdProject}/nunchunk_7.bik"/>'
        line_file = 56
        new_text = '<file disc="nunchunk_12.bik" external="/{IdProject}/nunchunk_12.bik"/>'
        line_file = 57
        new_text = '<file disc="opening.bnr" external="/{IdProject}/opening.bnr"/>'
        line_file = 58
        new_text = '<file disc="Rayman4.bf" external="/{IdProject}/Rayman4.bf"/>'
        line_file = 59
        new_text = '<file disc="strap_0.bik" external="/{IdProject}/strap_0.bik"/>'
        line_file = 60
        new_text = '<file disc="strap_1.bik" external="/{IdProject}/strap_1.bik"/>'
        line_file = 61
        new_text = '<file disc="strap_3.bik" external="/{IdProject}/strap_3.bik"/>'
        line_file = 62
        new_text = '<file disc="strap_5.bik" external="/{IdProject}/strap_5.bik"/>'
        line_file = 63
        new_text = '<file disc="strap_6.bik" external="/{IdProject}/strap_6.bik"/>'
        line_file = 64
        new_text = '<file disc="strap_7.bik" external="/{IdProject}/strap_7.bik"/>'
        line_file = 65
        new_text = '<file disc="strap_12.bik" external="/{IdProject}/strap_12.bik"/>'
        line_file = 66
        new_text = '<file disc="strap.tpl" external="/{IdProject}/strap.tpl"/>'
        line_file = 67
        new_text = '<file disc="strap0.tpl" external="/{IdProject}/strap0.tpl"/>'
        line_file = 68
        new_text = '<file disc="strap1.tpl" external="/{IdProject}/strap1.tpl"/>'
        line_file = 69
        new_text = '<file disc="strap3.tpl" external="/{IdProject}/strap3.tpl"/>'
        line_file = 70
        new_text = '<file disc="strap5.tpl" external="/{IdProject}/strap5.tpl"/>'
        line_file = 71
        new_text = '<file disc="strap6.tpl" external="/{IdProject}/strap6.tpl"/>'
        line_file = 72
        new_text = '<file disc="strap7.tpl" external="/{IdProject}/strap7.tpl"/>'
        line_file = 73
        new_text = '<file disc="strap12.tpl" external="/{IdProject}/strap12.tpl"/>'
        line_file = 74
        new_text = '<file disc="UBIMTP0.bik" external="/{IdProject}/UBIMTP0.bik"/>'
        line_file = 75
        new_text = '<file disc="UBIMTP1.bik" external="/{IdProject}/UBIMTP1.bik"/>'
        line_file = 76
        new_text = '<file disc="UBIMTP2.bik" external="/{IdProject}/UBIMTP2.bik"/>'
        line_file = 77
        new_text = '<file disc="UBIMTP3.bik" external="/{IdProject}/UBIMTP3.bik"/>'
        line_file = 78
        new_text = '<file disc="UBIMTP5.bik" external="/{IdProject}/UBIMTP5.bik"/>'
        line_file = 79
        new_text = '<file disc="UBIMTP6.bik" external="/{IdProject}/UBIMTP6.bik"/>'
        line_file = 80
        new_text = '<file disc="UBIMTP7.bik" external="/{IdProject}/UBIMTP7.bik"/>'
        line_file = 81
        new_text = '<file disc="vssver.scc" external="/{IdProject}/vssver.scc"/>'
        line_file = 82
        new_text = '<file disc="/HomeButton2/config.txt" external="/{IdProject}/HomeButton2/config.txt/>'
        line_file = 83
        new_text = '<file disc="/HomeButton2/home_nosave.csv" external="/{IdProject}/HomeButton2/home_nosave.csv/>'
        line_file = 84
        new_text = '<file disc="/HomeButton2/home.csv" external="/{IdProject}/HomeButton2/home.csv/>'
        line_file = 85
        new_text = '<file disc="/HomeButton2/homeBtn_ENG.arc" external="/{IdProject}/HomeButton2/homeBtn_ENG.arc/>'
        line_file = 86
        new_text = '<file disc="/HomeButton2/homeBtn_FRA.arc" external="/{IdProject}/HomeButton2/homeBtn_FRA.arc/>'
        line_file = 87
        new_text = '<file disc="/HomeButton2/homeBtn_GER.arc" external="/{IdProject}/HomeButton2/homeBtn_GER.arc/>'
        line_file = 88
        new_text = '<file disc="/HomeButton2/homeBtn_ITA.arc" external="/{IdProject}/HomeButton2/homeBtn_ITA.arc/>'
        line_file = 89
        new_text = '<file disc="/HomeButton2/homeBtn_NED.arc" external="/{IdProject}/HomeButton2/homeBtn_NED.arc/>'
        line_file = 90
        new_text = '<file disc="/HomeButton2/homeBtn_SPA.arc" external="/{IdProject}/HomeButton2/homeBtn_SPA.arc/>'
        line_file = 91
        new_text = '<file disc="/HomeButton2/homeBtn.arc" external="/{IdProject}/HomeButton2/homeBtn.arc/>'
        line_file = 92
        new_text = '<file disc="/HomeButton2/homeBtnIcon.tpl" external="/{IdProject}/HomeButton2/homeBtnIcon.tpl/>'
        line_file = 93
        new_text = '<file disc="/HomeButton2/HomebuttonSe.brsar" external="/{IdProject}/HomeButton2/HomebuttonSe.brsar/>'
        line_file = 94
        new_text = '<file disc="/HomeButton2/SpeakerSe.arc" external="/{IdProject}/HomeButton2/SpeakerSe.arc/>'
        line_file = 95
        new_text = '<file disc="/sound/2nd_time.mid" external="/{IdProject}/sound/2nd_time.mid/>'
        line_file = 96
        new_text = '<file disc="/sound/autumnal.mid" external="/{IdProject}/sound/autumnal.mid/>'
        line_file = 97
        new_text = '<file disc="/sound/sound_data.brsar" external="/{IdProject}/sound/sound_data.brsar/>'
        line_file = 98
        new_text = '<file disc="/sound/Roland/GM16.DLS" external="/{IdProject}/sound/Roland/GM16.DLS/>'
        line_file = 99
        new_text ='<file disc="/sound/Roland/gm16adpcm.pcm" external="/{IdProject}/sound/Roland/gm16adpcm.pcm/>'
        line_file = 100
        new_text ='<file disc="/sound/Roland/gm16adpcm.wt" external="/{IdProject}/sound/Roland/gm16adpcm.wt/>'
        

        line_file = 
        new_text = '<file disc="/TUTO/1_2_3_Soleil.bik" external="/{IdProject}/TUTO/1_2_3_Soleil.bik"/>'
