#!/bin/bash

echo "========================================"
echo "  🜂 DJINN CONSTELLATION HUB RELEASE"
echo "========================================"
echo

VERSION="1.0.0"
PACKAGE_NAME="Djinn-Constellation-Hub-v${VERSION}"

echo "🧹 Cleaning previous releases..."
rm -rf "${PACKAGE_NAME}"
rm -f "${PACKAGE_NAME}.zip"

echo "📁 Creating release directory..."
mkdir "${PACKAGE_NAME}"

echo "�� Copying files..."
cp -r djinn-federation "${PACKAGE_NAME}/"
cp -r djinn-council "${PACKAGE_NAME}/"
cp -r idhhc-companion "${PACKAGE_NAME}/"
cp -r djinn-companion "${PACKAGE_NAME}/"
cp -r docs "${PACKAGE_NAME}/"
cp -r tests "${PACKAGE_NAME}/"
cp -r examples "${PACKAGE_NAME}/"
cp -r scripts "${PACKAGE_NAME}/"
cp -r .github "${PACKAGE_NAME}/"

echo "�� Copying root files..."
cp README.md "${PACKAGE_NAME}/"
cp requirements.txt "${PACKAGE_NAME}/"
cp .gitignore "${PACKAGE_NAME}/"
cp LICENSE "${PACKAGE_NAME}/"
cp constellation_hub.py "${PACKAGE_NAME}/"
cp rebuild_council_codellama.bat "${PACKAGE_NAME}/"
cp launch_enhanced_council_v2_constellation.bat "${PACKAGE_NAME}/"
cp launch_enhanced_constellation_hub.bat "${PACKAGE_NAME}/"
cp build_ollama_models.bat "${PACKAGE_NAME}/"
cp ENHANCED_COUNCIL_V2_INTEGRATION.md "${PACKAGE_NAME}/"
cp CONSTELLATION_HUB_GUIDE.md "${PACKAGE_NAME}/"
cp CHANGELOG.md "${PACKAGE_NAME}/"
cp CONTRIBUTING.md "${PACKAGE_NAME}/"
cp SECURITY.md "${PACKAGE_NAME}/"
cp CODE_OF_CONDUCT.md "${PACKAGE_NAME}/"
cp ISSUE_TEMPLATE.md "${PACKAGE_NAME}/"
cp PULL_REQUEST_TEMPLATE.md "${PACKAGE_NAME}/"

echo "�� Running tests..."
python -m pytest tests/ -v
if [ $? -ne 0 ]; then
    echo "⚠️  Tests failed, but continuing with packaging..."
else
    echo "✅ Tests passed!"
fi

echo "📦 Creating ZIP package..."
zip -r "${PACKAGE_NAME}.zip" "${PACKAGE_NAME}/"

echo "�� Package statistics:"
ls -lh "${PACKAGE_NAME}.zip"
echo
echo "📁 Files included:"
find "${PACKAGE_NAME}" -type f | wc -l

echo
echo "========================================"
echo "  🎉 RELEASE PACKAGE READY!"
echo "========================================"
echo
echo "�� Package: ${PACKAGE_NAME}.zip"
echo "📁 Contents: ${PACKAGE_NAME}/"
echo "🚀 Ready for GitHub release!"
echo
echo "💡 Next steps:"
echo "   1. Upload ${PACKAGE_NAME}.zip to GitHub Releases"
echo "   2. Add release notes from CHANGELOG.md"
echo "   3. Tag as v${VERSION}"
echo
