graph = {
    'Alex': ['Riya', 'John'],
    'Riya': ['Alex']
}

for person, friends in graph.items():
    print(f"{person} -> {', '.join(friends)}")