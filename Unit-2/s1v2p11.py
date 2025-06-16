from collections import Counter
def frequency_sort(signals):

    # freq = {}
    # for signal in signals:
    #     if signal in freq:
    #         freq[signal] += 1
    #     else:
    #         freq[signal] = 1

    freq = Counter(signals)
    
    #sort by increasing frequency (freq[x]), then decreasing value when frequencies tie (-x)
    sorted_signals = sorted(signals, key=lambda x: (freq[x], -x))

    return sorted_signals

signals1 = [1, 1, 2, 2, 2, 3]
signals2 = [2, 3, 1, 3, 2]
signals3 = [-1, 1, -6, 4, 5, -6, 1, 4, 1]

print(frequency_sort(signals1)) 
print(frequency_sort(signals2)) 
print(frequency_sort(signals3))