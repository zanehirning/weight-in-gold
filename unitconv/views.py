from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from .models import convTable

def convert(request):
    table = convTable
    
    if 'from' not in request.GET or 'to' not in request.GET or 'value' not in request.GET:
        return HttpResponse(f"""<h1> Usage: http://127.0.0.1:8000/unitconv/convert?OPTIONS </h1>
                                    <h3> Each of these options must be included in the request: </h3>
                                        <ul>
                                            <li> from: T | lb | t_oz | g | kg | oz</li>
                                            <li> to: T | lb | t_oz | g | kg | oz</li>
                                            <li> value: a floating point integer</li>
                                        </ul>
                                    """)

    firstUnit = request.GET['from']
    secondUnit = request.GET['to']
    value = request.GET['value']
    if firstUnit=='' or secondUnit=='' or value=='':
        return JsonResponse({'error': 'One or more of these values are not in the correct input', 'usage': 'from - T | lb | t_oz | g | kg | oz // to - T | lb | t_oz | g | kg | oz // value - floating point integer'})
    
    if firstUnit == 't_oz' or secondUnit == "t_oz":
        if firstUnit.isdigit() or secondUnit.isdigit():
            return JsonResponse({'error': 'One or more of these values are not in the correct input', 'usage': 'from - T | lb | t_oz | g | kg | oz // to - T | lb | t_oz | g | kg | oz // value - floating point integer'})
        converted_unit = (float(value) * (1/float(table.toUnit(convTable.objects.get(unit=f'{firstUnit}')))) * (float(table.toUnit(convTable.objects.get(unit=f'{secondUnit}')))))
        return JsonResponse({'unit': secondUnit, 'value': (converted_unit)})

    if not firstUnit.isalpha() or not secondUnit.isalpha():
        return JsonResponse({'error': 'One or more of these values are not in the correct input', 'usage': 'from - T | lb | t_oz | g | kg | oz // to - T | lb | t_oz | g | kg | oz // value - floating point integer'})

    converted_unit = (float(value) * (1/float(table.toUnit(convTable.objects.get(unit=f'{secondUnit}')))) * (float(table.toUnit(convTable.objects.get(unit=f'{firstUnit}')))))
    return JsonResponse({'unit': secondUnit, 'value': (converted_unit)})

# Create your views here.
