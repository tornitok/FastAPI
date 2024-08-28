def extract_elements(element) -> str:
    return element[1::2]


a = 'РОЗА'
result = extract_elements(a)
print(result)
