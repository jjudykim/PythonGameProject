#051
movie_rank = ["닥터 스트레인지", "스플릿", "럭키"]

#052
movie_rank.append("배트맨")
print(movie_rank)

#053
movie_rank.insert(1, "슈퍼맨")
print(movie_rank)

#054
del movie_rank[3]
print(movie_rank)

#055
del movie_rank[2]
del movie_rank[2]
print(movie_rank)

#056
lang1 = ["C", "C++", "JAVA"]
lang2 = ["Python", "Go", "C#"]
new_lang = lang1 + lang2
print(new_lang)

#057
nums = [1, 2, 3, 4, 5, 6, 7]
print("max : ", max(nums))
print("min : ", min(nums))

#058
nums2 = [1, 2, 3, 4, 5]
print(sum(nums2))

#059
cook = ["피자", "김밥", "만두", "양념치킨", "족발", "피자", "김치만두", "쫄면", "쏘세지", "라면", "팥빙수", "김치전"]
print(len(cook))

#060
nums3 = [1, 2, 3, 4, 5]
print(sum(nums3) / len(nums3))
