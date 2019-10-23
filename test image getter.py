from google_images_download import google_images_download

def getimage():
    response = google_images_download.googleimagesdownload()  # class instantiation
    keyword = address.replace(",", "") +' '+citystatezip.replace(",", "")
    arguments = {"keywords": keyword, "limit":1}  # creating list of arguments
    paths = response.download(arguments)  # passing the arguments to the function
    print paths[0]
    path = '/'+str(paths[0]).split("'/")[1]
    print path
    path = path[:-3]
    print path
getimage()
