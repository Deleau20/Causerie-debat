from faker import Faker

r = Faker(locale="fr_FR")

for _ in range(10):
    print(r.job())