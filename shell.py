import gora

while True:
	text = input("G.O.R.A. >> ")
	result, error = gora.run("<stdlib> ",text)

	if error:
		print(error.as_string())
	else:
		print(result)