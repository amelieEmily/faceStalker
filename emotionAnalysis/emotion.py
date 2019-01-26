import http.client, urllib.request, urllib.parse, urllib.error, base64
import json

headers = {
    # Request headers
    #'Content-Type': 'application/json',
    'Content-Type': 'application/octet-stream',
    'Ocp-Apim-Subscription-Key': 'c91dcc9052a04898890b376f8a526c4f',
}

params = urllib.parse.urlencode({
    # Request parameters
    'returnFaceId': 'true',
    'returnFaceLandmarks': 'false',
    'returnFaceAttributes': "emotion",
})
def analysisPhoto(filename):
    # Read the image with the given filename
    with open(filename, 'rb') as f:
        img_data = f.read()

    #body = json.dumps({"url": "http://wp.doc.ic.ac.uk/ajf/wp-content/uploads/sites/49/2014/01/meBigHoleAdjusted.jpg"})
    body = img_data
    try:
        conn = http.client.HTTPSConnection('westcentralus.api.cognitive.microsoft.com')
        conn.request("POST", "/face/v1.0/detect?%s" % params, body, headers)
        response = conn.getresponse()
        data = response.read()
        print(data)
        conn.close()
    except Exception as e:
        print("[Errno {0}] {1}".format(e.errno, e.strerror))

analysisPhoto("images/image4855.jpg")


# import http.client, urllib.request, urllib.parse, urllib.error, base64
# import pathlib
#
# facephoto = pathlib.Path("/Users/yejinseo/ichack19/faceStalker/laugh.jpg").as_uri()
#
# headers = {
#     # Request headers
#     'Content-Type': 'application/json',
#     'Ocp-Apim-Subscription-Key': 'c91dcc9052a04898890b376f8a526c4f',
# }
#
# params = urllib.parse.urlencode({
#     "returnFaceAttributes": {"emotion"}
# })
#
# try:
#     conn = http.client.HTTPSConnection('westcentralus.api.cognitive.microsoft.com')
#     conn.request("POST", "/face/v1.0/detect?%s" % params, "http://wp.doc.ic.ac.uk/ajf/wp-content/uploads/sites/49/2014/01/meBigHoleAdjusted.jpg", headers)
#     response = conn.getresponse()
#     data = response.read()
#     print(data)
#     conn.close()
# except Exception as e:
#     print("[Errno {0}] {1}".format(e.errno, e.strerror))
