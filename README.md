# CS337_Project3

Video: https://www.youtube.com/watch?v=uY-sty3dDPw
Github Link: https://github.com/jemmons27/CS337_Project3
Python Version: 3.9.6

Can set up .venv or .conda environment with pip install -r requirements.txt
To finish setting up environment, run "python -m spacy download en_core_web_sm" from terminal

Required Transformations:
- Different cuisine (Chinese cuisine) in cuisine.py
- Healthy in healthy.py
- Vegetarian in vegetarian.py

Additional Transformations:
- Different cuisine (Peruvian cuisine) in cuisine.py
- Cooking method/time in cooking_method.py


Each file should be run independently when testing. Urls can be changed to test different recipes, these are found at:
vegetarian.py - line 65, outputs into veg.txt
healthy.py - line 57, outputs into healthy.txt 
cooking_method.py - line 170, outputs into cm.txt
cuisine.py - line 245, outputs into cuisine.txt


Additionally, cuisine can be changed from Chinese to Peruvian at line 282


# There are example use cases in every transformation file showing how to use each transformation.
