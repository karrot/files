ottawa=int(raw_input())

def timeshift(ottawa,city,cityname):
    x=ottawa-city
    if city>ottawa:
        print 2400+x,"in",cityname
    else:
        print x,"in",cityname
        
print ottawa,"in Ottawa"
timeshift(ottawa,300,"Victoria")
timeshift(ottawa,200,"Edmonton")
timeshift(ottawa,100,"Winnipeg")
timeshift(ottawa,0,"Toronto")
timeshift(ottawa,-100,"Halifax")
timeshift(ottawa,-130,"St. John's")
