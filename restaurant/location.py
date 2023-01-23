from .models import Location


# Location class handle


class LocationClass:
    citys = ['Jerusalem', 'Tel Aviv-Yafo', 'Haifa', 'Rishon LeẔiyyon', 'Petaẖ Tiqwa', 'Ashdod', 'Netanya', 'Beersheba', 'Bené Beraq', 'Holon', 'Ramat Gan', 'Ashqelon', 'Reẖovot', 'Bat Yam', 'Bet Shemesh', 'Kefar Sava', 'Herẕliyya', 'Hadera', 'Modi‘in Makkabbim Re‘ut', 'Nazareth', 'Lod', 'Ramla', 'Ra‘ananna', 'Rahat', 'Nahariyya', 'Givatayim', 'Hod HaSharon', 'Rosh Ha‘Ayin', 'Qiryat Ata', 'Umm el Faḥm', 'Qiryat Gat', 'Eilat', 'Nes Ẕiyyona', '‘Akko', 'El‘ad', 'Ramat HaSharon', 'Karmiel', 'Afula', 'Tiberias', 'Eṭ Ṭaiyiba', 'Qiryat Yam', 'Qiryat Moẕqin', 'Qiryat Bialik', 'Qiryat Ono', 'Or Yehuda', 'Ma‘alot Tarshīḥā', 'Ẕefat', 'Dimona', 'Tamra', 'Netivot', 'Sakhnīn', 'Yehud', 'Al Buţayḩah', 'Al Khushnīyah', 'Fīq']
    
    def create(self):
        for city in self.citys:
            location = Location.objects.create(location=city)
            location.save()

