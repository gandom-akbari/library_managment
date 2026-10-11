class Member:
    def __init__(self,name,age,id):
        self.name=name
        self.age=age
        self.id=id

member1=Member(name="gandom",age=20,id=1)
id=1
members=[member1]
new_member_name=input("what is your name?")
new_member_age=int(input("what is your age?"))
id+=1
new_member=Member(new_member_name,new_member_age,id)
members.append(new_member)
for member in members:
    print(f"member:{member.name},age:{member.age},id:{member.id}")
