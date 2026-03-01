# visualization.py

import matplotlib.pyplot as plt
import numpy as np
import os


def save_result(masked_img, fft_hist, low_thr, high_thr, output_dir):
    fig, axes = plt.subplots(1, 2, figsize=(12, 6))

    axes[0].imshow(np.clip(masked_img, 0, 1))
    axes[0].set_title(f"Masked Image\nLow={low_thr}, High={high_thr}")
    axes[0].axis('off')

    axes[1].imshow(fft_hist, cmap='inferno')
    axes[1].set_title("FFT Magnitude Spectrum")
    axes[1].axis('off')

    plt.tight_layout()

    output_path = os.path.join(
        output_dir,
        f"result_low{low_thr:03d}_high{high_thr:03d}.png"
    )

    plt.savefig(output_path, dpi=150)
    plt.close(fig)

    return output_path