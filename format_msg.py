def get_format_msg(data: dict):
    msg = """
    *{} {} {}*
    Chasis: {}
    N motor: {}
    Patente: {}

    *Repuestos*:
    - 

    """.format(
        data['car_data']['marca'],
        data['car_data']['modelo'],
        data['car_data']['año'],
        data['car_data']['nchasis'],
        data['car_data']['nmotor'],
        data['car_data']['patente'],
    )

    print(msg)
    return msg
