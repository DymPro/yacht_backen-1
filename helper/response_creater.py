def save_msg(data=None):
    msg = {
        'success':True,
        'messge':'Data saved successfully'
    }
    if data is not None:
        msg['data'] = data
    return msg

def update_msg():
    msg = {
        'success':True,
        'messge':'Data updated successfully'
    }
    return msg

def delete_msg():
    msg = {
        'success':True,
        'messge':'Data deleted successfully'
    }
    return msg

def fetch_msg(data=None):
    msg = {
        'success':True,
        'messge':'Data fetched successfully'
    }
    if data is not None:
        msg['data'] = data
    return msg

def failed_msg(data=None):
    msg = {
        'success':False,
        'messge':'Failed due to some error'
    }
    if data is not None:
        msg['messge'] = data
    return msg