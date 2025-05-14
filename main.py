from interface import interface_main as i_m
from database import database_main as d_m

main_window = i_m.Mainwindow()
main_window.mainrun()

d_main = d_m.Database()
d_main.default()
d_main.data_insert("사과", 10, "2025-12-31", "과일")