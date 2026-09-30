#pragma once

// RGB Matrix effects. Each effect gets an unconditional #undef followed by a
// #define - comment out just the #define line to disable that effect.
//
// Why both lines, always: keyboards/keychron/q3/info.json force-enables some
// effects at the board level (rgb_matrix.animations), and that generated
// header compiles before this file. A #define alone can't turn an effect on
// from scratch if it's already off, and commenting out a #define can't turn
// an already-forced-on effect off - only an #undef can. Pairing them and
// controlling only the #define keeps every effect's on/off switch working
// the same way, independent of what the board defaults to.
//
// Descriptions below are from docs/features/rgb_matrix.md's enum comments.
// RGB_MATRIX_SOLID_COLOR is always available and not listed here.

#undef ENABLE_RGB_MATRIX_ALPHAS_MODS
#define ENABLE_RGB_MATRIX_ALPHAS_MODS
// Static dual hue, speed is hue for secondary hue

#undef ENABLE_RGB_MATRIX_GRADIENT_UP_DOWN
#define ENABLE_RGB_MATRIX_GRADIENT_UP_DOWN
// Static gradient top to bottom, speed controls how much gradient changes

#undef ENABLE_RGB_MATRIX_GRADIENT_LEFT_RIGHT
#define ENABLE_RGB_MATRIX_GRADIENT_LEFT_RIGHT
// Static gradient left to right, speed controls how much gradient changes

#undef ENABLE_RGB_MATRIX_BREATHING
//#define ENABLE_RGB_MATRIX_BREATHING
// Single hue brightness cycling animation

#undef ENABLE_RGB_MATRIX_BAND_SAT
//#define ENABLE_RGB_MATRIX_BAND_SAT
// Single hue band fading saturation scrolling left to right

#undef ENABLE_RGB_MATRIX_BAND_VAL
//#define ENABLE_RGB_MATRIX_BAND_VAL
// Single hue band fading brightness scrolling left to right

#undef ENABLE_RGB_MATRIX_BAND_PINWHEEL_SAT
//#define ENABLE_RGB_MATRIX_BAND_PINWHEEL_SAT
// Single hue 3 blade spinning pinwheel fades saturation

#undef ENABLE_RGB_MATRIX_BAND_PINWHEEL_VAL
//#define ENABLE_RGB_MATRIX_BAND_PINWHEEL_VAL
// Single hue 3 blade spinning pinwheel fades brightness

#undef ENABLE_RGB_MATRIX_BAND_SPIRAL_SAT
//#define ENABLE_RGB_MATRIX_BAND_SPIRAL_SAT
// Single hue spinning spiral fades saturation

#undef ENABLE_RGB_MATRIX_BAND_SPIRAL_VAL
//#define ENABLE_RGB_MATRIX_BAND_SPIRAL_VAL
// Single hue spinning spiral fades brightness

#undef ENABLE_RGB_MATRIX_CYCLE_ALL
#define ENABLE_RGB_MATRIX_CYCLE_ALL
// Full keyboard solid hue cycling through full gradient

#undef ENABLE_RGB_MATRIX_CYCLE_LEFT_RIGHT
#define ENABLE_RGB_MATRIX_CYCLE_LEFT_RIGHT
// Full gradient scrolling left to right

#undef ENABLE_RGB_MATRIX_CYCLE_UP_DOWN
#define ENABLE_RGB_MATRIX_CYCLE_UP_DOWN
// Full gradient scrolling top to bottom

#undef ENABLE_RGB_MATRIX_RAINBOW_MOVING_CHEVRON
#define ENABLE_RGB_MATRIX_RAINBOW_MOVING_CHEVRON
// Full gradient Chevron shaped scrolling left to right

#undef ENABLE_RGB_MATRIX_CYCLE_OUT_IN
#define ENABLE_RGB_MATRIX_CYCLE_OUT_IN
// Full gradient scrolling out to in

#undef ENABLE_RGB_MATRIX_CYCLE_OUT_IN_DUAL
//#define ENABLE_RGB_MATRIX_CYCLE_OUT_IN_DUAL
// Full dual gradients scrolling out to in

#undef ENABLE_RGB_MATRIX_CYCLE_PINWHEEL
//#define ENABLE_RGB_MATRIX_CYCLE_PINWHEEL
// Full gradient spinning pinwheel around center of keyboard

#undef ENABLE_RGB_MATRIX_CYCLE_SPIRAL
//#define ENABLE_RGB_MATRIX_CYCLE_SPIRAL
// Full gradient spinning spiral around center of keyboard

#undef ENABLE_RGB_MATRIX_DUAL_BEACON
//#define ENABLE_RGB_MATRIX_DUAL_BEACON
// Full gradient spinning around center of keyboard

#undef ENABLE_RGB_MATRIX_RAINBOW_BEACON
#define ENABLE_RGB_MATRIX_RAINBOW_BEACON
// Full tighter gradient spinning around center of keyboard

#undef ENABLE_RGB_MATRIX_RAINBOW_PINWHEELS
//#define ENABLE_RGB_MATRIX_RAINBOW_PINWHEELS
// Full dual gradients spinning two halves of keyboard

#undef ENABLE_RGB_MATRIX_FLOWER_BLOOMING
//#define ENABLE_RGB_MATRIX_FLOWER_BLOOMING
// Full tighter gradient of first half scrolling left to right and second half scrolling right to left

#undef ENABLE_RGB_MATRIX_RAINDROPS
//#define ENABLE_RGB_MATRIX_RAINDROPS
// Randomly changes a single key's hue

