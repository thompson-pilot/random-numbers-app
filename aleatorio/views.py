from django.shortcuts import render
import random


def index(request):
    return render(request, "input.html")


def randomnum(request):
	num1 = request.POST['num1']
	num2 = request.POST['num2']

	if num1.isdigit() and num2.isdigit():
		a = int(num1)
		myGame = [n + 1 for n in range(a)]

		b = int(num2)
		res = random.sample(myGame, b)
		res.sort()

        #return render(request, "result.html", {"result":res})
		return render(request, "result.html", {"result": (',  '.join(str(e) for e in res))})

	else:
		res = "Only digits are allowed"
		return render(request, "result.html", {"result": res})
