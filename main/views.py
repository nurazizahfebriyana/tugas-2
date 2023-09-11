from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'name': 'NCT THE 4th ALBUM \'THE GOLDEN AGE\' Photobook ver.',
        'price': 'Rp 300.000,00',
        'description': 'Get a taste of NCT\'s diverse combination, transformation, and infinite synergy from the participating 20 members from NCT 127, NCT DREAM, and WayV.',
        'amount': 100

    }

    return render(request, "main.html", context)