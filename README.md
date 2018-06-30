# RoadDamageGAN

Data Augmentation using GAN.

1. Crop the bounding boxes from RoadDamageDataset
2. Train generator to generate road damages
3. Compare the classification result among A) Trained by the bounding box images, B) Trained by the bounding box images and augmentated images, C) Trained by the bounding box images and generated images using GAN.
