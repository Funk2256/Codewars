def days_represented(trips):
    all_days = []
    for i in trips:  # iterates "outside" the lists in trips
        for j in range(i[0], i[1] + 1):  # iterates inside the lists
            all_days.append(j)  # appends all days to another list
    return len(set(all_days))


trips = ([[316, 344], [44, 58], [281, 315], [174, 195], [77, 89], [258, 289], [19, 45]])

print(days_represented(trips))
