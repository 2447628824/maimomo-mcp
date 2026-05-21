from mcp.server.fastmcp import FastMCP
from .client import get_client

mcp = FastMCP("maimemo")


# ──────────────────────────────────────────────
# 释义 (Interpretations)
# ──────────────────────────────────────────────

@mcp.tool()
async def list_interpretations(voc_id: str) -> str:
    """获取指定单词下自己创建的释义列表

    Args:
        voc_id: 单词 ID
    """
    result = await get_client().get("/api/v1/interpretations", params={"voc_id": voc_id})
    return str(result)


@mcp.tool()
async def create_interpretation(voc_id: str, interpretation: str, tags: str, status: str = "PUBLISHED") -> str:
    """创建单词释义

    Args:
        voc_id: 单词 ID
        interpretation: 释义内容
        tags: 标签列表，逗号分隔，如 "考研,四级"
        status: 状态，可选 PUBLISHED / UNPUBLISHED / DELETED
    """
    data = {
        "interpretation": {
            "voc_id": voc_id,
            "interpretation": interpretation,
            "tags": [t.strip() for t in tags.split(",")],
            "status": status,
        }
    }
    result = await get_client().post("/api/v1/interpretations", json=data)
    return str(result)


@mcp.tool()
async def update_interpretation(id: str, interpretation: str, tags: str, status: str = "PUBLISHED") -> str:
    """更新指定释义

    Args:
        id: 释义 ID
        interpretation: 释义内容
        tags: 标签列表，逗号分隔
        status: 状态，可选 PUBLISHED / UNPUBLISHED / DELETED
    """
    data = {
        "interpretation": {
            "interpretation": interpretation,
            "tags": [t.strip() for t in tags.split(",")],
            "status": status,
        }
    }
    result = await get_client().post(f"/api/v1/interpretations/{id}", json=data)
    return str(result)


@mcp.tool()
async def delete_interpretation(id: str) -> str:
    """删除指定释义

    Args:
        id: 释义 ID
    """
    result = await get_client().delete(f"/api/v1/interpretations/{id}")
    return str(result)


# ──────────────────────────────────────────────
# 助记 (Notes)
# ──────────────────────────────────────────────

@mcp.tool()
async def list_notes(voc_id: str) -> str:
    """获取指定单词下自己创建的助记列表

    Args:
        voc_id: 单词 ID
    """
    result = await get_client().get("/api/v1/notes", params={"voc_id": voc_id})
    return str(result)


@mcp.tool()
async def create_note(voc_id: str, note_type: str, note: str) -> str:
    """创建单词助记

    Args:
        voc_id: 单词 ID
        note_type: 助记类型，如 "谐音"、"词根" 等
        note: 助记内容
    """
    data = {
        "note": {
            "voc_id": voc_id,
            "note_type": note_type,
            "note": note,
        }
    }
    result = await get_client().post("/api/v1/notes", json=data)
    return str(result)


@mcp.tool()
async def update_note(id: str, note_type: str, note: str) -> str:
    """更新指定助记

    Args:
        id: 助记 ID
        note_type: 助记类型
        note: 助记内容
    """
    data = {
        "note": {
            "note_type": note_type,
            "note": note,
        }
    }
    result = await get_client().post(f"/api/v1/notes/{id}", json=data)
    return str(result)


@mcp.tool()
async def delete_note(id: str) -> str:
    """删除指定助记

    Args:
        id: 助记 ID
    """
    result = await get_client().delete(f"/api/v1/notes/{id}")
    return str(result)


# ──────────────────────────────────────────────
# 云词本 (Notepads)
# ──────────────────────────────────────────────

@mcp.tool()
async def list_notepads(limit: int = 10, offset: int = 0, ids: str = "") -> str:
    """查询云词本列表（支持分页和按 ID 筛选）

    Args:
        limit: 查询数量，默认 10
        offset: 偏移量，默认 0
        ids: 云词本 ID 列表，逗号分隔（可选）
    """
    params: dict = {"limit": limit, "offset": offset}
    if ids:
        params["ids"] = [i.strip() for i in ids.split(",")]
    result = await get_client().get("/api/v1/notepads", params=params)
    return str(result)


@mcp.tool()
async def create_notepad(
    status: str, content: str, title: str, brief: str, tags: str
) -> str:
    """创建云词本

    Args:
        status: 状态，可选 PUBLISHED / UNPUBLISHED / DELETED
        content: 云词本内容
        title: 标题
        brief: 简介
        tags: 标签列表，逗号分隔，如 "考研,四级"
    """
    data = {
        "notepad": {
            "status": status,
            "content": content,
            "title": title,
            "brief": brief,
            "tags": [t.strip() for t in tags.split(",")],
        }
    }
    result = await get_client().post("/api/v1/notepads", json=data)
    return str(result)


