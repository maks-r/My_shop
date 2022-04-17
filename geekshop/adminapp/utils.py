from functools import partial
from django.contrib.auth.decorators import user_passes_test


def superuser_required():
    return user_passes_test(lambda u: u.is_superuser)

# def superuser_required(function):
#     return user_passes_test(lambda u: u.is_superuser)(function)

# !!!!!!!!!!У меня с вставкой function не работает, а без нее как выше все ОК!!!!!!!!!!!




# superuser_required = partial(user_passes_test(lambda u: u.is_superuser))
