import keras
import numpy as np
from keras.models import Sequential
from keras.layers import InputLayer, Dense , Dropout


def build_model():
    model = keras.models.Sequential()
    model.add(InputLayer((4,))) # tuple(x,y,height,width , nearest neighbour distance)
    model.add(Dense(50 , activation="tanh"))
    model.add(Dense(100 , activation="tanh"))
    model.add(Dropout(0.50))
    model.add(Dense(50, activation="relu"))
    model.add(Dense(5 , activation="softmax")) # adnotation , title , content, footer , page number
    model.compile(optimizer = keras.optimizers.Adam(), loss = "categorical_crossentropy", metrics = ["accuracy"])
    return model;


def save_model(model):
	model.save_weights("weights.h5")


def load_model(model):
	model.load_weights("weights.h5")
	model.compile(keras.optimizers.Adam(), loss = "categorical_crossentropy", metrics = ["accuracy"])
	return model


def read_test_data():
    input = []
    with open("test_data.txt" , "r") as fd:
        for line in fd:
            line_split = line.replace("\n" , "").split(" ")
            input.append(list(map(float , line_split)))
    return input

def predict_and_write(model , test_data_input):
    lines = []
    switcher = {
                0: "Adnotation",
                1: "Title",
                2: "Content",
                3: "Footer",
                4: "Page Number",
    }
    test_data_label = model.predict_classes(np.array(test_data_input))
    with open("column_indexes.txt", 'r') as fd:     # load file
        lines = fd.read().splitlines()
    with open("column_indexes.txt" , 'w') as fd:
        for i in range(len(lines)):
            fd.write(lines[i] + " " + switcher[test_data_label[i]] + "\n")

def read_training_data():
    data = []
    input = []
    label = []
    with open("train_data.txt" , "r") as fd:
        for line in fd:
            data = line.replace("\n" , "").split(" ")
            input.append(list(map(float , data[0:4])))
            label.append(list(map(float , data[4:]))[0])
    return (np.array(input) , keras.utils.to_categorical(label, num_classes = 5))


if __name__ == "__main__":
    train_data_input = []
    train_data_label = []
    model  = build_model()
    # model = load_model(build_model())
    train_data_input , train_data_label = read_training_data()
    model.fit(train_data_input, train_data_label, epochs = 300 ,  batch_size = 20)
    # save_model(model)
    test_data = read_test_data()
    predict_and_write(model , test_data)
