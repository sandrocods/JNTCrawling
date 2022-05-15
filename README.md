
# JNTCrawling-py
<p align="left">

 <img alt="GitHub top language" src="https://img.shields.io/github/languages/top/sandrocods/JNTCrawling-py?style=for-the-badge">
 <img alt="GitHub repo size" src="https://img.shields.io/github/repo-size/sandrocods/JNTCrawling-py?style=for-the-badge">
 <img alt="GitHub Release Date" src="https://img.shields.io/github/release-date/sandrocods/JNTCrawling-py?style=for-the-badge">
 <img alt="Tests Passing" src="https://github.com/sandrocods/JNTCrawling-py/actions/workflows/python-app.yml/badge.svg" />
  
</p>


Crawling menggunakan Automation program yang dibuat dengan Python3 dan menggunakan Application Programming Interface (API) sebagai jalur komunikasi dalam mendapatkan data, Dibuat untuk keperluan pembelajaran dan riset.



[![Desain-tanpa-judul-3.png](https://i.postimg.cc/MTpBC1RT/Desain-tanpa-judul-3.png)](https://postimg.cc/HJFj5c6D)
## Demo
<p align="left">
 <img alt="replit" href="https://replit.com/@sandrocods/JNTCrawling-py#main.py" src="https://img.shields.io/badge/replit-000?style=for-the-badge&logo=replit&logoColor=white">
 <img alt="replit" href="https://insomnia.rest/run/?label=JNT%20Unofficial%20API&uri=https%3A%2F%2Fraw.githubusercontent.com%2Fsandrocods%2FJNTCrawling-py%2Fmaster%2FInsomnia_2022-05-15.json" src="https://insomnia.rest/images/run.svg">
 
</p>

## Build With

 - [Python3](https://www.python.org/)
 - [Requests](https://pypi.org/project/requests/)
 - [Geocoder](https://pypi.org/project/geocoder/)
 - [Logging](https://docs.python.org/3/library/logging.html)
 - [Json](https://docs.python.org/3.10/library/json.html)
 - [Unittest](https://docs.python.org/3/library/unittest.html)

## Features

| Feature             | Available                                                                |
| ----------------- | ------------------------------------------------------------------ |
| getCityList | ✅ |
| trackReceipt | ✅ |
| checkDropPointByGPS | ✅ |
| checkRates by weight | ✅ |
| checkDropPointByDistrict | ✅ |
| checkDropPointByGPS by ISP | ✅ |
| checkRates by height, length, width | ✅ |




## Run Locally

Clone the project

```bash
  git clone https://github.com/sandrocods/JNTCrawling-py/
```

Go to the project directory

```bash
  cd JNTCrawling-py
```

Install dependencies

```bash
  pip install .\requirements.txt
```

Go to the Example project directory

```bash
  cd example
```

Run Example
```bash
  python3 Example.py
```


## API Reference

#### Create Instance Objects

```python
  jnt = JntCrawling(
    enable_log
)
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `enable_log` | `boolean` | **Required**. False to Disable logging, True to Enable logging |

#### Get City, Province, Country Area

```python
  jnt.getCityList()['data']
```

#### Check Rate Delivery with height, length, width

```python
jnt.checkRates(
        height,
        length,
        width,
        receiverAddress,
        senderAddress
    )
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `height` | `float` | **Required**. height object |
| `length` | `float` | **Required**. length object |
| `width` | `float` | **Required**. width object |
| ` receiverAddress` | `string` | **Required**.  receiverAddress from getCityList |
| `senderAddress` | `string` | **Required**. senderAddressh from getCityList |

#### Check Rate Delivery with weight

```python
jnt.checkRates(
        weight,
        receiverAddress,
        senderAddress
    )
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| ` weight` | `float` | **Required**.  weight object |
| ` receiverAddress` | `string` | **Required**.  receiverAddress from getCityList |
| `senderAddress` | `string` | **Required**. senderAddressh from getCityList |

#### Track Delivery with billCodes

```python
jnt.trackReceipt(
        billCodes="Jxxxxxxxxxx"
    )
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| ` billCodes` | `string` | **Required**.  receipt of delivery  |

#### Check DropPoint by District

```python
jnt.checkDropPointByDistrict(
            district,
            city,
            province
        )
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| ` district` | `string` | **Required**. district from getCityList  |
| ` city` | `string` | **Required**. city from getCityList  |
| ` province` | `string` | **Required**. province from getCityList  |


#### Check DropPoint by GPS

```python
jnt.checkDropPointByGPS(
        longitude,
        latitude
    )
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| ` longitude` | `string` | **Required**. longitude from maps  |
| ` latitude` | `string` | **Required**. latitude from maps  |

_Note: Get latitude and longitude from ISP ip address, If location not accurate, fill latitude and longitude manually._

#### Check DropPoint by GPS ISP

```python
jnt.checkDropPointByGPS()
```

## Running Tests

To run tests, run the following command

```bash
  cd test
```
List of test in folder test
```bash
  python3 test_checkDropPointByDistrict.py 
```
## Running All Test Passed

#### All tests are made with UnitTest and display the results as below
[![image.png](https://i.postimg.cc/Nj9dXK4y/image.png)](https://postimg.cc/jDT60dBK)

[![Check Result](https://img.shields.io/badge/check%20result%20Test-47C119?style=for-the-badge&logo=HTML&logoColor=white)](https://htmlpreview.github.io/?https://github.com/sandrocods/JNTCrawling-py/blob/master/test/Test%20Results%20-%20.html)


## Authors

- [@sandrocods](https://www.github.com/sandrocods)

