_base_ = [
    '../_base_/models/pspnet_r50-d8.py', '../_base_/datasets/homework_pipeline.py',
    '../_base_/default_runtime.py', '../_base_/schedules/schedule_40k.py'
]

norm_cfg = dict(type='BN', requires_grad=True)

crop_size = (256, 256) # 输入图像尺寸，根据自己数据集情况修改
data_preprocessor = dict(size=crop_size)
model = dict(data_preprocessor=data_preprocessor,
             backbone=dict(norm_cfg=norm_cfg),
             decode_head=dict(num_classes=7, norm_cfg=norm_cfg),
             auxiliary_head=dict(num_classes=7, norm_cfg=norm_cfg)
             )
randomness = dict(seed=42)


optimizer = dict(type='SGD', # 优化器种类，更多细节可参考 https://github.com/open-mmlab/mmengine/blob/main/mmengine/optim/optimizer/default_constructor.py
                lr=0.01,  # 优化器的学习率，参数的使用细节请参照对应的 PyTorch 文档
                momentum=0.9,  # 动量大小 (Momentum)
                weight_decay=0.0005)  # SGD 的权重衰减 (weight decay)
optim_wrapper = dict(type='OptimWrapper',  # 优化器包装器(Optimizer wrapper)为更新参数提供了一个公共接口
                    optimizer=optimizer,  # 用于更新模型参数的优化器(Optimizer)
                    clip_grad=None)  # 如果 'clip_grad' 不是None，它将是 ' torch.nn.utils.clip_grad' 的参数。
# 学习策略
param_scheduler = [
    dict(
        type='PolyLR',  # 调度流程的策略，同样支持 Step, CosineAnnealing, Cyclic 等. 请从 https://github.com/open-mmlab/mmengine/blob/main/mmengine/optim/scheduler/lr_scheduler.py 参考 LrUpdater 的细节
        eta_min=1e-4,  # 训练结束时的最小学习率
        power=0.9,  # 多项式衰减 (polynomial decay) 的幂
        begin=0,  # 开始更新参数的时间步(step)
        end=12000,  # 停止更新参数的时间步(step)
        by_epoch=False)  # 是否按照 epoch 计算训练时间
]
# 40k iteration 的训练计划
train_cfg = dict(type='IterBasedTrainLoop', max_iters=12000, val_interval=400)
val_cfg = dict(type='ValLoop')
test_cfg = dict(type='TestLoop')
# 默认钩子(hook)配置
default_hooks = dict(
    timer=dict(type='IterTimerHook'),  # 记录迭代过程中花费的时间
    logger=dict(type='LoggerHook', interval=100, log_metric_by_epoch=False),  # 从'Runner'的不同组件收集和写入日志
    param_scheduler=dict(type='ParamSchedulerHook'),  # 更新优化器中的一些超参数，例如学习率
    checkpoint=dict(type='CheckpointHook', by_epoch=False, interval=400),  # 定期保存检查点(checkpoint)
    sampler_seed=dict(type='DistSamplerSeedHook'))  # 用于分布式训练的数据加载采样器