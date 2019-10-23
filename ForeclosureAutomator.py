from selenium import webdriver
import zillow
from re import sub
from decimal import Decimal
from zcrmsdk import ZCRMRestClient, ZCRMRecord, ZCRMModule, ZCRMUser, ZCRMException, ZohoOAuth
import zcrmsdk
from google_images_download import google_images_download



def getimage():
    response = google_images_download.googleimagesdownload()  # class instantiation
    keyword = address.replace(",", "") + ' ' + citystatezip.replace(",", "")
    keyword.replace('\n'," ")
    arguments = {"keywords": keyword, "limit": 1, "specific_site" : "https://zillow.com/"}  # creating list of arguments
    paths = response.download(arguments)  # passing the arguments to the function
    print paths[0]
    try:
        path = '/' + str(paths[0]).split("'/")[1]
        print path
        path = path[:-3]
        print path
        record = zcrmsdk.ZCRMRecord.get_instance('Leads', resp.data.entity_id)
        record.upload_photo(path)
    except IndexError:
        print "error"
        pass
def check():
    if Zestimate_New is not None and approxupset is not None:
        zestimate_upset = Zestimate_New / approxupset
        zestimate_upset = round(zestimate_upset, 3)
    else:
        zestimate_upset = 0.0
    pass
    newrecord.set_field_value('Zestimate_Upset', zestimate_upset)
    return (zestimate_upset)


with open("/home/noahbenezra/PycharmProjects/untitled3/venv/bin/config/zillow key.conf", 'r') as f:
    key = f.readline().replace("\n", "")

url = 'https://salesweb.civilview.com/Sales/SalesSearch?countyId=2'
driver = webdriver.Chrome("/home/noahbenezra/PycharmProjects/untitled3/Selenium Resource/chromedriver")


options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.binary_location = "/usr/bin/chromium"
##options.add_argument('--headless')
options.add_argument('/home/noahbenezra/.cache/google-chrome/Default/')
options.add_argument("--user-data-dir=/home/noahbenezra/.config/google-chrome/Default") # change to profile path
options.add_argument('--profile-directory=Noah')


driver.get(url)

