Balloon

## 数据集可视化

![](C:\Users\11139\Desktop\openmmlab\MMdetection\vis\traindataset.png)

![](C:\Users\11139\Desktop\openmmlab\MMdetection\vis\valdataset.png)

## 标签可视化

![](C:\Users\11139\Desktop\openmmlab\MMdetection\vis\trainanno.png)

![](C:\Users\11139\Desktop\openmmlab\MMdetection\vis\valcoco.png)



## 性能指标

```
2023/06/10 14:33:15 - mmengine - INFO - Epoch(test) [ 5/13]    eta: 0:00:21  time: 2.7333  data_time: 1.9610  memory: 665  
2023/06/10 14:33:16 - mmengine - INFO - Epoch(test) [10/13]    eta: 0:00:04  time: 1.3958  data_time: 0.9807  memory: 78  
2023/06/10 14:33:16 - mmengine - INFO - Evaluating bbox...
2023/06/10 14:33:16 - mmengine - INFO - bbox_mAP_copypaste: 0.656 0.810 0.731 0.000 0.376 0.788
2023/06/10 14:33:16 - mmengine - INFO - Epoch(test) [13/13]    coco/bbox_mAP: 0.6560  coco/bbox_mAP_50: 0.8100  coco/bbox_mAP_75: 0.7310  coco/bbox_mAP_s: 0.0000  coco/bbox_mAP_m: 0.3760  coco/bbox_mAP_l: 0.7880  data_time: 0.7545  time: 1.0874
```

加入tta后，性能有所增长，mAP增加4%左右

```
2023/06/10 15:14:27 - mmengine - INFO - Epoch(test) [ 5/13]    eta: 0:00:31  time: 3.9333  data_time: 2.0411  memory: 829  
2023/06/10 15:14:29 - mmengine - INFO - Epoch(test) [10/13]    eta: 0:00:06  time: 2.1489  data_time: 1.0211  memory: 123  
2023/06/10 15:14:31 - mmengine - INFO - Evaluating bbox...
2023/06/10 15:14:31 - mmengine - INFO - bbox_mAP_copypaste: 0.695 0.854 0.794 0.017 0.623 0.754
2023/06/10 15:14:31 - mmengine - INFO - Epoch(test) [13/13]    coco/bbox_mAP: 0.6950  coco/bbox_mAP_50: 0.8540  coco/bbox_mAP_75: 0.7940  coco/bbox_mAP_s: 0.0170  coco/bbox_mAP_m: 0.6230  coco/bbox_mAP_l: 0.7540  data_time: 0.7858  time: 1.7379
```



## 检测结果

![](C:\Users\11139\Desktop\openmmlab\MMdetection\test.png)

![](C:\Users\11139\Desktop\openmmlab\MMdetection\test1.png)

## 热力图展示

### 特征图可视化

BackBone

![](C:\Users\11139\Desktop\openmmlab\MMdetection\balloonbackbone.png)

Neck

![](C:\Users\11139\Desktop\openmmlab\MMdetection\balloonneck.png)

### Box AM 可视化

由于在训练过程中进行冻结权重，所以在可视化时报错，在解除冻结权重后，可视化正常运行

未冻结的Neck部分可视化

out layers0

![](C:\Users\11139\Desktop\openmmlab\MMdetection\balloonstage0.png)

out layers1

![](C:\Users\11139\Desktop\openmmlab\MMdetection\balloonstage1.png)

out layers2

![](C:\Users\11139\Desktop\openmmlab\MMdetection\balloonstage2.png)

