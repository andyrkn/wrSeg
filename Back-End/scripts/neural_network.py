import keras
import numpy as np
from keras.models import Sequential
from keras.layers import InputLayer, Dense , Dropout


train_data_input = []
train_data_label = []

def get_labels():
    switcher = {
            0: "Adnotation",
            1: "Title",
            2: "Content",
            3: "Footer",
            4: "Page Number",
    }
    data = []
    input = []
    with open("test_data.txt" , "r") as fd:
        for line in fd:
            line_split = line.replace("\n" , "").split(" ")
            input.append(line_split[:1])
            data.append(list(map(float , line_split[1:])))
    labels = model.predict_classes(np.array(data))
    for i in range(len(input)):
        print(input[i] , switcher[labels[i]])


with open("train_data.txt" , "r") as fd:
    for line in fd:
        data = line.replace("\n" , "").split(" ")
        input = list(map(float , data[1:6]))
        label = list(map(float , data[6:]))
        train_data_input.append(input)
        train_data_label.append(label[0])

train_data_input = np.array(train_data_input)
train_data_label = keras.utils.to_categorical(train_data_label, num_classes = 5)

model = keras.models.Sequential()
model.add(InputLayer((5,))) # tuple(x,y,height,width , nearest neighbour distance)
model.add(Dense(500 , activation="tanh"))
model.add(Dense(800 , activation="tanh"))
model.add(Dropout(0.50))
model.add(Dense(500, activation="relu"))
model.add(Dense(5 , activation="softmax")) # adnotation , title , content, footer , page number


model.compile(optimizer = keras.optimizers.SGD(lr = 0.05), loss = "categorical_crossentropy", metrics = ["accuracy"])

model.fit(train_data_input, train_data_label, epochs = 300,  batch_size = 10)

# model.save("test_model.h5")

# model = keras.models.load_model("test_model.h5")

get_labels()
