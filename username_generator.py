import random

def generate_username(full_name):
    name_parts=full_name.split()
    if len(name_parts)<2:
        return "Please enter a full name (first and last)"
    first_name=name_parts[0].lower()
    last_name=name_parts[-1].lower()

    username1=first_name+last_name
    username2=first_name[:3]+last_name[-3:]
    username3=last_name[:3]+first_name[-2:]

    rand_num=random.randint(10,99)
    username4=first_name+str(rand_num)
    username5=last_name+str(rand_num)


    username6=first_name[1:3]+last_name[-4:-1]+str(random.randint(1,9))
    

    username8=first_name[:3]+rand_num+last_name

    #username9=first_name[:3]+first_name[:3]
    

    usernames=[username1,username2,username3,username4,username5,username6,username8,]
    return random.choice(usernames)


while True:

    full_name=input("Enter your full name (or type 'exit' to quit): ")

    if full_name.lower()=="exit":

        break

    username=generate_username(full_name)

    print(username)
    print("-"*40)

