from src.controller.database import DatabaseController

class Monitoracao:
    def __init__(self):
        self.database = DatabaseController()
        
    def getMonitoracao(self):
        return self.database.getData("MONITORIA")
        
