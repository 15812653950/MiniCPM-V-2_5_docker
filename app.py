from flask import Flask, request, jsonify
from PIL import Image
from transformers import AutoModel, AutoTokenizer
import traceback
import os
import uuid
app = Flask(__name__)


model_name = 'openbmb/MiniCPM-Llama3-V-2_5-int4'
model_path = f'model/{model_name}'
# model_path = model_name
# model_path = f'/media/gennexuslabs/data1/model/{model_name}'
# model_path = f'/home/shjas/Raid1/shjas/model/{model_name}'
load_flag = 0


@app.route('/',methods=['POST','GET'])
def index():
    return 'Docker container is openbmb/MiniCPM-Llama3-V-2_5-int4'

##总台链接测试，确保启动正常
@app.route('/connect_test',methods=['POST','GET'])
def connect_test():
    return 'Docker container is up and running!'

@app.route('/load_model',methods=['POST','GET'])
def load_model():
    global tokenizer
    global model
    global load_flag
    if os.path.exists(model_path):
        model = AutoModel.from_pretrained(model_path,trust_remote_code=True)
        tokenizer = AutoTokenizer.from_pretrained(model_path, trust_remote_code=True)
        model = model.eval()
    else:
        model = AutoModel.from_pretrained(model_name,trust_remote_code=True)
        tokenizer = AutoTokenizer.from_pretrained(model_name, trust_remote_code=True)
        model.save_pretrained(model_path)
        tokenizer.save_pretrained(model_path)
        model = AutoModel.from_pretrained(model_path,trust_remote_code=True)
        tokenizer = AutoTokenizer.from_pretrained(model_path, trust_remote_code=True)
        model = model.eval()
    load_flag = 1
    return "model is loaded!!!"
    

## 发送结果到总台
##任务执行，发送任务进行处理
@app.route('/predict', methods=['POST','GET'])
def predict():
    
    if load_flag:
        print("model loaded")
    else:
        load_model()
        print("model loading")
    try:
        # Debugging info
        print("Request received")
        print("Headers:", request.headers)
        print("Form data:", request.form)
        print("Files:", request.files)
        # 获取 question 参数
        question = request.form.get('question')

        # 检查 question 是否为空
        if not question:
            return jsonify({"code": 400, "msg": "Question is required", "data": {}}), 400

        if 'file' not in request.files:
            return jsonify({"code": 404, "msg": "No file part", "data": {}}), 404


        if 'file' not in request.files:
            return jsonify({"code": 404, "msg": "No file part", "data": {}}), 404

        file = request.files['file']

        # 检查是否有文件被上传
        if file.filename == '':
            return jsonify({"code": 404, "msg": "No selected file", "data": {}}), 404

        # 检查文件类型
        if not (file.filename.endswith('.png') or file.filename.endswith('.jpg')):
            return jsonify({"code": 400, "msg": "Invalid file type. Only .png and .jpg are supported.", "data": {}}), 400

        # Debugging info
        print(f"File received: {file.filename}")
        # 生成 UUID 文件名并保存文件
        name = uuid.uuid4()
        filename = f"{name}.png"
        file.save(filename)

        image = Image.open(filename).convert('RGB')
        # question = 'What is in the image?'
        msgs = [{'role': 'user', 'content': question}]

        res = model.chat(
            image=image,
            msgs=msgs,
            tokenizer=tokenizer,
            sampling=True,  # if sampling=False, beam_search will be used by default
            temperature=0.7,
            # system_prompt='' # pass system_prompt if needed
        )
        # print(res)

        os.remove(filename)
        return jsonify({"code": 200, "msg": "Success", "data": res}), 200

    except Exception as e:
        traceback.print_exc()
        return jsonify({"code": 404, "msg": str(e), "data": {}}), 404

# Run the app if this file is executed
if __name__ == "__main__":
    app.run(port = 6790, host='0.0.0.0', debug=True)

