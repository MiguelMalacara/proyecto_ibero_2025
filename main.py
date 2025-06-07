import pandas as pd
import numpy as np 

def numpy_df():
    df = pd.DataFrame(np.random.randn(5, 3), columns=["A", "B", "C"])
    
    print("DataFrame")
    print(df)
    
    arr = df.to_numpy()
    
    print("\nNumpy Array:")
    print(arr)
    
numpy_df()