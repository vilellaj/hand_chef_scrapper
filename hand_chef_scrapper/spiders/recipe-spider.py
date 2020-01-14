import scrapy
from ..models import recipe


class RecipeSpider(scrapy.Spider):
    name = "panelinha"

    allowed_domains = ["panelinha.com.br"]
    start_urls = [
        'https://www.panelinha.com.br/home/cozinhapratica2019-2',
        'https://www.panelinha.com.br/home/cardapios-rapidos',
        'https://www.panelinha.com.br/home/receitas-refogado'
    ]

    def parse(self, response):
        for recipe in response.css("article"):
            recipe_url = recipe.css("a::attr(href)").extract_first()

            if recipe_url is not None and "receita" in recipe_url:
                yield scrapy.Request(response.urljoin(recipe_url), callback=self.parse_item)

    def parse_item(self, response):
        item = recipe.Recipe()

        item['url'] = response.url
        item['title'] = response.css('h1::text').extract_first()
        item['thumb'] = response.css(
            'section.section__recipe-highlight img::attr(src)').get()
        item['ingredients'] = response.css(
            'div.editor > ul > li::text').getall()
        item['directions'] = response.css(
            'div.editor > ol > li::text').getall()
        item['readyInTime'] = response.css('span.dd::text')[1].get(),
        item['servings'] = response.css('span.dd::text')[2].get()

        return item
