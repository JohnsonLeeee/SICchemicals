# SICchemicals
为便于硅所碳化物课题组对于药品的管理和使用，用django写的药品管理网站：

- 直接采用django自带的后台管理系统，前端自动跳转并登录后台管理系统；
- 如果是访客，则自动登录：访客只有查询权限，没有删查改权限；
- 如果需要删改药品，需要退出访客账号，并登录管理员账号进行增删改查。