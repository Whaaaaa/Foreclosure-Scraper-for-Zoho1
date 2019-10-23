from selenium import webdriver
import zillow

with open("/home/noahbenezra/PycharmProjects/untitled3/venv/bin/config/zillow key.conf", 'r') as f:
    key = f.readline().replace("\n", "")

url = 'https://salesweb.civilview.com/Sales/SalesSearch?countyId=2'
driver = webdriver.Chrome("/home/noahbenezra/PycharmProjects/untitled3/Selenium Resource/chromedriver")


options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument("--test-type")
options.binary_location = "/usr/bin/chromium"


driver.get(url)


details = [detail.get_attribute('href') for detail in driver.find_elements_by_partial_link_text("Details")]
for details in details:
    driver.get(details)
    auctiondate = driver.find_element_by_css_selector('body > div > div.table-responsive > table:nth-child(1) > tbody > tr:nth-child(3) > td:nth-child(2)').text
    if auctiondate == '6/11/2019':
        driver.implicitly_wait(8)
        sheriff = driver.find_element_by_css_selector('body > div > div.table-responsive > table:nth-child(1) > tbody > tr:nth-child(1) > td:nth-child(2)').text
        street = driver.find_element_by_css_selector('body > div > div.table-responsive > table:nth-child(1) > tbody > tr:nth-child(6) > td:nth-child(2)').text
        courtcase = driver.find_element_by_css_selector('body > div > div.table-responsive > table:nth-child(1) > tbody > tr:nth-child(2) > td:nth-child(2)').text
        salesdate = driver.find_element_by_css_selector('body > div > div.table-responsive > table:nth-child(1) > tbody > tr:nth-child(3) > td:nth-child(2)').text
        Plaintiff = driver.find_element_by_css_selector('body > div > div.table-responsive > table:nth-child(1) > tbody > tr:nth-child(3) > td:nth-child(2)').text
        salesdate = driver.find_element_by_css_selector('body > div > div.table-responsive > table:nth-child(1) > tbody > tr:nth-child(3) > td:nth-child(2)').text
        Defendant = driver.find_element_by_css_selector('body > div > div.table-responsive > table:nth-child(1) > tbody > tr:nth-child(5) > td:nth-child(2)').text
        Description = driver.find_element_by_css_selector('body > div > div.table-responsive > table:nth-child(1) > tbody > tr:nth-child(7) > td:nth-child(2)').text
        salesdate = driver.find_element_by_css_selector(
            'body > div > div.table-responsive > table:nth-child(1) > tbody > tr:nth-child(3) > td:nth-child(2)').text
        salesdate = driver.find_element_by_css_selector(
            'body > div > div.table-responsive > table:nth-child(1) > tbody > tr:nth-child(3) > td:nth-child(2)').text
        salesdate = driver.find_element_by_css_selector(
            'body > div > div.table-responsive > table:nth-child(1) > tbody > tr:nth-child(3) > td:nth-child(2)').text


        data = {detail:{"sheriff": sheriff, "street": street}}
        print(data)

        searchstreet, searchcityzip = street.split("\n",1)
        address = searchstreet
        citystatezip = searchcityzip


        api = zillow.ValuationApi()
        deep_results = api.GetDeepSearchResults(key, address, citystatezip)
        resultsdict = deep_results.get_dict()

        from zcrmsdk import ZCRMRestClient, ZCRMRecord, ZCRMModule, ZCRMUser, ZCRMException, ZohoOAuth

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
        oauth_client = ZohoOAuth.get_client_instance()

        newrecord = ZCRMRecord.get_instance('Leads')  # Module API Name
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
        newrecord.set_field_value('Zestimate_New', resultsdict['zestimate']['amount'])
        newrecord.set_field_value('Total_Assessment', resultsdict['extended_data']['tax_assessment'])
        newrecord.set_field_value('Zillow_Link', resultsdict['links']['home_details'])
        newrecord.set_field_value('Assessment_Year', resultsdict['extended_data']['tax_assessment_year'])
        newrecord.set_field_value('Zestimate_Low', resultsdict['zestimate']['valuation_range_low'])
        newrecord.set_field_value('Zestimate_High', resultsdict['zestimate']['valuation_range_high'])

        user = ZCRMUser.get_instance(677853022, 'Avery Steinberg')  # user id and user name
        newrecord.set_field_value('Owner', user)

        resp = newrecord.create()
        print(resp.status_code)
        print(resp.code)
        print(resp.details)
        print(resp.message)
        print(resp.status)
        print(resp.data.entity_id)
        print(resp.data.created_by.id)
        print(resp.data.created_time)
        print(data)

    else: driver.get(details)










