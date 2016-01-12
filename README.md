逻辑树
===

一个基于Python和nltk的NLP，负责将输入语句按照逻辑树要求进行拆分。


安装方式：
---

* 安装Python 2.6+ (不支持3.0)
* 安装Java
* 安装nltk及其附属包
* 下载并解压STANFORD_PARSER，修改main.py line19中的路径 

<pre>
<code>
parser = stanford.StanfordParser(model_path="D:\\stanfordparser\\stanford-parser-full-2015-04-20\\model\\edu\\stanford\\nlp\\models\\lexparser\\englishPCFG.ser.gz")
</code>
</pre>

程序规则：
---

* “\*"标注规则：首先在第一层中寻找NP，没有NP找VP。最后clean的时候将无符号句子标注为“\*"。
* “\^"标注规则：将所有"\*"前面的成分，分段的合并，标为一句"\^"。
* “\>"标注规则：从"SBAR","TO","PP"but not "of"处分开，并加入"\>"。
* “\_"标注规则：如果"NN"后面为"SBAR",则分开，并将"NN"前后添加"\_"。
* 其他：遇到","和":"将"\>"层数回归。
* 其他：如果分段时候，后一词数少于3，则不分开。




Contributers:
---

* thuxugang
