import time
import os
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

ram_type = input("Ce tip de RAM cautati:  ").strip()
frequency = input("Ce frecvență va intereseaza : ").strip()
max_price = float(input("Care este pretul maxim (lei): ").strip())

options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

try:
    driver.get("https://www.cel.ro/")
    search_box = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "keyword"))
    )
    search_box.send_keys(f"{ram_type} {frequency}")
    search_box.submit()
    time.sleep(2)

    try:
        category_link = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//a[contains(text(),'Memorii')]"))
        )
        category_link.click()
        time.sleep(2)
    except:
        print("Nu am găsit categoria Memorii.")

    try:
        sort_select = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "sortare"))
        )
        driver.execute_script(
            "arguments[0].value = 'pret'; arguments[0].dispatchEvent(new Event('change'))",
            sort_select
        )
        time.sleep(3)
    except:
        print("Nu am găsit butonul de sortare.")

    try:
        products = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div.product_data.productListing-tot"))
        )
        print(f"Am găsit {len(products)} produse.")
    except:
        print("Nu s-au găsit produse.")
        products = []

    product_list = []
    for prod in products:
        try:
            title_elem = prod.find_element(By.CSS_SELECTOR, "h2 a")
            title = title_elem.text
            href = title_elem.get_attribute("href")
        except:
            title = "N/A"
            href = ""
        try:
            price_text = \
            prod.find_element(By.CSS_SELECTOR, ".price").text.replace('.', '').replace(',', '.').split(' ')[0]
            price = float(price_text)
        except:
            price = 0
        product_list.append({"Title": title, "Price": price, "Element": prod, "Href": href})

    filtered = []
    for p in product_list:
        prod_elem = p["Element"]
        stoc = prod_elem.find_elements(By.CSS_SELECTOR, "strong.info_stoc.in_stoc_furnizor")
        if stoc and p['Price'] <= max_price:
            filtered.append(p)

    if not filtered:
        print("Nu am găsit produse pe stoc care să se încadreze în prețul tău.")
    else:
        df = pd.DataFrame(filtered[:10])[["Title", "Price", "Href"]]
        df.rename(columns={"Href": "Link"}, inplace=True)
        excel_name = os.path.join(os.getcwd(), f"RAM_{ram_type}_{frequency}.xlsx")
        df.to_excel(excel_name, index=False)
        print(f"Excel generat: {excel_name}")

        first_prod = filtered[0]
        href_prod = first_prod["Href"]
        try:
            driver.get(href_prod)

            buy_a_tag = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "div.specialButtons a[href*='cumpara_market']"))
            )
            buy_link = buy_a_tag.get_attribute("href")

            driver.get(buy_link)
            print(f"Produs adaugat in cos: {first_prod['Title']}")

        except Exception as e:
            print(f"Nu am putut adăuga produsul: {first_prod['Title']}, eroare: {e}")

        try:
            driver.get("https://www.cel.ro/index.php?main_page=shopping_cart")
            print("Cosul a fost deschis.")
        except Exception as e:
            print(f"Nu am reușit să deschid cosul: {e}")

finally:
    input("Apasă Enter pentru a închide browserul...")
    driver.quit()
