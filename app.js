import React, { useEffect, useState } from 'react';
import { View, Text, Image } from 'react-native';
import Swiper from 'react-native-deck-swiper';

export default function App() {
  const [dogs, setDogs] = useState([]);

  useEffect(() => {
    fetch("https://api.thedogapi.com/v1/breeds")
      .then(res => res.json())
      .then(data => setDogs(data.slice(0, 10)));
  }, []);

  return (
    <View style={{ flex: 1 }}>
      <Swiper
        cards={dogs}
        renderCard={(card) => (
          <View>
            <Image
              source={{ uri: card.image?.url }}
              style={{ height: 300 }}
            />
            <Text>{card.name}</Text>
          </View>
        )}
      />
    </View>
  );
}
