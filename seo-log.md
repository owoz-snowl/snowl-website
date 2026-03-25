# SNOWL 网站 SEO 优化日志

> 每次优化后由 AI 自动追加记录

---

## 任务清单（优先级顺序）

- [ ] 1. Schema 结构化数据（JSON-LD）
- [ ] 2. 图片 alt 文字优化
- [ ] 3. 产品页内容补充
- [ ] 4. Meta description 优化
- [ ] 5. 速度优化（WebP / CDN / 缓存）
- [ ] 6. 内容层优化（新闻/视频/about）

---

## 记录

<!-- 新增记录追加在下方 -->


## 2026-03-26 — 任务1：Schema 结构化数据（JSON-LD）

### 执行摘要
为全部 36 个页面添加了 JSON-LD Product + Organization 结构化数据标记。

### 修改详情

**Product Schema**（32个产品页）：
- 4000系列工具页（20个）：4000a1t1, 4000ax, 4000b1, 4000b1t1, 4000b3, 4000b5, 4000b5t, 4000b6, 4000b6t, 4000b7, 4000b8, 4000bn, 4000bs316, 4000c1, 4000c4, 4000c5, 4000c7, 4000d8t1, 4000dx, 4000rx
- OWOZ系列（8个）：owoz-800000x ~ owoz-800007x, owoz-fastener
- 其他产品（3个）：snap-fastener, nylon-button, turn-button
- 分类页（1个）：tool.html

**Organization Schema**（4个核心页）：
- index.html, about.html, products.html, tool.html

### Schema 内容
每个 Product 页面包含：
- `@type: Product`
- `name`: 从 `<title>` 提取
- `description`: 从 `<meta name="description">` 提取
- `brand`: SNOWL / OWOZ
- `category`: 对应分类
- `mpn`: 产品型号
- `url`: 完整 URL
- `offers`: 价格区间（priceCurrency: USD, InStock）
- `manufacturer` 关联 Organization

每个页面还包含 Organization Schema（`@id: https://snowl.top/#organization`），与 Product 互相关联。

### Git 提交
```
feat(seo): add JSON-LD Product + Organization schema to all pages
43 files changed, 2893 insertions(+), 1435 deletions(-)
Pushed to origin/main ✓
```

