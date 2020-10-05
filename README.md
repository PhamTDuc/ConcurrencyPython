## Concurrency Python

### Switch Decision
	* **threading:** The OS decides when to switch tasks external  to Python                  (Processors: 1)
	* **asyncio:** The tasks decides when to give up control                                  (Processor: 1)
	* **Multiprocessing:** The processes all run at the same time on different processors     (Processor: Many)

	CPU Bound => Multi Processing
	I/O Bound, Fast I/O, Limited number of Connections => Multi Threading
	I/O Bound, Slow I/O, Many connections => Asyncio