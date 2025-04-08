history = []
history_limit = 15
history_prompt = "Here is the conversation history of your previous repsonses, they are in order of oldest to newest: "

def add_to_history(response):

    # Split the response into a thinking portion and an answering portion. Delete thinking portion
    pre_proccessed_response = response.split("</think>")
    pre_proccessed_response.pop(0)
    # Answering portion
    proccessed_response = pre_proccessed_response[0]

    # Add the response to the history
    if len(history) >= history_limit:
        history.pop(0)
        history.append(proccessed_response)
    else:
        history.append(proccessed_response)

def supply_history():
    if len(history) > 0:
        history_string_list = " ".join(history)
        return(history_prompt + history_string_list)
    else:
        return ""