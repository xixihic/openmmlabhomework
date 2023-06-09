_base_ = [                                    
    '../_base_/models/resnet50.py',              
    '../_base_/default_runtime.py'            
]

dataset_type = 'CustomDataset'

model = dict(
    type='ImageClassifier',
    backbone=dict(
        type='ResNet',
        depth=50,
        num_stages=4,
        out_indices=(3, ),
        style='pytorch'),
    neck=dict(type='GlobalAveragePooling'),
    head=dict(
        type='MultiLabelLinearClsHead',
        num_classes=30,
        in_channels=2048,
        loss=dict(type='CrossEntropyLoss', loss_weight=1.0, use_soft=True),
        topk=1),
    init_cfg=dict(type='Pretrained', checkpoint="https://download.openmmlab.com/mmclassification/v0/resnet/resnetv1d50_b32x8_imagenet_20210531-db14775a.pth"),
    train_cfg=dict(augments=dict(type='Mixup', alpha=0.2)),
)


data_preprocessor = dict(
    num_classes=30,
    # RGB format normalization parameters
    mean=[123.675, 116.28, 103.53],
    std=[58.395, 57.12, 57.375],
    # convert image from BGR to RGB
    to_rgb=True,
)

train_pipeline = [
    dict(type='LoadImageFromFile'),
    dict(type='RandomResizedCrop', scale=416),
    dict(type='RandomFlip', prob=0.5, direction='horizontal'),
    dict(type='PackInputs'),
]

test_pipeline = [
    dict(type='LoadImageFromFile'),
    dict(type='ResizeEdge', scale=512, edge='short'),
    dict(type='CenterCrop', crop_size=416),
    dict(type='PackInputs'),
]

train_dataloader = dict(
    batch_size=4,
    num_workers=2,
    dataset=dict(
        type=dataset_type,
        data_root='D:/code/mmpretrain/data/fruit_train/train',
        pipeline=train_pipeline),
    sampler=dict(type='DefaultSampler', shuffle=True),
)

val_dataloader = dict(
    batch_size=2,
    num_workers=2,
    dataset=dict(
        type=dataset_type,
        data_root='D:/code/mmpretrain/data/fruit_train/val',
        pipeline=test_pipeline),
    sampler=dict(type='DefaultSampler', shuffle=False),
)
val_evaluator = dict(type='Accuracy', topk=(1,5))

test_dataloader = dict(
    batch_size=2,
    num_workers=8,
    dataset=dict(
        type=dataset_type,
        data_root='D:/code/mmpretrain/data/fruit_train/test',
        pipeline=test_pipeline),
    sampler=dict(type='DefaultSampler', shuffle=False),
)

# If you want standard test, please manually configure the test dataset
test_evaluator = val_evaluator

# optimizer
optim_wrapper = dict(
    optimizer=dict(type='SGD', lr=0.01, momentum=0.9, weight_decay=0.0001))

# learning policy
param_scheduler = dict(
    type='MultiStepLR', by_epoch=True, milestones=[10, 30, 40], gamma=0.1)

# train, val, test setting
train_cfg = dict(by_epoch=True, max_epochs=50, val_interval=5)
val_cfg = dict()
test_cfg = dict()

# NOTE: `auto_scale_lr` is for automatically scaling LR,
# based on the actual training batch size.
auto_scale_lr = dict(base_batch_size=256)