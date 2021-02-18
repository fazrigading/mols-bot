from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
#from selenium.webdriver.common.keys import Keys
from datetime import datetime, time
from time import sleep, strftime
'''
class urls:
    mols = 'https://mols.unmul.ac.id/mahasiswa/login'
    elearn = 'https://elearning.unmul.ac.id/login/index.php'
    apl = 'https://elearning.unmul.ac.id/mod/attendance/view.php?id=4731'
    jkk = 'https://elearning.unmul.ac.id/course/view.php?id=189'
    sisdig = 'https://mols.unmul.ac.id/mahasiswa/mahasiswa-group/sistem-digital-a-2020/7075/jRGbzs/index'
    fis = 'https://mols.unmul.ac.id/mahasiswa/mahasiswa-group/fge-ab2020/8099/bGqFnp/index'
    isbd = 'https://mols.unmul.ac.id/mahasiswa/mahasiswa-group/kelas-isbd-a-2020/7480/J192eR/index'
    mtk = 'https://mols.unmul.ac.id/mahasiswa/mahasiswa-group/matematika-informatika-2015-2020a/7118/s0vdBP/index'
    pbo = 'https://mols.unmul.ac.id/mahasiswa/mahasiswa-group/pbo-gabungan-2020/7791/iByGIW/index'
    sisope = 'https://mols.unmul.ac.id/mahasiswa/mahasiswa-group/sistem-operasi/7208/FJTddP/index'
'''
class urls:
    sisope = 'G:\MOLS\MOLS.html'
class jadwal:
    apl = '08:00'
    jkk = '10:00'
    sisdig = '13:00'
    fis = '15:00'
    isbd = '08:00'
    mtk = '12:00'
    pbo = '13:00'
    sisope = '08:30'
class account:
    usr = '2009106031'
    pwd = '516166'
acc = account()
url = urls()
jam = jadwal()
def act(x):
    return x+10
def wait_start(runTime, action):
    startTime = time(*(map(int, runTime.split(':'))))
    while startTime > datetime.today().time():
        sleep(1)
    return action
absen = input("Jam Absen (hh:mm): ")
wait_start(absen, lambda: act(100))
browser = webdriver.Chrome(ChromeDriverManager().install())
hari = strftime("%a")
skrg = strftime("%H:%M")
def keluar():
    browser.close()
def mols_login():
    browser.get(urls.mols)
    sleep(1)
    browser.find_element_by_id('nim').send_keys(acc.usr)
    sleep(1)
    browser.find_element_by_id('password').send_keys(acc.pwd)
    sleep(1)
    browser.find_element_by_id('btn-login').click()
    sleep(8)
def el_login():
    browser.get(urls.elearn)
    sleep(1)
    browser.find_element_by_id('username').send_keys(acc.usr)
    sleep(1)
    browser.find_element_by_id('password').send_keys(acc.pwd)
    sleep(1)
    browser.find_element_by_id('loginbtn').click()
    sleep(8)
def mols_hadir():
    while True:
        try:
            sleep(3)
            browser.find_element_by_class_name("btn.btn-outline-success.btn-rounded.btn-absent").click()
            sleep(5)
            break
        except:
            sleep(5)
            browser.refresh()
def el_hadir(): #perlu informasi
    browser.find_element_by_id('yui_3_17_2_1_1613425178836_20').click()
def senin():
    if jam.apl <= absen:
        el_login()
        browser.get(url.apl)
        el_hadir()
    elif jam.jkk <= absen: 
        el_login()
        browser.get(url.jkk)
    elif jam.sisdig <= absen:
        mols_login()
        browser.get(url.sisdig)
        mols_hadir()
    elif jam.fis <= absen:
        mols_login()
        browser.get(url.fis)
        mols_hadir()
def selasa():
    if jam.isbd <= absen:
        mols_login()
        browser.get(url.isbd)
        mols_hadir()
    elif jam.mtk <= absen:
        mols_login()
        browser.get(url.mtk)
        mols_hadir()
def rabu():
    if jam.pbo <= absen:
        mols_login()
        browser.get(url.pbo)
        mols_hadir()
def kamis():
    if jam.sisope <= absen:
        #mols_login()
        browser.get(url.sisope)
        mols_hadir()
print(hari+" "+skrg)
if hari == "Mon":
    if skrg <= absen:
        senin()
    elif skrg > absen:
        selasa()
elif hari == "Tue":
    if skrg <= absen:
        selasa()
    elif skrg > absen:
        rabu()
elif hari == "Wed":
    if skrg <= absen:
        rabu()
    elif skrg > absen:
        kamis()
elif hari == "Thu":
    if skrg <= absen:
        kamis()
    elif skrg > absen:
        pass #senin()
elif hari == "Sun":
    senin()