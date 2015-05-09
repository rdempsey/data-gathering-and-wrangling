from scrapy.spider import Spider
from scrapy.selector import Selector

from govbenefitsspider.items import BenefitProgramItem

class BenefitProgramSpider(Spider):
  name = "benefitprograms"
  allowed_domains = ["benefits.gov"]
  start_urls = [
        "http://www.benefits.gov/benefits/browse-by-category/category/FOO"
    ]

  def parse(self, response):
    sel = Selector(response)
    programs = sel.xpath('//div[@class="top"]')

    for program in programs:
      item = BenefitProgramItem()
      item['program_title'] = program.xpath(
            'span[@class="benefit-header"]/a/text()').extract()
      item['program_details_link'] = program.xpath(
           'span[@class="benefit-header"]/a/@href').extract()
      item['program_description'] = program.xpath(
           'span[@class="benefit-description hidden-phone"]/text()').extract()
      yield item