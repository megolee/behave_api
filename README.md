# Behave API
> 一个基于Python Behave的接口测试小框架，还要不断完善呀


### 环境要求
   
   * Python3.7
   * 安装pipenv https://docs.pipenv.org/en/latest/
   * Pipfile中的各种依赖 ```pipenv install```
   
### 使用方法

   * 在```features/feature```文件夹下编写接口测试脚本feature文件 
   * 在```config/project.ini```文件中配置各种变量，在feature文件中使用```$name```来引用变量
   * 关于文件上传，将文件放在```files``` 文件夹下，并使用对应的关键字即可
   * 关于使用不用的环境变量，```config/project.ini```文件中配置不同的Section，然后在运行脚本是使用命令```behave -Denv=Prd```，
   默认情况下使用Default
   * 默认请求超时时间为1秒，可以使用关键字对其进行修改
   * 使用Allure生成报告 ```behave -f allure_behave.formatter:AllureFormatter -o allure/results```，查看生成的报告 ```allure serve allure/results```
   
### 可用关键字
    
   * 请求相关
     * 设置全局请求超时时间为{timeout:f}秒
     * 设置全局请求头信息为
     * 设置全局Cookies信息为{cookies}
     > 以上三个关键字可以在Background中使用，设置整个Feature文件中Http请求的timeout,header,cookies的默认值，在Scenario中可以使用下面关于
     timeout,header,cookies关键字对单独的Http请求的这些值进行修改
     * 请求的接口地址是{path}
     * 设置请求头信息为
     * 设置请求的Content-Type为{content_type}
     * 设置Cookies信息为{cookies}
     * 设置请求超时时间为{timeout:f}秒
     * 设置RequestBody为
     * 设置RequestParams为
     * 添加上传的文件{key},文件名为{file_name}
     * 发送{method}请求
   
   * 响应相关
     * 请求返回的状态码为{expect_status_code:d}
     * 使用JsonPath校验结果中的{expression}等于{expect_value}
     * 使用JsonPath提取结果中的{expression}, 并缓存为{name}
     * 使用JsonPath校验返回结果中包含{expression}
     * 使用RegEx校验结果中的{expression}等于{expect_value}
     * 使用RegEx提取结果中的{expression}, 并缓存为{name}
     * 校验返回结果等于{expect_value}
   
### 特别注意

   * 在使用cookies时，需要将获取的cookies字符串中的```%替换为%%```