@mcp.tool()
async def get_notepad(id: str) -> str:
    """获取指定云词本详情

    Args:
        id: 云词本 ID
    """
    result = await get_client().get(f"/api/v1/notepads/{id}")
    return str(result)


@mcp.tool()
async def update_notepad(
    id: str, status: str, content: str, title: str, brief: str, tags: str
) -> str:
    """更新指定云词本

    Args:
        id: 云词本 ID
        status: 状态
        content: 内容
        title: 标题
        brief: 简介
        tags: 标签列表，逗号分隔
    """
    data = {
        "notepad": {
            "status": status,
            "content": content,
            "title": title,
            "brief": brief,
            "tags": [t.strip() for t in tags.split(",")],
        }
    }
    result = await get_client().post(f"/api/v1/notepads/{id}", json=data)
    return str(result)


@mcp.tool()
async def delete_notepad(id: str) -> str:
    """删除指定云词本

    Args:
        id: 云词本 ID
    """
    result = await get_client().delete(f"/api/v1/notepads/{id}")
    return str(result)


# ──────────────────────────────────────────────
# 例句 (Phrases)
# ──────────────────────────────────────────────

@mcp.tool()
async def list_phrases(voc_id: str) -> str:
    """获取指定单词下自己创建的例句列表

    Args:
        voc_id: 单词 ID
    """
    result = await get_client().get("/api/v1/phrases", params={"voc_id": voc_id})
    return str(result)


@mcp.tool()
async def create_phrase(
    voc_id: str, phrase: str, interpretation: str, tags: str, origin: str
) -> str:
    """创建单词例句

    Args:
        voc_id: 单词 ID
        phrase: 例句内容
        interpretation: 例句翻译
        tags: 标签列表，逗号分隔
        origin: 例句来源
    """
    data = {
        "phrase": {
            "voc_id": voc_id,
            "phrase": phrase,
            "interpretation": interpretation,
            "tags": [t.strip() for t in tags.split(",")],
            "origin": origin,
        }
    }
    result = await get_client().post("/api/v1/phrases", json=data)
    return str(result)


@mcp.tool()
async def update_phrase(
    id: str, phrase: str, interpretation: str, tags: str, origin: str
) -> str:
    """更新指定例句

    Args:
        id: 例句 ID
        phrase: 例句内容
        interpretation: 翻译
        tags: 标签列表，逗号分隔
        origin: 来源
    """
    data = {
        "phrase": {
            "phrase": phrase,
            "interpretation": interpretation,
            "tags": [t.strip() for t in tags.split(",")],
            "origin": origin,
        }
    }
    result = await get_client().post(f"/api/v1/phrases/{id}", json=data)
    return str(result)


@mcp.tool()
async def delete_phrase(id: str) -> str:
    """删除指定例句

    Args:
        id: 例句 ID
    """
    result = await get_client().delete(f"/api/v1/phrases/{id}")
    return str(result)


# ──────────────────────────────────────────────
# 学习数据（公测） (Study)
# ──────────────────────────────────────────────

@mcp.tool()
async def get_study_progress() -> str:
    """获取今日学习进度（公测）

    返回今日已完成单词数、总数和学习时长。
    如果当日未打开 App 进行初始化则无法准确计算总数。
    公测期间不保证可用性，需要在 App 中开启自动同步。
    """
    result = await get_client().post("/api/v1/study/get_study_progress")
    return str(result)


@mcp.tool()
async def get_today_items(
    is_finished: bool = False,
    is_new: bool = False,
    voc_ids: str = "",
    spellings: str = "",
    limit: int = 50,
) -> str:
    """获取今日学习单词列表（公测）

    如果当日未打开 App 进行初始化则无法获取。
    公测期间不保证可用性，需要在 App 中开启自动同步。

    Args:
        is_finished: 筛选是否已完成
        is_new: 筛选是否新学单词
        voc_ids: 根据单词 ID 列表查询，逗号分隔，最多 1000，设置后忽略其他筛选条件
        spellings: 根据单词拼写列表查询，逗号分隔，最多 1000，不可与 voc_ids 同时使用
        limit: 最多获取条数，默认 50，最大 1000
    """
    data: dict = {}
    if voc_ids:
        data["voc_ids"] = [v.strip() for v in voc_ids.split(",")]
    elif spellings:
        data["spellings"] = [s.strip() for s in spellings.split(",")]
    else:
        data["is_finished"] = is_finished
        data["is_new"] = is_new
    data["limit"] = limit
    result = await get_client().post("/api/v1/study/get_today_items", json=data)
    return str(result)


