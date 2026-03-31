import { useState, useRef } from 'react';
import { View, Text, Pressable } from 'react-native';
import { router, useLocalSearchParams } from 'expo-router';
import { GestureHandlerRootView } from 'react-native-gesture-handler';
import DrawingCanvas, { COLORS } from '../../components/canvas/DrawingCanvas';
import TeacherCharacter from '../../components/teacher/TeacherCharacter';
import { requestMockAssist } from '../../services/api-client';

export default function DrawScreen() {
  const { projectId, teacherId, theme } = useLocalSearchParams();
  const [teacherLine, setTeacherLine] = useState(
    'What would you like to draw?',
  );
  const [teacherMood, setTeacherMood] = useState('idle');
  const [selectedColor, setSelectedColor] = useState('#000000');
  const undoRef = useRef(null);

  const handleHelp = async () => {
    setTeacherMood('thinking');
    setTeacherLine('Hmm, let me think...');
    const res = await requestMockAssist({ projectId, teacherId, theme });
    setTeacherMood(res.expression || 'happy');
    setTeacherLine(res.teacher_line);
  };

  const handleUndo = () => {
    if (undoRef.current) {
      undoRef.current();
    }
  };

  const handleFinish = () => {
    router.push({
      pathname: `/result/${projectId}`,
      params: { teacherId, theme },
    });
  };

  return (
    <GestureHandlerRootView style={{ flex: 1, backgroundColor: '#F9F4FF' }}>
      {/* Canvas */}
      <DrawingCanvas
        style={{
          flex: 1,
          margin: 16,
          backgroundColor: 'white',
          borderRadius: 24,
        }}
        color={selectedColor}
        strokeWidth={4}
        onUndo={undoRef}
      />

      {/* Teacher Character */}
      <TeacherCharacter
        teacherId={teacherId}
        mood={teacherMood}
        line={teacherLine}
      />

      {/* Color Picker */}
      <View
        style={{
          flexDirection: 'row',
          justifyContent: 'center',
          gap: 10,
          paddingHorizontal: 16,
          paddingBottom: 8,
        }}
      >
        {COLORS.map((c) => (
          <Pressable
            key={c}
            onPress={() => setSelectedColor(c)}
            style={{
              width: 36,
              height: 36,
              borderRadius: 18,
              backgroundColor: c,
              borderWidth: selectedColor === c ? 3 : 0,
              borderColor: '#FFD700',
            }}
          />
        ))}
      </View>

      {/* Toolbar */}
      <View
        style={{
          flexDirection: 'row',
          justifyContent: 'space-around',
          paddingBottom: 28,
          paddingHorizontal: 16,
        }}
      >
        <Pressable
          onPress={handleUndo}
          style={({ pressed }) => ({
            backgroundColor: '#E5E7EB',
            paddingVertical: 14,
            paddingHorizontal: 20,
            borderRadius: 18,
            transform: [{ scale: pressed ? 0.95 : 1 }],
          })}
        >
          <Text style={{ fontSize: 16, fontWeight: '600' }}>
            {'\u21A9\uFE0F'} Undo
          </Text>
        </Pressable>

        <Pressable
          onPress={handleHelp}
          style={({ pressed }) => ({
            backgroundColor: '#8B5CF6',
            paddingVertical: 14,
            paddingHorizontal: 24,
            borderRadius: 18,
            transform: [{ scale: pressed ? 0.95 : 1 }],
          })}
        >
          <Text style={{ color: 'white', fontWeight: '700', fontSize: 16 }}>
            {'\uD83E\uDD16'} Help Me
          </Text>
        </Pressable>

        <Pressable
          onPress={handleFinish}
          style={({ pressed }) => ({
            backgroundColor: '#10B981',
            paddingVertical: 14,
            paddingHorizontal: 24,
            borderRadius: 18,
            transform: [{ scale: pressed ? 0.95 : 1 }],
          })}
        >
          <Text style={{ color: 'white', fontWeight: '700', fontSize: 16 }}>
            {'\u2705'} Finish
          </Text>
        </Pressable>
      </View>
    </GestureHandlerRootView>
  );
}
