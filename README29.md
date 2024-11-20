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

## Dados Diários - Página 29

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| de3c3118-d8e2-32fc-8e04-33cbf639e8ec | -2.65546 | -46.23783 | 2024-11-20 04:25:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 924192c3-5ff1-3b96-bc9a-bc21cfcadb05 | -3.5935 | -43.62793 | 2024-11-20 04:25:00 | NOAA-21 | NINA RODRIGUES | MARANHÃO | Brasil | 2107209 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e9fd013e-ff31-300c-8962-fcc70eeb27c5 | -1.73743 | -45.58304 | 2024-11-20 04:25:00 | NOAA-21 | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 5.6 |
| a0f49f6e-39ea-332b-a397-5cd653b6f91e | -2.67932 | -49.24628 | 2024-11-20 04:25:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b691ba1c-daf3-3f4b-a9ce-78ac91acd254 | -2.53187 | -46.37477 | 2024-11-20 04:25:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d45a8ca0-7838-3522-b298-dc3507a68507 | -2.30043 | -48.49308 | 2024-11-20 04:25:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e00f79fd-7e42-37c7-8d2d-df7a4d0ed5a9 | -1.94922 | -45.57775 | 2024-11-20 04:25:00 | NOAA-21 | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 876f5cc5-8657-3d10-9373-03cafd8db383 | 0.61595 | -51.7722 | 2024-11-20 04:25:00 | NOAA-21 | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 3bf0c5de-6252-3ea7-bbda-cb989be77e89 | -2.68504 | -46.17875 | 2024-11-20 04:25:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| abc17d67-cb38-3015-b8a7-9130be844e7e | -0.19539 | -51.63066 | 2024-11-20 04:25:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 3.7 |
| a8bf1ba7-1d55-349a-8221-224fd0aa8194 | -3.14903 | -45.90953 | 2024-11-20 04:25:00 | NOAA-21 | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3a49308d-527c-3bfe-a166-16b7831ec106 | -0.95201 | -51.724 | 2024-11-20 04:25:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 61693bc3-0567-3973-90b9-83558c8304dc | -1.47584 | -51.96852 | 2024-11-20 04:25:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 99683055-dae2-3a84-908c-663982e351c3 | -0.90182 | -51.72517 | 2024-11-20 04:25:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a7d1ccac-7f8e-32af-a680-c9991f78897f | -2.05709 | -53.4363 | 2024-11-20 04:25:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 11a81156-0fc5-359b-89b8-38351db875c0 | -1.99605 | -46.6053 | 2024-11-20 04:25:00 | NOAA-21 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 88a1325d-bc37-3142-88f4-8c1650b68e74 | -1.90964 | -50.61027 | 2024-11-20 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3702e967-b6b5-365d-9b98-b7dbeba20c98 | -2.71996 | -46.08535 | 2024-11-20 04:25:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| eea2f640-5b6b-3e50-9381-3a134fe6973b | -2.36199 | -48.60554 | 2024-11-20 04:25:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4506fe83-8a53-3615-871a-f8fdad40a1be | -1.44843 | -52.66563 | 2024-11-20 04:25:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 3dc9c054-02b9-3d5c-a349-aeea66a64a8d | -2.72077 | -49.34245 | 2024-11-20 04:25:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| a17c0d13-bcd6-3f22-b3b0-263e4274a389 | -2.22415 | -46.47253 | 2024-11-20 04:25:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 688c6207-3dff-3c44-9657-cdf95567f985 | -2.61028 | -49.25861 | 2024-11-20 04:25:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| fe765f7f-f17f-375a-938d-15519557e720 | -2.06289 | -53.43149 | 2024-11-20 04:25:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 3c1c1b0d-4187-3548-a895-300f1c47421a | -2.68742 | -46.22861 | 2024-11-20 04:25:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ae86017f-bd57-3850-a6fa-fa544d0e2474 | -2.21218 | -46.35305 | 2024-11-20 04:25:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 69169b2e-dca4-3ce3-abd4-2e24713313b8 | -2.8425 | -46.67313 | 2024-11-20 04:25:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| aeb0151c-7fb1-3fb8-84e8-507b84d6385e | -0.19093 | -51.62996 | 2024-11-20 04:25:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 8a9c0b20-f7b9-3fe9-a9c3-9f0303373eb3 | -0.27753 | -51.39096 | 2024-11-20 04:25:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 51a915d1-1fdb-399b-8cd6-2b379e2c6dcd | -2.50217 | -46.21772 | 2024-11-20 04:25:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2c5360d0-9d54-3c54-879b-d9f4cb859f41 | -2.65877 | -46.23835 | 2024-11-20 04:25:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 630ced4c-3427-333e-b0d7-201475e92930 | -2.15929 | -49.14531 | 2024-11-20 04:25:00 | NOAA-21 | IGARAPÉ-MIRI | PARÁ | Brasil | 1503309 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e06c239c-7847-3618-9ffc-1166e920040a | -2.66979 | -46.23296 | 2024-11-20 04:25:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7bb25a38-f1c7-392b-90f8-3b3d6a4eb5e9 | -2.69235 | -46.21877 | 2024-11-20 04:25:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a602a76f-afbd-339b-a84d-a1b23492457d | -2.00583 | -49.00402 | 2024-11-20 04:25:00 | NOAA-21 | IGARAPÉ-MIRI | PARÁ | Brasil | 1503309 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bf308b99-cfc8-30a2-9bc0-9e395f87d529 | -2.21586 | -46.48198 | 2024-11-20 04:25:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 94a10fbc-3cb2-3bd2-8bfd-0e6f3dd583fd | -2.61927 | -48.21623 | 2024-11-20 04:25:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d85407be-b860-3790-84dc-4a9445cbb3c0 | -2.21865 | -46.48598 | 2024-11-20 04:25:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 3fbd28a0-5e08-373c-8b6c-0c5c328d541e | -2.24662 | -48.44451 | 2024-11-20 04:25:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a18f9b6f-fc3f-38b0-804a-2c5d5fb32b43 | -1.14971 | -53.51711 | 2024-11-20 04:25:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| c29f7b32-f92d-3f3e-92fb-532ee98a686e | -2.6952 | -46.24397 | 2024-11-20 04:25:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 18fac28a-3b1c-3b31-9ae7-59b6aaa8bcee | -2.78834 | -45.99734 | 2024-11-20 04:25:00 | NOAA-21 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b15b7d72-31d3-3173-a6f7-c71c6881e397 | -0.96464 | -51.73043 | 2024-11-20 04:25:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 67eb93a7-9c2a-3aad-a4f8-4a554910ba62 | -1.69953 | -52.35555 | 2024-11-20 04:25:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 107b8d44-1c1b-3650-9aec-d9366dc9abc6 | -2.66262 | -46.23539 | 2024-11-20 04:25:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| eaad1794-57d9-3d93-8beb-aac90043c479 | -2.18416 | -48.40188 | 2024-11-20 04:25:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bd202a80-7251-3d78-bcc1-3b84777c582c | -1.54837 | -52.27226 | 2024-11-20 04:25:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 4ee3287f-5f09-3523-a308-c2daccd2aa43 | -2.26672 | -45.45831 | 2024-11-20 04:25:00 | NOAA-21 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e7144f1e-c73c-3319-8f09-40f0a8080339 | -2.71538 | -47.97775 | 2024-11-20 04:25:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ec1c7e8f-9928-3446-b37e-c2e5f72b918c | -1.60373 | -52.24765 | 2024-11-20 04:25:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3a4f7cfc-c8fd-32a9-bb9d-ade2572541c5 | -2.64323 | -46.20764 | 2024-11-20 04:25:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8ba91a7f-59d5-3f6e-8a99-d033b1a8cc61 | -1.99659 | -46.60179 | 2024-11-20 04:25:00 | NOAA-21 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 25556b9d-ccf5-3448-b442-14abadb1ce2b | -2.6397 | -46.83553 | 2024-11-20 04:25:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f2d63863-ff3e-39db-b1dd-f49eb6e0b8d6 | -2.68635 | -46.08369 | 2024-11-20 04:25:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 864f09ee-7901-3ea5-9669-991c6d030a29 | -2.4555 | -49.1487 | 2024-11-20 04:25:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b9a4dd14-ce69-314a-b727-0d6c90b153a8 | -2.67896 | -46.17428 | 2024-11-20 04:25:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 149fa928-404c-3753-a06c-291cb36731cb | -2.22271 | -49.7174 | 2024-11-20 04:25:00 | NOAA-21 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 50a6d68f-9d4e-3e55-8b0e-bf10187bcc70 | -3.59754 | -43.62462 | 2024-11-20 04:25:00 | NOAA-21 | NINA RODRIGUES | MARANHÃO | Brasil | 2107209 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a99622c8-4544-3510-be1b-e52e02376220 | -2.51564 | -44.99689 | 2024-11-20 04:25:00 | NOAA-21 | PERI MIRIM | MARANHÃO | Brasil | 2108405 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 09cf0845-b53d-3465-b196-0b1077f1af05 | -2.54193 | -46.22383 | 2024-11-20 04:25:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ec659f13-00a9-3350-8fe5-fa7674960ed8 | -2.61183 | -48.24644 | 2024-11-20 04:25:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9648ca0d-7a1a-30de-bc68-7aaeee9278c6 | -1.20034 | -53.67952 | 2024-11-20 04:25:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| c9290420-18c9-3572-b11e-a65176cf0e7a | -2.58049 | -48.39576 | 2024-11-20 04:25:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a7fb428d-a5b9-30f1-b261-5b6635e80964 | -2.81529 | -46.67251 | 2024-11-20 04:25:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2a4b9f33-7229-37c2-9ef6-63a677634bc9 | -2.24367 | -46.8247 | 2024-11-20 04:25:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a7b79a6f-0bf2-3033-8e44-37de38dbc970 | -2.54132 | -46.20605 | 2024-11-20 04:25:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b1fab5a4-b2a6-31bb-967a-bcc852fe76ca | -2.30755 | -48.4942 | 2024-11-20 04:25:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 21.6 |
| 1d1e2c83-09c9-389d-9805-80b988c6c331 | -2.27003 | -45.45881 | 2024-11-20 04:25:00 | NOAA-21 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3d9d384c-0fe9-38f0-9185-038de6f4da4f | -2.63189 | -46.84154 | 2024-11-20 04:25:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6b4cfefc-d20c-3de5-a303-931a082123d8 | -3.07444 | -45.86285 | 2024-11-20 04:25:00 | NOAA-21 | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| beb263f8-bad9-3ac8-bd02-734169ba1474 | -1.48192 | -51.16009 | 2024-11-20 04:25:00 | NOAA-21 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| eb2fbf18-5699-3989-944c-d2a01464479c | -2.61534 | -48.24698 | 2024-11-20 04:25:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 409c8de3-8af0-360e-a029-db0053405084 | -2.22143 | -46.48998 | 2024-11-20 04:25:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3ea35f1e-61a9-3d3e-80b8-efe5ee8e8b19 | -2.61677 | -45.89684 | 2024-11-20 04:25:00 | NOAA-21 | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 18.6 |
| 94092f08-4975-3c20-908e-fa68d33f9948 | -2.5397 | -46.21641 | 2024-11-20 04:25:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ade86871-8246-36fd-ae33-d7067e363f4b | -1.16033 | -46.74804 | 2024-11-20 04:25:00 | NOAA-21 | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9ce3f9cc-054c-394d-8452-62d16f208c26 | -2.70844 | -47.97669 | 2024-11-20 04:25:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 79d18b2a-d71f-363e-b086-4c0c800a27a7 | -2.56172 | -48.17136 | 2024-11-20 04:25:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 31e7dcd6-b7f5-3ce8-824d-2dd1eada13c3 | -2.60464 | -48.21798 | 2024-11-20 04:25:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fa811fe1-8ef6-351c-ae3a-8c012be633b9 | -1.86192 | -47.82481 | 2024-11-20 04:25:00 | NOAA-21 | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a2a3f8f3-3840-374d-911b-ed52cc652780 | -2.84125 | -46.61567 | 2024-11-20 04:25:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 57a4e3dd-73e4-314e-b11f-6515ce56dfb6 | -2.31875 | -46.86526 | 2024-11-20 04:25:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 64ddbf37-a770-36d2-bf48-a4e3069567a9 | -2.14221 | -50.64725 | 2024-11-20 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| afffd0fa-c7dd-3d23-8710-a7458721c8f2 | -2.17186 | -46.39312 | 2024-11-20 04:25:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9f06fc3e-e868-3015-b666-0a50cbbb0ffd | -1.72914 | -52.69746 | 2024-11-20 04:25:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c75e279a-bb0a-3bd2-a7d7-6bfcb86d8360 | -1.14157 | -51.69354 | 2024-11-20 04:25:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| cfba7a50-4234-3304-a5f5-3e275eddbd7d | -2.51979 | -46.40849 | 2024-11-20 04:25:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8f3c79fb-5b46-3b0b-be8f-4a3c1aec2c20 | -3.07775 | -45.86336 | 2024-11-20 04:25:00 | NOAA-21 | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7629cf97-d81f-36b1-9184-6e69784cadf6 | -3.09428 | -45.97847 | 2024-11-20 04:25:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 245b0485-7400-3778-ab78-cfcf9b24efd9 | -1.13708 | -53.65934 | 2024-11-20 04:25:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cc13f27b-dee8-3e33-bbdf-af7d224ec04b | -1.63277 | -52.62466 | 2024-11-20 04:25:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 41881126-e6ac-3560-9ad6-3ffde7d5b6ae | -1.85844 | -47.82429 | 2024-11-20 04:25:00 | NOAA-21 | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 21dbd831-921b-39e1-8755-8bd8b2b59711 | -1.86572 | -46.80235 | 2024-11-20 04:25:00 | NOAA-21 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 95fe200e-4336-3d2c-b3cd-241f30dbce55 | -1.25052 | -53.36407 | 2024-11-20 04:25:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 52bf80fc-4509-33e5-a6c8-07b11bb6f046 | -1.32456 | -52.4047 | 2024-11-20 04:25:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 12.0 |
| 00332bab-24b7-3c1a-81fa-0fd44d11566d | -1.25465 | -53.37008 | 2024-11-20 04:25:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| c6b55c9d-1e63-3642-9864-5c4dd8af698a | -1.86963 | -46.79931 | 2024-11-20 04:25:00 | NOAA-21 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d06dced2-bd93-31f6-bffa-cfb229933136 | 0.64484 | -50.73748 | 2024-11-20 04:25:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3ae9cea3-8227-3d7b-a013-5bfaa6be114d | -1.96227 | -49.54939 | 2024-11-20 04:25:00 | NOAA-21 | LIMOEIRO DO AJURU | PARÁ | Brasil | 1504000 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9a60e35d-0f13-32fd-873b-a783f0dbbff4 | -2.60525 | -48.21406 | 2024-11-20 04:25:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |


[Clique aqui para ver as próximas entradas](README30.md)
