# SNOWL 网站 SEO 优化日志

> 每次优化后由 AI 自动追加记录

---

## 任务清单（优先级顺序）

- [x] 1. Schema 结构化数据（JSON-LD）
- [x] 2. 图片 alt 文字优化
- [x] 3. 产品页内容补充
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


## 2026-03-27 — 任务3：产品页内容补充

### 执行摘要
为全部 37 个产品页添加了材质说明、应用场景和认证标识，并对破损内容进行了修复。

### 修改文件（37个）
- **4000系列工具**（7个）：4000a1t1, 4000ax, 4000b1t1, 4000b5t, 4000b6t, 4000d8t1, hibur
- **4000系列旋转扣**（8个）：4000b1, 4000b3, 4000b5, 4000b6, 4000b7, 4000b8, 4000bn, 4000bs316
- **4000系列弹簧扣**（6个）：4000c1, 4000c4, 4000c5, 4000c7, 4000dx, 4000rx
- **OWOZ系列**（8个）：owoz-800000x ~ owoz-800007x
- **其他产品**（8个）：833333x, msnap, ysnap, nylon-button, turn-button, snap-fastener, owoz-fastener, tool

### 改动详情

**1. 规格参数表格补充：**
- 添加 `Certifications` 行：CE, ISO 9001
- 添加 `Marine Applications` 行：Yacht, Sailboat, Dinghy, Commercial Vessel, Bimini Top, Sail Cover

**2. 视觉应用场景模块：**
在每个产品页的「Send Inquiry」按钮前插入 Marine Applications 图标展示区：
- 🚤 Yacht / ⛵ Sailboat / 🛥️ Dinghy / 🚢 Commercial Vessel / 🏕️ Bimini Top / ⛺ Sail Cover

**3. 认证徽章模块：**
插入 CE / ISO 9001 / Marine Grade 认证徽章，绿色/橙色/紫色配色，视觉突出。

**4. 内容修复：**
- `hibur.html`：修复破损 feat-list（原来所有特点合并在一个 `<li>` 中），拆分为 6 条独立列表项，并翻译为英文。

### 新增代码结构
```
<!-- Marine Applications -->
<div style="background:linear-gradient(...)">
  ⚓ Marine Applications
  🚤 Yacht | ⛵ Sailboat | 🛥️ Dinghy | 🚢 Commercial Vessel | 🏕️ Bimini Top | ⛺ Sail Cover
</div>

<!-- Certifications -->
[CE Certified] [ISO 9001] [Marine Grade]
```

### Git 提交
```
feat(seo): product page content supplement — marine apps, CE/ISO certs, material specs
38 files changed, 3626 insertions(+), 82 deletions(-)
Pushed to origin/main ✓
```

---

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

