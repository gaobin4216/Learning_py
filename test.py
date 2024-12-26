import cv2

# 读取图像
image = cv2.imread('example.jpg')  # 替换为你的图像路径

# 检查图像是否成功加载
if image is None:
    print("无法读取图像！")
else:
    # 显示图像
    cv2.imshow('Original Image', image)
    
    # 等待用户按下任意键
    cv2.waitKey(0)  # 0 表示无限等待，直到按键事件发生
    
    # 将图像转换为灰度图像
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # 显示灰度图像
    cv2.imshow('Gray Image', gray_image)
    
    # 等待用户按下任意键
    cv2.waitKey(0)
    
    # 保存灰度图像
    cv2.imwrite('gray_image.jpg', gray_image)  # 保存为灰度图像

    # 关闭所有 OpenCV 窗口
    cv2.destroyAllWindows()
