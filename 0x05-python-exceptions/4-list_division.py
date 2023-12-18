#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    """Divides two lists element by element.

    Args:
        my_list_1 (list): The first list.
        my_list_2 (list): The second list.
        list_length (int): The number of elements to divide.

    Returns:
        A new list of length list_length containing all the divisions.
    """
    new_list = []
    for i in range(0, list_length):
        try:
            elem_1 = my_list_1[i] if i < len(my_list_1) else 0
            elem_2 = my_list_2[i] if i < len(my_list_2) else 0

            if elem_2 == 0:
                raise ZeroDivisionError("division by 0")

            division_result = elem_1 / elem_2

            if not isinstance(division_result, (int, float)):
                raise TypeError("wrong type")

            new_list.append(division_result)

        except TypeError:
            print("wrong type")
            new_list.append(0)

        except ZeroDivisionError:
            print("division by 0")
            new_list.append(0)

        except IndexError:
            print("out of range")
            new_list.append(0)

        finally:
            pass

    return (new_list)
