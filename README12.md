# Monitoramento de Queimadas na Amazônia

Este projeto tem como objetivo monitorar as queimadas na Amazônia e apresentar informações diárias atualizadas sobre os focos de incêndio detectados. Abaixo, você pode visualizar as queimadas mais recentes, com detalhes sobre localização, satélite que realizou a detecção, e outros fatores relevantes.

## Estrutura dos Dados

Cada entrada na tabela representa um foco de incêndio com as seguintes informações:

- **ID:** Identificador único do foco de incêndio.
- **Latitude/Longitude:** Coordenadas geográficas do foco detectado. Para visualizar o local exato, insira estas coordenadas no Google Maps ou outro aplicativo de mapas.
- **Data/Hora GMT:** Data e hora da detecção em formato GMT (Greenwich Mean Time).
- **Satélite:** Satélite responsável pela detecção do foco de incêndio.
- **Município, Estado e País:** Localização administrativa do foco detectado.
- **Dias sem Chuva:** Número de dias consecutivos sem precipitação na região, o que pode indicar um aumento no risco de incêndio.
- **Precipitação:** Quantidade de chuva (em milímetros) registrada no local.
- **Risco de Fogo:** Índice que indica a probabilidade de ocorrência de incêndio, baseado em fatores como condições climáticas e quantidade de combustível disponível.
- **Bioma:** Bioma onde o foco foi identificado, como Amazônia, Cerrado, ou Mata Atlântica.
- **FRP (Fire Radiative Power):** Potência radiativa do fogo, que mede a intensidade do incêndio. Focos com FRP mais alto indicam incêndios mais intensos.

## Visualização Gráfica

Se você deseja visualizar de forma gráfica onde as queimadas estão ocorrendo, copie as coordenadas de latitude e longitude mais recentes e cole no Google Maps. Isso permite uma compreensão espacial mais clara da distribuição dos focos de incêndio. Alternativamente, você também pode usar a descrição de localização (Município, Estado e País) para identificar a região afetada.

## Informação Adicional

As queimadas na Amazônia não apenas afetam a biodiversidade local, mas também têm implicações globais, contribuindo para o aquecimento global e a emissão de gases de efeito estufa. O monitoramento contínuo é essencial para entender e mitigar os impactos desses incêndios, além de auxiliar na gestão de políticas ambientais e ações de preservação.

