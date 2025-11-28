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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 68bc1729-3169-381b-9452-a9b6033dd302 | -5.5582 | -46.5102 | 2025-11-28 01:40:00 | GOES-19 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 49.2 |
| 2d636203-ff0d-3f76-b64b-3621d057c28a | -3.7694 | -46.96 | 2025-11-28 01:40:00 | GOES-19 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 55.8 |
| 47a04a52-34c7-3940-a9e8-ed5eeac4be51 | -1.8245 | -54.332 | 2025-11-28 01:40:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 143.2 |
| 23dce822-a6e9-392a-9cd8-6f894dcef31a | -9.4 | -40.3722 | 2025-11-28 01:40:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 235.0 |
| 1cc839f5-f95a-3f2f-8e7a-f904411d227b | -2.7006 | -45.2214 | 2025-11-28 01:40:00 | GOES-19 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 80.6 |
| 94f9a372-8bd0-31c9-939a-62dd17f48b04 | -2.7191 | -45.2208 | 2025-11-28 01:50:00 | GOES-19 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 143.3 |
| 1574a2ca-761e-3301-8304-8f1ad0d24cde | -5.5398 | -46.4893 | 2025-11-28 01:50:00 | GOES-19 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 50.0 |
| 5b32c073-2774-3450-90b3-97176b2544e2 | -3.751 | -46.9388 | 2025-11-28 01:50:00 | GOES-19 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 50.3 |
| 989db325-c567-3e0e-bf9a-7f9785034486 | -3.7694 | -46.96 | 2025-11-28 01:50:00 | GOES-19 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 83.2 |
| 400902ba-0a53-3f22-b7fe-7edf53021b17 | -2.6181 | -47.3521 | 2025-11-28 01:50:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 81.7 |
| ba24aa57-dd2d-34f2-86ea-dc9b92b0f1ac | -5.0631 | -40.8171 | 2025-11-28 01:50:00 | GOES-19 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 82.4 |
| 5fb75b41-5193-39ef-ba2d-48cea1bf296d | -1.8245 | -54.332 | 2025-11-28 01:50:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 55.6 |
| 94f01478-84ae-3313-8014-38f46e617d3c | -3.7508 | -46.9608 | 2025-11-28 01:50:00 | GOES-19 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 102.1 |
| 6e3db5c2-436b-3395-9813-0f3bc913d420 | -5.5396 | -46.5115 | 2025-11-28 01:50:00 | GOES-19 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 63.2 |
| e48abfc7-57f9-3593-84a5-97b19e255a3a | -9.4 | -40.3722 | 2025-11-28 01:50:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 237.4 |
| d26f8ce7-c5c0-327f-a13a-6fd640829a28 | -9.3809 | -40.375 | 2025-11-28 01:50:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 264.3 |
| 1bdc9b6c-2f65-30ca-809c-39ae459ed00e | -8.1633 | -43.2055 | 2025-11-28 01:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 70.4 |
| fb1d45a1-00f5-333b-bea2-52000c680310 | -1.8428 | -54.3317 | 2025-11-28 01:50:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 28.9 |
| 99c5dee4-d044-33bc-b982-4cf054eac8c0 | -9.3813 | -40.3501 | 2025-11-28 01:50:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 153.4 |
| c39201fb-aa41-3f21-83e6-35d50315eec6 | -9.4004 | -40.3474 | 2025-11-28 01:50:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 133.4 |
| 1b3f8922-57e2-3ca8-97bd-5aeace89018e | -1.8245 | -54.312 | 2025-11-28 01:50:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 31.2 |
| d3163366-5af9-3f8e-a6b3-cfffd7c65273 | -9.4 | -40.3722 | 2025-11-28 02:00:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 176.6 |
| af1b7cab-5cf9-32e5-8ff7-6f1581dbf4f6 | -2.7191 | -45.2208 | 2025-11-28 02:00:00 | GOES-19 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 105.6 |
| 083bd107-229d-3465-a44c-159f214370fe | -2.6181 | -47.3521 | 2025-11-28 02:00:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 65.1 |
| 38e76a11-c1d3-31a9-b78e-a7467fe77b1d | -5.5396 | -46.5115 | 2025-11-28 02:00:00 | GOES-19 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 50.2 |
| e1eaa720-eb14-3a49-974d-c30ed581cc75 | -1.8245 | -54.332 | 2025-11-28 02:00:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 33.4 |
| a23c5878-9ff9-3804-8a73-4a91b857cb2c | -2.7006 | -45.2214 | 2025-11-28 02:00:00 | GOES-19 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 52.1 |
| 73d8bc5b-d0d5-3609-ad81-83235b44595d | -9.4004 | -40.3474 | 2025-11-28 02:00:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 97.2 |
| 0d8a642e-d762-3dd1-b305-fbc256bbeb0c | -9.3813 | -40.3501 | 2025-11-28 02:00:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 151.1 |
| 95b356cd-ea16-3478-9213-2b248c3dddee | -9.3809 | -40.375 | 2025-11-28 02:00:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 312.7 |
| 0050e6ec-c045-3f7b-9a36-d8f5e3d70934 | -3.7694 | -46.96 | 2025-11-28 02:10:00 | GOES-19 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 48.4 |
| 467ef627-d418-3add-bf21-3e16279f18ac | -5.5396 | -46.5115 | 2025-11-28 02:10:00 | GOES-19 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 50.8 |
| e0f02224-9872-381a-b09a-f399e4d03362 | -2.6181 | -47.3521 | 2025-11-28 02:10:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 64.1 |
| d010305f-c525-391d-ba06-9d721d654826 | -19.9973 | -49.9861 | 2025-11-28 02:10:00 | GOES-19 | CARDOSO | SÃO PAULO | Brasil | 3510708 | 35 | 33 | nan | nan | nan | Mata Atlântica | 61.8 |
| 90cf92b1-0aca-302a-884c-88feb8b2b74b | -9.3813 | -40.3501 | 2025-11-28 02:10:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 139.2 |
| ab54600b-165e-36eb-b32a-52ffe0c870d8 | -9.4004 | -40.3474 | 2025-11-28 02:10:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 104.4 |
| b37467e8-87f1-3906-9b3c-85c768ea215f | -2.7191 | -45.2208 | 2025-11-28 02:10:00 | GOES-19 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 84.4 |
| 20f55f75-bd72-3696-8011-6f689478f862 | -9.4 | -40.3722 | 2025-11-28 02:10:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 187.3 |
| 9fa124f7-c343-3477-9fcb-0b73d46c4f7d | -9.3809 | -40.375 | 2025-11-28 02:10:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 271.3 |
| 0f5026dc-a9f3-3691-82b6-f147df56bc60 | -9.3805 | -40.3998 | 2025-11-28 02:10:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 83.4 |
| 174603f4-f0e2-33e7-b7b9-afda5eeae8d0 | -3.8618 | -47.0438 | 2025-11-28 02:20:00 | GOES-19 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 97.2 |
| 7c1dfcd0-483d-3fef-8180-62c8dae27dda | -2.7191 | -45.2208 | 2025-11-28 02:20:00 | GOES-19 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 82.8 |
| f0df1385-346f-36bc-bf0b-e9080e0673e5 | -6.7199 | -40.8188 | 2025-11-28 02:20:00 | GOES-19 | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 76.7 |
| 400202c9-f152-370c-9d74-d1e33c51d129 | -9.4004 | -40.3474 | 2025-11-28 02:20:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 88.8 |
| 5e7405b5-1450-3bab-a393-355344c31d31 | -3.7694 | -46.96 | 2025-11-28 02:20:00 | GOES-19 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 73.5 |
| 27cd9116-bc79-3a4f-8222-29284240b4a9 | -9.3809 | -40.375 | 2025-11-28 02:20:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 207.3 |
| 5215ddb9-d8c3-386c-8dea-f52a2f7de380 | -3.8431 | -47.0666 | 2025-11-28 02:20:00 | GOES-19 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 70.7 |
| 00e1d6e2-085c-3317-83f7-e0d73a0e818d | -9.3813 | -40.3501 | 2025-11-28 02:20:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 115.0 |
| 41c0bba5-beeb-3cc9-b95b-7f4099c0f5c0 | -2.7025 | -49.5634 | 2025-11-28 02:20:00 | GOES-19 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 53.6 |
| 0073fa73-b6f6-39d5-9200-a9cf06bb5d20 | -3.8432 | -47.0446 | 2025-11-28 02:20:00 | GOES-19 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 60.9 |
| 8a9f5525-f165-38f9-bdbb-fe469e759439 | -9.4 | -40.3722 | 2025-11-28 02:20:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 147.8 |
| 52825d2f-4fb4-3031-a7ba-ce751bf539fb | -2.6181 | -47.3521 | 2025-11-28 02:20:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 52.8 |
| 5d4333ec-2495-3189-bed9-08d63521d9d4 | -3.7508 | -46.9608 | 2025-11-28 02:20:00 | GOES-19 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 54.4 |
| 3ac0ec34-5d31-34ef-b017-253f1e51b8df | -3.8617 | -47.0657 | 2025-11-28 02:20:00 | GOES-19 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 118.8 |
| 174e47ac-2a4e-35d2-9b5f-0fafecf70162 | -9.3813 | -40.3501 | 2025-11-28 02:30:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 104.5 |
| 9b292d52-5778-34f7-8644-758ce6bb4886 | -3.7694 | -46.96 | 2025-11-28 02:30:00 | GOES-19 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 74.6 |
| daab9229-6485-375f-a4ac-23787db2acf8 | -2.7025 | -49.5634 | 2025-11-28 02:30:00 | GOES-19 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 54.9 |
| 26973526-5514-3b56-8bb1-a79ea004b936 | -3.8618 | -47.0438 | 2025-11-28 02:30:00 | GOES-19 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 54.3 |
| 24dd2e65-f786-3fd1-8a2b-f1cfc5bd488b | -2.7191 | -45.2208 | 2025-11-28 02:30:00 | GOES-19 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 70.0 |
| f4170c71-1ea1-306f-8516-0ea7b38e5596 | -3.7508 | -46.9608 | 2025-11-28 02:30:00 | GOES-19 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 69.0 |
| 36d272b3-6661-3b6d-98ff-95d5e12dc1ef | -9.3809 | -40.375 | 2025-11-28 02:30:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 195.0 |
| 6d0db48e-866f-3364-8c02-65b698f193b5 | -3.8617 | -47.0657 | 2025-11-28 02:30:00 | GOES-19 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 79.1 |
| 004f8c65-f651-3301-b401-a41a66b71b6e | -9.4004 | -40.3474 | 2025-11-28 02:30:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 82.7 |
| 50057213-3f6b-3eb9-8131-beea21d62493 | -9.4 | -40.3722 | 2025-11-28 02:30:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 145.8 |
| 7831e1a1-e4c9-3726-b7bd-60980f8fb199 | -6.7199 | -40.8188 | 2025-11-28 02:30:00 | GOES-19 | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 73.4 |
| 6f83b363-e200-35af-b104-98ce29e9fd2e | -3.8432 | -47.0446 | 2025-11-28 02:30:00 | GOES-19 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 46.5 |
| fa99ec24-38c5-33ba-8123-a545a0da1b47 | -3.8431 | -47.0666 | 2025-11-28 02:30:00 | GOES-19 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 62.8 |
| 23b36009-85d6-374d-83f2-3af897c639bf | -9.3809 | -40.375 | 2025-11-28 02:40:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 153.3 |
| 35e37ee2-d11e-33a3-af53-2af4f00c202e | -19.9973 | -49.9861 | 2025-11-28 02:40:00 | GOES-19 | CARDOSO | SÃO PAULO | Brasil | 3510708 | 35 | 33 | nan | nan | nan | Mata Atlântica | 62.2 |
| 8875f859-ce8b-3818-818e-7b8e3873a81e | -9.4 | -40.3722 | 2025-11-28 02:40:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 141.1 |
| 70b93250-6c0a-33ff-b354-9b3b6326659e | -2.7191 | -45.2208 | 2025-11-28 02:40:00 | GOES-19 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 65.4 |
| 9218d0c8-6322-39f9-bc84-315715229eba | -9.3813 | -40.3501 | 2025-11-28 02:40:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 82.2 |
| a342a507-e36a-3b2e-b0b3-412a2a268a26 | -3.7508 | -46.9608 | 2025-11-28 02:50:00 | GOES-19 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 69.0 |
| 92c689b7-3eb9-3616-ae29-aac476cfedbe | -2.684 | -49.5639 | 2025-11-28 02:50:00 | GOES-19 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 53.9 |
| 47fac846-47b7-362f-a11b-f4d75ac7f130 | -2.6181 | -47.3521 | 2025-11-28 02:50:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 47.1 |
| 813c21db-be53-3e18-aa40-32a9f7a82482 | -9.3809 | -40.375 | 2025-11-28 02:50:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 137.9 |
| 7f32dce4-2cce-37a9-a63d-c4490a03d401 | -9.4 | -40.3722 | 2025-11-28 02:50:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 156.9 |
| 68c909cc-b1ec-396a-9936-da82f9ce1509 | -9.72685 | -36.25375 | 2025-11-28 02:51:00 | NOAA-21 | ANADIA | ALAGOAS | Brasil | 2700201 | 27 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 612dc1b0-d394-369e-a559-64d68ce2ab83 | -7.33471 | -35.07444 | 2025-11-28 02:51:00 | NOAA-21 | PEDRAS DE FOGO | PARAÍBA | Brasil | 2511202 | 25 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| c0790907-e3c4-3aad-b51b-528a1124e168 | -9.72969 | -36.2594 | 2025-11-28 02:51:00 | NOAA-21 | ANADIA | ALAGOAS | Brasil | 2700201 | 27 | 33 | nan | nan | nan | Mata Atlântica | 7.1 |
| 2f5f24bf-5691-3e87-a789-041cd54c1203 | -5.88014 | -35.37868 | 2025-11-28 02:51:00 | NOAA-21 | MACAÍBA | RIO GRANDE DO NORTE | Brasil | 2407104 | 24 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 3e94a0b0-3833-3703-b284-7af1efc7b0fe | -7.33359 | -35.08044 | 2025-11-28 02:51:00 | NOAA-21 | PEDRAS DE FOGO | PARAÍBA | Brasil | 2511202 | 25 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| 02eb8333-0c23-3069-b617-f554c5220d4e | -9.72564 | -36.25976 | 2025-11-28 02:51:00 | NOAA-21 | ANADIA | ALAGOAS | Brasil | 2700201 | 27 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| ee1227ab-7a94-334b-8d21-5cb09c309864 | -9.73236 | -36.26097 | 2025-11-28 02:51:00 | NOAA-21 | CAMPO ALEGRE | ALAGOAS | Brasil | 2701407 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 8854bb1f-460b-395b-9724-1442ea76f59b | -3.8617 | -47.0657 | 2025-11-28 03:00:00 | GOES-19 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 53.1 |
| 2dba526c-ce8e-3222-8147-10efc32875db | -3.751 | -46.9388 | 2025-11-28 03:00:00 | GOES-19 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 56.1 |
| f62a95e5-9878-305d-bbad-af48bfb02ca2 | -9.4 | -40.3722 | 2025-11-28 03:00:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 117.6 |
| e070b17c-a6a5-3a4d-9b13-0c85f91f4850 | -3.7694 | -46.96 | 2025-11-28 03:00:00 | GOES-19 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 85.5 |
| 69e7f7a2-fc85-34cf-a180-77b1f2b3bcfd | -3.7508 | -46.9608 | 2025-11-28 03:00:00 | GOES-19 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 103.2 |
| ae9b1c31-d955-3f35-b68a-5d1a03eb3f83 | -9.3809 | -40.375 | 2025-11-28 03:00:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 109.3 |
| 74cf7db0-7700-3fd4-a9d2-ea2e49e48862 | -2.6181 | -47.3521 | 2025-11-28 03:00:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 88.7 |
| 31f0b5f7-1260-380d-bfa4-3bbd64ce6f30 | -3.8431 | -47.0666 | 2025-11-28 03:00:00 | GOES-19 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 54.2 |
| 2269a247-a019-3a20-b5fb-31beea1052dc | -2.6181 | -47.3521 | 2025-11-28 03:10:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 95.6 |
| 09ee6551-812e-3d0c-bab1-30c9fd5d581d | -3.7508 | -46.9608 | 2025-11-28 03:10:00 | GOES-19 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 137.8 |
| e9292612-c055-3fb9-97ec-f8a19cac6f70 | -3.751 | -46.9388 | 2025-11-28 03:10:00 | GOES-19 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 68.6 |
| 2dbbb0bf-7333-353d-af4d-2fbe008371f3 | -3.7694 | -46.96 | 2025-11-28 03:10:00 | GOES-19 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 101.0 |
| 450a54fe-a60d-3574-afb0-a085dcdec7f9 | -9.3809 | -40.375 | 2025-11-28 03:10:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 101.3 |
| c88d1619-0597-3f23-ba23-6261355f8ae5 | -9.4 | -40.3722 | 2025-11-28 03:10:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 122.4 |
| 0fa27c66-5a44-340f-9af1-3c7785d7fa7b | -3.8431 | -47.0666 | 2025-11-28 03:10:00 | GOES-19 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 51.2 |
| 9ec1d8da-81d7-3b56-b7d9-083febbcb3c1 | -3.86899 | -40.64238 | 2025-11-28 03:19:00 | NPP-375D | CARIRÉ | CEARÁ | Brasil | 2303105 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |


[Clique aqui para ver as próximas entradas](README5.md)
