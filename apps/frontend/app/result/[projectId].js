import { View, Text, Pressable } from 'react-native';
import { useLocalSearchParams, router } from 'expo-router';
import { TEACHERS } from '../../constants/teachers';
import { THEMES } from '../../constants/themes';

export default function ResultScreen() {
  const { projectId, teacherId, theme } = useLocalSearchParams();
  const teacher = TEACHERS.find((t) => t.id === teacherId) || TEACHERS[0];
  const themeData = THEMES.find((t) => t.id === theme);

  return (
    <View
      style={{
        flex: 1,
        justifyContent: 'center',
        alignItems: 'center',
        backgroundColor: '#FFF8EE',
        padding: 32,
      }}
    >
      <Text style={{ fontSize: 60 }}>{'\uD83C\uDF89'}</Text>
      <Text style={{ fontSize: 32, fontWeight: '800', marginTop: 16 }}>
        Great Job!
      </Text>
      <Text
        style={{
          fontSize: 18,
          color: '#666',
          marginTop: 8,
          textAlign: 'center',
        }}
      >
        You finished your drawing!
      </Text>

      <View
        style={{
          backgroundColor: 'white',
          padding: 20,
          borderRadius: 20,
          marginTop: 24,
          width: '100%',
          alignItems: 'center',
          shadowColor: '#000',
          shadowOffset: { width: 0, height: 2 },
          shadowOpacity: 0.08,
          shadowRadius: 8,
          elevation: 3,
        }}
      >
        <Text style={{ fontSize: 50 }}>{teacher.emoji}</Text>
        <Text
          style={{
            fontSize: 16,
            textAlign: 'center',
            marginTop: 12,
            color: '#555',
          }}
        >
          {teacher.name} says:{'\n'}
          <Text style={{ fontWeight: '700' }}>
            "What a wonderful drawing! I loved drawing with you!"
          </Text>
        </Text>
      </View>

      <View
        style={{
          backgroundColor: '#F0F8FF',
          padding: 16,
          borderRadius: 16,
          marginTop: 16,
          width: '100%',
        }}
      >
        <Text style={{ fontWeight: '700', fontSize: 16, marginBottom: 8 }}>
          {'\uD83D\uDCD6'} Your Story
        </Text>
        <Text style={{ color: '#555', fontStyle: 'italic', lineHeight: 22 }}>
          Once upon a time, a little artist created a beautiful drawing
          {themeData ? ` about ${themeData.name.toLowerCase()}` : ''}...
          {'\n\n'}The end was just the beginning of another adventure!
        </Text>
        <Text style={{ color: '#999', marginTop: 8, fontSize: 12 }}>
          Full story generation coming in Sprint 2!
        </Text>
      </View>

      <Pressable
        onPress={() => router.replace('/')}
        style={({ pressed }) => ({
          marginTop: 32,
          backgroundColor: '#4CAF50',
          paddingVertical: 16,
          paddingHorizontal: 48,
          borderRadius: 30,
          transform: [{ scale: pressed ? 0.97 : 1 }],
        })}
      >
        <Text style={{ color: 'white', fontSize: 18, fontWeight: '700' }}>
          {'\uD83C\uDFA8'} Draw Again!
        </Text>
      </Pressable>
    </View>
  );
}
