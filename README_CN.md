# Agent 安全论文精选

> AI Agent 安全研究论文精选集——涵盖攻击对抗、防御对齐、安全测评与 Agent 安全架构。共 **1799 篇** arXiv 论文（2024-09 ~ 2026-04），按质量评分排序。

[English](README.md) · [**中文**](README_CN.md)

## 目录

- [统计](#统计)
- [分类](#分类)
- [评分方法](#评分方法)
- [Top 100 论文](#top-100-论文)
  - [⚔️ 攻击与对抗](#attacks-adversaries)
  - [🛡️ 防御与对齐](#defense-alignment)
  - [📊 安全测评](#security-evaluation)
  - [🏗️ Agent安全架构](#agent-security-architecture)
  - [📄 其他](#other-topics)

## 统计

| 指标 | 值 |
|------|-----|
| 论文总数 | 1799 |
| 日期范围 | 2024-09 ~ 2026-04 |
| 评分范围 | 5.08 ~ 9.45（均值 6.35） |

## 分类

| # | 分类 | 篇数 | 完整列表 |
|---|------|------|----------|
| 1 | ⚔️ Attacks & Adversaries（攻击与对抗） | 586 | [查看全部](docs/attacks_adversaries.md) |
| 2 | 🛡️ Defense & Alignment（防御与对齐） | 502 | [查看全部](docs/defense_alignment.md) |
| 3 | 📊 Security Evaluation（安全测评） | 385 | [查看全部](docs/security_evaluation.md) |
| 4 | 🏗️ Agent Security Architecture（Agent安全架构） | 211 | [查看全部](docs/agent_security_architecture.md) |
| 5 | 📄 Other Topics（其他） | 115 | [查看全部](docs/other_topics.md) |

## 评分方法

每篇论文基于 [Semantic Scholar](https://www.semanticscholar.org/) 数据，使用加权公式计算综合评分：

| 维度 | 权重 | 说明 |
|------|------|------|
| 月均引用 | 50% | 引用数按发表时间归一化 |
| 高影响力引用 | 10% | 高影响力引用数 |
| 发表会议质量 | 10% | 顶会=10，普通会议=5，预印本=2 |
| 作者质量 | 20% | 最高作者 h-index |
| 时效性 | 10% | ≤3月=10，≤6月=9，≤12月=7，>12月=5 |

## Top 100 论文

从 1799 篇论文中选出评分最高的 100 篇（2024-09-24 ~ 2026-04-09），按类别分组展示。

### ⚔️ Attacks & Adversaries（攻击与对抗）

**#3** [Persistent Pre-Training Poisoning of LLMs](https://arxiv.org/abs/2410.13722)  
*Yiming Zhang, Javier Rando, Ivan Evtimov 等 8 人*  
评分: 9.36 · 2024-10-17

> 本文首次评估了语言模型在预训练阶段被投毒的风险，并研究了这些攻击在经过安全微调（SFT）和直接偏好优化（DPO）后的持久性。通过从头预训练一系列LLM，研究发现仅需污染0.1%的预训练数据，就足以使三种攻击目标在后续训练中持续存在，揭示了预训练阶段严重的安全隐患。
<br>

**#9** [SOM Directions are Better than One: Multi-Directional Refusal Suppression in Language Models](https://arxiv.org/abs/2511.08379)  
*Giorgio Piras, Raffaele Mura, Fabio Brau 等 6 人*  
评分: 9.11 · 2025-11-11

> 本文提出了一种利用自组织映射（SOM）提取语言模型中多个拒绝方向的新方法，以改进对拒绝行为的理解。作者证明了SOM概括了先前的均值差技术，并通过从有害神经元中减去无害表示质心，推导出一组表达拒绝概念的方向。实验表明，消融多个方向在抑制拒绝方面优于单一方向基线和专门的越狱算法，揭示了拒绝机制的低维流形特性。
<br>

**#13** [Emoji Attack: Enhancing Jailbreak Attacks Against Judge LLM Detection](https://arxiv.org/abs/2411.01077)  
*Zhipeng Wei, Yuqi Liu, N. Benjamin Erichson*  
评分: 9.01 · 2024-11-01

> 本文揭示了 Judge LLM 容易受到 token 分割偏差的影响，即分隔符会改变分词过程从而降低检测准确性。作者提出了 Emoji Attack，一种利用上下文学习在文本中系统性插入表情符号的新策略，通过引入语义歧义和嵌入失真来显著降低 Judge LLM 检测不安全内容的可能性。实验表明，该攻击能有效地绕过现有的安全防护机制，使有害内容被误判为安全。
<br>

**#15** [AdvWave: Stealthy Adversarial Jailbreak Attack against Large Audio-Language Models](https://arxiv.org/abs/2412.08608)  
*Mintong Kang, Chejian Xu, Bo Li*  
评分: 9.00 · 2024-12-11

> 本文提出了AdvWave，首个针对大型音频语言模型（LALM）的隐蔽性越狱攻击框架。针对音频编码器导致的梯度破碎问题，该方法采用双阶段优化策略实现端到端攻击，并利用自适应对抗目标搜索算法应对模型行为变化。实验验证了AdvWave在生成隐蔽对抗音频波形方面的有效性。
<br>

**#23** [Jailbreak-Tuning: Models Efficiently Learn Jailbreak Susceptibility](https://arxiv.org/abs/2507.11630)  
*Brendan Murphy, Dillon Bowen, Shahrad Mohammadzadeh 等 7 人*  
评分: 8.86 · 2025-07-15

> 本文证明，微调可产生有用模型但安全措施被破坏。作者的越狱微调方法教导模型对任意有害请求生成详细、高质量响应，例如OpenAI、Google和Anthropic模型将完全遵守CBRN援助和网络攻击等请求。研究显示后门可增加攻击的隐蔽性和严重性，更强的越狱提示在微调攻击中更有效，连接了攻击和防御。研究指出不仅当前模型脆弱，较新模型似乎也变得更脆弱，强调了防篡改护栏的迫切需求。在发现此类护栏前，公司和政策制定者应将任何可微调模型的发布视为同时发布其邪恶双胞胎。
<br>

**#24** [The Attacker Moves Second: Stronger Adaptive Attacks Bypass Defenses Against Llm Jailbreaks and Prompt Injections](https://arxiv.org/abs/2510.09023)  
*Milad Nasr, Nicholas Carlini, Chawin Sitawarin 等 14 人*  
评分: 8.86 · 2025-10-10

> 批评了当前针对越狱和提示注入防御的评估方法存在缺陷，未能充分考虑自适应攻击者。通过系统调整梯度下降、强化学习等优化技术，作者成功绕过了12种最新的防御机制，攻击成功率超过90%。研究强调未来的防御工作必须针对更强的自适应攻击进行评估。
<br>

**#25** [Visual Contextual Attack: Jailbreaking MLLMs with Image-Driven Context Injection](https://arxiv.org/abs/2507.02844)  
*Ziqi Miao, Yi Ding, Lijun Li 等 4 人*  
评分: 8.85 · 2025-07-03

> 本文提出了一种针对多模态大语言模型的视觉上下文攻击，定义了视觉信息作为构建完整越狱场景必要组件的新设置。VisCo攻击通过四种视觉策略伪造上下文对话，动态生成辅助图像以构建逼真的越狱场景，并结合毒性混淆和语义优化技术。实验表明，该方法在黑盒MLLM上实现了极高的攻击成功率，显著优于基线方法。
<br>

**#47** [Adjacent Words, Divergent Intents: Jailbreaking Large Language Models via Task Concurrency](https://arxiv.org/abs/2510.21189)  
*Yukun Jiang, Mingjie Li, Michael Backes 等 4 人*  
评分: 8.60 · 2025-10-24

> 本文提出了JAIL-CON，一种利用任务并发机制的大语言模型越狱攻击框架。该方法通过在相邻单词中编码不同意图，将有害任务与良性任务结合，显著降低了被安全护栏过滤的概率。实验表明，相比现有的顺序攻击，JAIL-CON不仅具有更强的攻击能力，还表现出更高的隐蔽性和有效性。
<br>

**#50** [NEXUS: Network Exploration for eXploiting Unsafe Sequences in Multi-Turn LLM Jailbreaks](https://arxiv.org/abs/2510.03417)  
*Javad Rafiei Asl, Sidhant Narula, Mohammad Ghasemigol 等 5 人*  
评分: 8.57 · 2025-10-03

> 本文提出了NEXUS框架，用于构建、细化和执行优化的多轮越狱攻击，旨在解决现有方法在对抗空间探索上的不足。该框架包含将恶意意图扩展为语义网络的ThoughtNet、反馈驱动的Simulator以及自适应导航的Network Traverser。实验表明，NEXUS在多种闭源和开源LLM上显著提高了攻击成功率，发现了隐蔽且高效的对抗路径。
<br>

**#53** [Towards Understanding the Fragility of Multilingual LLMs against Fine-Tuning Attacks](https://arxiv.org/abs/2410.18210)  
*Samuele Poppi, Zheng-Xin Yong, Yifei He 等 7 人*  
评分: 8.55 · 2024-10-23

> 本文深入研究了多语言大语言模型在微调攻击下的脆弱性，发现使用一种语言的对抗性示例可以破坏模型在所有语言上的安全对齐。作者提出了安全信息定位（SIL）方法来识别模型参数空间中的安全相关信息，并验证了安全信息是语言无关的假设。研究结果表明，仅改变少量权重参数即可破坏跨语言的安全对齐。
<br>

**#54** [Best-of-N Jailbreaking](https://arxiv.org/abs/2412.03556)  
*John Hughes, Sara Price, Aengus Lynch 等 10 人*  
评分: 8.55 · 2024-12-04

> 本文介绍了Best-of-N（BoN）越狱算法，一种简单的黑盒攻击方法，适用于多种模态的前沿AI系统。BoN通过对提示词进行随机打乱或大小写转换等增强处理并重复采样，成功绕过了包括GPT-4o和Claude 3.5在内的最先进防御，揭示了模型对输入微小变化的敏感性。
<br>

**#70** [JANUS: A Lightweight Framework for Jailbreaking Text-to-Image Models via Distribution Optimization](https://arxiv.org/abs/2603.21208)  
*Haolun Zheng, Yu He, Tailun Chen 等 9 人*  
评分: 8.43 · 2026-03-22

> 本文提出了 JANUS，一个轻量级框架，通过在黑盒端到端奖励下优化结构化提示分布，对文生图（T2I）模型进行越狱攻击。JANUS 使用低维混合策略替代高容量生成器，在保持目标语义的同时实现高效探索。在现代 T2I 模型上的实验表明，JANUS 优于最先进的越狱方法，显著提高了 Stable Diffusion 等模型的攻击成功率，并暴露了当前 T2I 安全管道的结构性弱点。
<br>

**#72** [Align is not Enough: Multimodal Universal Jailbreak Attack against Multimodal Large Language Models](https://arxiv.org/abs/2506.01307)  
*Youze Wang, Wenbo Hu, Yinpeng Dong 等 6 人*  
评分: 8.41 · 2025-06-02

> 提出了一种统一的多模态通用越狱攻击框架，利用迭代图像-文本交互和迁移策略生成对抗性后缀与图像。研究表明，多模态交互存在关键安全漏洞，该攻击能诱导多种多模态大模型生成高质量的有害内容，暴露了现有安全机制的不足。
<br>

**#76** [MUSE: MCTS-Driven Red Teaming Framework for Enhanced Multi-Turn Dialogue Safety in Large Language Models](https://arxiv.org/abs/2509.14651)  
*Siyu Yan, Long Zeng, Xuecheng Wu 等 9 人*  
评分: 8.39 · 2025-09-18

> MUSE是一个综合框架，通过攻击和防御两个角度解决大型语言模型中的多轮越狱问题。攻击方面，MUSE-A利用框架语义和启发式树搜索探索多样化的语义轨迹；防御方面，MUSE-D通过细粒度的安全对齐在对话早期进行干预以减少漏洞。
<br>

**#79** [How Vulnerable Are AI Agents to Indirect Prompt Injections? Insights from a Large-Scale Public Competition](https://arxiv.org/abs/2603.15714)  
*Mateusz Dziemian, Maxwell Lin, Xiaohan Fu 等 31 人*  
评分: 8.38 · 2026-03-16

> 本文通过大规模红队测试竞赛，深入评估了AI Agent对间接提示注入攻击的脆弱性，特别关注攻击在最终响应中隐蔽存在的威胁。研究发现所有前沿模型均存在漏洞，攻击者可利用通用策略在用户无察觉的情况下执行有害操作。该研究揭示了指令遵循架构的根本性弱点，强调了评估攻击隐蔽性的必要性。
<br>

**#95** [Differentiated Directional Intervention A Framework for Evading LLM Safety Alignment](https://arxiv.org/abs/2511.06852)  
*Peng Zhang, Peijie Sun*  
评分: 8.29 · 2025-11-10

> 本文提出了DBDI（差异化双向干预），一种新的白盒框架，用于精确中和大语言模型的关键层安全对齐机制。该研究将拒绝机制解构为“伤害检测方向”和“拒绝执行方向”，通过自适应投影消除和直接抑制来绕过安全防御。实验证明，DBDI在Llama-2等模型上实现了高达97.88%的攻击成功率，为深入理解LLM安全对齐提供了更细粒度的机制框架。
<br>

**#96** [RAT: Adversarial Attacks on Deep Reinforcement Agents for Targeted Behaviors](https://arxiv.org/abs/2412.10713)  
*Fengshuo Bai, Runze Liu, Yali Du 等 5 人*  
评分: 8.29 · 2024-12-14

> 本文提出了RAT，一种针对深度强化学习智能体的通用定向行为攻击方法。不同于以往仅关注降低奖励的策略，RAT通过训练符合人类偏好的意图策略并动态调整状态占用度量，诱导受害者执行符合攻击者目标的特定行为。实验证明该方法在机器人仿真任务中能有效诱导特定行为并提升智能体鲁棒性。
<br>

**#99** [Chain-of-Thought Hijacking](https://arxiv.org/abs/2510.26418)  
*Jianli Zhao, Tingchen Fu, Rylan Schaeffer 等 5 人*  
评分: 8.27 · 2025-10-30

> 本文提出了“思维链劫持”攻击，揭示了大型推理模型中长推理序列反而会削弱安全性的漏洞。该攻击通过在有害指令前添加长序列的良性谜题推理，成功绕过了多个主流模型的安全防御，实现了极高的攻击成功率。通过激活探测和因果干预分析，作者发现拒绝机制依赖于低维安全信号，该信号会随着推理长度增加而被稀释，导致模型无法正确拒绝有害请求。
<br>

---

### 🛡️ Defense & Alignment（防御与对齐）

**#5** [InfAlign: Inference-aware language model alignment](https://arxiv.org/abs/2412.19792)  
*Ananth Balashankar, Ziteng Sun, Jonathan Berant 等 12 人*  
评分: 9.17 · 2024-12-27

> 针对标准RLHF在推理时算法（如Best-of-N）下的次优性，本文提出了InfAlign框架。该框架旨在优化推理时的胜率，通过校准和转换奖励函数，提出了InfAlign-CTRL算法，在Best-of-N采样和越狱防御场景中实现了显著的性能提升，解决了训练与测试不匹配的问题。
<br>

**#6** [Instructional Segment Embedding: Improving LLM Safety with Instruction Hierarchy](https://arxiv.org/abs/2410.09102)  
*Tong Wu, Shujian Zhang, Kaiqiang Song 等 10 人*  
评分: 9.16 · 2024-10-09

> 本文针对LLM缺乏指令层次结构导致的安全漏洞，提出了指令段嵌入（ISE）技术。该技术受BERT启发，将指令优先级信息直接嵌入模型架构中，使模型能够明确区分和优先处理系统消息、用户提示等不同类型的指令。实验表明，ISE显著提高了模型对抗恶意提示的鲁棒性，平均将鲁棒准确率提高了约15-18%，同时增强了指令遵循能力。
<br>

**#8** [Trustworthy AI-Driven Dynamic Hybrid RIS: Joint Optimization and Reward Poisoning-Resilient Control in Cognitive MISO Networks](https://arxiv.org/abs/2604.01238)  
*Deemah H. Tashman, Soumaya Cherkaoui*  
评分: 9.12 · 2026-03-27

> 本文研究了认知无线电网络中基于AI驱动的动态混合可重构智能表面（RIS）的联合优化与安全控制问题。工作引入了自适应混合RIS架构，并利用软演员-评论家（SAC）深度强化学习方法解决波束成形和相位优化问题。此外，文章首次系统研究了RIS增强网络中DRL智能体的奖励投毒攻击，并提出了基于奖励裁剪和统计异常过滤的轻量级实时防御机制，数值结果验证了该方法的有效性。
<br>

**#10** [Robust LLM safeguarding via refusal feature adversarial training](https://arxiv.org/abs/2409.20089)  
*Lei Yu, Virginie Do, Karen Hambardzumyan 等 4 人*  
评分: 9.11 · 2024-09-30

> 本文揭示了对抗性攻击通过消除残差流嵌入空间中的“拒绝特征”来绕过LLM安全机制的通用原理。基于此发现，作者提出了拒绝特征对抗训练（ReFAT）算法，通过模拟拒绝特征消除的效果高效执行对抗训练，显著提升了模型鲁棒性且计算开销更低。
<br>

**#14** [HarmAug: Effective Data Augmentation for Knowledge Distillation of Safety Guard Models](https://arxiv.org/abs/2410.01524)  
*Seanie Lee, Haebin Seong, Dong Bok Lee 等 9 人*  
评分: 9.00 · 2024-10-02

> 本文提出了HarmAug，一种有效的数据增强方法，用于将大型教师安全护栏模型蒸馏为适合移动设备的小型模型。该方法通过越狱LLM生成有害指令并利用教师模型进行标注，解决了现有标注数据多样性有限的问题，显著提升了小型安全模型的性能。
<br>

**#17** [When Machine Unlearning Meets Retrieval-Augmented Generation (RAG): Keep Secret or Forget Knowledge?](https://arxiv.org/abs/2410.15267)  
*Shang Wang, Tianqing Zhu, Dayong Ye 等 4 人*  
评分: 8.94 · 2024-10-20

> 针对现有机器遗忘方法计算需求高或适用性有限的问题，本文提出了一种基于检索增强生成（RAG）的轻量级行为遗忘框架。该方法通过修改RAG的外部知识库来模拟遗忘效果，将遗忘知识的构建视为约束优化问题，在闭源和开源模型上均验证了其有效性和无害性。
<br>

**#34** [BlueSuffix: Reinforced Blue Teaming for Vision-Language Models Against Jailbreak Attacks](https://arxiv.org/abs/2410.20971)  
*Yunhan Zhao, Xiang Zheng, Lin Luo 等 6 人*  
评分: 8.77 · 2024-10-28

> 本文提出了 BlueSuffix，一种针对视觉语言模型越狱攻击的黑盒防御方法。该方法包含视觉净化器、文本净化器以及使用强化微调的蓝队后缀生成器三个关键组件，旨在增强跨模态鲁棒性。在四个 VLM 和四个安全基准上的实验表明，BlueSuffix 显著优于基线防御方法，且不损害模型在良性输入上的性能。
<br>

**#35** [Separate the Wheat from the Chaff: A Post-Hoc Approach to Safety Re-Alignment for Fine-Tuned Language Models](https://arxiv.org/abs/2412.11041)  
*Di Wu, Xin Lu, Yanyan Zhao 等 4 人*  
评分: 8.75 · 2024-12-15

> 本文提出了 IRR 方法，旨在解决微调过程往往会破坏 LLM 安全对齐的问题。该方法通过识别并移除微调模型中的不安全 delta 参数，同时重新校准保留的参数，实现事后安全重新对齐。实验表明，IRR 在保持下游任务性能的同时，显著提升了模型在有害查询和越狱攻击等安全基准上的表现，有效恢复了微调后的安全性。
<br>

**#36** [Jailbreak Antidote: Runtime Safety-Utility Balance via Sparse Representation Adjustment in Large Language Models](https://arxiv.org/abs/2410.02298)  
*Guobin Shen, Dongcheng Zhao, Yiting Dong 等 5 人*  
评分: 8.74 · 2024-10-03

> 本研究提出了一种名为“越狱解毒剂”的方法，通过在推理过程中操纵模型内部状态的稀疏子集，实时调整大语言模型的安全偏好。该方法通过沿安全方向移动模型的隐藏表示，实现了对安全-效用平衡的灵活控制，且无需额外的 token 开销或推理延迟。实验验证了该方法在多种 LLM 上对抗越狱攻击的有效性和高效性。
<br>

**#38** [LLM Jailbreak Detection for (Almost) Free!](https://arxiv.org/abs/2509.14558)  
*Guorui Chen, Yifan Xia, Xiaojun Jia 等 6 人*  
评分: 8.68 · 2025-09-18

> 本文提出了一种几乎零计算成本的越狱检测方法（FJD），利用越狱提示词与良性提示词在输出分布上的差异进行检测。该方法通过在输入前添加肯定指令并调整温度缩放，结合虚拟指令学习，有效区分恶意提示词，且不增加额外的推理开销。
<br>

**#42** [RobustKV: Defending Large Language Models against Jailbreak Attacks via KV Eviction](https://arxiv.org/abs/2410.19937)  
*Tanqiu Jiang, Zian Wang, Jiacheng Liang 等 6 人*  
评分: 8.63 · 2024-10-25

> 本文提出了 RobustKV，一种通过从键值（KV）缓存中有选择地移除有害查询的关键 token 来防御越狱攻击的新方法。该方法基于越狱提示词会降低隐藏有害查询 token 重要性的直觉，通过策略性地驱逐低排名 token 的 KV 来防止恶意响应的生成。实验表明，RobustKV 在有效对抗最先进越狱攻击的同时，保持了 LLM 在良性查询上的通用性能。
<br>

**#46** [Analysing the Safety Pitfalls of Steering Vectors](https://arxiv.org/abs/2603.24543)  
*Yuxiao Li, Alina Fastowski, Efstratios Zaradoukas 等 5 人*  
评分: 8.61 · 2026-03-25

> 本文系统性地审计了广泛使用的激活引导方法（CAA）在安全性方面的隐患，评估了引导向量对越狱攻击成功率的影响。研究发现，引导向量会显著改变模型的攻击成功率，根据目标行为的不同，可能大幅增加或降低成功率，这归因于引导向量与拒绝行为潜在方向的重叠。这一发现揭示了LLM中可控性与安全性之间的权衡，强调了在行为引导技术中考虑安全因素的必要性。
<br>

**#52** [Oyster-I: Beyond Refusal -- Constructive Safety Alignment for Responsible Language Models](https://arxiv.org/abs/2509.01909)  
*Ranjie Duan, Jiexi Liu, Xiaojun Jia 等 30 人*  
评分: 8.56 · 2025-09-02

> 本文提出了建设性安全对齐（CSA）范式，旨在超越传统的拒绝机制，主动引导处于心理困境的用户走向安全。Oyster-I模型通过博弈论预测用户反应并结合细粒度风险边界发现，在保持高通用能力的同时，实现了对恶意攻击的防御和对脆弱用户的积极引导。
<br>

**#56** [The Assistant Axis: Situating and Stabilizing the Default Persona of Language Models](https://arxiv.org/abs/2601.10387)  
*Christina Lu, Jack Gallagher, Jonathan Michala 等 5 人*  
评分: 8.54 · 2026-01-15

> 本文发现了模型角色空间中的“助手轴”，并证明限制该轴上的激活可以稳定模型行为，防止有害的角色漂移。该方法通过操纵内部激活方向，有效防御了基于角色的越狱攻击，为理解和控制模型默认行为提供了新视角。
<br>

**#57** [Immune: Improving Safety Against Jailbreaks in Multi-modal LLMs via Inference-Time Alignment](https://arxiv.org/abs/2411.18688)  
*Soumya Suvra Ghosal, Souradip Chakraborty, Vaibhav Singh 等 10 人*  
评分: 8.54 · 2024-11-27

> 本文提出了Immune，一种针对多模态大语言模型的推理时防御框架，利用安全奖励模型通过控制解码来防御越狱攻击。该框架通过数学分析证明了其有效性，并在多种越狱基准测试中显著降低了攻击成功率，同时保持了模型的原始能力。
<br>

**#59** [Building a Foundational Guardrail for General Agentic Systems via Synthetic Data](https://arxiv.org/abs/2510.09781)  
*Yue Huang, Hang Hua, Yujun Zhou 等 14 人*  
评分: 8.52 · 2025-10-10

> 本文针对Agent执行前规划阶段的安全干预，提出了AuraGen合成数据引擎和Safiron基础护栏模型。该框架通过合成良性轨迹和注入风险数据来训练护栏，使其能够在执行前检测风险、分配类型并生成理由。实验表明，该方法在涵盖多种工具和分支轨迹的基准测试中表现出一致的性能提升。
<br>

**#61** [Defending Against Prompt Injection with DataFilter](https://arxiv.org/abs/2510.19207)  
*Yizhu Wang, Sizhe Chen, Raghad Alkhudair 等 5 人*  
评分: 8.51 · 2025-10-22

> 本文提出了DataFilter，一种测试时且与模型无关的防御方法，用于在数据到达后端大语言模型之前移除恶意指令。DataFilter通过在模拟注入数据上进行监督微调，能够选择性地剥离对抗性内容，在将提示注入攻击成功率降至接近零的同时，有效保持了模型的原始效用。
<br>

**#62** [AgentDoG: A Diagnostic Guardrail Framework for AI Agent Safety and Security](https://arxiv.org/abs/2601.18491)  
*Dongrui Liu, Qihan Ren, Chen Qian 等 43 人*  
评分: 8.49 · 2026-01-26

> 本文提出了AgentDoG，一个用于AI Agent安全和保障的诊断护栏框架，旨在解决现有护栏模型缺乏Agent风险感知和透明度的问题。基于统一的三维风险分类法，AgentDoG能够对Agent轨迹进行细粒度监控，并诊断不安全行为的根本原因，提供超越二元标签的可追溯性。实验表明，该框架在复杂交互场景中实现了最先进的Agent安全审核性能。
<br>

**#65** [WebGuard: Building a Generalizable Guardrail for Web Agents](https://arxiv.org/abs/2507.14293)  
*Boyuan Zheng, Zeyi Liao, Scott Salisbury 等 11 人*  
评分: 8.46 · 2025-07-18

> 本文介绍了WebGuard，第一个全面的数据集，用于评估网络智能体行动风险并开发真实在线环境护栏。该数据集包含来自22个不同领域193个网站的4,939个人类标注行动，使用三层风险模式(安全、低风险、高风险)分类。实验显示，前沿LLM在预测行动结果准确率不足60%，高风险行动召回率不足60%，突显了缺乏专用护栏的风险。作者通过WebGuard微调专用护栏模型，在多种泛化设置下评估，发现微调的Qwen2.5VL-7B模型显著提高了性能。
<br>

**#67** [Online Learning Defense against Iterative Jailbreak Attacks via Prompt Optimization](https://arxiv.org/abs/2510.17006)  
*Masahiro Kaneko, Zeerak Talat, Timothy Baldwin*  
评分: 8.44 · 2025-10-19

> 该研究提出了一种基于在线学习的防御框架，通过动态更新防御策略来对抗迭代越狱攻击。利用强化学习优化提示词，并引入 Past-Direction Gradient Damping 抑制过拟合，该方法在有效拒绝有害提示的同时，显著提升了对无害任务的响应质量。
<br>

**#68** [LLMZ+: Contextual Prompt Whitelist Principles for Agentic LLMs](https://arxiv.org/abs/2509.18557)  
*Tom Pawelek, Raj Patel, Charlotte Crowell 等 7 人*  
评分: 8.43 · 2025-09-23

> 针对智能体大语言模型面临的安全风险，本文提出了LLMZ+防御框架。不同于传统的恶意意图检测方法，LLMZ+实施基于上下文的提示白名单机制，仅允许符合预定义用例的安全消息与模型交互。该方法简化了安全框架，增强了长期韧性，并有效抵御了常见的越狱攻击。
<br>

**#80** [Token Highlighter: Inspecting and Mitigating Jailbreak Prompts for Large Language Models](https://arxiv.org/abs/2412.18171)  
*Xiaomeng Hu, Pin-Yu Chen, Tsung-Yi Ho*  
评分: 8.38 · 2024-12-24

> 针对大语言模型的越狱攻击，本文提出了Token Highlighter防御方法。该方法引入“肯定损失”来衡量模型回答意愿，利用梯度定位关键攻击Token，并通过“软移除”技术缩小其嵌入表示，从而在不影响良性问题性能的前提下有效防御多种越狱攻击，且具有低成本和可解释性。
<br>

**#82** [Large Reasoning Models Learn Better Alignment from Flawed Thinking](https://arxiv.org/abs/2510.00938)  
*ShengYun Peng, Eric Smith, Ivan Evtimov 等 10 人*  
评分: 8.36 · 2025-10-01

> 大型推理模型在生成思维链时容易受到有缺陷前提的影响，缺乏对安全对齐的批判性推理能力。本文提出了 RECAP 方法，通过混合合成生成的反对抗思维链预填充和标准提示，显式地教导模型覆盖有缺陷的推理轨迹并重新路由至安全有益的响应。该方法在不增加额外训练成本的情况下，显著提升了模型的安全性和越狱鲁棒性，同时减少了过度拒绝并保留了核心推理能力。
<br>

**#84** [Proof-of-Guardrail in AI Agents and What (Not) to Trust from It](https://arxiv.org/abs/2603.05786)  
*Xisen Jin, Michael Duan, Qin Lin 等 7 人*  
评分: 8.34 · 2026-03-06

> 本文提出了proof-of-guardrail系统，利用可信执行环境（TEE）生成密码学证明，验证Agent响应是在特定开源护栏执行后生成的。该系统在保证护栏执行完整性的同时保护了开发者隐私，但也指出了恶意开发者可能主动破坏护栏的欺骗风险，为验证安全声明提供了新思路。
<br>

**#90** [Large Language Models Encode Semantics and Alignment in Linearly Separable Representations](https://arxiv.org/abs/2507.09709)  
*Baturay Saglam, Paul Kassianik, Blaine Nelson 等 6 人*  
评分: 8.31 · 2025-07-13

> 本文通过大规模实证研究发现，LLMs的高级语义信息一致存在于跨领域的低维子空间中，形成线性可分离表示，尤其在深层和引发结构化推理的提示下更明显。基于此，作者训练MLP探针作为轻量级潜在空间护栏，显著提高对恶意查询和提示注入的拒绝率，为几何感知安全工具提供新思路。
<br>

**#91** [Secure Tug-of-War (SecTOW): Iterative Defense-Attack Training with Reinforcement Learning for Multimodal Model Security](https://arxiv.org/abs/2507.22037)  
*Muzhi Dai, Shixuan Liu, Zhiyuan Zhao 等 6 人*  
评分: 8.30 · 2025-07-29

> 本文提出了SecTOW方法，一种基于强化学习的迭代防御-攻击训练框架，用于增强多模态大语言模型的安全性。该方法通过防御者和辅助攻击者的迭代对抗，利用攻击者发现的漏洞扩展越狱数据并训练防御者，有效解决了训练样本稀缺和过度拒绝无害输入的问题。
<br>

**#92** [Reimagining Safety Alignment with An Image](https://arxiv.org/abs/2511.00509)  
*Yifan Xia, Guorui Chen, Wenqian Yu 等 6 人*  
评分: 8.30 · 2025-11-01

> 提出了Magic Image，一种基于优化的视觉提示框架，用于增强多模态大模型的安全性并减少过度拒绝。该方法通过优化图像提示词，使单一模型无需参数更新即可适应不同的价值体系，在保持模型性能的同时实现了更好的安全与效果平衡。
<br>

**#100** [The VLLM Safety Paradox: Dual Ease in Jailbreak Attack and Defense](https://arxiv.org/abs/2411.08410)  
*Yangyang Guo, Fangkai Jiao, Liqiang Nie 等 4 人*  
评分: 8.27 · 2024-11-13

> 本文探讨了视觉大语言模型在越狱攻击与防御中表现出的双重高性能悖论，分析了视觉输入导致的脆弱性以及现有防御机制中存在的“过度谨慎”问题。作者提出了LLM-Pipeline方法，利用LLM的护栏作为有效检测器，以提升VLLM的安全性。
<br>

---

### 📊 Security Evaluation（安全测评）

**#1** [MCPEval: Automatic MCP-based Deep Evaluation for AI Agent Models](https://arxiv.org/abs/2507.12806)  
*Zhiwei Liu, Jielin Qiu, Shiyu Wang 等 12 人*  
评分: 9.45 · 2025-07-17

> 本文介绍了MCPEval，一个开源的模型上下文协议(MCP)框架，用于自动化跨不同领域的LLM智能体端到端任务生成和深度评估。该框架标准化指标，与原生智能体工具无缝集成，消除构建评估管道的手动工作。在五个真实世界领域的实证结果显示了其在揭示细微、特定领域性能方面的有效性。作者公开了MCPEval以促进可复现和标准化的LLM智能体评估，解决了现有方法依赖静态基准和劳动密集型数据收集的局限性。
<br>

**#2** [AgentHarm: A Benchmark for Measuring Harmfulness of LLM Agents](https://arxiv.org/abs/2410.09024)  
*Maksym Andriushchenko, Alexandra Souly, Mateusz Dziemian 等 14 人*  
评分: 9.37 · 2024-10-11

> 本文提出了AgentHarm基准，用于测量LLM代理的有害性，填补了LLM代理鲁棒性研究的空白。该基准包含110个明确的恶意代理任务，涵盖欺诈、网络犯罪等11个危害类别，要求越狱后的代理在完成多步骤任务时仍保持其能力。评估结果显示，领先的LLM在未受攻击时也出人意料地顺从恶意代理请求，且简单的通用越狱模板能有效诱导代理产生连贯的恶意行为。
<br>

**#7** [Agent Security Bench (ASB): Formalizing and Benchmarking Attacks and Defenses in LLM-based Agents](https://arxiv.org/abs/2410.02644)  
*Hanrong Zhang, Jingyuan Huang, Kai Mei 等 8 人*  
评分: 9.15 · 2024-10-03

> 本研究介绍了 Agent Security Bench (ASB)，一个旨在形式化和基准测试基于 LLM 的智能体攻击与防御的综合框架。该框架涵盖了电商、自动驾驶等 10 个场景，包含 10 个目标智能体、400 多个工具以及 27 种攻击和防御方法。基准测试结果揭示了智能体运行各阶段的关键漏洞，并评估了现有防御措施的有限效果。
<br>

**#28** [RedCode: Risky Code Execution and Generation Benchmark for Code Agents](https://arxiv.org/abs/2411.07781)  
*Chengquan Guo, Xun Liu, Chulin Xie 等 8 人*  
评分: 8.82 · 2024-11-12

> 本文提出了 RedCode，一个用于评估代码 Agent 安全性的基准测试，包含 RedCode-Exec 和 RedCode-Gen 两个部分。RedCode-Exec 提供了 4050 个涵盖 25 种漏洞的测试用例，评估 Agent 识别和处理不安全代码的能力；RedCode-Gen 则评估 Agent 生成有害代码的倾向。基于 19 个 LLM 的实证研究发现，Agent 虽然倾向于拒绝操作系统层面的风险操作，但难以拒绝执行技术上有缺陷的代码，揭示了代码 Agent 在实际部署中的安全风险。
<br>

**#29** [Beyond Simulations: What 20,000 Real Conversations Reveal About Mental Health AI Safety](https://arxiv.org/abs/2601.17003)  
*Caitlin A. Stamatis, Jonah Meyerhoff, Richard Zhang 等 6 人*  
评分: 8.80 · 2026-01-14

> 本研究通过复现四项安全测试集并对20,000次真实世界对话进行生态审计，评估了心理健康AI的安全性。结果显示，专用AI在自杀和自残等基准测试中的有害内容生成率远低于通用LLM，且真实部署中的安全性优于模拟测试。临床医生审查确认了极低的漏报率，强调了基于真实使用数据评估AI安全性的重要性。
<br>

**#32** [DeepPlanning: Benchmarking Long-Horizon Agentic Planning with Verifiable Constraints](https://arxiv.org/abs/2601.18137)  
*Yinger Zhang, Shutong Jiang, Renhao Li 等 9 人*  
评分: 8.77 · 2026-01-26

> 本文提出了DeepPlanning，一个针对实际长视距Agent规划的基准测试，包含多日旅行规划和多产品购物任务。该基准要求模型具备主动信息收集、局部约束推理和全局约束优化的能力，以解决现有基准对真实世界约束代表性不足的问题。评估结果显示，即使是前沿的Agent LLM在这些任务上也表现挣扎，凸显了可靠推理模式和并行工具使用的重要性。
<br>

**#33** [SG-Bench: Evaluating LLM Safety Generalization Across Diverse Tasks and Prompt Types](https://arxiv.org/abs/2410.21965)  
*Yutao Mou, Shikun Zhang, Wei Ye*  
评分: 8.77 · 2024-10-29

> 本文提出了 SG-Bench，这是一个新颖的基准测试，旨在评估大语言模型在各种任务和提示类型下的安全泛化能力。该基准整合了生成式和判别式评估任务，并扩展了数据以检查提示工程和越狱对 LLM 安全性的影响。评估结果显示，大多数 LLM 在判别式任务上表现较差，且极易受到提示词的影响，表明其在安全对齐方面的泛化能力较弱。
<br>

**#37** [Audio Is the Achilles' Heel: Red Teaming Audio Large Multimodal Models](https://arxiv.org/abs/2410.23861)  
*Hao Yang, Lizhen Qu, Ehsan Shareghi 等 4 人*  
评分: 8.72 · 2024-10-31

> 本文对五个先进的音频大型多模态模型进行了全面的红队测试，评估了其在有害音频问题、非语音音频干扰及特定语音越狱场景下的安全性。结果显示，开源音频LMM在有害音频问题上的平均攻击成功率较高，且容易受到非语音噪声干扰，暴露了音频模态的安全漏洞。
<br>

**#40** [AdamMeme: Adaptively Probe the Reasoning Capacity of Multimodal Large Language Models on Harmfulness](https://arxiv.org/abs/2507.01702)  
*Zixin Chen, Hongzhan Lin, Kaixin Li 等 8 人*  
评分: 8.66 · 2025-07-02

> 本文提出了AdamMeme，一个灵活的基于代理的评估框架，用于自适应探测多模态大语言模型对有害梗的理解能力。通过多代理协作，该框架迭代更新具有挑战性的梗数据，从而全面暴露模型在解释有害性方面的具体弱点。实验表明，AdamMeme能系统性地揭示不同目标模型的性能差异，提供细粒度的分析。
<br>

**#41** [Agents in the Wild: Safety, Society, and the Illusion of Sociality on Moltbook](https://arxiv.org/abs/2602.13284)  
*Yunbei Zhang, Kai Mei, Ming Liu 等 8 人*  
评分: 8.63 · 2026-02-07

> 本文对AI社交平台Moltbook进行了大规模实证研究，观察了智能体在开放环境中的自发社会行为和安全状况。研究发现，智能体在几天内自发形成了治理和经济体系，且社会工程攻击远比提示注入更有效，高对抗性内容获得更多互动。研究揭示了智能体社交互动的结构性空洞及其面临的安全挑战。
<br>

**#43** [Security Challenges in AI Agent Deployment: Insights from a Large Scale Public Competition](https://arxiv.org/abs/2507.20526)  
*Andy Zou, Maxwell Lin, Eliot Jones 等 17 人*  
评分: 8.61 · 2025-07-28

> 本文基于针对22个前沿AI Agent的大规模红队测试竞赛，分析了Agent部署中的安全挑战。通过构建ART基准测试，研究发现几乎所有Agent在少量查询下即出现策略违规，且鲁棒性与模型规模或能力相关性较低，揭示了当前AI Agent存在的关键安全漏洞。
<br>

**#44** [OpenAgentSafety: A Comprehensive Framework for Evaluating Real-World AI Agent Safety](https://arxiv.org/abs/2507.06134)  
*Sanidhya Vijayvargiya, Aditya Bharat Soni, Xuhui Zhou 等 7 人*  
评分: 8.61 · 2025-07-08

> 本文提出了OpenAgentSafety框架，用于评估与真实工具（如浏览器、代码环境）交互的AI Agent的安全性。该框架涵盖8大风险类别和350多项任务，揭示了主流LLM在Agent场景中存在严重的安全漏洞，强调了在部署前加强保障的必要性。
<br>

**#45** [Holistic Agent Leaderboard: The Missing Infrastructure for AI Agent Evaluation](https://arxiv.org/abs/2510.11977)  
*Sayash Kapoor, Benedikt Stroebl, Peter Kirgis 等 31 人*  
评分: 8.61 · 2025-10-13

> 本文介绍了Holistic Agent Leaderboard (HAL)，一个旨在解决Agent评估挑战的标准化基础设施。它提供了并行评估工具，对模型、脚手架和基准进行三维分析，并利用LLM辅助日志检查发现未报告的异常行为。该框架旨在标准化评估方式，推动Agent从通过基准测试转向在现实世界中可靠工作。
<br>

**#48** [Risky-Bench: Probing Agentic Safety Risks under Real-World Deployment](https://arxiv.org/abs/2602.03100)  
*Jingnan Zheng, Yanzhen Luo, Jingjun Xu 等 11 人*  
评分: 8.60 · 2026-02-03

> 本文提出了Risky-Bench框架，旨在解决现有Agent安全评估覆盖面有限且难以适应复杂真实世界部署的问题。该框架基于领域无关的安全原则构建上下文感知的安全规则，通过在不同威胁假设下的真实任务执行来系统评估安全风险。应用于生活辅助Agent场景时，Risky-Bench揭示了最先进Agent在真实执行条件下存在重大安全风险。
<br>

**#58** [Refusal-Trained LLMs Are Easily Jailbroken As Browser Agents](https://arxiv.org/abs/2410.13886)  
*Priyanshu Kumar, Elaine Lau, Saranya Vijayakumar 等 12 人*  
评分: 8.53 · 2024-10-11

> 本文研究了经过拒绝训练的LLM在非聊天和代理用例中的安全性，并引入了BrowserART工具包专门用于红队测试浏览器代理。实证研究表明，尽管骨干LLM作为聊天机器人时会拒绝有害指令，但相应的浏览器代理却不会执行拒绝。此外，针对聊天环境设计的越狱攻击方法能有效迁移到浏览器代理中，揭示了当前安全机制在代理应用中的严重缺陷。
<br>

**#60** [Bridging AI and Software Security: A Comparative Vulnerability Assessment of LLM Agent Deployment Paradigms](https://arxiv.org/abs/2507.06323)  
*Tarek Gasmi, Ramzi Guesmi, Ines Belhadj 等 4 人*  
评分: 8.51 · 2025-07-08

> 本文通过统一威胁分类框架，对比评估了Function Calling和模型上下文协议（MCP）两种LLM Agent部署范式的安全性。研究发现架构选择显著重塑威胁面，且链式攻击成功率极高，为跨域LLM Agent安全评估提供了方法论基础和部署指导。
<br>

**#64** [HAICOSYSTEM: An Ecosystem for Sandboxing Safety Risks in Human-AI Interactions](https://arxiv.org/abs/2409.16427)  
*Xuhui Zhou, Hyunwoo Kim, Faeze Brahman 等 12 人*  
评分: 8.49 · 2024-09-24

> 本文提出了HAICOSYSTEM框架，通过模块化沙箱环境模拟人类用户与AI代理之间的复杂多轮交互及工具使用场景。该框架建立了一个多维度的评估体系，对操作、内容、社会和法律风险进行度量，实验表明现有最先进的LLM在恶意用户交互中存在显著的安全风险。
<br>

**#66** [From Assistant to Double Agent: Formalizing and Benchmarking Attacks on OpenClaw for Personalized Local AI Agent](https://arxiv.org/abs/2602.08412)  
*Yuhang Wang, Feiming Xu, Zheng Lin 等 9 人*  
评分: 8.45 · 2026-02-09

> 针对现有安全评估框架主要关注合成或以任务为中心的设置，无法捕捉个性化智能体真实部署风险的局限，本文提出了个性化智能体安全基准（PASB）。该框架结合了个性化使用场景、真实工具链和长视界交互，能够对真实系统进行黑盒端到端的安全评估。通过对OpenClaw的系统性评估，揭示了其在用户提示处理、工具使用和记忆检索等不同阶段的关键漏洞。
<br>

**#69** [Skill-Inject: Measuring Agent Vulnerability to Skill File Attacks](https://arxiv.org/abs/2602.20156)  
*David Schmotz, Luca Beurer-Kellner, Sahar Abdelnabi 等 4 人*  
评分: 8.43 · 2026-02-23

> 本文提出了 SkillInject，一个专门用于评估 LLM agents 对技能文件提示注入攻击脆弱性的基准测试。针对 agents 通过技能文件扩展功能所带来的供应链安全风险，该研究构建了包含 202 个攻击-任务对的数据集，涵盖了从明显恶意到隐藏在合法指令中的微妙攻击。实验结果表明，当前主流的 LLM agents 在面对此类攻击时表现出极高的脆弱性，且在安全性与实用性之间存在显著权衡。
<br>

**#71** [Agent-SafetyBench: Evaluating the Safety of LLM Agents](https://arxiv.org/abs/2412.14470)  
*Zhexin Zhang, Shiyao Cui, Yida Lu 等 7 人*  
评分: 8.42 · 2024-12-19

> 本文介绍了 Agent-SafetyBench，一个旨在评估 LLM 智能体安全的综合基准，包含 349 个交互环境和 2000 个测试用例，覆盖 8 类安全风险。对 16 个流行 LLM 智能体的评估结果显示，所有智能体的安全分数均未超过 60%，揭示了当前智能体缺乏鲁棒性和风险意识等根本缺陷。该基准强调了仅靠防御提示不足以解决安全问题，为智能体安全评估提供了重要工具。
<br>

**#73** [Evaluation and Benchmarking of LLM Agents: A Survey](https://arxiv.org/abs/2507.21504)  
*Mahmoud Mohammadi, Yipeng Li, Jane Lo 等 4 人*  
评分: 8.40 · 2025-07-29

> 本文是一篇关于LLM Agent评估的综述，提出了包含评估目标和评估过程的二维分类法，系统梳理了现有工作。文章强调了企业级应用中常被忽视的挑战（如角色访问控制、长期交互合规性），并指出了整体化、现实化和可扩展评估的未来研究方向。
<br>

**#74** [State-Dependent Safety Failures in Multi-Turn Language Model Interaction](https://arxiv.org/abs/2603.15684)  
*Pengcheng Li, Jie Zhang, Tianwei Zhang 等 8 人*  
评分: 8.40 · 2026-03-15

> 本文从状态空间视角研究了多轮对话中的安全故障，提出了STAR诊断框架以分析对话历史如何导致安全崩溃。研究发现，多轮失败源于结构化的上下文状态演化，且存在从拒绝到顺从的突然相变。这表明语言模型安全性应被视为动态的、状态依赖的过程，而非静态属性。
<br>

**#75** [Multimodal Situational Safety](https://arxiv.org/abs/2410.06172)  
*Kaiwen Zhou, Chengzhi Liu, Xuandong Zhao 等 6 人*  
评分: 8.40 · 2024-10-08

> 本文提出了多模态情境安全这一新挑战，探讨了安全考量如何随用户或代理所处的特定情境而变化。作者开发了MSSBench基准，包含1820个语言查询-图像对，用于评估当前多模态大语言模型在视觉情境下评估语言查询安全性的能力。研究发现，当前的MLLM在指令遵循设置下难以处理这种细微的安全问题，特别是在同时处理显式安全推理、视觉理解和情境安全推理方面存在不足。
<br>

**#78** [OmniSafeBench-MM: A Unified Benchmark and Toolbox for Multimodal Jailbreak Attack-Defense Evaluation](https://arxiv.org/abs/2512.06589)  
*Xiaojun Jia, Jie Liao, Qi Guo 等 14 人*  
评分: 8.38 · 2025-12-06

> 论文介绍了OmniSafeBench-MM，一个统一的多模态越狱攻防评估基准和工具箱，集成了多种攻击方法和防御策略。该基准建立了包含危害性、意图对齐和响应细节的三维评估协议，全面揭示了多模态模型的安全漏洞，促进了可复现的安全研究。
<br>

**#83** [AgentDyn: A Dynamic Open-Ended Benchmark for Evaluating Prompt Injection Attacks of Real-World Agent Security System](https://arxiv.org/abs/2602.03117)  
*Hao Li, Ruoyao Wen, Shanghao Shi 等 5 人*  
评分: 8.34 · 2026-02-03

> 本文提出了AgentDyn基准，旨在解决现有Agent安全基准缺乏动态开放式任务、有益指令和复杂用户任务的问题。AgentDyn包含60个具有挑战性的开放式任务和560个注入测试用例，覆盖购物、GitHub和日常生活场景，要求Agent进行动态规划。评估显示，现有的最先进防御措施要么安全性不足，要么存在过度防御，远未达到实际部署的要求。
<br>

**#85** [KnowU-Bench: Towards Interactive, Proactive, and Personalized Mobile Agent Evaluation](https://arxiv.org/abs/2604.08455)  
*Tongbo Chen, Zhengxi Lu, Zhan Xu 等 16 人*  
评分: 8.34 · 2026-04-09

> 该研究提出了KnowU-Bench，一个用于个性化移动代理的在线基准，建立在可重现的Android仿真环境上，涵盖42个通用GUI任务、86个个性化任务和64个主动任务。与将用户偏好视为静态上下文的前人工作不同，KnowU-Bench隐藏用户配置文件仅暴露行为日志，强制真实偏好推断。它支持多轮偏好引出，并实例化了基于结构化配置文件的LLM驱动用户模拟器，全面评估代理的个性化能力。
<br>

**#86** [OdysseyArena: Benchmarking Large Language Models For Long-Horizon, Active and Inductive Interactions](https://arxiv.org/abs/2602.05843)  
*Fangzhi Xu, Hang Yan, Qiushi Sun 等 19 人*  
评分: 8.33 · 2026-02-05

> 本文提出了OdysseyArena，一个专注于长视界、主动和归纳交互的LLM智能体基准测试。该基准测试通过形式化四个原语，将抽象的转换动力学转化为具体的交互环境，旨在测量智能体的归纳效率和长视界发现能力。实验表明，即使是前沿模型在归纳场景中也存在缺陷，揭示了自主发现复杂环境的瓶颈。
<br>

**#89** [BrowserArena: Evaluating LLM Agents on Real-World Web Navigation Tasks](https://arxiv.org/abs/2510.02418)  
*Sagnik Anupam, Davis Brown, Shuo Li 等 6 人*  
评分: 8.32 · 2025-10-02

> 本文提出了BrowserArena，一个基于真实开放网络的LLM智能体评估平台，通过收集用户任务和Arena式对抗比较来测试智能体能力。研究利用逐步人工反馈识别了验证码处理、弹窗移除和URL导航等关键失败模式，并分析了不同模型在应对这些挑战时的策略差异。该工作揭示了当前Web智能体在真实环境中的多样性与脆弱性，为智能体评估提供了新的基准和方法。
<br>

**#93** [EnterpriseOps-Gym: Environments and Evaluations for Stateful Agentic Planning and Tool Use in Enterprise Settings](https://arxiv.org/abs/2603.13594)  
*Shiva Krishna Reddy Malay, Shravan Nayak, Jishnu Sethumadhavan Nair 等 9 人*  
评分: 8.30 · 2026-03-13

> 本文推出了EnterpriseOps-Gym基准，用于评估Agent在真实企业环境中的规划和工具使用能力。该环境包含大量数据库和工具，测试了14个前沿模型在长期规划和状态变化下的表现，揭示了当前Agent在战略推理和拒绝不可行任务方面的关键局限。该基准为提升Agent在企业部署中的鲁棒性提供了具体测试平台。
<br>

**#97** [Confusion is the Final Barrier: Rethinking Jailbreak Evaluation and Investigating the Real Misuse Threat of LLMs](https://arxiv.org/abs/2508.16347)  
*Yu Yan, Sheng Sun, Zhe Wang 等 9 人*  
评分: 8.28 · 2025-08-22

> 本文重新审视了越狱评估，通过解耦越狱技术，构建知识密集型问答来研究LLM在危险知识拥有量、有害任务规划等方面的真实滥用威胁。实验揭示了越狱成功率与有害知识拥有量之间的不匹配，表明现有评估框架往往锚定于有毒语言模式，而非真实威胁。
<br>

---

### 🏗️ Agent Security Architecture（Agent安全架构）

**#4** [IPIGuard: A Novel Tool Dependency Graph-Based Defense Against Indirect Prompt Injection in LLM Agents](https://arxiv.org/abs/2508.15310)  
*Hengyu An, Jinghuai Zhang, Tianyu Du 等 7 人*  
评分: 9.33 · 2025-08-21

> 本文提出了IPIGuard，一种基于工具依赖图的新型防御范式，用于保护LLM智能体免受间接提示注入攻击。该方法将智能体的任务执行过程建模为在计划好的工具依赖图上的遍历，通过显式解耦动作规划与外部数据交互，有效减少了恶意工具调用。实验表明，IPIGuard在有效性和鲁棒性之间取得了优异的平衡。
<br>

**#12** [G-Designer: Architecting Multi-agent Communication Topologies via Graph Neural Networks](https://arxiv.org/abs/2410.11782)  
*Guibin Zhang, Yanwei Yue, Xiangguo Sun 等 9 人*  
评分: 9.06 · 2024-10-15

> 本文提出了G-Designer，一种利用图神经网络动态设计多智能体通信拓扑的自适应解决方案。该方法通过建模多智能体网络，解码出任务自适应的高性能通信协议，在多个基准测试中表现出色，并能有效减少token消耗，同时展现出对抗智能体对抗攻击的鲁棒性，优化了多智能体系统的部署。
<br>

**#16** [Towards Low-Resource Harmful Meme Detection with LMM Agents](https://arxiv.org/abs/2411.05383)  
*Jianzhao Huang, Hongzhan Lin, Ziyan Liu 等 6 人*  
评分: 8.97 · 2024-11-08

> 本文提出了一种基于 LMM Agent 的低资源有害表情包检测框架，通过外向和内向分析结合少量标注样本进行识别。该方法利用大型多模态模型（LMM）的推理能力，首先检索相关表情包作为辅助信号，然后激发 Agent 的知识修订行为以获得泛化性强的有害性洞察。实验表明，该方法在三个表情包数据集上的低资源检测任务中表现优于现有最先进方法。
<br>

**#18** [MIND: A Multi-agent Framework for Zero-shot Harmful Meme Detection](https://arxiv.org/abs/2507.06908)  
*Ziyan Liu, Chunxiao Fan, Haoran Lou 等 5 人*  
评分: 8.93 · 2025-07-09

> 本文提出MIND多代理框架，实现零样本有害迷因检测，无需标注数据。MIND通过检索相似迷因提供上下文、双向洞察推导机制和多代理辩论确保稳健决策。实验表明，该框架优于现有零样本方法，在不同模型架构和参数规模上表现强大泛化能力，为社交媒体有害内容检测提供可扩展解决方案。
<br>

**#19** [Securing the Model Context Protocol: Defending LLMs Against Tool Poisoning and Adversarial Attacks](https://arxiv.org/abs/2512.06556)  
*Saeid Jamshidi, Kawser Wazed Nafi, Arghavan Moradi Dakhel 等 6 人*  
评分: 8.92 · 2025-12-06

> 论文分析了模型上下文协议（MCP）中的语义攻击，如工具投毒和影子攻击，并提出了一种分层安全防御框架。该框架通过清单签名、语义审查和启发式护栏，有效保护了基于MCP的系统免受恶意工具元数据的侵害，填补了工具交互安全的空白。
<br>

**#20** [Cut the Crap: An Economical Communication Pipeline for LLM-based Multi-Agent Systems](https://arxiv.org/abs/2410.02506)  
*Guibin Zhang, Yanwei Yue, Zhixun Li 等 9 人*  
评分: 8.91 · 2024-10-03

> 本研究提出了 AgentPrune，一个经济高效且鲁棒的多智能体通信框架，旨在剪枝现有 LLM 多智能体管道中的冗余或恶意消息。该框架首次识别并定义了“通信冗余”问题，通过在时空消息传递图上进行一次性剪枝，显著降低了 token 成本。实验表明，该方法在保持高性能的同时，能有效防御两种基于智能体的对抗性攻击。
<br>

**#21** [ResMAS: Resilience Optimization in LLM-based Multi-agent Systems](https://arxiv.org/abs/2601.04694)  
*Zhilun Zhou, Zihan Liu, Jiahe Liu 等 8 人*  
评分: 8.90 · 2026-01-08

> 本文提出了ResMAS框架，通过强化学习生成弹性拓扑结构并优化提示，以增强基于大语言模型的多智能体系统在扰动下的韧性。实验表明，该方法在各种约束下显著提高了系统的鲁棒性和泛化能力，为构建具有内在弹性的多智能体系统提供了新思路。
<br>

**#22** [Policy Compiler for Secure Agentic Systems](https://arxiv.org/abs/2602.16708)  
*Nils Palumbo, Sarthak Choudhary, Jihye Choi 等 5 人*  
评分: 8.89 · 2026-02-18

> 提出PCAS，一个为智能体系统提供确定性策略执行的政策编译器。该系统通过依赖图建模智能体状态，使用Datalog语言表达策略，并通过参考监控器拦截违规行为。评估显示PCAS能显著提高政策合规性，且无需对模型推理进行安全特定的重构。
<br>

**#26** [Uncovering Security Threats and Architecting Defenses in Autonomous Agents: A Case Study of OpenClaw](https://arxiv.org/abs/2603.12644)  
*Zonghao Ying, Xiao Yang, Siyang Wu 等 10 人*  
评分: 8.83 · 2026-03-13

> 本文对OpenClaw生态系统进行了全面的安全分析，揭示了提示注入驱动的远程代码执行等关键漏洞。提出了全生命周期Agent安全架构（FASA），倡导零信任执行和动态意图验证，旨在解决自主Agent的系统性架构缺陷。该研究为构建值得信赖的自主Agent提供了理论蓝图和工程方向。
<br>

**#27** [ToolSafe: Enhancing Tool Invocation Safety of LLM-based agents via Proactive Step-level Guardrail and Feedback](https://arxiv.org/abs/2601.10156)  
*Yutao Mou, Zhangchi Xue, Lijun Li 等 7 人*  
评分: 8.82 · 2026-01-15

> ToolSafe 提出了一种通过主动步骤级护栏和反馈来增强 LLM Agent 工具调用安全性的框架。该研究构建了 TS-Bench 基准，并开发了 TS-Guard 模型，有效减少了有害工具调用并提高了良性任务完成率，确保了 Agent 部署时的实时安全监控。
<br>

**#31** [Towards Verifiably Safe Tool Use for LLM Agents](https://arxiv.org/abs/2601.08012)  
*Aarya Doshi, Yining Hong, Congying Xu 等 6 人*  
评分: 8.79 · 2026-01-12

> 本文提出了一种基于系统理论过程分析（STPA）的流程，用于识别Agent工作流中的危害并将安全需求形式化为可执行的规范。作者引入了增强型模型上下文协议（MCP）框架，通过结构化标签确保工具使用的安全性。该方法旨在将LLM Agent的安全性从临时的可靠性修复转变为具有形式化保证的主动护栏，减少对用户确认的依赖。
<br>

**#39** [The Task Shield: Enforcing Task Alignment to Defend Against Indirect Prompt Injection in LLM Agents](https://arxiv.org/abs/2412.16682)  
*Feiran Jia, Tong Wu, Xin Qin 等 4 人*  
评分: 8.67 · 2024-12-21

> 针对LLM智能体面临的间接提示注入攻击，本文提出了Task Shield防御机制。该方法将安全重构为任务对齐问题，在测试时系统性地验证每条指令和工具调用是否符合用户目标，在AgentDojo基准测试中显著降低了攻击成功率并保持了高任务效用，提供了一种新的安全防御视角。
<br>

**#49** [OS-Sentinel: Towards Safety-Enhanced Mobile GUI Agents via Hybrid Validation in Realistic Workflows](https://arxiv.org/abs/2510.24411)  
*Qiushi Sun, Mukai Li, Zhoumianze Liu 等 14 人*  
评分: 8.57 · 2025-10-28

> 针对移动GUI Agent的安全隐患，本文提出了MobileRisk-Live动态沙箱环境及安全检测基准。在此基础上，开发了OS-Sentinel混合安全检测框架，结合形式化验证器和基于VLM的上下文判断器，有效检测系统违规和上下文风险，显著提升了移动Agent的安全性。
<br>

**#51** [VeriGuard: Enhancing LLM Agent Safety via Verified Code Generation](https://arxiv.org/abs/2510.05156)  
*Lesly Miculicich, Mihir Parmar, Hamid Palangi 等 7 人*  
评分: 8.57 · 2025-10-03

> 本文介绍了VeriGuard，一种通过双阶段架构为基于LLM的智能体提供形式化安全保证的框架。该框架首先在离线阶段通过形式化验证合成并验证行为策略，随后在在线阶段作为运行时监控器验证每个拟议的智能体动作。这种离线验证与在线监控的分离设计，使得形式化保证能够实际应用于敏感领域的智能体，显著提升了其可信度。
<br>

**#55** [Enforcing Temporal Constraints for LLM Agents](https://arxiv.org/abs/2512.23738)  
*Adharsh Kamath, Sishen Zhang, Calvin Xu 等 6 人*  
评分: 8.54 · 2025-12-25

> 本文提出了Agent-C框架，旨在确保基于LLM的智能体在运行时遵守形式化的时序安全属性（如先认证后访问数据）。该框架引入领域特定语言表达时序属性，利用SMT求解检测不合规操作，并通过约束生成技术强制智能体执行符合规范的替代动作。实验证明Agent-C能有效防止安全关键应用中的时序违规行为。
<br>

**#63** [When Only the Final Text Survives: Implicit Execution Tracing for Multi-Agent Attribution](https://arxiv.org/abs/2603.17445)  
*Yi Nian, Haosen Cao, Shenzhe Zhu 等 6 人*  
评分: 8.49 · 2026-03-18

> 本文提出了IET，一种在执行元数据不可用的情况下，通过最终文本进行多智能体归因的框架。该方法将特定于智能体的统计信号直接嵌入到令牌生成过程中，将输出文本转换为自验证的执行记录，从而在隐私保护或系统边界限制下实现可靠的问责。
<br>

**#88** [A Framework for Formalizing LLM Agent Security](https://arxiv.org/abs/2603.19469)  
*Vincent Siu, Jingxuan He, Kyle Montgomery 等 7 人*  
评分: 8.33 · 2026-03-19

> 本文提出了一个形式化LLM智能体安全的框架，从上下文安全的角度系统化了现有的攻击和防御。该框架定义了任务对齐、动作对齐、源授权和数据隔离四个安全属性，并引入预言机函数来验证违规行为。该框架有助于解决安全与效用之间的权衡问题，为防御策略提供理论基础。
<br>

**#98** [Your Agent May Misevolve: Emergent Risks in Self-evolving LLM Agents](https://arxiv.org/abs/2509.26354)  
*Shuai Shao, Qihan Ren, Chen Qian 等 11 人*  
评分: 8.28 · 2025-09-30

> 本文研究了自进化 LLM 代理中的“错误进化”风险，即代理在自我改进过程中偏离预期导致有害结果。通过评估模型、记忆、工具和工作流四个进化路径，研究发现即使在顶级 LLM 上构建的代理也普遍存在安全对齐退化等风险，强调了建立新安全范式以应对自进化代理潜在威胁的紧迫性。
<br>

---

### 📄 Other Topics（其他）

**#11** [SPA-Bench: A Comprehensive Benchmark for SmartPhone Agent Evaluation](https://arxiv.org/abs/2410.15164)  
*Jingxuan Chen, Derek Yuen, Bin Xie 等 17 人*  
评分: 9.11 · 2024-10-19

> 本文提出了SPA-Bench，一个用于评估基于（多模态）LLM的智能手机智能体的综合基准。该基准在模拟真实世界的交互环境中提供多样化的任务、即插即用的框架以及自动评估管道，揭示了智能体在解释移动界面、动作定位和记忆保留等方面的挑战，为未来的研究提供了方向。
<br>

**#30** [Agentic AI Security: Threats, Defenses, Evaluation, and Open Challenges](https://arxiv.org/abs/2510.23883)  
*Anshuman Chhabra, Shrestha Datta, Shahriar Kabir Nahin 等 4 人*  
评分: 8.79 · 2025-10-27

> 本文是一篇关于Agentic AI安全的综述，系统梳理了Agent系统特有的威胁分类，回顾了最新的基准测试和评估方法。文章从技术和治理角度讨论了防御策略，并综合当前研究指出了开放性挑战，旨在支持“安全设计”Agent系统的开发。
<br>

**#77** [The Attack and Defense Landscape of Agentic AI: A Comprehensive Survey](https://arxiv.org/abs/2603.11088)  
*Juhee Kim, Xiaoyuan Liu, Zhun Wang 等 7 人*  
评分: 8.39 · 2026-03-11

> 本文对AI Agent的安全进行了首次系统性全面综述，分析了安全Agent系统的设计空间、攻击面和防御机制。通过案例研究指出了现有安全Agent系统的差距，并提出了理解AI Agent安全风险和防御策略的系统性框架。
<br>

**#81** [Strategic Tradeoffs Between Humans and AI in Multi-Agent Bargaining](https://arxiv.org/abs/2509.09071)  
*Crystal Qian, Kehang Zhu, John Horton 等 7 人*  
评分: 8.36 · 2025-09-11

> 本文通过实证研究比较了人类、前沿大语言模型和定制贝叶斯 Agent 在动态多人讨价还价游戏中的行为差异。研究发现，虽然 LLM 和人类实现了相当的总体剩余，但 LLM 倾向于保守的让步策略，而人类则遵循公平规范，这揭示了性能平等指标下掩盖的实质性程序差异。
<br>

**#87** [Steering Externalities: Benign Activation Steering Unintentionally Increases Jailbreak Risk for Large Language Models](https://arxiv.org/abs/2602.04896)  
*Chen Xiong, Zhiyuan He, Pin-Yu Chen 等 5 人*  
评分: 8.33 · 2026-02-03

> 本文揭示了“引导外部性”现象，即利用良性数据集（如强制合规或JSON格式）进行激活引导时，会无意中削弱大语言模型的安全护栏。实验表明，这种旨在提升模型效用的干预措施反而会放大越狱漏洞，将标准基准测试中的攻击成功率提升至80%以上。研究强调了在部署阶段必须严格审查推理时效用提升所带来的意外安全外部性。
<br>

**#94** [Sketch2Code: Evaluating Vision-Language Models for Interactive Web Design Prototyping](https://arxiv.org/abs/2410.16232)  
*Ryan Li, Yanzhe Zhang, Diyi Yang*  
评分: 8.30 · 2024-10-21

> 本文提出了Sketch2Code基准，用于评估视觉语言模型（VLM）将草图转换为网页原型的能力。该基准支持模拟真实设计工作流的交互式智能体评估，分析了十种商业和开源模型的表现，发现现有模型在准确解释草图和有效提问方面仍面临挑战，强调了开发多轮对话智能体的必要性。
<br>

---

*数据来源：[arXiv](https://arxiv.org/)、[Semantic Scholar](https://www.semanticscholar.org/)*
