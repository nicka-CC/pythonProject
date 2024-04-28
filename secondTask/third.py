dictionary = {1: 11, 2: 22, 3: 33, 4: 4, 5: 33, 6: 1}
keySet = set(dictionary.keys())
valueSet = set(dictionary.values())
mnozhestvo1 = keySet | valueSet
mnozhestvo2 = {(k,v) for k, v in dictionary.items()}
print("Множество ключей: ", keySet)
print("Множество значений: ", valueSet)
print("Объединенное множество: ", mnozhestvo1)
print("Объединенноё множество, где ключ соответствует значению: ", mnozhestvo2)