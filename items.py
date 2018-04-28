plant_types = {"orchid": "flower", "cedar": "tree", "maple": "tree"}

for key, value in plant_types.items():
	print(key)
	print(value)
	


top_female_names = []
for key, val in name_counts.items():
    if val == 2:
	top_female_names.append(key)
  