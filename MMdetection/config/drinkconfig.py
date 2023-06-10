_base_ = '../../rtmdet/rtmdet_tiny_syncbn_fast_8xb32-300e_coco.py'

data_root = 'D:/data/Drink_284_Detection_coco/'
class_name = ('cola', 'pepsi', 'sprite', 'ice', 'scream', 'milk', 'red', 'king', 'fanta', 'spring')
num_classes = len(class_name)
metainfo = dict(classes=class_name, palette=[(20, 220, 60),(255,0,255),(0,255,0),(0,0,255),(255,0,0),(0,255,255),(255,255,0),(70,230,166),(28,128,50),(55,255,0)])

num_epochs_stage2 = 20

max_epochs = 120
train_batch_size_per_gpu = 12
train_num_workers = 4
val_batch_size_per_gpu = 1
val_num_workers = 2
randomness = dict(seed=42)
img_scale = (640, 640)

load_from = 'https://download.openmmlab.com/mmyolo/v0/rtmdet/rtmdet_tiny_syncbn_fast_8xb32-300e_coco/rtmdet_tiny_syncbn_fast_8xb32-300e_coco_20230102_140117-dbb1dc83.pth'  # noqa

model = dict(
    backbone=dict(frozen_stages=4),
    bbox_head=dict(head_module=dict(num_classes=num_classes)),
    train_cfg=dict(assigner=dict(num_classes=num_classes)))

test_pipeline = [
    dict(
        type='LoadImageFromFile',
        file_client_args=_base_.file_client_args),
    dict(type='mmdet.Resize', scale=img_scale, keep_ratio=False), # 这里将 LetterResize 修改成 mmdet.Resize
    dict(type='LoadAnnotations', with_bbox=True, _scope_='mmdet'),
    dict(
        type='mmdet.PackDetInputs',
        meta_keys=('img_id', 'img_path', 'ori_shape', 'img_shape',
                   'scale_factor'))
]

train_dataloader = dict(
    batch_size=train_batch_size_per_gpu,
    num_workers=train_num_workers,
    dataset=dict(
        data_root=data_root,
        metainfo=metainfo,
        ann_file='train_coco.json',
        data_prefix=dict(img='images/')))

val_dataloader = dict(
    batch_size=val_batch_size_per_gpu,
    num_workers=val_num_workers,
    dataset=dict(
        metainfo=metainfo,
        data_root=data_root,
        ann_file='val_coco.json',
        data_prefix=dict(img='images/'),
        pipeline=test_pipeline))

test_dataloader = val_dataloader

param_scheduler = [
    dict(
        type='LinearLR',
        start_factor=_base_.lr_start_factor,
        by_epoch=True,
        begin=0,
        end=5),
    dict(
        # use cosine lr from 150 to 300 epoch
        type='CosineAnnealingLR',
        eta_min=_base_.base_lr * 0.05,
        begin=max_epochs // 2,
        end=max_epochs,
        T_max=max_epochs // 2,
        by_epoch=True,
        convert_to_iter_based=True),
]

_base_.custom_hooks[1].switch_epoch = max_epochs - num_epochs_stage2

val_evaluator = dict(ann_file=data_root + 'val_coco.json')
test_evaluator = val_evaluator

default_hooks = dict(
    checkpoint=dict(interval=1, max_keep_ckpts=120, save_best='auto'),
    logger=dict(type='LoggerHook', interval=5))
train_cfg = dict(max_epochs=max_epochs, val_interval=1)
# visualizer = dict(vis_backends = [dict(type='LocalVisBackend'), dict(type='WandbVisBackend')]) # noqa
