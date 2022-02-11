import autogluon.core as ag
from autogluon.vision import ImagePredictor, ImageDataset

def train_evaluate_model(num_epochs):
    # Download dataset
    train_set, _, test_set = ImageDataset.from_folders('https://autogluon.s3.amazonaws.com/datasets/shopee-iet.zip')
    print(train_set)

    # Create classifier
    predictor = ImagePredictor()
    predictor.fit(train_set, hyperparameters={'epochs': 2})

    # Train classifier
    fit_result = predictor.fit_summary()
    print('Top-1 train acc: %.3f, val acc: %.3f' %(fit_result['train_acc'], fit_result['valid_acc']))

    image_path = test_set.iloc[0]['image']
    result = predictor.predict(image_path)
    print(result)

    proba = predictor.predict_proba(image_path)
    print(proba)

    bulk_result = predictor.predict(test_set)
    print(bulk_result)

    test_acc = predictor.evaluate(test_set)
    print('Top-1 test acc: %.3f' % test_acc['top1'])