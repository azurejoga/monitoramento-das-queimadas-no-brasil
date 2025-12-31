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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1467aa38-55be-3a70-98b1-eefb045f0bc1 | -4.3073 | -43.789299 | 2025-12-31 01:02:00 | METOP-C | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 7dad8ce4-b4b5-3590-aead-702c291fb246 | -33.7118 | -53.366402 | 2025-12-31 01:02:00 | METOP-C | SANTA VITÓRIA DO PALMAR | RIO GRANDE DO SUL | Brasil | 4317301 | 43 | 33 | nan | nan | nan | Pampa | nan |
| d1f59d91-65c0-3e76-8f07-d279e409fc93 | -17.364401 | -42.6073 | 2025-12-31 01:02:00 | METOP-C | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 4a67531c-c80e-3120-aa1a-67d4f5d2585b | -17.374001 | -42.604401 | 2025-12-31 01:02:00 | METOP-C | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 8b2b7750-1710-3f85-9a9b-c5f35329a045 | -17.370001 | -42.627399 | 2025-12-31 01:02:00 | METOP-C | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 39624353-1775-3df0-ac95-7e52f96b050c | -33.713799 | -53.378502 | 2025-12-31 01:02:00 | METOP-C | CHUÍ | RIO GRANDE DO SUL | Brasil | 4305439 | 43 | 33 | nan | nan | nan | Pampa | nan |
| cc2ce820-b12a-3f02-9533-a4743bb1ece4 | -1.0822 | -49.1912 | 2025-12-31 01:05:00 | METOP-C | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 12683c8d-67b5-3040-b65f-c8d17ee3e74b | -4.3099 | -43.7811 | 2025-12-31 01:10:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 221.2 |
| 403818f3-711d-36ed-b8b6-7aaa5923c81d | -4.3286 | -43.7801 | 2025-12-31 01:10:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 145.1 |
| 5e0d1f6c-7b97-3d32-8a7a-818029f855ba | -4.3098 | -43.8042 | 2025-12-31 01:10:00 | GOES-19 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 84.0 |
| 8ee4f452-dc8c-3c49-aa3d-02af0ca4600e | -17.3844 | -42.6235 | 2025-12-31 01:10:00 | GOES-19 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 144.2 |
| 3e0b8f63-e325-3a7e-af90-cf4cce73ca85 | -4.3285 | -43.8032 | 2025-12-31 01:10:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 64.2 |
| 339a3fe9-ab6d-36af-b860-af4c87db749d | -4.3286 | -43.7801 | 2025-12-31 01:20:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 120.8 |
| 45162631-6602-3022-8058-95d3521880bb | -2.9064 | -49.3879 | 2025-12-31 01:20:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 44.1 |
| 51f4fa18-9769-32ce-bc65-85b1744605c7 | -17.3844 | -42.6235 | 2025-12-31 01:20:00 | GOES-19 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 132.7 |
| 7af19e8b-1b3b-3459-ab79-4b5f59c3c3c2 | -4.3098 | -43.8042 | 2025-12-31 01:20:00 | GOES-19 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 63.1 |
| 518b99eb-eb50-35f9-be0e-55b4bd2ebbb7 | -2.9064 | -49.3667 | 2025-12-31 01:20:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 37.3 |
| 5cbfc1b4-e8ba-38d7-b634-f4522d046d42 | -4.3099 | -43.7811 | 2025-12-31 01:20:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 161.9 |
| 28ad0a54-ce99-3401-bc5f-83d5f53a7ee6 | -4.3286 | -43.7801 | 2025-12-31 01:30:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 69.1 |
| 8ee70f11-548d-32e7-91b3-9e580178eb9a | -17.3844 | -42.6235 | 2025-12-31 01:30:00 | GOES-19 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 130.1 |
| 568c4ad6-565d-380e-a4ac-8f8e1a4dd5ab | -4.3099 | -43.7811 | 2025-12-31 01:30:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 110.1 |
| 807b744b-ea66-3147-8ffb-7ecc289a8927 | -4.3098 | -43.8042 | 2025-12-31 01:30:00 | GOES-19 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 59.7 |
| e93e257e-91fa-342d-8ce1-3f0cebb529fc | -17.3844 | -42.6235 | 2025-12-31 01:40:00 | GOES-19 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 109.9 |
| 2e696ab1-c1d8-3e76-b158-ecb7b50552d2 | -4.3286 | -43.7801 | 2025-12-31 01:40:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 55.2 |
| fddf8238-5d42-357a-8107-be29a8a2ab58 | -17.3844 | -42.6235 | 2025-12-31 01:50:00 | GOES-19 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 119.4 |
| e57cba1c-2622-3d33-9933-3dab8216bf83 | -4.3099 | -43.7811 | 2025-12-31 01:50:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 64.5 |
| 59b3f07b-9767-35f0-a6e6-3ec7e2860fef | -4.3286 | -43.7801 | 2025-12-31 01:50:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 63.5 |
| fc6f3f54-29af-3176-b17d-e44f3f1f5aaf | -17.3844 | -42.6235 | 2025-12-31 02:00:00 | GOES-19 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 102.4 |
| 5b4034a5-afcb-3d7c-a832-530b3cd100c3 | -17.3844 | -42.6235 | 2025-12-31 02:10:00 | GOES-19 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 91.4 |
| bdf437e9-e0e6-317a-a612-db5b5107f5dd | -4.3286 | -43.7801 | 2025-12-31 02:30:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 51.8 |
| 3420f53b-d654-308b-8217-60b54d7b8f49 | -4.3099 | -43.7811 | 2025-12-31 02:30:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 74.3 |
| 738c852c-8e1d-34e6-ab63-802c8d6bae9e | -7.1722 | -35.0291 | 2025-12-31 02:30:00 | GOES-19 | SANTA RITA | PARAÍBA | Brasil | 2513703 | 25 | 33 | nan | nan | nan | Mata Atlântica | 60.2 |
| 3c6a4f98-86a0-3da5-998e-b0ac6dc3e21e | -4.3099 | -43.7811 | 2025-12-31 02:40:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 57.1 |
| bbc219f9-d4c7-3c18-8995-b75134a62ac9 | -4.3099 | -43.7811 | 2025-12-31 02:50:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 57.9 |
| c3a991b2-3613-3156-9111-48fa83504464 | -4.3099 | -43.7811 | 2025-12-31 03:00:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 66.1 |
| 913df5a4-0138-3ac5-83fb-72607aa95793 | -4.76558 | -37.82096 | 2025-12-31 03:02:00 | NPP-375D | JAGUARUANA | CEARÁ | Brasil | 2307007 | 23 | 33 | nan | nan | nan | Caatinga | 3.1 |
| c37e22dd-96ee-3537-97fc-35eae21f0875 | -4.76428 | -37.82815 | 2025-12-31 03:02:00 | NPP-375D | JAGUARUANA | CEARÁ | Brasil | 2307007 | 23 | 33 | nan | nan | nan | Caatinga | 4.3 |
| e7fc97e8-44cb-307e-a4e2-bc379e0b45c9 | -4.77147 | -37.82951 | 2025-12-31 03:02:00 | NPP-375D | JAGUARUANA | CEARÁ | Brasil | 2307007 | 23 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 9debb605-7eac-3935-8c7a-cb2e762d4291 | -20.19912 | -41.69224 | 2025-12-31 03:08:00 | NPP-375D | LAJINHA | MINAS GERAIS | Brasil | 3137700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| 31c314ce-9232-370c-b8c0-2efc7dd70716 | -20.19979 | -41.69208 | 2025-12-31 03:08:00 | NPP-375D | LAJINHA | MINAS GERAIS | Brasil | 3137700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| 679cad78-b182-3e70-80e3-890dca0017df | -4.3099 | -43.7811 | 2025-12-31 03:10:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 62.3 |
| bc7f07e8-b20b-3254-9499-6b51db9546df | -6.1122 | -39.80347 | 2025-12-31 03:23:00 | NOAA-20 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 0.5 |
| d9800cba-3280-3932-be6e-c4568573cd4c | -9.21017 | -35.71553 | 2025-12-31 03:23:00 | NOAA-20 | FLEXEIRAS | ALAGOAS | Brasil | 2702801 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| eff498e0-2073-358d-b622-2f97ccb62fff | -3.40808 | -39.35779 | 2025-12-31 03:23:00 | NOAA-20 | TRAIRI | CEARÁ | Brasil | 2313500 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| da361b14-6582-33fc-b675-40dbdc1e0ea7 | -5.30692 | -35.54465 | 2025-12-31 03:23:00 | NOAA-20 | TOUROS | RIO GRANDE DO NORTE | Brasil | 2414407 | 24 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 07b5c2d6-9a29-3485-a5b0-d4c0dc17cedf | -6.42292 | -35.13623 | 2025-12-31 03:23:00 | NOAA-20 | CANGUARETAMA | RIO GRANDE DO NORTE | Brasil | 2402204 | 24 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 7762685b-1c2d-3542-ac67-b15271046cf3 | -6.21392 | -39.27576 | 2025-12-31 03:23:00 | NOAA-20 | IGUATU | CEARÁ | Brasil | 2305506 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| ce4070b9-0afa-3c75-bdfb-1037d13a1ab9 | -7.7759 | -37.19862 | 2025-12-31 03:23:00 | NOAA-20 | IGUARACY | PERNAMBUCO | Brasil | 2606903 | 26 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 7e2b5488-4d0a-36d4-b0a7-d3ba6024d01f | -3.43327 | -41.68393 | 2025-12-31 03:23:00 | NOAA-20 | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 3abeefbe-bd86-32d8-a7f7-9c77f771b960 | -6.29199 | -39.60103 | 2025-12-31 03:23:00 | NOAA-20 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 97d87b37-70c2-3cad-92a9-9810b1839b39 | -6.49463 | -39.03819 | 2025-12-31 03:23:00 | NOAA-20 | CEDRO | CEARÁ | Brasil | 2303808 | 23 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 0f86dab2-7ecc-3846-8b09-c57e605b337b | -7.49506 | -37.41448 | 2025-12-31 03:23:00 | NOAA-20 | SANTA TEREZINHA | PERNAMBUCO | Brasil | 2612802 | 26 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 24b00b7a-675a-35e6-8996-20e3d90bce59 | -6.21339 | -39.27886 | 2025-12-31 03:23:00 | NOAA-20 | IGUATU | CEARÁ | Brasil | 2305506 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 959dcf9d-c15f-3d62-b938-47bdc13d06cd | -7.7422 | -35.97751 | 2025-12-31 03:23:00 | NOAA-20 | SANTA CECÍLIA | PARAÍBA | Brasil | 2513158 | 25 | 33 | nan | nan | nan | Caatinga | 0.9 |
| fc734a7c-3de7-365c-8539-1ba8e4823a03 | -5.34724 | -35.40054 | 2025-12-31 03:23:00 | NOAA-20 | RIO DO FOGO | RIO GRANDE DO NORTE | Brasil | 2408953 | 24 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 65c5e79d-a7d4-37a8-8ab6-6d46f9b1727a | -3.87591 | -40.4528 | 2025-12-31 03:23:00 | NOAA-20 | CARIRÉ | CEARÁ | Brasil | 2303105 | 23 | 33 | nan | nan | nan | Caatinga | 2.9 |
| f527eeec-5a6d-3ad6-b059-5f0f7b914aa9 | -4.76565 | -37.82582 | 2025-12-31 03:23:00 | NOAA-20 | JAGUARUANA | CEARÁ | Brasil | 2307007 | 23 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 19778969-f6e2-32ae-8d98-a72d9403aca1 | -3.43771 | -41.68081 | 2025-12-31 03:23:00 | NOAA-20 | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| c5dfb58a-4079-36f4-8a6c-2c5adb03b450 | -6.28609 | -39.60356 | 2025-12-31 03:23:00 | NOAA-20 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| b41dbfd5-6e21-3ca2-bed4-ff61261d93d1 | -5.54325 | -36.94181 | 2025-12-31 03:23:00 | NOAA-20 | AÇU | RIO GRANDE DO NORTE | Brasil | 2400208 | 24 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 3729b0ed-7aca-30de-ad99-ea1c5b2bb433 | -3.43416 | -41.67887 | 2025-12-31 03:23:00 | NOAA-20 | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 9596ce0d-5f68-337a-885c-b0f71368d930 | -3.3451 | -42.15124 | 2025-12-31 03:23:00 | NOAA-20 | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 40d7e9ef-61c3-329c-98a3-9c7ad7a34af4 | -7.09535 | -38.78696 | 2025-12-31 03:23:00 | NOAA-20 | BARRO | CEARÁ | Brasil | 2302008 | 23 | 33 | nan | nan | nan | Caatinga | 2.5 |
| cb92b008-a05b-3cc5-baca-b87351549afe | -3.41354 | -39.35869 | 2025-12-31 03:23:00 | NOAA-20 | TRAIRI | CEARÁ | Brasil | 2313500 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| febab328-1a39-3187-8b6b-94ecd48b6324 | -3.43686 | -41.68587 | 2025-12-31 03:23:00 | NOAA-20 | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 81e78f99-fe77-3348-898c-c694b2d3046a | -5.54492 | -36.94429 | 2025-12-31 03:23:00 | NOAA-20 | AÇU | RIO GRANDE DO NORTE | Brasil | 2400208 | 24 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 3d436f33-9a20-36c5-9d2f-c3d5361ced41 | -6.48955 | -39.03739 | 2025-12-31 03:23:00 | NOAA-20 | CEDRO | CEARÁ | Brasil | 2303808 | 23 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 6023558f-2651-33a8-8c38-9bc295f9bf25 | -3.8694 | -40.45593 | 2025-12-31 03:23:00 | NOAA-20 | CARIRÉ | CEARÁ | Brasil | 2303105 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 547925d3-5c07-3bd0-abe5-5364e777a7c4 | -6.11762 | -39.8041 | 2025-12-31 03:23:00 | NOAA-20 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 7c5079a8-65c2-344c-a8c5-73754b4886ea | -5.54567 | -36.93974 | 2025-12-31 03:23:00 | NOAA-20 | AÇU | RIO GRANDE DO NORTE | Brasil | 2400208 | 24 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 2a18b9a2-2126-391f-9cd9-3ea73f132afa | -3.34416 | -42.15675 | 2025-12-31 03:23:00 | NOAA-20 | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 66dd444a-2ffa-33a0-bb68-f8b9181b77bb | -6.23151 | -40.63709 | 2025-12-31 03:23:00 | NOAA-20 | PARAMBU | CEARÁ | Brasil | 2310308 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 1dae105d-a313-3ce7-a3b3-e7f087c27a33 | -3.87572 | -40.45104 | 2025-12-31 03:23:00 | NOAA-20 | CARIRÉ | CEARÁ | Brasil | 2303105 | 23 | 33 | nan | nan | nan | Caatinga | 2.6 |
| daa41d68-cca5-38b5-b82f-34760a7dfac1 | -4.76655 | -37.82058 | 2025-12-31 03:23:00 | NOAA-20 | JAGUARUANA | CEARÁ | Brasil | 2307007 | 23 | 33 | nan | nan | nan | Caatinga | 5.4 |
| 4f6f7b7a-1e92-3f30-ab5d-7c8a22b86e7b | -6.41901 | -35.13558 | 2025-12-31 03:23:00 | NOAA-20 | CANGUARETAMA | RIO GRANDE DO NORTE | Brasil | 2402204 | 24 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 06f0eab4-d0ba-3f4a-aa35-8decd09fcc53 | -3.4126 | -39.35899 | 2025-12-31 03:23:00 | NOAA-20 | TRAIRI | CEARÁ | Brasil | 2313500 | 23 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 6735dfcd-f172-3d2a-8221-5848addb7cba | -4.77046 | -37.82664 | 2025-12-31 03:23:00 | NOAA-20 | JAGUARUANA | CEARÁ | Brasil | 2307007 | 23 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 36236c46-01d5-3619-9a7d-b71913bd0d93 | -6.29139 | -39.60435 | 2025-12-31 03:23:00 | NOAA-20 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 6ccd57b1-ab7d-3e62-8779-6e1e17d9bdf2 | -3.86919 | -40.45417 | 2025-12-31 03:23:00 | NOAA-20 | CARIRÉ | CEARÁ | Brasil | 2303105 | 23 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 1f39c430-a3cf-3979-b12e-f4f896cf4b3a | -6.19181 | -35.34126 | 2025-12-31 03:23:00 | NOAA-20 | JUNDIÁ | RIO GRANDE DO NORTE | Brasil | 2406155 | 24 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 76bb2dbf-9813-3b08-8d6c-eaac60dc4813 | -5.54772 | -36.94252 | 2025-12-31 03:23:00 | NOAA-20 | AÇU | RIO GRANDE DO NORTE | Brasil | 2400208 | 24 | 33 | nan | nan | nan | Caatinga | 0.8 |
| fcf42f7f-0b91-38e0-ab1c-b1fcb0ac4bdc | -6.32346 | -35.80211 | 2025-12-31 03:23:00 | NOAA-20 | SÃO JOSÉ DO CAMPESTRE | RIO GRANDE DO NORTE | Brasil | 2412302 | 24 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 7b94b9d7-15e6-336d-9bbf-f4033eb66a8f | -12.14249 | -37.98006 | 2025-12-31 03:25:00 | NOAA-20 | ENTRE RIOS | BAHIA | Brasil | 2910503 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 396f64ff-c5dc-3bf0-ad57-e9946ab80b5e | -9.52797 | -40.33925 | 2025-12-31 03:25:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 1d813fad-5ab9-324f-baf9-6a5aa4501c29 | -9.52212 | -40.34151 | 2025-12-31 03:25:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 96543f8c-e446-369c-987b-76447dfda3de | -9.8504 | -37.63733 | 2025-12-31 03:25:00 | NOAA-20 | POÇO REDONDO | SERGIPE | Brasil | 2805406 | 28 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 07cd2864-c57c-30c9-b994-6777a7e2b808 | -9.85475 | -37.63816 | 2025-12-31 03:25:00 | NOAA-20 | POÇO REDONDO | SERGIPE | Brasil | 2805406 | 28 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 37f6b64b-b753-345c-8ef3-addb1351af9d | -9.52736 | -40.34252 | 2025-12-31 03:25:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 3.3 |
| f65a1d50-96bd-30f3-9304-57607455b367 | -16.89924 | -39.77392 | 2025-12-31 03:27:00 | NOAA-20 | ITAMARAJU | BAHIA | Brasil | 2915601 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| ecde2ab9-5dfe-3316-a091-83cfdccd628a | -20.52952 | -40.9339 | 2025-12-31 03:27:00 | NOAA-20 | ALFREDO CHAVES | ESPÍRITO SANTO | Brasil | 3200300 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| db3622a7-d907-3b23-9b02-9e1c53692815 | -17.37832 | -42.62629 | 2025-12-31 03:27:00 | NOAA-20 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 7b082826-8642-3fd9-9f2d-2156ee207805 | -16.86769 | -40.56908 | 2025-12-31 03:27:00 | NOAA-20 | BERTÓPOLIS | MINAS GERAIS | Brasil | 3106606 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| 27fce2c0-6f3d-39d5-a193-734e215854b2 | -17.51934 | -40.62654 | 2025-12-31 03:27:00 | NOAA-20 | CARLOS CHAGAS | MINAS GERAIS | Brasil | 3113701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 820dc80c-eda7-3275-bbde-77b063457119 | -19.28459 | -42.19363 | 2025-12-31 03:27:00 | NOAA-20 | SÃO JOÃO DO ORIENTE | MINAS GERAIS | Brasil | 3162609 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 53e2235f-52d2-3613-b621-24bc0e7ff72f | -17.37625 | -42.63044 | 2025-12-31 03:27:00 | NOAA-20 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 815c8278-3951-34d6-a369-9893a2565774 | -17.37307 | -42.62509 | 2025-12-31 03:27:00 | NOAA-20 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 4.8 |
| b7ec10dd-a0b9-36b5-b72c-eb7569894f86 | -17.37762 | -42.62971 | 2025-12-31 03:27:00 | NOAA-20 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 10.6 |
| e7647283-6491-3b2c-9418-1d45a1ab9015 | -16.90011 | -39.76941 | 2025-12-31 03:27:00 | NOAA-20 | ITAMARAJU | BAHIA | Brasil | 2915601 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| e5ac8a1a-d9bc-3d46-a8e3-9a0a040995b7 | -17.37692 | -42.63316 | 2025-12-31 03:27:00 | NOAA-20 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 10.6 |
| d0fefac6-e08a-3206-bdda-f87177157860 | -17.3777 | -42.62361 | 2025-12-31 03:27:00 | NOAA-20 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 7.0 |


[Clique aqui para ver as próximas entradas](README4.md)
