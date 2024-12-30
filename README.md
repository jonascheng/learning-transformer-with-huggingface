# 與 Hugging Face 共舞：認識 Transformer

透過本文，您將了解 Transformer 的基本概念，並透過 Hugging Face 的 Transformer 套件深入瞭解。

### [章節1：Hugging Face 初體驗](https://colab.research.google.com/github/jonascheng/learning-transformer-with-huggingface/blob/main/intro-huggingface.ipynb)

分別以 Token Classification、Zero-Shot Classification 及 Image Classification 三個任務，示範如何使用 Hugging Face 的 Transformer 套件。

### [章節2：Transformer 深入淺出](https://colab.research.google.com/github/jonascheng/learning-transformer-with-huggingface/blob/main/intro-transformer.ipynb)

初探 Transformer 架構，介紹 Input Embedding 及 Positional Encoding。

#### [2.1 The encoder](https://colab.research.google.com/github/jonascheng/learning-transformer-with-huggingface/blob/main/intro-transformer-encoder.ipynb)

進一步探討 Transformer Encoder 的運作原理。包含 Self-Attention、Multi-Head Attention 及 Feed-Forward Neural Network。

#### [2.2 The decoder](https://colab.research.google.com/github/jonascheng/learning-transformer-with-huggingface/blob/main/intro-transformer-decoder.ipynb)

介紹 Transformer Decoder 的運作原理。包含 Masked Self-Attention、Multi-Head Attention 及 Feed-Forward Neural Network。最後簡單說明 Encoder, Decoder, Encoder-Decoder 三者的相關應用。

### [章節3：訓練PII偵測模型 (Encoder)](https://colab.research.google.com/github/jonascheng/learning-transformer-with-huggingface/blob/main/pii-detection-ner.ipynb)

基於 Encoder 預訓練模型，訓練一個 PII (Personal Identifiable Information) 偵測模型。

### [章節4：訓練PII遮掩模型 (Decoder)](https://colab.research.google.com/github/jonascheng/learning-transformer-with-huggingface/blob/main/pii-masking-encoder.ipynb)

基於 Decoder 預訓練模型，訓練一個 PII (Personal Identifiable Information) 遮掩模型。

# 參考資料

- [NLP实战-Huggingface神器](https://www.udemy.com/course/nlp-huggingface/?srsltid=AfmBOoqxi590EHyXKB-FBc-OW3cDnZ5bpz8ZVAfhxDuSDEQK15kDPCiw)
- [Introduction to Transformer Models for NLP](https://www.linkedin.com/learning/introduction-to-transformer-models-for-nlp/introduction?resume=false&u=373648218)
- [Transformers: how do they work internally?](https://www.alexisalulema.com/2022/08/23/transformers-how-do-they-work-internally/)
- [A Comprehensive Overview of Transformer-Based Models: Encoders, Decoders, and More](https://medium.com/@minh.hoque/a-comprehensive-overview-of-transformer-based-models-encoders-decoders-and-more-e9bc0644a4e5)
- [台大資訊 深度學習之應用 | ADL TA Recitation: LLM LoRA Training 大型語言模型太大怎麼調整呢?](https://youtu.be/eGQMzbhokg0?si=CbbiGg_Osa5naA5A)
