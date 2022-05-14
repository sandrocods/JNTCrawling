from src.JntCrawling import *

jnt = JntCrawling(
    enable_log=False
)

print(f"Print List City ")
for data in jnt.getCityList()['data']:
    print(data)

print()

print(f"Check Rate Delivery with height, length, width")
print(
    jnt.checkRates(
        height=100,
        length=10,
        width=100,
        receiverAddress="PURWOKERTO SELATAN",
        senderAddress="KARANG ANYAR"
    )
)
print()

print("Check Rate Delivery with weight")
print(
    jnt.checkRates(
        weight=16.68,
        receiverAddress="PURWOKERTO SELATAN",
        senderAddress="KARANG ANYAR"
    )
)

print(f"Track Delivery with billCodes")
print(
    jnt.trackReceipt(
        billCodes="JP4392231394"
    )
)
print()

print(f"Track Delivery with Try Except")
try:
    print(
        jnt.trackReceipt(
            billCodes="JP4392231394"
        )
    )
except connection_error as message:
    print(message)
except error_no_billCode as message:
    print(message)
except no_data_found as message:
    print(message)
print()

print(f"Check DropPoint by District")
try:
    print(
        jnt.checkDropPointByDistrict(
            district="SRAGEN",
            city="SRAGEN",
            province="JAWA TENGAH"
        )
    )
except Exception as e:
    print(e)

print()

print(f"Check DropPoint by GPS")
print(
    jnt.checkDropPointByGPS(
        longitude="109.23896994441748",
        latitude="-7.446290145162584"
    )
)

print()

print(f"Check DropPoint by GPS ISP")
print(
    jnt.checkDropPointByGPS()
)
