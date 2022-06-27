from country import Country

#create countries
#Thailand lat = 13.7649136 , 100.5360959
#population = 70,078,203
#area = 513,120
#temp = 32 C

c1 = Country('Thailand',513120,70078203)
c1.setcordinate(13.7649136,100.5360959)
c1.setcelciues(32)
c1.showdetail()

#China 34.4149507,86.0530732
#Population: 1,412,600,000
#area = 9,597,000
#temp = 27 C

c2 = Country('China',9597000,1412600000)
c2.setcordinate(34.4149507,86.0530732)
c2.setcelciues(27)
c2.showdetail()

#Egypt 26.8349495,26.3821971
#pop = 105,838,455
#area = 1,001,450
#temp = 25

c3 = Country('Egypt',1001450,105838455)
c3.setcordinate(26.8349495,26.3821971)
c3.setcelciues(25)
c3.showdetail()