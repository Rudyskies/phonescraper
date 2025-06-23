from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
from bs4 import BeautifulSoup
import requests
import pandas as pd
import time
import random
import os

# Pilihan User
def user_choise():    
    while True:
        try:
            user_input = input("Pilihan: ").strip()

            # Cek apakah input hanya angka
            if not user_input.isdigit():
                raise ValueError("Input harus berupa angka.")

            user_number = int(user_input)

            # Cek apakah dalam rentang 1–125
            if not (1 <= user_number <= 125):
                raise ValueError("Angka harus antara 1 sampai 125.")

            # Jika valid, keluar dari loop
            break

        except ValueError as e:
            print(f"Input tidak valid: {e} Coba lagi.\n")


    if user_input == "1":
        brand = 'acer'
        user_url = "https://www.gsmarena.com/acer-phones-59.php"
    elif user_input == "2":
        brand = 'alcatel'
        user_url = "https://www.gsmarena.com/alcatel-phones-5.php"
    elif user_input == "3":
        brand = 'allview'
        user_url = "https://www.gsmarena.com/allview-phones-88.php"
    elif user_input == "4":
        brand = 'amazon'
        user_url = "https://www.gsmarena.com/amazon-phones-76.php"
    elif user_input == "5":
        brand = 'amoi'
        user_url = "https://www.gsmarena.com/amoi-phones-28.php"
    elif user_input == "6":
        brand = 'apple'
        user_url = "https://www.gsmarena.com/apple-phones-48.php"
    elif user_input == "7":
        brand = 'archos'
        user_url = "https://www.gsmarena.com/archos-phones-90.php"
    elif user_input == "8":
        brand = 'asus'
        user_url = "https://www.gsmarena.com/asus-phones-46.php"
    elif user_input == "9":
        brand = 'at&t'
        user_url = "https://www.gsmarena.com/at&t-phones-57.php"
    elif user_input == "10":
        brand = 'benefon'
        user_url = "https://www.gsmarena.com/benefon-phones-15.php"
    elif user_input == "11":
        brand = 'benq'
        user_url = "https://www.gsmarena.com/benq-phones-31.php"
    elif user_input == "12":
        brand = 'benq-siemens'
        user_url = "https://www.gsmarena.com/benq_siemens-phones-42.php"
    elif user_input == "13":
        brand = 'bird'
        user_url = "https://www.gsmarena.com/bird-phones-34.php"
    elif user_input == "14":
        brand = 'blackberry'
        user_url = "https://www.gsmarena.com/blackberry-phones-36.php"
    elif user_input == "15":
        brand = 'blackview'
        user_url = "https://www.gsmarena.com/blackview-phones-116.php"
    elif user_input == "16":
        brand = 'blu'
        user_url = "https://www.gsmarena.com/blu-phones-67.php"
    elif user_input == "17":
        brand = 'bosch'
        user_url = "https://www.gsmarena.com/bosch-phones-10.php"
    elif user_input == "18":
        brand = 'bq'
        user_url = "https://www.gsmarena.com/bq-phones-108.php"
    elif user_input == "19":
        brand = 'casio'
        user_url = "https://www.gsmarena.com/casio-phones-77.php"
    elif user_input == "20":
        brand = 'cat'
        user_url = "https://www.gsmarena.com/cat-phones-89.php"
    elif user_input == "21":
        brand = 'celkon'
        user_url = "https://www.gsmarena.com/celkon-phones-75.php"
    elif user_input == "22":
        brand = 'chea'
        user_url = "https://www.gsmarena.com/chea-phones-24.php"
    elif user_input == "23":
        brand = 'coolpad'
        user_url = "https://www.gsmarena.com/coolpad-phones-105.php"
    elif user_input == "24":
        brand = 'cubot'
        user_url = "https://www.gsmarena.com/cubot-phones-130.php"
    elif user_input == "25":
        brand = 'dell'
        user_url = "https://www.gsmarena.com/dell-phones-61.php"
    elif user_input == "26":
        brand = 'doogee'
        user_url = "https://www.gsmarena.com/doogee-phones-129.php"
    elif user_input == "27":
        brand = 'emporia'
        user_url = "https://www.gsmarena.com/emporia-phones-93.php"
    elif user_input == "28":
        brand = 'energizer'
        user_url = "https://www.gsmarena.com/energizer-phones-106.php"
    elif user_input == "29":
        brand = 'ericsson'
        user_url = "https://www.gsmarena.com/ericsson-phones-2.php"
    elif user_input == "30":
        brand = 'eten'
        user_url = "https://www.gsmarena.com/eten-phones-40.php"
    elif user_input == "31":
        brand = 'fairphone'
        user_url = "https://www.gsmarena.com/fairphone-phones-127.php"
    elif user_input == "32":
        brand = 'fujitsu siemens'
        user_url = "https://www.gsmarena.com/fujitsu_siemens-phones-50.php"
    elif user_input == "33":
        brand = 'garmin-asus'
        user_url = "https://www.gsmarena.com/garmin_asus-phones-65.php"
    elif user_input == "34":
        brand = 'gigabyte'
        user_url = "https://www.gsmarena.com/gigabyte-phones-47.php"
    elif user_input == "35":
        brand = 'gionee'
        user_url = "https://www.gsmarena.com/gionee-phones-92.php"
    elif user_input == "36":
        brand = 'google'
        user_url = "https://www.gsmarena.com/google-phones-107.php"
    elif user_input == "37":
        brand = 'haier'
        user_url = "https://www.gsmarena.com/haier-phones-33.php"
    elif user_input == "38":
        brand = 'hmd'
        user_url = "https://www.gsmarena.com/hmd-phones-133.php"
    elif user_input == "39":
        brand = 'honor'
        user_url = "https://www.gsmarena.com/honor-phones-121.php"
    elif user_input == "40":
        brand = 'hp'
        user_url = "https://www.gsmarena.com/hp-phones-41.php"
    elif user_input == "41":
        brand = 'htc'
        user_url = "https://www.gsmarena.com/htc-phones-45.php"
    elif user_input == "42":
        brand = 'huawei'
        user_url = "https://www.gsmarena.com/huawei-phones-58.php"
    elif user_input == "43":
        brand = 'i-mate'
        user_url = "https://www.gsmarena.com/i_mate-phones-35.php"
    elif user_input == "44":
        brand = 'i-mobile'
        user_url = "https://www.gsmarena.com/i_mobile-phones-52.php"
    elif user_input == "45":
        brand = 'icemobile'
        user_url = "https://www.gsmarena.com/icemobile-phones-69.php"
    elif user_input == "46":
        brand = 'infinix'
        user_url = "https://www.gsmarena.com/infinix-phones-119.php"
    elif user_input == "47":
        brand = 'innostream'
        user_url = "https://www.gsmarena.com/innostream-phones-29.php"
    elif user_input == "48":
        brand = 'inq'
        user_url = "https://www.gsmarena.com/inq-phones-60.php"
    elif user_input == "49":
        brand = 'intex'
        user_url = "https://www.gsmarena.com/intex-phones-102.php"
    elif user_input == "50":
        brand = 'itel'
        user_url = "https://www.gsmarena.com/itel-phones-131.php"
    elif user_input == "51":
        brand = 'jolla'
        user_url = "https://www.gsmarena.com/jolla-phones-84.php"
    elif user_input == "52":
        brand = 'karbonn'
        user_url = "https://www.gsmarena.com/karbonn-phones-83.php"
    elif user_input == "53":
        brand = 'kyocera'
        user_url = "https://www.gsmarena.com/kyocera-phones-17.php"
    elif user_input == "54":
        brand = 'lava'
        user_url = "https://www.gsmarena.com/lava-phones-94.php"
    elif user_input == "55":
        brand = 'leeco'
        user_url = "https://www.gsmarena.com/leeco-phones-109.php"
    elif user_input == "56":
        brand = 'lenovo'
        user_url = "https://www.gsmarena.com/lenovo-phones-73.php"
    elif user_input == "57":
        brand = 'lg'
        user_url = "https://www.gsmarena.com/lg-phones-20.php"
    elif user_input == "58":
        brand = 'maxon'
        user_url = "https://www.gsmarena.com/maxon-phones-14.php"
    elif user_input == "59":
        brand = 'maxwest'
        user_url = "https://www.gsmarena.com/maxwest-phones-87.php"
    elif user_input == "60":
        brand = 'meizu'
        user_url = "https://www.gsmarena.com/meizu-phones-74.php"
    elif user_input == "61":
        brand = 'micromax'
        user_url = "https://www.gsmarena.com/micromax-phones-66.php"
    elif user_input == "62":
        brand = 'microsoft'
        user_url = "https://www.gsmarena.com/microsoft-phones-64.php"
    elif user_input == "63":
        brand = 'mitac'
        user_url = "https://www.gsmarena.com/mitac-phones-25.php"
    elif user_input == "64":
        brand = 'mitsubishi'
        user_url = "https://www.gsmarena.com/mitsubishi-phones-8.php"
    elif user_input == "65":
        brand = 'modu'
        user_url = "https://www.gsmarena.com/modu-phones-63.php"
    elif user_input == "66":
        brand = 'motorola'
        user_url = "https://www.gsmarena.com/motorola-phones-4.php"
    elif user_input == "67":
        brand = 'mwg'
        user_url = "https://www.gsmarena.com/mwg-phones-56.php"
    elif user_input == "68":
        brand = 'nec'
        user_url = "https://www.gsmarena.com/nec-phones-12.php"
    elif user_input == "69":
        brand = 'neonode'
        user_url = "https://www.gsmarena.com/neonode-phones-22.php"
    elif user_input == "70":
        brand = 'niu'
        user_url = "https://www.gsmarena.com/niu-phones-79.php"
    elif user_input == "71":
        brand = 'nokia'
        user_url = "https://www.gsmarena.com/nokia-phones-1.php"
    elif user_input == "72":
        brand = 'nothing'
        user_url = "https://www.gsmarena.com/nothing-phones-128.php"
    elif user_input == "73":
        brand = 'nvidia'
        user_url = "https://www.gsmarena.com/nvidia-phones-97.php"
    elif user_input == "74":
        brand = 'o2'
        user_url = "https://www.gsmarena.com/o2-phones-30.php"
    elif user_input == "75":
        brand = 'oneplus'
        user_url = "https://www.gsmarena.com/oneplus-phones-95.php"
    elif user_input == "76":
        brand = 'oppo'
        user_url = "https://www.gsmarena.com/oppo-phones-82.php"
    elif user_input == "77":
        brand = 'orange'
        user_url = "https://www.gsmarena.com/orange-phones-71.php"
    elif user_input == "78":
        brand = 'oscal'
        user_url = "https://www.gsmarena.com/oscal-phones-134.php"
    elif user_input == "79":
        brand = 'oukitel'
        user_url = "https://www.gsmarena.com/oukitel-phones-132.php"
    elif user_input == "80":
        brand = 'palm'
        user_url = "https://www.gsmarena.com/palm-phones-27.php"
    elif user_input == "81":
        brand = 'panasonic'
        user_url = "https://www.gsmarena.com/panasonic-phones-6.php"
    elif user_input == "82":
        brand = 'pantech'
        user_url = "https://www.gsmarena.com/pantech-phones-32.php"
    elif user_input == "83":
        brand = 'parla'
        user_url = "https://www.gsmarena.com/parla-phones-81.php"
    elif user_input == "84":
        brand = 'philips'
        user_url = "https://www.gsmarena.com/philips-phones-11.php"
    elif user_input == "85":
        brand = 'plum'
        user_url = "https://www.gsmarena.com/plum-phones-72.php"
    elif user_input == "86":
        brand = 'posh'
        user_url = "https://www.gsmarena.com/posh-phones-101.php"
    elif user_input == "87":
        brand = 'prestigio'
        user_url = "https://www.gsmarena.com/prestigio-phones-86.php"
    elif user_input == "88":
        brand = 'qmobile'
        user_url = "https://www.gsmarena.com/qmobile-phones-103.php"
    elif user_input == "89":
        brand = 'qtek'
        user_url = "https://www.gsmarena.com/qtek-phones-38.php"
    elif user_input == "90":
        brand = 'razer'
        user_url = "https://www.gsmarena.com/razer-phones-117.php"
    elif user_input == "91":
        brand = 'realme'
        user_url = "https://www.gsmarena.com/realme-phones-118.php"
    elif user_input == "92":
        brand = 'sagem'
        user_url = "https://www.gsmarena.com/sagem-phones-13.php"
    elif user_input == "93":
        brand = 'samsung'
        user_url = "https://www.gsmarena.com/samsung-phones-9.php"
    elif user_input == "94":
        brand = 'sendo'
        user_url = "https://www.gsmarena.com/sendo-phones-18.php"
    elif user_input == "95":
        brand = 'sewon'
        user_url = "https://www.gsmarena.com/sewon-phones-26.php"
    elif user_input == "96":
        brand = 'sharp'
        user_url = "https://www.gsmarena.com/sharp-phones-23.php"
    elif user_input == "97":
        brand = 'siemens'
        user_url = "https://www.gsmarena.com/siemens-phones-3.php"
    elif user_input == "98":
        brand = 'sonim'
        user_url = "https://www.gsmarena.com/sonim-phones-54.php"
    elif user_input == "99":
        brand = 'sony'
        user_url = "https://www.gsmarena.com/sony-phones-7.php"
    elif user_input == "100":
        brand = 'sony ericsson'
        user_url = "https://www.gsmarena.com/sony_ericsson-phones-19.php"
    elif user_input == "101":
        brand = 'spice'
        user_url = "https://www.gsmarena.com/spice-phones-68.php"
    elif user_input == "102":
        brand = 't-mobile'
        user_url = "https://www.gsmarena.com/t_mobile-phones-55.php"
    elif user_input == "103":
        brand = 'tcl'
        user_url = "https://www.gsmarena.com/tcl-phones-123.php"
    elif user_input == "104":
        brand = 'tecno'
        user_url = "https://www.gsmarena.com/tecno-phones-120.php"
    elif user_input == "105":
        brand = 'tel.me.'
        user_url = "https://www.gsmarena.com/tel_me_-phones-21.php"
    elif user_input == "106":
        brand = 'telit'
        user_url = "https://www.gsmarena.com/telit-phones-16.php"
    elif user_input == "107":
        brand = 'thuraya'
        user_url = "https://www.gsmarena.com/thuraya-phones-49.php"
    elif user_input == "108":
        brand = 'toshiba'
        user_url = "https://www.gsmarena.com/toshiba-phones-44.php"
    elif user_input == "109":
        brand = 'ulefone'
        user_url = "https://www.gsmarena.com/ulefone-phones-124.php"
    elif user_input == "110":
        brand = 'umidigi'
        user_url = "https://www.gsmarena.com/umidigi-phones-135.php"
    elif user_input == "111":
        brand = 'unnecto'
        user_url = "https://www.gsmarena.com/unnecto-phones-91.php"
    elif user_input == "112":
        brand = 'vertu'
        user_url = "https://www.gsmarena.com/vertu-phones-39.php"
    elif user_input == "113":
        brand = 'verykool'
        user_url = "https://www.gsmarena.com/verykool-phones-70.php"
    elif user_input == "114":
        brand = 'vivo'
        user_url = "https://www.gsmarena.com/vivo-phones-98.php"
    elif user_input == "115":
        brand = 'vk mobile'
        user_url = "https://www.gsmarena.com/vk_mobile-phones-37.php"
    elif user_input == "116":
        brand = 'vodafone'
        user_url = "https://www.gsmarena.com/vodafone-phones-53.php"
    elif user_input == "117":
        brand = 'wiko'
        user_url = "https://www.gsmarena.com/wiko-phones-96.php"
    elif user_input == "118":
        brand = 'wnd'
        user_url = "https://www.gsmarena.com/wnd-phones-51.php"
    elif user_input == "119":
        brand = 'xcute'
        user_url = "https://www.gsmarena.com/xcute-phones-43.php"
    elif user_input == "120":
        brand = 'xiaomi'
        user_url = "https://www.gsmarena.com/xiaomi-phones-80.php"
    elif user_input == "121":
        brand = 'xolo'
        user_url = "https://www.gsmarena.com/xolo-phones-85.php"
    elif user_input == "122":
        brand = 'yezz'
        user_url = "https://www.gsmarena.com/yezz-phones-78.php"
    elif user_input == "123":
        brand = 'yota'
        user_url = "https://www.gsmarena.com/yota-phones-99.php"
    elif user_input == "124":
        brand = 'yu'
        user_url = "https://www.gsmarena.com/yu-phones-100.php"
    elif user_input == "125":
        brand = 'zte'
        user_url = "https://www.gsmarena.com/zte-phones-62.php"

    else:
        print("Pilihan tidak valid.")
        exit()
    print(f"✅ Brand yang dipilih: {brand}")

    return user_url, brand

