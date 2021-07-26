import wikipedia 

query= 'cryptocurrency'
result = 'Acccording to wikipedia,'+ wikipedia.summary(query, sentences=2)
print(result)