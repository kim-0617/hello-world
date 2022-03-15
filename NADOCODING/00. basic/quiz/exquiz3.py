class Word:
    def __init__(self,new_word, item1, item2, answer):
        self.new_word = new_word
        self.item1 = item1
        self.item2 = item2
        self.answer = answer

    def show_question(self):
        print(
            f"""
            - 출력 결과
            "{self.new_word}" 의 뜻은?
            1. {self.item1}
            2. {self.item2}
            """
        )

    def check_answer(self, num):
        if num == self.answer:
            print("정답입니다.")
        else:
            print("틀렸습니다.")
        
word = Word("얼죽아", "얼어 죽어도 아메리카노", "얼굴만은 죽어도 아기피부", 1)
word.show_question()
word.check_answer(int(input("=> ")))