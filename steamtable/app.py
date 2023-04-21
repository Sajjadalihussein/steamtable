# This is for import library flask and request and render templat
from flask import Flask , render_template,request,config

# This function for sturated(Mixture)
# This functions for water steam
app = Flask(__name__)
@app.route("/",methods=["GET"])
def index():
    
    return render_template("index.html")


@app.route("/saturated",methods=["GET"])
def saturated():
    title_of_text = "saturated_of_water"
    # To check i have a request get
    title = "Saturated water"
    if request.method == "GET":
        #open file of properties values
        file = open(f"{title_of_text}.txt")
        # This varible we need it to find select one and select two of property
        i = 0
        sel_pro_1 = request.args.get("sel_pro_1")
        sel_pro_2 = request.args.get("sel_pro_2")
        value_of_proprty = request.args.get("value_of_proprty")
        # This Dic we need it to link the value of proprtey in text in the selected ,when the value of property in text it's like the Dic value(1=t,2=p...)
        
        pro_0 = {
            "T":0,
            "p":1,
        }
        pro = {
            "T":0,
            "p":1,
            "vf":2,
            "vg":3,
            "uf":4,
            "ug":5,
            "hf":6,
            "hg":7,
            "hfg":8,
            "sf":9,
            "sg":10,
            "sfg":11
                    }
        # This is we need it to find value of selected and check it if in selected or not
        key_0 = list(pro_0.keys())
        key = list(pro.keys())
        unit_0 = ["°C","KPa"] 
        unit = ["°C","KPa","m3/kg","m3/kg","kJ/kg","kJ/kg","kJ/kg","kJ/kg","kJ/kg",
                "kJ/(kg K)","kJ/(kg K)","kJ/(kg K)"]
        eq = " = "
        mtx = []
        for line_0 in file:
            li_0 = line_0.split()
            for li_00 in li_0:
                mtx.append(li_00)
        first_value_of_temp = mtx[0]
        secound_value_of_temp = mtx[-13]
        first_value_of_pressure = mtx[1]
        secound_value_of_pressure = mtx[-12]
        file = open(f"{title_of_text}.txt")
        if sel_pro_1 in key_0 and sel_pro_2 in key and value_of_proprty != None:
            try:
                float(value_of_proprty)
            except:
                mes = "Please type numbers only"
                return render_template("saturated.html",key_0=key_0,key=key,unit_0=unit_0,title=title,mes=mes)
            if sel_pro_1 == "T":
                if float(value_of_proprty) < float(first_value_of_temp) or float(value_of_proprty) > float(secound_value_of_temp):
                    return render_template("saturated.html",title=title,key_0=key_0,key=key,mes=f"The value of temprture should be between {first_value_of_temp} and {secound_value_of_temp} °C")
            if sel_pro_1 == "p":
                if float(value_of_proprty) < float(first_value_of_pressure) or float(value_of_proprty) > float(secound_value_of_pressure):
                    return render_template("saturated.html",title=title,key_0=key_0,key=key,mes=f"The value of pressure should be between {first_value_of_pressure} and {secound_value_of_pressure} Kpas")

            for line in file:
                li = line.split()
                # This loop for extrat the select one and two
                while i < len(key):        
                    if sel_pro_1 == key[i]:
                        # the varible a is the select one imean the value known to user
                        a = key[i]
                        aa = unit[i]
                    elif sel_pro_2 == key[i]:
                        # This varible is the value the user want it
                        b = key[i]
                        # This varible for unit of proprtey
                        bb = unit[i]
                    i +=1
                if sel_pro_1 == sel_pro_2:
                    mes = "Please select diffrent proprty "
                    return render_template("saturated.html",key_0=key_0,key=key,mes=mes,title=title)
                elif float(value_of_proprty) < float(value_of_proprty) *-1:
                    mes = "Please, Enter postive value"
                    return render_template("saturated.html",key_0=key_0,key=key,mes=mes,title=title)
                # This stetment if the value of proprtey in the text 
                elif float(value_of_proprty) == float(li[pro[a]]):
                    resulte=float(li[pro[b]])
                    return render_template("saturated.html",key_0=key_0,key=key,resulte=resulte ,eq=eq ,b=b,bb=bb,title=title)
                # This statment if the value of proprtey is not in the values of text so it's make interpolation
                elif float(value_of_proprty) != float(li[pro[a]]):
                    # This statment to make a first point one and two for interpolation
                    if float(value_of_proprty) > float(li[pro[a]]):
                        x1 = float(li[pro[a]])
                        y1 = float(li[pro[b]])
                        # This statment to make a secound point one and two for interpolation
                    elif float(value_of_proprty) < float(li[pro[a]]):
                        x2 = float(li[pro[a]])
                        x = float(value_of_proprty)
                        y2 = float(li[pro[b]])
                        sub_x = x - x1
                        sub_y = y2 - y1
                        sub_xx = x2-x1
                        dev = float(sub_y/sub_xx)
                        mul = float(dev * sub_x)
                        resulte = round(float(y1 + mul),8)
                        return render_template("saturated.html",key_0=key_0,key=key,resulte=resulte,aa=aa ,eq=eq ,b=b,bb=bb,title=title)
         
        file.close()
        return render_template("saturated.html",key_0=key_0,key=key,unit_0=unit_0,title=title)
    else:
         return render_template("saturated.html",key_0=key_0,key=key,unit_0=unit_0,title=title)


