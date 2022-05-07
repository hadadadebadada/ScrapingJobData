import scrapy
from funscraper.items import SimpleItem
import re

class EntrylvljobspiderArgeSpider(scrapy.Spider):
    name = 'entrylvljobspider_arge'

    start_urls = [

        "https://www.arbeitsagentur.de/jobsuche/jobdetail/10000-1189058788-S",
        "https://www.arbeitsagentur.de/jobsuche/jobdetail/10000-1184995294-S",
        "https://www.arbeitsagentur.de/jobsuche/jobdetail/10000-1188751701-S",
        "https://www.arbeitsagentur.de/jobsuche/jobdetail/11858-448366900-sd-S",
        "https://www.arbeitsagentur.de/jobsuche/jobdetail/13621-504411220503020117-S",
        "https://www.arbeitsagentur.de/jobsuche/jobdetail/10000-1189054486-S",
        "https://www.arbeitsagentur.de/jobsuche/jobdetail/10000-1188745213-S",
        "https://www.arbeitsagentur.de/jobsuche/jobdetail/15265-k45925.2085-S",
        "https://www.arbeitsagentur.de/jobsuche/jobdetail/11858-450537700-sd-S",
        "https://www.arbeitsagentur.de/jobsuche/jobdetail/13243-4537124000000-jb-S",
        "https://www.arbeitsagentur.de/jobsuche/jobdetail/10000-1188899291-S",
        "https://www.arbeitsagentur.de/jobsuche/jobdetail/11858-448028800-sd-S",
        "https://www.arbeitsagentur.de/jobsuche/jobdetail/10000-1188904507-S",
        "https://www.arbeitsagentur.de/jobsuche/jobdetail/10000-1189018905-S",
        "https://www.arbeitsagentur.de/jobsuche/jobdetail/13621-504407220503020117-S",
        "https://www.arbeitsagentur.de/jobsuche/jobdetail/13621-504405220503020117-S",
        "https://www.arbeitsagentur.de/jobsuche/jobdetail/13621-504428220503020117-S",
        "https://www.arbeitsagentur.de/jobsuche/jobdetail/10000-1189022566-S",
        "https://www.arbeitsagentur.de/jobsuche/jobdetail/10000-1188688617-S",
        "https://www.arbeitsagentur.de/jobsuche/jobdetail/12288-2406212880-S",
        "https://www.arbeitsagentur.de/jobsuche/jobdetail/12634-493946_JB2767356-S",
        "https://www.arbeitsagentur.de/jobsuche/jobdetail/11119-2411021225-S",
        "https://www.arbeitsagentur.de/jobsuche/jobdetail/12117-11539627000-YF-S",
        "https://www.arbeitsagentur.de/jobsuche/jobdetail/10000-1189003885-S",
        "https://www.arbeitsagentur.de/jobsuche/jobdetail/10000-1189042611-S",
        "https://www.arbeitsagentur.de/jobsuche/jobdetail/10000-1187405492-S",
        "https://www.arbeitsagentur.de/jobsuche/jobdetail/11949-14446854-S",
        "https://www.arbeitsagentur.de/jobsuche/jobdetail/10000-1189009583-S",
        "https://www.arbeitsagentur.de/jobsuche/jobdetail/10000-1188919734-S",
        "https://www.arbeitsagentur.de/jobsuche/jobdetail/10000-1189017759-S",
        "https://www.arbeitsagentur.de/jobsuche/jobdetail/13621-509720220503020117-S",
        "https://www.arbeitsagentur.de/jobsuche/jobdetail/10000-1189023745-S",
        "https://www.arbeitsagentur.de/jobsuche/jobdetail/13643-3L_334214-S",
        "https://www.arbeitsagentur.de/jobsuche/jobdetail/13643-3L_334212-S",
        "https://www.arbeitsagentur.de/jobsuche/jobdetail/13643-3L_334200-S",
        "https://www.arbeitsagentur.de/jobsuche/jobdetail/11289-210776082-S",
        "https://www.arbeitsagentur.de/jobsuche/jobdetail/11119-2400313451-S",
        "https://www.arbeitsagentur.de/jobsuche/jobdetail/10000-1188994483-S",
        "https://www.arbeitsagentur.de/jobsuche/jobdetail/11081-9353401-S",
        "https://www.arbeitsagentur.de/jobsuche/jobdetail/11070-800932-1-S",
        "https://www.arbeitsagentur.de/jobsuche/jobdetail/10000-1189061324-S",
        "https://www.arbeitsagentur.de/jobsuche/jobdetail/12288-2408291663-S",
        "https://www.arbeitsagentur.de/jobsuche/jobdetail/12362-PUB304772_333879LS-S",
        "https://www.arbeitsagentur.de/jobsuche/jobdetail/14369-2021exjwu2fs-000-S",
        "https://www.arbeitsagentur.de/jobsuche/jobdetail/10000-1182191767-S",
        "https://www.arbeitsagentur.de/jobsuche/jobdetail/12288-2409532960-S",
        "https://www.arbeitsagentur.de/jobsuche/jobdetail/12288-2409395441-S",
        "https://www.arbeitsagentur.de/jobsuche/jobdetail/12288-2408383985-S",
        "https://www.arbeitsagentur.de/jobsuche/jobdetail/12288-2408344195-S",
        "https://www.arbeitsagentur.de/jobsuche/jobdetail/12288-2408278854-S",
        "https://www.arbeitsagentur.de/jobsuche/jobdetail/11949-14448440-S",
        "https://www.arbeitsagentur.de/jobsuche/jobdetail/11949-14446829-S",
        "https://www.arbeitsagentur.de/jobsuche/jobdetail/11119-2410857844-S",
        "https://www.arbeitsagentur.de/jobsuche/jobdetail/12265-295261_JB2761997-S",
        "https://www.arbeitsagentur.de/jobsuche/jobdetail/11858-447058500-sd-S",
        "https://www.arbeitsagentur.de/jobsuche/jobdetail/10000-1188748407-S",
        "https://www.arbeitsagentur.de/jobsuche/jobdetail/10000-1186234900-S",
        "https://www.arbeitsagentur.de/jobsuche/jobdetail/12362-PUB352494_336535LS-S",
        "https://www.arbeitsagentur.de/jobsuche/jobdetail/10000-1188882060-S",
        "https://www.arbeitsagentur.de/jobsuche/jobdetail/12739-NHH1Y5E0VCHPIKQV-S",
        "https://www.arbeitsagentur.de/jobsuche/jobdetail/10000-1188816815-S",
        "https://www.arbeitsagentur.de/jobsuche/jobdetail/10000-1188395160-S",
        "https://www.arbeitsagentur.de/jobsuche/jobdetail/10000-1189015662-S",
        "https://www.arbeitsagentur.de/jobsuche/jobdetail/13319-605968/1_336703LS-S",
        "https://www.arbeitsagentur.de/jobsuche/jobdetail/10000-1188128269-S",
        "https://www.arbeitsagentur.de/jobsuche/jobdetail/13643-2L_334246-S",
        "https://www.arbeitsagentur.de/jobsuche/jobdetail/10000-1188898792-S",
        "https://www.arbeitsagentur.de/jobsuche/jobdetail/13319-611665/1_332570LS-S",
        "https://www.arbeitsagentur.de/jobsuche/jobdetail/12362-PUB352506_336394LS-S",
        "https://www.arbeitsagentur.de/jobsuche/jobdetail/15112-764908-1-S",
        "https://www.arbeitsagentur.de/jobsuche/jobdetail/13621-6473-1355808-0-S",
        "https://www.arbeitsagentur.de/jobsuche/jobdetail/13319-615380/1_336498LS-S",
        "https://www.arbeitsagentur.de/jobsuche/jobdetail/10000-1188682590-S",
        "https://www.arbeitsagentur.de/jobsuche/jobdetail/12288-2409481789-S",
        "https://www.arbeitsagentur.de/jobsuche/jobdetail/10000-1188983911-S",
        "https://www.arbeitsagentur.de/jobsuche/jobdetail/12688-1147555600000-RJA-S",
        "https://www.arbeitsagentur.de/jobsuche/jobdetail/11868-9398088-S",
        "https://www.arbeitsagentur.de/jobsuche/jobdetail/13643-3L_333726-S",
        "https://www.arbeitsagentur.de/jobsuche/jobdetail/13643-336905LS-S",
        "https://www.arbeitsagentur.de/jobsuche/jobdetail/12908-028833497-S",
        "https://www.arbeitsagentur.de/jobsuche/jobdetail/12288-2410395269-S",
        "https://www.arbeitsagentur.de/jobsuche/jobdetail/12288-2409435543-S",
        "https://www.arbeitsagentur.de/jobsuche/jobdetail/12288-2409394932-S",
        "https://www.arbeitsagentur.de/jobsuche/jobdetail/12288-2409384062-S",
        "https://www.arbeitsagentur.de/jobsuche/jobdetail/12288-2408378516-S",
        "https://www.arbeitsagentur.de/jobsuche/jobdetail/12288-2408274530-S",
        "https://www.arbeitsagentur.de/jobsuche/jobdetail/11858-452024500-sd-S",
        "https://www.arbeitsagentur.de/jobsuche/jobdetail/11858-432052000-sd-S",
        "https://www.arbeitsagentur.de/jobsuche/jobdetail/11119-2410920995-S",
        "https://www.arbeitsagentur.de/jobsuche/jobdetail/10000-1189032054-S",
        "https://www.arbeitsagentur.de/jobsuche/jobdetail/10000-1188940677-S",
        "https://www.arbeitsagentur.de/jobsuche/jobdetail/10000-1189045053-S",
        "https://www.arbeitsagentur.de/jobsuche/jobdetail/10000-1188956041-S",
        "https://www.arbeitsagentur.de/jobsuche/jobdetail/12265-307936_JB2761922-S",
        "https://www.arbeitsagentur.de/jobsuche/jobdetail/12362-PUB352566_336661LS-S",
        "https://www.arbeitsagentur.de/jobsuche/jobdetail/15933-0017788374-S",
        "https://www.arbeitsagentur.de/jobsuche/jobdetail/10000-1188955171-S",
        "https://www.arbeitsagentur.de/jobsuche/jobdetail/10000-1187465194-S",
        "https://www.arbeitsagentur.de/jobsuche/jobdetail/10000-1189046931-S",
        "https://www.arbeitsagentur.de/jobsuche/jobdetail/14369-20224wicydq8-000-S",


    ]

    def parse(self, response):
        item = SimpleItem()
        pattern = '''(?:[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*|"(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*")@(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\[(?:(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9]))\.){3}(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9])|[a-z0-9-]*[a-z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])+)\])'''
        myRespo = response.text
        x = re.search(pattern, myRespo)

        if x is not None:
            item['company'] = response.xpath('//*[@id="jobdetails-arbeitgeberArbeitgeber"]//text()').extract()[0]


            title = response.xpath('//*[@id="jobdetails-titel"]//text()').extract()[0]
            item['title'] = title
            print(x.group(0))
            item['ref'] = x.group(0)
            item['url'] =response.request.url[49:]
            item['address'] = response.xpath('//*[@id="jobdetails-firmenadresse"]//text()').extract()[0]

        yield item




    #################DOWNLOAD HTML################################################################
    # def parse(self, response):
    #     filename = response.url.split("/")[-1] + '.html'
    #     with open(filename, 'wb') as f:
    #         f.write(response.body)




