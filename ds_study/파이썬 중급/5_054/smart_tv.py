class NormalTV:
    def __init__(self, i=32, c="black", r="full-HD"):
        self.inch = i
        self.color = c
        self.resolution = r
        self.smart_tv = "off"
        self.ai_tv = "off"

    def turn_on(self):
        print("TV power ON!!")

    def turn_off(self):
        print("TV power OFF!!")

    def print_tv_info(self):
        print(f"inch : {self.inch}inch")
        print(f"color : {self.color}")
        print(f"resolution : {self.resolution}")
        print(f"smart tv : {self.smart_tv}")
        print(f"ai tv: {self.ai_tv}")

class Tv4K(NormalTV):

    def __init__(self, i, c, r="4K"):
        super().__init__(i, c, r)

    def set_smart_tv(self, s):
        self.smart_tv = s
    
    def set_ai_tv(self, a):
        self.ai_tv = a
