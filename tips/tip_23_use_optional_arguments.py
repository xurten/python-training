# Tip 23 use optional arguments
# Operator ** allows pass arguments as dictionary

def remainder(number, divisor):
    return number % divisor


my_kwargs = {
    'number': 20,
    'divisor': 7
}
print(remainder(**my_kwargs))


def flow_rate(weight_diff, time_diff):
    return weight_diff / time_diff


print(flow_rate(0.5, 3))


def flow_rate_extend(weight_diff, time_diff, period=1, units_per_kg=1):
    return ((weight_diff * units_per_kg) / time_diff) * period


print(flow_rate_extend(0.5, 3, 3600, 2.2))
