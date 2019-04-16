from django.shortcuts import render,redirect
from driver.database import mongo_test
from driver.database import get_last_hour,get_miner_config
from django.http import HttpResponseRedirect

# Create your views here.
def monitoring(request):
    if mongo_test():
        if request.COOKIES.get('SessionAuth'):
            temp_hash = get_last_hour('my-mongo-user', 'NGEyY2IwZWQ5OGM1', 'mon.hcsone.net:27117/')
            temp = get_miner_config('vahid', 1, 'my-mongo-user', 'NGEyY2IwZWQ5OGM1', 'mon.hcsone.net:27117/')
            out =[]
            for item in temp_hash:
                for tem in temp:
                    if item['miner'] == tem['id']:
                        item['miner'] = tem['name']
                if item['miner'] not in out:
                    out.append(item['miner'])
            final =[]
            for item in out:
                final.append(item)

            #for item in out:
            #    for miner in temp_hash:
            #       if miner['miner'] == item:
            #            final[item].append(miner)
            print(final)
            return render(request,'monitoring.html',context={'miner_name':final,'log':temp_hash})
        else:
            return redirect('/')
    else:
        return render(request,'db_error.html')