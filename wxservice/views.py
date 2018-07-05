from django.shortcuts import render,redirect
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from wxservice import util
import time
from django.views.decorators.csrf import csrf_exempt
from .models import recharge_oder, fee, pay_user
from django.db.models import Q

import requests
import os

from django.urls import reverse


# Create your views here.

def home(request):
    return render(request, 'home.html')


def check_order(request):
    out_trade_no = request.GET['order']
    order = recharge_oder.objects.filter(out_trade_no=out_trade_no)
    if order:
        return render(request, 'sign.html')
    else:
        return HttpResponse('未查询到该订单，若您已支付可复制支付订单号留言，我收到后会第一时间联系您！')


def fee_info(request):
    no = request.POST['staff_no']
    request.session['staff_no'] = no
    fee_month = time.strftime("%Y%m", time.localtime())

    fee_Detail = fee.objects.filter(userid__staffNo=no).filter(month=fee_month).values()[0]
    user_info = pay_user.objects.filter(staffNo=no).values()[0]
    out_trade_no = time.strftime("%Y%m%d%H%M%S", time.localtime()) + no
    pay_data = {
        'mchid': 'ZBEQWD',
        'total_fee': int(fee_Detail['feeOwn'] * 100),
        'out_trade_no': out_trade_no,
        'notify_url': 'www.yoouhome.com/pay_notify',
        'callback_url': 'www.yoouhome.com/check_order?order=' + out_trade_no
    }

    if fee_Detail['payMethod'] == 1:
        pay_method = '按月缴纳'
    elif fee_Detail['payMethod'] == 3:
        pay_method = '按季缴纳'
    else:
        pay_method = '按年缴纳'

    user_data = {
        'fee_amount': fee_Detail['feeOwn'],
        'sub_method': pay_method,
        'monthly_fee': fee_Detail['monthlyFee'],
        'apart': user_info['depart'],
        'staff_no': no,
        'staff_name': user_info['name'],
        'staff': user_info['staff'],
        'mchid': 'ZBEQWD',
        'total_fee': int(fee_Detail['feeOwn'] * 100),
        'out_trade_no': time.strftime("%Y%m%d%H%M%S", time.localtime()) + no,
        'sign': util.signData(pay_data),
        'notify_url': 'www.yoouhome.com/pay_notify',
        'callback_url': 'www.yoouhome.com/check_order?order=' + out_trade_no
    }
    return render(request, 'fee_info.html', user_data)


def getsession(request):
    if request.method=='POST':
        if request.session.has_key('staff_no'):
            return HttpResponse(request.session['staff_no'])
        else:
            return HttpResponse('none')
    else:
        return HttpResponse('get方法')

def sign(request):
    return render(request, 'sign.html')


## # 接受客户端签名,并跳转至支付
def result(request):
    user = request.session['staff_no']
    if len(request.POST['i_sign']) > 0:
        str_base64 = request.POST['i_sign'].split(",")[1]
    timeStamp = time.strftime("%Y%m%d%H%M%S", time.localtime())
    filename = str(timeStamp) + "_" + user
    save_result = util.save_pic(filename, str_base64)
    if save_result == "success":
        return render(request, 'result.html', {'result': '缴纳成功！'})
    else:
        return render(request, 'result.html', {'result': '签名存储失败，请返回上一页重新操作！'})

    # response = requests.post(psot_url, data=post_data)

@csrf_exempt
def pay_notify(request):
    post_data = request.POST.dict()
    for key in post_data:
        print('%s=%s' % (key, post_data[key]))

    if post_data['return_code'] == 1 or  post_data['return_code'] == '1':
        # Todo 验签逻辑
        data_sign = post_data['sign']
        post_data.pop('sign')
        sign = util.signData(post_data)
        # if data_sign != sign:
        #     return HttpResponse('签名有误')

        # Todo 验证重复问题
        out_trade_no = post_data['out_trade_no']
        order = recharge_oder.objects.filter(out_trade_no=out_trade_no)
        if order:
            return HttpResponse('该订单已存在')
        else:
            # Todo 处理自身业务逻辑
            #  存储数据,attach 可能不存在
            if 'attach' in post_data:
                attach = post_data['attach']
            else:
                attach = ''

            print(type(post_data['total_fee']))
            order = recharge_oder(total_fee=int(post_data['total_fee'])/100, out_trade_no=post_data['out_trade_no'], payjs_order_id=post_data['payjs_order_id'], transaction_id=post_data['transaction_id'], time_end=post_data['time_end'],
                                  openid=post_data['openid'], attach=attach, mchid=post_data['mchid'])
            order.save()
            user_id = out_trade_no[14:]
            fee_month = out_trade_no[:6]
            fee_update = fee.objects.get(Q(userid_id=user_id), Q(month=fee_month))
            fee_update.status = 1
            fee_update.feeOwn = float(fee_update.feeOwn) - int(post_data['total_fee'])/100
            fee_update.feeDone = float(fee_update.feeDone) + int(post_data['total_fee'])/100
            fee_update.order = post_data['out_trade_no']
            fee_update.save()
            return HttpResponse('Success!')

    else:
        return HttpResponse('return code 错误')





def cashier_pay(request):
    return render(request, 'cashier.html')


def native_pay():
    native_post_url = "https://payjs.cn/api/native"
    native_post_data = {
        'mchid': 'ZBEQWD',
        'notify_url': 'http://yoouhome.com/pay_notify',
        'out_trade_no': '20180501140760',
        'total_fee': 1,
    }
    native_sign = util.generSign(native_post_data)
    native_post_data['sign'] = native_sign
    native_response = requests.post(native_post_url, data=native_post_data)
    pay_url = eval(native_response.text)
    return pay_url['code_url']

def cashTest(request):
    return render(request, 'cashTest.html')

def jqueryTest(request):
    return render(request, 'jquertMobile.html')



if __name__=='__main__':
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    print(BASE_DIR)
