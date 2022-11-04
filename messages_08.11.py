#Make a copy of unsent messages -use command forward slash to comment
def send_messages(unsent_messages, sent_messages):
    '''Show messages currently being sent.'''
    while unsent_messages:
        current_message = unsent_messages.pop()
        print(f"Sending message: {current_message}")
        sent_messages.append(current_message)

# def show_sent_messages(sent_message):
#     '''Display messages that have been sent.'''
#     print(f"The following messages have been sent: ")
#     for sent_message in sent_messages:
#         print(sent_message)

unsent_messages = ['How are you?', 'Good morning', 'How was your day?', 'I love you']
sent_messages = []

send_messages(unsent_messages[:], sent_messages)
# show_sent_messages(sent_messages)
print(f"Unsent messages - {unsent_messages}")
print(f"Sent messages - {sent_messages}")