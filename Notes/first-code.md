# Basic CNN in PyTorch – Simple Explanation

This document explains a very basic Convolutional Neural Network (CNN) operation using PyTorch. The goal is to understand how an image tensor passes through a convolution layer and an activation function.

---

## 1. Importing Required Libraries

```python
import torch
import torch.nn as nn
````

* `torch` is the main PyTorch library.
* `torch.nn` provides neural network layers such as convolution and activation functions.

---

## 2. Creating a Convolution Layer

```python
conv = nn.Conv2d(
    in_channels=3,
    out_channels=8,
    kernel_size=3,
    padding=1
)
```

This layer performs the convolution operation.

### Parameter Explanation:

* `in_channels = 3`
  The input image has 3 channels (Red, Green, Blue).
* `out_channels = 8`
  The layer will learn 8 different filters, producing 8 feature maps.
* `kernel_size = 3`
  A 3×3 filter slides over the image.
* `padding = 1`
  Padding keeps the output image size the same as the input.

---

## 3. Activation Function (ReLU)

```python
relu = nn.ReLU()
```

* ReLU stands for **Rectified Linear Unit**.
* It replaces all negative values with zero.
* This helps the network learn complex patterns.

---

## 4. Creating a Dummy Input Image

```python
x = torch.randn(1, 3, 64, 64)
```

This represents a batch of images.

### Tensor Shape Meaning:

```
(batch_size, channels, height, width)
```

* `batch_size = 1` → one image
* `channels = 3` → RGB
* `height = 64`, `width = 64` → image size

---

## 5. Applying the Convolution Layer

```python
x = conv(x)
```

* The convolution layer slides its filters over the image.
* Each filter detects a different visual feature such as edges or textures.

### Output Shape:

```
(1, 8, 64, 64)
```

* 8 feature maps are produced.
* Image size remains the same due to padding.

---

## 6. Applying ReLU Activation

```python
x = relu(x)
```

* ReLU removes negative values.
* Keeps only meaningful positive activations.

### Output Shape:

```
(1, 8, 64, 64)
```

The shape does not change.

---

## 7. Summary

* The convolution layer extracts features from the image.
* ReLU introduces non-linearity.
* CNNs preserve spatial information and use fewer parameters than fully connected networks.
* This is the basic building block of all CNN architectures.

---

## Interview Key Point

**Why use CNNs for images?**

CNNs are effective for image data because they preserve spatial structure, reduce parameters through weight sharing, and automatically learn hierarchical features from images.

```

