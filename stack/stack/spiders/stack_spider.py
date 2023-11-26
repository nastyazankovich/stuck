import scrapy


class StackOverflowSpider(scrapy.Spider):
    name = 'stack'
    start_urls = ['https://ru.stackoverflow.com/questions?tab=Newest']

    def parse(self, response):
        questions = response.css('.question-summary')
        for question in questions:
            title = question.css('.title::text').get()
            description = question.css('.excerpt::text').get()
            yield {
                'title': title,
                'description': description
            }