# ========= DETAIL SCRAPER: FAST & AMAN DARI BLOKIR ========= #
def extract_detail_data_request(url, status, max_retries=3):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"
    }

    for attempt in range(max_retries):
        try:
            response = requests.get(url, headers=headers, timeout=10)
            if response.status_code == 429:
                wait = random.uniform(5, 10)
                print(f"[WARN] 429 Too Many Requests for {status}, tunggu {wait:.1f} detik...")
                time.sleep(wait)
                continue

            response.raise_for_status()
            soup = BeautifulSoup(response.text, "html.parser")
            specs_table = soup.select_one("div#specs-list")
            if not specs_table:
                return {}

            specs = {}
            for category in specs_table.select("table"):
                category_name = category.select_one("th")
                for row in category.select("tr"):
                    label = row.select_one("td.ttl")
                    value = row.select_one("td.nfo")
                    if label and value:
                        specs[f"{category_name.text.strip()} - {label.text.strip()}"] = value.text.strip()

            print(f"[DONE] Detail: {status}")
            return specs

        except requests.RequestException as e:
            wait = random.uniform(3, 6)
            print(f"[ERROR] Gagal request {status} (percobaan {attempt+1}) => {e}. Tunggu {wait:.1f}s")
            time.sleep(wait)

    print(f"[FAIL] Gagal total ambil {status} setelah {max_retries} percobaan.")
    return {}

