#通过class函数将对象进行分类然后定义
#分类要根据对象的属性和作用

#训练:"电子宠物(Tamagotchi)"模拟器
class Tamagotchi:
    def __init__(self,Tamagotchi):
        self.Tamagotchi=Tamagotchi
        self.hungry=50
        self.energy=50
    def eat(self,food):
        try:
            self.hungry=self.hungry-food
            self.energy=self.energy+food//2
            if (self.hungry<0):
                self.hungry=0
                print(f"{self.Tamagotchi}已经吃饱了")
            if (self.energy>100):
                self.energy=100
                print(f"{self.Tamagotchi}精神饱满,是时候和ta玩耍了")

            print(f"{self.Tamagotchi}的饥饿值为{self.hungry}")
        except ValueError:
            print(f"{self.Tamagotchi}不吃数字以外的食物哦")

    def play(self,exercise):
        try:
            self.hungry=self.hungry+4*exercise
            self.energy=self.energy-4*exercise
            if (self.hungry>100):
                self.hungry=100
                print(f"{self.Tamagotchi}好饿啊")
            if (self.energy<0):
                self.energy=0
                print(f"{self.Tamagotchi}好累啊")
            if (self.energy>0 and self.hungry<100):
                print(f"{self.Tamagotchi}锻炼了{exercise}秒")
        except ValueError:
            print(f"{self.Tamagotchi}无法理解这句话")

    def back(self,back):
        try:
            self.hungry=self.hungry-back//2
            self.energy=self.energy+back
            if (self.hungry>100):
                self.hungry=100
                print(f"{self.Tamagotchi}好饿啊")
            if (self.energy>100):
                self.energy=100
                print(f"{self.Tamagotchi}精神饱满,是时候和ta玩耍了")

            print(f"{self.Tamagotchi}的能量值为{self.energy}")
        except ValueError:
            print(f"{self.Tamagotchi}无法理解这句话")



my_first_Tamagotchi=Tamagotchi("pet")
my_first_Tamagotchi.eat(1)
my_first_Tamagotchi.back(0)
my_first_Tamagotchi.play(5)