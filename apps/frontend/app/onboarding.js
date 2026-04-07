import React, { useState } from 'react';
import { View, ScrollView, StyleSheet } from 'react-native';
import { router } from 'expo-router';
import AsyncStorage from '@react-native-async-storage/async-storage';
import { ThemedView } from '@/components/themed-view';
import { palette, spacing } from '../constants/tokens';
import {
  NameAgeStep,
  ModeStep,
  TutorialStep,
  ParentGateStep,
  ReadyStep,
} from '../components/onboarding';
import { createChildProfile } from '@/services/children';
import { useInvalidateChildProfile } from '../hooks/use-child-profile';
import { STORAGE_KEY_CHILD_ID } from '../constants/storage';

export default function OnboardingScreen() {
  const [saving, setSaving] = useState(false);
  const [step, setStep] = useState(1);
  const [userData, setUserData] = useState({ nickname: '', age: '', mode: '' });
  const invalidateProfile = useInvalidateChildProfile();

  const nextStep = () => setStep((s) => s + 1);
  const updateUser = (fields) => setUserData((prev) => ({ ...prev, ...fields }));

  const finishOnboarding = async () => {
    setSaving(true);
    try {
      const profile = await createChildProfile({
        nickname: userData.nickname.trim(),
        ageBand: userData.age,
        mode: userData.mode,
      });
      await AsyncStorage.setItem(STORAGE_KEY_CHILD_ID, profile.id);
      invalidateProfile();
    } catch (err) {
      console.warn('Failed to save profile, continuing anyway:', err);
    }
    setSaving(false);
    router.replace('/(tabs)');
  };

  const renderStep = () => {
    switch (step) {
      case 1:
        return <NameAgeStep userData={userData} onUpdate={updateUser} onNext={nextStep} />;
      case 2:
        return <ModeStep userData={userData} onUpdate={updateUser} onNext={nextStep} />;
      case 3:
        return <TutorialStep onNext={nextStep} />;
      case 4:
        return <ParentGateStep onNext={nextStep} />;
      case 5:
        return <ReadyStep saving={saving} onFinish={finishOnboarding} />;
      default:
        return null;
    }
  };

  return (
    <ThemedView style={styles.container}>
      <View style={styles.bgCircle} />
      <ScrollView contentContainerStyle={styles.scrollContent}>
        {renderStep()}
      </ScrollView>
    </ThemedView>
  );
}

const styles = StyleSheet.create({
  container: { flex: 1, backgroundColor: palette.cream },
  scrollContent: {
    flexGrow: 1,
    justifyContent: 'center',
    alignItems: 'center',
    paddingVertical: spacing.xxl,
  },
  bgCircle: {
    position: 'absolute',
    width: 400,
    height: 400,
    borderRadius: 200,
    backgroundColor: '#FFD70020',
    top: -100,
    right: -100,
  },
});
