# 1. 퀴즈 클래스 정의
class Quiz:
    def __init__(self, question, choices, answer):
        self.question = question  # 문제 내용
        self.choices = choices    # 보기 (리스트)
        self.answer = answer      # 정답 번호 (1, 2, 3, 4)

    def is_correct(self, user_answer):
        # 사용자가 입력한 번호가 정답과 일치하는지 확인
        return user_answer == str(self.answer)

# 2. 퀴즈 데이터 생성 (파일에서 읽어오기)
def get_quiz_list():
    quiz_objects = []
    try:
        with open("quizzes.txt", "r", encoding="utf-8") as file:
            for line in file:
                # 줄바꿈 제거 후 '|' 기호로 분리
                parts = line.strip().split("|")
                if len(parts) == 3:
                    question = parts[0]
                    choices = parts[1].split(",") # 쉼표로 보기 분리
                    answer = int(parts[2])
                    # Quiz 객체 생성 후 리스트에 추가
                    quiz_objects.append(Quiz(question, choices, answer))
    except FileNotFoundError:
        print("❌ quizzes.txt 파일을 찾을 수 없습니다.")
    
    return quiz_objects

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

        # --- 여기서부터 예외 처리 시작 ---
        try:
            # 입력받은 값이 숫자인지 확인하기 위해 int()로 변환 시도
            user_answer = int(user_input) 
            
            # 숫자로 변환이 성공했다면 기존 정답 체크 로직 실행
            if q.is_correct(user_input):
                print("정답입니다! ✨")
                score += 1
            else:
                print(f"아쉽네요. 정답은 {q.answer}번입니다. 😅")
        
        except ValueError:
            # 사용자가 숫자가 아닌 문자(예: 'abc')를 입력했을 때 실행됨
            print("❌ 숫자만 입력해주세요! 이번 문제는 틀린 것으로 처리됩니다.")
        # --- 예외 처리 끝 ---

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