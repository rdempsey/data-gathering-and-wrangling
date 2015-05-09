from scrapy.item import Item, Field

class BenefitProgramItem(Item):
  program_title = Field()
  program_description = Field()
  program_details_link = Field()

class ProgramDetail(Item):
  program_title = Field()
  program_description = Field()
  managing_agency = Field()
  managing_agency_url = Field()
  general_program_requirements = Field()
  application_process = Field()
  program_contact_information = Field()