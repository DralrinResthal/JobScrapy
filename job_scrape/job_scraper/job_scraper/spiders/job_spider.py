import scrapy
import json
from datetime import date
from ..items import JobScraperItem


class JobSpider(scrapy.Spider):
    name = "jobs"
    start_urls = [
        "https://www.indeed.com/jobs?q=Python%20Developer%20%2450%2C000&l=Fort%20Worth%2C%20TX&radius=50&vjk=50d12d27d21c624d",
    ]

    temp_start_urls = []

    def parse(self, response):
        items = JobScraperItem()

        job_cards = response.css(".jobsearch-SerpJobCard").getall()
        link_list = response.css(".pagination-list li a::attr(href)").getall()
        job_list = []
        log_data = f"{response.url}\n"

        # Get the paginated links
        for link in link_list:
            next_page = f"https://indeed.com{link}"
            if next_page not in self.temp_start_urls:
                self.temp_start_urls.append(next_page)
                print(self.temp_start_urls)
                yield scrapy.Request(next_page, callback=self.parse)
            else:
                continue

        # Seperating, filtering and creating jobs based on scraped data
        for job in response.css(".jobsearch-SerpJobCard"):

            job_title = (
                "".join(job.css(".title ::text").extract())
                .replace("\n", "")
                .replace("new", "")
            )

            job_link = f"https://indeed.com{job.css('.title a::attr(href)').get()}"

            company = "".join(
                job.css(".jobsearch-SerpJobCard .company ::text").extract()
            ).replace("\n", "")

            salary = "".join(
                job.css(
                    ".jobsearch-SerpJobCard .salarySnippet .salary .salaryText::text"
                ).getall()
            ).replace("\n", "")

            if "Python" in job_title:
                items["title"] = job_title
                items["link"] = job_link
                items["company"] = company
                items["salary"] = salary

                yield items

            else:
                continue