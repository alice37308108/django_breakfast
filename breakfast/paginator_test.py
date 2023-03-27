from django.core.paginator import Paginator
from breakfast.models import Breakfast


def paginator_test():
    objects = Breakfast.objects.all()
    p = Paginator(objects, 2)

    print(p.count)  # 5
    print(p.num_pages)  # 3
    print(type(p.page_range))  # <class 'range'>
    print(p.page_range)  # range(1, 4)

    page1 = p.page(1)
    print(page1)  # <Page 1 of 3>
    print(page1.object_list)
    # <QuerySet [<Breakfast: Breakfast object (1)>, <Breakfast: Breakfast object (2)>]>

    page2 = p.page(2)
    print(page2)  # <Page 2 of 3>
    print(page2.object_list)
    # <QuerySet [<Breakfast: Breakfast object (3)>, <Breakfast: Breakfast object (4)>]>

    print(page2.has_next())  # True
    print(page2.has_previous())  # True
    print(page2.has_other_pages())  # True
    print(page2.next_page_number())  # 3

    print(page2.previous_page_number())  # 1
    print(page2.start_index())  # 3
    print(page2.end_index())  # 4
