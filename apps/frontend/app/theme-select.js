import { View, Text, Pressable, ScrollView } from 'react-native';
import { router, useLocalSearchParams } from 'expo-router';
import { THEMES } from '../constants/themes';

export default function ThemeSelectScreen() {
  const { teacherId } = useLocalSearchParams();

  const handleThemeSelect = (themeId) => {
    const projectId = `draft-${Date.now()}`;
    router.push({
      pathname: `/draw/${projectId}`,
      params: { teacherId, theme: themeId },
    });
  };

  return (
    <ScrollView
      contentContainerStyle={{
        padding: 24,
        paddingBottom: 40,
      }}
      style={{ flex: 1, backgroundColor: '#F0F8FF' }}
    >
      <Text style={{ fontSize: 32, fontWeight: '800', marginBottom: 8 }}>
        What do you want to draw?
      </Text>
      <Text style={{ fontSize: 16, color: '#666', marginBottom: 24 }}>
        Pick a theme for your drawing adventure
      </Text>

      <View
        style={{
          flexDirection: 'row',
          flexWrap: 'wrap',
          justifyContent: 'space-between',
        }}
      >
        {THEMES.map((theme) => (
          <Pressable
            key={theme.id}
            onPress={() => handleThemeSelect(theme.id)}
            style={({ pressed }) => ({
              width: '48%',
              backgroundColor: 'white',
              padding: 20,
              borderRadius: 20,
              marginBottom: 16,
              alignItems: 'center',
              shadowColor: '#000',
              shadowOffset: { width: 0, height: 2 },
              shadowOpacity: 0.08,
              shadowRadius: 8,
              elevation: 3,
              transform: [{ scale: pressed ? 0.95 : 1 }],
            })}
          >
            <Text style={{ fontSize: 40, marginBottom: 8 }}>{theme.emoji}</Text>
            <Text
              style={{ fontSize: 16, fontWeight: '700', textAlign: 'center' }}
            >
              {theme.name}
            </Text>
            <Text
              style={{
                fontSize: 12,
                color: '#888',
                marginTop: 4,
                textAlign: 'center',
              }}
            >
              {theme.description}
            </Text>
          </Pressable>
        ))}
      </View>
    </ScrollView>
  );
}
