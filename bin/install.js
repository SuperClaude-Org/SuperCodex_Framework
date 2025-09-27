#!/usr/bin/env node
const { run, detectPython, detectPip, isSuperCodexInstalled } = require("./checkEnv");

console.log("🔍 Checking environment...");

let pythonCmd = detectPython();
if (!pythonCmd) {
  console.error("❌ Python 3 is required but not found.");
  process.exit(1);
}
console.log(`✅ Found Python: ${pythonCmd}`);

let pipCmd = detectPip();
if (!pipCmd) {
  console.error("❌ pip is required but not found.");
  process.exit(1);
}
console.log(`✅ Found Pip: ${pipCmd}`);

// Check installation
if (!isSuperCodexInstalled(pipCmd)) {
  console.log("📦 Installing SuperCodex from PyPI...");
  const result = run(pipCmd, ["install", "SuperCodex"], { stdio: "inherit" });
  if (result.status !== 0) {
    console.error("❌ Installation failed.");
    process.exit(1);
  }
  console.log("✅ SuperCodex installed successfully!");
} else {
  console.log("✅ SuperCodex already installed.");
       }
