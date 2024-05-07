names = ['Finland', 'Sweden', 'Norway','Denmark','Iceland', 'Estonia','Russia']

def unpack_nordic(a,b,c,d,e,f,g):
    return [a,b,c,d,e]

def unpack_es(a,b,c,d,e,f,g):
    return f

def unpack_rs(a,b,c,d,e,f,g):
    return g

nordic_countries = unpack_nordic(*names)

es = unpack_es(*names)

rs = unpack_rs(*names)

print(nordic_countries)

print(es)

print(rs)