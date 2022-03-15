# encode ([encoding, [errors]]) : 해당 인코딩으로 변경
# test_str = "가나다"
# print(test_str.encode('utf-8'))
# b'\xea\xb0\x80\xeb\x82\x98\xeb\x8b\xa4'

# endswith(postfix, [start,[end]]) : postfix로 문자열이 끝나면 True 반환
# test_str = "python is powerful"
# print(test_str.endswith("ful"))
# True

# expandtabs([tabsie]) : 탭을 공백으로 치환
# test_str = "python\tis\tpowerful"
# print(test_str)
# print(test_str.expandtabs(2))
# tabsize에 0 : 모든 탭이 없어짐
# tabsize에 1 : 첫번째 탭이 공백으로 치환됨
# tabsize에 2 : 두번째 탭이 공백으로 치환됨

# isaalnum() : 알파벳과 숫자로 이루어져 있으면 True 반환
# test_str = "python300"
# print(test_str.isalnum())
# True

# strip([chars]) : 공백제거, chars에 값이 있으면 그 문자에 해당하는 모든 조합을 제거
# test_str = "<<< python is powerful >>>"
# print(test_str.strip('<>'))
# python is powerful (<> 제거)

