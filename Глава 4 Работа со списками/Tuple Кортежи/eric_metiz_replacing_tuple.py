
"""
Замена кортежа
Элементы кортежа не могут изменяться, но можно присвоить новое значение переменной, в которой хранится кортеж. Таким
образом, для изменения размеров прямоугольника, следует переопределить весь кортеж.
"""

dimensions = (200, 50)
print("Оригинальный прямоугольник:")
for dimension in dimensions:
    print(dimension)

dimensions = (400, 100)
print("\nМодифицируемый прямоугольник:")
for dimension in dimensions:
    print(dimension)
