
for x in range(65):
    if(x>0):
        #string = ("<a class=\"pin pin--5-ZZZ\" id=\"Pin YYY\" data-category=\"0\" data-space=\"YYY\" href=\"#\" aria-label=\"Pin for YYY\">\n<span class=\"pin__icon\">\n<svg class=\"icon icon--pin\">\n<use xlink:href=\"#icon-pin\"></use>\n</svg>\n<svg class=\"icon icon--numeric--1 icon--number-XXX\">\n<use xlink:href=\"#icon-number-XXX\"></use>\n</svg>\n<svg class=\"icon icon--numeric--2 icon--number-WWW\">\n<use xlink:href=\"#icon-number-WWW\"></use>\n</svg>\n</span>\n</a>")
        string= ("<div class=\"content__item\" id=\"Content YYY\" data-space=\"YYY\" data-category=\"0\" >\n <img class=\"content__item-picture\" id=\"Pic YYY\"></img>\n <h3 class=\"content__item-title\" id=\"ConTittle YYY\">Vacant (YYY)</h3>\n<div class=\"content__item-details\">\n<p class=\"content__meta\">\n<span class=\"content__meta-item\" id=\"Status YYY\"><strong>Status:</strong></span>\n<span class=\"content__meta-item\" id=\"Email YYY\"><strong>Email:</strong></span>\n<span class=\"content__meta-item\" id=\"Phone YYY\"><strong>Phone:</strong></span>\n</p>\n</div>\n</div>")
        #string=("<li id=\"LL YYY\" data-level=\"1\" data-category=\"0\" data-space=\"YYY\"><a id=\"LLc YYY\" href=\"#\"></a></li>")
        no1=int(x/10)
        no2=int(x%10)
        no3=(x/100)+5
        no3=round(no3,2)
        s_no3=str(no3).replace(".","")
        if(len(s_no3)==2):
            s_no3+="0"
        n_string = string.replace("ZZZ",str(x)).replace("YYY",str(s_no3)).replace("XXX",str(no1)).replace("WWW",str(no2))
        #print(".pin--5-"+str(x)+" { top: px; left: px; }")
        print(n_string)
