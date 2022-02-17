
hambre = True
sed = True

if hambre and not sed:
    print('Tenemos hambre!')
elif hambre and sed:
    print('Tenemos hambre y sed')
else:
    print('Estamos llenos!')
# > Tenemos hambre y sed