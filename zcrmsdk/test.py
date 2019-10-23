from zcrmsdk import ZCRMRestClient
import json

config = {
    "client_id": "1000.M4WLRMKKQ6Z1261586Z7BJZZX7AIVH",
    "client_secret": "5b64aa3ac92e9ca017dbde2231cceb127239ce1427",
    "redirect_uri": "https://www.buyabeautifulhome.com/",
    "token_persistence_path": ".",
    "accounts_url": "https://accounts.zoho.com"
}

ZCRMRestClient.initialize(config)

lead_record