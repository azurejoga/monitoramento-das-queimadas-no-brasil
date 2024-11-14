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

## Dados Diários - Página 51

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 922f6e48-8340-3290-9260-435abadd88fa | -17.58418 | -57.55651 | 2024-11-14 05:05:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 16.4 |
| 33f61b38-831d-36a2-afba-c29dd9893bb4 | -17.57696 | -57.53655 | 2024-11-14 05:05:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.1 |
| b706dab0-8969-3161-a5ee-5485b2621f73 | -17.24925 | -57.46776 | 2024-11-14 05:05:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 14.7 |
| d6e4cd6d-3136-36c7-ac86-abaedc5e664d | -17.59931 | -57.48024 | 2024-11-14 05:05:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 8.9 |
| 6624dff3-d533-38f4-a56e-52fee49c5b8e | -17.57584 | -57.54386 | 2024-11-14 05:05:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 7f0e23f1-3b82-32aa-89d7-da628fecbb67 | -15.99004 | -57.59174 | 2024-11-14 05:05:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 7a6b1f26-43c9-3256-8ed4-e60718886819 | -17.5882 | -57.44079 | 2024-11-14 05:05:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 6b6a08f4-c937-3d35-ba4c-35407252bdc3 | -15.87172 | -59.29542 | 2024-11-14 05:05:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 308a9b02-0f80-3c20-b9ee-03875b7aab5a | -14.49931 | -56.9192 | 2024-11-14 05:05:00 | NPP-375D | ARENÁPOLIS | MATO GROSSO | Brasil | 5101308 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 793305a2-57e7-3a17-9470-1552ebc6a16c | -17.57475 | -57.52868 | 2024-11-14 05:05:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 16.2 |
| e6dd4f0c-17f3-38ac-8f9e-b645e30403f9 | -17.59765 | -57.46869 | 2024-11-14 05:05:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 989b742c-cb56-329f-8872-53e70acac834 | -17.6332 | -57.5497 | 2024-11-14 05:05:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.8 |
| cb9ef929-f400-3f66-b9c9-a80c1c0af6ea | -16.0764 | -59.70736 | 2024-11-14 05:05:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6d6bc2dc-e2da-333d-b041-31de84effa6d | -15.46472 | -57.25151 | 2024-11-14 05:05:00 | NPP-375D | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 65e9b880-ebbe-30df-aad0-00d4aab1483b | -17.59532 | -57.55087 | 2024-11-14 05:05:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 7af632fb-3e52-3286-9d29-843347f2f528 | -17.58365 | -57.53766 | 2024-11-14 05:05:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| fb74edd9-abaf-3525-905f-2ca91529b5cf | -17.5853 | -57.54919 | 2024-11-14 05:05:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.6 |
| 175c9b0e-a2ac-307b-827b-116c53ec23b7 | -17.60869 | -57.5531 | 2024-11-14 05:05:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.5 |
| 48492b97-036d-3dc2-8462-a4e50432a208 | -17.57862 | -57.54807 | 2024-11-14 05:05:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 4900aa3f-708b-314e-bb29-7ba006bf76f4 | -17.57808 | -57.52924 | 2024-11-14 05:05:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 3caa8820-64b5-37dc-8827-1c7fc40486c2 | -17.70789 | -57.54281 | 2024-11-14 05:05:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 70470ae4-6b8b-3c8a-9d11-db3413bca868 | -15.99849 | -59.10065 | 2024-11-14 05:05:00 | NPP-375D | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 64cd467f-9121-38ab-8eda-9dea49c68a78 | -17.24257 | -57.46666 | 2024-11-14 05:05:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 10fe876d-2447-31b0-af0a-b6adf8139599 | -17.59375 | -57.47179 | 2024-11-14 05:05:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.2 |
| abf942e1-5116-3587-92f1-61b8a8e9d427 | -17.2938 | -57.46771 | 2024-11-14 05:05:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 7126db16-dc1e-3e5a-83c7-2e49b4491a48 | -21.55239 | -55.82045 | 2024-11-14 05:08:00 | NPP-375D | GUIA LOPES DA LAGUNA | MATO GROSSO DO SUL | Brasil | 5004106 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9332de5d-81fd-3def-a43a-cc070ef89dbb | -23.1035 | -52.09488 | 2024-11-14 05:08:00 | NPP-375D | ATALAIA | PARANÁ | Brasil | 4102208 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| e0e0690b-00f5-3d94-9b52-2c9cc08fefb1 | -20.6968 | -48.80194 | 2024-11-14 05:08:00 | NPP-375D | OLÍMPIA | SÃO PAULO | Brasil | 3533908 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 04dd0044-38b2-3e89-9837-4382c1c03330 | -21.55604 | -55.82097 | 2024-11-14 05:08:00 | NPP-375D | GUIA LOPES DA LAGUNA | MATO GROSSO DO SUL | Brasil | 5004106 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7bb54fa7-8af1-3620-81a6-94eae0f82822 | -26.91914 | -52.71338 | 2024-11-14 05:08:00 | NPP-375D | CORONEL FREITAS | SANTA CATARINA | Brasil | 4204400 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 1e89fa7b-1e0a-32f5-8f23-a373802e22c8 | -21.5105 | -57.91899 | 2024-11-14 05:08:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 5225bdba-05aa-3caa-bf2c-eb7964255314 | -21.90844 | -56.45866 | 2024-11-14 05:08:00 | NPP-375D | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d14e3051-86cc-3ac9-a1b4-c9f016cd40cd | -20.69293 | -48.80345 | 2024-11-14 05:08:00 | NPP-375D | OLÍMPIA | SÃO PAULO | Brasil | 3533908 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| 92978ea0-cd56-3ee7-8665-0ac2f5d1610d | -21.84631 | -56.43566 | 2024-11-14 05:08:00 | NPP-375D | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 3be16ba0-170c-34bd-936f-13b07ef63b8d | -20.38605 | -55.69256 | 2024-11-14 05:08:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8daa1947-4d30-303b-b6a5-788160b6c312 | -23.10579 | -52.09401 | 2024-11-14 05:08:00 | NPP-375D | ATALAIA | PARANÁ | Brasil | 4102208 | 41 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| 26c461d2-f66f-349c-b766-e3944ac34d8f | -20.55758 | -56.15024 | 2024-11-14 05:08:00 | NPP-375D | MIRANDA | MATO GROSSO DO SUL | Brasil | 5005608 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d7e4df47-00f3-3141-a69a-7c9b63e6827f | -19.57979 | -54.88843 | 2024-11-14 05:08:00 | NPP-375D | RIO NEGRO | MATO GROSSO DO SUL | Brasil | 5007307 | 50 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 2eefcf6f-939b-397f-a9b2-14a1bc5240c9 | -20.69122 | -48.80141 | 2024-11-14 05:08:00 | NPP-375D | OLÍMPIA | SÃO PAULO | Brasil | 3533908 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 1fcf62ce-5ea8-3c10-8be5-fa8399b317a6 | -21.90667 | -56.46079 | 2024-11-14 05:08:00 | NPP-375D | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4e78761a-e4df-3b8a-925e-9e0c1c2016af | -21.85341 | -56.43681 | 2024-11-14 05:08:00 | NPP-375D | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9f5719cf-0c4f-36f1-9af8-194b20668ad8 | -23.10813 | -52.09563 | 2024-11-14 05:08:00 | NPP-375D | ATALAIA | PARANÁ | Brasil | 4102208 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 8c2f223c-1bc8-34d4-9b30-7b9947a13192 | -21.90726 | -56.4565 | 2024-11-14 05:08:00 | NPP-375D | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| dbd7722a-b900-3ee9-9b14-5cae6d9c0331 | -23.96092 | -54.04375 | 2024-11-14 05:08:00 | NPP-375D | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 5.1 |
| 2be5c53e-b4f0-3ebc-b2c3-99614504ce38 | -22.6839 | -50.47398 | 2024-11-14 05:08:00 | NPP-375D | ASSIS | SÃO PAULO | Brasil | 3504008 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 27e42396-f3d1-3a4b-9e3d-3271c4474d39 | -21.84986 | -56.43623 | 2024-11-14 05:08:00 | NPP-375D | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 7.5 |
| db3dc061-1627-3888-a784-705a3804e193 | -23.96045 | -54.04778 | 2024-11-14 05:08:00 | NPP-375D | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 5.1 |
| fcd4418e-0858-3ff0-87dd-57e39eb52451 | -21.07479 | -54.22045 | 2024-11-14 05:08:00 | NPP-375D | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4782e9d6-ae1d-323f-8f7e-4c8b3aed11a7 | -20.47644 | -53.67483 | 2024-11-14 05:08:00 | NPP-375D | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 770a5696-8c16-3f98-8216-1fb16aed7e9b | -21.55177 | -55.82491 | 2024-11-14 05:08:00 | NPP-375D | GUIA LOPES DA LAGUNA | MATO GROSSO DO SUL | Brasil | 5004106 | 50 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f24e0c35-2e6f-374b-906c-d4960c3f437c | -21.90489 | -56.45807 | 2024-11-14 05:08:00 | NPP-375D | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bafc938e-52bd-3230-97a4-5a4370ced590 | -1.643 | -53.2677 | 2024-11-14 05:10:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 69.2 |
| 0a742746-c748-3ac2-b4a3-82314b488647 | -1.8105 | -52.1857 | 2024-11-14 05:10:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 53.3 |
| d622e869-c20c-3c6d-86d7-e0658f5525d0 | -1.8106 | -52.1652 | 2024-11-14 05:10:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 58.2 |
| 032ee5c1-aeda-37ec-bba6-b27b83cb6113 | -1.7922 | -52.1655 | 2024-11-14 05:20:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 52.9 |
| eb1458b7-9b4c-3222-886c-f5e5a436cf21 | -1.643 | -53.2677 | 2024-11-14 05:20:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 69.7 |
| 4e9ccf4c-029f-3542-b0c5-7cb8cee46933 | 0.85332 | -50.20913 | 2024-11-14 05:27:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3cf7717d-045f-3b76-b991-6232b2539ccc | -3.46528 | -50.3123 | 2024-11-14 05:27:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f1d73caf-7464-3ede-b0b9-9441bf19dcf0 | -2.87422 | -51.79818 | 2024-11-14 05:27:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8ae979b9-d5fb-333c-8d77-b44dfd346033 | -1.94784 | -52.15973 | 2024-11-14 05:27:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| da7ca610-a839-38e4-a293-4eaf62df7ab8 | -1.40078 | -51.13598 | 2024-11-14 05:27:00 | NOAA-20 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b413d54e-eeb4-3844-81cf-44f974f48cb6 | -1.38625 | -51.11823 | 2024-11-14 05:27:00 | NOAA-20 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| c944332d-3d89-3a39-9ecb-c8318f9da972 | -1.80537 | -52.17791 | 2024-11-14 05:27:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 38fa6eb1-c193-3681-a107-8fb3169039b1 | -0.8971 | -51.72931 | 2024-11-14 05:27:00 | NOAA-20 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e478530d-d798-39f9-a313-7d93be1f8419 | -1.36709 | -52.3352 | 2024-11-14 05:27:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c7a40287-5927-3d18-94b1-53ef0129ba1a | -0.90759 | -52.42127 | 2024-11-14 05:27:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c992c09c-9676-3258-9567-a52684ccb34d | -0.20237 | -51.50613 | 2024-11-14 05:27:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 935517c4-08d5-39e6-9e06-03bb86c8f860 | -1.38567 | -51.12204 | 2024-11-14 05:27:00 | NOAA-20 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d10827c5-a2cd-3eca-8990-67166cb69a86 | -0.20076 | -51.51628 | 2024-11-14 05:27:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 53569343-7467-3e04-94c3-05a707191352 | -1.63718 | -53.26915 | 2024-11-14 05:27:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 22.9 |
| 2f75cc95-e570-3a28-a638-9ef9036736a3 | 2.62208 | -60.41175 | 2024-11-14 05:27:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d66da908-7398-39bc-93d4-9f6369c41b0b | -1.39517 | -51.13512 | 2024-11-14 05:27:00 | NOAA-20 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 852859d3-8e0f-3fb1-ae24-32b2842267b1 | -3.49535 | -50.83462 | 2024-11-14 05:27:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| a092f2d9-4c9a-379d-ab8e-cd2ce510dfee | -1.94835 | -52.15645 | 2024-11-14 05:27:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 35a5a89b-4e82-34d0-8088-e5c2481a46f1 | -2.08568 | -47.73413 | 2024-11-14 05:27:00 | NOAA-20 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 4896e6a4-cb1b-32c5-bde7-580579f82b82 | -1.21084 | -51.78452 | 2024-11-14 05:27:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e0cbac8c-d239-3ebc-b965-58a1d646ae7a | -1.5542 | -51.85863 | 2024-11-14 05:27:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 598af90a-5f1e-3a8d-a1eb-01c36988e7de | -2.28995 | -53.80253 | 2024-11-14 05:27:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0519b94e-adee-3ef6-854a-3c233769c8b1 | -3.48504 | -50.26282 | 2024-11-14 05:27:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 32ee8412-58e1-32b8-a5db-7d8cac0c2bd6 | 1.05815 | -60.60417 | 2024-11-14 05:27:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| df68cd90-35b1-38c9-a72c-1aeb728ca7d1 | -3.47825 | -50.26652 | 2024-11-14 05:27:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 4311f823-bcf6-3472-bcaf-2e38952cfc26 | 0.84669 | -50.20895 | 2024-11-14 05:27:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 215ae9ec-9c81-382e-be3e-fb2cdac5bdcf | -1.41903 | -53.47592 | 2024-11-14 05:27:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 111c4686-c5ed-3e50-933d-fb83e924aeca | -1.13571 | -53.66017 | 2024-11-14 05:27:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6ad08a82-a209-3663-be39-6461328fbe09 | 0.90826 | -50.14664 | 2024-11-14 05:27:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2632dcc5-aebd-36dc-9350-a861e9345ae8 | -3.47893 | -50.26189 | 2024-11-14 05:27:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d1bb4aa4-b521-353b-a4ac-cadfcdcae812 | -2.11711 | -50.68476 | 2024-11-14 05:27:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f3301fbe-ad95-3b43-a9bc-7d528c297d55 | -2.87364 | -51.79753 | 2024-11-14 05:27:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| a9afc097-210e-3c0d-86a5-ccd24afcd946 | -2.89561 | -54.60567 | 2024-11-14 05:27:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ac72c69a-8841-3489-95b7-bbcfdb0a7423 | -1.38683 | -51.11443 | 2024-11-14 05:27:00 | NOAA-20 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| ab7322fc-032e-3770-8800-cd798139d974 | -1.21136 | -51.78115 | 2024-11-14 05:27:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 07d6de0b-05c5-3740-92d3-40cea9fc628a | -3.80825 | -47.80192 | 2024-11-14 05:27:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| da82372e-6053-354c-95b4-28ed0d65876a | -0.41136 | -51.57791 | 2024-11-14 05:27:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3b8fba79-0e51-3034-8457-1941e758e0d9 | -2.84048 | -56.78824 | 2024-11-14 05:27:00 | NOAA-20 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 0a61702d-c513-3f7b-b521-4de2ae7bb07c | -1.2107 | -51.74988 | 2024-11-14 05:27:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 0.2 |
| d882d1b2-14f1-353a-a967-3ad2dd85731a | -1.80059 | -52.17392 | 2024-11-14 05:27:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 1e67a35a-46f9-3161-9e7c-4420dbd5120a | -1.35208 | -53.08733 | 2024-11-14 05:27:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 756d3ea2-423c-39b1-b42f-a28c1c92be8f | 0.84756 | -50.21004 | 2024-11-14 05:27:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6f73be5b-659f-3009-a6cc-889d9c63fe19 | -2.83657 | -56.78766 | 2024-11-14 05:27:00 | NOAA-20 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 6b7f7206-44bd-3607-bee9-01f936716c2c | -0.20183 | -51.50952 | 2024-11-14 05:27:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.8 |


[Clique aqui para ver as próximas entradas](README52.md)
