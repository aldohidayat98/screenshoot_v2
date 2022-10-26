# Import Plugin Selenium dll ==========================================
from selenium.webdriver.common.keys import Keys #Di Gunakan untuk Keys.ENTER
from selenium.webdriver.common.by import By #Di Gunakan untuk By.CSS_SELECTOR/XPATH
from selenium import webdriver #Webdriver untuk Chrome
import time
import datetime

# Input Data Waktu Netflow --------------------------
print('-- Masukan Waktu Awal --')
tahun = int(input("Masukan Tahun : "))
bulan = int(input("Masukan Bulan : "))
tgl = int(input("Masukan Tanggal : "))
jam = int(input("Masukan Jam : "))
menit = int(input("Masukan Menit : "))

print('')
print('-- Masukan Jam Akhir --')
jam2 = int(input("Masukan Jam : "))
menit2 = int(input("Masukan Menit : "))


print('')
print('-- Masukan Tanggal Folder --')
tgl_folder = str(input('Masukan Tanggal Gambar (Ex 10-OKTOBER) : '))

epoch_time = datetime.datetime(tahun, bulan, tgl, jam, menit, 0).timestamp()*1000
epoch_time2 = datetime.datetime(tahun, bulan, tgl, jam2, menit2, 0).timestamp()*1000
# print("Converted epoch time:", int(epoch_time)) ========================================


# Membuat Function untuk di panggil kembali pada Looping
def loop (ip1:(str), ip2:(str), lokasi:(str), nama:(str)):
    web = 'http://10.38.3.25/report.jsp?templid=_if&output=chart&device=' + ip1 + '&if=' + ip2 + '&chartTitle=Traffic+Rate'
    driver.get(web+'&stime='+ str(int(epoch_time)) + '&etime=' + str(int(epoch_time2)) + '&sample_nunits=1&sample_unit=minute')
    driver.set_window_size(782, 768)
    time.sleep(1)
    element = driver.find_element('name','rep_form')
    element.screenshot(lokasi+str(tgl_folder)+'-2022_'+nama+'-WAN-IPSEC1_traffic.png')
   

def loop2 (ip1:(str), ip2:(str), lokasi:(str), nama:(str)):
    web = 'http://10.38.3.25/report.jsp?templid=_if&output=chart&device=' + ip1 + '&if=' + ip2 + '&chartTitle=Traffic+Rate'
    driver.get(web+'&stime='+ str(int(epoch_time)) + '&etime=' + str(int(epoch_time2)) + '&sample_nunits=1&sample_unit=minute')
    driver.set_window_size(782, 768)
    time.sleep(1)
    element = driver.find_element('name','rep_form')
    element.screenshot(lokasi+str(tgl_folder)+'-2022_'+nama+'-WAN-IPSEC2_traffic.png')



# Deklarasi webdriver & Tampilan Windows Maksimal ====================
driver = webdriver.Chrome()
driver.maximize_window() 

# Login ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
driver.get('http://10.38.3.25/login/login.jsp')
driver.find_element('name','j_username').send_keys('ald')
driver.find_element('name','j_password').send_keys('ald' + Keys.ENTER)

# Looping ------------------------------------------------------------------
loop('10.68.68.2','10.68.68.2%2F19','./Capture link IP Sec/BCALC1/2022/Oktober/','BCALC1')
loop2('10.68.68.3','10.68.68.3%2F19','./Capture link IP Sec/BCALC1/2022/Oktober/','BCALC1')    
loop('10.63.140.3','10.63.140.3%2F14','./Capture link IP Sec/BSD/2022/Oktober/','BSD')  
loop2('10.63.140.4','10.63.140.4%2F14','./Capture link IP Sec/BSD/2022/Oktober/','BSD')  
loop('10.64.0.29','10.64.0.29%2F14','./Capture link IP Sec/CPC/2022/Oktober/','CPC')  
loop2('10.64.0.30','10.64.0.30%2F14','./Capture link IP Sec/CPC/2022/Oktober/','CPC')  
loop('10.61.0.1','10.61.0.1%2F14','./Capture link IP Sec/FOR/2022/Oktober/','FOR')  
loop2('10.61.0.2','10.61.0.2%2F14','./Capture link IP Sec/FOR/2022/Oktober/','FOR')  
loop('10.70.4.1','10.70.4.1%2F11','./Capture link IP Sec/GSW/2022/Oktober/','GSW')  
loop2('10.70.4.2','10.70.4.2%2F11','./Capture link IP Sec/GSW/2022/Oktober/','GSW')  
loop('10.66.128.1','10.66.128.1%2F13','./Capture link IP Sec/HSB/2022/Oktober/','HSB')  
loop2('10.66.128.2','10.66.128.2%2F13','./Capture link IP Sec/HSB/2022/Oktober/','HSB')  
loop('10.70.0.1','10.70.0.1%2F11','./Capture link IP Sec/JDL/2022/Oktober/','JDL')  
loop2('10.70.0.2','10.70.0.2%2F11','./Capture link IP Sec/JDL/2022/Oktober/','JDL')
loop('10.69.0.29','10.69.0.29%2F12','./Capture link IP Sec/LMP/2022/Oktober/','LMP')  
loop2('10.69.0.30','10.69.0.30%2F13','./Capture link IP Sec/LMP/2022/Oktober/','LMP')    
loop('10.70.8.1','10.70.8.1%2F9','./Capture link IP Sec/TCM/2022/Oktober/','TCM')  
loop2('10.70.8.2','10.70.8.2%2F9','./Capture link IP Sec/TCM/2022/Oktober/','TCM')  
loop('10.60.31.29','10.60.31.29%2F12','./Capture link IP Sec/WBCA-PI/2022/Oktober/','WBCA')
loop2('10.60.31.30','10.60.31.30%2F12','./Capture link IP Sec/WBCA-PI/2022/Oktober/','WBCA')  


time.sleep(2)
driver.quit()   








# DOCUMENTATION!!!!!
# -------------------------------------------------------------------------------------------
# from selenium.webdriver.common.by import By
# driver.find_element('name','q').send_keys('Aldo Hidayat' + Keys.ENTER)
# assert 'Aldo Hidayat','Aldo' in driver.find_element(By.CSS_SELECTOR,'h3').text
# assert 'Aldo Hidayat' in driver.title


# -------------------------------------------------------------------------------------------
# # BCALC1 - IPSEC1
# driver.get('http://10.38.3.25/report.jsp?templid=_if&output=chart&device=10.68.68.2&if=10.68.68.2%2F19&chartTitle=Traffic+Rate'+str(epoch))
# driver.set_window_size(782, 768)
# time.sleep(1)
# element = driver.find_element('name','rep_form')
# element.screenshot('./Capture link IP Sec/BCALC1/2022/Oktober/'+str(date)+'-2022_BCALC1-WAN-IPSEC1_traffic.png') 