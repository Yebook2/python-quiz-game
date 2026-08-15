import json
import os
import signal
import sys

class Quiz:
    def __init__(self, question, choices, answer):
        self.question = question
        self.choices = choices
        self.answer = int(answer)

    def is_correct(self, user_answer):
        return int(user_answer) == self.answer

    def to_dict(self):
        return {"question": self.question, "choices": self.choices, "answer": self.answer}

class QuizGame:
    def __init__(self, filename="state.json"):
        self.filename = filename
        self.quizzes = []
        self.high_score = 0
        self.load_data()

    def load_data(self):
        try:
            with open(self.filename, 'r', encoding='utf-8') as f:
                data = json.load(f)
                self.quizzes = [Quiz(q['question'], q['choices'], q['answer']) for q in data.get('quizzes', [])]
                self.high_score = data.get('high_score', 0)
            
            if not self.quizzes:
                self.set_default_quizzes()
                
        except (FileNotFoundError, json.JSONDecodeError):
      
       
            self.set_default_quizzes()

    def set_default_quizzes(self):
        self.quizzes = [
            Quiz("파이썬의 창시자는?", ["1. Guido van Rossum", "2. Elon Musk", "3. Steve Jobs", "4. James Gosling"], 1),
            Quiz("리스트에 요소를 추가하는 함수는?", ["1. add", "2. push", "3. append", "4. insert"], 3),
            Quiz("파이썬의 출력 함수는?", ["1. print", "2. echo", "3. console.log", "4. printf"], 1),
            Quiz("파이썬의 확장자는?", ["1. .pt", "2. .py", "3. .python", "4. .pi"], 2),
            Quiz("참과 거짓을 나타내는 자료형은?", ["1. int", "2. str", "3. bool", "4. float"], 3)
        ]
        self.save_data()

    def save_data(self):
        data = {
            "quizzes": [q.to_dict() for q in self.quizzes],
            "high_score": self.high_score
        }
        try:
            with open(self.filename, 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=4)
        except IOError:
            print("\n[경고] 데이터를 저장하는 중 오류가 발생했습니다.")

    def play(self):
        if not self.quizzes:
            print("퀴즈가 없습니다.")
            return

        score = 0
        print("\n--- 퀴즈를 시작합니다! ---")
        for i, q in enumerate(self.quizzes):
            print(f"\n문제 {i+1}: {q.question}")
            for choice in q.choices:
                print(choice)
            
            while True:
                try:
                    user_input = int(input("정답 번호를 입력하세요 (1-4): "))
                    if 1 <= user_input <= 4:
                        break
                    print("1~4 사이의 숫자를 입력해주세요.")
                except ValueError:
                    print("숫자만 입력해주세요. (빈칸 입력 불가)")

            if q.is_correct(user_input):
                print("정답입니다!")
                score += 1
            else:
                print(f"아쉽네요. 정답은 {q.answer}번입니다.")

        print("\n모든 문제를 풀었습니다!")
        print(f"당신의 최종 점수: {score} / {len(self.quizzes)}")
        
        if score > self.high_score:
            self.high_score = score
            print("최고 기록 갱신!")
            self.save_data()

    def add_quiz(self):
        question = input("질문 입력: ")
        choices = [input(f"보기 {i+1}: ") for i in range(4)]
        while True:
            try:
                answer = int(input("정답 번호(1-4): "))
                if 1 <= answer <= 4:
                    break
                print("1~4 사이만 가능합니다.")
            except ValueError:
                print("숫자를 입력하세요.")
        
        self.quizzes.append(Quiz(question, choices, answer))
        self.save_data()
        print("퀴즈 추가 완료!")

    def show_quizzes(self):
        print("\n--- 퀴즈 목록 ---")
        for i, q in enumerate(self.quizzes):
            print(f"{i+1}. {q.question}")


def main():
    game = QuizGame()

    def signal_handler(sig, frame):
        print("\n\n강제 종료 감지! 현재 상태를 저장하고 안전하게 종료합니다.")
        game.save_data()
        sys.exit(0)

    signal.signal(signal.SIGINT, signal_handler)

    while True:
        print(f"\n=== 파이썬 퀴즈 게임 (최고점수: {game.high_score}) ===")
        print("1. 게임 시작")
        print("2. 퀴즈 추가")
        print("3. 퀴즈 목록 보기")
        print("4. 종료")

        choice = input("메뉴를 선택하세요: ")

        if choice == '1':
            game.play()
        elif choice == '2':
            game.add_quiz()
        elif choice == '3':
            game.show_quizzes()
        elif choice == '4':
            game.save_data()
            print("데이터를 안전하게 저장했습니다. 게임을 종료합니다.")
            break
        else:
            print("잘못된 입력입니다. 1~4번을 선택해주세요.")

if __name__ == "__main__":
    main()

