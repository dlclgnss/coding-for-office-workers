class Article:
    author = "이치훈"
    count_view = 0

# 공통에 들어가는 내용을 적음
    def __init__(self,title,content):
        self.title= title
        self.content = content

    def read(self):
        self.count_view = self.count_view+1


article1 = Article('코딩','재미있는 파이썬')

# print(article1.count_view)
# article1.read()
# print(article1.count_view)


# Article을 상속
class BrunchArticle(Article):
    source = "브런치"

    #Article 내용을 변경 
    def read(self):
        self.count_view = self.count_view+2   

brunch_article = BrunchArticle('만남','장고로 만나요')
print(brunch_article.source)
print(brunch_article.title)
brunch_article.read()

print(brunch_article.count_view)




class School:
    def __init__(self,name,published,address):
        self.name = name
        self.published = published
        self.address = address

school_seoul = School('서울대',1960,'서울시')

print(school_seoul.name)
print(school_seoul.address)


