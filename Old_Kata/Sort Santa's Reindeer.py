def sort_reindeer(reindeer_names):
    lt = [x.split(' ')[1] for x in reindeer_names]

    return sorted(reindeer_names, key=lambda name: name.split()[1])


print(sort_reindeer(['Kenjiro Mori', 'Susumu Tokugawa', 'Juzo Okita', 'Akira Sanada']))