# ========= PRODUK SCRAPER ========= #
def extract_product_data(soup, start_index=0):
    product = soup.select("div.section-body div.makers ul li")
    page_items = []

    for index, item in enumerate(product):
        global_index = start_index + index + 1
        product_name = item.select_one("span")
        detail_link_tag = item.select_one("a[href]")
        detail_link = "https://www.gsmarena.com/" + str(detail_link_tag['href'].strip()) \
            if detail_link_tag else ""

        page_items.append({
            'no': global_index,
            'product_name': product_name.text.strip() if product_name else "",
            'detail_link': detail_link
        })

        print(f'[INFO] {product_name.text.strip()} Data Found')

    return page_items

# ========= TOMBOL NEXT ========= #
def klik_tombol_next(driver):
    try:
        next_btn = WebDriverWait(driver, 8).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "a.prevnextbutton[title='Next page']"))
        )
        if "prevnextbuttondis" in next_btn.get_attribute("class"):
            return False
        driver.execute_script("arguments[0].scrollIntoView(true);", next_btn)
        time.sleep(1)
        next_btn.click()
        return True
    except (TimeoutException, ElementClickInterceptedException, NoSuchElementException, NoSuchWindowException, WebDriverException):
        return False

def brand_list():
    print(f'''
Pilih merk yg anda inginkan :  
1. Acer             	26. Doogee          	51. Jolla           	76. Oppo            	101. Spice          
2. alcatel          	27. Emporia         	52. Karbonn         	77. Orange          	102. T-Mobile       
3. Allview          	28. Energizer       	53. Kyocera         	78. Oscal           	103. TCL            
4. Amazon           	29. Ericsson        	54. Lava            	79. Oukitel         	104. Tecno          
5. Amoi             	30. Eten            	55. LeEco           	80. Palm            	105. Tel.Me.        
6. Apple            	31. Fairphone       	56. Lenovo          	81. Panasonic       	106. Telit          
7. Archos           	32. Fujitsu Siemens 	57. LG              	82. Pantech         	107. Thuraya        
8. Asus             	33. Garmin-Asus     	58. Maxon           	83. Parla           	108. Toshiba        
9. AT&T             	34. Gigabyte        	59. Maxwest         	84. Philips         	109. Ulefone        
10. Benefon         	35. Gionee          	60. Meizu           	85. Plum            	110. Umidigi        
11. BenQ            	36. Google          	61. Micromax        	86. Posh            	111. Unnecto        
12. BenQ-Siemens    	37. Haier           	62. Microsoft       	87. Prestigio       	112. Vertu          
13. Bird            	38. HMD             	63. Mitac           	88. QMobile         	113. verykool       
14. BlackBerry      	39. Honor           	64. Mitsubishi      	89. Qtek            	114. vivo           
15. Blackview       	40. HP              	65. Modu            	90. Razer           	115. VK Mobile      
16. BLU             	41. HTC             	66. Motorola        	91. Realme          	116. Vodafone       
17. Bosch           	42. Huawei          	67. MWg             	92. Sagem           	117. Wiko           
18. BQ              	43. i-mate          	68. NEC             	93. Samsung         	118. WND            
19. Casio           	44. i-mobile        	69. Neonode         	94. Sendo           	119. XCute          
20. Cat             	45. Icemobile       	70. NIU             	95. Sewon           	120. Xiaomi         
21. Celkon          	46. Infinix         	71. Nokia           	96. Sharp           	121. XOLO           
22. Chea            	47. Innostream      	72. Nothing         	97. Siemens         	122. Yezz           
23. Coolpad         	48. iNQ             	73. Nvidia          	98. Sonim           	123. Yota           
24. Cubot           	49. Intex           	74. O2              	99. Sony            	124. YU             
25. Dell            	50. itel            	75. OnePlus         	100. Sony Ericsson  	125. ZTE                      
          ''')

