#step1
from bs4 import BeautifulSoup
import urllib.request as req
import urllib
import os
import time
from urllib.parse import urljoin

baseurl_list = ["https://www.jitec.ipa.go.jp/1_04hanni_sukiru/mondai_kaitou_2019h31.html",
"https://www.jitec.ipa.go.jp/1_04hanni_sukiru/mondai_kaitou_2018h30.html",
"https://www.jitec.ipa.go.jp/1_04hanni_sukiru/mondai_kaitou_2017h29.html",
"https://www.jitec.ipa.go.jp/1_04hanni_sukiru/mondai_kaitou_2016h28.html",
"https://www.jitec.ipa.go.jp/1_04hanni_sukiru/mondai_kaitou_2015h27.html",
"https://www.jitec.ipa.go.jp/1_04hanni_sukiru/mondai_kaitou_2014h26.html",
"https://www.jitec.ipa.go.jp/1_04hanni_sukiru/mondai_kaitou_2013h25.html",
"https://www.jitec.ipa.go.jp/1_04hanni_sukiru/mondai_kaitou_2012h24.html",
"https://www.jitec.ipa.go.jp/1_04hanni_sukiru/mondai_kaitou_2011h23.html",
"https://www.jitec.ipa.go.jp/1_04hanni_sukiru/mondai_kaitou_2010h22.html",
"https://www.jitec.ipa.go.jp/1_04hanni_sukiru/mondai_kaitou_2009h21.html",
"https://www.jitec.ipa.go.jp/1_04hanni_sukiru/mondai_kaitou_2008h20.html",
"https://www.jitec.ipa.go.jp/1_04hanni_sukiru/mondai_kaitou_2007h19.html",
"https://www.jitec.ipa.go.jp/1_04hanni_sukiru/mondai_kaitou_2006h18.html",
"https://www.jitec.ipa.go.jp/1_04hanni_sukiru/mondai_kaitou_2005h17.html",
"https://www.jitec.ipa.go.jp/1_04hanni_sukiru/mondai_kaitou_2004h16.html",
]
for url in baseurl_list:
    #step2
    res = req.urlopen(url)
    soup = BeautifulSoup(res, "html.parser")
    result = soup.select("a[href]")
    #step3
    link_list =[]
    for link in result:
        href = link.get("href")
        link_list.append(href)
    #step4
    pdf_list = [temp for temp in link_list if temp.endswith('pdf')]
    #step5
    dbpdf_list = [temp for temp in pdf_list if '_db_' in temp]
    #step6
    abs_dbpdf_list = []
    for relative in dbpdf_list:
        temp_url = urljoin(url, relative)
        abs_dbpdf_list.append(temp_url)
    #step7
    filename_list = []
    for target in abs_dbpdf_list:
        temp_list = target.split("/")
        filename_list.append(temp_list[len(temp_list)-1])
    #step8
    target_dir = "C:\\Users\\makky\\Downloads\\DB"
    savepath_list = []
    for filename in filename_list:
        savepath_list.append(os.path.join(target_dir, filename))
    #step9
    for (pdflink, savepath) in zip(abs_dbpdf_list, savepath_list):
        print(pdflink)
        urllib.request.urlretrieve(pdflink, savepath)
        time.sleep(2)
