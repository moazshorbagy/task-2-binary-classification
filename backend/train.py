import sys, getopt

models = ['neural_n', 'knn']

if __name__ == "__main__":
    model = ''
    try:
        opts, args = getopt.getopt(sys.argv[1:], "m:", ["model="])
    except getopt.GetoptError:
        print('Usage: python train.py -m <modelName>')
        sys.exit(2)

    if len(opts) < 1:
        model = models[0]

    elif opts[0][0] in ("-m", "--model"):
        model = opts[0][1]
        if not model in models:
            print('Error: available models are:', models)
            sys.exit(2)

    if model == models[0]:
        from neural_n_model import train
        print('Neural Network Model')

    elif model == models[1]:
        from knn_model import train
        print('kNN Model')

    train()
