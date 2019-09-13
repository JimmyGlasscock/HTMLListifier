def promptUser():
	print("----- HTML Listifier -----")
	text = input("Enter path of file containing text:")

	return text

def echoHTML(path):
	f = open(path, "r")
	row = f.read()
	row = row.splitlines()
	for items in row:
		items = items.split(',')

		print('<tr>')

		for item in items:
			if(item != None):
				print("\t<td>"+item+"</td>")

		print('</tr>')

path = promptUser()
echoHTML(path)