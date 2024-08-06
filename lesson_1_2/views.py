from django.http import HttpResponse
from django.shortcuts import render

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
}

def dish_view(request, dish):
    servings = request.GET.get("servings")
    context = {
        'recipe': {
        }
    }
    if servings != None:
        for k, v in DATA.items():
            if k == dish:
                for a, b in v.items():
                    context["recipe"][a] = b * int(servings)
        return render(request, "demo.html", context)
    else:
        for k, v in DATA.items():
            if k == dish:
                for a, b in v.items():
                    context["recipe"][a] = b
        return render(request, "demo.html", context)

