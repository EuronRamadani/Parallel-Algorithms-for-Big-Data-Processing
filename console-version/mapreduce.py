import multiprocessing as mp
from collections import defaultdict
from functools import partial

class ParallelMapReduce:
    def __init__(self, n_workers=None):
        self.n_workers = n_workers or max(1, mp.cpu_count() - 1)
        
    def _map_worker(self, chunk, map_func):
        results = []
        for item in chunk:
            mapped = map_func(item)
            results.extend(mapped)
            
        # Local aggregation to reduce communication overhead
        aggregated = defaultdict(list)
        for key, value in results:
            aggregated[key].append(value)
        return list(aggregated.items())
    
    def _reduce_worker(self, key_values_group, reduce_func):
        key, values = key_values_group
        result = reduce_func(key, values)
        return (key, result)
    
    def execute(self, dataset, map_func, reduce_func):
        # Partition data into chunks
        chunk_size = max(1, len(dataset) // self.n_workers)
        chunks = [dataset[i:i + chunk_size] for i in range(0, len(dataset), chunk_size)]
        
        # Map phase
        print(f"Starting map phase with {len(chunks)} chunks across {self.n_workers} workers...")
        with mp.Pool(self.n_workers) as pool:
            map_func_wrapped = partial(self._map_worker, map_func=map_func)
            intermediate = pool.map(map_func_wrapped, chunks)
        
        # Flatten and group intermediate results
        print("Shuffling intermediate results...")
        grouped = defaultdict(list)
        for result_list in intermediate:
            for key, values in result_list:
                grouped[key].extend(values)
                
        # Reduce phase
        print(f"Starting reduce phase with {len(grouped)} keys...")
        with mp.Pool(self.n_workers) as pool:
            reduce_func_wrapped = partial(self._reduce_worker, reduce_func=reduce_func)
            results = pool.map(reduce_func_wrapped, grouped.items())
            
        # Convert results to a dictionary
        return dict(results) 