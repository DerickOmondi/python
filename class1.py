class fruits:
    def __init__(self,name,color,area_grown,taste):
        self.name = name
        self.color = color
        self.area_grown = area_grown
        self.taste = taste
        
fruits1 = fruits('mango','yellow','Transzoia','sugary')
fruits2 = fruits('pineapple','green','Homabay','sweet')

print(fruits1.color)

class sour_fruits(fruits):
    def __init__(self, name, color, area_grown, taste,condition_grown):
        super().__init__(name, color, area_grown, taste)
        self.condition_grown = condition_grown
        

sour_fruits1 = sour_fruits('melon','green','nakuru','sour','swampy')


print(f"{sour_fruits1.name}")


class red_fruits(sour_fruits):
    def __init__(self, name, color, area_grown, taste, condition_grown,imported_fruits):
        super().__init__(name, color, area_grown, taste, condition_grown)
        self.imported_fruits = imported_fruits

    def fruit_owner(self):
        fruit_owner = self.name
        return fruit_owner
    
    print(fruit_owner)

# red_fruits1 = red_fruits('melon','green','nakuru','sour','swampy','apoyo')


# print(f"{red_fruits1.imported_fruits}")