#completed
import requests
from bs4 import BeautifulSoup
target_price = 1799.00
my_email = "vishnutester95@gmail.com"
# lets extract the price first
import smtplib
url = "https://www.amazon.com/Alienware-15-6inch-i7-10750H-GeForce-AWm15-7272WHT-PUS" \
      "/dp/B0897ZBRQR/?_encoding=UTF8&pd_rd_w=BvUhM&pf_rd_p=21b0f1e9-721e-43b5-bb7a-5" \
      "616fc4f0fe1&pf_rd_r=J3Z7WB94KXXS8MYRQ2YA&pd_rd_r=e2cc9285-b97a-4fac-83ed-ed037" \
      "88debee&pd_rd_wg=eKOgN&ref_=pd_gw_hlp13n_bbn&th=1"

headers = {
    "Accept-Language": "en-US,en;q=0.9,te;q=0.8,la;q=0.7",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 "
                "Safari/537.36"

}
response = requests.get(url=url, headers=headers)
data_amazon = response.text

#print(data_amazon)

soup = BeautifulSoup(data_amazon, 'html.parser')

name_of_product = soup.find(name="span", class_="a-size-large product-title-word-break")
name_of_product = name_of_product.getText()
price = soup.find(name="span", class_="a-size-medium a-color-price priceBlockBuyingPriceString").getText()
price_numbers = (price[1:].split(","))
final_price = ""
for i in price_numbers:
    final_price += i
final_price = float(final_price)
if final_price < target_price:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user="vishnutester95@gmail.com", password="Qwerty@123")
        connection.sendmail(from_addr=my_email, to_addrs="vishnukalyan95@gmail.com",
                            msg=f"The {name_of_product} is below the desired price. You can buy it now")
