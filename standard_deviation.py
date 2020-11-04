stats = [12, 13, 16, 17, 26, 6]

def total(stats):
    total = 0
    for stat in stats:
        total += stat
    return total

stats_total = total(stats)

def mean(stats_total, stats):
    mean = stats_total / len(stats)
    return mean

stats_mean = mean(stats_total, stats)

def deviate(stats, stats_mean):
    deviations = []
    for stat in stats:
        deviation = stat - stats_mean
        abs(deviation)
        deviations.append(deviation)
    return deviations

stats_deviations = deviate(stats, stats_mean)

def deviation_square(stats_deviations):
    deviations_squared = []
    for deviation in stats_deviations:
        squared_dev = deviation ** 2
        deviations_squared.append(squared_dev)
    return deviations_squared

d2 = deviation_square(stats_deviations)

def variance(d2):
    d2_total = total(d2)
    variance = d2_total / len(stats)
    return variance

variance =  variance(d2)

def standard_deviation(variance):
     sd = variance ** (0.5)
     return sd

standard_deviation = standard_deviation(variance)

print(round(standard_deviation, 3))



