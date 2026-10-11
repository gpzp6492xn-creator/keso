import time
import random
import string
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

# إعداد خيارات المتصفح للعمل بسلاسة
chrome_options = Options()
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

# تشغيل المتصفح
driver = webdriver.Chrome(options=chrome_options)

try:
    # 1. فتح صفحة إنشاء حساب فيسبوك الجديدة
    driver.get("https://www.facebook.com/reg/")
    time.sleep(3)

    # توليد بيانات عشوائية (اسم ولقب)
    first_names = ["Ahmed", "Mohamed", "Ali", "Khaled", "Mahmoud", "Ibrahim"]
    last_names = ["Hassan", "Ali", "Samir", "Mostafa", "Adel", "Youssef"]
    
    random_first = random.choice(first_names)
    random_last = random.choice(last_names)
    
    # توليد بريد إلكتروني أو رقم عشوائي مؤقت / بيانات وهمية للاختبار
    random_pass = ''.join(random.choices(string.ascii_letters + string.digits, k=10))

    # 2. ملء الاسم الأول والأخير
    firstname_field = driver.find_element(By.NAME, "firstname")
    firstname_field.send_keys(random_first)

    lastname_field = driver.find_element(By.NAME, "lastname")
    lastname_field.send_keys(random_last)

    # 3. ملء تاريخ الميلاد عشوائياً
    day_select = driver.find_element(By.ID, "day")
    day_select.send_keys(str(random.randint(1, 28)))

    month_select = driver.find_element(By.ID, "month")
    month_select.send_keys("Jan")

    year_select = driver.find_element(By.ID, "year")
    year_select.send_keys(str(random.randint(1995, 2005)))

    # 4. تحديد النوع (مثلاً ذكر)
    gender_radio = driver.find_element(By.XPATH, "//input[@value='2']")
    gender_radio.click()

    # 5. الوصول لحقل رقم التليفون أو البريد (هنا بيقف السكربت لحد ما تدخله أو نربطه بخطوة الأرقام)
    print("تم ملء البيانات العشوائية بنجاح، ووصلنا لحقل إدخال رقم الهاتف!")
    
    # إيقاف مؤقت لمشاهدة النتيجة
    time.sleep(10)

finally:
    driver.quit()
