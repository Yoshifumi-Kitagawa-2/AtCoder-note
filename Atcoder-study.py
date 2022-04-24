#数字のみからなる、長さがちょうど9の文字列Sが与えられます。
#Sには0から9までのうち、ちょうど1つの数字を除いた9種類の数字が一度ずつ登場します。
#Sに登場しない唯一の数字を出力してください。
m = input()
for n in range(10):
    if"{}".format(n)not in m:
        print(n)

#A匹のスライムがいます。
#すぬけくんが1回叫ぶたびに、スライムはK倍に増殖します。
#スライムがB匹以上になるには、すぬけくんは最小で何回叫ぶ必要があるでしょうか？
a,b,k=map(int,input().split())
ans=0
while a<b:
    ans+=1
    a*=k
print(ans)

#長さNの整数からなる数列 A=(A1,…,AN) であって、
#以下の条件を全て満たすものは何通りありますか？
#1≤Ai≤M (1≤i≤N)
# N
# ∑Ai≤K
# i=1
# ただし、答えは非常に大きくなることがあるので、答えを 998244353 で割った余りを求めてください。
#動的計画法で解くことができる。
def main():
    import math
    n, m, K = map(int, input().split())
    mod=998244353
#dpの定義 dp[i][j]:=数列の先頭から i 項まで決めた際に、総和が j であるような数列の決め方の総数
    dp = [[0]*(K+1) for _ in range(n+1)]
#dpの初期値：はじめ、dp[0][0]=1で残りは0で埋めます。
    dp[0][0] = 1
#dpの遷移iの昇順に計算していきます。 
#j=0,…,K−1、k=1,…,M について、もしj+k≤Kならば、dp[i+1][j+k]にdp[i][j]を加算する、と遷移すればよいです。
    for i in range(n):
        for j in range(K):
            for k in range(1, m+1):
                if j+k <= K: 
                    dp[i+1][j+k] += dp[i][j] 
                    dp[i+1][j+k] %= mod
    res = 0
    for i in dp[n]:
        res = (res+i)%mod
    print(res)            
main()

#長さNの数列A=(A1,…,AN)が与えられます。
#以下の形式で与えられるQ個のクエリに答えてください。
#整数L,R,Xが与えられる。AL,…,ARのうち、値がXに等しいものの個数を求めよ。
#制約
#1≤N≤2×10^5
#1≤Ai≤N
#1≤Q≤2×10^5
#各クエリについて、1≤L≤R≤N,1≤X≤N
#入力は全て整数
#解説
# x=1,…,N それぞれについて、 Ai=x なるiを昇順に管理した配列をidxxとします。
#このとき、各クエリは以下のように言い換えられます。
#L,R,X が与えられる。 idxxの要素のうち、 L 以上 R 以下のものは何個あるか答えよ。
#解説
#このクエリはidxxの要素のうち L 以上の最小の要素は前から何番目か、R+1 以上の最小の要素は前から何番目かを求めることで解くことができ、
#これらは二分探索により O(logN) で求められます。
import bisect
N = int(input())
A = list(map(int, input().rstrip().split()))
Q = int(input())
Query = [list(map(int, input().rstrip().split())) for i in range(Q)]

idx = [[] for i in range(N)]

for i, a in enumerate(A):
    idx[a-1].append(i)

for q in Query:
    l,r,x = q
    l_ind = bisect.bisect_left(idx[x-1], l - 1)
    r_ind = bisect.bisect_right(idx[x-1], r - 1)
    print(r_ind - l_ind)

#横一列に4つのマスが並んでいます。
#各文字が0または1である長さ4の文字列Sが与えられます。
#Sのi文字目が1であるとき、左からi番目のマスには1人の人がおり、
#Sのi文字目が0であるとき、左からi番目のマスには人がいません。
#全ての人が一斉に、1つ右隣のマスへ移動します。この移動により、もともと右端のマスにいた人は消えます。
#移動後の各マスに人がいるかどうかを、Sと同様のルールで文字列として出力してください。
S = input()
#print(a[1:3])添字が1以上3未満の要素。-1は末尾の要素。
print("0" + S[:-1])

