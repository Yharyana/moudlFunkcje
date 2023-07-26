#print("hello funckje")
#def fukncja_parametrem(i):
#    for j in range (1,i+1):
#        print(j)

#fukncja_parametrem(20)

#def best_grade_sub(list):
#    best_sb = None
#    best_gr = 0
#   real_br=0
#    for subject,grade in list.items():
#        best_gr=max(grade)
#        if real_br<best_gr:
##            real_br=best_gr
 #           best_sb=subject
 #   return best_sb,real_br
#dzienniczek={
#    "matma":[2,4,5,1],
#    "polish":[2,5,6],
#    "eng":[2,1,3,7]
#}#

#bs,br=best_grade_sub(dzienniczek)
#print(f"naj ocenka {br} a subject to {bs}")

#zadanka

#def prostokat(a,b):
#    return a*b

#a=int(input("podaj a"))
#b=int(input("podaj b"))
#pole=prostokat(a,b)
#print(f"pole to {pole} jendostek kwadraotwych")

#def srednia_predkosc(czas,dystans):
#   return dystans/czas



#to zl ejest chyba idk co miałem zrobic zopabcze na filmiku
#f oblicz_dec():
#    while True:
#        category_name = input("Podaj kategorię wydatków albo zakończ wpisując 'X': ")
#        if category_name == "X":
#            break
#        expenditures[category_name] = []
#
 #       while True:
  #          expenditure = input(
   #             f"Podaj wartość następnego wydatku w kategorii {category_name} albo zakończ wpisując 'X': ")
    ###
       #     expenditure_value = float(expenditure)
        #    expenditures[category_name].append(expenditure_value)
#print("Kalkulator budżetu miesięcznego")
#expenditures = {}
#
#oblicz_dec()


#total_expenditures = 0
#for category_expenditures in expenditures.values():
 #   total_expenditures += sum(category_expenditures)


#expenditures_percentage = {}
#for category_name, category_expenditures in expenditures.items():
  #  total_category_expenditures = sum(category_expenditures)
 #   expenditures_percentage[category_name] = total_category_expenditures * 100 / total_expenditures
#
#most_important_category = None
#most_important_category_percentage = 0
#for category, percentage in expenditures_percentage.items():
   #
#if most_important_category is not None:
 #   print(f"Najwięcej wydajesz na {most_important_category} - {most_important_category_percentage:.0f}% wszystkich wydatków")

#for category, percentage in expenditures_percentage.items():
  #  print(f"Na {category} wydajesz {percentage:.0f}% miesięcznych wydatków")


  #okej to juz kumam z filmiku nex

  #Argumenty p[ozycyjne  i nazwane


#def avg_speed(distance, time):
#    return distance / time
#def run_avg_speed_calculator(vehicle_name):
#    distance = float(input(f"Ile km pokonałeś/pokonałaś za pomocą {vehicle_name}? "))
#    time = float(input("Ile godzin Ci to zajęło? "))
#    average_speed = avg_speed(distance=distance, time=time)
#    print(f"Twoja średnia prędkość przemieszczania się za pomocą {vehicle_name} to {average_speed}km/h")

#run_avg_speed_calculator(vehicle_name="biegu")
#run_avg_speed_calculator("roweru")
#run_avg_speed_calculator("samochodu")

#parametry domyślne

#print("domyslny sepraratos","llolo")
#print("nie domyslny sepraratos","llolo",sep="---")


