from collections import Counter

from django.shortcuts import render

# Для отладки механизма ab-тестирования используйте эти счетчики
# в качестве хранилища количества показов и количества переходов.
# но помните, что в реальных проектах так не стоит делать
# так как при перезапуске приложения они обнулятся
counter_show = Counter()
counter_click = Counter()


def index(request):
    from_where = request.GET.get('from-landing')

    if from_where == 'original':
        counter_click['original'] += 1
    elif from_where == 'test':
        counter_click['test'] += 1

    return render(request, 'index.html')


def landing(request):
    landing_type = request.GET.get('ab-test-arg', 'original')

    if landing_type == 'original':
        counter_show['original'] += 1
        return render(request, 'landing.html')
    else:
        counter_show['test'] += 1
        return render(request, 'landing_alternate.html')


def stats(request):
    try:
        test_stats = counter_click['test'] / counter_show['test']
    except ZeroDivisionError:
        test_stats = 'Пока недостаточно информации'

    try:
        original_stats = counter_click['original'] / counter_show['original']
    except ZeroDivisionError:
        original_stats = 'Пока недостаточно информации'

    return render(request, 'stats.html', context={
        'test_conversion': test_stats,
        'original_conversion': original_stats,
    })
