values = [None, 10, 20, 30, None, 50]
checks = []
checks = [x is not None and x > 30 for x in values]

print(checks)