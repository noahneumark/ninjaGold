from django.shortcuts import render, redirect, HttpResponse
import random, datetime

def index(request):
    if not "gold" in request.session:
        request.session['gold'] = 0
        request.session['activitylist'] = []
    return render(request, "index.html")

def process(request):
    if request.POST['location'] == "farm":
        earnings = random.randint(10, 20)

    elif request.POST['location'] == "cave":
        earnings = random.randint(5, 10)

    elif request.POST['location'] == "house":
        earnings = random.randint(2, 5)

    elif request.POST['location'] == "casino":
        if request.session['gold'] < 50:
            request.session['activitylist'].insert(0, {"message" : 'You only have ' + str(request.session['gold']) + ' gold. Get out of here! ' + str(datetime.datetime.now().strftime('%a %x %S')), "color" : "black" } )
            gold = request.session['gold']
            request.session.modified = True
            return redirect('/')

        else:
            loseearn = random.randint(0, 1)
            if loseearn == 0:
                earnings = random.randint(0, 50)
                request.session['gold'] -= earnings
                request.session['activitylist'].insert(0, {"message" : 'You lost ' + str(earnings) + ' golds from the casino! ' + str(datetime.datetime.now().strftime('%a %x %S')), "color" : "red" } )
                return redirect('/')
            else:
                earnings = random.randint(0, 50)

    request.session['gold'] += earnings
    request.session['activitylist'].insert(0, {"message" : 'You earned ' + str(earnings) + ' golds from the ' + str(request.POST['location']) + '! ' + str(datetime.datetime.now().strftime('%a %x %S')), "color" : "green" } )

    return redirect('/')

def reset(request):
    del request.session['gold'] 
    return redirect('/')