#undef ENABLE_RGB_MATRIX_JELLYBEAN_RAINDROPS
//#define ENABLE_RGB_MATRIX_JELLYBEAN_RAINDROPS
// Randomly changes a single key's hue and saturation

#undef ENABLE_RGB_MATRIX_HUE_BREATHING
#define ENABLE_RGB_MATRIX_HUE_BREATHING
// Hue shifts up a slight amount at the same time, then shifts back

#undef ENABLE_RGB_MATRIX_HUE_PENDULUM
#define ENABLE_RGB_MATRIX_HUE_PENDULUM
// Hue shifts up a slight amount in a wave to the right, then back to the left

#undef ENABLE_RGB_MATRIX_HUE_WAVE
#define ENABLE_RGB_MATRIX_HUE_WAVE
// Hue shifts up a slight amount and then back down in a wave to the right

#undef ENABLE_RGB_MATRIX_PIXEL_FRACTAL
//#define ENABLE_RGB_MATRIX_PIXEL_FRACTAL
// Single hue fractal filled keys pulsing horizontally out to edges

#undef ENABLE_RGB_MATRIX_PIXEL_FLOW
//#define ENABLE_RGB_MATRIX_PIXEL_FLOW
// Pulsing RGB flow along LED wiring with random hues

#undef ENABLE_RGB_MATRIX_PIXEL_RAIN
//#define ENABLE_RGB_MATRIX_PIXEL_RAIN
// Randomly light keys with random hues

#undef ENABLE_RGB_MATRIX_STARLIGHT
//#define ENABLE_RGB_MATRIX_STARLIGHT
// LEDs turn on and off at random at varying brightness, maintaining user set color

#undef ENABLE_RGB_MATRIX_STARLIGHT_DUAL_HUE
//#define ENABLE_RGB_MATRIX_STARLIGHT_DUAL_HUE
// LEDs turn on and off at random at varying brightness, modifies user set hue by +- 30

#undef ENABLE_RGB_MATRIX_STARLIGHT_DUAL_SAT
//#define ENABLE_RGB_MATRIX_STARLIGHT_DUAL_SAT
// LEDs turn on and off at random at varying brightness, modifies user set saturation by +- 30

#undef ENABLE_RGB_MATRIX_RIVERFLOW
//#define ENABLE_RGB_MATRIX_RIVERFLOW
// Modification to breathing animation, offsets animation depending on key location to simulate a river flowing

#undef ENABLE_RGB_MATRIX_TYPING_HEATMAP
//#define ENABLE_RGB_MATRIX_TYPING_HEATMAP
// How hot is your WPM!

#undef ENABLE_RGB_MATRIX_DIGITAL_RAIN
//#define ENABLE_RGB_MATRIX_DIGITAL_RAIN
// That famous computer simulation

#undef ENABLE_RGB_MATRIX_SOLID_REACTIVE_SIMPLE
//#define ENABLE_RGB_MATRIX_SOLID_REACTIVE_SIMPLE
// Pulses keys hit to hue & value then fades value out

#undef ENABLE_RGB_MATRIX_SOLID_REACTIVE
#define ENABLE_RGB_MATRIX_SOLID_REACTIVE
// Static single hue, pulses keys hit to shifted hue then fades to current hue

#undef ENABLE_RGB_MATRIX_SOLID_REACTIVE_WIDE
//#define ENABLE_RGB_MATRIX_SOLID_REACTIVE_WIDE
// Hue & value pulse near a single key hit then fades value out

#undef ENABLE_RGB_MATRIX_SOLID_REACTIVE_MULTIWIDE
//#define ENABLE_RGB_MATRIX_SOLID_REACTIVE_MULTIWIDE
// Hue & value pulse near multiple key hits then fades value out

#undef ENABLE_RGB_MATRIX_SOLID_REACTIVE_CROSS
//#define ENABLE_RGB_MATRIX_SOLID_REACTIVE_CROSS
// Hue & value pulse the same column and row of a single key hit then fades value out

#undef ENABLE_RGB_MATRIX_SOLID_REACTIVE_MULTICROSS
//#define ENABLE_RGB_MATRIX_SOLID_REACTIVE_MULTICROSS
// Hue & value pulse the same column and row of multiple key hits then fades value out

#undef ENABLE_RGB_MATRIX_SOLID_REACTIVE_NEXUS
//#define ENABLE_RGB_MATRIX_SOLID_REACTIVE_NEXUS
// Hue & value pulse away on the same column and row of a single key hit then fades value out

#undef ENABLE_RGB_MATRIX_SOLID_REACTIVE_MULTINEXUS
//#define ENABLE_RGB_MATRIX_SOLID_REACTIVE_MULTINEXUS
// Hue & value pulse away on the same column and row of multiple key hits then fades value out

#undef ENABLE_RGB_MATRIX_SPLASH
//#define ENABLE_RGB_MATRIX_SPLASH
// Full gradient & value pulse away from a single key hit then fades value out

#undef ENABLE_RGB_MATRIX_MULTISPLASH
//#define ENABLE_RGB_MATRIX_MULTISPLASH
// Full gradient & value pulse away from multiple key hits then fades value out

#undef ENABLE_RGB_MATRIX_SOLID_SPLASH
//#define ENABLE_RGB_MATRIX_SOLID_SPLASH
// Hue & value pulse away from a single key hit then fades value out

#undef ENABLE_RGB_MATRIX_SOLID_MULTISPLASH
//#define ENABLE_RGB_MATRIX_SOLID_MULTISPLASH
// Hue & value pulse away from multiple key hits then fades value out