details = [detail.get_attribute('href') for detail in driver.find_elements_by_partial_link_text("Details")]
for details in details[646:]:
    driver.get(details)
    auctiondate = driver.find_element_by_css_selector('body > div > div.table-responsive > table:nth-child(1) > tbody > tr:nth-of-type(-n+606)').text
    driver.implicitly_wait(1)
    sheriff = driver.find_element_by_css_selector('body > div > div.table-responsive > table:nth-child(1) > tbody > tr:nth-child(1) > td:nth-child(2)').text.replace("u'", '')
    street = driver.find_element_by_css_selector('body > div > div.table-responsive > table:nth-child(1) > tbody > tr:nth-child(6) > td:nth-child(2)').text
    courtcase = driver.find_element_by_css_selector('body > div > div.table-responsive > table:nth-child(1) > tbody > tr:nth-child(2) > td:nth-child(2)').text
    salesdate = driver.find_element_by_css_selector('body > div > div.table-responsive > table:nth-child(1) > tbody > tr:nth-child(3) > td:nth-child(2)').text
    plaintiff = driver.find_element_by_css_selector('body > div > div.table-responsive > table:nth-child(1) > tbody > tr:nth-child(4) > td:nth-child(2)').text.replace("u'", '')
    defendant = driver.find_element_by_css_selector('body > div > div.table-responsive > table:nth-child(1) > tbody > tr:nth-child(5) > td:nth-child(2)').text
    description = driver.find_element_by_css_selector('body > div > div.table-responsive > table:nth-child(1) > tbody > tr:nth-child(7) > td:nth-child(2)').text
    approxupset = driver.find_element_by_css_selector('body > div > div.table-responsive > table:nth-child(1) > tbody > tr:nth-child(8) > td:nth-child(2)').text
    attorney = driver.find_element_by_css_selector('body > div > div.table-responsive > table:nth-child(1) > tbody > tr:nth-child(9) > td:nth-child(2)').text
    attorneyphone = driver.find_element_by_css_selector('body > div > div.table-responsive > table:nth-child(1) > tbody > tr:nth-child(10) > td:nth-child(2)').text
        #county = driver.find_element_by_xpath('//h3').text
        #county = county.split(",")[1]
    label = driver.find_element_by_xpath('/html/body/div/div[2]/table[1]/tbody/tr[7]/td[1]').text
    if label=='Priors :':
        attorney = driver.find_element_by_css_selector(
            'body > div > div.table-responsive > table:nth-child(1) > tbody > tr:nth-child(8) > td:nth-child(2)').text
        approxupset = driver.find_element_by_css_selector(
            'body > div > div.table-responsive > table:nth-child(1) > tbody > tr:nth-child(9) > td:nth-child(2)').text
        priors = driver.find_element_by_xpath('/html/body/div/div[2]/table[1]/tbody/tr[7]/td[2]')
        approxupset = Decimal(sub(r'[^\d.]', '', approxupset))
        approxupset = float(approxupset)

    else:
        approxupset = driver.find_element_by_css_selector('body > div > div.table-responsive > table:nth-child(1) > tbody > tr:nth-child(8) > td:nth-child(2)').text
        approxupset = Decimal(sub(r'[^\d.]', '', approxupset))
        approxupset = float(approxupset)
    try:
        searchstreet, searchcityzip = street.split("\n",1)
        address = searchstreet
        citystatezip = searchcityzip
    except ValueError:
        print "no address"
        continue
    api = zillow.ValuationApi()
    deep_results = api.GetDeepSearchResults(key, address, citystatezip)
    resultsdict = deep_results.get_dict()
    config = {
    "sandbox": "False",
    "applicationLogFilePath": "./log",
    "client_id": "1000.M4WLRMKKQ6Z1261586Z7BJZZX7AIVH",
    "client_secret": "5b64aa3ac92e9ca017dbde2231cceb127239ce1427",
    "redirect_uri": "https://www.localhost:8080/some_path",
    "accounts_url": "https://accounts.zoho.com",
    "token_persistence_path": ".",
    "currentUserEmail": "elie@buyabeautifulhome.com"
    }
    ZCRMRestClient.initialize(config)
    newrecord = zcrmsdk.ZCRMRecord.get_instance('Leads')  # Module API Name

    Zestimate_New = resultsdict['zestimate']['amount']

    newrecord.set_field_value('Last_Name', searchstreet)  # This method use to set FieldApiName and value similar to all other FieldApis and Custom field
    newrecord.set_field_value('Street', searchstreet)
    newrecord.set_field_value('City', resultsdict['full_address']['city'])
    newrecord.set_field_value('Zip', resultsdict['full_address']['zipcode'])
    newrecord.set_field_value('Status', resultsdict['full_address']['street'])
    newrecord.set_field_value('Property_Type', resultsdict['extended_data']['usecode'])
    newrecord.set_field_value('Sq_Ft', resultsdict['extended_data']['finished_sqft'])
    newrecord.set_field_value('Year_Built', resultsdict['extended_data']['year_built'])
    newrecord.set_field_value('Lot_Size', resultsdict['extended_data']['lot_size_sqft'])
    newrecord.set_field_value('Baths', resultsdict['extended_data']['bathrooms'])
    newrecord.set_field_value('Beds_for_Import', resultsdict['extended_data']['bedrooms'])
    newrecord.set_field_value('Zestimate_New', Zestimate_New)
    newrecord.set_field_value('Total_Assessment', resultsdict['extended_data']['tax_assessment'])
    newrecord.set_field_value('Zillow_Link', resultsdict['links']['home_details'])
    newrecord.set_field_value('Assessment_Year', resultsdict['extended_data']['tax_assessment_year'])
    newrecord.set_field_value('Zestimate_Low', resultsdict['zestimate']['valuation_range_low'])
    newrecord.set_field_value('Zestimate_High', resultsdict['zestimate']['valuation_range_high'])
    newrecord.set_field_value('Court_Case', courtcase)
    newrecord.set_field_value('Auction_Date', salesdate)
    newrecord.set_field_value('Plaintiff', plaintiff)
    newrecord.set_field_value('Defendant', defendant)
    newrecord.set_field_value('Notes1', description)
    newrecord.set_field_value('Approx_Upset', approxupset)
    newrecord.set_field_value('Attorney_Name', attorney)
        #newrecord.set_field_value('County', county)
    newrecord.set_field_value('Attorney_Phone', attorneyphone)
    check()

    user = ZCRMUser.get_instance(677853022, 'Avery Steinberg')  # user id and user name
    newrecord.set_field_value('Owner', user)
    try:
        resp = newrecord.create()
        print(resp.status_code)
        print(resp.code)
        print(resp.details)
        print(resp.message)
        print(resp.status)
        print(resp.data.entity_id)
        print(resp.data.created_by.id)
        print(resp.data.created_time)
        getimage()
    except zcrmsdk.ZCRMException as ex:
        print(ex.status_code)
        print(ex.error_message)
        print(ex.error_code)
        print(ex.error_details)
        print(ex.error_content)

    except AttributeError:
        print('attribute error')
                #newevent = zcrmsdk.ZCRMRecord.get_instance('Events')
                #newrecord.set_field_value('All_day', True)
                #newrecord.set_field_value('Owner', user)
                #newrecord.set_field_value('Event_Title', 'Auction')
                #newrecord.set_field_value('Start_DateTime', auctiondate)
                #newrecord.set_field_value('End_DateTime', auctiondate)
                #event_ins_list.append(newevent)
                #resp2 = zcrmsdk.ZCRMModule.get_instance('Events').create_records(event_ins_list)
                #print(resp2.status_code)

        continue

    continue

##search MLS

##driver.get('https://mls2.gsmls.com/member/advncSearch.do?method=advanceSearchdefualt&ptype=RES&isMenu=TRUE&')

## username = driver.find_element_by_id('usernametxt')
## username.send_keys('303616')
## password = driver.find_element_by_id('passwordtxt')
## password.send_keys('champ0655')
## log_in_button = driver.find_element_by_id('login-btn')
##driver.implicitly_wait(1000000000)
## log_in_button.click()
## driver.implicitly_wait(1000000000)












