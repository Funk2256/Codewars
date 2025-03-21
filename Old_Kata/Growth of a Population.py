def nb_year(population, percent, aug, target):
    year = 0
    while population < target:
        population += population * percent / 100 + aug
        year += 1
    return year


print(nb_year(1500000, 0.25, 1000, 2000000))
