# SNOWL 网站 SEO 优化日志

> 每次优化后由 AI 自动追加记录

---

## 任务清单（优先级顺序）

- [x] 1. Schema 结构化数据（JSON-LD）
- [x] 2. 图片 alt 文字优化
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


## 2026-03-27 — 任务2：图片 alt 文字优化

### 执行摘要
修复了 13 个 HTML 文件中的 15 个泛化 alt 属性，替换为符合 WCAG 可访问性和 SEO 要求的描述性 alt 文字。

### 修改文件（13个）
- `4000a1t1.html` — `alt="Thumb"` → `alt="SNOWL 4000A1T1 snap fastener installation tool thumbnail"`
- `4000b1.html` — `alt="Thumbnail 1"` → `alt="SNOWL 4000B1 turn button product photo"`
- `4000b1t1.html` — `alt="Thumb"` → `alt="SNOWL 4000B1T1 turn button installation tool thumbnail"`
- `4000b3.html` — `alt="Thumbnail 1"` → `alt="SNOWL 4000B3 turn button product photo"`
- `4000b5.html` — `alt="Thumbnail 1"` + `alt="Thumbnail 2"` → `alt="SNOWL 4000B5 turn button product photo"` + `alt="SNOWL 4000B5 turn button detail view"`
- `4000b5t.html` — 2个 `alt="Thumb"` → `alt="SNOWL 4000B5T snap fastener installation tool thumbnail 1/2"`
- `4000b6.html` — `alt="Thumbnail 1"` → `alt="SNOWL 4000B6 turn button product photo"`
- `4000b6t.html` — 2个 `alt="Thumb"` → `alt="SNOWL 4000B6T snap fastener installation tool thumbnail 1/2"`
- `4000b7.html` — `alt="Thumbnail 1"` → `alt="SNOWL 4000B7 turn button product photo"`
- `4000b8.html` — `alt="Thumbnail 1/2"` → `alt="SNOWL 4000B8A/B turn button product/detail photo"`
- `4000bs316.html` — `alt="Thumbnail 1"` → `alt="SNOWL 4000BS316 316 stainless steel turn button product photo"`
- `4000d8t1.html` — `alt="Thumb"` → `alt="SNOWL 4000D8T1 snap fastener installation tool thumbnail"`
- `hibur.html` — `alt="Thumb"` → `alt="SNOWL HIBUR snap fastener installation tool thumbnail"`

### alt 命名规范
遵循格式：`SNOWL {产品型号} {产品类型} {视图类型}`
- 产品类型：snap fastener, turn button, nylon button, installation tool
- 视图类型：product photo, detail view, thumbnail 1/2, installation tool thumbnail

### 注意
- `#lightbox-img` 占位符 `<img>` 保持 `alt=""`（由 JS 动态填充，非 SEO 问题）
- LOGO 等已有明确 alt 文字，无需修改

### Git 提交
```
feat(seo): improve image alt text with descriptive labels across product pages
13 files changed, 15 insertions(+), 15 deletions(-)
Pushed to origin/main ✓
```

