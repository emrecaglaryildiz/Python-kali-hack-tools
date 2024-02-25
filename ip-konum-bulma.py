import requests

def get_location_info(ip_address):
    try:
        # IP adresi için konum bilgilerini almak üzere ip-api.com servisine istek gönderme
        response = requests.get(f"http://ip-api.com/json/{ip_address}")
        data = response.json()
        
        # JSON'dan gelen bilgileri alma
        country = data['country']
        city = data['city']
        latitude = data['lat']
        longitude = data['lon']
        
        # Alınan konum bilgilerini döndürme
        return f"IP Adresi: {ip_address}\nÜlke: {country}\nŞehir: {city}\nEnlem: {latitude}\nBoylam: {longitude}"
    except requests.exceptions.RequestException as e:
        # IP adresi bulunamadığında veya bağlantı sorunu yaşandığında hata mesajı döndürme
        return "Hata: IP adresi bulunamadı veya bağlantı sorunu."

def main():
    # Kullanıcıdan IP adresi isteme
    ip_address = input("Lütfen bir IP adresi girin: ")
    
    # IP adresi için konum bilgilerini alma
    location_info = get_location_info(ip_address)
    
    # Alınan konum bilgilerini konsola yazma
    print(location_info)
    
    # Uygulamanın kapanmaması için bir tuşa basılmasını bekleme
    input("Devam etmek için bir tuşa basın...")

if __name__ == "__main__":
    main()
