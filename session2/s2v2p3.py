def remove_name(people, secret_identity):
    for name in people:
        if name == secret_identity:
            people.remove(name)
    print(people)
    
people = ['Batman', 'Superman', 'Bruce Wayne', 'The Riddler', 'Bruce Wayne']
secret_identity = 'Bruce Wayne'
remove_name(people, secret_identity)