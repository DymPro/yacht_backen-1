from django.apps import apps


def savePractices(data,app_name,model_name):
    try:
        model = apps.get_model(app_name,model_name)
        model.create(**data)
        return model
    except:
        return None

def getData(data,app_name,model_name):
    if data is None:
        model = apps.get_model(app_name,model_name)
        # model.all()
        return model
    if data is not None:
        model = apps.get_model(app_name,model_name)
        model.filter(**data)
        return model
    return None
