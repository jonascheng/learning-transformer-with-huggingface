# 與 Hugging Face 共舞：認識 Transformer

透過本文，您將了解 Transformer 的基本概念，我們將透過 Hugging Face 的 Transformer 套件手把手操作深入瞭解。

課程規劃演練的部分，將以 Google Colab 為主要環境，並使用 Hugging Face 的 Transformer 套件進行操作。

關於 Colab 的申請及使用，請參考 [Google Colab](https://colab.research.google.com/notebooks/intro.ipynb)。

### [章節1：Hugging Face 初體驗](https://colab.research.google.com/github/jonascheng/learning-transformer-with-huggingface/blob/main/intro-huggingface.ipynb)

分別以 Token Classification、Zero-Shot Classification 及 Image Classification 三個任務，示範如何使用 Hugging Face 的 Transformer 套件。

### [章節2：Transformer 深入淺出](https://colab.research.google.com/github/jonascheng/learning-transformer-with-huggingface/blob/main/intro-transformer.ipynb)

初探 Transformer 架構，介紹 Input Embedding 及 Positional Encoding。

#### [2.1 The encoder](https://colab.research.google.com/github/jonascheng/learning-transformer-with-huggingface/blob/main/intro-transformer-encoder.ipynb)

進一步探討 Transformer Encoder 的運作原理。包含 Self-Attention、Multi-Head Attention 及 Feed-Forward Neural Network。

#### [2.2 The decoder](https://colab.research.google.com/github/jonascheng/learning-transformer-with-huggingface/blob/main/intro-transformer-decoder.ipynb)

介紹 Transformer Decoder 的運作原理。包含 Masked Self-Attention、Multi-Head Attention 及 Feed-Forward Neural Network。最後簡單說明 Encoder, Decoder, Encoder-Decoder 三者的相關應用。

### [章節3：訓練 PII 偵測模型 (Encoder-Only)](https://colab.research.google.com/github/jonascheng/learning-transformer-with-huggingface/blob/main/pii-detection-encoder.ipynb)

基於 Encoder-Only 預訓練模型，微調一個 PII (Personal Identifiable Information) 偵測模型。

### [章節4：訓練 QA 問答模型 (Decoder-Only)](https://colab.research.google.com/github/jonascheng/learning-transformer-with-huggingface/blob/main/qa-decoder.ipynb)

基於 Decoder-Only 預訓練模型，微調一個 QA 問答模型。

這個章節也會介紹半精度訓練及 LoRA 訓練技巧。以此降低 GPU 記憶體需求，提升訓練效率。

### [章節5：訓練 PII 遮掩模型 (Encoder-Decoder)](https://colab.research.google.com/github/jonascheng/learning-transformer-with-huggingface/blob/main/pii-masking-encode-decode.ipynb)

基於 Encoder-Decoder 預訓練模型，微調一個 PII 遮掩模型。

# 參考資料

## 影視課程

- [NLP实战-Huggingface神器](https://www.udemy.com/course/nlp-huggingface/?srsltid=AfmBOoqxi590EHyXKB-FBc-OW3cDnZ5bpz8ZVAfhxDuSDEQK15kDPCiw)
- [手把手带你实战HuggingFace Transformers](https://youtube.com/playlist?list=PL2ecZnqc6-L7r8tSr6r3bYHsqkyChUVbM&si=W9f104zWreQ0tS7F)

## 文章探討

### Transformer

- [Introduction to Transformer Models for NLP](https://www.linkedin.com/learning/introduction-to-transformer-models-for-nlp/introduction?resume=false&u=373648218)
- [Transformers: how do they work internally?](https://www.alexisalulema.com/2022/08/23/transformers-how-do-they-work-internally/)
- [A Comprehensive Overview of Transformer-Based Models: Encoders, Decoders, and More](https://medium.com/@minh.hoque/a-comprehensive-overview-of-transformer-based-models-encoders-decoders-and-more-e9bc0644a4e5)

### Embeddings

- [How to Create Bert Vector Embeddings? A Comprehensive Tutorial](https://airbyte.com/data-engineering-resources/bert-vector-embedding)
- [BERT Embeddings](https://tinkerd.net/blog/machine-learning/bert-embeddings/)
- [Beyond Attention: How Advanced Positional Embedding Methods Improve upon the Original Approach in Transformer Architecture](https://towardsdatascience.com/beyond-attention-how-advanced-positional-embedding-methods-improve-upon-the-original-transformers-90380b74d324)

### Encoder

- [BERT Encoder Layer](https://tinkerd.net/blog/machine-learning/bert-encoder/)

## 模型微調

- [台大資訊 深度學習之應用 | ADL TA Recitation: LLM LoRA Training 大型語言模型太大怎麼調整呢?](https://youtu.be/eGQMzbhokg0?si=CbbiGg_Osa5naA5A)
