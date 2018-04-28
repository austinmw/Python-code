top_male_names = []
male_name_counts = {}
for row in legislators:
	if row[3] == "M" and row[7] > 1940:
		name = row[1]
		if name in male_name_counts:
			male_name_counts[name] = male_name_counts[name] + 1
		else:
			male_name_counts[name] = 1

highest_value = None
for name,count in male_name_counts.items():
	if highest_value is None or count > highest_value:
		highest_value = count

for name,count in male_name_counts.items():
	if count == highest_value:
		top_male_names.append(name)