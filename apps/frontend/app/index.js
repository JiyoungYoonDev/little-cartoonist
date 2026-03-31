import { Dimensions, Pressable, View } from 'react-native';
import { router } from 'expo-router';
import { ThemedText } from '@/components/themed-text';
import { ThemedView } from '@/components/themed-view';
import { Image } from 'expo-image';

const { width } = Dimensions.get('window');
const isTablet = width > 768;

export default function HomeScreen() {
  return (
    <ThemedView
      style={{
        flex: 1,
        justifyContent: 'space-between',
        alignItems: 'center',
        paddingVertical: isTablet ? 80 : 50,
        paddingHorizontal: isTablet ? 40 : 20,
      }}
    >
      <View style={{ alignItems: 'center', gap: 12 }}>
        <Image
          source={require('../assets/images/logo/Logo.svg')}
          style={{
            width: isTablet ? 150 : 100,
            height: isTablet ? 150 : 100,
          }}
          contentFit='contain'
        />
        <ThemedText
          type='title'
          style={{
            fontSize: isTablet ? 48 : 32,
            lineHeight: isTablet ? 56 : 40,
            textAlign: 'center',
          }}
        >
          Little Cartoonist
        </ThemedText>
        <ThemedText
          style={{
            fontSize: isTablet ? 24 : 16,
            fontWeight: '600',
            color: '#666',
            textAlign: 'center',
          }}
        >
          Draw with your animal teacher and make your own storybook
        </ThemedText>
      </View>

      <View style={{ alignItems: 'center', marginTop: 20 }}>
        <View
          style={{
            backgroundColor: 'white',
            paddingHorizontal: 24,
            paddingVertical: 16,
            borderRadius: 30,
            marginBottom: 20,
            shadowColor: '#000',
            shadowOffset: { width: 0, height: 4 },
            shadowOpacity: 0.1,
            shadowRadius: 8,
            elevation: 5,
          }}
        >
          <ThemedText
            style={{
              fontSize: isTablet ? 28 : 18,
              fontWeight: 'bold',
              color: '#333',
            }}
          >
            Hi! Want to draw with me? 👋
          </ThemedText>
        </View>

        <Image
          source={require('../assets/images/logo/Logo.svg')}
          style={{
            width: isTablet ? 300 : 200,
            height: isTablet ? 300 : 200,
          }}
          contentFit='contain'
        />
      </View>

      <View style={{ alignItems: 'center', width: '100%', gap: 16 }}>
        <Pressable
          onPress={() => router.push('/teacher-select')}
          style={({ pressed }) => ({
            width: isTablet ? 400 : '90%',
            paddingVertical: isTablet ? 24 : 18,
            backgroundColor: '#4CAF50',
            borderRadius: 30,
            alignItems: 'center',
            transform: [{ scale: pressed ? 0.98 : 1 }],
          })}
        >
          <ThemedText
            style={{
              color: 'white',
              fontSize: isTablet ? 28 : 20,
              fontWeight: '900',
            }}
          >
            🎨 Start Drawing
          </ThemedText>
        </Pressable>
      </View>
    </ThemedView>
  );
}
