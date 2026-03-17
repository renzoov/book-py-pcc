from pathlib import Path

path = Path('pi_digits.txt')
contents = path.read_text(encoding='utf-8')

lines = contents.splitlines()
for line in lines:
    print(line)