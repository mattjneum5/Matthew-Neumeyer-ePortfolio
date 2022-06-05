#!/usr/bin/python3

#### import the cgi module to handle data passed from the browser
import cgi

#### create an object storing the data passed from the browser
data = cgi.FieldStorage()

#### retrieve the data values
customer = data.getvalue('Name')
city = data.getvalue('city')
cardnumber = data.getvalue('cardnumber')
cardtype = data.getvalue('cardtype')

#### print the first line of the HTML response 
print('Content-type:text/html\r\n\r\n')


#### html templates
header = '''	
	<html>
	<head>
		<title>Buy Your Way to a Better Health!</title>
		<link rel="stylesheet" href="lab3.css" />
	</head>

	<body>
'''

thanks = '''
		<h1>Thanks!</h1>
		<p>Your information has been recorded.</p>
		<dl>
'''

sorry = '''
		<h1>Sorry</h1>
		<p>You did not fill out the form compeletly. <a href="lab3.html">Try again?</a></p>
		<dl>
'''

trailer = '''
		</dl>
	</body>
</html>  
'''

#### define the main function
def main():
	#### print html header
	print(header)

	def luhn_checksum(cardnumber):
		def digits_of(n):
			 return [int(d) for d in str(n)]
		digits = digits_of(cardnumber)
		odd_digits = digits[-1::-2]
		even_digits = digits[-2::-2]
		checksum = 0
		checksum += sum(odd_digits)
		for d in even_digits:
        		checksum += sum(digits_of(d*2))
		return checksum % 10

	#### print values passed to the server by the form
	if customer!=None and city!=None and cardnumber!=None and cardtype!=None:
		print(thanks)

		print('''
			<dt>Name</dt>
				<dd> 
			%s </dd>''' %customer)

		print('''
			<dt>City</dt>
				<dd> 
			%s </dd>''' %city)

		print('''
			<dt>Credit Card</dt>
				<dd> 
			%s </dd>''' %(cardnumber.strip() + " (" + cardtype + ")"))

		print("<p>Here are all the customers who have submitted here:</p>")

		f=open("lab3.txt", "a+")
		f.write(customer + cardnumber + cardtype)
		f.close()

		print("<pre>")
		f = open("lab3.txt", "r")
		#### read the lab3.txt file and display the information submitted
		print("<p>Name;Number;Type</p>")
		print(customer, cardnumber, cardtype)
		f.close()

		print("</pre>")

		luhn_checksum(cardnumber)

	else:
		#### print sorry
		print(sorry)		

	if cardtype == "visa" and str(cardnumber).startswith('4') and len(cardnumber) == 16 and luhn_checksum(cardnumber) == 0:
		print("<p> This is a valid Visa card")
	
	elif cardtype == "mastercard" and str(cardnumber).startswith('5') and len(cardnumber) == 16 and luhn_checksum(cardnumber) == 0:
		print("<p> This is a valid Master card <p>")

	elif cardtype == "" or cardnumber == "" or str(cardnumber).startswith('1', '2', '3', '6', '7', '8', '9') or len(cardnumber) != 16 or luhn_checksum(cardnumber) !=0: 
		print("<p> You didn't provide a valid card number.<a href='lab3.html'>Try again?</a></p>")

	else:
		#### print sorry
		print(sorry)
		
#### print html trailer
print(trailer)


#### call the main function
main()
