try:
    from motion_db_interface import *
    try:
        from model_db_interface import *
    except:
        print("Warning: morphablegraphs is not installed")
        pass
except:
    print("Error: anim_utils is not installed")
    pass
    
