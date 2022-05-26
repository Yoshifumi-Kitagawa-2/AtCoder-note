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

#ABCコンテスト241
#1桁の数字が表示される画面と、ボタンからなる機械があります。
#画面に数字kが表示されているとき、ボタンを1回押すと画面の数字が ak に変わります。
#0が表示されている状態からボタンを3回押すと、画面には何が表示されますか？
A=list(map(int,input().split()))
if A[0]==0:
    print(A[0])
elif A[0]!=0:
    n=int(A[0])
    if A[n]==n:
        print(A[n])
    elif A[n]!=n:
        m=int(A[n])
        print(A[m])
#正解!
#ABCコンテスト241B問題
#高橋君の家には N 本の麺からなるパスタがあり、i 本目の麺の長さは Aiです。
# 高橋君はこれから M 日間の食事計画を立てており、 i 日目にはパスタの麺のうち長さがちょうど Biであるようなものを 1 本選び、食べようと考えています。 もし、1 日目から M 日目の間に 1 日でもそのような麺が無い日があれば、食事計画は失敗となります。 また、同じ麺を複数の日に食べることはできません。
# 高橋君が食事計画を最後まで実行することは可能ですか？
#自分の回答
N,M=map(int, input().split())
for _ in range(N):
    A=map(int, input().split())
for _ in range(M):
    B=map(int, input().split())
for i in range(M):
    for j in range(N):
        if B[i]!=A[j]:
            j+=1
            continue
        elif B[i]==A[j]:
            i+=1
            continue
        else:
            print('No')
            exit()
print('Yes')
#模範回答
n,m=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
ans ='Yes'
for i in range(m):
    pasta = b[i]
    if pasta in a:
        a.remove(pasta)
    else:
        ans='No'
        break
print(ans)

#ABCコンテスト240A問題
#下の画像で示す図において、a 番の点と b 番の点が線で直接結ばれているかを答えてください。
a,b =map(int, input().split())
ans = 'Yes'
if a == 1:
    if b==2 or b==10:
        print(ans)
    else:
        ans = 'No'
        print(ans)
else:
    if b == a+1:
        print(ans)
    else:
        ans = 'No'
        print(ans)
#ABCコンテスト240B問題
#長さ N の正整数列 a=(a1,a2,…,aN) には何種類の整数が現れますか？
N =int(input())
a =list(map(int, input().split()))
A =set(a)
print(len(A))

#ABCコンテスト239A問題
#地上 x メートルの高さから見える水平線は x(12800000+x)
#メートル先にあるとするとき、地上Hメートルの高さから見える水平線が何メートル先にあるか求めてください。
H = int(input())
x = (H*(12800000+H))**0.5
print(x)

#ABCコンテスト239B問題
# −10^18以上 10^18以下の整数 X が与えられるので、⌊X/10⌋ を出力してください
#実数 x に対して、「x 以下の整数の中で最大の整数」を ⌊x⌋ と表します。たとえば ⌊4.7⌋=4,⌊−2.4⌋=−3,⌊5⌋=5 
X=int(input())
x = X//10
if x >= 0:
    print(x)
else:
    print(x)

#ABCコンテスト238A問題
# 2n>n^2ですか？
n = int(input())
if n >= 5 or n == 1:
    print('Yes')
else:
    print('No')

#ABCコンテスト238B問題
#ここに円形のピザが 1 枚あります。
# 高橋くんは長さ N の数列 A を使ってこのピザを以下の手順で切り分けます。
# 最初に、円の中心から 12 時の方向に切れ込みをひとつ入れます。
# 次に、以下の操作を N 回繰り返します。 i 回目の操作では以下を行います。
# まず、ピザを時計回りに Ai度回転させる。
# 次に、円の中心から 12 時の方向に切れ込みをひとつ入れる。
# 例えば、A=(90,180,45,195) として手順を行うと、下図のようになります。
#自分の回答
N = int(input())
A = list(map(int, input().split()))
S = list()
s=0
for i in range(N):
    if i == 0:
        s = A[i]
        S.append(s)
    else:
        s += S[i-1]+A[i]
        S.append(s)
def calc(n):
    return n%360
S2 = list()
for val in S:
    S2.append(calc(val))
S2.sort()
S3 = list()
x=0
for i in range(1,n):
    x = S2[i]-S2[i-1]
    S3.append(x)
print(max(S3))
#回答
n = input()
l1 = [int(item) for item in input().split()]
l2 = []
s = 0
for e in l1:
    s += e
    if(s >= 360): 
        s = s % 360
    l2.append(s)
l2.sort()
l3 = l2
ma = l3[0]
for i in range(1,len(l3)):
    ma = max(ma, l3[i]-l3[i-1])
ma = max(ma, 360 - l3[-1])
print(ma)

#ABCコンテスト237A問題
#整数Nが与えられます。 N が −2^31以上かつ2^31未満ならばYesを、そうでないならば No を出力してください。
N =int(input())
if N >= -2**31 and N < 2**31:
    print('Yes')
else:
    print('No')

#ABCコンテスト237B問題
# H 行 W 列の行列 A が与えられます。
# A の上から i 行目、左から j 列目の要素は Ai,jです。
# ここで、W 行 H 列の行列 B を、上から i 行目、左から j 列目の要素が Aj,iと一致するような行列として定めます。すなわち、B は A の転置行列です。
# Bを出力してください。

H,W = map(int,input().split())
#リスト内包表記
#上から順にlistを読み込んでlistに格納していく。
a = [list(map(int, input().split()))for l in range(W)]
b = [[]for i in range(H)]

for i in range(W):
    for j in range(H):
        b[i][j] = a[j][i]
for i in range(W):
    print(*b[i])

#回答
H,W = map(int,input().split())
A = []
for i in range(H):
    A_W = list(map(int,input().split()))
    A.append(A_W)

B = [[0]*H for i in range(W)]
for i in range(H):
    for j in range(W):
        B[j][i] = A[i][j]

for i in range(W):
    print(*B[i])

#ABCコンテスト236A問題
# 英小文字からなる文字列Sが与えられます。
# Sの先頭からa文字目とb文字目を入れ替えて得られる文字列を出力してください。
S = list(input().split())
a,b = map(int, input().split())
S2 = S
S2[a-1] = S[b-1]
S2[b-1] = S[a-1]
print("".join(S2))

#ABCコンテスト200B問題
#整数 N が与えられます。
#以下の操作を K 回行った後の整数 N を出力してください。
#整数 N が 200 の倍数であれば、N を 200 で割る。
#そうでなければ、整数 N を、N の後ろに文字列として 200 を付け加えた整数に置き換える。
#例えば、7 を置き換えると 7200 に、1234 を置き換えると 1234200 になります。
N,K =  map(int,input().split())
for i in range(K):
    if N%200 == 0:
        N = N//200
    else:
        N = N*1000+200
print(N)
#これは書けたと思う。
#ABCコンテスト200C問題
# 200 という整数が大好きなりんごさんのために、次の問題を解いてください。
# N 個の正整数からなる数列 A が与えられるので、以下の条件をすべて満たす整数の組 (i,j) の個数を求めてください。
# 1≤i<j≤N
# Ai−Ajは200の倍数である。
# 「Ai−Ajが 200 の倍数である」ということは、「Aiを 200 で割った余りと Ajを 200 で割った余りが一致する」と言い換えられます。
# なので、求めるものは、 Aiを 200 で割った余りと Ajを 200 で割った余りが一致するような (i,j) (1≤i<j≤N) の組の通り数(位置が異なる 2 つの要素の選び取り方の場合の数)と言い換えられます。
# まず、数列 Aiに 200 で割った余りが k であるような要素がいくつ含まれるかを求めます。今回の問題では愚直にループを回して数えてもよいですが、バケットソートの要領で調べると高速です。
# 数列 Aiに 200 で割った余りが k であるような要素が X 個含まれるとします。このとき、この中から数列 A での位置が異なる 2 つの要素を選び取る場合の数は、X×(X−1)/2通りです。この式は X=0,1 の場合でも適用できます。
# これを 0 以上 199 以下の全ての整数 k について足し合わせると、この問題を解くことができます。
# 最終的な計算量は O(N) です。
N = int(input())
A = list(map(int, input().split()))
B = [0]*200
ans = 0
for a in A:
    B[a%200] += 1
