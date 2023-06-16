config路径地址：https://github.com/xixihic/openmmlabhomework/blob/a36305eb21e57fd9d0143c9ddc726ac0d12bcdc1/MMSegmentation/Segformer/config.py

log地址：https://github.com/xixihic/openmmlabhomework/tree/a36305eb21e57fd9d0143c9ddc726ac0d12bcdc1/MMSegmentation/Segformer/log

图片地址：https://github.com/xixihic/openmmlabhomework/tree/a36305eb21e57fd9d0143c9ddc726ac0d12bcdc1/MMSegmentation/Segformer/%E5%8E%9F%E5%9B%BE%E5%92%8C%E8%A7%86%E9%A2%91

推理地址：https://github.com/xixihic/openmmlabhomework/tree/a36305eb21e57fd9d0143c9ddc726ac0d12bcdc1/MMSegmentation/Segformer/%E6%8E%A8%E7%90%86

测试集评估结果地址：https://github.com/xixihic/openmmlabhomework/tree/a36305eb21e57fd9d0143c9ddc726ac0d12bcdc1/MMSegmentation/Segformer/%E6%B5%8B%E8%AF%95%E9%9B%86%E8%AF%84%E4%BC%B0%E7%BB%93%E6%9E%9C

本次作业不仅做了PSPNet的相关训练和测试，同样也使用了Segformer进行了训练与测试，在实验过程中，感觉Segformer比较轻量化，运行速度快，然而出现了与PSPNet相同的数据集设置的问题，暂时无法解决，总体来说两个网络可以在训练的时候跑到6、70的精度，但是当进行推理测试的时候，效果不是很好，尤其是背景比较单一（如只有整个西瓜瓤），不知道是什么地方出现的问题。
