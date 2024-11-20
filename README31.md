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

## Dados Diários - Página 31

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a0aac70d-ca92-3038-9062-4e57b55c96cc | -3.1077 | -53.7408 | 2024-11-20 04:27:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9c810063-7c0e-399b-b58e-f67b6ba25c05 | -8.00033 | -44.37581 | 2024-11-20 04:27:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9170e084-fca5-3508-85e1-5bebc8a22bc3 | -3.31575 | -54.74516 | 2024-11-20 04:27:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1e08431e-c6a5-3991-ad48-9a8f458e7a01 | -3.78534 | -44.06846 | 2024-11-20 04:27:00 | NOAA-21 | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| af0a917a-d471-3068-bd85-2bb3461ccd47 | -2.93244 | -49.42618 | 2024-11-20 04:27:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3569df3f-81ab-3fa1-b428-4d5082fab2e5 | -5.97347 | -45.35027 | 2024-11-20 04:27:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5cbd930e-83d5-3f74-9bfb-ed21348ffb44 | -2.93854 | -48.33557 | 2024-11-20 04:27:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9dc665c3-4b0a-3383-bf1e-0031d825e466 | -4.28118 | -50.58221 | 2024-11-20 04:27:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 58599e2f-173a-3727-b01f-53724b03f2d6 | -11.06698 | -41.62137 | 2024-11-20 04:27:00 | NOAA-21 | SÃO GABRIEL | BAHIA | Brasil | 2929255 | 29 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 41dec2d3-e952-336a-b5b6-1662088bfa50 | -3.80235 | -51.14743 | 2024-11-20 04:27:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| c89b83aa-ed0d-3b0c-9471-3516a1c06ed6 | -4.11377 | -51.05315 | 2024-11-20 04:27:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3b083a74-4c57-37b1-9c87-0ee32f2c68f3 | -4.44903 | -46.57964 | 2024-11-20 04:27:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 65f46cac-3900-3000-b27a-abe722c3bf0a | -3.20143 | -54.32895 | 2024-11-20 04:27:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 017d7f1b-69ca-3fd7-b1e5-4a46b7b620d5 | -5.45506 | -49.68954 | 2024-11-20 04:27:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 24b5793d-e21b-3eb6-9496-cc85ef6c3845 | -2.25377 | -53.68114 | 2024-11-20 04:27:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| a87f5425-5c04-35f0-a0f1-c4e232f909e1 | -3.81204 | -52.29237 | 2024-11-20 04:27:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cb94ba8b-506d-3b1f-ad44-797833bf70d1 | -7.56663 | -46.45674 | 2024-11-20 04:27:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d096c29c-4436-3066-8d9c-90b101ce14cd | -4.631 | -49.54193 | 2024-11-20 04:27:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 116313fa-6354-3c51-be72-ad40bace2a2d | -3.88567 | -46.65807 | 2024-11-20 04:27:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6969951b-91df-3568-911e-38d0f63f1564 | -2.63447 | -54.27121 | 2024-11-20 04:27:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 35ce3386-4015-33c5-ab91-2ec12330b772 | -4.41334 | -43.11757 | 2024-11-20 04:27:00 | NOAA-21 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 78596407-03f7-3c46-9a54-5e4154acd455 | -4.09851 | -44.8555 | 2024-11-20 04:27:00 | NOAA-21 | LAGO VERDE | MARANHÃO | Brasil | 2105906 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 90c6af2d-2878-3f82-9d8b-182e7f686fb2 | -4.06066 | -54.05212 | 2024-11-20 04:27:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 96614c9d-f374-3175-b253-84df9f39672e | -5.23634 | -46.24514 | 2024-11-20 04:27:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| db07113f-16e8-37e9-b5bc-bdd9325b85e1 | -3.00597 | -51.01272 | 2024-11-20 04:27:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e8ac0a5f-bac6-32a8-b5b6-aa347ab22c00 | -4.8873 | -45.75582 | 2024-11-20 04:27:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c632e0fe-71f8-3d50-b03f-c33719b86d6b | -2.59594 | -51.7946 | 2024-11-20 04:27:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 89e35bc8-3520-38d2-8d0c-703fc70b4d7e | -10.68907 | -45.00204 | 2024-11-20 04:27:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 798aa221-cd08-322d-9a9b-0dd2d8848d4a | -3.50977 | -53.80159 | 2024-11-20 04:27:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| ddc47499-6152-317e-adcb-51a9f0f80780 | -2.90916 | -53.05518 | 2024-11-20 04:27:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 09458183-4a2a-3dac-a659-013e316d1097 | -8.32177 | -45.11006 | 2024-11-20 04:27:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 63791fdc-8bf1-3e05-b375-3afac5fb1614 | -6.14571 | -41.90798 | 2024-11-20 04:27:00 | NOAA-21 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 871c6213-f9cd-380c-abc4-244ba6649eeb | -5.60125 | -46.17199 | 2024-11-20 04:27:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 62d1e38e-be5d-3852-99c9-a4acf6510bf3 | -2.84919 | -54.00291 | 2024-11-20 04:27:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b0bf2341-35cd-3bc4-8984-bc157effd34e | -2.84857 | -48.67409 | 2024-11-20 04:27:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 4315664c-e487-352c-a410-fe6be2f94314 | -5.39586 | -47.00634 | 2024-11-20 04:27:00 | NOAA-21 | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 220728d3-28d8-3b3d-bf91-150c94335fd8 | -2.92172 | -53.06736 | 2024-11-20 04:27:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 13.7 |
| 5ff44c56-dfba-3850-8441-1619840b6484 | -6.51409 | -47.82975 | 2024-11-20 04:27:00 | NOAA-21 | SANTA TEREZINHA DO TOCANTINS | TOCANTINS | Brasil | 1720002 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 082d9798-2004-335b-b755-93dd355ee2dc | -7.55327 | -45.25923 | 2024-11-20 04:27:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 568e1a55-c81f-3039-8411-4ce5a128090c | -2.62932 | -54.27041 | 2024-11-20 04:27:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 89ba5ce6-37c6-398b-bf79-64f8d3c4d4af | -4.07357 | -46.84778 | 2024-11-20 04:27:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 91d70632-9b15-37a1-a37a-89084e92e758 | -7.22037 | -45.1795 | 2024-11-20 04:27:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 60b1bb07-bf72-322e-a3d7-5b06cbcd5f4e | -4.2679 | -46.06465 | 2024-11-20 04:27:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c07797bb-e417-3390-a48e-6a27d199419b | -2.92641 | -53.06824 | 2024-11-20 04:27:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 13.7 |
| 0446256e-76c2-3b17-a805-a8308a31b266 | -10.49545 | -42.50843 | 2024-11-20 04:27:00 | NOAA-21 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 18f9e436-343d-3569-b732-246f2b08b43a | -7.19039 | -47.92289 | 2024-11-20 04:27:00 | NOAA-21 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| aa6300f6-7de9-3152-9c96-0bf45f247d2a | -3.46926 | -48.2528 | 2024-11-20 04:27:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0aa73b29-4eb2-32e7-bdf0-9ccae9e248e3 | -3.92037 | -46.41534 | 2024-11-20 04:27:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2078da9d-013e-3e3b-b3e4-5d35dc591827 | -5.51198 | -46.44048 | 2024-11-20 04:27:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3e780241-5a33-3a90-9169-255662a1becc | -9.65967 | -44.40448 | 2024-11-20 04:27:00 | NOAA-21 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d493ee58-9741-3eff-92cf-627ff93cb8cf | -3.21141 | -46.46701 | 2024-11-20 04:27:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f07cddcd-0b3e-3c7f-9ded-b1cff2a9cefb | -7.21796 | -45.08255 | 2024-11-20 04:27:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 034a60de-464a-348c-b081-3d37c432b889 | -4.62639 | -46.42398 | 2024-11-20 04:27:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c4650c95-94e1-32d7-baca-8f183060b170 | -3.19729 | -54.32219 | 2024-11-20 04:27:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| e73188a2-60ef-30e5-af4a-a6478e7819d8 | -4.06359 | -46.84623 | 2024-11-20 04:27:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5523ae19-5c85-3a71-ad55-c106c95fb6ee | -5.97796 | -45.36543 | 2024-11-20 04:27:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d18ce4f3-1caa-3a47-9087-244e1bf54ec5 | -3.70528 | -43.46795 | 2024-11-20 04:27:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 0c56c8f7-a2e0-3d0e-830d-3c59beeb5e01 | -2.85375 | -54.00666 | 2024-11-20 04:27:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 62c13408-ab5c-37f9-8932-9ad43544794b | -5.13034 | -49.44316 | 2024-11-20 04:27:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c26f066a-c048-31fe-8b5b-7b4912548e25 | -6.14963 | -41.90848 | 2024-11-20 04:27:00 | NOAA-21 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 309dfaca-fa20-341e-b2eb-9e9fddc718df | -7.17217 | -45.042 | 2024-11-20 04:27:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 77e0808a-bd31-3a1c-91d9-0d77ecbf8cb9 | -4.47374 | -45.65947 | 2024-11-20 04:27:00 | NOAA-21 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| aa365437-348b-38cb-8c9f-a566cf3936cb | -4.20594 | -42.19834 | 2024-11-20 04:27:00 | NOAA-21 | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| e4ae9800-6773-368b-86a7-2be85b006876 | -9.17608 | -44.71673 | 2024-11-20 04:27:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a68277e6-34e0-36a9-9cf7-4958842b8fd9 | -2.74956 | -54.01609 | 2024-11-20 04:27:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a1ec2709-1063-3d18-aa2c-1e75c0a37296 | -3.94166 | -46.71299 | 2024-11-20 04:27:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bd765fb7-81cb-3872-a375-4f0fdf6e38f4 | -6.3794 | -46.21994 | 2024-11-20 04:27:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 38fb20a5-0a17-38ae-85f3-c2460e32302c | -6.98529 | -47.08778 | 2024-11-20 04:27:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 467b8dd4-ef0b-3747-9814-eb8b2ea6e064 | -4.24935 | -53.66805 | 2024-11-20 04:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 14.4 |
| d6580043-c354-329d-89db-74ac4e6fe36f | -2.62285 | -51.80296 | 2024-11-20 04:27:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 40df5628-4791-306e-ad66-e77cf60161d3 | -6.93265 | -41.1947 | 2024-11-20 04:27:00 | NOAA-21 | SANTO ANTÔNIO DE LISBOA | PIAUÍ | Brasil | 2209401 | 22 | 33 | nan | nan | nan | Caatinga | 12.5 |
| 3cec2161-aafa-3489-a494-9063aad59bb1 | -2.92461 | -53.06005 | 2024-11-20 04:27:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 40afe388-ebcf-3d0e-868e-a79715ebea43 | -3.48389 | -48.23889 | 2024-11-20 04:27:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2ce015eb-606c-30b5-bf1c-e20639b4e6cf | -8.00148 | -44.36802 | 2024-11-20 04:27:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f8fb9fd9-1350-3b0f-8adb-f9c0068e48be | -2.74829 | -51.83463 | 2024-11-20 04:27:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 07d30f4c-f7a4-336d-8a37-2686ac447747 | -3.81404 | -47.80052 | 2024-11-20 04:27:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| f5ab9bb6-3b74-342e-b9a0-44750189d0b5 | -2.86427 | -51.78786 | 2024-11-20 04:27:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3eda1304-67e0-3c55-8948-dc9e0d1b0367 | -3.24201 | -48.43356 | 2024-11-20 04:27:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 48175ef0-7c76-35b0-8440-314b50339b79 | -5.71657 | -44.81075 | 2024-11-20 04:27:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| fec8d3e4-8778-3541-bca6-fdf95c3b32aa | -3.81122 | -47.79629 | 2024-11-20 04:27:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 86a92d91-b868-3017-906b-322d4fb71e78 | -4.38613 | -47.75774 | 2024-11-20 04:27:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 199e66fd-d035-3b0e-b38c-a457e18f2b16 | -4.28508 | -50.58287 | 2024-11-20 04:27:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| eaed5317-24af-3305-9292-a8ad6f05c119 | -5.59849 | -46.16803 | 2024-11-20 04:27:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b67aa3fe-8af5-3f5d-8f73-d0632e3b05ad | -2.92416 | -48.33014 | 2024-11-20 04:27:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d7d6f3f1-8426-314b-bcc3-bcbadbb3ab61 | -3.87992 | -52.23604 | 2024-11-20 04:27:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4797d7f8-60b0-3457-b65a-fc8b6c9edd64 | -2.92512 | -48.32946 | 2024-11-20 04:27:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 621469aa-e8bd-325b-ac1d-0cc40e7417f1 | -2.94971 | -48.33327 | 2024-11-20 04:27:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 4bb71d6f-2bf0-3a75-bdb2-dcf189153bf5 | -6.53735 | -44.18436 | 2024-11-20 04:27:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6bafafdc-2988-3191-85f4-6ae652bf473c | -6.06133 | -41.93381 | 2024-11-20 04:27:00 | NOAA-21 | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 296d872b-e297-30bf-84f4-21ca7d1b7da2 | -2.9152 | -53.05845 | 2024-11-20 04:27:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| cd3183aa-17f4-3231-a996-62583fda282f | -4.5535 | -48.00915 | 2024-11-20 04:27:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f4e5bd8e-164c-373a-9c45-7a17ab88a81b | -7.91434 | -45.61615 | 2024-11-20 04:27:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6e409385-963a-3cc9-9299-9445a6caa477 | -4.34748 | -45.87975 | 2024-11-20 04:27:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| fbfbc93e-c56b-3072-94a9-9f0180971d18 | -9.25613 | -45.00346 | 2024-11-20 04:27:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d0037973-2143-344c-a01f-8fc556060eb9 | -5.69196 | -45.85017 | 2024-11-20 04:27:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e0f85dec-3674-3a79-953b-5b54482931b9 | -10.71464 | -45.02205 | 2024-11-20 04:27:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 477446ef-39ac-316b-a9aa-f93efde83006 | -6.94186 | -45.08171 | 2024-11-20 04:27:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9b777fe5-9df2-3cd3-b89a-0063897f5c62 | -2.53416 | -54.01444 | 2024-11-20 04:27:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1063905c-e3ed-3bc4-a61a-b7225e7a1a79 | -4.69504 | -42.10992 | 2024-11-20 04:27:00 | NOAA-21 | NOSSA SENHORA DE NAZARÉ | PIAUÍ | Brasil | 2206753 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| bd9ea9c4-f96d-3b1f-84a6-0f7a2189dc0a | -3.94493 | -46.71358 | 2024-11-20 04:27:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |


[Clique aqui para ver as próximas entradas](README32.md)
