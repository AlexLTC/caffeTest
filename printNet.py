# https://stackoverflow.com/questions/60703735/how-to-show-all-the-names-of-caffe-layers-in-python
import sys
import caffe
sys_path = '/da-faster-rcnn/models/da_faster_rcnn'
sys.path.append(sys_path)

net = caffe.Net('train.prototxt', caffe.TEST)

for key in net.layer_dict:
    print(key)
