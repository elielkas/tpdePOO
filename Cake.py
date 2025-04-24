# Class Cake
class Cake: 
    def __init__(self, flavor):
        self.flavor = flavor
        
    def cut_in_part(self):
        print("le gateaux est coupés à 4 morceaux")
        
        
cake = Cake("Chocolate")
print(cake.flavor)
cake.cut_in_part()
        
