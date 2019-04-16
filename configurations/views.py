from django.shortcuts import render,redirect
from driver.database import mongo_test
from driver.database import get_miner_config,get_total_miner_config,add_miner_config
from .forms import addNewMiner

# Create your views here.
def configurations(request):
    if mongo_test():
        if request.COOKIES.get('SessionAuth'):
            if request.method == 'POST':
                request.POST['miner_name']
                miner_list = get_miner_config('vahid', 1, 'my-mongo-user', 'NGEyY2IwZWQ5OGM1', 'mon.hcsone.net:27117/')
                id=[]
                for item in miner_list:
                    id.append(item['id'])
                if len(id) != 0:
                    final_id = max(id) +1
                else:
                    final_id = 1
                miner_config = get_total_miner_config('vahid','my-mongo-user', 'NGEyY2IwZWQ5OGM1', 'mon.hcsone.net:27117/')
                old = miner_config
                my_conf= {"id": final_id, 'name':request.POST['miner_name'],'ip':request.POST['miner_ip'],
                                                         "user":request.POST['miner_user'],"pass":request.POST['miner_pass']}
                add_miner_config(old[0],my_conf,final_id-1,'my-mongo-user', 'NGEyY2IwZWQ5OGM1', 'mon.hcsone.net:27117/')
                form = addNewMiner()
                miner_list = get_miner_config('vahid', 1, 'my-mongo-user', 'NGEyY2IwZWQ5OGM1', 'mon.hcsone.net:27117/')
                return render(request, 'configurations.html', context={"miners": miner_list, 'form': form})
            else:
                miner_list = get_miner_config('vahid',1,'my-mongo-user','NGEyY2IwZWQ5OGM1','mon.hcsone.net:27117/')
                form = addNewMiner()
                return render(request,'configurations.html',context={"miners" : miner_list,'form':form})
        else:
            return redirect('/')
    else:
        return render(request,'db_error.html')