    from library.existing_members import library_existing_members
    from library.member_class import Member

    id = 1


    def adding_member(name, age, id):
        members = library_existing_members()
        new_member = Member(name, age, id)
        new_member_name = input("what is your name?")
        new_member_age = int(input("what is your age?"))


        id += 1
        new_member = Member(new_member_name, new_member_age, id)
        members.append(new_member)
        for member in members:
            print(f"member:{member.name},age:{member.age},id:{member.id}")
