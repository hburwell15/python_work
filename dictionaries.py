favorite_numbers = {
	'frank': [13, 22, 16], 
	'mona': [17, 2, 7], 
	'jimmy': [25, 100, 66], 
	'hannah': [15, 3, 20], 
	}
franks_number = favorite_numbers.get('frank')
print('frank: ' + str(franks_number))
monas_number = favorite_numbers.get('mona')
print('mona: ' + str(monas_number))
jimmys_number = favorite_numbers.get('jimmy')
print('jimmy: ' + str(jimmys_number))
hannahs_number = favorite_numbers.get('hannah')
print('hannah: ' + str(hannahs_number))