with open("recipes.txt", encoding="utf8") as file:
    cook_book={}
    file=file.readlines() #общий список со всеми рецептами из txt
    oneList=[] #список с одним рецептом
    for i in file:
        oneList.append(i)
        if i=="\n": #обозначаем конец блюда
            ingrDict={}
            key=oneList[0].strip("\n")
            cook_book[key]=[]
            for ingr in oneList[2:-1]: #пробегаемся по ингридиентам
                ingr=ingr.split("|")
                ingrDict["ingredient_name"]=ingr[0].strip(" ")
                ingrDict["quantity"]=int(ingr[1])
                ingrDict["measure"]=ingr[2].strip("\n ")
                cook_book[key]+=[ingrDict]
                ingrDict={}
            oneList.clear() #очищаем список, чтобы работать со след.рецептом


#print(cook_book)


def get_shop_list_by_dishes(*dishes, person_count=1):
    result={}
    for i in dishes:
        ingr=cook_book[i]
        for j in ingr:
            name=j["ingredient_name"]
            mea=j["measure"]
            if name not in result:
                value=j["quantity"]*person_count
            else:
                value+=j["quantity"]*person_count+person_count
            result[name]={"measure":mea,"quantity":value}
    print(result)


get_shop_list_by_dishes("Омлет","Фахитос", person_count=2)




