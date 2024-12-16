import { useRef } from "react";
import { Text, useWindowDimensions, View } from "react-native";
import BottomSheet, { BottomSheetFlatList } from "@gorhom/bottom-sheet";
import { useRouter } from "expo-router";

import { Place, PlaceProps } from "../place";
import { s } from "./styles";

type Props = {
  data: PlaceProps[];
};

export function Places({ data }: Props) {
  const dimensions = useWindowDimensions();
  const bottomSheetRef = useRef<BottomSheet>(null);
  const router = useRouter();

  const snapPoints = {
    min: 278,
    max: dimensions.height - 128,
  };

  return (
    <BottomSheet
      ref={bottomSheetRef}
      snapPoints={[snapPoints.min, snapPoints.max]}
      handleIndicatorStyle={s.indicator}
      backgroundStyle={s.container}
      enableOverDrag={false}
      maxDynamicContentSize={snapPoints.max}
    >
      <BottomSheetFlatList
        data={data}
        keyExtractor={(item) => item.id}
        renderItem={({ item }) => (
          <Place
            onPress={() => router.navigate(`/market/${item.id}`)}
            data={item}
          />
        )}
        contentContainerStyle={s.content}
        ListHeaderComponent={() =>
          data?.length ? (
            <Text style={s.title}>Explore locais perto de você</Text>
          ) : null
        }
        ListEmptyComponent={() => (
          <Text style={s.emptyText}>
            Não encontramos locais nesta categoria {"\n"} perto de você.
          </Text>
        )}
      />
    </BottomSheet>
  );
}
