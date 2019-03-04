def vokal(b):
    a="aiueoAIUEO"
    x=0
    for i in b:
        if i not in a:
            x+=1
    print(len(b),x)

vokal("Surakarta")