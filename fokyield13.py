def foksiyon_yield(xxx):
   for meyve in xxx:
    yield meyve

meyveler = ["muz","karadut","elma"]
output = foksiyon_yield(meyveler)
print(output)
print(next(output))
print(next(output))