for b in B:
    if b!=0:
        ans += (b*(b-1))//2#切り捨て
    else:
        pass
print(ans)

#ABCコンテスト200D問題
# N 個の正整数からなる数列 A=(A1,A2,…,AN) が与えられます。 以下の条件を全て満たす 2 つの数列 B=(B1,B2,…,Bx), C=(C1,C2,…,Cy) が存在するか判定し、存在する場合はひとつ出力してください。
# 1≤ x,y≤N
# 1≤B1<B2<⋯<Bx≤N
# 1≤C1<C 2<⋯<Cy≤N
# B と C は、異なる数列である。
# x≠y のとき、または、ある整数 i (1≤ i≤ min(x,y)) が存在して Bi≠Ciであるとき、B と C は異なるものとする。
# AB1+AB2+⋯+ABxを 200 で割った余りと AC1+AC2+⋯+ACyを 200 で割った余りが等しい。
# 解説
# 実は、数列 B (または C )の候補を 201 通り探索すれば、その中で必ず条件を満たす数列の組を見つけることができます。
# X+1 羽の鳩を X 個の鳥かごに入れるとき、 2 羽以上の鳩が入った鳥かごが少なくとも 1 つ以上存在する
# これは、「鳩ノ巣原理」と呼ばれます。今回の問題では、
# 201 個の数列を、含まれる要素の総和を 200 で割った余りという 200 個のグループに分けるとき、 2 個以上の数列を含んだグループが少なくとも 1 つ以上存在する
# と言い換えられます。
# 数列の候補は全部で 2^N−1 通りあるので、 N≥8 のケースについては、必ず答えが存在することが分かります。
# では、どのようにして数列を 201 通り探索すればよいでしょうか。
# 例えば、数列のうち先頭の min(N,8) 要素を取り出して、その中で数列の候補をbit全探索するという方法があります。 N≤8 の場合は通常の全探索と変わらないので正しく動作します。N≥9 の場合でも、 8 要素の中での数列の候補は 255 通りあるので、答えを 1 組見つけるには十分です。
# このbit全探索は、定数時間で動作します。
#!/usr/bin/env python3
import sys
from bisect import bisect, bisect_left, bisect_right, insort, insort_left, insort_right  # type: ignore
from collections import Counter, defaultdict, deque  # type: ignore
from math import gcd  # type: ignore
from heapq import heapify, heappop, heappush, heappushpop, heapreplace, merge  # type: ignore
from itertools import accumulate, combinations, permutations, product  # type: ignore

def LI(): return list(map(int, sys.stdin.buffer.readline().split()))
def MI(): return map(int, sys.stdin.buffer.readline().split())
def I(): return int(sys.stdin.buffer.readline())
def LS(): return sys.stdin.buffer.readline().rstrip().decode("utf-8").split()
def S(): return sys.stdin.buffer.readline().rstrip().decode("utf-8")
def IR(n): return [I() for _ in range(n)]
def LIR(n): return [LI() for _ in range(n)]
def SR(n): return [S() for _ in range(n)]
def LSR(n): return [LS() for _ in range(n)]
def SRL(n): return [list(S()) for _ in range(n)]
def MSRL(n): return [[int(i) for i in list(S())] for _ in range(n)]

n = I()
a = LI()
d = {}
mod = 200
for i in range(1,min(2**n,202)):
    cand = []
    summod = 0
    for j in range(n):
        if i & (1<<j):
            cand.append(j+1)
            summod += a[j]
            summod %= mod
    if d.get(summod, False):
        print('Yes')
        print(len(cand),*cand)
        print(len(d[summod]),*d[summod])
        exit()
    else:
        d[summod] = cand
print('No')

#ABCコンテスト201B問題
# AtCoder国には N 個の山があり、i 個目の山の名前は Si, 高さは Tiです。
# 2番目に高い山の名前を答えてください。N 個の山の名前、高さはそれぞれ相異なることが保証されます。
#N 個の山を (高さ→名前) の順に優先度を付けて降順にソートした後、先頭から 2 番目の山の名前を出力すればいいです。
N = int(input())
m = []
for i in range(n):
    s_, t_ = input().split()
    m.append([int(t_),s_])
m.sort(reverse = True)#reverseキーワード引数はソートを昇順／降順に行うかどうかを指定するものだ。これをTrueに指定すると、ソートの結果は通常とは逆の順序（降順）になる。
print(m[1][1])

#ABCコンテスト201C問題
#高橋くんは、暗証番号を忘れてしまいました。暗証番号は 0 から 9 までの数字のみからなる 4 桁の文字列で、0 から始まる場合もあります。
# 0 から 9 までの各数字について、高橋くんは以下のように記憶しています。彼の記憶は長さ 10 の文字列 S0S1…S9によって表されます。
# Siが o のとき : 数字 i は暗証番号に確実に含まれていた。
# Siが x のとき : 数字 i は暗証番号に確実に含まれていなかった。
# Siが ? のとき : 数字 i が暗証番号に含まれているか分からない。
# 高橋くんが忘れてしまった暗証番号としてあり得るものは何通りありますか？
#回答
# 0000 から 9999 までの 10^4通りの暗証番号それぞれについて高橋くんの記憶に合致するかを判定し、合致するものの個数を数えることでこの問題を解くことができます。
# 実装の際は、0000 から 9999 までの暗証番号を「0 以上 9999 以下の整数に leading zero を付けたもの」と見做すことで簡潔なコードを書くことができます。例えば、1 に leading zero を付けて生成される暗証番号は 0001, 132 に leading zero を付けて生成される暗証番号は 0132 です。
s = input()
c_n = s.count('o')
t_n = s.count('?')
if c_n > 4:
    print(0)
    exit()
if c_n == 0 and t_n == 0:
    print(0)
    exit()

l_1 = []
l_2 = []
for i,a in enumerate(s):
    if a == 'o':
        l_1.append(i)
    elif a == '?':
        l_2.appedn(i)
result = 0
for n_1 in l_1 + l_2:
    for n_2 in l_1 + l_2:
        for n_3 in l_1 + l_2:
            for n_4 in l_1 + l_2:
                if set([n_1, n_2, n_3, n_4]) & set(l_1) == set(l_1):
                    result += 1
print(result)

#ABC202B問題
# 0、1、6、8、9 からなる文字列 S が与えられます。
# S を 180 度回転したものを出力してください。すなわち、S に次の操作を施してできる文字列を出力してください。
# S を反転する。
# 0 を 0 に、1 を 1 に、6 を 9 に、8 を 8 に、9 を 6 に変換する。
S = list(str(input()))
for i in range (len(S)):
    if S[i] == '6':
        S[i] = '9'
    elif S[i] == '9':
        S[i] = '6'
    else:
        pass
S=reversed(S)
print(''.join(S))

#ABC202C問題
# 1 以上 N 以下の整数からなる長さ N の数列 A=(A1,A2,…,AN),B=(B1,B2,…,BN),C=(C1,C2,…,CN) が与えられます。
# 1 以上 N 以下の整数 i,j の組 (i,j) であって、Ai=BCjとなるものの総数を求めてください。
#自分の回答
N = int(input())
A = [0] * N
B = [0] * N
C = [0] * N
for i in range(N):
    A[i], B[i], C[i] = map(int, input().split())
ans = 0
for i in range(N):
    for j in range(N):
        if A[i] == B[C[j]]:
            ans += 1
        else:
            pass
print(ans)
#解答
# iを固定したときに、Ai=BCjとなる j の個数が高速に求められればよいです。これを前もって計算しておく方法を考えます。
# Bkの値は 1 以上 N 以下であるので、長さ N 程度の配列 countxを用意し、j の値を全て試すことによって、各 1≤x≤N について BCj=x となる j の個数を countxとして保持しておくことが出来ます。
# 各 i について countAiを足し合わせたものが答えとなります。答えは最大で N^2になるため、32 bit 整数に収まらないことに注意してください。
# このように、「同じような処理を何度も行う」ような問題においては、「前もって計算しておく」という方法がうまくいくことがしばしばあります。
n = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
c = list(map(int,input().split()))
countb=[0]*n
ans = 0
for i in range(N):
    countb[b[c[i]-1]-1] += 1
for i in range(n):
    ans +=countb[a[i]-1]
print(ans)

