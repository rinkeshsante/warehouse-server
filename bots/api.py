import json
from django.http import JsonResponse
from packages.models import Package
from location_manager.models import LoactionManger
from bots.models import Bot
from django.views.decorators.csrf import csrf_exempt
from django.forms.models import model_to_dict


@csrf_exempt
def nextTask(request):
    try:
        # get data from request
        data = json.loads(request.body)['data']
        bot_id = data['bot_id']
        current_loacation = data['location']

        # update bot loaction
        bot = Bot.objects.get(id=bot_id)
        bot.location_X = current_loacation['X']
        bot.location_Y = current_loacation['Y']
        bot.save()

        # select best parcel to move
        pakages = Package.objects.order_by('-date_of_arrival')[0]

        # get destination location for postal code
        loaction = LoactionManger.objects.get(
            postal_address=pakages.postal_code)

        if loaction.is_full:
            return JsonResponse({"error": f"No Free space at location for postal code {loaction.postal_address} at {loaction.location_X},{loaction.location_Y}"})

        # generate respose
        response = {}
        response["Bot_id"] = bot_id
        response["package"] = model_to_dict(pakages)
        response["destination"] = {
            "X": loaction["location_X"],
            "Y": loaction["location_Y"]
        }

        return JsonResponse(response)
    except Exception as e:
        print(e)
        return JsonResponse({"error": str(e)})
