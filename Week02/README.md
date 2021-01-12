优化程序速度的方法：
1、用cprofile ,line_profiler,Intel Vtune等工具分析程序，寻找hotspots,查看程序哪里占用时间最多
2、思考算法复杂度，优化算法复杂度，比如原算法复杂度为O(N2),思考优化如何降为O(N)，甚至降为O(1)
3，用调用速度更快的数据类型，比如nparray对象的调用速度>pandas的
4，采用cython优化重写程序，需要熟悉的是cython的语法和编译
5，最后思考采用并行，用openMP和SIMD的操作

使用CYTHON的建议：
1，cython 所有数据类型都要有type
2,尽量使用c++自带的数据结构 和通用方法
3，numpy使用memoryview传递给C使用，C使用openMP或者Eigen。使用map可以使用类似MATLAB的语法，但是不支持openMP
4，所有内存分配和传递都应该在python中完成，临时变量用c++类构建。
