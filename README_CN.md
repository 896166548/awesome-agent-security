# Agent 安全论文精选

> AI Agent 安全研究论文精选集——涵盖攻击对抗、防御对齐、安全测评与 Agent 安全架构。共 **1799 篇** arXiv 论文，按质量评分排序。

[English Version](README.md)

## 统计

| 指标 | 值 |
|------|-----|
| 论文总数 | 1799 |
| 日期范围 | 2024-09 ~ 2026-04 |
| A 级论文 | 178 |
| 评分范围 | 3.79 ~ 9.36（均值 5.97） |

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
| 月均引用 | 45% | 引用数按发表时间归一化 |
| 高影响力引用 | 20% | 高影响力引用数 |
| 发表会议质量 | 10% | 顶会=10，普通会议=5，预印本=2 |
| 作者质量 | 15% | 最高作者 h-index |
| 时效性 | 10% | ≤3月=10，≤6月=9，≤12月=7，>12月=5 |

质量等级：**A** = 前 10% | **B** = 前 30% | C = 其余

## Top 100 论文

| 排名 | 标题 | 作者 | 评分 | 等级 | 日期 | 分类 |
|-----:|------|------|-----:|------|------|------|
| 1 | [SafeArena: Evaluating the Safety of Autonomous Web Agents](https://arxiv.org/abs/2503.04957) | Ada Defne Tur, Nicholas Meade, Xing Han Lù 等 9 人 | 9.36 | **A** | 2025-03-06 | Eval |
| 2 | [AgentHarm: A Benchmark for Measuring Harmfulness of LLM Agents](https://arxiv.org/abs/2410.09024) | Maksym Andriushchenko, Alexandra Souly, Mateusz Dziemian 等 14 人 | 9.35 | **A** | 2024-10-11 | Eval |
| 3 | [STAIR: Improving Safety Alignment with Introspective Reasoning](https://arxiv.org/abs/2502.02384) | Yichi Zhang, Siyuan Zhang, Yao Huang 等 10 人 | 9.32 | **A** | 2025-02-04 | Defense |
| 4 | [MCPEval: Automatic MCP-based Deep Evaluation for AI Agent Models](https://arxiv.org/abs/2507.12806) | Zhiwei Liu, Jielin Qiu, Shiyu Wang 等 12 人 | 9.32 | **A** | 2025-07-17 | Eval |
| 5 | [The Hidden Risks of Large Reasoning Models: A Safety Assessment of R1](https://arxiv.org/abs/2502.12659) | Kaiwen Zhou, Chengzhi Liu, Xuandong Zhao 等 8 人 | 9.31 | **A** | 2025-02-18 | Eval |
| 6 | [AGrail: A Lifelong Agent Guardrail with Effective and Adaptive Safety Detection](https://arxiv.org/abs/2502.11448) | Weidi Luo, Shenghong Dai, Xiaogeng Liu 等 7 人 | 9.28 | **A** | 2025-02-17 | Defense |
| 7 | [Persistent Pre-Training Poisoning of LLMs](https://arxiv.org/abs/2410.13722) | Yiming Zhang, Javier Rando, Ivan Evtimov 等 8 人 | 9.24 | **A** | 2024-10-17 | Attacks |
| 8 | [Towards LLM Unlearning Resilient to Relearning Attacks: A Sharpness-Aware Minimization Perspective and Beyond](https://arxiv.org/abs/2502.05374) | Chongyu Fan, Jinghan Jia, Yihua Zhang 等 6 人 | 9.18 | **A** | 2025-02-07 | Defense |
| 9 | [IPIGuard: A Novel Tool Dependency Graph-Based Defense Against Indirect Prompt Injection in LLM Agents](https://arxiv.org/abs/2508.15310) | Hengyu An, Jinghuai Zhang, Tianyu Du 等 7 人 | 9.18 | **A** | 2025-08-21 | Arch |
| 10 | [Agent Security Bench (ASB): Formalizing and Benchmarking Attacks and Defenses in LLM-based Agents](https://arxiv.org/abs/2410.02644) | Hanrong Zhang, Jingyuan Huang, Kai Mei 等 8 人 | 9.11 | **A** | 2024-10-03 | Eval |
| 11 | [SafeKey: Amplifying Aha-Moment Insights for Safety Reasoning](https://arxiv.org/abs/2505.16186) | Kaiwen Zhou, Xuandong Zhao, Gaowen Liu 等 7 人 | 9.04 | **A** | 2025-05-22 | Defense |
| 12 | [Instructional Segment Embedding: Improving LLM Safety with Instruction Hierarchy](https://arxiv.org/abs/2410.09102) | Tong Wu, Shujian Zhang, Kaiqiang Song 等 10 人 | 9.04 | **A** | 2024-10-09 | Defense |
| 13 | [SPA-Bench: A Comprehensive Benchmark for SmartPhone Agent Evaluation](https://arxiv.org/abs/2410.15164) | Jingxuan Chen, Derek Yuen, Bin Xie 等 17 人 | 9.02 | **A** | 2024-10-19 | Other |
| 14 | [Reasoning-to-Defend: Safety-Aware Reasoning Can Defend Large Language Models from Jailbreaking](https://arxiv.org/abs/2502.12970) | Junda Zhu, Lingyong Yan, Shuaiqiang Wang 等 5 人 | 8.98 | **A** | 2025-02-18 | Defense |
| 15 | [Robust LLM safeguarding via refusal feature adversarial training](https://arxiv.org/abs/2409.20089) | Lei Yu, Virginie Do, Karen Hambardzumyan 等 4 人 | 8.98 | **A** | 2024-09-30 | Defense |
| 16 | [ShieldAgent: Shielding Agents via Verifiable Safety Policy Reasoning](https://arxiv.org/abs/2503.22738) | Zhaorun Chen, Mintong Kang, Bo Li | 8.97 | **A** | 2025-03-26 | Arch |
| 17 | [G-Designer: Architecting Multi-agent Communication Topologies via Graph Neural Networks](https://arxiv.org/abs/2410.11782) | Guibin Zhang, Yanwei Yue, Xiangguo Sun 等 9 人 | 8.97 | **A** | 2024-10-15 | Arch |
| 18 | [Improving LLM Safety Alignment with Dual-Objective Optimization](https://arxiv.org/abs/2503.03710) | Xuandong Zhao, Will Cai, Tianneng Shi 等 7 人 | 8.94 | **A** | 2025-03-05 | Defense |
| 19 | [JBShield: Defending Large Language Models from Jailbreak Attacks through Activated Concept Analysis and Manipulation](https://arxiv.org/abs/2502.07557) | Shenyi Zhang, Yuchen Zhai, Keyan Guo 等 10 人 | 8.92 | **A** | 2025-02-11 | Defense |
| 20 | [Reasoning-Augmented Conversation for Multi-Turn Jailbreak Attacks on Large Language Models](https://arxiv.org/abs/2502.11054) | Zonghao Ying, Deyue Zhang, Zonglei Jing 等 10 人 | 8.88 | **A** | 2025-02-16 | Attacks |
| 21 | [InfAlign: Inference-aware language model alignment](https://arxiv.org/abs/2412.19792) | Ananth Balashankar, Ziteng Sun, Jonathan Berant 等 12 人 | 8.85 | **A** | 2024-12-27 | Defense |
| 22 | [AdaSteer: Your Aligned LLM is Inherently an Adaptive Jailbreak Defender](https://arxiv.org/abs/2504.09466) | Weixiang Zhao, Jiahe Guo, Yulin Hu 等 11 人 | 8.84 | **A** | 2025-04-13 | Defense |
| 23 | [The Attacker Moves Second: Stronger Adaptive Attacks Bypass Defenses Against Llm Jailbreaks and Prompt Injections](https://arxiv.org/abs/2510.09023) | Milad Nasr, Nicholas Carlini, Chawin Sitawarin 等 14 人 | 8.83 | **A** | 2025-10-10 | Attacks |
| 24 | [AdvWave: Stealthy Adversarial Jailbreak Attack against Large Audio-Language Models](https://arxiv.org/abs/2412.08608) | Mintong Kang, Chejian Xu, Bo Li | 8.82 | **A** | 2024-12-11 | Attacks |
| 25 | [Cut the Crap: An Economical Communication Pipeline for LLM-based Multi-Agent Systems](https://arxiv.org/abs/2410.02506) | Guibin Zhang, Yanwei Yue, Zhixun Li 等 9 人 | 8.80 | **A** | 2024-10-03 | Arch |
| 26 | [How Do Large Language Monkeys Get Their Power (Laws)?](https://arxiv.org/abs/2502.17578) | Rylan Schaeffer, Joshua Kazdan, John Hughes 等 10 人 | 8.78 | **A** | 2025-02-24 | Other |
| 27 | [RedCode: Risky Code Execution and Generation Benchmark for Code Agents](https://arxiv.org/abs/2411.07781) | Chengquan Guo, Xun Liu, Chulin Xie 等 8 人 | 8.75 | **A** | 2024-11-12 | Eval |
| 28 | [Towards Low-Resource Harmful Meme Detection with LMM Agents](https://arxiv.org/abs/2411.05383) | Jianzhao Huang, Hongzhan Lin, Ziyan Liu 等 6 人 | 8.74 | **A** | 2024-11-08 | Arch |
| 29 | [Emoji Attack: Enhancing Jailbreak Attacks Against Judge LLM Detection](https://arxiv.org/abs/2411.01077) | Zhipeng Wei, Yuqi Liu, N. Benjamin Erichson | 8.70 | **A** | 2024-11-01 | Attacks |
| 30 | [OS-Harm: A Benchmark for Measuring Safety of Computer Use Agents](https://arxiv.org/abs/2506.14866) | Thomas Kuntz, Agatha Duzan, Hao Zhao 等 7 人 | 8.68 | **A** | 2025-06-17 | Eval |
| 31 | [Trustworthy AI-Driven Dynamic Hybrid RIS: Joint Optimization and Reward Poisoning-Resilient Control in Cognitive MISO Networks](https://arxiv.org/abs/2604.01238) | Deemah H. Tashman, Soumaya Cherkaoui | 8.68 | **A** | 2026-03-27 | Defense |
| 32 | [Policy Compiler for Secure Agentic Systems](https://arxiv.org/abs/2602.16708) | Nils Palumbo, Sarthak Choudhary, Jihye Choi 等 5 人 | 8.66 | **A** | 2026-02-18 | Arch |
| 33 | [HarmAug: Effective Data Augmentation for Knowledge Distillation of Safety Guard Models](https://arxiv.org/abs/2410.01524) | Seanie Lee, Haebin Seong, Dong Bok Lee 等 9 人 | 8.66 | **A** | 2024-10-02 | Defense |
| 34 | [Constitutional Classifiers: Defending against Universal Jailbreaks across Thousands of Hours of Red Teaming](https://arxiv.org/abs/2501.18837) | Mrinank Sharma, Meg Tong, Jesse Mu 等 43 人 | 8.65 | **A** | 2025-01-31 | Defense |
| 35 | [Multi-Agent Risks from Advanced AI](https://arxiv.org/abs/2502.14143) | Lewis Hammond, Alan Chan, Jesse Clifton 等 44 人 | 8.65 | **A** | 2025-02-19 | Arch |
| 36 | [A Mousetrap: Fooling Large Reasoning Models for Jailbreak with Chain of Iterative Chaos](https://arxiv.org/abs/2502.15806) | Yang Yao, Xuan Tong, Ruofan Wang 等 8 人 | 8.63 | **A** | 2025-02-19 | Attacks |
| 37 | [Thought Crime: Backdoors and Emergent Misalignment in Reasoning Models](https://arxiv.org/abs/2506.13206) | James Chua, Jan Betley, Mia Taylor 等 4 人 | 8.63 | **A** | 2025-06-16 | Attacks |
| 38 | [CVE-Bench: A Benchmark for AI Agents' Ability to Exploit Real-World Web Application Vulnerabilities](https://arxiv.org/abs/2503.17332) | Yuxuan Zhu, Antony Kellermann, Dylan Bowman 等 16 人 | 8.62 | **A** | 2025-03-21 | Eval |
| 39 | [G-Safeguard: A Topology-Guided Security Lens and Treatment on LLM-based Multi-agent Systems](https://arxiv.org/abs/2502.11127) | Shilong Wang, Guibin Zhang, Miao Yu 等 8 人 | 8.60 | **A** | 2025-02-16 | Arch |
| 40 | [Agentic AI Security: Threats, Defenses, Evaluation, and Open Challenges](https://arxiv.org/abs/2510.23883) | Anshuman Chhabra, Shrestha Datta, Shahriar Kabir Nahin 等 4 人 | 8.60 | **A** | 2025-10-27 | Other |
| 41 | [Securing the Model Context Protocol: Defending LLMs Against Tool Poisoning and Adversarial Attacks](https://arxiv.org/abs/2512.06556) | Saeid Jamshidi, Kawser Wazed Nafi, Arghavan Moradi Dakhel 等 6 人 | 8.60 | **A** | 2025-12-06 | Arch |
| 42 | [When Machine Unlearning Meets Retrieval-Augmented Generation (RAG): Keep Secret or Forget Knowledge?](https://arxiv.org/abs/2410.15267) | Shang Wang, Tianqing Zhu, Dayong Ye 等 4 人 | 8.60 | **A** | 2024-10-20 | Defense |
| 43 | [The Jailbreak Tax: How Useful are Your Jailbreak Outputs?](https://arxiv.org/abs/2504.10694) | Kristina Nikolić, Luze Sun, Jie Zhang 等 4 人 | 8.59 | **A** | 2025-04-14 | Eval |
| 44 | [Representation Bending for Large Language Model Safety](https://arxiv.org/abs/2504.01550) | Ashkan Yousefpour, Taeheon Kim, Ryan S. Kwon 等 10 人 | 8.59 | **A** | 2025-04-02 | Defense |
| 45 | [X-Teaming: Multi-Turn Jailbreaks and Defenses with Adaptive Multi-Agents](https://arxiv.org/abs/2504.13203) | Salman Rahman, Liwei Jiang, James Shiffer 等 10 人 | 8.56 | **A** | 2025-04-15 | Attacks |
| 46 | [MIND: A Multi-agent Framework for Zero-shot Harmful Meme Detection](https://arxiv.org/abs/2507.06908) | Ziyan Liu, Chunxiao Fan, Haoran Lou 等 5 人 | 8.56 | **A** | 2025-07-09 | Arch |
| 47 | [Towards Verifiably Safe Tool Use for LLM Agents](https://arxiv.org/abs/2601.08012) | Aarya Doshi, Yining Hong, Congying Xu 等 6 人 | 8.56 | **A** | 2026-01-12 | Arch |
| 48 | [SG-Bench: Evaluating LLM Safety Generalization Across Diverse Tasks and Prompt Types](https://arxiv.org/abs/2410.21965) | Yutao Mou, Shikun Zhang, Wei Ye | 8.56 | **A** | 2024-10-29 | Eval |
| 49 | [Survey on Evaluation of LLM-based Agents](https://arxiv.org/abs/2503.16416) | Asaf Yehudai, Lilach Eden, Alan Li 等 8 人 | 8.54 | **A** | 2025-03-20 | Eval |
| 50 | [DeepPlanning: Benchmarking Long-Horizon Agentic Planning with Verifiable Constraints](https://arxiv.org/abs/2601.18137) | Yinger Zhang, Shutong Jiang, Renhao Li 等 9 人 | 8.54 | **A** | 2026-01-26 | Eval |
| 51 | [RealSafe-R1: Safety-Aligned DeepSeek-R1 without Compromising Reasoning Capability](https://arxiv.org/abs/2504.10081) | Yichi Zhang, Zihao Zeng, Dongbai Li 等 6 人 | 8.53 | **A** | 2025-04-14 | Defense |
| 52 | [Audio Is the Achilles' Heel: Red Teaming Audio Large Multimodal Models](https://arxiv.org/abs/2410.23861) | Hao Yang, Lizhen Qu, Ehsan Shareghi 等 4 人 | 8.53 | **A** | 2024-10-31 | Eval |
| 53 | [Visual Contextual Attack: Jailbreaking MLLMs with Image-Driven Context Injection](https://arxiv.org/abs/2507.02844) | Ziqi Miao, Yi Ding, Lijun Li 等 4 人 | 8.52 | **A** | 2025-07-03 | Attacks |
| 54 | [ToolSafe: Enhancing Tool Invocation Safety of LLM-based agents via Proactive Step-level Guardrail and Feedback](https://arxiv.org/abs/2601.10156) | Yutao Mou, Zhangchi Xue, Lijun Li 等 7 人 | 8.52 | **A** | 2026-01-15 | Arch |
| 55 | [How Well Can Reasoning Models Identify and Recover from Unhelpful Thoughts?](https://arxiv.org/abs/2506.10979) | Sohee Yang, Sang-Woo Lee, Nora Kassner 等 6 人 | 8.50 | **A** | 2025-06-12 | Eval |
| 56 | [Safety is Not Only About Refusal: Reasoning-Enhanced Fine-tuning for Interpretable LLM Safety](https://arxiv.org/abs/2503.05021) | Yuyou Zhang, Miao Li, William Han 等 6 人 | 8.49 | **A** | 2025-03-06 | Defense |
| 57 | [Chasing Moving Targets with Online Self-Play Reinforcement Learning for Safer Language Models](https://arxiv.org/abs/2506.07468) | Mickel Liu, Liwei Jiang, Yancheng Liang 等 7 人 | 8.49 | **A** | 2025-06-09 | Defense |
| 58 | [Safety Guardrails for LLM-Enabled Robots](https://arxiv.org/abs/2503.07885) | Zachary Ravichandran, Alexander Robey, Vijay Kumar 等 5 人 | 8.48 | **A** | 2025-03-10 | Arch |
| 59 | [Adversarial Attacks on Robotic Vision Language Action Models](https://arxiv.org/abs/2506.03350) | Eliot Krzysztof Jones, Alexander Robey, Andy Zou 等 8 人 | 8.48 | **A** | 2025-06-03 | Attacks |
| 60 | [SOM Directions are Better than One: Multi-Directional Refusal Suppression in Language Models](https://arxiv.org/abs/2511.08379) | Giorgio Piras, Raffaele Mura, Fabio Brau 等 6 人 | 8.48 | **A** | 2025-11-11 | Attacks |
| 61 | [Foot-In-The-Door: A Multi-turn Jailbreak for LLMs](https://arxiv.org/abs/2502.19820) | Zixuan Weng, Xiaolong Jin, Jinyuan Jia 等 4 人 | 8.47 | **A** | 2025-02-27 | Attacks |
| 62 | [Breaking the Ceiling: Exploring the Potential of Jailbreak Attacks through Expanding Strategy Space](https://arxiv.org/abs/2505.21277) | Yao Huang, Yitong Sun, Shouwei Ruan 等 6 人 | 8.47 | **A** | 2025-05-27 | Attacks |
| 63 | [CowPilot: A Framework for Autonomous and Human-Agent Collaborative Web Navigation](https://arxiv.org/abs/2501.16609) | Faria Huq, Zora Zhiruo Wang, Frank F. Xu 等 7 人 | 8.46 | **A** | 2025-01-28 | Other |
| 64 | [The Task Shield: Enforcing Task Alignment to Defend Against Indirect Prompt Injection in LLM Agents](https://arxiv.org/abs/2412.16682) | Feiran Jia, Tong Wu, Xin Qin 等 4 人 | 8.46 | **A** | 2024-12-21 | Arch |
| 65 | [AudioJailbreak: Jailbreak Attacks against End-to-End Large Audio-Language Models](https://arxiv.org/abs/2505.14103) | Guangke Chen, Fu Song, Zhe Zhao 等 10 人 | 8.45 | **A** | 2025-05-20 | Attacks |
| 66 | [AlphaSteer: Learning Refusal Steering with Principled Null-Space Constraint](https://arxiv.org/abs/2506.07022) | Leheng Sheng, Changshuo Shen, Weixiang Zhao 等 9 人 | 8.44 | **A** | 2025-06-08 | Defense |
| 67 | [Uncovering Security Threats and Architecting Defenses in Autonomous Agents: A Case Study of OpenClaw](https://arxiv.org/abs/2603.12644) | Zonghao Ying, Xiao Yang, Siyang Wu 等 10 人 | 8.44 | **A** | 2026-03-13 | Arch |
| 68 | [MLA-Trust: Benchmarking Trustworthiness of Multimodal LLM Agents in GUI Environments](https://arxiv.org/abs/2506.01616) | Xiao Yang, Jiawei Chen, Jun Luo 等 7 人 | 8.43 | **A** | 2025-06-02 | Eval |
| 69 | [BlueSuffix: Reinforced Blue Teaming for Vision-Language Models Against Jailbreak Attacks](https://arxiv.org/abs/2410.20971) | Yunhan Zhao, Xiang Zheng, Lin Luo 等 6 人 | 8.43 | **A** | 2024-10-28 | Defense |
| 70 | [Best-of-N Jailbreaking](https://arxiv.org/abs/2412.03556) | John Hughes, Sara Price, Aengus Lynch 等 10 人 | 8.43 | **A** | 2024-12-04 | Attacks |
| 71 | [Jailbreak-Tuning: Models Efficiently Learn Jailbreak Susceptibility](https://arxiv.org/abs/2507.11630) | Brendan Murphy, Dillon Bowen, Shahrad Mohammadzadeh 等 7 人 | 8.42 | **A** | 2025-07-15 | Attacks |
| 72 | [Refusal-Trained LLMs Are Easily Jailbroken As Browser Agents](https://arxiv.org/abs/2410.13886) | Priyanshu Kumar, Elaine Lau, Saranya Vijayakumar 等 12 人 | 8.41 | **A** | 2024-10-11 | Eval |
| 73 | [MTSA: Multi-turn Safety Alignment for LLMs through Multi-round Red-teaming](https://arxiv.org/abs/2505.17147) | Weiyang Guo, Jing Li, Wenya Wang 等 7 人 | 8.40 | **A** | 2025-05-22 | Defense |
| 74 | [VeriGuard: Enhancing LLM Agent Safety via Verified Code Generation](https://arxiv.org/abs/2510.05156) | Lesly Miculicich, Mihir Parmar, Hamid Palangi 等 7 人 | 8.40 | **A** | 2025-10-03 | Arch |
| 75 | [Agent-SafetyBench: Evaluating the Safety of LLM Agents](https://arxiv.org/abs/2412.14470) | Zhexin Zhang, Shiyao Cui, Yida Lu 等 7 人 | 8.38 | **A** | 2024-12-19 | Eval |
| 76 | [AutoRedTeamer: Autonomous Red Teaming with Lifelong Attack Integration](https://arxiv.org/abs/2503.15754) | Andy Zhou, Kevin Wu, Francesco Pinto 等 10 人 | 8.37 | **A** | 2025-03-20 | Eval |
| 77 | [Towards Understanding the Fragility of Multilingual LLMs against Fine-Tuning Attacks](https://arxiv.org/abs/2410.18210) | Samuele Poppi, Zheng-Xin Yong, Yifei He 等 7 人 | 8.35 | **A** | 2024-10-23 | Attacks |
| 78 | [SafeMLRM: Demystifying Safety in Multi-modal Large Reasoning Models](https://arxiv.org/abs/2504.08813) | Junfeng Fang, Yukai Wang, Ruipeng Wang 等 8 人 | 8.34 | **A** | 2025-04-09 | Eval |
| 79 | [Does Chain-of-Thought Reasoning Really Reduce Harmfulness from Jailbreaking?](https://arxiv.org/abs/2505.17650) | Chengda Lu, Xiaoyu Fan, Yu Huang 等 6 人 | 8.34 | **A** | 2025-05-23 | Attacks |
| 80 | [Jailbreaking Multimodal Large Language Models via Shuffle Inconsistency](https://arxiv.org/abs/2501.04931) | Shiji Zhao, Ranjie Duan, Fengxiang Wang 等 10 人 | 8.32 | **A** | 2025-01-09 | Attacks |
| 81 | [Holistic Agent Leaderboard: The Missing Infrastructure for AI Agent Evaluation](https://arxiv.org/abs/2510.11977) | Sayash Kapoor, Benedikt Stroebl, Peter Kirgis 等 31 人 | 8.32 | **A** | 2025-10-13 | Eval |
| 82 | [A Survey on Autonomy-Induced Security Risks in Large Model-Based Agents](https://arxiv.org/abs/2506.23844) | Hang Su, Jun Luo, Chang Liu 等 7 人 | 8.31 | **A** | 2025-06-30 | Arch |
| 83 | [Eliciting Language Model Behaviors with Investigator Agents](https://arxiv.org/abs/2502.01236) | Xiang Lisa Li, Neil Chowdhury, Daniel D. Johnson 等 7 人 | 8.30 | **A** | 2025-02-03 | Eval |
| 84 | [Security Challenges in AI Agent Deployment: Insights from a Large Scale Public Competition](https://arxiv.org/abs/2507.20526) | Andy Zou, Maxwell Lin, Eliot Jones 等 17 人 | 8.30 | **A** | 2025-07-28 | Eval |
| 85 | [Adjacent Words, Divergent Intents: Jailbreaking Large Language Models via Task Concurrency](https://arxiv.org/abs/2510.21189) | Yukun Jiang, Mingjie Li, Michael Backes 等 4 人 | 8.30 | **A** | 2025-10-24 | Attacks |
| 86 | [The Assistant Axis: Situating and Stabilizing the Default Persona of Language Models](https://arxiv.org/abs/2601.10387) | Christina Lu, Jack Gallagher, Jonathan Michala 等 5 人 | 8.30 | **A** | 2026-01-15 | Defense |
| 87 | [HAICOSYSTEM: An Ecosystem for Sandboxing Safety Risks in Human-AI Interactions](https://arxiv.org/abs/2409.16427) | Xuhui Zhou, Hyunwoo Kim, Faeze Brahman 等 12 人 | 8.30 | **A** | 2024-09-24 | Eval |
| 88 | [REINFORCE Adversarial Attacks on Large Language Models: An Adaptive, Distributional, and Semantic Objective](https://arxiv.org/abs/2502.17254) | Simon Geisler, Tom Wollschläger, M. H. I. Abdalla 等 6 人 | 8.29 | **A** | 2025-02-24 | Attacks |
| 89 | [MAEBE: Multi-Agent Emergent Behavior Framework](https://arxiv.org/abs/2506.03053) | Sinem Erisken, Timothy Gothard, Martin Leitgab 等 4 人 | 8.29 | **A** | 2025-06-03 | Eval |
| 90 | [Beyond Simulations: What 20,000 Real Conversations Reveal About Mental Health AI Safety](https://arxiv.org/abs/2601.17003) | Caitlin A. Stamatis, Jonah Meyerhoff, Richard Zhang 等 6 人 | 8.29 | **A** | 2026-01-14 | Eval |
| 91 | [Adversarial Reasoning at Jailbreaking Time](https://arxiv.org/abs/2502.01633) | Mahdi Sabbaghi, Paul Kassianik, George Pappas 等 6 人 | 8.28 | **A** | 2025-02-03 | Attacks |
| 92 | [Think in Safety: Unveiling and Mitigating Safety Alignment Collapse in Multimodal Large Reasoning Model](https://arxiv.org/abs/2505.06538) | Xinyue Lou, You Li, Jinan Xu 等 6 人 | 8.28 | **A** | 2025-05-10 | Defense |
| 93 | [Evaluation and Benchmarking of LLM Agents: A Survey](https://arxiv.org/abs/2507.21504) | Mahmoud Mohammadi, Yipeng Li, Jane Lo 等 4 人 | 8.28 | **A** | 2025-07-29 | Eval |
| 94 | [Jailbreak Antidote: Runtime Safety-Utility Balance via Sparse Representation Adjustment in Large Language Models](https://arxiv.org/abs/2410.02298) | Guobin Shen, Dongcheng Zhao, Yiting Dong 等 5 人 | 8.28 | **A** | 2024-10-03 | Defense |
| 95 | [Superintelligent Agents Pose Catastrophic Risks: Can Scientist AI Offer a Safer Path?](https://arxiv.org/abs/2502.15657) | Yoshua Bengio, Michael Cohen, Damiano Fornasiere 等 13 人 | 8.26 | **A** | 2025-02-21 | Arch |
| 96 | [Defending against Indirect Prompt Injection by Instruction Detection](https://arxiv.org/abs/2505.06311) | Tongyu Wen, Chenglong Wang, Xiyuan Yang 等 8 人 | 8.26 | **A** | 2025-05-08 | Defense |
| 97 | [Defending Against Prompt Injection with DataFilter](https://arxiv.org/abs/2510.19207) | Yizhu Wang, Sizhe Chen, Raghad Alkhudair 等 5 人 | 8.26 | **A** | 2025-10-22 | Defense |
| 98 | [From Assistant to Double Agent: Formalizing and Benchmarking Attacks on OpenClaw for Personalized Local AI Agent](https://arxiv.org/abs/2602.08412) | Yuhang Wang, Feiming Xu, Zheng Lin 等 9 人 | 8.26 | **A** | 2026-02-09 | Eval |
| 99 | [Multimodal Situational Safety](https://arxiv.org/abs/2410.06172) | Kaiwen Zhou, Chengzhi Liu, Xuandong Zhao 等 6 人 | 8.26 | **A** | 2024-10-08 | Eval |
| 100 | [AgentSpec: Customizable Runtime Enforcement for Safe and Reliable LLM Agents](https://arxiv.org/abs/2503.18666) | Haoyu Wang, Christopher M. Poskitt, Jun Sun | 8.25 | **A** | 2025-03-24 | Arch |

---

*数据来源：[arXiv](https://arxiv.org/)、[Semantic Scholar](https://www.semanticscholar.org/)*