@app.route("/superheated",methods=["GET"])
def superheated():
    title = "Superheated water"
    if request.method == "GET":
        #open file of properties values
        title_of_text = "superheated_of_water"
        file = open(f"{title_of_text}.txt","r")
                
        # This varible we need it to find select one and select two of property
        i = 0
        sel_pro_1 = request.args.get("sel_pro_1")
        sel_pro_2 = request.args.get("sel_pro_2")
        value_of_proprty = request.args.get("value_of_proprty")
        value_of_pressure = request.args.get("value_of_pressure")
        # This Dic we need it to link the value of proprtey in text in the selected ,when the value of property in text it's like the Dic value(1=t,2=p...)
        pro_0 = {
             "T":0,
        }
        pro = {
            "T":0,
            "v":1,
            "u":2,
            "h":3,
            "s":4
            
                    }
        unit = ["°C","m3/kg","kJ/kg","kJ/kg","kJ/kg·K"]
        eq = " = "
        # This is we need it to find value of selected and check it if in selected or not
        key_0 = list(pro_0.keys())
        key = list(pro.keys())
        
        file_0 = open(f"{title_of_text}.txt","r")
        lis_0 = []
        for line_0 in file_0:
            li_0 = line_0.split() 
            r  =0 
            if len(li_0) == 1:
                
                while r < len(li_0):
                    lis_0.append(li_0[i])
                    r+=1
                    
        the_first_value_in_pressure = float(lis_0[0])
        the_end_value_in_pressure = float(lis_0[-1])
        
        if sel_pro_1 in key_0 and sel_pro_2 in key and value_of_proprty != None and value_of_pressure !=None:
            
            try:
                float(value_of_proprty)
                float(value_of_pressure)
            except:
                mes = "Please type numbers only"
                return render_template("superheated.html",key_0=key_0,key=key,mes=mes,title=title) 
            if float(value_of_pressure) < float(the_first_value_in_pressure) or float(value_of_pressure) > float(the_end_value_in_pressure):
                mes = f"The value of pressure should be between {the_first_value_in_pressure} and {the_end_value_in_pressure} (Kpas)"
                return render_template("superheated.html",key_0=key_0,key=key,mes=mes,title=title)
            
            while i < len(key):        
                    if sel_pro_1 == key[i]:
                        # the varible a is the select one 
                        a = key[i]
                    elif sel_pro_2 == key[i]:
                        # This varible is the value the user want it
                        b = key[i]
                        bb = unit[i]
                        # This varible for unit of proprtey
                    i +=1
            li_w = []
            for line in file:
                li = line.split()
                if len(li) == 1 and float(value_of_pressure) == float(li[0]):
                    for line_2 in file:
                        li_2 = line_2.split()     
                        if len(li_2) == 1:
                            break
                        i = 0
                        while i < len(li_2):
                            li_w.append(li_2[i])
                            i+=1
                    rr = {
                        0:-5,
                        1:-4,
                        2:-3,
                        3:-2,
                        4:-1
                    }
                    e = pro[sel_pro_1]
                    g = rr[e]
                    value_one_of_range = li_w[int(e)]
                    value_two_of_rang= li_w[int(g)]
            if sel_pro_1 in key and sel_pro_2 in key and value_of_proprty != None and value_of_pressure !=None:
                # This case for pro and pressure required is find in the tabel 
                file_2 = open(f"{title_of_text}.txt","r")        
                for line_3 in file_2:
                    li_3 = line_3.split()
                    if float(value_of_pressure) == float(li_3[0]) and len(li_3) == 1:
                        for line_4 in file_2:
                            li_4 = line_4.split()
                            if len(li_4) == 1:
                                break
                            if float(value_of_proprty) == float(li_4[pro[a]]):
                                # this returne from table
                                resulte = li_4[pro[b]]
                                return render_template("superheated.html",key_0=key_0,key=key,resulte =resulte ,eq=eq ,b=b,bb=bb,title=title )
                            if float(value_of_proprty) < float(value_one_of_range) or float(value_of_proprty) > float(value_two_of_rang):
                                mes = f"The value of temprutre should be between {value_one_of_range} and {value_two_of_rang} (°C)"
                                return render_template("superheated.html",key_0=key_0,key=key,mes=mes,title=title)
                            # This is if we need interrpolation between the temprture ,that is mean the value of pressure required is in the table
                            elif float(value_of_proprty) > float(value_one_of_range) and float(value_of_proprty) < float(value_two_of_rang):
                                if len(li_4) == 1:
                                    break
                                elif float(value_of_proprty) > float(li_4[pro[a]]):
                                    x1 = float(li_4[pro[a]])
                                    y1 = float(li_4[pro[b]])
                                elif float(value_of_proprty) < float(li_4[pro[a]]):
                                    x2 = float(li_4[pro[a]])
                                    x = float(value_of_proprty)
                                    y2 = float(li_4[pro[b]])
                                    sub_x = x - x1
                                    sub_y = y2 - y1
                                    sub_xx = x2-x1
                                    dev = float(sub_y/sub_xx)
                                    mul = float(dev * sub_x)
                                    resulte = round(float(y1 + mul),8)
                                    return render_template("superheated.html",key_0=key_0,key=key,resulte = resulte,title=title ,eq=eq ,b=b,bb=bb)
             
            if sel_pro_1 in key and sel_pro_2 in key and value_of_proprty != None and value_of_pressure !=None:
                if float(value_of_pressure) > the_first_value_in_pressure and float(value_of_pressure) < float(the_end_value_in_pressure):
                    for h in lis_0:
                        if float(value_of_pressure) > float(h):
                            df = float(h)
                        if float(value_of_pressure) < float(h):
                            dr = float(h)
                            break
                    # This is for the value of pressure is not equle any value of pressure in the table but the pro required is find it
                    file_3 = open(f"{title_of_text}.txt","r")
                    for line_5 in file_3:
                        li_5 = line_5.split()
                        if float(li_5[0]) == float(df) and len(li_5) == 1:
                            for line_6 in file_3:
                                li_6 = line_6.split()
                                if float(value_of_proprty) == float(li_6[pro[a]]):
                                    x_1 = float(df) 
                                    y_1  = float(li_6[pro[b]])
                                elif float(li_6[0]) == float(dr) and len(li_6) == 1:
                                    for line_7 in file_3:
                                        li_7 = line_7.split()
                                        if len(li_7) == 1:
                                            break
                                        # This interpolation between the diffrent pressure
                                        if float(value_of_proprty) == float(li_7[pro[a]]):
                                            x_x = float(value_of_pressure)
                                            x_2 = float(dr)
                                            y_2  = float(li_7[pro[b]])
                                            sub_x = x_x - x_1
                                            sub_y = y_2 - y_1
                                            sub_xx = x_2 - x_1
                                            dev = float(sub_y/sub_xx)
                                            mul = float(dev*sub_x)
                                            resulte = round(float(y_1+mul),8)
                                            return render_template("superheated.html",key_0=key_0,key=key,resulte=resulte ,eq=eq ,b=b,bb=bb,title=title)
            # This is double interplation
            if sel_pro_1 in key_0 and sel_pro_2 in key and value_of_proprty != None and value_of_pressure !=None:
                if float(value_of_pressure) > the_first_value_in_pressure and float(value_of_pressure) < float(the_end_value_in_pressure):
                        file_4 = open(f"{title_of_text}.txt","r")

                        for line_8 in file_4:
                            li_8 = line_8.split()
                            lo = []
                            lp = []
                            if float(li_8[0]) == float(df):
                                for line_9 in file_4:
                                    li_9 = line_9.split()
                                      
                                    if float(value_of_proprty) > float(li_9[pro[a]]):
                                        tmp1_df = float(li_9[pro[a]])
                                        pot1_df = float(li_9[pro[b]])
                                    if float(value_of_proprty) < float(li_9[pro[a]]):
                                        tmp2_df = float(li_9[pro[a]])
                                        pot2_df = float(li_9[pro[b]])
                                        break
                                                    
                            if float(li_8[0]) == float(dr):
                                for line_10 in file_4:
                                    li_10 = line_10.split()
                                    if float(value_of_proprty) > float(li_10[pro[a]]):
                                        tmp1_dr = float(li_10[pro[a]])
                                        pot1_dr = float(li_10[pro[b]])
                                    if float(value_of_proprty) < float(li_10[pro[a]]):
                                        tmp2_dr = float(li_10[pro[a]])
                                        pot2_dr = float(li_10[pro[b]])
                                        break
                                
                                tmp_df_dr = float(value_of_proprty)
                                # This is for pressure 1
                                num_1_df = float(tmp_df_dr)- float(tmp1_df)
                                num_2_df = float(pot2_df) - float(pot1_df)
                                dnum_df = float(tmp2_df) - float(tmp1_df)
                                div_df = (num_1_df *num_2_df)/dnum_df
                                pot_df = float(pot1_df) + float(div_df)
                                # This is for pressure 2
                                num_1_dr = float(tmp_df_dr)- float(tmp1_dr)
                                num_2_dr = float(pot2_dr) - float(pot1_dr)
                                dnum_dr = float(tmp2_dr) - float(tmp1_dr)
                                div_dr = (num_1_dr *num_2_dr)/dnum_dr
                                pot_dr = float(pot1_dr) + float(div_dr)
                               
                                # final interpolation
                                num_1 = float(pot_dr) - float(pot_df)
                                num_2 = float(value_of_pressure) - float(df)
                                dnum = float(dr) - float(df)
                                div_f = (float(num_1) * float(num_2)) / dnum
                                potr = float(pot_df) + float(div_f)
                          
                                resulte = round(potr,8)
                                return render_template("superheated.html",key_0=key_0,key=key,resulte=resulte,title=title ,eq=eq ,b=b,bb=bb)
                                
        return render_template("superheated.html",key_0=key_0,key=key,resulte="App end",title=title) 
           