## Dados Diários - Página 12

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d7ad3306-c81c-3847-9ed3-6870e1060a93 | -10.8934 | -50.686501 | 2026-09-28 00:55:00 | METOP-C | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| c597d2e1-c2ed-355f-a7f9-c8c0da81085d | -7.6853 | -54.8545 | 2026-09-28 00:55:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7e0aa065-81b8-3716-9146-4152095118b1 | -6.6872 | -45.6456 | 2026-09-28 01:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 67.6 |
| f28ba277-4762-3263-8245-e77ff2e14b44 | -3.1471 | -54.0849 | 2026-09-28 01:00:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 94.5 |
| 49bc02c6-f543-32ca-8d29-bfd43b2d7890 | -11.0959 | -51.3443 | 2026-09-28 01:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 90.6 |
| 3a79e401-2fbe-316b-b5a4-fb1163d45977 | -2.7582 | -49.4771 | 2026-09-28 01:00:00 | GOES-19 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 77.0 |
| 885fa123-8fb1-37c0-9d63-d855dd1f9e73 | -3.1472 | -54.0648 | 2026-09-28 01:00:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 57.5 |
| 4ca656e7-d55a-31de-a41f-bcb623173d8b | -3.2137 | -51.0384 | 2026-09-28 01:00:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 119.7 |
| 0488ae5d-af95-3a72-b7e7-ce6612bead80 | -2.7766 | -49.4977 | 2026-09-28 01:00:00 | GOES-19 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 77.9 |
| 8ac696e9-2645-3632-92f7-72bb71255279 | -11.4616 | -44.9276 | 2026-09-28 01:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 106.9 |
| b61fc5e8-d613-31be-96d9-3330e31429be | -6.7251 | -45.5975 | 2026-09-28 01:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 56.5 |
| 3a291318-ddea-3e2d-9685-cea2bdd8ff4c | -6.7064 | -45.599 | 2026-09-28 01:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 140.7 |
| 7ca31dae-d40b-3237-a78a-28a326f6ba14 | -6.7835 | -59.3823 | 2026-09-28 01:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 63.6 |
| c05b9135-2c4c-31c8-a689-265c6729024d | -6.7066 | -45.5765 | 2026-09-28 01:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 61.3 |
| 656146b8-d89d-341e-a44b-a212b5981b91 | -6.7836 | -59.363 | 2026-09-28 01:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 47.3 |
| aaefeb59-02b6-3866-b092-6af785b787f8 | -11.4425 | -44.9303 | 2026-09-28 01:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 263.1 |
| 6cdfb4bf-7f5c-3cd2-9bbe-31fa78dc432e | -9.9266 | -60.7171 | 2026-09-28 01:00:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 48.0 |
| 4fea3917-f112-3631-9d0c-562125dcad8b | -3.1471 | -54.1049 | 2026-09-28 01:00:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 57.9 |
| c30f1f23-3684-3ba4-aecb-4a9b315beca4 | -8.0373 | -54.8926 | 2026-09-28 01:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 64.8 |
| 99bf81e9-1d7b-38c4-b5f7-40a9ef47393c | -6.7059 | -45.6441 | 2026-09-28 01:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 67.3 |
| 8a422fe5-95f2-303c-a27b-d640819993fe | -10.8907 | -43.6813 | 2026-09-28 01:00:00 | GOES-19 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 93.1 |
| 0c21c01b-d9ee-38e2-afaf-bdf59c8b207f | -2.7767 | -49.4765 | 2026-09-28 01:00:00 | GOES-19 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 95.1 |
| f743de32-be38-3f76-83ee-4de29129f83f | -11.4429 | -44.9072 | 2026-09-28 01:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 88.7 |
| db32aff6-2968-354c-834f-ca8deabbb2f9 | -11.1149 | -51.3423 | 2026-09-28 01:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 76.6 |
| 3b924d94-c69c-3d11-a760-c44f3873c0d6 | -4.0478 | -54.2194 | 2026-09-28 01:00:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 54.3 |
| 8c988a8a-5620-3497-a472-68c3b4a63336 | -2.9081 | -54.1309 | 2026-09-28 01:00:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 54.5 |
| 7bdf5eda-90c5-333e-9cac-8288000d895e | -3.1471 | -54.0849 | 2026-09-28 01:10:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 121.3 |
| cb838534-b8bd-39c9-8726-ee300ce474c8 | -11.6985 | -44.5217 | 2026-09-28 01:10:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 83.8 |
| 9fbfb328-f45b-31c4-ad14-68bf79b22ee4 | -11.4425 | -44.9303 | 2026-09-28 01:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 365.4 |
| 0d4d3740-c51f-350b-9de3-33859345e80a | -2.7766 | -49.4977 | 2026-09-28 01:10:00 | GOES-19 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 83.3 |
| 4da3a256-7aa6-369e-a939-4f6cd458196e | -3.2137 | -51.0384 | 2026-09-28 01:10:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 122.0 |
| 5b5d47dc-deae-3729-86eb-e063d888a70a | -2.9082 | -54.1108 | 2026-09-28 01:10:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 56.6 |
| 30c2205e-a0cf-3954-92c3-abf76a9551e8 | -11.4429 | -44.9072 | 2026-09-28 01:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 86.3 |
| b050e257-5e6e-3805-91cb-bc9eeb911724 | -11.1958 | -44.8269 | 2026-09-28 01:10:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 130.1 |
| 64dad1e6-a34f-32df-900a-1fe04156a823 | -2.7767 | -49.4765 | 2026-09-28 01:10:00 | GOES-19 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 100.0 |
| 96526a04-a01b-3a49-8a81-403ae1ae9834 | -11.4421 | -44.9535 | 2026-09-28 01:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 76.8 |
| d8fbf424-b7cc-3189-adfb-f2cf7c8848a6 | -10.8907 | -43.6813 | 2026-09-28 01:10:00 | GOES-19 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 186.4 |
| f9431ad6-586b-39ed-bad9-488878fa7bc3 | -9.9266 | -60.7171 | 2026-09-28 01:10:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 48.5 |
| f4c0198f-043e-3e18-af1a-6453f448b616 | -12.1928 | -50.3689 | 2026-09-28 01:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 72.3 |
| 225ec83d-a91e-332e-825a-fc373560b883 | -6.7835 | -59.3823 | 2026-09-28 01:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 50.9 |
| ba4102c6-f309-3624-9098-29a1eeb070a0 | -6.7251 | -45.5975 | 2026-09-28 01:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 181.1 |
| 5ea5cc51-90fa-34ae-9062-4369abb0630e | -3.1471 | -54.1049 | 2026-09-28 01:10:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 60.9 |
| b6994acd-2051-37ac-ad11-66544469c2f4 | -11.1771 | -44.8064 | 2026-09-28 01:10:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 151.9 |
| 65901ba7-0096-33ba-adce-bf6120fa42d0 | -11.7177 | -44.5188 | 2026-09-28 01:10:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 140.0 |
| 2e34c0ad-4780-362f-8b37-d53efaaa4f62 | -3.1472 | -54.0648 | 2026-09-28 01:10:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 63.5 |
| 3e5b9629-32e0-31cb-9514-372c57229fcd | -11.1962 | -44.8037 | 2026-09-28 01:10:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 375.2 |
| de459c43-6574-3cd4-ba07-dad364bc9385 | -2.9265 | -54.1305 | 2026-09-28 01:10:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 57.9 |
| 3cf30b96-5ba4-3c5a-a647-6d7122412917 | -11.2154 | -44.801 | 2026-09-28 01:10:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 130.6 |
| ce6bc938-813b-3492-a5e7-180ebf65caf6 | -6.7066 | -45.5765 | 2026-09-28 01:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 66.9 |
| d6b21f09-d1f2-3c38-b232-a66b1f3f213d | -6.7064 | -45.599 | 2026-09-28 01:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 195.0 |
| 5070e055-a6d5-3776-b222-204f7386c4ba | -8.0373 | -54.8926 | 2026-09-28 01:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 60.5 |
| 9ad656d9-9578-32d6-b534-e270ce379078 | -3.1655 | -54.0844 | 2026-09-28 01:10:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 65.3 |
| 17c194b0-7c41-351c-9592-20196ddbe223 | -9.9973 | -50.1393 | 2026-09-28 01:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 65.4 |
| dd50527a-1781-3613-9c33-06d7c251268c | -2.9081 | -54.1309 | 2026-09-28 01:10:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 63.9 |
| db7530f5-e2c1-382b-aed2-ac0f9a0df401 | -10.8715 | -43.684 | 2026-09-28 01:10:00 | GOES-19 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 100.9 |
| bca45256-e38f-30d6-9e13-b0cd39d5f02d | -11.4616 | -44.9276 | 2026-09-28 01:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 124.9 |
| 8579d5bc-d137-37e8-87e7-34d27126d402 | -9.9784 | -50.1412 | 2026-09-28 01:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 57.4 |
| 53a90c7b-d174-3891-8d83-3e7e11f2a310 | -9.9781 | -50.1626 | 2026-09-28 01:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 56.4 |
| 5a183c4c-23e4-3e1d-beed-66733118daae | -11.1966 | -44.7805 | 2026-09-28 01:10:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 106.3 |
| d324ae47-bfcc-31a9-9d85-e92d027491cb | -11.19 | -44.8 | 2026-09-28 01:15:00 | MSG-03 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 4580e59f-6290-355e-919d-0cbeb66e01cd | -11.45 | -44.92 | 2026-09-28 01:15:00 | MSG-03 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 03bb0fe9-b94e-3fdc-9187-04a955e1f8fc | -11.22 | -44.81 | 2026-09-28 01:15:00 | MSG-03 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 79511f56-aa4d-3b31-a5c2-ee8d124135ad | -7.7086 | -44.92 | 2026-09-28 01:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 59.8 |
| 812ebfdb-b4fd-3826-92ce-9765fd8bd722 | -6.7254 | -45.5749 | 2026-09-28 01:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 52.1 |
| 9e856bfa-b4e0-3da8-a301-5fe43de455fb | -6.7062 | -45.6216 | 2026-09-28 01:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 61.5 |
| 9a8a083d-2942-3811-b2e0-737902f06734 | -3.2137 | -51.0384 | 2026-09-28 01:20:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 112.1 |
| df7e9d5f-4b94-318c-a109-deed3cf283f8 | -2.7767 | -49.4765 | 2026-09-28 01:20:00 | GOES-19 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 79.2 |
| c72af62c-ca76-3bea-ac9c-d71c29cbdbf2 | -7.7083 | -44.9429 | 2026-09-28 01:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 72.5 |
| a9026a52-e4fc-3ac6-91f2-003f604e4754 | -6.7064 | -45.599 | 2026-09-28 01:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 226.3 |
| fdccd83a-9816-3a97-b458-cb48dedad8ee | -3.1471 | -54.0849 | 2026-09-28 01:20:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 62.4 |
| d0aa4842-519a-359d-b102-11e45fb7f681 | -11.7177 | -44.5188 | 2026-09-28 01:20:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 75.1 |
| 98499825-d2bf-3575-a77d-7756f59f9464 | -2.9081 | -54.1309 | 2026-09-28 01:20:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 65.8 |
| fb8938e4-38aa-3e1e-81a7-dbf1e3c7cbef | -11.1771 | -44.8064 | 2026-09-28 01:20:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 125.6 |
| 6f16e961-2eb2-3f45-b403-67e12dbcfe66 | -11.2154 | -44.801 | 2026-09-28 01:20:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 66.9 |
| fae6ccf8-8627-3d58-97cc-28f8f67951c7 | -11.4425 | -44.9303 | 2026-09-28 01:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 140.6 |
| 9c37b56b-5eb9-34be-a637-2a3d2743d03a | -11.1962 | -44.8037 | 2026-09-28 01:20:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 332.8 |
| 387c9069-21f5-3d21-ad82-b28367fb2ffe | -11.1958 | -44.8269 | 2026-09-28 01:20:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 100.3 |
| e9dcbcb0-9775-3154-9634-348a75b7bea3 | -3.1953 | -51.039 | 2026-09-28 01:20:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 86.8 |
| 65e5155a-64a0-3383-8b11-9c730fb1966b | -6.7066 | -45.5765 | 2026-09-28 01:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 62.5 |
| 9180fc69-9983-3231-a4bb-020cb9809ae7 | -6.7835 | -59.3823 | 2026-09-28 01:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 50.3 |
| 0b7932a1-9164-3e16-bab2-fe96b7cc1454 | -8.0373 | -54.8926 | 2026-09-28 01:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 67.3 |
| 7ecad5c7-21f7-30ea-969d-d63cd5b7dc87 | -9.177 | -61.4073 | 2026-09-28 01:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 61.5 |
| d9e07c98-afab-3fee-abd6-6335266ccc61 | -10.8715 | -43.684 | 2026-09-28 01:20:00 | GOES-19 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 91.4 |
| 79e71643-6610-31a4-b203-83bbf3e302da | -11.0959 | -51.3443 | 2026-09-28 01:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 93.6 |
| 5490ae16-49a6-37b3-8ebf-6f70081bbd04 | -6.7251 | -45.5975 | 2026-09-28 01:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 272.8 |
| 581fd6d0-8d92-3d88-9a3a-f23388bd9392 | -9.9266 | -60.7171 | 2026-09-28 01:20:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 50.1 |
| e694dca6-08dc-3f61-a85e-303b03974cc2 | -11.1966 | -44.7805 | 2026-09-28 01:20:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 111.8 |
| b5d25127-e855-385b-976f-af2e46b023f6 | -7.8625 | -61.1978 | 2026-09-28 01:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 59.5 |
| 1c0e525a-a650-3c89-a17b-e6462ec9dc8e | -10.8903 | -43.7048 | 2026-09-28 01:20:00 | GOES-19 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 91.4 |
| e77afbbf-6937-3f6b-bcb6-b87ee84d77b9 | -10.8907 | -43.6813 | 2026-09-28 01:20:00 | GOES-19 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 232.4 |
| dde07009-1c8f-3cef-9764-cc41defec1b2 | -6.7249 | -45.62 | 2026-09-28 01:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 67.4 |
| 274400ff-d25c-3531-8cd2-881bb35cc013 | -15.1847 | -46.141 | 2026-09-28 01:30:00 | GOES-19 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 60.0 |
| b63b7323-969a-36c8-bdda-52b4de13d8f3 | -10.8911 | -43.6577 | 2026-09-28 01:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 75.7 |
| d0548e2d-6b01-323e-9a29-508d30589eef | -10.8903 | -43.7048 | 2026-09-28 01:30:00 | GOES-19 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 86.4 |
| ec21002e-6dc0-3417-805c-45367260b241 | -3.2137 | -51.0384 | 2026-09-28 01:30:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 98.7 |
| a508d747-491f-3206-b91b-587f271a1fd5 | -6.1485 | -47.2871 | 2026-09-28 01:30:00 | GOES-19 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 94.5 |
| 5c261379-e70b-3a6b-98f5-4e8573e2ea64 | -3.1472 | -54.0648 | 2026-09-28 01:30:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 61.8 |
| fff4f0ef-ab4f-3129-b6e5-3246e1cd0b84 | -10.8715 | -43.684 | 2026-09-28 01:30:00 | GOES-19 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 147.8 |
| 6f6a7c8d-67e0-3182-86bb-c2cca599ac2f | -10.2067 | -49.9898 | 2026-09-28 01:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 70.1 |
| 6f338064-5559-3b54-87d7-1c9075c26070 | -9.177 | -61.4073 | 2026-09-28 01:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 66.9 |


[Clique aqui para ver as próximas entradas](README13.md)
