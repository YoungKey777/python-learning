# 策略（strategy）

> 整理于 2026-10-05，随《黑箱》第1章阅读。标准定义引自 Investopedia（链接见文末）。

## 最标准的定义

> **A strategy is a set of objective, absolute rules defining when a trader will take action.**
> 策略 = 一套**客观、明确的规则**，规定交易者在什么条件下采取什么行动。

每个词都是判据：

- **rules（规则）**——不是想法、不是感觉、不是"看情况"。判据：**换一个人、换一台机器来执行，动作完全一样**；
- **objective（客观）**——不含"我觉得要涨"这类主观判断；
- **when → action**——必须回答"**什么条件 → 做什么**"这个映射。

## 一套完整的策略要回答五个问题

1. **什么时候进**——什么条件算机会
2. **买卖什么**——标的
3. **买多少**——头寸规模、资金管理
4. **什么时候走**——止盈 / 止损 / 换仓条件
5. **怎么下单**——订单类型与执行方式

少一个都是半成品。

## 理工科版表述

策略就是一个函数：

**f（当前能拿到的全部信息）→ 交易动作（买 / 卖 / 持有，多少）**

同一份信息喂进去，永远吐出同样的动作。正因为它确定、无歧义，才能写进代码（量化）、才能用历史数据检验（回测）。

## 三个术语的边界

| 术语 | 是什么 |
|---|---|
| **信号** signal | 此刻"该看不该多"的即时判断（模型的输出） |
| **模型** model | 产生信号的那套数学（回归、机器学习……） |
| **策略** strategy | 完整规则包 = 信号 + 头寸规则 + 出场规则 + 执行方式；内含一个或多个模型 |

常被引用的判词：**"指标不是策略"**——均线、MACD 只是零件，好比比较函数不是排序程序。业内说"我们跑一个策略"，指的是整套东西。

## 回到书里

- 约翰"创建量化策略"＝把市场判断写成规则、塞进模型、交给机器执行；
- "策略的稳健性"＝这套规则换个市场环境还灵不灵；
- 宽泛语境里"策略"也指打法大类：趋势跟随、均值回复……（第 3 章逐个展开）。

---

来源：[Investopedia · Using Technical Indicators to Develop Trading Strategies](https://www.investopedia.com/articles/trading/11/indicators-and-strategies-explained.asp)｜[How to Create Your Own Trading Strategies](https://www.investopedia.com/articles/trading/10/create-trading-strategies.asp)｜[Systematic Trading Explained](https://damanmarkets.academy/glossary-item/systematic-trading/)

相关：[[quant]]（宽客）｜[[black_box]]（《黑箱》笔记）｜[[fund_concept_map]]（概念地图）