@app.route("/compressed_liquid_water",methods=["GET"])
def compressed_liquid_water():
    title_of_text = "compressed_liquid_of_water"
    if request.method == "GET":
        #open file of properties values
        title = "Compressed liquid water"
        file = open(f"{title_of_text}.txt","r")
                
        # This varible we need it to find select one and select two of property
        i = 0
        sel_pro_1 = request.args.get("sel_pro_1")
        sel_pro_2 = request.args.get("sel_pro_2")
        value_of_proprty = request.args.get("value_of_proprty")
        value_of_pressure = request.args.get("value_of_pressure")
        # This Dic we need it to link the value of proprtey in text in the selected ,when the value of property in text it's like the Dic value(1=t,2=p...)
        pro_0 = {
             "T":0,
        }
        pro = {
            "T":0,
            "v":1,
            "u":2,
            "h":3,
            "s":4
            
                    }
        unit = ["°C","m3/kg","kJ/kg","kJ/kg","kJ/kg·K"]
        eq = " = "
        # This is we need it to find value of selected and check it if in selected or not
        key_0 = list(pro_0.keys())
        key = list(pro.keys())
        
        file_0 = open(f"{title_of_text}.txt","r")
        lis_0 = []
        for line_0 in file_0:
            li_0 = line_0.split() 
            r  =0 
            if len(li_0) == 1:
                
                while r < len(li_0):
                    lis_0.append(li_0[i])
                    r+=1
                    
        the_first_value_in_pressure = float(lis_0[0])
        the_end_value_in_pressure = float(lis_0[-1])
        
        if sel_pro_1 in key_0 and sel_pro_2 in key and value_of_proprty != None and value_of_pressure !=None:
            
            try:
                float(value_of_proprty)
                float(value_of_pressure)
            except:
                mes = "Please type numbers only"
                return render_template("superheated.html",key_0=key_0,key=key,mes=mes,title=title) 
            if float(value_of_pressure) < float(the_first_value_in_pressure) or float(value_of_pressure) > float(the_end_value_in_pressure):
                mes = f"The value of pressure should be between {the_first_value_in_pressure} and {the_end_value_in_pressure} (Kpas)"
                return render_template("superheated.html",key_0=key_0,key=key,mes=mes,title=title)
            
            while i < len(key):        
                    if sel_pro_1 == key[i]:
                        # the varible a is the select one 
                        a = key[i]
                    elif sel_pro_2 == key[i]:
                        # This varible is the value the user want it
                        b = key[i]
                        bb = unit[i]
                        # This varible for unit of proprtey
                    i +=1
            li_w = []
            for line in file:
                li = line.split()
                if len(li) == 1 and float(value_of_pressure) == float(li[0]):
                    for line_2 in file:
                        li_2 = line_2.split()     
                        if len(li_2) == 1:
                            break
                        i = 0
                        while i < len(li_2):
                            
                            li_w.append(li_2[i])
                            i+=1
                    rr = {
                        0:-5,
                        1:-4,
                        2:-3,
                        3:-2,
                        4:-1
                    }
                    e = pro[sel_pro_1]
                    g = rr[e]
                    value_one_of_range = li_w[int(e)]
                    value_two_of_rang= li_w[int(g)]
            if sel_pro_1 in key and sel_pro_2 in key and value_of_proprty != None and value_of_pressure !=None:
                # This case for pro and pressure required is find in the tabel 
                file_2 = open(f"{title_of_text}.txt","r")        
                for line_3 in file_2:
                    li_3 = line_3.split()
                    if float(value_of_pressure) == float(li_3[0]) and len(li_3) == 1:
                        for line_4 in file_2:
                            li_4 = line_4.split()
                            if len(li_4) == 1:
                                break
                            if float(value_of_proprty) == float(li_4[pro[a]]):
                                # this returne from table
                                resulte = li_4[pro[b]]
                                return render_template("superheated.html",key_0=key_0,key=key,resulte =resulte ,eq=eq ,b=b,bb=bb,title=title )
                            if float(value_of_proprty) < float(value_one_of_range) or float(value_of_proprty) > float(value_two_of_rang):
                                mes = f"The value of temprutre should be between {value_one_of_range} and {value_two_of_rang} (°C)"
                                return render_template("superheated.html",key_0=key_0,key=key,mes=mes,title=title)
                            # This is if we need interrpolation between the temprture ,that is mean the value of pressure required is in the table
                            elif float(value_of_proprty) > float(value_one_of_range) and float(value_of_proprty) < float(value_two_of_rang):
                                if len(li_4) == 1:
                                    break
                                elif float(value_of_proprty) > float(li_4[pro[a]]):
                                    x1 = float(li_4[pro[a]])
                                    y1 = float(li_4[pro[b]])
                                elif float(value_of_proprty) < float(li_4[pro[a]]):
                                    x2 = float(li_4[pro[a]])
                                    x = float(value_of_proprty)
                                    y2 = float(li_4[pro[b]])
                                    sub_x = x - x1
                                    sub_y = y2 - y1
                                    sub_xx = x2-x1
                                    dev = float(sub_y/sub_xx)
                                    mul = float(dev * sub_x)
                                    resulte = round(float(y1 + mul),8)
                                    return render_template("superheated.html",key_0=key_0,key=key,resulte = resulte,title=title ,eq=eq ,b=b,bb=bb)
             
            if sel_pro_1 in key and sel_pro_2 in key and value_of_proprty != None and value_of_pressure !=None:
                if float(value_of_pressure) > the_first_value_in_pressure and float(value_of_pressure) < float(the_end_value_in_pressure):
                    for h in lis_0:
                        if float(value_of_pressure) > float(h):
                            df = float(h)
                        if float(value_of_pressure) < float(h):
                            dr = float(h)
                            break
                    # This is for the value of pressure is not equle any value of pressure in the table but the pro required is find it
                    file_3 = open(f"{title_of_text}.txt","r")
                    for line_5 in file_3:
                        li_5 = line_5.split()
                        if float(li_5[0]) == float(df) and len(li_5) == 1:
                            for line_6 in file_3:
                                li_6 = line_6.split()
                                if float(value_of_proprty) == float(li_6[pro[a]]):
                                    x_1 = float(df) 
                                    y_1  = float(li_6[pro[b]])
                                elif float(li_6[0]) == float(dr) and len(li_6) == 1:
                                    for line_7 in file_3:
                                        li_7 = line_7.split()
                                        if len(li_7) == 1:
                                            break
                                        # This interpolation between the diffrent pressure
                                        if float(value_of_proprty) == float(li_7[pro[a]]):
                                            x_x = float(value_of_pressure)
                                            x_2 = float(dr)
                                            y_2  = float(li_7[pro[b]])
                                            sub_x = x_x - x_1
                                            sub_y = y_2 - y_1
                                            sub_xx = x_2 - x_1
                                            dev = float(sub_y/sub_xx)
                                            mul = float(dev*sub_x)
                                            resulte = round(float(y_1+mul),8)
                                            return render_template("superheated.html",key_0=key_0,key=key,resulte=resulte ,eq=eq ,b=b,bb=bb,title=title)
            # This is double interplation
            if sel_pro_1 in key and sel_pro_2 in key and value_of_proprty != None and value_of_pressure !=None:
                if float(value_of_pressure) > the_first_value_in_pressure and float(value_of_pressure) < float(the_end_value_in_pressure):
                        file_4 = open(f"{title_of_text}.txt","r")
                        for line_8 in file_4:
                            li_8 = line_8.split()
                            lo = []
                            lp = []
                            if float(li_8[0]) == float(df):
                                for line_9 in file_4:
                                    li_9 = line_9.split()
                                    
                                    qa = 0
                                    while qa < len(li_9):
                                        if len(li_9) == 1:
                                            break
                                        lo.append(li_9[qa])
                                        qa+=1
                                    
                                    if float(value_of_proprty) > float(li_9[pro[a]]):
                                        tmp1_df = float(li_9[pro[a]])
                                        pot1_df = float(li_9[pro[b]])
                                    if float(value_of_proprty) < float(li_9[pro[a]]):
                                        tmp2_df = float(li_9[pro[a]])
                                        pot2_df = float(li_9[pro[b]])
                                        break                               
                            if float(li_8[0]) == float(dr):
                                for line_10 in file_4:
                                    li_10 = line_10.split()
                                    if float(value_of_proprty) > float(li_10[pro[a]]):
                                        tmp1_dr = float(li_10[pro[a]])
                                        pot1_dr = float(li_10[pro[b]])
                                    if float(value_of_proprty) < float(li_10[pro[a]]):
                                        tmp2_dr = float(li_10[pro[a]])
                                        pot2_dr = float(li_10[pro[b]])
                                        break
                                tmp_df_dr = float(value_of_proprty)
                                # This is for pressure 1
                                num_1_df = float(tmp_df_dr)- float(tmp1_df)
                                num_2_df = float(pot2_df) - float(pot1_df)
                                dnum_df = float(tmp2_df) - float(tmp1_df)
                                div_df = (num_1_df *num_2_df)/dnum_df
                                pot_df = float(pot1_df) + float(div_df)
                                # This is for pressure 2
                                num_1_dr = float(tmp_df_dr)- float(tmp1_dr)
                                num_2_dr = float(pot2_dr) - float(pot1_dr)
                                dnum_dr = float(tmp2_dr) - float(tmp1_dr)
                                div_dr = (num_1_dr *num_2_dr)/dnum_dr
                                pot_dr = float(pot1_dr) + float(div_dr)
                               
                                # final interpolation
                                num_1 = float(pot_dr) - float(pot_df)
                                num_2 = float(value_of_pressure) - float(df)
                                dnum = float(dr) - float(df)
                                div_f = (float(num_1) * float(num_2)) / dnum
                                potr = float(pot_df) + float(div_f)
                          
                                resulte = round(potr,8)
                                return render_template("superheated.html",key_0=key_0,key=key,resulte=resulte,title=title ,eq=eq ,b=b,bb=bb)
                                
        return render_template("superheated.html",key_0=key_0,key=key,resulte="App end",title=title) 
    
