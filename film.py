class Film:
    def __init__(self, title, episode_id, opening_crawl, director, producer, release_date):
        self._title = title
        self._episode_id = episode_id
        self._opening_crawl = opening_crawl
        self._director = director
        self._producer = producer
        self._release_date = release_date

    @property
    def title(self):
        return self._title
    @property
    def episode_id(self):
        return self._episode_id
    @property
    def opening_crawl(self):
        return self._opening_crawl
    @property
    def director(self):
        return self._director
    @property
    def producer(self):
        return self._producer
    @property
    def release_date(self):
        return self._release_date

    @title.setter
    def title(self, title):
        self._title = title
    @episode_id.setter
    def episode_id(self, episode_id):
        self._episode_id = episode_id
    @opening_crawl.setter
    def opening_crawl(self, opening_crawl):
        self._opening_crawl = opening_crawl
    @director.setter
    def director(self, director):
        self._director = director
    @producer.setter
    def producer(self, producer):
        self._producer = producer
    @release_date.setter
    def release_date(self, release_date):
        self._release_date = release_date
