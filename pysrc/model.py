import autogluon.core as ag
from autogluon.vision import ImagePredictor, ImageDataset

def train_evaluate_model():
    train_set, _, test_set = ImageDataset