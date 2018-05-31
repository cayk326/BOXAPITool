# Date: 05/23/2018
# Author: cay
# Version: version 1.0
# Description:
# this code is get box application information using box API
# Not include function of getting access token automatically
# So that you must access box developer and get access token manually
# After get the access taken, please update main.oauth.access_taken<string>


from boxsdk import Client, OAuth2, DeveloperTokenClient


def main():
    oauth = OAuth2(
        client_id='<CLIENT_ID>',
        client_secret='<CLIENT_SECRET>',
        access_token='<ACCESS_TOKEN>'# manual input
    )

    client = Client(oauth=oauth)
    box_contentlists = client.folder('0').get_items(100, 0, None)
    print(box_contentlists)
    return (box_contentlists)



if __name__ == "__main__":
    contentslist = main()
    print('below is box contents list')
    print(contentslist)
    print('finish program')