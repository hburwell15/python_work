sandwich_orders = ['tuna', 'pastrami', 'meatball', 'pastrami', 'turkey', 'beef', 'pastrami']
finished_sandwiches = []

if 'pastrami' in sandwich_orders:
    print("I'm sorry we are out of pastrami")

while sandwich_orders:
    in_progress = sandwich_orders.pop()
    if in_progress == 'pastrami':
        continue
    print(f"\nOrder ready for the {in_progress} sandwich!")
    finished_sandwiches.append(in_progress)

print("\nWe have made these sandwiches today:")
for finished_sandwich in finished_sandwiches:
    print(finished_sandwich)