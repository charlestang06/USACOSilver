# https://codeforces.com/contest/279/problem/B

n, t = map(int, input().split())
books = list(map(int, input().split()))

# prefix sum
books.insert(0, 0)

for i in range(1, n + 1):
    books[i] += books[i - 1]

pointerOne = 0
pointerTwo = 1

max_books = 0

while pointerOne < n and pointerTwo <= n:
    if books[pointerTwo] - books[pointerOne] <= t:
        max_books = max(max_books, pointerTwo - pointerOne)
        pointerTwo += 1
    else:
        pointerOne += 1

print(max_books)
