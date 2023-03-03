class Multiton:
    amount = 3
    count = 0
    obj_list = []

    def __new__(cls, *args, **kwargs):
        cls.count += 1
        if cls.amount != 0:
            cls.amount -= 1
            obj = super().__new__(cls)
            cls.obj_list.append(obj)
            return obj
        else:
            return cls.obj_list[cls.count % 3-1]
