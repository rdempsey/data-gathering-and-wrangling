from scrapy.spider import Spider
from scrapy.selector import Selector

from govbenefitsspider.items import ProgramDetail

class ProgramDetailsSpider(Spider):
  name = "programdetails"
  allowed_domains = ["benefits.gov"]

  base_url = "http://www.benefits.gov"
  start_urls = ["http://www.benefits.gov/benefits/benefit-details/1578"]
  # Parse the JSON file and extract the detail urls

  def parse(self, response):
    sel = Selector(response)
    programs = sel.xpath('//div[@class="main"]')

    for program in programs:
      item = ProgramDetail()

      xp = lambda x: program.xpath(x).extract()
      
      item['program_title'] = xp('//div[@class="span8 benefit-detail-title"]/text()')
      
      # item['program_description'] = xp('')
      
      item['managing_agency'] = xp('//div[@class="span4 benefit-detail-agency"]/span[2]/text()')
      
      item['managing_agency_url'] = xp('//div[@class="span4 benefit-detail-agency"]/span[3]/a/@href')
      
      # item['general_program_requirements'] = xp('')
      
      # item['application_process'] = xp('')

      # item['program_contact_information'] = xp('')

      yield item