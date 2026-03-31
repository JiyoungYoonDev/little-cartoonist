import { useCallback, useRef, useState } from 'react';
import { View } from 'react-native';
import { Canvas, Path, Skia } from '@shopify/react-native-skia';
import { Gesture, GestureDetector } from 'react-native-gesture-handler';

const COLORS = [
  '#000000',
  '#FF3B30',
  '#007AFF',
  '#34C759',
  '#FF9500',
  '#AF52DE',
];

export default function DrawingCanvas({
  style,
  color = '#000000',
  strokeWidth = 3,
  onUndo,
}) {
  const [paths, setPaths] = useState([]);
  const currentPath = useRef(null);
  const [, forceUpdate] = useState(0);

  const pan = Gesture.Pan()
    .minDistance(0)
    .onStart((e) => {
      const path = Skia.Path.Make();
      path.moveTo(e.x, e.y);
      currentPath.current = { path, color, strokeWidth };
      forceUpdate((n) => n + 1);
    })
    .onUpdate((e) => {
      if (currentPath.current) {
        currentPath.current.path.lineTo(e.x, e.y);
        forceUpdate((n) => n + 1);
      }
    })
    .onEnd(() => {
      if (currentPath.current) {
        setPaths((prev) => [...prev, currentPath.current]);
        currentPath.current = null;
        forceUpdate((n) => n + 1);
      }
    });

  const undo = useCallback(() => {
    setPaths((prev) => prev.slice(0, -1));
  }, []);

  // Expose undo to parent
  if (onUndo) {
    onUndo.current = undo;
  }

  return (
    <View style={[{ overflow: 'hidden' }, style]}>
      <GestureDetector gesture={pan}>
        <Canvas style={{ flex: 1 }}>
          {paths.map((p, i) => (
            <Path
              key={i}
              path={p.path}
              color={p.color}
              style='stroke'
              strokeWidth={p.strokeWidth}
              strokeCap='round'
              strokeJoin='round'
            />
          ))}
          {currentPath.current && (
            <Path
              path={currentPath.current.path}
              color={currentPath.current.color}
              style='stroke'
              strokeWidth={currentPath.current.strokeWidth}
              strokeCap='round'
              strokeJoin='round'
            />
          )}
        </Canvas>
      </GestureDetector>
    </View>
  );
}

export { COLORS };
