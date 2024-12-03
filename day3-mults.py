import re
from pathlib import Path
sum = 0

# part 1
data = Path('data3.txt').read_text()
matches = re.findall('mul\(\d{1,3}\,\d{1,3}\)', data)
i = 0
while i < len(matches):
  nums = re.findall(r'\d+', matches[i])
  sum = sum + (int(nums[0]) * int(nums[1]))
  i = i + 1
print(sum)

#part 2
sum2 = 0
i = 0
with open("data3.txt") as file:
    active = True
    for line in file.readlines():
        matches = list(re.findall(r"mul\(\d{1,3}\,\d{1,3}\)|do\(\)|don\'t\(\)", line))
        for match in matches:
          if match == "do()":
            active = True
          elif match == "don't()":
            active = False
          else:
            if active:
                nums = re.findall(r'\d+', match)
                sum2 = sum2 + (int(nums[0]) * int(nums[1]))
print(sum2)