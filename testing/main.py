def stuff(num):
    try:
        return int(num) + 3
    except ValueError as err:
        return err
