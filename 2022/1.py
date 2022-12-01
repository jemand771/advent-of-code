import util

data = util.load_input(1)
grouped = []
current_group = []
for line in data:
    if not (stripped := line.strip()):
        grouped.append(current_group)
        current_group = []
        continue
    current_group.append(int(stripped))
grouped.append(current_group)

print("highest:", max(sum(group) for group in grouped))
print("sum of highest 3:", sum(list(sorted((sum(group) for group in grouped), reverse=True))[:3]))
