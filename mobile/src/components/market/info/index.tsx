import React from "react";
import { Text, View } from "react-native";
import { IconProps, Icon } from "@tabler/icons-react-native";

import { colors } from "@/styles/theme";

import { s } from "./styles";

type Props = {
  icon: React.ComponentType<IconProps>;
  description: string;
};

export function Info({ icon: Icon, description }: Props) {
  return (
    <View style={s.container}>
      <Icon size={16} color={colors.gray[400]} />
      <Text style={s.text}>{description}</Text>
    </View>
  );
}
