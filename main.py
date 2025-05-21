from interface import interface_main as i_m
from database.cold_storage import db as cs_db

# d_main = d_m.Database()

# d_main.setting_table()
# d_main.data_edit_amount('사과', 5)
cold_storage = cs_db.Database()
cold_storage.setting_table()

d_main = d_m.Database()

d_main.setting_table()
d_main.data_edit_amount('사과', 5)