# ========= MAIN PROGRAM ========= #
print("========== PHONE DATA SCRAPER ==========\n")
print(f'SELAMAT DATANG :)')
print(f'''
      Program Ini Dapat Meng Generate Data SmartPhone Ter Update
      versi ini cukup stabil, namun hindari mengambil terlalu banyak
      data secara sekaligus untuk menghindari pemblokiran
      
      GUNAKAN DGN BIJAK
      JIKA ANDA MENDAPAT MASALAH JGN SALAHKAN SAYA\n''')

next_message = input("Tekan Enter Bila Setuju ")

brand_list()

user_url, brand = user_choise()

search_url = user_url
os.makedirs("output", exist_ok=True)

options = Options()
options.add_argument("--headless=new")  # ✅ HEADLESS agar browser tidak muncul
options.add_argument("--disable-gpu")
options.add_argument("--window-size=1920,1080")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--no-sandbox")
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36")
options.add_argument('--ignore-certificate-errors')

driver = webdriver.Chrome(options=options)
driver.get(search_url)
time.sleep(2)

all_items = []
current_index = 0

try:
    while True:
        try:
            soup = BeautifulSoup(driver.page_source, "html.parser")
        except Exception as e:
            print(f"[WARNING] Gagal mengambil page source: {e}")
            break

        items = extract_product_data(soup, start_index=current_index)
        all_items.extend(items)
        current_index += len(items)

        if not klik_tombol_next(driver):
            print("[INFO] Halaman terakhir atau tidak bisa klik Next.")
            break

        time.sleep(2)

finally:
    # SCRAPE DETAIL SETELAH SEMUA PRODUK TERKUMPUL
    print("[INFO] Mulai ambil data detail dari tiap produk (pakai requests)...")
    for i, item in enumerate(all_items):
        print(f"[{i+1}/{len(all_items)}] Ambil detail: {item['product_name']}")
        detail_data = extract_detail_data_request(item['detail_link'], item['product_name'])
        item.update(detail_data)
        time.sleep(random.uniform(1.5, 3.5))  # ✅ jeda acak agar tidak diblokir

    # Simpan hasil ke CSV
    filename = f"output/smartphone {brand}.csv"
    pd.DataFrame(all_items).to_csv(filename, index=False, encoding='utf-8')
    print(f"[DONE] Data disimpan ke: {filename}")
    time.sleep(5)
    try:
        driver.quit()
    except:
        pass