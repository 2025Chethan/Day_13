d={"chethan":[1,2,3,4,5,6,7,8,9,(9,8,7,6,5,4,3,2,1,{'suresh':(2,4,6,8,[1,3,5,7,9])})]}

#if given variable is dictnory, then find out the type of chethan key value otherwise print prabhas.
#if value is list find out the secound element data type. 
#if second element data type is tuple, thenm find out the last element data type. 
#if last elemenet data type is dictnory, then prient appu otherwise print yash.


print(type(d))
if type(d) is dict:
    print("chethan")
else:
    print("prabhas")

print(d['chethan'])
print(type(d['chethan']))

print(d["chethan"][9])
print(type(d["chethan"][9]))
print(d["chethan"][9][9]["suresh"][4])
print(type(d["chethan"][9][9]["suresh"][4]))
if (type(d["chethan"][9][9]["suresh"][4]))==dict:
    print("appu")
else:
    print("yash")