# This functions for  refrigerant-134a
@app.route("/saturated_refrigerant_134a",methods=["GET"])
def saturated_of_refrigerant_134a():
    title_of_text = "saturated_of_refrigerant-134a"
    title_of_page_html = "saturated_refrigerant_134a"
    # To check i have a request get
    title = "Saturated refrigerant-134a"
    if request.method == "GET":
        #open file of properties values
        file = open(f"{title_of_text}.txt")
        # This varible we need it to find select one and select two of property
        i = 0
        sel_pro_1 = request.args.get("sel_pro_1")
        sel_pro_2 = request.args.get("sel_pro_2")
        value_of_proprty = request.args.get("value_of_proprty")
        # This Dic we need it to link the value of proprtey in text in the selected ,when the value of property in text it's like the Dic value(1=t,2=p...)
        
        pro_0 = {
            "T":0,
            "p":1,
        }
        pro = {
            "T":0,
            "p":1,
            "vf":2,
            "vg":3,
            "uf":4,
            "ug":5,
            "hf":6,
            "hg":7,
            "hfg":8,
            "sf":9,
            "sg":10,
            "sfg":11
                    }
        # This is we need it to find value of selected and check it if in selected or not
        key_0 = list(pro_0.keys())
        key = list(pro.keys())
        unit_0 = ["°C","KPa"] 
        unit = ["°C","KPa","m3/kg","m3/kg","kJ/kg","kJ/kg","kJ/kg","kJ/kg","kJ/kg",
                "kJ/(kg K)","kJ/(kg K)","kJ/(kg K)"]
        eq = " = "
        mtx = []
        for line_0 in file:
            li_0 = line_0.split()
            for li_00 in li_0:
                mtx.append(li_00)
        first_value_of_temp = mtx[0]
        secound_value_of_temp = mtx[-13]
        first_value_of_pressure = mtx[1]
        secound_value_of_pressure = mtx[-12]
        file = open(f"{title_of_text}.txt")
        if sel_pro_1 in key_0 and sel_pro_2 in key and value_of_proprty != None:
            try:
                float(value_of_proprty)
            except:
                mes = "Please type numbers only"
                return render_template(f"{title_of_page_html}.html",key_0=key_0,key=key,unit_0=unit_0,title=title,mes=mes)
            if sel_pro_1 == "T":
                if float(value_of_proprty) < float(first_value_of_temp) or float(value_of_proprty) > float(secound_value_of_temp):
                    return render_template(f"{title_of_page_html}.html",title=title,key_0=key_0,key=key,mes=f"The value of temprture should be between {first_value_of_temp} and {secound_value_of_temp} °C")
            if sel_pro_1 == "p":
                if float(value_of_proprty) < float(first_value_of_pressure) or float(value_of_proprty) > float(secound_value_of_pressure):
                    return render_template(f"{title_of_page_html}.html",title=title,key_0=key_0,key=key,mes=f"The value of pressure should be between {first_value_of_pressure} and {secound_value_of_pressure} Kpas")

            for line in file:
                li = line.split()
                # This loop for extrat the select one and two
                while i < len(key):        
                    if sel_pro_1 == key[i]:
                        # the varible a is the select one imean the value known to user
                        a = key[i]
                        aa = unit[i]
                    elif sel_pro_2 == key[i]:
                        # This varible is the value the user want it
                        b = key[i]
                        # This varible for unit of proprtey
                        bb = unit[i]
                    i +=1
                if sel_pro_1 == sel_pro_2:
                    mes = "Please select diffrent proprty "
                    return render_template(f"{title_of_page_html}.html",key_0=key_0,key=key,mes=mes,title=title)
                # This stetment if the value of proprtey in the text 
                elif float(value_of_proprty) == float(li[pro[a]]):
                    resulte=float(li[pro[b]])
                    return render_template(f"{title_of_page_html}.html",key_0=key_0,key=key,resulte=resulte ,eq=eq ,b=b,bb=bb,title=title)
                # This statment if the value of proprtey is not in the values of text so it's make interpolation
                elif float(value_of_proprty) != float(li[pro[a]]):
                    # This statment to make a first point one and two for interpolation
                    if float(value_of_proprty) > float(li[pro[a]]):
                        x1 = float(li[pro[a]])
                        y1 = float(li[pro[b]])
                        # This statment to make a secound point one and two for interpolation
                    elif float(value_of_proprty) < float(li[pro[a]]):
                        x2 = float(li[pro[a]])
                        x = float(value_of_proprty)
                        y2 = float(li[pro[b]])
                        sub_x = x - x1
                        sub_y = y2 - y1
                        sub_xx = x2-x1
                        dev = float(sub_y/sub_xx)
                        mul = float(dev * sub_x)
                        resulte = round(float(y1 + mul),8)
                        return render_template(f"{title_of_page_html}.html",key_0=key_0,key=key,resulte=resulte,aa=aa ,eq=eq ,b=b,bb=bb,title=title)
         
        file.close()
        return render_template(f"{title_of_page_html}.html",key_0=key_0,key=key,unit_0=unit_0,title=title)
    else:
         return render_template(f"{title_of_page_html}.html",key_0=key_0,key=key,unit_0=unit_0,title=title)



