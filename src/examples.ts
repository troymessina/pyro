/// <reference types="vite/client" />
/**
 * Examples are loaded from src/examples/ (any depth). Each pair of .py and .md
 * files with the same relative path without extension defines one example, e.g.
 * basic-shapes.py + basic-shapes.md → key "basic-shapes", or
 * mechanics/projectile.py + mechanics/projectile.md → key "mechanics/projectile".
 */

const pyModules = import.meta.glob<Record<string, string>>("./examples/**/*.py", {
  query: "?raw",
  import: "default",
  eager: true,
});

const mdModules = import.meta.glob<string>("./examples/**/*.md", {
  query: "?raw",
  import: "default",
  eager: true,
});

/** Strip ./examples/ prefix and extension; keys are stable and unique across subdirs. */
function exampleKeyFromPath(globPath: string, ext: ".py" | ".md"): string {
  const normalized = globPath.replace(/\\/g, "/");
  const withoutPrefix = normalized.replace(/^\.\/examples\//, "");
  if (withoutPrefix.endsWith(ext)) {
    return withoutPrefix.slice(0, -ext.length);
  }
  const base = withoutPrefix.split("/").pop() ?? withoutPrefix;
  return base.endsWith(ext) ? base.slice(0, -ext.length) : base;
}

function segmentToTitle(segment: string): string {
  return segment
    .split("-")
    .map((word) => word.charAt(0).toUpperCase() + word.slice(1))
    .join(" ");
}

function keyToDisplayName(key: string): string {
  return key.split("/").map(segmentToTitle).join(" · ");
}

/** Map of example keys (filename without extension) to their Python source code. */
export const EXAMPLES: Record<string, string> = {};

/** Ordered list of example keys for consistent dropdown/UI ordering. */
export const EXAMPLE_KEYS: string[] = [];

/** Map of example keys to human-readable display names. */
export const EXAMPLE_DISPLAY_NAMES: Record<string, string> = {};

for (const path of Object.keys(pyModules).sort()) {
  const content = pyModules[path];
  if (typeof content !== "string") {
    continue;
  }
  const key = exampleKeyFromPath(path, ".py");
  EXAMPLES[key] = content;
  EXAMPLE_KEYS.push(key);
  EXAMPLE_DISPLAY_NAMES[key] = keyToDisplayName(key);
}

/** Map of example keys to their markdown instructions content. */
export const EXAMPLE_INSTRUCTIONS: Record<string, string> = {};

for (const path of Object.keys(mdModules).sort()) {
  const raw = mdModules[path];
  const content =
    typeof raw === "string"
      ? raw
      : raw && typeof raw === "object" && "default" in raw
        ? (raw as { default: string }).default
        : null;
  if (!content || typeof content !== "string") {
    continue;
  }
  const key = exampleKeyFromPath(path, ".md");
  EXAMPLE_INSTRUCTIONS[key] = content;
}

/** Default code shown when no example is loaded (first example alphabetically). */
const firstKey = EXAMPLE_KEYS[0];
export const DEFAULT_CODE: string = firstKey ? (EXAMPLES[firstKey] ?? "") : "";
