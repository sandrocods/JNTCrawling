from src.Exception import *
import requests
import json
import geocoder
import os.path
import logging


def Formatrupiah(uang):
    y = str(uang)
    if len(y) <= 3:
        return 'Rp ' + y
    else:
        p = y[-3:]
        q = y[:-3]
        return Formatrupiah(q) + '.' + p


class JntCrawling:
    def __init__(self, enable_log=False):
        logging.basicConfig(
            format='[%(levelname)s] %(asctime)s - %(message)s',
            datefmt='%d-%b-%y %H:%M:%S',
            level=logging.INFO
        )
        if enable_log:
            pass
        else:
            logging.disable(logging.INFO)

        self.endPoint = "https://secure-jk.jet.co.id/jandt-app-ifd-web/router.do"
        self.header = {
            "Content-Type": "application/x-www-form-urlencoded",
            "Host": "secure-jk.jet.co.id"
        }

        current_dir = os.path.dirname(os.path.realpath(__file__))
        filename = os.path.join(current_dir, "data_list.json")

        if os.path.exists(filename):
            logging.info('File data_list.json exists')

        else:
            logging.info('File data_list.json not exists')
            request_get_data_list = requests.get(
                url='https://gist.githubusercontent.com/sandrocods/db54b71923f6d13468f279ff1a8ba115/raw/6dcbfd12b5eeeff92ddaae60121364bca0cd6bda/data_list.json',
            )
            if request_get_data_list.status_code == 200:

                logging.info('File data_list.json created')
                with open(filename, 'w') as write:
                    write.write(request_get_data_list.text)
            else:

                logging.error('File data_list.json not created')
                raise FileNotFoundError('File data_list.json not created')

    @staticmethod
    def getCityList():
        """
        It opens the data_list.json file, reads the contents, and then loads the contents into a variable called data
        :return: A list of dictionaries.
        """
        current_dir = os.path.dirname(os.path.realpath(__file__))
        filename = os.path.join(current_dir, "data_list.json")
        with open(filename, 'r') as read:
            data = json.loads(read.read())
        return data

    def trackReceipt(self, billCodes):
        """
        It takes a list of bill codes, and returns a JSON object containing the status of the bill code, the process of the
        bill code, and the details of the bill code

        :param billCodes: The bill code you want to track
        :return: The data is being returned in a JSON format.
        """

        if not billCodes:
            logging.error('Bill code is empty')
            raise error_no_billCode()

        data = {
            "parameter":
                json.dumps({
                    "billCodes": billCodes,
                    "lang": "en"
                })
        }
        try:

            logging.info('Requesting data from J&T')
            request_trackReceipt = requests.post(
                url=self.endPoint,
                headers=self.header,
                data="method=order.massOrderTrack&format=json&v=1.0&data=" + json.dumps(data),
            )
            if request_trackReceipt.status_code == 200 and \
                    len(json.loads(request_trackReceipt.json()['data'])['bills'][0]['details']) == 0:
                logging.error('Bill code not found')
                raise no_data_found

            else:

                logging.info('Data received')
                data_collection = []
                data = {
                    "status": "success",
                    "billCodes": billCodes,
                    "data": data_collection,
                }
                for index in json.loads(request_trackReceipt.json()['data'])['bills']:
                    data['status_package'] = index['status']
                    data['process'] = index['process']
                    for detail in index['details']:
                        try:

                            if detail['scanscode'] == '2':
                                data_collection.append({
                                    "city": detail['city'],
                                    "scan_status": detail['scanstatus'],
                                    "state": detail['state'],
                                    "accepted_date": detail['acceptTime'],
                                    "next_site": detail['nextsite'],
                                    "next_drop_point": detail['nextDroppoint'],
                                })
                            else:
                                data_collection.append({
                                    "city": detail['city'],
                                    "scan_status": detail['scanstatus'],
                                    "state": detail['state'],
                                    "accepted_date": detail['acceptTime'],
                                    "next_site": detail['nextsite'],
                                })
                        except KeyError:
                            data_collection.append({
                                "city": detail['city'],
                                "scan_status": detail['scanstatus'],
                                "state": detail['state'],
                                "accepted_date": detail['acceptTime'],
                                "next_site": detail['nextsite'],
                            })
                return json.dumps(data, indent=5)

        except (requests.exceptions.ConnectionError or requests.exceptions.Timeout):

            logging.error('Connection Error')
            raise connection_error

    def checkDropPointByGPS(self, latitude=None, longitude=None, radius=4):
        """
        It checks if there is a drop point near the user's location

        :param latitude: The latitude of the location you want to check
        :param longitude: longitude of the location
        :param radius: The radius of the search area in kilometers, defaults to 4 (optional)
        :return: The return value is a JSON string.
        """
        if not latitude and not longitude:
            logging.info('Latitude and Longitude not found using default value from ISP data')
            # Get latitude and longitude from ISP ip address
            # If location not accurate, fill latitude and longitude manually
            latitude, longitude = geocoder.ip('me').latlng

        data = {
            "parameter":
                json.dumps({
                    "latitude": latitude,
                    "longitude": longitude,
                    "radius": radius,
                })
        }
        try:

            logging.info('Checking Drop Point by GPS')
            request_CheckDropPointByGPS = requests.post(
                url=self.endPoint,
                headers=self.header,
                data="method=site.findSitesByGPS&format=json&v=1.0&data=" + json.dumps(data)
            )
            if request_CheckDropPointByGPS.status_code == 200 and \
                    len(json.loads(request_CheckDropPointByGPS.json()['data'])['Droppoints']) != 0:

                logging.info('Drop Point found')
                data_collection = []
                for data in json.loads(request_CheckDropPointByGPS.json()['data'])['Droppoints']:
                    data_collection.append({
                        "id": data['id'],
                        "site_code": data['siteCode'],
                        "site_name": data['siteName'],
                        "province": data['province'],
                        "city": data['city'],
                        "is_open": data['isOpen'],
                        "distance": data['distance'],
                        "business_hours": data['businesshours'],
                        "latitude": data['latitude'],
                        "longitude": data['longitude'],
                        "site_address": data['siteAddr'],
                        "site_phone": data['sitePhone'],
                        "site_leader": data['siteLeader'],
                    })

                return json.dumps(
                    {
                        "status": "success",
                        "total_drop_point": len(json.loads(request_CheckDropPointByGPS.json()['data'])['Droppoints']),
                        "data": data_collection
                    },
                    indent=5
                )
            else:

                logging.info('Drop Point not found')
                raise no_data_found
        except (requests.exceptions.ConnectionError or requests.exceptions.Timeout):

            logging.error('Connection Error')
            raise connection_error

    def checkDropPointByDistrict(self, district=None, province=None, city=None):
        """
        It checks if there is a drop point in a certain district, province, or city

        :param district: District name
        :param province: The province name
        :param city: City name
        :return: The return value is a JSON string.
        """
        if not district and not province and not city:
            logging.error('District, Province and City not provided ')
            raise parameter_error

        data = {
            "parameter":
                json.dumps({
                    "district": district,
                    "province": province,
                    "city": city,
                })
        }
        try:
            logging.info('Checking Drop Point by District')
            request_CheckDropPointByDistrict = requests.post(
                url=self.endPoint,
                headers=self.header,
                data="method=site.findSitesByDistrict&format=json&v=1.0&data=" + json.dumps(data)
            )

            if request_CheckDropPointByDistrict.status_code == 200 and \
                    len(json.loads(request_CheckDropPointByDistrict.json()['data'])['droppoints']) != 0:

                logging.info('Drop Point found')
                data_collection = []
                for data in json.loads(request_CheckDropPointByDistrict.json()['data'])['droppoints']:
                    data_collection.append({
                        "id": data['id'],
                        "site_code": data['siteCode'],
                        "site_name": data['siteName'],
                        "province": data['province'],
                        "city": data['city'],
                        "is_open": data['isOpen'],
                        "distance": data['distance'],
                        "business_hours": data['businesshours'],
                        "latitude": data['latitude'],
                        "longitude": data['longitude'],
                        "site_address": data['siteAddr'],
                        "site_phone": data['sitePhone'],
                        "site_leader": data['siteLeader'],
                    })

                return json.dumps(
                    {
                        "status": "success",
                        "total_drop_point": len(
                            json.loads(request_CheckDropPointByDistrict.json()['data'])['droppoints']
                        ),
                        "data": data_collection
                    },
                    indent=5
                )
            else:

                logging.info('Drop Point not found')
                raise no_data_found
        except (requests.exceptions.ConnectionError or requests.exceptions.Timeout):

            logging.error('Connection Error')
            raise ConnectionError

    def checkRates(self, weight=None, length=None, width=None, height=None, receiverAddress="", senderAddress=""):
        """
        The above function is used to check the shipping rates of the JNT shipping service.

        :param weight: weight of the package in grams
        :param length: Length of the package in cm
        :param width: width of the package in cm
        :param height: Height of the package in cm
        :param receiverAddress: The address of the recipient
        :param senderAddress: The address of the sender
        :return: The return value is a JSON string.
        """

        if receiverAddress and senderAddress is None:
            logging.error('Sender Address and Receiver Address not provided')
            raise parameter_error

        weightFinal = 0
        if weight is None:
            logging.info('Calculation using length, width, height')
            weightFinal = (length * width * height) / 6000
        else:
            if length and width and height is None:
                pass
            else:
                logging.info('Calculation using weight')
                weightFinal = weight

        data = {
            "parameter":
                json.dumps({
                    "DimensionH": 0.0,
                    "DimensionL": 0.0,
                    "DimensionW": 0.0,
                    "receiverAddr": receiverAddress,
                    "senderAddr": senderAddress,
                    "weight": weightFinal
                }
                )
        }
        try:

            request_checkRates = requests.post(
                url=self.endPoint,
                headers=self.header,
                data="method=order.findRates&format=json&v=1.0&data=" + json.dumps(data)
            )

            if request_checkRates.status_code == 200 and len(
                    json.loads(request_checkRates.json()['data'])['Rates']) != 0:

                data_collection = []
                for data in json.loads(request_checkRates.json()['data'])['Rates']:
                    data_collection.append({
                        'product_type': data['productType'],
                        'product_type_name': data['productTypeName'],
                        'shipping_rate': Formatrupiah(data['shippingRate']),
                        'estimate_days': data['estimateDays']
                    })

                return json.dumps({
                    "status": "success",
                    "data": data_collection[0]
                }, indent=5)

            else:
                logging.info('Rate Delivery not found')
                raise no_data_found

        except (requests.exceptions.ConnectionError and requests.exceptions.Timeout):

            logging.error('Connection Error')
            raise ConnectionError
