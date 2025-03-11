'''#Current Bill Problem
Write  a  program  to  determine  bill  amount  and  input  is  units

Units                                                      Cost
------------------------------------------------------------
First  100  units								Rs. 3.00 / unit

Next  100  units								Rs. 3.50 / unit

Next  200  units								Rs. 4.00 / unit

Next  300  units								Rs. 4.50 / unit

Above  700  units								Rs. 5.00 / unit
'''

units=int(input("Enter units: "))
match units//100:
	case 0:
		cost=units*3.0
		print(cost)
	case 1:
		cost=100*3.0+(units-100)*3.5
		print(cost)
	case 2|3:
		cost=100*3.0+100*3.5+(units-200)*4.0
		print(cost)
	case 4|5|6:
		cost=100*3.0+100*3.5+200*4.0+(units-400)*4.5
		print(cost)
	case _:
		cost=100*3.0+100*3.5+200*4.0+300*4.5+(units-700)*5.0
		print(cost)