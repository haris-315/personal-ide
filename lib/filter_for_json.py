class Filter:
    def __init__(self,data: dict) -> None:
        self.data = str(data)
        self.data = self.data.replace("'",'"')
        self.data = self.data.replace("True","true")
        self.data = self.data.replace("False","false")
    def GetResult(self):
        return self.data
        