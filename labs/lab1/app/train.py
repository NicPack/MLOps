import pandas as pd
from api.inference import load_model
from api.training import load_data, save_model, train_model

X, y, class_mapping = load_data()

model = train_model(X, y)

save_model(model, "iris_model")


model = load_model("iris_model")
print(model)

data = pd.DataFrame(
    {
        "sepal_length": 5.1,
        "sepal_width": 3.5,
        "petal_length": 1.4,
        "petal_width": 0.2,
    },
    index=[0],
)


prediction = model.predict(data)
print(class_mapping[2])
print(X[47:55])
print(y[47:55])
