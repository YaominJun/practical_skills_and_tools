# MATLAB function Usage

## 1. 同一个function 文件下写入多个函数及其调用

第一步，设置总的一个function，该function名称和文件名称一样。</br>
第二步，在该文件中可以任意添加许多小函数，用@符号链接过去即可。</br>
第三步，调用的时候，定义总函数，然后用 . 符号关联到小函数即可。

### 实现堆栈为例
* 定义

        function stack = stackFuns
        stack.pushStack = @pushStack;
        stack.popStack = @popStack;
        end

        function newStack = pushStack(oldStack, newValue)
        %将后来的值插入到数组前面（堆栈），然后取出的时候，先取前面的（后进先出原则）
            newStack = [newValue,oldStack];
        end

        function [newStack,popedValue] = popStack(oldStack)
        %判断堆栈是否为空
            [~, c] = size(oldStack);
            if c < 1
                popedValue = [];
                newStack = oldStack;
                return;
            end
            popedValue = oldStack(1);
            newStack = oldStack(2:end);
        end

* 调用
        
        stack = stackFuns;
        [Stack, CurP] = stack.popStack(Stack);
        Stack = stack.pushStack(Stack, Vertex);



### 实现队列为例
* 定义

        function queue = queueFuns
        queue.enQueue = @enQueue;
        queue.deQueue = @deQueue;
        end

        function newQueue = enQueue(oldQueue, newValue)
        %将后来的值插入到数组后面（队列），然后取出的时候，先取前面的（先进先出原则）
            newQueue = [oldQueue, newValue];
        end

        function [newQueue,popedValue] = deQueue(oldQueue)
        %判断堆栈是否为空
            [~, c] = size(oldQueue);
            if c < 1
                popedValue = [];
                newQueue = oldQueue;
                return;
            end
            popedValue = oldQueue(1);
            newQueue = oldQueue(2:end);
        end

* 调用

        queue = queueFuns;
        [Queue, CurP] = queue.deQueue(Queue);
        Queue = queue.enQueue(Queue, Vertex);

### 实现最小堆/优先级队列为例
* 定义

        function heap = heapFuns
        heap.pushHeap = @pushHeap;
        heap.popHeap = @popHeap;
        end

        function newHeap = pushHeap(oldHeap, newValue)
        %将后来的值找到合适的位置插入，要满足最小堆原理
            len = length(oldHeap);
            newHeap = [];
            for i = 1:len
                if newValue.Q <= oldHeap(i).Q
                    newHeap = [newHeap, oldHeap(1:i-1)];
                    newHeap = [newHeap, newValue];
                    newHeap = [newHeap, oldHeap(i:end)];
                    return;
                end        
            end
            newHeap = [newHeap, oldHeap];
            newHeap = [newHeap, newValue];
        end

        function [newHeap,popedValue] = popHeap(oldHeap)
        %判断堆栈是否为空
            [~, c] = size(oldHeap);
            if c < 1
                popedValue = [];
                newHeap = oldHeap;
                return;
            end
            popedValue = oldHeap(1);
            newHeap = oldHeap(2:end);
        end

* 调用

        heap = heapFuns;
        [OpenSet, CurP] = heap.popHeap(OpenSet);
        Heap = heap.pushHeap(Heap,V);

