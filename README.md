POKRETANJE NA LINUXU
-----------------------
prije pokretanja main programa potrebno je instalirati sve knjižnice iz requirements.txt:
$ pip install -r requirements.txt
i zatim pokrenuti main.py:
$ python main.py --shape-predictor shape_predictor_5_face_landmarks.dat

POKRETANJE NA WINDOSIMA uz pomoć Anaconde
------------------------
stvoriti SmartMirror enviroment i instalirati sve potrebne pakete iz env.txt
$conda env create -f env.txt
i zatim pokrenuti unutar stvorenog env:
$python main.py --shape-predictor shape_predictor_5_face_landmarks.dat