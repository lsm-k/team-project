from interface import interface_main as i_m
from database import database_main as d_m

main_window = i_m.Mainwindow()
main_window.mainrun()

d_main = d_m.Database()

d_main.setting_table()