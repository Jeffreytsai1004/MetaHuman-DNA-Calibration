# DNACalib
这个库用于对DNA文件进行修改。
它是用C++编写的，还有一个Python包装器。 [SWIG](https://www.swig.org/)库用于生成
Python的绑定。DNACalib可以在命令行中使用，也可以在Maya中使用。
提供了Windows和Linux的二进制文件。 **如果您使用的是不同的架构和/或平台，您必须构建DNACalib。**

## DNACalib文件夹结构
- [`DNACalib`](/dnacalib/DNACalib) - 包含DNACalib和其依赖项的C++源代码。还有一个用于
读取和写入DNA文件的库，以及其他几个实用程序库。
- [`PyDNACalib`](/dnacalib/PyDNACalib) - 包含生成DNACalib的Python包装器的源代码。
- [`PyDNA`](/dnacalib/PyDNA) - 包含生成DNA库的Python包装器的源代码，该库位于
包含C++源代码的DNACalib文件夹下。
- [`SPyUS`](/dnacalib/SPyUS) - 包含PyDNACalib和PyDNA共同使用的一些常见SWIG接口文件。
- [`CMakeModulesExtra`](/dnacalib/CMakeModulesExtra) - 包含项目中在C++和Python包装器中广泛使用的一些常见CMake函数。

## 用法

例如，要更改中性关节的旋转值，请使用
[`SetNeutralJointRotationsCommand`](/dnacalib/DNACalib/include/dnacalib/commands/SetNeutralJointRotationsCommand.h)。

以下是一个示例，它读取DNA，将所有中性关节的旋转值更改为`{1, 2, 3}`，并用这些新值覆盖DNA
文件。

```

// 创建DNA读取器
auto inOutStream = dnac::makeScoped<dnac::FileStream>("example.dna",
                                                      dnac::FileStream::AccessMode::ReadWrite,
                                                      dnac::FileStream::OpenMode::Binary);
auto reader = dnac::makeScoped<dnac::BinaryStreamReader>(inOutStream.get());
reader->read();

// 检查读取DNA文件时是否发生错误
if (!dnac::Status::isOk()) {
    // 处理读取器错误
}

// 创建DNACalib读取器以编辑DNA
auto dnaReader = dnac::makeScoped<dnac::DNACalibDNAReader>(reader.get());

std::vector<dnac::Vector3> rotations{dnaReader->getJointCount(), {1.0f, 2.0f, 3.0f}};

// 创建命令实例
dnac::SetNeutralJointRotationsCommand cmd{dnac::ConstArrayView<dnac::Vector3>{rotations}};

// 执行命令
cmd.run(dnaReader.get());

// 写入DNA文件
auto writer = dnac::makeScoped<dnac::BinaryStreamWriter>(inOutStream.get());
writer->setFrom(dnaReader.get());
writer->write();

// 检查写入DNA文件时是否发生错误
if (!dnac::Status::isOk()) {
    // 处理写入器错误
}
```

## 示例

### C++
可以在[这里](/dnacalib/DNACalib/examples)找到使用C++库的示例。

这些是：
- [链接多个命令](/dnacalib/DNACalib/examples/CommandSequence.cpp)
- [重命名混合形状](/dnacalib/DNACalib/examples/SingleCommand.cpp)

### Python
可以在[这里](/examples)找到从Python使用该库的示例。

这些是：
- [展示一些命令](/examples/dnacalib_demo.py)
- [重命名关节](/examples/dnacalib_rename_joint_demo.py)
- [从头开始创建一个小DNA](/examples/dna_demo.py)
- [通过提取特定LOD从现有DNA创建新的DNA](/examples/dnacalib_lod_demo.py)
- [读取二进制DNA并以人类可读的格式写入](/examples/dna_binary_to_json_demo.py)
- [移除一个关节](/examples/dnacalib_remove_joint.py)
- [清除混合形状数据](/examples/dnacalib_clear_blend_shapes.py)
- [从中性网格中减去值](/examples/dnacalib_neutral_mesh_subtract.py)


## 构建
提供了64位Windows和Linux的预构建二进制文件 [provided](/lib).
如果您使用的是不同的架构和/或平台，您必须构建DNACalib。

先决条件：
- [CMake](https://cmake.org/download/) 至少3.14版本
- [SWIG](https://www.swig请确保你的系统已安装以下软件：
- [CMake](https://cmake.org/download/) 至少版本 4.0.0
- [Python](https://www.python.org/downloads/) 若要指定要使用的 python3 的确切版本，请设置 CMake 变量 `PYTHON3_EXACT_VERSION`。例如，要使用 Maya 2022 中的库，请使用版本 3.7。对于 Maya 2023，请使用版本 3.9。

使用 CMake 生成构建所需的构建脚本，例如，通过从 [`MetaHuman-DNA-Calibration/dnacalib/`](/dnacalib) 目录执行以下命令：

```
mkdir build
cd build
cmake ..
```

接着，开始构建过程：
```
cmake --build
```
