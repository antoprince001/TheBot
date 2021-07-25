import wikipedia 

query= 'cryptocurrency'
result = 'Acccording to wikipedia,'+ wikipedia.summary(query, sentences=4)
print(result)