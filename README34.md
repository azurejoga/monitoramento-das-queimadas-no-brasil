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

## Dados Diários - Página 34

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 649f8423-be49-34b3-86b2-3e448578fa15 | -4.99937 | -49.89458 | 2024-11-07 04:18:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 065a72a4-c945-3379-9238-fbfdf206e9a1 | -1.45874 | -52.58153 | 2024-11-07 04:18:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f48d5a42-9a1d-3812-a1f0-7ceccf23010b | -4.46223 | -46.51644 | 2024-11-07 04:18:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 2c255202-0265-35b3-ad89-4a2d75f284f3 | -6.10708 | -43.97056 | 2024-11-07 04:18:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 06818c9d-f961-3640-99f0-59d14ba72d47 | -7.75766 | -42.23986 | 2024-11-07 04:18:00 | NOAA-20 | PAES LANDIM | PIAUÍ | Brasil | 2207306 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| bc230904-f001-3b6d-9c8e-e490a0462093 | -7.16087 | -35.09686 | 2024-11-07 04:18:00 | NOAA-20 | CRUZ DO ESPÍRITO SANTO | PARAÍBA | Brasil | 2504900 | 25 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| f1e43c16-5b53-36da-a48f-df49418e188a | -4.07163 | -48.31327 | 2024-11-07 04:18:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 7ffa61cc-6969-3aca-9f44-fb3d6c55df06 | -2.04602 | -53.27652 | 2024-11-07 04:18:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| bd8fc8f6-2448-396e-94c6-bf96ad0e4a25 | -3.03057 | -53.27296 | 2024-11-07 04:18:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1be4f18f-62a4-3da3-920f-3ae4ccb55510 | -3.01244 | -53.42373 | 2024-11-07 04:18:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 26b7331b-c7ca-3c66-ad77-060b92d39273 | -2.8427 | -52.90595 | 2024-11-07 04:18:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6cca05ec-ba15-32f4-a762-48520029fea9 | -5.96233 | -45.36599 | 2024-11-07 04:18:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ef7ed40b-5033-3899-9e22-448e3a4f5f96 | -1.27597 | -54.13803 | 2024-11-07 04:18:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1f2aaba3-f80f-34f5-963f-99d39336f37c | -4.68579 | -46.38834 | 2024-11-07 04:18:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 1dc5a592-1fb0-3f90-ae8a-43cc971aa32c | -3.4341 | -50.25625 | 2024-11-07 04:18:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f1317a60-94fd-3a75-9395-b0336b4cdc4b | -2.77803 | -52.87507 | 2024-11-07 04:18:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 73073d60-a438-33df-84a9-00fdde0ad74a | -2.24049 | -53.67259 | 2024-11-07 04:18:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 82c10f60-b89d-30ea-985e-2e7731977c21 | -2.87787 | -51.46661 | 2024-11-07 04:18:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 80c4e9af-f2ca-3c08-9ae5-d09f682e9ed0 | -2.86439 | -50.32512 | 2024-11-07 04:18:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3d9379a2-a5f7-3c73-98b5-f853010bb281 | -2.9615 | -48.72919 | 2024-11-07 04:18:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 5f17e22b-cc21-3276-9ea6-3e5d310e5f5e | -7.56416 | -42.18055 | 2024-11-07 04:18:00 | NOAA-20 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| d66a773f-17ab-3a0b-97e7-84097fab1998 | -6.36571 | -45.35091 | 2024-11-07 04:18:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 474b1c49-3b6f-3df8-9319-9ec09727949e | -2.42852 | -53.6719 | 2024-11-07 04:18:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f69b0dc4-dd08-350c-8122-735bad9af2b6 | -5.14637 | -45.26147 | 2024-11-07 04:18:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7e16d3ad-c73b-391d-bcd9-d45b45f3a82d | -2.87167 | -49.54654 | 2024-11-07 04:18:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a3649f8b-a487-3e2c-a8ea-7b6893b103d4 | -3.70928 | -49.00291 | 2024-11-07 04:18:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 11.7 |
| 799bb94b-db4e-38d1-a20c-ad51c98f976d | -3.15677 | -49.52864 | 2024-11-07 04:18:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 79a7e82f-2ade-307b-96a6-2f2935867904 | -5.97894 | -45.36857 | 2024-11-07 04:18:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 10.4 |
| ce669f52-6658-358b-86b7-eb2f3d205630 | -2.85426 | -51.78104 | 2024-11-07 04:18:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 13cd4c16-0869-339a-ae35-ecb3ce68b694 | -1.14046 | -53.71729 | 2024-11-07 04:18:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| d83e3656-a7d7-3ac9-81b7-9065de8c7b44 | -3.71896 | -51.2075 | 2024-11-07 04:18:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ea318e9a-e2b6-3e3f-bdf8-d5a316ed8777 | -4.76722 | -45.74476 | 2024-11-07 04:18:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ed9f4bf0-41d3-3200-bb38-d5fabab82b29 | -1.62051 | -52.25159 | 2024-11-07 04:18:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cde7b38c-027e-3d09-bc67-18d5163f1625 | -3.00997 | -53.43821 | 2024-11-07 04:18:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 98054120-2ad8-3abd-b9e8-2241f88cbe14 | -5.4035 | -46.22287 | 2024-11-07 04:18:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1268ab1c-3979-37ed-9f4f-c6deb06a2f6d | -2.8012 | -46.64686 | 2024-11-07 04:18:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| bd12007d-fb25-383f-9660-d1abe890b581 | -4.92893 | -45.62822 | 2024-11-07 04:18:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 74a34f00-6f26-3196-85dc-d12958c73a90 | -2.79908 | -51.49649 | 2024-11-07 04:18:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 79a061c5-f354-3de9-83af-ea5313fe549e | -2.15396 | -53.65048 | 2024-11-07 04:18:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 5435f22e-b243-31e8-8220-3d551d2d937f | -5.3964 | -46.66034 | 2024-11-07 04:18:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a980d0df-2d3b-398d-b362-d69fb3399088 | -3.21506 | -50.38398 | 2024-11-07 04:18:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 6a7dbf29-8cce-358e-bd2e-3687ec3c5d13 | -4.39662 | -49.77079 | 2024-11-07 04:18:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9d586b76-d922-3de6-95c2-5b944ea09fcf | -2.41482 | -48.53623 | 2024-11-07 04:18:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c1b11730-c6f7-35da-a122-50e13c47445c | -7.36632 | -42.96019 | 2024-11-07 04:18:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 59d0b4d5-bf99-3ab6-a41e-88bf3d6e7973 | -5.33063 | -46.10736 | 2024-11-07 04:18:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| bbfd4eeb-d2e4-3158-b9d4-70c1ed172880 | -2.84219 | -52.90907 | 2024-11-07 04:18:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5e5124ad-fc02-3e98-b86d-957e2dbcc746 | -6.68848 | -46.18779 | 2024-11-07 04:18:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 230a472a-cf28-338e-b375-5673601c76a4 | -2.77748 | -52.87848 | 2024-11-07 04:18:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 84e9ca2a-e01c-3f04-8665-0cb7e3296182 | -3.22641 | -50.453 | 2024-11-07 04:18:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 966e4d79-9224-3785-9145-9a7ceba2c4c7 | -3.01121 | -53.43096 | 2024-11-07 04:18:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1a1217aa-d2c7-3bee-8559-857b1ba154b2 | -2.72425 | -51.71697 | 2024-11-07 04:18:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2320b919-00d4-333a-b50f-6055bb5291bf | -5.61606 | -41.65129 | 2024-11-07 04:18:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| b9071d22-94c6-393e-973a-ff0246c61597 | -2.82401 | -52.95329 | 2024-11-07 04:18:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0dbe0a46-38e7-381d-bb1f-1a65478d5b37 | -7.44557 | -42.89959 | 2024-11-07 04:18:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 0d905a97-ca68-301b-821a-feaf0bb5b609 | -2.8176 | -52.95908 | 2024-11-07 04:18:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fbbf8cbe-d30f-3e95-a679-cb2918d58416 | -5.158 | -45.25256 | 2024-11-07 04:18:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ee6f5af4-87fc-3bb1-8022-03492077b334 | -2.81232 | -52.95805 | 2024-11-07 04:18:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| bb74c61d-f30a-315b-8c64-c03b28cc92ac | -2.98062 | -50.30235 | 2024-11-07 04:18:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 409e09f1-166d-3134-bf31-903d8f023a5c | -3.31691 | -51.57345 | 2024-11-07 04:18:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 4ca65fe6-b9a2-37e9-ae05-0e4019868027 | -2.82344 | -52.95668 | 2024-11-07 04:18:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a8042ecc-3a5e-3d72-a439-31a0eb481f1e | -3.97267 | -48.3977 | 2024-11-07 04:18:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 3f3fbbb5-f5e4-335a-b11c-f15d373319fb | -1.344 | -54.6234 | 2024-11-07 04:18:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7f8067c8-615a-3e4f-bf98-07e2615ecd1b | -4.99461 | -49.89764 | 2024-11-07 04:18:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| c9c3d67f-e472-3dc9-9d66-edc871c40aa5 | -3.33151 | -50.08273 | 2024-11-07 04:18:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 10fb0994-0e22-3247-91e1-40574d6ba97d | -3.5772 | -49.30494 | 2024-11-07 04:18:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| fcbee922-5a79-305a-ad34-61e1c5b7c777 | -3.97651 | -48.3983 | 2024-11-07 04:18:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 584d1d20-552d-3598-ae7f-10283f88d708 | -5.61712 | -43.95467 | 2024-11-07 04:18:00 | NOAA-20 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 0415efa7-93b6-3236-a5af-b3013e0fa068 | -1.05986 | -53.66121 | 2024-11-07 04:18:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| bb1b5283-7dd5-3bdb-9b57-664c84053a62 | -7.16534 | -35.09687 | 2024-11-07 04:18:00 | NOAA-20 | CRUZ DO ESPÍRITO SANTO | PARAÍBA | Brasil | 2504900 | 25 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| e60449a8-1659-3f81-bd3d-9ce1cc1ac379 | -3.30419 | -50.14187 | 2024-11-07 04:18:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f8154592-be47-359e-a93f-02da07222908 | -5.34035 | -46.19861 | 2024-11-07 04:18:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e11ec8bc-d481-3acf-ba6e-4fe837df4c4b | -3.51202 | -50.47481 | 2024-11-07 04:18:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| c465f9c6-5ccd-3143-87bc-4ac3ca7409f7 | -3.24291 | -49.58548 | 2024-11-07 04:18:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 01fc1825-623e-30a6-8b66-cdb3bfd685f7 | -3.70158 | -51.38831 | 2024-11-07 04:18:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 1959d360-a13e-3e2f-a19c-6298519651e6 | -4.07199 | -48.31667 | 2024-11-07 04:18:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c721faee-cf58-3162-be09-55fea131d12e | -4.66891 | -46.33969 | 2024-11-07 04:18:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8a1191c8-1774-3a29-bb3a-b932cae3aebc | -2.85074 | -48.66858 | 2024-11-07 04:18:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 714ab898-f6f0-3d90-bb2b-6ed8085a7f99 | -6.45831 | -44.67787 | 2024-11-07 04:18:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 266bb6f6-864e-345f-99c4-c4ef7f230480 | -2.24565 | -47.66515 | 2024-11-07 04:18:00 | NOAA-20 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 29038df3-7468-31d2-8c62-0addb111b464 | -7.37831 | -40.36061 | 2024-11-07 04:18:00 | NOAA-20 | ARARIPINA | PERNAMBUCO | Brasil | 2601102 | 26 | 33 | nan | nan | nan | Caatinga | 0.7 |
| a47529db-d1cb-3f7a-b12b-7013a75468c5 | -5.70331 | -45.94763 | 2024-11-07 04:18:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 8d4572b3-0201-3fd8-9880-c5c9c50d1e2b | -3.00854 | -53.44221 | 2024-11-07 04:18:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| ae38c1eb-a657-3b80-89a0-e9fd464eb078 | -2.67198 | -51.821 | 2024-11-07 04:18:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 72418271-d241-3b7d-a39b-05d42f15bd27 | -2.92335 | -49.35608 | 2024-11-07 04:18:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 30d0fb44-1ff8-30ad-a8f0-22cbeb4232d0 | -4.75836 | -45.69218 | 2024-11-07 04:18:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8e472a64-3719-3a2f-9099-eee5885670e2 | -3.5188 | -50.34753 | 2024-11-07 04:18:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0fe2fdbc-83d3-3199-b44e-cd890f3c749f | -3.00689 | -53.24836 | 2024-11-07 04:18:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f3410291-b77a-3fe3-8fb1-76c624eb509c | -6.45555 | -44.6739 | 2024-11-07 04:18:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 1bca21d9-f94c-39f6-bce7-44bdfed30f56 | -3.09931 | -53.71266 | 2024-11-07 04:18:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| cdae3ebc-826d-351b-bce1-c08727f27775 | -1.13479 | -53.71597 | 2024-11-07 04:18:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f235db19-139f-3d19-9cae-a2f4ac8f24a4 | -7.67552 | -42.76659 | 2024-11-07 04:18:00 | NOAA-20 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 0.3 |
| 787019e8-67c8-32d0-b05f-3090980ec51c | -2.59443 | -47.01087 | 2024-11-07 04:18:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 89b76f14-a717-3cfb-a21f-c8386c716789 | -8.19071 | -42.8383 | 2024-11-07 04:18:00 | NOAA-20 | BREJO DO PIAUÍ | PIAUÍ | Brasil | 2201988 | 22 | 33 | nan | nan | nan | Caatinga | 4.3 |
| d1c98037-c353-3d32-beb7-3c79b7ec9bcc | -1.27656 | -54.13438 | 2024-11-07 04:18:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e9ee4387-118a-37ff-a0f0-52a231ee2c8a | -3.15786 | -50.21039 | 2024-11-07 04:18:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c97fc0a5-21e1-3e7e-b562-8a32db35bb28 | -3.9008 | -50.08985 | 2024-11-07 04:18:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 8993636a-c71e-3a9f-9e9f-611c905f0416 | -1.21784 | -54.54173 | 2024-11-07 04:18:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f0dc72b3-5b08-3c66-a687-c58e1cf949de | -3.7104 | -48.99592 | 2024-11-07 04:18:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 13.4 |
| 8345bcbc-363f-3f18-ab49-436e61e43709 | -4.34606 | -48.62415 | 2024-11-07 04:18:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 030c1d41-dca1-3529-82d3-2c39048bc93d | -2.80218 | -49.78933 | 2024-11-07 04:18:00 | NOAA-20 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |


[Clique aqui para ver as próximas entradas](README35.md)
