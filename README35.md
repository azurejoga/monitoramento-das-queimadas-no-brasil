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

## Dados Diários - Página 35

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f45970fb-127d-3fdb-a3b1-d0630b6f7a19 | -0.8773 | -51.72343 | 2024-11-26 04:59:00 | NOAA-20 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d8a0c7f5-9b6c-3578-86f3-8b85d47bb3fb | -1.08745 | -53.64664 | 2024-11-26 04:59:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 06913da5-f155-3453-8041-07d0453c3086 | -1.42192 | -55.27906 | 2024-11-26 04:59:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2a44907a-5171-3f8f-834e-55a0a362d8dd | 0.66815 | -50.79385 | 2024-11-26 04:59:00 | NOAA-20 | ITAUBAL | AMAPÁ | Brasil | 1600253 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| aba99241-1463-37c9-8bf1-931175478797 | -1.1575 | -53.67541 | 2024-11-26 04:59:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 68cd879c-bb7c-3f54-b873-563e4ee84ffb | -2.71895 | -46.28667 | 2024-11-26 04:59:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 80b59779-79d6-32f9-9cba-f83b5a702631 | -1.37314 | -52.33154 | 2024-11-26 04:59:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 67ec8edf-96ad-3ec8-9aac-49397622ffe8 | -1.55948 | -45.67639 | 2024-11-26 04:59:00 | NOAA-20 | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b0baad4e-0a48-36f6-ad86-aa84c6196564 | -0.09487 | -51.74976 | 2024-11-26 04:59:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.2 |
| dc8a20da-ed04-370e-bed6-bff999006f3c | 1.93187 | -55.72116 | 2024-11-26 04:59:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 91fed3d3-11f7-3637-bd47-a0ff9626decb | -1.30957 | -51.73687 | 2024-11-26 04:59:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 58b79143-77fb-3a8c-bcda-10f05eae73f7 | -1.72396 | -53.24956 | 2024-11-26 04:59:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| acd05c68-ea39-3a9b-a2f0-0eb86cf60dfc | -2.17848 | -45.60263 | 2024-11-26 04:59:00 | NOAA-20 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 1023e8a4-6c3e-3ea0-8b79-a4937c8a89f6 | -0.87792 | -51.71947 | 2024-11-26 04:59:00 | NOAA-20 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fd4d2517-dc9d-30d5-bb91-93ecc8d6a6d2 | -1.37698 | -52.84598 | 2024-11-26 04:59:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ca13891f-2ac1-31c1-9b75-d2e53e702691 | -0.34173 | -51.98011 | 2024-11-26 04:59:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b8a3af60-d73c-3634-af93-a613996ebaa5 | -1.29244 | -51.73013 | 2024-11-26 04:59:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d08502a9-df1e-3e0d-aeff-c09118980ed6 | -1.1156 | -53.57588 | 2024-11-26 04:59:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bf15a97f-1734-3b56-abfc-fe24c8e7fccb | -1.14002 | -54.11185 | 2024-11-26 04:59:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 972f678f-347b-3470-8785-5c889cce90e4 | -1.59445 | -52.25844 | 2024-11-26 04:59:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 53a2b9ce-293d-356a-a6a2-8d1bb2a1eaca | -0.36692 | -51.53959 | 2024-11-26 04:59:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 86206451-8b12-3ed4-bfdd-aa4b2b33aa46 | -1.04482 | -51.73946 | 2024-11-26 04:59:00 | NOAA-20 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1eb4c279-288c-328a-8f7e-6382e2dfdf1e | -1.35875 | -51.37637 | 2024-11-26 04:59:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d479a6ff-e254-3751-9720-3875b4ce6573 | -1.57038 | -52.01406 | 2024-11-26 04:59:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 755f1237-3ead-373b-a9e2-64ddc7ea1470 | -1.27382 | -52.16878 | 2024-11-26 04:59:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a4855d2b-b543-329f-b4ca-8d20fbf60eca | -1.58506 | -53.83038 | 2024-11-26 04:59:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 12a155d6-5f91-3427-b2e9-4610503bff7c | 1.94732 | -60.85823 | 2024-11-26 04:59:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 4.2 |
| c8719080-0dde-31f8-a0bc-423fe6418eba | -0.34989 | -51.97343 | 2024-11-26 04:59:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6677ebd2-d1d6-35fa-b469-79489078a8b0 | 3.82667 | -59.59607 | 2024-11-26 04:59:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 532c15ab-3c87-3631-b205-965d6cec6ee7 | -1.32231 | -52.23471 | 2024-11-26 04:59:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c966aa78-acd8-330d-886f-642c407e0919 | -1.23912 | -53.39362 | 2024-11-26 04:59:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b914a847-fd7f-3f69-b35a-8814741657f0 | 0.48693 | -50.95288 | 2024-11-26 04:59:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3b6026cc-68cc-3a6d-a9d9-06f5839a3a74 | -1.11027 | -53.39172 | 2024-11-26 04:59:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 656deba6-075e-3f6f-8be8-4861f31fd519 | -1.10379 | -54.14851 | 2024-11-26 04:59:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0091fcd8-c484-3e70-b1ec-06b94ef3dbf4 | -1.82584 | -45.58721 | 2024-11-26 04:59:00 | NOAA-20 | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| eb61b5a4-399b-31fc-84a9-d2fbc3b99768 | -1.78325 | -52.73779 | 2024-11-26 04:59:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b987db5c-34e3-3b51-90d6-522af7f15a61 | -1.06246 | -53.19946 | 2024-11-26 04:59:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c9c82f36-4889-3c05-93e1-d09fbe1e3016 | -2.15034 | -48.04441 | 2024-11-26 04:59:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9273c15c-512b-38b7-b989-134427878fac | -1.36743 | -52.55025 | 2024-11-26 04:59:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 29c85c21-9878-34ba-a1b1-e92d5dc3dea3 | -1.10325 | -54.15195 | 2024-11-26 04:59:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 2b668bbf-01c3-3bcd-ab7e-79ec1202ecf4 | -1.35706 | -54.63446 | 2024-11-26 04:59:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 55d2c8ac-abfd-30a3-9e61-58af17828c0c | 1.81655 | -55.9471 | 2024-11-26 04:59:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 223ee1a7-7b50-3cfe-80e8-e0f5adcd4374 | -1.60023 | -52.26718 | 2024-11-26 04:59:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9f1b18be-b9b5-3f6b-9e6d-36301e448ffd | 1.84584 | -55.88969 | 2024-11-26 04:59:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b8fd90c7-a06a-3e9e-a1fa-27f128d99869 | -1.75704 | -52.7034 | 2024-11-26 04:59:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3a9c6956-3983-3453-a5ad-a34894ce604a | 1.93361 | -55.75485 | 2024-11-26 04:59:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 9f488bc5-65c0-3ba1-803a-2159164e03ed | -1.351 | -54.63001 | 2024-11-26 04:59:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5334397d-9f83-3185-a72e-9bd3185132fb | -0.95407 | -51.64881 | 2024-11-26 04:59:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 965fb754-33ac-3b0a-bf33-40fce7f83a87 | -1.3576 | -54.63103 | 2024-11-26 04:59:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| fe0f1655-d838-38f6-afbb-6a86f7313fa7 | -1.69114 | -52.60995 | 2024-11-26 04:59:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d70b32bf-6382-3ef8-bd62-a49050998c35 | -1.471 | -52.29599 | 2024-11-26 04:59:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| e847296d-9d35-3dce-bda8-958fd2f46c6d | -2.71684 | -46.28874 | 2024-11-26 04:59:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 65f8ccee-fd94-3c78-8e40-87aef2106a6f | -1.56526 | -45.67394 | 2024-11-26 04:59:00 | NOAA-20 | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 06ece690-798a-3b01-939a-db684edb1590 | -1.55997 | -45.67316 | 2024-11-26 04:59:00 | NOAA-20 | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7ebfb7c8-8109-3bdc-bc44-017511841d19 | -1.37255 | -52.33534 | 2024-11-26 04:59:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9ebc0e03-52c9-3b6d-a226-a4b0dda472d0 | -1.4829 | -53.81089 | 2024-11-26 04:59:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 98c2a16f-b9a2-342e-b324-228be1cf1882 | -1.58561 | -53.8269 | 2024-11-26 04:59:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 889cc1ff-2e9f-3eea-b43d-b283cfe3dd6a | -1.36735 | -52.08399 | 2024-11-26 04:59:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 46cb68bd-f044-36d9-9fcd-80804a306658 | -2.18623 | -45.60743 | 2024-11-26 04:59:00 | NOAA-20 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2d9c5860-eda6-3ae0-9b00-4486a1abb9a0 | -1.78383 | -52.73409 | 2024-11-26 04:59:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c1ec4f6b-7ecc-34db-8ada-0f3e705cafb2 | 4.23468 | -60.0731 | 2024-11-26 04:59:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 2.6 |
| fed19a0c-d0fb-35e8-b82c-2ae4cdb291c4 | -1.39632 | -55.20422 | 2024-11-26 04:59:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b7701142-dc87-36f4-986a-20cbce05035b | -1.63468 | -53.30178 | 2024-11-26 04:59:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| cd91facc-b245-3cdd-87c6-7fa9bae92587 | -1.42578 | -55.27612 | 2024-11-26 04:59:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 27e818c3-ffdb-3d2e-9f89-6f96142af06f | -1.12108 | -53.19018 | 2024-11-26 04:59:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1c288b3b-fe9f-335a-b593-9bf16c0c94da | 0.95113 | -50.75863 | 2024-11-26 04:59:00 | NOAA-20 | CUTIAS | AMAPÁ | Brasil | 1600212 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 17ce8f3c-d57e-3e14-b16f-558707c21946 | -1.35046 | -54.63344 | 2024-11-26 04:59:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 78c634b4-db3f-374f-a595-557a575e65b7 | -0.87313 | -51.72688 | 2024-11-26 04:59:00 | NOAA-20 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 54e3a91b-eb2b-3cfc-9124-cf4e9dad0313 | -1.77071 | -52.72828 | 2024-11-26 04:59:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e4dec9a9-98d0-3900-8db2-4f336d7f48f6 | -1.8685 | -50.66719 | 2024-11-26 04:59:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 22ee1957-2296-3921-82c4-3bea20cf419a | -1.10693 | -53.3912 | 2024-11-26 04:59:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ac473214-ccd8-3463-9a93-fb6c80a1bca0 | -1.59964 | -52.27102 | 2024-11-26 04:59:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 695b0cdc-cae2-31ac-a7d4-5f43a183e437 | -2.18138 | -45.60315 | 2024-11-26 04:59:00 | NOAA-20 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a817e46e-37e7-3705-8a23-6f2396d0fc3a | -2.71548 | -46.26332 | 2024-11-26 04:59:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0f3d9aca-3f56-3d42-9ed4-48e075ef68a2 | -1.6144 | -52.35929 | 2024-11-26 04:59:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 22203d18-8e9b-3724-9f2b-1ec65939618b | 0.94713 | -50.73329 | 2024-11-26 04:59:00 | NOAA-20 | CUTIAS | AMAPÁ | Brasil | 1600212 | 16 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5dc5e097-471d-3c9f-8f9b-14a2d77db283 | 3.82231 | -59.59672 | 2024-11-26 04:59:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 218491ef-547d-39f3-98a7-f1322aa42785 | -1.44013 | -52.44631 | 2024-11-26 04:59:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0e11d16f-0fd0-3825-879a-72641b4af669 | -1.74104 | -52.73886 | 2024-11-26 04:59:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5272c272-8e9a-317d-8b3f-7292167daf58 | -1.3991 | -55.20818 | 2024-11-26 04:59:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f62ca364-cb2d-350c-a4c0-e6fb0a657b43 | -1.69172 | -52.60622 | 2024-11-26 04:59:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 74f455b7-fbe6-3810-9c19-2d6ae7dcf90e | -1.35982 | -51.44031 | 2024-11-26 04:59:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c3398753-3796-3a9d-ad23-96bf6ee3e2b8 | 2.68391 | -60.42698 | 2024-11-26 04:59:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 08db0606-e0e6-3924-8a9d-e2bf481126cf | -1.72365 | -52.49211 | 2024-11-26 04:59:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9e0b6bf3-fc47-3920-9a95-e4cf5be13f3f | -1.5716 | -52.00624 | 2024-11-26 04:59:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 204287b3-b192-390e-a90e-e583acdd6b65 | -1.3543 | -54.63052 | 2024-11-26 04:59:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 0fa19cc4-b47c-3176-bca7-ab36bbc4a0bc | -1.3949 | -52.55446 | 2024-11-26 04:59:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b49a377e-063d-383f-b1fa-bd1cfdf3ae4e | 1.95122 | -60.85275 | 2024-11-26 04:59:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 87c42c9b-4d6e-3d7a-96ee-d50e950bd18e | -2.71731 | -46.28569 | 2024-11-26 04:59:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c671e338-d0e9-30fc-ac06-939fc0a2ec67 | -1.062 | -48.02422 | 2024-11-26 04:59:00 | NOAA-20 | VIGIA | PARÁ | Brasil | 1508209 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 54b4c992-b043-30ef-98ab-a5880ed8f0f1 | -0.76483 | -52.45996 | 2024-11-26 04:59:00 | NOAA-20 | LARANJAL DO JARI | AMAPÁ | Brasil | 1600279 | 16 | 33 | nan | nan | nan | Amazônia | 0.5 |
| f611151a-a706-3223-b524-18d7d28646d1 | 1.94661 | -60.8535 | 2024-11-26 04:59:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 59190241-7cf8-3030-8a19-66710d1b1525 | -1.78041 | -52.73356 | 2024-11-26 04:59:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0c3698c2-7392-31c0-bb5a-019a57eef670 | 1.93929 | -55.74642 | 2024-11-26 04:59:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9306abc2-d413-3dfe-b281-24ce785d8bb5 | -2.6943 | -51.9831 | 2024-11-26 05:00:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 55.3 |
| e9d432f9-18c1-352b-b4f1-c60455f87766 | -3.1877 | -48.4172 | 2024-11-26 05:00:00 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 60.0 |
| 26efba51-7900-30db-97c3-eecebe4ad379 | -3.1691 | -48.4394 | 2024-11-26 05:00:00 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 50.6 |
| 3c8ea564-b927-3fe1-9fab-51ad9dc5efd9 | -3.1876 | -48.4387 | 2024-11-26 05:00:00 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 140.8 |
| 61bd6d0b-0d6d-340e-87ef-c1b09f7a49df | -17.6453 | -57.5874 | 2024-11-26 05:00:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 63.5 |
| 2f0fbccf-82c2-38b5-acf3-1883727cccbf | -4.0 | -48.09 | 2024-11-26 05:00:00 | MSG-03 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README36.md)
