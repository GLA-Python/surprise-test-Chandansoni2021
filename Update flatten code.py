def flatten(dct):
    def recusor(parentK,givenVal):
        if type(givenVal)!=dict:
            o[parentK]= givenVal
            return
        else:
            for eachchildK in givenVal.keys():
                if(eachchildK==""):
                    recusor(parentK, givenVal[eachchildK])
                else:
                    if parentK!="":
                        recusor(parentK+"."+eachchildK,givenVal[eachchildK])
                    else:
                        recusor(eachchildK,givenVal[eachchildK])  
    o = {}
    for eachK in dct.keys():
        recusor(eachK,dct[eachK])   
    return o                               
dct = {"key":3,  "foo":{"a":5, "bar":{"baz":8}}}
print(flatten(dct))

#{"key":3, "foo.a":5, "foo.bar.baz":8}