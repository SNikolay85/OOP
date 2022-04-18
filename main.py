""" while True:
  try:
    person = int(input("Введите кол-во человек (число): "))
    print()
    break
  except ValueError:
    print("Вы должны ввести число, попробуйте снова.") """
# import main


class Dish:
    def __init__(self, ingredients='', mass=0, unit=''):
        self.ingredients = ingredients
        self.mass = mass
        self.unit = unit

class Cook_book:
    def __init__(self, name):
        self.name = name
        self.content = []


potatos = Dish('Картошка', 100, 'гр.')
carrots = Dish('Морковь', 50, 'гр.')
cucumbers = Dish('Огурцы', 50, 'гр.')
pea = Dish('Горошек', 30, 'гр.')
mayonnaise = Dish('Майонез', 70, 'мл.')

salad = Cook_book('Салат')
print(salad.name)
print(salad.content)
salad.content.append(potatos.ingredients)
salad.content.append(potatos.mass)
salad.content.append(potatos.unit)
print(salad.content)



# def rate_hw(self, student, course, grade):
#     if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
#         if course in student.grades:
#             student.grades[course] += [grade]
#         else:
#             student.grades[course] = [grade]
#     else:
#         return 'Ошибка'


# best_student = Student('Ruoy', 'Eman', 'your_gender')
# best_student.courses_in_progress += ['Python']
#
# cool_mentor = Mentor('Some', 'Buddy')
# cool_mentor.courses_attached += ['Python']
#
# cool_mentor.mix(best_student, 'Python', 10)
# cool_mentor.mix(best_student, 'Python', 10)
# cool_mentor.rate_hw(best_student, 'Python', 10)
#
# print(best_student.grades)



print(potatos.ingredients, potatos.mass, potatos.unit)
print(carrots.ingredients, carrots.mass, carrots.unit)
print(cucumbers.ingredients, cucumbers.mass, cucumbers.unit)
print(pea.ingredients, pea.mass, pea.unit)
print(mayonnaise.ingredients, mayonnaise.mass, mayonnaise.unit)

# print(salad.content)

""" cook = Cook_book('Салат') """
""" cook = Cook_book('Пицца')
cook = Cook_book('Фруктовый десерт') """
""" # print(Cook_book) """




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
]

for dish in cook_book:
  print(f'{dish[0].capitalize()}:')
  for ingredients, weight, measure in dish[1]:
    print(f'{ingredients}, {weight*person} {measure}')
  print() """