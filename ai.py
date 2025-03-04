for i in range(20, 2001):
    if i % 2 != 0:
        is_prime = True
        if i > 1:
            for j in range(2, int(i**0.5) + 1):
                if i % j == 0:
                    is_prime = False
                    break
        else:
            is_prime = False

        if is_prime:
            print("소수")
        else:
            print(1)
    else:
        print(2)

# https://data.busan.go.kr/bdip/analysis/addressCleaning.do
# https://marketplace.visualstudio.com/items?itemName=Google.geminicodeassist
# https://bookshelf-journey.tistory.com/entry/%EC%B4%88%EB%B3%B4%EC%9E%90%EB%A5%BC-%EC%9C%84%ED%95%9C-Gemini-Code-Assist-for-individuals-%EC%82%AC%EC%9A%A9-%EA%B0%80%EC%9D%B4%EB%93%9C