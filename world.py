import time

class Frog:
    def __init__(self):
        self.hungry = True

    def day_of_frog(self):
        time.sleep(3)
        print("Frog: moving, eating, breathing")
        if self.hungry:
            time.sleep(3)
            print("Grass: being eaten")
        self.hungry = False

    def night_of_frog(self):
        time.sleep(3)
        print("Frog: sleeping, sleeping, sleeping")
        self.hungry = True


class Tree:
    def __init__(self, frog: Frog):
        self.o2 = False
        self.frog = frog

    def day_of_tree(self):
        self.o2 = True
        time.sleep(3)
        print("Tree: creating oxygen")
        self.frog.day_of_frog()

    def night_of_tree(self):
        self.o2 = False
        time.sleep(3)
        print("Tree: doing nothing")
        self.frog.night_of_frog()

class Sun:
    def __init__(self, light, tree: Tree):
        self.light = light
        self.tree = tree

    def day(self):
        while True:
            time.sleep(3)
            if self.light:
                print("Sun: shining")
                self.tree.day_of_tree()
                self.light = False
            if not self.light:
                time.sleep(3)
                print("Sun: not shining")
                self.tree.night_of_tree()
                self.light = True


frog = Frog()
tree = Tree(frog)
sun = Sun(True, tree)
sun.day()





