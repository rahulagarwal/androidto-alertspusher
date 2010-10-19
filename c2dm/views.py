from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from alertspusher.c2dm.models import AndroidDevice
from django.shortcuts import render_to_response, get_object_or_404

def index(request):
    return HttpResponse("Hello, Android. You're at the Registration index.")
    
def register(request, device_id):
    if request.method == 'GET':
        return HttpResponse("Invalid request. Need to POST with required parameters.")
    elif request.method == 'POST':
        return _registerPost(request, device_id)
    else:
        return HttpResponse("Invalid request.")

def _registerPost(request, device_id):
    device = None
    try:
        device = AndroidDevice.objects.get(device_id=device_id)
    except AndroidDevice.DoesNotExist:
        print 'New Device to Add- DeviceID- ', device_id

    if device is None:
        device = AndroidDevice()
        if request.POST.get('registration_id') is None:
            return HttpResponse("Invalid/Missing POST parms.")
        device.device_id = device_id
        device.registration_id = request.POST.get('registration_id')
        device.save()
        return HttpResponse("Successfully ADDED the device - %s" % device_id)
    else:
        device.registration_id = request.POST.get('registration_id')
        device.save()
        return HttpResponse("Successfully UPDATED the device - %s" % device_id)
        
def unregister(request, device_id):
    device = None
    try:
        device = AndroidDevice.objects.get(device_id=device_id)
        device.delete()
    except AndroidDevice.DoesNotExist:
        print "Device to unregister not found: ", device_id
    
    return HttpResponse("Successfully UNREGISTERED the device - %s" % device_id)
    
def alert(request):
     return render_to_response('alert.html', {}, context_instance=RequestContext(request))
        
def sendAlert(request):
    message = request.POST['message']
    if message is None or len(str(message)) == 0:
        return render_to_response('alert.html', {'error_message':'Empty Message!'}, context_instance=RequestContext(request))
    else:
        all_devices = AndroidDevice.objects.filter()
        for device in all_devices:
            device.send_message(alert=message)
            
    return render_to_response('alertsent.html', {'last_message': message}, context_instance=RequestContext(request))
        
        