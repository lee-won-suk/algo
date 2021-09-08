while True:
    mess=input().rstrip()
    if mess=="END":
        break
    else:
        print(mess[::-1] )
