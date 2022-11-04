sandwich_orders = ['tuna', 'meatball', 'pastrami', 'turkey', 'beef']
finished_sandwiches = []

while sandwich_orders:
    in_progress = sandwich_orders.pop()
    print(f"Order ready for the {in_progress} sandwich!")
    finished_sandwiches.append(in_progress)

print("\nWe have made these sandwiches today:")
for finished_sandwich in finished_sandwiches:
    print(finished_sandwich)