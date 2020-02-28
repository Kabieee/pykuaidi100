from query import Query
from flask import Flask,make_response,jsonify,request,redirect
import json,hashlib
import time
import traceback
# "python.analysis.disabled":["unresolved-import"]

# def main():
#     ex_code = '70256206847223'
#     ex_type = 'huitongkuaidi'
#     q = Query('https://www.kuaidi100.com',ex_type,ex_code)
#     f = q.query_express()
#     data_dict = json.loads(f)
#     new_dict = {
#         'errmsg':data_dict['message'],
#         'status':data_dict['status'],
#         'ex_code':ex_code,
#         'ex_type':ex_type,
#         'desc':data_dict['data']
#     }

app = Flask(__name__)
    
@app.before_request
def before():
    if(request.path == '/query/'):
        # return request.path;
        try:
            request_time = int(request.args.get('ts'))
            server_time = int(time.time())
            request_token = request.args.get('tk')

            diff_time = abs(server_time-request_time)
            # if diff_time > 3:
            #     return json.dumps({'errmsg':'请求参数不正确','status':'500','desc':''})
            sha1 = hashlib.sha1()
            sha1.update('feiren_{0}'.format(request_time).encode('utf8'))
            server_token = sha1.hexdigest()
            # print(server_token,'feiren_{0}'.format(request_time))
            if server_token == request_token:
                return None
            else:
                return json.dumps({'errmsg':'token不正确','status':500,'desc':''})

        except Exception as e:
            return json.dumps({
                'errmsg':str(e),
                'status':500,
                'desc':''
            })

@app.after_request
def after(response):
    response.headers['Content-Type'] = 'application/json;charset=UTF-8'
    response.headers['Connection'] = 'close'
    return response

@app.route('/query/',methods=['POST','GET'])
def query():
        ex_code = '70256206847223'
        ex_type = 'huitongkuaidi'
        q = Query('https://www.kuaidi100.com',ex_type,ex_code)
        kuaidi_data = q.query_express()
        data_dict = json.loads(kuaidi_data)
        new_dict = {
            'errmsg':data_dict['message'],
            'status':data_dict['status'],
            'ex_code':ex_code,
            'ex_type':ex_type,
            'desc':data_dict['data']
        }
        response = make_response(json.dumps(new_dict,ensure_ascii=False))
        return response 

    

@app.errorhandler(404)
def not_fount(error):
    new_dict = {
        'errmsg':error.description,
        'status':error.code,
        'desc':''
    }
    return make_response(json.dumps(new_dict),200)

@app.errorhandler(500)
def not_fount(error):
    new_dict = {
        'errmsg':error.description,
        'status':error.code,
        'desc':''
    }
    return make_response(json.dumps(new_dict),200)

if __name__ == '__main__':
    app.run(debug=True)
    # main()