avl_candy = 10
req_candy = int(input())
if req_candy < avl_candy and req_candy != 0:
    print("candy sold :", req_candy)
    avl_candy = avl_candy - req_candy
    if avl_candy < 5: avl_candy = 10
    print("candy in jar :", avl_candy)
else:
    print("Invalid Input")
    print("candy in jar : ", avl_candy)