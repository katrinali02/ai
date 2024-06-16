# HW 6 - Neural Nets


## The Objective

This assignment allows you to explore the role and importance of hyperparameters in the design and operation of neural networks (aka neural nets). The supplied code is for a Feedforward Neural Network (FFNN) that classifies handwritten digits in the famous MNIST dataset. Remember the 28 x 28 example digit we saw when learning about neural nets? We saw how it was flattened into a long string of pixel values before being fed to a FFNN for classification. The supplied code does the same. All you have to do is tweak the hyperparameters to see how that impacts classification and report your observations. 


## The Task

Identify the block of code with `# Hyperparameters` as a header. Notice that it lists the following hyperparameters and specifies some values for them:

* `Learning Rate`
* `Batch Size`
* `Epochs`
* `Dropout Rate` (We haven't discussed this in class, but you can read up on it quickly on the Web.)
* `Hidden Layer Size`

Run your code and observe the dynamic output in the output console of your IDE or your terminal. Note that the output shows certain metrics: Training Loss (`loss`), Training Accuracy (`accuracy`), Validation Loss (`val_loss`), and Validation Accuracy (`val_accuracy`). Notice how they change over the epochs. Also shown at the very end is the Test Accuracy, preceded by a line showing the Test Loss (also called simply `loss`) and the Test Accuracy (also called simply `accuracy`).

Now, get tweaking! Start by tweaking one hyperparameter at a time and observe its effect on the training and test metrics. Use your intuition to guide how you change the hyperparameters. For example, changing the learning rate from 0.001 to 0.002 will likely not have a noticeable effect, but changing it to 0.01 or 0.1 certainly will. Once you get a good understanding of the individual hyperparameters, start experimenting by changing more than one of them at a time. For example, what happens if you lower the learning rate down to 0.0001 (that's 1/10th the default provided) but use 10 times as many nodes in the hidden layer as the default? What happens if you add 10 epochs of training or don't train for enough epochs? Does batch size make things interesting? How so? Let your curiosity drive and questions as you experiment. Oh, and keep a log of everything you do. That's a part and parcel of the experimentation step of the scientific method -- keep a detailed log of your experiments so you can report on them. For this assignment, however, you don't have to report on your entire suite of experiments. Read on to know how much to report on.


## The Report

For the report, show a table of 10 different combinations of settings of hyperparameters and discuss them. Your table should have a header row and 10 rows, one for each combination of hyperparameter values. There should be a column for each of the 5 hyperparameters plus a column for each of the aforementioned metrics for training, validation, and test. For the first 5 rows, tweak only one hyperparameter on each row with respect to the defaults, i.e., change one of the default hyperparameters for each combination. For the last 5 rows, tweak two hyperparameters on each row. Below the table, discuss your observation for each row - how changing one hyperparameter compares with the default settings and then what effect changing two at a time had.

How long should your report be? However long it ends up being with your observation described for the 10 combinations of hyperparameter settings. If you can fit the table and your 10 observations on one page, that's fine; if you need more pages, that's fine too. **Also, submit the report on Canvas as a PDF.**


## The Setup

The original code was tested on a Mac running macOS Ventura 13.1 and Python 3.9 running in a virtual environment, but given its simplicity, it should run on any computer with a relatively recent operating system and a recent Python version. A couple of things that needed to be done to test the code:

1. Install Tensorflow within the virtual environment using `pip install tensorflow`.
   
2. Within the folder where Python is installed, the `Install Certificates.command` file needed to be run to install the certificates provided with Python. Not executing this step was preventing the MNIST dataset from being downloaded because Python could not verify the SSL certificate of the server it was trying to connect to.


## The End

That's it! That's all you have to do. Completing this assignment should provide you with an understanding and an appreciation of neural net hyperparameters.
