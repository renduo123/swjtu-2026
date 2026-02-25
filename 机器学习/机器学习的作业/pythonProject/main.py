# 导入必要库
from keras.datasets import cifar10
from keras.utils import np_utils
from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Activation, BatchNormalization, Dropout
from keras.regularizers import l2
from keras.preprocessing.image import ImageDataGenerator
from keras.callbacks import EarlyStopping
from keras.optimizers import Adam
import numpy as np

# 1. 加载CIFAR-10数据集
print("加载数据...")
(X_train, y_train), (X_test, y_test) = cifar10.load_data()
print(f"训练集形状: {X_train.shape}, 测试集形状: {X_test.shape}")
print(f"训练标签形状: {y_train.shape}, 测试标签形状: {y_test.shape}")

# 2. 数据预处理
print("数据预处理...")
X_train = X_train.astype('float32') / 255.0
X_test = X_test.astype('float32') / 255.0
Y_train = np_utils.to_categorical(y_train, 10)
Y_test = np_utils.to_categorical(y_test, 10)

# 3. 数据增强（移除PIL依赖的亮度参数）
print("配置数据增强...")
datagen = ImageDataGenerator(
    rotation_range=20,          # 随机旋转20度
    width_shift_range=0.2,      # 水平平移20%
    height_shift_range=0.2,     # 垂直平移20%
    horizontal_flip=True,       # 水平翻转
    vertical_flip=True,         # 垂直翻转
    zoom_range=0.2,             # 随机缩放20%
    shear_range=0.2,            # 剪切变换
    fill_mode='nearest'         # 边界填充策略
)
datagen.fit(X_train)

# 4. 构建优化的CNN模型
print("构建模型...")
model = Sequential()

# 第一层卷积块
model.add(Conv2D(32, (3, 3), padding='same', input_shape=X_train.shape[1:], kernel_regularizer=l2(0.0005)))
model.add(BatchNormalization())
model.add(Activation('relu'))
model.add(Conv2D(32, (3, 3), padding='same', kernel_regularizer=l2(0.0005)))
model.add(BatchNormalization())
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Dropout(0.25))

# 第二层卷积块
model.add(Conv2D(64, (3, 3), padding='same', kernel_regularizer=l2(0.0005)))
model.add(BatchNormalization())
model.add(Activation('relu'))
model.add(Conv2D(64, (3, 3), padding='same', kernel_regularizer=l2(0.0005)))
model.add(BatchNormalization())
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Dropout(0.25))

# 第三层卷积块
model.add(Conv2D(128, (3, 3), padding='same', kernel_regularizer=l2(0.0005)))
model.add(BatchNormalization())
model.add(Activation('relu'))
model.add(Conv2D(128, (3, 3), padding='same', kernel_regularizer=l2(0.0005)))
model.add(BatchNormalization())
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Dropout(0.3))

# 全连接层
model.add(Flatten())
model.add(Dense(512, kernel_regularizer=l2(0.0005)))
model.add(BatchNormalization())
model.add(Activation('relu'))
model.add(Dropout(0.5))
model.add(Dense(10, activation='softmax'))

# 5. 编译模型
print("编译模型...")
model.compile(
    loss='categorical_crossentropy',
    optimizer=Adam(learning_rate=0.0001),  # 降低学习率确保稳定训练
    metrics=['accuracy']
)

# 6. 设置早停策略
early_stopping = EarlyStopping(
    monitor='val_accuracy',
    patience=15,           # 延长耐心值以充分训练
    restore_best_weights=True
)

# 7. 训练模型
print("开始训练...")
history = model.fit(
    datagen.flow(X_train, Y_train, batch_size=64),  # 减小batch_size提高稳定性
    steps_per_epoch=len(X_train) // 64,
    epochs=50,
    validation_data=(X_test, Y_test),
    callbacks=[early_stopping],
    verbose=1
)

# 8. 评估模型
print("评估模型...")
score = model.evaluate(X_test, Y_test, verbose=0)
print(f"测试集损失: {score[0]:.4f}")
print(f"测试集准确率: {score[1]:.4f}")
