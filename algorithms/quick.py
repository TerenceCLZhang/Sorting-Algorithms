from misc import finished_animation

def quick_sort_lomuto(arr):
    def partition(low, high):
        pivot = arr[high]
        i = low - 1
        for j in range(low, high):
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
                yield arr, [i, j], [] 
        arr[i + 1], arr[high] = arr[high], arr[i + 1]  
        yield arr, [i + 1, high], [] 
        return i + 1  
    
    def quick_sort_recursive(low, high):
        if low < high:
            gen = partition(low, high)
            try:
                while True:
                    yield next(gen)
            except StopIteration as e:
                pivot = e.value
                
            yield from quick_sort_recursive(low, pivot - 1)
            yield from quick_sort_recursive(pivot + 1, high)
    
    yield from quick_sort_recursive(0, len(arr) - 1)
    
    
def quick_sort_hoare(arr):
    def partition(low, high):
        pivot = arr[low]
        i = low - 1
        j = high + 1
        
        while True:
            i += 1
            while arr[i] < pivot:
                i += 1
            
            j -= 1
            while arr[j] > pivot:
                j -= 1
            
            if i >=j:
                return j

            arr[i], arr[j] = arr[j], arr[i]
            yield arr, [i, j], [] 
    
    def quick_sort_recursive(low, high):
        if low < high:
            gen = partition(low, high)
            try:
                while True:
                    yield next(gen)
            except StopIteration as e:
                pivot = e.value
                
            yield from quick_sort_recursive(low, pivot)
            yield from quick_sort_recursive(pivot + 1, high)
    
    yield from quick_sort_recursive(0, len(arr) - 1)
    

def quick_sort_dutch(arr):
    def partition(low, high):
        pivot = arr[high]
        lt = low
        gt = high
        i = low

        while i <= gt:
            if arr[i] < pivot:
                arr[lt], arr[i] = arr[i], arr[lt]
                yield arr, [lt, i], []
                lt += 1
                i += 1
            elif arr[i] > pivot:
                arr[i], arr[gt] = arr[gt], arr[i]
                yield arr, [i, gt], []
                gt -= 1
            else:
                i += 1
        return lt, gt

    def quick_sort_recursive(low, high):
        if low < high:
            gen = partition(low, high)
            try:
                while True:
                    yield next(gen)
            except StopIteration as e:
                lt, gt = e.value

            yield from quick_sort_recursive(low, lt - 1)
            yield from quick_sort_recursive(gt + 1, high)

    yield from quick_sort_recursive(0, len(arr) - 1)


def quick_sort(arr, scheme="hoare"):
    SCHEME = {
        "lomuto": quick_sort_lomuto,
        "hoare": quick_sort_hoare,
        "dutch": quick_sort_dutch,
    }
    
    if scheme not in SCHEME:
        raise ValueError(f"Invalid partition scheme '{scheme}'. Supported schemes are: {', '.join(SCHEME.keys())}.")
    
    yield from SCHEME[scheme](arr)
    yield from finished_animation(arr)