from flask import Flask, render_template, jsonify, request
import save_codes
app = Flask(__name__)

# TODO: 解决语言分类
@app.route('/upload', methods=['POST'])
def upload():
    data = request.form.to_dict()
    print(data['name'])
    save_codes.save(data['name'], data['language'], data['code'])
    save_codes.upload(data['name'])
    resp = jsonify({'data': '上传成功'})
    resp.headers['Access-Control-Allow-Origin'] = 'https://leetcode-cn.com'
    return resp


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

# TODO: 完成python与github的接口