#ABC203B問題
#AtCoder マンションは 1 階から N 階までの N 階建てのマンションです。 各階には K 室の部屋があり、1 号室から K 号室まで番号が振られています。
# ここで N,K は 1 桁の整数であり、 i 階の j 号室の部屋番号は i0j で表されます。 例えば、1 階の 2 号室の部屋番号は 102 です。
# マンションの管理人である高橋君は各部屋番号を 3 桁の整数とみなし、 AtCoder マンションに存在するすべての部屋について足しあわせたらいくつになるのか興味を持ちました。 その値を求めてください。
N,K = map(int,input().split())
ans = 0
for i in range(1,N+1):
    for j in range(1,K+1):
        ans += i*100+j
print(ans)
#ABC203C問題
# 10^100+1 個の村があり、それぞれ村 0, 村 1, …, 村 10^100と番号がついています。
# 0 以上 10^100−1 以下の全ての整数 i について、村 i で 1 円を払う事で村 (i+1) に移動することができます。 それ以外の移動方法はありません。
# 太郎君は初め K 円を持った状態で村 0 におり、その後、可能な限り大きな番号の村まで進もうとします。
# 太郎君には N 人の友達がいます。i 人目の友達は村 Aiにいて、太郎君が村 Aiに着いたときに Bi円を太郎君に渡します。
# 太郎君が最終的にたどり着く村の番号を求めてください。
#自分の回答
N,K = map(int, input().split())
A = [0]*N
B = [0]*N
for i in range(N):
    A[i],B[i] = map(int, input().split())

for i in range(1,N+1):
    if K+sum(B[:i]) < A[i]:
        print(K+sum(B[:i]))
    else:
        pass
#解答
def main():
    N, K = map(int, input().split())
    mat = []
    for _ in range(N):
        a, b = map(int, input().split())
        mat.append((a, b))
    mat.sort()  # aが小さい順にソートされます
    now = K  # はじめの所持金で村Kまで行けます
    for i in range(N):
        a, b = mat[i]
        if now >= a:
            # 村A_i の人が B_i円 くれるので、即座に消費してB_i進みます
            now += b
        else:
            # 村A_i にたどり着く前に所持金が尽きたので、ここでおしまいです
            break
    print(now)

if __name__ == '__main__':
    main()
    
#ABC204B
#N本の木があり、i番目の木には Ai個の木の実が実っています。
# シマリスは、次のルールで全ての木から木の実を収穫します。
# 実っている木の実が 10 個以下の木からは木の実を収穫しない
# 実っている木の実が 10 個より多い木からは、10 個を残して残りの全てを収穫する
# シマリスが収穫する木の実の個数の合計を求めてください。
N = int(input())
A = list(map(int,input().split()))
cnt = 0
for i in range(N):
    if A[i] <= 10:
        pass
    elif A[i] > 10:
        cnt += A[i] - 10
print(cnt)
#ABC204C
#AtCoder国には1からNの番号がついた N 個の都市と、1 から M の番号がついた M 個の道路があります。
# 道路 i を通ると都市 Aiから Biへ移動することができます。都市 Biから都市Aiへの通行はできません。
# ピューマは、どこかの都市からスタートし、0 本以上の道路を使い移動して、どこかの都市をゴールとするような旅行の計画を立てようとしています。
# スタート地点とゴール地点の都市の組として考えられるものは何通りありますか？
# 解説
# スタート地点を固定したときゴール地点にできる都市の個数を数えることを考えてみましょう。
# ゴール地点にできる都市は、スタート地点からいくつかの道路を使って到達できるような都市です。そのような都市は、DFSやBFSなどの探索アルゴリズムを用いて求めることができます。この際、既にチェックした頂点を2度以上調べないようにすることで、O(N+M) で求めることができます。
# どの都市をスタート地点とするかN通り全てを試すことで、全体で O(N(N+M))で問題が解けました。
#解答
# おまじない
import sys #この関数を使うことで好きな時に早期にプログラムを終了させることができます。
sys.setrecursionlimit(10000)#再起回数の設定

# 入力の読み込み
N,M=map(int,input().split())
G=[[] for i in range(N)]
# G[i] は都市iから道路で直接繋がっている都市のリスト
for i in range(M):
  A,B=map(int,input().split())
  G[A-1].append(B-1)

# dfs=深さ優先探索
def dfs(v):
  if temp[v]: return  
  temp[v]=True# 同じ頂点を2度以上調べないためのreturn
  for vv in G[v]: dfs(vv)

ans=0

# 都市iからスタートする場合
for i in range(N):
	temp=[False]*N
	# temp[j] は都市jに到達可能かどうかを表す
	dfs(i)
	ans+=sum(temp)

print(ans)

#DFSの典型問題
#スタートからゴールまで辿り着けるかを判定する問題です。
# スタートから辿り着ける場所を全て列挙して、その中にゴールがあるか確認すればいいので、深さ優先探索でスタートから探索してゴールに辿り着けるか判定します。
# 深さ優先探索は再起関数で簡単に書けます。
# Pythonでは再起呼び出しの上限があり、デフォルトでは1000になっています。AtCoderのテストケースでは足りないので、上限の設定をしておく必要があります。
#サンプルコード
import sys
sys.setrecursionlimit(10**7) # 再起回数の設定

H, W = map(int, input().split())
maze = [list(input()) for h in range(H)]

for h in range(H):
    for w in range(W):
        if maze[h][w] == "s":
            sx, sy = h, w

# 深さ優先探索
def dfs(x, y):
    # 範囲外や壁の場合は終了
    if y >= W or y < 0 or x >= H or x < 0 or maze[x][y] == '#':
        return

    # ゴールに辿り着ければ終了
    if maze[x][y] == 'g':
        print('Yes')
        exit()

    maze[x][y] = '#' # 確認したルートは壁にしておく

    # 上下左右への移動パターンで再起していく
    dfs(x+1, y)
    dfs(x-1, y)
    dfs(x, y+1)
    dfs(x, y-1)

dfs(sx, sy) # スタート位置から深さ優先探索
print('No')

#ABCコンテスト205B
# 1 以上 N 以下の整数からなる長さ N の数列 A=(A1,A2,…,AN) が与えられます。
# A が (1,2,…,N) の並び替えによって得られるかどうか判定してください。
N = int(input())
A = map(int,input().split())
A1 = set(A)
if len(A1) == N:
    print('Yes')
else:
    print('No')
#ABCコンテスト205C
# 数XをY回掛けたものを「XのY乗」といい、pow(X,Y)で表します。例えば pow(2,3)=2×2×2=8 です。
# 3つの整数 A,B,C が与えられるので、pow(A,C) と pow(B,C) の大小を比較してください。
A, B, C = map(int, input().split())
if C % 2:
  if A < B: print("<")
  elif A > B: print(">")
  else: print("=")
else:
  A, B = abs(A), abs(B)
  if A < B: print("<")
  elif A > B: print(">")
  else: print("=")

#ABCコンテスト206B
#シカのAtCoDeerくんは、空の貯金箱を持っています。
# AtCoDeerくんは、その貯金箱に、1 日目の朝に 1 円、2 日目の朝に 2 円 … というように、i 日目の朝に i 円を貯金箱に入れます。
# また、AtCoDeerくんは、毎日夜に貯金箱にいくら入っているかを確認します。
# AtCoDeerくんが貯金箱に N 円以上入っていることを初めて確認するのは、何日目の夜でしょうか?
N = int(input())
sum = 0
i = 0
while sum < N:
    i += 1
    sum += i
print(i)

#ABCコンテスト206C
# N 個の整数からなる配列 A=(A1,A2,...,AN) が与えられるので、次の条件を全て満たす整数組 (i,j) の数を求めてください。
# 1≤i<j≤N
# Ai≠Aj
#自分の解答
N = int(input())
A = list(map(int,input().split()))
cnt = 0
for i in range(N):
    for j in range(i+1,N):
        if A[i] != A[j]:
            cnt += 1
        else:
            pass
