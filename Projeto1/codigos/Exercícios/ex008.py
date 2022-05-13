

#Crie um algoritmo que receba um valor em metros e o exiba em centímetros e milímetros.
m = float(input('Insira o valor de metros a ser calculado: '))
cm = float(m*100)
mm = float(m*1000)
dm = float(m*10)
km = float(m/1000)
dam = float(m/10)
hm = float(m/100)

print ('O valor de {} metros \n Convertido para centímetros é igual a {:.0f} cm \n Convertido para milímetros é igual a {:.0f} mm'.format(m, cm, mm))
print ('Convertido para decímetros e igual a {:.4f} dm \n Convertido para quilômetros e igual a {:.4f} km \n Convertido para decâmetros é igual a {:.4f} dam \n Convertido para hectômetros é igual a {:.4f} hm'.format(dm, km, dam, hm))