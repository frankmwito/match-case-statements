# match case of a friut with message

def friut_message(fruit):
    ruit = fruit.lower()
    match ruit:
        case "apple":
            return "Apples are sweet"
        case "banana":
            return "Bananas are yellow"
        case "tangerine":
            return "Tangerines are sour"
        case "ovacado":
            return "ovacados are huge"
        case "watermelon":
            return "watermelon are juicy"
        case _:
            return "invalid choice of fruit"
   
print(friut_message( input("Enter your choice of fruit: ")))