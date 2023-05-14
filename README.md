# Detection-YOLO
In this task, I will show you how you can build an object detection model with your own dataset.
For example, I tried to study a model for detecting buildings from maps. For this, I used the YOLO neural network, the Pillow library and PyTorch, which you must install for this task.
First, I had to collect my own dataset and annotate it. I collected a small dataset that I've shared in my repository. For the annotation I used https://www.makesense.ai/
![1](https://github.com/arik-1998/Detection-YOLO/assets/116187220/affef03f-0463-486d-bb07-b1380b0ea1f3)
After that we export all annotations in YOLO format (txt file) and split our dataset in train and val folders.
In the YOLO documentation, we can find different models, depending on their speed and accuracy.
![Screenshot (17)](https://github.com/arik-1998/Detection-YOLO/assets/116187220/8147bbcb-09d9-4f26-8355-3876f4819648)
I chose the middle one. Click and download it.
After that we must create a (.yaml) file with that information.
![Screenshot (18)](https://github.com/arik-1998/Detection-YOLO/assets/116187220/986c73ac-9714-471c-8aba-beb9fe3cc2d9)
At the end, we collect all the files in one folder with the dataset. We must have "train" and "val" folders, downloaded YOLO model and (.yaml) file.
Run the train script with your own parameters. I have shared example in my repository.
After training, a folder "runs" is created, in which there is a file named "best.pt". This is your best trained model for the training process.
You can use your model with both images and video files. For example, I will try to detect buildings from an image.
![Screenshot (19)](https://github.com/arik-1998/Detection-YOLO/assets/116187220/a2edb133-e8cb-4936-9319-cc8dc9d2483f)
After this script, in "runs" folder created folder "predict", where you can find detection information.
![image0](https://github.com/arik-1998/Detection-YOLO/assets/116187220/11e6dfca-d301-446f-b7db-96483882b511)
As we can see, there are small flaws. This can be fixed by increasing the dataset, since I showed an example of solving such problems with a small dataset.
