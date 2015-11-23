#!/usr/local/bin/python2.7

import csv
import requests
from bs4 import BeautifulSoup

hospital_foundation = "http://www.dlp.vermont.gov/standard-surveys-hospitals"
slug = {"Brattleboro Memorial Hospital": "/brattleboro-acc-poc-folder/", "Brattleboro Retreat": "/brattleboro-retreat-acc-poc-folder/", "Central Vermont Medical Center": "/central-vermont-acc-poc-folder/", "Copley Hospital": "/copley-acc-poc-folder/", "Fletcher Allen Health Care": "/fletcher-allen-acc-poc-folder/", "Gifford Memorial Hospital": "/gifford-acc-poc-folder/", "Grace Cottage Hospital": "/grace-acc-poc-folder/", "Vermont Psychiatric Care Hospital": "/green-mountain-psychiatric-care-center/", "Mt. Ascutney Hospital & Health Center": "/mt-ascutney-acc-poc-folder/", "North Country Hospital & Health Center": "/north-country-acc-poc-folder/", "Northeastern Vermont Regional Hospital": "/northeastern-acc-poc-folder/", "Northwestern Medical Center": "/northwestern-acc-poc-folder/", "Porter Hospital": "/porter-acc-poc-folder/", "Rutland Regional Medical Center": "/rutland-acc-poc-folder/", "Southwestern Vermont Medical Center": "/southwestern-acc-poc-folder/", "Springfield Hospital": "/springfield-acc-poc-folder/", "Navigation": "portlet-navigation-tree"}

outfile = open("/home/vprnet/webapps/bots/bots/hospital-reports/reports.csv", "wb")
writer = csv.writer(outfile)

for key, value in slug.iteritems():

    hospital_url = hospital_foundation + value

    response = requests.get(hospital_url)
    html = response.content
    soup = BeautifulSoup(html)

    reports = soup.find_all("dt")
    list_of_reports = []
    list_of_hospitals = []

    for report in reports:
        new_report = report.a.string
        associated_hospital = key
        list_of_hospitals.append(associated_hospital)
        list_of_reports.append(str(new_report))

    del list_of_reports[-1]
    hospital_and_report = zip(list_of_hospitals, list_of_reports)

    writer.writerows(hospital_and_report)
