import replicate
#for i in range(2100, 2351, 10):
    
    #location= "C:/Users/shubh/OneDrive/Desktop/STARC/frames/frame"+str(i)+".jpg"
output = replicate.run("nelsonjchen/minigpt-4_vicuna-13b:c1f0352f9da298ac874159e350d6d78139e3805b7e55f5df7c5b79a66ae19528",input={"image": open("C:/Users/shubh/OneDrive/Desktop/STARC/frames/frame2140.jpg", "rb") , "message":" reply with only if the batsman is left handed or right handed  reply only with left or right no other words"}

)

print(output)
