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

## Dados Diários - Página 88

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 03f887eb-d8ef-3a57-954f-7d41136313be | -1.3666 | -53.8362 | 2024-11-24 13:40:00 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 68.0 |
| bbbe6c30-fc5b-3957-9004-39d848ca2a18 | -3.8472 | -49.8216 | 2024-11-24 13:40:00 | GOES-16 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 68.1 |
| 8bd3ba2f-41df-387d-a56c-21ef09e4c946 | -1.6419 | -53.8731 | 2024-11-24 13:40:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 100.3 |
| 47eb06fe-aeb4-36b1-bd10-715dd731d5a7 | -3.8928 | -41.8568 | 2024-11-24 13:40:00 | GOES-16 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 93.7 |
| 94f9f6ab-c399-3df2-9f9c-2b1581d5668a | -3.8473 | -49.8005 | 2024-11-24 13:40:00 | GOES-16 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 152.0 |
| dfd30df9-20ec-3f71-b5c9-80d2b5d12b71 | -3.8417 | -44.0594 | 2024-11-24 13:40:00 | GOES-16 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 90.3 |
| c489b005-7f50-35d5-ae2d-cc094643bf4c | -1.479 | -52.5178 | 2024-11-24 13:50:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 86.8 |
| b44e8c61-d57b-38d4-b3c9-34c1307ac06e | -0.5608 | -51.7061 | 2024-11-24 13:50:00 | GOES-16 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 62.9 |
| 6e0c5f6a-fee1-324b-bad7-86ce5600bc07 | -0.3771 | -51.4387 | 2024-11-24 13:50:00 | GOES-16 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 62.5 |
| 7d41b3da-ad2f-3dc9-91f9-caa24b4b668a | -3.8741 | -41.8579 | 2024-11-24 13:50:00 | GOES-16 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 77.1 |
| 59d6dbec-9f86-3dff-a1a7-071700b576fe | -0.3587 | -51.4387 | 2024-11-24 13:50:00 | GOES-16 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 88.2 |
| fb0b4fbe-ae51-35dc-82e8-c4c1ad928ed0 | -3.8472 | -49.8216 | 2024-11-24 13:50:00 | GOES-16 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 74.4 |
| 32b6681f-5fff-399e-bfde-6e9758beddce | -3.8473 | -49.8005 | 2024-11-24 13:50:00 | GOES-16 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 152.3 |
| 4412c693-dcb9-3469-a1ff-713e264f8fd1 | -0.3587 | -51.4387 | 2024-11-24 14:00:00 | GOES-16 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 108.2 |
| 8d3fc6f6-f9b9-3eed-9de2-ba2ddf4e3024 | -0.3587 | -51.4594 | 2024-11-24 14:00:00 | GOES-16 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 63.8 |
| e91a82e8-fb66-3dc1-981e-644b996164ca | -3.8928 | -41.8568 | 2024-11-24 14:00:00 | GOES-16 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 89.2 |
| 02b09ed1-9cd1-35cc-a124-e017ac6f97c0 | -2.2114 | -53.6828 | 2024-11-24 14:00:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 59.4 |
| ebbc2ef5-5f1f-3075-a019-8aa4fcede18f | -1.9551 | -53.3237 | 2024-11-24 14:00:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 85.6 |
| 741168e6-9c05-3076-bc85-5573d2b5ef0d | -2.2114 | -53.6626 | 2024-11-24 14:00:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 60.8 |
| ca783da4-ffbc-3ee6-a68b-b01c041a21b0 | -3.7987 | -41.9335 | 2024-11-24 14:10:00 | GOES-16 | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 76.5 |
| 6f984c26-54e3-3b5f-ad0a-41cb755c1ccb | -1.9551 | -53.3237 | 2024-11-24 14:10:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 77.0 |
| aa5d483b-3c6e-369a-aff3-948358d6cf57 | -0.5608 | -51.7061 | 2024-11-24 14:10:00 | GOES-16 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 83.5 |
| c6627ba6-a3cf-3ebb-964a-39da6882ac30 | -0.3587 | -51.4387 | 2024-11-24 14:10:00 | GOES-16 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 67.6 |
| a714be3f-6ec0-353e-9d5e-2beb6958df0a | -0.5608 | -51.7267 | 2024-11-24 14:10:00 | GOES-16 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 70.4 |
| 5fda6aaf-844f-383e-9829-4d1398ba5981 | 1.8764 | -55.9199 | 2024-11-24 14:10:00 | GOES-16 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 81.0 |
| 79803112-b9d8-30d1-ac0d-a506378ff6bd | -0.8215 | -48.6395 | 2024-11-24 14:10:00 | GOES-16 | SALVATERRA | PARÁ | Brasil | 1506302 | 15 | 33 | nan | nan | nan | Amazônia | 66.4 |
| 7faecc3b-ce09-3a75-b9f2-9c52f580a712 | -2.2114 | -53.6626 | 2024-11-24 14:10:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 61.7 |
| 66d7042f-a255-33cc-9b09-69d220819a99 | -3.447 | -44.6721 | 2024-11-24 14:20:00 | GOES-16 | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 71.0 |
| 4f0cae80-0ac1-3162-8351-a6359d296422 | -1.9551 | -53.3237 | 2024-11-24 14:20:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 68.0 |
| 3eab9e4d-8adf-3131-91d2-fadb8827d6e1 | -2.2114 | -53.6626 | 2024-11-24 14:20:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 56.8 |
| 077a1513-16b6-3eec-8650-c44048209165 | -1.7891 | -53.6495 | 2024-11-24 14:20:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 61.2 |
| 1979ea89-2f81-3582-8dc9-f8e4a5fd3749 | -0.5608 | -51.7061 | 2024-11-24 14:20:00 | GOES-16 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 82.3 |
| de515fcf-c3dc-370d-8d46-646d25894730 | -1.3667 | -53.8161 | 2024-11-24 14:30:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 69.9 |
| 3133c4c3-a0f5-373c-a7c3-c5c899838d70 | -0.2851 | -51.5009 | 2024-11-24 14:30:00 | GOES-16 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 120.1 |
| eae12c05-d7b9-3078-890e-a57976f31bd1 | -2.2114 | -53.6626 | 2024-11-24 14:30:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 57.3 |
| f3c6a0ee-7f49-3c1b-923d-a56d51b45daf | -2.1931 | -53.6428 | 2024-11-24 14:30:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 56.9 |
| 8a1dbc9a-6ee4-371f-8bdc-afce31283e8d | -1.9551 | -53.3237 | 2024-11-24 14:30:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 74.4 |
| f3d03347-fd9c-3765-b7d8-c44c8b5395c8 | -0.3587 | -51.4387 | 2024-11-24 14:30:00 | GOES-16 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 76.6 |


