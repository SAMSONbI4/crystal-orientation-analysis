# main.py

import os
from config import *
from image_loader import load_and_preprocess
from segmentation import two_threshold_dither, apply_mask_to_original
from fft_analysis import compute_fft_histogram
from visualization import save_result


def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    original_rgb, blurred = load_and_preprocess(INPUT_IMAGE, GAUSS_SIGMA)

    total = 0
    total_expected = (
        ((LOW_THR_MAX - LOW_THR_MIN) // STEP) *
        ((HIGH_THR_MAX - HIGH_THR_MIN) // STEP)
    )

    print(f"Starting processing of {total_expected} parameter combinations...")

    for low_thr in range(LOW_THR_MIN, LOW_THR_MAX, STEP):
        for high_thr in range(HIGH_THR_MIN, HIGH_THR_MAX, STEP):
            if low_thr >= high_thr:
                continue

            mask = two_threshold_dither(blurred, low_thr, high_thr)

            if INVERT_MASK:
                mask = 1.0 - mask

            masked_img = apply_mask_to_original(original_rgb, mask)
            fft_hist = compute_fft_histogram(masked_img)

            output_path = save_result(
                masked_img,
                fft_hist,
                low_thr,
                high_thr,
                OUTPUT_DIR
            )

            total += 1
            print(f"Saved: {output_path}")

    print(f"Processing completed. Total images saved: {total}")


if __name__ == "__main__":
    main()