#人1,人2,…人NのN人の人がいます。人iの姓はsi、名はtiです。
# N人の人すべてにあだ名をつけることを考えます。人iのあだ名aiは以下の条件を満たす必要があります。
#aiは人iの姓あるいは名と一致する。言い換えると、ai=siまたは ai=tiの少なくとも一方が成り立つ。
#aiは自分以外の人の姓および名のどちらとも一致しない。
# 言い換えると、1≤j≤N,i=j を満たすすべての整数 j について ai≠sjかつai≠tjが成り立つ。
#N人全員に条件を満たすあだ名をつけることは可能でしょうか。可能ならば Yes を、そうでないならば No を出力してください。
N=int(input())
S=[]
T=[]
count=0
for _ in range(N):
    s,t= input().split #指定された数の文字列を格納する。
    S.append(s) #リスト.appen(リストに追加したい値)
    T.append(t)
for i in range(N):
    f1=f2=True
    for j in range(N):
        if i==j:
            continue
        if S[i]==S[j] or S[i]==T[j]:
            f1 = False
        if T[i]==T[j] or T[i]==S[j]:
            f2 = False
            print('Yes')
        if not(f1 or f2):
            print('No')
            exit()
print('Yes')

#列Snを次のように定義します。
# S1は 1 つの 1 からなる長さ 1 の列である。
# Sn(n は 2 以上の整数) は Sn−1, n, Sn−1をこの順につなげた列である。
#たとえばS2,S3は次のような列です。
#S2はS1, 2, S1をこの順につなげた列なので 1,2,1 である。
#S3はS2, 3, S2をこの順につなげた列なので 1,2,1,3,1,2,1 である。
#Nが与えられるので、列 SNをすべて出力してください。
#解答1：再帰関数
def S(n):
    if n == 1:
        return[1]
    else:
        return S(n-1)+[n]+S(n-1)
N=int(input())
print(*S(N))

#解答2：動的計画法
N=int(input())
dp=[[]for _ in range(N+1)]
dp[1]=1
for n in range(2,N+1):
    dp[n]=dp[n-1]+[n]+dp[n-1]
print(*dp[N])

#高橋君と青木君はジョギングをすることにしました。
#高橋君は「A 秒間秒速 B メートルで歩き、C 秒間休む」ことを繰り返します。
#青木君は「D 秒間秒速 E メートルで歩き、F 秒間休む」ことを繰り返します。
#二人が同時にジョギングを始めてから X 秒後、高橋君と青木君のうちどちらが長い距離を進んでいますか？

#高橋くん A*B*K+(X%(A+C))*B 青木くん D*E*K+(X%(D+F))*E
#自分の解答
def main():
    import math
    A,B,C,D,E,F,X= map(int, input().split())
    V = X/(A+C)
    W = X/(D+F)
    Y = X%(A+C)
    Z = X%(D+F)

    if B*(Y+A*V) > E*(Z+D*W):
        print('Takahashi')
    elif B*(Y+A*V) < E*(Z+D*W):
        print('Aoki')
    else:
        print('Draw')
main()
#模範解答
def solve(a,b,c,x):
  q = x // (a+c)
  r = x % (a+c)
  return (a*q + min(a, r)) * b #min(a, r)はaとrの小さい方

a,b,c,d,e,f,x = map(int, input().split()) #これは合ってた

takahashi = solve(a,b,c,x)
aoki = solve(d,e,f,x)
#以下も合ってた
if takahashi > aoki:
  print("Takahashi")
elif takahashi < aoki:
  print("Aoki")
else:
  print("Draw")

#英大文字と英小文字からなる文字列のうち、以下の条件を全て満たすものを素晴らしい文字列ということとします。
#英大文字が文字列の中に現れる。
# 英小文字が文字列の中に現れる。
#全ての文字が相異なる。
#例えば、AtCoder や Aa は素晴らしい文字列ですが、atcoder や Perfect は素晴らしい文字列ではありません。
#文字列 S が与えられるので、S が素晴らしい文字列か判定してください。
#自分の解答
S= input()
for i in range(len(S)):
    f=True
    for j in range(len(S)):
        if i == j:
            continue
        if S[i] == S[j]:
            f=False