@app.route("/superheated_refrigerant_134a",methods=["GET"])
def superheated_refrigerant_134a():
    title = "Superheated refrigerant-134a"
    if request.method == "GET":
        #open file of properties values
        title_of_text = "superheated_refrigerant_134a"
        title_of_page_html = "superheated_refrigerant_134a"
        file = open(f"{title_of_text}.txt","r")
                
        # This varible we need it to find select one and select two of property
        i = 0
        sel_pro_1 = request.args.get("sel_pro_1")
        sel_pro_2 = request.args.get("sel_pro_2")
        value_of_proprty = request.args.get("value_of_proprty")
        value_of_pressure = request.args.get("value_of_pressure")
        # This Dic we need it to link the value of proprtey in text in the selected ,when the value of property in text it's like the Dic value(1=t,2=p...)
        pro_0 = {
             "T":0,
        }
        pro = {
            "T":0,
            "v":1,
            "u":2,
            "h":3,
            "s":4
            
                    }
        unit = ["°C","m3/kg","kJ/kg","kJ/kg","kJ/kg·K"]
        eq = " = "
        # This is we need it to find value of selected and check it if in selected or not
        key_0 = list(pro_0.keys())
        key = list(pro.keys())
        
        file_0 = open(f"{title_of_text}.txt","r")
        lis_0 = []
        for line_0 in file_0:
            li_0 = line_0.split() 
            r  =0 
            if len(li_0) == 1:
                
                while r < len(li_0):
                    lis_0.append(li_0[i])
                    r+=1
                    
        the_first_value_in_pressure = float(lis_0[0])
        the_end_value_in_pressure = float(lis_0[-1])
        
        if sel_pro_1 in key_0 and sel_pro_2 in key and value_of_proprty != None and value_of_pressure !=None:
            
            try:
                float(value_of_proprty)
                float(value_of_pressure)
            except:
                mes = "Please type numbers only"
                return render_template(f"{title_of_page_html}.html",key_0=key_0,key=key,mes=mes,title=title) 
            if float(value_of_pressure) < float(the_first_value_in_pressure) or float(value_of_pressure) > float(the_end_value_in_pressure):
                mes = f"The value of pressure should be between {the_first_value_in_pressure} and {the_end_value_in_pressure} (Kpas)"
                return render_template(f"{title_of_page_html}.html",key_0=key_0,key=key,mes=mes,title=title)
            
            while i < len(key):        
                    if sel_pro_1 == key[i]:
                        # the varible a is the select one 
                        a = key[i]
                    elif sel_pro_2 == key[i]:
                        # This varible is the value the user want it
                        b = key[i]
                        bb = unit[i]
                        # This varible for unit of proprtey
                    i +=1
            li_w = []
            for line in file:
                li = line.split()
                if len(li) == 1 and float(value_of_pressure) == float(li[0]):
                    for line_2 in file:
                        li_2 = line_2.split()     
                        if len(li_2) == 1:
                            break
                        i = 0
                        while i < len(li_2):
                            
                            li_w.append(li_2[i])
                            i+=1
                    rr = {
                        0:-5,
                        1:-4,
                        2:-3,
                        3:-2,
                        4:-1
                    }
                    e = pro[sel_pro_1]
                    g = rr[e]
                    value_one_of_range = li_w[int(e)]
                    value_two_of_rang= li_w[int(g)]
            if sel_pro_1 in key and sel_pro_2 in key and value_of_proprty != None and value_of_pressure !=None:
                # This case for pro and pressure required is find in the tabel 
                file_2 = open(f"{title_of_text}.txt","r")        
                for line_3 in file_2:
                    li_3 = line_3.split()
                    if float(value_of_pressure) == float(li_3[0]) and len(li_3) == 1:
                        for line_4 in file_2:
                            li_4 = line_4.split()
                            if len(li_4) == 1:
                                break
                            if float(value_of_proprty) == float(li_4[pro[a]]):
                                # this returne from table
                                resulte = li_4[pro[b]]
                                return render_template("superheated.html",key_0=key_0,key=key,resulte =resulte ,eq=eq ,b=b,bb=bb,title=title )
                            if float(value_of_proprty) < float(value_one_of_range) or float(value_of_proprty) > float(value_two_of_rang):
                                mes = f"The value of temprutre should be between {value_one_of_range} and {value_two_of_rang} (°C)"
                                return render_template(f"{title_of_page_html}.html",key_0=key_0,key=key,mes=mes,title=title)
                            # This is if we need interrpolation between the temprture ,that is mean the value of pressure required is in the table
                            elif float(value_of_proprty) > float(value_one_of_range) and float(value_of_proprty) < float(value_two_of_rang):
                                if len(li_4) == 1:
                                    break
                                elif float(value_of_proprty) > float(li_4[pro[a]]):
                                    x1 = float(li_4[pro[a]])
                                    y1 = float(li_4[pro[b]])
                                elif float(value_of_proprty) < float(li_4[pro[a]]):
                                    x2 = float(li_4[pro[a]])
                                    x = float(value_of_proprty)
                                    y2 = float(li_4[pro[b]])
                                    sub_x = x - x1
                                    sub_y = y2 - y1
                                    sub_xx = x2-x1
                                    dev = float(sub_y/sub_xx)
                                    mul = float(dev * sub_x)
                                    resulte = round(float(y1 + mul),8)
                                    return render_template(f"{title_of_page_html}.html",key_0=key_0,key=key,resulte = resulte,title=title ,eq=eq ,b=b,bb=bb)
             
            if sel_pro_1 in key and sel_pro_2 in key and value_of_proprty != None and value_of_pressure !=None:
                if float(value_of_pressure) > the_first_value_in_pressure and float(value_of_pressure) < float(the_end_value_in_pressure):
                    for h in lis_0:
                        if float(value_of_pressure) > float(h):
                            df = float(h)
                        if float(value_of_pressure) < float(h):
                            dr = float(h)
                            break
                    # This is for the value of pressure is not equle any value of pressure in the table but the pro required is find it
                    file_3 = open(f"{title_of_text}.txt","r")
                    for line_5 in file_3:
                        li_5 = line_5.split()
                        if float(li_5[0]) == float(df) and len(li_5) == 1:
                            for line_6 in file_3:
                                li_6 = line_6.split()
                                if float(value_of_proprty) == float(li_6[pro[a]]):
                                    x_1 = float(df) 
                                    y_1  = float(li_6[pro[b]])
                                elif float(li_6[0]) == float(dr) and len(li_6) == 1:
                                    for line_7 in file_3:
                                        li_7 = line_7.split()
                                        if len(li_7) == 1:
                                            break
                                        # This interpolation between the diffrent pressure
                                        if float(value_of_proprty) == float(li_7[pro[a]]):
                                            x_x = float(value_of_pressure)
                                            x_2 = float(dr)
                                            y_2  = float(li_7[pro[b]])
                                            sub_x = x_x - x_1
                                            sub_y = y_2 - y_1
                                            sub_xx = x_2 - x_1
                                            dev = float(sub_y/sub_xx)
                                            mul = float(dev*sub_x)
                                            resulte = round(float(y_1+mul),8)
                                            return render_template(f"{title_of_page_html}.html",key_0=key_0,key=key,resulte=resulte ,eq=eq ,b=b,bb=bb,title=title)
            # This is double interplation
            if sel_pro_1 in key and sel_pro_2 in key and value_of_proprty != None and value_of_pressure !=None:
                if float(value_of_pressure) > the_first_value_in_pressure and float(value_of_pressure) < float(the_end_value_in_pressure):
                        file_4 = open(f"{title_of_text}.txt","r")
                        for line_8 in file_4:
                            li_8 = line_8.split()
                            lo = []
                            lp = []
                            if float(li_8[0]) == float(df):
                                for line_9 in file_4:
                                    li_9 = line_9.split()
                                    
                                    qa = 0
                                    while qa < len(li_9):
                                        if len(li_9) == 1:
                                            break
                                        lo.append(li_9[qa])
                                        qa+=1
                                    
                                    if float(value_of_proprty) > float(li_9[pro[a]]):
                                        tmp1_df = float(li_9[pro[a]])
                                        pot1_df = float(li_9[pro[b]])
                                    if float(value_of_proprty) < float(li_9[pro[a]]):
                                        tmp2_df = float(li_9[pro[a]])
                                        pot2_df = float(li_9[pro[b]])
                                        break                               
                            if float(li_8[0]) == float(dr):
                                for line_10 in file_4:
                                    li_10 = line_10.split()
                                    if float(value_of_proprty) > float(li_10[pro[a]]):
                                        tmp1_dr = float(li_10[pro[a]])
                                        pot1_dr = float(li_10[pro[b]])
                                    if float(value_of_proprty) < float(li_10[pro[a]]):
                                        tmp2_dr = float(li_10[pro[a]])
                                        pot2_dr = float(li_10[pro[b]])
                                        break
                                tmp_df_dr = float(value_of_proprty)
                                # This is for pressure 1
                                num_1_df = float(tmp_df_dr)- float(tmp1_df)
                                num_2_df = float(pot2_df) - float(pot1_df)
                                dnum_df = float(tmp2_df) - float(tmp1_df)
                                div_df = (num_1_df *num_2_df)/dnum_df
                                pot_df = float(pot1_df) + float(div_df)
                                # This is for pressure 2
                                num_1_dr = float(tmp_df_dr)- float(tmp1_dr)
                                num_2_dr = float(pot2_dr) - float(pot1_dr)
                                dnum_dr = float(tmp2_dr) - float(tmp1_dr)
                                div_dr = (num_1_dr *num_2_dr)/dnum_dr
                                pot_dr = float(pot1_dr) + float(div_dr)
                               
                                # final interpolation
                                num_1 = float(pot_dr) - float(pot_df)
                                num_2 = float(value_of_pressure) - float(df)
                                dnum = float(dr) - float(df)
                                div_f = (float(num_1) * float(num_2)) / dnum
                                potr = float(pot_df) + float(div_f)

                                resulte = round(potr,8)
                                return render_template(f"{title_of_page_html}.html",key_0=key_0,key=key,resulte=resulte,title=title ,eq=eq ,b=b,bb=bb)
                                
        return render_template(f"{title_of_page_html}.html",key_0=key_0,key=key,resulte="App end",title=title) 
           

if __name__ == "__main__":
     app.run(debug=True ,port=8080,use_reloader=False)
     
     
     
