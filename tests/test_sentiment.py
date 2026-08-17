from src.sentiment import build_sentiment_pipeline


def test_pipeline_learns_basic_sentiment_signal():
    model = build_sentiment_pipeline()
    model.fit(["excellent product", "great service", "terrible product", "bad service"], [1, 1, 0, 0])
    predictions = model.predict(["excellent service", "terrible service"])
    assert list(predictions) == [1, 0]
