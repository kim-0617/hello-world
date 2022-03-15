class House:
    def __init__(self, location, house_type, deal_tpye, price,  completion_year):
        self.location = location
        self.house_type = house_type
        self.deal_type = deal_tpye
        self.price = price
        self.completion_year = completion_year
    def show_detail(self):
        print(f"{self.location} {self.house_type} {self.deal_type} {self.price} {self.completion_year}")

gangnam_apt = House("강남", "아파트", "매매", "10억", "2010년")
mapo_op = House("마포", "오피스텔", "전세", "5억", "2007년")
songpa_vila = House("송파", "빌라", "월세", "500/50", "2000년")

house_list = []
house_list.append(gangnam_apt)
house_list.append(mapo_op)
house_list.append(songpa_vila)

print(f"총 {len(house_list)}대의 매물이 있습니다.")
for i in house_list:
    i.show_detail()