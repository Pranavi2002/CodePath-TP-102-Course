def data_difference(experiment1, experiment2):
    return dict((key, val) for key, val in experiment1.items() 
    if key in experiment2 and experiment2[key] != val
    or key not in experiment2)

exp1_data = {'temperature': 22, 'pressure': 101.3, 'humidity': 45}
exp2_data = {'temperature': 18, 'pressure': 101.3, 'radiation': 0.5}

print(data_difference(exp1_data, exp2_data))