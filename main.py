while True:
  try:
    person = int(input("Введите кол-во человек (число): "))
    print()
    break
  except ValueError:
    print("Вы должны ввести число, попробуйте снова.")



class Dish:
    def __init__(self, ingredients='', mass=0, unit=''):
        self.ingredients = ingredients
        self.mass = mass
        self.unit = unit

class Cook_book:
    def __init__(self, name):
        self.name = name
        self.content = []

    def mix(self, components):
        # Добавление списка компонентов в список content:
        self.content.append([components.ingredients, components.mass, components.unit])

        # Добавление в список content:
        # self.content.append(components.ingredients)
        # self.content.append(components.mass)
        # self.content.append(components.unit)

potatos = Dish('Картошка', 100, 'гр.')
carrots = Dish('Морковь', 50, 'гр.')
cucumbers = Dish('Огурцы', 50, 'гр.')
pea = Dish('Горошек', 30, 'гр.')
mayonnaise = Dish('Майонез', 70, 'мл.')

cheese = Dish('Сыр', 50, 'гр.')
tomato = Dish('Томаты', 50, 'гр.')
batter = Dish('Тесто', 100, 'гр.')
bacon = Dish('Бекон', 30, 'гр.')
sausage = Dish('Колбаса', 30, 'гр.')
mushroom = Dish('Грибы', 20, 'гр.')

hurma = Dish('хурма', 60, 'гр.')
kiwi = Dish('киви', 60, 'гр.')
tworog = Dish('творог', 60, 'гр.')
sugar = Dish('сахар', 10, 'гр.')
honey = Dish('мед', 50, 'гр.')



salad = Cook_book('Салат')
pizza = Cook_book('Пицца')
fruits = Cook_book('Фруктовый десерт')
#print(salad.__dict__)
# print(salad.name)
# print(salad.content)

# добавление ингредиентов в состав с помощью собственного метода
salad.mix(potatos)
salad.mix(carrots)
salad.mix(cucumbers)
salad.mix(pea)
salad.mix(mayonnaise)

pizza.mix(cheese)
pizza.mix(tomato)
pizza.mix(batter)
pizza.mix(bacon)
pizza.mix(sausage)
pizza.mix(mushroom)

fruits.mix(hurma)
fruits.mix(kiwi)
fruits.mix(tworog)
fruits.mix(sugar)
fruits.mix(honey)

# print(salad.content)
# print(pizza.content)
# print(fruits.content)
#print(salad.__dict__)

# Вывод на экран состав класса:
# print(potatos.ingredients, potatos.mass, potatos.unit)
# print(carrots.ingredients, carrots.mass, carrots.unit)
# print(cucumbers.ingredients, cucumbers.mass, cucumbers.unit)
# print(pea.ingredients, pea.mass, pea.unit)
# print(mayonnaise.ingredients, mayonnaise.mass, mayonnaise.unit)

print(f'{salad.name}:')
for ingredient, weight, measure in salad.content:
    print(f'{ingredient}, {weight*person} {measure}')
print()
print(f'{pizza.name}:')
for ingredient, weight, measure in pizza.content:
    print(f'{ingredient}, {weight*person} {measure}')
print()
print(f'{fruits.name}:')
for ingredient, weight, measure in fruits.content:
    print(f'{ingredient}, {weight*person} {measure}')


# def rate_hw(self, student, course, grade):
#     if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
#         if course in student.grades:
#             student.grades[course] += [grade]
#         else:
#             student.grades[course] = [grade]
#     else:
#         return 'Ошибка'
""" cook_book = [
  ['Салат',
    [
      ['картофель', 100, 'гр.'],
      ['морковь', 50, 'гр.'],
      ['огурцы', 50, 'гр.'],
      ['горошек', 30, 'гр.'],
      ['майонез', 70, 'мл.'],
    ],
  ],
  ['Пицца',
    [
      ['сыр', 50, 'гр.'],
      ['томаты', 50, 'гр.'],
      ['тесто', 100, 'гр.'],
      ['бекон', 30, 'гр.'],
      ['колбаса', 30, 'гр.'],
      ['грибы', 20, 'гр.'],
    ],
  ],
  ['фруктовый десерт',
    [
      ['хурма', 60, 'гр.'],
      ['киви', 60, 'гр.'],
      ['творог', 60, 'гр.'],
      ['сахар', 10, 'гр.'],
      ['мед', 50, 'гр.'],
    ],
  ],
] """