from interface import interface_main as i_m
from database import database_main as d_m

<<<<<<< HEAD
main_window = i_m.Mainwindow()
main_window.mainrun()

# d_main = d_m.Database()

# d_main.setting_table()
# d_main.data_edit_amount('사과', 5)
cold_storage = cs_db.Database()
cold_storage.setting_table()
=======
# main_window = i_m.Mainwindow()
# main_window.mainrun()
>>>>>>> parent of 261cda4 (change to pyside6 and migrate previous changes)

d_main = d_m.Database()

d_main.setting_table()
d_main.data_edit_amount('사과', 5)