if S.isupper()==True or S.islower()==True or f==False:
    print('No')
else:
    print('Yes')
#模範解答
#len(set(s))・・・セットは集合を表すデータ型で、リスト等と同様に複数の要素をもつことができます。setは重複の格納不可
#集合なので、リストとは異なり要素は順番をもちません。また、重複した要素は取り除かれます。
s=input()
if (not s.isupper()) and (not s.islower()) and len(s) == len(set(s)):
  print('Yes')
else:
  print('No')

#英小文字のみからなる N 個の文字列 S1,S2,…,SNが与えられます。
#S1,S2,…,SNから文字列を好きな個数選ぶことを考えます。
#このとき、「選んだ文字列の中でちょうど K 個の文字列に登場する英小文字」の種類数としてあり得る最大値を求めてください。
#制約
#1≤N≤15
#1≤K≤N
# N,K は整数
#Siは英小文字からなる空でない文字列である。
# 1≤i≤N を満たす整数 i に対し、Siに同じ文字は 2 個以上含まれない。
# i≠j ならば Si≠Sjである。
#解説
#N 個の文字列のうち、いくつか選ぶ方法は 2^N通りあります。
#この全てに対して、「選んだ文字列の中でちょうど K 個の文字列に登場する英小文字」の種類数を求めて最大値を出力すればよいです。
#計算量は O(2^N×N×σ) となります。ただし、σ は英小文字の種類数です。
# 実装の際には、それぞれの文字列を選ぶかどうかを N 桁の 2 進数とみなし、0 以上 2^N−1 以下の整数と対応させる bit全探索と呼ばれている手法が便利です。
n, k = map(int, input().split())

l = [[False for _ in range(26)] for _ in range(n)] #
for i in range(n):
    s = input()
    for j in range(len(s)):
        l[i][ord(s[j])-97] = True

result = 0
for i in range(2**n):
    count = 0
    for j in range(26):
        tmp = 0
        for m in range(n):
            if ((i >> m) & 1):
                if l[m][j]:
                    tmp += 1
        if tmp == k:
            count += 1
    result = max(result, count)

print(result)

#ABC245
#A問題
#ある日、高橋君は A時B分ちょうどに、青木君は C時D分1秒に起きました。
# 高橋君の起床時刻が青木君より早いならばTakahashiを、そうでないならばAokiを出力してください。
# 制約
# 0≤A≤23
# 0≤B≤59
# 0≤C≤23
# 0≤D≤59
# 入力はすべて整数である。
a,b,c,d=map(int,input().split()) #int(input())ではダメ。なぜなら、一行に複数の整数を入れたいから。
if a<c or (a==c and b<=d):
    print('Takahashi')
else:
    print('Aoki')
#B問題
# 長さ N の整数からなる数列 A=(A1,…,AN)が与えられます。
# A1,…,ANに含まれない最小の非負整数を求めてください。
#賢い。。。。
N=int(input())
A = list(map(int, input().split()))
for i in range(2001):
    if not i in A:
        print(i)
        exit()

#ABC244のAB問題
#A問題
# 英小文字からなる長さNの文字列Sが与えられます。Sの末尾の文字を出力してください。
N=int(input())
S=input()
print(S[N-1])
#B問題
# xy平面を考えます。x 軸の正の向きを東向き、y 軸の正の向きを北向きとします。
# 高橋君ははじめ、点 (x,y)=(0,0) にいて東（ x 軸の正の向き）を向いています。
# SとRのみからなる長さNの文字列 T=t1,t2…tNが与えられます。高橋君は i=1,2,…,N の順番で下記を行います。
#ti=S ならば、高橋君はいま向いている方向に距離 1 だけ進む。
# ti= R ならば、高橋君はその場で右に 90 度回転する。その結果、高橋君の向いている方向が下記の通りに変わる。
# 回転前の向きが東向き（ x 軸の正の向き）ならば、回転後の向きは南向き（ y 軸の負の向き）になる。
# 回転前の向きが南向き（ y 軸の負の向き）ならば、回転後の向きは西向き（ x 軸の負の向き）になる。
# 回転前の向きが西向き（ x 軸の負の向き）ならば、回転後の向きは北向き（ y 軸の正の向き）になる。
# 回転前の向きが北向き（ y 軸の正の向き）ならば、回転後の向きは東向き（ x 軸の正の向き）になる。
# 上記の手順を終えた後に高橋君がいる点の座標を出力してください。
#解答①
N = int(input())
T = input()
#北：N, 東：E, 南：S, 西：W
direct = "E"
#座標
x = 0
y = 0
for n in range(N):
  #移動
  if T[n]=="S":
    if direct=="E":
      x += 1
    elif direct=="W":
      x -= 1
    elif direct=="N":
      y += 1
    elif direct=="S":
      y -= 1
  #方向転換
  elif T[n]=="R":
    if direct=="E":
      direct = "S"
    elif direct=="W":
      direct = "N"
    elif direct=="N":
      direct = "E"
    elif direct=="S":
      direct = "W"
