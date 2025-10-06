from django.shortcuts import render

def power_calculator(request):
    
    power = None
    if request.method == 'POST':
        try:
            # Get values from the POST request
            voltage = float(request.POST.get('voltage'))
            current = float(request.POST.get('current'))
            
            # Perform the calculation
            power = voltage * current
            
        except (ValueError, TypeError):
            # Handle invalid input gracefully
            power = "Invalid input"

    # Render the template with the calculation result
    return render(request, 'mathapp/math.html', {'power': power})

