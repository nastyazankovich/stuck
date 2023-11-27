import scrapy


class StackOverflowSpider(scrapy.Spider):
    name = 'stack'
    start_urls = ['https://ru.stackoverflow.com/questions?tab=Newest/']

    def parse(self, response):
        print(12345)
        questions = response.css('div.s-post-summary--content')
        print(questions)
        for i in questions:
            title = i.css('a::text').get()
            description = i.css('div.s-post-summary--content-excerpt::text').get()
            print(title)
            print(description)
            yield {
                'title': title,
                'description': description

            }
        # for question in questions:
        #     title = question.css('.s-post-summary--content-title::text').get()
        #     description = question.css('.s-post-summary--content-excerpt"::text').get()
        #     yield {
        #         'title': title,
        #         'description': description
        #     }
        #     print(title)
        #     print(description)
