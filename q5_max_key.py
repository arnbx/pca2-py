def max_key(d):
    return max(d, key=d.get)

scores = {"Ann": 70, "Bob": 95, "Cy": 88}
print(max_key(scores))
