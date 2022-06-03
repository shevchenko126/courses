
a = 'Hello'
b = ' World!'
print( a+b )
print(len(a))


s = ["a", "b", "crrrrrr"]
t = ["x", "i", "yhyhyh"]
print(s[1])
s.append(t)
t.sort()


print( t )


f = ("a", "b", "crrrrrr") #tuple

statuses = ("published", "not published", "trash")

print( f[0] )

f = ["a", "a","a", "a","a", "a","a", "a","a", "a", "b","b","b", "crrrrrr"]
d = set(f)

print(d)

dict_ex = {
    "key1":{
        "fff1":"sss",
        "fff2":"sss",
        "fff3":["fff", "ssss"],
    },
    "key2":"value2",
    "key3":"value3",
    "key4":"value4"
}

print(dict_ex["key1"]["fff3"][1])



dict_homework = {
    "key1":{
        "d":44,
        "f":None,
        "s":{
            8:44,
            9:None,
            10:{"mm":["s", "GET ME", 7]},
        },
    },
    "key2":{
        "fff1":44,
        "f":None,
    },
}
