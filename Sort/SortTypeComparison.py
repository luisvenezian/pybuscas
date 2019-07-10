from Sort.TestTimeSort import *
import random

vetor = list(range(0,1000))

# Objeto de teste
st = SortTest(vetor, time.time())
random.shuffle(vetor)
b = st.bubble_sort()

random.shuffle(vetor)
st.start = time.time()
s = st.selection_sort()

random.shuffle(vetor)
st.start = time.time()
i = st.insertion_sort()

print("Resultado:\n\tBubble Sort.: {:.2f} ms\n\tSelection Sort: {:.2f} ms\n\tInsertion Sort: {:.2f} ms".format(b,s,i))
