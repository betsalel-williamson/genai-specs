# Egui Menu Interaction Guidelines

## Problem: Dropdown Menus in Submenus Close Parent Menu

### Issue Description

When using `egui::ComboBox` (dropdown menus) inside submenus, clicking on the dropdown causes the parent menu to close, preventing users from making selections. This is a common egui behavior where interactive widgets in menus can trigger menu closure.

### Root Cause

- `egui::ComboBox::selectable_value()` triggers menu closure when clicked
- Parent menus interpret the click as "user wants to close menu"
- This prevents users from actually selecting dropdown options

### Solutions

#### ✅ **Solution 1: Use Radio Buttons (Recommended)**

For simple selections with 2-4 options, use radio buttons instead of dropdowns:

```rust
// ✅ GOOD: Radio buttons for simple choices
ui.label("Format:");
let png_selected = ui.radio(settings.format == Format::Png, "PNG").clicked();
let jpeg_selected = ui.radio(settings.format == Format::Jpeg, "JPEG").clicked();

if png_selected || jpeg_selected {
    // Handle selection
    msgs.push(Message::UpdateSettings(settings));
}
```

**Benefits:**

- No menu closure issues
- Better UX for small option sets
- Clear visual feedback
- Works reliably in nested menus

#### ✅ **Solution 2: Use Collapsing Headers**

For larger option sets, use collapsing headers:

```rust
// ✅ GOOD: Collapsing header for many options
ui.collapsing("Resolution Settings", |ui| {
    ui.radio_value(&mut settings.resolution, Resolution::Auto, "Auto");
    ui.radio_value(&mut settings.resolution, Resolution::Standard, "1x Standard");
    ui.radio_value(&mut settings.resolution, Resolution::HighDpi, "2x High DPI");
    ui.radio_value(&mut settings.resolution, Resolution::Retina, "3x Retina");
});
```

#### ❌ **Avoid: Dropdowns in Menus**

```rust
// ❌ BAD: Dropdown in menu causes parent menu to close
egui::ComboBox::from_id_salt("format_combo")
    .selected_text(settings.format.display_name())
    .show_ui(ui, |ui| {
        ui.selectable_value(&mut settings.format, Format::Png, "PNG");
        ui.selectable_value(&mut settings.format, Format::Jpeg, "JPEG");
    });
```

### Guidelines for Menu UI Components

#### **Use Radio Buttons When:**

- ✅ 2-4 options maximum
- ✅ Simple, mutually exclusive choices
- ✅ Options have short, clear labels
- ✅ Inside nested menus or submenus

#### **Use Collapsing Headers When:**

- ✅ 4+ options
- ✅ Related settings that can be grouped
- ✅ Options need longer descriptions
- ✅ Want to save vertical space

#### **Use Dropdowns Only When:**

- ✅ Outside of menus (main UI areas)
- ✅ Many options (10+ items)
- ✅ Options have long names that would clutter radio buttons
- ✅ Space is extremely limited

### Implementation Pattern

```rust
pub fn settings_menu(&self, ui: &mut egui::Ui, msgs: &mut Vec<Message>) {
    let mut settings = self.user.settings.clone().unwrap_or_default();

    ui.label("Settings");
    ui.separator();

    // ✅ Format selection with radio buttons
    ui.label("Format:");
    let png_selected = ui.radio(
        settings.format == Format::Png,
        Format::Png.display_name()
    ).clicked();

    let jpeg_selected = ui.radio(
        settings.format == Format::Jpeg,
        Format::Jpeg.display_name()
    ).clicked();

    if png_selected || jpeg_selected {
        msgs.push(Message::UpdateSettings(settings.clone()));
    }

    // ✅ Resolution with collapsing header for more options
    ui.collapsing("Resolution", |ui| {
        for resolution in [Resolution::Auto, Resolution::Standard, Resolution::HighDpi, Resolution::Retina] {
            ui.radio_value(&mut settings.resolution, resolution, resolution.display_name());
        }
    });

    // ✅ Simple checkbox
    ui.checkbox(&mut settings.include_ui, "Include UI")
        .clicked()
        .then(|| {
            msgs.push(Message::UpdateSettings(settings.clone()));
        });
}
```

### Testing Checklist

Before implementing menu UI components, verify:

- [ ] **No dropdowns in submenus** - Use radio buttons or collapsing headers instead
- [ ] **Radio buttons for 2-4 options** - Simple, clear selections
- [ ] **Collapsing headers for 4+ options** - Grouped, space-efficient
- [ ] **Proper message handling** - Settings update when selections change
- [ ] **Visual feedback** - Clear indication of current selection
- [ ] **Accessibility** - All options are easily selectable

### Common Anti-Patterns to Avoid

❌ **Dropdown in submenu** - Causes parent menu closure
❌ **Too many radio buttons** - Clutters the UI
❌ **No visual feedback** - Users can't see current selection
❌ **Missing message handling** - Selections don't persist
❌ **Inconsistent patterns** - Mixing radio buttons and dropdowns arbitrarily

### Related Issues

This guideline addresses the recurring pattern where:

1. Developer implements dropdown in menu
2. User reports "can't select options"
3. Developer switches to radio buttons
4. Problem is solved

By following this guideline from the start, we can avoid this cycle and create better UX.

---

**Last Updated:** December 2024
**Applies To:** All egui menu implementations
**Priority:** High - Prevents recurring UX issues
