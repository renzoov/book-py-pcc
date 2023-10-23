favorite_languages = {
  'jen': 'python',
  'sarah': 'c',
  'edward': 'rust',
  'phil': 'python',
}

language = favorite_languages['sarah'].title()
print(f"Sarah's favorite language is {language}.")

print("\n------------------------------\n")

for name, language in favorite_languages.items():
  print(f"{name.title()}'s favorite language is {language.title()}.")
  
print("\n------------------------------\n")

for name in favorite_languages.keys():
  print(name.title())
  
print("\n------------------------------\n")

for name in sorted(favorite_languages.keys()):
  print(f"{name.title()}, thank you for taking the poll.")
  
print("\n------------------------------\n")

print("The following languages have been mentioned:")

for language in favorite_languages.values():
  print(language.title())
  
print("\n------------------------------\n")

favorite_languages = {
  'jen': ['python', 'rust'],
  'sarah': ['c'],
  'edward': ['rust', 'go'],
  'phil': ['python', 'haskell'],
}

for name, languages in favorite_languages.items():
  print(f"\n{name.title()}'s favorite languages are:")
  for language in languages:
    print(f"\t{language.title()}")