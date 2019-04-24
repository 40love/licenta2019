# licenta2019

Steps that you have to follow in order to have a working setup:

1. Make sure to download Anaconda for Windows. Anaconda version 3 for Python 3.7 is recommended
2. After installing Anaconda3 on your PC, make sure to add this env variables: "D:\Tools\Anaconda3\Library\bin"; "D:\Tools\Anaconda3" and "D:\Tools\Anaconda3\Scripts"
3. Next step you have to install TenserFlow. For this you have to open the Command Prompt and type "conda create -n tensorflow_env tensorflow" and after you sucesfully run it, also type "conda activate tensorflow_env" and run it aswell.
4. Now you should be able to install Keras, using the same Command Prompt you opened earlier, run the command "pip install keras"
5. After this you should be able to also install NumPy with the help of instruction "pip install numpy"
6. Module Pillow is needed aswell, make sure you install the latest version of it, so I advise you to unistall it first ("pip uninstall Pillow") and the install it again ("pip install Pillow")
7. CV2 will be requiered aswell, so make sure you run ("conda install opencv") and imutilis ("conda install -c pjamesjoyce imutils")

This should be enough so you could compile our Narcis.py file.

