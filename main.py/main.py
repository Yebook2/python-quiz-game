def main():
    print("=" * 20)
    print("  파이썬 퀴즈 게임  ")
    print("=" * 20)
    print("1. 게임 시작")
    print("2. 점수 확인")
    print("3. 종료")
    print("=" * 20)

    choice = input("원하는 메뉴 번호를 입력하세요: ")
    
    if choice == '1':
        print("게임을 시작합니다!")
    elif choice == '2':
        print("최고 점수를 확인합니다.")
    elif choice == '3':
        print("게임을 종료합니다. 안녕!")
    else:
        print("잘못된 입력입니다. 1~3번을 선택해 주세요.")

if __name__ == "__main__":
    main()