#要检测自己反向传导得到的偏导函数是否正确，梯度检验
#通过对某一个参数加以及减一个较小的值的差除以2倍较小的值即可近似算出该点偏导值
#因此可以用来检验偏导是否计算正确，较小的值数量级例如在1e-4
#但是由于这种方法的运算效率太低，速度很慢，我们可以使用L-BFGS算法快速的计算偏导数

#![](http://opu8lkq3n.bkt.clouddn.com/17-10-19/8283393.jpg)

