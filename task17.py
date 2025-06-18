names = []
n = int(input("Nechta ism kiritmoqchisiz: "))
for i in range(n):
    name = input(f"{i+1}-ism kiriting: ")
    names.append(name)

print("Ismlar ruyxati: ", names)
print("Ismlar soni: ", len(names))