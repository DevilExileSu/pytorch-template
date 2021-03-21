# pytorch-template

pytorch使用模板，简化并规范模块编写。

```bash
├── config
│   ├── cfg.py                      # 配置类， 配置文件的保存和加载
│   ├── __init__.py 			
│   └── logger.py                   # 	日志类， 打印并保存训练中相关信息以及训练结果
├── config.json                     # 	配置文件， 每个可控参数的设置
├── data                            # 数据加载模块
│   ├── dataloader.py               # 	不使用torch.nn.data
│   ├── dataset.py                  # 	借助torch.nn.data加载以及处理数据集
│   └── __init__.py
├── dataset                         # 模型所使用的训练集	
├── logs                            # 日志
│   ├── debug.log                   # 	debug日志文件: 模型调试信息 logger.debug("....")
│   └── info.log                    # 	info日志文件： 模型训练损失，评估信息 logger.info("...")
├── model                           # 该模块存放网络模型结构
│   └── base_model.py               # 	模型基类
├── saved_models                    # 保存模型
├── trainer                         # 该模块存放模型训练器
│   └── trainer.py                  # 	训练器基类
└── utils                           # 通用的函数和类模块
    ├── metrics .py                 # 	评估函数
    └── util.py                     # 	工具函数
```

### 例子

[DevilExileSu/transformer](https://github.com/DevilExileSu/transformer) 

[DevilExileSu/AGGCN](https://github.com/DevilExileSu/AGGCN)
