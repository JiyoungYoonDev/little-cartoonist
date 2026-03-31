import { View, Text, Pressable, ScrollView } from 'react-native';
import { router } from 'expo-router';
import { TEACHERS } from '../constants/teachers';

export default function TeacherSelectScreen() {
  return (
    <ScrollView
      contentContainerStyle={{
        padding: 24,
        paddingBottom: 40,
      }}
      style={{ flex: 1, backgroundColor: '#FFF8EE' }}
    >
      <Text style={{ fontSize: 32, fontWeight: '800', marginBottom: 8 }}>
        Choose your teacher!
      </Text>
      <Text style={{ fontSize: 16, color: '#666', marginBottom: 24 }}>
        Pick a friendly animal teacher to draw with you
      </Text>

      {TEACHERS.map((teacher) => (
        <Pressable
          key={teacher.id}
          onPress={() =>
            router.push({
              pathname: '/theme-select',
              params: { teacherId: teacher.id },
            })
          }
          style={({ pressed }) => ({
            backgroundColor: 'white',
            padding: 20,
            borderRadius: 20,
            marginBottom: 16,
            flexDirection: 'row',
            alignItems: 'center',
            shadowColor: '#000',
            shadowOffset: { width: 0, height: 2 },
            shadowOpacity: 0.08,
            shadowRadius: 8,
            elevation: 3,
            transform: [{ scale: pressed ? 0.97 : 1 }],
          })}
        >
          <View
            style={{
              width: 70,
              height: 70,
              borderRadius: 35,
              backgroundColor: '#FFF3E0',
              justifyContent: 'center',
              alignItems: 'center',
              marginRight: 16,
            }}
          >
            <Text style={{ fontSize: 36 }}>{teacher.emoji}</Text>
          </View>
          <View style={{ flex: 1 }}>
            <Text style={{ fontSize: 22, fontWeight: '700' }}>
              {teacher.name}
            </Text>
            <Text style={{ fontSize: 14, color: '#888', marginTop: 4 }}>
              {teacher.personality}
            </Text>
          </View>
          <Text style={{ fontSize: 24, color: '#ccc' }}>›</Text>
        </Pressable>
      ))}
    </ScrollView>
  );
}
