def cloud_check(persent: int) -> str:
    if persent < 15:
        return 'солнечно'
    elif persent <= 50 and persent >= 15:
        return 'облачно'
    else:
        return 'пасмурно'

