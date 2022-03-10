from ssl import CertificateError


print('vacature ruimtevuilnisman')
print()
naam = input("Wat is je naam?")
if naam == 'diemaco' or 'Diemaco':
    raise NameError("sorry diemacos nemen wij niet aan.")
else:
    if input('hoeveel praktijkervaring heeft u met dierendressuur? ') > '4':
        if input('welke diploma heeft u? ') == 'MBO-4 ondernemen':
            if input('Typ een salto! ') != '|/-\|':
                if input('kan u vliegend water drinken? ') != 'fdfsfs':
                    if input('ben je ooit in de ruimte geweest? ') != 'fjhsgj':
                        if input('hoeveel kinderen heeft u? ') != 'fgksjhgf':
                            if input('bezit u een Vrachtwagen rijbewijs? ja of nee? ') == 'ja':
                                if input('bent u man met een snor breder dan 10cm of bent u vrouw en draagt rood krulhaar langer dan 20cm? ja of nee? ') == 'ja': 
                                    if input('hoe lang bent u? in hele cm ') > '150':
                                        if input('hoe zwaar bent u? in hele KG ') > '90':
                                            if input('heeft e een Certificaat "Overleven met gevaarlijk personeel?" ja of nee? ') == 'ja':
                                                print('gefeliciteerd u bent aangenomen') 
                                            else: raise CertificateError('helaas u voldoet niet aan de eisen') 
                                        else:print('helaas u voldoet niet aan de eisen')   
                                    else: print('helaas u voldoet niet aan de eisen') 
                                else: print('helaas u voldoet niet aan de eisen') 
                            else: raise CertificateError('helaas u voldoet niet aan de eisen') 
                        else: print('helaas u voldoet niet aan de eisen') 
                    else: print('helaas u voldoet niet aan de eisen') 
                else: print('helaas u voldoet niet aan de eisen') 
            else: print('helaas u voldoet niet aan de eisen') 
        else: raise CertificateError('helaas u voldoet niet aan de eisen')
    else: print('helaas u voldoet niet aan de eisen')  
    
    