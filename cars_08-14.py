def new_car(manufacturer, model, **car_info):
    '''Build a dictonary of car information'''
    car_info['manufacturer_name'] = manufacturer
    car_info['car_model'] = model
    return car_info

car_profile = new_car('honda', 'civic', color='red', drive='2WD')
print(car_profile)