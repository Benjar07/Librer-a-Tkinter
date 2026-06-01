"""
Estudiantes 7mo 3ra
Benjamin Rodriguez
Alejo Gomez
"""

#Importa la librerias de UIManager y ControlData de los directorios ui y data
from ui.UIManager import window, ConfigWindow, CreateList, CreateOptionButtons
from data.ControlData import LoadDataFromCSV

#Utiliza una funcion de UIManager para configurar la resolucion de la ventana
ConfigWindow(800, 600)
#Carga los datos de un CSV, en las variables headers y data
headers, data = LoadDataFromCSV("data/students.csv")
#Crea una lista con los datos de headers y data
CreateList(headers, data)
#Crea los botones para las diferentes opciones
CreateOptionButtons()
#Ejecuta la aplicacion
window.mainloop()
