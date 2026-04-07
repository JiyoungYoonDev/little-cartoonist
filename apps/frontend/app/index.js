import React, { useEffect, useCallback } from 'react';
import { View, StyleSheet, Dimensions } from 'react-native';
import { router } from 'expo-router';
import AsyncStorage from '@react-native-async-storage/async-storage';
import Animated, {
  useSharedValue,
  useAnimatedStyle,
  withTiming,
  withDelay,
  withSequence,
  Easing,
} from 'react-native-reanimated';
import { palette, fonts } from '../constants/tokens';
import { ensureAuth } from '../services/auth';
import LogoSvg from '../assets/images/logo/test1.svg';
import { getChildProfile } from '@/services/children';

const STORAGE_KEY_CHILD_ID = '@littlecartoonist:child_id';
const { width } = Dimensions.get('window');

export default function SplashScreen() {
  // Mascot
  const mascotOpacity = useSharedValue(0);
  const mascotScale = useSharedValue(0.3);
  const mascotTranslateY = useSharedValue(60);
  // Title
  const titleOpacity = useSharedValue(0);
  const titleTranslateY = useSharedValue(20);

  const navigate = useCallback(async () => {
    try {
      await ensureAuth();
    } catch {}

    const childId = await AsyncStorage.getItem(STORAGE_KEY_CHILD_ID);
    if (!childId) {
      router.replace('/onboarding');
      return;
    }

    try {
      await getChildProfile(childId);
    } catch {
      await AsyncStorage.removeItem(STORAGE_KEY_CHILD_ID);
      router.replace('/onboarding');
      return;
    }

    router.replace('/(tabs)');
  }, []);

  useEffect(() => {
    // Step 1: Mascot fades in + slides up + overshoots scale
    mascotOpacity.value = withDelay(
      300,
      withTiming(1, { duration: 600 }),
    );
    mascotTranslateY.value = withDelay(
      300,
      withTiming(0, { duration: 800, easing: Easing.out(Easing.cubic) }),
    );
    mascotScale.value = withDelay(
      300,
      withSequence(
        // grow past target
        withTiming(1.12, { duration: 600, easing: Easing.out(Easing.cubic) }),
        // bounce back
        withTiming(0.95, { duration: 250, easing: Easing.inOut(Easing.quad) }),
        // settle
        withTiming(1, { duration: 250, easing: Easing.inOut(Easing.quad) }),
      ),
    );

    // Step 2: Title appears after mascot settles
    titleOpacity.value = withDelay(
      1500,
      withTiming(1, { duration: 800 }),
    );
    titleTranslateY.value = withDelay(
      1500,
      withTiming(0, { duration: 800, easing: Easing.out(Easing.cubic) }),
    );

    // Step 3: Navigate after animation
    const timer = setTimeout(() => {
      navigate();
    }, 3500);

    return () => clearTimeout(timer);
  }, []);

  const mascotStyle = useAnimatedStyle(() => ({
    opacity: mascotOpacity.value,
    transform: [
      { scale: mascotScale.value },
      { translateY: mascotTranslateY.value },
    ],
  }));

  const titleStyle = useAnimatedStyle(() => ({
    opacity: titleOpacity.value,
    transform: [{ translateY: titleTranslateY.value }],
  }));

  return (
    <View style={styles.container}>
      {/* Mascot */}
      <Animated.View style={[styles.mascotWrapper, mascotStyle]}>
        <LogoSvg width='80%' height='80%' />
      </Animated.View>

      {/* Tagline */}
      <Animated.Text style={[styles.tagline, titleStyle]}>
        Draw your story!
      </Animated.Text>
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: palette.pink,
    justifyContent: 'center',
    alignItems: 'center',
  },
  mascotWrapper: {
    width: width * 0.55,
    height: width * 0.55,
    justifyContent: 'center',
    alignItems: 'center',
  },
  mascot: {
    width: '100%',
    height: '100%',
  },
  tagline: {
    marginTop: 16,
    fontSize: 18,
    fontFamily: fonts.semiBold,
    color: palette.white,
    letterSpacing: 1,
  },
});
