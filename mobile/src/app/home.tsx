import { useEffect, useState } from "react";
import { Alert, Text, View } from "react-native";
import MapView, { Callout, Marker } from "react-native-maps";
import * as Location from "expo-location";

import { Categories, CategoriesProps } from "@/components/categories";
import { api } from "@/services/api";
import { PlaceProps } from "@/components/place";
import { Places } from "@/components/places";
import { Loading } from "@/components/loading";
import { fontFamily, colors } from "@/styles/theme";
import { useRouter } from "expo-router";

type MarketProps = PlaceProps & {
  latitude: number;
  longitude: number;
};

export default function Home() {
  const [categories, setCategories] = useState<CategoriesProps>([]);
  const [category, setCategory] = useState("");
  const [markets, setMarkets] = useState<MarketProps[]>([]);
  const [location, setLocation] = useState<Location.LocationObject>(
    {} as Location.LocationObject
  );
  const router = useRouter();

  async function fetchCategories() {
    try {
      const { data } = await api.get<CategoriesProps>("/categories");

      setCategories(data);
      setCategory(data[0].id);
    } catch (error) {
      console.log(error);
      Alert.alert("Categorias", "Não foi possível carregar as categorias.");
    }
  }

  async function fetchMarkets() {
    try {
      if (!category) return;

      const { data } = await api.get<MarketProps[]>(
        "/markets/category/" + category
      );

      setMarkets(data);
    } catch (error) {
      console.log(error);
      Alert.alert("Locais", "Não foi possível carregar os locais.");
    }
  }

  async function getCurrentLocation() {
    try {
      let { granted } = await Location.requestForegroundPermissionsAsync();
      if (granted) {
        let location = await Location.getCurrentPositionAsync({});
        setLocation(location);
      }
    } catch (error) {
      console.log(error);
      Alert.alert("Localização", "Não foi possível obter a localização atual.");
    }
  }

  useEffect(() => {
    getCurrentLocation();
    fetchCategories();
  }, []);

  useEffect(() => {
    fetchMarkets();
  }, [category]);

  return (
    <View style={{ flex: 1, backgroundColor: "#CECECE" }}>
      <Categories
        data={categories}
        onSelect={setCategory}
        selected={category}
      />
      {!location?.coords ? (
        <View
          style={{
            position: "absolute",
            top: "40%",
            left: "46%",
          }}
        >
          <Loading size={48} style={{ backgroundColor: "#CECECE" }} />
        </View>
      ) : (
        <MapView
          initialRegion={{
            latitude: location?.coords?.latitude,
            longitude: location?.coords?.longitude,
            latitudeDelta: 0.01,
            longitudeDelta: 0.01,
          }}
          style={{ flex: 1 }}
        >
          <Marker
            identifier="current"
            coordinate={{
              latitude: location?.coords?.latitude,
              longitude: location?.coords?.longitude,
            }}
            image={require("@/assets/location.png")}
          />
          {markets.map((item) => (
            <Marker
              key={item.id}
              identifier={item.id}
              coordinate={{
                latitude: item.latitude,
                longitude: item.longitude,
              }}
              image={require("@/assets/pin.png")}
            >
              <Callout onPress={() => router.navigate(`/market/${item.id}`)}>
                <View>
                  <Text
                    style={{
                      fontSize: 14,
                      color: colors.gray[600],
                      fontFamily: fontFamily.medium,
                    }}
                  >
                    {item.name}
                  </Text>
                  <Text
                    style={{
                      fontSize: 12,
                      color: colors.gray[600],
                      fontFamily: fontFamily.regular,
                    }}
                  >
                    {item.address}
                  </Text>
                </View>
              </Callout>
            </Marker>
          ))}
        </MapView>
      )}
      <Places data={markets} />
    </View>
  );
}
