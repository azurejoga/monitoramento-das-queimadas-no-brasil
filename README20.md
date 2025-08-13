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

## Dados Diários - Página 20

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0489873d-9223-33fc-a787-21ba7ea22379 | -6.91106 | -59.13456 | 2025-08-13 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 19.9 |
| cfd93fe5-76c9-3063-82ca-43fc72812f0e | -9.06401 | -60.65145 | 2025-08-13 04:40:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 558fadce-29fe-357a-9fa8-893fa8dfeab2 | -9.0626 | -60.65209 | 2025-08-13 04:40:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 64802b84-abba-310a-b8b3-9645b33eaf20 | -10.02045 | -58.43233 | 2025-08-13 04:40:00 | NOAA-21 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 6.2 |
| b1d0f0da-dad2-3ca1-815a-c3fc4d2844d7 | -9.36334 | -47.62806 | 2025-08-13 04:40:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9f976843-6f10-3eb4-b812-8113aa99bad5 | -9.27532 | -60.76545 | 2025-08-13 04:40:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 34343926-9f0c-390e-85e4-585e94c9fe9a | -6.91168 | -59.13107 | 2025-08-13 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 7cda1692-55bc-3273-9eb5-d7507b0f1ff9 | -10.71143 | -48.8448 | 2025-08-13 04:40:00 | NOAA-21 | OLIVEIRA DE FÁTIMA | TOCANTINS | Brasil | 1715507 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8cd10e97-80ab-3701-9b06-1c6cb20e2326 | -12.51736 | -46.97043 | 2025-08-13 04:40:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| b40fccd4-9c19-3c7b-ab90-e4edc6fc54a8 | -7.24302 | -59.9983 | 2025-08-13 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 5768ae64-5a20-332c-8dc2-c9b5afe5f3a5 | -5.89255 | -57.74863 | 2025-08-13 04:40:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 892898dc-b444-3da7-bdda-1b48c8e27bab | -8.7999 | -52.04635 | 2025-08-13 04:40:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7aefa3df-3c94-3245-aa87-f5b9e8daecb0 | -7.14138 | -60.12379 | 2025-08-13 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.2 |
| e95d96df-b131-36a3-8060-3cf999e8f57f | -12.58206 | -47.05958 | 2025-08-13 04:40:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| af5a7a71-ff2f-3720-a73b-2a37e491470b | -7.26006 | -60.00115 | 2025-08-13 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b18f873e-e76c-3bb1-9ff1-0d3809df672e | -6.2777 | -53.63542 | 2025-08-13 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a5da0b79-82a8-372a-85e0-7fcf68822daa | -8.56231 | -54.71056 | 2025-08-13 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ffc33924-2245-305a-a789-a76a1afda07f | -9.19335 | -59.66095 | 2025-08-13 04:40:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 0356e092-c77f-39e5-a185-687943f094e2 | -8.89185 | -50.15551 | 2025-08-13 04:40:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e9cbf660-525d-35fe-82df-d2a91bc3e731 | -10.41723 | -54.40656 | 2025-08-13 04:40:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 561283de-247c-33e1-a71d-8d32e6c7266e | -7.48625 | -43.93102 | 2025-08-13 04:40:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 10d2cd4b-25ef-36be-8b69-1cdafd960832 | -6.87563 | -59.14601 | 2025-08-13 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 9.0 |
| e503e573-77bb-3ffb-8b3d-cb4c770e3b4c | -13.38538 | -44.41832 | 2025-08-13 04:40:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7fec2ce4-6459-31e1-8375-9aeee0ea97c8 | -7.45436 | -60.63514 | 2025-08-13 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a13387fd-1d52-3570-bfe1-49385b6dcbc1 | -9.19868 | -59.66211 | 2025-08-13 04:40:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2091d931-06a3-3ec0-b9f5-2a303c4ef6fe | -12.53471 | -46.98537 | 2025-08-13 04:40:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 3bfe8797-8081-36d7-a91a-395c3926e66b | -11.69252 | -50.13841 | 2025-08-13 04:40:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| cd7b2e47-c1a6-3254-bf49-eee25969991c | -8.93423 | -60.73343 | 2025-08-13 04:40:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e3210374-d9fb-39c5-a7d8-f3df990816a7 | -12.51803 | -46.9658 | 2025-08-13 04:40:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 62516365-aeb4-3634-b66b-75332b585f24 | -6.10417 | -59.93258 | 2025-08-13 04:40:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f68e9bfb-591d-3475-8796-1bc412237857 | -9.06477 | -60.64743 | 2025-08-13 04:40:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 83ab60d6-1f8e-3cb7-b292-15736c917420 | -6.87808 | -59.13242 | 2025-08-13 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 13.2 |
| 3702cb12-2b1d-3181-b2a1-c4ef2de607da | -6.61133 | -43.88847 | 2025-08-13 04:40:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 738b6a4b-a49e-3f1a-b4a7-3e12d2c21555 | -5.73226 | -51.68438 | 2025-08-13 04:40:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9b210e05-2c82-3d92-86e5-105694c3d052 | -6.89551 | -59.12822 | 2025-08-13 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 13.3 |
| 015952aa-c0c3-34a7-8b43-40a60d5c7c85 | -6.88701 | -59.14463 | 2025-08-13 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 32.4 |
| 20994351-8812-3e7b-8664-eab3ce56c9fc | -9.2072 | -59.64595 | 2025-08-13 04:40:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ada571ee-3a79-393d-9dba-eed54ffb9ccb | -7.45843 | -59.88686 | 2025-08-13 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 38aa246d-b4c0-3d5c-b66f-8054506fd193 | -10.18599 | -49.50601 | 2025-08-13 04:40:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e86fab55-60d9-39b9-9bfa-21988d96e70f | -6.87746 | -59.13582 | 2025-08-13 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 13.2 |
| 260545ee-9e51-3cdd-bb60-611e1c19de5a | -12.56578 | -47.03885 | 2025-08-13 04:40:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| f59429c5-0e77-3378-b83f-61473e5074ac | -10.36465 | -50.8063 | 2025-08-13 04:40:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 13e1b7ad-f87a-3607-8680-dd67259843c1 | -9.85148 | -50.15157 | 2025-08-13 04:40:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 66ef3ec7-a081-37db-84f6-7fd6d2eceecc | -11.68478 | -50.14443 | 2025-08-13 04:40:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2104bc2b-1237-3573-8c0c-8daca64413d3 | -11.63996 | -50.1482 | 2025-08-13 04:40:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3cdae8e5-da04-38b4-a0a5-1a6d4a298da0 | -10.96686 | -49.57247 | 2025-08-13 04:40:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 0bec2bf1-96ab-3d3d-ab2f-b592ded96d5e | -9.05688 | -60.65097 | 2025-08-13 04:40:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 11f1aeec-f9e6-39d9-b0fe-d4f4e9da874d | -7.46024 | -60.63618 | 2025-08-13 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fe171f5a-f412-371a-8c57-789e94813821 | -7.05617 | -43.44145 | 2025-08-13 04:40:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| b77fbcdf-dbc6-3b1a-9a81-b9e67eea7fc9 | -7.12713 | -60.13027 | 2025-08-13 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 12.4 |
| 13f913f0-98ba-3307-93d7-8aeea9097282 | -8.6842 | -51.45085 | 2025-08-13 04:40:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a16255d4-9440-3ed3-bbff-a5d577b18eb2 | -6.59044 | -44.55645 | 2025-08-13 04:40:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 9e2846dd-300e-36f9-bdfd-fdb1fbf6ce5b | -6.88579 | -59.15141 | 2025-08-13 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 21.3 |
| 1e4fc22d-0a28-3d7b-b6b2-a110a636f35e | -12.57444 | -47.05916 | 2025-08-13 04:40:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d205688b-0e90-3cdc-8572-ea23df1122f5 | -10.47735 | -61.32235 | 2025-08-13 04:40:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 57df6230-d1d6-354b-a92f-8fc94a2008b0 | -12.50604 | -46.9687 | 2025-08-13 04:40:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 880fe52b-7093-3e6d-a165-731a4e4a28b2 | -12.58438 | -46.98862 | 2025-08-13 04:40:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a8116971-b6b7-324c-944c-c2a7aa380ce6 | -12.51425 | -46.96522 | 2025-08-13 04:40:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| cb8f343d-daa6-3eca-8183-8449d71386de | -9.19933 | -59.65862 | 2025-08-13 04:40:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e1e9dc96-7bd5-3ba0-ab50-ec8453f68daf | -12.52491 | -46.9716 | 2025-08-13 04:40:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 3622d32b-5380-32b5-823f-ac25017b6517 | -12.54419 | -46.97253 | 2025-08-13 04:40:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 731598e8-a8f1-3274-a31e-e2c4374d2114 | -12.30727 | -46.04824 | 2025-08-13 04:40:00 | NOAA-21 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| ef101ab7-f897-3ed6-9b36-f83dbad36d36 | -8.92926 | -60.72817 | 2025-08-13 04:40:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fbe9d03c-def9-3000-9cee-070cf519e8f2 | -9.77584 | -46.67755 | 2025-08-13 04:40:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b36b9ef7-fe1f-3941-a904-0cf07988f63c | -7.14779 | -60.12104 | 2025-08-13 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 37e6a2d2-1038-35bf-9e40-234b1d31ee3a | -11.90809 | -52.53276 | 2025-08-13 04:40:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b481a12a-04af-37a7-a74a-940b3f802224 | -9.71754 | -49.47966 | 2025-08-13 04:40:00 | NOAA-21 | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 2a6e13f6-404e-3eb8-ada2-b5c26481747c | -5.85522 | -52.10739 | 2025-08-13 04:40:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 30d1830d-03ef-3c72-8630-fda92ea0a905 | -12.30333 | -50.00884 | 2025-08-13 04:40:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a694e881-1a84-3982-8dee-239259619d16 | -6.10274 | -59.94057 | 2025-08-13 04:40:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 36d3eef1-b378-321a-93d8-b51c3baf8b28 | -12.49537 | -46.9623 | 2025-08-13 04:40:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 5c59460a-8606-391a-9057-84a3bf040d30 | -7.1342 | -60.13073 | 2025-08-13 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.2 |
| ad58dbff-0740-3979-a93b-ae242c391cde | -9.51384 | -62.37541 | 2025-08-13 04:40:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 23dc3602-86f2-30a8-acc7-22066b296fb0 | -9.71421 | -49.47914 | 2025-08-13 04:40:00 | NOAA-21 | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 2ebe3dfa-b13d-3f4e-bed8-91121effca67 | -9.71088 | -49.47861 | 2025-08-13 04:40:00 | NOAA-21 | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 7.7 |
| cefe3d09-4d79-36eb-b5ba-7a9992c94651 | -6.92604 | -59.1441 | 2025-08-13 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 13.2 |
| cdd10bc2-6faa-3862-83b2-3dce52fde129 | -8.56481 | -54.69567 | 2025-08-13 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b02e378c-fe41-3501-bbcd-30ee61852e39 | -9.94287 | -48.34284 | 2025-08-13 04:40:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 09ed99ed-85d9-3aff-85f9-b495274018d7 | -6.97553 | -59.28472 | 2025-08-13 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3af9c93e-a4f5-3174-ad69-4eefeec0d1d9 | -10.5592 | -52.65818 | 2025-08-13 04:40:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 556d033c-86c4-3dc9-9f4b-b2a64bb48c0b | -12.48339 | -46.96523 | 2025-08-13 04:40:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 94b4704a-66b1-3375-87cf-d5017446e6e9 | -8.38312 | -49.361 | 2025-08-13 04:40:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 94a9f608-44a9-399d-a31b-aa68fe06d279 | -8.10756 | -55.57554 | 2025-08-13 04:40:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 7cfd3285-cd67-3746-8e71-0f8f9189dade | -6.09622 | -59.94383 | 2025-08-13 04:40:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 4aa83b57-4ca3-3618-9ffb-c2a90c9ce370 | -6.95186 | -56.39127 | 2025-08-13 04:40:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 483e50fa-7907-3c65-b8c9-201c4cee600a | -7.14709 | -60.12489 | 2025-08-13 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 92844b8a-da60-381c-a26e-10013ad5c813 | -10.70859 | -48.84056 | 2025-08-13 04:40:00 | NOAA-21 | OLIVEIRA DE FÁTIMA | TOCANTINS | Brasil | 1715507 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6cd7ae07-01cd-32f5-85e9-2c96bfc36a58 | -11.78419 | -51.89631 | 2025-08-13 04:40:00 | NOAA-21 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 19552dae-c52a-3e64-8e51-6598063b4345 | -9.18673 | -59.66679 | 2025-08-13 04:40:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b0f7aec3-8baa-325b-97d2-87c3bf247043 | -8.56564 | -54.6907 | 2025-08-13 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e51d30cb-bb68-3d50-9d77-10968f1860cc | -6.90442 | -59.14062 | 2025-08-13 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 12.4 |
| aa5d0fab-e424-3a1b-a50f-24092da03de9 | -9.38304 | -61.52758 | 2025-08-13 04:40:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| dcd086ba-9ede-39a0-afe3-d898eb2c769e | -10.96966 | -49.57657 | 2025-08-13 04:40:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 56269924-69c8-32e5-86b0-9a46f226b211 | -6.91044 | -59.13805 | 2025-08-13 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 19.9 |
| 810ae078-27d8-3761-95b3-99045dbc62e4 | -11.45999 | -47.30651 | 2025-08-13 04:40:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a04e1331-f077-3af1-b4a3-5626f2e64037 | -6.87147 | -59.1382 | 2025-08-13 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 13.2 |
| b43a12a0-ef29-3652-9da3-b18d51f3f5aa | -8.10949 | -55.56404 | 2025-08-13 04:40:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 23.5 |
| d2a98d13-91f9-3cfc-883b-600ac5590f93 | -12.5218 | -46.96637 | 2025-08-13 04:40:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 6abe38e8-9d96-3379-b135-7ba940572252 | -8.37926 | -49.364 | 2025-08-13 04:40:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b40bc834-9356-395d-aa4b-e676dfd244d1 | -8.79307 | -52.04523 | 2025-08-13 04:40:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |


[Clique aqui para ver as próximas entradas](README21.md)