print(x, y)

#ABC243
#A問題
# 高橋君の家には、高橋君、高橋君の父、高橋君の母の3人が住んでおり、全員が毎晩風呂で髪を洗います。
# 風呂には、高橋君の父、高橋君の母、高橋君の順に入り、それぞれシャンプーを A,B,C ミリリットル使います。
# 今朝の時点で、ボトルには V ミリリットルのシャンプーが残っていました。このまま補充しない時、初めてシャンプーが不足するのは誰が使おうとした時ですか？
v,a,b,c=map(int, input().split())
x = v%(a+b+c)
if x < a:
    print('F')
elif x>=a:
    x-=a
    if x < b:
        print('M')
    else:
        print('T')
#B問題
#長さ N の整数列 A=(A1,A2,…,AN),B=(B1,B2,…,BN)が与えられます。
# Aの要素はすべて異なります。Bの要素もすべて異なります。
# 次の 2 つを出力してください。
# AにもBにも含まれ、その位置も一致している整数の個数。言い換えると、Ai=Biを満たす整数 i の個数。
# AにもBにも含まれるが、その位置は異なる整数の個数。言い換えると、Ai=Bj,i≠j を満たす整数の組 (i,j) の個数。
N=int(input())
A=list(map(int, input().split())) 
B=list(map(int, input().split())) 
ans1 = 0
ans2 = 0

for i in range(N):
    for j in range(N):
        if i == j:
            if A[i] == B[j]:
                ans1+=1
            else:
                continue
        elif i!=j:
            if A[i] == B[j]:
                ans2+=1
            else:
                continue
print(ans1)
print(ans2)

#ABCコンテスト242
#A問題
# あるプログラミングコンテストでは、以下のルールに従って参加者に T シャツをプレゼントします。
# 上位 A 位までの参加者は、必ず T シャツが貰える。
# 加えて、上位 A+1 位から B 位までの参加者のうち C 人が一様ランダムに選ばれ、選ばれた参加者は T シャツを貰える。
# コンテストには 1000 人が参加し、全ての参加者が相異なる順位を取りました。
# このコンテストの参加者であるいろはちゃんは、X 位を取りました。
# このとき、いろはちゃんが T シャツを貰える確率を求めてください。
#自分の解答
a,b,c,x = map(int, input().split())
ans = 0
if x<=a:
    ans=1
    print(ans)
elif a<x<=b:
    ans = c/(b-a)
    print(ans)
else:
    print(ans)

#B問題
# 文字列Sが与えられます。Sの各文字を並び替えて得られる文字列S′のうち、辞書順で最小のものを出力してください。
# なお、相異なる 2 つの文字列 s=s1s2…snと t=t1t2…tmについて、それらが以下の条件のいずれかを満たすとき、辞書順で s<t であるとします。
# ある整数 i (1≤i≤min(n,m)) が存在し、si<tiかつすべての整数 j (1≤j<i) について sj=tj
# すべての整数 i (1≤i≤min(n,m)) について si=tiかつ、n<m
S = list(input())
S.sort()
print(''.join(S)) #'間に挿入する文字列'.join([連結したい文字列のリスト])


