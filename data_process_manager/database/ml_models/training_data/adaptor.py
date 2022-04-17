from . import supplier

# functions:
#   Load new training set
#   Load New target set
#   Update training set
#   Update target set


def load_training_set():

    for i in range(len(supplier.TRAINING_SETS)):
        set = supplier.TRAINING_SETS[i]
        __add_training_set__(
            i,
            set['labels'],
            set['description']
        )

        for source in set['sources']:
            values = set['values']
            for date in values:
                __add_training_point(
                    i,
                    source,
                    date,
                    values[date]
                )

    return

def load_target_set():
    
    return 

def update_training_set():
    return

def update_target_set():

    return