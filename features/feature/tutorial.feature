Feature: Test Feature
  
  Background: 
    Given 设置全局请求超时时间为0.5秒

  @skip
  Scenario Outline: 基础测试

    When 请求的接口地址是<path>
    And 设置请求超时时间为5秒
    Then 发送<method>请求
    And 请求返回的状态码为<number>
    And 使用JsonPath校验结果中的$.headers.Host等于httpbin.org
    Examples:
      | path          | method | number |
      | /get          | GET    | 200    |
      | /put          | PUT    | 200    |
      | /delay/$delay | GET    | 200    |

  Scenario: 参数化
    When 请求的接口地址是/anything/$site
    Then 发送GET请求
    And 请求返回的状态码为200
    And 使用RegEx校验结果中的anything/(.*?)"等于$site

  Scenario: 上传文件
    When 请求的接口地址是/anything
    And 添加上传的文件file1,文件名为Match2.png
    Then 发送POST请求
    And 请求返回的状态码为200
    And 使用JsonPath校验返回结果中包含$.files.file1



  Scenario: 缓存相应联系请求
    When 请求的接口地址是/anything
    Then  设置请求的Content-Type为application/json
    Then 设置RequestBody为
     """
     {
       "data": {
           "host": "httpbin",
           "date": "2019"
       },
       "sign": "Hc8SK6shGj^l)p1Kd5J"
     }
     """
    Then 发送POST请求
    And 请求返回的状态码为200
    Then 使用JsonPath提取结果中的$.json.sign, 并缓存为sign
    When 请求的接口地址是/anything
    And 设置RequestParams为
     """
     {"sign":"$sign"}
     """
    Then 发送GET请求