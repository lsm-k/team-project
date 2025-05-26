from interface import interface_main as ui_root
from database.cold_storage import db as cs_db
from database.favorite_ref import db as fr_db

cold_storage = cs_db.Database()
cold_storage.setting_table()

fr_db.Database.setting_table()

main_window = ui_root.Mainwindow()
main_window.show()
