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

## Dados Diários - Página 113

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 554e4fc8-a1c2-3d81-820a-aaaaccfb55e7 | -3.81543 | -50.79559 | 2024-11-10 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 82b4f1fd-1883-374c-9646-80bf0fd50a94 | -2.40503 | -50.30855 | 2024-11-10 04:38:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 02a5a938-ccb9-382c-9aff-436c8b9f87b9 | -8.38986 | -44.1307 | 2024-11-10 04:38:00 | NPP-375D | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d52d600b-0511-3d51-9a16-cbd11e478c80 | -2.41955 | -48.85576 | 2024-11-10 04:38:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f4853cac-6c4b-3b58-af4d-5a3ea17f5eb2 | -2.71954 | -51.70725 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 87aeb2af-21c6-3c91-ac89-fc1645207de5 | -3.49311 | -45.86541 | 2024-11-10 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 29119623-3497-3e89-8650-83a5d977d32a | -8.38144 | -44.12944 | 2024-11-10 04:38:00 | NPP-375D | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5ca73ee8-81f2-3d38-b87f-f0761ae19500 | -3.58976 | -50.23681 | 2024-11-10 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0ba178f6-062e-3186-87d7-23d21317ef9a | -1.52438 | -54.99908 | 2024-11-10 04:38:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 33bbc2b1-d27c-33b7-91ea-f436d096b2bb | -4.36998 | -47.252 | 2024-11-10 04:38:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5a699302-4c7d-39fc-8c57-03b8a33c922b | -2.87192 | -50.40285 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2b355a00-d51e-3a12-ac6e-642eded592dc | -2.27739 | -50.64595 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 543fb5a4-9388-3004-8fd6-13d5c105be30 | -3.03438 | -50.30324 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 99d24da5-68e2-3150-baf5-87b95cff7b03 | -2.83199 | -49.46231 | 2024-11-10 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4b5b5f15-d842-3808-930a-b6f6ed06dff2 | -5.32512 | -45.06107 | 2024-11-10 04:38:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 4c1774c4-1030-3c80-9b00-2c52ae5cd5a3 | -6.40886 | -47.51701 | 2024-11-10 04:38:00 | NPP-375D | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 47fe304a-e7ca-3ea0-824e-99efc26a4b4d | -2.87709 | -47.90834 | 2024-11-10 04:38:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 30c0b4da-e321-3a70-8bdd-68e777ae5049 | -3.30788 | -44.39336 | 2024-11-10 04:38:00 | NPP-375D | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| f9aa50ff-1db2-3d95-bd94-fcdbf1eb6a46 | -6.26754 | -44.54891 | 2024-11-10 04:38:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| bf0bdb6d-5a18-3fc1-8e39-6dc6b608818d | -2.80917 | -52.53771 | 2024-11-10 04:38:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 18.5 |
| c1384ad0-cd44-3fc3-8763-5770a20e3000 | -2.30572 | -50.46847 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 30e7f959-73a5-3810-ba49-d1f8e75d8c24 | -2.45286 | -53.68888 | 2024-11-10 04:38:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 066a8ca9-fb58-3dc3-88e2-e48a7901a0ec | -3.23457 | -50.45119 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b7c63b0a-8fe4-3d95-ac72-d903a70ab7e4 | -2.63876 | -51.74613 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0326f997-d86e-327e-b235-3a08dd979bd7 | -2.57348 | -54.01102 | 2024-11-10 04:38:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 08c3ec17-10da-307d-adae-3606a88280b1 | -8.39295 | -44.13912 | 2024-11-10 04:38:00 | NPP-375D | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 195d2e88-5a52-3d80-85d0-1808b09e4606 | -3.05446 | -51.09069 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 06948025-4a6d-38d1-a10b-6542fd935435 | -3.22199 | -50.28748 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 19.6 |
| a1e50f90-ee47-3054-afa0-c7bbbb4f09ea | -3.74289 | -44.53852 | 2024-11-10 04:38:00 | NPP-375D | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 69c32062-ec63-3ae4-a60f-3ff73fa579eb | -3.59015 | -47.35186 | 2024-11-10 04:38:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 8499a0e1-f940-34a3-b89c-88c1dc96ebc5 | -4.71034 | -43.79435 | 2024-11-10 04:38:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 79d922c4-b7da-3162-bd50-ddbfd1712e26 | -3.69154 | -48.83886 | 2024-11-10 04:38:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1bf8dd20-617a-32f4-a3ac-e4e8a0997d26 | -3.37102 | -57.24727 | 2024-11-10 04:38:00 | NPP-375D | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cf07272f-2c7b-30b5-9239-97ed400e4c87 | -6.27226 | -44.54446 | 2024-11-10 04:38:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 58192779-6969-33fc-aa34-52d982fee2a5 | -4.03901 | -48.2848 | 2024-11-10 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c97db297-9478-3498-834d-c9f22bea9fb7 | -3.12908 | -50.43515 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| e9e109d5-15c6-38a2-a4c0-02a31b7e22dc | -3.98863 | -46.41172 | 2024-11-10 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 0fe6eaf8-4834-3eb5-8134-0c81bdee86a0 | -2.87198 | -49.38242 | 2024-11-10 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 81bd43b6-39ab-3d13-b37c-0cf561f2decd | -8.40783 | -44.1255 | 2024-11-10 04:38:00 | NPP-375D | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2709db66-df36-38c1-ad68-5d61eae5731b | -3.10187 | -53.31837 | 2024-11-10 04:38:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| f17c64f1-1195-34be-81bd-71233454f0b7 | -3.35888 | -50.13023 | 2024-11-10 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d8ae3b50-f6d1-35da-b652-ab203bbaaa9b | -2.90404 | -49.36575 | 2024-11-10 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3a909fe4-04f3-3e44-8ffd-fee1a09af0a2 | -4.27699 | -48.19009 | 2024-11-10 04:38:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 94a5fd6c-eb54-3117-acfd-654830cdb2ce | -4.89445 | -48.61375 | 2024-11-10 04:38:00 | NPP-375D | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 648fef2e-2cfc-3bb5-836f-1691a719a4bf | -5.90637 | -50.21548 | 2024-11-10 04:38:00 | NPP-375D | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 02bfb20c-1e9c-3aa9-9aab-ae5082078ecb | -3.49149 | -44.55116 | 2024-11-10 04:38:00 | NPP-375D | MIRANDA DO NORTE | MARANHÃO | Brasil | 2106755 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e9c70e6c-8fff-3137-b56c-53903884b2b8 | -3.61288 | -47.52285 | 2024-11-10 04:38:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7c170d47-1370-3872-aa4a-604d512291bf | -3.16955 | -49.10042 | 2024-11-10 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f4950d55-5a50-322c-9801-5cb7a8f3ac46 | -2.76502 | -49.35078 | 2024-11-10 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 20.8 |
| 3b5a081b-5c7d-3d90-a1dc-1eb1239c3b5f | -2.41835 | -49.87003 | 2024-11-10 04:38:00 | NPP-375D | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 91f64eb7-1a1c-3544-86ca-b41452d3c4b2 | -3.74113 | -50.45029 | 2024-11-10 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| f81e05ab-fed9-37f9-8415-742348341ab6 | -8.4067 | -44.13329 | 2024-11-10 04:38:00 | NPP-375D | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| ac938b0d-a61e-31a2-8abb-af30cb54c00c | -4.72714 | -50.37699 | 2024-11-10 04:38:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| cb25726e-73ee-371d-9ef4-77e124ec8689 | -3.24283 | -46.48508 | 2024-11-10 04:38:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8efe74d2-b07c-3e04-ac5b-7b19436dc849 | -3.034 | -49.53323 | 2024-11-10 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 62e8440c-31af-39a8-852f-5340d350ad7f | -3.96595 | -48.16668 | 2024-11-10 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4789c60f-6263-380d-a84a-fff56fe1e7db | -4.32568 | -48.63478 | 2024-11-10 04:38:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0978d140-a8b7-3f58-90e7-8f23438e0c0e | -3.70878 | -50.43393 | 2024-11-10 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ab2e00f0-ac0a-31e9-9ff2-8ebc582f33a1 | -4.09981 | -45.70104 | 2024-11-10 04:38:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e4058b51-d8c1-337a-9ed1-86c5d68f6046 | -8.8461 | -47.70112 | 2024-11-10 04:38:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7fb726c8-5f84-3747-83a9-c9c7499fc6fd | -4.18605 | -49.77885 | 2024-11-10 04:38:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 34fc0a0f-a78d-37eb-8a65-eab373a3713c | -2.82126 | -48.34953 | 2024-11-10 04:38:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1760d33b-81d3-33d2-b52e-7e8f613f578e | -4.06182 | -48.31322 | 2024-11-10 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a6ad945c-9f30-3408-83d1-9efd0baac41b | -2.71148 | -51.33986 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5ec1333d-e6d9-300e-85bf-5da00d6e7865 | -3.0793 | -50.57187 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fddfb49d-ad04-3082-877f-3174c1e595a2 | -3.78275 | -53.70852 | 2024-11-10 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b800ef89-e2ed-3792-8e1e-10fc31cc771f | -2.857 | -49.83566 | 2024-11-10 04:38:00 | NPP-375D | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 53cd23f5-2efa-3029-84af-05b75f9f5dc2 | -4.59312 | -48.48478 | 2024-11-10 04:38:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0623a6c4-5e1e-3a2f-83d6-4debd986577b | -2.84212 | -53.97794 | 2024-11-10 04:38:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 3a13b7bc-02ed-3f7e-beb1-666334c74e99 | -3.13269 | -50.3678 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a65c504e-70f4-3da9-9af9-e1b6f690d866 | -4.18204 | -48.79591 | 2024-11-10 04:38:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3caa405e-0ff3-3c94-a519-57f8761550df | -4.40823 | -48.60522 | 2024-11-10 04:38:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9cf70253-a548-3460-96a5-113d6198ceb1 | -5.14402 | -48.24941 | 2024-11-10 04:38:00 | NPP-375D | SÃO PEDRO DA ÁGUA BRANCA | MARANHÃO | Brasil | 2111532 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 74815bf9-6c84-3fac-9c5a-482cf1d772fa | -7.43141 | -39.76682 | 2024-11-10 04:38:00 | NPP-375D | EXU | PERNAMBUCO | Brasil | 2605301 | 26 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 6fe4beb4-7493-3002-9faa-fd161b2a8fed | -2.46194 | -50.25666 | 2024-11-10 04:38:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 99192f57-77e7-37dd-adf1-009c3c803379 | -2.42109 | -50.42489 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c3f5ecfe-47f3-306c-aeb6-27f965c65d6e | -3.12535 | -50.14983 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 282af842-5e3e-3128-ae9e-cd28f0868aa5 | -2.6961 | -51.69069 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 89e07751-adf5-3a4b-9409-fd824a5a03a3 | -4.20998 | -48.12247 | 2024-11-10 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 307fc9fe-abcf-3ebd-b6ea-acf1c78864f5 | -3.52536 | -50.00161 | 2024-11-10 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 86b5d4af-7ff5-3248-b18c-106aa8b7eaeb | -2.65509 | -48.47881 | 2024-11-10 04:38:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 43dde97e-d397-33f3-b90c-c075d967d38d | -2.80923 | -49.83183 | 2024-11-10 04:38:00 | NPP-375D | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a68b339c-9d20-3c5a-937b-3b50f4d4e72d | -3.02421 | -47.95996 | 2024-11-10 04:38:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 43d9b91c-57e1-308f-9e70-8110ebcc0fb5 | -3.95766 | -48.17607 | 2024-11-10 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 17.6 |
| 2e348004-1610-3786-8944-167bd9c84967 | -8.38565 | -44.13006 | 2024-11-10 04:38:00 | NPP-375D | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 68233d20-c55e-33a8-bf95-01b8400e7084 | -2.67911 | -51.94064 | 2024-11-10 04:38:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| bdf13725-fc1c-30ca-be6d-cad7a5864641 | -3.13855 | -49.12398 | 2024-11-10 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 21b36b06-f9d8-3a0e-8ffd-9ba23da5ece5 | -2.37665 | -50.42211 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c29c6e9b-81da-3471-8d1a-86ef429d0c55 | -2.75669 | -49.36022 | 2024-11-10 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 22.2 |
| 9ae59b48-50b2-3256-9146-83070c63bb7e | -4.21676 | -45.44996 | 2024-11-10 04:38:00 | NPP-375D | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 93a0a98e-9ee3-3952-ab17-24afa8eb2b6c | -2.23545 | -53.77689 | 2024-11-10 04:38:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 340c2a23-b887-30a6-b584-5cd472c059d3 | -1.42927 | -55.26886 | 2024-11-10 04:38:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| dac20aa1-2cf4-37fd-91c8-e310461d1c98 | -4.21466 | -48.60996 | 2024-11-10 04:38:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b70e930d-b70f-3498-beaa-0c0b4083696b | -2.25211 | -50.41495 | 2024-11-10 04:38:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| dcbb371a-0d99-32b2-9ade-8c0dab43f72c | -2.84087 | -49.42776 | 2024-11-10 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 99bf912c-7abe-3ab1-85b9-6a10fe698601 | -10.00121 | -48.494 | 2024-11-10 04:38:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7fe9e2c0-3688-315d-9e5e-8a0a6ff95849 | -4.76711 | -49.48708 | 2024-11-10 04:38:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 7b43e0fe-2b41-3b22-8da0-1529aab14afc | -3.91933 | -47.9489 | 2024-11-10 04:38:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7298bf89-f6e1-3dc7-8526-d6796b78a845 | -2.25492 | -52.20742 | 2024-11-10 04:38:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 8efa0732-621f-3507-b5d1-a899894a1a38 | -3.342 | -45.79015 | 2024-11-10 04:38:00 | NPP-375D | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |


[Clique aqui para ver as próximas entradas](README114.md)
