from inheritance_05.project.food.food import Food
from inheritance_05.project.food.dessert import Dessert
from inheritance_05.project.food.cake import Cake
from inheritance_05.project.food.salmon import Salmon
from inheritance_05.project.food.main_dish import MainDish


ds = Cake('Chocolate Pie')
print(ds.name)
print(ds.price)
print(ds.grams)
print(ds.calories)

da = Salmon('fish',5)
print(da.name)
print(da.price)
print(da.grams)