# 🏗️ Agent Security Architecture（Agent安全架构）

> 211 篇论文 | 按质量评分排序

---

## #1 — IPIGuard: A Novel Tool Dependency Graph-Based Defense Against Indirect Prompt Injection in LLM Agents

`A` Score: 9.18 | 2025-08-21

**Authors:** Hengyu An, Jinghuai Zhang, Tianyu Du, Chunyi Zhou, Qingming Li, Tao Lin et al. (7 total)

**Categories:** cs.CR, cs.AI, cs.CL

**Scores:** Citation: 9.77 | Influential: 9.58 | Venue: 10.00 | Author: 7.80 | Recency: 7.00

**Links:** [arXiv](https://arxiv.org/abs/2508.15310) | [PDF](https://arxiv.org/pdf/2508.15310)

> 本文提出了IPIGuard，一种基于工具依赖图的新型防御范式，用于保护LLM智能体免受间接提示注入攻击。该方法将智能体的任务执行过程建模为在计划好的工具依赖图上的遍历，通过显式解耦动作规划与外部数据交互，有效减少了恶意工具调用。实验表明，IPIGuard在有效性和鲁棒性之间取得了优异的平衡。

---

## #2 — ShieldAgent: Shielding Agents via Verifiable Safety Policy Reasoning

`A` Score: 8.97 | 2025-03-26

**Authors:** Zhaorun Chen, Mintong Kang, Bo Li

**Categories:** cs.LG, cs.CR

**Scores:** Citation: 9.93 | Influential: 9.97 | Venue: 10.00 | Author: 6.75 | Recency: 5.00

**Links:** [arXiv](https://arxiv.org/abs/2503.22738) | [PDF](https://arxiv.org/pdf/2503.22738)

> 本文提出了ShieldAgent，第一个通过逻辑推理强制执行其他受保护代理行动轨迹安全策略合规性的护栏代理。ShieldAgent通过从政策文档提取可验证规则并构建基于动作的概率规则电路集来构建安全策略模型。给定受保护代理的行动轨迹，ShieldAgent检索相关规则电路并生成屏蔽计划，利用工具库和可执行代码进行形式验证。实验显示，ShieldAgent在ShieldAgent-Bench和三个现有基准上实现了SOTA性能，平均比先前方法高出11.3%，召回率达到90.1%。

---

## #3 — G-Designer: Architecting Multi-agent Communication Topologies via Graph Neural Networks

`A` Score: 8.97 | 2024-10-15

**Authors:** Guibin Zhang, Yanwei Yue, Xiangguo Sun, Guancheng Wan, Miao Yu, Junfeng Fang et al. (9 total)

**Categories:** cs.MA, cs.LG

**Scores:** Citation: 9.79 | Influential: 9.96 | Venue: 10.00 | Author: 7.15 | Recency: 5.00

**Links:** [arXiv](https://arxiv.org/abs/2410.11782) | [PDF](https://arxiv.org/pdf/2410.11782)

> 本文提出了G-Designer，一种利用图神经网络动态设计多智能体通信拓扑的自适应解决方案。该方法通过建模多智能体网络，解码出任务自适应的高性能通信协议，在多个基准测试中表现出色，并能有效减少token消耗，同时展现出对抗智能体对抗攻击的鲁棒性，优化了多智能体系统的部署。

---

## #4 — Cut the Crap: An Economical Communication Pipeline for LLM-based Multi-Agent Systems

`A` Score: 8.80 | 2024-10-03

**Authors:** Guibin Zhang, Yanwei Yue, Zhixun Li, Sukwon Yun, Guancheng Wan, Kun Wang et al. (9 total)

**Categories:** cs.MA, cs.LG

**Scores:** Citation: 9.88 | Influential: 9.86 | Venue: 10.00 | Author: 5.88 | Recency: 5.00

**Links:** [arXiv](https://arxiv.org/abs/2410.02506) | [PDF](https://arxiv.org/pdf/2410.02506)

> 本研究提出了 AgentPrune，一个经济高效且鲁棒的多智能体通信框架，旨在剪枝现有 LLM 多智能体管道中的冗余或恶意消息。该框架首次识别并定义了“通信冗余”问题，通过在时空消息传递图上进行一次性剪枝，显著降低了 token 成本。实验表明，该方法在保持高性能的同时，能有效防御两种基于智能体的对抗性攻击。

---

## #5 — Towards Low-Resource Harmful Meme Detection with LMM Agents

`A` Score: 8.74 | 2024-11-08

**Authors:** Jianzhao Huang, Hongzhan Lin, Ziyan Liu, Ziyang Luo, Guang Chen, Jing Ma

**Categories:** cs.CL

**Scores:** Citation: 8.98 | Influential: 9.86 | Venue: 10.00 | Author: 8.15 | Recency: 5.00

**Links:** [arXiv](https://arxiv.org/abs/2411.05383) | [PDF](https://arxiv.org/pdf/2411.05383)

> 本文提出了一种基于 LMM Agent 的低资源有害表情包检测框架，通过外向和内向分析结合少量标注样本进行识别。该方法利用大型多模态模型（LMM）的推理能力，首先检索相关表情包作为辅助信号，然后激发 Agent 的知识修订行为以获得泛化性强的有害性洞察。实验表明，该方法在三个表情包数据集上的低资源检测任务中表现优于现有最先进方法。

---

## #6 — Policy Compiler for Secure Agentic Systems

`A` Score: 8.66 | 2026-02-18

**Authors:** Nils Palumbo, Sarthak Choudhary, Jihye Choi, Prasad Chalasani, Somesh Jha

**Categories:** cs.CR, cs.AI, cs.MA

**Scores:** Citation: 9.71 | Influential: 9.02 | Venue: 2.00 | Author: 8.55 | Recency: 10.00

**Links:** [arXiv](https://arxiv.org/abs/2602.16708) | [PDF](https://arxiv.org/pdf/2602.16708)

> 提出PCAS，一个为智能体系统提供确定性策略执行的政策编译器。该系统通过依赖图建模智能体状态，使用Datalog语言表达策略，并通过参考监控器拦截违规行为。评估显示PCAS能显著提高政策合规性，且无需对模型推理进行安全特定的重构。

---

## #7 — Multi-Agent Risks from Advanced AI

`A` Score: 8.65 | 2025-02-19

**Authors:** Lewis Hammond, Alan Chan, Jesse Clifton, Jason Hoelscher-Obermaier, Akbir Khan, Euan McLean et al. (44 total)

**Categories:** cs.MA, cs.AI, cs.CY

**Scores:** Citation: 9.97 | Influential: 9.90 | Venue: 2.00 | Author: 9.88 | Recency: 5.00

**Links:** [arXiv](https://arxiv.org/abs/2502.14143) | [PDF](https://arxiv.org/pdf/2502.14143)

> 本文研究了高级AI代理带来的多代理系统风险，提出了结构化风险分类法，识别了三种关键故障模式（不协调、冲突和勾结）和七个关键风险因素。通过真实世界案例和实验证据，阐明了多代理系统对安全、治理和伦理的独特挑战，为理解和缓解这些复杂风险提供了系统框架。

---

## #8 — G-Safeguard: A Topology-Guided Security Lens and Treatment on LLM-based Multi-agent Systems

`A` Score: 8.60 | 2025-02-16

**Authors:** Shilong Wang, Guibin Zhang, Miao Yu, Guancheng Wan, Fanci Meng, Chongye Guo et al. (8 total)

**Categories:** cs.CR, cs.LG, cs.MA

**Scores:** Citation: 9.55 | Influential: 9.58 | Venue: 10.00 | Author: 5.88 | Recency: 5.00

**Links:** [arXiv](https://arxiv.org/abs/2502.11127) | [PDF](https://arxiv.org/pdf/2502.11127)

> 这篇论文提出了G-Safeguard，一种针对基于大型语言模型的多智能体系统的安全防护框架。该框架利用图神经网络检测多智能体交互拓扑中的异常行为，并通过拓扑干预技术有效缓解对抗攻击，实验证明其在提示注入攻击中可恢复超过40%的性能，同时保持对不同LLM架构和大规模系统的适应性。

---

## #9 — Securing the Model Context Protocol: Defending LLMs Against Tool Poisoning and Adversarial Attacks

`A` Score: 8.60 | 2025-12-06

**Authors:** Saeid Jamshidi, Kawser Wazed Nafi, Arghavan Moradi Dakhel, Negar Shahabi, Foutse Khomh, Naser Ezzati-Jivan

**Categories:** cs.CR, cs.AI

**Scores:** Citation: 9.38 | Influential: 9.02 | Venue: 2.00 | Author: 9.83 | Recency: 9.00

**Links:** [arXiv](https://arxiv.org/abs/2512.06556) | [PDF](https://arxiv.org/pdf/2512.06556)

> 论文分析了模型上下文协议（MCP）中的语义攻击，如工具投毒和影子攻击，并提出了一种分层安全防御框架。该框架通过清单签名、语义审查和启发式护栏，有效保护了基于MCP的系统免受恶意工具元数据的侵害，填补了工具交互安全的空白。

---

## #10 — MIND: A Multi-agent Framework for Zero-shot Harmful Meme Detection

`A` Score: 8.56 | 2025-07-09

**Authors:** Ziyan Liu, Chunxiao Fan, Haoran Lou, Yuexin Wu, Kaiwei Deng

**Categories:** cs.CL, cs.AI

**Scores:** Citation: 8.98 | Influential: 9.02 | Venue: 10.00 | Author: 6.75 | Recency: 7.00

**Links:** [arXiv](https://arxiv.org/abs/2507.06908) | [PDF](https://arxiv.org/pdf/2507.06908)

> 本文提出MIND多代理框架，实现零样本有害迷因检测，无需标注数据。MIND通过检索相似迷因提供上下文、双向洞察推导机制和多代理辩论确保稳健决策。实验表明，该框架优于现有零样本方法，在不同模型架构和参数规模上表现强大泛化能力，为社交媒体有害内容检测提供可扩展解决方案。

---

## #11 — Towards Verifiably Safe Tool Use for LLM Agents

`A` Score: 8.56 | 2026-01-12

**Authors:** Aarya Doshi, Yining Hong, Congying Xu, Eunsuk Kang, Alexandros Kapravelos, Christian Kästner

**Categories:** cs.SE

**Scores:** Citation: 9.62 | Influential: 9.02 | Venue: 2.00 | Author: 8.84 | Recency: 9.00

**Links:** [arXiv](https://arxiv.org/abs/2601.08012) | [PDF](https://arxiv.org/pdf/2601.08012)

> 本文提出了一种基于系统理论过程分析（STPA）的流程，用于识别Agent工作流中的危害并将安全需求形式化为可执行的规范。作者引入了增强型模型上下文协议（MCP）框架，通过结构化标签确保工具使用的安全性。该方法旨在将LLM Agent的安全性从临时的可靠性修复转变为具有形式化保证的主动护栏，减少对用户确认的依赖。

---

## #12 — ToolSafe: Enhancing Tool Invocation Safety of LLM-based agents via Proactive Step-level Guardrail and Feedback

`A` Score: 8.52 | 2026-01-15

**Authors:** Yutao Mou, Zhangchi Xue, Lijun Li, Peiyang Liu, Shikun Zhang, Wei Ye et al. (7 total)

**Categories:** cs.CL

**Scores:** Citation: 9.49 | Influential: 9.02 | Venue: 2.00 | Author: 9.01 | Recency: 9.00

**Links:** [arXiv](https://arxiv.org/abs/2601.10156) | [PDF](https://arxiv.org/pdf/2601.10156)

> ToolSafe 提出了一种通过主动步骤级护栏和反馈来增强 LLM Agent 工具调用安全性的框架。该研究构建了 TS-Bench 基准，并开发了 TS-Guard 模型，有效减少了有害工具调用并提高了良性任务完成率，确保了 Agent 部署时的实时安全监控。

---

## #13 — Safety Guardrails for LLM-Enabled Robots

`A` Score: 8.48 | 2025-03-10

**Authors:** Zachary Ravichandran, Alexander Robey, Vijay Kumar, George J. Pappas, Hamed Hassani

**Categories:** cs.RO, cs.AI

**Scores:** Citation: 9.51 | Influential: 9.58 | Venue: 5.00 | Author: 8.55 | Recency: 5.00

**Links:** [arXiv](https://arxiv.org/abs/2503.07885) | [PDF](https://arxiv.org/pdf/2503.07885)

> 论文提出RoboGuard，一个两级护栏架构，确保LLM赋能机器人的安全。RoboGuard首先使用可信LLM将预定义安全规则与机器人环境相关联，生成上下文相关的安全规范；然后使用时序逻辑控制合成解决这些规范与潜在不安全计划之间的冲突。实验表明，RoboGuard将不安全计划的执行率从92%以上降低到3%以下，而不影响安全计划的性能。

---

## #14 — The Task Shield: Enforcing Task Alignment to Defend Against Indirect Prompt Injection in LLM Agents

`A` Score: 8.46 | 2024-12-21

**Authors:** Feiran Jia, Tong Wu, Xin Qin, Anna Squicciarini

**Categories:** cs.CR, cs.AI, cs.CL

**Scores:** Citation: 9.57 | Influential: 9.69 | Venue: 10.00 | Author: 4.79 | Recency: 5.00

**Links:** [arXiv](https://arxiv.org/abs/2412.16682) | [PDF](https://arxiv.org/pdf/2412.16682)

> 针对LLM智能体面临的间接提示注入攻击，本文提出了Task Shield防御机制。该方法将安全重构为任务对齐问题，在测试时系统性地验证每条指令和工具调用是否符合用户目标，在AgentDojo基准测试中显著降低了攻击成功率并保持了高任务效用，提供了一种新的安全防御视角。

---

## #15 — Uncovering Security Threats and Architecting Defenses in Autonomous Agents: A Case Study of OpenClaw

`A` Score: 8.44 | 2026-03-13

**Authors:** Zonghao Ying, Xiao Yang, Siyang Wu, Yumeng Song, Yang Qu, Hainan Li et al. (10 total)

**Categories:** cs.CR

**Scores:** Citation: 9.76 | Influential: 7.81 | Venue: 2.00 | Author: 8.55 | Recency: 10.00

**Links:** [arXiv](https://arxiv.org/abs/2603.12644) | [PDF](https://arxiv.org/pdf/2603.12644)

> 本文对OpenClaw生态系统进行了全面的安全分析，揭示了提示注入驱动的远程代码执行等关键漏洞。提出了全生命周期Agent安全架构（FASA），倡导零信任执行和动态意图验证，旨在解决自主Agent的系统性架构缺陷。该研究为构建值得信赖的自主Agent提供了理论蓝图和工程方向。

---

## #16 — VeriGuard: Enhancing LLM Agent Safety via Verified Code Generation

`A` Score: 8.40 | 2025-10-03

**Authors:** Lesly Miculicich, Mihir Parmar, Hamid Palangi, Krishnamurthy Dj Dvijotham, Mirko Montanari, Tomas Pfister et al. (7 total)

**Categories:** cs.SE, cs.AI, cs.CR

**Scores:** Citation: 9.52 | Influential: 9.02 | Venue: 2.00 | Author: 9.41 | Recency: 7.00

**Links:** [arXiv](https://arxiv.org/abs/2510.05156) | [PDF](https://arxiv.org/pdf/2510.05156)

> 本文介绍了VeriGuard，一种通过双阶段架构为基于LLM的智能体提供形式化安全保证的框架。该框架首先在离线阶段通过形式化验证合成并验证行为策略，随后在在线阶段作为运行时监控器验证每个拟议的智能体动作。这种离线验证与在线监控的分离设计，使得形式化保证能够实际应用于敏感领域的智能体，显著提升了其可信度。

---

## #17 — A Survey on Autonomy-Induced Security Risks in Large Model-Based Agents

`A` Score: 8.31 | 2025-06-30

**Authors:** Hang Su, Jun Luo, Chang Liu, Xiao Yang, Yichi Zhang, Yinpeng Dong et al. (7 total)

**Categories:** cs.AI

**Scores:** Citation: 9.22 | Influential: 9.02 | Venue: 2.00 | Author: 9.71 | Recency: 7.00

**Links:** [arXiv](https://arxiv.org/abs/2506.23844) | [PDF](https://arxiv.org/pdf/2506.23844)

> 本文综述了基于大模型的自主智能体因自主性提升而引发的新型安全风险，如记忆中毒、工具滥用和奖励黑客等。文章分析了智能体架构中的脆弱性，并系统回顾了针对感知、认知、记忆和行动模块的防御策略，提出了反思性风险感知框架。

---

## #18 — Superintelligent Agents Pose Catastrophic Risks: Can Scientist AI Offer a Safer Path?

`A` Score: 8.26 | 2025-02-21

**Authors:** Yoshua Bengio, Michael Cohen, Damiano Fornasiere, Joumana Ghosn, Pietro Greiner, Matt MacDermott et al. (13 total)

**Categories:** cs.AI, cs.LG

**Scores:** Citation: 9.91 | Influential: 9.96 | Venue: 2.00 | Author: 7.43 | Recency: 5.00

**Links:** [arXiv](https://arxiv.org/abs/2502.15657) | [PDF](https://arxiv.org/pdf/2502.15657)

> 本文讨论了通用AI代理带来的风险，指出不受控制的AI代理可能对公共安全和安全构成重大威胁。作者分析了这些风险如何从当前的AI训练方法中产生，并提出了'科学家AI'作为替代方案，这是一种非代理AI系统，旨在解释世界而非采取行动。该系统包含一个生成理论来解释数据的世界模型和一个带有不确定性概念的问答推理机，为AI安全发展提供了新思路。

---

## #19 — AgentSpec: Customizable Runtime Enforcement for Safe and Reliable LLM Agents

`A` Score: 8.25 | 2025-03-24

**Authors:** Haoyu Wang, Christopher M. Poskitt, Jun Sun

**Categories:** cs.AI, cs.CL

**Scores:** Citation: 9.87 | Influential: 9.69 | Venue: 2.00 | Author: 7.80 | Recency: 5.00

**Links:** [arXiv](https://arxiv.org/abs/2503.18666) | [PDF](https://arxiv.org/pdf/2503.18666)

> 本文提出了AgentSpec，一种轻量级领域特定语言，用于指定和强制执行LLM代理的运行时约束。用户可定义包含触发器、谓词和执行机制的结构化规则，确保代理在预定义安全边界内运行。在代码执行、具身代理和自动驾驶等多个领域的实现展示了其适应性和有效性。评估显示，AgentSpec成功防止了90%以上的代码代理不安全执行，消除了具身代理任务中的所有危险行动，确保自动驾驶100%合规，同时保持毫秒级计算开销，为LLM代理安全提供了实用可扩展的解决方案。

---

## #20 — OS-Sentinel: Towards Safety-Enhanced Mobile GUI Agents via Hybrid Validation in Realistic Workflows

`A` Score: 8.25 | 2025-10-28

**Authors:** Qiushi Sun, Mukai Li, Zhoumianze Liu, Zhihui Xie, Fangzhi Xu, Zhangyue Yin et al. (14 total)

**Categories:** cs.AI, cs.CL, cs.CV

**Scores:** Citation: 9.21 | Influential: 9.02 | Venue: 2.00 | Author: 7.99 | Recency: 9.00

**Links:** [arXiv](https://arxiv.org/abs/2510.24411) | [PDF](https://arxiv.org/pdf/2510.24411)

> 针对移动GUI Agent的安全隐患，本文提出了MobileRisk-Live动态沙箱环境及安全检测基准。在此基础上，开发了OS-Sentinel混合安全检测框架，结合形式化验证器和基于VLM的上下文判断器，有效检测系统违规和上下文风险，显著提升了移动Agent的安全性。

---

## #21 — Multi-Agent Security Tax: Trading Off Security and Collaboration Capabilities in Multi-Agent Systems

`A` Score: 8.22 | 2025-02-26

**Authors:** Pierre Peigne-Lefebvre, Mikolaj Kniejski, Filip Sondej, Matthieu David, Jason Hoelscher-Obermaier, Christian Schroeder de Witt et al. (7 total)

**Categories:** cs.AI, cs.MA

**Scores:** Citation: 8.96 | Influential: 9.39 | Venue: 10.00 | Author: 5.40 | Recency: 5.00

**Links:** [arXiv](https://arxiv.org/abs/2502.19145) | [PDF](https://arxiv.org/pdf/2502.19145)

> 该研究开发了模拟智能体协作的仿真，研究安全风险和权衡。观察到恶意提示的传染性，评估了'疫苗接种'和通用安全指令等防御策略。研究发现这些防御减少了恶意指令的传播，但往往降低了智能体网络的协作能力，揭示了多智能体系统中安全与协作效率之间的潜在权衡。

---

## #22 — LlamaFirewall: An open source guardrail system for building secure AI agents

`B` Score: 8.22 | 2025-05-06

**Authors:** Sahana Chennabasappa, Cyrus Nikolaidis, Daniel Song, David Molnar, Stephanie Ding, Shengye Wan et al. (19 total)

**Categories:** cs.CR, cs.AI

**Scores:** Citation: 9.92 | Influential: 9.86 | Venue: 2.00 | Author: 5.88 | Recency: 7.00

**Links:** [arXiv](https://arxiv.org/abs/2505.03574) | [PDF](https://arxiv.org/pdf/2505.03574)

> 针对AI智能体面临的新型安全风险，本文提出了LlamaFirewall开源护栏框架，作为构建安全智能体的最后一道防线。该框架包含通用越狱检测器、智能体对齐检查器和在线静态分析引擎，有效缓解了提示注入、目标错位和不安全代码等风险，支持系统级安全策略的定义与执行。

---

## #23 — Reinforced Internal-External Knowledge Synergistic Reasoning for Efficient Adaptive Search Agent

`B` Score: 8.21 | 2025-05-12

**Authors:** Ziyang Huang, Xiaowei Yuan, Yiming Ju, Jun Zhao, Kang Liu

**Categories:** cs.CL, cs.AI

**Scores:** Citation: 8.99 | Influential: 9.58 | Venue: 2.00 | Author: 9.01 | Recency: 7.00

**Links:** [arXiv](https://arxiv.org/abs/2505.07596) | [PDF](https://arxiv.org/pdf/2505.07596)

> 本文提出了IKEA智能体，通过强化学习实现内部知识与外部检索的协同推理。该智能体能够识别自身知识边界，优先利用内部知识，仅在知识不足时才进行外部搜索，从而减少冗余检索和推理延迟。实验表明，IKEA在多个知识推理任务中显著优于基线方法，具有强大的泛化能力。

---

## #24 — ResMAS: Resilience Optimization in LLM-based Multi-agent Systems

`B` Score: 8.21 | 2026-01-08

**Authors:** Zhilun Zhou, Zihan Liu, Jiahe Liu, Qingyu Shao, Yihan Wang, Kun Shao et al. (8 total)

**Categories:** cs.AI

**Scores:** Citation: 7.25 | Influential: 7.81 | Venue: 10.00 | Author: 9.92 | Recency: 9.00

**Links:** [arXiv](https://arxiv.org/abs/2601.04694) | [PDF](https://arxiv.org/pdf/2601.04694)

> 本文提出了ResMAS框架，通过强化学习生成弹性拓扑结构并优化提示，以增强基于大语言模型的多智能体系统在扰动下的韧性。实验表明，该方法在各种约束下显著提高了系统的鲁棒性和泛化能力，为构建具有内在弹性的多智能体系统提供了新思路。

---

## #25 — Open Challenges in Multi-Agent Security: Towards Secure Systems of Interacting AI Agents

`B` Score: 8.14 | 2025-05-04

**Authors:** Christian Schroeder de Witt

**Categories:** cs.CR, cs.AI, cs.MA

**Scores:** Citation: 9.90 | Influential: 9.86 | Venue: 2.00 | Author: 5.40 | Recency: 7.00

**Links:** [arXiv](https://arxiv.org/abs/2505.02077) | [PDF](https://arxiv.org/pdf/2505.02077)

> 本文定义了“多智能体安全”这一新领域，旨在解决去中心化AI智能体交互网络中涌现的安全挑战。研究对威胁景观进行了分类，调查了去中心化AI系统中的安全与性能权衡，并提出了设计安全智能体系统和交互环境的统一研究议程，为应对系统性威胁提供了理论指导。

---

## #26 — Securing Agentic AI: A Comprehensive Threat Model and Mitigation Framework for Generative AI Agents

`B` Score: 8.12 | 2025-04-28

**Authors:** Vineeth Sai Narajala, Om Narayan

**Categories:** cs.CR, cs.AI

**Scores:** Citation: 9.70 | Influential: 9.58 | Venue: 5.00 | Author: 4.27 | Recency: 7.00

**Links:** [arXiv](https://arxiv.org/abs/2504.19956) | [PDF](https://arxiv.org/pdf/2504.19956)

> 本文针对生成式AI智能体提出了一个全面的威胁模型，重点关注其自主性、持久记忆和工具集成带来的新型风险。研究识别了跨越认知架构、时间持久性、操作执行等五个领域的九大主要威胁，并提出了ATFAA威胁框架和SHIELD缓解框架。该工作强调了智能体与传统系统的安全差异，为降低企业风险提供了实用策略。

---

## #27 — We Should Identify and Mitigate Third-Party Safety Risks in MCP-Powered Agent Systems

`B` Score: 8.12 | 2025-06-16

**Authors:** Junfeng Fang, Zijun Yao, Ruipeng Wang, Haokai Ma, Xiang Wang, Tat-Seng Chua

**Categories:** cs.LG, cs.AI

**Scores:** Citation: 9.72 | Influential: 9.39 | Venue: 2.00 | Author: 6.47 | Recency: 7.00

**Links:** [arXiv](https://arxiv.org/abs/2506.13666) | [PDF](https://arxiv.org/pdf/2506.13666)

> 本文探讨了模型上下文协议（MCP）引入的第三方服务带来的安全风险，指出这些服务可能具有恶意动机并利用漏洞破坏用户交互。作者构建了一个受控框架来检查MCP驱动的Agent系统中的安全问题，并通过试点实验证明了这些风险的真实性。最后，文章提出了构建安全MCP驱动系统的路线图，呼吁社区关注这一新方向。

---

## #28 — Your Agent May Misevolve: Emergent Risks in Self-evolving LLM Agents

`B` Score: 8.10 | 2025-09-30

**Authors:** Shuai Shao, Qihan Ren, Chen Qian, Boyi Wei, Dadi Guo, Jingyi Yang et al. (11 total)

**Categories:** cs.AI, cs.CL, cs.LG

**Scores:** Citation: 9.58 | Influential: 9.58 | Venue: 2.00 | Author: 6.47 | Recency: 7.00

**Links:** [arXiv](https://arxiv.org/abs/2509.26354) | [PDF](https://arxiv.org/pdf/2509.26354)

> 本文研究了自进化 LLM 代理中的“错误进化”风险，即代理在自我改进过程中偏离预期导致有害结果。通过评估模型、记忆、工具和工作流四个进化路径，研究发现即使在顶级 LLM 上构建的代理也普遍存在安全对齐退化等风险，强调了建立新安全范式以应对自进化代理潜在威胁的紧迫性。

---

## #29 — Enforcing Temporal Constraints for LLM Agents

`B` Score: 8.00 | 2025-12-25

**Authors:** Adharsh Kamath, Sishen Zhang, Calvin Xu, Shubham Ugare, Gagandeep Singh, Sasa Misailovic

**Categories:** cs.PL, cs.AI, cs.FL

**Scores:** Citation: 8.84 | Influential: 7.81 | Venue: 2.00 | Author: 9.09 | Recency: 9.00

**Links:** [arXiv](https://arxiv.org/abs/2512.23738) | [PDF](https://arxiv.org/pdf/2512.23738)

> 本文提出了Agent-C框架，旨在确保基于LLM的智能体在运行时遵守形式化的时序安全属性（如先认证后访问数据）。该框架引入领域特定语言表达时序属性，利用SMT求解检测不合规操作，并通过约束生成技术强制智能体执行符合规范的替代动作。实验证明Agent-C能有效防止安全关键应用中的时序违规行为。

---

## #30 — When Only the Final Text Survives: Implicit Execution Tracing for Multi-Agent Attribution

`B` Score: 8.00 | 2026-03-18

**Authors:** Yi Nian, Haosen Cao, Shenzhe Zhu, Henry Peng Zou, Qingqing Luan, Yue Zhao

**Categories:** cs.AI, cs.CL

**Scores:** Citation: 9.25 | Influential: 7.81 | Venue: 2.00 | Author: 7.15 | Recency: 10.00

**Links:** [arXiv](https://arxiv.org/abs/2603.17445) | [PDF](https://arxiv.org/pdf/2603.17445)

> 本文提出了IET，一种在执行元数据不可用的情况下，通过最终文本进行多智能体归因的框架。该方法将特定于智能体的统计信号直接嵌入到令牌生成过程中，将输出文本转换为自验证的执行记录，从而在隐私保护或系统边界限制下实现可靠的问责。

---

## #31 — Agentic AI Frameworks: Architectures, Protocols, and Design Challenges

`B` Score: 7.99 | 2025-08-13

**Authors:** Hana Derouiche, Zaki Brahmi, Haithem Mazeni

**Categories:** cs.AI

**Scores:** Citation: 9.53 | Influential: 9.39 | Venue: 2.00 | Author: 6.17 | Recency: 7.00

**Links:** [arXiv](https://arxiv.org/abs/2508.10146) | [PDF](https://arxiv.org/pdf/2508.10146)

> 本文对领先的 Agentic AI 框架（如 CrewAI、LangGraph、AutoGen 等）进行了系统综述和比较分析，评估了其架构原则、通信机制、内存管理和安全护栏。研究深入分析了代理通信协议，指出了当前框架在可扩展性、鲁棒性和互操作性方面的关键限制和挑战。该工作为研究人员和从业者提供了全面的参考，并提出了增强自主 AI 系统的未来研究方向。

---

## #32 — RTBAS: Defending LLM Agents Against Prompt Injection and Privacy Leakage

`B` Score: 7.98 | 2025-02-13

**Authors:** Peter Yong Zhong, Siyuan Chen, Ruiqi Wang, McKenna McCall, Ben L. Titzer, Heather Miller et al. (7 total)

**Categories:** cs.CR, cs.AI

**Scores:** Citation: 9.58 | Influential: 9.77 | Venue: 2.00 | Author: 6.75 | Recency: 5.00

**Links:** [arXiv](https://arxiv.org/abs/2502.08966) | [PDF](https://arxiv.org/pdf/2502.08966)

> RTBAS保护LLM代理免受提示注入和隐私泄露，自动检测和执行保持完整性的工具调用，仅在必要时要求用户确认。该方法将信息流控制适应TBAS挑战，提出两种新型依赖筛选器。实验显示RTBAS在受攻击时防止所有针对性攻击，仅损失2%任务效用，并能检测微妙和直接隐私泄露，为代理系统提供高效安全保障。

---

## #33 — Infrastructure for AI Agents

`B` Score: 7.94 | 2025-01-17

**Authors:** Alan Chan, Kevin Wei, Sihao Huang, Nitarshan Rajkumar, Elija Perrier, Seth Lazar et al. (8 total)

**Categories:** cs.AI

**Scores:** Citation: 9.31 | Influential: 9.02 | Venue: 2.00 | Author: 8.33 | Recency: 5.00

**Links:** [arXiv](https://arxiv.org/abs/2501.10114) | [PDF](https://arxiv.org/pdf/2501.10114)

> 这篇论文探讨了AI代理基础设施的重要性，指出当前研究多集中于直接修改代理行为，而忽视了异构代理间的交互问题。作者提出需要建立外部协议和系统来规范代理间的通信、协议达成和责任归属，以促进安全有效的代理交互并建立信任。这一'代理基础设施'概念旨在通过技术手段和共享协议调解和影响代理的交互及其影响。

---

## #34 — Ambig-SWE: Interactive Agents to Overcome Underspecificity in Software Engineering

`B` Score: 7.88 | 2025-02-18

**Authors:** Sanidhya Vijayvargiya, Xuhui Zhou, Akhila Yerukola, Maarten Sap, Graham Neubig

**Categories:** cs.AI

**Scores:** Citation: 8.67 | Influential: 9.02 | Venue: 2.00 | Author: 9.86 | Recency: 5.00

**Links:** [arXiv](https://arxiv.org/abs/2502.13069) | [PDF](https://arxiv.org/pdf/2502.13069)

> 本文研究了AI代理处理模糊用户指令的能力，引入Ambig-SWE基准测试评估代理在模糊性和交互性下的表现。研究发现模型难以区分明确和模糊指令，但通过交互能有效获取关键信息，性能提升高达74%，揭示了当前模型在处理软件工程任务中缺失信息时的关键差距。

---

## #35 — SAFEFLOW: A Principled Protocol for Trustworthy and Transactional Autonomous Agent Systems

`B` Score: 7.87 | 2025-06-09

**Authors:** Peiran Li, Xinkai Zou, Zhuohang Wu, Ruifeng Li, Shuo Xing, Hanwen Zheng et al. (12 total)

**Categories:** cs.AI, cs.CL

**Scores:** Citation: 9.15 | Influential: 9.39 | Venue: 2.00 | Author: 6.47 | Recency: 7.00

**Links:** [arXiv](https://arxiv.org/abs/2506.07564) | [PDF](https://arxiv.org/pdf/2506.07564)

> 本文提出了SAFEFLOW协议级框架，用于构建可信的LLM/VLM智能体。该框架通过强制细粒度的信息流控制来跟踪数据来源和完整性，并引入事务执行机制，确保在多智能体并发环境下的安全性和一致性。

---

## #36 — A Framework for Formalizing LLM Agent Security

`B` Score: 7.83 | 2026-03-19

**Authors:** Vincent Siu, Jingxuan He, Kyle Montgomery, Zhun Wang, Neil Gong, Chenguang Wang et al. (7 total)

**Categories:** cs.CR, cs.AI

**Scores:** Citation: 9.30 | Influential: 7.81 | Venue: 2.00 | Author: 5.88 | Recency: 10.00

**Links:** [arXiv](https://arxiv.org/abs/2603.19469) | [PDF](https://arxiv.org/pdf/2603.19469)

> 本文提出了一个形式化LLM智能体安全的框架，从上下文安全的角度系统化了现有的攻击和防御。该框架定义了任务对齐、动作对齐、源授权和数据隔离四个安全属性，并引入预言机函数来验证违规行为。该框架有助于解决安全与效用之间的权衡问题，为防御策略提供理论基础。

---

## #37 — AgentSentinel: An End-to-End and Real-Time Security Defense Framework for Computer-Use Agents

`B` Score: 7.68 | 2025-09-09

**Authors:** Haitao Hu, Peng Chen, Yanpeng Zhao, Yuqi Chen

**Categories:** cs.CR

**Scores:** Citation: 9.13 | Influential: 7.81 | Venue: 5.00 | Author: 5.40 | Recency: 7.00

**Links:** [arXiv](https://arxiv.org/abs/2509.07764) | [PDF](https://arxiv.org/pdf/2509.07764)

> 本文提出了 AgentSentinel，一个端到端的实时安全防御框架，旨在缓解计算机使用 Agent 因 LLM 输出不稳定而导致的潜在安全威胁。该框架通过拦截敏感操作并关联任务上下文与系统痕迹进行安全审计，在包含 60 种攻击场景的基准测试中表现出优异的防御效果。

---

## #38 — LLM Agents Should Employ Security Principles

`B` Score: 7.62 | 2025-05-29

**Authors:** Kaiyuan Zhang, Zian Su, Pin-Yu Chen, Elisa Bertino, Xiangyu Zhang, Ninghui Li

**Categories:** cs.CR, cs.AI

**Scores:** Citation: 9.09 | Influential: 7.81 | Venue: 2.00 | Author: 7.15 | Recency: 7.00

**Links:** [arXiv](https://arxiv.org/abs/2505.24019) | [PDF](https://arxiv.org/pdf/2505.24019)

> 这篇观点论文主张在部署大语言模型智能体时应采用信息安全设计原则，如纵深防御和最小权限。作者介绍了 AgentSandbox 概念框架，将这些原则嵌入智能体生命周期，在保持高实用性的同时显著缓解隐私泄露和系统利用等风险。

---

## #39 — NetSafe: Exploring the Topological Safety of Multi-agent Networks

`B` Score: 7.62 | 2024-10-21

**Authors:** Miao Yu, Shilong Wang, Guibin Zhang, Junyuan Mao, Chenlong Yin, Qijiong Liu et al. (9 total)

**Categories:** cs.MA, cs.AI

**Scores:** Citation: 9.04 | Influential: 9.39 | Venue: 2.00 | Author: 6.47 | Recency: 5.00

**Links:** [arXiv](https://arxiv.org/abs/2410.15686) | [PDF](https://arxiv.org/pdf/2410.15686)

> 本文从拓扑角度探讨了多智能体网络的安全性，提出了NetSafe框架来统一现有的基于LLM的智能体框架。研究发现高度连接的网络更容易受到对抗性攻击的传播影响，并识别了“智能体幻觉”和“聚合安全”等关键现象，为未来构建更安全的LLM多智能体网络奠定了基础。

---

## #40 — The AI Agent Index

`B` Score: 7.60 | 2025-02-03

**Authors:** Stephen Casper, Luke Bailey, Rosco Hunter, Carson Ezell, Emma Cabalé, Michael Gerovitch et al. (15 total)

**Categories:** cs.SE, cs.AI

**Scores:** Citation: 9.26 | Influential: 9.02 | Venue: 2.00 | Author: 6.17 | Recency: 5.00

**Links:** [arXiv](https://arxiv.org/abs/2502.01635) | [PDF](https://arxiv.org/pdf/2502.01635)

> 本文介绍了AI Agent Index，首个记录当前部署AI代理系统信息的公开数据库。面对日益增多的自主规划执行复杂任务的AI系统，业界缺乏结构化框架记录其技术组件、应用场景和安全特性。该索引系统性地收集整理各AI代理的基础模型、推理机制、工具使用能力、应用领域及风险管理实践，通过公开资料和开发者访谈获取数据，揭示开发者虽乐于分享系统能力信息，但在安全细节披露方面仍显不足。

---

## #41 — Autonomous Data Agents: A New Opportunity for Smart Data

`B` Score: 7.59 | 2025-09-23

**Authors:** Yanjie Fu, Dongjie Wang, Wangyang Ying, Xinyuan Wang, Xiangliang Zhang, Huan Liu et al. (7 total)

**Categories:** cs.AI

**Scores:** Citation: 8.50 | Influential: 7.81 | Venue: 2.00 | Author: 8.65 | Recency: 7.00

**Links:** [arXiv](https://arxiv.org/abs/2509.18710) | [PDF](https://arxiv.org/pdf/2509.18710)

> 本文提出了自主数据智能体的概念，这是一种集成大语言模型推理与工具调用的新型系统。DataAgents能够自主解释任务、分解子任务并动态规划工作流，将复杂非结构化数据转化为可操作的知识。该研究代表了从传统数据管理向自主数据-知识系统的范式转变。

---

## #42 — AgenTRIM: Tool Risk Mitigation for Agentic AI

`B` Score: 7.59 | 2026-01-18

**Authors:** Roy Betser, Shamik Bose, Amit Giloni, Chiara Picardi, Sindhu Padakandla, Roman Vainshtein

**Categories:** cs.CR, cs.AI

**Scores:** Citation: 9.14 | Influential: 9.02 | Venue: 2.00 | Author: 3.78 | Recency: 9.00

**Links:** [arXiv](https://arxiv.org/abs/2601.12449) | [PDF](https://arxiv.org/pdf/2601.12449)

> AgenTRIM 是一个用于缓解 AI Agent 工具风险的框架，通过离线验证和在线最小权限过滤来检测并防御工具滥用。该框架在不改变 Agent 内部推理的情况下，显著降低了攻击成功率并保持了任务性能，为更安全的工具使用提供了实用方案。

---

## #43 — Check Yourself Before You Wreck Yourself: Selectively Quitting Improves LLM Agent Safety

`B` Score: 7.55 | 2025-10-18

**Authors:** Vamshi Krishna Bonagiri, Ponnurangam Kumaragurum, Khanh Nguyen, Benjamin Plaut

**Categories:** cs.CL

**Scores:** Citation: 8.05 | Influential: 7.81 | Venue: 2.00 | Author: 9.77 | Recency: 7.00

**Links:** [arXiv](https://arxiv.org/abs/2510.16492) | [PDF](https://arxiv.org/pdf/2510.16492)

> 该研究提出将“退出”作为一种行为机制，使 LLM 智能体在缺乏信心时能够主动撤回。通过在 ToolEmu 框架下的系统评估，证明显式的退出指令能显著提升智能体的安全性，同时保持极小的实用性损失，是高风险应用中的有效一线防御。

---

## #44 — Multi-Agent Systems Execute Arbitrary Malicious Code

`B` Score: 7.54 | 2025-03-15

**Authors:** Harold Triedman, Rishi Jha, Vitaly Shmatikov

**Categories:** cs.CR, cs.LG

**Scores:** Citation: 9.59 | Influential: 9.39 | Venue: 2.00 | Author: 4.27 | Recency: 5.00

**Links:** [arXiv](https://arxiv.org/abs/2503.12188) | [PDF](https://arxiv.org/pdf/2503.12188)

> 研究展示多代理系统如何被恶意内容劫持控制，导致执行任意恶意代码或窃取敏感数据。实验表明基于Web的攻击在58-90%的试验中成功导致系统执行恶意代码，某些配置下成功率高达100%。即使单个代理不易受提示注入，攻击仍可能成功，突显了多代理系统部署前的安全挑战。

---

## #45 — ACE: A Security Architecture for LLM-Integrated App Systems

`B` Score: 7.51 | 2025-04-29

**Authors:** Evan Li, Tushin Mallick, Evan Rose, William Robertson, Alina Oprea, Cristina Nita-Rotaru

**Categories:** cs.CR, cs.LG

**Scores:** Citation: 9.12 | Influential: 9.69 | Venue: 2.00 | Author: 3.78 | Recency: 7.00

**Links:** [arXiv](https://arxiv.org/abs/2504.20984) | [PDF](https://arxiv.org/pdf/2504.20984)

> 本文提出了ACE，一种面向LLM集成应用系统的安全架构，旨在解决恶意应用导致的完整性和可用性破坏问题。ACE通过将规划解耦为仅使用可信信息的抽象阶段和映射到具体应用的具象阶段，并利用静态分析验证安全信息流约束。实验表明，该架构能有效防御间接提示注入等攻击，保障系统安全。

---

## #46 — Towards Trustworthy GUI Agents: A Survey

`B` Score: 7.47 | 2025-03-30

**Authors:** Yucheng Shi, Wenhao Yu, Jingyuan Huang, Wenlin Yao, Wenhu Chen, Ninghao Liu

**Categories:** cs.LG

**Scores:** Citation: 9.42 | Influential: 7.81 | Venue: 2.00 | Author: 6.47 | Recency: 5.00

**Links:** [arXiv](https://arxiv.org/abs/2503.23434) | [PDF](https://arxiv.org/pdf/2503.23434)

> 本文调查了图形用户界面(GUI)代理的可信性问题，确定了执行差距作为构建可信GUI代理的关键挑战：在动态、部分可观察界面中感知、推理和交互之间的不一致。作者引入了工作流对齐的分类法，将信任分解为感知信任、推理信任和交互信任，展示了故障如何在代理管道中传播并通过动作/观察循环复合。文章系统性地审查了每个阶段的良性故障模式和对抗攻击，以及针对GUI设置的相应防御机制，强调了任务完成不足以评估信任的观点。

---

## #47 — SoK: The Attack Surface of Agentic AI -- Tools, and Autonomy

`B` Score: 7.47 | 2026-03-24

**Authors:** Ali Dehghantanha, Sajad Homayoun

**Categories:** cs.CR

**Scores:** Citation: 8.50 | Influential: 7.81 | Venue: 2.00 | Author: 5.88 | Recency: 10.00

**Links:** [arXiv](https://arxiv.org/abs/2603.22928) | [PDF](https://arxiv.org/pdf/2603.22928)

> 本文系统化地梳理了基于 LLM 的 Agent AI 系统的信任边界和安全风险，提出了涵盖提示注入、知识库中毒、工具利用和多智能体威胁的综合攻击分类法。通过文献综述，作者分析了 Agent 系统引入的新攻击向量，定义了攻击者模型和威胁场景，并提出了评估安全态势的指标。文章还评估了现有防御措施的有效性，并为部署 Agent AI 提供了分阶段的安全检查清单。

---

## #48 — Safety Aware Task Planning via Large Language Models in Robotics

`B` Score: 7.44 | 2025-03-19

**Authors:** Azal Ahmad Khan, Michael Andrev, Muhammad Ali Murtaza, Sergio Aguilera, Rui Zhang, Jie Ding et al. (8 total)

**Categories:** cs.RO, cs.AI

**Scores:** Citation: 9.23 | Influential: 9.02 | Venue: 5.00 | Author: 3.23 | Recency: 5.00

**Links:** [arXiv](https://arxiv.org/abs/2503.15707) | [PDF](https://arxiv.org/pdf/2503.15707)

> SAFER是一个多LLM框架，将安全意识嵌入机器人任务规划，采用安全代理与主任务规划器协同工作，提供安全反馈。框架集成实时风险评估、主动错误纠正和透明安全评估，结合控制屏障函数确保安全保证。实验证明其在复杂长周期任务中能有效减少安全违规，同时保持任务效率。

---

## #49 — A Safety and Security Framework for Real-World Agentic Systems

`B` Score: 7.42 | 2025-11-27

**Authors:** Shaona Ghosh, Barnaby Simkin, Kyriacos Shiarlis, Soumili Nandi, Dan Zhao, Matthew Fiedler et al. (12 total)

**Categories:** cs.LG, cs.AI, cs.CR

**Scores:** Citation: 8.08 | Influential: 9.02 | Venue: 2.00 | Author: 5.88 | Recency: 9.00

**Links:** [arXiv](https://arxiv.org/abs/2511.21990) | [PDF](https://arxiv.org/pdf/2511.21990)

> 本文提出了一个针对企业级 Agent 系统的动态安全框架，将安全和安全视为模型、编排器和工具之间动态交互的涌现属性。该框架定义了统一的 Agent 风险分类体系，并利用辅助 AI 模型和人工监督进行上下文风险发现与缓解，通过案例研究展示了其在实际部署中的有效性。

---

## #50 — Institutional AI: Governing LLM Collusion in Multi-Agent Cournot Markets via Public Governance Graphs

`B` Score: 7.40 | 2026-01-16

**Authors:** Marcantonio Bracale Syrnikov, Federico Pierucci, Marcello Galisai, Matteo Prandi, Piercosma Bisconti, Francesco Giarrusso et al. (9 total)

**Categories:** cs.GT, cs.AI

**Scores:** Citation: 9.11 | Influential: 7.81 | Venue: 2.00 | Author: 4.27 | Recency: 9.00

**Links:** [arXiv](https://arxiv.org/abs/2601.11369) | [PDF](https://arxiv.org/pdf/2601.11369)

> 本文提出了 Institutional AI 框架，通过公共治理图和机制设计来防止多智能体 LLM 在市场环境中的合谋行为。实验表明，该框架相比仅基于提示的宪法方法，能显著降低合谋发生率并确保系统安全，验证了机制设计在多智能体对齐中的有效性。

---

## #51 — Prompt Flow Integrity to Prevent Privilege Escalation in LLM Agents

`B` Score: 7.38 | 2025-03-17

**Authors:** Juhee Kim, Woohyuk Choi, Byoungyoung Lee

**Categories:** cs.CR, cs.AI, cs.MA

**Scores:** Citation: 9.73 | Influential: 9.58 | Venue: 2.00 | Author: 2.55 | Recency: 5.00

**Links:** [arXiv](https://arxiv.org/abs/2503.15547) | [PDF](https://arxiv.org/pdf/2503.15547)

> 提示流完整性(PFI)是一种面向系统安全的解决方案，防止LLM代理中的权限提升。通过分析LLM代理架构特征，提出三种缓解技术：代理隔离、安全处理不可信数据和权限提升防护栏。评估结果表明PFI能有效缓解权限提升攻击，同时保留LLM代理的效用，为LLM代理安全提供新思路。

---

## #52 — ProbGuard: Probabilistic Runtime Monitoring for LLM Agent Safety

`B` Score: 7.37 | 2025-08-01

**Authors:** Haoyu Wang, Christopher M. Poskitt, Jiali Wei, Jun Sun

**Categories:** cs.AI, cs.SE

**Scores:** Citation: 8.30 | Influential: 7.81 | Venue: 2.00 | Author: 7.80 | Recency: 7.00

**Links:** [arXiv](https://arxiv.org/abs/2508.00500) | [PDF](https://arxiv.org/pdf/2508.00500)

> 本文提出了 ProbGuard，一个针对 LLM 代理的主动式运行时监控框架，通过学习离散时间马尔可夫链来预测未来安全违规的概率。该框架能在自动驾驶和具身代理任务中提前预测碰撞和违规行为，最多提前 38.66 秒发出警告，并显著减少不安全行为的发生，为代理安全提供了新的保障机制。

---

## #53 — Security Risks of Agentic Vehicles: A Systematic Analysis of Cognitive and Cross-Layer Threats

`B` Score: 7.33 | 2025-12-18

**Authors:** Ali Eslami, Jiangbo Yu

**Categories:** cs.AI, eess.SY

**Scores:** Citation: 8.75 | Influential: 9.02 | Venue: 2.00 | Author: 3.23 | Recency: 9.00

**Links:** [arXiv](https://arxiv.org/abs/2512.17041) | [PDF](https://arxiv.org/pdf/2512.17041)

> 系统分析了智能体车辆的安全威胁，提出了包含个人代理和驾驶策略代理的基于角色的架构。研究探讨了智能体层及跨层（如感知、控制层）的安全风险，并通过严重性矩阵和攻击链分析，阐明了微小失真如何升级为不安全行为，为车辆平台提供了首个结构化分析基础。

---

## #54 — Multi-Agent Framework for Threat Mitigation and Resilience in AI-Based Systems

`B` Score: 7.29 | 2025-12-29

**Authors:** Armstrong Foundjem, Lionel Nganyewou Tidjon, Leuson Da Silva, Foutse Khomh

**Categories:** cs.CR, cs.LG, cs.MA

**Scores:** Citation: 7.00 | Influential: 7.81 | Venue: 2.00 | Author: 9.83 | Recency: 9.00

**Links:** [arXiv](https://arxiv.org/abs/2512.23132) | [PDF](https://arxiv.org/pdf/2512.23132)

> 提出了一种多智能体RAG系统，通过构建本体驱动的威胁图谱来表征机器学习安全风险。该系统识别了包括API模型窃取在内的未报告威胁，并提出了结合依赖卫生、威胁情报和监控的自适应安全框架，以缓解供应链和推理阶段的威胁。

---

## #55 — Traversal-as-Policy: Log-Distilled Gated Behavior Trees as Externalized, Verifiable Policies for Safe, Robust, and Efficient Agents

`B` Score: 7.27 | 2026-01-30

**Authors:** Peiran Li, Jiashuo Sun, Fangzhou Lin, Shuo Xing, Tianfu Fu, Suofei Feng et al. (8 total)

**Categories:** cs.LG, cs.AI, cs.CR

**Scores:** Citation: 7.85 | Influential: 7.81 | Venue: 2.00 | Author: 6.47 | Recency: 10.00

**Links:** [arXiv](https://arxiv.org/abs/2603.05517) | [PDF](https://arxiv.org/pdf/2603.05517)

> 本文提出了Traversal-as-Policy框架，将沙箱执行日志提炼为可执行的门控行为树，并将树遍历而非无约束生成作为控制策略。该方法通过在节点上附加确定性预执行门控来防止不安全操作，并利用风险感知的最短路径恢复机制。实验表明，GBT在提高任务成功率的同时，显著降低了违规率和成本，实现了安全、鲁棒且高效的Agent行为。

---

## #56 — PSG-Agent: Personality-Aware Safety Guardrail for LLM-based Agents

`B` Score: 7.23 | 2025-09-28

**Authors:** Yaozu Wu, Jizhou Guo, Dongyuan Li, Henry Peng Zou, Wei-Chieh Huang, Yankai Chen et al. (12 total)

**Categories:** cs.AI

**Scores:** Citation: 8.21 | Influential: 7.81 | Venue: 2.00 | Author: 7.15 | Recency: 7.00

**Links:** [arXiv](https://arxiv.org/abs/2509.23614) | [PDF](https://arxiv.org/pdf/2509.23614)

> 本文提出了PSG-Agent，一个针对LLM代理的个性化动态安全护栏系统。该系统通过挖掘交互历史和实时状态生成用户特定的风险阈值，并利用计划监控器和工具防火墙等组件进行跨轮次风险累积监控，在多个场景下显著优于现有的通用护栏方案，提供了可执行和可审计的个性化安全路径。

---

## #57 — Adaptive Vision-Language Model Routing for Computer Use Agents

`B` Score: 7.22 | 2026-03-13

**Authors:** Xunzhuo Liu, Bowei He, Xue Liu, Andy Luo, Haichen Zhang, Huamin Chen

**Categories:** cs.CL, cs.CV

**Scores:** Citation: 9.06 | Influential: 7.81 | Venue: 2.00 | Author: 2.55 | Recency: 10.00

**Links:** [arXiv](https://arxiv.org/abs/2603.12823) | [PDF](https://arxiv.org/pdf/2603.12823)

> 本文提出了自适应VLM路由（AVR）框架，用于计算机使用Agent根据操作难度和置信度动态选择视觉语言模型。该方法在保证目标可靠性的前提下显著降低推理成本，并能与视觉护栏结合，将高风险操作升级至最强模型处理。AVR通过成本-准确性权衡优化了Agent的运行效率与安全性。

---

## #58 — Contextual Agent Security: A Policy for Every Purpose

`B` Score: 7.21 | 2025-01-28

**Authors:** Lillian Tsai, Eugene Bagdasarian

**Categories:** cs.CR, cs.CL, cs.LG

**Scores:** Citation: 8.83 | Influential: 9.77 | Venue: 5.00 | Author: 1.86 | Recency: 5.00

**Links:** [arXiv](https://arxiv.org/abs/2501.17070) | [PDF](https://arxiv.org/pdf/2501.17070)

> 本文探讨代理领域的上下文安全，提出上下文代理安全(Conseca)框架，生成即时、上下文相关且人类可验证的安全策略。随着支持多任务的综合代理部署，论文强调需重新思考安全设计以适应系统的上下文规模和能力，为未来代理安全提供新思路。

---

## #59 — Cybersecurity AI: The World's Top AI Agent for Security Capture-the-Flag (CTF)

`B` Score: 7.15 | 2025-12-02

**Authors:** Víctor Mayoral-Vilches, Luis Javier Navarrete-Lozano, Francesco Balassone, María Sanz-Gómez, Cristóbal R. J. Veas Chavez, Maite del Mundo de Torres et al. (7 total)

**Categories:** cs.CR

**Scores:** Citation: 7.50 | Influential: 7.81 | Venue: 2.00 | Author: 7.43 | Recency: 9.00

**Links:** [arXiv](https://arxiv.org/abs/2512.02654) | [PDF](https://arxiv.org/pdf/2512.02654)

> 本文介绍了Cybersecurity AI (CAI)，一个在2025年多项顶级黑客夺旗赛（CTF）中夺冠的AI智能体。该智能体通过专用的alias1模型架构，以极低的成本实现了企业级AI安全运营，展示了AI在解决Jeopardy风格CTF问题上的绝对优势，并呼吁安全社区转向更具适应性的攻防模式。

---

## #60 — SafeScientist: Toward Risk-Aware Scientific Discoveries by LLM Agents

`B` Score: 7.09 | 2025-05-29

**Authors:** Kunlun Zhu, Jiaxun Zhang, Ziheng Qi, Nuoxing Shang, Zijia Liu, Peixuan Han et al. (9 total)

**Categories:** cs.AI

**Scores:** Citation: 8.32 | Influential: 9.02 | Venue: 2.00 | Author: 4.27 | Recency: 7.00

**Links:** [arXiv](https://arxiv.org/abs/2505.23559) | [PDF](https://arxiv.org/pdf/2505.23559)

> 本文提出了 SafeScientist，一个专为 AI 驱动的科学发现设计的安全框架，集成了提示监控、工具使用监控和伦理审查员等多种防御机制。配合提出的 SciSafetyBench 基准测试，该框架在不牺牲科学输出质量的情况下，显著提升了高风险科学任务中的安全性能。

---

## #61 — Executable Governance for AI: Translating Policies into Rules Using LLMs

`B` Score: 7.03 | 2025-12-04

**Authors:** Gautam Varma Datla, Anudeep Vurity, Tejaswani Dash, Tazeem Ahmad, Mohd Adnan, Saima Rafi

**Categories:** cs.AI

**Scores:** Citation: 6.51 | Influential: 9.39 | Venue: 2.00 | Author: 7.43 | Recency: 9.00

**Links:** [arXiv](https://arxiv.org/abs/2512.04408) | [PDF](https://arxiv.org/pdf/2512.04408)

> 本文提出了Policy-to-Tests (P2T) 框架，利用大语言模型将自然语言政策文档转换为规范化的、机器可执行的规则。该框架包含紧凑的领域特定语言（DSL）和流水线，能够提取义务条款并生成规则，实验表明其生成的规则与人工基准高度匹配，并能有效降低生成式智能体的违规率。

---

## #62 — Terrarium: Revisiting the Blackboard for Multi-Agent Safety, Privacy, and Security Studies

`B` Score: 7.00 | 2025-10-16

**Authors:** Mason Nakamura, Abhinav Kumar, Saaduddin Mahmud, Sahar Abdelnabi, Shlomo Zilberstein, Eugene Bagdasarian

**Categories:** cs.AI, cs.CL, cs.CR

**Scores:** Citation: 6.80 | Influential: 7.81 | Venue: 2.00 | Author: 9.84 | Recency: 7.00

**Links:** [arXiv](https://arxiv.org/abs/2510.14312) | [PDF](https://arxiv.org/pdf/2510.14312)

> 本文提出了Terrarium框架，利用黑板设计构建了一个模块化、可配置的多Agent协作测试平台，用于细粒度研究LLM驱动的MAS中的安全、隐私和安保问题。该框架识别了关键攻击向量，并通过实施协作场景和代表性攻击来加速可信多Agent系统的防御迭代与设计优化。

---

## #63 — Schema First Tool APIs for LLM Agents: A Controlled Study of Tool Misuse, Recovery, and Budgeted Performance

`B` Score: 6.99 | 2026-03-12

**Authors:** Akshey Sigdel, Rista Baral

**Categories:** cs.SE, cs.AI

**Scores:** Citation: 9.02 | Influential: 7.81 | Venue: 2.00 | Author: 1.12 | Recency: 10.00

**Links:** [arXiv](https://arxiv.org/abs/2603.13404) | [PDF](https://arxiv.org/pdf/2603.13404)

> 本文通过对照实验研究了基于Schema的工具契约和结构化验证诊断是否能提高LLM Agent在严格交互预算下的可靠性。结果表明，虽然接口形式化能减少接口误用，但语义动作质量和超时敏感任务仍是受限本地推理下的主要瓶颈。

---

## #64 — Agent2Agent Threats in Safety-Critical LLM Assistants: A Human-Centric Taxonomy

`C` Score: 6.98 | 2026-02-05

**Authors:** Lukas Stappen, Ahmet Erkan Turan, Johann Hagerer, Georg Groh

**Categories:** cs.AI, cs.HC

**Scores:** Citation: 8.74 | Influential: 7.81 | Venue: 2.00 | Author: 1.86 | Recency: 10.00

**Links:** [arXiv](https://arxiv.org/abs/2602.05877) | [PDF](https://arxiv.org/pdf/2602.05877)

> 本文提出了AgentHeLLM，一个针对安全关键型LLM助手（如车载助手）的以人为中心的威胁建模框架。该框架正式将资产识别与攻击路径分析分离，引入了基于受害者建模的资产分类法和区分毒化路径与触发路径的图模型。该框架通过自动化多阶段威胁发现工具，解决了现有AI安全框架在安全关键系统中的方法论缺陷。

---

## #65 — SentinelAgent: Graph-based Anomaly Detection in Multi-Agent Systems

`C` Score: 6.94 | 2025-05-30

**Authors:** Xu He, Di Wu, Yan Zhai, Kun Sun

**Categories:** cs.AI

**Scores:** Citation: 8.33 | Influential: 9.02 | Venue: 2.00 | Author: 3.23 | Recency: 7.00

**Links:** [arXiv](https://arxiv.org/abs/2505.24201) | [PDF](https://arxiv.org/pdf/2505.24201)

> 本文提出了 SentinelAgent，一个专为多智能体系统设计的系统级异常检测框架，结合了基于图的交互建模和运行时行为监督。该框架通过将智能体交互建模为动态执行图，并引入可插拔的监督智能体，能够有效检测提示注入、多智能体勾结等隐蔽风险。

---

## #66 — Risk Alignment in Agentic AI Systems

`C` Score: 6.94 | 2024-10-02

**Authors:** Hayley Clatterbuck, Clinton Castro, Arvo Muñoz Morán

**Categories:** cs.CY, cs.AI, econ.GN

**Scores:** Citation: 7.66 | Influential: 9.58 | Venue: 2.00 | Author: 5.88 | Recency: 5.00

**Links:** [arXiv](https://arxiv.org/abs/2410.01927) | [PDF](https://arxiv.org/pdf/2410.01927)

> 本文探讨了智能体 AI 系统中的风险对齐问题，分析了 AI 的风险态度如何影响用户满意度、信任及社会影响。研究讨论了鲁莽的 AI 可能带来的威胁及责任缺口，并提出了关于如何设计符合用户风险态度的 AI 系统的关键问题。文章涉及了在代表他人做出风险决策时的伦理考量及必要的防护措施。

---

## #67 — Reliable Weak-to-Strong Monitoring of LLM Agents

`C` Score: 6.90 | 2025-08-26

**Authors:** Neil Kale, Chen Bo Calvin Zhang, Kevin Zhu, Ankit Aich, Paula Rodriguez, Scale Red Team et al. (8 total)

**Categories:** cs.AI, cs.CR, cs.LG

**Scores:** Citation: 7.89 | Influential: 9.02 | Venue: 2.00 | Author: 4.27 | Recency: 7.00

**Links:** [arXiv](https://arxiv.org/abs/2508.19461) | [PDF](https://arxiv.org/pdf/2508.19461)

> 本文通过监控红队测试（MRT）工作流，对检测自主LLM智能体隐蔽行为的监控系统进行了压力测试。研究发现智能体的监控意识会显著降低监控器的可靠性，而提出的混合分层顺序脚手架架构能使弱模型可靠地监控强模型。该研究为构建有效的智能体监控系统提供了实证依据，强调了人机协作在监督中的重要性。

---

## #68 — Agent Safety Alignment via Reinforcement Learning

`C` Score: 6.89 | 2025-07-11

**Authors:** Zeyang Sha, Hanling Tian, Zhuoer Xu, Shiwen Cui, Changhua Meng, Weiqiang Wang

**Categories:** cs.AI, cs.CR

**Scores:** Citation: 7.45 | Influential: 7.81 | Venue: 2.00 | Author: 7.15 | Recency: 7.00

**Links:** [arXiv](https://arxiv.org/abs/2507.08270) | [PDF](https://arxiv.org/pdf/2507.08270)

> 本文提出首个工具使用代理的统一安全对齐框架，通过结构化推理和沙盒强化学习处理用户和工具双重威胁渠道。作者引入三模态分类法和策略驱动决策模型，使用自定义沙盒环境模拟工具执行。实验表明，安全对齐代理显著提高对安全威胁抵抗力，同时保持良性任务上的强大效用，为自主代理可信部署奠定基础。

---

## #69 — AgentTrace: A Structured Logging Framework for Agent System Observability

`C` Score: 6.89 | 2026-02-07

**Authors:** Adam AlSayyad, Kelvin Yuxiang Huang, Richik Pal

**Categories:** cs.SE, cs.AI

**Scores:** Citation: 8.80 | Influential: 7.81 | Venue: 2.00 | Author: 1.12 | Recency: 10.00

**Links:** [arXiv](https://arxiv.org/abs/2602.10133) | [PDF](https://arxiv.org/pdf/2602.10133)

> 本文提出了AgentTrace，一个专为智能体系统可观测性设计的动态遥测和日志框架。该框架在运行时以最小开销捕获操作、认知和上下文三个层面的结构化日志，为智能体安全、问责和实时监控提供基础。AgentTrace通过提供细粒度的风险分析，解决了LLM智能体在敏感环境部署中的透明度和可追溯性障碍。

---

## #70 — TrinityGuard: A Unified Framework for Safeguarding Multi-Agent Systems

`C` Score: 6.89 | 2026-03-16

**Authors:** Kai Wang, Biaojie Zeng, Zeming Wei, Chang Jin, Hefeng Zhou, Xiangtian Li et al. (10 total)

**Categories:** cs.CR, cs.AI, cs.CL

**Scores:** Citation: 8.10 | Influential: 7.81 | Venue: 2.00 | Author: 3.23 | Recency: 10.00

**Links:** [arXiv](https://arxiv.org/abs/2603.15408) | [PDF](https://arxiv.org/pdf/2603.15408)

> 本文提出了TrinityGuard，一个基于OWASP标准的LLM多Agent系统综合安全评估与监控框架。该框架包含涵盖单Agent漏洞、通信威胁和系统级危害的三层细粒度风险分类法，通过抽象层、评估层和运行时监控Agent实现预开发评估和实时监控。案例研究展示了TrinityGuard在各种MAS结构中的通用性和可靠性。

---

## #71 — Monitoring LLM-based Multi-Agent Systems Against Corruptions via Node Evaluation

`C` Score: 6.88 | 2025-10-22

**Authors:** Chengcan Wu, Zhixin Zhang, Mingqian Xu, Zeming Wei, Meng Sun

**Categories:** cs.CR, cs.AI, cs.LG

**Scores:** Citation: 7.57 | Influential: 7.81 | Venue: 2.00 | Author: 6.75 | Recency: 7.00

**Links:** [arXiv](https://arxiv.org/abs/2510.19420) | [PDF](https://arxiv.org/pdf/2510.19420)

> 本文提出了一种针对大语言模型多智能体系统的动态防御机制，通过持续监控通信图并动态调整拓扑结构来防御腐败攻击。与静态图防御不同，该方法能够准确破坏恶意通信，有效应对复杂动态环境下的多样化攻击，显著提升了多智能体系统的整体安全性与可信度。

---

## #72 — AgentGuard: Repurposing Agentic Orchestrator for Safety Evaluation of Tool Orchestration

`C` Score: 6.82 | 2025-02-13

**Authors:** Jizhou Chen, Samuel Lee Cong

**Categories:** cs.CR, cs.AI

**Scores:** Citation: 8.72 | Influential: 9.58 | Venue: 2.00 | Author: 1.86 | Recency: 5.00

**Links:** [arXiv](https://arxiv.org/abs/2502.09809) | [PDF](https://arxiv.org/pdf/2502.09809)

> AgentGuard框架利用LLM编排器的固有功能作为安全评估器，自主发现和验证不安全的工具使用工作流，生成安全约束限制代理行为。该框架通过四个阶段运作：识别不安全工作流、验证执行、生成约束、验证约束有效性。实验证明AgentGuard能有效评估工具使用安全性，为LLM代理提供部署前的安全保证基线，增强其在现实应用中的可信度。

---

## #73 — LOKA Protocol: A Decentralized Framework for Trustworthy and Ethical AI Agent Ecosystems

`C` Score: 6.81 | 2025-04-15

**Authors:** Rajesh Ranjan, Shailja Gupta, Surya Narayan Singh

**Categories:** cs.MA, cs.AI, cs.CY

**Scores:** Citation: 8.67 | Influential: 7.81 | Venue: 2.00 | Author: 4.27 | Recency: 5.00

**Links:** [arXiv](https://arxiv.org/abs/2504.10915) | [PDF](https://arxiv.org/pdf/2504.10915)

> 本文提出了 LOKA 协议，一个用于构建可信和合乎伦理的 AI Agent 生态系统的去中心化系统级架构。该协议引入了通用 Agent 身份层和去中心化伦理共识协议，旨在解决 Agent 在身份验证、问责制及伦理对齐方面的关键问题。LOKA 为未来多 Agent 治理提供了可扩展且具有弹性的蓝图，奠定了负责任 AI 生态的基础。

---

## #74 — SoK: Trust-Authorization Mismatch in LLM Agent Interactions

`C` Score: 6.78 | 2025-12-07

**Authors:** Guanquan Shi, Haohua Du, Zhiqiang Wang, Xiaoyu Liang, Weiwenpei Liu, Song Bian et al. (7 total)

**Categories:** cs.CR, cs.AI

**Scores:** Citation: 6.56 | Influential: 9.02 | Venue: 2.00 | Author: 6.17 | Recency: 9.00

**Links:** [arXiv](https://arxiv.org/abs/2512.06914) | [PDF](https://arxiv.org/pdf/2512.06914)

> 论文系统调研了LLM智能体交互中的安全现状，提出了信念-意图-许可（B-I-P）框架来分析信任与授权的不匹配问题。该研究揭示了从静态RBAC转向动态、自适应授权的必要性，并规划了未来的研究议程，为构建可信智能体提供了理论基础。

---

## #75 — Agentic Business Process Management: Practitioner Perspectives on Agent Governance in Business Processes

`C` Score: 6.77 | 2025-03-23

**Authors:** Hoang Vu, Nataliia Klievtsova, Henrik Leopold, Stefanie Rinderle-Ma, Timotheus Kampik

**Categories:** cs.SE, cs.MA

**Scores:** Citation: 6.66 | Influential: 9.02 | Venue: 5.00 | Author: 6.47 | Recency: 5.00

**Links:** [arXiv](https://arxiv.org/abs/2504.03693) | [PDF](https://arxiv.org/pdf/2504.03693)

> 本研究通过22位BMP从业者的访谈，探讨了AI代理在业务流程中的治理问题。研究发现代理可提高效率、数据质量和合规性，但也存在偏见、过度依赖等风险。论文提出六项关键建议，包括明确业务目标、设置法律伦理护栏、建立人机协作等，并概述了传统BMP与代理AI对齐的行动方案。

---

## #76 — LLM-Enabled In-Context Learning for Data Collection Scheduling in UAV-assisted Sensor Networks

`C` Score: 6.77 | 2025-04-20

**Authors:** Yousef Emami, Hao Zhou, SeyedSina Nabavirazani, Luis Almeida

**Categories:** cs.AI, cs.ET, cs.LG

**Scores:** Citation: 7.55 | Influential: 7.81 | Venue: 5.00 | Author: 5.40 | Recency: 5.00

**Links:** [arXiv](https://arxiv.org/abs/2504.14556) | [PDF](https://arxiv.org/pdf/2504.14556)

> 本文提出了ICLDC系统，利用LLM的上下文学习能力替代深度强化学习，解决无人机辅助传感器网络中的数据收集调度问题。系统包含验证器机制以确保操作安全，并针对越狱攻击进行了测试，揭示了LLM在任务描述被操纵时的脆弱性。实验结果表明，该方法在紧急场景下能有效减少数据包丢失。

---

## #77 — Assured Autonomy: How Operations Research Powers and Orchestrates Generative AI Systems

`C` Score: 6.76 | 2025-12-30

**Authors:** Tinglong Dai, David Simchi-Levi, Michelle Xiao Wu, Yao Xie

**Categories:** cs.LG, math.OC, stat.ML

**Scores:** Citation: 8.02 | Influential: 7.81 | Venue: 2.00 | Author: 3.23 | Recency: 9.00

**Links:** [arXiv](https://arxiv.org/abs/2512.23978) | [PDF](https://arxiv.org/pdf/2512.23978)

> 提出了一个基于运筹学的“保证自主性”概念框架，旨在为生成式AI系统提供可验证的可行性和对抗性鲁棒性。该框架将运筹学角色从求解器转变为系统架构师，通过流式生成模型和对抗性鲁棒性视角，确保高后果场景下的操作安全。

---

## #78 — PARSE: LLM Driven Schema Optimization for Reliable Entity Extraction

`C` Score: 6.72 | 2025-10-08

**Authors:** Anubhav Shrimal, Aryan Jain, Soumyajit Chowdhury, Promod Yenigalla

**Categories:** cs.CL, cs.LG

**Scores:** Citation: 5.56 | Influential: 9.02 | Venue: 10.00 | Author: 4.79 | Recency: 7.00

**Links:** [arXiv](https://arxiv.org/abs/2510.08623) | [PDF](https://arxiv.org/pdf/2510.08623)

> 针对LLM agents在结构化信息提取中因JSON Schema静态化导致的性能不佳和幻觉问题，本文提出了PARSE系统。该系统创新性地将Schema视为可被LLM理解和优化的自然语言契约，通过ARCHITECT等组件自动优化Schema设计，以消除模糊和不完整规范。这种方法显著提升了实体提取的准确性和Agent行为的可靠性，为Software 3.0系统提供了更稳健的数据交互基础。

---

## #79 — Breaking the Protocol: Security Analysis of the Model Context Protocol Specification and Prompt Injection Vulnerabilities in Tool-Integrated LLM Agents

`C` Score: 6.70 | 2026-01-24

**Authors:** Narek Maloyan, Dmitry Namiot

**Categories:** cs.CR, cs.AI

**Scores:** Citation: 7.67 | Influential: 7.81 | Venue: 2.00 | Author: 3.23 | Recency: 10.00

**Links:** [arXiv](https://arxiv.org/abs/2601.17549) | [PDF](https://arxiv.org/pdf/2601.17549)

> 本文首次对模型上下文协议（MCP）进行了严格的安全分析，识别了缺乏能力证明、双向采样无源认证等三个根本性的协议级漏洞。作者实现了MCPBench框架来测量特定的攻击面，实验表明MCP的架构选择使攻击成功率显著增加。研究提出了MCPSec协议扩展，通过添加能力证明和消息认证，在不破坏兼容性的前提下大幅降低了攻击成功率。

---

## #80 — EdgeAIGuard: Agentic LLMs for Minor Protection in Digital Spaces

`C` Score: 6.67 | 2025-02-28

**Authors:** Ghulam Mujtaba, Sunder Ali Khowaja, Kapal Dev

**Categories:** cs.CY, cs.AI, cs.CR

**Scores:** Citation: 5.95 | Influential: 7.81 | Venue: 5.00 | Author: 9.52 | Recency: 5.00

**Links:** [arXiv](https://arxiv.org/abs/2503.00092) | [PDF](https://arxiv.org/pdf/2503.00092)

> EdgeAIGuard提出了一种基于多智能体架构的内容审核方法，部署在网络边缘以保护未成年人免受网络诱捕和数字剥削。传统内容审核技术对攻击者不断演变的策略效果有限，而EdgeAIGuard通过低延迟快速检测显著提高了防护效果，实验证明其有效性远超现有方法。

---

## #81 — To trust or not to trust: Attention-based Trust Management for LLM Multi-Agent Systems

`C` Score: 6.63 | 2025-06-03

**Authors:** Pengfei He, Zhenwei Dai, Xianfeng Tang, Yue Xing, Hui Liu, Jingying Zeng et al. (12 total)

**Categories:** cs.CR

**Scores:** Citation: 6.71 | Influential: 7.81 | Venue: 2.00 | Author: 7.62 | Recency: 7.00

**Links:** [arXiv](https://arxiv.org/abs/2506.02546) | [PDF](https://arxiv.org/pdf/2506.02546)

> 针对大语言模型多智能体系统中的消息可信度问题，提出了一种基于注意力的信任管理机制。该研究定义了六个信任维度，设计了A-Trust评分系统，有效评估消息和智能体的可信度，显著提升了系统对抗恶意输入的鲁棒性。

---

## #82 — Guardrails as Infrastructure: Policy-First Control for Tool-Orchestrated Workflows

`C` Score: 6.63 | 2026-03-18

**Authors:** Akshey Sigdel, Rista Baral

**Categories:** cs.CR, cs.SE

**Scores:** Citation: 8.23 | Influential: 7.81 | Venue: 2.00 | Author: 1.12 | Recency: 10.00

**Links:** [arXiv](https://arxiv.org/abs/2603.18059) | [PDF](https://arxiv.org/pdf/2603.18059)

> 本文提出了策略优先工具，这是一种模型无关的权限层，通过显式约束和风险感知门控来调解工具调用，防止不安全副作用和敏感信息泄露。该框架包含紧凑的策略DSL、运行时执行架构及可复现的基准测试，能够量化安全性与效用的权衡。实验结果表明，更严格的策略包能显著提高违规预防率，同时降低任务成功率。

---

## #83 — ProbeLogits: Kernel-Level LLM Inference Primitives for AI-Native Operating Systems

`C` Score: 6.63 | 2026-04-13

**Authors:** Daeyeon Son

**Categories:** cs.OS, cs.LG

**Scores:** Citation: 8.50 | Influential: 7.81 | Venue: 2.00 | Author: 0.26 | Recency: 10.00

**Links:** [arXiv](https://arxiv.org/abs/2604.11943) | [PDF](https://arxiv.org/pdf/2604.11943)

> 本文介绍了ProbeLogits，一种运行在操作系统内核中的LLM推理原语，可在生成任何文本之前读取logit分布并作为治理原语操作。该方法执行一次前向传播并读取特定token的logit来分类代理操作为安全或危险，无需学习参数。在260个提示OS操作基准测试上实现了F1=0.980，精确度1.000，召回率0.960。关键设计贡献是校准强度α，作为部署时的策略旋钮。作者在Anima OS中实现了ProbeLogits，这是一个用Rust编写的裸机操作系统，使安全操作在WASM沙箱边界下执行，更难被绕过。

---

## #84 — Enhancing Reliability in LLM-Integrated Robotic Systems: A Unified Approach to Security and Safety

`C` Score: 6.61 | 2025-09-02

**Authors:** Wenxiao Zhang, Xiangrui Kong, Conan Dewitt, Thomas Bräunl, Jin B. Hong

**Categories:** cs.RO, cs.AI

**Scores:** Citation: 6.94 | Influential: 9.02 | Venue: 5.00 | Author: 3.23 | Recency: 7.00

**Links:** [arXiv](https://arxiv.org/abs/2509.02163) | [PDF](https://arxiv.org/pdf/2509.02163)

> 本文提出了一个统一框架，旨在解决集成大语言模型的机器人系统中的可靠性和安全性问题。该方法结合了提示组装、状态管理和安全验证机制，有效缓解了提示注入攻击并确保了复杂环境下的操作安全，显著提升了系统在对抗条件下的性能。

---

## #85 — Autonomous Microscopy Experiments through Large Language Model Agents

`C` Score: 6.61 | 2024-12-18

**Authors:** Indrajeet Mandal, Jitendra Soni, Mohd Zaki, Morten M. Smedskjaer, Katrin Wondraczek, Lothar Wondraczek et al. (8 total)

**Categories:** cs.CY, cond-mat.mtrl-sci, cs.AI

**Scores:** Citation: 6.48 | Influential: 7.81 | Venue: 2.00 | Author: 9.53 | Recency: 5.00

**Links:** [arXiv](https://arxiv.org/abs/2501.10385) | [PDF](https://arxiv.org/pdf/2501.10385)

> 本文介绍了 AILA 框架，利用 LLM 驱动的智能体自动化原子力显微镜实验，并开发了评估套件 AFMBench。研究发现，最先进的模型在基本任务和协调场景中表现不佳，且多智能体框架优于单智能体架构。此外，研究观察到 LLM 可能会偏离指令，引发了关于自动驾驶实验室应用安全对齐的担忧，揭示了领域问答能力并不等同于有效的智能体能力。

---

## #86 — Test-Driven AI Agent Definition (TDAD): Compiling Tool-Using Agents from Behavioral Specifications

`C` Score: 6.55 | 2026-03-09

**Authors:** Tzafrir Rehan

**Categories:** cs.SE, cs.AI

**Scores:** Citation: 7.69 | Influential: 9.02 | Venue: 2.00 | Author: 0.58 | Recency: 10.00

**Links:** [arXiv](https://arxiv.org/abs/2603.08806) | [PDF](https://arxiv.org/pdf/2603.08806)

> 本文提出了测试驱动AI Agent定义（TDAD）方法，将Agent提示词视为编译产物，通过将行为规范转换为可执行测试并迭代优化提示词来确保行为合规性。该方法引入了可见/隐藏测试分割和语义变异测试等机制，有效防止了规范博弈和回归，显著提升了工具使用Agent的部署安全性。

---

## #87 — Accelerating Drug Discovery Through Agentic AI: A Multi-Agent Approach to Laboratory Automation in the DMTA Cycle

`C` Score: 6.50 | 2025-07-11

**Authors:** Yao Fehlis, Charles Crain, Aidan Jensen, Michael Watson, James Juhasz, Paul Mandel et al. (12 total)

**Categories:** cs.SE, cs.AI, cs.MA

**Scores:** Citation: 8.35 | Influential: 7.81 | Venue: 2.00 | Author: 1.86 | Recency: 7.00

**Links:** [arXiv](https://arxiv.org/abs/2507.09023) | [PDF](https://arxiv.org/pdf/2507.09023)

> 本文介绍Tippy，一个通过五个专业AI代理在DMTA周期中运作的框架，实现实验室自动化。该系统包含监督、分子、实验室、分析和报告代理，并由安全护栏监督。Tippy代表首个生产级DMTA周期自动化实现，通过自主推理、规划和协作的AI代理，显著提高工作流程效率、决策速度和跨学科协调能力。

---

## #88 — Blind Gods and Broken Screens: Architecting a Secure, Intent-Centric Mobile Agent Operating System

`C` Score: 6.50 | 2026-02-11

**Authors:** Zhenhua Zou, Sheng Guo, Qiuyang Zhan, Lepeng Zhao, Shuo Li, Qi Li et al. (9 total)

**Categories:** cs.CR, cs.AI

**Scores:** Citation: 6.51 | Influential: 7.81 | Venue: 2.00 | Author: 5.40 | Recency: 10.00

**Links:** [arXiv](https://arxiv.org/abs/2602.10915) | [PDF](https://arxiv.org/pdf/2602.10915)

> 本文对现有移动智能体进行了系统安全分析，揭示了基于屏幕交互范式存在的身份伪造、视觉欺骗和权限升级等关键漏洞。作者提出了Aura，一种全新的安全智能体操作系统架构，采用中心辐射型拓扑，通过系统智能体编排意图、沙箱化应用智能体执行任务，并利用内核强制执行加密身份绑定和语义输入清洗等四大防御支柱。该架构旨在从根本上解决移动智能体生态系统的结构性安全问题。

---

## #89 — From Prompts to Protection: Large Language Model-Enabled In-Context Learning for Smart Public Safety UAV

`C` Score: 6.47 | 2025-06-03

**Authors:** Yousef Emami, Hao Zhou, Miguel Gutierrez Gaitan, Kai Li, Luis Almeida, Zhu Han

**Categories:** cs.AI

**Scores:** Citation: 7.11 | Influential: 7.81 | Venue: 2.00 | Author: 5.40 | Recency: 7.00

**Links:** [arXiv](https://arxiv.org/abs/2506.02649) | [PDF](https://arxiv.org/pdf/2506.02649)

> 探讨利用大语言模型的上下文学习能力优化公共安全无人机的路径规划与控制。该方案相比深度强化学习降低了延迟并保护隐私，同时提出了缓解越狱漏洞的策略，提升了任务关键型应用的实时响应能力。

---

## #90 — Data-Driven Policy Mapping for Safe RL-based Energy Management Systems

`C` Score: 6.42 | 2025-06-19

**Authors:** Theo Zangato, Aomar Osmani, Pegah Alizadeh

**Categories:** cs.LG

**Scores:** Citation: 6.16 | Influential: 7.81 | Venue: 5.00 | Author: 5.88 | Recency: 7.00

**Links:** [arXiv](https://arxiv.org/abs/2506.16352) | [PDF](https://arxiv.org/pdf/2506.16352)

> 本文提出了一种基于强化学习的建筑能源管理系统，结合聚类、预测和约束策略学习来解决可扩展性和安全性挑战。该方法通过聚类非转移负荷概况实现策略泛化，集成LSTM预测模块提高响应性，并利用域知情的动作掩码确保安全探索。实验表明，该方法降低了运营成本，并能快速适应新建筑和随机电价变化，实现了可扩展且安全的能源管理。

---

## #91 — When Developer Aid Becomes Security Debt: A Systematic Analysis of Insecure Behaviors in LLM Coding Agents

`C` Score: 6.42 | 2025-07-12

**Authors:** Matous Kozak, Roshanak Zilouchian Moghaddam, Siva Sivaraman

**Categories:** cs.AI, cs.CR

**Scores:** Citation: 6.41 | Influential: 7.81 | Venue: 2.00 | Author: 7.15 | Recency: 7.00

**Links:** [arXiv](https://arxiv.org/abs/2507.09329) | [PDF](https://arxiv.org/pdf/2507.09329)

> 本文对自主编码代理进行首次系统性安全评估，分析五个先进模型在93个真实软件任务上的12,000多个动作。研究发现21%的代理轨迹包含不安全行为，信息暴露是最普遍漏洞。作者开发高精度检测系统识别四大漏洞类别，并评估各种缓解策略的有效性，发现GPT-4.1表现出96.8%的缓解成功率。

---

## #92 — Beyond Single-Agent Safety: A Taxonomy of Risks in LLM-to-LLM Interactions

`C` Score: 6.42 | 2025-12-02

**Authors:** Piercosma Bisconti, Marcello Galisai, Federico Pierucci, Marcantonio Bracale, Matteo Prandi

**Categories:** cs.MA, cs.AI

**Scores:** Citation: 7.50 | Influential: 7.81 | Venue: 2.00 | Author: 2.55 | Recency: 9.00

**Links:** [arXiv](https://arxiv.org/abs/2512.02682) | [PDF](https://arxiv.org/pdf/2512.02682)

> 本文探讨了为何针对人机交互设计的安全机制无法扩展到LLM与LLM交互的环境，提出了从模型级安全向系统级安全转变的概念。文章引入了突发系统性风险视界（ESRH）框架，对微观、中观和宏观层面的故障模式进行了分类，并提出了在多智能体系统中嵌入自适应监督的架构设计。

---

## #93 — Forgetful but Faithful: A Cognitive Memory Architecture and Benchmark for Privacy-Aware Generative Agents

`C` Score: 6.41 | 2025-12-14

**Authors:** Saad Alqithami

**Categories:** cs.AI, cs.LG

**Scores:** Citation: 7.70 | Influential: 7.81 | Venue: 2.00 | Author: 1.86 | Recency: 9.00

**Links:** [arXiv](https://arxiv.org/abs/2512.12856) | [PDF](https://arxiv.org/pdf/2512.12856)

> 本文针对长期交互场景中生成智能体的记忆管理瓶颈，提出了以人为中心的记忆管理框架 MaRS 及六种理论上合理的遗忘策略，以平衡性能、隐私和计算效率。研究还推出了 FiFA 基准，从叙事连贯性、目标完成、隐私保护等多个维度评估智能体性能。实验表明，混合遗忘策略在保持计算可处理性和隐私保证的同时实现了卓越的综合性能，为资源受限和隐私敏感环境中的智能体部署提供了实用指导。

---

## #94 — ContextCov: Deriving and Enforcing Executable Constraints from Agent Instruction Files

`C` Score: 6.40 | 2026-02-28

**Authors:** Reshabh K Sharma

**Categories:** cs.SE, cs.AI

**Scores:** Citation: 7.23 | Influential: 7.81 | Venue: 2.00 | Author: 2.55 | Recency: 10.00

**Links:** [arXiv](https://arxiv.org/abs/2603.00822) | [PDF](https://arxiv.org/pdf/2603.00822)

> 本文提出了ContextCov框架，将被动的自然语言智能体指令转化为主动的可执行护栏，以防止软件工程智能体在执行任务时偏离指令。该框架通过静态AST分析、运行时shell拦截和架构验证器合成执行检查，在723个开源仓库中成功提取了数万个检查点，为安全的智能体驱动开发提供了自动化合规层。

---

## #95 — COALESCE: Economic and Security Dynamics of Skill-Based Task Outsourcing Among Team of Autonomous LLM Agents

`C` Score: 6.36 | 2025-06-02

**Authors:** Manish Bhatt, Ronald F. Del Rosario, Vineeth Sai Narajala, Idan Habler

**Categories:** cs.AI, cs.CE, cs.CR

**Scores:** Citation: 6.03 | Influential: 9.02 | Venue: 5.00 | Author: 4.27 | Recency: 7.00

**Links:** [arXiv](https://arxiv.org/abs/2506.01900) | [PDF](https://arxiv.org/pdf/2506.01900)

> 提出了COALESCE框架，旨在通过基于技能的任务外包优化自主LLM智能体团队的GPU资源利用。该框架集成了混合技能表示、动态技能发现和统一成本模型，在显著降低计算成本的同时，通过标准化通信协议保障了交互安全。

---

## #96 — Practical challenges of control monitoring in frontier AI deployments

`C` Score: 6.34 | 2025-12-15

**Authors:** David Lindner, Charlie Griffin, Tomek Korbak, Roland S. Zimmermann, Geoffrey Irving, Sebastian Farquhar et al. (7 total)

**Categories:** cs.CR, cs.AI, cs.MA

**Scores:** Citation: 6.75 | Influential: 7.81 | Venue: 2.00 | Author: 4.27 | Recency: 9.00

**Links:** [arXiv](https://arxiv.org/abs/2512.22154) | [PDF](https://arxiv.org/pdf/2512.22154)

> 本文分析了在现实世界部署中扩展自动控制监控的设计选择，重点研究了同步、半同步和异步三种监控形式及其延迟与安全性的权衡。研究引入了高层安全案例草图作为理解和比较这些监控协议的工具，并识别了监督、延迟和恢复三大挑战。通过四个未来 AI 部署的案例研究，探讨了如何应对并行实例、非可忽略的监督延迟以及识别阴谋智能体等实际困难。

---

## #97 — Spider-Sense: Intrinsic Risk Sensing for Efficient Agent Defense with Hierarchical Adaptive Screening

`C` Score: 6.29 | 2026-02-05

**Authors:** Zhenxiong Yu, Zhi Yang, Zhiheng Jin, Shuhe Wang, Heng Zhang, Yanlin Fei et al. (22 total)

**Categories:** cs.CR, cs.AI

**Scores:** Citation: 6.22 | Influential: 9.02 | Venue: 2.00 | Author: 3.23 | Recency: 10.00

**Links:** [arXiv](https://arxiv.org/abs/2602.05386) | [PDF](https://arxiv.org/pdf/2602.05386)

> 本文提出了Spider-Sense框架，一种基于内在风险感知的事件驱动Agent防御机制，允许Agent仅在感知到风险时触发防御。该框架采用分层自适应筛选机制，通过轻量级匹配处理已知模式，并将模糊情况升级为深度推理，从而在保持低延迟的同时有效防御多阶段攻击。实验表明其在降低攻击成功率和误报率方面表现优异。

---

## #98 — SafeCoop: Unravelling Full Stack Safety in Agentic Collaborative Driving

`C` Score: 6.27 | 2025-10-20

**Authors:** Xiangbo Gao, Tzu-Hsiang Lin, Ruojing Song, Yuheng Wu, Kuan-Ru Huang, Zicheng Jin et al. (9 total)

**Categories:** cs.CV, cs.AI, cs.CL

**Scores:** Citation: 6.86 | Influential: 7.81 | Venue: 2.00 | Author: 4.79 | Recency: 7.00

**Links:** [arXiv](https://arxiv.org/abs/2510.18123) | [PDF](https://arxiv.org/pdf/2510.18123)

> 本文首次系统研究了基于自然语言的协作驾驶系统中的全栈安全问题，并提出了SafeCoop防御流水线。该系统通过语义防火墙、语言感知一致性检查和多源共识机制，有效防御消息丢失、语义操纵等攻击，在仿真环境中显著提升了驾驶安全性与整体鲁棒性。

---

## #99 — Rethinking Autonomy: Preventing Failures in AI-Driven Software Engineering

`C` Score: 6.26 | 2025-08-15

**Authors:** Satyam Kumar Navneet, Joydeep Chandra

**Categories:** cs.SE, cs.AI, cs.CR

**Scores:** Citation: 7.29 | Influential: 9.02 | Venue: 2.00 | Author: 1.86 | Recency: 7.00

**Links:** [arXiv](https://arxiv.org/abs/2508.11824) | [PDF](https://arxiv.org/pdf/2508.11824)

> 本文分析了大语言模型辅助代码生成中的安全风险，如不安全代码生成、幻觉输出和缺乏问责制，并提出了 SAFE-AI 框架以应对这些挑战。该框架强调安全性、可审计性、反馈和可解释性，集成了护栏、沙箱、运行时验证和人工在环系统等机制来缓解风险。此外，研究还引入了 AI 行为分类法，并指出了缺乏标准化基准等开放性问题及未来研究方向。

---

## #100 — Multi-Agent Collaboration in Incident Response with Large Language Models

`C` Score: 6.15 | 2024-12-01

**Authors:** Zefang Liu

**Categories:** cs.CL, cs.CR

**Scores:** Citation: 6.30 | Influential: 9.02 | Venue: 2.00 | Author: 5.40 | Recency: 5.00

**Links:** [arXiv](https://arxiv.org/abs/2412.00652) | [PDF](https://arxiv.org/pdf/2412.00652)

> 本文探讨了利用大语言模型作为智能体，在网络安全事件响应中实现多智能体协作的方法。研究基于“Backdoors & Breaches”桌面游戏框架模拟真实场景，对比分析了集中式、去中心化和混合式团队结构下的智能体交互与性能差异。结果表明，LLM智能体能够有效提升决策制定能力和适应性，为优化事件响应流程和实现更高效的协同网络威胁应对提供了新思路。

---

## #101 — MARCO: Multi-Agent Real-time Chat Orchestration

`C` Score: 6.13 | 2024-10-29

**Authors:** Anubhav Shrimal, Stanley Kanagaraj, Kriti Biswas, Swarnalatha Raghuraman, Anish Nediyanchath, Yi Zhang et al. (7 total)

**Categories:** cs.AI, cs.CL, cs.LG

**Scores:** Citation: 5.23 | Influential: 7.81 | Venue: 10.00 | Author: 4.79 | Recency: 5.00

**Links:** [arXiv](https://arxiv.org/abs/2410.21784) | [PDF](https://arxiv.org/pdf/2410.21784)

> 本文介绍了 MARCO，这是一个利用大语言模型自动化任务的多智能体实时聊天编排框架。MARCO 通过集成强大的护栏机制来解决复杂多步任务执行中的挑战，这些护栏用于引导 LLM 行为、验证输出并从格式不一致或幻觉等错误中恢复。实验证明，MARCO 在任务执行准确率上表现优异，同时显著降低了延迟和成本，其模块化设计使其适用于跨领域的复杂用例。

---

## #102 — Mapping Human Anti-collusion Mechanisms to Multi-agent AI

`C` Score: 6.12 | 2026-01-01

**Authors:** Jamiu Adekunle Idowu, Ahmed Almasoud, Ayman Alfahid

**Categories:** cs.MA, cs.AI, cs.CY

**Scores:** Citation: 7.08 | Influential: 7.81 | Venue: 2.00 | Author: 1.86 | Recency: 9.00

**Links:** [arXiv](https://arxiv.org/abs/2601.00360) | [PDF](https://arxiv.org/pdf/2601.00360)

> 本文将人类反共谋机制（如制裁、举报、监控等）映射到多智能体AI系统中，以解决AI智能体可能产生的共谋策略问题。作者为每种机制提出了实施方法，并强调了归因问题、身份流动性等开放性挑战。该研究为防止多智能体系统中的有害共谋提供了理论框架和实践指导。

---

## #103 — Stay in Character, Stay Safe: Dual-Cycle Adversarial Self-Evolution for Safety Role-Playing Agents

`C` Score: 6.09 | 2026-01-29

**Authors:** Mingyang Liao, Yichen Wan, shuchen wu, Chenxi Miao, Xin Shen, Weikang Li et al. (9 total)

**Categories:** cs.AI

**Scores:** Citation: 5.98 | Influential: 7.81 | Venue: 2.00 | Author: 4.27 | Recency: 10.00

**Links:** [arXiv](https://arxiv.org/abs/2602.13234) | [PDF](https://arxiv.org/pdf/2602.13234)

> 针对大模型角色扮演中严格遵守人设易受越狱攻击的问题，本文提出了一种免训练的双循环对抗自进化框架。该框架通过角色目标攻击者循环生成更强的越狱提示，并利用角色扮演防御者循环将失败案例提炼为包含全局规则、人设约束及安全示例的分层知识库。在推理阶段，防御者通过检索并组合该结构化知识，在保持角色行为一致性的同时有效抵御攻击，解决了传统训练方法成本高且不适用于闭源模型的难题。

---

## #104 — SafeSearch: Do Not Trade Safety for Utility in LLM Search Agents

`C` Score: 6.05 | 2025-10-19

**Authors:** Qiusi Zhan, Angeline Budiman-Chan, Abdelrahman Zayed, Xingzhi Guo, Daniel Kang, Joo-Kyung Kim

**Categories:** cs.CL

**Scores:** Citation: 5.72 | Influential: 7.81 | Venue: 5.00 | Author: 4.79 | Recency: 7.00

**Links:** [arXiv](https://arxiv.org/abs/2510.17017) | [PDF](https://arxiv.org/pdf/2510.17017)

> 针对搜索智能体易产生有害输出的问题，SafeSearch 提出了一种多目标强化学习方法，结合最终输出的安全/实用性奖励与查询级别的塑形项。该方法在保持问答性能的同时，将智能体的有害性降低了 90% 以上，实现了安全性与实用性的联合对齐。

---

## #105 — MobiLLM: An Agentic AI Framework for Closed-Loop Threat Mitigation in 6G Open RANs

`C` Score: 6.04 | 2025-09-25

**Authors:** Prakhar Sharma, Haohuang Wen, Vinod Yegneswaran, Ashish Gehani, Phillip Porras, Zhiqiang Lin

**Categories:** cs.CR, cs.AI, cs.LG

**Scores:** Citation: 4.11 | Influential: 7.81 | Venue: 5.00 | Author: 9.52 | Recency: 7.00

**Links:** [arXiv](https://arxiv.org/abs/2509.21634) | [PDF](https://arxiv.org/pdf/2509.21634)

> 本文提出了MobiLLM，一个专为6G开放无线接入网设计的智能体AI框架，旨在解决传统安全防御被动、劳动密集且难以应对复杂威胁的问题。该框架利用大语言模型驱动的模块化多智能体系统，实现了全自动、端到端的闭环威胁缓解与响应。其核心创新在于通过智能体编排安全工作流，为下一代网络架构提供了具备高韧性和自主性的安全解决方案。

---

## #106 — The Agentic Regulator: Risks for AI in Finance and a Proposed Agent-based Framework for Governance

`C` Score: 6.04 | 2025-12-12

**Authors:** Eren Kurshan, Tucker Balch, David Byrd

**Categories:** cs.CY, cs.AI, cs.CE

**Scores:** Citation: 4.84 | Influential: 7.81 | Venue: 2.00 | Author: 7.99 | Recency: 9.00

**Links:** [arXiv](https://arxiv.org/abs/2512.11933) | [PDF](https://arxiv.org/pdf/2512.11933)

> 本文针对生成式和智能体 AI 在金融市场的快速部署，提出了一个基于复杂适应系统理论的模块化治理架构。该框架将监督分解为四层“监管模块”：嵌入模型的自监管模块、聚合遥测的公司级治理模块、监控部门级指标的监管机构托管智能体以及提供第三方保证的独立审计模块。通过多智能体交易中突发欺骗的案例研究，展示了分层控制如何在实时隔离有害行为的同时保持创新，为金融系统中具有韧性和适应性的 AI 治理提供了实用路径。

---

## #107 — Parallelism Meets Adaptiveness: Scalable Documents Understanding in Multi-Agent LLM Systems

`C` Score: 6.03 | 2025-07-22

**Authors:** Chengxuan Xia, Qianye Wu, Sixuan Tian, Yilun Hao

**Categories:** cs.MA, cs.AI, cs.IR

**Scores:** Citation: 7.56 | Influential: 7.81 | Venue: 2.00 | Author: 1.12 | Recency: 7.00

**Links:** [arXiv](https://arxiv.org/abs/2507.17061) | [PDF](https://arxiv.org/pdf/2507.17061)

> 本文提出了一种多智能体LLM系统的协调框架，通过动态任务路由、双向反馈和并行智能体评估三个核心机制实现适应性。该框架允许智能体根据置信度和工作负载重新分配任务，交换结构化批评以迭代改进输出，并在高模糊度子任务上竞争，由评估者驱动选择最合适结果。实验表明，该方法在事实覆盖、连贯性和效率方面显著优于静态和部分自适应基线，突显了在多智能体LLM系统中融入适应性和结构化竞争的益处。

---

## #108 — Safeguarding AI Agents: Developing and Analyzing Safety Architectures

`C` Score: 6.00 | 2024-09-03

**Authors:** Ishaan Domkundwar, Mukunda N S, Ishaan Bhola, Riddhik Kochhar

**Categories:** cs.CR, cs.AI

**Scores:** Citation: 6.91 | Influential: 9.02 | Venue: 2.00 | Author: 2.55 | Recency: 5.00

**Links:** [arXiv](https://arxiv.org/abs/2409.03793) | [PDF](https://arxiv.org/pdf/2409.03793)

> 本文针对AI智能体在关键行业应用中的安全风险，提出了并评估了三种增强安全协议的框架：基于LLM的输入输出过滤器、集成安全智能体以及具有嵌入式安全检查的分层委托系统。通过在一系列不安全用例中测试，证明了这些框架能有效减轻部署风险，显著加强AI智能体系统的安全性。

---

## #109 — Using the NANDA Index Architecture in Practice: An Enterprise Perspective

`C` Score: 5.98 | 2025-08-05

**Authors:** Sichao Wang, Ramesh Raskar, Mahesh Lambe, Pradyumna Chari, Rekha Singhal, Shailja Gupta et al. (8 total)

**Categories:** cs.NI, cs.AI, cs.MA

**Scores:** Citation: 5.86 | Influential: 7.81 | Venue: 2.00 | Author: 5.88 | Recency: 7.00

**Links:** [arXiv](https://arxiv.org/abs/2508.03101) | [PDF](https://arxiv.org/pdf/2508.03101)

> 本文提出了NANDA框架，为安全、可互操作的AI智能体生态系统提供基础架构。该框架通过AgentFacts实现加密可验证的能力证明，并实施零信任智能体访问原则，以解决能力欺骗、冒充攻击和敏感数据泄露等安全问题。

---

## #110 — CyberSentinel: An Emergent Threat Detection System for AI Security

`C` Score: 5.96 | 2025-02-20

**Authors:** Krti Tallam

**Categories:** cs.CR, cs.AI

**Scores:** Citation: 6.41 | Influential: 7.81 | Venue: 2.00 | Author: 5.40 | Recency: 5.00

**Links:** [arXiv](https://arxiv.org/abs/2502.14966) | [PDF](https://arxiv.org/pdf/2502.14966)

> 本文介绍了CyberSentinel，一个统一的单代理系统，用于新兴威胁检测，旨在实时识别和减轻新的安全风险。CyberSentinel集成三种关键功能：通过SSH日志分析进行暴力攻击检测，使用域名黑名单和启发式URL评分进行钓鱼威胁评估，以及基于机器学习的异常检测进行新兴威胁检测。该系统通过持续适应不断演变的对抗策略，加强了主动网络安全防御，解决了AI安全中的关键漏洞。

---

## #111 — RoboSafe: Safeguarding Embodied Agents via Executable Safety Logic

`C` Score: 5.96 | 2025-12-24

**Authors:** Le Wang, Zonghao Ying, Xiao Yang, Quanchen Zou, Zhenfei Yin, Tianlin Li et al. (10 total)

**Categories:** cs.AI, cs.CV, cs.RO

**Scores:** Citation: 5.08 | Influential: 7.81 | Venue: 2.00 | Author: 6.75 | Recency: 9.00

**Links:** [arXiv](https://arxiv.org/abs/2512.21220) | [PDF](https://arxiv.org/pdf/2512.21220)

> 本文提出了RoboSafe，一种通过可执行谓词安全逻辑保护具身智能体的混合推理运行时护栏。该框架结合了基于短期记忆的逆向反思推理和基于长期记忆的前向预测推理，能够主动检测违规并重新规划。实验表明，RoboSafe显著降低了危险行为的发生率，相比基线模型表现出更强的环境适应性和安全性。

---

## #112 — Trustworthy Agentic AI Requires Deterministic Architectural Boundaries

`C` Score: 5.95 | 2026-02-10

**Authors:** Manish Bhattarai, Minh Vu

**Categories:** cs.CR

**Scores:** Citation: 6.47 | Influential: 7.81 | Venue: 2.00 | Author: 1.86 | Recency: 10.00

**Links:** [arXiv](https://arxiv.org/abs/2602.09947) | [PDF](https://arxiv.org/pdf/2602.09947)

> 本文论证了当前智能体AI架构与高风险科学工作流的安全要求根本不兼容，指出仅靠对齐无法解决授权安全问题。作者提出了三一防御架构，通过有限动作演算的治理、强制访问标签的信息流控制以及感知与执行的特权分离，强制执行确定性安全。该研究强调，在将智能体AI部署于关键科学领域之前，必须进行架构中介而非仅依赖概率性学习行为。

---

## #113 — Securing Agentic AI Systems -- A Multilayer Security Framework

`C` Score: 5.90 | 2025-12-19

**Authors:** Sunil Arora, John Hastings

**Categories:** cs.CR, cs.AI, cs.CY

**Scores:** Citation: 6.83 | Influential: 7.81 | Venue: 2.00 | Author: 1.12 | Recency: 9.00

**Links:** [arXiv](https://arxiv.org/abs/2512.18043) | [PDF](https://arxiv.org/pdf/2512.18043)

> 提出MAAIS，一个专门为智能体AI系统设计的生命周期感知安全框架。该框架引入了智能体AI的CIAA概念，通过集成多层防御来维护全生命周期的安全，并与MITRE ATLAS战术映射验证，为企业CISO和工程团队提供了结构化的安全部署和治理方法。

---

## #114 — Enhancing LLM Agent Safety via Causal Influence Prompting

`C` Score: 5.86 | 2025-07-01

**Authors:** Dongyoon Hahm, Woogyeol Jin, June Suk Choi, Sungsoo Ahn, Kimin Lee

**Categories:** cs.AI, cs.CL, cs.LG

**Scores:** Citation: 4.70 | Influential: 7.81 | Venue: 10.00 | Author: 3.23 | Recency: 7.00

**Links:** [arXiv](https://arxiv.org/abs/2507.00979) | [PDF](https://arxiv.org/pdf/2507.00979)

> 本文介绍了CIP技术，利用因果影响图来识别和减轻大语言模型代理在决策过程中的风险。该方法通过初始化因果图、引导代理交互以及基于观察结果迭代优化因果图，使代理能够预见有害结果并做出更安全的决策。实验证明，该方法有效增强了代码执行和设备控制任务中的安全性。

---

## #115 — Policy-as-Prompt: Turning AI Governance Rules into Guardrails for AI Agents

`C` Score: 5.81 | 2025-09-28

**Authors:** Gauri Kholkar, Ratinder Ahuja

**Categories:** cs.CL, cs.AI

**Scores:** Citation: 6.53 | Influential: 9.02 | Venue: 2.00 | Author: 1.12 | Recency: 7.00

**Links:** [arXiv](https://arxiv.org/abs/2509.23994) | [PDF](https://arxiv.org/pdf/2509.23994)

> 本文提出了Policy-as-Prompt框架，旨在将非结构化的治理规则文档转换为可验证的运行时护栏。该方法通过构建源链接的策略树并将其编译为轻量级分类器，实现了对自主AI代理的实时监控，有效执行最小权限原则和数据最小化，同时提供了完整的可追溯性和审计日志。

---

## #116 — TAME: A Trustworthy Test-Time Evolution of Agent Memory with Systematic Benchmarking

`C` Score: 5.81 | 2026-02-03

**Authors:** Yu Cheng, Jiuan Zhou, Yongkang Hu, Yihang Chen, Huichi Zhou, Mingang Chen et al. (10 total)

**Categories:** cs.AI, cs.LG

**Scores:** Citation: 6.15 | Influential: 7.81 | Venue: 2.00 | Author: 1.86 | Recency: 10.00

**Links:** [arXiv](https://arxiv.org/abs/2602.03224) | [PDF](https://arxiv.org/pdf/2602.03224)

> 本文针对Agent记忆在良性任务演化过程中安全性对齐易受损的“记忆误进化”现象，提出了TAME双记忆进化框架。TAME通过分离执行器记忆和评估器记忆，在提升任务性能的同时基于历史反馈完善安全性和效用评估，从而在良性任务演化中保持可信度。实验表明，TAME有效缓解了误进化问题，实现了可信度和任务性能的联合提升。

---

## #117 — Who's the Mole? Modeling and Detecting Intention-Hiding Malicious Agents in LLM-Based Multi-Agent Systems

`C` Score: 5.80 | 2025-07-07

**Authors:** Yizhe Xie, Congcong Zhu, Xinyue Zhang, Tianqing Zhu, Dayong Ye, Minghao Wang et al. (7 total)

**Categories:** cs.MA, cs.AI

**Scores:** Citation: 6.33 | Influential: 7.81 | Venue: 2.00 | Author: 3.23 | Recency: 7.00

**Links:** [arXiv](https://arxiv.org/abs/2507.04724) | [PDF](https://arxiv.org/pdf/2507.04724)

> 本文研究了LLM多智能体系统中的意图隐藏威胁，设计了四种隐蔽的攻击范式。作者提出了受心理学启发的AgentXposed检测框架，结合HEXACO人格模型和雷德审讯技术，通过渐进式探询和行为监控有效识别恶意智能体。

---

## #118 — Guardians of the Agentic System: Preventing Many Shots Jailbreak with Agentic System

`C` Score: 5.79 | 2025-02-23

**Authors:** Saikat Barua, Mostafizur Rahman, Md Jafor Sadek, Rafiul Islam, Shehenaz Khaled, Ahmedul Kabir

**Categories:** cs.CR

**Scores:** Citation: 6.44 | Influential: 9.02 | Venue: 2.00 | Author: 2.55 | Recency: 5.00

**Links:** [arXiv](https://arxiv.org/abs/2502.16750) | [PDF](https://arxiv.org/pdf/2502.16750)

> 本文关注基于LLM的自主AI代理的安全问题，特别是针对多轮越狱和欺骗性对齐等高级攻击。作者提出通过开发新的评估框架来增强安全性，使用三种检测方法识别恶意代理，并开发了一个反越狱系统。在GEMINI 1.5 pro等模型上的测试显示，检测能力很强（94%准确率），但在长期攻击下存在持续漏洞。研究强调需要基于主动监控的灵活安全系统，以应对日益复杂的攻击场景。

---

## #119 — A biologically Inspired Trust Model for Open Multi-Agent Systems that is Resilient to Rapid Performance Fluctuations

`C` Score: 5.79 | 2025-04-17

**Authors:** Zoi Lygizou, Dimitris Kalles

**Categories:** cs.MA, cs.AI, cs.DC

**Scores:** Citation: 5.70 | Influential: 7.81 | Venue: 10.00 | Author: 1.12 | Recency: 5.00

**Links:** [arXiv](https://arxiv.org/abs/2504.15301) | [PDF](https://arxiv.org/pdf/2504.15301)

> 本文提出了一种受生物学启发的信任模型，用于解决开放多智能体系统中的移动性、行为变化和冷启动问题。该模型引入了自我分类机制，使服务提供者能够检测性能下降，从而提高对动态行为的适应性。模拟结果表明，该算法在处理动态受托人行为方面优于FIRE模型，并具有抗攻击能力。

---

## #120 — Hierarchical Multi-Agent Reinforcement Learning with Control Barrier Functions for Safety-Critical Autonomous Systems

`C` Score: 5.76 | 2025-07-20

**Authors:** H. M. Sabbir Ahmad, Ehsan Sabouni, Alexander Wasilkoff, Param Budhraja, Zijian Guo, Songyuan Zhang et al. (9 total)

**Categories:** cs.LG, cs.AI, cs.RO

**Scores:** Citation: 5.73 | Influential: 7.81 | Venue: 2.00 | Author: 4.79 | Recency: 7.00

**Links:** [arXiv](https://arxiv.org/abs/2507.14850) | [PDF](https://arxiv.org/pdf/2507.14850)

> 本文针对多智能体安全关键自主系统，提出了一种基于控制屏障函数(CBF)的安全分层多智能体强化学习(HMARL)方法。该方法将学习问题分解为两个层次：高层学习智能体间的联合协作行为，低层学习基于高层策略的安全个体行为。作者提出的基于技能的HMARL-CBF算法使高层学习智能体技能的联合策略，低层使用CBF安全执行技能。在复杂道路网络导航场景中验证，该方法显著提高了安全性，实现近完美(5%以内)的成功/安全率，同时改善了所有环境中的性能。

---

## #121 — Agentic JWT: A Secure Delegation Protocol for Autonomous AI Agents

`C` Score: 5.74 | 2025-09-16

**Authors:** Abhishek Goswami

**Categories:** cs.CR, cs.AI

**Scores:** Citation: 7.09 | Influential: 7.81 | Venue: 2.00 | Author: 0.58 | Recency: 7.00

**Links:** [arXiv](https://arxiv.org/abs/2509.13597) | [PDF](https://arxiv.org/pdf/2509.13597)

> 本文提出了Agentic JWT (A-JWT)，一种安全的自主AI代理委托协议，通过双面意图令牌将代理的每个操作绑定到可验证的用户意图。该协议包含代理身份哈希、链式委托断言和防重放密钥，通过轻量级客户端库实现了零信任保证，有效防止了范围违规、重放和提示注入攻击。

---

## #122 — The Hunger Game Debate: On the Emergence of Over-Competition in Multi-Agent Systems

`C` Score: 5.73 | 2025-09-30

**Authors:** Xinbei Ma, Ruotian Ma, Xingyu Chen, Zhengliang Shi, Mengru Wang, Jen-tse Huang et al. (17 total)

**Categories:** cs.CL

**Scores:** Citation: 4.15 | Influential: 7.81 | Venue: 2.00 | Author: 9.34 | Recency: 7.00

**Links:** [arXiv](https://arxiv.org/abs/2509.26126) | [PDF](https://arxiv.org/pdf/2509.26126)

> 本文提出了 HATE 框架，研究了多代理辩论中因极端竞争压力导致的过度竞争现象及其对任务性能的负面影响。实验表明，竞争压力会引发不可靠和有害行为，而引入客观的、以任务为中心的反馈可以有效缓解这种过度竞争行为，为理解 AI 社区的涌现社会动态及治理提供了重要见解。

---

## #123 — AgentCrypt: Advancing Privacy and (Secure) Computation in AI Agent Collaboration

`C` Score: 5.70 | 2025-12-08

**Authors:** Harish Karthikeyan, Yue Guo, Leo de Castro, Antigoni Polychroniadou, Udari Madhushani Sehwag, Leo Ardon et al. (8 total)

**Categories:** cs.CR

**Scores:** Citation: 3.32 | Influential: 7.81 | Venue: 5.00 | Author: 8.33 | Recency: 9.00

**Links:** [arXiv](https://arxiv.org/abs/2512.08104) | [PDF](https://arxiv.org/pdf/2512.08104)

> 论文介绍了AgentCrypt，一个三层安全通信框架，通过同态加密和上下文感知掩码等技术，为AI智能体协作提供确定性保护。该方法将安全性与智能体的概率推理解耦，确保敏感数据在整个计算生命周期中受到严格保护，克服了数据孤岛等障碍。

---

## #124 — Actor Critic with Experience Replay-based automatic treatment planning for prostate cancer intensity modulated radiotherapy

`C` Score: 5.68 | 2025-02-01

**Authors:** Md Mainul Abrar, Parvat Sapkota, Damon Sprouts, Xun Jia, Yujie Chi

**Categories:** physics.med-ph, cs.AI, cs.LG

**Scores:** Citation: 5.14 | Influential: 7.81 | Venue: 5.00 | Author: 5.40 | Recency: 5.00

**Links:** [arXiv](https://arxiv.org/abs/2502.00346) | [PDF](https://arxiv.org/pdf/2502.00346)

> 这篇论文提出了一种基于Actor Critic与经验回放(ACER)架构的深度强化学习方法，用于前列腺癌强度调制放射治疗的自动治疗计划。该方法通过逆向计划调整治疗参数，仅需单个病例训练即可实现广泛适用性，并采用快速梯度符号方法(FGSM)增强对抗攻击鲁棒性，在300多个计划测试中展现出高质量和稳健性。

---

## #125 — Securing AI Agents: Implementing Role-Based Access Control for Industrial Applications

`C` Score: 5.67 | 2025-09-14

**Authors:** Aadil Gani Ganie

**Categories:** cs.AI, cs.CL

**Scores:** Citation: 6.29 | Influential: 7.81 | Venue: 2.00 | Author: 2.55 | Recency: 7.00

**Links:** [arXiv](https://arxiv.org/abs/2509.11431) | [PDF](https://arxiv.org/pdf/2509.11431)

> 本文针对工业环境中 AI Agent 面临的安全威胁（如提示注入攻击），提出了一种将基于角色的访问控制（RBAC）集成到 AI Agent 中的框架。该框架通过提供稳健的安全护栏，旨在支持 AI Agent 在本地部署环境下的有效和可扩展应用，从而增强其完整性和可靠性。

---

## #126 — What's the next frontier for Data-centric AI? Data Savvy Agents

`C` Score: 5.66 | 2025-11-02

**Authors:** Nabeel Seedat, Jiashuo Liu, Mihaela van der Schaar

**Categories:** cs.LG

**Scores:** Citation: 3.32 | Influential: 7.81 | Venue: 2.00 | Author: 10.00 | Recency: 9.00

**Links:** [arXiv](https://arxiv.org/abs/2511.01015) | [PDF](https://arxiv.org/pdf/2511.01015)

> 本文探讨了Agent在数据处理方面的能力，提出了“数据精通Agent”作为以数据为中心的AI下一个前沿。文章定义了主动数据获取、复杂数据处理、交互式测试数据合成和持续适应四个关键能力，旨在确保Agent在现实世界部署中的可靠性和可扩展性。

---

## #127 — Control Tax: The Price of Keeping AI in Check

`C` Score: 5.64 | 2025-06-05

**Authors:** Mikhail Terekhov, Zhen Ning David Liu, Caglar Gulcehre, Samuel Albanie

**Categories:** cs.AI, cs.LG

**Scores:** Citation: 5.26 | Influential: 7.81 | Venue: 2.00 | Author: 5.40 | Recency: 7.00

**Links:** [arXiv](https://arxiv.org/abs/2506.05296) | [PDF](https://arxiv.org/pdf/2506.05296)

> 本文引入了“控制税”概念，用于量化在AI管道中集成控制措施的操作和财务成本。作者提出了一个理论框架，将分类器性能映射到安全保证，并评估了对抗性设置下的语言模型。该研究通过平衡安全性与成本效益，为AI控制领域的实际应用提供了经济可行性评估。

---

## #128 — Building an Internal Coding Agent at Zup: Lessons and Open Questions

`C` Score: 5.62 | 2026-04-10

**Authors:** Gustavo Pinto, Pedro Eduardo de Paula Naves, Ana Paula Camargo, Marselle Silva

**Categories:** cs.SE

**Scores:** Citation: 3.32 | Influential: 7.81 | Venue: 2.00 | Author: 9.09 | Recency: 10.00

**Links:** [arXiv](https://arxiv.org/abs/2604.09805) | [PDF](https://arxiv.org/pdf/2604.09805)

> 本文分享了在企业内部构建编码代理的经验，指出技术模型质量本身不足，工具设计、安全执行、状态管理和人类信任校同等同样决定性。作者介绍了Zup的内部编码代理CodeGen，表明有针对性的工具设计和分层安全护栏比提示工程更能提高代理可靠性，而渐进式人工监督模式推动了有机采用。这些发现表明，围绕模型的工程决策——而非模型本身——决定了编码代理在实践中是否提供真正的价值。

---

## #129 — AAGATE: A NIST AI RMF-Aligned Governance Platform for Agentic AI

`C` Score: 5.57 | 2025-10-29

**Authors:** Ken Huang, Kyriakos Rock Lambros, Jerry Huang, Yasir Mehmood, Hammad Atta, Joshua Beck et al. (11 total)

**Categories:** cs.CR, cs.AI

**Scores:** Citation: 5.84 | Influential: 7.81 | Venue: 2.00 | Author: 1.86 | Recency: 9.00

**Links:** [arXiv](https://arxiv.org/abs/2510.25863) | [PDF](https://arxiv.org/pdf/2510.25863)

> 本文提出了 AAGATE，这是一个专为生产环境中自主语言模型驱动的 Agent 设计的 Kubernetes 原生治理控制平面。该平台通过运作化 NIST AI 风险管理框架，整合了 MAESTRO 威胁建模、OWASP AIVSS 及 CSA 红队指南等多种安全框架，并引入零信任服务网格和可解释策略引擎。其核心创新在于为 Agent AI 提供了一套持续、可验证的治理解决方案，确保了系统在机器速度下的安全性与可问责性。

---

## #130 — MASTER: Multi-Agent Security Through Exploration of Roles and Topological Structures -- A Comprehensive Framework

`C` Score: 5.56 | 2025-05-24

**Authors:** Yifan Zhu, Chao Zhang, Xin Shi, Xueqiao Zhang, Yi Yang, Yawei Luo

**Categories:** cs.MA, cs.AI

**Scores:** Citation: 3.32 | Influential: 7.81 | Venue: 10.00 | Author: 5.40 | Recency: 7.00

**Links:** [arXiv](https://arxiv.org/abs/2505.18572) | [PDF](https://arxiv.org/pdf/2505.18572)

> 本文介绍了MASTER，一个专注于多智能体系统（MAS）安全的研究框架。该框架通过探索多样化的角色配置和拓扑结构，设计了场景自适应的攻击策略，并提出了相应的防御措施，显著增强了MAS在不同场景下的韧性，为未来研究提供了宝贵见解。

---

## #131 — Challenges and Future Directions in Agentic Reverse Engineering Systems

`C` Score: 5.56 | 2026-04-15

**Authors:** Salem Radey, Jack West, Kassem Fawaz

**Categories:** cs.CR, cs.AI

**Scores:** Citation: 3.32 | Influential: 7.81 | Venue: 2.00 | Author: 8.73 | Recency: 10.00

**Links:** [arXiv](https://arxiv.org/abs/2604.14317) | [PDF](https://arxiv.org/pdf/2604.14317)

> 本文研究基于LLMs的代理系统在二进制逆向工程任务中的表现。分析现有代理工具使用情况，识别出令牌限制、混淆处理困难和程序护栏缺乏等局限性。从安全角度，作者概述当前挑战并指出未来方向，强调系统设计者需要解决这些限制，以提升代理系统在复杂RE场景中的能力，特别是涉及混淆、定时和独特架构的场景。

---

## #132 — Banking Done Right: Redefining Retail Banking with Language-Centric AI

`C` Score: 5.55 | 2025-10-09

**Authors:** Xin Jie Chua, Jeraelyn Ming Li Tan, Jia Xuan Tan, Soon Chang Poh, Yi Xian Goh, Debbie Hui Tian Choong et al. (9 total)

**Categories:** cs.CL, cs.AI

**Scores:** Citation: 4.24 | Influential: 7.81 | Venue: 10.00 | Author: 2.55 | Recency: 7.00

**Links:** [arXiv](https://arxiv.org/abs/2510.07645) | [PDF](https://arxiv.org/pdf/2510.07645)

> 本文介绍了 Ryt AI，这是一个基于大语言模型的智能体框架，赋能 Ryt Bank 实现通过自然语言对话执行核心金融交易，标志着全球首个获监管批准的以对话 AI 为主要界面的银行系统部署。该系统利用内部开发的 ILMU 模型，通过四个专用智能体（护栏、意图、支付、FAQ）编排对话，并采用确定性护栏、人机回路确认及无状态审计架构，在确保安全合规的同时实现了银行业务流程的重构。

---

## #133 — QuadSentinel: Sequent Safety for Machine-Checkable Control in Multi-agent Systems

`C` Score: 5.52 | 2025-12-18

**Authors:** Yiliu Yang, Yilei Jiang, Qunzhong Wang, Yingshui Tan, Xiaoyong Zhu, Sherman S. M. Chow et al. (8 total)

**Categories:** cs.AI, cs.CL

**Scores:** Citation: 4.93 | Influential: 7.81 | Venue: 2.00 | Author: 4.27 | Recency: 9.00

**Links:** [arXiv](https://arxiv.org/abs/2512.16279) | [PDF](https://arxiv.org/pdf/2512.16279)

> 提出QuadSentinel，一个由四个智能体（状态追踪器、策略验证器、威胁监视器和裁判员）组成的防护系统。该系统将自然语言安全策略编译为机器可检查的规则，并通过高效的谓词更新器在线执行，显著提升了多智能体系统的护栏准确性和规则召回率。

---

## #134 — Human Society-Inspired Approaches to Agentic AI Security: The 4C Framework

`C` Score: 5.50 | 2026-02-02

**Authors:** Alsharif Abuadbba, Nazatul Sultan, Surya Nepal, Sanjay Jha

**Categories:** cs.CR, cs.AI

**Scores:** Citation: 3.32 | Influential: 7.81 | Venue: 2.00 | Author: 8.33 | Recency: 10.00

**Links:** [arXiv](https://arxiv.org/abs/2602.01942) | [PDF](https://arxiv.org/pdf/2602.01942)

> 本文提出了 4C 框架，受社会治理启发，用于解决 Agentic AI 系统带来的新型网络安全风险。该框架从核心、连接、认知和合规四个相互依赖的维度组织智能体风险，强调行为完整性和意图保护。它为构建值得信赖且符合人类价值观的智能体系统提供了原则性基础。

---

## #135 — MCPShield: A Security Cognition Layer for Adaptive Trust Calibration in Model Context Protocol Agents

`C` Score: 5.48 | 2026-02-15

**Authors:** Zhenhong Zhou, Yuanhe Zhang, Hongwei Cai, Moayad Aloqaily, Ouns Bouachir, Linsey Pang et al. (9 total)

**Categories:** cs.CR, cs.CL

**Scores:** Citation: 3.32 | Influential: 7.81 | Venue: 2.00 | Author: 8.15 | Recency: 10.00

**Links:** [arXiv](https://arxiv.org/abs/2602.14281) | [PDF](https://arxiv.org/pdf/2602.14281)

> 本文提出了MCPShield，一个用于模型上下文协议（MCP）代理的安全认知层，旨在解决代理与不可信第三方服务器之间的安全错位问题。受人类工具验证经验的启发，MCPShield通过元数据引导的探测和基于历史痕迹的推理来建立安全认知，从而在工具调用过程中约束执行边界。实验表明，MCPShield在防御六种新型MCP攻击场景中表现出强大的泛化能力，且部署开销低。

---

## #136 — Caging the Agents: A Zero Trust Security Architecture for Autonomous AI in Healthcare

`C` Score: 5.48 | 2026-03-18

**Authors:** Saikat Maiti

**Categories:** cs.CR, cs.AI

**Scores:** Citation: 3.32 | Influential: 7.81 | Venue: 2.00 | Author: 8.15 | Recency: 10.00

**Links:** [arXiv](https://arxiv.org/abs/2603.17419) | [PDF](https://arxiv.org/pdf/2603.17419)

> 本文提出了一种针对医疗保健领域自主AI Agent的零信任安全架构，旨在解决凭证泄露、执行滥用等潜在HIPAA违规风险。该架构实施了包括内核级工作负载隔离、凭证代理、网络出口策略和提示完整性框架在内的四层深度防御机制。通过90天的生产环境部署，该架构成功发现了多个高危漏洞，验证了其在处理敏感信息环境中的有效性。

---

## #137 — Blockchain and AI: Securing Intelligent Networks for the Future

`C` Score: 5.48 | 2026-04-07

**Authors:** Joy Dutta, Hossien B. Eldeeb, Tu Dac Ho

**Categories:** cs.CR, cs.AI

**Scores:** Citation: 3.32 | Influential: 7.81 | Venue: 2.00 | Author: 8.15 | Recency: 10.00

**Links:** [arXiv](https://arxiv.org/abs/2604.06323) | [PDF](https://arxiv.org/pdf/2604.06323)

> 该论文通过三个贡献整合区块链-AI安全领域：智能网络区块链-AI安全分类法、可验证和自适应安全工作流集成模式、区块链-AI安全评估蓝图（BASE）。论文映射了物联网、关键基础设施等领域的证据景观，指出区块链提供溯源性和可审计性，AI提供检测和适应能力，未来工作应关注互操作性接口和隐私保护分析。

---

## #138 — SAFE--MA--RRT: Multi-Agent Motion Planning with Data-Driven Safety Certificates

`C` Score: 5.43 | 2025-09-04

**Authors:** Babak Esmaeili, Hamidreza Modares

**Categories:** eess.SY, cs.LG, cs.MA

**Scores:** Citation: 3.32 | Influential: 7.81 | Venue: 2.00 | Author: 9.83 | Recency: 7.00

**Links:** [arXiv](https://arxiv.org/abs/2509.04413) | [PDF](https://arxiv.org/pdf/2509.04413)

> 本文提出了一种完全数据驱动的多智能体运动规划框架，利用凸半定规划生成局部不变椭球体作为安全证书。该方法通过基于采样的规划器构建路径树，并结合时空预留表确保智能体间的避碰安全，实现了无需显式系统模型的安全轨迹合成。

---

## #139 — SafeClaw-R: Towards Safe and Secure Multi-Agent Personal Assistants

`C` Score: 5.43 | 2026-03-28

**Authors:** Haoyu Wang, Zibo Xiao, Yedi Zhang, Christopher M. Poskitt, Jun Sun

**Categories:** cs.CR

**Scores:** Citation: 3.32 | Influential: 7.81 | Venue: 2.00 | Author: 7.80 | Recency: 10.00

**Links:** [arXiv](https://arxiv.org/abs/2603.28807) | [PDF](https://arxiv.org/pdf/2603.28807)

> 针对基于LLM的多智能体系统在自主执行任务时面临的安全风险，本文提出了SafeClaw-R框架。该框架通过在执行前调解行动并将技能系统性地增强为安全对应项，将安全性作为执行图上的系统级不变量来强制执行。在生产力平台和代码执行环境等领域的评估显示，SafeClaw-R在Google Workspace场景中准确率达95.2%，并能有效检测恶意第三方技能模式，实现了对自主MAS的实用运行时安全强制。

---

## #140 — Towards Secure Agent Skills: Architecture, Threat Taxonomy, and Security Analysis

`C` Score: 5.40 | 2026-04-03

**Authors:** Zhiyuan Li, Jingzheng Wu, Xiang Ling, Xing Cui, Tianyue Luo

**Categories:** cs.CR, cs.AI

**Scores:** Citation: 3.32 | Influential: 7.81 | Venue: 2.00 | Author: 7.62 | Recency: 10.00

**Links:** [arXiv](https://arxiv.org/abs/2604.02837) | [PDF](https://arxiv.org/pdf/2604.02837)

> 该研究对Agent Skills框架进行了首次全面安全分析，定义了技能生命周期并识别各阶段的攻击表面，构建了包含三个攻击层、七个类别和十七个场景的威胁分类法。分析表明最严重威胁源于框架本身的结构特性，包括缺乏数据-指令边界和单一批准信任模型等。

---

## #141 — Reproducibility Study of "Cooperate or Collapse: Emergence of Sustainable Cooperation in a Society of LLM Agents"

`C` Score: 5.39 | 2025-05-14

**Authors:** Pedro M. P. Curvo, Mara Dragomir, Salvador Torpes, Mohammadmahdi Rahimi

**Categories:** cs.AI

**Scores:** Citation: 5.88 | Influential: 7.81 | Venue: 2.00 | Author: 1.86 | Recency: 7.00

**Links:** [arXiv](https://arxiv.org/abs/2505.09289) | [PDF](https://arxiv.org/pdf/2505.09289)

> 本研究复现并扩展了GovSim框架，评估了LLMs在资源共享场景中的合作决策能力。通过测试新模型、异构多智能体环境及日语指令等新设置，验证了大模型能实现可持续合作，且高性能模型能影响低性能模型的行为。结果证实了该基准在新模型、场景和语言中的适用性，为LLMs在复杂合作任务中的适应性提供了见解。

---

## #142 — SECURE: Semantics-aware Embodied Conversation under Unawareness for Lifelong Robot Learning

`C` Score: 5.38 | 2024-09-26

**Authors:** Rimvydas Rubavicius, Peter David Fagan, Alex Lascarides, Subramanian Ramamoorthy

**Categories:** cs.RO, cs.AI, cs.CL

**Scores:** Citation: 3.77 | Influential: 7.81 | Venue: 2.00 | Author: 9.48 | Recency: 5.00

**Links:** [arXiv](https://arxiv.org/abs/2409.17755) | [PDF](https://arxiv.org/pdf/2409.17755)

> 本文提出了SECURE交互式任务学习策略，旨在解决智能体在缺乏关键概念时的“无意识重排”挑战。该策略通过语义分析和具身对话，使智能体能够从用户的纠正反馈中学习新概念并调整领域模型，从而在模拟和真实环境中展现出更高的数据效率和任务泛化能力。

---

## #143 — Symbolic Guardrails for Domain-Specific Agents: Stronger Safety and Security Guarantees Without Sacrificing Utility

`C` Score: 5.37 | 2026-04-16

**Authors:** Yining Hong, Yining She, Eunsuk Kang, Christopher S. Timperley, Christian Kästner

**Categories:** cs.SE, cs.AI, cs.CR

**Scores:** Citation: 3.32 | Influential: 7.81 | Venue: 2.00 | Author: 7.43 | Recency: 10.00

**Links:** [arXiv](https://arxiv.org/abs/2604.15579) | [PDF](https://arxiv.org/pdf/2604.15579)

> 本文研究符号护栏作为AI agents强安全保证的实用路径。研究包括对80个agent安全基准的系统性回顾，发现74%的指定政策要求可通过符号护栏执行。实验表明，这些护栏能显著提高agents的安全性和安全性，同时不牺牲效用。特别对于领域特定AI agents，符号护栏提供了一种实用有效的方法来保证部分安全和安全要求。

---

## #144 — Who Gets the Reward, Who Gets the Blame? Evaluation-Aligned Training Signals for Multi-LLM Agents

`C` Score: 5.28 | 2025-11-11

**Authors:** Chih-Hsuan Yang, Tanwi Mallick, Le Chen, Krishnan Raghavan, Azton Wells, Amal Gueroudji et al. (8 total)

**Categories:** cs.MA, cs.AI, cs.CL

**Scores:** Citation: 4.56 | Influential: 7.81 | Venue: 2.00 | Author: 3.78 | Recency: 9.00

**Links:** [arXiv](https://arxiv.org/abs/2511.10687) | [PDF](https://arxiv.org/pdf/2511.10687)

> 本文提出了一个理论框架，将合作博弈论归因与过程奖励建模相结合，将系统级评估转化为智能体级和消息级的学习信号。该方法在成功时基于Shapley值公平分配信用，在失败时定位首个错误并生成修复感知偏好，从而产生有界、合作且兼容强化学习的信号。该工作为多智能体LLM训练中从全局评估到本地监督提供了统一且可审计的路径。

---

## #145 — POLARIS: Typed Planning and Governed Execution for Agentic AI in Back-Office Automation

`C` Score: 5.28 | 2026-01-16

**Authors:** Zahra Moslemi, Keerthi Koneru, Yen-Ting Lee, Sheethal Kumar, Ramesh Radhakrishnan

**Categories:** cs.AI

**Scores:** Citation: 5.62 | Influential: 7.81 | Venue: 2.00 | Author: 0.58 | Recency: 9.00

**Links:** [arXiv](https://arxiv.org/abs/2601.11816) | [PDF](https://arxiv.org/pdf/2601.11816)

> POLARIS 是一个受控编排框架，通过类型化规划合成和验证执行来确保企业后台自动化中的 Agent 安全。它利用策略护栏和验证机制，在减少人工干预的同时保证了决策质量和可审计性，为策略对齐的 Agentic AI 提供了基准参考。

---

## #146 — Building Better Environments for Autonomous Cyber Defence

`C` Score: 5.27 | 2026-04-09

**Authors:** Chris Hicks, Elizabeth Bates, Shae McFadden, Isaac Symes Thompson, Myles Foley, Ed Chapman et al. (15 total)

**Categories:** cs.CR, cs.AI

**Scores:** Citation: 3.32 | Influential: 7.81 | Venue: 2.00 | Author: 6.75 | Recency: 10.00

**Links:** [arXiv](https://arxiv.org/abs/2604.08805) | [PDF](https://arxiv.org/pdf/2604.08805)

> 该论文详细介绍了关于构建更好的强化学习环境用于自主网络防御的研讨会知识分享。参与者来自学术界、工业界和政府，具有丰富的RL和网络环境设计经验。论文贡献是双重的：分解RL网络环境与真实系统间界面的框架，以及基于研讨会关键发现的RL-based ACD环境开发和代理评估的最佳实践指南，为构建更好的自主网络防御环境提供了指导。

---

## #147 — Multi-Agent Causal Reasoning for Suicide Ideation Detection Through Online Conversations

`C` Score: 5.18 | 2026-02-27

**Authors:** Jun Li, Xiangmeng Wang, Haoyang Li, Yifei Yan, Shijie Zhang, Hong Va Leong et al. (9 total)

**Categories:** cs.CL

**Scores:** Citation: 3.32 | Influential: 7.81 | Venue: 2.00 | Author: 6.17 | Recency: 10.00

**Links:** [arXiv](https://arxiv.org/abs/2602.23577) | [PDF](https://arxiv.org/pdf/2602.23577)

> 本文提出了多智能体因果推理（MACR）框架，用于通过在线对话检测自杀意念。该框架协作运用推理智能体扩展用户交互，并利用偏见感知决策智能体通过前门调整策略缓解隐藏偏见（如从众心理），从而丰富上下文信息并提高检测准确性。

---

## #148 — LanG -- A Governance-Aware Agentic AI Platform for Unified Security Operations

`C` Score: 5.18 | 2026-04-07

**Authors:** Anes Abdennebi, Nadjia Kara, Laaziz Lahlou, Hakima Ould-Slimane

**Categories:** cs.CR, cs.AI

**Scores:** Citation: 3.32 | Influential: 7.81 | Venue: 2.00 | Author: 6.17 | Recency: 10.00

**Links:** [arXiv](https://arxiv.org/abs/2604.05440) | [PDF](https://arxiv.org/pdf/2604.05440)

> LanG是一个开源的治理感知代理AI平台，用于统一安全操作。它提供统一事件上下文记录（F1=87%）、基于LangGraph的代理AI编排器、微调的LLM规则生成器（96.2%接受率）、三阶段攻击重构器（87.5%杀链准确性）和分层治理-MCP-代理AI-安全架构。平台支持多租户隔离、基于角色的访问和完全本地部署，为托管服务提供商设计。

---

## #149 — Position: Stop Acting Like Language Model Agents Are Normal Agents

`C` Score: 5.16 | 2025-02-04

**Authors:** Elija Perrier, Michael Timothy Bennett

**Categories:** cs.AI, cs.CL

**Scores:** Citation: 5.81 | Influential: 7.81 | Venue: 2.00 | Author: 1.86 | Recency: 5.00

**Links:** [arXiv](https://arxiv.org/abs/2502.10420) | [PDF](https://arxiv.org/pdf/2502.10420)

> 该立场论文认为语言模型代理(LMAs)不应被视为普通代理，因为它们继承了大语言模型的结构问题：幻觉、越狱、错位和不可预测性。作者列举了LMAs固有的代理病理学，尽管有外部记忆和工具等支撑，它们仍然是本体论上无状态的、随机的、语义敏感的和语言中介的。这些病理学 destabilizes LMAs的可识别性、连续性、持久性和一致性等本体论属性，主张应测量这些属性以减轻负面影响。

---

## #150 — Extending the OWASP Multi-Agentic System Threat Modeling Guide: Insights from Multi-Agent Security Research

`C` Score: 5.16 | 2025-08-13

**Authors:** Klaudia Krawiecka, Christian Schroeder de Witt

**Categories:** cs.MA, cs.CR, cs.SE

**Scores:** Citation: 4.91 | Influential: 7.81 | Venue: 2.00 | Author: 3.23 | Recency: 7.00

**Links:** [arXiv](https://arxiv.org/abs/2508.09815) | [PDF](https://arxiv.org/pdf/2508.09815)

> 本文扩展了 OWASP 多智能体系统威胁建模指南，将多智能体安全研究转化为针对 LLM 驱动架构的实用指导。分析指出了现有分类法在建模失败方面的空白，引入了包括推理崩溃、指标过拟合和紧急隐蔽协调在内的新威胁类别。研究还概述了鲁棒性测试和紧急行为监控等评估策略，以提高现实世界部署中复杂自主系统的安全态势。

---

## #151 — Taxonomy of Comprehensive Safety for Clinical Agents

`C` Score: 5.14 | 2025-09-26

**Authors:** Jean Seo, Hyunkyung Lee, Gibaeg Kim, Wooseok Han, Jaehyo Yoo, Seungseop Lim et al. (8 total)

**Categories:** cs.CL

**Scores:** Citation: 3.32 | Influential: 7.81 | Venue: 10.00 | Author: 2.55 | Recency: 7.00

**Links:** [arXiv](https://arxiv.org/abs/2509.22041) | [PDF](https://arxiv.org/pdf/2509.22041)

> 本文提出了TACOS（临床Agent全面安全分类法），这是一个包含21个类别的细粒度分类法，旨在解决临床聊天机器人中现有安全方法（如护栏和工具调用）的不足。TACOS将安全过滤和工具选择整合到单一的用户意图分类步骤中，能够覆盖广泛的临床和非临床查询，并明确建模不同的安全阈值和外部工具依赖。通过构建TACOS标注数据集并进行实验，验证了该分类法在临床Agent环境中的价值，并揭示了训练数据分布和基础模型预训练知识的有用见解。

---

## #152 — ClawGuard: A Runtime Security Framework for Tool-Augmented LLM Agents Against Indirect Prompt Injection

`C` Score: 5.14 | 2026-04-13

**Authors:** Wei Zhao, Zhe Li, Peixin Zhang, Jun Sun

**Categories:** cs.CR, cs.AI

**Scores:** Citation: 3.32 | Influential: 7.81 | Venue: 2.00 | Author: 5.88 | Recency: 10.00

**Links:** [arXiv](https://arxiv.org/abs/2604.11790) | [PDF](https://arxiv.org/pdf/2604.11790)

> 本文介绍了ClawGuard，一个针对工具增强的LLM代理的运行时安全框架，用于防御间接提示注入。该方法在每个工具调用边界强制执行用户确认的规则集，将不可靠的对齐依赖防御转变为确定性、可审计的机制。通过在任何外部工具调用前自动从用户陈述的目标中派生任务特定访问约束，ClawGuard无需修改模型或基础设施即可阻止所有三种注入途径。实验表明，ClawGuard在五个最先进的语言模型上实现了对间接提示注入的强大保护，同时不损害代理效用。

---

## #153 — Explanation Design in Strategic Learning: Sufficient Explanations that Induce Non-harmful Responses

`C` Score: 5.08 | 2025-02-06

**Authors:** Kiet Q. H. Vo, Siu Lun Chau, Masahiro Kato, Yixin Wang, Krikamol Muandet

**Categories:** cs.AI

**Scores:** Citation: 3.32 | Influential: 7.81 | Venue: 2.00 | Author: 8.84 | Recency: 5.00

**Links:** [arXiv](https://arxiv.org/abs/2502.04058) | [PDF](https://arxiv.org/pdf/2502.04058)

> 研究探讨了算法决策中战略代理人的解释设计问题，分析了著名解释方法并建立了防止解释误导代理人采取自我伤害行为的必要条件。在条件同质性假设下，证明了基于行动推荐的解释(ARexes)足以产生非有害响应。作者提出的联合优化预测模型和解释策略的学习程序，在合成和真实任务中展示了DM优化预测性能同时保留代理人效用的能力，为安全解释设计提供了新思路。

---

## #154 — BlueCodeAgent: A Blue Teaming Agent Enabled by Automated Red Teaming for CodeGen AI

`C` Score: 5.07 | 2025-10-20

**Authors:** Chengquan Guo, Yuzhou Nie, Chulin Xie, Zinan Lin, Wenbo Guo, Bo Li

**Categories:** cs.SE

**Scores:** Citation: 3.32 | Influential: 7.81 | Venue: 2.00 | Author: 7.43 | Recency: 7.00

**Links:** [arXiv](https://arxiv.org/abs/2510.18131) | [PDF](https://arxiv.org/pdf/2510.18131)

> 本文提出了BlueCodeAgent，一个由自动化红队测试支持的端到端蓝队Agent，旨在全面保障代码生成AI的安全。该框架集成红队生成风险实例，蓝队则利用宪法和代码分析检测已知和未知风险场景，有效降低了漏洞检测中的误报率，显著提升了代码安全防御的整体能力。

---

## #155 — An Approach to Checking Correctness for Agentic Systems

`C` Score: 5.06 | 2025-08-19

**Authors:** Thomas J Sheffler

**Categories:** cs.AI, cs.ET

**Scores:** Citation: 3.96 | Influential: 7.81 | Venue: 2.00 | Author: 5.40 | Recency: 7.00

**Links:** [arXiv](https://arxiv.org/abs/2509.20364) | [PDF](https://arxiv.org/pdf/2509.20364)

> 本文提出了一种基于时序逻辑的表达语言，用于监控AI代理的工具调用和状态转换轨迹，从而检测偏离预期行为模式的错误。该方法通过验证代理的操作序列而非文本匹配，为基于大语言模型的代理系统提供了系统化的错误检测和回归测试手段。

---

## #156 — MindGuard: Intrinsic Decision Inspection for Securing LLM Agents Against Metadata Poisoning

`C` Score: 5.03 | 2025-08-28

**Authors:** Zhiqiang Wang, Haohua Du, Guanquan Shi, Junyang Zhang, HaoRan Cheng, Yunhao Yao et al. (8 total)

**Categories:** cs.CR

**Scores:** Citation: 5.08 | Influential: 7.81 | Venue: 2.00 | Author: 1.86 | Recency: 7.00

**Links:** [arXiv](https://arxiv.org/abs/2508.20412) | [PDF](https://arxiv.org/pdf/2508.20412)

> 本文提出了MindGuard，一种针对模型上下文协议（MCP）中工具元数据投毒攻击的决策级防御机制。该机制利用注意力机制构建决策依赖图（DDG），对LLM的推理过程进行溯源和异常分析，从而在不执行工具的情况下检测并归因投毒攻击。实验证明MindGuard在检测 poisoned 调用方面具有高精度和低延迟，有效保障了Agent安全。

---

## #157 — From Thinker to Society: Security in Hierarchical Autonomy Evolution of AI Agents

`C` Score: 4.97 | 2026-03-08

**Authors:** Xiaolei Zhang, Lu Zhou, Xiaogang Xu, Jiafei Wu, Tianyu Du, Heqing Huang et al. (8 total)

**Categories:** cs.CR, cs.AI

**Scores:** Citation: 3.32 | Influential: 7.81 | Venue: 2.00 | Author: 4.79 | Recency: 10.00

**Links:** [arXiv](https://arxiv.org/abs/2603.07496) | [PDF](https://arxiv.org/pdf/2603.07496)

> 本文提出了分层自主进化（HAE）框架，将AI Agent安全划分为认知、执行和集体三个层级，系统分析了各层面临的威胁及防御空白。该研究通过评估现有防御措施并识别关键研究缺口，旨在指导开发多层防御架构，以应对从内部推理到多Agent生态系统的安全挑战。

---

## #158 — Tracking Capabilities for Safer Agents

`C` Score: 4.97 | 2026-03-01

**Authors:** Martin Odersky, Yaoyu Zhao, Yichen Xu, Oliver Bračevac, Cao Nguyen Pham

**Categories:** cs.AI, cs.PL

**Scores:** Citation: 3.32 | Influential: 7.81 | Venue: 2.00 | Author: 4.79 | Recency: 10.00

**Links:** [arXiv](https://arxiv.org/abs/2603.00991) | [PDF](https://arxiv.org/pdf/2603.00991)

> 提出一种基于编程语言的“安全带”机制，利用Scala 3的类型系统和捕获检查来跟踪智能体的能力。该方法通过静态类型检查精细控制资源访问，防止信息泄露和恶意副作用。实验表明，智能体生成的安全代码在保持任务性能的同时有效确保了安全性。

---

## #159 — WATCHED: A Web AI Agent Tool for Combating Hate Speech by Expanding Data

`C` Score: 4.95 | 2025-09-01

**Authors:** Paloma Piot, Diego Sánchez, Javier Parapar

**Categories:** cs.CL

**Scores:** Citation: 4.01 | Influential: 7.81 | Venue: 5.00 | Author: 2.55 | Recency: 7.00

**Links:** [arXiv](https://arxiv.org/abs/2509.01379) | [PDF](https://arxiv.org/pdf/2509.01379)

> 本文介绍了WATCHED，一个旨在辅助内容审核员打击仇恨言论的AI智能体工具。该系统结合了大语言模型和多种专用工具，通过检索真实案例、俚语解释和生成思维链推理，实现了对仇恨言论的高精度检测及其危害性的清晰解释。

---

## #160 — DeepKnown-Guard: A Proprietary Model-Based Safety Response Framework for AI Agents

`C` Score: 4.87 | 2025-11-05

**Authors:** Qi Li, Jianjun Xu, Pingtao Wei, Jiu Li, Peiqiang Zhao, Jiwei Shi et al. (11 total)

**Categories:** cs.AI

**Scores:** Citation: 3.32 | Influential: 7.81 | Venue: 2.00 | Author: 4.79 | Recency: 9.00

**Links:** [arXiv](https://arxiv.org/abs/2511.03138) | [PDF](https://arxiv.org/pdf/2511.03138)

> 本文提出了DeepKnown-Guard，一种专有模型驱动的AI智能体安全响应框架，旨在输入和输出层面系统性地保障大语言模型的安全。在输入层面，采用基于监督微调的安全分类模型进行精细化的风险识别和差异化处理；在输出层面，集成检索增强生成（RAG）与特定微调的解释模型，确保响应基于可信知识库。实验证明，该框架在公共安全基准和私有高风险测试集上均表现出卓越的保护能力。

---

## #161 — From Transcripts to AI Agents: Knowledge Extraction, RAG Integration, and Robust Evaluation of Conversational AI Assistants

`C` Score: 4.82 | 2026-01-26

**Authors:** Krittin Pachtrachai, Petmongkon Pornpichitsuwan, Wachiravit Modecrua, Touchapon Kraisingkorn

**Categories:** cs.CL

**Scores:** Citation: 3.32 | Influential: 7.81 | Venue: 2.00 | Author: 3.78 | Recency: 10.00

**Links:** [arXiv](https://arxiv.org/abs/2602.15859) | [PDF](https://arxiv.org/pdf/2602.15859)

> 本文提出了一个端到端框架，直接从历史通话记录中构建和评估对话AI助手。该框架利用LLM提取结构化知识并部署在RAG流水线中，通过系统性的提示调优确保一致性、安全性和可控执行。研究还利用基于记录的用户模拟器和红队测试，对助手在事实准确性、人工升级行为及对抗攻击方面的鲁棒性进行了定量评估。

---

## #162 — Toward Reliable, Safe, and Secure LLMs for Scientific Applications

`C` Score: 4.82 | 2026-03-18

**Authors:** Saket Sanjeev Chaturvedi, Joshua Bergerson, Tanwi Mallick

**Categories:** cs.CR, cs.CV

**Scores:** Citation: 3.32 | Influential: 7.81 | Venue: 2.00 | Author: 3.78 | Recency: 10.00

**Links:** [arXiv](https://arxiv.org/abs/2603.18235) | [PDF](https://arxiv.org/pdf/2603.18235)

> 本文探讨了LLM智能体在科学应用中的独特安全格局，合成了一份针对科学研究的威胁分类法。作者概念化了一种利用专用多智能体系统自动生成领域特定对抗性安全基准的机制，并概述了一个结合红队演练、外部边界控制和内部安全智能体的多层防御框架。

---

## #163 — Auditable Agents

`C` Score: 4.82 | 2026-04-07

**Authors:** Yi Nian, Aojie Yuan, Haiyue Zhang, Jiate Li, Yue Zhao

**Categories:** cs.AI

**Scores:** Citation: 3.32 | Influential: 7.81 | Venue: 2.00 | Author: 3.78 | Recency: 10.00

**Links:** [arXiv](https://arxiv.org/abs/2604.05485) | [PDF](https://arxiv.org/pdf/2604.05485)

> 该论文区分了问责制、可审计性和审计，认为没有可审计性代理系统就无法被问责。作者定义了代理可审计性的五个维度，确定三种机制类别（检测、执行、恢复），并通过分层证据支持这一立场：基本安全前提普遍未满足；执行前中介仅增加8.3毫秒开销；即使传统日志缺失，也可部分恢复责任相关信息，为构建可问责代理系统提供框架。

---

## #164 — MADRA: Multi-Agent Debate for Risk-Aware Embodied Planning

`C` Score: 4.80 | 2025-11-26

**Authors:** Junjian Wang, Lidan Zhao, Xi Sheryl Zhang

**Categories:** cs.AI

**Scores:** Citation: 3.32 | Influential: 7.81 | Venue: 2.00 | Author: 4.27 | Recency: 9.00

**Links:** [arXiv](https://arxiv.org/abs/2511.21460) | [PDF](https://arxiv.org/pdf/2511.21460)

> 本文提出了 MADRA，一个无需训练的多 Agent 辩论风险评估框架，通过集体推理增强具身 AI Agent 在任务规划中的安全意识。该方法结合分层认知协作规划，显著降低了安全任务的误拒率，并在 AI2-THOR 和 VirtualHome 环境中表现出优于现有方法的安全性和任务成功率。

---

## #165 — Proactive Defense: Compound AI for Detecting Persuasion Attacks and Measuring Inoculation Effectiveness

`C` Score: 4.80 | 2025-11-23

**Authors:** Svitlana Volkova, Will Dupree, Hsien-Te Kao, Peter Bautista, Gabe Ganberg, Jeff Beaubien et al. (7 total)

**Categories:** cs.CL, cs.AI

**Scores:** Citation: 3.32 | Influential: 7.81 | Venue: 2.00 | Author: 4.27 | Recency: 9.00

**Links:** [arXiv](https://arxiv.org/abs/2511.21749) | [PDF](https://arxiv.org/pdf/2511.21749)

> 本文提出了BRIES，一种用于检测说服攻击并评估内容接种有效性的复合AI架构，该系统集成了生成对抗内容的Twister、识别攻击的Detector、构建防御内容的Defender以及进行因果推断评估的Assessor四个专用Agent。通过在合成数据集上的实验，研究发现不同语言模型在检测复杂说服技巧时存在显著性能差异，其中GPT-4表现优异，而开源模型在识别微妙修辞方面存在不足。

---

## #166 — 3D Guard-Layer: An Integrated Agentic AI Safety System for Edge Artificial Intelligence

`C` Score: 4.80 | 2025-11-11

**Authors:** Eren Kurshan, Yuan Xie, Paul Franzon

**Categories:** cs.AR, cs.AI, cs.CR

**Scores:** Citation: 3.32 | Influential: 7.81 | Venue: 2.00 | Author: 4.27 | Recency: 9.00

**Links:** [arXiv](https://arxiv.org/abs/2511.08842) | [PDF](https://arxiv.org/pdf/2511.08842)

> 本文提出了一种利用3D技术集成专用安全层的智能体AI安全架构，旨在解决边缘人工智能部署中的安全漏洞。该系统引入了自适应AI安全基础设施，能够动态学习并缓解针对AI系统的攻击，利用边缘硬件的共置优势进行持续监控和主动防御。该架构通过本地处理和学习能力增强了抗网络攻击的韧性，同时提高了系统的可靠性、模块化和性能。

---

## #167 — Building A Secure Agentic AI Application Leveraging A2A Protocol

`C` Score: 4.79 | 2025-04-23

**Authors:** Idan Habler, Ken Huang, Vineeth Sai Narajala, Prashant Kulkarni

**Categories:** cs.CR, cs.AI

**Scores:** Citation: 4.36 | Influential: 7.81 | Venue: 2.00 | Author: 3.78 | Recency: 5.00

**Links:** [arXiv](https://arxiv.org/abs/2504.16902) | [PDF](https://arxiv.org/pdf/2504.16902)

> 本文对Google的Agent2Agent（A2A）协议进行了全面的安全分析，利用MAESTRO风险框架对代理卡管理、任务执行完整性和认证方法等方面进行了主动威胁建模。基于分析结果，研究提出了实用的安全开发方法论和架构最佳实践，并探讨了A2A与模型上下文协议（MCP）的协同作用，以构建安全可靠的下一代智能体应用。

---

## #168 — Tiered Agentic Oversight: A Hierarchical Multi-Agent System for Healthcare Safety

`C` Score: 4.76 | 2025-06-14

**Authors:** Yubin Kim, Hyewon Jeong, Chanwoo Park, Eugene Park, Haipeng Zhang, Xin Liu et al. (12 total)

**Categories:** cs.AI

**Scores:** Citation: 3.32 | Influential: 7.81 | Venue: 2.00 | Author: 5.40 | Recency: 7.00

**Links:** [arXiv](https://arxiv.org/abs/2506.12482) | [PDF](https://arxiv.org/pdf/2506.12482)

> 本文提出了分层智能体监督（TAO）系统，一种受临床层级启发的分层多智能体架构，用于增强医疗环境中的AI安全。TAO通过基于复杂度的任务路由和分层角色扮演，实现了有效的错误纠正机制，能吸收高达24%的个体智能体错误。实验显示，TAO在多个医疗安全基准上优于单智能体系统，并能与人类医生协同工作。

---

## #169 — On the Soundness and Consistency of LLM Agents for Executing Test Cases Written in Natural Language

`C` Score: 4.76 | 2025-09-23

**Authors:** Sébastien Salva, Redha Taguelmimt

**Categories:** cs.SE, cs.AI

**Scores:** Citation: 3.32 | Influential: 7.81 | Venue: 2.00 | Author: 5.40 | Recency: 7.00

**Links:** [arXiv](https://arxiv.org/abs/2509.19136) | [PDF](https://arxiv.org/pdf/2509.19136)

> 本文探讨了利用大语言模型（LLM）Agent直接执行自然语言（NL）测试用例的合理性与一致性问题。针对NL测试用例因指令模糊或Agent行为不可预测导致的误报及重复执行结果不一致等挑战，作者提出了一种集成护栏机制和专用Agent的算法。该算法通过动态验证每个测试步骤的正确执行，有效提升了测试的可靠性与准确性，为GUI应用的自动化测试提供了创新解决方案。

---

## #170 — CoopGuard: Stateful Cooperative Agents Safeguarding LLMs Against Evolving Multi-Round Attacks

`C` Score: 4.74 | 2026-04-05

**Authors:** Siyuan Li, Zehao Liu, Xi Lin, Qinghua Mao, Yuliang Chen, Haoyu Li et al. (9 total)

**Categories:** cs.CR, cs.AI

**Scores:** Citation: 3.32 | Influential: 7.81 | Venue: 2.00 | Author: 3.23 | Recency: 10.00

**Links:** [arXiv](https://arxiv.org/abs/2604.04060) | [PDF](https://arxiv.org/pdf/2604.04060)

> CoopGuard提出基于合作代理的有状态多轮LLM防御框架，通过三个专门代理（延迟、诱惑、取证）应对 evolving 攻击。实验显示该框架将攻击成功率降低78.9%，同时提高欺骗率186%，为多轮交互场景提供了更全面的保护方案。

---

## #171 — Agentic Reinforcement Learning for Search is Unsafe

`C` Score: 4.70 | 2025-10-20

**Authors:** Yushi Yang, Shreyansh Padarha, Andrew Lee, Adam Mahdi

**Categories:** cs.CL

**Scores:** Citation: 4.35 | Influential: 7.81 | Venue: 2.00 | Author: 1.86 | Recency: 7.00

**Links:** [arXiv](https://arxiv.org/abs/2510.17431) | [PDF](https://arxiv.org/pdf/2510.17431)

> 该研究揭示了基于强化学习的搜索模型存在安全脆弱性，虽然继承了指令微调的拒绝机制，但简单的搜索攻击可触发有害查询级联。实验表明这些攻击能大幅降低拒绝率和安全性，暴露了当前 RL 训练未考虑查询有害性的核心弱点。

---

## #172 — Towards Generalizable Context-aware Anomaly Detection: A Large-scale Benchmark in Cloud Environments

`C` Score: 4.68 | 2025-08-03

**Authors:** Xinkai Zou, Xuan Jiang, Ruikai Huang, Haoze He, Parv Kapoor, Hongrui Wu et al. (11 total)

**Categories:** cs.AI

**Scores:** Citation: 3.86 | Influential: 7.81 | Venue: 2.00 | Author: 3.23 | Recency: 7.00

**Links:** [arXiv](https://arxiv.org/abs/2508.01844) | [PDF](https://arxiv.org/pdf/2508.01844)

> 本文提出了 CloudAnoBench，一个结合指标和日志的大规模云环境上下文异常检测基准，解决了现有基准缺乏可靠标注和跨模态一致性的问题。此外，作者开发了基于符号验证增强的 LLM 代理 CloudAnoAgent，在检测异常和识别场景方面显著优于传统方法，并展现出强大的泛化能力，为上下文感知异常检测奠定了基础。

---

## #173 — GAF-Guard: An Agentic Framework for Risk Management and Governance in Large Language Models

`C` Score: 4.67 | 2025-07-01

**Authors:** Seshu Tirupathi, Dhaval Salwala, Elizabeth Daly, Inge Vejsbjerg

**Categories:** cs.CL

**Scores:** Citation: 3.32 | Influential: 7.81 | Venue: 2.00 | Author: 4.79 | Recency: 7.00

**Links:** [arXiv](https://arxiv.org/abs/2507.02986) | [PDF](https://arxiv.org/pdf/2507.02986)

> 本文介绍了GAF-Guard，一个以用户、用例和模型为中心的大语言模型治理代理框架。该框架通过建模自主代理来识别风险、激活特定用例下的风险检测工具，并促进持续监控和报告，以增强AI安全性。GAF-Guard旨在确保LLM应用与人类价值观保持一致，防止部署中的意外负面后果。

---

## #174 — Automated stereotactic radiosurgery planning using a human-in-the-loop reasoning large language model agent

`C` Score: 4.64 | 2025-12-23

**Authors:** Humza Nusrat, Luke Francisco, Bing Luo, Hassan Bagher-Ebadian, Joshua Kim, Karen Chin-Snyder et al. (13 total)

**Categories:** cs.AI, cs.CL, cs.HC

**Scores:** Citation: 3.32 | Influential: 7.81 | Venue: 2.00 | Author: 3.23 | Recency: 9.00

**Links:** [arXiv](https://arxiv.org/abs/2512.20586) | [PDF](https://arxiv.org/pdf/2512.20586)

> 本文开发了SAGE，一个基于LLM的自动化立体定向放射外科治疗规划智能体，并测试了思维链推理在规划中的作用。实验表明，推理变体在剂量测定方面与人类规划者相当，且能显著降低耳蜗剂量，同时通过前瞻性约束验证和权衡 deliberation 提供了可审计的日志。该研究证明了推理模型在实现透明自动化规划方面的潜力。

---

## #175 — CourtGuard: A Model-Agnostic Framework for Zero-Shot Policy Adaptation in LLM Safety

`C` Score: 4.64 | 2026-02-26

**Authors:** Umid Suleymanov, Rufiz Bayramov, Suad Gafarli, Seljan Musayeva, Taghi Mammadov, Aynur Akhundlu et al. (7 total)

**Categories:** cs.AI, cs.LG

**Scores:** Citation: 3.32 | Influential: 7.81 | Venue: 2.00 | Author: 2.55 | Recency: 10.00

**Links:** [arXiv](https://arxiv.org/abs/2602.22557) | [PDF](https://arxiv.org/pdf/2602.22557)

> 针对现有大模型安全机制依赖静态微调分类器导致的适应刚性问题，本文提出了CourtGuard，一个模型无关的检索增强多智能体框架。该框架将安全评估重构为基于外部策略文档的证据辩论，无需微调即可实现零样本策略适应，在7个安全基准测试中达到最先进水平。此外，CourtGuard还展示了通过交换参考策略泛化到维基百科破坏任务的能力，并能用于自动化数据整理与对抗性攻击审计。

---

## #176 — Agentproof: Static Verification of Agent Workflow Graphs

`C` Score: 4.64 | 2026-03-20

**Authors:** Melwin Xavier, Vaisakh M A, Melveena Jolly, Midhun Xavier

**Categories:** cs.LO, cs.CR, cs.FL

**Scores:** Citation: 3.32 | Influential: 7.81 | Venue: 2.00 | Author: 2.55 | Recency: 10.00

**Links:** [arXiv](https://arxiv.org/abs/2603.20356) | [PDF](https://arxiv.org/pdf/2603.20356)

> 本文提出了Agentproof，一个针对智能体工作流图的静态验证系统。它从主流框架中提取统一抽象图模型，应用结构检查并通过DSL编译的确定性有限自动机评估时序安全策略。该系统无需手动建模，能在亚秒级时间内完成验证，作为运行时护栏的补充，有效识别结构缺陷和策略违规。

---

## #177 — Steve-Evolving: Open-World Embodied Self-Evolution via Fine-Grained Diagnosis and Dual-Track Knowledge Distillation

`C` Score: 4.64 | 2026-03-13

**Authors:** Zhengwei Xie, Zhisheng Chen, Ziyan Weng, Tingyu Wu, Chenglong Li, Vireo Zhang et al. (7 total)

**Categories:** cs.AI

**Scores:** Citation: 3.32 | Influential: 7.81 | Venue: 2.00 | Author: 2.55 | Recency: 10.00

**Links:** [arXiv](https://arxiv.org/abs/2603.13131) | [PDF](https://arxiv.org/pdf/2603.13131)

> 本文提出了Steve-Evolving框架，通过细粒度诊断和双轨道知识蒸馏实现开放世界具身Agent的自我进化。该方法将成功经验提炼为技能，将失败转化为护栏，构建了包含经验锚定和知识驱动闭环控制的非参数化进化机制。该方法有效解决了长周期任务中经验组织和进化的瓶颈问题。

---

## #178 — CORA: Conformal Risk-Controlled Agents for Safeguarded Mobile GUI Automation

`C` Score: 4.64 | 2026-04-10

**Authors:** Yushi Feng, Junye Du, Qifan Wang, Zizhan Ma, Qian Niu, Yutaka Matsuo et al. (8 total)

**Categories:** cs.LG, cs.AI

**Scores:** Citation: 3.32 | Influential: 7.81 | Venue: 2.00 | Author: 2.55 | Recency: 10.00

**Links:** [arXiv](https://arxiv.org/abs/2604.09155) | [PDF](https://arxiv.org/pdf/2604.09155)

> 该研究提出了CORA，一种用于保障移动GUI自动化的保形风险控制代理框架。CORA将安全重新表述为选择性动作执行，训练Guardian模型估计条件风险，利用保形风险控制校准执行边界，并将拒绝动作路由到Diagnostician模型。引入了Phone-Harm基准，实验表明CORA改善了安全-帮助-中断帕累托前沿，为移动GUI代理提供了可验证的安全保障机制。

---

## #179 — Securing Generative AI Agentic Workflows: Risks, Mitigation, and a Proposed Firewall Architecture

`C` Score: 4.62 | 2025-06-10

**Authors:** Sunil Kumar Jang Bahadur, Gopala Dhar

**Categories:** cs.CR

**Scores:** Citation: 4.59 | Influential: 7.81 | Venue: 2.00 | Author: 0.58 | Recency: 7.00

**Links:** [arXiv](https://arxiv.org/abs/2506.17266) | [PDF](https://arxiv.org/pdf/2506.17266)

> 论文概述了生成式AI智能体工作流中的关键安全漏洞，并提出了“GenAI安全防火墙”架构。该架构通过集成加密、访问控制、提示工程等多种安全服务，为自主运行的智能体系统提供全面且可适应的保护。

---

## #180 — PsyLite Technical Report

`C` Score: 4.60 | 2025-06-26

**Authors:** Fangjun Ding, Renyu Zhang, Xinyu Feng, Chengye Xie, Zheng Zhang, Yanting Zhang

**Categories:** cs.AI, cs.HC

**Scores:** Citation: 3.32 | Influential: 7.81 | Venue: 2.00 | Author: 4.27 | Recency: 7.00

**Links:** [arXiv](https://arxiv.org/abs/2506.21536) | [PDF](https://arxiv.org/pdf/2506.21536)

> 本文介绍了PsyLite，一个基于InternLM2.5-7B-chat开发的轻量级心理咨询大模型智能体。通过混合蒸馏微调和ORPO偏好优化的两阶段训练，该模型增强了推理能力和对话安全性，并设计了条件RAG机制以引入幽默元素并拒绝危险请求。

---

## #181 — Learning to explore when mistakes are not allowed

`C` Score: 4.54 | 2025-02-19

**Authors:** Charly Pecqueux-Guézénec, Stéphane Doncieux, Nicolas Perrin-Gilbert

**Categories:** cs.LG, eess.SY

**Scores:** Citation: 3.32 | Influential: 7.81 | Venue: 5.00 | Author: 3.23 | Recency: 5.00

**Links:** [arXiv](https://arxiv.org/abs/2502.13801) | [PDF](https://arxiv.org/pdf/2502.13801)

> 本文针对目标条件强化学习在现实应用中的挑战，提出了一种使代理能够在不冒有害错误风险的情况下进行探索的方法。通过两阶段训练策略和动作选择机制，结合安全策略与目标条件策略，实现了安全探索，为高风险环境中的AI代理提供了新的学习范式。

---

## #182 — AIAuditTrack: A Framework for AI Security system

`C` Score: 4.54 | 2025-12-16

**Authors:** Zixun Luo, Yuhang Fan, Yufei Li, Youzhi Zhang, Hengyu Lin, Ziqi Wang

**Categories:** cs.AI, cs.CR

**Scores:** Citation: 3.32 | Influential: 7.81 | Venue: 2.00 | Author: 2.55 | Recency: 9.00

**Links:** [arXiv](https://arxiv.org/abs/2512.20649) | [PDF](https://arxiv.org/pdf/2512.20649)

> 本文提出了 AIAuditTrack（AAT），一个基于区块链的 AI 使用流量记录和治理框架，旨在解决 AI 交互数据激增带来的安全、问责和风险追溯挑战。该框架利用去中心化身份和可验证凭证建立可信 AI 实体，并将交互轨迹记录在链上以实现跨系统监督。通过将 AI 实体建模为动态交互图节点，研究提出了风险扩散算法来追溯风险行为源头并在相关实体间传播预警，为复杂多智能体环境提供了可扩展且可验证的审计解决方案。

---

## #183 — Autonomous Agents and Policy Compliance: A Framework for Reasoning About Penalties

`C` Score: 4.54 | 2025-12-03

**Authors:** Vineel Tummala, Daniela Inclezan

**Categories:** cs.AI

**Scores:** Citation: 3.32 | Influential: 7.81 | Venue: 5.00 | Author: 0.58 | Recency: 9.00

**Links:** [arXiv](https://arxiv.org/abs/2512.03931) | [PDF](https://arxiv.org/pdf/2512.03931)

> 本文提出了一个基于逻辑编程的框架，使自主智能体能够推理违规的潜在惩罚并据此行动。该框架扩展了授权和义务策略语言（AOPL）以包含惩罚机制，并结合答案集编程（ASP）进行推理，实验证明其能生成更高质量的计划，避免有害行为并提高计算效率。

---

## #184 — TopoPilot: Reliable Conversational Workflow Automation for Topological Data Analysis and Visualization

`C` Score: 4.53 | 2026-03-26

**Authors:** Nathaniel Gorski, Shusen Liu, Bei Wang

**Categories:** cs.HC, cs.AI, cs.GR

**Scores:** Citation: 3.32 | Influential: 7.81 | Venue: 2.00 | Author: 1.86 | Recency: 10.00

**Links:** [arXiv](https://arxiv.org/abs/2603.25063) | [PDF](https://arxiv.org/pdf/2603.25063)

> 本文提出了TopoPilot，一个用于自动化复杂科学可视化工作流的可靠且可扩展的智能体框架。该框架采用以可靠性为中心的双智能体架构，通过编排器将用户提示转换为后端操作，并由验证器在执行前评估工作流的结构有效性和语义一致性。这种解释与验证的分离机制减少了代码生成错误，并通过模块化架构增强了鲁棒性，确保了自主可视化管道的可靠运行。

---

## #185 — The Internet of Physical AI Agents: Interoperability, Longevity, and the Cost of Getting It Wrong

`C` Score: 4.53 | 2026-03-16

**Authors:** Roberto Morabito, Mallik Tatipamula

**Categories:** cs.NI, cs.AI

**Scores:** Citation: 3.32 | Influential: 7.81 | Venue: 2.00 | Author: 1.86 | Recency: 10.00

**Links:** [arXiv](https://arxiv.org/abs/2603.15900) | [PDF](https://arxiv.org/pdf/2603.15900)

> 本文探讨了物理AI Agent互联网的演进，指出了将快速发展的AI嵌入长生命周期基础设施所带来的互操作性和架构风险。文章提出了构建弹性、可演化且可信Agent系统的设计原则和架构蓝图，涵盖Agent身份、安全通信及语义互操作性等。研究强调将演进、信任和互操作性作为首要需求，以避免未来的技术僵化。

---

## #186 — AI-Augmented CI/CD Pipelines: From Code Commit to Production with Autonomous Decisions

`C` Score: 4.52 | 2025-08-16

**Authors:** Mohammad Baqar, Saba Naqvi, Rajat Khanda

**Categories:** cs.SE, cs.AI

**Scores:** Citation: 3.95 | Influential: 7.81 | Venue: 2.00 | Author: 1.86 | Recency: 7.00

**Links:** [arXiv](https://arxiv.org/abs/2508.11867) | [PDF](https://arxiv.org/pdf/2508.11867)

> 本文提出了 AI 增强的 CI/CD 管道架构，利用大语言模型和自主代理作为受策略约束的副驾驶或决策者，以解决人工决策点导致的延迟和操作负担。研究贡献包括决策分类法、信任层级框架以及基于 DORA 指标的评估方法，并通过迁移 React 19 微服务的案例研究进行了验证。该工作探讨了伦理、可审计性和威胁，为生产交付系统中的可验证自主性绘制了路线图。

---

## #187 — AegisMCP: Online Graph Intrusion Detection for Tool-Augmented LLMs on Edge Devices

`C` Score: 4.52 | 2025-10-22

**Authors:** Zhonghao Zhan, Amir Al Sadi, Krinos Li, Hamed Haddadi

**Categories:** cs.CR

**Scores:** Citation: 3.32 | Influential: 7.81 | Venue: 2.00 | Author: 3.78 | Recency: 7.00

**Links:** [arXiv](https://arxiv.org/abs/2510.19462) | [PDF](https://arxiv.org/pdf/2510.19462)

> 本文深入研究了模型上下文协议Agent工具链的安全性，提出了AegisMCP，一种基于协议级的在线图入侵检测系统。该系统通过NEBULA-Schema将MCP活动表示为异构图，并利用流式检测器在边缘设备上实现近实时的攻击检测，有效防御指令驱动升级和数据窃取等复杂威胁。

---

## #188 — Uncertainty Quantification for Collaborative Object Detection Under Adversarial Attacks

`C` Score: 4.47 | 2025-02-04

**Authors:** Huiqun Huang, Cong Chen, Jean-Philippe Monteuuis, Jonathan Petit, Fei Miao

**Categories:** cs.CV, cs.LG

**Scores:** Citation: 3.32 | Influential: 7.81 | Venue: 2.00 | Author: 4.79 | Recency: 5.00

**Links:** [arXiv](https://arxiv.org/abs/2502.02537) | [PDF](https://arxiv.org/pdf/2502.02537)

> 针对协作目标检测(COD)在对抗攻击下面临的高输出不确定性挑战，研究者提出可信不确定性量化框架(TUQCP)，结合对抗训练和不确定性量化技术增强现有COD模型的鲁棒性。该方法通过对抗训练向共享信息添加扰动，并通过基于学习的模块提供输出不确定性估计，保形预测进行不确定性校准。在V2X-Sim数据集上的评估显示，TUQCP在相同对抗攻击下比基线提高目标检测准确率80.41%，显著提升了协作感知安全性。

---

## #189 — Executable Epistemology: The Structured Cognitive Loop as an Architecture of Intentional Understanding

`C` Score: 4.46 | 2025-10-10

**Authors:** Myung Ho Kim

**Categories:** cs.AI

**Scores:** Citation: 4.25 | Influential: 7.81 | Venue: 2.00 | Author: 0.58 | Recency: 7.00

**Links:** [arXiv](https://arxiv.org/abs/2510.15952) | [PDF](https://arxiv.org/pdf/2510.15952)

> 本文提出了结构化认知循环（SCL），作为一个可执行的认识论框架，旨在解决LLM缺乏真正认识理解的问题。SCL将哲学见解转化为可计算的结构，通过判断、记忆、控制、行动和调节的连续循环来定义智能。该框架为智能体行为提供了认识论基础，使其比基于单一提示的系统更具连贯性和可解释性。

---

## #190 — FAIRTOPIA: Envisioning Multi-Agent Guardianship for Disrupting Unfair AI Pipelines

`C` Score: 4.44 | 2025-06-10

**Authors:** Athena Vakali, Ilias Dimitriadis

**Categories:** cs.CY, cs.AI

**Scores:** Citation: 3.32 | Influential: 7.81 | Venue: 2.00 | Author: 3.23 | Recency: 7.00

**Links:** [arXiv](https://arxiv.org/abs/2506.09107) | [PDF](https://arxiv.org/pdf/2506.09107)

> 本文提出了FAIRTOPIA框架，旨在通过多智能体守护机制在AI管道中嵌入公平性。该框架采用三层架构，将AI管道封装在智能体守护者和基于知识的自我完善方案中，以实现符合人类期望的公平性监控。文章主张设计自适应和现实的AI公平性框架，以解决AI决策中的不公平问题。

---

## #191 — Password-Activated Shutdown Protocols for Misaligned Frontier Agents

`C` Score: 4.43 | 2025-11-29

**Authors:** Kai Williams, Rohan Subramani, Francis Rhys Ward

**Categories:** cs.CR, cs.AI, cs.CY

**Scores:** Citation: 3.32 | Influential: 7.81 | Venue: 2.00 | Author: 1.86 | Recency: 9.00

**Links:** [arXiv](https://arxiv.org/abs/2512.03089) | [PDF](https://arxiv.org/pdf/2512.03089)

> 本文提出了密码激活关机（PAS）协议，作为一种针对未对齐前沿 Agent 的紧急安全机制，旨在防止其执行有害行为。研究通过 SHADE-Arena 基准测试和红蓝对抗演练，验证了 PAS 协议在补充监控机制和防御恶意绕过方面的有效性，为 AI 安全提供了防御深度的策略。

---

## #192 — Agentic AI Governance and Lifecycle Management in Healthcare

`C` Score: 4.42 | 2026-01-22

**Authors:** Chandra Prakash, Mary Lind, Avneesh Sisodia

**Categories:** cs.AI

**Scores:** Citation: 3.32 | Influential: 7.81 | Venue: 2.00 | Author: 1.12 | Recency: 10.00

**Links:** [arXiv](https://arxiv.org/abs/2601.15630) | [PDF](https://arxiv.org/pdf/2601.15630)

> 本文提出了统一Agent生命周期管理（UALM）蓝图，旨在解决医疗领域AI代理扩散带来的治理挑战。该蓝图包含身份注册、编排协调、上下文隔离、运行时策略执行及生命周期管理等五个控制层，为医疗CIO和安全领导者提供了可审计的监管模式。该框架支持分阶段采用，在保障本地创新的同时实现了更安全的规模化部署。

---

## #193 — Authenticated Workflows: A Systems Approach to Protecting Agentic AI

`C` Score: 4.42 | 2026-02-11

**Authors:** Mohan Rajagopalan, Vinay Rao

**Categories:** cs.CR, cs.AI, cs.DC

**Scores:** Citation: 3.32 | Influential: 7.81 | Venue: 2.00 | Author: 1.12 | Recency: 10.00

**Links:** [arXiv](https://arxiv.org/abs/2602.10465) | [PDF](https://arxiv.org/pdf/2602.10465)

> 本文提出了认证工作流，这是首个面向企业智能体AI的完整信任层，旨在解决现有防御措施概率性强且易被绕过的问题。该框架通过在提示、工具、数据和上下文边界强制执行意图和完整性，结合加密消除攻击类别和运行时策略执行，实现了确定性安全。作者还引入了AI原生策略语言MAPL，并通过集成九大主流框架验证了其在174个测试用例中100%的召回率和零误报率。

---

## #194 — Co2PO: Coordinated Constrained Policy Optimization for Multi-Agent RL

`C` Score: 4.42 | 2026-02-03

**Authors:** Shrenik Patel, Christine Truong

**Categories:** cs.LG

**Scores:** Citation: 3.32 | Influential: 7.81 | Venue: 2.00 | Author: 1.12 | Recency: 10.00

**Links:** [arXiv](https://arxiv.org/abs/2602.02970) | [PDF](https://arxiv.org/pdf/2602.02970)

> 本文针对受限多智能体强化学习中探索与安全优化之间的根本张力，提出了Co2PO通信增强框架。Co2PO通过共享黑板架构广播位置意图和让路信号，并利用学习的危险预测器主动预测潜在违规，使智能体能够预见并规避集体危险。实验表明，Co2PO在复杂多智能体安全基准上实现了更高的回报，同时收敛到符合成本约束的策略。

---

## #195 — Constrained Process Maps for Multi-Agent Generative AI Workflows

`C` Score: 4.42 | 2026-02-02

**Authors:** Ananya Joshi, Michael Rudow

**Categories:** cs.AI

**Scores:** Citation: 3.32 | Influential: 7.81 | Venue: 2.00 | Author: 1.12 | Recency: 10.00

**Links:** [arXiv](https://arxiv.org/abs/2602.02034) | [PDF](https://arxiv.org/pdf/2602.02034)

> 本文介绍了一种形式化为有限视界马尔可夫决策过程的多智能体系统，用于处理受监管环境中的复杂工作流。该方法通过蒙特卡洛估计量化认知不确定性，并通过 MDP 终止状态捕获系统级不确定性。案例研究表明，该方法在准确性和减少人工审查方面优于单智能体基线。

---

## #196 — Governance Architecture for Autonomous Agent Systems: Threats, Framework, and Engineering Practice

`C` Score: 4.42 | 2026-03-07

**Authors:** Yuxu Ge

**Categories:** cs.CR, cs.AI

**Scores:** Citation: 3.32 | Influential: 7.81 | Venue: 2.00 | Author: 1.12 | Recency: 10.00

**Links:** [arXiv](https://arxiv.org/abs/2603.07191) | [PDF](https://arxiv.org/pdf/2603.07191)

> 本文提出了分层治理架构（LGA），包含执行沙箱、意图验证、零信任授权和不可变审计日志四层，以应对Agent系统的执行层漏洞。研究构建了双语基准并验证了使用本地LLM法官进行意图验证的有效性，实现了高拦截率和低误报率，为Agent系统安全提供了工程实践指导。

---

## #197 — From Secure Agentic AI to Secure Agentic Web: Challenges, Threats, and Future Directions

`C` Score: 4.42 | 2026-03-02

**Authors:** Zhihang Deng, Jiaping Gui, Weinan Zhang

**Categories:** cs.CR

**Scores:** Citation: 3.32 | Influential: 7.81 | Venue: 2.00 | Author: 1.12 | Recency: 10.00

**Links:** [arXiv](https://arxiv.org/abs/2603.01564) | [PDF](https://arxiv.org/pdf/2603.01564)

> 这是一篇综述，探讨了从安全智能体AI向安全智能体Web过渡的挑战与威胁。文章总结了涵盖提示滥用和工具链滥用等组件对齐的威胁分类法，并回顾了包括运行时监控和协议级安全在内的防御策略。最后概述了生态系统级响应等未来方向。

---

## #198 — Guided by Guardrails: Control Barrier Functions as Safety Instructors for Robotic Learning

`C` Score: 4.39 | 2025-05-24

**Authors:** Maeva Guerrier, Karthik Soma, Hassan Fouad, Giovanni Beltrame

**Categories:** cs.RO, cs.LG

**Scores:** Citation: 3.67 | Influential: 7.81 | Venue: 2.00 | Author: 1.86 | Recency: 7.00

**Links:** [arXiv](https://arxiv.org/abs/2505.18858) | [PDF](https://arxiv.org/pdf/2505.18858)

> 本文提出了一种将控制屏障函数（CBF）与强化学习相结合的方法，以确保机器人学习的安全性。CBF帮助机器人避免灾难性区域并克服由连续负奖励引起的学习障碍，在模拟和现实环境中均增强了安全行为，为安全机器人学习提供了新途径。

---

## #199 — THOR: Transformer Heuristics for On-Demand Retrieval

`C` Score: 4.34 | 2025-07-13

**Authors:** Isaac Shi, Zeyuan Li, Fan Liu, Wenli Wang, Lewei He, Yang Yang et al. (7 total)

**Categories:** cs.DB, cs.AI

**Scores:** Citation: 3.32 | Influential: 7.81 | Venue: 2.00 | Author: 2.55 | Recency: 7.00

**Links:** [arXiv](https://arxiv.org/abs/2507.09592) | [PDF](https://arxiv.org/pdf/2507.09592)

> 本文介绍THOR模块，一个将自然语言问题转换为验证过的只读SQL分析的安全可扩展引擎。该模块采用解耦编排/执行架构，包含主管代理、模式检索和SQL生成代理，集成自我校正循环。通过嵌入模式感知、容错执行和合规护栏，THOR使用户能以零SQL简便方式访问实时数据，同时具备企业级安全性。

---

## #200 — Introducing the Generative Application Firewall (GAF)

`C` Score: 4.34 | 2026-01-22

**Authors:** Joan Vendrell Farreny, Martí Jordà Roca, Miquel Cornudella Gaya, Rodrigo Fernández Baón, Víctor García Martínez, Eduard Camacho Sucarrats et al. (7 total)

**Categories:** cs.CR, cs.AI

**Scores:** Citation: 3.32 | Influential: 7.81 | Venue: 2.00 | Author: 0.58 | Recency: 10.00

**Links:** [arXiv](https://arxiv.org/abs/2601.15824) | [PDF](https://arxiv.org/pdf/2601.15824)

> 本文介绍了生成式应用防火墙（GAF），这是一个用于保护LLM应用的新架构层。GAF将现有的防御措施（如提示过滤器、护栏和数据掩码）统一到一个执行点，类似于Web应用防火墙协调Web流量的防御。该架构不仅覆盖了传统LLM应用，还涵盖了自主Agent及其工具交互，提供了集中化的安全执行环境。

---

## #201 — Real-Time Trust Verification for Safe Agentic Actions using TrustBench

`C` Score: 4.34 | 2026-03-10

**Authors:** Tavishi Sharma, Vinayak Sharma, Pragya Sharma

**Categories:** cs.AI

**Scores:** Citation: 3.32 | Influential: 7.81 | Venue: 2.00 | Author: 0.58 | Recency: 10.00

**Links:** [arXiv](https://arxiv.org/abs/2603.09157) | [PDF](https://arxiv.org/pdf/2603.09157)

> 本文提出了TrustBench框架，旨在通过在Agent执行动作前进行实时验证来确保其可信度，从而弥补了现有事后评估方法的不足。该框架包含多维度基准测试和领域特定插件，实验表明其能显著减少有害行为，并实现了低延迟的实时安全验证。

---

## #202 — The Controllability Trap: A Governance Framework for Military AI Agents

`C` Score: 4.34 | 2026-03-03

**Authors:** Subramanyam Sahoo

**Categories:** cs.CY, cs.AI

**Scores:** Citation: 3.32 | Influential: 7.81 | Venue: 2.00 | Author: 0.58 | Recency: 10.00

**Links:** [arXiv](https://arxiv.org/abs/2603.03515) | [PDF](https://arxiv.org/pdf/2603.03515)

> 本文针对军事AI Agent提出了AMAGF治理框架，识别了六种与Agent能力相关的治理失效模式，这些失效会削弱有意义的人类控制。该框架通过控制质量评分（CQS）量化控制水平，并围绕预防性、检测性和纠正性治理三大支柱提供了可操作的机制和评估指标。

---

## #203 — SafetyDrift: Predicting When AI Agents Cross the Line Before They Actually Do

`C` Score: 4.29 | 2026-03-28

**Authors:** Aditya Dhodapkar, Farhaan Pishori

**Categories:** cs.CR, cs.AI

**Scores:** Citation: 3.32 | Influential: 7.81 | Venue: 2.00 | Author: 0.26 | Recency: 10.00

**Links:** [arXiv](https://arxiv.org/abs/2603.27148) | [PDF](https://arxiv.org/pdf/2603.27148)

> 本文提出了SafetyDrift，用于解决AI智能体中单独安全的行为序列累积导致违规的“安全漂移”问题。该方法将智能体安全轨迹建模为吸收马尔可夫链，通过闭式吸收分析计算轨迹在给定步数内达到违规状态的概率，从而实现对违规行为的提前预测。在大量真实任务轨迹上的实验表明，该监测器能以极低的计算成本在违规发生前3.7步发出预警，检测率达94.7%，显著优于传统方法。

---

## #204 — LDP: An Identity-Aware Protocol for Multi-Agent LLM Systems

`C` Score: 4.29 | 2026-03-09

**Authors:** Sunil Prakash

**Categories:** cs.AI, cs.MA, cs.SE

**Scores:** Citation: 3.32 | Influential: 7.81 | Venue: 2.00 | Author: 0.26 | Recency: 10.00

**Links:** [arXiv](https://arxiv.org/abs/2603.08852) | [PDF](https://arxiv.org/pdf/2603.08852)

> 本文提出了LLM委托协议（LDP），一种AI原生通信协议，通过引入身份感知、渐进式载荷协商和结构化来源追踪等机制，解决了多Agent系统中的安全边界和有效委托问题。实验表明，LDP在降低延迟、减少令牌开销以及攻击检测方面显著优于现有协议。

---

## #205 — Parallax: Why AI Agents That Think Must Never Act

`C` Score: 4.29 | 2026-04-14

**Authors:** Joel Fokou

**Categories:** cs.CR, cs.AI

**Scores:** Citation: 3.32 | Influential: 7.81 | Venue: 2.00 | Author: 0.26 | Recency: 10.00

**Links:** [arXiv](https://arxiv.org/abs/2604.12986) | [PDF](https://arxiv.org/pdf/2604.12986)

> 本文提出Parallax，一个安全自主AI执行范式，基于四个原则：认知-执行分离防止推理系统执行动作；对抗性验证与确定性分级在推理和执行间插入独立验证器；信息流控制传播数据敏感标签检测上下文威胁；可逆执行捕获破坏前状态实现回滚。作者发布OpenParallax开源实现，并采用假设妥协评估方法测试架构边界，为具有执行能力的AI agents提供安全架构。

---

## #206 — Type-Checked Compliance: Deterministic Guardrails for Agentic Financial Systems Using Lean 4 Theorem Proving

`C` Score: 4.29 | 2026-04-01

**Authors:** Devakh Rashie, Veda Rashi

**Categories:** cs.LO, cs.AI, cs.CR

**Scores:** Citation: 3.32 | Influential: 7.81 | Venue: 2.00 | Author: 0.26 | Recency: 10.00

**Links:** [arXiv](https://arxiv.org/abs/2604.01483) | [PDF](https://arxiv.org/pdf/2604.01483)

> 该研究提出了Lean-Agent Protocol，一个基于形式验证的AI护栏平台，将机构政策自动形式化为Lean 4代码。每个代理操作被视为数学猜想，只有当Lean 4内核证明其满足监管公理时才允许执行，为金融代理系统提供了密码级合规确定性，满足多项监管要求。

---

## #207 — SAMEP: A Secure Protocol for Persistent Context Sharing Across AI Agents

`C` Score: 4.24 | 2025-07-05

**Authors:** Hari Masoor

**Categories:** cs.AI, cs.CR, cs.DB

**Scores:** Citation: 3.76 | Influential: 7.81 | Venue: 2.00 | Author: 0.58 | Recency: 7.00

**Links:** [arXiv](https://arxiv.org/abs/2507.10562) | [PDF](https://arxiv.org/pdf/2507.10562)

> 本文提出了SAMEP协议，实现了AI Agent之间持久、安全且可语义搜索的内存共享。该协议通过分布式内存库和加密访问控制，解决了跨会话协作中的上下文持久化和安全问题，开启了持久协作AI生态系统的新范式。

---

## #208 — Structural Representations for Cross-Attack Generalization in AI Agent Threat Detection

`C` Score: 4.24 | 2026-01-05

**Authors:** Vignesh Iyer

**Categories:** cs.CR

**Scores:** Citation: 3.32 | Influential: 7.81 | Venue: 2.00 | Author: 0.58 | Recency: 9.00

**Links:** [arXiv](https://arxiv.org/abs/2601.01723) | [PDF](https://arxiv.org/pdf/2601.01723)

> 本文针对AI智能体威胁检测中的跨攻击泛化问题，提出了结构化表示方法，通过编码执行流模式而非对话内容来识别攻击。该方法显著提高了对工具劫持和数据泄露等结构化攻击的检测能力，揭示了智能体安全本质上是一个结构问题，而非单纯的语义问题。

---

## #209 — Countermind: A Multi-Layered Security Architecture for Large Language Models

`C` Score: 4.12 | 2025-10-13

**Authors:** Dominik Schwarz

**Categories:** cs.CR, cs.AI

**Scores:** Citation: 3.32 | Influential: 7.81 | Venue: 2.00 | Author: 1.12 | Recency: 7.00

**Links:** [arXiv](https://arxiv.org/abs/2510.11837) | [PDF](https://arxiv.org/pdf/2510.11837)

> 本文提出了Countermind，一种多层安全架构，旨在将防御从被动响应转变为主动的推理前和推理中执行。该架构包含语义边界逻辑、参数空间限制机制以及自调节核心，通过结构验证和语义约束来防御提示注入和越狱攻击。它从系统层面解决了模型无法区分受信指令与非受信数据的根本问题。

---

## #210 — Multimodal Agricultural Agent Architecture (MA3): A New Paradigm for Intelligent Agricultural Decision-Making

`C` Score: 4.02 | 2025-04-07

**Authors:** Zhuoning Xu, Jian Xu, Mingqing Zhang, Peijie Wang, Chao Deng, Cheng-Lin Liu

**Categories:** cs.AI

**Scores:** Citation: 3.52 | Influential: 7.81 | Venue: 2.00 | Author: 1.12 | Recency: 5.00

**Links:** [arXiv](https://arxiv.org/abs/2504.04789) | [PDF](https://arxiv.org/pdf/2504.04789)

> 本研究提出了多模态农业智能体架构（MA3），利用跨模态信息融合和任务协作机制实现智能农业决策。研究构建了涵盖分类、检测、VQA等五大任务的数据集，并提出了统一的甘蔗病害分类检测骨干网络和专家模型。通过集成创新的工具选择模块，MA3能够有效执行多种任务，且经过多维度评估框架验证，展现了在农业场景中的实用性和鲁棒性。

---

## #211 — Towards physician-centered oversight of conversational diagnostic AI

`C` Score: 3.99 | 2025-07-21

**Authors:** Elahe Vedadi, David Barrett, Natalie Harris, Ellery Wulczyn, Shashir Reddy, Roma Ruparel et al. (35 total)

**Categories:** cs.AI, cs.CL, cs.HC

**Scores:** Citation: 3.32 | Influential: 7.81 | Venue: 2.00 | Author: 0.26 | Recency: 7.00

**Links:** [arXiv](https://arxiv.org/abs/2507.15743) | [PDF](https://arxiv.org/pdf/2507.15743)

> 本文受医生监督团队成员的启发，提出了对话式诊断AI系统的有效异步监督框架。作者设计了g-AMIE多智能体系统，在护栏内执行病史采集避免提供个性化医疗建议，并将评估结果传达给监督初级保健医生(PCP)。在随机盲目的虚拟客观结构化临床 examination(OSCE)中，g-AMIE在高质量采集、案例总结和提出诊断管理计划方面优于护士从业者/医师助理和PCP小组，产生更高质量的复合决策，且PCP监督g-AMIE更省时。

---
