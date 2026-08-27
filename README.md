# zxLeafOS2.0正式版

基于 Scratch / 02Engine 构建的网页操作系统，包含完整窗口管理、虚拟文件系统和内置应用生态。

## 项目概况

| 项目 | 数值 |
|---|---|
| 角色（Sprite）总数 | 308 |
| 自定义扩展数量 | 32 |
| 引用资源数 | 706 |
| 项目文件总数 | 724 |

## 目录结构

```
zxLeafOS2.0正式版/
├── README.md              # 本文件
├── LICENSE                # 开源协议
├── .gitignore             # Git 忽略规则
├── project.zip            # 原始 sb3 格式项目包（可直接导入编辑器）
├── src/                   # 解包后的项目源码
│   ├── project.json       # 项目主文件（所有角色、脚本、积木逻辑）
│   ├── *.svg              # 矢量造型资源
│   ├── *.png              # 位图造型资源
│   ├── *.wav              # 声音资源
│   └── *.ttf              # 字体资源
└── tools/
    └── unpack.py          # 从 02Engine HTML 重新解包的脚本
```

## 角色列表

  - 应用
  - 程序切换
  - 桌面右键菜单
  - 应用市场//.a应用市场窗口
  - 应用市场//.a应用市场放大缩小
  - 应用市场//.a应用市场最小化
  - 应用市场//.a应用市场X
  - 应用市场//.a应用市场广告
  - 应用市场//.a应用市场应用介绍窗口
  - 应用市场//.a应用市场应用介绍UI
  - 应用市场//.a应用市场应用介绍X
  - 应用市场//应用下载模块
  - 桌面//应用名称显示
  - 桌面//任务栏【克隆】
  - 桌面//输入框名字
  - 桌面//桌面壁纸
  - 桌面//任务栏
  - 桌面//角色1
  - 桌面//关机画面
  - 桌面//托盘
  - 桌面//托盘控制颜色
  - 桌面//托盘2
  - 桌面//托盘5
  - 桌面//托盘4
  - 桌面//登录
  - 桌面//任务栏按钮
  - 桌面//任务栏托盘按钮
  - 桌面//ai
  - 桌面//应用资源库按钮
  - 桌面//显示桌面按钮
  - ... 及其他 278 个角色

## 自定义扩展

  - `SPmbpCST`
  - `tw`
  - `skyhigh173JSON`
  - `lmsclonesplus`
  - `lmsTempVars2`
  - `mistiumindexeddb`
  - `0832rxfs2`
  - `zx`
  - `filehelperprov2`
  - `lmsAssets`
  - `text`
  - `advancedMonacoEditor`
  - `iframePlus`
  - `lmsLooksPlus`
  - `cyberexplorertoolboxzx`
  - `cst1229zip`
  - `gsaHTTPRequests`
  - `betterText`
  - `enhancedruntimeoptions`
  - `lmsVideo`
  - `zxHtmlPreview`
  - `zxMusicPlayerV2`
  - `theshovelcanvaseffects`
  - `pageosWeatherOpenMeteoFull`
  - `numericalencoding2`
  - `zxTools4`
  - `lmsSoundExpanded`
  - `zxCharacterControl`
  - `speechapi`
  - `WhenKeyPress`
  - `variablesnapshot`
  - `WitCatInput`

## 资源文件类型分布

  - .json: 1 个
  - .svg: 721 个
  - .ttf: 1 个
  - .wav: 1 个

## 使用方式

### 方式一：直接运行
下载 Release 中的 HTML 文件，用浏览器直接打开即可运行。

### 方式二：编辑器中打开
1. 下载 `project.zip`（即 sb3 格式）
2. 使用 [02Engine](https://02engine.02studio.xyz/) 或 Scratch 兼容编辑器打开
3. 查看和编辑所有角色、脚本和资源

### 方式三：从源码构建
1. 将 `src/` 目录下的所有文件打包为 ZIP（确保 project.json 在根目录）
2. 将后缀改为 `.sb3`
3. 用 02Engine Packager 打包为 HTML

## 开发说明

- `src/project.json` 是项目的核心，包含所有角色的脚本和积木逻辑
- 造型和声音文件以 `assetId.ext` 命名，在 project.json 中通过 assetId 引用
- 修改源码后需重新打包为 sb3 才能在编辑器中使用

## 许可证

MIT License（详见 LICENSE 文件）
