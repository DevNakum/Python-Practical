# 5....
# Write a Python script to concatenate following dictionaries to create a new one.
# Sample Dictionary :
# dic1={1:10, 2:20}
# dic2={3:30, 4:40}
# dic3={5:50,6:60}
# ExpectedResult : {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}

d1 = {1:10, 2:20}

d2 = {3:30, 4:40}

d3 = {5:50,6:60}

d4 = {}

d4.update(d1)       # {1: 10, 2: 20}
d4.update(d2)       # {1: 10, 2: 20, 3: 30, 4: 40}
d4.update(d3)
print(d4)       # {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}