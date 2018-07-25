import requests
import lxml.html
# from robobrowser import RoboBrowser

s = requests.session()

login_url = "https://academia.srmuniv.ac.in/"

login = s.get(login_url)
login_html = lxml.html.fromstring(login.text)

hidden_inputs = login_html.xpath(r'//form//input[@type="hidden"]')
form = {x.attrib["name"]: x.attrib["value"] for x in hidden_inputs}
print(form)

form = {
	"username":"",
	"password":"",
	"client_portal":"true",
	"serviceurl":"https://academia.srmuniv.ac.in/",
	"servicename":"ZohoCreator",
	"portal":"10002227248",
	"service_language":"en",
	"is_ajax":"true",
	"grant_type":"password"
}

headers = {
	# "Accept":"*/*",
	"Accept-Encoding": "gzip, deflate, br",
	"Accept-Language": "en-US,en;q=0.9",
	"Connection": "keep-alive",
	"Content-Length": "229",
	"Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
	"Cookie": "IAM_TEST_COOKIE=IAM_TEST_COOKIE; _ga=GA1.3.2074912917.1485098723; 3884164421=cd8a4b406568daaeec71b8df22d9ec99; zccpn=bbb0d544-dec6-44db-acd3-2914bf9fa94f; clientauthtoken=; ZCNEWUIPUBLICPORTAL=false; a42ea4520c=d8fe4612aeeef35bc503fe11aa818ae2; a8c61fa0dc=412d04ceb86ecaf57aa7a1d4903c681d; iamcsr=deafea36-7ce7-4647-b7d3-f7623df70169; BetaFeature=1; JSESSIONID=5BC82DB4155DB79BABA78A422B94621E",
	"DNT": "1",
	"Host": "academia.srmuniv.ac.in",
	"Origin": "https://academia.srmuniv.ac.in",
	"Referer": "https://academia.srmuniv.ac.in/accounts/signin?_sh=false&hideidp=true&portal=10002227248&client_portal=true&servicename=ZohoCreator&serviceurl=https://academia.srmuniv.ac.in/&service_language=en",
	"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36"
}

response = s.post(login_url, data=form, headers=headers)

print(response.url)

# browser = RoboBrowser()
# form = browser.get_form(id="signinForm")