
values= [[ 1, 7, 14, 15],
[2, 5, 10],
[3, 8, 16],
[4, 11, 12, 13],
[6, 9]
]



def utility(ls):
    res = []
    for i in range(1,17):
        if i in ls:
            res.append(1)
        else:
            res.append(0)
    return res

#for vs in values:
#    print(utility(vs))

nomi = ["Hiroshi Tanaka", 
"Takeshi Yamamoto",
"Satoshi Nakamura",
"Akira Sato",
"Kenji Suzuki",
"Masaru Watanabe",
"Kazuki Takahashi",
"Shinji Kobayashi",
"Yoshio Ishikawa",
"Haruto Yamaguchi",
"Makoto Nakajima",
"Tatsuya Mori",
"Ryota Kato",
"Daisuke Yamata",
"Akihiro Fujimoto",
"Naoki Inoue"]

for x in nomi:
    print(x.upper()) 