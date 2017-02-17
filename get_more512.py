import Oslo_model as om
import pickle


## Getting back the objects:
with open('newobj512.pickle') as f:  # Python 3: open(..., 'rb')
    av7, std7, h_dict7, A = pickle.load(f)

length = len(A.avalanches) - A.t_c - 100
A.add_grain(int(1e6 - length))

with open('newnewobj512.pickle', 'w') as f:  # Python 3: open(..., 'wb')
    pickle.dump([A], f)
