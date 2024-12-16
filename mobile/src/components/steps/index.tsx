import React from "react";
import { View, Text, FlatList } from "react-native";
import { IconMapPin, IconQrcode, IconTicket } from "@tabler/icons-react-native";

import { s } from "./styles";
import { Step } from "../step";

const steps = [
  {
    id: "map",
    icon: IconMapPin,
    title: "Encontre estabelecimentos",
    description: "Veja locais perto de você que são parceiros Nearby",
  },
  {
    id: "qrcode",
    icon: IconQrcode,
    title: "Ative o cupom com QR Code",
    description: "Escaneie o código no estabelecimento para usar o benefício",
  },
  {
    id: "ticket",
    icon: IconTicket,
    title: "Garanta vantagens perto de você",
    description:
      "Ative cupons onde estiver, em diferentes tipos de estabelecimento",
  },
];

export function Steps() {
  return (
    <View style={s.container}>
      <Text style={s.title}>Veja como funciona:</Text>
      <FlatList
        scrollEnabled={false}
        data={steps}
        keyExtractor={(item) => item.id}
        renderItem={({ item }) => <Step {...item} />}
      />
    </View>
  );
}
