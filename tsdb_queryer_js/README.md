百度云函数计算(CFC)中查询时序数据库代码示例
===========================================

简介
----

该样例代码展示了如何在函数计算(CFC)中，通过时序数据库(TSDB)的Nodejs client，查询TSDB中的数据。查询的方式通过(event)输入传入CFC，查询到的结果增加了扁平化(避免数组)的表示，方便规则引擎、告警服务处理。

步骤
----
1，下载tsdb_queryer.zip，并且解压
2，修改index.js，替换其中的
* config.endpoint, 换成你自己TSDB的地址，例如： http://mytsdb.tsdb.iot.bj.baidubce.com
* config.credentials.ak: 替换成你的access key
* config.credentials.sk: 替换成你的secret key

3，将整个目录压缩成zip，目录格式与tsdb_queryer.zip一样，index.js在根目录。
4，创建函数计算：
* 运行语言：Nodejs
* 点击上传.ZIP文件
* 选择tsdb_queryer.zip并且点击保存

输入输出示例
------------
输入：
~~~~~
[
    {
        "metric": "RuleEngineProcess",
        "filters": {
            "start": "2 minute ago"
        },
        "aggregators": [
            {
                "name": "Sum",
                "sampling": "3 minutes"
            }
        ]
    }
]
~~~~~

输出：
~~~~~
{
    "results": [
        {
            "metric": "RuleEngineProcess",
            "field": "value",
            "groups": [
                {
                    "groupInfos": [],
                    "values": [
                        [
                            1515031594300,
                            2150985
                        ]
                    ]
                }
            ],
            "rawCount": 4808
        }
    ],
    "flatResults": {
        "count": 1,
        "result0": {
            "metric": "RuleEngineProcess",
            "field": "value",
            "rawCount": 4808,
            "groupCount": 1,
            "groups": {
                "group0": {
                    "valueCount": 1,
                    "values": {
                        "value0": {
                            "ts": 1515031594300,
                            "val": 2150985
                        }
                    }
                }
            }
        }
    }
}
~~~~~