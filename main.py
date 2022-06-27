import durakonline, json

Durak = durakonline.Client("$2a$06$aFpreTCZF6q7JCqqUJbAuO")

@Durak.event(command="user_msg")
def event(data):
    try:
        user_id = data["from"]
    except:
        user_id = Durak.uid
    to = data["from"] if data["to"] == Durak.uid else data["to"]
    user_name = data["name"]
    Durak.friend.send_message(f">>{user_name}, hello!", to)
    # Durak.send_message(f">>{user_name}, hello!", to)