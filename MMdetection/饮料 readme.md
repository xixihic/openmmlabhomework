饮料

## 数据集可视化

![](C:\Users\11139\Desktop\openmmlab\MMdetection\vis\drink.png)

## 标注可视化

![](C:\Users\11139\Desktop\openmmlab\MMdetection\vis\dtraincoco.png)

![](C:\Users\11139\Desktop\openmmlab\MMdetection\vis\dvalcoco.png)



## 性能指标

```
2023/06/10 19:31:37 - mmengine - INFO - Epoch(test) [ 5/56]    eta: 0:03:03  time: 3.5974  data_time: 2.8446  memory: 660  
2023/06/10 19:31:38 - mmengine - INFO - Epoch(test) [10/56]    eta: 0:01:27  time: 1.8995  data_time: 1.4910  memory: 65  
2023/06/10 19:31:39 - mmengine - INFO - Epoch(test) [15/56]    eta: 0:00:54  time: 1.3237  data_time: 1.0286  memory: 65  
2023/06/10 19:31:40 - mmengine - INFO - Epoch(test) [20/56]    eta: 0:00:37  time: 1.0509  data_time: 0.8120  memory: 65  
2023/06/10 19:31:41 - mmengine - INFO - Epoch(test) [25/56]    eta: 0:00:27  time: 0.8761  data_time: 0.6725  memory: 65  
2023/06/10 19:31:42 - mmengine - INFO - Epoch(test) [30/56]    eta: 0:00:19  time: 0.7649  data_time: 0.5847  memory: 65  
2023/06/10 19:31:44 - mmengine - INFO - Epoch(test) [35/56]    eta: 0:00:15  time: 0.7261  data_time: 0.5082  memory: 661  
2023/06/10 19:31:45 - mmengine - INFO - Epoch(test) [40/56]    eta: 0:00:10  time: 0.6526  data_time: 0.4535  memory: 69  
2023/06/10 19:31:46 - mmengine - INFO - Epoch(test) [45/56]    eta: 0:00:06  time: 0.6027  data_time: 0.4170  memory: 69  
2023/06/10 19:31:47 - mmengine - INFO - Epoch(test) [50/56]    eta: 0:00:03  time: 0.5570  data_time: 0.3817  memory: 69  
2023/06/10 19:31:47 - mmengine - INFO - Epoch(test) [55/56]    eta: 0:00:00  time: 0.2093  data_time: 0.1017  memory: 69  
2023/06/10 19:31:48 - mmengine - INFO - Evaluating bbox...
2023/06/10 19:31:50 - mmengine - INFO - bbox_mAP_copypaste: 0.977 0.995 0.995 -1.000 -1.000 0.977
2023/06/10 19:31:50 - mmengine - INFO - Epoch(test) [56/56]    coco/bbox_mAP: 0.9770  coco/bbox_mAP_50: 0.9950  coco/bbox_mAP_75: 0.9950  coco/bbox_mAP_s: -1.0000  coco/bbox_mAP_m: -1.0000  coco/bbox_mAP_l: 0.9770  data_time: 0.3470  time: 0.5114

```

加入tta后，性能有所增长，mAP下降0.6%左右

```
2023/06/10 19:33:26 - mmengine - INFO - Epoch(test) [ 5/56]    eta: 0:03:58  time: 4.6836  data_time: 2.4782  memory: 830  
2023/06/10 19:33:29 - mmengine - INFO - Epoch(test) [10/56]    eta: 0:01:59  time: 2.5942  data_time: 1.2397  memory: 125  
2023/06/10 19:33:31 - mmengine - INFO - Epoch(test) [15/56]    eta: 0:01:17  time: 1.8935  data_time: 0.8269  memory: 126  
2023/06/10 19:33:34 - mmengine - INFO - Epoch(test) [20/56]    eta: 0:00:55  time: 1.5546  data_time: 0.6205  memory: 125  
2023/06/10 19:33:37 - mmengine - INFO - Epoch(test) [25/56]    eta: 0:00:41  time: 1.3495  data_time: 0.4967  memory: 125  
2023/06/10 19:33:40 - mmengine - INFO - Epoch(test) [30/56]    eta: 0:00:31  time: 1.2284  data_time: 0.4149  memory: 126  
2023/06/10 19:33:43 - mmengine - INFO - Epoch(test) [35/56]    eta: 0:00:24  time: 1.1445  data_time: 0.3558  memory: 125  
2023/06/10 19:33:46 - mmengine - INFO - Epoch(test) [40/56]    eta: 0:00:17  time: 1.0692  data_time: 0.3116  memory: 126  
2023/06/10 19:33:49 - mmengine - INFO - Epoch(test) [45/56]    eta: 0:00:11  time: 1.0178  data_time: 0.2771  memory: 125  
2023/06/10 19:33:51 - mmengine - INFO - Epoch(test) [50/56]    eta: 0:00:05  time: 0.9725  data_time: 0.2496  memory: 126  
2023/06/10 19:33:54 - mmengine - INFO - Epoch(test) [55/56]    eta: 0:00:00  time: 0.5560  data_time: 0.0020  memory: 125  
2023/06/10 19:33:55 - mmengine - INFO - Evaluating bbox...
2023/06/10 19:33:56 - mmengine - INFO - bbox_mAP_copypaste: 0.971 0.993 0.993 -1.000 -1.000 0.971
2023/06/10 19:33:56 - mmengine - INFO - Epoch(test) [56/56]    coco/bbox_mAP: 0.9710  coco/bbox_mAP_50: 0.9930  coco/bbox_mAP_75: 0.9930  coco/bbox_mAP_s: -1.0000  coco/bbox_mAP_m: -1.0000  coco/bbox_mAP_l: 0.9710  data_time: 0.2231  time: 0.9231

```

## 检测结果

![](C:\Users\11139\Desktop\openmmlab\MMdetection\test2.png)

![](C:\Users\11139\Desktop\openmmlab\MMdetection\test6.png)

## 热力图展示

### 特征图可视化

BackBone

![](C:\Users\11139\Desktop\openmmlab\MMdetection\DSC_3656backone.jpg)

neck

![](C:\Users\11139\Desktop\openmmlab\MMdetection\DSC_3656neck.jpg)

### Box AM 可视化

由于未训练骨干网络，则只展示neck部分

out layers0

![](C:\Users\11139\Desktop\openmmlab\MMdetection\neck0.jpg)

out layers1

![](C:\Users\11139\Desktop\openmmlab\MMdetection\neck1.jpg)

out layers2

![](C:\Users\11139\Desktop\openmmlab\MMdetection\neck2.jpg)
