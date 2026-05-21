# maimomo-mcp

MCP Server for [墨墨背单词](https://www.maimemo.com) Open API，让 AI 助手可以直接管理你的单词学习数据。

## 安装

```bash
pip install git+https://github.com/2447628824/maimomo-mcp.git
```

## 配置

### 获取 API Token

1. 打开墨墨背单词 App，进入「我的」→「更多设置」→「实验功能」→「开放API」
2. 生成并复制 API Token

### 配置 MCP Client

在 opencode / Claude Desktop 等 MCP 客户端的配置文件中添加：

```json
{
  "mcpServers": {
    "maimemo": {
      "command": "maimemo-mcp",
      "env": {
        "MAIMEMO_API_TOKEN": "你的-API-Token"
      }
    }
  }
}
```

也可以直接编辑 `~/.config/opencode/opencode.jsonc`，server 会自动从中读取 token。

## 工具列表

### 单词查询

| 工具 | 说明 |
|------|------|
| `get_vocabulary` | 根据拼写查询单词信息 |
| `list_vocabulary` | 批量查询单词（按拼写或 ID） |

### 学习管理（公测）

| 工具 | 说明 |
|------|------|
| `get_study_progress` | 获取今日学习进度 |
| `get_today_items` | 获取今日学习单词列表 |
| `query_study_records` | 查询学习记录 |
| `add_words` | 添加单词到学习规划 |
| `advance_study` | 提前复习指定单词 |

### 释义管理

| 工具 | 说明 |
|------|------|
| `list_interpretations` | 获取单词的释义列表 |
| `create_interpretation` | 创建单词释义 |
| `update_interpretation` | 更新指定释义 |
| `delete_interpretation` | 删除指定释义 |

### 助记管理

| 工具 | 说明 |
|------|------|
| `list_notes` | 获取单词的助记列表 |
| `create_note` | 创建单词助记（谐音、词根等） |
| `update_note` | 更新指定助记 |
| `delete_note` | 删除指定助记 |

### 例句管理

| 工具 | 说明 |
|------|------|
| `list_phrases` | 获取单词的例句列表 |
| `create_phrase` | 创建单词例句 |
| `update_phrase` | 更新指定例句 |
| `delete_phrase` | 删除指定例句 |

### 云词本管理

| 工具 | 说明 |
|------|------|
| `list_notepads` | 查询云词本列表 |
| `get_notepad` | 获取云词本详情 |
| `create_notepad` | 创建云词本 |
| `update_notepad` | 更新云词本 |
| `delete_notepad` | 删除云词本 |

## 使用示例

配置完成后，在 AI 助手中可以直接对话：

- 「我今天背了多少单词？」
- 「把 abandon 加入学习规划」
- 「帮我查一下 apple 这个单词」
- 「给我创建一个'考研核心词汇'云词本」

## 环境变量

| 变量 | 说明 | 必填 |
|------|------|------|
| `MAIMEMO_API_TOKEN` | 墨墨 Open API Token | 是 |
| `MAIMEMO_BASE_URL` | API 基础地址 | 否（默认 `https://open.maimemo.com/open`） |

## 开发

```bash
git clone https://github.com/2447628824/maimomo-mcp.git
cd maimomo-mcp
pip install -e .
```

### 本地运行

```bash
# Windows PowerShell
$env:MAIMEMO_API_TOKEN = "你的-Token"
maimemo-mcp

# Linux / macOS
export MAIMEMO_API_TOKEN="你的-Token"
maimemo-mcp
```

也可以直接用 Python 模块启动：

```bash
python -m maimemo_mcp
```

### MCP Inspector 调试

使用 [MCP Inspector](https://github.com/modelcontextprotocol/inspector) 测试工具：

```bash
npx @modelcontextprotocol/inspector maimemo-mcp
```

### 本地 opencode 配置

在 `~/.config/opencode/opencode.jsonc` 中配置指向本地项目：

```json
{
  "mcpServers": {
    "maimemo": {
      "command": "python",
      "args": ["-m", "maimemo_mcp"],
      "cwd": "/path/to/maimomo-mcp",
      "env": {
        "MAIMEMO_API_TOKEN": "你的-Token"
      }
    }
  }
}
```

## License

MIT
