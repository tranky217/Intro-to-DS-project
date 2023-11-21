import scrapy
from housing_data.items import HousingDataItem


class HomedySpider(scrapy.Spider):
    name = "homedy"
    allowed_domains = ["homedy.com"]
    start_urls = ["https://homedy.com/search/p1?typeId=1&fbclid=IwAR3XiZgCdq3gBurtge2q_dNMnad2wiAte3cM_LoOIDI5Pif1NaMoT2gmwkM"]

    custom_settings = {
        'FEEDS': {'data.json' : {'format': 'json'}}
    }
    def parse(self, response):
        houses = response.css("div.box-content div.item:not(.item-iframe)")
        # extract all the links in each page
        base_url = "https://homedy.com"

        scraped_number = 0
        for house in houses:
            # if(house.css())
            info_url = house.css("div.info a::attr(href)").get()
            # print(info_url)
            full_into_url = base_url + info_url
            scraped_number += 1
            print(f"\n house number : {scraped_number}")
            # print(f"after concaternating: {full_into_url}")
            # jump to parse method to parse each item data
            yield scrapy.Request(full_into_url, callback = self.parse_house_page)
        relative_next_page = response.css("div.box-content + div.page-nav ul li a::attr(href)").getall()[-1]
        abs_next_page = "none"
        if("p10" not in relative_next_page):
            abs_next_page = base_url + relative_next_page
        if(abs_next_page != "none"):
            yield response.follow(abs_next_page, callback = self.parse)
    
    def parse_house_page(self, response):
        container = response.css("div.product-detail-top") 

        # # haven't seen any exception
        short_info = container.css("div.option-bar div.short-item")
        title = container.css("h1::text").get()

        price = short_info.css("strong span::text").get()
        acreage = short_info.css("span:contains('Diện tích') + strong span::text").get()
        address = container.css("div.address a ~ span::text").getall()
        street = ""
        district = ""
        city = ""
        try:
            if(len(address) > 3):
                street = address[-3]
                district = address[-2]
                city = address[-1]
            elif(len(address) > 2):
                street = address[0]
                district = address[1]
                city = address[2]
            elif(len(address) > 1):
                district = address[0]
                city = address[1]
            else:
                city = address[0]
            print(f"\naddress: {street} - {district} - {city}")
        except IndexError as i:
            print(f"\n*********** somthing when wrong in taking address info: {i}***********\n")
        
        print(f"\ntitle: {title}")
        print(f"\nprice: {price}")
        print(f"\nacreage: {acreage}")
        
        # prone to exception
        # each department or house have different attributes
        attributes = response.css("div.content div.product-attributes")
        # try:
        type = attributes.css("div.product-attributes--item span:contains('Loại hình') + span::text").get()
        # except :
        print(f"\ntype: {type}")

        legal_status = attributes.css("div.product-attributes--item span:contains('Tình trạng pháp lý') + span::text").get()
        print(f"\nlegal_status: {legal_status}")
        
        corner = attributes.css("div.product-attributes--item span:contains('Căn góc') + span::text").get()
        print(f"\ncorner unit: {corner}")
        
        num_of_bedrooms = attributes.css("div.product-attributes--item span:contains('Số phòng ngủ') + span::text").get()
        print(f"\nnumber of bderooms: {num_of_bedrooms}")
        
        num_of_floors = attributes.css("div.product-attributes--item span:contains('Số tầng') + span::text").get()
        print(f"\nnumber of floors: {num_of_floors}")
        
        interior = attributes.css("div.product-attributes--item span:contains('Nội thất') + span::text").get()
        print(f"\ninterior: {interior}")
        
        house_direction = attributes.css("div.product-attributes--item span:contains('Hướng nhà') + span::text").get()
        print(f"\nhouse direction: {house_direction}")
        balcony_direction = attributes.css("div.product-attributes--item span:contains('Hướng ban công') + span::text").get()
        print(f"\nbalcony direction: {balcony_direction}")
        
        facade = attributes.css("div.product-attributes--item span:contains('Mặt tiền') + span::text").get()
        way_in = attributes.css("div.product-attributes--item span:contains('Đường vào') + span::text").get()
        # ridig structure
        location = response.css("div.location_reviews")
        area_population = location.css("div.text-location div.lc-info div.text label:contains('Số dân') + span::text").get()
        area_acreage = location.css("div.text-location div.lc-info div.text label:contains('Diện tích') + span::text").get()
        
        being_sold = location.css("div.text-location div.lc-info div.text label:contains('Số BĐS đang bán') + span strong::text").get()
        print(f"\nbeing sold: {being_sold}")
        print("\n---------------------------------------------------\n")
        
        # print(f"\narea_popula{}")
        # take care of being_sold_properties
        house = HousingDataItem()
        try:
            house["being_sold_properties"] = being_sold
        except KeyError:
            print("\n********* what the fuck just happend with being sold properties ********\n")
            print(f"\n herer it is {being_sold}")
        house["title"] = title
        house["price"] = price
        house["acreage"] = acreage
        house["street"] = street
        house["district"] = district
        house["city"] = city
        house["type"] = type
        house["legal_status"] = legal_status
        house["corner_unit"] = corner
        house["num_of_bedrooms"] = num_of_bedrooms
        house["num_of_floors"] = num_of_floors
        house["interior"] = interior
        house["area_population"] = area_population
        house["area_acreage"] = area_acreage
        # house["being_sold_properties"] == being_sold
        house["house_direction"] = house_direction
        house["balcony_direction"] = balcony_direction
        house["facade"] = facade
        house["way_in"] = way_in
        yield house
