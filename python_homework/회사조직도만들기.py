# 구현 내용

# 사람 클래스를 하나 만듭니다. 사람의 기본 요소는 이름, 나이, 성별로 합시다.
# 직장 동료 클래스를 사람 클래스를 이용해서 만듭시다. 사람 기본 요소 외 별도의 추가 사항은 직급입니다.
# 힌트

# 클래스와 상속을 활용합니다.
# 사람의 기본 요소인 이름, 나이, 성별은 각각 새로운 사람을 만들 때, 입력을 받을 수 있도록 합시다.
# 직장 동료의 기본 직급은 "대리"로 지정합니다.
# (고급) 사람 클래스에서 새로운 사람을 만들 때 입력은 그대로 유지하면서, 직급도 처음 만들어질 때 입력하도록 변경을 도전해봅시다.



class People:
    
    def __init__(self,name,age,sex):
        self.name =name
        self.age = age
        self.sex = sex

class Colleague(People):
    
    def __init__(self,name,age,sex,position):
        super().__init__(name,age,sex)
        self.position = position



company_people = Colleague('이치훈','36','남자','과장')
print(company_people.name)
print(company_people.sex)
print(company_people.age)
print(company_people.position)
print(company_people.__dict__)
