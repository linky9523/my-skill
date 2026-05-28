# Material Planning Rules

Use these rules to map smartphone product information and selling points into rows for a core material list.

## Base Rows

Always consider these rows unless the user explicitly excludes them:

| 素材分类 | 需求细则 | 需求说明 | 手机展现 | 需求数量 | 优先级 |
|---|---|---|---|---|---|
| KV | 产品 KV | 产品全色 KV | 全色 | 1 | 重点素材 |
| 产品图 / （突出产品定位感） | 基础角度八视图 | 纯正面 | 已确认颜色 | 颜色数 |  |
| 产品图 / （突出产品定位感） | 基础角度八视图 | 纯背面 | 已确认颜色 | 颜色数 |  |
| 产品图 / （突出产品定位感） | 基础角度八视图 | 顶面 | 已确认颜色 | 颜色数 |  |
| 产品图 / （突出产品定位感） | 基础角度八视图 | 底面 | 已确认颜色 | 颜色数 |  |
| 产品图 / （突出产品定位感） | 基础角度八视图 | 左45度正 | 已确认颜色 | 颜色数 |  |
| 产品图 / （突出产品定位感） | 基础角度八视图 | 右45度正 | 已确认颜色 | 颜色数 |  |
| 产品图 / （突出产品定位感） | 基础角度八视图 | 左45度背 | 已确认颜色 | 颜色数 |  |
| 产品图 / （突出产品定位感） | 基础角度八视图 | 右45度背 | 已确认颜色 | 颜色数 |  |
| 场景图 | 静物场景图 | 单色 CMF | 已确认颜色 | 颜色数 | 重点素材 |
| 场景图 | 静物场景图 | 全色静物组合 | 全色 | 1 |  |
| 场景图 | 开箱图 | 开箱图 | TBD | 1 |  |

Add celebrity, outdoor, co-brand, IoT, or accessory KV rows only when the source or user asks for that communication direction.

## Row Granularity

- Use one row for one concrete material requirement.
- Do not pack multiple shots or components into one `需求说明`.
- Split eight-view product renders into eight rows. Each row keeps `需求数量` as the color count, such as `3`; the section can still visually merge `素材分类` and `需求细则`.
- Split combined hardware claims into separate rows when each component needs a separate visual, such as main camera, telephoto, ultrawide, front camera, flash, battery, SoC, antenna, or cooling.
- Keep shared big titles readable by merging repeated `素材分类` and `需求细则` cells in Excel output instead of compressing requirements into one row.

## Design And ID

- Straight screen, narrow bezels, eye protection screen, high brightness, display shape -> `产品图 / 特殊角度 / 屏幕特写`.
- Small straight screen, light body, slim body, hand feel -> `产品图 / 特殊角度 / 中框特写` and `场景图 / 手模图 / 特殊角度握持`.
- Back material, glass, texture, CMF, color process, color-changing process -> `产品图 / 特殊角度 / 背板特写` and CMF still-life rows.
- Deco, camera island, lens module, design ring, integrated camera module -> `产品图 / 特殊角度 / Deco 特写`.
- Button, AI key, custom key, quick launch key -> `产品图 / 特殊角度 / 按键特写` and `场景图 / 手模图 / 按键操作手势`.
- Waterproof, drop resistance, scratch resistance, dust resistance -> scene rows only when a safe visual metaphor or test-like setup can be planned; otherwise add to `待确认项`.

## Hardware And Structure

Map internal or parameter-led selling points to `产品图 / 爆炸图` or structure rows:

- SoC, chip platform, performance engine -> processor/chip exploded view.
- Main camera, sensor size, telephoto, ultrawide, front camera, flash, multispectral sensor -> imaging module exploded view or lens-specific structure rows. If a claim says "quad camera" or "multi camera", split each named component into its own row.
- Battery, charging, bypass charging -> battery/charging structure row and scenario row when use case matters.
- Cooling, graphite, vapor chamber, thermal design -> structure diagram and/or heat map. If combining structure and heat map is uncertain, add a confirmation item.
- Communication antenna, communication chip, weak network, satellite communication -> antenna/communication structure row plus scenario row if user experience is emphasized.
- Motor, speaker, haptics, biometrics -> component close-up or exploded view when it is launch-relevant.

Use quantity `1` by default. Increase quantity when the feature has multiple focal lengths, multiple components, or separate structure and scenario needs.

## Imaging, AI, OS, And Interaction Scenarios

Map user-facing experiences to scene rows:

- Portrait, night portrait, live photo, 4K video, vlog, concert, telephoto, snapshot -> `场景图 / 人物场景图` with the camera capability named in `需求说明`.
- Game, high frame rate, game filter, super resolution, horizontal holding -> `场景图 / 手模图` or `人物场景图` for game environment.
- AI key, one-tap memo, AI translation, AI scan, AI notes -> `场景图 / 手模图` showing vertical holding, button trigger, or screen demo. Add `待确认项` for exact UI screenshots.
- Cross-ecosystem transfer, one-touch transfer, multi-device interaction -> `场景图 / 手模图` showing phone plus target device.
- Sunlight display -> outdoor strong-light scene.
- Night eye protection -> dark room or lights-off scene.
- Weak network communication -> elevator, basement, crowded venue, travel, or other weak-signal scene.
- Cold battery/low-temperature use -> cold outdoor scene.
- Magnetic accessory or power bank -> phone plus accessory scene.

## Priority Rules

Mark `重点素材` when the row supports:

- product positioning or launch KV
- official hero selling points
- visually distinctive CMF/design
- flagship/differentiated hardware
- new or first-time feature in the product line
- a feature that cannot be understood without visual proof

Use `新增` only when the user/source says it is newly added but priority is not yet final. Use blank priority for routine support rows.

## Confirmation Rules

Add a `待确认项` when:

- colors or phone display are not confirmed
- a feature exists but visual execution is unclear
- exact UI screenshots, sample photos, CG, exploded view assets, or structure diagrams are needed
- a claim needs test data or legal/parameter confirmation
- source information conflicts across product pages, PRDs, or user notes

Do not resolve these by inventing details.
