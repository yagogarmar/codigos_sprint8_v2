from textblob import TextBlob
texto = "My sister is a bad person"
blob = TextBlob(texto)
sentimiento = blob.sentiment
polaridad = sentimiento.polarity
print(polaridad)

if polaridad < 0:
    print("Sentimineto negativo")
elif polaridad > 0:
    print("Sentimineto positivo")
