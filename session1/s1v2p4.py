def get_last(items):
    n = len(items)
    if n == 0:
        return None
    else:
        return '"' +''.join(items[n-1]) + '"'

items = ["spider man", "batman", "superman", "iron man", "wonder woman", "black adam"]
print(get_last(items))

items = []
print(get_last(items))