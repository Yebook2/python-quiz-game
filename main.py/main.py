# 1. 퀴즈 클래스 정의
class Quiz:
    def __init__(self, question, choices, answer):
        self.question = question  # 문제 내용
        self.choices = choices    # 보기 (리스트)
        self.answer = answer      # 정답 번호 (1, 2, 3, 4)

    def is_correct(self, user_answer):
        # 사용자가 입력한 번호가 정답과 일치하는지 확인
        return user_answer == str(self.answer)

# 2. 퀴즈 데이터 생성
def get_quiz_list():
    return [
        Quiz("파이썬에서 출력을 할 때 사용하는 함수는?", ["1. input", "2. print", "3. len", "4. type"], 2),
        Quiz("대한민국의 수도는?", ["1. 부산", "2. 인천", "3. 서울", "4. 대구"], 3),
        Quiz("파이썬의 상징 동물은?", ["1. 사자", "2. 호랑이", "3. 뱀", "4. 독수리"], 3),
        Quiz("1 + 1은?", ["1. 1", "2. 2", "3. 3", "4. 4"], 2),
        Quiz("리스트에 요소를 추가하는 함수는?", ["1. add", "2. push", "3. append", "4. insert"], 3)
    ]

# 3. 게임 실행 함수
def start_game():
    quizzes = get_quiz_list()
    score = 0

    print("\n--- 퀴즈를 시작합니다! ---")
    
    for i, q in enumerate(quizzes):
        print(f"\n문제 {i+1}: {q.question}")
        for choice in q.choices:
            print(choice)
        
        user_input = input("정답 번호를 입력하세요: ")
        
        if q.is_correct(user_input):
            print("정답입니다! ✨")
            score += 1
        else:
            print(f"아쉽네요. 정답은 {q.answer}번입니다. 😢")

    print(f"\n모든 문제를 풀었습니다!")
    print(f"당신의 최종 점수: {score} / {len(quizzes)}")

# 4. 메인 메뉴
def main():
    while True:
        print("\n" + "=" * 20)
        print("  파이썬 퀴즈 게임  ")
        print("=" * 20)
        print("1. 게임 시작")
        print("2. 종료")
        print("=" * 20)

        choice = input("메뉴를 선택하세요: ")

        if choice == '1':
            start_game()
        elif choice == '2':
            print("게임을 종료합니다. 다음에 또 봐요!")
            break
        else:
            print("잘못된 입력입니다. 1번이나 2번을 눌러주세요.")

if __name__ == "__main__":
    main()