
def chequear_numero_par_en_lista(num_list):

    for number in num_list:
        if number % 2 == 0:
            print('True')
            return True
        else:
            pass
    print('False')
    return False

chequear_numero_par_en_lista([1, 3, 5]) # Impares es False
chequear_numero_par_en_lista([2, 4, 6]) # ares es True