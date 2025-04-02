import argparse
from http.client import responses
from urllib import response
from urllib.parse import urljoin

import requests

def inputCheck():
    global args
    try:
        parser = argparse.ArgumentParser(description="Send data to a URL to check for URL validity")

        parser.add_argument("-u", "--url", type=str, required=True, help="Data to check URL validity")
        parser.add_argument("-f", "--file", type=str, required=True, help="Path to a file containing URLs to check")

        args = parser.parse_args()
    except:
        pass


    try:
        if args.url:
            check_url(args.url)
        with open(args.file, "r") as file:
         urls = file.readlines()
         for url in urls:
             url = url.strip()
             full_url = urljoin(args.url, path)
             check_url(url)

    except:
        pass



def check_url(url):
    try:
        response = requests.get(args.url)
        if (response.status_code == requests.codes.ok):
            print("Website exists.. continuing.. ")

        else:
            print("Website doesn't exist.. Try again")

    except:
        pass

def check_url(url):
    try:
        response = requests.get(url)
        if response.status_code == requests.codes.ok:
            print(f"Website {url} exists.. continuing..")
        else:
            print(f"Website {url} doesn't exist.. Status code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"An error occurred with {url}: {e}")


    if args.url:
        if args.file:
            try:
                with open(args.file, 'r') as file:
                    paths = file.readlines()
                    for path in paths:
                        full_url = urljoin(args.url, path)
                        check_url(full_url)
            except FileNotFoundError:
                print("File not found.. check the path..")
            except Exception as e:
                print(f"{e}")

inputCheck()