print(cnt)
#解説
# 今回の問題は、 ABC200-C の類題です。解けなかった方にとって、この問題が手掛かりになるかもしれません。
# Ai≠Ajとなるような整数組をどう数えればよいでしょうか？
# この問題では、 N≤3×10^5
# なので、愚直にループを回して数えていくようでは間に合いません。なので、効率的な解法を考える必要があります。
# 方針は色々と考えられますが、そのうちの 2 つを紹介します。
# 方針1
# 整数組 (i,j) (1≤i<j≤N) は N×(N−1)/2個存在しますが、それらから Ai=Ajとなるものを引き去ることを考えます。
# まず、数列をソートする。
# その後、整数が連続して何個存在するか数える。
# 例えば、ソート後の数列 A′=(2,2,3,4,4,4) なら、 2 が 2 つ、 3 が 1 つ、 4 が 3 つ存在します。
# 最後に、全ての数列 A′に含まれる整数 p について、 p が q 個含まれるなら、答えからq×(q−1)/2を減算する。 
# これは、 Ai=Aj=p となる整数組 (i,j) (i<j) の個数である。
# この式は、 q=0,1 の場合でも成立することに注意してください。
# 例えば、 A′=(2,2,3,4,4,4) なら、  6×5/2−2×1/2−3×2/2=11 となります。
from collections import Counter #collections.Counterは標準モジュールの一つで、リストの各要素の数え上げが出来ます。また、返り値であるCounterクラスは辞書型のサブクラスということで、辞書型と同じ操作ができます。
N = int(input())
cnt = Counter(map(int, input().split()))
# 辞書型（dictionary）をリスト型で取得する 
#for キーの変数,値の変数 in 辞書型.items():
    #処理
ans = N * (N - 1) // 2
for a, c in cnt.items():
    ans -= c * (c - 1) // 2
print(ans)

#ABC207B
# 水色のボールがA個容器に入っています。高橋くんはこの容器に対し、以下の操作を 0 回以上好きなだけ繰り返します。
# 水色のボール B 個と赤色のボール C 個を容器に追加する。
# 高橋くんの目標は、容器に入っている水色のボールの個数が赤色のボールの個数の D 倍以下になるようにすることです。
# 目標が達成可能かを判定し、可能なら必要な操作回数の最小値を求めてください。
#自分の解答
a,b,c,d = map(int,input().split())
x = 0
sum1 = a+b*x
sum2 = c*x*d
if b >= c:
    print(-1)
elif b < c:
    while sum1 > sum2:
        x += 1
print(x)
#解答
A,B,C,D = map(int,input().split())
ans = -1
diff = C*D-B
if 0 < diff:
    ans = (A+diff-1)//diff
print(ans)
#ABC207C
# 1 から N までの番号が付いた N 個の区間が与えられます。
# 区間 i は、ti=1 なら [li,ri](以上以下)
# ti=2 なら [li,ri)(以上未満)
# ti=3 なら (li,ri](より大きく、以下)
# ti=4 なら (li,ri)です。(より大きく、未満)
# 1≤i<j≤N を満たす整数の組 (i,j) のうち、区間 i と区間 j が共通部分を持つようなものは幾つありますか？
#解説
# 制約が N≤2000 と小さいので、O(N^2) 回のループによって 1≤i<j≤N を満たす整数の組 (i,j) を列挙し、それぞれについて O(1) で区間 i, j が共通部分を持つかを判定すればよいです。以降、O(1) で区間が共通部分を持つかを判定する方法のみについて解説します。
# 各区間を閉区間に直すことを考えましょう。
# 区間の両端点が整数であるという制約から、
# [li,ri] を [li,ri]
# [li,ri) を [li,ri−0.5]
# (li,ri] を [li+0.5,ri]
# (li,ri) を [li+0.5,ri−0.5]
# に置き換えても答えは変わりません。
# このような区間の置き換えをすることで共通部分を持つかの判定を高々 1 通りの場合分けで済ませることができ、実装が非常に軽くなります。
# なお、2 つの閉区間 [a,b],[c,d] が共通部分を持つかの判定は max(a,c)≤min(b,d) と書くことができます。
N = int(input())
l = [0]*N
r = [0]*N
for i in range(N):
    t,l[i],r[i] = map(int,input().split())
    if t == 2:
        r[i] -= 0.5
    elif t == 3:
        l[i] += 0.5
    elif t == 4:
        l[i] += 0.5
        r[i] -= 0.5
ans = 0
for i in range(N):
    for j in range(i+1,N):
        ans += (max(l[i],l[j]) <= min(r[i],r[j]))
print(ans)
#ABC208B
# 高橋王国では 1! 円硬貨 ,2! 円硬貨 ,…,10! 円硬貨が流通しています。ここで、N!=1×2×⋯×N です。
# 高橋君は全ての種類の硬貨を 100 枚ずつ持っており、P 円の商品をお釣りが出ないようにちょうどの金額を支払って買おうとしています。
# 問題の制約下で条件を満たす支払い方は必ず存在することが証明できます。
# 最小で何枚の硬貨を使えば支払うことができますか？
#価値の高い貨幣から決める
#貪欲法を用いる
from math import factorial
P = int(input())
answer = 0
for i in range(10, 0, -1):
  while factorial(i) <= P:
    answer += 1
    P -= factorial(i)
print(answer)
#ABC208C
# 高橋王国には N 人の国民がいます。 全ての国民には国民番号が割り振られており、 i 人目の国民の国民番号は aiです。
# ここで、aiは互いに異なります。
# 高橋君は K 個のお菓子を持っています。高橋君は次のルールに従って、持っているお菓子が無くなるまで国民にお菓子を配ることにしました。
# 持っているお菓子が N 個以上ある場合、全員に 1 個ずつお菓子を配る。
# そうでない場合、その時点で高橋くんが持っているお菓子の個数を K'として、国民番号が小さい方から K′人に 1 個ずつ配る。
# より厳密には、aiの値が小さい方から K′人を選び、選んだ人に 1 個ずつお菓子を配る。
# 全てのお菓子を配り終えたとき、i 人目の国民は何個のお菓子を持っていますか？
# 問題で与えられた操作を愚直に行うと、最大で K=10^18
# 回の操作が必要になりTLEしてしまうので、適切な考察により計算量を改善する必要があります。
# 全員に配る回数は全部で何回になるかを考えると、K×t が N を超えないような最大の t が答えになります。この t は
# K×t≤N⟺t<=N/K
# より、N を K で切り捨て除算した値 ⌊N/K⌋ になります。
# 以上より全員に配る部分は高速に操作することが出来ました。残りのお菓子の個数は K′=N−K×⌊N/K⌋ 個で、
# この K′個を番号の小さい K′人に配ればこの問題を解くことが出来ます。
# 実装方法はいくつかありますが、ここでは他の問題でも使える O(NlogN) のアルゴリズムを説明します。
# 新たに配列 order を宣言して、 1,2,…,N を追加する。
# i<j ならば a[i]<a[j] になるように比較関数を定義して、配列 order をソートする。
# 配列 order の先頭 K′項の添え字に対応する要素が求める要素である。
# 以上のアルゴリズムにより、 aiの小さい K′人が誰かを高速に求めることが出来ました。
# 定数倍の良い実装
N, K = map(int,input().split())
a = list(map(int,input().split()))
order = [(a[i] << 32) + i for i in range(N)]
order.sort()

