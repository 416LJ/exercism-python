def answer(question):
    
    if not question.startswith("What is") or "cubed?" in question:
        raise ValueError("unknown operation")
    
    cleaned_string = question.replace("?","").replace("divided by","/").replace("multiplied by","*").replace("What is","").replace("plus","+").replace("minus","-")
    cleaned_string = cleaned_string.split()   

    if not cleaned_string:
        raise ValueError("syntax error")

    while len(cleaned_string) > 1:
        try:
            x = int(cleaned_string[0])
            y = int(cleaned_string[2])
            operation = cleaned_string[1]
            remaining = cleaned_string[3:]

            if operation == "+":
                cleaned_string = [x + y] + remaining
            elif operation == "*":
                cleaned_string = [x * y] + remaining
            elif operation == "/":
                cleaned_string = [x / y] + remaining
            elif operation == "-":
                cleaned_string = [x - y] + remaining
            else:
                raise ValueError("syntax error")
            
        except:
            raise ValueError("syntax error")
    
    return int(cleaned_string[0])
       