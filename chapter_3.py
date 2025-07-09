bicycles = ['trek', 'cannonadale', 'redline', 'specialized']

print(bicycles)
print(type(bicycles))

#Access
print(bicycles[0])
print(bicycles[0].title())

#Last item in list
print(bicycles[-1])


name = ['Perka', 'Mika', 'Zika', 'Leonidas']

print(f"Hello {name[0]}, greetings from Serbia")
print(f"Hello {name[1]}, greetings from Serbia")
print(f"Hello {name[2]}, greetings from Serbia")
print(f"Hello {name[3]}, greetings from Serbia")

motocycles = ['honda', 'yamaha', 'suzuki']

print(motocycles)

motocycles[0] = 'ducati'

print(motocycles)

motocycles.append('honda')

print(motocycles)

motocycles.insert(3, 'bmw')

print(motocycles)