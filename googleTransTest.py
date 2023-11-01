import pprint

import googletrans

trans = googletrans.Translator() #구글 번역 객체

str = input("번역할 문장을 입력하세요:")


#pprint.pprint(googletrans.LANGUAGES)#번역 언어 종류 ticker 불러오기/pprint 딕셔너리 예쁘게 보여줌


result1=trans.translate(str, dest='en')#한글을 영어로 번역
result2=trans.translate(str, dest='ja')#한글을 영어로 번역
result3=trans.translate(str, dest='zh-cn')#한글을 영어로 번역

print(f"입력하신{str}은 영어로 '{result1.text}'입니다")
print(f"입력하신{str}은 일본어로 '{result2.text}'입니다")
print(f"입력하신{str}은 중국어로 '{result3.text}'입니다")


