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

## Dados Diários - Página 25

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1e396f7c-9f6a-3580-b211-8a9c2e39b17d | -7.72909 | -42.38195 | 2025-10-06 04:25:00 | NOAA-21 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 6554214a-83d8-3a9f-93d3-08deeab2b581 | -5.83241 | -45.82965 | 2025-10-06 04:25:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 53735f4c-4280-3871-bc83-b98cc960647c | -8.87811 | -47.60992 | 2025-10-06 04:25:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 27f626a9-0400-3ba6-8416-c6bab26337a7 | -5.21691 | -43.67857 | 2025-10-06 04:25:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b55de058-421d-306d-803a-3299113aef15 | -6.15182 | -48.10159 | 2025-10-06 04:25:00 | NOAA-21 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 6a3569a5-598a-3d1a-bcf2-e3eb90e48a8f | -3.66268 | -52.12791 | 2025-10-06 04:25:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7314d6a1-903e-3c36-a731-1050e889aa28 | -2.29753 | -47.99222 | 2025-10-06 04:25:00 | NOAA-21 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 797105ea-c431-325e-96a6-19f24bffbda6 | -4.57785 | -44.94826 | 2025-10-06 04:25:00 | NOAA-21 | LAGO DOS RODRIGUES | MARANHÃO | Brasil | 2105948 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 043ace27-ebae-346c-abb0-e7067bdec1b6 | -4.05588 | -38.29704 | 2025-10-06 04:25:00 | NOAA-21 | PINDORETAMA | CEARÁ | Brasil | 2310852 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 5898652b-cab2-3722-8c33-f26513a57ba7 | -7.46427 | -43.07236 | 2025-10-06 04:25:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 929555a5-d5d5-36f3-83f4-07f645558f25 | -6.70268 | -42.14964 | 2025-10-06 04:25:00 | NOAA-21 | TANQUE DO PIAUÍ | PIAUÍ | Brasil | 2210979 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| e1af98e5-95c9-3305-952e-763cdb5229e5 | -5.09384 | -42.62809 | 2025-10-06 04:25:00 | NOAA-21 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 4842043d-d923-349d-93ea-6a9925329a8c | -6.10841 | -43.41988 | 2025-10-06 04:25:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 1038bd09-a350-3531-a793-d57a149fcf5b | -5.46809 | -43.15133 | 2025-10-06 04:25:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 11e3c857-24e6-391e-b01d-81da83c5e2c3 | -8.47214 | -47.22644 | 2025-10-06 04:25:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b62e55e4-6775-3315-8bbf-1ec0ba4eaa31 | -8.54483 | -46.30769 | 2025-10-06 04:25:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| b0f06b13-f64a-3057-a22d-4c386a5a919f | -5.97778 | -45.87706 | 2025-10-06 04:25:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 652dd7cc-204d-3bcc-9fef-ffb4732a245a | -6.82521 | -46.00743 | 2025-10-06 04:25:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d50b9e33-b596-30f9-9f07-ad7689a25575 | -6.57528 | -49.86312 | 2025-10-06 04:25:00 | NOAA-21 | CANAÃ DOS CARAJÁS | PARÁ | Brasil | 1502152 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 5a808a34-32f0-3214-a78b-97883271811e | -7.42423 | -46.53373 | 2025-10-06 04:25:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f95340f2-222a-3b79-ba67-8b990a8bd99a | -8.7229 | -41.68546 | 2025-10-06 04:25:00 | NOAA-21 | LAGOA DO BARRO DO PIAUÍ | PIAUÍ | Brasil | 2205565 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 734d801c-ce00-3f73-8c5b-ce4d392639ab | -7.79072 | -42.5993 | 2025-10-06 04:25:00 | NOAA-21 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 3fb45b81-7f5c-3223-82e5-ea2d1867dc02 | -5.70527 | -44.84755 | 2025-10-06 04:25:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 4eac4379-aa39-33b8-b3ad-0fa973c8b8dc | -4.32431 | -46.80759 | 2025-10-06 04:25:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e97617d1-7de0-3656-9201-abec77e7d55c | -8.18125 | -44.24928 | 2025-10-06 04:25:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8492b2a3-4482-3378-b147-7c86eaa26017 | -7.70666 | -46.24953 | 2025-10-06 04:25:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5bfca933-7cb4-38a6-8da8-eb21380f917d | -6.66644 | -40.9116 | 2025-10-06 04:25:00 | NOAA-21 | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 63766590-5b6e-334d-9cae-4b12f9cd1c5b | -7.02692 | -42.79016 | 2025-10-06 04:25:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 12.1 |
| 56e8ea6c-e1f1-3edd-9c5a-f1389d67ac86 | -6.638 | -41.98669 | 2025-10-06 04:25:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| f1bc1ae8-db3a-3ca1-b4d0-b361e23db691 | -5.66522 | -48.92318 | 2025-10-06 04:25:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cd949961-9953-3208-bd7c-fba378f8c528 | -3.68095 | -55.57727 | 2025-10-06 04:25:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8c4beb74-fca4-3eed-ba86-2fb85dc0db47 | -8.55044 | -47.67931 | 2025-10-06 04:25:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 44e3a6e0-e5b5-3ea8-9491-8e75cbc25383 | -3.59108 | -51.44146 | 2025-10-06 04:25:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 62ccec1f-e281-36a0-96e4-7546fa731ad6 | -6.28693 | -42.93487 | 2025-10-06 04:25:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| ec7273b6-03e9-3b82-87d6-da4928af4a22 | -8.17021 | -44.2516 | 2025-10-06 04:25:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b33e5b53-d4c6-3d4c-8c1d-55ccda7c3bc8 | -5.19747 | -45.07678 | 2025-10-06 04:25:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a4a29447-51cb-3d54-a3d3-a85ef2c7da1f | -3.63394 | -51.44418 | 2025-10-06 04:25:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0ba33b5f-664b-39b7-92f7-1f20e85c56b9 | -4.76105 | -46.60544 | 2025-10-06 04:25:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3b0d55b8-b1a0-3f55-8014-2d423ea54db3 | -7.23866 | -47.64217 | 2025-10-06 04:25:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e3681de8-6c58-3ea7-822a-2e04530cd491 | -7.80605 | -42.57325 | 2025-10-06 04:25:00 | NOAA-21 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 96ae1bd2-19b2-37cd-86c1-d1c5b6e2d1a4 | -3.826 | -51.30836 | 2025-10-06 04:25:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| dbf6db9d-9a0c-3963-9863-5f0729c382ad | -6.73984 | -44.03816 | 2025-10-06 04:25:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 415889db-1c67-3db1-84de-28acf5e7efe7 | -5.64877 | -50.31804 | 2025-10-06 04:25:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7b4e963a-4a69-3b2d-bbea-0ed3ba4d2942 | -8.61461 | -46.27237 | 2025-10-06 04:25:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 56d3fe48-46a5-352f-8bff-424f796fd0cf | -9.20192 | -46.91688 | 2025-10-06 04:25:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 19519947-d0c8-352c-9ffe-80ab68b794bf | -6.44172 | -44.17813 | 2025-10-06 04:25:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| dc90a6c9-ccbd-38ff-bd4d-e146297c509e | -7.80159 | -42.5774 | 2025-10-06 04:25:00 | NOAA-21 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| f4ef2c60-effe-335d-8ca4-40a3d965176e | -7.00341 | -47.47408 | 2025-10-06 04:25:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 66cd5c6b-be90-3d92-98a2-02cf160240f5 | -6.77753 | -41.58253 | 2025-10-06 04:25:00 | NOAA-21 | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 03f3b3f9-a81a-3166-810c-f3c5bc821399 | -9.3214 | -46.01367 | 2025-10-06 04:25:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 68869f80-b678-3a4e-9dc8-bb02ecd596b8 | -5.15792 | -46.22321 | 2025-10-06 04:25:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f8d26ace-9f92-3f93-90a7-8c7a8b6880a0 | -5.5047 | -42.23543 | 2025-10-06 04:25:00 | NOAA-21 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 155ef73b-e37b-361e-a1ed-63ed21c1d785 | -4.65114 | -43.19011 | 2025-10-06 04:25:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f3941ef7-c343-3508-a5a3-40be93e6d1d1 | -4.86385 | -45.25311 | 2025-10-06 04:25:00 | NOAA-21 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a37173f5-5c9f-3fc0-be4d-98af5e9ede7c | -3.81463 | -51.07624 | 2025-10-06 04:25:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5d9bd0ce-e9a6-351f-a489-2ad35dbeaf6e | -8.6422 | -46.31582 | 2025-10-06 04:25:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2acff87c-04d3-328a-b65e-2adc0c15df43 | -6.72878 | -42.15801 | 2025-10-06 04:25:00 | NOAA-21 | TANQUE DO PIAUÍ | PIAUÍ | Brasil | 2210979 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 5112ea07-00b4-3137-a236-c5f9b7a3b9cc | -7.68425 | -42.58554 | 2025-10-06 04:25:00 | NOAA-21 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 5.8 |
| a6374e04-5176-35bf-b7a4-54dc940d6132 | -3.81525 | -51.07238 | 2025-10-06 04:25:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1fb8581c-ca1b-39e0-8db3-929a6f742182 | -8.86966 | -46.79634 | 2025-10-06 04:25:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 450e1ef8-465e-38de-abc3-6db565de6f45 | -6.05902 | -42.55352 | 2025-10-06 04:25:00 | NOAA-21 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 650f924d-5f35-3b32-8bae-3d29cf8d4d51 | -7.71871 | -42.39988 | 2025-10-06 04:25:00 | NOAA-21 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 34345383-a395-3cfe-8944-67b42194d2f3 | -8.19501 | -44.13529 | 2025-10-06 04:25:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1242a249-a4fb-3bcb-994f-1971cfd62353 | -4.26619 | -48.55086 | 2025-10-06 04:25:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ffafd832-5518-3035-9234-b8c07744e20e | -8.87755 | -47.61342 | 2025-10-06 04:25:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| de925bff-b854-389c-8e26-c701dd4ff056 | -5.13215 | -46.23682 | 2025-10-06 04:25:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 26b0dc00-f31d-3e65-9a17-c62df8f9c767 | -6.64463 | -42.77189 | 2025-10-06 04:25:00 | NOAA-21 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 5.8 |
| 24084176-a841-3df7-96d9-3eae6f0faf7e | -6.39364 | -47.71187 | 2025-10-06 04:25:00 | NOAA-21 | NAZARÉ | TOCANTINS | Brasil | 1714302 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 94c5ccce-f50c-3393-8f91-f7127fe5f92a | -5.28021 | -42.93219 | 2025-10-06 04:25:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 4d8c60a7-d858-39a2-a1f1-08bbea19ecd4 | -6.6701 | -42.77351 | 2025-10-06 04:25:00 | NOAA-21 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| a2784bea-7929-349e-a1a0-b09c967becca | -8.61569 | -46.26543 | 2025-10-06 04:25:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| ad3cdf2f-1b51-36f6-b48b-132a6df29111 | -8.61408 | -46.27584 | 2025-10-06 04:25:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| b3ca6a0d-7499-3a46-8100-5ee19c4708e2 | -6.28034 | -42.92925 | 2025-10-06 04:25:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 2242a8db-0065-32fe-97a3-ae8f311c3301 | -5.15462 | -46.2227 | 2025-10-06 04:25:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4469b41e-a736-3c16-9c4b-6b1a65f6bde3 | -7.71421 | -42.40401 | 2025-10-06 04:25:00 | NOAA-21 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| fecf4083-31a1-3274-b588-ee93b9c09986 | -8.62688 | -46.32411 | 2025-10-06 04:25:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 3b634b6e-39c2-32a2-ae6b-558a6c88863f | -5.3338 | -43.36893 | 2025-10-06 04:25:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 2e1a3059-b335-3ab0-94e1-a75c5532fc80 | -5.57053 | -45.58701 | 2025-10-06 04:25:00 | NOAA-21 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3dc66a9f-abae-37f7-af9d-c4be090c6b91 | -8.63072 | -46.32116 | 2025-10-06 04:25:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 4c52af4e-9717-3d0e-ac38-bc5bd3dfd6de | -7.74457 | -42.54251 | 2025-10-06 04:25:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 93460296-508f-3820-a2e6-e3d1c7e42269 | -6.69432 | -42.15338 | 2025-10-06 04:25:00 | NOAA-21 | TANQUE DO PIAUÍ | PIAUÍ | Brasil | 2210979 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| a3650cc7-1b08-3827-8c45-31a21f79604f | -4.61771 | -41.42592 | 2025-10-06 04:25:00 | NOAA-21 | MILTON BRANDÃO | PIAUÍ | Brasil | 2206357 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 07e365d2-f9a1-30fa-8548-73fb31d59c71 | -7.4774 | -43.87483 | 2025-10-06 04:25:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 442ace20-c3f6-3db4-9fb9-3922dd9f7b54 | -8.17139 | -44.2438 | 2025-10-06 04:25:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c30d7d3f-07cb-3566-a803-87f71ddcab99 | -5.34447 | -44.30617 | 2025-10-06 04:25:00 | NOAA-21 | GRAÇA ARANHA | MARANHÃO | Brasil | 2104701 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| ab149701-0b7c-35ad-83e7-05d2eaaa9c0c | -7.11232 | -45.0966 | 2025-10-06 04:25:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a0b524a4-0b87-3398-b455-02481de2e81a | -7.52269 | -45.41511 | 2025-10-06 04:25:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| fc4c3c21-41d4-3fd6-806c-d0b537ba02c8 | -6.24975 | -44.26419 | 2025-10-06 04:25:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 129ba8e3-b956-35b4-8d2c-8a9bb76cece5 | -8.65976 | -40.59896 | 2025-10-06 04:25:00 | NOAA-21 | DORMENTES | PERNAMBUCO | Brasil | 2605152 | 26 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 7a6dec7b-f807-3665-a670-eed008a95886 | -8.61792 | -46.27289 | 2025-10-06 04:25:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| c9f82ce0-ebb1-3473-abd0-5f3464e2cf5e | -6.30699 | -44.46598 | 2025-10-06 04:25:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 825dff5e-9da3-3c68-94a0-d5c40df62016 | -6.40674 | -43.81374 | 2025-10-06 04:25:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e8d19823-dc30-30f4-8287-3eff8155969f | -7.72262 | -46.25559 | 2025-10-06 04:25:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| b3ea38f2-71f2-3333-a73f-86ec3567096d | -7.55476 | -44.93478 | 2025-10-06 04:25:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| cda334c2-4640-3cc2-9936-af0ecbfb923b | -7.77878 | -44.11789 | 2025-10-06 04:25:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d6122493-ab4d-347c-80fe-5dc142ec8ddd | -2.14652 | -47.50662 | 2025-10-06 04:25:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3e49d323-c570-33bf-83fc-a08491a8c9fa | -5.60877 | -51.79789 | 2025-10-06 04:25:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 83822eff-3f76-3c54-ace9-59f71c2ea012 | -7.72208 | -46.25905 | 2025-10-06 04:25:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| e78d8dca-ffaa-33d5-808f-8cee2570dcb5 | -3.82538 | -51.31212 | 2025-10-06 04:25:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 61f020ee-18b2-3a4f-aeb1-d0b3733d25af | -8.61293 | -46.26144 | 2025-10-06 04:25:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |


[Clique aqui para ver as próximas entradas](README26.md)
