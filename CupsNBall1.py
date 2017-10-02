#initial position=1
def alpha(post):#for switching type A
    post[0],post[1]=post[1],post[0]
    return post
def beta(post):#for switching type B
    post[1],post[2]=post[2],post[1]
    return post
def charlie(post):#for swhiching type C
    post[0],post[2]=post[2],post[0]
    return post
def pattern_main():#main program
    post=['alpha','beta','gamma']
    patterns=input("")
    pattern=list(patterns.upper())
    for pattern in patterns:
        if pattern=="A":
            alpha(post)
        if pattern=="B":
            beta(post)
        if pattern=="C":
            charlie(post)

    ballpost=post.index('alpha')
    print(ballpost+1)#printing mechanism
pattern_main()
