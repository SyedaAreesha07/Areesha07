from users.intern import Intern
from users.mentor import Mentor
from managers.manager import Manager
from messages.message import Message

def main():
    intern = Intern("intern_amy", "amy@uni.edu", "MIT")
    mentor = Mentor("mentor_john", "john@expert.com", "Python")
    manager = Manager("manager_lee", "lee@company.com")

    manager.add_user(intern)
    manager.add_user(mentor)

    print(intern)
    print(mentor)
    print(manager)

    msg1 = Message(intern, "Can you help me with my project?")
    msg2 = Message(mentor, "Sure! What do you need help with?")
    print(msg1)
    print(msg2)

    print(manager.broadcast_message("Reminder: Meeting at 3 PM"))

    for user in [intern, mentor, manager]:
        print(f"{user._username} role: {user.role()} | Length of username: {len(user)}")

if __name__ == "__main__":
    main()
