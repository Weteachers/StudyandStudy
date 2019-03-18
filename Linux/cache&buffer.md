buffer是用于存放要输出到disk（块设备）的数据的，而cache是存放从disk上读出的数据。  
这二者是为了提高IO性能的，并由OS管理。  

- 1.Cache：A cache is something that has been "read" from the disk and stored for later use.
  ```
  缓存区，是高速缓存，是位于CPU和主内存之间的容量较小但速度很快的存储器，
  因为CPU的速度远远高于主内存的速度，CPU从内存中读取数据需等待很长的时间，
  而Cache保存着CPU刚用过的数据或循环使用的部分数据，这时从Cache中读取数据会更快，减少了CPU等待的时间，提高了系统的性能。
  
  Cache并不是缓存文件的，而是缓存块的(块是I/O读写最小的单元)；
  Cache一般会用在I/O请求上，如果多个进程要访问某个文件，可以把此文件读入Cache中，
  这样下一个进程获取CPU控制权并访问此文件直接从Cache读取，提高系统性能。
  ```

- 2.Buffer：A buffer is something that has yet to be "written" to disk. 

  ```
  缓冲区，用于存储速度不同步的设备或优先级不同的设备之间传输数据；
  通过buffer可以减少进程间通信需要等待的时间，当存储速度快的设备与存储速度慢的设备进行通信时，
  存储慢的数据先把数据存放到buffer，达到一定程度存储快的设备再读取buffer的数据，在此期间存储快的设备CPU可以干其他的事情。

  Buffer：一般是用在写入磁盘的，例如：某个进程要求多个字段被读入，当所有要求的字段被读入之前已经读入的字段会先放到buffer中。
  ```



