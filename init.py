from zcrmsdk import ZCRMRestClient, ZCRMRecord, ZCRMModule, ZCRMUser, ZCRMException, ZohoOAuth

config = {
            "sandbox": "False",
            "applicationLogFilePath": "./log",
            "client_id": "1000.2NV5D3YG1XFD36415FF2CU2AAPK1ZH",
            "client_secret": "23e8de3fc705d2853ed65e780b3ac138dc37b1ce34",
            "redirect_uri": "https://www.localhost:8080/some_path",
            "accounts_url": "https://accounts.zoho.com",
            "token_persistence_path": ".",
            "currentUserEmail": "elie@buyabeautifulhome.com"
}

ZCRMRestClient.initialize(config)
oauth_client = ZohoOAuth.get_client_instance()
grant_token = "1000.73fd9ca1ba865844f741158894e0efee.2d94f6c6dc7d6ea3a15c706d99b6f18b"
oauthtokens = oauth_client.generate_access_token(grant_token)

print(oauthtokens)