answer = [K // N for i in range(N)]#これはできた
for i in range(K % N):
  answer[order[i] & ((1 << 32) - 1)] += 1#32ってなに、、、？
for x in answer:
  print(x)

#ABC209B
# 高橋商店では N 個の商品が売られています。i(1≤i≤N) 番目の商品の定価は Ai円です。
# 今日はセールが行われており、偶数番目の商品は定価の 1 円引きの値段で買うことができます。奇数番目の商品は定価で売られています。
# あなたの所持金は X 円です。これら N 個の商品を全て買うことができますか？
N,X = map(int, input().split())
A = list(map(int,input().split()))
for i in range(N):
    if i%2 == 1:
        A[i] -= 1
if X >= sum(A):
    print('Yes')
else:
    print('No')
#ABC209C
# 長さ N の整数列 C が与えられます。以下の条件を全て満たす長さ N の整数列 A の個数を求めてください。
# 1≤Ai≤Ci(1≤i≤N)
# Ai≠Aj(1≤i<j≤N)
# ただし、答えは非常に大きくなる可能性があるので、(10^9+7) で割った余りを出力してください。
N = int(input())
C = list(map(int, input().split()))
#解説
# 解けない問題にあたった時、具体例を考えてみるという戦略はどの問題においても有用です。
# 本解説では具体例として、C=(100,100,100) の場合を考えてみます。
# まず、A1の値としてありうるのは 1,2,…,100 の 100 通りです。
# 次に、A2の値としてありうるのは 1,2,…,100 から A1としてすでに用いた 1 つを取り除いた 99 通りです。
# 最後に、A3の値としてありうるのは 1,2,…,100 から A1,A2としてすでに用いた 2 つを取り除いた 98 通りです。
# よって A としてありうるのは 100×99×98 通りと求められます。
# 同じように考えると C が昇順に並んでいるとき、条件を満たす A の個数は (Ci−i+1) を掛け合わせた値であることが分かります。
# 証明としては、A1,A2,… の順に値を決めていったときに、Aiの値の候補が 1,2,…Ciから A1,A2,…Ai−1(これらは相異なり、全て 1 以上 Ci以下) を除いた
# 計 Ci−i+1 個であるからです。ただし、Ci−i+1<0 となる i が一つでも存在すれば答えは 0 です。
# なお、入力で与えられる C は昇順に並んでいるとは限らないので昇順に並び替える必要があります。
# 32-bit 型を用いると計算途中でオーバーフローしてしまう可能性があることに注意してください。
N = int(input())
C = list(map(int, input().split()))
C.sort()
ans=1
for i in range(N):
    ans = ans * max(0, C[i] - i) % 1000000007
print(ans)

#ABC210B
# N枚のカードからなる山札があります。
# それぞれのカードは、「良いカード」か「悪いカード」かのどちらかです。
# 高橋君と青木君は、この山札を使って対戦ゲームをします。
# このゲームでは、2 人は交互に山札の一番上のカードを引いて、そのカードを食べます。
# 先に悪いカードを食べたプレイヤーの負けです。（ここで、山札には少なくとも 1 枚の悪いカードが含まれていることが保証されます。）
# 0と1からなる文字列 S が与えられます。i=1,2,…,N について、
# Sのi 文字目が 0 のとき、山札の上から i 番目のカードが良いカードであることを表します。
# Sのi 文字目が 1 のとき、山札の上から i 番目のカードが悪いカードであることを表します。
# 高橋君が先手でゲームを始めるとき、高橋君と青木君のどちらが負けるかを答えてください。
N = int(input())
S = list(map(str,input().split()))
for i in range(N):
    if S[i] == '0':
        i += 1
    else:
        if i%2 == 0:
            print('Takahashi')
        elif i%2 == 1:
            print('Aoki')
        break
n=int(input())
s=input()
x=s.index('1')
print('Takahashi' if x%2==0 else 'Aoki')

#ABC210C
# N 個のキャンディが左右一列に並んでいます。
# それぞれのキャンディは、色 1、色 2、…、色 10^9の、10^9種類の色のうちいずれかの色をしています。
# i=1,2,…,N について、左から i 番目のキャンディの色は色 ciです。
# 高橋君は並んでいるキャンディのうち、連続して並んだ K 個のキャンディをもらうことができます。
# すなわち、1≤i≤N−K+1 を満たす整数 i を選んで、 左から i 番目、i+1 番目、i+2 番目、…、i+K−1 番目のキャンディをもらうことができます。
# 高橋君はいろいろな色のキャンディを食べたいので、 もらうキャンディに含まれる色の種類数が多いほどうれしい気持ちになります。
# 高橋君がもらうキャンディに含まれる色の種類数の最大値を出力してください。
N,K = map(int, input().split())
c = list(map(int, input().split))
c1 = set(c)
if K > len(c1):
    print(len(c1))
else:
#解説
#i 番目、i+1 番目、i+2 番目、…、i+K−1 番目のキャンディをまとめて、区間 [i,i+K−1] で表すことにします。
# 高橋君がとる区間の候補は、 [1,K],[2,K+1],[3,K+2],…,[N−K+1,N] の N+K−1 個があります。
# これらすべてについて「区間に含まれるキャンディの色の種類数」を求め、それらの最大値を答えとして出力すれば良いです。
# そこで、上記の方法を高速化します。
# いま、[i,i+K−1] を調べてその直後に [i+1,i+K] を調べたいとします。 ここで、[i,i+K−1] から i+K 番目のキャンディを追加して代わりに i 番目のキャンディを削除すると、[i+1,i+K] になることに注意します。 つまり、[i,i+K−1] と [i+1,i+K] には「わずかな差」しかありません。 そこで [i+1,i+K] について調べるときは [i+1,i+K] のキャンディをすべて見るのではなく、 直前に調べた [i,i+K−1] との「差分」のみに着目することで、高速化を図ることができます。
# この考え方に基づいて、以下のアルゴリズムを考えます。
# まず c1,c2,…,cKを見て、 [1,K] 内にキャンディが 1 個以上存在する各色についてキャンディの個数を連想配列（C++言語ではstd::mapなど）で記録します。このとき、連想配列のエントリ数は [1,K] 内の色の種類数に等しいことに注意します。
# 次に、連想配列内の色 cK+1の個数を 1 増やし、色 c1の個数を 1 減らす操作を行います（その結果、色 c1の個数が 0 個になったら連想配列から色 c1のエントリを削除します。）すると、連想配列のエントリ数は [2,K+1] 内の色の種類数に等しくなります。
# さらに、連想配列に対して、色 cK+2の個数を 1 増やし、色 c2の個数を 1 減らす操作を行います。（その結果、色 c2の個数が 0 個になったら連想配列から色 c2のエントリを削除します。）すると、連想配列のエントリ数は [3,K+2] 内の色の種類数に等しくなります。
# これを繰り返すことで、[1,K],[2,K+1],[3,K+2],…,[N−K+1,N] のそれぞれについて、区間内の色の種類数を連想配列のエントリ数として求めることができるので、それらの最大値を答えとして出力すれば良いです。
# 各キャンディについて、連想配列への追加と削除はそれぞれ高々 1 回ずつしか行われないので、このアルゴリズムの時間計算量は O(NlogN) であり、この問題に正解するためには十分高速です。

from collections import defaultdict
n, k = map(int, input().split())
c = list(map(int, input().split()))

mp = defaultdict(int)
ans = 00
for i in range(n - k + 1):
	if i == 0:
		for i in range(k):
			mp[c[i]] += 1
	else:
		mp[c[i + k - 1]] += 1
		mp[c[i - 1]] -= 1
		if mp[c[i - 1]] == 0:
			del mp[c[i - 1]]
	ans = max(ans, len(mp))
#	print(mp)
print(ans)

#211B
# 4 つの文字列 S1,S2,S3,S4が与えられます。
# この中に、H , 2B , 3B , HR がそれぞれ 1 つずつあるか判定してください。
# ただし、全ての Siは H , 2B , 3B , HR のいずれかと一致します。
#解答１
S = set()
for _ in range(4):
    S.add(input())
print('Yes' if len(S) == 4 else 'No')
#解答2
S1 = input()
S2 = input()
S3 = input()
S4 = input()
S = [S1,S2,S3,S4]
print("Yes" if len(set(S)) == 4 else "No")
#211C
# 文字列 S が与えられます。
# このうち 8 文字を選び下線を引き、下線を引いた文字が左から順に c , h , o , k , u , d , a , i となるようにする方法は何通りありますか？
# ただし答えは非常に大きくなる可能性があるので、(10^9+7) で割った余りを出力してください。
# 動的計画法(DP)を用います。
# dp[i][j] を、「 S の i 文字目までを使って、chokudai の j 文字目まで選択する方法」と定義します。
# ここで、N=∣S∣ , T=chokudai として、以下の漸化式が成り立ちます。
# dp[i][j]= 
# ①1(j=0)
# ②0(i=0,1≤j≤8)
# ③dp[i−1][j](1≤i≤N,1≤j≤8,S[i]≠T[j])
# ④dp[i−1][j]+dp[i−1][j−1](1≤i≤N,1≤j≤8,S[i]=T[j])
MOD = 10**9 + 7
S = input()
T = "chokudai"
dp = [[0]*9 for _ in range(len(S)+1)]
dp[0][0] = 1
for i in range(1, len(S)+1):
  dp[i][0] = 1
  for j in range(1, 8+1):
    if S[i-1] == T[j-1]:
      dp[i][j] = (dp[i-1][j] + dp[i-1][j-1]) % MOD
    else:
      dp[i][j] = dp[i-1][j]
      
print(dp[len(S)][8])

#213B
#1,…,Nの番号のついたN人の選手がゲームを行いました。選手iのスコアは Aiであり、スコアが小さい方が上位になります。
#ブービー賞に該当する選手、すなわち、下位から 2 番目の選手の番号を求めてください。
N = int(input())
A = list(map(int,input().split()))
A1 = sorted(A)
for i in range(N):
    if A[i] == A1[-2]:
        print(i+1)
#213C
#H 行 W 列の格子状に HW 枚のカードが並べられています。
# i=1,…,N について、上から Ai行目、左から Bi列目にあるカードには数 i が書かれており、それ以外の HW−N 枚のカードには何も書かれていません。
# これらのカードに対し、以下の 2 種類の操作を可能な限り繰り返します。
# 数の書かれたカードを含まない行が存在するとき、その行のカードを全て取り除き、残りのカードを上へ詰める
# 数の書かれたカードを含まない列が存在するとき、その列のカードを全て取り除き、残りのカードを左へ詰める
# 操作が終了したとき、数が書かれたカードがそれぞれどこにあるか求めてください。なお、答えは操作の仕方に依らず一意に定まることが証明されます。
#解説
# 行に関する操作と列に関する操作は互いに干渉しません。そのため行と列について独立に考えることができます。以下では上から何行目かについて考えますが、左から何列目かも同様に求めることができます。
# まず、操作によってカード同士の位置関係(どちらがより上にあるか、など)が変わることはありません。また、操作終了後には全ての行・列が数の書かれたカードを含みます。
# このことから、操作終了後には、もともと最も上にあった数の書かれたカードが1行目に、2番目に上にあった数の書かれたカードが2行目に、……となることがわかります。
# したがって元の問題は「Aiたちを、大小関係を保ったまま、値を小さくせよ」と読み替えることができました。 例えば A=(2,9,9,7,9,2,4) であれば (1,4,4,3,4,1,2) に変換せよ、という意味です。
# これは「座標圧縮」と呼ばれる操作にほかなりません。したがって O(NlogN) で問題が解けました。具体的な実装方法については各自で調べてください。
H,W,N=map(int,input().split())
X,Y=[],[]
for i in range(N):
  x,y=map(int,input().split())
  X.append(x)
  Y.append(y)

Xdict = {x:i+1 for i,x in enumerate(sorted(list(set(X))))}
Ydict = {y:i+1 for i,y in enumerate(sorted(list(set(Y))))}

for i in range(N):
  print(Xdict[X[i]], Ydict[Y[i]])


#214B
#a+b+c≤S かつ a×b×c≤T を満たす非負整数の組 (a,b,c) はいくつありますか？
s,t = map(int, input().split())
ans = 0
for a in range(s+1):
    for b in range(s+1-a):
        for c in range(s+1-a-b):
            if a*b*c <= t:
                ans += 1
print(ans)

#214C
# N 人のすぬけ君が円周上に並んでおり、反時計回りに 1,2,...,N の番号がついています。
# i(1≤i≤N) 番目のすぬけ君は時刻 t に宝石をもらうと Si単位時間後、すなわち時刻 t+Siにその宝石を (i+1) 番目のすぬけ君に渡します。ただし、(N+1) 番目のすぬけ君とは 1 番目のすぬけ君のことを指すとします。
# また、高橋君は時刻 Tiにi番目のすぬけ君に宝石を渡します。
# 全ての i(1≤i≤N) について、i 番目のすぬけ君が初めて宝石をもらう時刻を求めてください。なお、宝石の受け渡しにかかる時間は無視できるものとします。
# 解説
# まず、memo1=T1,memoi+1=memoi+Siという漸化式で定められる 
# memoiが、高橋君が 1 番目のすぬけ君に直接渡した宝石が i 番目のすぬけ君に初めて届く時刻です。
# 2,3,…,N 番目のすぬけ君に直接渡した宝石が i 番目のすぬけ君にいつ届くかについても同じように考えます。
# これを愚直に実装することで O(N^2) で解けますが、実行時間に間に合わないため高速化を考えます。
# ここですぬけ君が受け取る宝石の中で 2 番目以降の宝石は無視できることに注目して今までの N 個の計算を一つにまとめると、以下のようなコードになります。
# 少なくとも 2N 回ループを回さないといけないことに注意してください。
N = int(input())
S = list(map(int,input().split()))
T = list(map(int,input().split()))
for i in range(N*2):
    T[(i+1)%N] = min(T[(i+1)%N], T[i%N] + S[i%N])
for ans in T:
  print(ans)

#ABC250A
#縦 H 行、横 W 列のマス目があり、このうち上から i 個目、左から j 個目のマスを (i,j) と呼びます。
#このとき、マス (R,C) に辺で隣接するマスの個数を求めてください。
#ただし、ある 2 つのマス (a,b),(c,d) が辺で隣接するとは、 ∣a−c∣+∣b−d∣=1 (∣x∣ を x の絶対値とする) であることを言います。
#解説
#ぱっと思いつきそうな解法として、場合分けに頼った解法が挙げられますが、非常に間違いが発生しやすいため危険です。そこで、この解説ではなるべく簡単に解く方針を紹介します。
#全体の方針としては、
#マス (R,C) の左側にマスがある
#マス (R,C) の右側にマスがある
#マス (R,C) の上側にマスがある
#マス (R,C) の下側にマスがある
#のうち、真であるようなものの数を数えます。
#まず、マス (R,C) の左側にマスが存在する条件を考えます。
#「マス (R,C) の左側にマスが存在する」ことは「 C≠1 」と同値です。
#次に、マス (R,C) の右側にマスが存在する条件を考えます。
#「マス (R,C) の右側にマスが存在する」ことは「 C≠W 」と同値です。
#上下方向も同様にして判定することができます。
#include<bits/stdc++.h>
h,w = map(int,input().split())
r,c = map(int,input().split())
ans = 0
if c!=1:
	ans += 1
if c!=w:
	ans += 1
if r!=1:
	ans += 1
if r!=h:
	ans += 1
print(ans)

#ABC251A
S = input()
if len(S) == 1:
    print(S*6)
elif len(S) == 2:
    print(S*3)
elif len(S) == 3:
    print(S*2)
#ABC251B
N,W = map(int,input().split())
A = list(map(int,input().split()))
A.sort(N)
S = list()
ans = 0
for i in range(N):
    if A[i] <= W:
        ans += 1
        S.append(A[i])
    else:
        continue
for i in range(N):
    for j in range(i+1,N):
        if A[i]+A[j] <= W and (A[i]+A[j] not in S):
            ans += 1
            S.append(A[i]+A[j])
        else:
            continue
for i in range(N):
    for j in range(i+1,N):
        for k in range(j+1,N):
            if A[i]+A[j]+A[k]<= W and (A[i]+A[j]+A[k] not in S):
                ans += 1
                S.append(A[i]+A[j]+A[k])
            else:
                continue
print(ans)
#ABC251B
#おもり 1, おもり 2, …, おもり N の N 個のおもりがあります。おもり i の重さは Aiです。
#以下の条件を満たす正整数 n を 良い整数 と呼びます。
#3 個以下 の異なるおもりを自由に選んで、選んだおもりの重さの和を n にすることができる。
#W 以下の正整数のうち、良い整数は何個ありますか？
#解説
#まず、この問題文をプログラミング的な手続きに言い換えると次のような問題になります。この手順を十分高速に計算できればこの問題を解くことができます。
#1 以上 W 以下のすべての整数について「n はよい整数か」を管理するフラグ用の配列 flag を用意する。flag ははじめ false で初期化されている。
#3 個以下であるおもりの集合全てを調べる。各集合についておもりの重さの和 w を求める。そして、w が W 以下ならば flag[w] を true にする。
#最終的に true であるフラグの個数が答えとなる。
#上の手順の中で一番難しいのが「 3 個以下であるおもりの集合全てを調べる」という部分で、ここで探索の方法を間違えると計算量が膨大になって TLE しています。
#この部分は「3 個以下である」を「1 個 または 2 個または 3 個である」と言い換えるのがポイントです。「おもりの個数がちょうど x 個である集合」の場合は 以下のような for-loop を用いた実装で O(N 
#x) で計算することができるので、このように言い換えたあと 1 個の場合, 2 個の場合, 3 個の場合を別々に計算すれば、この問題は for-loop で実装できる問題に帰着します。
n,w = map(int,input().split())
a = list(map(int,input().split()))
size = len(a)
good = [0]*(w+1)
for i in range(size):
	if a[i] <= w:
		good[a[i]]=1
 for i in range(size - 1):
	for j in range(i+1,size):
		total = a[i] + a[j]
		if total <= w:
			good[total] =1
for j in range(size - 2):
	for j in range(i+1,size-1):
		for k in range(j+1,size):
			total = a[i]+a[j]+a[k]
			if total <= w:
				good[total] = 1
print(sum(good))
#ABC251C
#ポエムオンラインジャッジ (Poem Online Judge, 以下 POJ と表記) は提出された文字列に得点をつけるオンラインジャッジです。
#POJ に N 回の提出がありました。早い方から i 番目の提出では文字列 Siが提出されて、得点は Tiでした。(同じ文字列が複数回提出される場合もあります)
#ただし、POJ では 同じ文字列を提出しても得点が等しいとは限らない のに注意してください。
#N 回の提出のうち、その提出よりも早い提出であって文字列が一致するものが存在しないような提出を オリジナル であると呼びます。
#また、オリジナルな提出の中で最も得点が高いものを 最優秀賞 と呼びます。ただし、そのような提出が複数ある場合は、最も提出が早いものを最優秀賞とします。
#最優秀賞は早い方から何番目の提出ですか？
#解説
#この問題はいくつかの解法が考えられると思いますが、例えば for-loop を用いて前から調べていく方法を使って解けないか考えてみましょう。すると、一例として次のような手順が考えられます。
#暫定的に優秀な提出 best、およびその得点 best_score を変数として用意する。
#1 番目の提出から昇順に調べていく。i 番目の提出を調べるときは、まずその提出がオリジナルかを判定する。
#もしオリジナルであれば、得点 T_i が best_score より大きいかを判定する。
#大きければ best を i に、best_score を T_i に更新する。
#そうでなければ何もしない。
#もしオリジナルでなければ何もしない。
#これを 2 重の for-loop を用いて Python でナイーブに実装すると以下のようになります。
#しかしこのままでは提出 i がオリジナルか判定する部分に O(N) かかっており、全体で O(N^2)時間かかりTLE してしまいます。

#TLEする解法
N = int(input())
S,T = [],[]
for i in range(N):
	s,t = input().split()
	S.append(s)
	T.append(int(t))
best = -1
best_score = -1

for i in range(N):
	original = True
	for j in range(i):
		if S[i] == S[j]:
			original = False
	if original = False:
		continue
	if best_score < T[i]:
		best = i
		best_score = T[i]
print(best+1)
#そこで、今まで出てきた文字列を Python の set や C++ の std::set のような集合型や連想配列(辞書)を用いて管理しましょう。
#集合型は次の操作を O(1) あるいは O(log(集合の要素数)) で行うことができるデータ構造です。
#ある文字列が集合に含まれているか判定する
#集合を文字列に追加する
#このようなデータ構造を用いることで、ボトルネックの部分であった「文字列が前に登場したか判定する」部分を高速に行うことができるのでACすることができます。
N = int(input())
S,T = [],[]
for i in range(N):
	s,t = input().split()
	S.append(s)
	T.append(int(t))

best = -1
best_score = -1

appeared = set()
for i in range(N):
	if S[i] in appeared:
		continue
	appeared.add(S[i])
	if best_score < T[i]:
		best = i
		best_score = T[i]
print(best+1)

#ABC216B
#N 人の人がいます。i(1≤i≤N) 人目の人の姓は Si、名は Tiです。
#同姓同名であるような人の組が存在するか、すなわち 1≤i<j≤N かつ Si=Sjかつ Ti=Tjを満たすような整数対 (i,j) が存在するか判定してください。
#制約
#2≤N≤1000
#N は整数
# Si,Tiは英小文字のみからなる長さ 1 以上 10 以下の文字列
N = int(input())
S,T = [],[]
for i in range(N):
    s,t = input().split()
    S.append(s)
    T.append(t)

for i in range(N):
    for j in range(i+1,N):
        if (S[i] == S[j]) and (T[i] == T[j]):
            print('Yes')
            exit()
print('No')

##全探索：O(2^N)/O(N^2)
#全探索とは、あり得るすべてのパターンをしらみつぶしに調べる方法
##二分探索:O(logN)
##組み合わせの全探索:O(2^N)
##素数判定法：O(√N)

#高速な素数判定法
#実は2からN-1まで全部を調べる必要はなく、√N以下まで調べて割り切れなければ素数だと言い切って良い→このアルゴリズムの計算量はO(√N)
def isprime(N):
    LIMIT = int(N**0.5)
    for i in range(2,LIMIT+1):
        if N%i == 0:
            return False
    return True

N = int(input())
if isprime(N):
    print("prime")
else:
    print("not prime")

##約数列挙:
#約数列挙
#素数判定法と似たような次の手順でNの約数を列挙出来る
#1:i=1,2,3,・・・√N
#2:割り切れる場合、iとN/iを約数に追加する
N=int(input())
#すべての約数を求め、配列divisorsに入れる
LIMIT=int(N**0.5)
divisors=[]
for i in range(1,LIMIT+1):
    if N%i == 0:
        divisors.append(i)
        if i != N//i:
            divisors.append(N//i)
#小さい順に並べ替え→出力
divisors.sort()
for i in divisors:
    print(i)

##ユークリッドの互助法:O(logN)
#ユークリッド互除法
#自然数AとBの最大公約数を求める
#1:大きい方の数を「大きいほうを小さい方で割った余り」に書き換えるという操作を繰り返す
#2:片方が0になったら操作を終了する。もう片方の数が最大公約数
def GCD(A,B):
    while A>=1 and B>=1:
        if A<B:
            B=B%A
        else:
            A=A%B
    if A>=1:
        return A
    return B

A,B =map(int,input().split())
print(GCD(A,B))

#場合の数とアルゴリズム
n個のモノからr個を並べる方法：nPr=n×(n-1)×(n-2)×・・・×(n-r+1)
n個のモノからr個を選ぶ方法:n!/r!(n-r)!

N枚のカードがあり、左からi番目のカードには整数Aiが書かれている。カードを5枚選ぶ方法のうち、選んだカードに書かれた整数の和がちょうど1000となるものは何とおり？
# 注意
# Python で提出すると、N = 100 では実行に 10 秒程度かかり、TLE（実行時間制限オーバー）になります。
# 一方、同じプログラムを PyPy3 で提出すると、実行に 0.5 秒程度しかかからず、AC（正解）することができます。
100C5=約75300000 <=10^9をはるかに下回る
N=int(input())
A=list(map(int, input().split()))
answer = 0
for i in range(0, N):
	for j in range(i + 1, N):
		for k in range(j + 1, N):
			for l in range(k + 1, N):
				for m in range(l + 1, N):
					if A[i] + A[j] + A[k] + A[l] + A[m] == 1000:
						answer += 1

# 出力
print(answer)

##確率・期待値とアルゴリズム
#期待値=1回の試行で得られる平均的な値のこと
#期待値の線形性
N=int(input())
B=list(map(int,input().split()))
R=list(map(int,input().split()))
#出目の和の期待値=青の出目の期待値+赤の出目の期待値
for i in range(N):
    b=0
    b += B[i]
for i in range(N):
    r=0
    r += R[i]
x = (b+r)/N
print(N)

#選択式の試験でランダムに答える
#問題
#ある国語のテストの問題はN問からなり、すべて選択式。i問目はPi個の選択肢から1つの正解を選ぶ形式で、配点はQi
N = int(input())
P = list(map(int,input().split()))
Q = list(map(int,input().split()))
for i in range(N):
    ans = 0
    ans += Q[i]/P[i]
print(ans)


##モンテカルロ法
#モンテカルロ法:n回のランダムな試行のうち、m回成功した場合、理論上成功率がm/nであるとみなして近似する→n数が大きくなるほど、精度は良くなる。
#円周率πの計算
import random
N = 10000 #Nは試行回数(適宜変更する)
M = 0
for i in range(N):
    px = random.random() #0以上1未満の乱数を生成
    py = random.random() #0以上1未満の乱数を生成

    if px * px + py*py <= 1.0: #原点からの距離が1以下なので
        M += 1
print(M/N)

#平均値
μ=x1+x2+x3+・・・+xn/N
#標準偏差
σ=√(x1-μ)^2+(x2-μ)^2+・・・+(xn-μ)^2/N

#モンテカルロ法の理論的検証
nが十分大きい値である場合、確率pで成功する試行をn回行った時、n回のうち成功したものの割合は平均μ=p、標準偏差σ=√p(1-p)/n
μ=0.5、σ=0.05
μ±σ：68%
μ±2σ：95%
μ±3σ：99.7%

##選択ソート:O(N^2)
#小さい順に整列するプログラム
# 入力（たとえば N = 5, A = [3, 1, 4, 1, 5] を入力したとする）
N = int(input())
A = list(map(int, input().split()))

# 配列 A 全体をソートする
A.sort()

# 出力（1, 1, 3, 4, 5 の順に出力される）
for i in range(N):
	print(A[i])

#選択ソート:まだ調べていない中で最も小さい数を探すことを繰り返して、配列をソートする手法
#次の操作をN-1回繰り返す。i回目の操作では、以下のことを行う。
#1.未ソート部分(AiからANまで)の中で最小の要素Aminを探す
#AiとAminを変換する
#この時、操作後のA1,A2,・・・ANは小さい順に整列されている。
N=int(input())
A=list(map(int,input().split()))
for i in range(N-1):
    min_position = i
    min_value = A[i]
    for j in range(i+1,N):
        if A[j] < min_value: 
            min_position=j
            min_value=A[j]
    #A[i]とA[min_position]を変換
    A[i],A[min_position]=A[min_position],A[i]
#出力
for j in range(N):
    print(A[i])

##再帰関数
#5の階乗の計算
#Nが1の場合：1を返す
#Nが2以上の場合：(操作N-1の計算結果)×N を返す
def func(N):
    if N == 1:
        return 1
    return func(N-1)*N
N = int(input())
print(func(N))
#解説
# Python では、呼び出せる再帰関数の深さに上限が設定されており、デフォルトでは 1000 などの深さに設定されています。
# この上限は、sys.getrecursionlimit() を呼び出すことで取得できます。
# 一方、sys.setrecursionlimit(depth) を呼び出すことで、再帰呼び出しの深さ depth の上限を変えることができます。
# （これらの機能を使うためには、最初に import sys と書く必要があります）

#再帰関数の例②：ユークリッドの互除法
def GCD(A,B):
    if B == 0:
        return A #ベースケース
    return GCD(B,A%B)

A,B = map(int,input().split())
print(GCD(A,B))

##分割統治法
#再帰関数の例③:分割統治法で合計値を求める
#分割統治法とは:問題を複数の部分問題に分割し、それぞれの部分問題を再帰的にとき、その計算結果を統治することで問題を解くアルゴリズムを分割統治法という。
def solve(l,r,A):
    if r-l == 1:
        return A[l]
    m = (l+r)//2 #区間[l,r)の中央で分割する
    s1 = solve(l,m,A) #s1はA[l]+・・・+A[m-1]の合計値となる
    s2 = solve(m,r,A) #s1はA[m]+・・・+A[r-1]の合計値となる
    return s1+s2

#入力
N = int(input())
A = list(map(int,input().split()))

#再帰呼び起こし→答えの出力
answer=solve(0,N,A)
print(answer)


##マージソート:O(NlogN)
#マージ操作
#マージソート
#merge操作
#長さaの列Aと長さbの列bが与えられる。ここで、列A・Bはすでにソートされている。2つの列を合併し、小さい順に整列するプログラムを作成しよう。
#手順
#列Cを用意する。列Cは最初、空である。
#以下の操作を、列A・Bのすべての要素が消えるまで繰り返す。
#列Aが空であれば、列Bで最小の要素を列Cに移す。
#列Bが空であれば、列Bで最小の要素を列Cに移す。
#そのいずれでもなければ、列Aで残っている最小の要素と、列Bで残っている最小の要素を比較する。
#その後、小さい方を列Cに移す。
#================================================================
#マージソート
#k個の要素からなる列をそれぞれk/2個の要素からなる列A・Bに分割する。
#列Aに対してマージソートを行い、ソートした後の列をA'とする。
#列Bに対してマージソートを行い、ソートした後の列をB'とする。
#列A'とB'に対してMerge操作を行うことでk個の要素からなる列がソートされる。



##動的計画法
#数列の漸化式のように、小さい問題(この問題では前の)結果を利用して解くアルゴリズム
#カエルの移動の一般化
#問題
#N個の足場があり、左からi番目の足場(足場iとする)の高さはhi。カエルは以下の行動を繰り返すこと、足場1から足場Nに移動したい。
#足場iからi+1にジャンプ。体力|hi-hi+1|を消費する。(1<=i<=N+1)
#足場iからi+2にジャンプ。体力|hi-hi+2|を消費する。(1<=i<=N+2)
#消費する体力の合計として考えられる最小値を求めよ。
# 入力
N = int(input())
H = list(map(int, input().split()))

# 動的計画法
dp = [ None ] * N
dp[0] = 0
for i in range(1, N):
	if i == 1:
		dp[i] = abs(H[i - 1] - H[i])
	if i >= 2:
		v1 = dp[i - 1] + abs(H[i - 1] - H[i])  # 1 個前の足場からジャンプするとき
		v2 = dp[i - 2] + abs(H[i - 2] - H[i])  # 2 個前の足場からジャンプするとき
		dp[i] = min(v1, v2)

# 答えの出力
print(dp[N - 1])

#階段の上り方の問題
#太郎くんはN段の階段を上ろうとしています。彼は一歩で1段か2段登ることができます。0段目から出発し、N段目に辿り着くまでの移動方法は何通りあるかを計算してください。
N = int(input())
dp = [None]*[N+1]
for i in range(N+1):
    if i<=1:
        dp[i]=1
    else: 
        dp[i]=dp[i-1]+dp[i-2]
print(dp[N])

#ナップザック問題
#N個の品物があり、品物には1,2,・・・Nと番号が付けられている。品物i(1<=i<=N)の重さはwiであり、価値はviである。
#太郎君は、重さの合計がWを超えないようにN個の品物からいくつか選ぶことにした。選んだ品物の価値として考えられる最大値を求めてください。
#二次元配列を用いた動的計画法を考える。
#d[i][j]:品物iまでの中から、重さの合計がjとなるように選んだときの価値の最大値
#i>=1の場合、重さの合計がjとなるように品物iまでの中から選ぶ方法は以下の二つ
#1:品物i-1までの重さの総和がjであり、品物iを選ばない
#2:品物i-1までの重さの総和がj-wiであり、品物iを選ぶ
#よって、dp[i][j]=max(d[i-1][j],dp[i-1][j-wi]+vi)
#コード
## 注意
# Python は配列のランダムアクセスに時間がかかるため、N = 100, W = 100000 では実行に 5 秒程度かかり、TLE（実行時間制限オーバー）になります。
# 一方、同じプログラムを PyPy3 で提出すると、実行に 0.5 秒程度しかかからず、AC（正解）することができます。
# 入力
N,W = map(int,map(int,input().split()))
w = [None]*N
v = [None]*N
for i in range(N):
    w[i],v[i] = map(int,input().split())

#配列の初期化
INF = 10**10
#x = [リストの要素を計算する式 for 計算で使用する変数 in 反復可能オブジェクト]
dp = [[None]*(W+1) for i in range(N+1)]
dp[0][0]=0
for i in range(1,W+1):
    dp[0][i]= -INF

#動的計画法
for i in range(1,N+1):
    for j in range(0,W+1):
        if j<w[i-1]:
            #j<w[i-1]のとき、方法1だけしか選べない
            dp[i][j]=dp[i-1][j]
        else:
            #j >= w[i-1] のとき、方法 A・方法 B どちらも選べる
            dp[i][j]=max(dp[i-1][j],dp[i-1][j-w[i-1]+v[i-1]])

answer = max(dp[N])
print(answer)


##配列の二分探索


##計算幾何
##累積和:0(N)
##ニュートン法
##エラトステネスのふるい:O(NloglogN)
##深さ優先探索
##幅優先探索
##繰り返し二乗法:O(logN)
##行列累乗の計算
##勾配降下法
##貪欲法
##A*
	
	
