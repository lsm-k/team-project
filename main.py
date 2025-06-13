from interface import interface_main as ui_root
from cold_storage import db as cs_db
from setting import db as setting_db

cold_storage = cs_db.Database()
cold_storage.setting_table()

setting_db.Database.setting_table()

main_window = ui_root.Mainwindow()
main_window.show()