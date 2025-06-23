def find_the_log_conc_val(logs):
    str_logs = [str(log) for log in logs]
    sum = 0
    while len(str_logs):
        if len(str_logs) >= 2:
            c = str_logs[0] + str_logs[len(str_logs) - 1]
            sum += int(c)
            str_logs.pop(0)
            str_logs.pop(len(str_logs) - 1)
        else:
            sum += int(str_logs[len(str_logs) - 1])
            str_logs.pop(len(str_logs) - 1)
    return sum

print(find_the_log_conc_val([7, 52, 2, 4])) 
print(find_the_log_conc_val([5, 14, 13, 8, 12])) 