

def set_chat_for_users_from_scratch(views):

    for view in views:
        view.request_password_icon.click()
    for view in views:
        view.type_message_edit_box.send_keys("qwerty1234")
    for view in views:
        view.confirm()
    for view in views:
        view.type_message_edit_box.send_keys("qwerty1234")
    for view in views:
        view.confirm()
    for view in views:
        view.find_text("Tap here to enter your phone number & I\'ll find your friends")
