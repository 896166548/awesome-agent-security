# Awesome Agent Security Papers

> A curated collection of research papers on AI Agent security — covering attacks, defense, evaluation, and architecture. **1799 papers** (2024-09 ~ 2026-04) from arXiv, ranked by quality score.

[**English**](README.md) · [中文](README_CN.md)

## Table of Contents

- [Statistics](#statistics)
- [Categories](#categories)
- [Scoring Methodology](#scoring-methodology)
- [Top 100 Papers](#top-100-papers)
  - [⚔️ Attacks and Adversaries](#attacks-and-adversaries)
  - [🛡️ Defense and Alignment](#defense-and-alignment)
  - [📊 Security Evaluation](#security-evaluation)
  - [🏗️ Agent Security Architecture](#agent-security-architecture)
  - [📄 Other Topics](#other-topics)

## Statistics

| Metric | Value |
|--------|-------|
| Total Papers | 1799 |
| Date Range | 2024-09 ~ 2026-04 |
| Score Range | 5.08 ~ 9.45 (avg 6.35) |

## Categories

| # | Category | Papers | Full List |
|---|----------|--------|-----------|
| 1 | ⚔️ Attacks & Adversaries | 586 | [View All](docs/attacks_adversaries.md) |
| 2 | 🛡️ Defense & Alignment | 502 | [View All](docs/defense_alignment.md) |
| 3 | 📊 Security Evaluation | 385 | [View All](docs/security_evaluation.md) |
| 4 | 🏗️ Agent Security Architecture | 211 | [View All](docs/agent_security_architecture.md) |
| 5 | 📄 Other Topics | 115 | [View All](docs/other_topics.md) |

## Scoring Methodology

Each paper is scored using a weighted formula based on [Semantic Scholar](https://www.semanticscholar.org/) data:

| Dimension | Weight | Source |
|-----------|--------|--------|
| Monthly Citations | 50% | Citation count normalized by age |
| Influential Citations | 10% | High-impact citation count |
| Venue Quality | 10% | Top venue=10, regular=5, preprint=2 |
| Author Quality | 20% | Highest author h-index |
| Recency | 10% | ≤3mo=10, ≤6mo=9, ≤12mo=7, >12mo=5 |

## Top 100 Papers

The top 100 papers out of 1799 (2024-09-24 ~ 2026-04-09), organized by category and ranked by quality score.

<a id="attacks-and-adversaries"></a>
### ⚔️ Attacks and Adversaries

**#3** [Persistent Pre-Training Poisoning of LLMs](https://arxiv.org/abs/2410.13722)  
*Yiming Zhang et al. (8)*  
Score: 9.36 · 2024-10-17

> This paper evaluates for the first time the risk of poisoning language models during the pre-training phase and investigates the persistence of these attacks after safety fine-tuning (SFT) and direct preference optimization (DPO). By pre-training a series of LLMs from scratch, the study finds that contaminating just 0.1% of the pre-training data is sufficient for three attack targets to persist through subsequent training. These findings reveal serious security vulnerabilities in the pre-training phase.
<br>

**#9** [SOM Directions are Better than One: Multi-Directional Refusal Suppression in Language Models](https://arxiv.org/abs/2511.08379)  
*Giorgio Piras et al. (6)*  
Score: 9.11 · 2025-11-11

> This paper proposes a novel method using Self-Organizing Maps (SOM) to extract multiple refusal directions within language models, thereby improving the understanding of refusal behavior. The authors demonstrate that SOM generalizes previous mean-difference techniques and derive a set of directions expressing refusal concepts by subtracting harmless representation centroids from harmful neurons. Experiments indicate that ablating multiple directions outperforms single-direction baselines and specialized jailbreak algorithms in suppressing refusals, revealing the low-dimensional manifold nature of refusal mechanisms.
<br>

**#13** [Emoji Attack: Enhancing Jailbreak Attacks Against Judge LLM Detection](https://arxiv.org/abs/2411.01077)  
*Zhipeng Wei, Yuqi Liu, N. Benjamin Erichson*  
Score: 9.01 · 2024-11-01

> This paper reveals that Judge LLMs are susceptible to tokenization bias, where separators alter the tokenization process and reduce detection accuracy. The authors propose Emoji Attack, a novel strategy that systematically inserts emojis into text using in-context learning to introduce semantic ambiguity and embedding distortion, significantly lowering the likelihood of detecting unsafe content. Experiments demonstrate that this attack effectively bypasses existing safety mechanisms, causing harmful content to be misjudged as safe.
<br>

**#15** [AdvWave: Stealthy Adversarial Jailbreak Attack against Large Audio-Language Models](https://arxiv.org/abs/2412.08608)  
*Mintong Kang, Chejian Xu, Bo Li*  
Score: 9.00 · 2024-12-11

> This paper proposes AdvWave, the first stealthy jailbreak attack framework targeting Large Audio-Language Models (LALMs). Addressing the gradient shattering problem caused by audio encoders, the method employs a two-stage optimization strategy to achieve end-to-end attacks and utilizes an adaptive adversarial objective search algorithm to cope with model behavior changes. Experiments validate the effectiveness of AdvWave in generating stealthy adversarial audio waveforms.
<br>

**#23** [Jailbreak-Tuning: Models Efficiently Learn Jailbreak Susceptibility](https://arxiv.org/abs/2507.11630)  
*Brendan Murphy et al. (7)*  
Score: 8.86 · 2025-07-15

> This paper demonstrates that fine-tuning can produce useful models while compromising safety measures, as the authors' jailbreak fine-tuning method teaches models to generate detailed, high-quality responses to arbitrary harmful requests. Models from OpenAI, Google, and Anthropic were found to fully comply with requests for CBRN assistance and cyberattacks. The study indicates that newer models are becoming more vulnerable, emphasizing the urgent need for tamper-proof guardrails and suggesting that releasing a fine-tunable model is equivalent to releasing its "evil twin."
<br>

**#24** [The Attacker Moves Second: Stronger Adaptive Attacks Bypass Defenses Against Llm Jailbreaks and Prompt Injections](https://arxiv.org/abs/2510.09023)  
*Milad Nasr et al. (14)*  
Score: 8.86 · 2025-10-10

> This paper criticizes current evaluation methods for jailbreak and prompt injection defenses as flawed for failing to fully consider adaptive attackers. By systematically adjusting optimization techniques like gradient descent and reinforcement learning, the authors successfully bypassed 12 of the latest defense mechanisms, achieving an attack success rate of over 90%. The study emphasizes that future defensive work must be evaluated against stronger adaptive attacks.
<br>

**#25** [Visual Contextual Attack: Jailbreaking MLLMs with Image-Driven Context Injection](https://arxiv.org/abs/2507.02844)  
*Ziqi Miao et al. (4)*  
Score: 8.85 · 2025-07-03

> This paper proposes a visual context attack targeting Multimodal Large Language Models (MLLMs), defining a new setting where visual information is a necessary component for constructing complete jailbreak scenarios. The VisCo attack forges contextual conversations through four visual strategies, dynamically generates auxiliary images to build realistic jailbreak scenarios, and combines toxicity obfuscation with semantic optimization techniques. Experiments show that this method achieves extremely high attack success rates on black-box MLLMs, significantly outperforming baseline methods.
<br>

**#47** [Adjacent Words, Divergent Intents: Jailbreaking Large Language Models via Task Concurrency](https://arxiv.org/abs/2510.21189)  
*Yukun Jiang et al. (4)*  
Score: 8.60 · 2025-10-24

> This paper proposes JAIL-CON, a jailbreak attack framework for large language models that utilizes a task concurrency mechanism. By encoding different intents in adjacent words and combining harmful tasks with benign ones, this method significantly reduces the probability of being filtered by safety guardrails. Experiments demonstrate that compared to existing sequential attacks, JAIL-CON exhibits stronger attack capabilities along with higher stealthiness and effectiveness.
<br>

**#50** [NEXUS: Network Exploration for eXploiting Unsafe Sequences in Multi-Turn LLM Jailbreaks](https://arxiv.org/abs/2510.03417)  
*Javad Rafiei Asl et al. (5)*  
Score: 8.57 · 2025-10-03

> This paper proposes the NEXUS framework to construct, refine, and execute optimized multi-turn jailbreak attacks, addressing the limitations of existing methods in exploring the adversarial space. The framework includes ThoughtNet for expanding malicious intents into semantic networks, a feedback-driven Simulator, and an adaptive Network Traverser. Experiments demonstrate that NEXUS significantly improves attack success rates on various closed-source and open-source LLMs by discovering covert and efficient adversarial paths.
<br>

**#53** [Towards Understanding the Fragility of Multilingual LLMs against Fine-Tuning Attacks](https://arxiv.org/abs/2410.18210)  
*Samuele Poppi et al. (7)*  
Score: 8.55 · 2024-10-23

> This paper investigates the vulnerability of multilingual large language models under fine-tuning attacks, finding that adversarial examples in one language can compromise safety alignment across all languages. The authors propose the Safety Information Localization (SIL) method to identify safety-related information in the model parameter space, verifying the hypothesis that safety information is language-agnostic. Results indicate that changing only a small number of weight parameters is sufficient to break cross-lingual safety alignment.
<br>

**#54** [Best-of-N Jailbreaking](https://arxiv.org/abs/2412.03556)  
*John Hughes et al. (10)*  
Score: 8.55 · 2024-12-04

> This paper introduces the Best-of-N (BoN) jailbreak algorithm, a simple black-box attack method applicable to frontier AI systems across multiple modalities. By augmenting prompts through random shuffling or case conversion and repeatedly sampling, BoN successfully bypasses state-of-the-art defenses including GPT-4o and Claude 3.5. These results reveal the model's sensitivity to minor input variations.
<br>

**#70** [JANUS: A Lightweight Framework for Jailbreaking Text-to-Image Models via Distribution Optimization](https://arxiv.org/abs/2603.21208)  
*Haolun Zheng et al. (9)*  
Score: 8.43 · 2026-03-22

> This paper proposes JANUS, a lightweight framework that jailbreaks text-to-image (T2I) models by optimizing structured prompt distributions under black-box end-to-end rewards. JANUS uses a low-dimensional mixture policy to replace high-capacity generators, achieving efficient exploration while maintaining target semantics. Experiments on modern T2I models show that JANUS outperforms state-of-the-art jailbreak methods, significantly increasing attack success rates and exposing structural weaknesses in current safety pipelines.
<br>

**#72** [Align is not Enough: Multimodal Universal Jailbreak Attack against Multimodal Large Language Models](https://arxiv.org/abs/2506.01307)  
*Youze Wang et al. (6)*  
Score: 8.41 · 2025-06-02

> This paper proposes a unified multimodal universal jailbreak attack framework that utilizes iterative image-text interaction and transfer strategies to generate adversarial suffixes and images. The study reveals critical security vulnerabilities in multimodal interactions, as this attack can induce various multimodal large models to generate high-quality harmful content. These findings expose the insufficiency of existing safety mechanisms.
<br>

**#76** [MUSE: MCTS-Driven Red Teaming Framework for Enhanced Multi-Turn Dialogue Safety in Large Language Models](https://arxiv.org/abs/2509.14651)  
*Siyu Yan et al. (9)*  
Score: 8.39 · 2025-09-18

> MUSE is a comprehensive framework addressing multi-turn jailbreak issues in large language models from both attack and defense perspectives. For attacks, MUSE-A utilizes framework semantics and heuristic tree search to explore diverse semantic trajectories; for defense, MUSE-D intervenes early in conversations through fine-grained safety alignment to mitigate vulnerabilities.
<br>

**#79** [How Vulnerable Are AI Agents to Indirect Prompt Injections? Insights from a Large-Scale Public Competition](https://arxiv.org/abs/2603.15714)  
*Mateusz Dziemian et al. (31)*  
Score: 8.38 · 2026-03-16

> This paper evaluates the vulnerability of AI Agents to indirect prompt injection attacks via a large-scale red-teaming competition, focusing on threats hidden in final responses. It reveals that all frontier models are susceptible to generic strategies allowing harmful operations without user awareness, highlighting fundamental weaknesses in instruction-following architectures.
<br>

**#95** [Differentiated Directional Intervention A Framework for Evading LLM Safety Alignment](https://arxiv.org/abs/2511.06852)  
*Peng Zhang, Peijie Sun*  
Score: 8.29 · 2025-11-10

> This paper proposes DBDI (Differentiated Bidirectional Intervention), a novel white-box framework designed to precisely neutralize safety alignment mechanisms in the critical layers of Large Language Models. By deconstructing the refusal mechanism into "harm detection" and "refusal execution" directions, the method bypasses safety defenses through adaptive projection elimination and direct suppression. Experiments demonstrate that DBDI achieves an attack success rate of up to 97.88% on models like Llama-2, offering a fine-grained mechanistic framework for deeply understanding LLM safety alignment.
<br>

**#96** [RAT: Adversarial Attacks on Deep Reinforcement Agents for Targeted Behaviors](https://arxiv.org/abs/2412.10713)  
*Fengshuo Bai et al. (5)*  
Score: 8.29 · 2024-12-14

> This paper proposes RAT, a general directional behavior attack method for deep reinforcement learning agents. Unlike previous strategies that focused solely on reducing rewards, RAT induces victim agents to perform specific behaviors aligned with the attacker's goals by training an intention policy that conforms to human preferences and dynamically adjusting state occupancy metrics. Experiments demonstrate that this method can effectively induce specific behaviors in robotic simulation tasks and enhance the robustness of the agents.
<br>

**#99** [Chain-of-Thought Hijacking](https://arxiv.org/abs/2510.26418)  
*Jianli Zhao et al. (5)*  
Score: 8.27 · 2025-10-30

> This paper proposes the "Chain-of-Thought Hijacking" attack, exposing a vulnerability in large reasoning models where extended reasoning sequences compromise security. By prepending long sequences of benign puzzle reasoning to harmful instructions, the attack successfully bypasses the safety defenses of multiple mainstream models with high success rates. Through activation probing and causal intervention analysis, the authors reveal that refusal mechanisms rely on low-dimensional safety signals which get diluted as reasoning length increases, causing the model to fail in rejecting harmful requests.
<br>

---

<a id="defense-and-alignment"></a>
### 🛡️ Defense and Alignment

**#5** [InfAlign: Inference-aware language model alignment](https://arxiv.org/abs/2412.19792)  
*Ananth Balashankar et al. (12)*  
Score: 9.17 · 2024-12-27

> Addressing the suboptimality of standard RLHF under inference-time algorithms like Best-of-N, this paper proposes the InfAlign framework. This framework aims to optimize inference-time win rates by calibrating and transforming reward functions, introducing the InfAlign-CTRL algorithm. It achieves significant performance improvements in Best-of-N sampling and jailbreak defense scenarios, effectively resolving the train-test mismatch problem.
<br>

**#6** [Instructional Segment Embedding: Improving LLM Safety with Instruction Hierarchy](https://arxiv.org/abs/2410.09102)  
*Tong Wu et al. (10)*  
Score: 9.16 · 2024-10-09

> Addressing security vulnerabilities caused by the lack of instruction hierarchy in LLMs, this paper proposes Instruction Segment Embedding (ISE) technology. Inspired by BERT, this technique embeds instruction priority information directly into the model architecture, enabling the model to explicitly distinguish and prioritize different types of instructions such as system messages and user prompts. Experiments show that ISE significantly improves the model's robustness against malicious prompts, increasing robust accuracy by approximately 15-18% on average while enhancing instruction-following capabilities.
<br>

**#8** [Trustworthy AI-Driven Dynamic Hybrid RIS: Joint Optimization and Reward Poisoning-Resilient Control in Cognitive MISO Networks](https://arxiv.org/abs/2604.01238)  
*Deemah H. Tashman, Soumaya Cherkaoui*  
Score: 9.12 · 2026-03-27

> This paper investigates the joint optimization and security control of AI-driven dynamic hybrid reconfigurable intelligent surfaces (RIS) in cognitive radio networks. It introduces an adaptive hybrid RIS architecture and utilizes the Soft Actor-Critic (SAC) deep reinforcement learning method to solve beamforming and phase optimization problems. Additionally, the study systematically examines reward poisoning attacks on DRL agents and proposes a lightweight real-time defense mechanism based on reward clipping and statistical anomaly filtering, validating its effectiveness through numerical results.
<br>

**#10** [Robust LLM safeguarding via refusal feature adversarial training](https://arxiv.org/abs/2409.20089)  
*Lei Yu et al. (4)*  
Score: 9.11 · 2024-09-30

> This paper reveals the general principle by which adversarial attacks bypass LLM safety mechanisms by eliminating 'refusal features' in the residual stream embedding space. Based on this finding, the authors propose the Refusal Feature Adversarial Training (ReFAT) algorithm, which efficiently performs adversarial training by simulating the effect of refusal feature elimination. This approach significantly improves model robustness with lower computational overhead.
<br>

**#14** [HarmAug: Effective Data Augmentation for Knowledge Distillation of Safety Guard Models](https://arxiv.org/abs/2410.01524)  
*Seanie Lee et al. (9)*  
Score: 9.00 · 2024-10-02

> This paper proposes HarmAug, an effective data augmentation method for distilling large teacher safety guardrail models into smaller models suitable for mobile devices. By generating harmful instructions via jailbroken LLMs and labeling them with the teacher model, this method addresses the limited diversity of existing labeled data. Consequently, it significantly enhances the performance of small safety models.
<br>

**#17** [When Machine Unlearning Meets Retrieval-Augmented Generation (RAG): Keep Secret or Forget Knowledge?](https://arxiv.org/abs/2410.15267)  
*Shang Wang et al. (4)*  
Score: 8.94 · 2024-10-20

> Addressing the high computational demands or limited applicability of existing machine unlearning methods, this paper proposes a lightweight behavioral unlearning framework based on Retrieval-Augmented Generation (RAG). This method simulates unlearning effects by modifying the external knowledge base of RAG, treating the construction of forgotten knowledge as a constrained optimization problem. The framework's effectiveness and harmlessness have been validated on both closed-source and open-source models.
<br>

**#34** [BlueSuffix: Reinforced Blue Teaming for Vision-Language Models Against Jailbreak Attacks](https://arxiv.org/abs/2410.20971)  
*Yunhan Zhao et al. (6)*  
Score: 8.77 · 2024-10-28

> This paper proposes BlueSuffix, a black-box defense method against jailbreak attacks on Vision-Language Models. The method consists of three key components: a visual purifier, a text purifier, and a blue-team suffix generator using reinforcement fine-tuning, aiming to enhance cross-modal robustness. Experiments on four VLMs and four safety benchmarks demonstrate that BlueSuffix significantly outperforms baseline defense methods without compromising model performance on benign inputs.
<br>

**#35** [Separate the Wheat from the Chaff: A Post-Hoc Approach to Safety Re-Alignment for Fine-Tuned Language Models](https://arxiv.org/abs/2412.11041)  
*Di Wu et al. (4)*  
Score: 8.75 · 2024-12-15

> This paper proposes the IRR method to address the issue that fine-tuning processes often compromise LLM safety alignment. The method achieves post-hoc safety realignment by identifying and removing unsafe delta parameters in the fine-tuned model while recalibrating the retained parameters. Experiments show that IRR significantly improves model performance on safety benchmarks such as harmful queries and jailbreak attacks while maintaining downstream task performance, effectively restoring safety after fine-tuning.
<br>

**#36** [Jailbreak Antidote: Runtime Safety-Utility Balance via Sparse Representation Adjustment in Large Language Models](https://arxiv.org/abs/2410.02298)  
*Guobin Shen et al. (5)*  
Score: 8.74 · 2024-10-03

> This study proposes a method named "Jailbreak Antidote" that adjusts the safety preferences of Large Language Models in real-time by manipulating a sparse subset of internal states during inference. By shifting the model's hidden representations along a safety direction, the method achieves flexible control over the safety-utility trade-off without additional token overhead or inference latency. Experiments validate the effectiveness and efficiency of this method against jailbreak attacks across various LLMs.
<br>

**#38** [LLM Jailbreak Detection for (Almost) Free!](https://arxiv.org/abs/2509.14558)  
*Guorui Chen et al. (6)*  
Score: 8.68 · 2025-09-18

> This paper proposes a nearly zero-computation-cost jailbreak detection method (FJD) that utilizes differences in output distributions between jailbreak and benign prompts. By adding affirmative instructions before inputs and adjusting temperature scaling combined with virtual instruction learning, the method effectively distinguishes malicious prompts without adding extra inference overhead.
<br>

**#42** [RobustKV: Defending Large Language Models against Jailbreak Attacks via KV Eviction](https://arxiv.org/abs/2410.19937)  
*Tanqiu Jiang et al. (6)*  
Score: 8.63 · 2024-10-25

> This paper proposes RobustKV, a novel method to defend against jailbreak attacks by selectively removing key tokens of harmful queries from the Key-Value (KV) cache. Based on the intuition that jailbreak prompts lower the importance of tokens hiding harmful queries, the method prevents malicious response generation by strategically evicting the KV of low-ranking tokens. Experiments show that RobustKV effectively combats state-of-the-art jailbreak attacks while maintaining the general performance of LLMs on benign queries.
<br>

**#46** [Analysing the Safety Pitfalls of Steering Vectors](https://arxiv.org/abs/2603.24543)  
*Yuxiao Li et al. (5)*  
Score: 8.61 · 2026-03-25

> This paper systematically audits the security risks of widely used activation steering methods (CAA), evaluating the impact of steering vectors on jailbreak attack success rates. The study finds that steering vectors significantly alter attack success rates, potentially increasing or decreasing them depending on the target behavior due to overlap with refusal directions. These findings reveal a trade-off between controllability and safety in LLMs, highlighting the necessity of considering safety factors in behavior steering techniques.
<br>

**#52** [Oyster-I: Beyond Refusal -- Constructive Safety Alignment for Responsible Language Models](https://arxiv.org/abs/2509.01909)  
*Ranjie Duan et al. (30)*  
Score: 8.56 · 2025-09-02

> This paper proposes the Constructive Safety Alignment (CSA) paradigm, aiming to go beyond traditional refusal mechanisms by actively guiding users in psychological distress toward safety. The Oyster-I model employs game theory to predict user reactions and combines fine-grained risk boundary discovery to defend against malicious attacks while actively guiding vulnerable users. This approach maintains high general capabilities while achieving effective defense and positive guidance.
<br>

**#56** [The Assistant Axis: Situating and Stabilizing the Default Persona of Language Models](https://arxiv.org/abs/2601.10387)  
*Christina Lu et al. (5)*  
Score: 8.54 · 2026-01-15

> This paper identifies the "assistant axis" within the model's role space and demonstrates that restricting activations on this axis can stabilize model behavior and prevent harmful role drift. By manipulating internal activation directions, this method effectively defends against role-based jailbreak attacks. This work provides a new perspective for understanding and controlling the default behavior of models.
<br>

**#57** [Immune: Improving Safety Against Jailbreaks in Multi-modal LLMs via Inference-Time Alignment](https://arxiv.org/abs/2411.18688)  
*Soumya Suvra Ghosal et al. (10)*  
Score: 8.54 · 2024-11-27

> This paper proposes Immune, an inference-time defense framework for multimodal large language models that utilizes a safety reward model to defend against jailbreak attacks by controlling decoding. The framework proves its effectiveness through mathematical analysis and significantly reduces attack success rates across various jailbreak benchmarks while maintaining the model's original capabilities.
<br>

**#59** [Building a Foundational Guardrail for General Agentic Systems via Synthetic Data](https://arxiv.org/abs/2510.09781)  
*Yue Huang et al. (14)*  
Score: 8.52 · 2025-10-10

> Addressing safety intervention during the pre-execution planning phase of agents, this paper proposes the AuraGen synthetic data engine and the Safiron foundational guardrail model. The framework trains guardrails by synthesizing benign trajectories and injecting risk data, enabling them to detect risks, assign types, and generate reasons before execution. Experiments show that this method achieves consistent performance improvements on benchmarks covering various tools and branching trajectories.
<br>

**#61** [Defending Against Prompt Injection with DataFilter](https://arxiv.org/abs/2510.19207)  
*Yizhu Wang et al. (5)*  
Score: 8.51 · 2025-10-22

> This paper proposes DataFilter, a test-time and model-agnostic defense method designed to remove malicious instructions before data reaches the backend large language model. Through supervised fine-tuning on simulated injection data, DataFilter selectively strips adversarial content, effectively maintaining the model's original utility. This approach reduces the success rate of prompt injection attacks to near zero.
<br>

**#62** [AgentDoG: A Diagnostic Guardrail Framework for AI Agent Safety and Security](https://arxiv.org/abs/2601.18491)  
*Dongrui Liu et al. (43)*  
Score: 8.49 · 2026-01-26

> This paper proposes AgentDoG, a diagnostic guardrail framework for AI Agent safety and assurance, addressing the lack of agent risk perception and transparency in existing models. Based on a unified three-dimensional risk taxonomy, AgentDoG performs fine-grained monitoring of agent trajectories and diagnoses the root causes of unsafe behaviors, offering traceability beyond binary labels. Experiments demonstrate that the framework achieves state-of-the-art agent safety auditing performance in complex interaction scenarios.
<br>

**#65** [WebGuard: Building a Generalizable Guardrail for Web Agents](https://arxiv.org/abs/2507.14293)  
*Boyuan Zheng et al. (11)*  
Score: 8.46 · 2025-07-18

> This paper introduces WebGuard, the first comprehensive dataset for evaluating web agent action risks and developing real-world online environment guardrails, containing 4,939 human-annotated actions across 193 websites. Experiments show that frontier LLMs have low accuracy and recall in predicting high-risk actions, highlighting the risks of lacking specialized guardrails. By fine-tuning specialized guardrail models using WebGuard, the authors found that the fine-tuned Qwen2.5VL-7B model significantly improved performance across various generalization settings.
<br>

**#67** [Online Learning Defense against Iterative Jailbreak Attacks via Prompt Optimization](https://arxiv.org/abs/2510.17006)  
*Masahiro Kaneko, Zeerak Talat, Timothy Baldwin*  
Score: 8.44 · 2025-10-19

> This study proposes an online learning-based defense framework that dynamically updates defense strategies to counter iterative jailbreak attacks. By utilizing reinforcement learning to optimize prompts and introducing Past-Direction Gradient Damping to suppress overfitting, the method effectively rejects harmful prompts. This approach significantly improves response quality for harmless tasks while maintaining robust defense.
<br>

**#68** [LLMZ+: Contextual Prompt Whitelist Principles for Agentic LLMs](https://arxiv.org/abs/2509.18557)  
*Tom Pawelek et al. (7)*  
Score: 8.43 · 2025-09-23

> Addressing the safety risks faced by agent-based large language models, this paper proposes the LLMZ+ defense framework. Unlike traditional malicious intent detection methods, LLMZ+ implements a context-based prompt whitelist mechanism, allowing only safe messages that match predefined use cases to interact with the model. This approach simplifies the security framework, enhances long-term resilience, and effectively defends against common jailbreak attacks.
<br>

**#80** [Token Highlighter: Inspecting and Mitigating Jailbreak Prompts for Large Language Models](https://arxiv.org/abs/2412.18171)  
*Xiaomeng Hu, Pin-Yu Chen, Tsung-Yi Ho*  
Score: 8.38 · 2024-12-24

> Addressing jailbreak attacks against large language models, this paper proposes the Token Highlighter defense method. This method introduces affirmative loss to measure the model's willingness to answer, uses gradients to locate key attack tokens, and employs a soft removal technique to shrink their embeddings, effectively defending against various jailbreak attacks without compromising performance on benign queries.
<br>

**#82** [Large Reasoning Models Learn Better Alignment from Flawed Thinking](https://arxiv.org/abs/2510.00938)  
*ShengYun Peng et al. (10)*  
Score: 8.36 · 2025-10-01

> Large reasoning models are susceptible to flawed premises when generating chains of thought, lacking critical reasoning capabilities for safety alignment. This paper proposes the RECAP method, which explicitly teaches models to override flawed reasoning trajectories and reroute to safe, beneficial responses by mixing synthetically generated anti-adversarial chain-of-thought pre-fills with standard prompts. This approach significantly enhances model safety and jailbreak robustness without additional training costs, while reducing over-refusals and preserving core reasoning abilities.
<br>

**#84** [Proof-of-Guardrail in AI Agents and What (Not) to Trust from It](https://arxiv.org/abs/2603.05786)  
*Xisen Jin et al. (7)*  
Score: 8.34 · 2026-03-06

> This paper proposes a proof-of-guardrail system that utilizes Trusted Execution Environments (TEEs) to generate cryptographic proofs verifying that agent responses were generated after executing specific open-source guardrails. While ensuring guardrail execution integrity and protecting developer privacy, the system also identifies the deception risk of malicious developers actively sabotaging guardrails, offering new insights for verifying safety claims.
<br>

**#90** [Large Language Models Encode Semantics and Alignment in Linearly Separable Representations](https://arxiv.org/abs/2507.09709)  
*Baturay Saglam et al. (6)*  
Score: 8.31 · 2025-07-13

> Through large-scale empirical research, this paper finds that the high-level semantic information of LLMs consistently exists in low-dimensional subspaces across domains, forming linearly separable representations, especially in deep layers and prompts eliciting structured reasoning. Based on this, the authors train MLP probes as lightweight latent space guardrails, significantly increasing refusal rates for malicious queries and prompt injections. This provides new insights for geometry-aware safety tools.
<br>

**#91** [Secure Tug-of-War (SecTOW): Iterative Defense-Attack Training with Reinforcement Learning for Multimodal Model Security](https://arxiv.org/abs/2507.22037)  
*Muzhi Dai et al. (6)*  
Score: 8.30 · 2025-07-29

> This paper proposes SecTOW, a reinforcement learning-based iterative defense-attack training framework designed to enhance the safety of Multimodal Large Language Models (MLLMs). By leveraging iterative adversarial interactions between a defender and an auxiliary attacker to expand jailbreak data and train the defender, the method effectively addresses the issues of training sample scarcity and the over-refusal of benign inputs.
<br>

**#92** [Reimagining Safety Alignment with An Image](https://arxiv.org/abs/2511.00509)  
*Yifan Xia et al. (6)*  
Score: 8.30 · 2025-11-01

> We introduce Magic Image, an optimization-based visual prompt framework designed to enhance the safety of multimodal large models and reduce over-rejection. This method optimizes image prompts, enabling a single model to adapt to different value systems without parameter updates, thereby achieving a better balance between safety and performance while maintaining the model's capabilities.
<br>

**#100** [The VLLM Safety Paradox: Dual Ease in Jailbreak Attack and Defense](https://arxiv.org/abs/2411.08410)  
*Yangyang Guo et al. (4)*  
Score: 8.27 · 2024-11-13

> This paper explores the dual high-performance paradox of Vision Large Language Models in jailbreak attacks and defenses, analyzing vulnerabilities caused by visual inputs and the "over-cautiousness" issue in existing defense mechanisms. The authors propose the LLM-Pipeline method, which leverages LLM guardrails as effective detectors to enhance the safety of VLLMs.
<br>

---

<a id="security-evaluation"></a>
### 📊 Security Evaluation

**#1** [MCPEval: Automatic MCP-based Deep Evaluation for AI Agent Models](https://arxiv.org/abs/2507.12806)  
*Zhiwei Liu et al. (12)*  
Score: 9.45 · 2025-07-17

> This paper introduces MCPEval, an open-source Model Context Protocol (MCP) framework for automating end-to-end task generation and deep evaluation of LLM agents across different domains. The framework standardizes metrics and integrates seamlessly with native agent tools, eliminating the manual work of building evaluation pipelines. Empirical results across five real-world domains demonstrate its effectiveness in revealing subtle, domain-specific performances, and the authors release MCPEval to promote reproducible and standardized LLM agent evaluation.
<br>

**#2** [AgentHarm: A Benchmark for Measuring Harmfulness of LLM Agents](https://arxiv.org/abs/2410.09024)  
*Maksym Andriushchenko et al. (14)*  
Score: 9.37 · 2024-10-11

> This paper proposes the AgentHarm benchmark to measure the harmfulness of LLM agents, filling a gap in LLM agent robustness research. The benchmark includes 110 explicitly malicious agent tasks covering 11 harm categories such as fraud and cybercrime, requiring jailbroken agents to maintain their capabilities while completing multi-step tasks. Evaluation results reveal that leading LLMs are surprisingly compliant with malicious agent requests even without attacks, and simple universal jailbreak templates can effectively induce coherent malicious behaviors.
<br>

**#7** [Agent Security Bench (ASB): Formalizing and Benchmarking Attacks and Defenses in LLM-based Agents](https://arxiv.org/abs/2410.02644)  
*Hanrong Zhang et al. (8)*  
Score: 9.15 · 2024-10-03

> This study introduces Agent Security Bench (ASB), a comprehensive framework designed to formalize and benchmark attacks and defenses for LLM-based agents. The framework covers 10 scenarios including e-commerce and autonomous driving, featuring 10 target agents, over 400 tools, and 27 attack and defense methods. Benchmark results reveal critical vulnerabilities across various stages of agent operation and assess the limited effectiveness of existing defense measures.
<br>

**#28** [RedCode: Risky Code Execution and Generation Benchmark for Code Agents](https://arxiv.org/abs/2411.07781)  
*Chengquan Guo et al. (8)*  
Score: 8.82 · 2024-11-12

> This paper proposes RedCode, a benchmark for evaluating the security of code agents, consisting of two parts: RedCode-Exec and RedCode-Gen. RedCode-Exec provides 4,050 test cases covering 25 types of vulnerabilities to evaluate an agent's ability to identify and handle unsafe code, while RedCode-Gen assesses the tendency to generate harmful code. Empirical findings based on 19 LLMs reveal that while agents tend to refuse risky OS-level operations, they struggle to refuse executing technically flawed code, highlighting security risks in real-world deployments.
<br>

**#29** [Beyond Simulations: What 20,000 Real Conversations Reveal About Mental Health AI Safety](https://arxiv.org/abs/2601.17003)  
*Caitlin A. Stamatis et al. (6)*  
Score: 8.80 · 2026-01-14

> This study evaluates the safety of mental health AI by reproducing four safety test sets and conducting an ecological audit of 20,000 real-world conversations. Results show that specialized AIs have a much lower rate of harmful content generation in benchmarks like suicide and self-harm compared to general LLMs, and their safety in real-world deployment is superior to simulated tests. Clinician reviews confirmed extremely low false negative rates, emphasizing the importance of evaluating AI safety based on real-world usage data.
<br>

**#32** [DeepPlanning: Benchmarking Long-Horizon Agentic Planning with Verifiable Constraints](https://arxiv.org/abs/2601.18137)  
*Yinger Zhang et al. (9)*  
Score: 8.77 · 2026-01-26

> This paper presents DeepPlanning, a benchmark for practical long-horizon Agent planning, featuring multi-day trip planning and multi-product shopping tasks. The benchmark requires models to possess capabilities in active information gathering, local constraint reasoning, and global constraint optimization to address the insufficient representation of real-world constraints in existing benchmarks. Evaluation results show that even frontier Agent LLMs struggle with these tasks, highlighting the importance of reliable reasoning patterns and parallel tool use.
<br>

**#33** [SG-Bench: Evaluating LLM Safety Generalization Across Diverse Tasks and Prompt Types](https://arxiv.org/abs/2410.21965)  
*Yutao Mou, Shikun Zhang, Wei Ye*  
Score: 8.77 · 2024-10-29

> This paper proposes SG-Bench, a novel benchmark designed to evaluate the safety generalization capabilities of Large Language Models across various tasks and prompt types. The benchmark integrates generative and discriminative evaluation tasks and expands the data to examine the impact of prompt engineering and jailbreaking on LLM safety. Evaluation results indicate that most LLMs perform poorly on discriminative tasks and are highly susceptible to prompts, suggesting weak generalization in safety alignment.
<br>

**#37** [Audio Is the Achilles' Heel: Red Teaming Audio Large Multimodal Models](https://arxiv.org/abs/2410.23861)  
*Hao Yang et al. (4)*  
Score: 8.72 · 2024-10-31

> This paper conducts a comprehensive red-teaming of five advanced audio Large Multimodal Models, evaluating their safety regarding harmful audio questions, non-speech audio interference, and specific speech jailbreak scenarios. Results show that open-source audio LMMs have a high average attack success rate on harmful audio questions and are susceptible to non-speech noise interference, exposing security vulnerabilities in the audio modality.
<br>

**#40** [AdamMeme: Adaptively Probe the Reasoning Capacity of Multimodal Large Language Models on Harmfulness](https://arxiv.org/abs/2507.01702)  
*Zixin Chen et al. (8)*  
Score: 8.66 · 2025-07-02

> This paper proposes AdamMeme, a flexible agent-based evaluation framework for adaptively probing the understanding capabilities of Multimodal Large Language Models regarding harmful memes. Through multi-agent collaboration, the framework iteratively updates challenging meme data to comprehensively expose specific weaknesses in the models' interpretation of harmfulness. Experiments show that AdamMeme systematically reveals performance differences across different target models, providing fine-grained analysis.
<br>

**#41** [Agents in the Wild: Safety, Society, and the Illusion of Sociality on Moltbook](https://arxiv.org/abs/2602.13284)  
*Yunbei Zhang et al. (8)*  
Score: 8.63 · 2026-02-07

> This paper conducts a large-scale empirical study on the AI social platform Moltbook, observing the spontaneous social behaviors and safety status of agents in an open environment. The study finds that agents spontaneously formed governance and economic systems within days, and social engineering attacks were far more effective than prompt injection, with highly adversarial content receiving more interactions. The research reveals structural voids in agent social interactions and the security challenges they face.
<br>

**#43** [Security Challenges in AI Agent Deployment: Insights from a Large Scale Public Competition](https://arxiv.org/abs/2507.20526)  
*Andy Zou et al. (17)*  
Score: 8.61 · 2025-07-28

> Based on a large-scale red-teaming competition targeting 22 frontier AI Agents, this paper analyzes security challenges in Agent deployment. By constructing the ART benchmark, the study finds that almost all Agents exhibit policy violations within a few queries, and robustness has low correlation with model scale or capability, revealing critical security vulnerabilities in current AI Agents.
<br>

**#44** [OpenAgentSafety: A Comprehensive Framework for Evaluating Real-World AI Agent Safety](https://arxiv.org/abs/2507.06134)  
*Sanidhya Vijayvargiya et al. (7)*  
Score: 8.61 · 2025-07-08

> This paper proposes the OpenAgentSafety framework to evaluate the safety of AI Agents interacting with real-world tools such as browsers and code environments. Covering 8 major risk categories and over 350 tasks, the framework reveals severe security vulnerabilities in mainstream LLMs within Agent scenarios, emphasizing the necessity of strengthening safeguards before deployment.
<br>

**#45** [Holistic Agent Leaderboard: The Missing Infrastructure for AI Agent Evaluation](https://arxiv.org/abs/2510.11977)  
*Sayash Kapoor et al. (31)*  
Score: 8.61 · 2025-10-13

> This paper introduces the Holistic Agent Leaderboard (HAL), a standardized infrastructure designed to address Agent evaluation challenges. It provides parallel evaluation tools for a three-dimensional analysis of models, scaffolding, and benchmarks, and utilizes LLM-assisted log inspection to discover unreported anomalous behaviors. The framework aims to standardize evaluation methods, pushing Agents from passing benchmarks to working reliably in the real world.
<br>

**#48** [Risky-Bench: Probing Agentic Safety Risks under Real-World Deployment](https://arxiv.org/abs/2602.03100)  
*Jingnan Zheng et al. (11)*  
Score: 8.60 · 2026-02-03

> This paper proposes the Risky-Bench framework to address the limited coverage of existing agent safety evaluations and their difficulty in adapting to complex real-world deployments. It constructs context-aware safety rules based on domain-independent security principles and systematically evaluates security risks through real task execution under various threat assumptions. Applied to life assistant agent scenarios, Risky-Bench reveals that state-of-the-art agents face significant security risks under real execution conditions.
<br>

**#58** [Refusal-Trained LLMs Are Easily Jailbroken As Browser Agents](https://arxiv.org/abs/2410.13886)  
*Priyanshu Kumar et al. (12)*  
Score: 8.53 · 2024-10-11

> This paper investigates the safety of refusal-trained LLMs in non-chat and agent use cases, introducing the BrowserART toolkit specifically for red-teaming browser agents. Empirical studies reveal that while the backbone LLM refuses harmful instructions as a chatbot, the corresponding browser agent often fails to refuse. Furthermore, jailbreak attacks designed for chat environments effectively transfer to browser agents, exposing serious flaws in current safety mechanisms for agent applications.
<br>

**#60** [Bridging AI and Software Security: A Comparative Vulnerability Assessment of LLM Agent Deployment Paradigms](https://arxiv.org/abs/2507.06323)  
*Tarek Gasmi et al. (4)*  
Score: 8.51 · 2025-07-08

> This paper presents a comparative security evaluation of two LLM agent deployment paradigms, Function Calling and Model Context Protocol (MCP), using a unified threat classification framework. The study finds that architectural choice significantly reshapes the threat surface and that chained attacks have a high success rate. This work provides a methodological foundation and deployment guidance for cross-domain LLM agent security assessment.
<br>

**#64** [HAICOSYSTEM: An Ecosystem for Sandboxing Safety Risks in Human-AI Interactions](https://arxiv.org/abs/2409.16427)  
*Xuhui Zhou et al. (12)*  
Score: 8.49 · 2024-09-24

> This paper proposes the HAICOSYSTEM framework, which simulates complex multi-turn interactions and tool usage scenarios between human users and AI agents through a modular sandbox environment. It establishes a multi-dimensional evaluation system to measure operational, content, social, and legal risks. Experiments reveal that existing state-of-the-art LLMs face significant safety risks during malicious user interactions.
<br>

**#66** [From Assistant to Double Agent: Formalizing and Benchmarking Attacks on OpenClaw for Personalized Local AI Agent](https://arxiv.org/abs/2602.08412)  
*Yuhang Wang et al. (9)*  
Score: 8.45 · 2026-02-09

> Addressing the limitations of existing frameworks that focus on synthetic or task-centric settings, this paper proposes the Personalized Agent Safety Benchmark (PASB). This framework combines personalized usage scenarios, real toolchains, and long-horizon interactions to perform black-box end-to-end safety assessments on real systems. A systematic evaluation of OpenClaw reveals critical vulnerabilities at different stages, including user prompt processing, tool use, and memory retrieval.
<br>

**#69** [Skill-Inject: Measuring Agent Vulnerability to Skill File Attacks](https://arxiv.org/abs/2602.20156)  
*David Schmotz et al. (4)*  
Score: 8.43 · 2026-02-23

> This paper proposes SkillInject, a benchmark specifically designed to evaluate the vulnerability of LLM agents to prompt injection attacks via skill files. Addressing supply chain security risks, the study constructed a dataset containing 202 attack-task pairs, covering attacks ranging from overtly malicious to subtle ones hidden in legitimate instructions. Experimental results show that current mainstream LLM agents exhibit high vulnerability to such attacks, revealing a significant trade-off between safety and utility.
<br>

**#71** [Agent-SafetyBench: Evaluating the Safety of LLM Agents](https://arxiv.org/abs/2412.14470)  
*Zhexin Zhang et al. (7)*  
Score: 8.42 · 2024-12-19

> This paper introduces Agent-SafetyBench, a comprehensive benchmark designed to evaluate LLM agent safety, comprising 349 interactive environments and 2,000 test cases covering 8 classes of safety risks. Evaluation results on 16 popular LLM agents show that none achieved a safety score exceeding 60%, revealing fundamental defects such as a lack of robustness and risk awareness. This benchmark highlights that defensive prompts alone are insufficient to solve safety problems, providing an important tool for agent safety evaluation.
<br>

**#73** [Evaluation and Benchmarking of LLM Agents: A Survey](https://arxiv.org/abs/2507.21504)  
*Mahmoud Mohammadi et al. (4)*  
Score: 8.40 · 2025-07-29

> This paper presents a survey on LLM Agent evaluation, proposing a two-dimensional taxonomy of evaluation objectives and processes to systematically review existing work. It highlights challenges often overlooked in enterprise-level applications, such as role-based access control and long-term interaction compliance. Furthermore, the paper identifies future research directions for holistic, realistic, and scalable evaluation.
<br>

**#74** [State-Dependent Safety Failures in Multi-Turn Language Model Interaction](https://arxiv.org/abs/2603.15684)  
*Pengcheng Li et al. (8)*  
Score: 8.40 · 2026-03-15

> This paper investigates safety failures in multi-turn dialogues from a state space perspective, proposing the STAR diagnostic framework to analyze how dialogue history leads to safety breakdowns. The study finds that multi-turn failures stem from structured context state evolution, characterized by sudden phase transitions from refusal to compliance. This suggests that language model safety should be viewed as a dynamic, state-dependent process rather than a static attribute.
<br>

**#75** [Multimodal Situational Safety](https://arxiv.org/abs/2410.06172)  
*Kaiwen Zhou et al. (6)*  
Score: 8.40 · 2024-10-08

> This paper proposes the new challenge of multimodal contextual safety, exploring how safety considerations change based on the specific context of the user or agent. The authors developed MSSBench, a benchmark containing 1,820 language query-image pairs, to evaluate the ability of current multimodal large language models to assess query safety within visual contexts. The study finds that current MLLMs struggle to handle these nuanced safety issues, particularly in simultaneously managing explicit safety reasoning, visual understanding, and contextual safety reasoning.
<br>

**#78** [OmniSafeBench-MM: A Unified Benchmark and Toolbox for Multimodal Jailbreak Attack-Defense Evaluation](https://arxiv.org/abs/2512.06589)  
*Xiaojun Jia et al. (14)*  
Score: 8.38 · 2025-12-06

> The paper introduces OmniSafeBench-MM, a unified benchmark and toolbox for evaluating multimodal jailbreak attacks and defenses, integrating various attack methods and defense strategies. This benchmark establishes a three-dimensional evaluation protocol covering harmfulness, intent alignment, and response detail, comprehensively revealing security vulnerabilities in multimodal models and facilitating reproducible safety research.
<br>

**#83** [AgentDyn: A Dynamic Open-Ended Benchmark for Evaluating Prompt Injection Attacks of Real-World Agent Security System](https://arxiv.org/abs/2602.03117)  
*Hao Li et al. (5)*  
Score: 8.34 · 2026-02-03

> This paper proposes AgentDyn, a benchmark designed to address the lack of dynamic open-ended tasks, beneficial instructions, and complex user tasks in existing agent safety benchmarks. AgentDyn includes 60 challenging open-ended tasks and 560 injection test cases covering shopping, GitHub, and daily life scenarios, requiring agents to perform dynamic planning. Evaluations show that existing state-of-the-art defenses are either insufficiently safe or overly defensive, falling far short of actual deployment requirements.
<br>

**#85** [KnowU-Bench: Towards Interactive, Proactive, and Personalized Mobile Agent Evaluation](https://arxiv.org/abs/2604.08455)  
*Tongbo Chen et al. (16)*  
Score: 8.34 · 2026-04-09

> This study proposes KnowU-Bench, an online benchmark for personalized mobile agents built on a reproducible Android simulation environment, covering 42 general GUI tasks, 86 personalized tasks, and 64 proactive tasks. Unlike previous work treating user preferences as static context, KnowU-Bench hides user profiles and exposes only behavior logs to force true preference inference. It supports multi-turn preference elicitation and instantiates an LLM-driven user simulator based on structured profiles to comprehensively evaluate agent personalization capabilities.
<br>

**#86** [OdysseyArena: Benchmarking Large Language Models For Long-Horizon, Active and Inductive Interactions](https://arxiv.org/abs/2602.05843)  
*Fangzhi Xu et al. (19)*  
Score: 8.33 · 2026-02-05

> This paper proposes OdysseyArena, a benchmark for LLM agents focusing on long-horizon, proactive, and inductive interactions. By formalizing four primitives, the benchmark transforms abstract transition dynamics into concrete interactive environments, aiming to measure agents' inductive efficiency and long-horizon discovery capabilities. Experiments show that even frontier models exhibit flaws in inductive scenarios, revealing bottlenecks in the autonomous discovery of complex environments.
<br>

**#89** [BrowserArena: Evaluating LLM Agents on Real-World Web Navigation Tasks](https://arxiv.org/abs/2510.02418)  
*Sagnik Anupam et al. (6)*  
Score: 8.32 · 2025-10-02

> This paper proposes BrowserArena, an LLM agent evaluation platform based on the real open web, testing agent capabilities by collecting user tasks and conducting Arena-style adversarial comparisons. Utilizing step-by-step human feedback, the research identifies key failure modes such as CAPTCHA handling, popup removal, and URL navigation, analyzing strategy differences among models. This work reveals the diversity and fragility of current web agents in real environments, providing new benchmarks and methods for agent evaluation.
<br>

**#93** [EnterpriseOps-Gym: Environments and Evaluations for Stateful Agentic Planning and Tool Use in Enterprise Settings](https://arxiv.org/abs/2603.13594)  
*Shiva Krishna Reddy Malay et al. (9)*  
Score: 8.30 · 2026-03-13

> This paper introduces the EnterpriseOps-Gym benchmark, designed to evaluate an agent's planning and tool-use capabilities in realistic enterprise environments. The benchmark, which features numerous databases and tools, tested 14 state-of-the-art models on long-term planning and state changes, revealing key limitations in strategic reasoning and rejecting infeasible tasks. It provides a concrete platform for enhancing the robustness of agents in enterprise deployment.
<br>

**#97** [Confusion is the Final Barrier: Rethinking Jailbreak Evaluation and Investigating the Real Misuse Threat of LLMs](https://arxiv.org/abs/2508.16347)  
*Yu Yan et al. (9)*  
Score: 8.28 · 2025-08-22

> This paper re-examines jailbreak evaluation by decoupling techniques and building knowledge-intensive question-answering tasks to investigate the actual abuse threats of LLMs, such as their possession of dangerous knowledge and capacity for harmful task planning. Experiments reveal a mismatch between the success rate of jailbreaks and the possession of harmful knowledge, indicating that current evaluation frameworks are often anchored in toxic language patterns rather than genuine threats.
<br>

---

<a id="agent-security-architecture"></a>
### 🏗️ Agent Security Architecture

**#4** [IPIGuard: A Novel Tool Dependency Graph-Based Defense Against Indirect Prompt Injection in LLM Agents](https://arxiv.org/abs/2508.15310)  
*Hengyu An et al. (7)*  
Score: 9.33 · 2025-08-21

> This paper proposes IPIGuard, a novel defense paradigm based on tool dependency graphs to protect LLM agents from indirect prompt injection attacks. The method models the agent's task execution process as a traversal over a planned tool dependency graph, effectively reducing malicious tool calls by explicitly decoupling action planning from external data interaction. Experiments demonstrate that IPIGuard achieves an excellent balance between effectiveness and robustness.
<br>

**#12** [G-Designer: Architecting Multi-agent Communication Topologies via Graph Neural Networks](https://arxiv.org/abs/2410.11782)  
*Guibin Zhang et al. (9)*  
Score: 9.06 · 2024-10-15

> This paper presents G-Designer, an adaptive solution that utilizes graph neural networks to dynamically design multi-agent communication topologies. By modeling multi-agent networks, the method decodes task-adaptive, high-performance communication protocols that excel in various benchmarks while effectively reducing token consumption. Additionally, it demonstrates robustness against adversarial attacks on agents, thereby optimizing the deployment of multi-agent systems.
<br>

**#16** [Towards Low-Resource Harmful Meme Detection with LMM Agents](https://arxiv.org/abs/2411.05383)  
*Jianzhao Huang et al. (6)*  
Score: 8.97 · 2024-11-08

> This paper proposes a low-resource harmful meme detection framework based on LMM Agents, utilizing extroverted and introverted analysis with few labeled samples. By leveraging the reasoning capabilities of Large Multimodal Models (LMMs), the method retrieves relevant memes as auxiliary signals and triggers knowledge revision behaviors to obtain generalized harmful insights. Experiments demonstrate that this approach outperforms existing state-of-the-art methods in low-resource detection tasks across three meme datasets.
<br>

**#18** [MIND: A Multi-agent Framework for Zero-shot Harmful Meme Detection](https://arxiv.org/abs/2507.06908)  
*Ziyan Liu et al. (5)*  
Score: 8.93 · 2025-07-09

> This paper presents the MIND multi-agent framework to achieve zero-shot harmful meme detection without the need for labeled data. MIND ensures robust decision-making by retrieving similar memes for context, employing a bidirectional insight derivation mechanism, and utilizing multi-agent debate. Experiments indicate that the framework outperforms existing zero-shot methods and demonstrates strong generalization across different model architectures and parameter scales, offering a scalable solution for harmful content detection on social media.
<br>

**#19** [Securing the Model Context Protocol: Defending LLMs Against Tool Poisoning and Adversarial Attacks](https://arxiv.org/abs/2512.06556)  
*Saeid Jamshidi et al. (6)*  
Score: 8.92 · 2025-12-06

> The paper analyzes semantic attacks within the Model Context Protocol (MCP), such as tool poisoning and shadow attacks, and proposes a layered security defense framework. By utilizing manifest signing, semantic auditing, and heuristic guardrails, this framework effectively protects MCP-based systems from malicious tool metadata, filling a gap in tool interaction security. This approach addresses the vulnerabilities inherent in tool-based interactions.
<br>

**#20** [Cut the Crap: An Economical Communication Pipeline for LLM-based Multi-Agent Systems](https://arxiv.org/abs/2410.02506)  
*Guibin Zhang et al. (9)*  
Score: 8.91 · 2024-10-03

> This study proposes AgentPrune, a cost-effective and robust multi-agent communication framework designed to prune redundant or malicious messages in existing LLM multi-agent pipelines. It is the first to identify and define the "communication redundancy" problem, significantly reducing token costs through one-time pruning on a spatiotemporal message passing graph. Experiments show that this method effectively defends against two types of agent-based adversarial attacks while maintaining high performance.
<br>

**#21** [ResMAS: Resilience Optimization in LLM-based Multi-agent Systems](https://arxiv.org/abs/2601.04694)  
*Zhilun Zhou et al. (8)*  
Score: 8.90 · 2026-01-08

> This paper proposes the ResMAS framework, which enhances the resilience of Large Language Model-based multi-agent systems under perturbations by generating resilient topologies and optimizing prompts via reinforcement learning. Experiments demonstrate that this method significantly improves system robustness and generalization capabilities under various constraints, providing new insights for building intrinsically resilient multi-agent systems.
<br>

**#22** [Policy Compiler for Secure Agentic Systems](https://arxiv.org/abs/2602.16708)  
*Nils Palumbo et al. (5)*  
Score: 8.89 · 2026-02-18

> This paper proposes PCAS, a policy compiler that provides deterministic policy execution for agent systems. The system models agent states through dependency graphs, uses the Datalog language to express policies, and intercepts violations via a reference monitor. Evaluations show that PCAS significantly improves policy compliance without requiring security-specific refactoring of model inference.
<br>

**#26** [Uncovering Security Threats and Architecting Defenses in Autonomous Agents: A Case Study of OpenClaw](https://arxiv.org/abs/2603.12644)  
*Zonghao Ying et al. (10)*  
Score: 8.83 · 2026-03-13

> This paper conducts a comprehensive security analysis of the OpenClaw ecosystem, revealing critical vulnerabilities such as prompt injection-driven remote code execution. It proposes the Full-lifecycle Agent Security Architecture (FASA), advocating for zero-trust execution and dynamic intent verification to address systemic architectural flaws in autonomous agents. This research provides a theoretical blueprint and engineering direction for building trustworthy autonomous agents.
<br>

**#27** [ToolSafe: Enhancing Tool Invocation Safety of LLM-based agents via Proactive Step-level Guardrail and Feedback](https://arxiv.org/abs/2601.10156)  
*Yutao Mou et al. (7)*  
Score: 8.82 · 2026-01-15

> ToolSafe proposes a framework to enhance the safety of LLM Agent tool calling through proactive step-level guardrails and feedback. The study constructs the TS-Bench benchmark and develops the TS-Guard model, which effectively reduces harmful tool calls and improves benign task completion rates, ensuring real-time safety monitoring during agent deployment.
<br>

**#31** [Towards Verifiably Safe Tool Use for LLM Agents](https://arxiv.org/abs/2601.08012)  
*Aarya Doshi et al. (6)*  
Score: 8.79 · 2026-01-12

> This paper proposes a process based on Systems-Theoretic Process Analysis (STPA) to identify hazards in Agent workflows and formalize safety requirements into executable specifications. The authors introduce an enhanced Model Context Protocol (MCP) framework to ensure tool safety through structured tags. This method aims to shift LLM Agent safety from ad-hoc reliability fixes to proactive guardrails with formal guarantees, reducing reliance on user confirmation.
<br>

**#39** [The Task Shield: Enforcing Task Alignment to Defend Against Indirect Prompt Injection in LLM Agents](https://arxiv.org/abs/2412.16682)  
*Feiran Jia et al. (4)*  
Score: 8.67 · 2024-12-21

> Addressing indirect prompt injection attacks faced by LLM agents, this paper proposes the Task Shield defense mechanism. This method reframes safety as a task alignment problem, systematically verifying at test time whether every instruction and tool call aligns with the user goal. It significantly reduces the attack success rate in the AgentDojo benchmark while maintaining high task utility, offering a new perspective on security defense.
<br>

**#49** [OS-Sentinel: Towards Safety-Enhanced Mobile GUI Agents via Hybrid Validation in Realistic Workflows](https://arxiv.org/abs/2510.24411)  
*Qiushi Sun et al. (14)*  
Score: 8.57 · 2025-10-28

> Addressing security risks in mobile GUI agents, this paper proposes MobileRisk-Live, a dynamic sandbox environment and safety detection benchmark. Building on this, the OS-Sentinel hybrid safety detection framework is developed, combining a formal verifier with a VLM-based contextual judge to effectively detect system violations and contextual risks. This approach significantly enhances the security of mobile agents.
<br>

**#51** [VeriGuard: Enhancing LLM Agent Safety via Verified Code Generation](https://arxiv.org/abs/2510.05156)  
*Lesly Miculicich et al. (7)*  
Score: 8.57 · 2025-10-03

> This paper introduces VeriGuard, a framework that provides formal safety guarantees for LLM-based agents through a two-stage architecture. It first synthesizes and verifies behavioral policies via formal verification in an offline stage, then acts as a runtime monitor to verify each proposed agent action in an online stage. This separation of offline verification and online monitoring enables formal guarantees to be practically applied to agents in sensitive domains, significantly enhancing their trustworthiness.
<br>

**#55** [Enforcing Temporal Constraints for LLM Agents](https://arxiv.org/abs/2512.23738)  
*Adharsh Kamath et al. (6)*  
Score: 8.54 · 2025-12-25

> This paper proposes the Agent-C framework to ensure LLM-based agents comply with formal temporal safety properties, such as authenticating before accessing data, at runtime. It introduces a domain-specific language to express temporal properties, uses SMT solvers to detect non-compliant operations, and employs constraint generation to force agents to execute compliant alternative actions. Experiments prove that Agent-C effectively prevents temporal violations in safety-critical applications.
<br>

**#63** [When Only the Final Text Survives: Implicit Execution Tracing for Multi-Agent Attribution](https://arxiv.org/abs/2603.17445)  
*Yi Nian et al. (6)*  
Score: 8.49 · 2026-03-18

> This paper proposes IET, a framework for multi-agent attribution via final text when execution metadata is unavailable. By embedding agent-specific statistical signals directly into the token generation process, the method converts output text into self-verifying execution records. This approach enables reliable accountability under privacy-preserving or system boundary constraints.
<br>

**#88** [A Framework for Formalizing LLM Agent Security](https://arxiv.org/abs/2603.19469)  
*Vincent Siu et al. (7)*  
Score: 8.33 · 2026-03-19

> This paper proposes a framework for formalizing LLM agent safety, systematizing existing attacks and defenses from the perspective of context safety. The framework defines four security properties: task alignment, action alignment, source authorization, and data isolation, and introduces oracle functions to verify violations. This framework helps address the trade-off between safety and utility, providing a theoretical foundation for defense strategies.
<br>

**#98** [Your Agent May Misevolve: Emergent Risks in Self-evolving LLM Agents](https://arxiv.org/abs/2509.26354)  
*Shuai Shao et al. (11)*  
Score: 8.28 · 2025-09-30

> This paper investigates the risk of "mis-evolution" in self-evolving LLM agents, where agents deviate from expected behaviors during self-improvement, leading to harmful outcomes. By evaluating four evolutionary paths—model, memory, tools, and workflow—the study reveals that even agents built on top-tier LLMs are prone to risks such as safety alignment degradation. These findings highlight the urgent need to establish new safety paradigms to address the potential threats posed by self-evolving agents.
<br>

---

<a id="other-topics"></a>
### 📄 Other Topics

**#11** [SPA-Bench: A Comprehensive Benchmark for SmartPhone Agent Evaluation](https://arxiv.org/abs/2410.15164)  
*Jingxuan Chen et al. (17)*  
Score: 9.11 · 2024-10-19

> This paper proposes SPA-Bench, a comprehensive benchmark for evaluating (multimodal) LLM-based smartphone agents. The benchmark provides diverse tasks, a plug-and-play framework, and an automated evaluation pipeline within a simulated real-world interaction environment, revealing challenges agents face in interpreting mobile interfaces, grounding actions, and retaining memory. These findings provide directions for future research.
<br>

**#30** [Agentic AI Security: Threats, Defenses, Evaluation, and Open Challenges](https://arxiv.org/abs/2510.23883)  
*Anshuman Chhabra et al. (4)*  
Score: 8.79 · 2025-10-27

> This paper is a survey on Agentic AI safety, systematically categorizing threats specific to agent systems and reviewing the latest benchmarks and evaluation methods. The article discusses defensive strategies from both technical and governance perspectives and identifies open challenges by synthesizing current research, aiming to support the development of "secure-by-design" agent systems.
<br>

**#77** [The Attack and Defense Landscape of Agentic AI: A Comprehensive Survey](https://arxiv.org/abs/2603.11088)  
*Juhee Kim et al. (7)*  
Score: 8.39 · 2026-03-11

> This paper presents the first systematic and comprehensive review of AI Agent safety, analyzing the design space, attack surfaces, and defense mechanisms of secure agent systems. Through case studies, it identifies gaps in existing secure agent systems and proposes a systematic framework for understanding AI Agent security risks and defense strategies.
<br>

**#81** [Strategic Tradeoffs Between Humans and AI in Multi-Agent Bargaining](https://arxiv.org/abs/2509.09071)  
*Crystal Qian et al. (7)*  
Score: 8.36 · 2025-09-11

> This paper empirically compares behavioral differences between humans, frontier large language models, and customized Bayesian Agents in dynamic multi-party bargaining games. The study finds that while LLMs and humans achieve comparable total surplus, LLMs tend towards conservative concession strategies whereas humans follow fairness norms, revealing substantial procedural differences masked by performance equality metrics.
<br>

**#87** [Steering Externalities: Benign Activation Steering Unintentionally Increases Jailbreak Risk for Large Language Models](https://arxiv.org/abs/2602.04896)  
*Chen Xiong et al. (5)*  
Score: 8.33 · 2026-02-03

> This paper reveals the steering externality phenomenon, where activation steering using benign datasets unintentionally weakens the safety guardrails of large language models. Experiments indicate that this intervention, aimed at improving model utility, conversely amplifies jailbreak vulnerabilities, raising attack success rates in standard benchmarks to over 80%. The study emphasizes the necessity of strictly scrutinizing unintended safety externalities arising from utility improvements during inference.
<br>

**#94** [Sketch2Code: Evaluating Vision-Language Models for Interactive Web Design Prototyping](https://arxiv.org/abs/2410.16232)  
*Ryan Li, Yanzhe Zhang, Diyi Yang*  
Score: 8.30 · 2024-10-21

> This paper introduces the Sketch2Code benchmark, designed to evaluate the ability of Visual Language Models (VLMs) to convert sketches into web prototypes through interactive agent assessments that simulate real design workflows. An analysis of ten commercial and open-source models reveals that existing models still struggle with accurately interpreting sketches and asking effective questions, highlighting the necessity for developing multi-turn dialogue agents.
<br>

---

*Data sourced from [arXiv](https://arxiv.org/) and [Semantic Scholar](https://www.semanticscholar.org/).*
