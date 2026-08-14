class Quiz:
    def __init__(self, question, choices, answer):
        self.question = question 
        self.choices = choices    
        self.answer = answer   

    def is_correct(self, user_answer):
        return user_answer == str(self.answer)

def get_quiz_list():
    quiz_objects = []
    try:
        with open("quizzes.txt", "r", encoding="utf-8") as file:
            for line in file:
                parts = line.strip().split("|")
                if len(parts) == 3:
                    question = parts[0]
                    choices = parts[1].split(",") 
                    answer = int(parts[2])
                    quiz_objects.append(Quiz(question, choices, answer))
    except FileNotFoundError:
        print("quizzes.txt 파일을 찾을 수 없습니다.")
    
    return quiz_objects

def start_game():
    quizzes = get_quiz_list()
    score = 0

    print("\n--- 퀴즈를 시작합니다! ---")

    for i, q in enumerate(quizzes):
        print(f"\n문제 {i+1}: {q.question}")
        for choice in q.choices:
            print(choice)
        
        user_input = input("정답 번호를 입력하세요: ")

        try:
            user_answer = int(user_input) 
            
            if q.is_correct(user_input):
                print("정답입니다! ✨")
                score += 1
            else:
                print(f"아쉽네요. 정답은 {q.answer}번입니다. ")
        
        except ValueError:
            print("숫자만 입력해주세요! 이번 문제는 틀린 것으로 처리됩니다.")

    print(f"\n모든 문제를 풀었습니다!")
    print(f"당신의 최종 점수: {score} / {len(quizzes)}")
    save_score(score) 

def save_score(score):
    with open("scores.txt", "a", encoding="utf-8") as file:
        file.write(f"최종 점수: {score}\n")
    print("점수가 scores.txt에 저장되었습니다.")

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

