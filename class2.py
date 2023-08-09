class GFG:
    def __init__(self,name,company):
        self.name=name
        self.company=company


    def saw(self):
        print(f"My name is{self.name} and i do work in {self.company}")



v=GFG("nature","apple")
w=GFG("bibek","microsoft")
x=GFG("narayan","NASA")

v.saw()
w.saw()
x.saw()