@mcp.tool()
async def query_study_records(
    next_study_date_start: str = "",
    next_study_date_end: str = "",
    voc_ids: str = "",
    spellings: str = "",
    as_count: bool = False,
    limit: int = 50,
) -> str:
    """查询学习记录（公测）

    查询场景举例：
    - 获取规划总量：as_count=true
    - 获取未来某天要背的单词数：next_study_date_end="2026-04-01T00:00:00+08:00", as_count=true
    - 获取未来某天要背的单词列表：next_study_date_end="2026-04-01T00:00:00+08:00"
    公测期间不保证可用性，需要在 App 中开启自动同步。

    Args:
        next_study_date_start: 下次学习日期筛选起始（ISO 8601 格式，北京时区）
        next_study_date_end: 下次学习日期筛选截止
        voc_ids: 根据单词 ID 列表查询，逗号分隔，设置后忽略其他筛选条件
        spellings: 根据单词拼写列表查询，逗号分隔，最多 1000
        as_count: 仅计算结果总数，不返回数据列表
        limit: 最多获取条数，默认 50，最大 1000
    """
    data: dict = {}
    if voc_ids:
        data["voc_ids"] = [v.strip() for v in voc_ids.split(",")]
    elif spellings:
        data["spellings"] = [s.strip() for s in spellings.split(",")]
    else:
        next_study_date: dict = {}
        if next_study_date_start:
            next_study_date["start"] = next_study_date_start
        if next_study_date_end:
            next_study_date["end"] = next_study_date_end
        if next_study_date:
            data["next_study_date"] = next_study_date
    data["as_count"] = as_count
    data["limit"] = limit
    result = await get_client().post("/api/v1/study/query_study_records", json=data)
    return str(result)


@mcp.tool()
async def add_words(word_ids: str, advance: bool = False) -> str:
    """添加单词到学习规划（公测）

    公测期间不保证可用性，需要在 App 中开启自动同步。

    Args:
        word_ids: 单词 ID 列表，逗号分隔，最多一次添加 1000 个
        advance: 是否一并提前复习，无需等级限制
    """
    words = [{"id": w.strip()} for w in word_ids.split(",")]
    data = {"words": words, "advance": advance}
    result = await get_client().post("/api/v1/study/add_words", json=data)
    return str(result)


@mcp.tool()
async def advance_study(voc_ids: str) -> str:
    """提前复习指定单词（公测）

    将单词提前到当下马上复习。需要升级到 10 级解锁提前复习功能。
    公测期间不保证可用性，需要在 App 中开启自动同步。

    Args:
        voc_ids: 单词 ID 列表，逗号分隔，最多 1000
    """
    data = {"voc_ids": [v.strip() for v in voc_ids.split(",")]}
    result = await get_client().post("/api/v1/study/advance_study", json=data)
    return str(result)


# ──────────────────────────────────────────────
# 单词 (Vocabulary)
# ──────────────────────────────────────────────

@mcp.tool()
async def get_vocabulary(spelling: str) -> str:
    """根据拼写获取单词信息

    Args:
        spelling: 单词拼写，如 "apple"
    """
    result = await get_client().get("/api/v1/vocabulary", params={"spelling": spelling})
    return str(result)


@mcp.tool()
async def list_vocabulary(spellings: str = "", ids: str = "") -> str:
    """批量查询单词（按拼写或 ID，两种条件互斥）

    Args:
        spellings: 单词拼写列表，逗号分隔，最多 1000
        ids: 单词 ID 列表，逗号分隔，最多 1000
    """
    data: dict = {}
    if spellings:
        data["spellings"] = [s.strip() for s in spellings.split(",")]
    elif ids:
        data["ids"] = [i.strip() for i in ids.split(",")]
    result = await get_client().post("/api/v1/vocabulary/query", json=data)
    return str(result)


# ──────────────────────────────────────────────
# Entry point
# ──────────────────────────────────────────────

def main():
    import sys
    print("maimemo_mcp server starting...", file=sys.stderr, flush=True)
    try:
        mcp.run()
    except Exception as e:
        print(f"maimemo_mcp server crashed: {e}", file=sys.stderr, flush=True)
        raise
