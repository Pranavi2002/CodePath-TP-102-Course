# # without dictionaries:
# def find_common_signals(signals1, signals2):
#     ans1 = 0
#     ans2 = 0
#     for signal in signals1:
#         if signal in signals2:
#             ans1 += 1
#     for signal in signals2:
#         if signal in signals1:
#             ans2 += 1
#     ans = []
#     ans.append(ans1)
#     ans.append(ans2)
#     return ans

# with dictionaries:
from collections import Counter

def find_common_signals(signals1, signals2):
    count1 = Counter(signals1)
    count2 = Counter(signals2)

    ans1 = sum(count1[sig] for sig in count1 if sig in count2)
    ans2 = sum(count2[sig] for sig in count2 if sig in count1)

    return [ans1, ans2]

signals1_example1 = [2, 3, 2]
signals2_example1 = [1, 2]
print(find_common_signals(signals1_example1, signals2_example1))

signals1_example2 = [4, 3, 2, 3, 1]
signals2_example2 = [2, 2, 5, 2, 3, 6]
print(find_common_signals(signals1_example2, signals2_example2))

signals1_example3 = [3, 4, 2, 3]
signals2_example3 = [1, 5]
print(find_common_signals(signals1_example3, signals2_example3))