<?xml version="1.0" encoding="UTF-8"?>
<map version="1.0.1">
<node TEXT="量化交易 · 基础概念（2026-10-05 随《黑箱》第1章）">
  <font NAME="Microsoft YaHei" SIZE="17" BOLD="true"/>
  <node TEXT="1 对冲基金（hedge fund）" POSITION="right">
    <font NAME="Microsoft YaHei" SIZE="14" BOLD="true" COLOR="#2f6fdb"/>
    <node TEXT="一句话：从有钱人和机构募钱的私募基金，目标「不管大盘涨跌都赚」（绝对收益）"/>
    <node TEXT="名字由来：1949 琼斯 —— 多低估值股 + 空高估值股，大盘涨跌被抵消，只剩选股收益"/>
    <node TEXT="四个招牌：做空 · 杠杆 · 绝对收益 · 收费 2/20"/>
    <node TEXT="在中国的身份 ≈ 私募证券投资基金（没有独立法律身份）"/>
    <node TEXT="「中等规模」≈ 管理几亿~几十亿美元资产"/>
  </node>
  <node TEXT="2 概念阶梯（基金的上游/下游）" POSITION="right">
    <font NAME="Microsoft YaHei" SIZE="14" BOLD="true" COLOR="#1f7a56"/>
    <node TEXT="上游（上位概念）">
      <node TEXT="金融：资金的融通"/>
      <node TEXT="资产管理（买方）—— 对面是卖方：投行 / 券商"/>
      <node TEXT="投资基金：集合投资 —— LP 出钱 / GP 管钱 / 托管看钱"/>
    </node>
    <node TEXT="三把刀（在「基金」这一层往下切）">
      <node TEXT="刀一 公募 / 私募：谁能买、怎么募"/>
      <node TEXT="刀二 投向：股票 · 债券 · 货币 · 混合 · 商品 · 衍生品"/>
      <node TEXT="刀三 主动 / 被动：赌跑赢 vs 抄指数（对冲基金全是主动）"/>
    </node>
    <node TEXT="下游（下位概念）：私募证券投资基金 → 对冲基金 → 量化对冲基金 → 宽客"/>
    <node TEXT="钱的上游 / 下游">
      <node TEXT="上游=钱从哪来：高净值个人 · 养老金 · 保险 · 捐赠基金 · FOF（统称 LP）"/>
      <node TEXT="下游=钱投到哪：股票 · 债券 · 期货 · 期权 · 外汇 · 商品 ＋ 两个动作：做空、加杠杆"/>
    </node>
  </node>
  <node TEXT="3 宽客（quant）" POSITION="right">
    <font NAME="Microsoft YaHei" SIZE="14" BOLD="true" COLOR="#b06f14"/>
    <node TEXT="是谁：做量化的人（quantitative + 客）"/>
    <node TEXT="干什么：把「何时买卖多少」写成模型，让电脑执行"/>
    <node TEXT="vs 主观交易员：判断在脑子里（不可检验） vs 写成模型（可回测 · 可复制 · 无情绪）"/>
    <node TEXT="三种职位：量化研究员 · 量化交易员 · 量化开发"/>
    <node TEXT="书里：约翰 = 模型的建造者与看护人；黑箱 = 他造的那台机器"/>
  </node>
  <node TEXT="4 衍生品（derivatives）" POSITION="right">
    <font NAME="Microsoft YaHei" SIZE="14" BOLD="true" COLOR="#7a3fb0"/>
    <node TEXT="定义：价格派生于「标的」的合约"/>
    <node TEXT="标的是什么：股票 · 指数 · 利率 · 汇率 · 商品"/>
    <node TEXT="四大类">
      <node TEXT="期货：交易所标准化，双方都是义务"/>
      <node TEXT="期权：买方有权利，可放弃"/>
      <node TEXT="远期：私下定制的期货"/>
      <node TEXT="互换：双方交换未来现金流"/>
    </node>
    <node TEXT="直觉：买房定金 —— 期权可反悔，期货必须认"/>
    <node TEXT="用途：对冲 / 杠杆 / 资金效率（做空大盘最干净的工具）"/>
  </node>
  <node TEXT="5 杠杆（leverage）" POSITION="right">
    <font NAME="Microsoft YaHei" SIZE="14" BOLD="true" COLOR="#c2410c"/>
    <node TEXT="定义：借来的钱，放大头寸，也放大盈亏"/>
    <node TEXT="公式：净收益率 ≈ 杠杆率 × 标的收益率 − 借钱利息"/>
    <node TEXT="10 倍例子：本金100万+借900万 → 标的涨1%＝本金+10%；标的跌10%＝本金归零（爆仓）"/>
    <node TEXT="来源：借钱 / 保证金交易 / 衍生品自带"/>
    <node TEXT="狠处：不对称 —— 标的只跌一点，本金可能先没了"/>
  </node>
  <node TEXT="6 做多 / 做空（long / short）" POSITION="right">
    <font NAME="Microsoft YaHei" SIZE="14" BOLD="true" COLOR="#0e7490"/>
    <node TEXT="做多：赌涨，先买后卖；亏有底（-100%），赚无顶"/>
    <node TEXT="做空：赌跌，先卖后买（借）；赚有顶（+100%），亏无底"/>
    <node TEXT="数学：多头盈亏 = +ΔP × 股数；空头 = −ΔP × 股数"/>
    <node TEXT="例子：茅台 1000 元 × 100 股，走一遍多、走一遍空"/>
    <node TEXT="术语：多头 · 空头 · 建仓 · 平仓 · 回补"/>
    <node TEXT="为什么需要做空：看跌也能赚 / 对冲 / 配对（多 A 空 B）"/>
  </node>
  <node TEXT="7 它们怎么咬合（关系）" POSITION="right">
    <font NAME="Microsoft YaHei" SIZE="14" BOLD="true" COLOR="#5b6472"/>
    <node TEXT="对冲基金 = 做空（消掉不想要的风险）＋ 杠杆（放大剩下的 Alpha）"/>
    <node TEXT="做空、杠杆的实现工具 → 衍生品（期货 / 期权）"/>
    <node TEXT="宽客 = 在对冲基金里把上面的东西写成模型的人"/>
    <node TEXT="黑箱 = 宽客那台机器；下一站：阿尔法模型（第3章）· 风险模型（第4章）"/>
  </node>
  <node TEXT="8 配套笔记（notes/quant/）" POSITION="right">
    <font NAME="Microsoft YaHei" SIZE="14" BOLD="true" COLOR="#8a8f99"/>
    <node TEXT="hedge_fund.md —— 对冲基金"/>
    <node TEXT="quant.md —— 宽客"/>
    <node TEXT="derivatives.md —— 衍生品"/>
    <node TEXT="leverage.md —— 杠杆"/>
    <node TEXT="long_and_short.md —— 做多与做空"/>
    <node TEXT="fund_concept_map.html —— 概念地图（图解）"/>
    <node TEXT="black_box.md —— 《黑箱》总笔记（骨架）"/>
  </node>
</node>
</map>
