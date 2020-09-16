import datetime
hora = datetime.datetime.now()
print ("hora: ", hora)
resultado = hora + datetime.timedelta(seconds=1)
print ("hora mas 1 segundo: ", resultado)