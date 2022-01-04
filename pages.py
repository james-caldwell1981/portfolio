class Page:

    def __init__(self, url, page_type, title, custom_layout, custom_script):
        self.url = url
        self.page_type = page_type
        self.title = title
        self.custom_layout = custom_layout
        self.custom_script = custom_script


class Landing(Page):

    def __init__(self, url, page_type, title, articles=None,
                 projects=None, kaggles=None, tutorials=None,
                 experiments=None, custom_layout=None,
                 custom_script=None):
        self.articles = articles
        self.projects = projects
        self.kaggles = kaggles
        self.tutorials = tutorials
        self.experiments = experiments

        super().__init__(url, page_type, title, custom_layout,
                         custom_script)


class Full(Page):

    def __init__(self, url, page_type, title,
                 body_text=None, images=None, relevant_links=None,
                 references=None, custom_style=None, comments=None,
                 custom_layout=None, custom_script=None):
        self.body_text = body_text
        self.images = images
        self.relevant_links = relevant_links
        self.references = references
        self.custom_style = custom_style
        self.comments = comments

        super().__init__(url, page_type, title, custom_layout,
                         custom_script)


class Gallery(Page):

    def __init__(self, url, page_type, title,
                 pages=None, description=None, num_pages=None,
                 custom_script=None):
        self.pages = pages
        self.description = description
        self.num_pages = num_pages

        super().__init__(url, page_type, title, custom_script)
