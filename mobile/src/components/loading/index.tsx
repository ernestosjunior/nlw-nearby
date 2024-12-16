import { ActivityIndicator, ActivityIndicatorProps } from "react-native";

import { colors } from "@/styles/theme";

import { s } from "./styles";

export function Loading({ style, ...rest }: ActivityIndicatorProps) {
  return (
    <ActivityIndicator
      color={colors.green.base}
      style={[s.container, style]}
      {...rest}
    />
  );
}
