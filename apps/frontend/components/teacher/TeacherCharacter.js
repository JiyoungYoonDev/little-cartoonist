import { View, Text } from 'react-native';
import { TEACHERS } from '../../constants/teachers';

export default function TeacherCharacter({
  teacherId = 'rabbit',
  mood = 'idle',
  line = '',
}) {
  const teacher =
    TEACHERS.find((t) => t.id === teacherId) || TEACHERS[0];

  const moodEmoji = {
    idle: '🙂',
    talking: '😄',
    happy: '🤩',
    thinking: '🤔',
    surprised: '😮',
  };

  return (
    <View
      style={{
        position: 'absolute',
        left: 18,
        bottom: 110,
        flexDirection: 'row',
      }}
    >
      <View
        style={{
          width: 80,
          height: 80,
          borderRadius: 40,
          backgroundColor: 'white',
          justifyContent: 'center',
          alignItems: 'center',
        }}
      >
        <Text style={{ fontSize: 30 }}>{teacher.emoji}</Text>
        <Text>{moodEmoji[mood]}</Text>
      </View>

      <View
        style={{
          marginLeft: 10,
          backgroundColor: 'white',
          padding: 12,
          borderRadius: 12,
          maxWidth: 220,
        }}
      >
        <Text style={{ fontWeight: '700' }}>
          {teacher.name}
        </Text>

        <Text>{line}</Text>
      </View>
    </View>
  );
}