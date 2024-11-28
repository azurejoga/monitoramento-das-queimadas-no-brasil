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

## Dados Diários - Página 86

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5b7fa0e6-664d-3cba-8fc2-2ff31c44283e | -2.99565 | -51.00328 | 2024-11-28 05:18:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9928f6eb-4755-399a-98d7-9d1016c22b47 | -4.21579 | -50.89128 | 2024-11-28 05:18:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 206c0cde-641d-3d3e-a4b5-0b6bbe54b235 | -2.83086 | -54.10351 | 2024-11-28 05:18:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 483c342f-13ce-35a8-9ce9-c4ff7fd84c3d | -3.08259 | -49.21109 | 2024-11-28 05:18:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 09a2739b-a69c-3a1c-a1df-632caef92d29 | -3.29273 | -50.5411 | 2024-11-28 05:18:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 77b9be13-2e09-3e12-ad53-07ef13bec0e2 | -3.75016 | -51.78167 | 2024-11-28 05:18:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d64cd0bf-5ee3-35cd-a063-03c37ff57492 | -2.90804 | -54.18022 | 2024-11-28 05:18:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 3df540f6-8e79-3ad8-bf01-44e78947a2fe | -2.85772 | -53.95481 | 2024-11-28 05:18:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4b11c071-bbed-3243-9920-b1aa5654df0d | -3.53746 | -50.19138 | 2024-11-28 05:18:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c44ea55b-5cfd-3502-9f28-058b8262a7d6 | -2.83199 | -54.0449 | 2024-11-28 05:18:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| da26de54-eaa0-3968-9843-5f5d58ff84f9 | -3.50009 | -53.82519 | 2024-11-28 05:18:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 0f64ce9f-357f-38dc-b298-9f565f3515ff | -3.96713 | -50.19129 | 2024-11-28 05:18:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 14.2 |
| 2bc92790-ab6a-369c-9f4d-1811bd3947a8 | -2.60336 | -53.96607 | 2024-11-28 05:18:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 267efa83-5494-3e99-b1b7-fa79f17bfb59 | -3.25337 | -50.62311 | 2024-11-28 05:18:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 3ecff27d-4959-3fee-94a2-cc393ac09308 | -3.33559 | -50.07686 | 2024-11-28 05:18:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2c92edd2-3881-33cc-9a70-d3efbcd7e79f | -2.96571 | -51.0028 | 2024-11-28 05:18:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 8b053cf6-dd52-308e-be72-7fc4b17c6194 | -3.51027 | -50.3129 | 2024-11-28 05:18:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| de9bd23f-814e-3973-82f4-1c4b28ac7aee | -3.47279 | -51.62512 | 2024-11-28 05:18:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 73039c66-5aa0-3a84-8a14-481b1a52995a | -2.91547 | -51.71344 | 2024-11-28 05:18:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| c7e53668-a117-3912-b73f-bfe8b7a3a331 | -6.37754 | -45.69278 | 2024-11-28 05:18:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 23c41ebf-c4af-3b61-837b-7148007effc5 | -3.17746 | -48.43992 | 2024-11-28 05:18:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8f53930f-719c-3d84-a000-15bae511dc46 | -3.37416 | -50.12092 | 2024-11-28 05:18:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f9ef7eb5-fffe-3a39-9f34-f0d37895a8a2 | -3.8154 | -52.23352 | 2024-11-28 05:18:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ef67931e-0d41-3588-af4d-fd7b7947393f | -3.26331 | -54.11373 | 2024-11-28 05:18:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e99a0907-0b27-31ff-a4ea-ef60b64e95ab | -2.97987 | -53.35489 | 2024-11-28 05:18:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d56b5e05-0e6c-365b-9f67-aad447ae6b9a | -3.10442 | -53.81363 | 2024-11-28 05:18:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 13.1 |
| aa34b421-df59-3e76-8230-cd0e9ed70410 | -3.31053 | -50.27594 | 2024-11-28 05:18:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e384e912-3e67-3ab8-959a-499bad6e722a | -2.60742 | -51.79235 | 2024-11-28 05:18:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 008bf6cd-3793-37e6-b1e8-d4e84f801223 | -3.57933 | -50.32967 | 2024-11-28 05:18:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 6ee1668c-1988-377d-b75e-a72742d0bfe5 | -3.54295 | -50.18921 | 2024-11-28 05:18:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d2cd8050-51f1-34de-9a3f-17371dbad187 | -2.25491 | -53.75143 | 2024-11-28 05:18:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 22c21dc8-bb1f-35bb-81cd-b5a2543c2665 | -4.13158 | -54.89727 | 2024-11-28 05:18:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 18a6d754-1fc5-300d-bbe0-eade2fb9e8d6 | -3.51875 | -50.22161 | 2024-11-28 05:18:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a1cf56e0-1d4f-3dae-8f8e-903945306de8 | -3.68266 | -50.21812 | 2024-11-28 05:18:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d4732cbc-f28e-3861-b5aa-58dfa359ddfd | -2.43466 | -50.41757 | 2024-11-28 05:18:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 199bd9e0-0fcd-3a76-b46f-a1f30d1c7583 | -3.57889 | -50.3327 | 2024-11-28 05:18:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 5b8f0b9e-bd94-38dc-b3ce-9473cd0b016c | -2.83635 | -54.11896 | 2024-11-28 05:18:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| d61a10c9-da73-32b1-8dbf-f50891d579cf | -2.60189 | -53.97573 | 2024-11-28 05:18:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| ccb794d6-23e6-3ca2-83cb-430b205132a3 | -2.58765 | -51.92375 | 2024-11-28 05:18:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5c63d5c7-9e36-3eeb-a381-2415304ba052 | -3.79644 | -51.39384 | 2024-11-28 05:18:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a784b558-449a-3360-9b29-31d777ec1de0 | -2.69988 | -51.68011 | 2024-11-28 05:18:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 5eeb7ab2-60b7-3f5e-a1fa-af0752ca9a32 | -3.01378 | -54.04181 | 2024-11-28 05:18:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0eb270ba-6a01-3fc1-ac28-991fd5de4fed | -3.39148 | -50.31829 | 2024-11-28 05:18:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| efaa2380-347d-31bf-b578-f8e835b12d70 | -2.7412 | -54.15966 | 2024-11-28 05:18:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 57354527-6759-37a6-a9f7-426a2636cd98 | -3.04547 | -54.04174 | 2024-11-28 05:18:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9988e90b-cc20-3b21-ad7e-e813539a592f | -2.59254 | -51.83065 | 2024-11-28 05:18:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 630661e3-f388-3295-bafd-ae216ab5da15 | -2.37404 | -56.12594 | 2024-11-28 05:18:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d8fceb96-90c4-36ce-8836-b6593c55202f | -2.90421 | -54.17962 | 2024-11-28 05:18:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 9cdd960b-cd92-3c10-ba55-3a4698b31fc2 | -3.41276 | -50.24465 | 2024-11-28 05:18:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 156a6757-fa6e-352c-a44e-caa1a291d001 | -2.59699 | -51.83134 | 2024-11-28 05:18:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cf5deca6-d0a8-3d7f-88f1-44b0c974c110 | -2.83913 | -54.07545 | 2024-11-28 05:18:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| b67100a0-ccfb-3f60-acb4-27a1681c6bce | -3.50275 | -50.46498 | 2024-11-28 05:18:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 5279380a-b701-3855-8f40-3303a18eb7a8 | -3.441 | -50.12537 | 2024-11-28 05:18:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 41c7333d-f9d3-3ceb-aa2a-d0f0d6a4b0dd | -3.6107 | -51.15276 | 2024-11-28 05:18:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e7b3f622-a352-3c0d-9a0b-310f5b7d46b4 | -2.8804 | -51.47468 | 2024-11-28 05:18:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7ab8b558-b461-3d78-b0e5-6a68fa2b277c | -3.68162 | -49.93314 | 2024-11-28 05:18:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 612508e6-e302-35cb-a888-4bdd9f5e0935 | -3.11491 | -53.25768 | 2024-11-28 05:18:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0a4bc1c0-5d06-3b92-9dfb-a23db6332ec5 | -3.78582 | -50.13919 | 2024-11-28 05:18:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4a92bc58-03ad-3b63-b7d4-cf84f2113f15 | -3.26913 | -51.2638 | 2024-11-28 05:18:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0cbe69a0-6027-330b-8ce1-564fb0f89e39 | -2.25954 | -53.7471 | 2024-11-28 05:18:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ca6a6c19-a569-3c2f-8e68-78ab5bd935b7 | -3.54339 | -50.4007 | 2024-11-28 05:18:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6ad71973-f69d-32a9-a0c3-8f970698c366 | -3.79179 | -50.13395 | 2024-11-28 05:18:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| cf1cef3b-1c4b-3078-a2c0-cafcd8d2d721 | -3.07779 | -48.6664 | 2024-11-28 05:18:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| d9bdb46c-d8b4-3d7f-8470-d9025df53b5b | -3.10216 | -53.25935 | 2024-11-28 05:18:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a280d10d-61f8-3533-875a-d3031e429ff3 | -3.09359 | -54.02155 | 2024-11-28 05:18:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9a48c2b8-9f8c-3cb3-bf83-5a68cadfbdd4 | -3.16715 | -51.09775 | 2024-11-28 05:18:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 007fcf21-4936-3377-835e-bc8d4893bc8b | -3.08747 | -49.21531 | 2024-11-28 05:18:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| dc73ef82-6cd7-3ed1-b129-401a772140d9 | -2.87568 | -53.94914 | 2024-11-28 05:18:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 7fbaae4f-20a7-33cb-b2c6-2c80b2a5a656 | -2.59416 | -53.97455 | 2024-11-28 05:18:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 38ae11e5-8da9-393d-9d04-85cbdd0b3268 | -2.1454 | -54.83259 | 2024-11-28 05:18:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 611d5bfe-f549-3b92-a9e4-c50b58db9349 | -2.9248 | -54.17317 | 2024-11-28 05:18:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| dff4d642-1894-3d62-8fb2-1a2d553ff216 | -3.10269 | -53.25571 | 2024-11-28 05:18:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 0cdfeb18-380f-39cf-a114-8611366f18ae | -3.08846 | -49.20851 | 2024-11-28 05:18:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 63b136fd-87ce-3064-ae8a-980b5050ba65 | -3.10295 | -50.36066 | 2024-11-28 05:18:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 882bdc2f-4736-305e-b452-2b4daf2ee88d | -3.5031 | -53.80524 | 2024-11-28 05:18:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 01e6e90a-6ea8-31f1-b59d-4f2ef13fb613 | -3.09603 | -54.03185 | 2024-11-28 05:18:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6fec13d4-f799-3f53-949a-da8e9ee147ac | -3.41543 | -50.15759 | 2024-11-28 05:18:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 183a09a5-a8a0-37d7-a039-523cea97cc66 | -2.77251 | -52.90593 | 2024-11-28 05:18:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c4ab01dd-6c02-3089-adea-270ed883a8d5 | -2.8883 | -53.97113 | 2024-11-28 05:18:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 70beef0c-2c45-396b-bf73-4aa7a3c43db0 | -2.93435 | -48.02515 | 2024-11-28 05:18:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 85ee4f5a-ebfc-3ff5-bb93-7dde6e564fa5 | -3.5016 | -53.81518 | 2024-11-28 05:18:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| f1e33b59-a648-35ed-8bc8-48aac5a4beb4 | -4.17905 | -48.45301 | 2024-11-28 05:18:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3398f990-0d0c-3564-bec2-28524429e13b | -2.06099 | -55.97115 | 2024-11-28 05:18:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 34ddb075-f76f-3b2c-9aff-eee04317af7e | -3.56976 | -52.28254 | 2024-11-28 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b76647c1-baad-3c50-909f-429dbaa555f2 | -3.34603 | -50.5214 | 2024-11-28 05:18:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| a8618892-2c0c-3d1c-b44b-42f41f539193 | -3.09865 | -50.36049 | 2024-11-28 05:18:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 90228f90-6d97-344f-83b8-54fc1b06ae6f | -2.62281 | -54.19702 | 2024-11-28 05:18:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e8673b1b-c67b-3326-89a9-47d599421ca7 | -3.50631 | -53.81075 | 2024-11-28 05:18:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| f5d24aa0-2885-342e-864c-917b4ebfdca9 | -3.96446 | -50.18776 | 2024-11-28 05:18:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| e61247bb-45b8-3f83-8804-55bb77f310f9 | -3.50393 | -50.32095 | 2024-11-28 05:18:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2be415a5-7061-31bf-9532-09f63d4d00c5 | -3.15581 | -50.14361 | 2024-11-28 05:18:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e0dd89cb-c42a-3b6a-aaa6-786a7b706d95 | -2.60576 | -53.97632 | 2024-11-28 05:18:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| ac7a9a58-b84c-3c56-9898-abf07147a1a4 | -3.12333 | -50.29581 | 2024-11-28 05:18:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b2437d49-3e65-3bfb-be52-a086d75eb91e | -2.84489 | -54.01237 | 2024-11-28 05:18:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| b05e508b-0839-3978-b785-3db0e158035f | -3.7084 | -51.80641 | 2024-11-28 05:18:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5f82c3f1-c1ac-3ca5-b0cd-966b3e851c80 | -3.40291 | -54.28581 | 2024-11-28 05:18:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bd5c43bc-fe01-32a6-81f9-8aaf4a9b27b8 | -2.86473 | -53.96089 | 2024-11-28 05:18:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| cb706cbb-ce94-3a99-8753-bebb26b77ab9 | -3.46209 | -50.53352 | 2024-11-28 05:18:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 74ce44d7-a948-3dcd-8098-ab4cf106f69f | -2.82238 | -54.48915 | 2024-11-28 05:18:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 307cdc6b-1be7-3d44-8d5a-2443685781ea | -6.44369 | -55.58532 | 2024-11-28 05:18:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |


[Clique aqui para ver as próximas entradas](README87.md)
