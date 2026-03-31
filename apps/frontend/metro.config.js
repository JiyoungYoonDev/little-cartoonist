const { getDefaultConfig } = require('expo/metro-config');

const config = getDefaultConfig(__dirname);

// Fix @shopify/react-native-skia bundling issue:
// The package's "react-native" field points to "src/index.ts" which has
// unresolvable imports. Force Metro to use "lib/module/index.js" instead.
config.resolver.resolveRequest = (context, moduleName, platform) => {
  if (moduleName === '@shopify/react-native-skia') {
    return {
      filePath:
        require.resolve('@shopify/react-native-skia/lib/module/index.js'),
      type: 'sourceFile',
    };
  }
  return context.resolveRequest(context, moduleName, platform);
};

module.exports = config;
