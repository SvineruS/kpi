import re

pattern = re.compile(r"\b[А-Яа-я]+\s[А-Яа-я]+")


assert pattern.match("Слово Ещеслово") is not None
assert pattern.match("Слово    Ещеслово") is None
assert pattern.match("Не123Слово Слово") is None
assert pattern.findall("лфогврт123фыв Слово Ещеслово 1235%*") == ['Слово Ещеслово']
