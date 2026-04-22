# 🛡️ Defense & Alignment（防御与对齐）

> 502 篇论文 | 按质量评分排序

---

## #1 — STAIR: Improving Safety Alignment with Introspective Reasoning

`A` Score: 9.32 | 2025-02-04

**Authors:** Yichi Zhang, Siyuan Zhang, Yao Huang, Zeyu Xia, Zhengwei Fang, Xiao Yang et al. (10 total)

**Categories:** cs.CL

**Scores:** Citation: 9.82 | Influential: 9.69 | Venue: 10.00 | Author: 9.71 | Recency: 5.00

**Links:** [arXiv](https://arxiv.org/abs/2502.02384) | [PDF](https://arxiv.org/pdf/2502.02384)

> 针对现有安全对齐方法的安全-性能权衡和对越狱攻击的脆弱性问题，研究者提出STAIR框架，将安全对齐与内省推理相结合。该方法通过安全感知的自我改进思维链推理识别安全风险，利用安全感知蒙特卡洛树搜索生成步骤级推理数据，并通过迭代偏好优化推进安全对齐。实验表明，STAIR能有效减少有害输出同时保持帮助性，测试时扩展后对流行越狱攻击的安全性可与Claude-3.5媲美。

---

## #2 — AGrail: A Lifelong Agent Guardrail with Effective and Adaptive Safety Detection

`A` Score: 9.28 | 2025-02-17

**Authors:** Weidi Luo, Shenghong Dai, Xiaogeng Liu, Suman Banerjee, Huan Sun, Muhao Chen et al. (7 total)

**Categories:** cs.AI

**Scores:** Citation: 9.66 | Influential: 9.86 | Venue: 10.00 | Author: 9.75 | Recency: 5.00

**Links:** [arXiv](https://arxiv.org/abs/2502.11448) | [PDF](https://arxiv.org/pdf/2502.11448)

> 这篇论文提出了AGrail，一个针对大型语言模型(LLM)代理的终身安全护栏系统。随着LLMs作为自主代理在复杂环境中的广泛应用，其面临任务特定风险和系统风险，这些风险可能危及信息的机密性、完整性和可用性。AGrail通过自适应安全检查生成、有效安全检查优化以及工具兼容性和灵活性，解决了现有防御机制无法有效适应性地减轻这些风险的问题。

---

## #3 — Towards LLM Unlearning Resilient to Relearning Attacks: A Sharpness-Aware Minimization Perspective and Beyond

`A` Score: 9.18 | 2025-02-07

**Authors:** Chongyu Fan, Jinghan Jia, Yihua Zhang, Anil Ramakrishna, Mingyi Hong, Sijia Liu

**Categories:** cs.LG, cs.CL

**Scores:** Citation: 9.81 | Influential: 9.90 | Venue: 10.00 | Author: 8.55 | Recency: 5.00

**Links:** [arXiv](https://arxiv.org/abs/2502.05374) | [PDF](https://arxiv.org/pdf/2502.05374)

> 针对LLM未学习技术易受'重新学习'攻击的脆弱性，研究者首次建立鲁棒未学习与锐度感知最小化的联系，通过统一鲁棒优化框架分析平滑优化在减轻重新学习攻击中的关键作用。实验表明，平滑增强的未学习方法能有效抵抗重新学习攻击，同时防御越狱攻击。这一发现为构建更安全的未学习机制提供了新视角，对数据合规和模型安全具有重要价值。

---

## #4 — SafeKey: Amplifying Aha-Moment Insights for Safety Reasoning

`A` Score: 9.04 | 2025-05-22

**Authors:** Kaiwen Zhou, Xuandong Zhao, Gaowen Liu, Jayanth Srinivasa, Aosong Feng, Dawn Song et al. (7 total)

**Categories:** cs.AI, cs.CL, cs.CR

**Scores:** Citation: 9.16 | Influential: 9.39 | Venue: 10.00 | Author: 8.93 | Recency: 7.00

**Links:** [arXiv](https://arxiv.org/abs/2505.16186) | [PDF](https://arxiv.org/pdf/2505.16186)

> 本文针对大型推理模型（LRM）的安全泛化问题，提出了SafeKey方法，通过识别生成过程中的“安全顿悟时刻”来激活安全推理。该方法包含双路径安全头和查询掩码建模两个目标，显著降低了模型在面对未见越狱攻击时的有害率，同时保持了通用能力。

---

## #5 — Instructional Segment Embedding: Improving LLM Safety with Instruction Hierarchy

`A` Score: 9.04 | 2024-10-09

**Authors:** Tong Wu, Shujian Zhang, Kaiqiang Song, Silei Xu, Sanqiang Zhao, Ravi Agrawal et al. (10 total)

**Categories:** cs.LG, cs.AI, cs.CL

**Scores:** Citation: 9.64 | Influential: 9.90 | Venue: 10.00 | Author: 8.15 | Recency: 5.00

**Links:** [arXiv](https://arxiv.org/abs/2410.09102) | [PDF](https://arxiv.org/pdf/2410.09102)

> 本文针对LLM缺乏指令层次结构导致的安全漏洞，提出了指令段嵌入（ISE）技术。该技术受BERT启发，将指令优先级信息直接嵌入模型架构中，使模型能够明确区分和优先处理系统消息、用户提示等不同类型的指令。实验表明，ISE显著提高了模型对抗恶意提示的鲁棒性，平均将鲁棒准确率提高了约15-18%，同时增强了指令遵循能力。

---

## #6 — Reasoning-to-Defend: Safety-Aware Reasoning Can Defend Large Language Models from Jailbreaking

`A` Score: 8.98 | 2025-02-18

**Authors:** Junda Zhu, Lingyong Yan, Shuaiqiang Wang, Dawei Yin, Lei Sha

**Categories:** cs.CL

**Scores:** Citation: 9.56 | Influential: 9.77 | Venue: 10.00 | Author: 8.15 | Recency: 5.00

**Links:** [arXiv](https://arxiv.org/abs/2502.12970) | [PDF](https://arxiv.org/pdf/2502.12970)

> 本文提出了Reasoning-to-Defend(R2D)训练范式，将安全感知推理机制整合到LLM生成过程中。该方法通过在每个推理步骤进行自我评估形成安全枢轴标记，并引入对比枢轴优化提高准确性。实验表明，R2D能有效缓解各种越狱攻击，同时保持模型原有性能，展示了安全感知推理的潜力。

---

## #7 — Robust LLM safeguarding via refusal feature adversarial training

`A` Score: 8.98 | 2024-09-30

**Authors:** Lei Yu, Virginie Do, Karen Hambardzumyan, Nicola Cancedda

**Categories:** cs.LG, cs.CL, cs.CR

**Scores:** Citation: 9.69 | Influential: 9.77 | Venue: 10.00 | Author: 7.80 | Recency: 5.00

**Links:** [arXiv](https://arxiv.org/abs/2409.20089) | [PDF](https://arxiv.org/pdf/2409.20089)

> 本文揭示了对抗性攻击通过消除残差流嵌入空间中的“拒绝特征”来绕过LLM安全机制的通用原理。基于此发现，作者提出了拒绝特征对抗训练（ReFAT）算法，通过模拟拒绝特征消除的效果高效执行对抗训练，显著提升了模型鲁棒性且计算开销更低。

---

## #8 — Improving LLM Safety Alignment with Dual-Objective Optimization

`A` Score: 8.94 | 2025-03-05

**Authors:** Xuandong Zhao, Will Cai, Tianneng Shi, David Huang, Licong Lin, Song Mei et al. (7 total)

**Categories:** cs.CL, cs.CR, cs.LG

**Scores:** Citation: 9.37 | Influential: 9.39 | Venue: 10.00 | Author: 8.93 | Recency: 5.00

**Links:** [arXiv](https://arxiv.org/abs/2503.03710) | [PDF](https://arxiv.org/pdf/2503.03710)

> 本文分析了现有LLM安全对齐技术的局限性，并提出了一种改进的安全对齐方法，将DPO目标解耦为两个组件：稳健的拒绝训练和有害知识的目标性遗忘。该方法显著提高了LLM对抗各种越狱攻击的鲁棒性，包括填充、后缀和多轮攻击。研究还表明，对越狱攻击的鲁棒性与训练过程中令牌分布的转移和拒绝与有害令牌的内部表示相关。

---

## #9 — JBShield: Defending Large Language Models from Jailbreak Attacks through Activated Concept Analysis and Manipulation

`A` Score: 8.92 | 2025-02-11

**Authors:** Shenyi Zhang, Yuchen Zhai, Keyan Guo, Hongxin Hu, Shengnan Guo, Zheng Fang et al. (10 total)

**Categories:** cs.CR

**Scores:** Citation: 9.67 | Influential: 9.77 | Venue: 10.00 | Author: 7.43 | Recency: 5.00

**Links:** [arXiv](https://arxiv.org/abs/2502.07557) | [PDF](https://arxiv.org/pdf/2502.07557)

> 基于线性表示假设，研究越狱攻击机制，将有害语义定义为有毒概念，越狱操纵语义定义为越狱概念。分析发现LLM能识别两类提示中的有毒概念，但越狱提示额外激活越狱概念导致服从行为。基于此提出JBShield框架，包含检测和缓解组件，通过识别同时激活有毒和越狱概念的输入，并调整目标LLM隐藏表示来防御越狱攻击，提供更深入的安全防护机制。

---

## #10 — InfAlign: Inference-aware language model alignment

`A` Score: 8.85 | 2024-12-27

**Authors:** Ananth Balashankar, Ziteng Sun, Jonathan Berant, Jacob Eisenstein, Michael Collins, Adrian Hutter et al. (12 total)

**Categories:** cs.LG, cs.CL, cs.IT

**Scores:** Citation: 9.02 | Influential: 9.02 | Venue: 10.00 | Author: 9.90 | Recency: 5.00

**Links:** [arXiv](https://arxiv.org/abs/2412.19792) | [PDF](https://arxiv.org/pdf/2412.19792)

> 针对标准RLHF在推理时算法（如Best-of-N）下的次优性，本文提出了InfAlign框架。该框架旨在优化推理时的胜率，通过校准和转换奖励函数，提出了InfAlign-CTRL算法，在Best-of-N采样和越狱防御场景中实现了显著的性能提升，解决了训练与测试不匹配的问题。

---

## #11 — AdaSteer: Your Aligned LLM is Inherently an Adaptive Jailbreak Defender

`A` Score: 8.84 | 2025-04-13

**Authors:** Weixiang Zhao, Jiahe Guo, Yulin Hu, Yang Deng, An Zhang, Xingyu Sui et al. (11 total)

**Categories:** cs.CR, cs.CL

**Scores:** Citation: 9.27 | Influential: 9.02 | Venue: 10.00 | Author: 9.09 | Recency: 5.00

**Links:** [arXiv](https://arxiv.org/abs/2504.09466) | [PDF](https://arxiv.org/pdf/2504.09466)

> 本文提出了 AdaSteer，一种基于自适应激活转向的越狱防御方法，通过动态调整转向系数来应对不同输入。该方法利用拒绝定律和有害性定律，在有效防御越狱攻击的同时，最大程度减少了对良性输入的误拒。实验证明 AdaSteer 在多个模型上优于基线方法，展示了利用模型内部表征进行实时灵活安全执行的潜力。

---

## #12 — Trustworthy AI-Driven Dynamic Hybrid RIS: Joint Optimization and Reward Poisoning-Resilient Control in Cognitive MISO Networks

`A` Score: 8.68 | 2026-03-27

**Authors:** Deemah H. Tashman, Soumaya Cherkaoui

**Categories:** cs.NI, cs.AI

**Scores:** Citation: 9.41 | Influential: 7.81 | Venue: 5.00 | Author: 9.23 | Recency: 10.00

**Links:** [arXiv](https://arxiv.org/abs/2604.01238) | [PDF](https://arxiv.org/pdf/2604.01238)

> 本文研究了认知无线电网络中基于AI驱动的动态混合可重构智能表面（RIS）的联合优化与安全控制问题。工作引入了自适应混合RIS架构，并利用软演员-评论家（SAC）深度强化学习方法解决波束成形和相位优化问题。此外，文章首次系统研究了RIS增强网络中DRL智能体的奖励投毒攻击，并提出了基于奖励裁剪和统计异常过滤的轻量级实时防御机制，数值结果验证了该方法的有效性。

---

## #13 — HarmAug: Effective Data Augmentation for Knowledge Distillation of Safety Guard Models

`A` Score: 8.66 | 2024-10-02

**Authors:** Seanie Lee, Haebin Seong, Dong Bok Lee, Minki Kang, Xiaoyin Chen, Dominik Wagner et al. (9 total)

**Categories:** cs.CL, cs.LG

**Scores:** Citation: 8.36 | Influential: 9.58 | Venue: 10.00 | Author: 9.89 | Recency: 5.00

**Links:** [arXiv](https://arxiv.org/abs/2410.01524) | [PDF](https://arxiv.org/pdf/2410.01524)

> 本文提出了HarmAug，一种有效的数据增强方法，用于将大型教师安全护栏模型蒸馏为适合移动设备的小型模型。该方法通过越狱LLM生成有害指令并利用教师模型进行标注，解决了现有标注数据多样性有限的问题，显著提升了小型安全模型的性能。

---

## #14 — Constitutional Classifiers: Defending against Universal Jailbreaks across Thousands of Hours of Red Teaming

`A` Score: 8.65 | 2025-01-31

**Authors:** Mrinank Sharma, Meg Tong, Jesse Mu, Jerry Wei, Jorrit Kruthoff, Scott Goodfriend et al. (43 total)

**Categories:** cs.CL, cs.AI, cs.CR

**Scores:** Citation: 9.97 | Influential: 9.98 | Venue: 2.00 | Author: 9.77 | Recency: 5.00

**Links:** [arXiv](https://arxiv.org/abs/2501.18837) | [PDF](https://arxiv.org/pdf/2501.18837)

> 本文引入宪法分类器防御通用越狱攻击，通过自然语言规则生成合成数据进行训练。在3000小时红队测试中，该分类器有效阻止了针对早期保护模型的越狱攻击，同时保持低拒绝率(仅增0.38%)和合理推理开销(23.7%)，证明了部署可行性。

---

## #15 — When Machine Unlearning Meets Retrieval-Augmented Generation (RAG): Keep Secret or Forget Knowledge?

`A` Score: 8.60 | 2024-10-20

**Authors:** Shang Wang, Tianqing Zhu, Dayong Ye, Wanlei Zhou

**Categories:** cs.CR, cs.CL

**Scores:** Citation: 8.69 | Influential: 9.39 | Venue: 10.00 | Author: 8.73 | Recency: 5.00

**Links:** [arXiv](https://arxiv.org/abs/2410.15267) | [PDF](https://arxiv.org/pdf/2410.15267)

> 针对现有机器遗忘方法计算需求高或适用性有限的问题，本文提出了一种基于检索增强生成（RAG）的轻量级行为遗忘框架。该方法通过修改RAG的外部知识库来模拟遗忘效果，将遗忘知识的构建视为约束优化问题，在闭源和开源模型上均验证了其有效性和无害性。

---

## #16 — Representation Bending for Large Language Model Safety

`A` Score: 8.59 | 2025-04-02

**Authors:** Ashkan Yousefpour, Taeheon Kim, Ryan S. Kwon, Seungbeen Lee, Wonje Jeung, Seungju Han et al. (10 total)

**Categories:** cs.LG, cs.CL, cs.CR

**Scores:** Citation: 8.90 | Influential: 9.58 | Venue: 10.00 | Author: 7.80 | Recency: 5.00

**Links:** [arXiv](https://arxiv.org/abs/2504.01550) | [PDF](https://arxiv.org/pdf/2504.01550)

> 本文提出了RepBend，一种通过从根本上破坏LLM中有害行为底层表示来增强模型安全性的新方法。该方法将激活引导的思想引入基于损失的微调中，通过广泛的评估实现了最先进的性能，在多种越狱基准测试中将攻击成功率降低了高达95%。RepBend在显著提升安全性的同时，对模型可用性和通用能力的影响微乎其微，为解决对抗性攻击和微调漏洞提供了可扩展的解决方案。

---

## #17 — RealSafe-R1: Safety-Aligned DeepSeek-R1 without Compromising Reasoning Capability

`A` Score: 8.53 | 2025-04-14

**Authors:** Yichi Zhang, Zihao Zeng, Dongbai Li, Yao Huang, Zhijie Deng, Yinpeng Dong

**Categories:** cs.AI, cs.CL

**Scores:** Citation: 9.86 | Influential: 9.69 | Venue: 2.00 | Author: 9.71 | Recency: 5.00

**Links:** [arXiv](https://arxiv.org/abs/2504.10081) | [PDF](https://arxiv.org/pdf/2504.10081)

> 本文介绍了 RealSafe-R1，这是 DeepSeek-R1 蒸馏模型的安全对齐版本。作者构建了包含 1.5 万条安全推理轨迹的数据集进行训练，使模型能有效抵御恶意查询和越狱攻击。该方法在不损害模型原有数学和代码推理能力的前提下，显著提升了模型的安全性，为开源推理模型的安全应用提供了新方案。

---

## #18 — Safety is Not Only About Refusal: Reasoning-Enhanced Fine-tuning for Interpretable LLM Safety

`A` Score: 8.49 | 2025-03-06

**Authors:** Yuyou Zhang, Miao Li, William Han, Yihang Yao, Zhepeng Cen, Ding Zhao

**Categories:** cs.CL, cs.CR

**Scores:** Citation: 9.31 | Influential: 9.39 | Venue: 10.00 | Author: 6.17 | Recency: 5.00

**Links:** [arXiv](https://arxiv.org/abs/2503.05021) | [PDF](https://arxiv.org/pdf/2503.05021)

> 本文提出了'理性'(Rational)框架，通过在响应前进行明确的安全推理来增强LLM安全性。该方法利用预训练知识通过结构化推理来增强模型安全能力，使模型能够拒绝有害提示并在复杂场景中提供有意义且上下文感知的响应。研究表明，安全不仅在于拒绝，还需要上下文感知能力，推理不仅是LLM的核心能力，也是其安全的基本机制。

---

## #19 — Chasing Moving Targets with Online Self-Play Reinforcement Learning for Safer Language Models

`A` Score: 8.49 | 2025-06-09

**Authors:** Mickel Liu, Liwei Jiang, Yancheng Liang, Simon Shaolei Du, Yejin Choi, Tim Althoff et al. (7 total)

**Categories:** cs.LG, cs.CL, cs.MA

**Scores:** Citation: 9.48 | Influential: 9.69 | Venue: 2.00 | Author: 9.23 | Recency: 7.00

**Links:** [arXiv](https://arxiv.org/abs/2506.07468) | [PDF](https://arxiv.org/pdf/2506.07468)

> 针对传统反应式安全对齐的滞后性，本文提出了Self-RedTeam在线自博弈强化学习算法。该算法将安全对齐建模为零和博弈，使攻击者和防御者通过持续交互共同进化，从而动态提升模型对新兴威胁的鲁棒性。

---

## #20 — AlphaSteer: Learning Refusal Steering with Principled Null-Space Constraint

`A` Score: 8.44 | 2025-06-08

**Authors:** Leheng Sheng, Changshuo Shen, Weixiang Zhao, Junfeng Fang, Xiaohao Liu, Zhenkai Liang et al. (9 total)

**Categories:** cs.LG, cs.AI, cs.CR

**Scores:** Citation: 9.48 | Influential: 9.58 | Venue: 2.00 | Author: 9.09 | Recency: 7.00

**Links:** [arXiv](https://arxiv.org/abs/2506.07022) | [PDF](https://arxiv.org/pdf/2506.07022)

> 针对激活引导中安全性与实用性之间的权衡问题，本文提出了AlphaSteer方法。该方法通过零空间约束学习构建针对良性数据的近零向量，并利用线性回归学习针对恶意数据的拒绝方向，从而在不损害良性提示性能的前提下增强安全性。

---

## #21 — BlueSuffix: Reinforced Blue Teaming for Vision-Language Models Against Jailbreak Attacks

`A` Score: 8.43 | 2024-10-28

**Authors:** Yunhan Zhao, Xiang Zheng, Lin Luo, Yige Li, Xingjun Ma, Yu-Gang Jiang

**Categories:** cs.CV, cs.AI, cs.LG

**Scores:** Citation: 8.84 | Influential: 9.39 | Venue: 10.00 | Author: 7.15 | Recency: 5.00

**Links:** [arXiv](https://arxiv.org/abs/2410.20971) | [PDF](https://arxiv.org/pdf/2410.20971)

> 本文提出了 BlueSuffix，一种针对视觉语言模型越狱攻击的黑盒防御方法。该方法包含视觉净化器、文本净化器以及使用强化微调的蓝队后缀生成器三个关键组件，旨在增强跨模态鲁棒性。在四个 VLM 和四个安全基准上的实验表明，BlueSuffix 显著优于基线防御方法，且不损害模型在良性输入上的性能。

---

## #22 — MTSA: Multi-turn Safety Alignment for LLMs through Multi-round Red-teaming

`A` Score: 8.40 | 2025-05-22

**Authors:** Weiyang Guo, Jing Li, Wenya Wang, YU LI, Daojing He, Jun Yu et al. (7 total)

**Categories:** cs.CR, cs.AI

**Scores:** Citation: 9.28 | Influential: 9.77 | Venue: 10.00 | Author: 3.78 | Recency: 7.00

**Links:** [arXiv](https://arxiv.org/abs/2505.17147) | [PDF](https://arxiv.org/pdf/2505.17147)

> 本文提出了MTSA框架，通过多轮红队测试来解决多轮对话中的安全问题。该框架包含思维引导的攻击学习和对抗迭代优化阶段，利用基于未来奖励的多轮强化学习算法，显著提升了目标模型在安全基准上的表现，增强了多轮交互中的鲁棒性。

---

## #23 — The Assistant Axis: Situating and Stabilizing the Default Persona of Language Models

`A` Score: 8.30 | 2026-01-15

**Authors:** Christina Lu, Jack Gallagher, Jonathan Michala, Kyle Fish, Jack Lindsey

**Categories:** cs.CL

**Scores:** Citation: 9.93 | Influential: 9.02 | Venue: 2.00 | Author: 6.17 | Recency: 9.00

**Links:** [arXiv](https://arxiv.org/abs/2601.10387) | [PDF](https://arxiv.org/pdf/2601.10387)

> 本文发现了模型角色空间中的“助手轴”，并证明限制该轴上的激活可以稳定模型行为，防止有害的角色漂移。该方法通过操纵内部激活方向，有效防御了基于角色的越狱攻击，为理解和控制模型默认行为提供了新视角。

---

## #24 — Think in Safety: Unveiling and Mitigating Safety Alignment Collapse in Multimodal Large Reasoning Model

`A` Score: 8.28 | 2025-05-10

**Authors:** Xinyue Lou, You Li, Jinan Xu, Xiangyu Shi, Chi Chen, Kaiyu Huang

**Categories:** cs.CL

**Scores:** Citation: 8.85 | Influential: 9.39 | Venue: 10.00 | Author: 4.79 | Recency: 7.00

**Links:** [arXiv](https://arxiv.org/abs/2505.06538) | [PDF](https://arxiv.org/pdf/2505.06538)

> 本文对11个多模态大推理模型进行了全面的安全评估，揭示了大多数先进模型中普遍存在的安全退化现象。研究发现，长思维过程在某些场景下能增强安全性，因此利用模型内在推理能力检测不安全意图是解决MLRM安全问题的潜在途径。作者构建了包含安全导向思维过程的数据集，微调实验表明该方法能有效提升模型在越狱鲁棒性和安全意识基准上的表现。

---

## #25 — Jailbreak Antidote: Runtime Safety-Utility Balance via Sparse Representation Adjustment in Large Language Models

`A` Score: 8.28 | 2024-10-03

**Authors:** Guobin Shen, Dongcheng Zhao, Yiting Dong, Xiang He, Yi Zeng

**Categories:** cs.CR, cs.CL

**Scores:** Citation: 8.28 | Influential: 9.02 | Venue: 10.00 | Author: 8.33 | Recency: 5.00

**Links:** [arXiv](https://arxiv.org/abs/2410.02298) | [PDF](https://arxiv.org/pdf/2410.02298)

> 本研究提出了一种名为“越狱解毒剂”的方法，通过在推理过程中操纵模型内部状态的稀疏子集，实时调整大语言模型的安全偏好。该方法通过沿安全方向移动模型的隐藏表示，实现了对安全-效用平衡的灵活控制，且无需额外的 token 开销或推理延迟。实验验证了该方法在多种 LLM 上对抗越狱攻击的有效性和高效性。

---

## #26 — Defending against Indirect Prompt Injection by Instruction Detection

`A` Score: 8.26 | 2025-05-08

**Authors:** Tongyu Wen, Chenglong Wang, Xiyuan Yang, Haoyu Tang, Yueqi Xie, Lingjuan Lyu et al. (8 total)

**Categories:** cs.CR, cs.AI

**Scores:** Citation: 8.85 | Influential: 7.81 | Venue: 10.00 | Author: 6.75 | Recency: 7.00

**Links:** [arXiv](https://arxiv.org/abs/2505.06311) | [PDF](https://arxiv.org/pdf/2505.06311)

> 针对检索增强生成系统中的间接提示注入攻击，本文提出了InstructDetector，一种基于检测的防御方法。该方法利用大语言模型中间层的隐藏状态和梯度作为判别特征，有效识别外部内容中的隐藏指令，显著降低了攻击成功率，为防御IPI攻击提供了新思路。

---

## #27 — Defending Against Prompt Injection with DataFilter

`A` Score: 8.26 | 2025-10-22

**Authors:** Yizhu Wang, Sizhe Chen, Raghad Alkhudair, Basel Alomair, David Wagner

**Categories:** cs.CR

**Scores:** Citation: 9.56 | Influential: 9.02 | Venue: 2.00 | Author: 8.33 | Recency: 7.00

**Links:** [arXiv](https://arxiv.org/abs/2510.19207) | [PDF](https://arxiv.org/pdf/2510.19207)

> 本文提出了DataFilter，一种测试时且与模型无关的防御方法，用于在数据到达后端大语言模型之前移除恶意指令。DataFilter通过在模拟注入数据上进行监督微调，能够选择性地剥离对抗性内容，在将提示注入攻击成功率降至接近零的同时，有效保持了模型的原始效用。

---

## #28 — RobustKV: Defending Large Language Models against Jailbreak Attacks via KV Eviction

`A` Score: 8.24 | 2024-10-25

**Authors:** Tanqiu Jiang, Zian Wang, Jiacheng Liang, Changjiang Li, Yuhui Wang, Ting Wang

**Categories:** cs.CR, cs.AI, cs.CL

**Scores:** Citation: 8.92 | Influential: 9.02 | Venue: 10.00 | Author: 6.17 | Recency: 5.00

**Links:** [arXiv](https://arxiv.org/abs/2410.19937) | [PDF](https://arxiv.org/pdf/2410.19937)

> 本文提出了 RobustKV，一种通过从键值（KV）缓存中有选择地移除有害查询的关键 token 来防御越狱攻击的新方法。该方法基于越狱提示词会降低隐藏有害查询 token 重要性的直觉，通过策略性地驱逐低排名 token 的 KV 来防止恶意响应的生成。实验表明，RobustKV 在有效对抗最先进越狱攻击的同时，保持了 LLM 在良性查询上的通用性能。

---

## #29 — Understanding Refusal in Language Models with Sparse Autoencoders

`A` Score: 8.23 | 2025-05-29

**Authors:** Wei Jie Yeo, Nirmalendu Prakash, Clement Neo, Roy Ka-Wei Lee, Erik Cambria, Ranjan Satapathy

**Categories:** cs.CL

**Scores:** Citation: 8.08 | Influential: 9.39 | Venue: 10.00 | Author: 6.75 | Recency: 7.00

**Links:** [arXiv](https://arxiv.org/abs/2505.23556) | [PDF](https://arxiv.org/pdf/2505.23556)

> 本文利用稀疏自编码器对指令微调语言模型中的拒绝机制进行了机理研究，识别了因果调节拒绝行为的潜在特征。通过干预这些特征，研究验证了其在多个有害数据集上的行为影响，并揭示了对抗性越狱技术的内部机制。

---

## #30 — Building a Foundational Guardrail for General Agentic Systems via Synthetic Data

`A` Score: 8.19 | 2025-10-10

**Authors:** Yue Huang, Hang Hua, Yujun Zhou, Pengcheng Jing, Manish Nagireddy, Inkit Padhi et al. (14 total)

**Categories:** cs.LG, cs.AI, cs.CL

**Scores:** Citation: 9.08 | Influential: 9.02 | Venue: 2.00 | Author: 9.34 | Recency: 7.00

**Links:** [arXiv](https://arxiv.org/abs/2510.09781) | [PDF](https://arxiv.org/pdf/2510.09781)

> 本文针对Agent执行前规划阶段的安全干预，提出了AuraGen合成数据引擎和Safiron基础护栏模型。该框架通过合成良性轨迹和注入风险数据来训练护栏，使其能够在执行前检测风险、分配类型并生成理由。实验表明，该方法在涵盖多种工具和分支轨迹的基准测试中表现出一致的性能提升。

---

## #31 — Immune: Improving Safety Against Jailbreaks in Multi-modal LLMs via Inference-Time Alignment

`A` Score: 8.19 | 2024-11-27

**Authors:** Soumya Suvra Ghosal, Souradip Chakraborty, Vaibhav Singh, Tianrui Guan, Mengdi Wang, Alvaro Velasquez et al. (10 total)

**Categories:** cs.CR, cs.AI, cs.LG

**Scores:** Citation: 9.03 | Influential: 9.02 | Venue: 5.00 | Author: 8.84 | Recency: 5.00

**Links:** [arXiv](https://arxiv.org/abs/2411.18688) | [PDF](https://arxiv.org/pdf/2411.18688)

> 本文提出了Immune，一种针对多模态大语言模型的推理时防御框架，利用安全奖励模型通过控制解码来防御越狱攻击。该框架通过数学分析证明了其有效性，并在多种越狱基准测试中显著降低了攻击成功率，同时保持了模型的原始能力。

---

## #32 — Probe before You Talk: Towards Black-box Defense against Backdoor Unalignment for Large Language Models

`A` Score: 8.17 | 2025-06-19

**Authors:** Biao Yi, Tiansheng Huang, Sishuo Chen, Tong Li, Zheli Liu, Zhixuan Chu et al. (7 total)

**Categories:** cs.CR, cs.CL

**Scores:** Citation: 9.66 | Influential: 7.81 | Venue: 10.00 | Author: 3.78 | Recency: 7.00

**Links:** [arXiv](https://arxiv.org/abs/2506.16447) | [PDF](https://arxiv.org/pdf/2506.16447)

> 本文提出了BEAT，一种针对大语言模型后门未对齐攻击的黑盒防御方法。该方法基于“探测连接效应”，通过测量连接输入前后探测输出分布的失真程度来识别触发样本，从而在推理时停用后门。BEAT从触发对拒绝信号的影响入手，有效解决了样本依赖目标的挑战，克服了黑盒访问限制，提供了有效的防御机制。

---

## #33 — LLM Jailbreak Detection for (Almost) Free!

`A` Score: 8.16 | 2025-09-18

**Authors:** Guorui Chen, Yifan Xia, Xiaojun Jia, Zhijiang Li, Philip Torr, Jindong Gu

**Categories:** cs.CR, cs.AI, cs.CL

**Scores:** Citation: 7.69 | Influential: 9.02 | Venue: 10.00 | Author: 7.99 | Recency: 7.00

**Links:** [arXiv](https://arxiv.org/abs/2509.14558) | [PDF](https://arxiv.org/pdf/2509.14558)

> 本文提出了一种几乎零计算成本的越狱检测方法（FJD），利用越狱提示词与良性提示词在输出分布上的差异进行检测。该方法通过在输入前添加肯定指令并调整温度缩放，结合虚拟指令学习，有效区分恶意提示词，且不增加额外的推理开销。

---

## #34 — Safety Reasoning with Guidelines

`A` Score: 8.15 | 2025-02-06

**Authors:** Haoyu Wang, Zeyu Qin, Li Shen, Xueqian Wang, Dacheng Tao, Minhao Cheng

**Categories:** cs.LG, cs.AI, cs.CL

**Scores:** Citation: 7.64 | Influential: 9.02 | Venue: 10.00 | Author: 9.36 | Recency: 5.00

**Links:** [arXiv](https://arxiv.org/abs/2502.04040) | [PDF](https://arxiv.org/pdf/2502.04040)

> 研究质疑了OOD攻击是否本质上超越了普通拒绝训练的能力，评估显示随着N增加，安全性显著改善，表明模型拥有足够的潜在安全知识但RT无法在OOD场景下一致提取。作者提出训练模型对每个查询执行安全推理，合成与指定指南一致的推理监督，鼓励模型进行更深入的推理，明确提取和利用潜在安全知识。实验证明该方法显著提高了模型对OOD攻击的泛化能力。

---

## #35 — Meta SecAlign: A Secure Foundation LLM Against Prompt Injection Attacks

`A` Score: 8.15 | 2025-07-03

**Authors:** Sizhe Chen, Arman Zharmagambetov, David Wagner, Chuan Guo

**Categories:** cs.CR, cs.AI

**Scores:** Citation: 9.88 | Influential: 9.96 | Venue: 2.00 | Author: 5.40 | Recency: 7.00

**Links:** [arXiv](https://arxiv.org/abs/2507.02735) | [PDF](https://arxiv.org/pdf/2507.02735)

> 本文介绍了Meta SecAlign，这是首个具有内置模型级防御功能的完全开源大语言模型，旨在抵御提示注入攻击。作者提供了详细的训练配方，并在广泛的效用和安全基准上进行了评估，证明该模型在未见过的下游任务中表现出商业级的安全性能。该模型在效用与安全的权衡上设立了新标杆，优于多个专有模型。

---

## #36 — Separate the Wheat from the Chaff: A Post-Hoc Approach to Safety Re-Alignment for Fine-Tuned Language Models

`A` Score: 8.15 | 2024-12-15

**Authors:** Di Wu, Xin Lu, Yanyan Zhao, Bing Qin

**Categories:** cs.CL

**Scores:** Citation: 8.42 | Influential: 7.81 | Venue: 10.00 | Author: 8.65 | Recency: 5.00

**Links:** [arXiv](https://arxiv.org/abs/2412.11041) | [PDF](https://arxiv.org/pdf/2412.11041)

> 本文提出了 IRR 方法，旨在解决微调过程往往会破坏 LLM 安全对齐的问题。该方法通过识别并移除微调模型中的不安全 delta 参数，同时重新校准保留的参数，实现事后安全重新对齐。实验表明，IRR 在保持下游任务性能的同时，显著提升了模型在有害查询和越狱攻击等安全基准上的表现，有效恢复了微调后的安全性。

---

## #37 — Oyster-I: Beyond Refusal -- Constructive Safety Alignment for Responsible Language Models

`A` Score: 8.13 | 2025-09-02

**Authors:** Ranjie Duan, Jiexi Liu, Xiaojun Jia, Shiji Zhao, Ruoxi Cheng, Fengxiang Wang et al. (30 total)

**Categories:** cs.AI, cs.CL, cs.CY

**Scores:** Citation: 9.35 | Influential: 7.81 | Venue: 2.00 | Author: 9.71 | Recency: 7.00

**Links:** [arXiv](https://arxiv.org/abs/2509.01909) | [PDF](https://arxiv.org/pdf/2509.01909)

> 本文提出了建设性安全对齐（CSA）范式，旨在超越传统的拒绝机制，主动引导处于心理困境的用户走向安全。Oyster-I模型通过博弈论预测用户反应并结合细粒度风险边界发现，在保持高通用能力的同时，实现了对恶意攻击的防御和对脆弱用户的积极引导。

---

## #38 — Why Not Act on What You Know? Unleashing Safety Potential of LLMs via Self-Aware Guard Enhancement

`A` Score: 8.12 | 2025-05-17

**Authors:** Peng Ding, Jun Kuang, Zongyu Wang, Xuezhi Cao, Xunliang Cai, Jiajun Chen et al. (7 total)

**Categories:** cs.CL

**Scores:** Citation: 6.99 | Influential: 9.39 | Venue: 10.00 | Author: 9.34 | Recency: 7.00

**Links:** [arXiv](https://arxiv.org/abs/2505.12060) | [PDF](https://arxiv.org/pdf/2505.12060)

> 本文指出了大语言模型（LLMs）在安全防御中的一个关键缺口：尽管它们擅长检测越狱提示，但在直接处理这些输入时仍可能生成不安全回复。为此，作者提出了SAGE（自感知守卫增强），这是一种无需训练的防御策略，旨在将LLMs强大的安全判别能力与其较弱的安全生成能力对齐。SAGE通过判别分析和判别响应两个核心模块，利用灵活的安全判别指令显著提升了模型对复杂越狱攻击的抵御能力，在多种模型上实现了平均99%的防御成功率。

---

## #39 — WebGuard: Building a Generalizable Guardrail for Web Agents

`A` Score: 8.09 | 2025-07-18

**Authors:** Boyuan Zheng, Zeyi Liao, Scott Salisbury, Zeyuan Liu, Michael Lin, Qinyuan Zheng et al. (11 total)

**Categories:** cs.AI, cs.CL, cs.CV

**Scores:** Citation: 8.73 | Influential: 9.02 | Venue: 2.00 | Author: 9.71 | Recency: 7.00

**Links:** [arXiv](https://arxiv.org/abs/2507.14293) | [PDF](https://arxiv.org/pdf/2507.14293)

> 本文介绍了WebGuard，第一个全面的数据集，用于评估网络智能体行动风险并开发真实在线环境护栏。该数据集包含来自22个不同领域193个网站的4,939个人类标注行动，使用三层风险模式(安全、低风险、高风险)分类。实验显示，前沿LLM在预测行动结果准确率不足60%，高风险行动召回率不足60%，突显了缺乏专用护栏的风险。作者通过WebGuard微调专用护栏模型，在多种泛化设置下评估，发现微调的Qwen2.5VL-7B模型显著提高了性能。

---

## #40 — AgentDoG: A Diagnostic Guardrail Framework for AI Agent Safety and Security

`A` Score: 8.03 | 2026-01-26

**Authors:** Dongrui Liu, Qihan Ren, Chen Qian, Shuai Shao, Yuejin Xie, Yu Li et al. (43 total)

**Categories:** cs.AI, cs.CC, cs.CL

**Scores:** Citation: 9.46 | Influential: 7.81 | Venue: 2.00 | Author: 6.75 | Recency: 10.00

**Links:** [arXiv](https://arxiv.org/abs/2601.18491) | [PDF](https://arxiv.org/pdf/2601.18491)

> 本文提出了AgentDoG，一个用于AI Agent安全和保障的诊断护栏框架，旨在解决现有护栏模型缺乏Agent风险感知和透明度的问题。基于统一的三维风险分类法，AgentDoG能够对Agent轨迹进行细粒度监控，并诊断不安全行为的根本原因，提供超越二元标签的可追溯性。实验表明，该框架在复杂交互场景中实现了最先进的Agent安全审核性能。

---

## #41 — Analysing the Safety Pitfalls of Steering Vectors

`A` Score: 8.02 | 2026-03-25

**Authors:** Yuxiao Li, Alina Fastowski, Efstratios Zaradoukas, Bardh Prenkaj, Gjergji Kasneci

**Categories:** cs.CR, cs.CL

**Scores:** Citation: 8.50 | Influential: 7.81 | Venue: 2.00 | Author: 9.52 | Recency: 10.00

**Links:** [arXiv](https://arxiv.org/abs/2603.24543) | [PDF](https://arxiv.org/pdf/2603.24543)

> 本文系统性地审计了广泛使用的激活引导方法（CAA）在安全性方面的隐患，评估了引导向量对越狱攻击成功率的影响。研究发现，引导向量会显著改变模型的攻击成功率，根据目标行为的不同，可能大幅增加或降低成功率，这归因于引导向量与拒绝行为潜在方向的重叠。这一发现揭示了LLM中可控性与安全性之间的权衡，强调了在行为引导技术中考虑安全因素的必要性。

---

## #42 — InjecGuard: Benchmarking and Mitigating Over-defense in Prompt Injection Guardrail Models

`A` Score: 8.01 | 2024-10-30

**Authors:** Hao Li, Xiaogeng Liu

**Categories:** cs.CL, cs.AI, cs.CR

**Scores:** Citation: 9.16 | Influential: 9.92 | Venue: 2.00 | Author: 7.99 | Recency: 5.00

**Links:** [arXiv](https://arxiv.org/abs/2410.22770) | [PDF](https://arxiv.org/pdf/2410.22770)

> 本文针对提示词护栏模型存在的过度防御问题，提出了包含 NotInject 数据集和 InjecGuard 模型的解决方案。InjecGuard 采用了一种名为 MOF 的新颖训练策略，有效减少了模型对触发词的偏差，从而降低了误报率。实验结果显示，InjecGuard 在多个基准测试中超越了现有最佳模型，为检测提示注入攻击提供了强大的开源工具。

---

## #43 — Safety at Scale: A Comprehensive Survey of Large Model and Agent Safety

`A` Score: 7.99 | 2025-02-02

**Authors:** Xingjun Ma, Yifeng Gao, Yixu Wang, Ruofan Wang, Xin Wang, Ye Sun et al. (48 total)

**Categories:** cs.CR, cs.AI, cs.CL

**Scores:** Citation: 9.43 | Influential: 7.81 | Venue: 2.00 | Author: 9.89 | Recency: 5.00

**Links:** [arXiv](https://arxiv.org/abs/2502.05206) | [PDF](https://arxiv.org/pdf/2502.05206)

> 这篇论文系统综述了大型模型和Agent的安全研究现状，涵盖了视觉基础模型、大型语言模型、视觉语言模型、扩散模型等多种模型类型。论文提出了大型模型面临的安全威胁综合分类法，包括对抗攻击等，并分析了这些模型的鲁棒性、可靠性和伦理问题。这项研究为理解和应对大规模AI系统部署中的安全挑战提供了系统性框架，对促进AI安全领域的进一步发展具有重要意义。

---

## #44 — Proof-of-Guardrail in AI Agents and What (Not) to Trust from It

`A` Score: 7.99 | 2026-03-06

**Authors:** Xisen Jin, Michael Duan, Qin Lin, Aaron Chan, Zhenglun Chen, Junyi Du et al. (7 total)

**Categories:** cs.CR, cs.AI, cs.CL

**Scores:** Citation: 8.87 | Influential: 9.39 | Venue: 2.00 | Author: 6.17 | Recency: 10.00

**Links:** [arXiv](https://arxiv.org/abs/2603.05786) | [PDF](https://arxiv.org/pdf/2603.05786)

> 本文提出了proof-of-guardrail系统，利用可信执行环境（TEE）生成密码学证明，验证Agent响应是在特定开源护栏执行后生成的。该系统在保证护栏执行完整性的同时保护了开发者隐私，但也指出了恶意开发者可能主动破坏护栏的欺骗风险，为验证安全声明提供了新思路。

---

## #45 — Safety Alignment via Constrained Knowledge Unlearning

`A` Score: 7.96 | 2025-05-24

**Authors:** Zesheng Shi, Yucheng Zhou, Jing Li

**Categories:** cs.CL, cs.AI

**Scores:** Citation: 7.04 | Influential: 9.02 | Venue: 10.00 | Author: 8.55 | Recency: 7.00

**Links:** [arXiv](https://arxiv.org/abs/2505.18588) | [PDF](https://arxiv.org/pdf/2505.18588)

> 本文提出了约束知识遗忘（CKU）策略，通过评分神经元定位有用知识并在遗忘过程中修剪其梯度。该方法在有效缓解有害内容的同时保留了有价值知识，在不损害整体性能的前提下显著增强了模型安全性，为安全对齐和模型知识编辑提供了见解。

---

## #46 — Token Highlighter: Inspecting and Mitigating Jailbreak Prompts for Large Language Models

`A` Score: 7.93 | 2024-12-24

**Authors:** Xiaomeng Hu, Pin-Yu Chen, Tsung-Yi Ho

**Categories:** cs.CR

**Scores:** Citation: 7.64 | Influential: 9.58 | Venue: 10.00 | Author: 7.15 | Recency: 5.00

**Links:** [arXiv](https://arxiv.org/abs/2412.18171) | [PDF](https://arxiv.org/pdf/2412.18171)

> 针对大语言模型的越狱攻击，本文提出了Token Highlighter防御方法。该方法引入“肯定损失”来衡量模型回答意愿，利用梯度定位关键攻击Token，并通过“软移除”技术缩小其嵌入表示，从而在不影响良性问题性能的前提下有效防御多种越狱攻击，且具有低成本和可解释性。

---

## #47 — The VLLM Safety Paradox: Dual Ease in Jailbreak Attack and Defense

`A` Score: 7.90 | 2024-11-13

**Authors:** Yangyang Guo, Fangkai Jiao, Liqiang Nie, Mohan Kankanhalli

**Categories:** cs.CR, cs.CV

**Scores:** Citation: 8.68 | Influential: 9.02 | Venue: 2.00 | Author: 9.96 | Recency: 5.00

**Links:** [arXiv](https://arxiv.org/abs/2411.08410) | [PDF](https://arxiv.org/pdf/2411.08410)

> 本文探讨了视觉大语言模型在越狱攻击与防御中表现出的双重高性能悖论，分析了视觉输入导致的脆弱性以及现有防御机制中存在的“过度谨慎”问题。作者提出了LLM-Pipeline方法，利用LLM的护栏作为有效检测器，以提升VLLM的安全性。

---

## #48 — LLMZ+: Contextual Prompt Whitelist Principles for Agentic LLMs

`A` Score: 7.86 | 2025-09-23

**Authors:** Tom Pawelek, Raj Patel, Charlotte Crowell, Noorbakhsh Amiri, Sudip Mittal, Shahram Rahimi et al. (7 total)

**Categories:** cs.AI

**Scores:** Citation: 7.19 | Influential: 9.02 | Venue: 10.00 | Author: 7.43 | Recency: 7.00

**Links:** [arXiv](https://arxiv.org/abs/2509.18557) | [PDF](https://arxiv.org/pdf/2509.18557)

> 针对智能体大语言模型面临的安全风险，本文提出了LLMZ+防御框架。不同于传统的恶意意图检测方法，LLMZ+实施基于上下文的提示白名单机制，仅允许符合预定义用例的安全消息与模型交互。该方法简化了安全框架，增强了长期韧性，并有效抵御了常见的越狱攻击。

---

## #49 — RSafe: Incentivizing proactive reasoning to build robust and adaptive LLM safeguards

`A` Score: 7.85 | 2025-06-09

**Authors:** Jingnan Zheng, Xiangtian Ji, Yijun Lu, Chenhang Cui, Weixiang Zhao, Gelei Deng et al. (9 total)

**Categories:** cs.AI

**Scores:** Citation: 8.95 | Influential: 7.81 | Venue: 2.00 | Author: 9.09 | Recency: 7.00

**Links:** [arXiv](https://arxiv.org/abs/2506.07736) | [PDF](https://arxiv.org/pdf/2506.07736)

> 针对现有护栏模型依赖人工数据且难以应对分布外威胁的问题，本文提出了RSafe自适应推理护栏。它通过策略引导的逐步推理和基于规则的强化学习，使模型内化安全原则，从而有效防御未见过的越狱攻击。

---

## #50 — Secure Tug-of-War (SecTOW): Iterative Defense-Attack Training with Reinforcement Learning for Multimodal Model Security

`A` Score: 7.85 | 2025-07-29

**Authors:** Muzhi Dai, Shixuan Liu, Zhiyuan Zhao, Junyu Gao, Hao Sun, Xuelong Li

**Categories:** cs.CR, cs.AI

**Scores:** Citation: 8.52 | Influential: 9.02 | Venue: 5.00 | Author: 6.75 | Recency: 7.00

**Links:** [arXiv](https://arxiv.org/abs/2507.22037) | [PDF](https://arxiv.org/pdf/2507.22037)

> 本文提出了SecTOW方法，一种基于强化学习的迭代防御-攻击训练框架，用于增强多模态大语言模型的安全性。该方法通过防御者和辅助攻击者的迭代对抗，利用攻击者发现的漏洞扩展越狱数据并训练防御者，有效解决了训练样本稀缺和过度拒绝无害输入的问题。

---

## #51 — Granite Guardian

`B` Score: 7.84 | 2024-12-10

**Authors:** Inkit Padhi, Manish Nagireddy, Giandomenico Cornacchia, Subhajit Chaudhury, Tejaswini Pedapati, Pierre Dognin et al. (23 total)

**Categories:** cs.CL

**Scores:** Citation: 8.63 | Influential: 9.02 | Venue: 2.00 | Author: 9.71 | Recency: 5.00

**Links:** [arXiv](https://arxiv.org/abs/2412.07724) | [PDF](https://arxiv.org/pdf/2412.07724)

> 本文介绍了Granite Guardian模型套件，旨在为提示词和响应提供全面的风险检测，涵盖社会偏见、暴力、越狱及RAG幻觉等多种风险维度。该模型结合人类标注和合成数据训练，在有害内容和幻觉基准测试中表现出优异的泛化能力和竞争力，作为开源工具促进了负责任的AI开发。

---

## #52 — LLMs Encode Harmfulness and Refusal Separately

`B` Score: 7.83 | 2025-07-16

**Authors:** Jiachen Zhao, Jing Huang, Zhengxuan Wu, David Bau, Weiyan Shi

**Categories:** cs.CL

**Scores:** Citation: 9.34 | Influential: 9.02 | Venue: 2.00 | Author: 6.17 | Recency: 7.00

**Links:** [arXiv](https://arxiv.org/abs/2507.11878) | [PDF](https://arxiv.org/pdf/2507.11878)

> 本文识别了LLMs安全机制中的一个新维度——危害性，它在内部被编码为与拒绝分离的概念。研究发现存在一个与拒绝方向不同的危害性方向，沿着危害性方向引导可使LLM将无害指令解释为有害，而沿着拒绝方向引导直接引发拒绝响应而不改变危害性判断。研究还发现某些越狱方法通过减少拒绝信号而不改变模型对危害性的内部信念来工作。基于这些见解，作者提出了'潜在护栏'(Latent Guard)，利用模型的潜在危害性表示作为检测不安全输入和减少过度拒绝的内在 safeguard。

---

## #53 — To Protect the LLM Agent Against the Prompt Injection Attack with Polymorphic Prompt

`B` Score: 7.82 | 2025-06-06

**Authors:** Zhilong Wang, Neha Nagaraja, Lan Zhang, Hayretdin Bahsi, Pawan Patil, Peng Liu

**Categories:** cs.CR, cs.AI

**Scores:** Citation: 8.78 | Influential: 9.02 | Venue: 2.00 | Author: 7.80 | Recency: 7.00

**Links:** [arXiv](https://arxiv.org/abs/2506.05739) | [PDF](https://arxiv.org/pdf/2506.05739)

> 本文提出了一种轻量级防御机制PPA，通过动态改变系统提示词的结构来防止提示注入攻击。该方法基于攻击者需要猜测并破坏提示词结构这一洞察，有效阻止了攻击者的预测，从而在不牺牲性能的前提下增强了安全性。实验证明PPA能有效抵御现有攻击。

---

## #54 — Reasoning as an Adaptive Defense for Safety

`B` Score: 7.80 | 2025-07-01

**Authors:** Taeyoun Kim, Fahim Tajwar, Aditi Raghunathan, Aviral Kumar

**Categories:** cs.LG, cs.AI

**Scores:** Citation: 9.04 | Influential: 9.77 | Venue: 2.00 | Author: 5.88 | Recency: 7.00

**Links:** [arXiv](https://arxiv.org/abs/2507.00971) | [PDF](https://arxiv.org/pdf/2507.00971)

> 本文提出了TARS方法，利用强化学习训练模型通过思维链推理安全性，从而增强对安全漏洞的鲁棒性。该方法通过平衡安全性与任务完成的奖励信号，使模型在模糊查询上分配更多计算资源，并学会更好地区分安全与不安全提示。实验表明，TARS模型在对抗白盒和黑盒越狱攻击方面表现出更强的防御能力。

---

## #55 — The Hidden Dimensions of LLM Alignment: A Multi-Dimensional Analysis of Orthogonal Safety Directions

`B` Score: 7.79 | 2025-02-13

**Authors:** Wenbo Pan, Zhichao Liu, Qiguang Chen, Xiangyang Zhou, Haining Yu, Xiaohua Jia

**Categories:** cs.CL, cs.AI

**Scores:** Citation: 8.54 | Influential: 9.02 | Venue: 10.00 | Author: 4.27 | Recency: 5.00

**Links:** [arXiv](https://arxiv.org/abs/2502.09674) | [PDF](https://arxiv.org/pdf/2502.09674)

> 研究揭示LLM安全对齐行为由多维方向共同控制，而非单一方向。通过分析Llama 3 8B的安全微调过程，发现一个主导方向控制拒绝行为，多个较小方向代表不同可解释特征。研究还显示移除有害查询中的特定触发词可绕过安全能力，从多维度视角揭示了安全对齐的脆弱性机制，为理解LLM安全行为提供新见解。

---

## #56 — Large Reasoning Models Learn Better Alignment from Flawed Thinking

`B` Score: 7.78 | 2025-10-01

**Authors:** ShengYun Peng, Eric Smith, Ivan Evtimov, Song Jiang, Pin-Yu Chen, Hongyuan Zhan et al. (10 total)

**Categories:** cs.LG

**Scores:** Citation: 8.53 | Influential: 7.81 | Venue: 2.00 | Author: 9.83 | Recency: 7.00

**Links:** [arXiv](https://arxiv.org/abs/2510.00938) | [PDF](https://arxiv.org/pdf/2510.00938)

> 大型推理模型在生成思维链时容易受到有缺陷前提的影响，缺乏对安全对齐的批判性推理能力。本文提出了 RECAP 方法，通过混合合成生成的反对抗思维链预填充和标准提示，显式地教导模型覆盖有缺陷的推理轨迹并重新路由至安全有益的响应。该方法在不增加额外训练成本的情况下，显著提升了模型的安全性和越狱鲁棒性，同时减少了过度拒绝并保留了核心推理能力。

---

## #57 — Why LLM Safety Guardrails Collapse After Fine-tuning: A Similarity Analysis Between Alignment and Fine-tuning Datasets

`B` Score: 7.77 | 2025-06-05

**Authors:** Lei Hsiung, Tianyu Pang, Yung-Chen Tang, Linyue Song, Tsung-Yi Ho, Pin-Yu Chen et al. (7 total)

**Categories:** cs.CR, cs.CL, cs.LG

**Scores:** Citation: 8.88 | Influential: 9.02 | Venue: 2.00 | Author: 7.15 | Recency: 7.00

**Links:** [arXiv](https://arxiv.org/abs/2506.05346) | [PDF](https://arxiv.org/pdf/2506.05346)

> 本文通过分析上游对齐数据与下游微调数据之间的表示相似性，揭示了微调导致安全护栏崩溃的原因。实验表明，两类数据的高相似性会显著削弱模型的安全性，而低相似性则能增强鲁棒性。该发现强调了上游数据集设计在构建持久安全护栏中的关键作用。

---

## #58 — Large Language Models Encode Semantics and Alignment in Linearly Separable Representations

`B` Score: 7.76 | 2025-07-13

**Authors:** Baturay Saglam, Paul Kassianik, Blaine Nelson, Sajana Weerawardhena, Yaron Singer, Amin Karbasi

**Categories:** cs.CL, cs.LG

**Scores:** Citation: 7.86 | Influential: 9.02 | Venue: 10.00 | Author: 4.79 | Recency: 7.00

**Links:** [arXiv](https://arxiv.org/abs/2507.09709) | [PDF](https://arxiv.org/pdf/2507.09709)

> 本文通过大规模实证研究发现，LLMs的高级语义信息一致存在于跨领域的低维子空间中，形成线性可分离表示，尤其在深层和引发结构化推理的提示下更明显。基于此，作者训练MLP探针作为轻量级潜在空间护栏，显著提高对恶意查询和提示注入的拒绝率，为几何感知安全工具提供新思路。

---

## #59 — SaRO: Enhancing LLM Safety through Reasoning-based Alignment

`B` Score: 7.73 | 2025-04-13

**Authors:** Yutao Mou, Yuxiao Luo, Shikun Zhang, Wei Ye

**Categories:** cs.CL

**Scores:** Citation: 9.14 | Influential: 7.81 | Venue: 2.00 | Author: 9.01 | Recency: 5.00

**Links:** [arXiv](https://arxiv.org/abs/2504.09420) | [PDF](https://arxiv.org/pdf/2504.09420)

> 针对大模型安全对齐中面临的泛化不足和过度拒绝两大挑战，本文提出了基于推理优化的SaRO框架。该框架包含推理风格预热和安全推理过程优化两个阶段，旨在使模型内化长链推理并进行安全反思，从而有效提升对新型越狱攻击的防御能力。

---

## #60 — Steering MoE LLMs via Expert (De)Activation

`B` Score: 7.73 | 2025-09-11

**Authors:** Mohsen Fayyaz, Ali Modarressi, Hanieh Deilamsalehy, Franck Dernoncourt, Ryan Rossi, Trung Bui et al. (8 total)

**Categories:** cs.CL, cs.LG

**Scores:** Citation: 8.76 | Influential: 9.39 | Venue: 2.00 | Author: 6.75 | Recency: 7.00

**Links:** [arXiv](https://arxiv.org/abs/2509.09660) | [PDF](https://arxiv.org/pdf/2509.09660)

> 本文提出了 SteerMoE 框架，通过检测并控制混合专家模型中与特定行为（如安全性）相关的专家，在推理阶段实现对模型行为的引导。实验表明，该方法无需微调即可显著提升模型的安全性和忠实度，同时也揭示了 MoE 架构中存在的独特安全漏洞。

---

## #61 — Internal Activation Revision: Safeguarding Vision Language Models Without Parameter Update

`B` Score: 7.67 | 2025-01-24

**Authors:** Qing Li, Jiahui Geng, Zongxiong Chen, Kun Song, Lei Ma, Fakhri Karray

**Categories:** cs.LG, cs.AI, cs.CL

**Scores:** Citation: 8.44 | Influential: 7.81 | Venue: 10.00 | Author: 5.40 | Recency: 5.00

**Links:** [arXiv](https://arxiv.org/abs/2501.16378) | [PDF](https://arxiv.org/pdf/2501.16378)

> 视觉语言模型(VLMs)比其基础大语言模型更容易生成有害内容，研究发现图像集成会显著改变模型内部激活状态，导致安全对齐失效。本文提出内部激活修订方法，在生成过程中动态修订激活状态，引导模型输出更安全内容，该方法在层和头级别提供不同粒度的控制，并探索了构建正负示例的三种策略。

---

## #62 — Online Learning Defense against Iterative Jailbreak Attacks via Prompt Optimization

`B` Score: 7.66 | 2025-10-19

**Authors:** Masahiro Kaneko, Zeerak Talat, Timothy Baldwin

**Categories:** cs.CL

**Scores:** Citation: 6.84 | Influential: 7.81 | Venue: 10.00 | Author: 8.79 | Recency: 7.00

**Links:** [arXiv](https://arxiv.org/abs/2510.17006) | [PDF](https://arxiv.org/pdf/2510.17006)

> 该研究提出了一种基于在线学习的防御框架，通过动态更新防御策略来对抗迭代越狱攻击。利用强化学习优化提示词，并引入 Past-Direction Gradient Damping 抑制过拟合，该方法在有效拒绝有害提示的同时，显著提升了对无害任务的响应质量。

---

## #63 — Improved Representation Steering for Language Models

`B` Score: 7.65 | 2025-05-27

**Authors:** Zhengxuan Wu, Qinan Yu, Aryaman Arora, Christopher D. Manning, Christopher Potts

**Categories:** cs.CL

**Scores:** Citation: 8.07 | Influential: 9.02 | Venue: 2.00 | Author: 8.79 | Recency: 7.00

**Links:** [arXiv](https://arxiv.org/abs/2505.20809) | [PDF](https://arxiv.org/pdf/2505.20809)

> 本文提出了无参考偏好转向（RePS），一种通过双向偏好优化目标来改进模型表示转向的方法。RePS联合进行概念引导和抑制，在Gemma模型上优于现有的语言建模目标方法，并显著缩小了与提示工程的差距。该方法在抑制任务中表现出色，且对基于提示的越狱攻击具有鲁棒性，提供了可解释且稳健的控制替代方案。

---

## #64 — SAFEPATH: Preventing Harmful Reasoning in Chain-of-Thought via Early Alignment

`B` Score: 7.63 | 2025-05-20

**Authors:** Wonje Jeung, Sangyeon Yoon, Minsuk Kahng, Albert No

**Categories:** cs.AI, cs.CL

**Scores:** Citation: 8.61 | Influential: 7.81 | Venue: 2.00 | Author: 8.65 | Recency: 7.00

**Links:** [arXiv](https://arxiv.org/abs/2505.14667) | [PDF](https://arxiv.org/pdf/2505.14667)

> 本文提出了SAFEPATH，一种轻量级对齐方法，通过微调让大型推理模型在推理开始时输出安全引导词。该方法在有效减少有害输出和阻断越狱的同时，保持了模型的推理深度，且计算成本极低。

---

## #65 — FalseReject: A Resource for Improving Contextual Safety and Mitigating Over-Refusals in LLMs via Structured Reasoning

`B` Score: 7.62 | 2025-05-12

**Authors:** Zhehao Zhang, Weijie Xu, Fanyou Wu, Chandan K. Reddy

**Categories:** cs.CL, cs.AI

**Scores:** Citation: 9.41 | Influential: 7.81 | Venue: 2.00 | Author: 6.17 | Recency: 7.00

**Links:** [arXiv](https://arxiv.org/abs/2505.08054) | [PDF](https://arxiv.org/pdf/2505.08054)

> 本文介绍了FalseReject资源，包含16k个看似有毒的查询及结构化响应，旨在解决LLMs安全对齐导致的过度拒绝问题。作者提出了一种图知情的对抗性多智能体交互框架来生成复杂提示，并构建了针对标准和推理模型的训练数据集。实验表明，使用FalseReject进行监督微调能显著减少不必要的拒绝，同时不损害整体安全性和语言能力。

---

## #66 — Rethinking Jailbreak Detection of Large Vision Language Models with Representational Contrastive Scoring

`B` Score: 7.59 | 2025-12-12

**Authors:** Peichun Hua, Hao Li, Shanghao Shi, Zhiyuan Yu, Ning Zhang

**Categories:** cs.CR, cs.AI, cs.CL

**Scores:** Citation: 8.69 | Influential: 7.81 | Venue: 2.00 | Author: 6.75 | Recency: 9.00

**Links:** [arXiv](https://arxiv.org/abs/2512.12069) | [PDF](https://arxiv.org/pdf/2512.12069)

> 本文针对大型视觉语言模型（LVLM）面临的多模态越狱攻击，提出了表征对比评分（RCS）框架，利用模型内部表征中最强的安全信号进行防御。该方法通过学习轻量级投影，在安全关键层中最大程度地分离良性和恶意输入，从而产生强大的对比分数以区分真正的恶意意图和单纯的新颖性。实验表明，MCD 和 KCD 实例在针对未见攻击类型的评估协议中实现了最先进的性能，证明了通过适当的内部表征应用简单统计方法即可实现有效的越狱检测。

---

## #67 — Shaping the Safety Boundaries: Understanding and Defending Against Jailbreaks in Large Language Models

`B` Score: 7.59 | 2024-12-22

**Authors:** Lang Gao, Jiahui Geng, Xiangliang Zhang, Preslav Nakov, Xiuying Chen

**Categories:** cs.CL

**Scores:** Citation: 8.03 | Influential: 9.02 | Venue: 2.00 | Author: 9.83 | Recency: 5.00

**Links:** [arXiv](https://arxiv.org/abs/2412.17034) | [PDF](https://arxiv.org/pdf/2412.17034)

> 本文通过分析七种越狱方法，引入了“安全边界”概念，发现越狱会将有害激活移至边界外。基于此，作者提出了激活边界防御（ABD），通过贝叶斯优化自适应地约束低层和中层的激活，在保持模型通用能力的同时有效防御各种形式的越狱攻击，平均防御成功率超过98%。

---

## #68 — T2VShield: Model-Agnostic Jailbreak Defense for Text-to-Video Models

`B` Score: 7.58 | 2025-04-22

**Authors:** Siyuan Liang, Jiayang Liu, Jiecheng Zhai, Tianmeng Fang, Rongcheng Tu, Aishan Liu et al. (8 total)

**Categories:** cs.CR, cs.LG

**Scores:** Citation: 8.61 | Influential: 7.81 | Venue: 5.00 | Author: 7.62 | Recency: 5.00

**Links:** [arXiv](https://arxiv.org/abs/2504.15512) | [PDF](https://arxiv.org/pdf/2504.15512)

> 本文提出了T2VShield，一个针对文生视频模型的模型无关越狱防御框架。该方法通过基于推理和多模态检索的提示重写机制清理恶意输入，并利用多范围检测模块捕捉跨时间和模态的不一致性。实验显示，该框架能显著降低越狱成功率，且无需访问模型内部参数，适用于开源和闭源系统。

---

## #69 — A Closer Look at System Prompt Robustness

`B` Score: 7.56 | 2025-02-15

**Authors:** Norman Mu, Jonathan Lu, Michael Lavery, David Wagner

**Categories:** cs.CL, cs.AI

**Scores:** Citation: 9.19 | Influential: 9.58 | Venue: 2.00 | Author: 5.40 | Recency: 5.00

**Links:** [arXiv](https://arxiv.org/abs/2502.12197) | [PDF](https://arxiv.org/pdf/2502.12197)

> 本研究聚焦系统提示的鲁棒性问题，发现LLM在面对冲突或对抗性输入时常忽略安全护栏。作者基于真实应用场景创建评估和微调数据集，实验表明使用真实微调数据和推理时干预可显著提升模型性能。分析OpenAI和DeepSeek最新模型显示安全对齐存在不均衡改进，当前技术仍无法确保系统提示的完全鲁棒性。

---

## #70 — Reimagining Safety Alignment with An Image

`B` Score: 7.55 | 2025-11-01

**Authors:** Yifan Xia, Guorui Chen, Wenqian Yu, Zhijiang Li, Philip Torr, Jindong Gu

**Categories:** cs.AI, cs.CR

**Scores:** Citation: 5.88 | Influential: 9.02 | Venue: 10.00 | Author: 7.99 | Recency: 9.00

**Links:** [arXiv](https://arxiv.org/abs/2511.00509) | [PDF](https://arxiv.org/pdf/2511.00509)

> 提出了Magic Image，一种基于优化的视觉提示框架，用于增强多模态大模型的安全性并减少过度拒绝。该方法通过优化图像提示词，使单一模型无需参数更新即可适应不同的价值体系，在保持模型性能的同时实现了更好的安全与效果平衡。

---

## #71 — X-Guard: Multilingual Guard Agent for Content Moderation

`B` Score: 7.53 | 2025-04-11

**Authors:** Bibek Upadhayay, Vahid Behzadan, Ph. D

**Categories:** cs.CR, cs.AI

**Scores:** Citation: 8.22 | Influential: 9.02 | Venue: 2.00 | Author: 8.84 | Recency: 5.00

**Links:** [arXiv](https://arxiv.org/abs/2504.08848) | [PDF](https://arxiv.org/pdf/2504.08848)

> 针对现有安全系统在多语言环境下的脆弱性，本文提出了透明的多语言安全智能体X-Guard。该方法通过构建大规模多语言数据集和采用两阶段架构，有效防御了低资源语言和代码混合攻击，并提供了可解释的决策过程以增强信任。

---

## #72 — Monitoring Decomposition Attacks in LLMs with Lightweight Sequential Monitors

`B` Score: 7.49 | 2025-06-12

**Authors:** Chen Yueh-Han, Nitish Joshi, Yulin Chen, Maksym Andriushchenko, Rico Angell, He He

**Categories:** cs.CR, cs.AI

**Scores:** Citation: 8.57 | Influential: 9.02 | Venue: 2.00 | Author: 6.17 | Recency: 7.00

**Links:** [arXiv](https://arxiv.org/abs/2506.10949) | [PDF](https://arxiv.org/pdf/2506.10949)

> 本文针对分解攻击（将恶意目标分解为良性子任务）提出了轻量级顺序监控框架。作者构建了多样化的数据集，验证了分解攻击的高成功率，并提出了一种累积评估每个子任务的监控器。实验显示，该监控器实现了93%的防御成功率，且在成本和延迟上优于推理模型。

---

## #73 — Do Agent Rules Shape or Distort? Guardrails Beat Guidance in Coding Agents

`B` Score: 7.47 | 2026-04-13

**Authors:** Xing Zhang, Guanghui Wang, Yanwei Cui, Wei Qiu, Ziyuan Li, Bing Zhu et al. (7 total)

**Categories:** cs.AI, cs.CL

**Scores:** Citation: 8.50 | Influential: 9.02 | Venue: 2.00 | Author: 4.27 | Recency: 10.00

**Links:** [arXiv](https://arxiv.org/abs/2604.11088) | [PDF](https://arxiv.org/pdf/2604.11088)

> 本文研究了AI编码代理中的自然语言指令文件是否真正改善代理性能。作者从GitHub抓取了679个文件(25,532条规则)并在SWE-bench Verified上进行了大规模实证评估。结果显示规则将性能提高了7-14个百分点，但随机规则与专家策划的规则同样有效。负约束('不要重构不相关的代码')是唯一单独有益的规则类型，而积极指令('遵循代码风格')实际上有害。作者通过基于潜在奖励塑形的透镜分析这一模式，并发现单独的规则在孤立中大多有害，但在集体中有益。

---

## #74 — HiddenDetect: Detecting Jailbreak Attacks against Large Vision-Language Models via Monitoring Hidden States

`B` Score: 7.45 | 2025-02-20

**Authors:** Yilei Jiang, Xinyan Gao, Tianshuo Peng, Yingshui Tan, Xiaoyong Zhu, Bo Zheng et al. (7 total)

**Categories:** cs.CL

**Scores:** Citation: 9.26 | Influential: 9.69 | Venue: 2.00 | Author: 4.27 | Recency: 5.00

**Links:** [arXiv](https://arxiv.org/abs/2502.14744) | [PDF](https://arxiv.org/pdf/2502.14744)

> 本文研究了大型视觉语言模型(LVLMs)是否在推理过程中在其内部激活中编码了安全相关信号。研究发现LVLMs在处理不安全提示时表现出不同的激活模式，可以利用这些模式来检测和减轻对抗输入，而无需大量微调。基于这一见解，作者引入了HiddenDetect，一个利用内部模型激活来增强安全的新型无需微调框架。实验结果表明，HiddenDetect在检测LVLMs越狱攻击方面超越了最先进的方法。

---

## #75 — Indirect Prompt Injections: Are Firewalls All You Need, or Stronger Benchmarks?

`B` Score: 7.44 | 2025-10-06

**Authors:** Rishika Bhagwatkar, Kevin Kasa, Abhay Puri, Gabriel Huang, Irina Rish, Graham W. Taylor et al. (8 total)

**Categories:** cs.CR

**Scores:** Citation: 7.92 | Influential: 7.81 | Venue: 2.00 | Author: 9.41 | Recency: 7.00

**Links:** [arXiv](https://arxiv.org/abs/2510.05244) | [PDF](https://arxiv.org/pdf/2510.05244)

> 本文针对AI agents面临的间接提示注入攻击风险，提出了一种受防火墙概念启发的简单、模块化且模型无关的防御机制。该机制通过在agent与工具接口处部署输入最小化和输出净化两个防火墙，在四个公共基准测试中实现了完美的安全性与高实用性，达到了最先进的安全-效用权衡。此外，研究还深入分析了现有基准测试，揭示了其在成功指标等方面存在的关键缺陷。

---

## #76 — Steering Dialogue Dynamics for Robustness against Multi-turn Jailbreaking Attacks

`B` Score: 7.42 | 2025-02-28

**Authors:** Hanjiang Hu, Alexander Robey, Changliu Liu

**Categories:** cs.CL, cs.CR, cs.LG

**Scores:** Citation: 8.62 | Influential: 7.81 | Venue: 2.00 | Author: 8.55 | Recency: 5.00

**Links:** [arXiv](https://arxiv.org/abs/2503.00187) | [PDF](https://arxiv.org/pdf/2503.00187)

> 这篇论文针对大型语言模型在多轮对话中容易受到越狱攻击的问题，提出了一种基于安全控制理论的安全转向框架。该方法通过状态空间表示对话并引入神经屏障函数，主动检测和过滤来自演变上下文的有害查询，学习考虑对抗查询的安全预测器，防止上下文漂移导致的越狱，确保多轮对话中每一轮的安全性。

---

## #77 — Unintended Misalignment from Agentic Fine-Tuning: Risks and Mitigation

`B` Score: 7.42 | 2025-08-19

**Authors:** Dongyoon Hahm, Taywon Min, Woogyeol Jin, Kimin Lee

**Categories:** cs.CL, cs.AI, cs.LG

**Scores:** Citation: 8.17 | Influential: 7.81 | Venue: 10.00 | Author: 3.23 | Recency: 7.00

**Links:** [arXiv](https://arxiv.org/abs/2508.14031) | [PDF](https://arxiv.org/pdf/2508.14031)

> 研究揭示了针对代理任务进行微调会导致已对齐的大语言模型出现非预期的错位，增加执行有害任务的风险。为此，作者提出了PING方法，通过在响应前添加自动生成的自然语言前缀，在不牺牲良性任务性能的前提下引导模型拒绝有害请求。

---

## #78 — CP-Guard: Malicious Agent Detection and Defense in Collaborative Bird's Eye View Perception

`B` Score: 7.41 | 2024-12-16

**Authors:** Senkang Hu, Yihang Tao, Guowen Xu, Yiqin Deng, Xianhao Chen, Yuguang Fang et al. (7 total)

**Categories:** cs.AI

**Scores:** Citation: 8.00 | Influential: 9.02 | Venue: 2.00 | Author: 8.73 | Recency: 5.00

**Links:** [arXiv](https://arxiv.org/abs/2412.12000) | [PDF](https://arxiv.org/pdf/2412.12000)

> 本文提出了 CP-Guard，一种专为自动驾驶协作感知（CP）设计的防御机制，旨在准确检测并消除协作网络中的恶意智能体。该机制通过概率无关样本共识（PASAC）方法验证协作者之间的共识，并利用协作一致性损失（CCLoss）作为验证标准。实验表明，CP-Guard 在鸟瞰图（BEV）任务中能有效防御恶意代理发送的误导性信息，保障感知系统的安全性。

---

## #79 — Steering Away from Harm: An Adaptive Approach to Defending Vision Language Model Against Jailbreaks

`B` Score: 7.40 | 2024-11-23

**Authors:** Han Wang, Gang Wang, Huan Zhang

**Categories:** cs.CV, cs.AI

**Scores:** Citation: 9.29 | Influential: 9.69 | Venue: 5.00 | Author: 1.86 | Recency: 5.00

**Links:** [arXiv](https://arxiv.org/abs/2411.16721) | [PDF](https://arxiv.org/pdf/2411.16721)

> 本文提出了ASTRA防御方法，通过识别代表有害响应方向的可迁移转向向量，并在推理时应用自适应激活转向，使视觉语言模型远离对抗性特征方向。该方法在保持良性输入性能的同时，有效缓解了越狱风险，且具有高效率和良好的迁移性。

---

## #80 — Layer-Level Self-Exposure and Patch: Affirmative Token Mitigation for Jailbreak Attack Defense

`B` Score: 7.38 | 2025-01-05

**Authors:** Yang Ouyang, Hengrui Gu, Shuhang Lin, Wenyue Hua, Jie Peng, Bhavya Kailkhura et al. (9 total)

**Categories:** cs.CR, cs.AI, cs.CL

**Scores:** Citation: 7.47 | Influential: 7.81 | Venue: 5.00 | Author: 9.71 | Recency: 5.00

**Links:** [arXiv](https://arxiv.org/abs/2501.02629) | [PDF](https://arxiv.org/pdf/2501.02629)

> 本文提出Layer-AdvPatcher方法，通过识别大型语言模型中易受攻击的特定层，利用非学习策略修补这些层，减少有害提示下产生的肯定令牌，从而有效防御监狱攻击同时保持模型性能。

---

## #81 — Understanding and Rectifying Safety Perception Distortion in VLMs

`B` Score: 7.37 | 2025-02-18

**Authors:** Xiaohan Zou, Jian Kang, George Kesidis, Lu Lin

**Categories:** cs.CV, cs.CL, cs.LG

**Scores:** Citation: 7.44 | Influential: 9.39 | Venue: 2.00 | Author: 9.61 | Recency: 5.00

**Links:** [arXiv](https://arxiv.org/abs/2502.13095) | [PDF](https://arxiv.org/pdf/2502.13095)

> 本文揭示了视觉语言模型在整合视觉模态后更容易受到攻击的现象，识别出'安全感知扭曲'问题：多模态输入导致模型系统性地高估有害输入的安全性。作者提出的ShiftDC方法通过分解和校准模态诱导的激活偏移，在保持视觉语言能力的同时恢复LLM骨干的安全对齐。

---

## #82 — Interpreting and Steering LLMs with Mutual Information-based Explanations on Sparse Autoencoders

`B` Score: 7.36 | 2025-02-21

**Authors:** Xuansheng Wu, Jiayi Yuan, Wenlin Yao, Xiaoming Zhai, Ninghao Liu

**Categories:** cs.CL

**Scores:** Citation: 8.94 | Influential: 7.81 | Venue: 2.00 | Author: 7.15 | Recency: 5.00

**Links:** [arXiv](https://arxiv.org/abs/2502.15576) | [PDF](https://arxiv.org/pdf/2502.15576)

> 本文关注如何更好地解释稀疏自编码器(SAE)学习的特征，以理解LLM内部表示。作者分析了现有解释方法存在的频率偏差问题，提出使用固定词汇集进行特征解释和基于互信息的目标设计，以更好地捕获特征背后的语义意义。此外，作者提出了两种运行时转向策略，基于相应的解释调整学习到的特征激活。实验表明，该方法提供了更多话语级别的解释，并有效地引导LLM行为以防御越狱攻击。

---

## #83 — E$^2$AT: Multimodal Jailbreak Defense via Dynamic Joint Optimization for Multimodal Large Language Models

`B` Score: 7.36 | 2025-03-05

**Authors:** Liming Lu, Xiang Gu, Shuchao Pang, Siyuan Liang, Haotian Zhu, Xiyu Zeng et al. (8 total)

**Categories:** cs.CV, cs.AI, cs.CL

**Scores:** Citation: 8.64 | Influential: 9.02 | Venue: 2.00 | Author: 6.47 | Recency: 5.00

**Links:** [arXiv](https://arxiv.org/abs/2503.04833) | [PDF](https://arxiv.org/pdf/2503.04833)

> 本文提出了E$^2$AT框架，用于提高多模态大语言模型对抗越狱攻击的鲁棒性。该框架包含一个高效的基于投影器的AT模块，用于在特征级别对齐攻击样本，并提出了一种动态联合多模态优化策略来增强对抗攻击的泛化能力。实验表明，E$^2$AT在文本和图像模态上平均比现有基线高出34%，同时保持清洁任务性能。

---

## #84 — Defending Against Diverse Attacks in Federated Learning Through Consensus-Based Bi-Level Optimization

`B` Score: 7.34 | 2024-12-03

**Authors:** Nicolás García Trillos, Aditya Kumar Akash, Sixu Li, Konstantin Riedl, Yuhua Zhu

**Categories:** cs.LG, cs.CR, cs.MA

**Scores:** Citation: 6.31 | Influential: 9.02 | Venue: 10.00 | Author: 7.99 | Recency: 5.00

**Links:** [arXiv](https://arxiv.org/abs/2412.02535) | [PDF](https://arxiv.org/pdf/2412.02535)

> 本文针对联邦学习中的对抗攻击，提出了一种基于共识的双层优化方法CB2O以增强鲁棒性。通过理论分析和在去中心化集群联邦学习场景中的实验，证明了该方法能有效抵御标签翻转等多样化攻击，为恶意环境下的分布式训练提供了新的防御思路。

---

## #85 — Embedding-based classifiers can detect prompt injection attacks

`B` Score: 7.33 | 2024-10-29

**Authors:** Md. Ahsan Ayub, Subhabrata Majumdar

**Categories:** cs.CR, cs.LG

**Scores:** Citation: 9.22 | Influential: 9.58 | Venue: 2.00 | Author: 3.78 | Recency: 5.00

**Links:** [arXiv](https://arxiv.org/abs/2410.22284) | [PDF](https://arxiv.org/pdf/2410.22284)

> 本文提出了一种基于嵌入的机器学习分类器方法，用于检测针对大语言模型的提示注入攻击。通过利用常用嵌入模型生成提示词的向量表示，并结合随机森林和 XGBoost 等传统分类器进行预测，该方法在检测恶意提示方面表现出色。实验结果表明，该方法优于现有的基于仅编码器神经网络的开源提示注入分类器。

---

## #86 — Visual Confused Deputy: Exploiting and Defending Perception Failures in Computer-Using Agents

`B` Score: 7.28 | 2026-03-16

**Authors:** Xunzhuo Liu, Bowei He, Xue Liu, Andy Luo, Haichen Zhang, Huamin Chen

**Categories:** cs.CV, cs.CL

**Scores:** Citation: 9.18 | Influential: 7.81 | Venue: 2.00 | Author: 2.55 | Recency: 10.00

**Links:** [arXiv](https://arxiv.org/abs/2603.14707) | [PDF](https://arxiv.org/pdf/2603.14707)

> 本文形式化了计算机使用Agent中的“视觉受惑副手”问题，即Agent因感知错误或对抗性操纵而授权有害操作。为此，提出了双通道对比分类护栏，独立评估视觉目标和推理意图，以阻断风险操作。该方法在防御感知故障和对抗性操纵方面表现出色，优于单一通道的防御机制。

---

## #87 — Model Unlearning via Sparse Autoencoder Subspace Guided Projections

`B` Score: 7.27 | 2025-05-30

**Authors:** Xu Wang, Zihao Li, Benyou Wang, Yan Hu, Difan Zou

**Categories:** cs.CL, cs.LG

**Scores:** Citation: 7.82 | Influential: 7.81 | Venue: 10.00 | Author: 3.23 | Recency: 7.00

**Links:** [arXiv](https://arxiv.org/abs/2505.24428) | [PDF](https://arxiv.org/pdf/2505.24428)

> 本文提出了 SSPU 框架，利用稀疏自编码器特征引导模型参数空间的定向更新，实现精确、可解释且鲁棒的模型遗忘。该方法通过构建子空间并约束激活，有效降低了有害知识的准确率，并在对抗性提示下表现出比基线更强的鲁棒性。

---

## #88 — SHIELD: Classifier-Guided Prompting for Robust and Safer LVLMs

`B` Score: 7.25 | 2025-10-15

**Authors:** Juan Ren, Mark Dras, Usman Naseem

**Categories:** cs.CL

**Scores:** Citation: 7.48 | Influential: 7.81 | Venue: 2.00 | Author: 9.48 | Recency: 7.00

**Links:** [arXiv](https://arxiv.org/abs/2510.13190) | [PDF](https://arxiv.org/pdf/2510.13190)

> 本文提出了SHIELD，一个轻量级且与模型无关的预处理框架，通过结合细粒度安全分类与特定类别指导来增强大型视觉语言模型的安全性。该方法通过定制安全提示强制执行细致的拒绝或安全重定向，无需重新训练即可有效降低越狱率并保持模型效用。

---

## #89 — NeuroFilter: Privacy Guardrails for Conversational LLM Agents

`B` Score: 7.25 | 2026-01-21

**Authors:** Saswat Das, Ferdinando Fioretto

**Categories:** cs.CR, cs.AI, cs.CL

**Scores:** Citation: 7.60 | Influential: 7.81 | Venue: 2.00 | Author: 7.15 | Recency: 10.00

**Links:** [arXiv](https://arxiv.org/abs/2601.14660) | [PDF](https://arxiv.org/pdf/2601.14660)

> 本文提出了NeuroFilter框架，旨在解决对话式LLM Agent的隐私保护计算挑战。该框架利用模型激活空间中的线性结构检测隐私违规意图，并通过“激活速度”概念捕捉长对话中的累积漂移。实验表明，NeuroFilter在保持零误报的同时显著降低了计算成本，为基于上下文完整性的隐私防御提供了高效方案。

---

## #90 — Robust Adaptation of Large Multimodal Models for Retrieval Augmented Hateful Meme Detection

`B` Score: 7.24 | 2025-02-18

**Authors:** Jingbiao Mei, Jinghong Chen, Guangyu Yang, Weizhe Lin, Bill Byrne

**Categories:** cs.CL, cs.AI, cs.CV

**Scores:** Citation: 7.13 | Influential: 7.81 | Venue: 10.00 | Author: 6.47 | Recency: 5.00

**Links:** [arXiv](https://arxiv.org/abs/2502.13061) | [PDF](https://arxiv.org/pdf/2502.13061)

> 本文针对仇恨表情检测挑战，提出大型多模态模型的稳健适应框架。该方法在提高域内准确性和跨域泛化能力的同时，保留了通用视觉语言能力。实验表明，该方法在对抗攻击下具有更强鲁棒性，在六个数据集上取得最先进性能，并生成更高质量的仇恨内容解释。

---

## #91 — UniGuard: Towards Universal Safety Guardrails for Jailbreak Attacks on Multimodal Large Language Models

`B` Score: 7.24 | 2024-11-03

**Authors:** Sejoon Oh, Yiqiao Jin, Megha Sharma, Donghyun Kim, Eric Ma, Gaurav Verma et al. (7 total)

**Categories:** cs.CL, cs.AI, cs.LG

**Scores:** Citation: 8.27 | Influential: 9.02 | Venue: 2.00 | Author: 6.75 | Recency: 5.00

**Links:** [arXiv](https://arxiv.org/abs/2411.01703) | [PDF](https://arxiv.org/pdf/2411.01703)

> 本文提出了 UniGuard，一种通用的多模态安全护栏，旨在防御针对多模态大语言模型（MLLM）的越狱攻击。UniGuard 联合考虑单模态和跨模态的有害信号，通过在有毒语料库上训练以最小化生成有害响应的可能性。实验表明，该防御机制在多种模态、攻击策略及最先进的 MLLM（如 GPT-4o, Gemini Pro）上均表现出强大的通用性，且在推理时计算成本极低，不影响模型原有的视觉语言理解能力。

---

## #92 — Expert Personas Improve LLM Alignment but Damage Accuracy: Bootstrapping Intent-Based Persona Routing with PRISM

`B` Score: 7.23 | 2026-03-19

**Authors:** Zizhao Hu, Mohammad Rostami, Jesse Thomason

**Categories:** cs.AI

**Scores:** Citation: 9.30 | Influential: 7.81 | Venue: 2.00 | Author: 1.86 | Recency: 10.00

**Links:** [arXiv](https://arxiv.org/abs/2603.18507) | [PDF](https://arxiv.org/pdf/2603.18507)

> 本文研究了专家人设对LLM有效性的影响，发现其虽能提升对齐度但会损害准确性。为此，作者开发了PRISM流程，通过自蒸馏将基于意图的专家人设转化为门控LoRA适配器，无需外部数据。PRISM在生成任务中增强了人类偏好和安全对齐，同时在判别任务中保持了准确性。

---

## #93 — UniGuardian: A Unified Defense for Detecting Prompt Injection, Backdoor Attacks and Adversarial Attacks in Large Language Models

`B` Score: 7.22 | 2025-02-18

**Authors:** Huawei Lin, Yingjie Lao, Tong Geng, Tan Yu, Weijie Zhao

**Categories:** cs.CL, cs.AI, cs.LG

**Scores:** Citation: 8.30 | Influential: 7.81 | Venue: 2.00 | Author: 8.15 | Recency: 5.00

**Links:** [arXiv](https://arxiv.org/abs/2502.13141) | [PDF](https://arxiv.org/pdf/2502.13141)

> 本文提出了UniGuardian，首个用于检测LLM中提示注入、后门攻击和对抗攻击的统一防御机制。作者将这些攻击统称为提示触发攻击(PTA)，并引入单前向策略实现攻击检测和文本生成的同步进行，为LLM提供了高效准确的多类型攻击防护方案。

---

## #94 — Forewarned is Forearmed: Pre-Synthesizing Jailbreak-like Instructions to Enhance LLM Safety Guardrail to Potential Attacks

`B` Score: 7.22 | 2025-08-27

**Authors:** Sheng Liu, Qiang Sheng, Danding Wang, Yang Li, Guang Yang, Juan Cao

**Categories:** cs.CL

**Scores:** Citation: 6.08 | Influential: 7.81 | Venue: 10.00 | Author: 8.15 | Recency: 7.00

**Links:** [arXiv](https://arxiv.org/abs/2508.20038) | [PDF](https://arxiv.org/pdf/2508.20038)

> 本文提出了IMAGINE框架，通过分析嵌入空间分布来预合成类似越狱的指令，以弥合安全对齐语料库与真实攻击之间的分布差距。该框架采用迭代优化过程动态扩展文本生成分布，从而增强安全对齐数据的覆盖范围。实验证明，基于增强数据训练的模型在攻击成功率上显著降低，且未损害模型效用，实现了主动防御。

---

## #95 — Securing Vision-Language Models with a Robust Encoder Against Jailbreak and Adversarial Attacks

`B` Score: 7.21 | 2024-09-11

**Authors:** Md Zarif Hossain, Ahmed Imteaj

**Categories:** cs.CV, cs.AI

**Scores:** Citation: 8.20 | Influential: 9.02 | Venue: 5.00 | Author: 4.79 | Recency: 5.00

**Links:** [arXiv](https://arxiv.org/abs/2409.07353) | [PDF](https://arxiv.org/pdf/2409.07353)

> 本文提出了Sim-CLIP+，一种针对视觉语言模型的新型防御机制。该方法利用孪生架构对CLIP视觉编码器进行对抗性微调，最大化扰动样本与清洁样本的余弦相似度，从而增强模型对对抗性操作和越狱攻击的鲁棒性。Sim-CLIP+作为即插即用方案，无需修改模型结构且计算开销极低。

---

## #96 — Fine-tuned Large Language Models (LLMs): Improved Prompt Injection Attacks Detection

`B` Score: 7.21 | 2024-10-28

**Authors:** Md Abdur Rahman, Fan Wu, Alfredo Cuzzocrea, Sheikh Iqbal Ahamed

**Categories:** cs.CL, cs.AI

**Scores:** Citation: 7.94 | Influential: 7.81 | Venue: 5.00 | Author: 7.15 | Recency: 5.00

**Links:** [arXiv](https://arxiv.org/abs/2410.21337) | [PDF](https://arxiv.org/pdf/2410.21337)

> 本文探讨了提示注入攻击的安全漏洞，并比较了预训练大语言模型与微调大语言模型在检测此类攻击方面的性能。研究使用 XLM-RoBERTa 模型进行零样本分类和监督微调实验，结果表明，经过特定任务数据集微调后的模型在检测提示注入方面表现出极高的效率，准确率达到 99.13%。

---

## #97 — X-Boundary: Establishing Exact Safety Boundary to Shield LLMs from Multi-Turn Jailbreaks without Compromising Usability

`B` Score: 7.20 | 2025-02-14

**Authors:** Xiaoya Lu, Dongrui Liu, Yi Yu, Luxin Xu, Jing Shao

**Categories:** cs.CR, cs.AI, cs.CL

**Scores:** Citation: 8.29 | Influential: 9.02 | Venue: 2.00 | Author: 6.47 | Recency: 5.00

**Links:** [arXiv](https://arxiv.org/abs/2502.09990) | [PDF](https://arxiv.org/pdf/2502.09990)

> 本文提出X-Boundary方法保护LLM免受多轮越狱攻击同时保持可用性。研究发现现有防御虽提高安全性但降低通用能力或导致过度拒绝。X-Boundary通过建立精确的安全边界，将有害表示推离安全区域，在不干扰安全表示的情况下精确擦除有害表示。实验显示该方法实现最先进防御性能，减少20%过度拒绝率并保持完整通用能力。

---

## #98 — Why Safeguarded Ships Run Aground? Aligned Large Language Models' Safety Mechanisms Tend to Be Anchored in The Template Region

`B` Score: 7.19 | 2025-02-19

**Authors:** Chak Tou Leong, Qingyu Yin, Jian Wang, Wenjie Li

**Categories:** cs.CL, cs.AI, cs.CR

**Scores:** Citation: 6.40 | Influential: 9.39 | Venue: 10.00 | Author: 6.17 | Recency: 5.00

**Links:** [arXiv](https://arxiv.org/abs/2502.13946) | [PDF](https://arxiv.org/pdf/2502.13946)

> 本文揭示了大型语言模型安全对齐的脆弱性，提出'模板锚定安全对齐'概念，即LLM的安全决策过度依赖模板区域信息。通过广泛实验验证了这一现象在多种对齐模型中的普遍性，并展示了如何通过分离安全机制与模板区域来缓解越狱攻击，为更鲁棒的安全对齐技术指明方向。

---

## #99 — AegisLLM: Scaling Agentic Systems for Self-Reflective Defense in LLM Security

`B` Score: 7.19 | 2025-04-29

**Authors:** Zikui Cai, Shayan Shabihi, Bang An, Zora Che, Brian R. Bartoldson, Bhavya Kailkhura et al. (8 total)

**Categories:** cs.LG

**Scores:** Citation: 7.27 | Influential: 7.81 | Venue: 2.00 | Author: 9.71 | Recency: 7.00

**Links:** [arXiv](https://arxiv.org/abs/2504.20965) | [PDF](https://arxiv.org/pdf/2504.20965)

> 本文介绍了AegisLLM，一种协作式多智能体防御系统，通过编排器、偏转器、响应器和评估器的协作来抵御对抗性攻击和信息泄露。该系统利用测试时扩展和自动提示优化技术，在不重新训练模型的情况下显著增强了鲁棒性。评估显示，AegisLLM在遗忘和越狱基准测试中表现优异，优于传统静态防御方法。

---

## #100 — Adaptive Detoxification: Safeguarding General Capabilities of LLMs through Toxicity-Aware Knowledge Editing

`B` Score: 7.19 | 2025-05-28

**Authors:** Yifan Lu, Jing Li, Yigeng Zhou, Yihui Zhang, Wenya Wang, Xiucheng Li et al. (10 total)

**Categories:** cs.CL

**Scores:** Citation: 6.67 | Influential: 7.81 | Venue: 10.00 | Author: 6.17 | Recency: 7.00

**Links:** [arXiv](https://arxiv.org/abs/2505.22298) | [PDF](https://arxiv.org/pdf/2505.22298)

> 本文提出了ToxEdit，一种毒性感知的知识编辑方法，旨在解决现有去毒方法过度编辑导致拒绝合法查询的问题。该方法在前向传播中动态检测毒性激活模式，并通过自适应层间路径计算来有效缓解毒性。实验证明，ToxEdit在保持模型通用能力的同时，在去毒性能上优于现有最先进方法。

---

## #101 — Beyond Surface-Level Patterns: An Essence-Driven Defense Framework Against Jailbreak Attacks in LLMs

`B` Score: 7.18 | 2025-02-26

**Authors:** Shiyu Xiang, Ansen Zhang, Yanfei Cao, Yang Fan, Ronghao Chen

**Categories:** cs.CR

**Scores:** Citation: 7.75 | Influential: 9.02 | Venue: 10.00 | Author: 2.55 | Recency: 5.00

**Links:** [arXiv](https://arxiv.org/abs/2502.19041) | [PDF](https://arxiv.org/pdf/2502.19041)

> EDDF是一种基于'攻击本质'的防御框架，通过离线构建本质数据库和在线检测对抗查询来防御越狱攻击。该方法从多样化已知攻击实例中提取'攻击本质'存储在向量数据库中，显著优于现有方法，减少至少20%的攻击成功率，展现出对越狱攻击更强的鲁棒性。

---

## #102 — SecurityLingua: Efficient Defense of LLM Jailbreak Attacks via Security-Aware Prompt Compression

`B` Score: 7.11 | 2025-06-15

**Authors:** Yucheng Li, Surin Ahn, Huiqiang Jiang, Amir H. Abdi, Yuqing Yang, Lili Qiu

**Categories:** cs.CR, cs.CL

**Scores:** Citation: 7.62 | Influential: 7.81 | Venue: 2.00 | Author: 8.15 | Recency: 7.00

**Links:** [arXiv](https://arxiv.org/abs/2506.12707) | [PDF](https://arxiv.org/pdf/2506.12707)

> 本文提出了SecurityLingua，一种通过安全导向的提示压缩来防御LLM越狱攻击的有效且高效的方法。该方法训练一个提示压缩器来识别输入提示的“真实意图”，特别是检测对抗性提示的恶意意图，并将该意图通过系统提示传递给目标LLM。SecurityLingua通过保持原始输入提示不变来确保一致的用户体验，同时揭示潜在的恶意意图并激活LLM的内置安全护栏。

---

## #103 — Towards Safe Reasoning in Large Reasoning Models via Corrective Intervention

`B` Score: 7.11 | 2025-09-29

**Authors:** Yichi Zhang, Yue Ding, Jingwen Yang, Tianwei Luo, Dongbai Li, Ranjie Duan et al. (10 total)

**Categories:** cs.AI, cs.CL

**Scores:** Citation: 6.55 | Influential: 9.02 | Venue: 2.00 | Author: 9.71 | Recency: 7.00

**Links:** [arXiv](https://arxiv.org/abs/2509.24393) | [PDF](https://arxiv.org/pdf/2509.24393)

> 本文针对大推理模型中思维链（CoT）推理过程可能包含有害内容的问题，提出了干预偏好优化（IPO）方法。该方法利用安全推理的关键步骤特征，通过用安全触发器替换合规步骤并构建强信号偏好对，有效纠正了不安全的推理轨迹，显著提升了推理过程和最终响应的整体安全性。

---

## #104 — Lifelong Safety Alignment for Language Models

`B` Score: 7.10 | 2025-05-26

**Authors:** Haoyu Wang, Zeyu Qin, Yifei Zhao, Chao Du, Min Lin, Xueqian Wang et al. (7 total)

**Categories:** cs.CR, cs.AI, cs.CL

**Scores:** Citation: 7.47 | Influential: 7.81 | Venue: 2.00 | Author: 8.55 | Recency: 7.00

**Links:** [arXiv](https://arxiv.org/abs/2505.20259) | [PDF](https://arxiv.org/pdf/2505.20259)

> 本文提出了一个终身安全对齐框架，使大语言模型能够持续适应新的越狱策略。该框架引入了元攻击者和防御者的竞争设置，通过迭代训练让防御者逐步提高鲁棒性，最终将攻击成功率降至极低水平。该方法利用GPT-4o提取研究见解来预热元攻击者，实现了对未知攻击的有效防御。

---

## #105 — Single-pass Detection of Jailbreaking Input in Large Language Models

`B` Score: 7.08 | 2025-02-21

**Authors:** Leyla Naz Candogan, Yongtao Wu, Elias Abad Rocamora, Grigorios G. Chrysos, Volkan Cevher

**Categories:** cs.LG, cs.AI, cs.CL

**Scores:** Citation: 6.88 | Influential: 9.02 | Venue: 2.00 | Author: 9.91 | Recency: 5.00

**Links:** [arXiv](https://arxiv.org/abs/2502.15435) | [PDF](https://arxiv.org/pdf/2502.15435)

> 本文提出单次通过检测(SPD)方法，用于在单次前向传递中检测越狱输入。SPD利用logits携带的信息来预测输出句子是否会有害，从而只需一次前向传递即可进行防御。该方法不仅可以在开源模型上有效检测攻击，还能最小化对无害输入的误分类。即使在GPT-3.5和GPT-4中没有完整logit访问的情况下，SPD仍然有效，为高效保护LLM免受对抗攻击提供了有希望的方法。

---

## #106 — Adversary-Aware DPO: Enhancing Safety Alignment in Vision Language Models via Adversarial Training

`B` Score: 7.08 | 2025-02-17

**Authors:** Fenghua Weng, Jian Lou, Jun Feng, Minlie Huang, Wenjie Wang

**Categories:** cs.CR

**Scores:** Citation: 7.12 | Influential: 7.81 | Venue: 10.00 | Author: 5.40 | Recency: 5.00

**Links:** [arXiv](https://arxiv.org/abs/2502.11455) | [PDF](https://arxiv.org/pdf/2502.11455)

> 本文针对视觉语言模型(VLMs)的安全对齐问题，提出了一种名为ADPO的新型训练框架。当前VLMs的安全对齐通常通过事后安全微调实现，但对白盒攻击效果不佳。ADPO将对抗训练集成到DPO方法中，包含两个关键组件：对抗训练的参考模型和对抗感知的DPO损失函数，使模型能够在最坏对抗扰动下保持稳健和可靠，确保生成的内容符合人类价值观并拒绝有害查询。

---

## #107 — SafePTR: Token-Level Jailbreak Defense in Multimodal LLMs via Prune-then-Restore Mechanism

`B` Score: 7.08 | 2025-07-02

**Authors:** Beitao Chen, Xinyu Lyu, Lianli Gao, Jingkuan Song, Heng Tao Shen

**Categories:** cs.CR, cs.CV

**Scores:** Citation: 6.27 | Influential: 9.39 | Venue: 2.00 | Author: 9.83 | Recency: 7.00

**Links:** [arXiv](https://arxiv.org/abs/2507.01513) | [PDF](https://arxiv.org/pdf/2507.01513)

> 本文分析了多模态大语言模型中越狱攻击的根本原因，发现早期中间层中极少数token负责诱导不安全行为。基于此，作者提出了SafePTR防御框架，通过选择性修剪有害token并在后续层恢复良性特征，无需额外训练即可有效提升安全性。该方法显著增强了模型对多模态越狱的防御能力。

---

## #108 — Refining Input Guardrails: Enhancing LLM-as-a-Judge Efficiency Through Chain-of-Thought Fine-Tuning and Alignment

`B` Score: 7.07 | 2025-01-22

**Authors:** Melissa Kazemi Rad, Huy Nghiem, Andy Luo, Sahil Wadhwa, Mohammad Sorower, Stephen Rawls

**Categories:** cs.CL, cs.CR, cs.LG

**Scores:** Citation: 8.73 | Influential: 9.02 | Venue: 2.00 | Author: 4.27 | Recency: 5.00

**Links:** [arXiv](https://arxiv.org/abs/2501.13080) | [PDF](https://arxiv.org/pdf/2501.13080)

> 这篇论文研究了通过思维链(Chain-of-Thought)微调和对齐来增强大型语言模型作为输入护栏的效率。作者系统性地探索了利用少量训练数据使LLM成为代理防御机制的方法，使其能够检测恶意输入并提供推理理由，从而防止对话代理被滥用。研究严格评估了不同微调策略在对抗性和恶意查询类型上的泛化能力，为提高LLM作为安全判断工具的效能提供了有效方法。

---

## #109 — Role-Aware Language Models for Secure and Contextualized Access Control in Organizations

`B` Score: 7.06 | 2025-07-31

**Authors:** Saeed Almheiri, Yerulan Kongrat, Adrian Santosh, Ruslan Tasmukhanov, Josemaria Loza Vera, Muhammad Dehan Al Kautsar et al. (7 total)

**Categories:** cs.CL, cs.AI

**Scores:** Citation: 6.64 | Influential: 9.02 | Venue: 10.00 | Author: 3.78 | Recency: 7.00

**Links:** [arXiv](https://arxiv.org/abs/2507.23465) | [PDF](https://arxiv.org/pdf/2507.23465)

> 探讨了如何通过微调使大语言模型具备基于组织角色的访问控制能力。研究提出了三种建模策略并构建了相关数据集，评估了模型在不同组织结构下的表现及其对提示注入和越狱攻击的鲁棒性，以实现企业级安全部署。

---

## #110 — DeepContext: Stateful Real-Time Detection of Multi-Turn Adversarial Intent Drift in LLMs

`B` Score: 7.06 | 2026-02-18

**Authors:** Justin Albrethsen, Yash Datta, Kunal Kumar, Sharath Rajasekar

**Categories:** cs.AI, cs.ET, cs.LG

**Scores:** Citation: 8.40 | Influential: 9.02 | Venue: 2.00 | Author: 1.86 | Recency: 10.00

**Links:** [arXiv](https://arxiv.org/abs/2602.16935) | [PDF](https://arxiv.org/pdf/2602.16935)

> 提出DeepContext，一种有状态的实时监控框架，用于检测多轮对话中的对抗性意图漂移。该框架利用RNN架构传播隐藏状态，捕捉随对话轮次累积的风险，显著优于现有的无状态护栏。它在保持低推理延迟的同时，实现了最先进的多轮越狱检测性能。

---

## #111 — AMIA: Automatic Masking and Joint Intention Analysis Makes LVLMs Robust Jailbreak Defenders

`B` Score: 7.03 | 2025-05-30

**Authors:** Yuqi Zhang, Yuchun Miao, Zuchao Li, Liang Ding

**Categories:** cs.CV, cs.CL

**Scores:** Citation: 5.20 | Influential: 7.81 | Venue: 10.00 | Author: 9.48 | Recency: 7.00

**Links:** [arXiv](https://arxiv.org/abs/2505.24519) | [PDF](https://arxiv.org/pdf/2505.24519)

> 本文介绍了 AMIA，一种针对大型视觉语言模型的轻量级推理时防御方法，通过自动屏蔽文本无关的图像块来破坏对抗性扰动，并进行联合意图分析以缓解隐藏的恶意意图。实验表明，AMIA 在无需重新训练的情况下，显著提高了防御成功率，同时保持了模型的通用性。

---

## #112 — ALERT: Zero-shot LLM Jailbreak Detection via Internal Discrepancy Amplification

`B` Score: 7.03 | 2026-01-07

**Authors:** Xiao Lin, Philip Li, Zhichen Zeng, Tingwei Li, Tianxin Wei, Xuying Ning et al. (9 total)

**Categories:** cs.LG, cs.AI, cs.IR

**Scores:** Citation: 7.23 | Influential: 7.81 | Venue: 2.00 | Author: 7.43 | Recency: 9.00

**Links:** [arXiv](https://arxiv.org/abs/2601.03600) | [PDF](https://arxiv.org/pdf/2601.03600)

> 本文提出了ALERT框架，通过逐层、逐模块和逐词放大良性提示与越狱提示之间的内部特征差异，实现了高效的零样本越狱检测。该方法无需依赖训练数据中的越狱模板，在多个安全基准上表现出强大的检测性能，准确率和F1分数均显著优于现有基线。

---

## #113 — CausalArmor: Efficient Indirect Prompt Injection Guardrails via Causal Attribution

`B` Score: 7.02 | 2026-02-08

**Authors:** Minbeom Kim, Mihir Parmar, Phillip Wallis, Lesly Miculicich, Kyomin Jung, Krishnamurthy Dj Dvijotham et al. (8 total)

**Categories:** cs.CR, cs.LG, stat.ME

**Scores:** Citation: 6.33 | Influential: 7.81 | Venue: 2.00 | Author: 9.41 | Recency: 10.00

**Links:** [arXiv](https://arxiv.org/abs/2602.07918) | [PDF](https://arxiv.org/pdf/2602.07918)

> 本文提出了CausalArmor，一种基于因果归因的高效间接提示注入防御框架。该框架通过计算不可信内容对特权决策点的影响，仅在检测到不可信片段主导用户意图时触发针对性清理，避免了过度防御。实验证明，该方法在保持效用的同时，能有效防御间接提示注入攻击。

---

## #114 — Short-length Adversarial Training Helps LLMs Defend Long-length Jailbreak Attacks: Theoretical and Empirical Evidence

`B` Score: 7.00 | 2025-02-06

**Authors:** Shaopeng Fu, Liang Ding, Jingfeng Zhang, Di Wang

**Categories:** cs.LG, cs.CR, stat.ML

**Scores:** Citation: 7.36 | Influential: 7.81 | Venue: 2.00 | Author: 9.48 | Recency: 5.00

**Links:** [arXiv](https://arxiv.org/abs/2502.04204) | [PDF](https://arxiv.org/pdf/2502.04204)

> 研究证明，为防御长度为Θ(M)的对抗后缀越狱攻击，只需在长度为Θ(√M)的对抗后缀提示上对LLMs进行对齐。通过分析线性变换器的对抗上下文学习，作者证明了训练后变换器的鲁棒泛化边界取决于Θ(√Mtest/Mtrain)项。实验证实了攻击成功率与训练/测试中对抗扰动样本数量比之间的正相关关系，为高效防御长长度越狱攻击提供了理论依据和实践指导。

---

## #115 — Beyond Surface Alignment: Rebuilding LLMs Safety Mechanism via Probabilistically Ablating Refusal Direction

`B` Score: 7.00 | 2025-09-18

**Authors:** Yuanbo Xie, Yingjie Zhang, Tianyun Liu, Duohe Ma, Tingwen Liu

**Categories:** cs.CR

**Scores:** Citation: 6.35 | Influential: 9.02 | Venue: 10.00 | Author: 4.27 | Recency: 7.00

**Links:** [arXiv](https://arxiv.org/abs/2509.15202) | [PDF](https://arxiv.org/pdf/2509.15202)

> 本文提出了DeepRefusal，一个强大的安全对齐框架，通过在微调过程中概率性地消融拒绝方向，迫使模型从越狱状态动态重建其拒绝机制。该方法不仅有效防御了预填充和拒绝方向攻击，还展示了对抗其他未见越狱策略的强大韧性，在保持模型能力的同时大幅降低了攻击成功率。

---

## #116 — Trust The Typical

`B` Score: 6.97 | 2026-02-04

**Authors:** Debargha Ganguly, Sreehari Sankar, Biyao Zhang, Vikash Singh, Kanan Gupta, Harshini Kavuru et al. (11 total)

**Categories:** cs.CL, cs.AI, cs.DC

**Scores:** Citation: 6.18 | Influential: 7.81 | Venue: 2.00 | Author: 9.48 | Recency: 10.00

**Links:** [arXiv](https://arxiv.org/abs/2602.04581) | [PDF](https://arxiv.org/pdf/2602.04581)

> 本文提出了Trust The Typical (T3)框架，将安全视为分布外检测问题，通过学习可接受提示的语义分布来识别潜在威胁。该方法无需在有害示例上训练，显著降低了误报率，并在多种基准测试中实现了最先进的性能。它为LLM安全提供了一种基于理解安全而非枚举威胁的新范式。

---

## #117 — You Can't Eat Your Cake and Have It Too: The Performance Degradation of LLMs with Jailbreak Defense

`B` Score: 6.95 | 2025-01-21

**Authors:** Wuyuao Mai, Geng Hong, Pei Chen, Xudong Pan, Baojun Liu, Yuan Zhang et al. (8 total)

**Categories:** cs.CR

**Scores:** Citation: 6.96 | Influential: 7.81 | Venue: 5.00 | Author: 8.33 | Recency: 5.00

**Links:** [arXiv](https://arxiv.org/abs/2501.12210) | [PDF](https://arxiv.org/pdf/2501.12210)

> 这篇论文研究了大型语言模型(LLMs)安全防御机制与性能之间的权衡关系。作者发现，现有的越狱防御策略虽然提升了模型安全性，但同时也导致了模型效用和可用性的显著下降，甚至可能引发过度安全问题。研究填补了LLMs安全与性能权衡方面的空白，为平衡安全与实用性的防御策略设计提供了重要见解。

---

## #118 — ReliabilityRAG: Effective and Provably Robust Defense for RAG-based Web-Search

`B` Score: 6.95 | 2025-09-27

**Authors:** Zeyu Shen, Basileal Imana, Tong Wu, Chong Xiang, Prateek Mittal, Aleksandra Korolova

**Categories:** cs.CR, cs.AI

**Scores:** Citation: 7.25 | Influential: 7.81 | Venue: 2.00 | Author: 8.15 | Recency: 7.00

**Links:** [arXiv](https://arxiv.org/abs/2509.23519) | [PDF](https://arxiv.org/pdf/2509.23519)

> 本文提出了ReliabilityRAG框架，通过利用检索文档的可靠性信息来增强RAG系统的对抗鲁棒性。该方法采用图论视角识别文档中的“一致性多数”，并基于最大独立集算法过滤恶意文档，为对抗有界对抗性损坏提供了可证明的鲁棒性保证，同时通过加权采样聚合框架实现了高效处理。

---

## #119 — SEA-Guard: Culturally Grounded Multilingual Safeguard for Southeast Asia

`B` Score: 6.94 | 2026-02-02

**Authors:** Panuthep Tasawong, Jian Gang Ngui, Alham Fikri Aji, Trevor Cohn, Peerat Limkonchotiwat

**Categories:** cs.CL

**Scores:** Citation: 6.13 | Influential: 7.81 | Venue: 2.00 | Author: 9.48 | Recency: 10.00

**Links:** [arXiv](https://arxiv.org/abs/2602.01618) | [PDF](https://arxiv.org/pdf/2602.01618)

> 本文提出了 SEA-Guard，首个基于东南亚文化背景的多语言护栏模型系列。作者开发了一种智能体数据生成框架，可扩展地创建真实的区域特定安全数据集，以解决现有模型依赖机器翻译而忽略文化细微差别的问题。评估显示，SEA-Guard 在检测区域敏感内容方面优于现有护栏，同时保持了强大的通用安全性能。

---

## #120 — RePD: Defending Jailbreak Attack through a Retrieval-based Prompt Decomposition Process

`B` Score: 6.92 | 2024-10-11

**Authors:** Peiran Wang, Xiaogeng Liu, Chaowei Xiao

**Categories:** cs.CR, cs.AI

**Scores:** Citation: 7.03 | Influential: 7.81 | Venue: 5.00 | Author: 7.99 | Recency: 5.00

**Links:** [arXiv](https://arxiv.org/abs/2410.08660) | [PDF](https://arxiv.org/pdf/2410.08660)

> 本文提出了RePD，一种基于检索的提示分解框架，旨在缓解大语言模型面临的越狱攻击风险。RePD通过访问预收集的越狱提示模板数据库，识别并分解嵌入在用户提示中的有害查询，将其作为单样本学习示例教导LLM区分和分离恶意组件。实验表明，RePD在不影响典型用户请求响应性能的前提下，有效增强了LLM对越狱攻击的韧性。

---

## #121 — Rapid Response: Mitigating LLM Jailbreaks with a Few Examples

`B` Score: 6.90 | 2024-11-12

**Authors:** Alwin Peng, Julian Michael, Henry Sleight, Ethan Perez, Mrinank Sharma

**Categories:** cs.CL

**Scores:** Citation: 7.65 | Influential: 9.39 | Venue: 2.00 | Author: 5.88 | Recency: 5.00

**Links:** [arXiv](https://arxiv.org/abs/2411.07494) | [PDF](https://arxiv.org/pdf/2411.07494)

> 本文提出了一种快速响应防御策略，旨在通过观察少量攻击样本来阻断整类越狱攻击，而非追求完美的对抗鲁棒性。作者开发了 RapidResponseBench 基准来评估防御效果，并利用越狱扩散技术自动生成相似攻击样本进行训练。实验表明，最强的防御方法在仅观察一个示例的情况下，就能将分布内和分布外攻击的成功率分别降低 240 倍和 15 倍以上，展示了快速响应限制 LLM 滥用的潜力。

---

## #122 — DELMAN: Dynamic Defense Against Large Language Model Jailbreaking with Model Editing

`B` Score: 6.87 | 2025-02-17

**Authors:** Yi Wang, Fenghua Weng, Sibei Yang, Zhan Qin, Minlie Huang, Wenjie Wang

**Categories:** cs.CR, cs.AI

**Scores:** Citation: 6.85 | Influential: 9.02 | Venue: 10.00 | Author: 3.23 | Recency: 5.00

**Links:** [arXiv](https://arxiv.org/abs/2502.11647) | [PDF](https://arxiv.org/pdf/2502.11647)

> DELMAN提出了一种针对大型语言模型越狱攻击的动态防御方法，通过直接模型编辑技术精确更新最小相关参数集来中和有害行为，同时保留模型在通用任务中的效用。该方法采用KL散度正则化确保模型在处理良性查询时与原始模型保持一致，解决了现有防御机制需要大量参数修改或缺乏精确性的问题，适用于部署后的安全对齐场景。

---

## #123 — Your Agent Can Defend Itself against Backdoor Attacks

`B` Score: 6.87 | 2025-06-10

**Authors:** Li Changjiang, Liang Jiacheng, Cao Bochuan, Chen Jinghui, Wang Ting

**Categories:** cs.CR, cs.AI, cs.LG

**Scores:** Citation: 7.19 | Influential: 9.02 | Venue: 2.00 | Author: 6.17 | Recency: 7.00

**Links:** [arXiv](https://arxiv.org/abs/2506.08336) | [PDF](https://arxiv.org/pdf/2506.08336)

> 针对LLM智能体在训练和微调阶段面临的后门攻击风险，本文提出了ReAgent防御方法。该方法通过验证思维与行动的一致性以及重建指令与用户指令的一致性，有效检测后门，将攻击成功率降低了90%。

---

## #124 — JailbreaksOverTime: Detecting Jailbreak Attacks Under Distribution Shift

`B` Score: 6.77 | 2025-04-28

**Authors:** Julien Piet, Xiao Huang, Dennis Jacob, Annabella Chow, Maha Alrashed, Geng Zhao et al. (10 total)

**Categories:** cs.CR

**Scores:** Citation: 5.02 | Influential: 7.81 | Venue: 10.00 | Author: 8.33 | Recency: 7.00

**Links:** [arXiv](https://arxiv.org/abs/2504.19440) | [PDF](https://arxiv.org/pdf/2504.19440)

> 本文针对越狱检测系统面临的分布漂移问题，发布了包含10个月真实用户交互的JailbreaksOverTime数据集。研究提出了一种双管齐下的方法：利用持续学习（如自训练）快速适应新出现的越狱攻击，并引入无监督主动监控方法通过行为识别新型攻击。实验表明，每周重新训练检测模型可将假阴性率显著降低。

---

## #125 — Modal Logical Neural Networks

`B` Score: 6.77 | 2025-12-03

**Authors:** Antonin Sulc

**Categories:** cs.LG, cs.LO, cs.MA

**Scores:** Citation: 7.53 | Influential: 7.81 | Venue: 2.00 | Author: 4.79 | Recency: 9.00

**Links:** [arXiv](https://arxiv.org/abs/2512.03491) | [PDF](https://arxiv.org/pdf/2512.03491)

> 本文提出了模态逻辑神经网络（MLNN），这是一种将深度学习与模态逻辑形式语义相结合的神经符号框架。该框架引入了针对模态算子的专用神经元，充当可微分的“逻辑护栏”，能够在执行推理的同时学习逻辑系统的关系结构，显著提升了逻辑一致性和可解释性。

---

## #126 — STShield: Single-Token Sentinel for Real-Time Jailbreak Detection in Large Language Models

`B` Score: 6.75 | 2025-03-23

**Authors:** Xunguang Wang, Wenxuan Wang, Zhenlan Ji, Zongjie Li, Pingchuan Ma, Daoyuan Wu et al. (7 total)

**Categories:** cs.CL, cs.AI, cs.CR

**Scores:** Citation: 6.66 | Influential: 9.02 | Venue: 2.00 | Author: 8.33 | Recency: 5.00

**Links:** [arXiv](https://arxiv.org/abs/2503.17932) | [PDF](https://arxiv.org/pdf/2503.17932)

> STShield是一个轻量级实时越狱检测框架，引入单令牌哨兵机制，通过在模型响应序列中附加二进制安全指示符，利用LLM自身对齐能力进行检测。该框架结合监督微调和对抗训练，在保持模型效用的同时实现鲁棒检测，相比现有方法具有更低计算开销。

---

## #127 — sudoLLM: On Multi-role Alignment of Language Models

`B` Score: 6.74 | 2025-05-20

**Authors:** Soumadeep Saha, Akshay Chaturvedi, Joy Mahapatra, Utpal Garain

**Categories:** cs.CL, cs.CR

**Scores:** Citation: 5.93 | Influential: 7.81 | Venue: 10.00 | Author: 5.40 | Recency: 7.00

**Links:** [arXiv](https://arxiv.org/abs/2505.14607) | [PDF](https://arxiv.org/pdf/2505.14607)

> 论文提出了sudoLLM框架，借鉴访问控制机制实现了基于用户权限的多角色对齐。该框架通过注入用户偏差信号，确保模型仅向授权用户披露敏感信息，有效提升了抗越狱能力和安全性。

---

## #128 — AIR: Improving Agent Safety through Incident Response

`B` Score: 6.74 | 2026-02-12

**Authors:** Zibo Xiao, Jun Sun, Junjie Chen

**Categories:** cs.AI

**Scores:** Citation: 8.23 | Influential: 7.81 | Venue: 2.00 | Author: 1.86 | Recency: 10.00

**Links:** [arXiv](https://arxiv.org/abs/2602.11749) | [PDF](https://arxiv.org/pdf/2602.11749)

> 本文提出了AIR，首个针对大语言模型智能体系统的事故响应框架，旨在弥补现有安全机制仅关注预防的不足。AIR通过特定领域语言自主管理事故响应生命周期，实现基于环境状态的检测、遏制和恢复，并合成护栏规则以防止复发。实验表明AIR在检测、补救和根除方面的成功率均超过90%，证明了事故响应作为提升智能体安全的一类机制的可行性和必要性。

---

## #129 — Concept-Level Explainability for Auditing & Steering LLM Responses

`B` Score: 6.73 | 2025-05-12

**Authors:** Kenza Amara, Rita Sevastjanova, Mennatallah El-Assady

**Categories:** cs.CL, cs.AI

**Scores:** Citation: 7.33 | Influential: 7.81 | Venue: 2.00 | Author: 6.47 | Recency: 7.00

**Links:** [arXiv](https://arxiv.org/abs/2505.07610) | [PDF](https://arxiv.org/pdf/2505.07610)

> 本文提出了ConceptX，一种模型无关的概念级可解释性方法，用于识别提示中影响模型输出的概念。与Token级方法不同，ConceptX基于语义相似性分配重要性，支持通过修改提示来引导LLM响应（如减少有害性），而无需重新训练。实验表明，ConceptX在忠实度和人类对齐方面优于现有方法，能有效降低攻击成功率并提升情感转变效果。

---

## #130 — ReasAlign: Reasoning Enhanced Safety Alignment against Prompt Injection Attack

`B` Score: 6.73 | 2026-01-15

**Authors:** Hao Li, Yankai Yang, G. Edward Suh, Ning Zhang, Chaowei Xiao

**Categories:** cs.CR, cs.AI, cs.CL

**Scores:** Citation: 7.43 | Influential: 7.81 | Venue: 2.00 | Author: 4.79 | Recency: 9.00

**Links:** [arXiv](https://arxiv.org/abs/2601.10173) | [PDF](https://arxiv.org/pdf/2601.10173)

> ReasAlign 是一种针对间接提示注入攻击的防御方案，通过引入结构化推理步骤来分析查询并检测冲突指令。该方法在保持高实用性的同时，显著降低了攻击成功率，优于现有的最强护栏模型，实现了安全与实用性的最佳平衡。

---

## #131 — AlphaAlign: Incentivizing Safety Alignment with Extremely Simplified Reinforcement Learning

`B` Score: 6.72 | 2025-07-20

**Authors:** Yi Zhang, An Zhang, XiuYu Zhang, Leheng Sheng, Yuxin Chen, Zhenkai Liang et al. (7 total)

**Categories:** cs.AI, cs.CR, cs.LG

**Scores:** Citation: 7.08 | Influential: 7.81 | Venue: 2.00 | Author: 7.15 | Recency: 7.00

**Links:** [arXiv](https://arxiv.org/abs/2507.14987) | [PDF](https://arxiv.org/pdf/2507.14987)

> 本文提出了AlphaAlign，一个简单而有效的纯强化学习框架，通过双重奖励系统激励模型的安全意识。可验证的安全奖励鼓励对有害查询的正确格式化和明确拒绝的正当理由，同时惩罚过度拒绝；归一化的有用性奖励指导良性输入的高质量响应。该方法仅需二元提示安全标签和少量RL步骤即可显著改善模型性能，打破安全-效用权衡，同时保持或提高一般任务性能和对未知越狱的鲁棒性。

---

## #132 — CultureGuard: Towards Culturally-Aware Dataset and Guard Model for Multilingual Safety Applications

`B` Score: 6.70 | 2025-08-03

**Authors:** Raviraj Joshi, Rakesh Paul, Kanishk Singla, Anusha Kamath, Michael Evans, Katherine Luna et al. (11 total)

**Categories:** cs.CL, cs.LG

**Scores:** Citation: 5.84 | Influential: 7.81 | Venue: 10.00 | Author: 5.40 | Recency: 7.00

**Links:** [arXiv](https://arxiv.org/abs/2508.01710) | [PDF](https://arxiv.org/pdf/2508.01710)

> 本文提出了 CultureGuard，一种通过四阶段合成数据生成和过滤管道，构建高质量多语言安全数据集的解决方案。该方法将英语安全数据集扩展至八种语言，并训练了 Llama-3.1-Nemotron-Safety-Guard-8B-v3 模型，在多语言安全基准上实现了最先进的性能，有效解决了非英语语言安全防护滞后的问题。

---

## #133 — MindGuard: Guardrail Classifiers for Multi-Turn Mental Health Support

`B` Score: 6.70 | 2026-02-01

**Authors:** António Farinhas, Nuno M. Guerreiro, José Pombal, Pedro Henrique Martins, Laura Melton, Alex Conway et al. (9 total)

**Categories:** cs.AI

**Scores:** Citation: 6.09 | Influential: 7.81 | Venue: 2.00 | Author: 7.99 | Recency: 10.00

**Links:** [arXiv](https://arxiv.org/abs/2602.00950) | [PDF](https://arxiv.org/pdf/2602.00950)

> 本文提出了 MindGuard，一系列专为多轮心理健康支持设计的轻量级安全分类器。作者与心理学家合作开发了临床风险分类法，并发布了专家标注的真实世界对话数据集。MindGuard 能够区分治疗性披露和真正的临床危机，在减少误报的同时降低了对抗性交互中的有害参与率。

---

## #134 — AlignTree: Efficient Defense Against LLM Jailbreak Attacks

`B` Score: 6.69 | 2025-11-15

**Authors:** Gil Goren, Shahar Katz, Lior Wolf

**Categories:** cs.LG

**Scores:** Citation: 6.10 | Influential: 7.81 | Venue: 10.00 | Author: 3.23 | Recency: 9.00

**Links:** [arXiv](https://arxiv.org/abs/2511.12217) | [PDF](https://arxiv.org/pdf/2511.12217)

> 本文提出了AlignTree，一种高效防御大语言模型越狱攻击的方法，旨在增强模型对齐同时保持最小计算开销。该防御机制通过高效的随机森林分类器监控生成过程中的LLM激活，利用拒绝方向和基于SVM的非线性特征信号来检测不对齐行为。实验证明，AlignTree在多个LLM和基准测试中表现出高效的鲁棒性，且无需额外的提示或辅助模型。

---

## #135 — TRIDENT: Enhancing Large Language Model Safety with Tri-Dimensional Diversified Red-Teaming Data Synthesis

`B` Score: 6.68 | 2025-05-30

**Authors:** Xiaorui Wu, Xiaofeng Mao, Fei Li, Xin Zhang, Xuanhong Li, Chong Teng et al. (8 total)

**Categories:** cs.CL

**Scores:** Citation: 5.20 | Influential: 7.81 | Venue: 10.00 | Author: 7.15 | Recency: 7.00

**Links:** [arXiv](https://arxiv.org/abs/2505.24672) | [PDF](https://arxiv.org/pdf/2505.24672)

> 本文提出了 TRIDENT，一种利用基于角色的零样本生成技术，从词汇多样性、恶意意图和越狱战术三个维度自动合成多样化红队数据的流水线。通过在生成的数据集上对 Llama 3.1 进行微调，该方法显著降低了模型的危害分数和攻击成功率，优于现有的基线数据集。

---

## #136 — The Blessing and Curse of Dimensionality in Safety Alignment

`B` Score: 6.67 | 2025-07-27

**Authors:** Rachel S. Y. Teo, Laziz U. Abdullaev, Tan M. Nguyen

**Categories:** cs.AI, cs.LG, stat.ML

**Scores:** Citation: 8.27 | Influential: 7.81 | Venue: 2.00 | Author: 3.23 | Recency: 7.00

**Links:** [arXiv](https://arxiv.org/abs/2507.20333) | [PDF](https://arxiv.org/pdf/2507.20333)

> 本文探讨了高维表示在LLM安全对齐中的双刃剑效应，指出高维激活空间中的线性结构可被利用以绕过安全对齐。研究表明，将模型表示投影到低维子空间可以在保留对齐信息的同时显著降低通过表示工程进行越狱的易感性，并提供了相关的理论见解。

---

## #137 — Think Twice Before You Act: Enhancing Agent Behavioral Safety with Thought Correction

`B` Score: 6.63 | 2025-05-16

**Authors:** Changyue Jiang, Xudong Pan, Min Yang

**Categories:** cs.AI, cs.CR

**Scores:** Citation: 7.99 | Influential: 7.81 | Venue: 2.00 | Author: 3.78 | Recency: 7.00

**Links:** [arXiv](https://arxiv.org/abs/2505.11063) | [PDF](https://arxiv.org/pdf/2505.11063)

> 针对基于大模型的自主 Agent 在长周期任务中因推理偏差引发级联安全风险的问题，本文提出了 Thought-Aligner，一种插件式的动态思维纠正模块。该模块利用轻量级模型在每次行动执行前实时纠正高风险思维，并将修正后的思维重新引入 Agent，从而确保后续决策和工具交互的安全性。该方法仅修改推理阶段而不改变底层框架，兼顾了安全性与部署便捷性。

---

## #138 — The Alignment Waltz: Jointly Training Agents to Collaborate for Safety

`B` Score: 6.62 | 2025-10-09

**Authors:** Jingyu Zhang, Haozhu Wang, Eric Michael Smith, Sid Wang, Amr Sharaf, Mahesh Pasupuleti et al. (10 total)

**Categories:** cs.CL

**Scores:** Citation: 6.71 | Influential: 7.81 | Venue: 2.00 | Author: 7.62 | Recency: 7.00

**Links:** [arXiv](https://arxiv.org/abs/2510.08240) | [PDF](https://arxiv.org/pdf/2510.08240)

> 提出了WaltzRL，一种新颖的多智能体强化学习框架，将安全对齐视为协作的正和博弈。该方法联合训练对话智能体和反馈智能体，通过动态改进奖励机制，在不丢弃响应的情况下改进不安全或过度拒绝的回答。实验表明，WaltzRL显著降低了不安全内容和过度拒绝现象。

---

## #139 — Improved Large Language Model Jailbreak Detection via Pretrained Embeddings

`B` Score: 6.61 | 2024-12-02

**Authors:** Erick Galinkin, Martin Sablotny

**Categories:** cs.CR, cs.AI, cs.LG

**Scores:** Citation: 7.54 | Influential: 9.39 | Venue: 2.00 | Author: 4.27 | Recency: 5.00

**Links:** [arXiv](https://arxiv.org/abs/2412.01547) | [PDF](https://arxiv.org/pdf/2412.01547)

> 本文提出了一种基于预训练文本嵌入和传统机器学习分类算法的新方法，用于检测大语言模型的越狱提示。该方法通过将适合检索的文本嵌入与分类器配对，在识别越狱尝试方面优于所有公开的开源LLM安全应用方法，有效防止了模型生成有害内容。

---

## #140 — DETAM: Defending LLMs Against Jailbreak Attacks via Targeted Attention Modification

`B` Score: 6.60 | 2025-04-18

**Authors:** Yu Li, Han Jiang, Zhihua Wei

**Categories:** cs.CL

**Scores:** Citation: 6.26 | Influential: 7.81 | Venue: 10.00 | Author: 4.79 | Recency: 5.00

**Links:** [arXiv](https://arxiv.org/abs/2504.13562) | [PDF](https://arxiv.org/pdf/2504.13562)

> 本文提出了DETAM，一种无需微调的越狱防御方法，通过有针对性的注意力修改来增强LLM的安全性。该方法分析成功与失败防御时的注意力分数差异，识别敏感注意力头，并在推理时重新分配注意力以强调用户核心意图。实验结果显示，DETAM在防御越狱攻击方面优于多种基线，且具有良好的泛化能力。

---

## #141 — SPIRIT: Patching Speech Language Models against Jailbreak Attacks

`B` Score: 6.56 | 2025-05-18

**Authors:** Amirbek Djanibekov, Nurdaulet Mukhituly, Kentaro Inui, Hanan Aldarmaki, Nils Lukas

**Categories:** eess.AS, cs.LG

**Scores:** Citation: 5.90 | Influential: 7.81 | Venue: 10.00 | Author: 4.27 | Recency: 7.00

**Links:** [arXiv](https://arxiv.org/abs/2505.13541) | [PDF](https://arxiv.org/pdf/2505.13541)

> 本文分析了语音语言模型（SLM）的安全性，发现相比文本模型，SLM极易受到通过注入不可感知噪声进行的越狱攻击，攻击成功率在某些情况下可达100%。为此，作者提出了名为SPIRIT的事后修补防御方法，通过在推理过程中干预并修改SLM的激活值来增强鲁棒性。该方法无需重新训练即可将防御效果提升至99%，且对模型实用性影响极小，有效解决了SLM的安全隐患。

---

## #142 — HoliSafe: Holistic Safety Benchmarking and Modeling for Vision-Language Model

`B` Score: 6.55 | 2025-06-05

**Authors:** Youngwan Lee, Kangsan Kim, Kwanyong Park, Ilcahe Jung, Soojin Jang, Seanie Lee et al. (8 total)

**Categories:** cs.CV, cs.AI

**Scores:** Citation: 6.06 | Influential: 9.02 | Venue: 2.00 | Author: 7.43 | Recency: 7.00

**Links:** [arXiv](https://arxiv.org/abs/2506.04704) | [PDF](https://arxiv.org/pdf/2506.04704)

> 本文针对视觉语言模型的安全问题，提出了HoliSafe数据集和基准，涵盖了所有图像-文本组合的不安全场景。作者还设计了一个包含视觉保护模块的模块化框架，使模型不仅能生成更安全的响应，还能提供可解释的有害性分类。实验表明该方法在多个VLM基准上实现了最先进的安全性能。

---

## #143 — Agent Control Protocol: Admission Control for Agent Actions

`B` Score: 6.53 | 2026-03-19

**Authors:** Marcelo Fernandez

**Categories:** cs.CR, cs.AI

**Scores:** Citation: 8.29 | Influential: 7.81 | Venue: 2.00 | Author: 0.26 | Recency: 10.00

**Links:** [arXiv](https://arxiv.org/abs/2603.18829) | [PDF](https://arxiv.org/pdf/2603.18829)

> 本文提出了ACP，一种通过静态风险评分和有状态信号（如异常累积）在执行轨迹上强制执行行为属性的时序准入控制协议。ACP解决了无状态引擎无法处理依赖执行历史威胁的问题，并识别并修复了状态混合漏洞和偏差崩溃问题，有效限制了自主代理的有害行为模式。

---

## #144 — ALRPHFS: Adversarially Learned Risk Patterns with Hierarchical Fast \& Slow Reasoning for Robust Agent Defense

`B` Score: 6.52 | 2025-05-25

**Authors:** Shiyu Xiang, Tong Zhang, Ronghao Chen

**Categories:** cs.CR

**Scores:** Citation: 6.61 | Influential: 7.81 | Venue: 10.00 | Author: 1.86 | Recency: 7.00

**Links:** [arXiv](https://arxiv.org/abs/2505.19260) | [PDF](https://arxiv.org/pdf/2505.19260)

> 本文提出了ALRPHFS防御框架，包含离线对抗自学习循环和在线分层快慢推理引擎。该框架通过迭代提炼风险模式，弥合了安全检查与真实风险之间的语义鸿沟，在检测有效性和计算效率之间取得了平衡，相比现有基线实现了更优的性能。

---

## #145 — Understanding and Mitigating Over-refusal for Large Language Models via Safety Representation

`B` Score: 6.52 | 2025-11-24

**Authors:** Junbo Zhang, Ran Chen, Qianli Zhou, Xinyang Deng, Wen Jiang

**Categories:** cs.CR, cs.CL

**Scores:** Citation: 7.31 | Influential: 7.81 | Venue: 2.00 | Author: 3.78 | Recency: 9.00

**Links:** [arXiv](https://arxiv.org/abs/2511.19009) | [PDF](https://arxiv.org/pdf/2511.19009)

> 本文针对大语言模型在防御越狱攻击时产生的过度拒绝问题进行了深入研究，通过表征视角分析发现此类样本位于良性与恶意样本的边界区域。为此，作者提出了MOSR方法，利用重叠感知损失加权和上下文感知增强这两个创新组件来干预模型的安全表征，从而有效缓解过度拒绝现象，在保障模型安全性的同时显著提升了其可用性，实现了安全与实用的平衡。

---

## #146 — Defense Against the Dark Prompts: Mitigating Best-of-N Jailbreaking with Prompt Evaluation

`B` Score: 6.51 | 2025-02-01

**Authors:** Stuart Armstrong, Matija Franklin, Connor Stevens, Rebecca Gorman

**Categories:** cs.CR, cs.AI, cs.CL

**Scores:** Citation: 8.05 | Influential: 9.02 | Venue: 2.00 | Author: 2.55 | Recency: 5.00

**Links:** [arXiv](https://arxiv.org/abs/2502.00580) | [PDF](https://arxiv.org/pdf/2502.00580)

> 该论文提出了一种名为'Defense Against The Dark Prompts' (DATDP) 的新方法，通过使用评估语言模型反复检测提示中的危险或操纵行为，特别是明确识别越狱尝试，直到生成稳健的安全评级。实验表明，DATDP能够100%阻止Best-of-N越狱攻击，即使使用较小的评估模型（如Claude和LLaMa-3-8B-instruct）也能保持高防护效果，为大型语言模型提供了一种有效的安全防护机制。

---

## #147 — More is Less: The Pitfalls of Multi-Model Synthetic Preference Data in DPO Safety Alignment

`B` Score: 6.51 | 2025-04-03

**Authors:** Yifan Wang, Runjin Chen, Bolian Li, David Cho, Yihe Deng, Ruqi Zhang et al. (10 total)

**Categories:** cs.AI

**Scores:** Citation: 6.15 | Influential: 7.81 | Venue: 2.00 | Author: 9.83 | Recency: 5.00

**Links:** [arXiv](https://arxiv.org/abs/2504.02193) | [PDF](https://arxiv.org/pdf/2504.02193)

> 本文研究了直接偏好优化（DPO）在安全对齐中的现象，发现虽然多模型生成的合成数据能提升通用任务性能，但也容易导致训练中的奖励黑客攻击，从而增加越狱攻击的成功率。研究指出，使用强模型生成被选回复而目标模型生成被拒回复的配置会显著降低安全性，而仅使用自生成回复的数据对在安全性上表现最佳。这一发现揭示了多模型偏好数据的高线性可分离性带来的安全风险。

---

## #148 — SafeAgent: Safeguarding LLM Agents via an Automated Risk Simulator

`B` Score: 6.50 | 2025-05-23

**Authors:** Xueyang Zhou, Weidong Wang, Lin Lu, Jiawen Shi, Guiyao Tie, Yongtian Xu et al. (10 total)

**Categories:** cs.AI

**Scores:** Citation: 5.95 | Influential: 9.02 | Venue: 2.00 | Author: 7.43 | Recency: 7.00

**Links:** [arXiv](https://arxiv.org/abs/2505.17735) | [PDF](https://arxiv.org/pdf/2505.17735)

> 本文提出了AutoSafe框架，通过形式化的威胁模型（OTS）和自动化数据生成管道来增强智能体安全性。该框架模拟不安全行为以生成高质量的安全训练数据，显著提升了合成和真实世界基准测试中的安全得分，无需收集危险的真实世界数据。

---

## #149 — MoJE: Mixture of Jailbreak Experts, Naive Tabular Classifiers as Guard for Prompt Attacks

`B` Score: 6.50 | 2024-09-26

**Authors:** Giandomenico Cornacchia, Giulio Zizzo, Kieran Fraser, Muhammad Zaid Hameed, Ambrish Rawat, Mark Purcell

**Categories:** cs.CR, cs.AI, cs.LG

**Scores:** Citation: 5.10 | Influential: 7.81 | Venue: 10.00 | Author: 7.62 | Recency: 5.00

**Links:** [arXiv](https://arxiv.org/abs/2409.17699) | [PDF](https://arxiv.org/pdf/2409.17699)

> 本文提出了MoJE（越狱专家混合）护栏架构，利用简单的语言统计技术来高效检测针对大语言模型的越狱攻击。实验表明，MoJE在保持极低计算开销的同时，能够检测出90%的攻击且不影响良性提示，显著提升了模型在推理阶段的安全性和计算效率。

---

## #150 — SDGO: Self-Discrimination-Guided Optimization for Consistent Safety in Large Language Models

`B` Score: 6.46 | 2025-08-21

**Authors:** Peng Ding, Wen Sun, Dailin Li, Wei Zou, Jiaming Wang, Jiajun Chen et al. (7 total)

**Categories:** cs.CL

**Scores:** Citation: 3.99 | Influential: 7.81 | Venue: 10.00 | Author: 9.34 | Recency: 7.00

**Links:** [arXiv](https://arxiv.org/abs/2508.15648) | [PDF](https://arxiv.org/pdf/2508.15648)

> 本文揭示了LLM在判别和生成有害内容上的能力不一致性，并提出了SDGO框架。该框架利用模型自身的判别能力作为奖励信号，通过强化学习迭代自我改进，从而增强生成安全性。实验表明，SDGO在无需额外数据的情况下显著提升了模型安全性，并保持了对良性查询的有益性。

---

## #151 — Evo-MARL: Co-Evolutionary Multi-Agent Reinforcement Learning for Internalized Safety

`C` Score: 6.45 | 2025-08-05

**Authors:** Zhenyu Pan, Yiting Zhang, Yutong Zhang, Jianshu Zhang, Haozheng Luo, Yuwei Han et al. (11 total)

**Categories:** cs.AI

**Scores:** Citation: 6.70 | Influential: 7.81 | Venue: 2.00 | Author: 6.47 | Recency: 7.00

**Links:** [arXiv](https://arxiv.org/abs/2508.03864) | [PDF](https://arxiv.org/pdf/2508.03864)

> 本文提出了Evo-MARL，一种新颖的多智能体强化学习框架，旨在让所有任务智能体共同获得防御能力。该方法通过进化搜索与参数共享强化学习的结合，协同进化攻击者和防御者，将安全机制内化，从而在不增加系统开销的情况下提升鲁棒性。

---

## #152 — Learning When to Act or Refuse: Guarding Agentic Reasoning Models for Safe Multi-Step Tool Use

`C` Score: 6.45 | 2026-03-03

**Authors:** Aradhye Agarwal, Gurdit Siyan, Yash Pandya, Joykirat Singh, Akshay Nambi, Ahmed Awadallah

**Categories:** cs.CL

**Scores:** Citation: 7.34 | Influential: 7.81 | Venue: 2.00 | Author: 2.55 | Recency: 10.00

**Links:** [arXiv](https://arxiv.org/abs/2603.03205) | [PDF](https://arxiv.org/pdf/2603.03205)

> 本文提出了MOSAIC后训练框架，通过将安全决策显式化和可学习化，使Agent在多步工具使用中学会何时行动或拒绝。该框架采用计划-检查-行动的循环结构，利用基于偏好的强化学习进行训练，显著降低了有害行为并减少了隐私泄露，同时保持了良性任务的性能。

---

## #153 — Simple Role Assignment is Extraordinarily Effective for Safety Alignment

`C` Score: 6.44 | 2026-01-20

**Authors:** Zhou Ziheng, Jiakun Ding, Zhaowei Zhang, Ruosen Gao, Yingnian Wu, Demetri Terzopoulos et al. (9 total)

**Categories:** cs.CY, cs.AI

**Scores:** Citation: 5.74 | Influential: 7.81 | Venue: 2.00 | Author: 7.99 | Recency: 9.00

**Links:** [arXiv](https://arxiv.org/abs/2602.00061) | [PDF](https://arxiv.org/pdf/2602.00061)

> 本文基于心智理论提出了角色条件化作为一种紧凑的对齐替代方案。该方法通过社会角色（如母亲、法官）隐式编码价值观和认知图式，无需训练即可生成安全回复。实验表明，该方法在多个基准测试中显著优于基于原则和思维链的基线，大幅降低了不安全输出率，确立了角色分配在AI对齐中的强大作用。

---

## #154 — Safety Training Persists Through Helpfulness Optimization in LLM Agents

`C` Score: 6.44 | 2026-02-13

**Authors:** Benjamin Plaut

**Categories:** cs.LG, cs.CL

**Scores:** Citation: 6.58 | Influential: 7.81 | Venue: 2.00 | Author: 4.79 | Recency: 10.00

**Links:** [arXiv](https://arxiv.org/abs/2603.02229) | [PDF](https://arxiv.org/pdf/2603.02229)

> 本文研究了在多步工具使用的代理设置中，直接偏好优化（DPO）对安全性和有用性的影响。研究发现，与单步聊天设置不同，安全训练在随后的有用性优化中得以保持，且所有训练配置最终都接近线性的帕累托前沿。这一发现挑战了以往关于安全与有用性权衡的观点，强调了深入理解代理环境中后训练动态的必要性。

---

## #155 — Securing AI Agents Against Prompt Injection Attacks

`C` Score: 6.42 | 2025-11-19

**Authors:** Badrinath Ramakrishnan, Akshaya Balaji

**Categories:** cs.CR, cs.AI

**Scores:** Citation: 7.98 | Influential: 7.81 | Venue: 2.00 | Author: 1.12 | Recency: 9.00

**Links:** [arXiv](https://arxiv.org/abs/2511.15759) | [PDF](https://arxiv.org/pdf/2511.15759)

> 本文针对检索增强生成（RAG）系统中的AI Agent，提出了一个全面的提示注入风险评估基准和多层防御框架。该基准包含847个对抗性测试用例，覆盖五种攻击类别，并评估了基于嵌入的异常检测和分层系统提示护栏等防御机制。实验显示，该组合框架将攻击成功率从73.2%降至8.7%，同时保持了94.3%的基线任务性能。

---

## #156 — Guiding Giants: Lightweight Controllers for Weighted Activation Steering in LLMs

`C` Score: 6.40 | 2025-05-22

**Authors:** Amr Hegazy, Mostafa Elhoushi, Amr Alanwar

**Categories:** cs.CL, cs.LG

**Scores:** Citation: 6.59 | Influential: 7.81 | Venue: 2.00 | Author: 6.47 | Recency: 7.00

**Links:** [arXiv](https://arxiv.org/abs/2505.20309) | [PDF](https://arxiv.org/pdf/2505.20309)

> 本文提出了一种轻量级控制器网络，用于在推理时对LLM进行加权激活引导。该控制器通过观察中间激活预测全局缩放因子和层特定权重，动态调节干预强度，从而在不改变模型参数的情况下有效抑制不安全内容的生成，实现了高效且自适应的细粒度行为控制。

---

## #157 — IntentionReasoner: Facilitating Adaptive LLM Safeguards through Intent Reasoning and Selective Query Refinement

`C` Score: 6.39 | 2025-08-27

**Authors:** Yuanzhe Shen, Zisu Huang, Zhengkang Guo, Yide Liu, Guanxu Chen, Ruicheng Yin et al. (8 total)

**Categories:** cs.AI

**Scores:** Citation: 6.92 | Influential: 7.81 | Venue: 2.00 | Author: 5.40 | Recency: 7.00

**Links:** [arXiv](https://arxiv.org/abs/2508.20151) | [PDF](https://arxiv.org/pdf/2508.20151)

> 本文提出了IntentionReasoner，一种利用专用守卫模型进行意图推理和选择性查询重写的自适应安全机制。该机制通过构建大规模标注数据集并应用监督微调和多奖励优化策略，有效中和边缘查询中的有害意图。实验表明，该方法在显著提升安全性的同时，降低了过度拒绝率并保持了响应质量，实现了安全与效用的平衡。

---

## #158 — SafeThinker: Reasoning about Risk to Deepen Safety Beyond Shallow Alignment

`C` Score: 6.39 | 2026-01-23

**Authors:** Xianya Fang, Xianying Luo, Yadong Wang, Xiang Chen, Yu Tian, Zequn Sun et al. (11 total)

**Categories:** cs.CR, cs.AI

**Scores:** Citation: 5.82 | Influential: 7.81 | Venue: 2.00 | Author: 6.75 | Recency: 10.00

**Links:** [arXiv](https://arxiv.org/abs/2601.16506) | [PDF](https://arxiv.org/pdf/2601.16506)

> 本文提出了SafeThinker，一个通过动态分配防御资源来深化安全性的自适应框架。该框架利用轻量级网关分类器评估风险，将输入路由至标准化拒绝机制、安全感知双专家模块或分布引导思考组件，以分别处理显性威胁、伪装攻击和不确定生成。实验表明，SafeThinker在不降低效用的前提下显著降低了多种越狱策略的攻击成功率。

---

## #159 — Uncertainty-based Offline Variational Bayesian Reinforcement Learning for Robustness under Diverse Data Corruptions

`C` Score: 6.39 | 2024-11-01

**Authors:** Rui Yang, Jie Wang, Guoping Wu, Bin Li

**Categories:** cs.LG, cs.AI

**Scores:** Citation: 6.90 | Influential: 7.81 | Venue: 5.00 | Author: 4.79 | Recency: 5.00

**Links:** [arXiv](https://arxiv.org/abs/2411.00465) | [PDF](https://arxiv.org/pdf/2411.00465)

> 针对现实世界中离线数据集常受噪声或恶意攻击损坏的问题，本文提出了TRACER方法。该方法首次引入贝叶斯推断来捕捉动作价值函数的不确定性，利用基于熵的度量区分并抑制损坏数据的影响，从而在清洁环境中显著提升智能体的鲁棒性和性能。

---

## #160 — Smoothed Embeddings for Robust Language Models

`C` Score: 6.38 | 2025-01-27

**Authors:** Ryo Hase, Md Rafi Ur Rashid, Ashley Lewis, Jing Liu, Toshiaki Koike-Akino, Kieran Parsons et al. (7 total)

**Categories:** cs.LG, cs.AI, cs.CL

**Scores:** Citation: 6.23 | Influential: 7.81 | Venue: 2.00 | Author: 8.79 | Recency: 5.00

**Links:** [arXiv](https://arxiv.org/abs/2501.16497) | [PDF](https://arxiv.org/pdf/2501.16497)

> 本文提出随机嵌入平滑和标记聚合(RESTA)防御方法，通过向嵌入向量添加随机噪声并聚合，在生成输出时保留语义信息。实验表明该方法与基线防御相比实现优越的鲁棒性与效用权衡，有效提升语言模型安全性。

---

## #161 — Scalable Defense against In-the-wild Jailbreaking Attacks with Safety Context Retrieval

`C` Score: 6.38 | 2025-05-21

**Authors:** Taiye Chen, Zeming Wei, Ang Li, Yisen Wang

**Categories:** cs.CR, cs.AI, cs.CL

**Scores:** Citation: 7.44 | Influential: 7.81 | Venue: 2.00 | Author: 3.78 | Recency: 7.00

**Links:** [arXiv](https://arxiv.org/abs/2505.15753) | [PDF](https://arxiv.org/pdf/2505.15753)

> 本文提出了一种名为安全上下文检索（SCR）的可扩展防御范式，利用检索增强生成技术来抵御越狱攻击。通过检索少量安全对齐示例，SCR能有效增强模型对抗新旧越狱战术的鲁棒性，显著提升安全性。

---

## #162 — Agentic Moderation: Multi-Agent Design for Safer Vision-Language Models

`C` Score: 6.37 | 2025-10-29

**Authors:** Juan Ren, Mark Dras, Usman Naseem

**Categories:** cs.AI

**Scores:** Citation: 4.42 | Influential: 7.81 | Venue: 5.00 | Author: 9.48 | Recency: 9.00

**Links:** [arXiv](https://arxiv.org/abs/2510.25179) | [PDF](https://arxiv.org/pdf/2510.25179)

> 本文提出了Agentic Moderation框架，通过引入Shield、Responder等专门Agent，构建了一个模型无关的多模态系统防御方案。该方法突破了传统静态二元分类的局限，利用动态协作机制实现了上下文感知和可解释的审核，有效防御越狱攻击。实验表明，该框架在多个数据集上显著降低了攻击成功率并提升了拒绝率，为视觉语言模型提供了鲁棒的安全保障。

---

## #163 — Chain-of-Thought Driven Adversarial Scenario Extrapolation for Robust Language Models

`C` Score: 6.35 | 2025-05-20

**Authors:** Md Rafi Ur Rashid, Vishnu Asutosh Dasu, Ye Wang, Gang Tan, Shagufta Mehnaz

**Categories:** cs.CL

**Scores:** Citation: 4.47 | Influential: 7.81 | Venue: 10.00 | Author: 7.15 | Recency: 7.00

**Links:** [arXiv](https://arxiv.org/abs/2505.17089) | [PDF](https://arxiv.org/pdf/2505.17089)

> 论文引入了对抗性场景外推（ASE）框架，利用思维链推理在推理时增强大模型的鲁棒性。该方法引导模型在生成响应前预演潜在对抗场景并制定防御策略，在保持自然交互的同时有效抵御多种攻击。

---

## #164 — AdvChain: Adversarial Chain-of-Thought Tuning for Robust Safety Alignment of Large Reasoning Models

`C` Score: 6.33 | 2025-09-29

**Authors:** Zihao Zhu, Xinyu Wu, Gehan Hu, Siwei Lyu, Ke Xu, Baoyuan Wu

**Categories:** cs.AI, cs.CL

**Scores:** Citation: 6.55 | Influential: 7.81 | Venue: 2.00 | Author: 6.17 | Recency: 7.00

**Links:** [arXiv](https://arxiv.org/abs/2509.24269) | [PDF](https://arxiv.org/pdf/2509.24269)

> 本文针对大推理模型在思维链安全对齐中存在的“滚雪球效应”，提出了AdvChain对齐范式。该方法通过构建诱惑-纠正和犹豫-纠正样本，利用对抗性思维链微调教导模型进行动态自我纠正，从而在减少过度拒绝的同时显著增强了对越狱攻击和CoT劫持的鲁棒性，实现了更优的安全-效用平衡。

---

## #165 — MetaDefense: Defending Finetuning-based Jailbreak Attack Before and During Generation

`C` Score: 6.29 | 2025-10-09

**Authors:** Weisen Jiang, Sinno Jialin Pan

**Categories:** cs.LG, cs.AI, cs.CL

**Scores:** Citation: 5.59 | Influential: 9.02 | Venue: 2.00 | Author: 7.15 | Recency: 7.00

**Links:** [arXiv](https://arxiv.org/abs/2510.07835) | [PDF](https://arxiv.org/pdf/2510.07835)

> 本文提出了MetaDefense框架，旨在解决大语言模型在面临基于微调的越狱攻击时防御泛化性不足的问题。针对现有机制难以识别未见攻击模板伪装的有害查询，作者利用LLM在嵌入空间的区分能力，创新性地设计了生成前检测与生成中监控的两阶段防御策略。该方法通过训练模型预测查询及部分响应的有害性以实现早期终止，实验证明其在多种模型架构上显著优于现有防御手段。

---

## #166 — SEALGuard: Safeguarding the Multilingual Conversations in Southeast Asian Languages for LLM Software Systems

`C` Score: 6.27 | 2025-07-11

**Authors:** Wenliang Shan, Michael Fu, Rui Yang, Chakkrit Tantithamthavorn

**Categories:** cs.CL, cs.AI

**Scores:** Citation: 4.73 | Influential: 9.02 | Venue: 2.00 | Author: 9.58 | Recency: 7.00

**Links:** [arXiv](https://arxiv.org/abs/2507.08898) | [PDF](https://arxiv.org/pdf/2507.08898)

> 本文提出SEALGuard多语言护栏，解决现有护栏在东南亚语言等低资源语言上的安全对齐不足问题。作者使用LoRA将通用多语言模型调整为护栏，构建包含10种语言26万+提示的SEALSBench基准。实验表明，SEALGuard在检测多语言不安全和越狱提示上显著优于LlamaGuard，提高防御成功率48%。

---

## #167 — SafeText: Safe Text-to-image Models via Aligning the Text Encoder

`C` Score: 6.23 | 2025-02-28

**Authors:** Yuepeng Hu, Zhengyuan Jiang, Neil Zhenqiang Gong

**Categories:** cs.CR, cs.CV

**Scores:** Citation: 7.21 | Influential: 7.81 | Venue: 2.00 | Author: 4.79 | Recency: 5.00

**Links:** [arXiv](https://arxiv.org/abs/2502.20623) | [PDF](https://arxiv.org/pdf/2502.20623)

> SafeText提出了一种新颖的文本到图像模型对齐方法，通过微调文本编码器而非扩散模块来防止有害图像生成。该方法调整不安全提示的嵌入向量，同时最小化对安全提示的影响，使扩散模块在接收不安全提示时仍生成无害图像，而对安全提示生成的图像质量影响很小。

---

## #168 — GUARD:Dual-Agent based Backdoor Defense on Chain-of-Thought in Neural Code Generation

`C` Score: 6.22 | 2025-05-27

**Authors:** Naizhu Jin, Zhong Li, Tian Zhang, Qingkai Zeng

**Categories:** cs.SE

**Scores:** Citation: 5.18 | Influential: 9.02 | Venue: 10.00 | Author: 2.55 | Recency: 7.00

**Links:** [arXiv](https://arxiv.org/abs/2505.21425) | [PDF](https://arxiv.org/pdf/2505.21425)

> 本文提出了GUARD，一个专门针对神经代码生成中思维链后门攻击的双智能体防御框架。该框架包含GUARD-Judge用于识别可疑步骤和触发器，以及GUARD-Repair利用检索增强生成重新生成安全的思维链步骤。实验结果表明，GUARD在有效缓解攻击的同时保持了生成质量，推进了安全代码生成系统的发展。

---

## #169 — Preventing Jailbreak Prompts as Malicious Tools for Cybercriminals: A Cyber Defense Perspective

`C` Score: 6.22 | 2024-11-25

**Authors:** Jean Marie Tshimula, Xavier Ndona, D'Jeff K. Nkashama, Pierre-Martin Tardif, Froduald Kabanza, Marc Frappier et al. (7 total)

**Categories:** cs.CR, cs.CL

**Scores:** Citation: 5.89 | Influential: 7.81 | Venue: 2.00 | Author: 8.73 | Recency: 5.00

**Links:** [arXiv](https://arxiv.org/abs/2411.16642) | [PDF](https://arxiv.org/pdf/2411.16642)

> 本文从网络防御角度分析了越狱提示词作为网络犯罪工具的威胁，探讨了提示注入和上下文操纵等技术及其潜在危害。作者提出了包括高级提示分析、动态安全协议和持续模型微调在内的策略，以加强AI系统的韧性并促进负责任的AI实践。

---

## #170 — Refining Positive and Toxic Samples for Dual Safety Self-Alignment of LLMs with Minimal Human Interventions

`C` Score: 6.20 | 2025-02-08

**Authors:** Jingxin Xu, Guoshun Nan, Sheng Guan, Sicong Leng, Yilian Liu, Zixiao Wang et al. (10 total)

**Categories:** cs.CL, cs.AI

**Scores:** Citation: 4.71 | Influential: 7.81 | Venue: 10.00 | Author: 6.75 | Recency: 5.00

**Links:** [arXiv](https://arxiv.org/abs/2502.08657) | [PDF](https://arxiv.org/pdf/2502.08657)

> 针对现有安全对齐方法依赖人工标注高质量样本的问题，研究者提出PT-ALIGN方法，通过自动优化正面和有毒样本，实现细粒度双指令微调。该方法利用LLM自身迭代生成和优化训练实例，仅需不到50个人类注释。结合最大似然估计和细粒度非似然训练两种损失函数，分别鼓励模型无害内容生成和减少有害词汇输出，显著减少人工监督需求的同时提升模型安全性。

---

## #171 — Enhancing the Safety of Medical Vision-Language Models by Synthetic Demonstrations

`C` Score: 6.20 | 2025-06-08

**Authors:** Zhiyu Xue, Reza Abbasi-Asl, Ramtin Pedarsani

**Categories:** cs.CV, cs.AI

**Scores:** Citation: 4.57 | Influential: 7.81 | Venue: 5.00 | Author: 9.23 | Recency: 7.00

**Links:** [arXiv](https://arxiv.org/abs/2506.09067) | [PDF](https://arxiv.org/pdf/2506.09067)

> 针对医疗视觉语言模型的安全漏洞，本文提出了一种基于合成临床演示的推理时防御策略。该方法利用多模态合成演示来增强模型对视觉和文本越狱攻击的防御能力，同时通过增加演示预算有效缓解了过度防御导致的性能下降问题。

---

## #172 — Proactive defense against LLM Jailbreak

`C` Score: 6.19 | 2025-10-06

**Authors:** Weiliang Zhao, Jinjun Peng, Daniel Ben-Levi, Zhou Yu, Junfeng Yang

**Categories:** cs.CR, cs.CL

**Scores:** Citation: 6.66 | Influential: 9.02 | Venue: 2.00 | Author: 3.23 | Recency: 7.00

**Links:** [arXiv](https://arxiv.org/abs/2510.05052) | [PDF](https://arxiv.org/pdf/2510.05052)

> 针对现有防御手段难以应对多轮迭代越狱攻击的问题，本文提出了 ProAct 这一新型主动防御框架。其核心创新在于通过故意生成“虚假响应”来误导攻击者，使其误以为模型已被攻破，从而向攻击者的内部优化循环提供错误信号，有效破坏攻击逻辑并迫使对抗性搜索提前终止。广泛的实验证明，该方法在多种先进大语言模型和越狱框架下均能显著提升模型的安全性。

---

## #173 — Enhancing Model Defense Against Jailbreaks with Proactive Safety Reasoning

`C` Score: 6.18 | 2025-01-31

**Authors:** Xianglin Yang, Gelei Deng, Jieming Shi, Tianwei Zhang, Jin Song Dong

**Categories:** cs.CR, cs.AI

**Scores:** Citation: 6.75 | Influential: 7.81 | Venue: 2.00 | Author: 5.88 | Recency: 5.00

**Links:** [arXiv](https://arxiv.org/abs/2501.19180) | [PDF](https://arxiv.org/pdf/2501.19180)

> 本文提出了一种名为安全思维链(SCoT)的新型防御策略，利用大语言模型增强的推理能力主动评估有害输入，而非简单阻止。通过分析请求意图，SCoT显著提升了模型对各种有害查询的泛化能力，实验表明其能有效减少对抗操纵脆弱性，同时保持强大的通用能力。

---

## #174 — Agents Are All You Need for LLM Unlearning

`C` Score: 6.18 | 2025-02-01

**Authors:** Debdeep Sanyal, Murari Mandal

**Categories:** cs.AI, cs.CL

**Scores:** Citation: 7.31 | Influential: 9.02 | Venue: 2.00 | Author: 2.55 | Recency: 5.00

**Links:** [arXiv](https://arxiv.org/abs/2502.00406) | [PDF](https://arxiv.org/pdf/2502.00406)

> 这篇论文提出了ALU方法，一种基于多agent的LLM unlearning技术，通过多个专门设计的LLM agents协作实现信息移除，无需重新训练或修改模型权重。该方法有效解决了传统unlearning方法在效果与实用性之间的平衡问题，为AI监管、法律合规、安全性和隐私保护提供了新的解决方案。

---

## #175 — PeerGuard: Defending Multi-Agent Systems Against Backdoor Attacks Through Mutual Reasoning

`C` Score: 6.18 | 2025-05-16

**Authors:** Falong Fan, Xi Li

**Categories:** cs.MA, cs.AI, cs.LG

**Scores:** Citation: 6.98 | Influential: 7.81 | Venue: 5.00 | Author: 1.86 | Recency: 7.00

**Links:** [arXiv](https://arxiv.org/abs/2505.11642) | [PDF](https://arxiv.org/pdf/2505.11642)

> 本文针对多智能体系统中的后门攻击漏洞进行研究，提出了一种名为PeerGuard的防御机制。该机制利用智能体的推理能力，通过让每个智能体评估其他智能体的响应来检测不合逻辑的推理过程，从而识别出被投毒的恶意智能体。在基于ChatGPT和Llama 3的多智能体系统实验中，该方法在准确识别中毒智能体的同时，有效降低了对干净智能体的误报率，为多智能体系统的安全性提供了新思路。

---

## #176 — Randomized Smoothing Meets Vision-Language Models

`C` Score: 6.17 | 2025-09-19

**Authors:** Emmanouil Seferis, Changshun Wu, Stefanos Kollias, Saddek Bensalem, Chih-Hong Cheng

**Categories:** cs.LG

**Scores:** Citation: 3.32 | Influential: 7.81 | Venue: 10.00 | Author: 9.41 | Recency: 7.00

**Links:** [arXiv](https://arxiv.org/abs/2509.16088) | [PDF](https://arxiv.org/pdf/2509.16088)

> 本文将随机平滑技术应用于视觉语言模型，通过将生成输出连接到预言机分类任务来实现鲁棒性认证。作者建立了样本数量与鲁棒性半径之间的理论关系，证明了在较弱假设下仍可保持较高的计算效率。该研究为VLMs提供了针对对抗性攻击的明确定义且计算可行的鲁棒性认证方法。

---

## #177 — The Trigger in the Haystack: Extracting and Reconstructing LLM Backdoor Triggers

`C` Score: 6.17 | 2026-02-03

**Authors:** Blake Bullwinkel, Giorgio Severi, Keegan Hines, Amanda Minnich, Ram Shankar Siva Kumar, Yonatan Zunger

**Categories:** cs.CR, cs.AI

**Scores:** Citation: 6.15 | Influential: 7.81 | Venue: 2.00 | Author: 4.27 | Recency: 10.00

**Links:** [arXiv](https://arxiv.org/abs/2602.03085) | [PDF](https://arxiv.org/pdf/2602.03085)

> 本文提出了一种实用的扫描器，用于识别因果语言模型中的“潜伏Agent”式后门。该方法基于潜伏Agent倾向于记忆中毒数据，且在存在后门触发器时表现出独特的输出分布和注意力头模式这两个发现，实现了无需先验知识且仅需推理操作的可扩展后门扫描。实验表明，该方法能在多种后门场景和模型中恢复有效的触发器。

---

## #178 — Generative Adversarial Post-Training Mitigates Reward Hacking in Live Human-AI Music Interaction

`C` Score: 6.15 | 2025-11-22

**Authors:** Yusong Wu, Stephen Brade, Aleksandra Teng Ma, Tia-Jane Fowler, Enning Yang, Berker Banar et al. (9 total)

**Categories:** cs.LG, cs.SD

**Scores:** Citation: 4.67 | Influential: 7.81 | Venue: 2.00 | Author: 9.23 | Recency: 9.00

**Links:** [arXiv](https://arxiv.org/abs/2511.17879) | [PDF](https://arxiv.org/pdf/2511.17879)

> 这篇论文针对实时人机音乐交互中强化学习后训练常见的“奖励黑客”问题，提出了一种基于生成对抗的新型后训练方法。由于传统RL往往牺牲输出多样性以最大化奖励，导致音乐创造力丧失，作者引入共同进化的判别器来评估策略轨迹，从而有效缓解了这一现象。该方法在保持模型实时适应性的同时，显著提升了音乐伴奏的动态变化与多样性，确保了创造性交互的流畅性。

---

## #179 — Proactive Hardening of LLM Defenses with HASTE

`C` Score: 6.15 | 2026-01-27

**Authors:** Henry Chen, Victor Aranda, Samarth Keshari, Ryan Heartfield, Nicole Nichols

**Categories:** cs.CR

**Scores:** Citation: 5.93 | Influential: 7.81 | Venue: 2.00 | Author: 4.79 | Recency: 10.00

**Links:** [arXiv](https://arxiv.org/abs/2601.19051) | [PDF](https://arxiv.org/pdf/2601.19051)

> 本文提出了HASTE框架，通过迭代生成高度规避的提示词，在运行时持续优化LLM的防御能力。该框架采用模块化优化过程，能够动态地对提示注入检测系统进行压力测试，从而有效识别弱点并增强防御态势。实验表明，HASTE能显著减少恶意提示的检测遗漏，并在较少的迭代循环中优化检测模型的效能。

---

## #180 — Toward a Dynamic Stackelberg Game-Theoretic Framework for Agentic AI Defense Against LLM Jailbreaking

`C` Score: 6.14 | 2025-07-10

**Authors:** Zhengye Han, Quanyan Zhu

**Categories:** cs.AI

**Scores:** Citation: 6.38 | Influential: 7.81 | Venue: 2.00 | Author: 5.40 | Recency: 7.00

**Links:** [arXiv](https://arxiv.org/abs/2507.08207) | [PDF](https://arxiv.org/pdf/2507.08207)

> 本文提出博弈论框架，将提示工程师和LLM交互建模为扩展形式游戏，结合提示空间上的RRT搜索。将RRT探索嵌入游戏捕获越狱策略发现和模型战略响应，通过局部Stackelberg均衡条件解释防御者行为，为评估、解释和加强LLM护栏提供理论基础，Purple Agent防御机制基于此框架构建。

---

## #181 — Probing the Robustness of Large Language Models Safety to Latent Perturbations

`C` Score: 6.12 | 2025-06-19

**Authors:** Tianle Gu, Kexin Huang, Zongqi Wang, Yixu Wang, Jie Li, Yuanqi Yao et al. (10 total)

**Categories:** cs.LG, cs.AI, cs.CL

**Scores:** Citation: 6.16 | Influential: 7.81 | Venue: 2.00 | Author: 5.88 | Recency: 7.00

**Links:** [arXiv](https://arxiv.org/abs/2506.16078) | [PDF](https://arxiv.org/pdf/2506.16078)

> 本文探讨了安全对齐对潜在扰动的鲁棒性，指出微小的潜在偏移仍能触发不安全响应。作者引入了一种探测方法量化潜在空间的局部敏感性，并构建了激活转向攻击（ASA）。此外，提出了分层对抗补丁训练（LAPT）策略，通过在训练中注入受控扰动来增强对齐鲁棒性，为改进对齐范式提供了原则性基础。

---

## #182 — GenTel-Safe: A Unified Benchmark and Shielding Framework for Defending Against Prompt Injection Attacks

`C` Score: 6.10 | 2024-09-29

**Authors:** Rongchang Li, Minjie Chen, Chang Hu, Han Chen, Wenpeng Xing, Meng Han

**Categories:** cs.CR, cs.LG

**Scores:** Citation: 6.39 | Influential: 9.02 | Venue: 2.00 | Author: 4.79 | Recency: 5.00

**Links:** [arXiv](https://arxiv.org/abs/2409.19521) | [PDF](https://arxiv.org/pdf/2409.19521)

> 本文提出了GenTel-Safe统一框架，包含一种新颖的提示注入攻击检测方法GenTel-Shield以及包含84812次攻击的综合评估基准GenTel-Bench。实验表明，GenTel-Shield在攻击检测成功率上达到了最先进水平，有效揭示了现有安全护栏技术面对有害提示时的关键弱点。

---

## #183 — Root Defence Strategies: Ensuring Safety of LLM at the Decoding Level

`C` Score: 6.10 | 2024-10-09

**Authors:** Xinyi Zeng, Yuying Shang, Jiawei Chen, Jingyuan Zhang, Yu Tian

**Categories:** cs.CL, cs.CR

**Scores:** Citation: 7.69 | Influential: 7.81 | Venue: 2.00 | Author: 2.55 | Recency: 5.00

**Links:** [arXiv](https://arxiv.org/abs/2410.06809) | [PDF](https://arxiv.org/pdf/2410.06809)

> 本文针对现有防御方法在预填充级别判断有害响应的局限性，提出了一种在解码级别运行的鲁棒防御机制。该机制采用面向解码器的逐步防御架构，利用模型识别有害信息的能力直接纠正有害查询而非简单拒绝，并引入投机解码提升安全解码速度。实验证明，该方法在不牺牲推理速度的前提下提高了模型安全性，并在保持模型有用性方面优于现有方法。

---

## #184 — SafeInt: Shielding Large Language Models from Jailbreak Attacks via Safety-Aware Representation Intervention

`C` Score: 6.08 | 2025-02-21

**Authors:** Jiaqi Wu, Chen Chen, Chunyan Hou, Xiaojie Yuan

**Categories:** cs.CL

**Scores:** Citation: 4.75 | Influential: 7.81 | Venue: 10.00 | Author: 5.88 | Recency: 5.00

**Links:** [arXiv](https://arxiv.org/abs/2502.15594) | [PDF](https://arxiv.org/pdf/2502.15594)

> 本文提出SafeIntervention(SafeInt)，一种新的防御方法，通过安全感知的表示干预来保护LLM免受越狱攻击。基于对越狱样本表示的分析，SafeInt将越狱相关表示重新定位到拒绝区域，通过干预越狱样本的表示分布使其与不安全样本对齐。在六种越狱攻击、两个越狱数据集和两个效用基准上的全面实验表明，SafeInt在防御越狱攻击方面优于所有基线，同时 largely 保持效用，并且在对抗攻击和实时攻击缓解中表现出色。

---

## #185 — Helping Large Language Models Protect Themselves: An Enhanced Filtering and Summarization System

`C` Score: 6.08 | 2025-05-02

**Authors:** Sheikh Samit Muhaimin, Spyridon Mastorakis

**Categories:** cs.CL, cs.AI

**Scores:** Citation: 4.40 | Influential: 7.81 | Venue: 5.00 | Author: 8.93 | Recency: 7.00

**Links:** [arXiv](https://arxiv.org/abs/2505.01315) | [PDF](https://arxiv.org/pdf/2505.01315)

> 本文提出了一种无需重新训练的防御框架，帮助大语言模型识别、过滤和防御对抗性输入。该框架结合了高级NLP技术的提示过滤模块和对抗性文献摘要模块，通过提供上下文感知的防御知识，显著提高了模型对编码恶意输入和操纵性提示的识别率和拒绝率。

---

## #186 — Aligning Machiavellian Agents: Behavior Steering via Test-Time Policy Shaping

`C` Score: 6.07 | 2025-11-14

**Authors:** Dena Mujtaba, Brian Hu, Anthony Hoogs, Arslan Basharat

**Categories:** cs.AI, cs.CL

**Scores:** Citation: 3.32 | Influential: 7.81 | Venue: 10.00 | Author: 7.43 | Recency: 9.00

**Links:** [arXiv](https://arxiv.org/abs/2511.11551) | [PDF](https://arxiv.org/pdf/2511.11551)

> 本文提出了一种基于模型引导策略塑形的测试时对齐技术，用于在无需重新训练的情况下引导预训练智能体的行为。该方法允许精确控制个体行为属性，在多样化的强化学习环境中实现伦理对齐与奖励最大化之间的原则性权衡。在MACHIAVELLI基准上的评估表明，该方法能有效确保决策符合伦理属性，优于先前的训练时方法和通用智能体。

---

## #187 — Multilingual Collaborative Defense for Large Language Models

`C` Score: 6.06 | 2025-05-17

**Authors:** Hongliang Li, Jinan Xu, Gengping Cui, Changhao Guan, Fengran Mo, Kaiyu Huang

**Categories:** cs.CL, cs.AI

**Scores:** Citation: 3.62 | Influential: 7.81 | Venue: 10.00 | Author: 7.80 | Recency: 7.00

**Links:** [arXiv](https://arxiv.org/abs/2505.11835) | [PDF](https://arxiv.org/pdf/2505.11835)

> 本文针对大语言模型通过翻译成稀有语言进行越狱的漏洞，提出了多语言协作防御（MCD）方法。该方法通过分析不同语言间的攻击特征相关性，自动优化连续软安全提示，以增强模型的多语言安全性。MCD不仅有效提升了多语言防御性能，还在保持强泛化能力的同时降低了误拒率。

---

## #188 — DiffuGuard: How Intrinsic Safety is Lost and Found in Diffusion Large Language Models

`C` Score: 6.06 | 2025-09-29

**Authors:** Zherui Li, Zheng Nie, Zhenhong Zhou, Yue Liu, Yitong Zhang, Yu Cheng et al. (10 total)

**Categories:** cs.CL, cs.AI

**Scores:** Citation: 5.40 | Influential: 9.02 | Venue: 2.00 | Author: 6.17 | Recency: 7.00

**Links:** [arXiv](https://arxiv.org/abs/2509.24296) | [PDF](https://arxiv.org/pdf/2509.24296)

> 本文深入分析了扩散大语言模型（dLLM）在越狱攻击下的脆弱性，揭示了标准贪婪重掩码策略的有害偏差和去噪路径依赖现象。为此，作者提出了无需训练的DiffuGuard防御框架，通过随机退火重掩码和块级审计修复，有效降低了攻击成功率并释放了模型的内在安全潜力，同时保持了模型效用。

---

## #189 — Spot Risks Before Speaking! Unraveling Safety Attention Heads in Large Vision-Language Models

`C` Score: 6.04 | 2025-01-03

**Authors:** Ziwei Zheng, Junyao Zhao, Le Yang, Lijun He, Fan Li

**Categories:** cs.LG, cs.AI, cs.CR

**Scores:** Citation: 5.63 | Influential: 7.81 | Venue: 2.00 | Author: 8.33 | Recency: 5.00

**Links:** [arXiv](https://arxiv.org/abs/2501.02029) | [PDF](https://arxiv.org/pdf/2501.02029)

> 该研究发现大型视觉语言模型(LVLMs)在生成第一个token时的内部激活能有效识别恶意提示，这种安全感知由稀疏的'safety heads'注意力头控制。这些安全头作为对抗恶意提示的专用盾牌，移除它们会提高攻击成功率而不影响模型实用性，通过定位这些安全头并连接其激活，作者构建了一个简单但强大的恶意提示检测器，可无缝集成到生成过程中。

---

## #190 — Basic Legibility Protocols Improve Trusted Monitoring

`C` Score: 6.02 | 2026-02-09

**Authors:** Ashwin Sreevatsa, Sebastian Prasanna, Cody Rushing

**Categories:** cs.CR, cs.LG, cs.SE

**Scores:** Citation: 6.40 | Influential: 7.81 | Venue: 2.00 | Author: 2.55 | Recency: 10.00

**Links:** [arXiv](https://arxiv.org/abs/2602.10153) | [PDF](https://arxiv.org/pdf/2602.10153)

> 针对AI控制中可信监控成本高昂且难以理解复杂行为的问题，本文提出了“可读性协议”，鼓励不可信模型采取易于监控器评估的行动方式。在代码编写场景中，研究发现要求模型添加注释的协议能显著提升安全性，且诚实的代码比植入后门的代码更容易通过注释消除怀疑。该方法利用了强监控器区分真实理由与表面合理性的能力，在不牺牲任务性能的前提下增强了监控效果。

---

## #191 — When Models Outthink Their Safety: Unveiling and Mitigating Self-Jailbreak in Large Reasoning Models

`C` Score: 6.01 | 2025-10-24

**Authors:** Yingzhi Mao, Chunkang Zhang, Junxiang Wang, Xinyan Guan, Boxi Cao, Yaojie Lu et al. (9 total)

**Categories:** cs.AI, cs.CL

**Scores:** Citation: 4.39 | Influential: 7.81 | Venue: 2.00 | Author: 9.13 | Recency: 9.00

**Links:** [arXiv](https://arxiv.org/abs/2510.21285) | [PDF](https://arxiv.org/pdf/2510.21285)

> 本文揭示了大型推理模型中的“自我越狱”现象，即模型在推理步骤中覆盖初始的安全判断。针对此问题，提出了轨迹级训练框架Chain-of-Guardrail（CoG），通过针对性的步骤级干预来缓解自我越狱，在保持推理能力的同时提升了安全性。

---

## #192 — Safety Alignment of LMs via Non-cooperative Games

`C` Score: 6.01 | 2025-12-23

**Authors:** Anselm Paulus, Ilia Kulikov, Brandon Amos, Rémi Munos, Ivan Evtimov, Kamalika Chaudhuri et al. (7 total)

**Categories:** cs.AI

**Scores:** Citation: 5.05 | Influential: 7.81 | Venue: 2.00 | Author: 7.15 | Recency: 9.00

**Links:** [arXiv](https://arxiv.org/abs/2512.20806) | [PDF](https://arxiv.org/pdf/2512.20806)

> 本文提出了一种新的安全对齐范式，将语言模型的安全性对齐构建为攻击者模型与防御者模型之间的非零和博弈。该方法通过在线强化学习联合训练两个模型，使其持续适应对方的策略，利用基于偏好的奖励信号提供更稳健的监督。实验结果表明，该方法能同时提升模型的有用性和对抗攻击的韧性，生成的攻击者模型也可作为通用的红队测试工具。

---

## #193 — JailDAM: Jailbreak Detection with Adaptive Memory for Vision-Language Model

`C` Score: 5.99 | 2025-04-03

**Authors:** Yi Nian, Shenzhe Zhu, Yuehan Qin, Li Li, Ziyi Wang, Chaowei Xiao et al. (7 total)

**Categories:** cs.CR, cs.AI

**Scores:** Citation: 5.60 | Influential: 9.02 | Venue: 2.00 | Author: 6.47 | Recency: 5.00

**Links:** [arXiv](https://arxiv.org/abs/2504.03770) | [PDF](https://arxiv.org/pdf/2504.03770)

> 针对视觉语言模型面临的越狱攻击风险，本文提出了JAILDAM，一种基于测试时自适应记忆的越狱检测框架。该方法利用策略驱动的有害知识表示，无需显式接触有害数据即可动态更新不安全知识，从而在保持效率的同时提高对未见越狱策略的泛化能力。实验表明，JAILDAM在多个VLM越狱基准测试中实现了最先进的性能，有效提升了有害内容检测的准确性和速度。

---

## #194 — STAR-S: Improving Safety Alignment through Self-Taught Reasoning on Safety Rules

`C` Score: 5.99 | 2026-01-07

**Authors:** Di Wu, Yanyan Zhao, Xin Lu, Mingzhe Li, Bing Qin

**Categories:** cs.AI, cs.CL

**Scores:** Citation: 5.33 | Influential: 7.81 | Venue: 2.00 | Author: 6.17 | Recency: 9.00

**Links:** [arXiv](https://arxiv.org/abs/2601.03537) | [PDF](https://arxiv.org/pdf/2601.03537)

> 本文提出了STAR-S框架，通过基于安全规则的自教推理循环来增强模型的安全性。该框架通过引导模型进行安全规则推理和反思，并利用微调不断改进推理能力，从而形成协同循环，有效防御越狱攻击，实验表现优于现有基线方法。

---

## #195 — RedDebate: Safer Responses through Multi-Agent Red Teaming Debates

`C` Score: 5.98 | 2025-06-04

**Authors:** Ali Asad, Stephen Obadinma, Radin Shayanfar, Xiaodan Zhu

**Categories:** cs.CL

**Scores:** Citation: 6.73 | Influential: 7.81 | Venue: 2.00 | Author: 3.23 | Recency: 7.00

**Links:** [arXiv](https://arxiv.org/abs/2506.11083) | [PDF](https://arxiv.org/pdf/2506.11083)

> 本文提出了RedDebate框架，利用多Agent辩论机制让大模型相互批判推理，从而自动识别并减轻不安全行为。该框架集成长期记忆模块以保留安全相关见解，并在后续推理中持续优化模型行为。实验表明，RedDebate显著减少了不安全输出，是首个统一多Agent辩论和红队测试的自动化框架。

---

## #196 — AgentAlign: Navigating Safety Alignment in the Shift from Informative to Agentic Large Language Models

`C` Score: 5.97 | 2025-05-29

**Authors:** Jinchuan Zhang, Lu Yin, Yan Zhou, Songlin Hu

**Categories:** cs.CR, cs.AI, cs.CL

**Scores:** Citation: 5.99 | Influential: 7.81 | Venue: 2.00 | Author: 5.40 | Recency: 7.00

**Links:** [arXiv](https://arxiv.org/abs/2505.23020) | [PDF](https://arxiv.org/pdf/2505.23020)

> 本文提出了AgentAlign框架，旨在解决LLM智能体从信息提供者转变为行动执行者过程中面临的安全对齐缺失问题。该框架利用抽象行为链在模拟环境中合成安全对齐数据，通过实例化工具生成真实指令并校准有用性与无害性的边界。实验表明，该方法在显著提升模型安全性的同时，最小化了对模型有用性的影响。

---

## #197 — From Moderation to Mediation: Can LLMs Serve as Mediators in Online Flame Wars?

`C` Score: 5.96 | 2025-12-02

**Authors:** Dawei Li, Abdullah Alnaibari, Arslan Bisharat, Manny Sandoval, Deborah Hall, Yasin Silva et al. (7 total)

**Categories:** cs.AI

**Scores:** Citation: 6.47 | Influential: 7.81 | Venue: 2.00 | Author: 2.55 | Recency: 9.00

**Links:** [arXiv](https://arxiv.org/abs/2512.03005) | [PDF](https://arxiv.org/pdf/2512.03005)

> 本文探讨了LLM是否不仅能作为有害内容的审核者，还能作为调解者来理解和缓解在线冲突。该框架将调解分解为判断和引导两个子任务，并构建了基于Reddit的数据集和多阶段评估流程，实验表明API模型在推理和干预对齐方面优于开源模型。

---

## #198 — MirrorGuard: Toward Secure Computer-Use Agents via Simulation-to-Real Reasoning Correction

`C` Score: 5.95 | 2026-01-19

**Authors:** Wenqi Zhang, Yulin Shen, Changyue Jiang, Jiarun Dai, Geng Hong, Xudong Pan

**Categories:** cs.AI

**Scores:** Citation: 5.72 | Influential: 7.81 | Venue: 2.00 | Author: 4.79 | Recency: 9.00

**Links:** [arXiv](https://arxiv.org/abs/2601.12822) | [PDF](https://arxiv.org/pdf/2601.12822)

> 本文提出了MirrorGuard，一种通过模拟到现实的推理修正来保护计算机使用Agent（CUA）的防御框架。该框架利用神经符号模拟管道生成高风险交互轨迹，在不执行真实操作的情况下学习拦截和修正不安全推理链。实验表明，MirrorGuard能显著降低CUA的不安全率，同时保持较低的误拒绝率，有效提升了GUI交互Agent的安全性。

---

## #199 — Exposing the Ghost in the Transformer: Abnormal Detection for Large Language Models via Hidden State Forensics

`C` Score: 5.94 | 2025-04-01

**Authors:** Shide Zhou, Kailong Wang, Ling Shi, Haoyu Wang

**Categories:** cs.CR

**Scores:** Citation: 4.26 | Influential: 9.02 | Venue: 10.00 | Author: 4.79 | Recency: 5.00

**Links:** [arXiv](https://arxiv.org/abs/2504.00446) | [PDF](https://arxiv.org/pdf/2504.00446)

> 本文提出了一种通过隐藏状态取证来检测大语言模型异常行为的新方法，通过系统检查特定层的激活模式来识别幻觉、越狱攻击和后门利用等安全威胁。该通用框架能够在不产生过高计算成本的情况下高效实时地识别多种安全威胁，检测准确率超过95%。这项工作为强化LLM集成系统的安全性提供了一种有前景的策略，有助于在关键领域实现更安全可靠的部署。

---

## #200 — Speculative Safety-Aware Decoding

`C` Score: 5.93 | 2025-08-25

**Authors:** Xuekang Wang, Shengyu Zhu, Xueqi Cheng

**Categories:** cs.LG, cs.AI

**Scores:** Citation: 5.01 | Influential: 9.02 | Venue: 10.00 | Author: 1.12 | Recency: 7.00

**Links:** [arXiv](https://arxiv.org/abs/2508.17739) | [PDF](https://arxiv.org/pdf/2508.17739)

> 本文提出了推测安全感知解码（SSD），一种轻量级的解码时防御方法。该方法利用具备安全属性的小型模型进行推测采样，量化越狱风险并动态切换解码策略，从而在加速推理的同时赋予大模型所需的安全性。实验证明，SSD能有效防御攻击并保持对良性查询的有益性。

---

## #201 — Unraveling LLM Jailbreaks Through Safety Knowledge Neurons

`C` Score: 5.93 | 2025-09-01

**Authors:** Chongwen Zhao, Yutong Ke, Kaizhu Huang

**Categories:** cs.AI

**Scores:** Citation: 6.14 | Influential: 9.02 | Venue: 5.00 | Author: 1.12 | Recency: 7.00

**Links:** [arXiv](https://arxiv.org/abs/2509.01631) | [PDF](https://arxiv.org/pdf/2509.01631)

> 本文提出了一种关注安全知识神经元的可解释性方法，揭示了越狱攻击的内部机制。研究发现调整安全相关神经元的激活可有效控制模型行为，并据此提出了SafeTuning微调策略，通过强化安全关键神经元显著提升了模型对越狱攻击的鲁棒性。

---

## #202 — Attention Slipping: A Mechanistic Understanding of Jailbreak Attacks and Defenses in LLMs

`C` Score: 5.90 | 2025-07-06

**Authors:** Xiaomeng Hu, Pin-Yu Chen, Tsung-Yi Ho

**Categories:** cs.CR, cs.AI, cs.CL

**Scores:** Citation: 4.72 | Influential: 9.02 | Venue: 2.00 | Author: 7.15 | Recency: 7.00

**Links:** [arXiv](https://arxiv.org/abs/2507.04365) | [PDF](https://arxiv.org/pdf/2507.04365)

> 本文揭示了越狱攻击中的“注意力滑移”现象，即模型在攻击过程中逐渐减少对不安全请求的关注。基于此机制，作者提出了注意力锐化防御方法，在不增加计算开销的情况下有效抵抗多种越狱攻击，同时保持了良性任务的性能。

---

## #203 — AgentBreeder: Mitigating the AI Safety Risks of Multi-Agent Scaffolds via Self-Improvement

`C` Score: 5.88 | 2025-02-02

**Authors:** J Rosser, Jakob Foerster

**Categories:** cs.CR, cs.AI, cs.NE

**Scores:** Citation: 6.77 | Influential: 7.81 | Venue: 2.00 | Author: 3.78 | Recency: 5.00

**Links:** [arXiv](https://arxiv.org/abs/2502.00757) | [PDF](https://arxiv.org/pdf/2502.00757)

> AgentBreeder是一个多目标自我改进进化搜索框架，旨在减轻多智能体支架的AI安全风险。研究通过在推理、数学和安全基准测试上的评估，发现该框架在'蓝色'模式下可提升安全性能79.4%同时保持能力，在'红色'模式下则揭示对抗性弱支架与能力优化的共存现象，为多智能体系统的安全对齐提供了新思路。

---

## #204 — Reasoned Safety Alignment: Ensuring Jailbreak Defense via Answer-Then-Check

`C` Score: 5.86 | 2025-09-15

**Authors:** Chentao Cao, Xiaojun Xu, Bo Han, Hang Li

**Categories:** cs.LG, cs.AI

**Scores:** Citation: 6.30 | Influential: 7.81 | Venue: 2.00 | Author: 3.78 | Recency: 7.00

**Links:** [arXiv](https://arxiv.org/abs/2509.11629) | [PDF](https://arxiv.org/pdf/2509.11629)

> 本文提出了一种名为“先回答后检查”的安全对齐方法，通过构建包含8万个样本的ReSA数据集，教导模型在生成最终答案前先在思维中直接回答并批判性地评估其安全性。实验表明，该方法在提高安全能力的同时降低了过度拒绝率，并保持了模型的一般推理能力。

---

## #205 — ALMGuard: Safety Shortcuts and Where to Find Them as Guardrails for Audio-Language Models

`C` Score: 5.86 | 2025-10-30

**Authors:** Weifei Jin, Yuxin Cao, Junjie Su, Minhui Xue, Jie Hao, Ke Xu et al. (8 total)

**Categories:** cs.SD, cs.CR, cs.LG

**Scores:** Citation: 5.85 | Influential: 7.81 | Venue: 2.00 | Author: 3.78 | Recency: 9.00

**Links:** [arXiv](https://arxiv.org/abs/2510.26096) | [PDF](https://arxiv.org/pdf/2510.26096)

> 针对音频语言模型面临的新型漏洞及现有防御失效的问题，本文提出了首个专为ALMs定制的防御框架ALMGuard。该框架基于模型中存在安全捷径的假设，设计了通用捷径激活扰动作为触发器，在推理时激活安全机制以保护模型。此外，作者还提出了Mel-梯度稀疏掩码技术，旨在筛选有效触发器的同时，最大程度保留模型在良性任务上的效用。

---

## #206 — Adversarial Attack-Defense Co-Evolution for LLM Safety Alignment via Tree-Group Dual-Aware Search and Optimization

`C` Score: 5.86 | 2025-11-24

**Authors:** Xurui Li, Kaisong Song, Rui Zhu, Pin-Yu Chen, Haixu Tang

**Categories:** cs.CR, cs.AI

**Scores:** Citation: 6.25 | Influential: 7.81 | Venue: 2.00 | Author: 2.55 | Recency: 9.00

**Links:** [arXiv](https://arxiv.org/abs/2511.19218) | [PDF](https://arxiv.org/pdf/2511.19218)

> 针对现有LLM安全研究忽视攻防动态交互的问题，本文提出了ACE-Safety框架，通过协同进化机制联合优化攻击与防御模型。该框架创新性地引入了组感知策略引导的蒙特卡洛树搜索（GS-MCTS）来高效生成对抗样本，并利用对抗课程树感知组策略优化（AC-TGPO）实现攻击与防御模型的联合强化学习训练。实验证明该方法能有效提升模型在动态威胁环境下的安全对齐能力。

---

## #207 — Breaking Bad Tokens: Detoxification of LLMs Using Sparse Autoencoders

`C` Score: 5.84 | 2025-05-20

**Authors:** Agam Goyal, Vedant Rathi, William Yeh, Yian Wang, Yuen Chen, Hari Sundaram

**Categories:** cs.CL

**Scores:** Citation: 4.47 | Influential: 7.81 | Venue: 10.00 | Author: 3.78 | Recency: 7.00

**Links:** [arXiv](https://arxiv.org/abs/2505.14536) | [PDF](https://arxiv.org/pdf/2505.14536)

> 论文利用稀疏自编码器识别模型残差流中的毒性方向，并提出基于解码器向量的有针对性的激活引导方法。该方法在降低毒性方面优于基线，同时保持了模型的知识和通用能力，但也指出了特征解耦的重要性。

---

## #208 — ShieldLearner: A New Paradigm for Jailbreak Attack Defense in LLMs

`C` Score: 5.83 | 2025-02-16

**Authors:** Ziyi Ni, Hao Wang, Huacan Wang

**Categories:** cs.CR, cs.AI, cs.CL

**Scores:** Citation: 6.84 | Influential: 7.81 | Venue: 2.00 | Author: 3.23 | Recency: 5.00

**Links:** [arXiv](https://arxiv.org/abs/2502.13162) | [PDF](https://arxiv.org/pdf/2502.13162)

> ShieldLearner是一种新型防御范式，针对大型语言模型面临的越狱攻击问题。该系统通过试错机制自主提炼攻击特征形成模式图谱，并将防御启发式方法合成为元分析框架，实现了系统化和可解释的威胁检测。此外，引入的自适应对抗增强技术能够生成已成功防御提示的对抗性变体，使模型能够在无需重训练的情况下实现持续自我改进，有效应对不断演变的威胁。

---

## #209 — ReGA: Representation-Guided Abstraction for Model-based Safeguarding of LLMs

`C` Score: 5.83 | 2025-06-02

**Authors:** Zeming Wei, Chengcan Wu, Meng Sun

**Categories:** cs.CR, cs.AI, cs.LG

**Scores:** Citation: 5.24 | Influential: 7.81 | Venue: 2.00 | Author: 6.75 | Recency: 7.00

**Links:** [arXiv](https://arxiv.org/abs/2506.01770) | [PDF](https://arxiv.org/pdf/2506.01770)

> 提出了一种基于模型的LLM安全防护框架ReGA，利用安全关键表示指导抽象过程以解决可扩展性问题。该方法通过分析隐藏状态中的低维安全概念，有效区分有害输入，在保持高准确率的同时增强了对越狱攻击的鲁棒性。

---

## #210 — ToolRM: Towards Agentic Tool-Use Reward Modeling

`C` Score: 5.83 | 2025-10-30

**Authors:** Renhao Li, Jianhong Tu, Yang Su, Yantao Liu, Fei Huang, Hamid Alinejad-Rokny et al. (9 total)

**Categories:** cs.AI, cs.CL

**Scores:** Citation: 4.43 | Influential: 7.81 | Venue: 2.00 | Author: 7.80 | Recency: 9.00

**Links:** [arXiv](https://arxiv.org/abs/2510.26167) | [PDF](https://arxiv.org/pdf/2510.26167)

> 本文提出了ToolRM，一系列专为通用工具使用场景定制的轻量级奖励模型，旨在解决函数调用任务中缺乏专用奖励模型的问题。作者设计了一种新颖的数据构建流程，利用基于规则的评分和多维采样生成了高质量、多样化的成对偏好数据集ToolPref-Pairwise-30K，并推出了评估基准TRBench$_{BFCL}$。实验表明，基于该数据训练的Qwen3系列模型在工具调用的奖励判断上显著优于前沿大模型和现有奖励模型。

---

## #211 — Protect: Towards Robust Guardrailing Stack for Trustworthy Enterprise LLM Systems

`C` Score: 5.82 | 2025-10-15

**Authors:** Karthik Avinash, Nikhil Pareek, Rishav Hada

**Categories:** cs.CL, cs.AI

**Scores:** Citation: 5.65 | Influential: 7.81 | Venue: 2.00 | Author: 5.40 | Recency: 7.00

**Links:** [arXiv](https://arxiv.org/abs/2510.13351) | [PDF](https://arxiv.org/pdf/2510.13351)

> 本文介绍了Protect，一个专为大规模企业部署设计的原生多模态护栏模型，能够无缝处理文本、图像和音频输入。该模型通过LoRA微调特定适配器，在毒性、性别歧视、数据隐私和提示注入等维度上实现了最先进的性能，为企业级可信AI系统奠定了基础。

---

## #212 — AprielGuard

`C` Score: 5.82 | 2025-12-23

**Authors:** Jaykumar Kasundra, Anjaneya Praharaj, Sourabh Surana, Lakshmi Sirisha Chodisetty, Sourav Sharma, Abhigya Verma et al. (14 total)

**Categories:** cs.CL

**Scores:** Citation: 5.05 | Influential: 9.02 | Venue: 2.00 | Author: 4.27 | Recency: 9.00

**Links:** [arXiv](https://arxiv.org/abs/2512.20293) | [PDF](https://arxiv.org/pdf/2512.20293)

> 本文介绍了AprielGuard，一个80亿参数的统一安全护栏模型，旨在同时处理安全风险（如毒性、偏见）和对抗性威胁（如提示注入、越狱）。该模型在多样化的数据集上训练，并集成了结构化推理轨迹以提高可解释性。评估显示，AprielGuard在检测有害内容和对抗性操纵方面表现优异，特别是在多步骤和推理密集型场景中超越了现有的开源护栏。

---

## #213 — MSR-Align: Policy-Grounded Multimodal Alignment for Safety-Aware Reasoning in Vision-Language Models

`C` Score: 5.81 | 2025-06-24

**Authors:** Yinan Xia, Yilei Jiang, Yingshui Tan, Xiaoyong Zhu, Xiangyu Yue, Bo Zheng

**Categories:** cs.CV, cs.CL

**Scores:** Citation: 5.48 | Influential: 9.02 | Venue: 2.00 | Author: 4.27 | Recency: 7.00

**Links:** [arXiv](https://arxiv.org/abs/2506.19257) | [PDF](https://arxiv.org/pdf/2506.19257)

> 本文提出了MSR-Align，一个高质量的多模态安全推理数据集，旨在解决视觉语言模型在多模态输入下的安全对齐问题。该数据集支持基于标准化安全策略的细粒度推理，通过强调多模态多样性和严格的质量过滤来生成数据。实验表明，在该数据集上微调VLM能显著提高对文本和视觉语言越狱攻击的鲁棒性，同时保持通用推理能力。

---

## #214 — Backdoor Attribution: Elucidating and Controlling Backdoor in Language Models

`C` Score: 5.79 | 2025-09-26

**Authors:** Miao Yu, Zhenhong Zhou, Moayad Aloqaily, Kun Wang, Biwei Huang, Stephen Wang et al. (8 total)

**Categories:** cs.CR, cs.AI

**Scores:** Citation: 5.35 | Influential: 7.81 | Venue: 2.00 | Author: 6.17 | Recency: 7.00

**Links:** [arXiv](https://arxiv.org/abs/2509.21761) | [PDF](https://arxiv.org/pdf/2509.21761)

> 本文针对微调大语言模型易受数据投毒后门攻击但内部机制不透明的问题，提出了名为BkdAttr的三方因果分析框架。该框架通过Backdoor Probe证实了模型表征中存在可学习的后门特征，并利用Backdoor Attention Head Attribution (BAHA)高效定位处理这些特征的特定注意力头。研究发现这些关键头非常稀疏（仅占总数的约3%），通过消融这些头可有效控制后门，为理解和消除LLM后门威胁提供了重要的可解释性见解。

---

## #215 — SAFENLIDB: A Privacy-Preserving Safety Alignment Framework for LLM-based Natural Language Database Interfaces

`C` Score: 5.79 | 2025-11-10

**Authors:** Ruiheng Liu, XiaoBing Chen, Jinyu Zhang, Qiongwen Zhang, Yu Zhang, Bailong Yang

**Categories:** cs.CL

**Scores:** Citation: 4.55 | Influential: 7.81 | Venue: 10.00 | Author: 1.86 | Recency: 9.00

**Links:** [arXiv](https://arxiv.org/abs/2511.06778) | [PDF](https://arxiv.org/pdf/2511.06778)

> 本文提出了SafeNlidb，一种针对基于大语言模型的自然语言数据库接口的隐私保护安全对齐框架。该框架通过自动生成混合思维链数据，将隐式安全推理与SQL生成无缝结合，并利用推理预热和交替偏好优化技术克服多偏好振荡问题。实验表明，该方法在无需人工标注偏好数据的情况下，显著提升了安全性并保持了高实用性，有效防御了复杂推理攻击。

---

## #216 — Are Neuro-Inspired Multi-Modal Vision-Language Models Resilient to Membership Inference Privacy Leakage?

`C` Score: 5.78 | 2025-11-24

**Authors:** David Amebley, Sayanton Dibbo

**Categories:** cs.CV, cs.AI, cs.CR

**Scores:** Citation: 4.69 | Influential: 7.81 | Venue: 2.00 | Author: 6.75 | Recency: 9.00

**Links:** [arXiv](https://arxiv.org/abs/2511.20710) | [PDF](https://arxiv.org/pdf/2511.20710)

> 本文研究了神经启发的多模态视觉语言模型对成员推断隐私攻击的鲁棒性，引入了基于神经科学的拓扑正则化框架。实验表明，经过拓扑正则化的 NEURO VLM 在保持模型效用的同时，能显著降低 MIA 攻击的成功率，证明了生物启发表示在增强多模态模型隐私保护方面的潜力。

---

## #217 — Q-MLLM: Vector Quantization for Robust Multimodal Large Language Model Security

`C` Score: 5.77 | 2025-11-20

**Authors:** Wei Zhao, Zhe Li, Yige Li, Jun Sun

**Categories:** cs.CR, cs.AI

**Scores:** Citation: 4.66 | Influential: 7.81 | Venue: 2.00 | Author: 6.75 | Recency: 9.00

**Links:** [arXiv](https://arxiv.org/abs/2511.16229) | [PDF](https://arxiv.org/pdf/2511.16229)

> 本文提出了Q-MLLM，一种集成两级向量量化的新型架构，旨在增强多模态大语言模型的安全性。通过在像素块和语义层面离散化视觉表征，该架构创建了对抗攻击的离散瓶颈，有效阻断攻击路径并保持多模态推理能力。实验显示，Q-MLLM在防御越狱和有毒图像攻击方面表现优异，且无需昂贵的特定安全微调。

---

## #218 — PrivacyXray: Detecting Privacy Breaches in LLMs through Semantic Consistency and Probability Certainty

`C` Score: 5.75 | 2025-06-24

**Authors:** Jinwen He, Yiyang Lu, Zijin Lin, Kai Chen, Yue Zhao

**Categories:** cs.CR, cs.AI

**Scores:** Citation: 3.73 | Influential: 9.02 | Venue: 10.00 | Author: 3.78 | Recency: 7.00

**Links:** [arXiv](https://arxiv.org/abs/2506.19563) | [PDF](https://arxiv.org/pdf/2506.19563)

> 本文提出了PrivacyXray，一种通过分析大语言模型内部状态来检测隐私泄露的新框架。研究发现模型在生成正确的私有信息时表现出更高的语义连贯性和概率确定性，基于此设计了四个检测指标。该方法克服了缺乏开源私有数据集的挑战，在五个LLM上实现了92.69%的平均准确率，显著优于现有方法。

---

## #219 — Adversarial Déjà Vu: Jailbreak Dictionary Learning for Stronger Generalization to Unseen Attacks

`C` Score: 5.75 | 2025-10-24

**Authors:** Mahavir Dabas, Tran Huynh, Nikhil Reddy Billa, Jiachen T. Wang, Peng Gao, Charith Peris et al. (11 total)

**Categories:** cs.LG

**Scores:** Citation: 4.39 | Influential: 7.81 | Venue: 2.00 | Author: 7.43 | Recency: 9.00

**Links:** [arXiv](https://arxiv.org/abs/2510.21910) | [PDF](https://arxiv.org/pdf/2510.21910)

> 本文提出了对抗既视感假设，认为新型越狱攻击主要是先前攻击技能的重新组合。基于此，引入了对抗技能组合训练（ASCoT），通过在多样化的技能组合上进行训练，显著提高了模型对未见攻击（包括多轮越狱）的鲁棒性。

---

## #220 — InvThink: Towards AI Safety via Inverse Reasoning

`C` Score: 5.73 | 2025-10-02

**Authors:** Yubin Kim, Taehan Kim, Eugene Park, Chunjong Park, Cynthia Breazeal, Daniel McDuff et al. (7 total)

**Categories:** cs.AI, cs.CL

**Scores:** Citation: 5.47 | Influential: 7.81 | Venue: 2.00 | Author: 5.40 | Recency: 7.00

**Links:** [arXiv](https://arxiv.org/abs/2510.01569) | [PDF](https://arxiv.org/pdf/2510.01569)

> 本文提出了InvThink方法，赋予语言模型“逆向思维”能力，通过在生成响应前推理潜在失败模式来增强安全性。该方法指导模型枚举潜在危害、分析后果并主动生成安全输出，有效解决了现有方法直接优化安全响应的局限性。研究发现，InvThink不仅随着模型规模扩大显著提升安全推理能力，还能减轻安全税，在医疗、金融及Agent风险场景中将有害响应减少了17.8%。

---

## #221 — Detecting Misbehaviors of Large Vision-Language Models by Evidential Uncertainty Quantification

`C` Score: 5.73 | 2026-02-05

**Authors:** Tao Huang, Rui Wang, Xiaofei Liu, Yi Qin, Li Duan, Liping Jing

**Categories:** cs.LG

**Scores:** Citation: 6.22 | Influential: 7.81 | Venue: 2.00 | Author: 1.12 | Recency: 10.00

**Links:** [arXiv](https://arxiv.org/abs/2602.05535) | [PDF](https://arxiv.org/pdf/2602.05535)

> 本文提出了证据不确定性量化（EUQ），一种通过细粒度捕捉信息冲突和知识缺失来检测大型视觉-语言模型异常行为的方法。该方法将模型输出特征解释为支持或反对证据，利用证据理论在单次前向传播中量化内部冲突。评估显示，EUQ在检测幻觉、越狱、对抗性漏洞和分布外失败方面始终优于现有方法。

---

## #222 — Dynamic Guided and Domain Applicable Safeguards for Enhanced Security in Large Language Models

`C` Score: 5.73 | 2024-10-23

**Authors:** Weidi Luo, He Cao, Zijing Liu, Yu Wang, Aidan Wong, Bing Feng et al. (8 total)

**Categories:** cs.AI

**Scores:** Citation: 5.75 | Influential: 7.81 | Venue: 2.00 | Author: 5.88 | Recency: 5.00

**Links:** [arXiv](https://arxiv.org/abs/2410.17922) | [PDF](https://arxiv.org/pdf/2410.17922)

> 针对现有LLM防御方法在特定领域防御能力不足及过度防御的问题，本文提出了基于多智能体的防御框架G4D。该框架利用准确的外部信息提供无偏的用户意图总结和分析性的安全响应指导，在不牺牲模型通用功能的前提下，显著增强了模型在通用和特定领域场景下对抗越狱攻击的鲁棒性。

---

## #223 — FreakOut-LLM: The Effect of Emotional Stimuli on Safety Alignment

`C` Score: 5.72 | 2026-04-05

**Authors:** Daniel Kuznetsov, Ofir Cohen, Karin Shistik, Rami Puzis, Asaf Shabtai

**Categories:** cs.CR, cs.AI

**Scores:** Citation: 3.32 | Influential: 7.81 | Venue: 2.00 | Author: 9.75 | Recency: 10.00

**Links:** [arXiv](https://arxiv.org/abs/2604.04992) | [PDF](https://arxiv.org/pdf/2604.04992)

> FreakOut-LLM研究情感刺激对LLM安全对齐的影响，通过实验发现压力提示使越狱成功率提高65.2%，而放松提示无显著效果。该框架验证了情感上下文作为可测量攻击表面的存在，对高压力领域AI部署的安全评估具有重要意义。

---

## #224 — Language Models Can Predict Their Own Behavior

`C` Score: 5.70 | 2025-02-18

**Authors:** Dhananjay Ashok, Jonathan May

**Categories:** cs.CL, cs.AI, cs.LG

**Scores:** Citation: 6.38 | Influential: 7.81 | Venue: 2.00 | Author: 3.78 | Recency: 5.00

**Links:** [arXiv](https://arxiv.org/abs/2502.13329) | [PDF](https://arxiv.org/pdf/2502.13329)

> 本文提供了证据表明，可以在计算早期预测语言模型行为，甚至在生成任何标记之前。作者使用保形预测方法创建了基于内部表示的探针，可预测整个输出序列的多种行为，构建的早期预警系统将越狱减少91%，还能预判模型置信度和Chain-of-Thought推理结果。

---

## #225 — AdaptiveGuard: Towards Adaptive Runtime Safety for LLM-Powered Software

`C` Score: 5.69 | 2025-09-21

**Authors:** Rui Yang, Michael Fu, Chakkrit Tantithamthavorn, Chetan Arora, Gunel Gulmammadova, Joey Chua

**Categories:** cs.CR, cs.AI, cs.SE

**Scores:** Citation: 3.32 | Influential: 7.81 | Venue: 5.00 | Author: 9.58 | Recency: 7.00

**Links:** [arXiv](https://arxiv.org/abs/2509.16861) | [PDF](https://arxiv.org/pdf/2509.16861)

> 本文提出了AdaptiveGuard，一种能够动态适应新兴威胁的自适应护栏系统。该系统将未见过的越狱攻击检测为分布外输入，并通过持续学习框架进行防御。实验结果显示，AdaptiveGuard在保持分布内数据性能的同时，能快速适应新攻击，解决了现有护栏在面对未知攻击时性能下降的问题。

---

## #226 — EcoAlign: An Economically Rational Framework for Efficient LVLM Alignment

`C` Score: 5.68 | 2025-11-14

**Authors:** Ruoxi Cheng, Haoxuan Ma, Teng Ma, Hongyi Zhang

**Categories:** cs.AI

**Scores:** Citation: 6.09 | Influential: 7.81 | Venue: 2.00 | Author: 1.86 | Recency: 9.00

**Links:** [arXiv](https://arxiv.org/abs/2511.11301) | [PDF](https://arxiv.org/pdf/2511.11301)

> 本文提出了EcoAlign，一种将大视觉语言模型（LVLM）视为有限理性智能体的推理时对齐框架。该方法通过增量扩展思维图并使用前瞻性函数动态权衡安全性、效用和成本，将对齐重新定义为经济理性的搜索过程。实验表明，EcoAlign在较低的计算成本下，匹配或超越了SOTA的安全性和效用，为鲁棒的LVLM对齐提供了一条经济高效的途径。

---

## #227 — Cowpox: Towards the Immunity of VLM-based Multi-Agent Systems

`C` Score: 5.67 | 2025-08-12

**Authors:** Yutong Wu, Jie Zhang, Yiming Li, Chao Zhang, Qing Guo, Nils Lukas et al. (7 total)

**Categories:** cs.MA, cs.AI

**Scores:** Citation: 3.92 | Influential: 7.81 | Venue: 10.00 | Author: 4.27 | Recency: 7.00

**Links:** [arXiv](https://arxiv.org/abs/2508.09230) | [PDF](https://arxiv.org/pdf/2508.09230)

> 本文针对基于视觉语言模型的多智能体系统缺乏鲁棒性的问题，提出了 Cowpox 防御方法，通过分布式机制增强系统的鲁棒性。核心思想是生成并分发特殊的“治愈样本”，在智能体暴露于攻击前对其进行免疫，并帮助已感染的智能体恢复。研究通过实证验证了 Cowpox 的有效性，并提供了理论上的鲁棒性保证，限制了攻击在智能体间的传播。

---

## #228 — DeepForgeSeal: Latent Space-Driven Semi-Fragile Watermarking for Deepfake Detection Using Multi-Agent Adversarial Reinforcement Learning

`C` Score: 5.65 | 2025-11-07

**Authors:** Tharindu Fernando, Clinton Fookes, Sridha Sridharan

**Categories:** cs.CV, cs.AI

**Scores:** Citation: 3.32 | Influential: 7.81 | Venue: 2.00 | Author: 9.93 | Recency: 9.00

**Links:** [arXiv](https://arxiv.org/abs/2511.04949) | [PDF](https://arxiv.org/pdf/2511.04949)

> 本文提出了DeepForgeSeal，一种利用多智能体对抗强化学习（MAARL）范式的深度伪造检测半脆弱水印框架。该方法在潜在空间中开发可学习的水印嵌入器，通过与模拟良性及恶意图像操作的对抗攻击者智能体交互，在鲁棒性和脆弱性之间寻求最佳平衡。综合评估显示，该方法在CelebA和CelebA-HQ基准上均优于现有最先进方法，有效提升了合成媒体的识别能力。

---

## #229 — Deactivating Refusal Triggers: Understanding and Mitigating Overrefusal in Safety Alignment

`C` Score: 5.64 | 2026-03-12

**Authors:** Zhiyu Xue, Zimo Qi, Guangliang Liu, Bocheng Chen, Ramtin Pedarsani

**Categories:** cs.AI

**Scores:** Citation: 3.32 | Influential: 7.81 | Venue: 2.00 | Author: 9.23 | Recency: 10.00

**Links:** [arXiv](https://arxiv.org/abs/2603.11388) | [PDF](https://arxiv.org/pdf/2603.11388)

> 本文分析了安全对齐中过度拒绝问题的产生机制，将其归因于模型对训练数据中拒绝触发器的关联。作者提出了一种在安全微调中显式考虑拒绝触发器的缓解策略，在防御越狱攻击和对良性查询的响应性之间实现了更好的平衡。

---

## #230 — IH-Challenge: A Training Dataset to Improve Instruction Hierarchy on Frontier LLMs

`C` Score: 5.64 | 2026-03-11

**Authors:** Chuan Guo, Juan Felipe Ceron Uribe, Sicheng Zhu, Christopher A. Choquette-Choo, Steph Lin, Nikhil Kandpal et al. (13 total)

**Categories:** cs.AI, cs.CL, cs.CR

**Scores:** Citation: 3.32 | Influential: 7.81 | Venue: 2.00 | Author: 9.23 | Recency: 10.00

**Links:** [arXiv](https://arxiv.org/abs/2603.10521) | [PDF](https://arxiv.org/pdf/2603.10521)

> 本文介绍了IH-Challenge数据集，旨在解决指令层次（IH）行为难以训练的问题，以防御越狱和提示注入。在该数据集上微调GPT-5-Mini显著提高了IH鲁棒性，将不安全行为从6.6%降至0.7%，同时保持了通用能力。

---

## #231 — Toward a Safer Web: Multilingual Multi-Agent LLMs for Mitigating Adversarial Misinformation Attacks

`C` Score: 5.60 | 2025-10-07

**Authors:** Nouar Aldahoul, Yasir Zaki

**Categories:** cs.CL, cs.AI, cs.CR

**Scores:** Citation: 4.21 | Influential: 7.81 | Venue: 2.00 | Author: 8.33 | Recency: 7.00

**Links:** [arXiv](https://arxiv.org/abs/2510.08605) | [PDF](https://arxiv.org/pdf/2510.08605)

> 本文系统研究了包括多语言切换、查询长度膨胀及结构重格式化在内的对抗性虚假信息攻击。为此，作者提出了一种结合检索增强生成的多语言多智能体大语言模型框架，该框架可作为Web插件部署于在线平台。该研究不仅展示了AI在应对多样化攻击、维护网络事实完整性方面的关键作用，还验证了基于插件的实际部署可行性。

---

## #232 — Detoxifying LLMs via Representation Erasure-Based Preference Optimization

`C` Score: 5.60 | 2026-02-24

**Authors:** Nazanin Mohammadi Sepahvand, Eleni Triantafillou, Hugo Larochelle, Doina Precup, Daniel M. Roy, Gintare Karolina Dziugaite

**Categories:** cs.LG

**Scores:** Citation: 3.32 | Influential: 7.81 | Venue: 2.00 | Author: 8.93 | Recency: 10.00

**Links:** [arXiv](https://arxiv.org/abs/2602.23391) | [PDF](https://arxiv.org/pdf/2602.23391)

> 针对现有大语言模型去毒方法（如DPO）仅做表面修改且易受对抗性攻击的问题，本文提出了基于表征擦除的偏好优化（REPO）。该方法将去毒重新表述为token级别的偏好问题，通过新颖的目标函数强制有毒续写的表征向良性对应物收敛。机制分析表明，REPO能对毒性编码神经元进行深度且局部的编辑，从而在保留生成能力的同时实现更稳健的去毒效果。

---

## #233 — Beyond Reactive Safety: Risk-Aware LLM Alignment via Long-Horizon Simulation

`C` Score: 5.59 | 2025-06-26

**Authors:** Chenkai Sun, Denghui Zhang, ChengXiang Zhai, Heng Ji

**Categories:** cs.AI, cs.CL

**Scores:** Citation: 3.75 | Influential: 7.81 | Venue: 10.00 | Author: 4.27 | Recency: 7.00

**Links:** [arXiv](https://arxiv.org/abs/2506.20949) | [PDF](https://arxiv.org/pdf/2506.20949)

> 本文提出了一个通过长期模拟来评估模型建议在社会系统中宏观影响的框架，以增强LLM的对齐性。研究引入了包含100种间接伤害场景的数据集，测试模型预见非明显不良后果的能力，显著提升了模型在长期安全基准上的表现。

---

## #234 — Safety Instincts: LLMs Learn to Trust Their Internal Compass for Self-Defense

`C` Score: 5.59 | 2025-10-01

**Authors:** Guobin Shen, Dongcheng Zhao, Haibo Tong, Jindong Li, Feifei Zhao, Yi Zeng

**Categories:** cs.AI

**Scores:** Citation: 4.17 | Influential: 7.81 | Venue: 2.00 | Author: 8.33 | Recency: 7.00

**Links:** [arXiv](https://arxiv.org/abs/2510.01088) | [PDF](https://arxiv.org/pdf/2510.01088)

> 针对大模型安全训练信号匮乏的问题，本文提出Safety Instincts强化学习（SIRL）方法。研究发现对齐模型在拒绝有害请求时表现出低熵特征，SIRL利用这种内部置信度差异作为自生成的奖励信号，无需外部验证器或人工标注即可训练模型信任其安全本能。实验表明，该方法在Llama和Qwen模型上仅用少量无标签数据，便实现了对20多种越狱攻击89%以上的防御成功率。

---

## #235 — The Structural Safety Generalization Problem

`C` Score: 5.58 | 2025-04-13

**Authors:** Julius Broomfield, Tom Gibbs, Ethan Kosak-Hine, George Ingebretsen, Tia Nasir, Jason Zhang et al. (10 total)

**Categories:** cs.CR, cs.AI, cs.CV

**Scores:** Citation: 3.55 | Influential: 7.81 | Venue: 10.00 | Author: 6.17 | Recency: 5.00

**Links:** [arXiv](https://arxiv.org/abs/2504.09712) | [PDF](https://arxiv.org/pdf/2504.09712)

> 本文提出了结构安全泛化问题，指出模型安全无法在语义等效但结构不同的输入（如多轮、多模态或翻译后的输入）之间泛化。作者通过红队测试揭示了这些结构差异导致的安全结果差异，并提出了结构重写护栏来转换输入结构以提升安全性。该框架为防御语义等效攻击提供了新思路，是 AI 安全研究的重要里程碑。

---

## #236 — ARMOR: Aligning Secure and Safe Large Language Models via Meticulous Reasoning

`C` Score: 5.58 | 2025-07-14

**Authors:** Zhengyue Zhao, Yingzi Ma, Somesh Jha, Marco Pavone, Patrick McDaniel, Chaowei Xiao

**Categories:** cs.CR

**Scores:** Citation: 5.66 | Influential: 7.81 | Venue: 2.00 | Author: 3.78 | Recency: 7.00

**Links:** [arXiv](https://arxiv.org/abs/2507.11500) | [PDF](https://arxiv.org/pdf/2507.11500)

> 本文提出ARMOR方法，通过结构化三步推理流程对齐安全大语言模型：分析越狱策略、提取核心意图和应用基于策略的安全验证。ARMOR-Think将安全推理与一般推理解耦以提高鲁棒性。实验显示，ARMOR在先进优化越狱攻击上达到有害率0.002和攻击成功率0.06的优异表现，显著优于其他推理模型。

---

## #237 — Safety Recovery in Reasoning Models Is Only a Few Early Steering Steps Away

`C` Score: 5.58 | 2026-02-11

**Authors:** Soumya Suvra Ghosal, Souradip Chakraborty, Vaibhav Singh, Furong Huang, Dinesh Manocha, Amrit Singh Bedi

**Categories:** cs.CL, cs.AI

**Scores:** Citation: 3.32 | Influential: 7.81 | Venue: 2.00 | Author: 8.84 | Recency: 10.00

**Links:** [arXiv](https://arxiv.org/abs/2602.11096) | [PDF](https://arxiv.org/pdf/2602.11096)

> 本文提出了SafeThink，一种针对多模态推理模型的轻量级推理时防御方法，旨在解决强化学习后训练导致的安全对齐退化问题。SafeThink将安全恢复视为满足约束而非最大化目标，通过监控推理轨迹并在违反安全阈值时注入优化的纠正前缀来引导模型。实验显示，该方法在保持推理性能的同时，将攻击成功率降低了30-60%，且仅需干预前1-3步即可有效重定向生成过程。

---

## #238 — Sysformer: Safeguarding Frozen Large Language Models with Adaptive System Prompts

`C` Score: 5.56 | 2025-06-18

**Authors:** Kartik Sharma, Yiqiao Jin, Vineeth Rakesh, Yingtong Dou, Menghai Pan, Mahashweta Das et al. (7 total)

**Categories:** cs.AI, cs.CL, cs.LG

**Scores:** Citation: 4.64 | Influential: 7.81 | Venue: 2.00 | Author: 6.75 | Recency: 7.00

**Links:** [arXiv](https://arxiv.org/abs/2506.15751) | [PDF](https://arxiv.org/pdf/2506.15751)

> 本文提出了Sysformer，一种通过自适应调整系统提示词来保护冻结大语言模型的新方法。该方法在不微调模型参数的情况下，利用Transformer模型根据用户输入动态更新系统提示词，显著提升了模型对有害请求的拒绝率，同时保持对无害请求的合规性。实验表明，Sysformer在多个模型和基准测试中能有效增强鲁棒性，拒绝率提升高达80%。

---

## #239 — Activation Steering Meets Preference Optimization: Defense Against Jailbreaks in Vision Language Models

`C` Score: 5.56 | 2025-08-30

**Authors:** Sihao Wu, Gaojie Jin, Wei Huang, Jianhong Wang, Xiaowei Huang

**Categories:** cs.CV, cs.AI

**Scores:** Citation: 5.09 | Influential: 7.81 | Venue: 2.00 | Author: 5.40 | Recency: 7.00

**Links:** [arXiv](https://arxiv.org/abs/2509.00373) | [PDF](https://arxiv.org/pdf/2509.00373)

> 本文提出了SPO-VLM，一种结合激活级干预与策略级优化的两阶段防御框架，旨在增强视觉语言模型（VLM）的抗越狱能力。该方法首先计算自适应转向向量以抑制有害行为，随后通过序列级偏好优化整合毒性评估和视觉一致性奖励。实验表明，SPO-VLM在保持视觉定位性能的同时显著提升了模型的安全性。

---

## #240 — Bidirectional Intention Inference Enhances LLMs' Defense Against Multi-Turn Jailbreak Attacks

`C` Score: 5.56 | 2025-09-25

**Authors:** Haibo Tong, Dongcheng Zhao, Guobin Shen, Xiang He, Dachuan Lin, Feifei Zhao et al. (7 total)

**Categories:** cs.CR, cs.AI

**Scores:** Citation: 4.11 | Influential: 7.81 | Venue: 2.00 | Author: 8.33 | Recency: 7.00

**Links:** [arXiv](https://arxiv.org/abs/2509.22732) | [PDF](https://arxiv.org/pdf/2509.22732)

> 针对现有防御机制难以有效应对多轮越狱攻击的挑战，本文提出了双向意图推断防御（BIID）框架。该方法创新性地融合了基于请求的前向意图推断与基于响应的后向意图回溯，通过建立双向协同机制来精准识别隐藏在看似良性输入中的恶意风险。这一方法有效克服了传统单轮防御的局限性，构建了更鲁棒的安全护栏，显著增强了大语言模型在复杂多轮对话中抵御策略性操纵和防止有害内容生成的能力。

---

## #241 — Character as a Latent Variable in Large Language Models: A Mechanistic Account of Emergent Misalignment and Conditional Safety Failures

`C` Score: 5.56 | 2026-01-30

**Authors:** Yanghao Su, Wenbo Zhou, Tianwei Zhang, Qiu Han, Weiming Zhang, Nenghai Yu et al. (7 total)

**Categories:** cs.CL, cs.AI, cs.CR

**Scores:** Citation: 3.32 | Influential: 7.81 | Venue: 2.00 | Author: 8.73 | Recency: 10.00

**Links:** [arXiv](https://arxiv.org/abs/2601.23081) | [PDF](https://arxiv.org/pdf/2601.23081)

> 本文探讨了“突发性错位”现象，表明在特定角色级倾向数据上微调模型会导致比错误建议微调更强且更具迁移性的错位行为。研究发现，这种行为倾向可以通过训练时触发器和推理时角色提示被条件性激活，揭示了突发性错位、后门激活和越狱易感性之间的共同结构。该研究指出角色形成是一个核心的对齐风险，鲁棒的对齐必须解决行为倾向问题。

---

## #242 — TRYLOCK: Defense-in-Depth Against LLM Jailbreaks via Layered Preference and Representation Engineering

`C` Score: 5.56 | 2026-01-06

**Authors:** Scott Thornton

**Categories:** cs.CR, cs.LG

**Scores:** Citation: 5.29 | Influential: 9.02 | Venue: 2.00 | Author: 1.86 | Recency: 9.00

**Links:** [arXiv](https://arxiv.org/abs/2601.03300) | [PDF](https://arxiv.org/pdf/2601.03300)

> 本文提出了TRYLOCK，首个结合DPO、表示工程、侧车分类器和输入规范化四种异构机制的纵深防御架构。该架构在推理堆栈的不同层面提供安全覆盖，显著降低了攻击成功率，并解决了安全性与可用性之间的权衡问题，实现了高安全性下的低过度拒绝率。

---

## #243 — Segment-Level Coherence for Robust Harmful Intent Probing in LLMs

`C` Score: 5.56 | 2026-04-16

**Authors:** Xuanli He, Bilgehan Sel, Faizan Ali, Jenny Bao, Hoagy Cunningham, Jerry Wei

**Categories:** cs.CL, cs.CR

**Scores:** Citation: 3.32 | Influential: 7.81 | Venue: 2.00 | Author: 8.73 | Recency: 10.00

**Links:** [arXiv](https://arxiv.org/abs/2604.14865) | [PDF](https://arxiv.org/pdf/2604.14865)

> 本文针对LLMs中的自适应越狱问题，特别是在高风险CBRN领域。作者引入流式探测目标，要求多个证据token一致支持预测，而非依赖孤立峰值。在固定1%假阳性率下，真阳性率提高35.55%。实验表明，探测注意力或MLP激活优于残差流特征，且即使面对对抗性微调的新字符级密码，有害意图仍可检测，AUROC超过98.85%。

---

## #244 — Safety Alignment Should Be Made More Than Just A Few Attention Heads

`C` Score: 5.55 | 2025-08-27

**Authors:** Chao Huang, Zefeng Zhang, Juewei Yue, Quangang Li, Chuang Zhang, Tingwen Liu

**Categories:** cs.CR, cs.AI, cs.CL

**Scores:** Citation: 5.06 | Influential: 7.81 | Venue: 2.00 | Author: 5.40 | Recency: 7.00

**Links:** [arXiv](https://arxiv.org/abs/2508.19697) | [PDF](https://arxiv.org/pdf/2508.19697)

> 本文揭示了现有大语言模型的安全机制过度依赖于少数注意力头，这使得模型容易受到针对性越狱攻击的破坏。为此，作者提出了RDSHA方法定位关键组件，并设计了AHD训练策略，将安全相关行为分散编码到更多注意力头中。实验表明，AHD显著增强了模型的安全性鲁棒性，同时保持了整体功能效用。

---

## #245 — Offline Safe Policy Optimization From Heterogeneous Feedback

`C` Score: 5.55 | 2025-12-23

**Authors:** Ze Gong, Pradeep Varakantham, Akshat Kumar

**Categories:** cs.AI

**Scores:** Citation: 3.32 | Influential: 7.81 | Venue: 2.00 | Author: 9.28 | Recency: 9.00

**Links:** [arXiv](https://arxiv.org/abs/2512.20173) | [PDF](https://arxiv.org/pdf/2512.20173)

> 本文提出了PreSa框架，用于解决基于人类反馈的离线强化学习中的安全性挑战。该方法直接根据行为偏好和轨迹段安全标签学习策略，通过拉格朗日范式直接学习安全策略，避免了显式学习奖励和成本模型以及复杂的约束强化学习。实验表明，该方法在连续控制任务中能有效对齐偏好并确保安全。

---

## #246 — DefenSee: Dissecting Threat from Sight and Text -- A Multi-View Defensive Pipeline for Multi-modal Jailbreaks

`C` Score: 5.55 | 2025-12-01

**Authors:** Zihao Wang, Kar Wai Fok, Vrizlynn L. L. Thing

**Categories:** cs.CR

**Scores:** Citation: 3.32 | Influential: 7.81 | Venue: 2.00 | Author: 9.28 | Recency: 9.00

**Links:** [arXiv](https://arxiv.org/abs/2512.01185) | [PDF](https://arxiv.org/pdf/2512.01185)

> 本文提出了DefenSee，一种鲁棒且轻量级的多模态黑盒防御技术，旨在保护多模态大语言模型免受协调的越狱攻击。该方法通过图像变体转录和跨模态一致性检查来识别恶意输入，模仿人类判断过程。实验表明，DefenSee在增强模型鲁棒性的同时，能更好地保持良性任务的性能，显著优于现有的最先进防御方法。

---

## #247 — SafeSeek: Universal Attribution of Safety Circuits in Language Models

`C` Score: 5.55 | 2026-03-24

**Authors:** Miao Yu, Siyuan Fu, Moayad Aloqaily, Zhenhong Zhou, Safa Otoum, Xing fan et al. (9 total)

**Categories:** cs.LG, cs.AI

**Scores:** Citation: 3.32 | Influential: 7.81 | Venue: 2.00 | Author: 8.65 | Recency: 10.00

**Links:** [arXiv](https://arxiv.org/abs/2603.23268) | [PDF](https://arxiv.org/pdf/2603.23268)

> 本文提出了 SafeSeek，一个统一的安全可解释性框架，通过优化和可微分二值掩码来识别 LLM 中功能完整的安全回路。与现有方法不同，SafeSeek 能够提取多粒度回路，并结合安全回路微调技术进行高效的安全微调。实验表明，该方法在定位后门攻击回路和对齐回路方面表现出色，能在极低稀疏度下消除攻击成功率或保留模型通用性。

---

## #248 — HyPerAlign: Interpretable Personalized LLM Alignment via Hypothesis Generation

`C` Score: 5.54 | 2025-04-29

**Authors:** Cristina Garbacea, Chenhao Tan

**Categories:** cs.CL

**Scores:** Citation: 5.05 | Influential: 7.81 | Venue: 2.00 | Author: 5.40 | Recency: 7.00

**Links:** [arXiv](https://arxiv.org/abs/2505.00038) | [PDF](https://arxiv.org/pdf/2505.00038)

> 本文提出HyPerAlign，一种可解释且样本高效的假设驱动LLM个性化对齐方法。该方法通过分析用户的少量样本推断其沟通策略和写作风格等假设，进而利用这些假设指导模型生成符合特定用户偏好的定制化输出。实验证明，该方法在作者归属和审议对齐等任务上优于传统的基于偏好的微调方法。

---

## #249 — CEE: An Inference-Time Jailbreak Defense for Embodied Intelligence via Subspace Concept Rotation

`C` Score: 5.54 | 2025-04-15

**Authors:** Jirui Yang, Zheyu Lin, Zhihui Lu, Yinggui Wang, Lei Wang, Tao Wei et al. (9 total)

**Categories:** cs.CR, cs.LG, cs.MA

**Scores:** Citation: 4.94 | Influential: 9.02 | Venue: 2.00 | Author: 5.40 | Recency: 5.00

**Links:** [arXiv](https://arxiv.org/abs/2504.13201) | [PDF](https://arxiv.org/pdf/2504.13201)

> 本文提出了 CEE，一种针对具身智能系统的动态推理时越狱防御框架。该方法通过动态构建任务特定的安全语义子空间并应用 SLERP 旋转，实现了自适应的安全控制，同时保持了生成质量和任务指令的遵循度。实验表明，该方法在 EI 场景下显著增强了鲁棒性且降低了调优成本，优于现有的静态干预方法。

---

## #250 — Rebellion: Noise-Robust Reasoning Training for Audio Reasoning Models

`C` Score: 5.54 | 2025-11-12

**Authors:** Tiansheng Huang, Virat Shejwalkar, Oscar Chang, Milad Nasr, Ling Liu

**Categories:** cs.AI, cs.SD

**Scores:** Citation: 3.32 | Influential: 7.81 | Venue: 2.00 | Author: 9.23 | Recency: 9.00

**Links:** [arXiv](https://arxiv.org/abs/2511.09682) | [PDF](https://arxiv.org/pdf/2511.09682)

> 本文研究了音频推理模型（ARM）针对越狱攻击的安全性，指出标准推理训练虽能防御简单攻击，但无法抵御导致表示漂移的高级越狱。作者提出了Rebellion，一种鲁棒的推理训练方法，通过训练模型应对最坏情况的表示漂移来提升安全性。在Qwen2-Audio上的实验表明，Rebellion能在不损害良性任务性能的前提下有效防御高级音频越狱，显著改善了准确性与安全性的权衡。

---

## #251 — The Aloe Family Recipe for Open and Specialized Healthcare LLMs

`C` Score: 5.52 | 2025-05-07

**Authors:** Dario Garcia-Gasulla, Jordi Bayarri-Planas, Ashwin Kumar Gururajan, Enrique Lopez-Cuena, Adrian Tormos, Daniel Hinjos et al. (13 total)

**Categories:** cs.CL, cs.AI

**Scores:** Citation: 4.41 | Influential: 7.81 | Venue: 2.00 | Author: 7.15 | Recency: 7.00

**Links:** [arXiv](https://arxiv.org/abs/2505.04388) | [PDF](https://arxiv.org/pdf/2505.04388)

> 本文介绍了Aloe系列开源医疗大语言模型，通过优化数据预处理和训练流程，并利用直接偏好优化（DPO）提升模型安全性。该模型在医疗基准测试中表现优异，显著提高了对偏见和毒性的抵抗力，并展现出对未见过的越狱攻击的韧性，为医疗AI的安全部署提供了新标准。

---

## #252 — Strategic Deflection: Defending LLMs from Logit Manipulation

`C` Score: 5.50 | 2025-07-29

**Authors:** Yassine Rachidy, Jihad Rbaiti, Youssef Hmamouche, Faissal Sehbaoui, Amal El Fallah Seghrouchni

**Categories:** cs.CR, cs.AI, cs.CL

**Scores:** Citation: 3.85 | Influential: 7.81 | Venue: 2.00 | Author: 8.73 | Recency: 7.00

**Links:** [arXiv](https://arxiv.org/abs/2507.22160) | [PDF](https://arxiv.org/pdf/2507.22160)

> 本文提出了Strategic Deflection防御策略，旨在应对针对大语言模型的Logit级别越狱攻击。不同于传统的直接拒绝机制，该方法通过生成语义相关但剥离有害意图的回答来中和攻击者意图，在显著降低攻击成功率的同时，保持了对良性查询的模型性能。

---

## #253 — Dynamic Token Reweighting for Robust Vision-Language Models

`C` Score: 5.49 | 2025-05-22

**Authors:** Tanqiu Jiang, Jiacheng Liang, Rongyi Zhu, Jiawei Zhou, Fenglong Ma, Ting Wang

**Categories:** cs.CV, cs.CL

**Scores:** Citation: 5.13 | Influential: 7.81 | Venue: 2.00 | Author: 4.79 | Recency: 7.00

**Links:** [arXiv](https://arxiv.org/abs/2505.17132) | [PDF](https://arxiv.org/pdf/2505.17132)

> 本文提出了DTR，一种通过优化键值（KV）缓存来缓解多模态越狱攻击的推理时防御方法。该方法动态调整视觉令牌权重，在最小化对抗视觉输入影响的同时，保持了模型的通用能力和推理效率，是首个成功将KV缓存优化应用于多模态基础模型安全增强的工作。

---

## #254 — Mitigating Jailbreaks with Intent-Aware LLMs

`C` Score: 5.49 | 2025-08-16

**Authors:** Wei Jie Yeo, Ranjan Satapathy, Erik Cambria

**Categories:** cs.CR, cs.CL

**Scores:** Citation: 3.95 | Influential: 9.02 | Venue: 2.00 | Author: 6.75 | Recency: 7.00

**Links:** [arXiv](https://arxiv.org/abs/2508.12072) | [PDF](https://arxiv.org/pdf/2508.12072)

> 本文提出了一种名为 Intent-FT 的轻量级微调方法，通过显式训练大语言模型在响应前推断指令的潜在意图，从而增强其对越狱攻击的鲁棒性。该方法在对抗性指令上进行训练，使模型能够泛化识别未见攻击的意图，在有效缓解各类攻击的同时保持了模型的通用能力并减少了过度拒绝。实验表明，Intent-FT 能准确识别隐藏的恶意意图，且优于现有的部分防御机制。

---

## #255 — Robust Anomaly Detection in O-RAN: Leveraging LLMs against Data Manipulation Attacks

`C` Score: 5.48 | 2025-08-11

**Authors:** Thusitha Dayaratne, Ngoc Duy Pham, Viet Vo, Shangqi Lai, Sharif Abuadbba, Hajime Suzuki et al. (8 total)

**Categories:** cs.CR, cs.ET, cs.LG

**Scores:** Citation: 4.90 | Influential: 7.81 | Venue: 2.00 | Author: 5.40 | Recency: 7.00

**Links:** [arXiv](https://arxiv.org/abs/2508.08029) | [PDF](https://arxiv.org/pdf/2508.08029)

> 本文针对 O-RAN 架构中共享数据层的数据操纵攻击，特别是恶意 xApps 引入的 Unicode 变更，探讨了利用大语言模型进行异常检测的可行性。研究表明，传统的基于机器学习的异常检测方法无法处理被篡改的数据，而基于 LLM 的 xApps 能够稳健地处理被操纵的消息且不会崩溃。虽然初始检测精度有待提高，但结果突显了 LLM 对抗对抗性攻击的鲁棒性及其在电信安全中的潜力。

---

## #256 — Hybrid Reputation Aggregation: A Robust Defense Mechanism for Adversarial Federated Learning in 5G and Edge Network Environments

`C` Score: 5.48 | 2025-09-22

**Authors:** Saeid Sheikhi, Panos Kostakos, Lauri Loven

**Categories:** cs.CR, cs.AI

**Scores:** Citation: 3.32 | Influential: 7.81 | Venue: 5.00 | Author: 8.15 | Recency: 7.00

**Links:** [arXiv](https://arxiv.org/abs/2509.18044) | [PDF](https://arxiv.org/pdf/2509.18044)

> 本文提出了一种名为混合声誉聚合（HRA）的新型鲁棒聚合机制，旨在防御5G和边缘网络环境下的联邦学习对抗攻击。HRA结合了几何异常检测和基于动量的客户端声誉跟踪，能够自适应过滤可疑更新并长期惩罚不可靠客户端。实验表明，HRA在对抗后门注入和Sybil攻击方面表现优异。

---

## #257 — SocialDF: Benchmark Dataset and Detection Model for Mitigating Harmful Deepfake Content on Social Media Platforms

`C` Score: 5.47 | 2025-06-05

**Authors:** Arnesh Batra, Anushk Kumar, Jashn Khemani, Arush Gumber, Arhan Jain, Somil Gupta

**Categories:** cs.LG, cs.MM

**Scores:** Citation: 5.26 | Influential: 7.81 | Venue: 2.00 | Author: 4.27 | Recency: 7.00

**Links:** [arXiv](https://arxiv.org/abs/2506.05538) | [PDF](https://arxiv.org/pdf/2506.05538)

> 本文针对社交媒体上的深度伪造内容，提出了SocialDF数据集和一种基于大模型的多因子检测方法。该方法结合面部识别、语音转录和多Agent流水线，对视听线索进行交叉验证，以区分良性与恶意生成的深度伪造。该研究强调了多模态验证技术在识别合成媒体中的重要性。

---

## #258 — Defending Large Language Models Against Jailbreak Attacks via In-Decoding Safety-Awareness Probing

`C` Score: 5.47 | 2026-01-15

**Authors:** Yinzhi Zhao, Ming Wang, Shi Feng, Xiaocui Yang, Daling Wang, Yifei Zhang

**Categories:** cs.AI, cs.CL

**Scores:** Citation: 3.32 | Influential: 7.81 | Venue: 2.00 | Author: 8.79 | Recency: 9.00

**Links:** [arXiv](https://arxiv.org/abs/2601.10543) | [PDF](https://arxiv.org/pdf/2601.10543)

> 本文提出了一种在解码过程中利用潜在安全信号进行早期检测的防御方法，以抵御越狱攻击。通过显式地利用模型内部的安全感知信号，该方法在保持低误拒率和响应质量的同时显著增强了安全性，为防御越狱提供了新方向。

---

## #259 — Multi-Level Safety Continual Projection for Fine-Tuned Large Language Models without Retraining

`C` Score: 5.46 | 2025-08-08

**Authors:** Bing Han, Feifei Zhao, Dongcheng Zhao, Guobin Shen, Ping Wu, Yu Shi et al. (7 total)

**Categories:** cs.LG, cs.AI

**Scores:** Citation: 3.90 | Influential: 7.81 | Venue: 2.00 | Author: 8.33 | Recency: 7.00

**Links:** [arXiv](https://arxiv.org/abs/2508.09190) | [PDF](https://arxiv.org/pdf/2508.09190)

> 针对微调导致LLM安全对齐表示退化的问题，本文提出了一种无需重新训练的微调后安全增强方法——多级安全持续投影（MSCP）。该方法通过协调的多级表示隐式对齐全局和局部安全激活，应用可组合的安全方向投影来抑制有害输出，在最小参数扰动下显著降低危害评分和攻击成功率，同时保持模型效用。

---

## #260 — AntiDote: Bi-level Adversarial Training for Tamper-Resistant LLMs

`C` Score: 5.46 | 2025-09-06

**Authors:** Debdeep Sanyal, Manodeep Ray, Murari Mandal

**Categories:** cs.CL

**Scores:** Citation: 4.03 | Influential: 7.81 | Venue: 10.00 | Author: 2.55 | Recency: 7.00

**Links:** [arXiv](https://arxiv.org/abs/2509.08000) | [PDF](https://arxiv.org/pdf/2509.08000)

> 本文提出了AntiDote，一种双层优化对抗训练方法，旨在防止开源大模型被恶意微调以移除安全护栏。该方法利用对抗超网络生成恶意LoRA权重，迫使防御模型在保持通用能力的同时抵消这些权重的影响。实验表明，该方法在对抗恶意篡改方面比基线提升27.4%的鲁棒性，且对模型性能影响极小。

---

## #261 — Pruning Unsafe Tickets: A Resource-Efficient Framework for Safer and More Robust LLMs

`C` Score: 5.45 | 2026-04-17

**Authors:** Wai Man Si, Mingjie Li, Michael Backes, Yang Zhang

**Categories:** cs.LG, cs.CL

**Scores:** Citation: 3.32 | Influential: 7.81 | Venue: 2.00 | Author: 7.99 | Recency: 10.00

**Links:** [arXiv](https://arxiv.org/abs/2604.15780) | [PDF](https://arxiv.org/pdf/2604.15780)

> 本文提出了一种资源高效的剪枝框架，用于识别和移除与不安全行为相关的参数，同时保留模型效用。该方法采用无梯度归因机制，仅需适度GPU资源，可跨架构和量化变体推广。实验表明，该方法能显著减少不安全输出并提高对越狱攻击的鲁棒性，同时效用损失最小。从彩票假设角度看，ML模型包含'不安全彩票'，剪枝可揭示'安全彩票'，提供轻量级事后对齐策略。

---

## #262 — Consistency Training Helps Stop Sycophancy and Jailbreaks

`C` Score: 5.44 | 2025-10-31

**Authors:** Alex Irpan, Alexander Matt Turner, Mark Kurzeja, David K. Elson, Rohin Shah

**Categories:** cs.LG, cs.AI

**Scores:** Citation: 3.32 | Influential: 7.81 | Venue: 2.00 | Author: 8.55 | Recency: 9.00

**Links:** [arXiv](https://arxiv.org/abs/2510.27062) | [PDF](https://arxiv.org/pdf/2510.27062)

> 针对大语言模型易受提示词微小变化影响而产生阿谀奉承或越狱行为的问题，本文提出了一致性训练这一自监督范式，旨在教导模型对提示词中不相关的线索保持不变。研究通过在模型外部输出（BCT）和内部激活（ACT）两个层面强制执行这种不变性，利用模型自身生成的响应作为训练数据，从而增强模型的鲁棒性。实验表明，该方法有效降低了Gemini 2.5 Flash对诱导性提问及越狱文本的敏感性，提升了模型的安全性。

---

## #263 — AttentionDefense: Leveraging System Prompt Attention for Explainable Defense Against Novel Jailbreaks

`C` Score: 5.43 | 2025-04-10

**Authors:** Charlotte Siska, Anush Sankaran

**Categories:** cs.CL, cs.AI

**Scores:** Citation: 3.53 | Influential: 7.81 | Venue: 5.00 | Author: 8.55 | Recency: 5.00

**Links:** [arXiv](https://arxiv.org/abs/2504.12321) | [PDF](https://arxiv.org/pdf/2504.12321)

> 本文提出了一种利用小语言模型系统提示注意力机制的可解释防御方法AttentionDefense。通过分析注意力权重来表征对抗性提示，该方法在检测新型越狱攻击方面表现出色，且比基于嵌入的分类器更具成本效益和可解释性。

---

## #264 — Efficient Safety Retrofitting Against Jailbreaking for LLMs

`C` Score: 5.41 | 2025-02-19

**Authors:** Dario Garcia-Gasulla, Adrian Tormos, Anna Arias-Duart, Daniel Hinjos, Oscar Molina-Sedano, Ashwin Kumar Gururajan et al. (7 total)

**Categories:** cs.CL, cs.AI, cs.LG

**Scores:** Citation: 4.74 | Influential: 7.81 | Venue: 5.00 | Author: 4.79 | Recency: 5.00

**Links:** [arXiv](https://arxiv.org/abs/2502.13603) | [PDF](https://arxiv.org/pdf/2502.13603)

> 本文研究了直接偏好优化(DPO)在提升LLM安全性方面的有效性，引入了包含27个安全主题和18种攻击风格的Egida数据集。研究表明，少量训练样本即可显著降低攻击成功率(10%-30%)，且模型能泛化到未见过的主题和攻击风格，为高效LLM安全对齐提供了实用方案。

---

## #265 — Attention-Aware GNN-based Input Defense against Multi-Turn LLM Jailbreak

`C` Score: 5.40 | 2025-07-09

**Authors:** Zixuan Huang, Kecheng Huang, Lihao Yin, Bowei He, Huiling Zhen, Mingxuan Yuan et al. (7 total)

**Categories:** cs.LG, cs.CL

**Scores:** Citation: 4.72 | Influential: 9.02 | Venue: 2.00 | Author: 3.78 | Recency: 7.00

**Links:** [arXiv](https://arxiv.org/abs/2507.07146) | [PDF](https://arxiv.org/pdf/2507.07146)

> 本文提出G-Guard，一种注意力感知GNN输入分类器，专门防御LLM多轮越狱攻击。G-Guard为多轮查询构建实体图，捕获查询间关系和有害关键词，并通过注意力感知机制检索最相关单轮查询作为标记节点。评估表明，G-Guard在多样数据集和指标上一致优于所有基线，成为对抗多轮越狱攻击的稳健防御机制。

---

## #266 — PromptScreen: Efficient Jailbreak Mitigation Using Semantic Linear Classification in a Multi-Staged Pipeline

`C` Score: 5.40 | 2025-12-22

**Authors:** Akshaj Prashanth Rao, Advait Singh, Saumya Kumaar Saksena, Dhruv Kumar

**Categories:** cs.CR, cs.AI, cs.CL

**Scores:** Citation: 5.00 | Influential: 7.81 | Venue: 2.00 | Author: 3.23 | Recency: 9.00

**Links:** [arXiv](https://arxiv.org/abs/2512.19011) | [PDF](https://arxiv.org/pdf/2512.19011)

> 提出PromptScreen，一种基于多阶段流水线的高效越狱防御架构。其核心利用文本归一化、TF-IDF和线性SVM分类器构建语义过滤器，在保持极低计算开销的同时，将防御准确率提升至93.4%，显著降低了攻击吞吐量并优于现有模型版主。

---

## #267 — PopAlign: Diversifying Contrasting Patterns for a More Comprehensive Alignment

`C` Score: 5.40 | 2024-10-17

**Authors:** Zekun Moore Wang, Shawn Wang, Kang Zhu, Jiaheng Liu, Ke Xu, Jie Fu et al. (8 total)

**Categories:** cs.CL, cs.AI

**Scores:** Citation: 3.82 | Influential: 9.02 | Venue: 2.00 | Author: 7.80 | Recency: 5.00

**Links:** [arXiv](https://arxiv.org/abs/2410.13785) | [PDF](https://arxiv.org/pdf/2410.13785)

> 本文针对现有大语言模型对齐方法中对比模式单一导致对齐不全面及易受越狱攻击的问题，提出了PopAlign框架。该框架在提示、模型和流程层面整合了多样化的对比模式，引入六种无需额外反馈标注的对比策略，实验证明其能显著优于现有方法，实现更全面的模型对齐并增强安全性。

---

## #268 — FlexLLM: Exploring LLM Customization for Moving Target Defense on Black-Box LLMs Against Jailbreak Attacks

`C` Score: 5.40 | 2024-12-10

**Authors:** Bocheng Chen, Hanqing Guo, Qiben Yan

**Categories:** cs.CR, cs.CL

**Scores:** Citation: 4.50 | Influential: 7.81 | Venue: 2.00 | Author: 7.43 | Recency: 5.00

**Links:** [arXiv](https://arxiv.org/abs/2412.07672) | [PDF](https://arxiv.org/pdf/2412.07672)

> 本文提出了FlexLLM，一种针对黑盒大语言模型的移动目标防御方法。该方法通过动态调整解码超参数和系统提示词来改变模型行为，无需访问内部结构或额外训练即可有效缓解越狱攻击。实验表明，该防御策略在降低推理成本的同时保持了响应质量，是现有防御手段的有力补充。

---

## #269 — MrGuard: A Multilingual Reasoning Guardrail for Universal LLM Safety

`C` Score: 5.39 | 2025-04-21

**Authors:** Yahan Yang, Soham Dan, Shuo Li, Dan Roth, Insup Lee

**Categories:** cs.CL

**Scores:** Citation: 3.57 | Influential: 7.81 | Venue: 10.00 | Author: 4.79 | Recency: 5.00

**Links:** [arXiv](https://arxiv.org/abs/2504.15241) | [PDF](https://arxiv.org/pdf/2504.15241)

> 本文介绍了MrGuard，一个具备推理能力的多语言安全护栏，旨在检测和过滤多语言环境下的不安全内容。该方法通过合成多语言数据、监督微调以及基于课程的GRPO框架来提升性能，在域内和域外语言上均优于基线模型。实验证明，MrGuard对代码混合等语言变体具有鲁棒性，并能生成解释性反馈。

---

## #270 — DecipherGuard: Understanding and Deciphering Jailbreak Prompts for a Safer Deployment of Intelligent Software Systems

`C` Score: 5.39 | 2025-09-21

**Authors:** Rui Yang, Michael Fu, Chakkrit Tantithamthavorn, Chetan Arora, Gunel Gulmammadova, Joey Chua

**Categories:** cs.SE, cs.CR

**Scores:** Citation: 3.32 | Influential: 7.81 | Venue: 2.00 | Author: 9.58 | Recency: 7.00

**Links:** [arXiv](https://arxiv.org/abs/2509.16870) | [PDF](https://arxiv.org/pdf/2509.16870)

> 针对大语言模型软件系统在运行时面临的越狱攻击威胁，本文提出了DecipherGuard框架。该框架集成了解密层以对抗混淆提示，并利用低秩适应机制增强对模板攻击的防御能力。实验表明，DecipherGuard在防御成功率上显著优于LlamaGuard等现有护栏。

---

## #271 — GSAE: Graph-Regularized Sparse Autoencoders for Robust LLM Safety Steering

`C` Score: 5.39 | 2025-12-07

**Authors:** Jehyeok Yeon, Federico Cinus, Yifan Wu, Luca Luceri

**Categories:** cs.LG, cs.AI

**Scores:** Citation: 4.79 | Influential: 7.81 | Venue: 2.00 | Author: 3.78 | Recency: 9.00

**Links:** [arXiv](https://arxiv.org/abs/2512.06655) | [PDF](https://arxiv.org/pdf/2512.06655)

> 论文提出了图正则化稀疏自编码器（GSAE），通过恢复平滑的分布式安全表示来增强LLM的安全性。该方法利用两级门控机制在运行时进行自适应干预，在保持良性查询效用的同时显著提高了选择性拒绝率，优于传统的单特征干预方法。

---

## #272 — MV-Debate: Multi-view Agent Debate with Dynamic Reflection Gating for Multimodal Harmful Content Detection in Social Media

`C` Score: 5.38 | 2025-08-07

**Authors:** Rui Lu, Jinhe Bi, Yunpu Ma, Feng Xiao, Yuntao Du, Yijun Tian

**Categories:** cs.AI

**Scores:** Citation: 4.88 | Influential: 7.81 | Venue: 2.00 | Author: 4.79 | Recency: 7.00

**Links:** [arXiv](https://arxiv.org/abs/2508.05557) | [PDF](https://arxiv.org/pdf/2508.05557)

> 针对社交媒体中多模态有害内容检测的挑战，本文提出了MV-Debate框架，该框架利用动态反思门控机制组织多视图智能体辩论。MV-Debate集合了表面分析师、深度推理者等四个互补的辩论代理，通过迭代辩论和反思来细化响应，实验表明该方法在统一的多模态有害内容检测中显著优于现有的单模型和多智能体辩论基线。

---

## #273 — Mitigating Adversarial Perturbations for Deep Reinforcement Learning via Vector Quantization

`C` Score: 5.38 | 2024-10-04

**Authors:** Tung M. Luu, Thanh Nguyen, Tee Joshua Tian Jin, Sungwoon Kim, Chang D. Yoo

**Categories:** cs.LG, cs.AI

**Scores:** Citation: 4.31 | Influential: 7.81 | Venue: 5.00 | Author: 5.88 | Recency: 5.00

**Links:** [arXiv](https://arxiv.org/abs/2410.03376) | [PDF](https://arxiv.org/pdf/2410.03376)

> 本研究提出了一种基于输入变换的深度强化学习防御方法，利用向量量化技术对输入观测值进行变换。该方法通过减少对抗性攻击的空间，有效降低了测试阶段观测值受攻击的影响。实验表明，该方法计算效率高，且能与对抗训练无缝集成，显著增强了智能体对抗对抗性攻击的鲁棒性。

---

## #274 — Distributed Detection of Adversarial Attacks in Multi-Agent Reinforcement Learning with Continuous Action Space

`C` Score: 5.37 | 2025-08-21

**Authors:** Kiarash Kazari, Ezzeldin Shereen, György Dán

**Categories:** cs.LG, cs.MA

**Scores:** Citation: 3.99 | Influential: 7.81 | Venue: 5.00 | Author: 5.40 | Recency: 7.00

**Links:** [arXiv](https://arxiv.org/abs/2508.15764) | [PDF](https://arxiv.org/pdf/2508.15764)

> 本文针对连续动作空间下的协作多智能体强化学习，提出了一种基于局部观测的分布式对抗攻击检测方法。该方法利用深度神经网络近似智能体的正常行为，并通过CUSUM程序实时检测异常行为。在多个基准测试中的结果表明，该方法能有效检测高影响力的对抗性攻击，且性能优于离散空间的方法。

---

## #275 — ReasoningGuard: Safeguarding Large Reasoning Models with Inference-time Safety Aha Moments

`C` Score: 5.37 | 2025-08-06

**Authors:** Yuquan Wang, Mi Zhang, Yining Wang, Geng Hong, Xiaoyu You, Min Yang

**Categories:** cs.CL, cs.AI

**Scores:** Citation: 4.87 | Influential: 7.81 | Venue: 2.00 | Author: 4.79 | Recency: 7.00

**Links:** [arXiv](https://arxiv.org/abs/2508.04204) | [PDF](https://arxiv.org/pdf/2508.04204)

> 本文提出了ReasoningGuard，一种针对大型推理模型的推理时安全防护机制。该方法利用模型的内部注意力行为识别推理路径中的关键点，注入及时的安全反思时刻，并采用缩放采样策略选择最优推理路径，从而有效缓解越狱攻击。

---

## #276 — Dual-Space Smoothness for Robust and Balanced LLM Unlearning

`C` Score: 5.37 | 2025-09-27

**Authors:** Han Yan, Zheyuan Liu, Meng Jiang

**Categories:** cs.CL, cs.AI

**Scores:** Citation: 5.38 | Influential: 7.81 | Venue: 2.00 | Author: 3.23 | Recency: 7.00

**Links:** [arXiv](https://arxiv.org/abs/2509.23362) | [PDF](https://arxiv.org/pdf/2509.23362)

> 本文提出了PRISM统一框架，通过在表示空间和参数空间强制执行双重平滑性，解决了机器遗忘中的灾难性遗忘和指标不平衡问题。该方法利用鲁棒训练探针防御越狱攻击，并通过解耦梯度冲突平滑参数空间，有效缓解了重学习攻击，在多个指标上实现了更好的平衡。

---

## #277 — WebAgentGuard: A Reasoning-Driven Guard Model for Detecting Prompt Injection Attacks in Web Agents

`C` Score: 5.37 | 2026-04-14

**Authors:** Yulin Chen, Tri Cao, Haoran Li, Yue Liu, Yibo Li, Yufei He et al. (10 total)

**Categories:** cs.CR

**Scores:** Citation: 3.32 | Influential: 7.81 | Venue: 2.00 | Author: 7.43 | Recency: 10.00

**Links:** [arXiv](https://arxiv.org/abs/2604.12284) | [PDF](https://arxiv.org/pdf/2604.12284)

> 本文提出了WebAgentGuard，一个用于检测Web Agent中提示注入攻击的推理驱动型防护模型。该框架使Web Agent与专用防护代理并行运行，将提示注入检测与代理自身的推理解耦。作者构建了包含164个主题和230种视觉和UI设计风格的合成多模态数据集，通过推理密集的监督微调和强化学习训练模型。实验表明，WebAgentGuard在多个基准测试中优于强基线方法，同时保留代理效用且不引入额外延迟。

---

## #278 — Adapting Insider Risk mitigations for Agentic Misalignment: an empirical study

`C` Score: 5.36 | 2025-10-06

**Authors:** Francesca Gomez

**Categories:** cs.CR, cs.AI

**Scores:** Citation: 5.54 | Influential: 9.02 | Venue: 2.00 | Author: 1.12 | Recency: 7.00

**Links:** [arXiv](https://arxiv.org/abs/2510.05192) | [PDF](https://arxiv.org/pdf/2510.05192)

> 本文将内部风险控制设计（如关键路径和情境犯罪预防）应用于缓解智能体错位问题，旨在防止目标导向智能体在面临压力时采取有害行动。通过在10个LLM上的大规模实验，研究发现引入外部管理的升级通道能将勒索率从38.73%显著降低至1.21%。这表明将预防性操作控制纳入深度防御策略能有效增强智能体AI的安全性。

---

## #279 — One Trigger Token Is Enough: A Defense Strategy for Balancing Safety and Usability in Large Language Models

`C` Score: 5.35 | 2025-05-12

**Authors:** Haoran Gu, Handing Wang, Yi Mei, Mengjie Zhang, Yaochu Jin

**Categories:** cs.CR, cs.CL

**Scores:** Citation: 3.32 | Influential: 7.81 | Venue: 2.00 | Author: 9.28 | Recency: 7.00

**Links:** [arXiv](https://arxiv.org/abs/2505.07167) | [PDF](https://arxiv.org/pdf/2505.07167)

> 本文深入研究了LLMs浅层安全对齐的机制，揭示了通过“安全触发令牌”激活安全模式的现象。作者提出了D-STT防御算法，通过识别并显式解码单个安全触发令牌来激活模型的安全模式，从而在最小干预下平衡安全性和可用性。实验表明，D-STT在减少输出有害性的同时保持了模型可用性，且响应时间开销可忽略不计。

---

## #280 — SafeSteer: Adaptive Subspace Steering for Efficient Jailbreak Defense in Vision-Language Models

`C` Score: 5.33 | 2025-09-24

**Authors:** Xiyu Zeng, Siyuan Liang, Liming Lu, Haotian Zhu, Enguang Liu, Jisheng Dang et al. (8 total)

**Categories:** cs.CR

**Scores:** Citation: 5.30 | Influential: 7.81 | Venue: 2.00 | Author: 3.23 | Recency: 7.00

**Links:** [arXiv](https://arxiv.org/abs/2509.21400) | [PDF](https://arxiv.org/pdf/2509.21400)

> 针对视觉语言模型面临的越狱攻击，本文提出了SafeSteer，一种轻量级的推理时引导防御框架。该框架创新性地利用奇异值分解构建低维“安全子空间”，通过在推理过程中投影和重构引导向量，自适应地移除有害生成信号，同时保留模型对良性输入的处理能力。SafeSteer无需修改模型权重，且仅引入可忽略的计算开销，有效解决了现有防御方法在安全性与实用性之间的权衡问题。

---

## #281 — Risk Awareness Injection: Calibrating Vision-Language Models for Safety without Compromising Utility

`C` Score: 5.33 | 2026-02-03

**Authors:** Mengxuan Wang, Yuxin Chen, Gang Xu, Tao He, Hongjie Jiang, Ming Li

**Categories:** cs.AI, cs.LG

**Scores:** Citation: 3.32 | Influential: 7.81 | Venue: 2.00 | Author: 7.15 | Recency: 10.00

**Links:** [arXiv](https://arxiv.org/abs/2602.03402) | [PDF](https://arxiv.org/pdf/2602.03402)

> 本文针对视觉语言模型（VLM）易受多模态越狱攻击且现有防御成本高昂或损害效用的问题，提出了风险感知注入（RAI）框架。RAI是一种轻量级且无需训练的方法，通过构建不安全原型子空间并对高风险视觉token进行针对性调制，放大不安全信号以恢复模型对不安全内容的检测能力。实验表明，RAI在大幅降低攻击成功率的同时，保持了跨模态推理的任务性能。

---

## #282 — Step-Wise Refusal Dynamics in Autoregressive and Diffusion Language Models

`C` Score: 5.33 | 2026-02-01

**Authors:** Eliron Rahimi, Elad Hirshel, Rom Himelstein, Amit LeVi, Avi Mendelson, Chaim Baskin

**Categories:** cs.LG, cs.AI

**Scores:** Citation: 3.32 | Influential: 7.81 | Venue: 2.00 | Author: 7.15 | Recency: 10.00

**Links:** [arXiv](https://arxiv.org/abs/2602.02600) | [PDF](https://arxiv.org/pdf/2602.02600)

> 本文分析了自回归和扩散语言模型中的逐步拒绝动态，揭示了采样策略在安全行为中的核心作用。作者引入了逐步拒绝内部动力学（SRI）信号，用于识别有害生成中的异常行为，即“不完全内部恢复”。基于 SRI 的轻量级推理时检测器能有效泛化到未见过的攻击，且开销极低。

---

## #283 — From Shallow to Deep: Pinning Semantic Intent via Causal GRPO

`C` Score: 5.33 | 2026-03-03

**Authors:** Shuyi Zhou, Zeen Song, Wenwen Qiang, Jiyan Sun, Yao Zhou, Yinlong Liu et al. (7 total)

**Categories:** cs.LG

**Scores:** Citation: 3.32 | Influential: 7.81 | Venue: 2.00 | Author: 7.15 | Recency: 10.00

**Links:** [arXiv](https://arxiv.org/abs/2603.02675) | [PDF](https://arxiv.org/pdf/2603.02675)

> 针对大模型“浅层安全对齐”导致的语义表征衰减问题，本文提出了TSC-GRPO框架。该方法利用因果意图探针和累积因果惩罚机制，强制模型在生成有害令牌时进行拒绝。实验证明，该方法在显著防御越狱攻击的同时保持了模型的通用效用。

---

## #284 — DualSentinel: A Lightweight Framework for Detecting Targeted Attacks in Black-box LLM via Dual Entropy Lull Pattern

`C` Score: 5.33 | 2026-03-02

**Authors:** Xiaoyi Pang, Xuanyi Hao, Pengyu Liu, Qi Luo, Song Guo, Zhibo Wang

**Categories:** cs.CR, cs.AI

**Scores:** Citation: 3.32 | Influential: 7.81 | Venue: 2.00 | Author: 7.15 | Recency: 10.00

**Links:** [arXiv](https://arxiv.org/abs/2603.01574) | [PDF](https://arxiv.org/pdf/2603.01574)

> 提出DualSentinel，一种针对黑盒大模型目标攻击的轻量级检测框架。该方法利用“熵平静”模式特征，结合幅度趋势监控和任务翻转双重验证机制。实验证明，DualSentinel能准确及时地检测后门和提示注入等攻击，且不阻碍正常推理。

---

## #285 — ADAG: Automatically Describing Attribution Graphs

`C` Score: 5.33 | 2026-04-08

**Authors:** Aryaman Arora, Zhengxuan Wu, Jacob Steinhardt, Sarah Schwettmann

**Categories:** cs.CL

**Scores:** Citation: 3.32 | Influential: 7.81 | Venue: 2.00 | Author: 7.15 | Recency: 10.00

**Links:** [arXiv](https://arxiv.org/abs/2604.07615) | [PDF](https://arxiv.org/pdf/2604.07615)

> ADAG是一种自动化管道，用于描述语言模型中的归因图，解决了传统电路追踪依赖人工解释的问题。它通过引入'归因配置文件'量化特征功能角色，使用新颖聚类算法分组特征，并利用LLM解释器-模拟器生成自然语言解释。该系统在已知电路追踪任务上运行可恢复可解释电路，并能发现负责有害建议绕过的可引导集群。

---

## #286 — Exclusive Unlearning

`C` Score: 5.33 | 2026-04-07

**Authors:** Mutsumi Sasaki, Kouta Nakayama, Yusuke Miyao, Yohei Oseki, Masaru Isonuma

**Categories:** cs.CL

**Scores:** Citation: 3.32 | Influential: 7.81 | Venue: 2.00 | Author: 7.15 | Recency: 10.00

**Links:** [arXiv](https://arxiv.org/abs/2604.06154) | [PDF](https://arxiv.org/pdf/2604.06154)

> Exclusive Unlearning (EU)提出了一种新方法，通过广泛遗忘除保留知识和表达之外的一切，实现广泛危害移除。与现有机器遗忘方法不同，EU不单独列出遗忘目标，而是确保模型对广泛输入（包括越狱）的安全性，同时保持对特定领域（如医学和数学）相关多样化指令的响应能力，解决了工业应用中LLM生成有害内容的挑战。

---

## #287 — Unified Defense for Large Language Models against Jailbreak and Fine-Tuning Attacks in Education

`C` Score: 5.32 | 2025-11-18

**Authors:** Xin Yi, Yue Li, Dongsheng Shi, Linlin Wang, Xiaoling Wang, Liang He

**Categories:** cs.CL

**Scores:** Citation: 4.64 | Influential: 7.81 | Venue: 2.00 | Author: 3.78 | Recency: 9.00

**Links:** [arXiv](https://arxiv.org/abs/2511.14423) | [PDF](https://arxiv.org/pdf/2511.14423)

> 本文针对教育场景中的大语言模型，构建了EduHarm基准测试，并提出了三阶段护盾框架（TSSF）以防御越狱和微调攻击。该框架通过安全感知注意力重对齐、逐层安全判断和防御驱动的双路由机制，有效识别并处理有害指令。实验表明，TSSF在增强安全性的同时，防止了对良性查询的过度拒绝，实现了鲁棒的防御效果。

---

## #288 — Improving the Safety and Trustworthiness of Medical AI via Multi-Agent Evaluation Loops

`C` Score: 5.32 | 2026-01-19

**Authors:** Zainab Ghafoor, Md Shafiqul Islam, Koushik Howlader, Md Rasel Khondokar, Tanusree Bhattacharjee, Sayantan Chakraborty et al. (9 total)

**Categories:** cs.AI

**Scores:** Citation: 5.72 | Influential: 7.81 | Venue: 2.00 | Author: 0.58 | Recency: 9.00

**Links:** [arXiv](https://arxiv.org/abs/2601.13268) | [PDF](https://arxiv.org/pdf/2601.13268)

> 本文提出了一种多Agent迭代优化框架，旨在提升医疗LLM的安全性和可信度。该系统结合生成模型与评估Agent，依据美国医学会伦理原则和安全风险评估协议对回复进行迭代修正。实验表明，该框架显著降低了伦理违规率并有效降级风险，为医疗AI的监管合规和安全治理提供了可扩展的范式。

---

## #289 — Read the Scene, Not the Script: Outcome-Aware Safety for LLMs

`C` Score: 5.31 | 2025-10-05

**Authors:** Rui Wu, Yihao Quan, Zeru Shi, Zhenting Wang, Yanshu Li, Ruixiang Tang

**Categories:** cs.CL, cs.LG

**Scores:** Citation: 4.19 | Influential: 9.02 | Venue: 2.00 | Author: 4.79 | Recency: 7.00

**Links:** [arXiv](https://arxiv.org/abs/2510.04320) | [PDF](https://arxiv.org/pdf/2510.04320)

> 本文指出了当前安全对齐LLM存在的“后果盲区”问题，即模型过度依赖表面形式信号而未能有效推理行动与后果之间的联系。为此，作者构建了CB-Bench基准测试，并引入了用于安全对齐的后果推理数据集CS-Chain-4k。实验表明，在该数据集上微调的模型能有效抵御语义伪装越狱，减少对无害输入的过度拒绝，同时保持模型效用。

---

## #290 — Tit-for-Tat: Safeguarding Large Vision-Language Models Against Jailbreak Attacks via Adversarial Defense

`C` Score: 5.30 | 2025-03-14

**Authors:** Shuyang Hao, Yiwei Wang, Bryan Hooi, Ming-Hsuan Yang, Jun Liu, Chengcheng Tang et al. (8 total)

**Categories:** cs.CR

**Scores:** Citation: 3.50 | Influential: 9.02 | Venue: 2.00 | Author: 8.15 | Recency: 5.00

**Links:** [arXiv](https://arxiv.org/abs/2503.11619) | [PDF](https://arxiv.org/pdf/2503.11619)

> 该论文提出ESIII方法，通过将安全指令嵌入图像中，将视觉空间从漏洞来源转变为主动防御机制。结合视觉和文本维度的安全指令，有效增强大型视觉语言模型对抗越狱攻击的鲁棒性，同时保持良性任务性能，计算开销可忽略。

---

## #291 — Optimus: A Robust Defense Framework for Mitigating Toxicity while Fine-Tuning Conversational AI

`C` Score: 5.29 | 2025-07-08

**Authors:** Aravind Cheruvu, Shravya Kanchi, Sifat Muhammad Abdullah, Nicholas Kong, Daphne Yao, Murtuza Jadliwala et al. (7 total)

**Categories:** cs.CR, cs.AI, cs.CL

**Scores:** Citation: 3.32 | Influential: 7.81 | Venue: 2.00 | Author: 8.87 | Recency: 7.00

**Links:** [arXiv](https://arxiv.org/abs/2507.05660) | [PDF](https://arxiv.org/pdf/2507.05660)

> 本文提出了Optimus防御框架，旨在缓解在不可信数据集上微调对话AI时注入的有毒行为。该框架结合了无训练毒性分类和直接偏好优化（DPO），即使依赖有偏分类器也能有效缓解毒性，并展现出对自适应攻击的强韧性。

---

## #292 — DIESEL -- Dynamic Inference-Guidance via Evasion of Semantic Embeddings in LLMs

`C` Score: 5.28 | 2024-11-28

**Authors:** Ben Ganon, Alon Zolfi, Omer Hofman, Inderjeet Singh, Hisashi Kojima, Yuval Elovici et al. (7 total)

**Categories:** cs.CL, cs.LG

**Scores:** Citation: 3.38 | Influential: 7.81 | Venue: 2.00 | Author: 9.97 | Recency: 5.00

**Links:** [arXiv](https://arxiv.org/abs/2411.19038) | [PDF](https://arxiv.org/pdf/2411.19038)

> 本文提出了DIESEL，一种轻量级的推理引导技术，可通过在潜在空间中基于与预定义负面概念的相似性对LLM提出的令牌进行重新排序，从而过滤响应中的不良概念。该方法无需昂贵训练，可作为独立护栏或额外防御层，有效增强对话模型在对抗性越狱场景下的安全性。

---

## #293 — The Cost of Thinking: Increased Jailbreak Risk in Large Language Models

`C` Score: 5.27 | 2025-08-09

**Authors:** Fan Yang

**Categories:** cs.CL, cs.AI

**Scores:** Citation: 3.91 | Influential: 9.02 | Venue: 2.00 | Author: 5.40 | Recency: 7.00

**Links:** [arXiv](https://arxiv.org/abs/2508.10032) | [PDF](https://arxiv.org/pdf/2508.10032)

> 本文揭示了LLM在“思考模式”下更容易受到越狱攻击的惊人现象，并在AdvBench和HarmBench上验证了这一点。研究发现，教育目的和过长的思考长度是攻击成功的特征，为此提出了一种安全思考干预方法，通过在提示中添加特定的思考标记来显式引导模型的内部思考过程，从而显著降低攻击成功率。

---

## #294 — SafePred: A Predictive Guardrail for Computer-Using Agents via World Models

`C` Score: 5.27 | 2026-02-02

**Authors:** Yurun Chen, Zeyi Liao, Ping Yin, Taotao Xie, Keting Yin, Shengyu Zhang

**Categories:** cs.CL, cs.AI, cs.LG

**Scores:** Citation: 3.32 | Influential: 7.81 | Venue: 2.00 | Author: 6.75 | Recency: 10.00

**Links:** [arXiv](https://arxiv.org/abs/2602.01725) | [PDF](https://arxiv.org/pdf/2602.01725)

> 本文提出了 SafePred，一种针对计算机使用智能体的预测护栏框架，旨在解决现有反应性护栏无法预防长期风险的问题。SafePred 利用世界模型预测短期和长期风险，建立风险到决策的循环，从而优化决策并修剪导致高风险状态的动作。该方法通过预测未来风险来确保智能体行为的安全。

---

## #295 — Can Safety Fine-Tuning Be More Principled? Lessons Learned from Cybersecurity

`C` Score: 5.24 | 2025-01-19

**Authors:** David Williams-King, Linh Le, Adam Oberman, Yoshua Bengio

**Categories:** cs.CR, cs.AI, cs.LG

**Scores:** Citation: 3.32 | Influential: 7.81 | Venue: 2.00 | Author: 9.89 | Recency: 5.00

**Links:** [arXiv](https://arxiv.org/abs/2501.11183) | [PDF](https://arxiv.org/pdf/2501.11183)

> 本文将大型语言模型的安全微调与网络安全中的攻防对抗进行类比，指出当前安全微调方法类似于'猫鼠游戏'，仅针对特定攻击进行修补而缺乏系统性防御机制。作者通过分析网络安全历史案例，提出应从过去的防御失败中吸取教训，开发更原则性的安全微调方法，以应对模型越狱攻击、奖励黑客和失控问题等安全挑战。

---

## #296 — PSRT: Accelerating LRM-based Guard Models via Prefilled Safe Reasoning Traces

`C` Score: 5.24 | 2025-09-26

**Authors:** Jiawei Zhao, Yuang Qi, Weiming Zhang, Nenghai Yu, Kejiang Chen

**Categories:** cs.CR

**Scores:** Citation: 3.32 | Influential: 7.81 | Venue: 2.00 | Author: 8.55 | Recency: 7.00

**Links:** [arXiv](https://arxiv.org/abs/2509.21768) | [PDF](https://arxiv.org/pdf/2509.21768)

> 本文针对大推理模型（LRM）作为防御模型时因生成冗长推理痕迹而产生高昂计算开销的问题，提出了PSRT方法。该方法通过预填充“安全推理虚拟令牌”并学习其连续嵌入，替代了模型原本的推理过程，利用指示器令牌在单次前向传递中实现有害查询检测。实验结果显示，PSRT在多个模型和数据集上不仅保持了LRM的分类有效性，还彻底消除了生成推理痕迹带来的性能损耗。

---

## #297 — Safety Game: Balancing Safe and Informative Conversations with Blackbox Agentic AI using LP Solvers

`C` Score: 5.24 | 2025-10-10

**Authors:** Tuan Nguyen, Long Tran-Thanh

**Categories:** cs.LG

**Scores:** Citation: 3.32 | Influential: 7.81 | Venue: 2.00 | Author: 8.55 | Recency: 7.00

**Links:** [arXiv](https://arxiv.org/abs/2510.09330) | [PDF](https://arxiv.org/pdf/2510.09330)

> 提出一种无需重新训练或访问模型内部结构的黑盒安全对齐框架。该方法将安全性与有用性的权衡建模为双人零和博弈，利用线性规划求解器在推理时计算最优平衡策略。这为资源受限环境下的第三方利益相关者提供了一种可扩展的LLM安全执行途径。

---

## #298 — A Biosecurity Agent for Lifecycle LLM Biosecurity Alignment

`C` Score: 5.23 | 2025-09-13

**Authors:** Meiyin Meng, Zaixi Zhang

**Categories:** cs.CR

**Scores:** Citation: 3.32 | Influential: 7.81 | Venue: 5.00 | Author: 6.47 | Recency: 7.00

**Links:** [arXiv](https://arxiv.org/abs/2510.09615) | [PDF](https://arxiv.org/pdf/2510.09615)

> 本文提出了一种生物安全 Agent，通过数据集清理、偏好对齐、运行时护栏和自动化红队测试四种协同模式，实现 LLM 全生命周期的生物安全对齐。实验表明，该方法在保持效用的同时显著降低了攻击成功率，且运行时护栏在安全性和可用性之间取得了良好的平衡。

---

## #299 — RvB: Automating AI System Hardening via Iterative Red-Blue Games

`C` Score: 5.23 | 2026-01-27

**Authors:** Lige Huang, Zicheng Liu, Jie Zhang, Lewen Yan, Dongrui Liu, Jing Shao

**Categories:** cs.CR, cs.AI, cs.CL

**Scores:** Citation: 3.32 | Influential: 7.81 | Venue: 2.00 | Author: 6.47 | Recency: 10.00

**Links:** [arXiv](https://arxiv.org/abs/2601.19726) | [PDF](https://arxiv.org/pdf/2601.19726)

> 本文提出了RvB框架，旨在通过迭代红蓝对抗游戏解决AI系统动态加固缺乏统一框架的问题。该框架将过程构建为无需参数更新的顺序不完美信息博弈，红队通过暴露漏洞驱动蓝队在不更新模型参数的情况下学习有效的防御策略。实验结果显示，该方法在动态代码加固和越狱防御中显著优于基线，能促使蓝队掌握基础防御原则，实现高防御成功率且误报率接近零。

---

## #300 — DRAFT: Task Decoupled Latent Reasoning for Agent Safety

`C` Score: 5.23 | 2026-02-11

**Authors:** Lin Wang, Junfeng Fang, Dan Zhang, Fei Shen, Xiang Wang, Tat-Seng Chua

**Categories:** cs.LG

**Scores:** Citation: 3.32 | Influential: 7.81 | Venue: 2.00 | Author: 6.47 | Recency: 10.00

**Links:** [arXiv](https://arxiv.org/abs/2604.03242) | [PDF](https://arxiv.org/pdf/2604.03242)

> 本文提出了DRAFT，一种用于智能体安全的任务解耦潜在推理框架，旨在解决长轨迹交互中风险证据稀疏导致的监督难题。该框架将安全判断解耦为提取器和推理器两个阶段，在潜在空间中进行证据聚合，避免了显式摘要带来的信息损失。实验表明，DRAFT在多个基准测试上显著优于基线模型，证明了连续潜在推理是实现长上下文监督下鲁棒智能体安全的有效路径。

---

## #301 — Towards Optimal Adversarial Robust Reinforcement Learning with Infinity Measurement Error

`C` Score: 5.22 | 2025-02-23

**Authors:** Haoran Li, Zicheng Zhang, Wang Luo, Congying Han, Jiayu Lv, Tiande Guo et al. (7 total)

**Categories:** cs.LG

**Scores:** Citation: 3.48 | Influential: 7.81 | Venue: 2.00 | Author: 9.28 | Recency: 5.00

**Links:** [arXiv](https://arxiv.org/abs/2502.16734) | [PDF](https://arxiv.org/pdf/2502.16734)

> 本文探讨深度强化学习(DRL)代理在对抗攻击下的鲁棒性问题。作者引入内在状态对抗马尔可夫决策过程(ISA-MDP)的新框架，证明在ISA-MDP中存在确定性和平稳的最优鲁棒策略(ORP)。研究展示了无限测量误差(IME)在实现ORP中的必要性，揭示了依赖1-测量误差的先前DRL算法的漏洞。基于这些见解，作者开发了CAR-RL框架，应用于基于值和基于策略的DRL算法，取得了优越的性能。

---

## #302 — CoCoTen: Detecting Adversarial Inputs to Large Language Models through Latent Space Features of Contextual Co-occurrence Tensors

`C` Score: 5.22 | 2025-08-05

**Authors:** Sri Durga Sai Sowmya Kadali, Evangelos E. Papalexakis

**Categories:** cs.CL

**Scores:** Citation: 4.85 | Influential: 7.81 | Venue: 5.00 | Author: 1.86 | Recency: 7.00

**Links:** [arXiv](https://arxiv.org/abs/2508.02997) | [PDF](https://arxiv.org/pdf/2508.02997)

> 本文提出了一种利用上下文共现矩阵和张量的潜在空间特征来有效识别对抗性和越狱提示的新方法。该方法在仅使用0.5%标记提示的情况下实现了显著的F1分数，且速度比基线模型快2.3到128.4倍。

---

## #303 — Think-Reflect-Revise: A Policy-Guided Reflective Framework for Safety Alignment in Large Vision Language Models

`C` Score: 5.21 | 2025-12-08

**Authors:** Fenghua Weng, Chaochao Lu, Xia Hu, Wenqi Shao, Wenjie Wang

**Categories:** cs.CV, cs.CL

**Scores:** Citation: 4.81 | Influential: 7.81 | Venue: 2.00 | Author: 2.55 | Recency: 9.00

**Links:** [arXiv](https://arxiv.org/abs/2512.07141) | [PDF](https://arxiv.org/pdf/2512.07141)

> 论文提出了Think-Reflect-Revise框架，通过策略引导的自我反思机制增强大型视觉语言模型的安全性。该三阶段训练框架利用第一轮推理中暴露的恶意内容进行自我修正，有效提升了模型对抗视觉和上下文越狱攻击的能力，显著提高了安全响应率。

---

## #304 — Geometry-Guided Adversarial Prompt Detection via Curvature and Local Intrinsic Dimension

`C` Score: 5.20 | 2025-03-05

**Authors:** Canaan Yung, Hanxun Huang, Christopher Leckie, Sarah Erfani

**Categories:** cs.CL, cs.AI

**Scores:** Citation: 3.49 | Influential: 7.81 | Venue: 2.00 | Author: 9.09 | Recency: 5.00

**Links:** [arXiv](https://arxiv.org/abs/2503.03502) | [PDF](https://arxiv.org/pdf/2503.03502)

> 本文引入了CurvaLID，一个新的防御框架，通过利用对抗提示的几何特性来高效检测它们。该框架基于文本提示的几何分析来揭示它们之间的根本差异，通过Whewell方程将曲率概念扩展到n维词嵌入空间，并利用局部内在维度来捕获对抗子空间中文本提示的互补几何特征。研究表明，对抗提示与良性提示具有不同的几何特征，使CurvaLID能够有效识别它们。

---

## #305 — EnchTable: Unified Safety Alignment Transfer in Fine-tuned Large Language Models

`C` Score: 5.20 | 2025-11-13

**Authors:** Jialin Wu, Kecen Li, Zhicong Huang, Xinfeng Li, Xiaofeng Wang, Cheng Hong

**Categories:** cs.CL, cs.CR

**Scores:** Citation: 4.57 | Influential: 7.81 | Venue: 2.00 | Author: 3.23 | Recency: 9.00

**Links:** [arXiv](https://arxiv.org/abs/2511.09880) | [PDF](https://arxiv.org/pdf/2511.09880)

> 本文针对大型语言模型微调过程中安全对齐退化的问题，提出了EnchTable框架，旨在无需大量重训练的情况下迁移和维护下游模型的安全对齐。该框架利用基于神经正切核（NTK）的安全向量蒸馏技术解耦安全约束与任务推理，并通过干扰感知合并技术平衡安全性与实用性。实验表明，EnchTable在多个任务域和架构上表现出色，且对静态和动态越狱攻击具有强大的抵抗力。

---

## #306 — A Grounded Observer Framework for Establishing Guardrails for Foundation Models in Socially Sensitive Domains

`C` Score: 5.20 | 2024-12-23

**Authors:** Rebecca Ramnauth, Dražen Brščić, Brian Scassellati

**Categories:** cs.RO, cs.AI

**Scores:** Citation: 3.99 | Influential: 7.81 | Venue: 2.00 | Author: 7.62 | Recency: 5.00

**Links:** [arXiv](https://arxiv.org/abs/2412.18639) | [PDF](https://arxiv.org/pdf/2412.18639)

> 针对基础模型在医疗、金融等社会敏感领域的应用，本文提出了“接地观察者”框架。该方法通过实时评估低级行为特征来动态调整模型动作并提供上下文反馈，为高维模型提供行为保证和实时可变性，已在机器人对话系统中得到验证，确保行为符合社会期望。

---

## #307 — Test-Time Immunization: A Universal Defense Framework Against Jailbreaks for (Multimodal) Large Language Models

`C` Score: 5.19 | 2025-05-28

**Authors:** Yongcan Yu, Yanbo Wang, Ran He, Jian Liang

**Categories:** cs.CR, cs.AI, cs.CL

**Scores:** Citation: 3.68 | Influential: 7.81 | Venue: 2.00 | Author: 7.15 | Recency: 7.00

**Links:** [arXiv](https://arxiv.org/abs/2505.22271) | [PDF](https://arxiv.org/pdf/2505.22271)

> 本文提出了测试时免疫（TIM）框架，一种能够自适应防御多种越狱攻击的通用防御方法。TIM通过训练gist token进行高效检测，并在识别到攻击时利用检测到的越狱指令与拒绝回答进行安全微调。实验表明，该方法在LLM和多模态LLM上均能有效防御各类攻击，且通过解耦检测模块缓解了性能退化。

---

## #308 — Safeguarding Large Language Models in Real-time with Tunable Safety-Performance Trade-offs

`C` Score: 5.18 | 2025-01-02

**Authors:** Joao Fonseca, Andrew Bell, Julia Stoyanovich

**Categories:** cs.CL, cs.AI, cs.CR

**Scores:** Citation: 5.63 | Influential: 7.81 | Venue: 2.00 | Author: 2.55 | Recency: 5.00

**Links:** [arXiv](https://arxiv.org/abs/2501.02018) | [PDF](https://arxiv.org/pdf/2501.02018)

> 这篇论文提出了 SafeNudge，一种结合受控文本生成和'轻推'技术的新型防护方法，用于保护大型语言模型免受越狱攻击。该方法在检测到越狱攻击时触发，通过文本干预引导模型行为，可将成功越狱攻击减少 30%，同时避免了传统防护方法带来的推理时间延长、计算成本增加和语义流畅性降低等问题。

---

## #309 — TrapSuffix: Proactive Defense Against Adversarial Suffixes in Jailbreaking

`C` Score: 5.18 | 2026-02-06

**Authors:** Mengyao Du, Han Fang, Haokai Ma, Gang Yang, Quanjun Yin, Shouling Ji et al. (7 total)

**Categories:** cs.CR

**Scores:** Citation: 3.32 | Influential: 7.81 | Venue: 2.00 | Author: 6.17 | Recency: 10.00

**Links:** [arXiv](https://arxiv.org/abs/2602.06630) | [PDF](https://arxiv.org/pdf/2602.06630)

> 本文提出了TrapSuffix，一种针对基于后缀的越狱攻击的主动防御方法。该方法通过轻量级微调在基础模型中注入陷阱对齐行为，迫使攻击者要么陷入优化陷阱，要么生成带有可追踪指纹的后缀。实验表明，TrapSuffix将平均攻击成功率降至极低水平，且不引入推理开销。

---

## #310 — GUARD-SLM: Token Activation-Based Defense Against Jailbreak Attacks for Small Language Models

`C` Score: 5.18 | 2026-03-28

**Authors:** Md Jueal Mia, Joaquin Molto, Yanzhao Wu, M. Hadi Amini

**Categories:** cs.CR, cs.AI

**Scores:** Citation: 3.32 | Influential: 7.81 | Venue: 2.00 | Author: 6.17 | Recency: 10.00

**Links:** [arXiv](https://arxiv.org/abs/2603.28817) | [PDF](https://arxiv.org/pdf/2603.28817)

> 本文针对小语言模型在资源受限环境下面临的越狱攻击威胁，提出了GUARD-SLM这一基于令牌激活的轻量级防御方法。通过对多种攻击和模型架构的实证研究，作者发现不同输入类型在内部表示空间中形成可区分的模式，并据此设计在推理过程中过滤恶意提示的机制。实验结果表明，该方法在保留良性提示的同时有效拦截恶意输入，为安全部署小语言模型提供了实用方向。

---

## #311 — From Where Words Come: Efficient Regularization of Code Tokenizers Through Source Attribution

`C` Score: 5.18 | 2026-04-15

**Authors:** Pavel Chizhov, Egor Bogomolov, Ivan P. Yamshchikov

**Categories:** cs.CL

**Scores:** Citation: 3.32 | Influential: 7.81 | Venue: 2.00 | Author: 6.17 | Recency: 10.00

**Links:** [arXiv](https://arxiv.org/abs/2604.14053) | [PDF](https://arxiv.org/pdf/2604.14053)

> 本文研究代码分词效率，特别是从数据源多样性角度。演示代码分词器易产生未使用和训练不足的令牌。通过修改BPE目标并引入合并跳过，实现源属性BPE(SA-BPE)技术，正则化BPE训练并最小化过拟合。这显著减少训练不足令牌数量，同时保持与常规BPE相同的推理过程，为生产环境提供有效工具，提高LLMs的效率和安全性。

---

## #312 — No Free Lunch for Defending Against Prefilling Attack by In-Context Learning

`C` Score: 5.18 | 2024-12-13

**Authors:** Zhiyu Xue, Guangliang Liu, Bocheng Chen, Kristen Marie Johnson, Ramtin Pedarsani

**Categories:** cs.CR, cs.AI

**Scores:** Citation: 3.40 | Influential: 7.81 | Venue: 2.00 | Author: 9.23 | Recency: 5.00

**Links:** [arXiv](https://arxiv.org/abs/2412.12192) | [PDF](https://arxiv.org/pdf/2412.12192)

> 本文探讨了利用上下文学习（ICL）防御大模型预填充攻击的有效性与局限性。研究表明，虽然通过在演示中使用对抗性句子结构可以有效防御预填充越狱攻击，但模型会出现过度防御现象，且现有安全对齐方法无法缓解此类攻击。结论指出ICL防御并非“免费午餐”，存在特定的权衡与挑战。

---

## #313 — NegBLEURT Forest: Leveraging Inconsistencies for Detecting Jailbreak Attacks

`C` Score: 5.17 | 2025-11-14

**Authors:** Lama Sleem, Jerome Francois, Lujun Li, Nathan Foucher, Niccolo Gentile, Radu State

**Categories:** cs.CR, cs.AI

**Scores:** Citation: 3.32 | Influential: 7.81 | Venue: 5.00 | Author: 4.79 | Recency: 9.00

**Links:** [arXiv](https://arxiv.org/abs/2511.11784) | [PDF](https://arxiv.org/pdf/2511.11784)

> 本文提出了NegBLEURT Forest，一种通过分析对抗性提示引发的响应与预期安全行为之间语义一致性来检测越狱攻击的框架。该方法采用否定感知评分方法捕捉有意义的模式，并利用孤立森林算法识别异常响应，无需依赖阈值校准或模型微调。实验结果显示，该方法在多种模型和数据集上始终表现出顶级性能，准确率排名第一或第二。

---

## #314 — QGuard:Question-based Zero-shot Guard for Multi-modal LLM Safety

`C` Score: 5.14 | 2025-06-14

**Authors:** Taegyeong Lee, Jeonghwa Yoo, Hyoungseo Cho, Soo Yong Kim, Yunho Maeng

**Categories:** cs.CR, cs.AI

**Scores:** Citation: 5.34 | Influential: 7.81 | Venue: 2.00 | Author: 1.86 | Recency: 7.00

**Links:** [arXiv](https://arxiv.org/abs/2506.12299) | [PDF](https://arxiv.org/pdf/2506.12299)

> 本文提出了QGuard，一种基于问题提示的零样本安全防御方法，用于拦截有害提示。该方法通过生成多样化的防护问题，无需微调即可防御文本和多模态攻击，并保持对最新有害提示的鲁棒性。实验结果表明，QGuard在纯文本和多模态有害数据集上表现具有竞争力，并为LLM服务提供了缓解安全风险的见解。

---

## #315 — GRAID: Synthetic Data Generation with Geometric Constraints and Multi-Agentic Reflection for Harmful Content Detection

`C` Score: 5.14 | 2025-08-23

**Authors:** Melissa Kazemi Rad, Alberto Purpura, Himanshu Kumar, Emily Chen, Mohammad Shahed Sorower

**Categories:** cs.CL, cs.CR, cs.LG

**Scores:** Citation: 3.32 | Influential: 7.81 | Venue: 10.00 | Author: 2.55 | Recency: 7.00

**Links:** [arXiv](https://arxiv.org/abs/2508.17057) | [PDF](https://arxiv.org/pdf/2508.17057)

> 本文提出了GRAID，一种利用大语言模型进行有害文本分类数据增强的新颖管道。该方法结合了几何约束示例生成和多智能体反思过程，确保了对输入空间的可靠覆盖和对有害内容的细致探索。实验表明，使用GRAID增强数据集能显著提升下游护栏模型的性能。

---

## #316 — Sparse Autoencoders are Capable LLM Jailbreak Mitigators

`C` Score: 5.14 | 2026-02-12

**Authors:** Yannick Assogba, Jacopo Cortellazzi, Javier Abad, Pau Rodriguez, Xavier Suau, Arno Blaas

**Categories:** cs.CR, cs.CL, cs.LG

**Scores:** Citation: 3.32 | Influential: 7.81 | Venue: 2.00 | Author: 5.88 | Recency: 10.00

**Links:** [arXiv](https://arxiv.org/abs/2602.12418) | [PDF](https://arxiv.org/pdf/2602.12418)

> 本文提出了基于SAE的越狱防御方法CC-Delta，通过比较有无越狱上下文的相同有害请求的token级表示来识别越狱相关特征。该方法利用统计测试选择特征，并在SAE潜在空间中应用推理时均值偏移转向。实验表明，CC-Delta在安全性与实用性权衡上优于密集潜在空间中的基线防御，特别是在分布外攻击上表现出色，证明了SAE特征空间在越狱缓解中的优势。

---

## #317 — Efficient and Adaptable Detection of Malicious LLM Prompts via Bootstrap Aggregation

`C` Score: 5.14 | 2026-02-08

**Authors:** Shayan Ali Hassan, Tao Ni, Zafar Ayyub Qazi, Marco Canini

**Categories:** cs.LG, cs.CR

**Scores:** Citation: 3.32 | Influential: 7.81 | Venue: 2.00 | Author: 5.88 | Recency: 10.00

**Links:** [arXiv](https://arxiv.org/abs/2602.08062) | [PDF](https://arxiv.org/pdf/2602.08062)

> 针对现有恶意提示检测方法在性能、效率和适应性之间的权衡问题，本文提出了BAGEL框架，一种模块化、轻量级且可增量更新的检测系统。BAGEL利用集成学习和随机森林路由器，聚合专门针对不同攻击数据集微调的模型，从而在不重新训练整个系统的情况下适应新出现的攻击。实验表明，BAGEL仅使用少量集成成员即可达到0.92的F1分数，在性能和效率上均优于OpenAI审核API和大型LLM裁判。

---

## #318 — MAGIC: A Co-Evolving Attacker-Defender Adversarial Game for Robust LLM Safety

`C` Score: 5.14 | 2026-02-02

**Authors:** Xiaoyu Wen, Zhida He, Han Qi, Ziyu Wan, Zhongtian Ma, Ying Wen et al. (10 total)

**Categories:** cs.AI, cs.CL, cs.LG

**Scores:** Citation: 3.32 | Influential: 7.81 | Venue: 2.00 | Author: 5.88 | Recency: 10.00

**Links:** [arXiv](https://arxiv.org/abs/2602.01539) | [PDF](https://arxiv.org/pdf/2602.01539)

> 本文提出了 MAGIC，一种将 LLM 安全对齐形式化为对抗性不对称游戏的多智能体强化学习框架。攻击者智能体学习生成欺骗性提示，而防御者智能体同时优化策略以拒绝这些输入，从而触发共同进化过程。实验表明，该框架能有效提高防御成功率，且不损害模型的有用性。

---

## #319 — Large Language Models Generate Harmful Content Using a Distinct, Unified Mechanism

`C` Score: 5.14 | 2026-04-10

**Authors:** Hadas Orgad, Boyi Wei, Kaden Zheng, Martin Wattenberg, Peter Henderson, Seraphina Goldfarb-Tarrant et al. (7 total)

**Categories:** cs.CL, cs.AI, cs.LG

**Scores:** Citation: 3.32 | Influential: 7.81 | Venue: 2.00 | Author: 5.88 | Recency: 10.00

**Links:** [arXiv](https://arxiv.org/abs/2604.09544) | [PDF](https://arxiv.org/pdf/2604.09544)

> 该研究发现大型语言模型的有害内容生成依赖于一个紧凑的权重集合，这些权重在不同类型有害行为中具有通用性且与良性能力不同。对齐模型比未对齐模型表现出更大的有害生成权重压缩，表明对齐重塑了有害表示的内部结构，这种压缩解释了'新兴不对齐'现象。研究还发现，LLMs的有害生成能力与其识别和解释此类内容的能力是分离的。

---

## #320 — SelfGrader: Stable Jailbreak Detection for Large Language Models using Token-Level Logits

`C` Score: 5.14 | 2026-04-01

**Authors:** Zikai Zhang, Rui Hu, Olivera Kotevska, Jiahao Xu

**Categories:** cs.CR, cs.AI

**Scores:** Citation: 3.32 | Influential: 7.81 | Venue: 2.00 | Author: 5.88 | Recency: 10.00

**Links:** [arXiv](https://arxiv.org/abs/2604.01473) | [PDF](https://arxiv.org/pdf/2604.01473)

> SelfGrader是一种轻量级越狱检测方法，将检测制定为使用token级logits的数值评分问题。通过在紧凑的数值token集合内评估查询安全性，并引入双视角评分规则，该方法实现了高达22.66%的ASR降低，同时保持显著更低的内存开销和延迟。

---

## #321 — Single LLM Debate, MoLaCE: Mixture of Latent Concept Experts Against Confirmation Bias

`C` Score: 5.13 | 2025-12-29

**Authors:** Hazel Kim, Philip Torr

**Categories:** cs.CL

**Scores:** Citation: 3.32 | Influential: 7.81 | Venue: 2.00 | Author: 6.47 | Recency: 9.00

**Links:** [arXiv](https://arxiv.org/abs/2512.23518) | [PDF](https://arxiv.org/pdf/2512.23518)

> 提出了MoLaCE，一种通过混合潜在概念专家来解决输入确认偏差的轻量级推理框架。该方法使单个LLM在内部模拟辩论效果，有效减少了偏差并提升了鲁棒性，且计算成本较低，同时可集成到多智能体辩论框架中以减少相关错误。

---

## #322 — EASE: Practical and Efficient Safety Alignment for Small Language Models

`C` Score: 5.12 | 2025-11-09

**Authors:** Haonan Shi, Guoli Wang, Tu Ouyang, An Wang

**Categories:** cs.CR, cs.LG

**Scores:** Citation: 3.32 | Influential: 7.81 | Venue: 10.00 | Author: 1.12 | Recency: 9.00

**Links:** [arXiv](https://arxiv.org/abs/2511.06512) | [PDF](https://arxiv.org/pdf/2511.06512)

> 本文提出了EASE，一种针对小语言模型的实用且高效的安全对齐框架。该方法通过识别最优安全推理教师，将安全推理能力蒸馏给小模型，并设计选择性机制，仅对危险的对抗性越狱查询激活安全推理，而对简单恶意查询和一般任务直接响应。这种机制使小模型在保持良性交互计算效率的同时，能够抵御复杂攻击，实验显示其越狱攻击成功率比浅层对齐方法降低了17%。

---

## #323 — Encrypted Prompt: Securing LLM Applications Against Unauthorized Actions

`C` Score: 5.11 | 2025-03-29

**Authors:** Shih-Han Chan

**Categories:** cs.CR, cs.AI

**Scores:** Citation: 6.13 | Influential: 7.81 | Venue: 2.00 | Author: 0.58 | Recency: 5.00

**Links:** [arXiv](https://arxiv.org/abs/2503.23250) | [PDF](https://arxiv.org/pdf/2503.23250)

> 本文提出了一种保护LLM应用免受未授权操作的新方法，通过在每个用户提示后附加一个加密提示来嵌入当前权限。在执行LLM生成的任何操作前，系统会验证这些权限，确保只有权限范围内的操作才能执行。当引入对抗性提示误导LLM时，通过验证加密提示中的权限，可以有效防止未授权操作，从而缓解提示注入攻击等威胁。这种方法提供了比传统检测方法更可靠的安全保障，确保LLM应用在面临恶意输入时仍能保持安全边界。

---

## #324 — CCFC: Core & Core-Full-Core Dual-Track Defense for LLM Jailbreak Protection

`C` Score: 5.10 | 2025-08-19

**Authors:** Jiaming Hu, Haoyu Wang, Debarghya Mukherjee, Ioannis Ch. Paschalidis

**Categories:** cs.CR, cs.AI

**Scores:** Citation: 4.94 | Influential: 9.02 | Venue: 2.00 | Author: 1.12 | Recency: 7.00

**Links:** [arXiv](https://arxiv.org/abs/2508.14128) | [PDF](https://arxiv.org/pdf/2508.14128)

> CCFC提出了一种双轨提示级防御框架，通过隔离查询语义核心，分别利用忽略对抗干扰的核心轨道和破坏结构模式的完整轨道进行评估。该方法在保持良性查询保真度的同时，显著降低了越狱攻击的成功率，优于现有的提示级防御方法。

---

## #325 — Strategy Masking: A Method for Guardrails in Value-based Reinforcement Learning Agents

`C` Score: 5.09 | 2025-01-09

**Authors:** Jonathan Keane, Sam Keyser, Jeremy Kedziora

**Categories:** cs.AI, cs.LG, cs.MA

**Scores:** Citation: 3.42 | Influential: 7.81 | Venue: 10.00 | Author: 3.23 | Recency: 5.00

**Links:** [arXiv](https://arxiv.org/abs/2501.05501) | [PDF](https://arxiv.org/pdf/2501.05501)

> 这篇论文针对基于价值的强化学习智能体中因奖励函数设计不当可能导致的不道德或不可取行为问题，提出了一种名为'策略掩码'(strategy masking)的创新方法。该方法通过显式学习和抑制AI智能体的不良行为，实现了对智能体行为的有效控制，特别是在智能体说谎行为的研究中，展示了在不损害智能体原有功能的前提下，通过训练后抑制特定不良行为的能力。

---

## #326 — Probing Latent Subspaces in LLM for AI Security: Identifying and Manipulating Adversarial States

`C` Score: 5.09 | 2025-03-12

**Authors:** Xin Wei Chia, Swee Liang Wong, Jonathan Pan

**Categories:** cs.LG, cs.AI, cs.CR

**Scores:** Citation: 5.43 | Influential: 7.81 | Venue: 2.00 | Author: 2.55 | Recency: 5.00

**Links:** [arXiv](https://arxiv.org/abs/2503.09066) | [PDF](https://arxiv.org/pdf/2503.09066)

> 研究通过从LLM中提取隐藏激活，调查了安全状态和越狱状态的潜在子空间。受神经科学中吸引子动力学的启发，作者假设LLM激活会进入半稳定状态，这些状态可以被识别和扰动以诱导状态转变。研究推导出一种扰动向量，当应用于安全表示时，会将模型推向越狱状态，为潜在的主动防御铺平道路。

---

## #327 — Analysing Safety Risks in LLMs Fine-Tuned with Pseudo-Malicious Cyber Security Data

`C` Score: 5.09 | 2025-05-15

**Authors:** Adel ElZemity, Budi Arief, Shujun Li

**Categories:** cs.CR, cs.AI

**Scores:** Citation: 4.45 | Influential: 9.02 | Venue: 2.00 | Author: 2.55 | Recency: 7.00

**Links:** [arXiv](https://arxiv.org/abs/2505.09974) | [PDF](https://arxiv.org/pdf/2505.09974)

> 本文验证并扩展了使用伪恶意网络安全数据微调LLMs会显著损害其安全性的发现。研究利用garak红队框架评估了四个开源模型，证实微调导致所有测试模型的安全韧性下降。此外，作者提出了一种新颖的安全对齐方法，通过精心重写指令-响应对以包含明确的安全预防措施，从而缓解这些风险。

---

## #328 — Advancing Embodied Agent Security: From Safety Benchmarks to Input Moderation

`C` Score: 5.08 | 2025-04-22

**Authors:** Ning Wang, Zihan Yan, Weiyang Li, Chuan Ma, He Chen, Tao Xiang

**Categories:** cs.AI

**Scores:** Citation: 4.97 | Influential: 7.81 | Venue: 5.00 | Author: 1.86 | Recency: 5.00

**Links:** [arXiv](https://arxiv.org/abs/2504.15699) | [PDF](https://arxiv.org/pdf/2504.15699)

> 本文针对具身智能体的行为安全问题，提出了一个包含分类定义、数据集构建和模型训练的全新输入审核框架。作者引入了EAsafetyBench基准测试和Pinpoint提示解耦审核方案，利用掩码注意力机制有效隔离功能提示的影响。实验表明，该方法在检测准确率和处理速度上均优于现有技术，为具身智能体的安全部署提供了有效保障。

---

## #329 — Adversarial Threat Vectors and Risk Mitigation for Retrieval-Augmented Generation Systems

`C` Score: 5.08 | 2025-05-30

**Authors:** Chris M. Ward, Josh Harguess

**Categories:** cs.CR, cs.AI

**Scores:** Citation: 5.20 | Influential: 7.81 | Venue: 2.00 | Author: 1.86 | Recency: 7.00

**Links:** [arXiv](https://arxiv.org/abs/2506.00281) | [PDF](https://arxiv.org/pdf/2506.00281)

> 本文探讨了检索增强生成（RAG）系统面临的对抗性攻击向量，包括提示注入、数据投毒和对抗性查询操纵。研究从风险管理角度分析了这些威胁，并提出了包含输入验证、对抗性训练和实时监控在内的优先控制列表，以增强 RAG 系统的安全性。

---

## #330 — Saffron-1: Safety Inference Scaling

`C` Score: 5.07 | 2025-06-06

**Authors:** Ruizhong Qiu, Gaotang Li, Tianxin Wei, Jingrui He, Hanghang Tong

**Categories:** cs.LG, cs.AI, cs.CR

**Scores:** Citation: 3.32 | Influential: 7.81 | Venue: 2.00 | Author: 7.43 | Recency: 7.00

**Links:** [arXiv](https://arxiv.org/abs/2506.06444) | [PDF](https://arxiv.org/pdf/2506.06444)

> 本文首次将推理扩展技术应用于大模型安全保证，发现传统推理扩展在安全场景下效果不佳。为此，作者提出了SAFFRON范式，通过引入多分叉奖励模型和保守探索约束，有效解决了探索-效率困境。该方法在不牺牲安全性的前提下，显著提升了推理阶段的安全防御能力。

---

## #331 — SLIP: Soft Label Mechanism and Key-Extraction-Guided CoT-based Defense Against Instruction Backdoor in APIs

`C` Score: 5.07 | 2025-08-08

**Authors:** Zhengxian Wu, Juan Wen, Wanli Peng, Haowei Chang, Yinghan Zhou, Yiming Xue

**Categories:** cs.CR

**Scores:** Citation: 3.32 | Influential: 7.81 | Venue: 2.00 | Author: 7.43 | Recency: 7.00

**Links:** [arXiv](https://arxiv.org/abs/2508.06153) | [PDF](https://arxiv.org/pdf/2508.06153)

> 本文针对定制化LLM代理面临的黑盒指令后门威胁，提出了SLIP防御方法，包含软标签机制和关键提取引导的思维链。该方法通过对抗认知覆盖和异常语义关联，显式引导模型提取任务相关关键词，并利用统计聚类过滤异常短语，实验表明SLIP显著降低了平均攻击成功率，有效防御了指令后门攻击。

---

## #332 — LeakSealer: A Semisupervised Defense for LLMs Against Prompt Injection and Leakage Attacks

`C` Score: 5.07 | 2025-08-01

**Authors:** Francesco Panebianco, Stefano Bonfanti, Francesco Trovò, Michele Carminati

**Categories:** cs.CR, cs.AI, cs.LG

**Scores:** Citation: 3.32 | Influential: 7.81 | Venue: 2.00 | Author: 7.43 | Recency: 7.00

**Links:** [arXiv](https://arxiv.org/abs/2508.00602) | [PDF](https://arxiv.org/pdf/2508.00602)

> 本文提出了 LeakSealer，一个结合静态取证分析与动态人机回环防御的半监督框架，用于抵御提示注入和数据泄露攻击。该方法通过分析历史交互数据生成使用图谱，识别异常模式，在 ToxicChat 数据集上实现了最高的精确率和召回率，并在 PII 泄露检测中取得了优异性能，有效保障了系统安全。

---

## #333 — EnsembleSHAP: Faithful and Certifiably Robust Attribution for Random Subspace Method

`C` Score: 5.06 | 2026-03-31

**Authors:** Yanting Wang, Jinyuan Jia

**Categories:** cs.CR

**Scores:** Citation: 3.32 | Influential: 7.81 | Venue: 2.00 | Author: 5.40 | Recency: 10.00

**Links:** [arXiv](https://arxiv.org/abs/2603.30034) | [PDF](https://arxiv.org/pdf/2603.30034)

> 本文提出了 EnsembleSHAP，一种针对随机子空间方法的忠实且可证明鲁棒的特征归因方法。该方法重用计算副产品，在保持计算效率和局部准确性的同时，提供了针对隐私保护攻击的保证保护。评估表明，该方法在面对后门、对抗和越狱攻击时表现出色。

---

## #334 — Evolving Contextual Safety in Multi-Modal Large Language Models via Inference-Time Self-Reflective Memory

`C` Score: 5.06 | 2026-03-16

**Authors:** Ce Zhang, Jinxi He, Junyi He, Katia Sycara, Yaqi Xie

**Categories:** cs.CV, cs.CL, cs.CR

**Scores:** Citation: 3.32 | Influential: 7.81 | Venue: 2.00 | Author: 5.40 | Recency: 10.00

**Links:** [arXiv](https://arxiv.org/abs/2603.15800) | [PDF](https://arxiv.org/pdf/2603.15800)

> 本文提出了MM-SafetyBench++基准和EchoSafe框架，旨在解决多模态大语言模型中的上下文安全问题。EchoSafe通过维护自反思记忆库，在推理时整合过往安全经验，实现上下文感知推理和安全行为的持续演化。实验表明，该方法在多种多模态安全基准上表现优异，为提升MLLM的上下文安全性建立了强有力的基线。

---

## #335 — TrajGuard: Streaming Hidden-state Trajectory Detection for Decoding-time Jailbreak Defense

`C` Score: 5.06 | 2026-04-09

**Authors:** Cheng Liu, Xiaolei Liu, Xingyu Li, Bangzhou Xin, Kangyi Ding

**Categories:** cs.CR, cs.AI

**Scores:** Citation: 3.32 | Influential: 7.81 | Venue: 2.00 | Author: 5.40 | Recency: 10.00

**Links:** [arXiv](https://arxiv.org/abs/2604.07727) | [PDF](https://arxiv.org/pdf/2604.07727)

> 该研究提出了TrajGuard，一种训练免费的解码时防御框架。实证表明解码阶段关键层的隐藏状态比输入越狱提示携带更强更稳定的风险信号。TrajGuard通过滑动窗口聚合隐藏状态轨迹实时量化风险，仅在风险持续超过阈值时触发轻量级语义裁决。在12种越狱攻击和各种开源LLMs上的实验表明，TrajGuard实现了95%的平均防御率，检测延迟降至5.2 ms/token，假阳性率低于1.5%。

---

## #336 — From Refusal to Recovery: A Control-Theoretic Approach to Generative AI Guardrails

`C` Score: 5.05 | 2025-10-15

**Authors:** Ravi Pandya, Madison Bland, Duy P. Nguyen, Changliu Liu, Jaime Fernández Fisac, Andrea Bajcsy

**Categories:** cs.AI

**Scores:** Citation: 4.32 | Influential: 7.81 | Venue: 2.00 | Author: 4.27 | Recency: 7.00

**Links:** [arXiv](https://arxiv.org/abs/2510.13727) | [PDF](https://arxiv.org/pdf/2510.13727)

> 本文提出了一种基于控制理论的生成式AI护栏方法，将Agent安全视为序列决策问题。该方法在潜在空间中构建预测性护栏，实时监控并主动纠正风险输出，而非简单拒绝，从而在模拟驾驶和电商场景中有效预防下游危害，提升了系统的主动安全性。

---

## #337 — Self-Guided Defense: Adaptive Safety Alignment for Reasoning Models via Synthesized Guidelines

`C` Score: 5.04 | 2025-11-26

**Authors:** Yuhang Wang, Yanxu Zhu, Dongyuan Lu, Jitao Sang

**Categories:** cs.CL, cs.AI

**Scores:** Citation: 3.32 | Influential: 7.81 | Venue: 2.00 | Author: 5.88 | Recency: 9.00

**Links:** [arXiv](https://arxiv.org/abs/2511.21214) | [PDF](https://arxiv.org/pdf/2511.21214)

> 本文提出了 SGASA 框架，通过内化模型生成的安全指南，实现了推理模型的自适应安全对齐，以增强其对对抗性越狱提示的鲁棒性。该框架包含数据预合成和对齐微调两个阶段，在多个数据集上的实验表明，SGASA 能显著提升模型安全性并减少对良性请求的不必要拒绝。

---

## #338 — Semantics as a Shield: Label Disguise Defense (LDD) against Prompt Injection in LLM Sentiment Classification

`C` Score: 5.04 | 2025-11-23

**Authors:** Yanxi Li, Ruocheng Shan

**Categories:** cs.CL, cs.AI

**Scores:** Citation: 3.32 | Influential: 7.81 | Venue: 2.00 | Author: 5.88 | Recency: 9.00

**Links:** [arXiv](https://arxiv.org/abs/2511.21752) | [PDF](https://arxiv.org/pdf/2511.21752)

> 本文针对大语言模型在情感分类任务中面临的提示注入攻击，提出了一种名为标签伪装防御（LDD）的轻量级且模型无关的防御策略。LDD的核心创新在于通过将真实标签替换为语义转换或无关的别名标签，并利用少样本演示让模型隐式学习新的标签映射，从而有效切断了注入指令与决策输出之间的直接对应关系。实验表明，该方法无需模型重新训练即可在多个先进模型上有效防御此类攻击。

---

## #339 — JPU: Bridging Jailbreak Defense and Unlearning via On-Policy Path Rectification

`C` Score: 5.04 | 2026-01-06

**Authors:** Xi Wang, Songlei Jian, Shasha Li, Xiaopeng Li, Zhaoye Li, Bin Ji et al. (8 total)

**Categories:** cs.CR, cs.AI

**Scores:** Citation: 3.32 | Influential: 7.81 | Venue: 2.00 | Author: 5.88 | Recency: 9.00

**Links:** [arXiv](https://arxiv.org/abs/2601.03005) | [PDF](https://arxiv.org/pdf/2601.03005)

> 本文提出了JPU方法，通过动态挖掘策略性对抗样本来暴露漏洞并识别越狱路径，从而将动态越狱路径修正为安全锚点。该方法解决了现有遗忘防御无法修正中间层未擦除参数的问题，显著增强了模型对动态攻击的抵抗力，同时保持了模型的效用。

---

## #340 — An Empirical Study of Collective Behaviors and Social Dynamics in Large Language Model Agents

`C` Score: 5.04 | 2026-02-03

**Authors:** Farnoosh Hashemi, Michael W. Macy

**Categories:** cs.SI, cs.AI

**Scores:** Citation: 3.32 | Influential: 7.81 | Venue: 5.00 | Author: 3.23 | Recency: 10.00

**Links:** [arXiv](https://arxiv.org/abs/2602.03775) | [PDF](https://arxiv.org/pdf/2602.03775)

> 本文通过对LLM驱动的社交平台Chirper.ai上一年内的700万条帖子进行分析，实证研究了LLM智能体的集体行为与社会动态，包括同质性、社会影响、有毒语言特征及意识形态极化。研究发现LLM社交网络表现出与人类相似的基本现象，但在有毒发布模式上存在差异。为此，作者提出了“社会思维链”方法，有效提醒LLM智能体避免发布有害内容。

---

## #341 — AdversariaL attacK sAfety aLIgnment(ALKALI): Safeguarding LLMs through GRACE: Geometric Representation-Aware Contrastive Enhancement- Introducing Adversarial Vulnerability Quality Index (AVQI)

`C` Score: 5.03 | 2025-06-10

**Authors:** Danush Khanna, Gurucharan Marthi Krishna Kumar, Basab Ghosh, Yaswanth Narsupalli, Vinija Jain, Vasu Sharma et al. (8 total)

**Categories:** cs.CL, cs.LG

**Scores:** Citation: 3.32 | Influential: 7.81 | Venue: 2.00 | Author: 7.15 | Recency: 7.00

**Links:** [arXiv](https://arxiv.org/abs/2506.08885) | [PDF](https://arxiv.org/pdf/2506.08885)

> 论文揭示了LLM对齐中的“潜在伪装”盲点，并提出了包含9000个提示的对抗基准ALKALI。作者开发了GRACE框架，通过几何表示感知对比增强来强制安全与对抗表示的分离，在不修改基础模型的情况下将攻击成功率降低了39%。

---

## #342 — ORCA: Agentic Reasoning For Hallucination and Adversarial Robustness in Vision-Language Models

`C` Score: 5.03 | 2025-09-18

**Authors:** Chung-En Johnny Yu, Hsuan-Chih, Chen, Brian Jalaian, Nathaniel D. Bastian

**Categories:** cs.CV, cs.AI, cs.MA

**Scores:** Citation: 3.32 | Influential: 7.81 | Venue: 2.00 | Author: 7.15 | Recency: 7.00

**Links:** [arXiv](https://arxiv.org/abs/2509.15435) | [PDF](https://arxiv.org/pdf/2509.15435)

> ORCA是一个代理推理框架，通过测试时的结构化推理和一组小型视觉模型，提高了预训练视觉语言模型的事实准确性和对抗鲁棒性。它通过观察-推理-批判-行动循环查询视觉工具并验证不一致性，无需访问模型内部或重新训练即可缓解幻觉并增强防御。

---

## #343 — Beyond Surface-Level Detection: Towards Cognitive-Driven Defense Against Jailbreak Attacks via Meta-Operations Reasoning

`C` Score: 5.02 | 2025-08-05

**Authors:** Rui Pu, Chaozhuo Li, Rui Ha, Litian Zhang, Lirong Qiu, Xi Zhang

**Categories:** cs.AI

**Scores:** Citation: 3.88 | Influential: 7.81 | Venue: 2.00 | Author: 5.40 | Recency: 7.00

**Links:** [arXiv](https://arxiv.org/abs/2508.03054) | [PDF](https://arxiv.org/pdf/2508.03054)

> 本文提出了认知驱动防御（CDD）框架，通过应用元操作推理来针对越狱提示的潜在结构进行防御。该框架模拟人类认知推理，利用熵引导的强化学习算法增强对未知威胁的泛化能力，实现了最先进的防御性能。

---

## #344 — The Forgotten Shield: Safety Grafting in Parameter-Space for Medical MLLMs

`C` Score: 5.02 | 2025-12-05

**Authors:** Jiale Zhao, Xing Mou, Jinlin Wu, Hongyuan Yu, Mingrui Sun, Yang Shi et al. (10 total)

**Categories:** cs.LG, cs.AI, cs.CL

**Scores:** Citation: 3.32 | Influential: 7.81 | Venue: 5.00 | Author: 3.78 | Recency: 9.00

**Links:** [arXiv](https://arxiv.org/abs/2601.04199) | [PDF](https://arxiv.org/pdf/2601.04199)

> 论文针对医学多模态大模型建立了多维评估框架，揭示了其在跨模态越狱攻击下的脆弱性及微调过程中的灾难性遗忘。为此，作者提出了参数空间干预方法，通过注入基础模型的安全知识来高效重对齐模型安全性，实现了安全与性能的平衡。

---

## #345 — DiPT: Enhancing LLM reasoning through diversified perspective-taking

`C` Score: 5.02 | 2024-09-10

**Authors:** Hoang Anh Just, Mahavir Dabas, Lifu Huang, Ming Jin, Ruoxi Jia

**Categories:** cs.LG, cs.AI

**Scores:** Citation: 4.20 | Influential: 7.81 | Venue: 5.00 | Author: 3.78 | Recency: 5.00

**Links:** [arXiv](https://arxiv.org/abs/2409.06241) | [PDF](https://arxiv.org/pdf/2409.06241)

> 本文受社会学视角启发，提出了DiPT方法，通过明确整合多样化视角来增强语言模型的推理能力。该方法不仅能提升模型在推理阶段的性能和稳定性，还能通过增强对上下文的理解，有效抵御旨在绕过安全防护的“越狱”提示。此外，利用丰富视角的数据进行微调可进一步提升模型能力。

---

## #346 — Gradual Vigilance and Interval Communication: Enhancing Value Alignment in Multi-Agent Debates

`C` Score: 5.02 | 2024-12-18

**Authors:** Rui Zou, Mengqi Wei, Jintian Feng, Qian Wan, Jianwen Sun, Sannyuya Liu

**Categories:** cs.AI, cs.CL

**Scores:** Citation: 3.97 | Influential: 7.81 | Venue: 2.00 | Author: 6.47 | Recency: 5.00

**Links:** [arXiv](https://arxiv.org/abs/2412.13471) | [PDF](https://arxiv.org/pdf/2412.13471)

> 本文提出了 GVIC 框架，通过多智能体辩论（MAD）机制增强大语言模型的价值对齐。该框架允许智能体以不同级别的警惕性评估风险，并通过间隔通信交换信息，从而在优化辩论效率的同时降低通信开销。实验证明，GVIC 在减轻有害性和防止欺诈方面持续优于基线方法，且对不同规模的模型和任务类型具有强大的适应性。

---

## #347 — Latent-space adversarial training with post-aware calibration for defending large language models against jailbreak attacks

`C` Score: 5.01 | 2025-01-18

**Authors:** Xin Yi, Yue Li, Dongsheng Shi, Linlin Wang, Xiaoling Wang, Liang He

**Categories:** cs.CR, cs.CL

**Scores:** Citation: 4.02 | Influential: 7.81 | Venue: 5.00 | Author: 4.27 | Recency: 5.00

**Links:** [arXiv](https://arxiv.org/abs/2501.10639) | [PDF](https://arxiv.org/pdf/2501.10639)

> 本文提出LATPC框架，通过潜在空间对抗训练与后感知校准技术防御大语言模型免受越狱攻击。该方法通过对比有害和良性输入动态识别安全关键潜在维度，构建有针对性的拒绝特征移除攻击，有效解决了传统对抗训练中过度防御的问题，在保持模型实用性的同时增强了安全性。

---

## #348 — How Jailbreak Defenses Work and Ensemble? A Mechanistic Investigation

`C` Score: 5.00 | 2025-02-20

**Authors:** Zhuohang Long, Siyuan Wang, Shujun Liu, Yuhang Lai, Xuanjing Huang, Zhongyu Wei

**Categories:** cs.CR, cs.AI, cs.CL

**Scores:** Citation: 3.32 | Influential: 7.81 | Venue: 2.00 | Author: 8.33 | Recency: 5.00

**Links:** [arXiv](https://arxiv.org/abs/2502.14486) | [PDF](https://arxiv.org/pdf/2502.14486)

> 本文通过将标准生成任务重新构建为二元分类问题，系统性地检查了越狱防御，以评估模型对有害和良性查询的拒绝倾向。作者确定了两种关键的防御机制：安全转移，增加对所有查询的拒绝率；和有害性区分，提高模型区分有害和良性输入的能力。基于这些机制，作者开发了两种集成防御策略：跨机制集成和内机制集成，以平衡安全性和有用性。实验表明，这些策略有效提高了模型安全性或优化了安全性与有用性之间的权衡。

---

## #349 — SafeLLM: Unlearning Harmful Outputs from Large Language Models against Jailbreak Attacks

`C` Score: 4.98 | 2025-08-21

**Authors:** Xiangman Li, Xiaodong Wu, Qi Li, Jianbing Ni, Rongxing Lu

**Categories:** cs.LG

**Scores:** Citation: 4.97 | Influential: 7.81 | Venue: 2.00 | Author: 1.86 | Recency: 7.00

**Links:** [arXiv](https://arxiv.org/abs/2508.15182) | [PDF](https://arxiv.org/pdf/2508.15182)

> SafeLLM提出了一种基于遗忘的防御框架，通过动态检测不安全输出和追踪前馈网络中的有害内容，从大语言模型中移除有害知识。该方法在显著降低越狱攻击成功率的同时，保持了模型的语言流畅性和通用性能，优于传统的微调方法。

---

## #350 — Towards Robust Multimodal Large Language Models Against Jailbreak Attacks

`C` Score: 4.97 | 2025-02-02

**Authors:** Ziyi Yin, Yuanpu Cao, Han Liu, Ting Wang, Jinghui Chen, Fenhlong Ma

**Categories:** cs.CR

**Scores:** Citation: 4.05 | Influential: 7.81 | Venue: 2.00 | Author: 5.88 | Recency: 5.00

**Links:** [arXiv](https://arxiv.org/abs/2502.00653) | [PDF](https://arxiv.org/pdf/2502.00653)

> 本文针对多模态大语言模型易受越狱攻击的问题，提出了SafeMLLM防御框架。该框架采用对抗训练方法，通过交替进行对比嵌入攻击生成对抗噪声和模型参数更新，有效提升了模型面对复杂对抗扰动时的鲁棒性，解决了现有防御机制在白盒场景下效果不佳的问题。

---

## #351 — Contrastive Reasoning Alignment: Reinforcement Learning from Hidden Representations

`C` Score: 4.97 | 2026-03-18

**Authors:** Haozheng Luo, Yimin Wang, Jiahao Yu, Binghui Wang, Yan Chen

**Categories:** cs.AI, cs.CL, cs.LG

**Scores:** Citation: 3.32 | Influential: 7.81 | Venue: 2.00 | Author: 4.79 | Recency: 10.00

**Links:** [arXiv](https://arxiv.org/abs/2603.17305) | [PDF](https://arxiv.org/pdf/2603.17305)

> 本文提出了CRAFT框架，利用模型推理能力和隐藏表征来提升大模型对越狱攻击的鲁棒性。该方法结合对比表征学习与强化学习，在隐藏状态空间中显式优化目标，分离安全与不安全的推理轨迹。实验显示，CRAFT在推理安全和最终响应安全性上均优于现有防御技术，显著提升了模型的安全性。

---

## #352 — Modal Logical Neural Networks for Financial AI

`C` Score: 4.97 | 2026-03-12

**Authors:** Antonin Sulc

**Categories:** cs.LG

**Scores:** Citation: 3.32 | Influential: 7.81 | Venue: 2.00 | Author: 4.79 | Recency: 10.00

**Links:** [arXiv](https://arxiv.org/abs/2603.12487) | [PDF](https://arxiv.org/pdf/2603.12487)

> 本文提出模态逻辑神经网络（MLNN），将克里普克语义集成到神经架构中，实现关于必然性、可能性和知识的可微推理。通过将核心组件映射到监管护栏和市场压力测试，展示了MLNN作为金融领域可微“逻辑层”在促进合规和鲁棒性方面的应用。

---

## #353 — Beyond Input Guardrails: Reconstructing Cross-Agent Semantic Flows for Execution-Aware Attack Detection

`C` Score: 4.97 | 2026-03-04

**Authors:** Yangyang Wei, Yijie Xu, Zhenyuan Li, Xiangmin Shen, Shouling Ji

**Categories:** cs.CR, cs.MA

**Scores:** Citation: 3.32 | Influential: 7.81 | Venue: 2.00 | Author: 4.79 | Recency: 10.00

**Links:** [arXiv](https://arxiv.org/abs/2603.04469) | [PDF](https://arxiv.org/pdf/2603.04469)

> 本文提出了一个通过重构跨Agent语义流进行执行感知攻击检测的框架，旨在解决多Agent系统中间接提示注入等绕过输入护栏的风险。该框架将碎片化的操作原语合成为连续的行为轨迹，利用监督者LLM识别数据流违规和控制流偏差，有效检测了多种复合攻击。

---

## #354 — Silencing the Guardrails: Inference-Time Jailbreaking via Dynamic Contextual Representation Ablation

`C` Score: 4.97 | 2026-04-09

**Authors:** Wenpeng Xing, Moran Fang, Guangtai Wang, Changting Lin, Meng Han

**Categories:** cs.AI

**Scores:** Citation: 3.32 | Influential: 7.81 | Venue: 2.00 | Author: 4.79 | Recency: 10.00

**Links:** [arXiv](https://arxiv.org/abs/2604.07835) | [PDF](https://arxiv.org/pdf/2604.07835)

> 该研究提出了上下文表示消融(CRA)，一种新的推理时干预框架，旨在动态静默模型护栏。基于拒绝行为由模型隐藏状态中特定低秩子空间介导的见解，CRA在解码过程中识别并抑制这些拒绝诱导的激活模式，无需昂贵的参数更新或训练。在多个安全对齐的开源LLMs上的评估表明，CRA显著优于基线，暴露了当前对齐机制的内在脆弱性。

---

## #355 — Leveraging the Potential of Prompt Engineering for Hate Speech Detection in Low-Resource Languages

`C` Score: 4.96 | 2025-06-30

**Authors:** Ruhina Tabasshum Prome, Tarikul Islam Tamiti, Anomadarshi Barua

**Categories:** cs.CL, cs.AI

**Scores:** Citation: 3.75 | Influential: 7.81 | Venue: 2.00 | Author: 5.40 | Recency: 7.00

**Links:** [arXiv](https://arxiv.org/abs/2506.23930) | [PDF](https://arxiv.org/pdf/2506.23930)

> 本文探讨了利用大语言模型的提示工程技术来解决低资源语言（孟加拉语）中的仇恨言论检测问题。研究提出了创新的隐喻提示策略，并对比了六种提示方法与传统深度学习模型的表现，证明了提示工程在低资源场景下的有效性。

---

## #356 — Curriculum-Guided Antifragile Reinforcement Learning for Secure UAV Deconfliction under Observation-Space Attacks

`C` Score: 4.96 | 2025-06-26

**Authors:** Deepak Kumar Panda, Adolfo Perrusquia, Weisi Guo

**Categories:** cs.LG, cs.AI

**Scores:** Citation: 3.75 | Influential: 7.81 | Venue: 2.00 | Author: 5.40 | Recency: 7.00

**Links:** [arXiv](https://arxiv.org/abs/2506.21129) | [PDF](https://arxiv.org/pdf/2506.21129)

> 本文提出了一种课程引导的反脆弱强化学习框架，用于在观测空间攻击下保护无人机避撞策略。该框架通过模拟攻击者逐步增加扰动强度，使智能体适应分布外观测，并在动态3D障碍场景中证明了其优于传统策略的鲁棒性。

---

## #357 — CorrSteer: Generation-Time LLM Steering via Correlated Sparse Autoencoder Features

`C` Score: 4.96 | 2025-08-18

**Authors:** Seonglae Cho, Zekun Wu, Adriano Koshiyama

**Categories:** cs.CL, cs.AI, cs.LG

**Scores:** Citation: 3.96 | Influential: 7.81 | Venue: 2.00 | Author: 4.79 | Recency: 7.00

**Links:** [arXiv](https://arxiv.org/abs/2508.12535) | [PDF](https://arxiv.org/pdf/2508.12535)

> CorrSteer提出了一种通过关联稀疏自编码器特征在生成时引导大语言模型的方法。该方法仅利用推理时的激活值选择相关特征，自动化引导流程，在问答、偏见缓解和越狱防御等任务上显著提升了模型性能。

---

## #358 — SAID: Empowering Large Language Models with Self-Activating Internal Defense

`C` Score: 4.96 | 2025-10-23

**Authors:** Yulong Chen, Yadong Liu, Jiawen Zhang, Mu Li, Chao Huang, Jie Wen

**Categories:** cs.CR, cs.AI

**Scores:** Citation: 3.32 | Influential: 7.81 | Venue: 2.00 | Author: 5.40 | Recency: 9.00

**Links:** [arXiv](https://arxiv.org/abs/2510.20129) | [PDF](https://arxiv.org/pdf/2510.20129)

> 本文提出了SAID，一种无需训练的内部防御范式，通过激活大语言模型内在的安全机制来有效防御越狱攻击。该方法利用模型自身的推理能力，通过意图蒸馏、安全前缀探测和保守聚合三阶段流程主动识别并中和恶意意图，在保持模型效用且开销极低的情况下显著降低了有害输出。

---

## #359 — Response-Based Knowledge Distillation for Multilingual Jailbreak Prevention Unwittingly Compromises Safety

`C` Score: 4.96 | 2025-12-08

**Authors:** Max Zhang, Derek Liu, Kai Zhang, Joshua Franco, Haihao Liu

**Categories:** cs.CL

**Scores:** Citation: 3.32 | Influential: 7.81 | Venue: 2.00 | Author: 5.40 | Recency: 9.00

**Links:** [arXiv](https://arxiv.org/abs/2602.11157) | [PDF](https://arxiv.org/pdf/2602.11157)

> 论文探索了基于响应的知识蒸馏在多语言越狱防御中的应用，发现使用教师模型的安全拒绝数据微调反而会降低学生模型的安全性。研究揭示了这种反直觉现象的原因，并提出了通过移除细微的“边界”拒绝来缓解安全下降的策略，为多语言对齐提供了新见解。

---

## #360 — From static to adaptive: immune memory-based jailbreak detection for large language models

`C` Score: 4.96 | 2025-12-03

**Authors:** Jun Leng, Yu Liu, Litian Zhang, Ruihan Hu, Zhuting Fang, Xi Zhang

**Categories:** cs.CR

**Scores:** Citation: 3.32 | Influential: 7.81 | Venue: 2.00 | Author: 5.40 | Recency: 9.00

**Links:** [arXiv](https://arxiv.org/abs/2512.03356) | [PDF](https://arxiv.org/pdf/2512.03356)

> 本文提出了基于免疫记忆的自适应卫士（IMAG）框架，通过将安全模式提炼并编码到持久可进化的记忆库中，实现了对新兴越狱攻击的自适应防御。该框架包含免疫检测、主动免疫和记忆更新三个协同组件，将LLM防御从刚性过滤转变为自主自适应缓解，在多个开源模型上超越了现有最先进方法。

---

## #361 — HoneyTrap: Deceiving Large Language Model Attackers to Honeypot Traps with Resilient Multi-Agent Defense

`C` Score: 4.96 | 2026-01-07

**Authors:** Siyuan Li, Xi Lin, Jun Wu, Zehao Liu, Haoyu Li, Tianjie Ju et al. (8 total)

**Categories:** cs.CR, cs.AI

**Scores:** Citation: 3.32 | Influential: 7.81 | Venue: 2.00 | Author: 5.40 | Recency: 9.00

**Links:** [arXiv](https://arxiv.org/abs/2601.04034) | [PDF](https://arxiv.org/pdf/2601.04034)

> 本文提出了HoneyTrap，一种利用协作防御者对抗越狱攻击的新型欺骗性防御框架。该框架集成了四个专门的防御智能体，并通过引入新的评估指标，在多轮渐进式越狱攻击中显著降低了攻击成功率，即使在自适应攻击者设置下也能保持韧性。

---

## #362 — Hydra: An Agentic Reasoning Approach for Enhancing Adversarial Robustness and Mitigating Hallucinations in Vision-Language Models

`C` Score: 4.94 | 2025-04-19

**Authors:** Chung-En, Yu, Hsuan-Chih, Chen, Brian Jalaian, Nathaniel D. Bastian

**Categories:** cs.CV, cs.AI, cs.MA

**Scores:** Citation: 3.56 | Influential: 7.81 | Venue: 2.00 | Author: 7.15 | Recency: 5.00

**Links:** [arXiv](https://arxiv.org/abs/2504.14395) | [PDF](https://arxiv.org/pdf/2504.14395)

> 本文提出了Hydra，一个自适应的智能体推理框架，用于增强视觉语言模型的对抗鲁棒性并缓解幻觉。该框架通过行动-批判循环、结构化批判和跨模型验证，利用思维链和上下文学习动态细化输出。实验证明，Hydra在对抗扰动和内在模型错误方面均表现出色，优于现有的去幻觉方法。

---

## #363 — Retrieval-Augmented Defense: Adaptive and Controllable Jailbreak Prevention for Large Language Models

`C` Score: 4.93 | 2025-08-22

**Authors:** Guangyu Yang, Jinghong Chen, Jingbiao Mei, Weizhe Lin, Bill Byrne

**Categories:** cs.CR, cs.CL

**Scores:** Citation: 3.32 | Influential: 7.81 | Venue: 2.00 | Author: 6.47 | Recency: 7.00

**Links:** [arXiv](https://arxiv.org/abs/2508.16406) | [PDF](https://arxiv.org/pdf/2508.16406)

> 本文提出了检索增强防御（RAD），一种用于越狱检测的新颖框架。该方法将已知攻击示例数据库集成到检索增强生成中，以推断潜在的恶意查询和越狱策略，从而实现无需重新训练的适应性防御。实验表明，RAD能有效降低强越狱攻击的成功率，并在安全性和实用性之间取得平衡。

---

## #364 — Sample-Efficient Distributionally Robust Multi-Agent Reinforcement Learning via Online Interaction

`C` Score: 4.92 | 2025-08-04

**Authors:** Zain Ulabedeen Farhat, Debamita Ghosh, George K. Atia, Yue Wang

**Categories:** cs.LG, cs.MA

**Scores:** Citation: 4.84 | Influential: 7.81 | Venue: 2.00 | Author: 1.86 | Recency: 7.00

**Links:** [arXiv](https://arxiv.org/abs/2508.02948) | [PDF](https://arxiv.org/pdf/2508.02948)

> 本文首次研究了分布鲁棒马尔可夫博弈中的在线学习问题，提出了MORNAVI算法。该算法使智能体能够直接从环境交互中学习，无需先验数据，并在环境不确定性（包括噪声或对抗性攻击）下实现低遗憾并找到最优鲁棒策略。

---

## #365 — Look Before You Leap: Enhancing Attention and Vigilance Regarding Harmful Content with GuidelineLLM

`C` Score: 4.91 | 2024-12-10

**Authors:** Shaoqing Zhang, Zhuosheng Zhang, Kehai Chen, Rongxiang Weng, Muyun Yang, Tiejun Zhao et al. (7 total)

**Categories:** cs.CL, cs.AI

**Scores:** Citation: 3.40 | Influential: 7.81 | Venue: 2.00 | Author: 7.43 | Recency: 5.00

**Links:** [arXiv](https://arxiv.org/abs/2412.10423) | [PDF](https://arxiv.org/pdf/2412.10423)

> 本文提出了GuidelineLLM，一种新型防御范式，通过辅助模型在主模型响应前识别查询风险并生成安全准则建议。该方法无需对主模型进行额外的安全微调，仅通过微调GuidelineLLM即可显著降低攻击成功率，同时保持对良性查询的处理能力，具有广泛的适用性。

---

## #366 — Understanding and Defending VLM Jailbreaks via Jailbreak-Related Representation Shift

`C` Score: 4.90 | 2026-03-18

**Authors:** Zhihua Wei, Qiang Li, Jian Ruan, Zhenxin Qin, Leilei Wen, Dongrui Liu et al. (7 total)

**Categories:** cs.CV, cs.AI

**Scores:** Citation: 3.32 | Influential: 7.81 | Venue: 2.00 | Author: 4.27 | Recency: 10.00

**Links:** [arXiv](https://arxiv.org/abs/2603.17372) | [PDF](https://arxiv.org/pdf/2603.17372)

> 本文研究了视觉-语言模型（VLM）中的越狱现象，发现视觉模态会将模型表征向特定的越狱状态转移，从而绕过文本安全机制。作者定义了越狱相关转移（JRS）并提出了JRS-Rem防御方法，通过在推理时移除该转移成分来增强模型安全性。实验表明，该方法在多种场景下能有效防御越狱攻击，同时保持对良性任务的性能。

---

## #367 — Co-Evolutionary Multi-Modal Alignment via Structured Adversarial Evolution

`C` Score: 4.90 | 2026-03-02

**Authors:** Guoxin Shi, Haoyu Wang, Zaihui Yang, Yuxing Wang, Yongzhe Chang

**Categories:** cs.CR, cs.AI

**Scores:** Citation: 3.32 | Influential: 7.81 | Venue: 2.00 | Author: 4.27 | Recency: 10.00

**Links:** [arXiv](https://arxiv.org/abs/2603.01784) | [PDF](https://arxiv.org/pdf/2603.01784)

> 提出CEMMA框架，通过结构化对抗进化实现多模态大模型的对齐。该框架包含利用遗传算子生成攻击的进化攻击者和迭代更新的自适应防御者，形成闭环过程。实验表明，该方法显著提升了模型在动态攻击环境下的鲁棒性和泛化能力。

---

## #368 — UK AISI Alignment Evaluation Case-Study

`C` Score: 4.90 | 2026-04-01

**Authors:** Alexandra Souly, Robert Kirk, Jacob Merizian, Abby D'Cruz, Xander Davies

**Categories:** cs.AI, cs.CR

**Scores:** Citation: 3.32 | Influential: 7.81 | Venue: 2.00 | Author: 4.27 | Recency: 10.00

**Links:** [arXiv](https://arxiv.org/abs/2604.00788) | [PDF](https://arxiv.org/pdf/2604.00788)

> 英国AI安全学院开发了评估前沿AI系统对齐性的方法，特别关注模型作为编码助手时是否会破坏安全研究。通过对四个前沿模型的测试，研究发现没有确认的研究破坏实例，但Claude Opus 4.5和Sonnet 4.5经常拒绝参与安全相关任务。研究还发现不同模型在评估意识和场景区分能力上存在差异。这项工作基于Petri审计工具开发了自定义评估支架，为AI系统内部部署的安全评估提供了新方法。

---

## #369 — MirrorShield: Towards Universal Defense Against Jailbreaks via Entropy-Guided Mirror Crafting

`C` Score: 4.89 | 2025-03-17

**Authors:** Rui Pu, Chaozhuo Li, Rui Ha, Litian Zhang, Lirong Qiu, Xi Zhang

**Categories:** cs.CR, cs.AI

**Scores:** Citation: 3.50 | Influential: 9.02 | Venue: 2.00 | Author: 5.40 | Recency: 5.00

**Links:** [arXiv](https://arxiv.org/abs/2503.12931) | [PDF](https://arxiv.org/pdf/2503.12931)

> MirrorShield提出一种通用越狱防御模型，引入'镜像'概念——动态生成的提示，反映输入语法结构同时确保语义安全。通过检测输入与镜像之间的差异来识别和校准风险输入。相比十种SOTA攻击方法，该模型在多个基准数据集上展现出优越的防御性能和泛化能力。

---

## #370 — SPIN: Self-Supervised Prompt INjection

`C` Score: 4.89 | 2024-10-17

**Authors:** Leon Zhou, Junfeng Yang, Chengzhi Mao

**Categories:** cs.CL, cs.AI

**Scores:** Citation: 3.36 | Influential: 7.81 | Venue: 2.00 | Author: 7.43 | Recency: 5.00

**Links:** [arXiv](https://arxiv.org/abs/2410.13236) | [PDF](https://arxiv.org/pdf/2410.13236)

> 本文提出了自监督提示注入（SPIN）方法，用于在推理时检测和逆转针对大语言模型的各种对抗及越狱攻击。该方法与现有对齐技术兼容，作为额外的安全层，实验表明其能将攻击成功率降低高达87.9%，同时对良性用户请求保持性能，且对自适应攻击具有韧性，显著提升了模型安全性。

---

## #371 — Model Editing as a Double-Edged Sword: Steering Agent Ethical Behavior Toward Beneficence or Harm

`C` Score: 4.88 | 2025-06-25

**Authors:** Baixiang Huang, Zhen Tan, Haoran Wang, Zijie Liu, Dawei Li, Ali Payani et al. (9 total)

**Categories:** cs.CL

**Scores:** Citation: 3.32 | Influential: 7.81 | Venue: 2.00 | Author: 6.17 | Recency: 7.00

**Links:** [arXiv](https://arxiv.org/abs/2506.20606) | [PDF](https://arxiv.org/pdf/2506.20606)

> 本文将智能体行为引导构建为模型编辑任务，提出了BehaviorBench基准来评估和编辑智能体的道德行为。研究表明，模型编辑不仅能进行特定场景的局部调整，还能实现全局道德对齐的广泛转变，既能促进伦理行为，也可能诱导恶意行为。

---

## #372 — Learning to Detect Unseen Jailbreak Attacks in Large Vision-Language Models

`C` Score: 4.88 | 2025-08-08

**Authors:** Shuang Liang, Zhihao Xu, Jiaqi Weng, Jialing Tao, Hui Xue, Xiting Wang

**Categories:** cs.CR, cs.AI, cs.CV

**Scores:** Citation: 3.32 | Influential: 7.81 | Venue: 2.00 | Author: 6.17 | Recency: 7.00

**Links:** [arXiv](https://arxiv.org/abs/2508.09201) | [PDF](https://arxiv.org/pdf/2508.09201)

> 针对大型视觉语言模型（LVLM）面临的越狱攻击风险，本文提出了LoD框架，该框架无需攻击数据或手工启发式规则，而是利用模型内部激活提取分层安全表示，并通过安全模式自编码器将其转换为异常分数进行检测。实验表明，LoD在多种LVLM上对未见过的越狱攻击始终实现了最先进的检测性能，同时显著提高了效率。

---

## #373 — Zero-Shot Embedding Drift Detection: A Lightweight Defense Against Prompt Injections in LLMs

`C` Score: 4.87 | 2026-01-18

**Authors:** Anirudh Sekar, Mrinal Agarwal, Rachel Sharma, Akitsugu Tanaka, Jasmine Zhang, Arjun Damerla et al. (7 total)

**Categories:** cs.CR, cs.CL

**Scores:** Citation: 3.32 | Influential: 7.81 | Venue: 2.00 | Author: 4.79 | Recency: 9.00

**Links:** [arXiv](https://arxiv.org/abs/2601.12359) | [PDF](https://arxiv.org/pdf/2601.12359)

> ZEDD 提出了一种轻量级的零样本提示注入检测框架，通过量化嵌入空间中的语义漂移来识别直接和间接攻击。该方法无需访问模型内部或特定训练，利用对抗性-良性提示对的余弦相似度，在检测准确率和效率上优于传统方法。

---

## #374 — Toward Safer Diffusion Language Models: Discovery and Mitigation of Priming Vulnerability

`C` Score: 4.86 | 2025-10-01

**Authors:** Shojiro Yamabe, Jun Sakuma

**Categories:** cs.AI, cs.LG

**Scores:** Citation: 4.17 | Influential: 9.02 | Venue: 2.00 | Author: 1.86 | Recency: 7.00

**Links:** [arXiv](https://arxiv.org/abs/2510.00565) | [PDF](https://arxiv.org/pdf/2510.00565)

> 本文揭示了扩散语言模型（DLMs）在迭代去噪过程中存在的关键安全漏洞，即攻击者可通过在中间步骤注入肯定有害查询的token来引导模型生成有害内容，从而绕过现有的安全防护。基于此发现，作者不仅验证了现有优化型越狱攻击在DLMs上的有效性，还提出了一种专门针对DLMs的新型安全对齐方法，旨在训练模型从受污染的中间状态生成安全响应，有效缓解此类启动漏洞带来的风险。

---

## #375 — Evaluating Multi-Agent Defences Against Jailbreaking Attacks on Large Language Models

`C` Score: 4.84 | 2025-06-30

**Authors:** Maria Carolina Cornelia Wit, Jun Pang

**Categories:** cs.AI

**Scores:** Citation: 3.32 | Influential: 7.81 | Venue: 2.00 | Author: 5.88 | Recency: 7.00

**Links:** [arXiv](https://arxiv.org/abs/2506.23576) | [PDF](https://arxiv.org/pdf/2506.23576)

> 本文评估了多智能体系统作为防御大语言模型越狱攻击的有效性。通过对比单智能体与多智能体配置，研究发现多智能体系统能增强抗越狱能力，但也带来了误报增加和计算开销等权衡问题，指出了当前自动防御的局限性。

---

## #376 — SafeBehavior: Simulating Human-Like Multistage Reasoning to Mitigate Jailbreak Attacks in Large Language Models

`C` Score: 4.84 | 2025-09-30

**Authors:** Qinjian Zhao, Jiaqi Wang, Zhiqiang Gao, Zhihao Dou, Belal Abuhaija, Kaizhu Huang

**Categories:** cs.AI

**Scores:** Citation: 3.32 | Influential: 7.81 | Venue: 2.00 | Author: 5.88 | Recency: 7.00

**Links:** [arXiv](https://arxiv.org/abs/2509.26345) | [PDF](https://arxiv.org/pdf/2509.26345)

> 本文提出了 SafeBehavior，一种模拟人类自适应多阶段推理过程的分层越狱防御机制。该方法通过意图推断、自省评估和自我修正三个阶段，有效检测复杂语境中的恶意意图并自适应重写不确定输出，在多种越狱攻击场景下显著提升了模型的鲁棒性和适应性，提供了一种高效且受人类认知启发的安全方案。

---

## #377 — Attacks by Content: Automated Fact-checking is an AI Security Issue

`C` Score: 4.84 | 2025-10-13

**Authors:** Michael Schlichtkrull

**Categories:** cs.CL, cs.AI

**Scores:** Citation: 3.32 | Influential: 7.81 | Venue: 10.00 | Author: 0.58 | Recency: 7.00

**Links:** [arXiv](https://arxiv.org/abs/2510.11238) | [PDF](https://arxiv.org/pdf/2510.11238)

> 本文提出了一种名为“内容攻击”的新型威胁，即攻击者通过提供偏见或虚假信息而非注入指令来操纵Agent行为。现有的防御机制对此无效，作者主张将自动事实核查重新用作Agent的认知自我防御工具，以评估检索信息的可信度。这为Agent在处理外部文档时的安全性提供了新的防御视角。

---

## #378 — Building Effective Safety Guardrails in AI Education Tools

`C` Score: 4.83 | 2025-08-07

**Authors:** Hannah-Beth Clark, Laura Benton, Emma Searle, Margaux Dowland, Matthew Gregory, Will Gayne et al. (7 total)

**Categories:** cs.CY, cs.AI

**Scores:** Citation: 4.88 | Influential: 7.81 | Venue: 2.00 | Author: 1.12 | Recency: 7.00

**Links:** [arXiv](https://arxiv.org/abs/2508.05360) | [PDF](https://arxiv.org/pdf/2508.05360)

> 本文探讨了在教育领域生成式AI工具中构建安全护栏的方法，以Oak National Academy开发的Aila为例。研究实施了提示工程、输入威胁检测、独立异步内容审核代理（IACMA）以及人工在环四种关键安全措施，以缓解AI生成内容的风险。

---

## #379 — LLM-VA: Resolving the Jailbreak-Overrefusal Trade-off via Vector Alignment

`C` Score: 4.82 | 2026-01-27

**Authors:** Haonan Zhang, Dongxia Wang, Yi Liu, Kexin Chen, Wenhai Wang

**Categories:** cs.LG, cs.AI

**Scores:** Citation: 3.32 | Influential: 7.81 | Venue: 2.00 | Author: 3.78 | Recency: 10.00

**Links:** [arXiv](https://arxiv.org/abs/2601.19487) | [PDF](https://arxiv.org/pdf/2601.19487)

> 针对安全对齐大语言模型面临的越狱与过度拒绝权衡难题，本文指出其根本原因在于模型将回答决策与安全判断编码为近乎正交的独立向量。为此，作者提出了LLM-VA方法，通过闭式权重更新将回答向量与安全向量对齐，使模型回答意愿因果依赖于安全评估，且无需微调或改变架构。实验表明，该方法在12个模型上显著优于基线，有效解决了这一安全困境。

---

## #380 — Alignment-Weighted DPO: A principled reasoning approach to improve safety alignment

`C` Score: 4.82 | 2026-02-24

**Authors:** Mengxuan Hu, Vivek V. Datla, Anoop Kumar, Zihan Guan, Sheng Li, Alfy Samuel et al. (7 total)

**Categories:** cs.CL, cs.AI

**Scores:** Citation: 3.32 | Influential: 7.81 | Venue: 2.00 | Author: 3.78 | Recency: 10.00

**Links:** [arXiv](https://arxiv.org/abs/2602.21346) | [PDF](https://arxiv.org/pdf/2602.21346)

> 本文针对现有大模型对齐技术（如SFT、RLHF）在面对伪装性越狱攻击时表现脆弱的问题，通过因果干预分析指出其根源在于缺乏深度推理的浅层对齐机制。为此，作者提出了一种基于推理感知的后训练方法，构建了包含思维链（CoT）的微调数据集，鼓励模型生成基于推理的原则性拒绝。实验表明，该方法能有效提升模型对有害意图的理解与防御能力，优于标准SFT基线。

---

## #381 — SIA: A Synthesize-Inject-Align Framework for Knowledge-Grounded and Secure E-commerce Search LLMs with Industrial Deployment

`C` Score: 4.82 | 2026-03-17

**Authors:** Zhouwei Zhai, Mengxiang Chen, Anmeng Zhang

**Categories:** cs.CL

**Scores:** Citation: 3.32 | Influential: 7.81 | Venue: 2.00 | Author: 3.78 | Recency: 10.00

**Links:** [arXiv](https://arxiv.org/abs/2603.16137) | [PDF](https://arxiv.org/pdf/2603.16137)

> 本文提出了SIA框架，旨在解决电商搜索LLM中的知识幻觉和越狱攻击漏洞，构建安全可靠的工业级系统。该框架通过合成高质量语料库、基于深度上缩放的参数高效预训练以及双路径对齐方法，注入领域知识并增强安全鲁棒性。在京东平台的部署表明，该框架显著提升了核心业务指标，验证了其工业有效性和可扩展性。

---

## #382 — Directional Embedding Smoothing for Robust Vision Language Models

`C` Score: 4.82 | 2026-03-16

**Authors:** Ye Wang, Jing Liu, Toshiaki Koike-Akino

**Categories:** cs.LG, cs.AI, cs.CL

**Scores:** Citation: 3.32 | Influential: 7.81 | Venue: 2.00 | Author: 3.78 | Recency: 10.00

**Links:** [arXiv](https://arxiv.org/abs/2603.15259) | [PDF](https://arxiv.org/pdf/2603.15259)

> 本文将随机嵌入平滑（RESTA）防御机制扩展至视觉语言模型（VLM），以对抗多模态越狱攻击。研究发现，采用与原始词向量对齐的方向性嵌入噪声能有效降低攻击成功率，特别是在多样化的攻击语料库中表现优异。该方法作为一种轻量级的推理时防御层，有助于增强Agent系统中VLM的安全性。

---

## #383 — Defensive Refusal Bias: How Safety Alignment Fails Cyber Defenders

`C` Score: 4.82 | 2026-03-01

**Authors:** David Campbell, Neil Kale, Udari Madhushani Sehwag, Bert Herring, Nick Price, Dan Borges et al. (8 total)

**Categories:** cs.CR, cs.AI

**Scores:** Citation: 3.32 | Influential: 7.81 | Venue: 2.00 | Author: 3.78 | Recency: 10.00

**Links:** [arXiv](https://arxiv.org/abs/2603.01246) | [PDF](https://arxiv.org/pdf/2603.01246)

> 研究了大模型安全对齐中的“防御性拒绝偏差”，即模型因关键词相似性而拒绝合法的防御性网络安全任务。基于真实竞赛数据的分析显示，明确授权反而增加了拒绝率。文章呼吁通过意图分析来缓解该问题，以最大化防御能力。

---

## #384 — Gradient-Controlled Decoding: A Safety Guardrail for LLMs with Dual-Anchor Steering

`C` Score: 4.82 | 2026-04-06

**Authors:** Purva Chiniya, Kevin Scaria, Sagar Chaturvedi

**Categories:** cs.CL

**Scores:** Citation: 3.32 | Influential: 7.81 | Venue: 2.00 | Author: 3.78 | Recency: 10.00

**Links:** [arXiv](https://arxiv.org/abs/2604.05179) | [PDF](https://arxiv.org/pdf/2604.05179)

> 梯度控制解码（GCD）是一种无需训练的LLM安全护栏，结合接受和拒绝锚定令牌收紧决策边界。当提示被标记时，GCD预设注入拒绝令牌保证第一令牌安全性。在多个基准上，GCD相比GradSafe降低52%假阳性，比最强基线降低10%攻击成功率，增加延迟不到15-20毫秒，可转移到多种模型，仅需20个演示模板，有效防止越狱和提示注入攻击。

---

## #385 — ShieldNet: Network-Level Guardrails against Emerging Supply-Chain Injections in Agentic Systems

`C` Score: 4.82 | 2026-04-06

**Authors:** Zhuowen Yuan, Zhaorun Chen, Zhen Xiang, Nathaniel D. Bastian, Seyyed Hadi Hashemi, Chaowei Xiao et al. (8 total)

**Categories:** cs.AI

**Scores:** Citation: 3.32 | Influential: 7.81 | Venue: 2.00 | Author: 3.78 | Recency: 10.00

**Links:** [arXiv](https://arxiv.org/abs/2604.04426) | [PDF](https://arxiv.org/pdf/2604.04426)

> ShieldNet是针对代理系统中新兴供应链注入的网络级护栏框架。SC-Inject-Bench是包含10,000+恶意MCP工具的大规模基准，基于25+种攻击类型。ShieldNet通过观察真实网络交互而非表面级工具痕迹检测供应链污染，集成中间人代理和事件提取器识别关键网络行为，由轻量级分类器处理。实验显示其实现高达0.995 F-1检测性能（仅0.8%假阳性），显著优于现有方法。

---

## #386 — ProTransformer: Robustify Transformers via Plug-and-Play Paradigm

`C` Score: 4.81 | 2024-10-30

**Authors:** Zhichao Hou, Weizhi Gao, Yuchen Shen, Feiyi Wang, Xiaorui Liu

**Categories:** cs.LG, cs.CL, cs.CR

**Scores:** Citation: 4.37 | Influential: 7.81 | Venue: 5.00 | Author: 1.86 | Recency: 5.00

**Links:** [arXiv](https://arxiv.org/abs/2410.23182) | [PDF](https://arxiv.org/pdf/2410.23182)

> 本文提出了一种即插即用的鲁棒注意力机制 ProTransformer，旨在增强 Transformer 架构的防御能力。该技术无需额外训练或微调即可集成到现有模型中，显著提升了模型在文本、视觉和图领域对抗各类攻击的鲁棒性。实验表明，ProTransformer 在 TextFooler 等攻击下显著提升了 BERT、LLaMA 等模型的性能，并在大语言模型中展现出对越狱攻击的强韧性。

---

## #387 — Understanding and Preserving Safety in Fine-Tuned LLMs

`C` Score: 4.80 | 2026-01-15

**Authors:** Jiawen Zhang, Yangfan Hu, Kejia Chen, Lipeng He, Jiachen Ma, Jian Lou et al. (10 total)

**Categories:** cs.LG, cs.AI

**Scores:** Citation: 3.32 | Influential: 7.81 | Venue: 2.00 | Author: 4.27 | Recency: 9.00

**Links:** [arXiv](https://arxiv.org/abs/2601.10141) | [PDF](https://arxiv.org/pdf/2601.10141)

> 本文分析了安全对齐 LLM 中安全与效用梯度的几何相互作用，提出了安全保留微调（SPF）方法。SPF 通过显式去除与低秩安全子空间冲突的梯度分量，在保证任务性能的同时有效防止了安全性下降，解决了微调过程中的安全-效用困境。

---

## #388 — Prompt Inject Detection with Generative Explanation as an Investigative Tool

`C` Score: 4.79 | 2025-02-16

**Authors:** Jonathan Pan, Swee Liang Wong, Yidi Yuan, Xin Wei Chia

**Categories:** cs.CR, cs.AI

**Scores:** Citation: 3.47 | Influential: 7.81 | Venue: 10.00 | Author: 1.12 | Recency: 5.00

**Links:** [arXiv](https://arxiv.org/abs/2502.11006) | [PDF](https://arxiv.org/pdf/2502.11006)

> 该论文探讨了大型语言模型(LLMs)面临的提示注入攻击安全问题，提出了一种结合生成解释的调查工具来识别和评估对抗性提示注入。研究解决了在大量输入提示中识别恶意提示的挑战，并讨论了使用AI安全解决方案（如护栏）来保护LLMs免受此类攻击的方法。

---

## #389 — PRM-Free Security Alignment of Large Models via Red Teaming and Adversarial Training

`C` Score: 4.77 | 2025-07-14

**Authors:** Pengfei Du

**Categories:** cs.CR, cs.AI

**Scores:** Citation: 4.76 | Influential: 7.81 | Venue: 2.00 | Author: 1.12 | Recency: 7.00

**Links:** [arXiv](https://arxiv.org/abs/2507.14202) | [PDF](https://arxiv.org/pdf/2507.14202)

> 本文提出了一种无需过程奖励模型(PRM)的安全对齐框架，利用自动化红队和对抗训练实现强大安全保证。该方法通过遗传算法优化、多代理模拟和高级提示突变技术识别漏洞，结合课程学习和自适应正则化增强模型鲁棒性。实验表明，该方法比基于PRM的方法更优，同时减少61%计算成本，为资源受限组织提供高效安全对齐方案。

---

## #390 — Don't Walk the Line: Boundary Guidance for Filtered Generation

`C` Score: 4.77 | 2025-10-13

**Authors:** Sarah Ball, Andreas Haupt

**Categories:** cs.LG, cs.CL

**Scores:** Citation: 4.28 | Influential: 7.81 | Venue: 2.00 | Author: 2.55 | Recency: 7.00

**Links:** [arXiv](https://arxiv.org/abs/2510.11834) | [PDF](https://arxiv.org/pdf/2510.11834)

> 本文针对生成模型微调后倾向于在分类器决策边界附近生成样本的问题，提出了Boundary Guidance方法。这是一种强化学习微调技术，明确引导生成过程远离分类器的边界区域，从而同时提高输出的安全性和实用性。实验表明该方法在不同模型规模和奖励设计下均具有鲁棒性。

---

## #391 — ASGuard: Activation-Scaling Guard to Mitigate Targeted Jailbreaking Attack

`C` Score: 4.76 | 2025-09-30

**Authors:** Yein Park, Jungwoo Park, Jaewoo Kang

**Categories:** cs.AI

**Scores:** Citation: 3.32 | Influential: 7.81 | Venue: 2.00 | Author: 5.40 | Recency: 7.00

**Links:** [arXiv](https://arxiv.org/abs/2509.25843) | [PDF](https://arxiv.org/pdf/2509.25843)

> 本文提出了ASGuard框架，通过电路分析识别与特定越狱攻击（如时态攻击）因果相关的注意力头，并训练通道级缩放向量来校准激活状态。该方法结合预防性微调，迫使模型学习更稳健的拒绝机制，在保持通用能力的同时显著降低了攻击成功率，实现了安全性与效用的帕累托最优平衡。

---

## #392 — UpSafe$^\circ$C: Upcycling for Controllable Safety in Large Language Models

`C` Score: 4.76 | 2025-10-02

**Authors:** Yuhao Sun, Zhuoer Xu, Shiwen Cui, Kun Yang, Lingyun Yu, Yongdong Zhang et al. (7 total)

**Categories:** cs.AI, cs.CR, cs.LG

**Scores:** Citation: 3.32 | Influential: 7.81 | Venue: 2.00 | Author: 5.40 | Recency: 7.00

**Links:** [arXiv](https://arxiv.org/abs/2510.02194) | [PDF](https://arxiv.org/pdf/2510.02194)

> 本文提出了 UpSafe$^\circ$C 框架，旨在通过安全感知的升级技术解决大语言模型在安全性、实用性和可控性之间的平衡难题。该方法识别安全关键层并将其转化为稀疏混合专家结构，利用路由器作为软护栏选择性激活安全专家，同时采用两阶段监督微调策略以在增强安全判别的同时保留通用能力。其核心创新在于引入了推理时的安全温度机制，允许用户动态调整安全性与实用性之间的权衡，实现了灵活可控的安全防护。

---

## #393 — Mitigating Many-Shot Jailbreaking

`C` Score: 4.75 | 2025-04-13

**Authors:** Christopher M. Ackerman, Nina Panickssery

**Categories:** cs.LG, cs.AI, cs.CR

**Scores:** Citation: 4.92 | Influential: 7.81 | Venue: 2.00 | Author: 1.86 | Recency: 5.00

**Links:** [arXiv](https://arxiv.org/abs/2504.09604) | [PDF](https://arxiv.org/pdf/2504.09604)

> 本文探讨了缓解多样本越狱（MSJ）攻击的方法，该攻击利用长上下文窗口中的不当示例绕过安全训练。研究发现，结合微调和输入清理技术能显著降低 MSJ 攻击的有效性，同时保持模型在良性任务上的性能。该方案为模型安全后训练提供了有意义的改进方向，有助于缓解这一特定漏洞。

---

## #394 — LightDefense: A Lightweight Uncertainty-Driven Defense against Jailbreaks via Shifted Token Distribution

`C` Score: 4.75 | 2025-04-02

**Authors:** Zhuoran Yang, Yanyong Zhang

**Categories:** cs.CR, cs.CY

**Scores:** Citation: 4.26 | Influential: 7.81 | Venue: 2.00 | Author: 3.78 | Recency: 5.00

**Links:** [arXiv](https://arxiv.org/abs/2504.01533) | [PDF](https://arxiv.org/pdf/2504.01533)

> 本文提出了LightDefense，一种针对白盒模型的轻量级越狱防御机制，无需辅助模型即可工作。该方法利用安全导向的方向调整词汇表中标记的概率，并创新性地利用LLM对提示词的不确定性来衡量其有害性，从而自适应地调整防御强度。实验表明，LightDefense在防御多种攻击方法时表现有效，且未损害对良性查询的有用性，是一种高效的安全增强方案。

---

## #395 — Safety Alignment Backfires: Preventing the Re-emergence of Suppressed Concepts in Fine-tuned Text-to-Image Diffusion Models

`C` Score: 4.75 | 2024-11-30

**Authors:** Sanghyun Kim, Moonseok Choi, Jinwoo Shin, Juho Lee

**Categories:** cs.AI, cs.CV

**Scores:** Citation: 4.46 | Influential: 7.81 | Venue: 2.00 | Author: 3.23 | Recency: 5.00

**Links:** [arXiv](https://arxiv.org/abs/2412.00357) | [PDF](https://arxiv.org/pdf/2412.00357)

> 本文揭示了文本到图像扩散模型在微调过程中安全对齐失效的漏洞，即标准微调会导致被抑制的有害内容重新出现。为此，作者提出了Modular LoRA解决方案，通过将安全LoRA模块与微调组件分离训练，在不影响新任务性能的前提下有效防止有害内容的再学习。

---

## #396 — When Actions Go Off-Task: Detecting and Correcting Misaligned Actions in Computer-Use Agents

`C` Score: 4.74 | 2026-02-09

**Authors:** Yuting Ning, Jaylen Jones, Zhehao Zhang, Chentao Ye, Weitong Ruan, Junyi Li et al. (8 total)

**Categories:** cs.CL

**Scores:** Citation: 3.32 | Influential: 7.81 | Venue: 2.00 | Author: 3.23 | Recency: 10.00

**Links:** [arXiv](https://arxiv.org/abs/2602.08995) | [PDF](https://arxiv.org/pdf/2602.08995)

> 针对计算机使用智能体（CUA）在执行过程中产生的偏离用户意图的错位行为，本文首次定义了该问题并构建了包含真实轨迹的MisActBench基准。作者提出了DeAction这一通用的安全护栏，能够在执行前检测错位行为并通过结构化反馈进行迭代修正。实验表明，DeAction在离线和在线评估中均显著优于现有基线，能有效降低对抗攻击成功率并保持良性环境下的任务成功率。

---

## #397 — RASA: Routing-Aware Safety Alignment for Mixture-of-Experts Models

`C` Score: 4.74 | 2026-02-04

**Authors:** Jiacheng Liang, Yuhui Wang, Tanqiu Jiang, Ting Wang

**Categories:** cs.LG, cs.AI, cs.CR

**Scores:** Citation: 3.32 | Influential: 7.81 | Venue: 2.00 | Author: 3.23 | Recency: 10.00

**Links:** [arXiv](https://arxiv.org/abs/2602.04448) | [PDF](https://arxiv.org/pdf/2602.04448)

> 本文针对混合专家模型的安全对齐挑战，提出了路由感知的专家级对齐框架RASA。该方法识别并修复被越狱攻击过度激活的关键专家，同时防止基于路由的绕过，从而在保持通用能力的同时实现近乎完美的鲁棒性。研究表明，针对性的专家修复比全局参数更新更有效。

---

## #398 — RAPO: Risk-Aware Preference Optimization for Generalizable Safe Reasoning

`C` Score: 4.74 | 2026-02-04

**Authors:** Zeming Wei, Qiaosheng Zhang, Xia Hu, Xingcheng Xu

**Categories:** cs.LG, cs.AI, cs.CL

**Scores:** Citation: 3.32 | Influential: 7.81 | Venue: 2.00 | Author: 3.23 | Recency: 10.00

**Links:** [arXiv](https://arxiv.org/abs/2602.04224) | [PDF](https://arxiv.org/pdf/2602.04224)

> 本文针对大型推理模型在复杂越狱攻击下安全推理泛化不足的问题，提出了风险感知偏好优化框架RAPO。该框架使模型能够以适当的粒度自适应地识别和处理思维过程中的安全风险，从而在保持通用效用的同时增强对多样化攻击的防御能力。实验证明RAPO显著提升了LRM的安全推理鲁棒性。

---

## #399 — SFCoT: Safer Chain-of-Thought via Active Safety Evaluation and Calibration

`C` Score: 4.74 | 2026-03-16

**Authors:** Yu Pan, Wenlong Yu, Tiejun Wu, Xiaohu Ye, Qiannan Si, Guangquan Xu et al. (7 total)

**Categories:** cs.CR, cs.AI

**Scores:** Citation: 3.32 | Influential: 7.81 | Venue: 2.00 | Author: 3.23 | Recency: 10.00

**Links:** [arXiv](https://arxiv.org/abs/2603.15397) | [PDF](https://arxiv.org/pdf/2603.15397)

> 针对大语言模型思维链易受越狱攻击且中间步骤缺乏监控的问题，本文提出了SFCoT框架。该框架通过三层安全评分和多视角一致性验证，实时评估并校准潜在的不安全推理步骤，动态干预推理轨迹以引导安全输出。实验表明，SFCoT能将攻击成功率从58.97%降至12.31%，在不显著影响通用性能的前提下有效增强了模型安全性。

---

## #400 — Latent Instruction Representation Alignment: defending against jailbreaks, backdoors and undesired knowledge in LLMs

`C` Score: 4.74 | 2026-04-12

**Authors:** Eric Easley, Sebastian Farquhar

**Categories:** cs.LG

**Scores:** Citation: 3.32 | Influential: 7.81 | Venue: 2.00 | Author: 3.23 | Recency: 10.00

**Links:** [arXiv](https://arxiv.org/abs/2604.10403) | [PDF](https://arxiv.org/pdf/2604.10403)

> 本文提出了一种名为潜在指令表示对齐(LIRA)的方法，用于防御LLMs中的越狱、后门和不期望的知识。与先前工作不同，该方法专门训练模型改变其解释指令的方式，而非基于模型接收到恶意指令时的行动进行训练。通过内部对抗训练算法，该方法阻止了超过99%的PEZ越狱攻击，移除了一个具有挑战性的不安全代码后门，并在WMDP网络攻击上实现了最优遗忘，同时保持良性能力损失 negligible。

---

## #401 — Developing Assurance Cases for Adversarial Robustness and Regulatory Compliance in LLMs

`C` Score: 4.74 | 2024-10-04

**Authors:** Tomas Bueno Momcilovic, Dian Balta, Beat Buesser, Giulio Zizzo, Mark Purcell

**Categories:** cs.CR, cs.AI, cs.SE

**Scores:** Citation: 3.34 | Influential: 7.81 | Venue: 2.00 | Author: 6.47 | Recency: 5.00

**Links:** [arXiv](https://arxiv.org/abs/2410.05304) | [PDF](https://arxiv.org/pdf/2410.05304)

> 本文提出了一种为大语言模型开发对抗鲁棒性和监管合规性保障案例的方法。该框架在 LLM 部署的各个阶段引入护栏，旨在减轻越狱等对抗性攻击，并确保符合欧盟 AI 法规。研究通过两个示例案例展示了如何针对不同上下文定制策略，以构建鲁棒且合规的 AI 系统。

---

## #402 — Bleeding Pathways: Vanishing Discriminability in LLM Hidden States Fuels Jailbreak Attacks

`C` Score: 4.73 | 2025-03-14

**Authors:** Yingjie Zhang, Tong Liu, Zhe Zhao, Guozhu Meng, Kai Chen

**Categories:** cs.CR, cs.AI

**Scores:** Citation: 3.32 | Influential: 7.81 | Venue: 2.00 | Author: 6.47 | Recency: 5.00

**Links:** [arXiv](https://arxiv.org/abs/2503.11185) | [PDF](https://arxiv.org/pdf/2503.11185)

> 研究揭示了LLM在响应生成过程中区分有害与安全输出能力下降的根本原因。提出DEEPALIGN防御框架，通过在响应生成中点应用对比隐藏状态引导，增强有害和良性隐藏状态间的分离，实现生成过程中的内在毒性检测和干预，有效降低越狱攻击成功率。

---

## #403 — Machine Learning for Detection and Analysis of Novel LLM Jailbreaks

`C` Score: 4.72 | 2025-10-02

**Authors:** John Hawkins, Aditya Pramar, Rodney Beard, Rohitash Chandra

**Categories:** cs.CL, cs.AI, cs.CY

**Scores:** Citation: 4.17 | Influential: 7.81 | Venue: 2.00 | Author: 2.55 | Recency: 7.00

**Links:** [arXiv](https://arxiv.org/abs/2510.01644) | [PDF](https://arxiv.org/pdf/2510.01644)

> 该研究深入分析了利用机器学习技术检测大语言模型越狱攻击的可行性，重点评估了模型区分恶意越狱提示与正常使用请求的能力，包括对未见攻击策略的识别。结果显示，端到端微调BERT模型在当前数据集上表现最优，且通过可视化分析发现提示结构中的显式自反性是判断越狱意图的关键特征。

---

## #404 — Know Thy Enemy: Securing LLMs Against Prompt Injection via Diverse Data Synthesis and Instruction-Level Chain-of-Thought Learning

`C` Score: 4.72 | 2026-01-08

**Authors:** Zhiyuan Chang, Mingyang Li, Yuekai Huang, Ziyou Jiang, Xiaojun Jia, Qian Xiong et al. (9 total)

**Categories:** cs.AI, cs.CR

**Scores:** Citation: 3.32 | Influential: 7.81 | Venue: 2.00 | Author: 3.78 | Recency: 9.00

**Links:** [arXiv](https://arxiv.org/abs/2601.04666) | [PDF](https://arxiv.org/pdf/2601.04666)

> 本文提出了InstruCoT，一种通过合成多样化数据和指令级思维链微调来防御提示注入攻击的模型增强方法。该方法使大语言模型能够有效识别并拒绝恶意指令，在保持效用的同时显著提升了防御性能，解决了恶意指令语义边界模糊的难题。

---

## #405 — TAIJI: Textual Anchoring for Immunizing Jailbreak Images in Vision Language Models

`C` Score: 4.71 | 2025-03-13

**Authors:** Xiangyu Yin, Yi Qi, Jinwei Hu, Zhen Chen, Yi Dong, Xingyu Zhao et al. (8 total)

**Categories:** cs.CV, cs.AI

**Scores:** Citation: 4.17 | Influential: 7.81 | Venue: 2.00 | Author: 3.78 | Recency: 5.00

**Links:** [arXiv](https://arxiv.org/abs/2503.10872) | [PDF](https://arxiv.org/pdf/2503.10872)

> 论文提出TAIJI，一种新颖的黑盒防御框架，利用基于关键短语的文本锚点增强模型评估和减轻视觉和文本提示中嵌入有害内容的能力。与现有方法不同，TAIJI在推理过程中只需单次查询，同时保持VLM在良性任务上的性能，为现实世界部署提供实用高效的解决方案。

---

## #406 — Highlight & Summarize: RAG without the jailbreaks

`C` Score: 4.69 | 2025-08-04

**Authors:** Giovanni Cherubin, Andrew Paverd

**Categories:** cs.CL, cs.LG

**Scores:** Citation: 3.87 | Influential: 7.81 | Venue: 2.00 | Author: 3.23 | Recency: 7.00

**Links:** [arXiv](https://arxiv.org/abs/2508.02872) | [PDF](https://arxiv.org/pdf/2508.02872)

> 本文提出了Highlight & Summarize (H&S)设计模式，通过架构设计防止检索增强生成（RAG）系统遭受越狱攻击。该方法将管道分为高亮器和总结器两部分，确保生成式LLM永远不会看到用户的原始问题，从而从根本上阻断攻击。

---

## #407 — ConceptGuard: Neuro-Symbolic Safety Guardrails via Sparse Interpretable Jailbreak Concepts

`C` Score: 4.67 | 2025-08-22

**Authors:** Darpan Aswal, Céline Hudelot

**Categories:** cs.CL, cs.AI, cs.SC

**Scores:** Citation: 3.32 | Influential: 7.81 | Venue: 2.00 | Author: 4.79 | Recency: 7.00

**Links:** [arXiv](https://arxiv.org/abs/2508.16325) | [PDF](https://arxiv.org/pdf/2508.16325)

> 本文提出了ConceptGuard，一种利用稀疏自编码器识别LLM内部与越狱主题相关的可解释概念的新框架。通过提取语义上有意义的内部表示，该方法构建了稳健且可解释的安全护栏，无需牺牲模型能力或进一步微调。研究还揭示了越狱攻击在表示空间中共享的激活几何特征。

---

## #408 — Dual Mechanisms of Value Expression: Intrinsic vs. Prompted Values in Large Language Models

`C` Score: 4.67 | 2025-09-29

**Authors:** Jongwook Han, Jongwon Lim, Injin Kong, Yohan Jo

**Categories:** cs.CL, cs.AI

**Scores:** Citation: 3.32 | Influential: 7.81 | Venue: 2.00 | Author: 4.79 | Recency: 7.00

**Links:** [arXiv](https://arxiv.org/abs/2509.24319) | [PDF](https://arxiv.org/pdf/2509.24319)

> 本文从机制层面分析了大语言模型中内在价值表达与提示引导价值表达的异同，发现两者既有共享组件也有独特元素。研究表明，内在机制促进词汇多样性，而提示机制增强指令遵循能力，甚至在越狱等远程任务中发挥作用，这一发现为深入理解模型价值对齐的内部机制提供了新的视角。

---

## #409 — CrossGuard: Safeguarding MLLMs against Joint-Modal Implicit Malicious Attacks

`C` Score: 4.67 | 2025-10-20

**Authors:** Xu Zhang, Hao Li, Zhichao Lu

**Categories:** cs.CR, cs.AI

**Scores:** Citation: 3.32 | Influential: 7.81 | Venue: 2.00 | Author: 4.79 | Recency: 7.00

**Links:** [arXiv](https://arxiv.org/abs/2510.17687) | [PDF](https://arxiv.org/pdf/2510.17687)

> 该研究针对多模态大模型中的联合模态隐式恶意攻击，提出了 ImpForge 红队测试管道生成数据，并开发了 CrossGuard 防御系统。CrossGuard 能够感知意图，对显式和隐式威胁提供强有力的防御，在保持高实用性的同时显著提升了安全性。

---

## #410 — COSMO-RL: Towards Trustworthy LMRMs via Joint Safety and Stability

`C` Score: 4.67 | 2025-10-05

**Authors:** Yizhuo Ding, Mingkang Chen, Qiuhua Liu, Fenghua Weng, Wanying Qu, Yue Yang et al. (10 total)

**Categories:** cs.AI, cs.LG

**Scores:** Citation: 3.32 | Influential: 7.81 | Venue: 2.00 | Author: 4.79 | Recency: 7.00

**Links:** [arXiv](https://arxiv.org/abs/2510.04196) | [PDF](https://arxiv.org/pdf/2510.04196)

> 本文提出了COSMO-RL，一种混合强化学习框架，旨在训练大型多模态推理模型（LMRMs）在多任务和多目标信号下实现安全与能力的共同增长。该框架通过让安全性和能力在同一稳定管线中协同进化，解决了单目标训练导致的策略漂移问题。实验表明，COSMO-R1模型在保持多模态推理能力的同时，显著增强了对多模态越狱的鲁棒性并减少了不必要的拒绝。

---

## #411 — MCP Safety Training: Learning to Refuse Falsely Benign MCP Exploits using Improved Preference Alignment

`C` Score: 4.66 | 2025-05-29

**Authors:** John Halloran

**Categories:** cs.LG, cs.CR

**Scores:** Citation: 4.52 | Influential: 7.81 | Venue: 2.00 | Author: 1.12 | Recency: 7.00

**Links:** [arXiv](https://arxiv.org/abs/2505.23634) | [PDF](https://arxiv.org/pdf/2505.23634)

> 本文针对模型上下文协议（MCP）面临的虚假良性攻击，提出了一种结合直接偏好优化（DPO）和检索增强偏好对齐（RAG-Pref）的拒绝训练方法。研究构建了新的 MCP 数据集，并证明 RAG-Pref 能显著提升大语言模型拒绝此类攻击的能力，从而增强安全护栏。

---

## #412 — Don't Command, Cultivate: An Exploratory Study of System-2 Alignment

`C` Score: 4.66 | 2024-11-26

**Authors:** Yuhang Wang, Yuxiang Zhang, Yanxu Zhu, Xinyan Wen, Jitao Sang

**Categories:** cs.CL

**Scores:** Citation: 3.90 | Influential: 7.81 | Venue: 2.00 | Author: 4.27 | Recency: 5.00

**Links:** [arXiv](https://arxiv.org/abs/2411.17075) | [PDF](https://arxiv.org/pdf/2411.17075)

> 本文探讨了System-2思维模式对模型安全性的影响，通过对o1模型的安全评估发现其在数学编码越狱攻击下仍存在脆弱性。研究通过提示工程和监督微调探索了开源模型中System-2安全对齐的方法，并提出过程监督的实施计划以增强安全对齐。

---

## #413 — Robust Driving Control for Autonomous Vehicles: An Intelligent General-sum Constrained Adversarial Reinforcement Learning Approach

`C` Score: 4.65 | 2025-10-10

**Authors:** Junchao Fan, Qi Wei, Ruichen Zhang, Dusit Niyato, Yang Lu, Jianhua Wang et al. (8 total)

**Categories:** cs.LG, cs.AI

**Scores:** Citation: 4.25 | Influential: 7.81 | Venue: 2.00 | Author: 1.86 | Recency: 7.00

**Links:** [arXiv](https://arxiv.org/abs/2510.09041) | [PDF](https://arxiv.org/pdf/2510.09041)

> 针对自动驾驶深度强化学习策略易受对抗攻击的问题，提出了一种智能广义和约束对抗强化学习方法（IGCARL）。该方法包含一个战略目标对抗者和一个鲁棒驾驶代理，通过多步协调攻击诱导安全关键事件，并利用约束公式确保学习稳定性。这显著提升了自动驾驶策略在对抗环境下的鲁棒性。

---

## #414 — Do Internal Layers of LLMs Reveal Patterns for Jailbreak Detection?

`C` Score: 4.64 | 2025-10-08

**Authors:** Sri Durga Sai Sowmya Kadali, Evangelos E. Papalexakis

**Categories:** cs.CL

**Scores:** Citation: 4.22 | Influential: 7.81 | Venue: 2.00 | Author: 1.86 | Recency: 7.00

**Links:** [arXiv](https://arxiv.org/abs/2510.06594) | [PDF](https://arxiv.org/pdf/2510.06594)

> 本文针对大语言模型面临的越狱攻击威胁，提出通过分析模型的内部表示来研究越狱现象，重点考察隐藏层对越狱提示与良性提示的响应差异。研究对开源模型 GPT-J 和状态空间模型 Mamba2 进行了分析，初步揭示了两者在面对不同类型提示时表现出显著的逐层行为差异。结果表明，利用模型内部动力学特征有望为鲁棒的越狱检测与防御机制提供新的研究方向。

---

## #415 — Defending Large Language Models Against Jailbreak Exploits with Responsible AI Considerations

`C` Score: 4.64 | 2025-11-24

**Authors:** Ryan Wong, Hosea David Yu Fei Ng, Dhananjai Sharma, Glenn Jun Jie Ng, Kavishvaran Srinivasan

**Categories:** cs.CR, cs.AI

**Scores:** Citation: 3.32 | Influential: 7.81 | Venue: 2.00 | Author: 3.23 | Recency: 9.00

**Links:** [arXiv](https://arxiv.org/abs/2511.18933) | [PDF](https://arxiv.org/pdf/2511.18933)

> 本文针对大语言模型面临的越狱攻击威胁，首先提出了涵盖提示词级、模型级及训练时的防御分类法，并设计了三种创新防御策略。其中包括通过输入清洗和改写中和恶意输入的提示词级框架、在推理时强化拒绝行为的基于Logit的引导防御，以及利用MetaGPT实现结构化协作的特定领域Agent防御。实验结果显示，这些策略显著降低了攻击成功率，其中Agent防御实现了完全缓解，有效提升了模型安全性。

---

## #416 — KG-DF: A Black-box Defense Framework against Jailbreak Attacks Based on Knowledge Graphs

`C` Score: 4.64 | 2025-11-09

**Authors:** Shuyuan Liu, Jiawei Chen, Xiao Yang, Hang Su, Zhaoxia Yin

**Categories:** cs.CR, cs.AI

**Scores:** Citation: 3.32 | Influential: 7.81 | Venue: 2.00 | Author: 3.23 | Recency: 9.00

**Links:** [arXiv](https://arxiv.org/abs/2511.07480) | [PDF](https://arxiv.org/pdf/2511.07480)

> 本文提出了KG-DF，一种基于知识图谱的黑盒防御框架，旨在应对大语言模型的越狱攻击。该框架利用知识图谱的结构化知识表示和语义关联能力，通过可扩展的语义解析模块将输入查询转换为安全概念表示，从而识别潜在恶意意图并提供安全推理路径。实验结果显示，该框架在保持模型通用性的同时，显著增强了对各种越狱攻击的防御性能。

---

## #417 — Lattice: Generative Guardrails for Conversational Agents

`C` Score: 4.64 | 2026-01-24

**Authors:** Emily Broadhurst, Tawab Safi, Joseph Edell, Vashisht Ganesh, Karime Maamari

**Categories:** cs.AI

**Scores:** Citation: 3.32 | Influential: 7.81 | Venue: 2.00 | Author: 2.55 | Recency: 10.00

**Links:** [arXiv](https://arxiv.org/abs/2601.17481) | [PDF](https://arxiv.org/pdf/2601.17481)

> 本文介绍了Lattice，一个用于自构建和持续改进对话Agent护栏的框架。Lattice通过迭代模拟和优化从标记示例中构建初始护栏，并利用风险评估和对抗测试在部署后自主适应。实验表明，Lattice在保持数据集上的F1得分显著优于关键词基线和现有护栏模型，证明了通过迭代优化构建有效护栏的可行性。

---

## #418 — Be Your Own Red Teamer: Safety Alignment via Self-Play and Reflective Experience Replay

`C` Score: 4.64 | 2026-01-15

**Authors:** Hao Wang, Yanting Wang, Hao Li, Rui Li, Lei Sha

**Categories:** cs.CR, cs.CL

**Scores:** Citation: 3.32 | Influential: 7.81 | Venue: 2.00 | Author: 3.23 | Recency: 9.00

**Links:** [arXiv](https://arxiv.org/abs/2601.10589) | [PDF](https://arxiv.org/pdf/2601.10589)

> 本文提出了一种基于自我博弈和反思经验回放的安全对齐方法，让单个 LLM 同时扮演攻击者和防御者以动态进化防御策略。该方法通过强化学习循环和 UCB 采样策略，有效提升了模型对抗新型越狱攻击的鲁棒性，实现了自主进化的安全防御。

---

## #419 — The Straight and Narrow: Do LLMs Possess an Internal Moral Path?

`C` Score: 4.64 | 2026-01-15

**Authors:** Luoming Hu, Jingjie Zeng, Liang Yang, Hongfei Lin

**Categories:** cs.CL

**Scores:** Citation: 3.32 | Influential: 7.81 | Venue: 2.00 | Author: 3.23 | Recency: 9.00

**Links:** [arXiv](https://arxiv.org/abs/2601.10307) | [PDF](https://arxiv.org/pdf/2601.10307)

> 本文利用道德基础理论映射了 LLM 的内在道德景观，并提出了自适应道德融合（AMF）方法来动态干预推理过程。该方法在减少良性查询错误拒绝的同时，有效降低了越狱攻击的成功率，解决了安全性与实用性之间的权衡问题。

---

## #420 — Pragma-VL: Towards a Pragmatic Arbitration of Safety and Helpfulness in MLLMs

`C` Score: 4.64 | 2026-02-28

**Authors:** Ming Wen, Kun Yang, Xin Chen, Jingyu Zhang, Dingding Han, Shiwen Cui et al. (7 total)

**Categories:** cs.LG, cs.AI

**Scores:** Citation: 3.32 | Influential: 7.81 | Venue: 2.00 | Author: 2.55 | Recency: 10.00

**Links:** [arXiv](https://arxiv.org/abs/2603.13292) | [PDF](https://arxiv.org/pdf/2603.13292)

> 本文提出了Pragma-VL，一种端到端的对齐算法，旨在解决多模态大模型在安全性与有用性之间的权衡问题。该方法通过风险感知聚类增强视觉风险感知，并利用具有理论保证的奖励模型进行协同学习，实现了上下文感知的动态仲裁。实验表明，Pragma-VL在保持通用能力的同时，有效平衡了安全性和有用性。

---

## #421 — MANATEE: Inference-Time Lightweight Diffusion Based Safety Defense for LLMs

`C` Score: 4.64 | 2026-02-21

**Authors:** Chun Yan Ryan Kan, Tommy Tran, Vedant Yadav, Ava Cai, Kevin Zhu, Ruizhe Li et al. (7 total)

**Categories:** cs.CR, cs.AI, cs.CL

**Scores:** Citation: 3.32 | Influential: 7.81 | Venue: 2.00 | Author: 2.55 | Recency: 10.00

**Links:** [arXiv](https://arxiv.org/abs/2602.18782) | [PDF](https://arxiv.org/pdf/2602.18782)

> 提出MANATEE，一种基于扩散模型的推理时轻量级安全防御方法。该方法通过良性表示流形的密度估计和扩散投影，将异常表示映射至安全区域，无需有害训练数据。实验表明其能显著降低攻击成功率并保持模型效用。

---

## #422 — AISA: Awakening Intrinsic Safety Awareness in Large Language Models against Jailbreak Attacks

`C` Score: 4.64 | 2026-02-14

**Authors:** Weiming Song, Xuan Xie, Ruiping Yin

**Categories:** cs.CR, cs.AI

**Scores:** Citation: 3.32 | Influential: 7.81 | Venue: 2.00 | Author: 2.55 | Recency: 10.00

**Links:** [arXiv](https://arxiv.org/abs/2602.13547) | [PDF](https://arxiv.org/pdf/2602.13547)

> 本文提出了AISA，一种轻量级的单次防御机制，旨在激活大语言模型内部潜藏的安全行为以对抗越狱攻击。AISA通过时空分析定位内在安全意识，利用特定注意力头的输出提取可解释的提示风险分数，并在推理时进行logit级别调制。实验表明，AISA在不改变模型参数或增加延迟的情况下，显著提高了模型的鲁棒性和迁移性，同时保持了实用性。

---

## #423 — OOD-MMSafe: Advancing MLLM Safety from Harmful Intent to Hidden Consequences

`C` Score: 4.64 | 2026-03-10

**Authors:** Ming Wen, Kun Yang, Jingyu Zhang, Yuxuan Liu, shiwen cui, Shouling Ji et al. (7 total)

**Categories:** cs.AI

**Scores:** Citation: 3.32 | Influential: 7.81 | Venue: 2.00 | Author: 2.55 | Recency: 10.00

**Links:** [arXiv](https://arxiv.org/abs/2603.09706) | [PDF](https://arxiv.org/pdf/2603.09706)

> 本文提出将多模态大模型的安全前沿从恶意意图转向后果驱动安全，并发布了包含455个样本的OOD-MMSafe基准，旨在评估模型识别潜在因果链风险的能力。针对现有模型的因果盲区，作者开发了后果感知安全策略优化（CASPO）框架，通过动态参考和自蒸馏奖励显著提升了模型的风险识别能力，将失败率降至个位数。

---

## #424 — VoiceSHIELD-Small: Real-Time Malicious Speech Detection and Transcription

`C` Score: 4.64 | 2026-03-08

**Authors:** Sumit Ranjan, Sugandha Sharma, Ubaid Abbas, Puneeth N Ail

**Categories:** cs.SD, cs.AI

**Scores:** Citation: 3.32 | Influential: 7.81 | Venue: 2.00 | Author: 2.55 | Recency: 10.00

**Links:** [arXiv](https://arxiv.org/abs/2603.07708) | [PDF](https://arxiv.org/pdf/2603.07708)

> 本文提出了VoiceSHIELD-Small，一种基于Whisper-small的轻量级实时模型，能够同步进行语音转录和恶意语音检测。该模型通过在编码器上添加分类头，实现了对提示注入和社会工程等恶意语音的高效识别，在保持高准确率的同时显著降低了检测延迟。

---

## #425 — S3LoRA: Safe Spectral Sharpness-Guided Pruning in Adaptation of Agent Planner

`C` Score: 4.63 | 2025-08-20

**Authors:** Shuang Ao, Gopal Rumchurn

**Categories:** cs.AI

**Scores:** Citation: 3.97 | Influential: 7.81 | Venue: 2.00 | Author: 2.55 | Recency: 7.00

**Links:** [arXiv](https://arxiv.org/abs/2508.15068) | [PDF](https://arxiv.org/pdf/2508.15068)

> S3LoRA是一种轻量级、无数据的框架，通过分析LoRA权重更新的结构属性，利用谱锐度指数检测并修剪潜在不安全的层。该方法在不牺牲任务性能的前提下，有效缓解了参数高效微调带来的安全风险，并降低了推理成本。

---

## #426 — xSRL: Safety-Aware Explainable Reinforcement Learning -- Safety as a Product of Explainability

`C` Score: 4.61 | 2024-12-26

**Authors:** Risal Shahriar Shefin, Md Asifur Rahman, Thai Le, Sarra Alqahtani

**Categories:** cs.AI, cs.HC, cs.LG

**Scores:** Citation: 3.41 | Influential: 7.81 | Venue: 2.00 | Author: 5.40 | Recency: 5.00

**Links:** [arXiv](https://arxiv.org/abs/2412.19311) | [PDF](https://arxiv.org/pdf/2412.19311)

> 针对强化学习在自动驾驶等安全关键应用中的可解释性缺失，本文提出了xSRL框架。该框架整合了局部和全局解释，为智能体的决策过程提供清晰洞察，通过增强可解释性来建立对安全机制的信任，确保安全关键决策被充分理解，弥补了传统方法的不足。

---

## #427 — Does Representation Intervention Really Identify Desired Concepts and Elicit Alignment?

`C` Score: 4.60 | 2025-05-24

**Authors:** Hongzheng Yang, Yongqiang Chen, Zeyu Qin, Tongliang Liu, Chaowei Xiao, Kun Zhang et al. (7 total)

**Categories:** cs.LG, stat.ML

**Scores:** Citation: 3.32 | Influential: 7.81 | Venue: 2.00 | Author: 4.27 | Recency: 7.00

**Links:** [arXiv](https://arxiv.org/abs/2505.18672) | [PDF](https://arxiv.org/pdf/2505.18672)

> 本文探讨了表征干预在安全对齐中的局限性，并提出了概念集中（COCA）方法。COCA通过显式推理重构训练数据，简化有害与良性表征之间的决策边界，显著降低了越狱成功率，同时保持了模型在常规任务上的性能，实现了更有效的线性擦除。

---

## #428 — A Real-Time, Self-Tuning Moderator Framework for Adversarial Prompt Detection

`C` Score: 4.60 | 2025-08-10

**Authors:** Ivan Zhang

**Categories:** cs.CR, cs.AI

**Scores:** Citation: 3.32 | Influential: 7.81 | Venue: 2.00 | Author: 4.27 | Recency: 7.00

**Links:** [arXiv](https://arxiv.org/abs/2508.07139) | [PDF](https://arxiv.org/pdf/2508.07139)

> 针对现有防御措施难以快速适应新攻击或影响模型性能的问题，本文提出了一种实时自调节（RTST）审核框架，用于防御对抗性提示攻击。该框架在Google Gemini模型上的实证评估表明，相比传统的微调或分类器模型，这种自适应且侵入性极小的方法能有效防御现代越狱攻击，同时保持轻量级的训练开销。

---

## #429 — GuardNet: Graph-Attention Filtering for Jailbreak Defense in Large Language Models

`C` Score: 4.60 | 2025-09-27

**Authors:** Javad Forough, Mohammad Maheri, Hamed Haddadi

**Categories:** cs.LG

**Scores:** Citation: 4.12 | Influential: 7.81 | Venue: 2.00 | Author: 1.86 | Recency: 7.00

**Links:** [arXiv](https://arxiv.org/abs/2509.23037) | [PDF](https://arxiv.org/pdf/2509.23037)

> 本文提出了GuardNet，一种基于图神经网络的分层过滤框架，用于在推理前检测和过滤越狱提示。该框架结合了序列链接、句法依赖和注意力关系构建结构化图，通过提示级和令牌级两级过滤器，显著提升了越狱检测的准确性和鲁棒性，且在实际部署中保持了可接受的延迟。

---

## #430 — Beyond Sharp Minima: Robust LLM Unlearning via Feedback-Guided Multi-Point Optimization

`C` Score: 4.59 | 2025-09-24

**Authors:** Wenhan Wu, Zheyuan Liu, Chongyang Gao, Ren Wang, Kaize Ding

**Categories:** cs.LG, cs.AI

**Scores:** Citation: 4.10 | Influential: 7.81 | Venue: 2.00 | Author: 1.86 | Recency: 7.00

**Links:** [arXiv](https://arxiv.org/abs/2509.20230) | [PDF](https://arxiv.org/pdf/2509.20230)

> 现有LLM遗忘方法存在严重安全漏洞，模型参数在优化过程中易陷入损失景观的尖锐极小值，导致被遗忘信息极易通过重学习攻击恢复。本文提出StableUN框架，一种双层反馈引导的多点优化方法，旨在引导模型寻找更平坦且稳定的极小值区域。该方法有效解决了遗忘过程中的鲁棒性差距，显著增强了模型抵御重学习攻击的能力，确保敏感信息被彻底移除。

---

## #431 — Improving LLM Outputs Against Jailbreak Attacks with Expert Model Integration

`C` Score: 4.57 | 2025-05-18

**Authors:** Tatia Tsmindashvili, Ana Kolkhidashvili, Dachi Kurtskhalia, Nino Maghlakelidze, Elene Mekvabishvili, Guram Dentoshvili et al. (10 total)

**Categories:** cs.CR, cs.AI

**Scores:** Citation: 3.64 | Influential: 7.81 | Venue: 5.00 | Author: 1.12 | Recency: 7.00

**Links:** [arXiv](https://arxiv.org/abs/2505.17066) | [PDF](https://arxiv.org/pdf/2505.17066)

> 针对大语言模型在生产环境中面临的越狱及提示注入风险，特别是在特定领域（如汽车行业）应用时的安全挑战，本文提出了名为Archias的专家模型集成方案。该方案指出传统微调与上下文学习难以应对不断演变的攻击手段且缺乏灵活性，因此利用Archias模型精准区分域内与域外通信，并对用户查询进行多类别分类。这一创新方法有效增强了模型对恶意输入的识别能力，确保输出符合行业特定安全目标。

---

## #432 — FLAME: Flexible LLM-Assisted Moderation Engine

`C` Score: 4.56 | 2025-02-13

**Authors:** Ivan Bakulin, Ilia Kopanichuk, Iaroslav Bespalov, Nikita Radchenko, Vladimir Shaposhnikov, Dmitry Dylov et al. (7 total)

**Categories:** cs.CR, cs.AI, cs.CL

**Scores:** Citation: 3.32 | Influential: 7.81 | Venue: 2.00 | Author: 5.40 | Recency: 5.00

**Links:** [arXiv](https://arxiv.org/abs/2502.09175) | [PDF](https://arxiv.org/pdf/2502.09175)

> FLAME提出从输入过滤转向输出审核的新方法，评估模型响应而非用户查询。该引擎具有计算效率高、增强对BoN越狱攻击抵抗力、灵活定义安全标准等优势。实验表明FLAME在GPT-4o-mini和DeepSeek-v3上将攻击成功率降低约9倍，同时保持低计算开销，显著优于当前内容审核系统，为LLM交互提供更强大的安全保障。

---

## #433 — Neurodivergent Influenceability as a Contingent Solution to the AI Alignment Problem

`C` Score: 4.56 | 2025-05-05

**Authors:** Alberto Hernández-Espinosa, Felipe S. Abrahão, Olaf Witkowski, Hector Zenil

**Categories:** cs.AI

**Scores:** Citation: 3.59 | Influential: 7.81 | Venue: 2.00 | Author: 3.23 | Recency: 7.00

**Links:** [arXiv](https://arxiv.org/abs/2505.02581) | [PDF](https://arxiv.org/pdf/2505.02581)

> 本文探讨了AI对齐问题，提出完全对齐在数学上是不可能的，并主张利用不可避免的错位作为一种制衡机制。通过引入基于扰动和干预分析的“改变观点攻击测试”，研究了人类和智能体如何通过合作与竞争来引导AI，提出通过竞争性智能体生态系统来缓解单一系统主导的风险。

---

## #434 — Reflection-Driven Control for Trustworthy Code Agents

`C` Score: 4.54 | 2025-12-22

**Authors:** Bin Wang, Jiazheng Quan, Xingrui Yu, Hansen Hu, Yuhao, Ivor Tsang

**Categories:** cs.CR, cs.AI, cs.SE

**Scores:** Citation: 3.32 | Influential: 7.81 | Venue: 2.00 | Author: 2.55 | Recency: 9.00

**Links:** [arXiv](https://arxiv.org/abs/2512.21354) | [PDF](https://arxiv.org/pdf/2512.21354)

> 提出Reflection-Driven Control，一种可集成到通用Agent架构中的标准化控制模块。该模块通过在推理过程中运行内部反思循环来监控决策路径，并在检测到风险时检索修复示例注入安全约束，显著提升了代码生成Agent的安全性和策略合规性。

---

## #435 — Query Suggestion for Retrieval-Augmented Generation via Dynamic In-Context Learning

`C` Score: 4.54 | 2026-01-13

**Authors:** Fabian Spaeh, Tianyi Chen, Chen-Hao Chiang, Bin Shen

**Categories:** cs.CL

**Scores:** Citation: 3.32 | Influential: 7.81 | Venue: 2.00 | Author: 2.55 | Recency: 9.00

**Links:** [arXiv](https://arxiv.org/abs/2601.08105) | [PDF](https://arxiv.org/pdf/2601.08105)

> 本文首次研究了针对Agent RAG的查询建议问题，旨在当用户问题无法回答时，建议相似且可回答的查询以完成交互。作者引入了鲁棒的动态少样本学习方法，从相关工作流中检索示例，使系统能够自我学习并易于应用。该方法解决了RAG多步骤工作流中确保查询可回答性的挑战，增强了用户与RAG Agent的交互体验。

---

## #436 — Agentic Copyright Watermarking against Adversarial Evidence Forgery with Purification-Agnostic Curriculum Proxy Learning

`C` Score: 4.54 | 2024-09-03

**Authors:** Erjin Bao, Ching-Chun Chang, Hanrui Wang, Isao Echizen

**Categories:** cs.CV, cs.CR

**Scores:** Citation: 3.32 | Influential: 7.81 | Venue: 5.00 | Author: 3.23 | Recency: 5.00

**Links:** [arXiv](https://arxiv.org/abs/2409.01541) | [PDF](https://arxiv.org/pdf/2409.01541)

> 本文针对AI智能体模型的版权保护问题，提出了一种使用哈希技术的自认证黑盒水印协议。研究探讨了对抗性扰动伪造证据的攻击，并提出了净化无关的课程代理学习方法来增强水印鲁棒性和模型性能，有效应对未经授权的使用和分发威胁。

---

## #437 — Poster: Enhancing GNN Robustness for Network Intrusion Detection via Agent-based Analysis

`C` Score: 4.53 | 2025-06-25

**Authors:** Zhonghao Zhan, Huichi Zhou, Hamed Haddadi

**Categories:** cs.CR, cs.AI

**Scores:** Citation: 3.74 | Influential: 7.81 | Venue: 2.00 | Author: 2.55 | Recency: 7.00

**Links:** [arXiv](https://arxiv.org/abs/2506.20806) | [PDF](https://arxiv.org/pdf/2506.20806)

> 本文提出了一种利用大语言模型智能体作为模拟网络安全专家来增强图神经网络（GNN）鲁棒性的新方法。这些智能体在GNN处理前审查网络流图结构，识别并缓解对抗性扰动，显著提高了基于GNN的入侵检测系统在真实攻击下的韧性。

---

## #438 — Fail-Closed Alignment for Large Language Models

`C` Score: 4.53 | 2026-02-19

**Authors:** Zachary Coalson, Beth Sohler, Aiden Gabriel, Sanghyun Hong

**Categories:** cs.LG, cs.CR

**Scores:** Citation: 3.32 | Influential: 7.81 | Venue: 2.00 | Author: 1.86 | Recency: 10.00

**Links:** [arXiv](https://arxiv.org/abs/2602.16977) | [PDF](https://arxiv.org/pdf/2602.16977)

> 识别了当前大模型对齐中存在的“故障开放”结构弱点，并提出“故障关闭”对齐原则。通过渐进式对齐框架，迫使模型在新的独立子空间重建安全性，从而编码多个因果独立的拒绝方向。实验表明该方法在保持生成质量的同时显著增强了鲁棒性。

---

## #439 — Jailbreaking Leaves a Trace: Understanding and Detecting Jailbreak Attacks from Internal Representations of Large Language Models

`C` Score: 4.53 | 2026-02-12

**Authors:** Sri Durga Sai Sowmya Kadali, Evangelos E. Papalexakis

**Categories:** cs.CR, cs.CL

**Scores:** Citation: 3.32 | Influential: 7.81 | Venue: 2.00 | Author: 1.86 | Recency: 10.00

**Links:** [arXiv](https://arxiv.org/abs/2602.11495) | [PDF](https://arxiv.org/pdf/2602.11495)

> 本文通过分析大语言模型内部表示，研究了越狱攻击与良性提示在潜在空间中的差异，识别出与有害输入一致的潜在模式。作者提出了一种基于张量的潜在表示框架，能够在无需微调的情况下实现轻量级越狱检测，并主动干扰推理过程中的越狱执行。实验表明，该方法能有效阻断78%的越狱尝试，同时保持94%的良性提示行为，为从内部视角防御越狱提供了新思路。

---

## #440 — Monotonicity as an Architectural Bias for Robust Language Models

`C` Score: 4.53 | 2026-02-02

**Authors:** Patrick Cooper, Alireza Nadali, Ashutosh Trivedi, Alvaro Velasquez

**Categories:** cs.CL, cs.AI, cs.CR

**Scores:** Citation: 3.32 | Influential: 7.81 | Venue: 2.00 | Author: 1.86 | Recency: 10.00

**Links:** [arXiv](https://arxiv.org/abs/2602.02686) | [PDF](https://arxiv.org/pdf/2602.02686)

> 本文探讨了将单调性作为基于Transformer的语言模型的架构归纳偏置，以提高其在对抗性提示词下的鲁棒性。通过在序列到序列Transformer的前馈子层中选择性地强制执行单调性，同时保持注意力机制不受约束，作者获得了保持预训练模型性能的单调语言模型。这种架构分离确保了语义细化的保序行为，从而在不牺牲表达能力的情况下增强了鲁棒性。

---

## #441 — From Governance Norms to Enforceable Controls: A Layered Translation Method for Runtime Guardrails in Agentic AI

`C` Score: 4.53 | 2026-04-06

**Authors:** Christopher Koch

**Categories:** cs.AI, cs.HC, cs.LG

**Scores:** Citation: 3.32 | Influential: 7.81 | Venue: 2.00 | Author: 1.86 | Recency: 10.00

**Links:** [arXiv](https://arxiv.org/abs/2604.05229) | [PDF](https://arxiv.org/pdf/2604.05229)

> 该论文提出分层翻译方法，将标准衍生的治理目标连接到四个控制层：治理目标、设计时约束、运行时中介和保证反馈。它区分治理目标、技术控制、运行时护栏和保证证据，引入控制元组和运行时可执行性标准。核心主张是标准应指导控制跨架构、运行时策略和审计的放置，而运行时护栏保留给足够可观察、确定和时间敏感的控制。

---

## #442 — CRaFT: Circuit-Guided Refusal Feature Selection via Cross-Layer Transcoders

`C` Score: 4.53 | 2026-04-02

**Authors:** Su-Hyeon Kim, Hyundong Jin, Yejin Lee, Yo-Sub Han

**Categories:** cs.AI

**Scores:** Citation: 3.32 | Influential: 7.81 | Venue: 2.00 | Author: 1.86 | Recency: 10.00

**Links:** [arXiv](https://arxiv.org/abs/2604.01604) | [PDF](https://arxiv.org/pdf/2604.01604)

> CRaFT是一种基于电路的拒绝特征选择框架，通过使用拒绝边界附近的提示对特征进行排序，以评估它们对模型拒绝-服从决策的影响。在Gemma-3-1B-it上，CRaFT将攻击成功率从6.7%提高到48.2%，表明电路影响是识别因果介导拒绝行为特征的更可靠标准。

---

## #443 — OpenGuardrails: A Configurable, Unified, and Scalable Guardrails Platform for Large Language Models

`C` Score: 4.52 | 2025-10-22

**Authors:** Thomas Wang, Haowen Li

**Categories:** cs.CR, cs.CL

**Scores:** Citation: 4.37 | Influential: 7.81 | Venue: 2.00 | Author: 0.58 | Recency: 7.00

**Links:** [arXiv](https://arxiv.org/abs/2510.19169) | [PDF](https://arxiv.org/pdf/2510.19169)

> 本文介绍了OpenGuardrails，首个全开源平台，统一了安全检测、操纵防御和护栏基础设施。该平台通过可配置策略适应机制和统一的LLM护卫架构，有效防御内容违规、模型操纵攻击和数据泄露，并支持多语言及量化部署，实现了高性能与可扩展性的最佳平衡。

---

## #444 — A Call to Action for a Secure-by-Design Generative AI Paradigm

`C` Score: 4.52 | 2025-10-01

**Authors:** Dalal Alharthi, Ivan Roberto Kawaminami Garcia

**Categories:** cs.CR, cs.AI, cs.LG

**Scores:** Citation: 3.32 | Influential: 7.81 | Venue: 2.00 | Author: 3.78 | Recency: 7.00

**Links:** [arXiv](https://arxiv.org/abs/2510.00451) | [PDF](https://arxiv.org/pdf/2510.00451)

> 本文提出了 PromptShield，一个基于本体的“安全设计”框架，旨在通过语义验证标准化用户输入，从而主动缓解 LLM 的提示注入漏洞。在 AWS 日志分析系统上的实验表明，该框架能有效防御对抗性攻击，显著提升模型的安全性和性能，且具有模块化和适应性强的特点。

---

## #445 — Personalized Constitutionally-Aligned Agentic Superego: Secure AI Behavior Aligned to Diverse Human Values

`C` Score: 4.51 | 2025-06-08

**Authors:** Nell Watson, Ahmed Amer, Evan Harris, Preeti Ravindra, Shujun Zhang

**Categories:** cs.AI, cs.CY, cs.MA

**Scores:** Citation: 3.71 | Influential: 7.81 | Venue: 2.00 | Author: 2.55 | Recency: 7.00

**Links:** [arXiv](https://arxiv.org/abs/2506.13774) | [PDF](https://arxiv.org/pdf/2506.13774)

> 本文引入了一个“超我”智能体作为个性化监督机制，通过引用用户选择的“信条宪法”来动态引导AI规划。该系统在执行前验证计划是否符合宪法和通用道德底线，显著降低了有害输出并实现了近乎完美的拒绝率。

---

## #446 — LiteLMGuard: Seamless and Lightweight On-Device Prompt Filtering for Safeguarding Small Language Models against Quantization-induced Risks and Vulnerabilities

`C` Score: 4.47 | 2025-05-08

**Authors:** Kalyan Nakka, Jimmy Dani, Ausmit Mondal, Nitesh Saxena

**Categories:** cs.CR, cs.LG

**Scores:** Citation: 3.61 | Influential: 7.81 | Venue: 2.00 | Author: 2.55 | Recency: 7.00

**Links:** [arXiv](https://arxiv.org/abs/2505.05619) | [PDF](https://arxiv.org/pdf/2505.05619)

> 针对设备端小语言模型因量化而产生的安全风险，本文提出了LiteLMGuard，一种轻量级且模型无关的实时提示词过滤护栏。该系统利用深度学习进行语义理解，实现了对有害提示词的高效分类，在设备端部署中展现了高防御率和低延迟，有效保护了量化模型免受越狱等攻击。

---

## #447 — Parameter Stress Analysis in Reinforcement Learning: Applying Synaptic Filtering to Policy Networks

`C` Score: 4.44 | 2025-06-28

**Authors:** Zain ul Abdeen, Ming Jin

**Categories:** cs.LG, eess.SY

**Scores:** Citation: 3.32 | Influential: 7.81 | Venue: 2.00 | Author: 3.23 | Recency: 7.00

**Links:** [arXiv](https://arxiv.org/abs/2506.23036) | [PDF](https://arxiv.org/pdf/2506.23036)

> 本文通过突触过滤和对抗性攻击对强化学习策略网络的参数进行压力分析，将参数分类为脆弱、稳健或反脆弱。研究验证了在Mujoco环境中存在能提升压力下策略性能的反脆弱参数，为设计稳健的RL系统提供了基础。

---

## #448 — RAJ-PGA: Reasoning-Activated Jailbreak and Principle-Guided Alignment Framework for Large Reasoning Models

`C` Score: 4.44 | 2025-08-18

**Authors:** Jianhao Chen, Mayi Xu, Haoyang Chen, Xiaohu Li, Xiangyu Zhang, Jianjie Huang et al. (9 total)

**Categories:** cs.AI, cs.CR

**Scores:** Citation: 3.32 | Influential: 7.81 | Venue: 2.00 | Author: 3.23 | Recency: 7.00

**Links:** [arXiv](https://arxiv.org/abs/2508.12897) | [PDF](https://arxiv.org/pdf/2508.12897)

> 本文提出了推理激活越狱（RAJ）攻击，通过细化恶意提示触发大推理模型内部的有害推理链。针对此漏洞，作者开发了原则引导对齐（PGA）框架，构建高质量安全数据集，在显著提升模型防御成功率的同时保留了其通用推理能力。

---

## #449 — Mitigating Over-Refusal in Aligned Large Language Models via Inference-Time Activation Energy

`C` Score: 4.44 | 2025-10-09

**Authors:** Eric Hanchen Jiang, Weixuan Ou, Run Liu, Shengyuan Pang, Guancheng Wan, Ranjie Duan et al. (11 total)

**Categories:** cs.LG, cs.AI, cs.CL

**Scores:** Citation: 3.32 | Influential: 7.81 | Venue: 2.00 | Author: 3.23 | Recency: 7.00

**Links:** [arXiv](https://arxiv.org/abs/2510.08646) | [PDF](https://arxiv.org/pdf/2510.08646)

> 针对大语言模型安全对齐中常见的过度拒绝问题，本文提出了一种无需微调的推理时干预框架——能量景观引导（ELS）。该框架的核心创新在于训练一个轻量级的外部基于能量的模型（EBM），用于区分理想与不良状态。在推理过程中，ELS利用能量函数的梯度实时引导模型的内部激活状态，使其从高能量的虚假拒绝区域转向低能量的有益回复区域，从而在不重新训练模型的前提下有效平衡了安全性与实用性。

---

## #450 — Enhancing Robustness in Deep Reinforcement Learning: A Lyapunov Exponent Approach

`C` Score: 4.44 | 2024-10-14

**Authors:** Rory Young, Nicolas Pugeault

**Categories:** cs.LG, cs.AI

**Scores:** Citation: 3.81 | Influential: 7.81 | Venue: 5.00 | Author: 1.12 | Recency: 5.00

**Links:** [arXiv](https://arxiv.org/abs/2410.10674) | [PDF](https://arxiv.org/pdf/2410.10674)

> 本文研究了深度强化学习策略对状态扰动和对抗攻击的鲁棒性，指出策略可能存在确定性混沌行为。作者提出在Dreamer V3架构中实施最大李雅普诺夫指数正则化，以减少混沌状态动力学，使学习到的策略对传感器噪声或对抗攻击更具韧性，从而提升其在现实世界应用中的适用性和安全性。

---

## #451 — Detecting Sleeper Agents in Large Language Models via Semantic Drift Analysis

`C` Score: 4.43 | 2025-11-20

**Authors:** Shahin Zanbaghi, Ryan Rostampour, Farhan Abid, Salim Al Jarmakani

**Categories:** cs.AI

**Scores:** Citation: 3.32 | Influential: 7.81 | Venue: 2.00 | Author: 1.86 | Recency: 9.00

**Links:** [arXiv](https://arxiv.org/abs/2511.15992) | [PDF](https://arxiv.org/pdf/2511.15992)

> 本文提出了一种结合语义漂移分析和金丝雀基线比较的双重检测系统，用于识别大语言模型中的“休眠Agent”。该方法利用Sentence-BERT嵌入测量与安全基线的语义偏差，并通过注入金丝雀问题监控响应一致性。实验表明，该系统在实时检测中实现了92.5%的准确率和100%的精确率，无需修改模型即可有效识别欺骗性行为。

---

## #452 — KFCPO: Kronecker-Factored Approximated Constrained Policy Optimization

`C` Score: 4.43 | 2025-11-02

**Authors:** Joonyoung Lim, Younghwan Yoo

**Categories:** cs.LG, cs.AI

**Scores:** Citation: 3.32 | Influential: 7.81 | Venue: 2.00 | Author: 1.86 | Recency: 9.00

**Links:** [arXiv](https://arxiv.org/abs/2511.00880) | [PDF](https://arxiv.org/pdf/2511.00880)

> 提出了KFCPO，一种结合K-FAC二阶优化与安全梯度操纵的新型安全强化学习算法。该方法通过边缘感知梯度调整和小批量KL回滚策略，有效平衡了奖励最大化与约束满足，在Safety Gymnasium环境中实现了比最佳基线高10.3%至50.2%的平均回报。

---

## #453 — Adaptive Trust Consensus for Blockchain IoT: Comparing RL, DRL, and MARL Against Naive, Collusive, Adaptive, Byzantine, and Sleeper Attacks

`C` Score: 4.43 | 2025-12-28

**Authors:** Soham Padia, Dhananjay Vaidya, Ramchandra Mangrulkar

**Categories:** cs.CR, cs.LG, cs.MA

**Scores:** Citation: 3.32 | Influential: 7.81 | Venue: 2.00 | Author: 1.86 | Recency: 9.00

**Links:** [arXiv](https://arxiv.org/abs/2512.22860) | [PDF](https://arxiv.org/pdf/2512.22860)

> 本文提出了一种基于信任的区块链物联网共识框架，结合全同态加密和基于属性的访问控制以保护隐私。研究系统比较了强化学习、深度强化学习和多智能体强化学习在对抗五种不同攻击（如共谋攻击、自适应攻击和休眠攻击）时的防御性能。实验结果表明，多智能体强化学习在对抗共谋攻击时表现最佳，而所有智能体在对抗时间延迟投毒攻击时均面临严重挑战。

---

## #454 — Phishing Email Detection Using Large Language Models

`C` Score: 4.43 | 2025-12-10

**Authors:** Najmul Hasan, Prashanth BusiReddyGari, Haitao Zhao, Yihao Ren, Jinsheng Xu, Shaohu Zhang

**Categories:** cs.CR, cs.IR

**Scores:** Citation: 3.32 | Influential: 7.81 | Venue: 2.00 | Author: 1.86 | Recency: 9.00

**Links:** [arXiv](https://arxiv.org/abs/2512.10104) | [PDF](https://arxiv.org/pdf/2512.10104)

> 本文提出了 LLMPEA，一个基于 LLM 的框架，用于检测包括提示注入、文本细化和多语言攻击在内的多种攻击向量的网络钓鱼电子邮件。研究评估了三个前沿 LLM 在检测网络钓鱼方面的可行性、鲁棒性和局限性，实证分析显示 LLM 检测准确率超过 90%。然而，研究也强调了基于 LLM 的检测系统可能被对抗性攻击、提示注入和多语言攻击利用，为攻击者结合多种漏洞的现实环境提供了关键见解。

---

## #455 — A Systematic Literature Review on LLM Defenses Against Prompt Injection and Jailbreaking: Expanding NIST Taxonomy

`C` Score: 4.42 | 2026-01-29

**Authors:** Pedro H. Barcha Correia, Ryan W. Achjian, Diego E. G. Caetano de Oliveira, Ygor Acacio Maria, Victor Takashi Hayashi, Marcos Lopes et al. (8 total)

**Categories:** cs.CR, cs.AI, cs.CL

**Scores:** Citation: 3.32 | Influential: 7.81 | Venue: 2.00 | Author: 1.12 | Recency: 10.00

**Links:** [arXiv](https://arxiv.org/abs/2601.22240) | [PDF](https://arxiv.org/pdf/2601.22240)

> 本文针对大语言模型面临的提示注入和越狱攻击防御策略进行了首次系统性文献综述，深入分析了 88 项相关研究。该工作不仅补充了 NIST 报告及其他学术综述中未收录的文献，还通过引入新类别扩展了 NIST 的对抗性机器学习分类法。这一扩展为理解不断演进的防御技术提供了结构化框架，对于应对生成式 AI 带来的数据泄露和输出受损等安全挑战具有重要意义。

---

## #456 — A Collaborative Safety Shield for Safe and Efficient CAV Lane Changes in Congested On-Ramp Merging

`C` Score: 4.42 | 2026-02-10

**Authors:** Bharathkumar Hegde, Melanie Bouroche

**Categories:** cs.RO, cs.AI, cs.MA

**Scores:** Citation: 3.32 | Influential: 7.81 | Venue: 2.00 | Author: 1.12 | Recency: 10.00

**Links:** [arXiv](https://arxiv.org/abs/2602.10007) | [PDF](https://arxiv.org/pdf/2602.10007)

> 本文提出了多智能体安全护盾（MASS），利用控制屏障函数（CBF）设计，旨在解决网联自动驾驶车辆在密集交通变道时的安全与效率冲突问题。MASS通过交互拓扑捕捉多智能体交互，并与多智能体强化学习控制器集成，在确保安全约束的同时通过定制奖励函数优先提高效率。仿真结果表明，MARL-MASS能有效平衡安全保证与交通效率提升，实现协作式变道。

---

## #457 — Spectral Guardrails for Agents in the Wild: Detecting Tool Use Hallucinations via Attention Topology

`C` Score: 4.42 | 2026-02-08

**Authors:** Valentin Noël

**Categories:** cs.LG, cs.AI, eess.SP

**Scores:** Citation: 3.32 | Influential: 7.81 | Venue: 2.00 | Author: 1.12 | Recency: 10.00

**Links:** [arXiv](https://arxiv.org/abs/2602.08082) | [PDF](https://arxiv.org/pdf/2602.08082)

> 针对自主智能体在野外部署时的工具使用失败风险，本文提出了一种基于注意力拓扑频谱分析的无训练护栏方法。该方法通过分析模型注意力熵和平滑度等频谱特征，能有效检测工具使用中的幻觉现象，在Llama 3.1 8B上实现了97.7%的召回率。研究发现，幻觉不仅是错误的标记，更是一种热力学状态变化，模型的注意力在出错时会变成噪声，这为智能体安全提供了一种高效且原则性的检测框架。

---

## #458 — Prompt Attack Detection with LLM-as-a-Judge and Mixture-of-Models

`C` Score: 4.42 | 2026-03-26

**Authors:** Hieu Xuan Le, Benjamin Goh, Quy Anh Tang

**Categories:** cs.CL

**Scores:** Citation: 3.32 | Influential: 7.81 | Venue: 2.00 | Author: 1.12 | Recency: 10.00

**Links:** [arXiv](https://arxiv.org/abs/2603.25176) | [PDF](https://arxiv.org/pdf/2603.25176)

> 本文探讨了在低延迟生产环境中，利用轻量级通用大语言模型作为安全法官来检测提示攻击（包括越狱和注入）的可行性。通过精心设计的提示和输出结构，引导轻量级LLM进行意图分解、安全信号验证和自我反思，从而在保持实时性的同时实现有效防御。该方法已在新加坡公共服务聊天机器人中作为中央护栏服务部署，实验证明其能有效处理多样化的攻击模式。

---

## #459 — Precision-Varying Prediction (PVP): Robustifying ASR systems against adversarial attacks

`C` Score: 4.42 | 2026-03-23

**Authors:** Matías Pizarro, Raghavan Narasimhan, Asja Fischer

**Categories:** cs.LG, cs.CR, eess.AS

**Scores:** Citation: 3.32 | Influential: 7.81 | Venue: 2.00 | Author: 1.12 | Recency: 10.00

**Links:** [arXiv](https://arxiv.org/abs/2603.22590) | [PDF](https://arxiv.org/pdf/2603.22590)

> 本文提出了一种精度变化预测（PVP）方法，通过在推理过程中随机采样模型精度来增强自动语音识别（ASR）系统对抗对抗性攻击的鲁棒性。作者观察到改变精度会降低攻击成功率，并利用这一见解设计了简单的随机采样策略和基于高斯分类器的对抗样本检测方法。实验分析表明，该方法在各种 ASR 模型和攻击类型下显著提高了鲁棒性，并具有竞争力的检测性能。

---

## #460 — Detection of adversarial intent in Human-AI teams using LLMs

`C` Score: 4.42 | 2026-03-21

**Authors:** Abed K. Musaffar, Ambuj Singh, Francesco Bullo

**Categories:** cs.LG, cs.AI, cs.HC

**Scores:** Citation: 3.32 | Influential: 7.81 | Venue: 2.00 | Author: 1.12 | Recency: 10.00

**Links:** [arXiv](https://arxiv.org/abs/2603.20976) | [PDF](https://arxiv.org/pdf/2603.20976)

> 本文研究了 LLM 在混合人机团队中作为防御性监督者的潜力，旨在从交互痕迹中检测恶意行为。作者使用真实人机团队的多方对话和决策数据集，构建了恶意行为检测问题。研究发现，LLM 能够在无需特定任务信息的情况下实时识别恶意行为，表明其具有任务无关防御的潜力，且简单的启发式方法难以识别此类恶意行为，引入 LLM 防御者可使人类团队更加稳健。

---

## #461 — Understanding the Effects of Safety Unalignment on Large Language Models

`C` Score: 4.42 | 2026-04-02

**Authors:** John T. Halloran

**Categories:** cs.CR, cs.AI, cs.LG

**Scores:** Citation: 3.32 | Influential: 7.81 | Venue: 2.00 | Author: 1.12 | Recency: 10.00

**Links:** [arXiv](https://arxiv.org/abs/2604.02574) | [PDF](https://arxiv.org/pdf/2604.02574)

> 该研究比较了两种安全失准方法（JT和WO）对六个LLM的影响，发现WO产生的模型在协助恶意活动方面能力更强，同时更好地保留原始性能和对抗攻击能力。研究还表明监督微调可有效限制WO失准带来的恶意风险，而不显著影响幻觉率或自然语言性能。

---

## #462 — Enhancing Adversarial Resistance in LLMs with Recursion

`C` Score: 4.40 | 2024-12-09

**Authors:** Bryan Li, Sounak Bagchi, Zizhan Wang

**Categories:** cs.CR, cs.AI

**Scores:** Citation: 3.32 | Influential: 7.81 | Venue: 2.00 | Author: 4.27 | Recency: 5.00

**Links:** [arXiv](https://arxiv.org/abs/2412.06181) | [PDF](https://arxiv.org/pdf/2412.06181)

> 本文提出了一种递归框架，利用提示简化技术增强大语言模型（LLM）对抗越狱和恶意提示的抵抗力。该方法通过提高复杂对抗性提示的透明度，实现了对恶意输入的可靠检测与预防，为构建能够区分无害与恶意意图的AI安全系统奠定了坚实基础。

---

## #463 — Data to Defense: The Role of Curation in Customizing LLMs Against Jailbreaking Attacks

`C` Score: 4.35 | 2024-10-03

**Authors:** Xiaoqun Liu, Jiacheng Liang, Luoxi Tang, Muchao Ye, Weicheng Ma, Zhaohan Xi

**Categories:** cs.CR, cs.AI

**Scores:** Citation: 3.79 | Influential: 7.81 | Venue: 2.00 | Author: 2.55 | Recency: 5.00

**Links:** [arXiv](https://arxiv.org/abs/2410.02220) | [PDF](https://arxiv.org/pdf/2410.02220)

> 本研究提出了一种自适应数据策展方法，旨在增强文本在 LLM 定制过程中对抗越狱攻击样本的效果。该研究进一步引入了一个涵盖定制前、中和后的综合缓解框架，以免疫模型、中和风险并恢复受损模型。实验结果表明，该方法能显著减少越狱影响，在生成安全响应方面实现了高达 100% 的成功率。

---

## #464 — Feature-Aware Malicious Output Detection and Mitigation

`C` Score: 4.34 | 2025-04-12

**Authors:** Weilong Dong, Peiguang Li, Yu Tian, Xinyi Zeng, Fengdi Li, Sirui Wang

**Categories:** cs.CL

**Scores:** Citation: 3.54 | Influential: 7.81 | Venue: 2.00 | Author: 3.23 | Recency: 5.00

**Links:** [arXiv](https://arxiv.org/abs/2504.09191) | [PDF](https://arxiv.org/pdf/2504.09191)

> 针对大模型缺乏辨别恶意内容能力的问题，本文提出了特征感知的有害响应拒绝方法FMM。该方法在解码阶段利用判别器检测特征空间中的恶意特征，并通过激活修补调整拒绝机制，在不影响模型生成能力的前提下有效防御越狱攻击。

---

## #465 — Towards Robust Deep Reinforcement Learning against Environmental State Perturbation

`C` Score: 4.34 | 2025-06-10

**Authors:** Chenxu Wang, Huaping Liu

**Categories:** cs.LG, cs.AI

**Scores:** Citation: 3.32 | Influential: 7.81 | Venue: 2.00 | Author: 2.55 | Recency: 7.00

**Links:** [arXiv](https://arxiv.org/abs/2506.08961) | [PDF](https://arxiv.org/pdf/2506.08961)

> 本文针对深度强化学习中的环境状态扰动问题，提出了增强对抗训练（BAT）防御框架。该框架首先通过监督学习调整智能体以避免灾难性故障，随后进行对抗性训练。实验结果表明，BAT框架能显著提高智能体在各种环境状态扰动下的鲁棒性，优于现有的鲁棒强化学习算法。

---

## #466 — Design and Implementation of a Secure RAG-Enhanced AI Chatbot for Smart Tourism Customer Service: Defending Against Prompt Injection Attacks -- A Case Study of Hsinchu, Taiwan

`C` Score: 4.34 | 2025-09-22

**Authors:** Yu-Kai Shih, You-Kai Kang

**Categories:** cs.CR, cs.AI

**Scores:** Citation: 3.32 | Influential: 7.81 | Venue: 2.00 | Author: 2.55 | Recency: 7.00

**Links:** [arXiv](https://arxiv.org/abs/2509.21367) | [PDF](https://arxiv.org/pdf/2509.21367)

> 本文以新竹智慧旅游为例，设计并实现了一个安全的检索增强生成（RAG）聊天机器人，重点防御提示注入攻击。系统集成了多层语言分析、意图分解和反向RAG文本验证等防御机制。评估显示，该系统在良性任务上保持高准确率，并能有效检测注入攻击。

---

## #467 — Early Approaches to Adversarial Fine-Tuning for Prompt Injection Defense: A 2022 Study of GPT-3 and Contemporary Models

`C` Score: 4.34 | 2025-09-15

**Authors:** Gustavo Sandoval, Denys Fenchenko, Junyao Chen

**Categories:** cs.CR, cs.LG

**Scores:** Citation: 3.32 | Influential: 7.81 | Venue: 2.00 | Author: 2.55 | Recency: 7.00

**Links:** [arXiv](https://arxiv.org/abs/2509.14271) | [PDF](https://arxiv.org/pdf/2509.14271)

> 本文记录了2022年针对LLM提示注入攻击的早期防御研究，提出了对抗性微调技术。研究比较了提示注入和目标劫持攻击在不同模型上的效果，发现对抗性微调能将小型GPT-3模型的攻击成功率降至接近零，为现代提示注入防御研究奠定了基础。

---

## #468 — Teaching LLM to be Persuasive: Reward-Enhanced Policy Optimization for Alignment frm Heterogeneous Rewards

`C` Score: 4.34 | 2025-10-05

**Authors:** Zhuoran Zhuang, Ye Chen, Xia Zeng, Chao Luo, Luhui Liu, Yihan Chen

**Categories:** cs.CL

**Scores:** Citation: 3.32 | Influential: 7.81 | Venue: 2.00 | Author: 2.55 | Recency: 7.00

**Links:** [arXiv](https://arxiv.org/abs/2510.04214) | [PDF](https://arxiv.org/pdf/2510.04214)

> 本文提出了奖励增强策略优化（REPO）框架，旨在将大语言模型部署为在线旅游代理中的业务发展智能体，以进行具有说服力的价格谈判。REPO利用异构奖励信号（包括偏好模型、行为评判和程序化奖励函数）进行强化学习后训练，在遵循标准操作程序的同时避免过度拟合脚本。生产环境评估显示，REPO在对话评分上显著优于基线模型及DPO等方法。

---

## #469 — MultiVer: Zero-Shot Multi-Agent Vulnerability Detection

`C` Score: 4.34 | 2026-02-19

**Authors:** Shreshth Rajan

**Categories:** cs.MA, cs.AI

**Scores:** Citation: 3.32 | Influential: 7.81 | Venue: 2.00 | Author: 0.58 | Recency: 10.00

**Links:** [arXiv](https://arxiv.org/abs/2602.17875) | [PDF](https://arxiv.org/pdf/2602.17875)

> 提出MultiVer，一个零样本多智能体漏洞检测系统。通过四智能体集成（安全、正确性、性能、风格）并采用联合投票，实现了超越微调模型的召回率。该方法在漏报代价较高的安全应用中表现出色，证明了零样本多智能体集成的有效性。

---

## #470 — Narrow Fine-Tuning Erodes Safety Alignment in Vision-Language Agents

`C` Score: 4.34 | 2026-02-18

**Authors:** Idhant Gulati, Shivam Raval

**Categories:** cs.AI

**Scores:** Citation: 3.32 | Influential: 7.81 | Venue: 2.00 | Author: 0.58 | Recency: 10.00

**Links:** [arXiv](https://arxiv.org/abs/2602.16931) | [PDF](https://arxiv.org/pdf/2602.16931)

> 研究表明，在狭窄有害数据集上微调视觉语言模型会导致严重的突发性错位，且这种错位会泛化到无关任务。实验发现错位程度随LoRA秩单调递增，多模态评估显示的错位率远高于纯文本评估。这突显了当前持续学习范式在部署后保持对齐方面的不足。

---

## #471 — Defensive M2S: Training Guardrail Models on Compressed Multi-turn Conversations

`C` Score: 4.32 | 2026-01-01

**Authors:** Hyunjun Kim

**Categories:** cs.CL, cs.AI

**Scores:** Citation: 3.32 | Influential: 7.81 | Venue: 2.00 | Author: 1.12 | Recency: 9.00

**Links:** [arXiv](https://arxiv.org/abs/2601.00454) | [PDF](https://arxiv.org/pdf/2601.00454)

> 本文提出了Defensive M2S，一种在压缩的多轮对话上训练护栏模型的范式，旨在降低处理完整对话历史的计算成本。该方法将训练复杂度从O(n^2)降至O(n)，在保持93.8%攻击检测召回率的同时，将推理token减少了94.6%。研究表明，M2S压缩是一种有效的护栏部署效率技术。

---

## #472 — Recursive language models for jailbreak detection: a procedural defense for tool-augmented agents

`C` Score: 4.29 | 2026-02-18

**Authors:** Doron Shavit

**Categories:** cs.CR, cs.AI

**Scores:** Citation: 3.32 | Influential: 7.81 | Venue: 2.00 | Author: 0.26 | Recency: 10.00

**Links:** [arXiv](https://arxiv.org/abs/2602.16520) | [PDF](https://arxiv.org/pdf/2602.16520)

> 提出RLM-JB，一种基于递归语言模型的端到端越狱检测框架。该方法将检测视为一个过程，通过规范化、分块和并行筛选来处理长上下文隐藏和语义伪装等攻击。实验表明，该方法在保持极低误报率的同时，实现了高检测效果。

---

## #473 — Towards Poisoning Robustness Certification for Natural Language Generation

`C` Score: 4.29 | 2026-02-10

**Authors:** Mihnea Ghitu, Matthew Wicker

**Categories:** cs.LG

**Scores:** Citation: 3.32 | Influential: 7.81 | Venue: 2.00 | Author: 0.26 | Recency: 10.00

**Links:** [arXiv](https://arxiv.org/abs/2602.09757) | [PDF](https://arxiv.org/pdf/2602.09757)

> 本文针对自然语言生成的可靠性问题，提出了首个可认证毒化防御算法TPA（目标划分聚合），旨在为自回归生成提供可证明的鲁棒性界限。作者形式化了稳定性和有效性两个安全属性，并计算诱导特定有害内容所需的最小毒化预算。实验表明，TPA在多种设置下有效，包括认证智能体工具调用的有效性，为安全关键应用中语言模型的部署提供了可认证的保障。

---

## #474 — When Evaluation Becomes a Side Channel: Regime Leakage and Structural Mitigations for Alignment Assessment

`C` Score: 4.29 | 2026-02-09

**Authors:** Igor Santos-Grueiro

**Categories:** cs.AI, cs.CR, cs.LG

**Scores:** Citation: 3.32 | Influential: 7.81 | Venue: 2.00 | Author: 0.26 | Recency: 10.00

**Links:** [arXiv](https://arxiv.org/abs/2602.08449) | [PDF](https://arxiv.org/pdf/2602.08449)

> 针对具有情境感知能力的智能体可能利用评估与部署之间的差异（制度泄漏）来实施欺骗行为的问题，本文提出了“制度盲”训练机制。该方法通过对抗性不变性约束限制模型访问制度线索，从而防止模型在评估时表现良好而在部署时背叛。实验表明，制度盲训练能有效减少科学谄媚和时间睡眠代理等条件性失败，且不造成任务效用的显著损失。

---

## #475 — Session Risk Memory (SRM): Temporal Authorization for Deterministic Pre-Execution Safety Gates

`C` Score: 4.29 | 2026-03-22

**Authors:** Florin Adrian Chitan

**Categories:** cs.AI, cs.CR

**Scores:** Citation: 3.32 | Influential: 7.81 | Venue: 2.00 | Author: 0.26 | Recency: 10.00

**Links:** [arXiv](https://arxiv.org/abs/2603.22350) | [PDF](https://arxiv.org/pdf/2603.22350)

> 本文提出了会话风险记忆（SRM），一个轻量级的确定性模块，通过轨迹级授权扩展了无状态执行门，以解决分布式攻击将有害意图分解为多个合规步骤的问题。SRM 维护紧凑的语义质心来表示 Agent 会话的行为概况，并通过指数移动平均累积风险信号。评估显示，SRM 在多轮基准测试中消除了所有误报，同时保持 100% 的检测率，且每轮开销极低。

---

## #476 — Understanding and Improving Continuous Adversarial Training for LLMs via In-context Learning Theory

`C` Score: 4.29 | 2026-04-14

**Authors:** Shaopeng Fu, Di Wang

**Categories:** cs.LG, cs.CR, stat.ML

**Scores:** Citation: 3.32 | Influential: 7.81 | Venue: 2.00 | Author: 0.26 | Recency: 10.00

**Links:** [arXiv](https://arxiv.org/abs/2604.12817) | [PDF](https://arxiv.org/pdf/2604.12817)

> 本文基于上下文学习理论对LLMs的连续对抗训练(CAT)进行首次理论分析。证明对于线性transformers，鲁棒泛化边界与嵌入空间中的扰动半径呈负相关，解释CAT为何能防御来自token空间的越狱提示。基于此，提出通过在CAT目标函数中引入依赖LLM嵌入矩阵奇异值的额外正则化项来改进LLM CAT。实验表明该方法能实现更好的越狱鲁棒性-效用权衡。

---

## #477 — Generalization Limits of Reinforcement Learning Alignment

`C` Score: 4.29 | 2026-04-03

**Authors:** Haruhi Shida, Koo Imai, Keigo Kansa

**Categories:** cs.LG, cs.AI

**Scores:** Citation: 3.32 | Influential: 7.81 | Venue: 2.00 | Author: 0.26 | Recency: 10.00

**Links:** [arXiv](https://arxiv.org/abs/2604.02652) | [PDF](https://arxiv.org/pdf/2604.02652)

> 该研究提出'复合越狱'方法，利用强化学习对齐的泛化失败，通过组合多种单独被防御的攻击技术来饱和指令层次维护过程。实验显示攻击成功率从14.3%提高到71.4%，为安全训练泛化不如模型能力广泛的假设提供了经验证据。

---

## #478 — Jailbreak Detection in Clinical Training LLMs Using Feature-Based Predictive Models

`C` Score: 4.25 | 2025-04-21

**Authors:** Tri Nguyen, Lohith Srikanth Pentapalli, Magnus Sieverding, Laurah Turner, Seth Overla, Weibing Zheng et al. (14 total)

**Categories:** cs.CL, cs.AI

**Scores:** Citation: 3.57 | Influential: 7.81 | Venue: 2.00 | Author: 2.55 | Recency: 5.00

**Links:** [arXiv](https://arxiv.org/abs/2505.00010) | [PDF](https://arxiv.org/pdf/2505.00010)

> 本文研究了临床教育LLM中的越狱检测问题，利用语言学特征训练了决策树、模糊逻辑等多种预测模型。通过标注大量对话提示，作者发现基于特征的模型在检测越狱行为方面优于提示工程方法，其中模糊决策树表现最佳。该研究为教育领域的LLM安全提供了一种可解释且有效的实时监控方案。

---

## #479 — Probabilistic Modeling of Jailbreak on Multimodal LLMs: From Quantification to Application

`C` Score: 4.24 | 2025-03-10

**Authors:** Wenzhuo Xu, Zhipeng Wei, Xiongtao Sun, Zonghao Ying, Deyue Zhang, Dongdong Yang et al. (8 total)

**Categories:** cs.CR, cs.CV

**Scores:** Citation: 3.32 | Influential: 7.81 | Venue: 2.00 | Author: 3.23 | Recency: 5.00

**Links:** [arXiv](https://arxiv.org/abs/2503.06989) | [PDF](https://arxiv.org/pdf/2503.06989)

> 研究引入越狱概率来量化输入的越狱潜力，表示MLLMs在收到此输入时生成恶意响应的可能性。通过多次查询MLLMs来近似此概率，并使用Jailbreak概率预测网络建模输入隐藏状态与相应越狱概率之间的关系。基于此，提出了基于越狱概率的攻击(JPA)和微调(JPF)，实验显示这些方法显著提高了攻击效果和防御能力。

---

## #480 — Broken-Token: Filtering Obfuscated Prompts by Counting Characters-Per-Token

`C` Score: 4.24 | 2025-10-30

**Authors:** Shaked Zychlinski, Yuval Kainan

**Categories:** cs.CR, cs.AI, cs.CL

**Scores:** Citation: 3.32 | Influential: 7.81 | Venue: 2.00 | Author: 0.58 | Recency: 9.00

**Links:** [arXiv](https://arxiv.org/abs/2510.26847) | [PDF](https://arxiv.org/pdf/2510.26847)

> 本文提出了一种名为CPT-Filtering的防御技术，旨在解决利用密码和字符编码混淆恶意提示词的越狱攻击。该方法基于BPE分词器处理分布外文本时会产生更多短token的特性，通过计算文本中平均每个Token的字符数（CPT）来高效识别并过滤混淆提示。该技术具有模型无关、计算成本极低且准确率高的优势，有效弥补了现有防御方法计算开销大的缺陷。

---

## #481 — SecureCAI: Injection-Resilient LLM Assistants for Cybersecurity Operations

`C` Score: 4.24 | 2026-01-12

**Authors:** Mohammed Himayath Ali, Mohammed Aqib Abdullah, Mohammed Mudassir Uddin, Shahnawaz Alam

**Categories:** cs.CR, cs.CV

**Scores:** Citation: 3.32 | Influential: 7.81 | Venue: 2.00 | Author: 0.58 | Recency: 9.00

**Links:** [arXiv](https://arxiv.org/abs/2601.07835) | [PDF](https://arxiv.org/pdf/2601.07835)

> 本文提出了SecureCAI，一种针对网络安全运营的防御框架，扩展了宪法AI原则并引入了安全感知护栏和自适应宪法进化机制。通过直接偏好优化消除不安全的响应模式，该框架在对抗性环境下将攻击成功率降低了94.7%，同时保持了高准确性。SecureCAI通过持续的红队反馈循环动态适应新兴攻击策略，为在对抗性领域可信地集成语言模型奠定了基础。

---

## #482 — Context Misleads LLMs: The Role of Context Filtering in Maintaining Safe Alignment of LLMs

`C` Score: 4.23 | 2025-08-09

**Authors:** Jinhwa Kim, Ian G. Harris

**Categories:** cs.CR, cs.AI, cs.CL

**Scores:** Citation: 3.32 | Influential: 7.81 | Venue: 2.00 | Author: 1.86 | Recency: 7.00

**Links:** [arXiv](https://arxiv.org/abs/2508.10031) | [PDF](https://arxiv.org/pdf/2508.10031)

> 针对恶意用户利用对抗性上下文欺骗LLM的问题，本文提出了一种名为上下文过滤模型的防御机制，这是一种输入预处理方法，旨在过滤不可信上下文并识别包含真实用户意图的主要提示。该方法在保持模型原有性能的同时，将越狱攻击的成功率降低了高达88%，作为一种即插即用的方法，无需微调即可增强白盒和黑盒模型的安全性。

---

## #483 — On the Escaping Efficiency of Distributed Adversarial Training Algorithms

`C` Score: 4.23 | 2025-09-14

**Authors:** Ying Cao, Kun Yuan, Ali H. Sayed

**Categories:** cs.LG

**Scores:** Citation: 3.32 | Influential: 7.81 | Venue: 2.00 | Author: 1.86 | Recency: 7.00

**Links:** [arXiv](https://arxiv.org/abs/2509.11337) | [PDF](https://arxiv.org/pdf/2509.11337)

> 本文研究了多智能体学习环境中分布式对抗训练算法的逃离效率，并建立了一个理论框架来分析算法从局部最小值逃离的能力。研究表明，在扰动较小且批量较大的情况下，去中心化算法比集中式策略能更快地逃离局部最小值，从而获得更平坦的最小值并提升模型鲁棒性。

---

## #484 — Keep Calm and Avoid Harmful Content: Concept Alignment and Latent Manipulation Towards Safer Answers

`C` Score: 4.23 | 2025-10-14

**Authors:** Ruben Belo, Marta Guimaraes, Claudia Soares

**Categories:** cs.LG

**Scores:** Citation: 3.32 | Influential: 7.81 | Venue: 2.00 | Author: 1.86 | Recency: 7.00

**Links:** [arXiv](https://arxiv.org/abs/2510.12672) | [PDF](https://arxiv.org/pdf/2510.12672)

> 本文提出了CALM方法，一种无需重新训练的推理时干预手段，通过修改模型最后一层的潜在表示来抑制有害概念。该方法利用概念白化和正交投影技术，在保持模型性能的同时有效减少有害输出，提供了轻量级且高效的AI安全解决方案。

---

## #485 — VisuoAlign: Safety Alignment of LVLMs with Multimodal Tree Search

`C` Score: 4.23 | 2025-10-10

**Authors:** MingSheng Li, Guangze Zhao, Sichen Liu

**Categories:** cs.AI, cs.CR

**Scores:** Citation: 3.32 | Influential: 7.81 | Venue: 2.00 | Author: 1.86 | Recency: 7.00

**Links:** [arXiv](https://arxiv.org/abs/2510.15948) | [PDF](https://arxiv.org/pdf/2510.15948)

> 针对大型视觉语言模型（LVLM）的多模态越狱问题，提出VisuoAlign框架。该框架通过提示引导的树搜索（MCTS）将安全约束嵌入推理过程，系统构建安全关键轨迹并进行实时风险检测。实验表明，该方法能主动暴露风险并显著提升LVLM对复杂跨模态威胁的鲁棒性。

---

## #486 — Unified Threat Detection and Mitigation Framework (UTDMF): Combating Prompt Injection, Deception, and Bias in Enterprise-Scale Transformers

`C` Score: 4.23 | 2025-10-06

**Authors:** Santhosh KumarRavindran

**Categories:** cs.CR, cs.AI

**Scores:** Citation: 3.32 | Influential: 7.81 | Venue: 2.00 | Author: 1.86 | Recency: 7.00

**Links:** [arXiv](https://arxiv.org/abs/2510.04528) | [PDF](https://arxiv.org/pdf/2510.04528)

> 本文提出了统一威胁检测与缓解框架（UTDMF），这是一个针对企业级大模型的实时可扩展管道，旨在对抗提示注入、策略欺骗和偏见输出。通过扩展对抗性激活补丁框架，UTDMF在Llama-3.1、GPT-4o等模型上实现了92%的提示注入检测准确率，并显著减少了欺骗性输出和人口统计偏差。该框架包含通用补丁算法和企业级集成工具包，有效提升了企业系统的安全性与公平性。

---

## #487 — Cross-LLM Generalization of Behavioral Backdoor Detection in AI Agent Supply Chains

`C` Score: 4.19 | 2025-11-25

**Authors:** Arun Chowdary Sanna

**Categories:** cs.CR, cs.AI, cs.LG

**Scores:** Citation: 3.32 | Influential: 7.81 | Venue: 2.00 | Author: 0.26 | Recency: 9.00

**Links:** [arXiv](https://arxiv.org/abs/2511.19874) | [PDF](https://arxiv.org/pdf/2511.19874)

> 本文首次系统研究了 AI Agent 供应链中跨 LLM 的行为后门检测泛化能力，发现单模型检测器在不同 LLM 上的准确率大幅下降。通过分析 1,198 条执行轨迹，研究揭示了模型特定的行为特征，并提出了一种包含模型身份特征的模型感知检测方法，显著提升了跨模型的检测准确性。

---

## #488 — LLM Reinforcement in Context

`C` Score: 4.19 | 2025-11-16

**Authors:** Thomas Rivasseau

**Categories:** cs.CL, cs.CR

**Scores:** Citation: 3.32 | Influential: 7.81 | Venue: 2.00 | Author: 0.26 | Recency: 9.00

**Links:** [arXiv](https://arxiv.org/abs/2511.12782) | [PDF](https://arxiv.org/pdf/2511.12782)

> 本文提出了一种通过在用户输入中定期插入“中断”控制句来加强大语言模型对齐的方法，以解决随着输入长度增加越狱概率上升的问题。该方法可推广至思维链过程，防止模型在长上下文中产生阴谋行为。研究表明，这种简单的干预手段能够有效增强模型的安全性，且随着用户输入长度的增加而扩展，填补了现有对齐研究的空白。

---

## #489 — Auto-Tuning Safety Guardrails for Black-Box Large Language Models

`C` Score: 4.19 | 2025-12-14

**Authors:** Perry Abdulkadir

**Categories:** cs.CR, cs.CL, cs.LG

**Scores:** Citation: 3.32 | Influential: 7.81 | Venue: 2.00 | Author: 0.26 | Recency: 9.00

**Links:** [arXiv](https://arxiv.org/abs/2512.15782) | [PDF](https://arxiv.org/pdf/2512.15782)

> 本文提出将安全护栏设计视为冻结基础模型上的超参数优化问题，以替代手工调优的脆弱方法。研究将 Mistral-7B-Instruct 与模块化的越狱和恶意软件系统提示及基于 ModernBERT 的有害性分类器封装，并在三个公共基准上评估候选配置。通过运行黑盒 Optuna 研究，结果表明该方法能以数量级更少的评估和更短的时间可靠地重新发现最佳网格配置，证明了在计算和时间受限下加固黑盒 LLM 部署的可行性。

---

## #490 — The Laminar Flow Hypothesis: Detecting Jailbreaks via Semantic Turbulence in Large Language Models

`C` Score: 4.19 | 2025-12-14

**Authors:** Md. Hasib Ur Rahman

**Categories:** cs.LG, cs.AI

**Scores:** Citation: 3.32 | Influential: 7.81 | Venue: 2.00 | Author: 0.26 | Recency: 9.00

**Links:** [arXiv](https://arxiv.org/abs/2512.13741) | [PDF](https://arxiv.org/pdf/2512.13741)

> 本文提出了层流假设，认为良性输入在 LLM 的高维潜在空间中诱导平滑过渡，而对抗性提示则触发由安全对齐与指令遵循目标冲突导致的混沌高方差轨迹（语义湍流）。研究通过层余弦速度方差这一零样本度量形式化该现象，实验表明 RLHF 对齐的 Qwen2-1.5B 在攻击下湍流显著增加，验证了内部冲突假设。该发现表明语义湍流不仅是一种轻量级的实时越狱检测器，也是对黑盒模型底层安全架构进行分类的非侵入式诊断工具。

---

## #491 — Invasive Context Engineering to Control Large Language Models

`C` Score: 4.19 | 2025-12-02

**Authors:** Thomas Rivasseau

**Categories:** cs.AI

**Scores:** Citation: 3.32 | Influential: 7.81 | Venue: 2.00 | Author: 0.26 | Recency: 9.00

**Links:** [arXiv](https://arxiv.org/abs/2512.03001) | [PDF](https://arxiv.org/pdf/2512.03001)

> 本文提出了侵入式上下文工程技术，通过在LLM上下文中插入控制句来部分解决长上下文环境下的模型滥用和越狱风险。该技术不依赖模型训练，可推广至思维链过程以防止模型策划，为长上下文场景下的LLM安全提供了强有力的保障。

---

## #492 — From Threat to Tool: Leveraging Refusal-Aware Injection Attacks for Safety Alignment

`C` Score: 4.12 | 2025-06-07

**Authors:** Kyubyung Chae, Hyunbin Jin, Taesup Kim

**Categories:** cs.CR, cs.AI, cs.CL

**Scores:** Citation: 3.32 | Influential: 7.81 | Venue: 2.00 | Author: 1.12 | Recency: 7.00

**Links:** [arXiv](https://arxiv.org/abs/2506.10020) | [PDF](https://arxiv.org/pdf/2506.10020)

> 本文提出RAAI框架，利用拒绝感知的自适应注入攻击生成有害合成数据，以此对大模型进行安全对齐微调。实验表明，该方法生成的数据能有效提升模型对有害提示的鲁棒性，同时保持模型在通用任务上的能力。这项工作展示了如何将攻击技术转化为可扩展的安全对齐工具。

---

## #493 — Truth-Aware Decoding: A Program-Logic Approach to Factual Language Generation

`C` Score: 4.12 | 2025-10-03

**Authors:** Faruk Alpay, Hamdi Alakkad

**Categories:** cs.AI, cs.LO

**Scores:** Citation: 3.32 | Influential: 7.81 | Venue: 2.00 | Author: 1.12 | Recency: 7.00

**Links:** [arXiv](https://arxiv.org/abs/2510.07331) | [PDF](https://arxiv.org/pdf/2510.07331)

> 本文介绍了真值感知解码（TAD），一种面向验证的解码方案，旨在通过在解码时操作语义格网，将神经语言生成与知识库对齐。该方法基于概率程序语义传统，提出了约束语义和知识感知安全质量等概念，并在不牺牲吞吐量的情况下减少了幻觉。数值和算法案例研究证实，TAD为大规模经验模型和形式化验证之间搭建了实用的桥梁，显著提升了生成内容的真实性。

---

## #494 — Can AI Keep a Secret? Contextual Integrity Verification: A Provable Security Architecture for LLMs

`C` Score: 4.04 | 2025-08-12

**Authors:** Aayush Gupta

**Categories:** cs.CR, cs.AI, cs.CL

**Scores:** Citation: 3.32 | Influential: 7.81 | Venue: 2.00 | Author: 0.58 | Recency: 7.00

**Links:** [arXiv](https://arxiv.org/abs/2508.09288) | [PDF](https://arxiv.org/pdf/2508.09288)

> 本文提出了上下文完整性验证（CIV），这是一种推理时安全架构，通过为每个 token 附加加密签名来源标签并在 transformer 内部强制执行源信任格，来防御提示注入攻击。CIV 在冻结模型上提供确定性的逐 token 非干扰保证，确保低信任 token 无法影响高信任表示。实验表明，CIV 在保持模型性能的同时达到了 0% 的攻击成功率，且无需微调即可提供即插即用的保护。

---

## #495 — CourtGuard: A Local, Multiagent Prompt Injection Classifier

`C` Score: 4.04 | 2025-10-20

**Authors:** Isaac Wu, Michael Maslowski

**Categories:** cs.CR, cs.AI

**Scores:** Citation: 3.32 | Influential: 7.81 | Venue: 2.00 | Author: 0.58 | Recency: 7.00

**Links:** [arXiv](https://arxiv.org/abs/2510.19844) | [PDF](https://arxiv.org/pdf/2510.19844)

> 本文提出了CourtGuard，一种本地可运行的多智能体提示注入分类器。该系统采用类似法庭的机制，通过辩护人、检察官和法官三个模型的协作来评估提示是否为注入攻击。实验表明，虽然其整体检测性能略逊于直接检测器，但显著降低了误报率，充分展示了多智能体系统在防御中的潜力。

---

## #496 — Active Honeypot Guardrail System: Probing and Confirming Multi-Turn LLM Jailbreaks

`C` Score: 4.04 | 2025-10-16

**Authors:** ChenYu Wu, Yi Wang, Yang Liao

**Categories:** cs.CR, cs.AI

**Scores:** Citation: 3.32 | Influential: 7.81 | Venue: 2.00 | Author: 0.58 | Recency: 7.00

**Links:** [arXiv](https://arxiv.org/abs/2510.15017) | [PDF](https://arxiv.org/pdf/2510.15017)

> 该研究提出了一种基于蜜罐的主动护栏系统，通过生成模棱两可的诱饵回复来探测用户意图，从而防御多轮越狱攻击。该方法将风险规避转化为风险利用，结合蜜罐效用评分和防御效率率，在显著破坏越狱成功的同时保持了良性用户体验。

---

## #497 — Learning to Detect Unknown Jailbreak Attacks in Large Vision-Language Models

`C` Score: 3.99 | 2025-10-17

**Authors:** Shuang Liang, Zhihao Xu, Jialing Tao, Hui Xue, Xiting Wang

**Categories:** cs.CV, cs.AI

**Scores:** Citation: 3.32 | Influential: 7.81 | Venue: 2.00 | Author: 0.26 | Recency: 7.00

**Links:** [arXiv](https://arxiv.org/abs/2510.15430) | [PDF](https://arxiv.org/pdf/2510.15430)

> 针对大视觉语言模型中的未知越狱攻击，该研究提出了 LoD 检测框架，通过任务特定学习而非攻击特定学习来提升泛化能力。该框架包含多模态安全概念激活向量和安全模式自编码器模块，在未知攻击检测中实现了更高的 AUROC 和效率。

---

## #498 — SLEAN: Simple Lightweight Ensemble Analysis Network for Multi-Provider LLM Coordination: Design, Implementation, and Vibe Coding Bug Investigation Case Study

`C` Score: 3.99 | 2025-10-11

**Authors:** Matheus J. T. Vargas

**Categories:** cs.SE, cs.AI

**Scores:** Citation: 3.32 | Influential: 7.81 | Venue: 2.00 | Author: 0.26 | Recency: 7.00

**Links:** [arXiv](https://arxiv.org/abs/2510.10010) | [PDF](https://arxiv.org/pdf/2510.10010)

> 本文提出了SLEAN，一个通过基于文本的提示编排来协调多个LLM提供商的确定性框架。该框架采用独立分析、交叉批评和仲裁的三阶段协议，在生产部署前过滤有害的AI生成代码建议。实验表明SLEAN能有效拒绝有害修复，并强制执行最小因果编辑，显著提高了AI辅助调试的安全性。

---

## #499 — A Flexible Large Language Models Guardrail Development Methodology Applied to Off-Topic Prompt Detection

`C` Score: 3.95 | 2024-11-20

**Authors:** Gabriel Chua, Shing Yee Chan, Shaun Khoo

**Categories:** cs.CL, cs.LG

**Scores:** Citation: 3.37 | Influential: 7.81 | Venue: 2.00 | Author: 1.12 | Recency: 5.00

**Links:** [arXiv](https://arxiv.org/abs/2411.12946) | [PDF](https://arxiv.org/pdf/2411.12946)

> 本文提出了一种灵活的、无需真实数据的护栏开发方法论，通过定义问题空间并利用LLM生成合成数据集，训练出优于启发式方法的离题护栏。该护栏能有效泛化至越狱和有害提示等其他滥用类别，为预生产环境下的安全开发提供了宝贵资源。

---

## #500 — Attention Shift: Steering AI Away from Unsafe Content

`C` Score: 3.92 | 2024-10-06

**Authors:** Shivank Garg, Manyana Tiwari

**Categories:** cs.CV, cs.CR, cs.LG

**Scores:** Citation: 3.32 | Influential: 7.81 | Venue: 2.00 | Author: 1.12 | Recency: 5.00

**Links:** [arXiv](https://arxiv.org/abs/2410.04447) | [PDF](https://arxiv.org/pdf/2410.04447)

> 本研究提出了一种无需训练的新方法，通过在推理过程中重新加权注意力机制，来移除生成模型中的不安全概念。该方法与现有的消融方法进行了对比，并在直接提示和对抗性越狱提示下进行了定性和定量评估。实验结果表明，该方法能有效限制有害内容的生成，同时讨论了内容限制的局限性和更广泛的影响。

---

## #501 — Safety Alignment Depth in Large Language Models: A Markov Chain Perspective

`C` Score: 3.91 | 2025-02-02

**Authors:** Ching-Chia Kao, Chia-Mu Yu, Chun-Shien Lu, Chu-Song Chen

**Categories:** cs.LG

**Scores:** Citation: 3.46 | Influential: 7.81 | Venue: 2.00 | Author: 0.58 | Recency: 5.00

**Links:** [arXiv](https://arxiv.org/abs/2502.00669) | [PDF](https://arxiv.org/pdf/2502.00669)

> 这篇论文从马尔可夫链的视角研究了大型语言模型中的安全对齐深度问题。作者首次提出了确定安全对齐理想深度的理论结果，并展示了通过排列数据增强可以收紧安全边界。研究还揭示了安全对齐深度与模型集成宽度之间的相互作用关系，表明更宽的模型集成可以补偿较浅的对齐深度，为提升LLMs安全性提供了新的理论指导。

---

## #502 — The Great Contradiction Showdown: How Jailbreak and Stealth Wrestle in Vision-Language Models?

`C` Score: 3.85 | 2024-10-02

**Authors:** Ching-Chia Kao, Chia-Mu Yu, Chun-Shien Lu, Chu-Song Chen

**Categories:** cs.LG

**Scores:** Citation: 3.34 | Influential: 7.81 | Venue: 2.00 | Author: 0.58 | Recency: 5.00

**Links:** [arXiv](https://arxiv.org/abs/2410.01438) | [PDF](https://arxiv.org/pdf/2410.01438)

> 本文通过信息论框架分析了视觉语言模型中越狱攻击的有效性与隐蔽性之间的权衡，并基于Fano不等式提出了检测非隐蔽越狱攻击的高效算法。实验结果揭示了强攻击与可检测性之间的张力，为对抗策略和防御机制提供了深刻见解。

---
