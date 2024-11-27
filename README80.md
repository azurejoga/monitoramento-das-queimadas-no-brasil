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

## Dados Diários - Página 80

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| fbc863fd-1fa6-3d1b-afae-ae04c87766d9 | -1.44559 | -52.5954 | 2024-11-27 06:01:00 | AQUA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 2f5e8ded-6c9f-3c83-a05b-96188fd225ff | -3.32737 | -53.72194 | 2024-11-27 06:01:00 | AQUA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| c96ee51a-8619-31c1-8ceb-83db5819ecc0 | -3.50279 | -50.49541 | 2024-11-27 06:01:00 | AQUA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 12.9 |
| 98f6781b-f9ce-31d3-9a22-130f630995bf | -2.80582 | -53.01578 | 2024-11-27 06:01:00 | AQUA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| a48a094b-5282-366d-90fb-4e338f973908 | -1.18975 | -51.76253 | 2024-11-27 06:01:00 | AQUA_M-M | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 7d64fe95-66e5-372a-a27e-49ae127c0464 | -3.50775 | -50.2985 | 2024-11-27 06:01:00 | AQUA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 865e04ef-87e1-3305-b092-af7366cc1852 | -1.66672 | -52.7164 | 2024-11-27 06:01:00 | AQUA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 18.3 |
| f04dfd2d-9a2b-32bd-9d6d-ac23df426f84 | -1.06492 | -52.41283 | 2024-11-27 06:01:00 | AQUA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| b6e3733f-5b27-3bb9-ac40-2491b4d217dc | -2.80192 | -52.91359 | 2024-11-27 06:01:00 | AQUA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 2fd4bdbb-5a07-3f75-ac11-f829a4ee6b37 | -1.69217 | -52.60786 | 2024-11-27 06:01:00 | AQUA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 3e2c9a5f-8a2f-3f32-b951-12eff5ef8991 | -1.19955 | -53.87761 | 2024-11-27 06:01:00 | AQUA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 16ba5d1a-4ba0-3da0-b0f5-8108d498a0ab | -1.66093 | -52.70993 | 2024-11-27 06:01:00 | AQUA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 6706550e-a471-3297-9fae-4efa68aadcc0 | -1.48582 | -52.51902 | 2024-11-27 06:01:00 | AQUA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 1cc6e201-3ba6-392e-9b59-0488f1e11537 | -2.87121 | -53.99809 | 2024-11-27 06:01:00 | AQUA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| ab33f6cb-bd74-3270-94b0-b7ebe7228e7f | -2.59933 | -53.96764 | 2024-11-27 06:01:00 | AQUA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 21.3 |
| a6e8ee18-c9cd-31c2-816e-1d218e9366e2 | -2.98014 | -53.8891 | 2024-11-27 06:01:00 | AQUA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| fd9da8de-138a-32ae-b3f5-c588d3e07e71 | -3.59201 | -50.34855 | 2024-11-27 06:01:00 | AQUA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 23.6 |
| 2a42c681-0c66-3a24-815d-25ab54b3e00b | -2.97627 | -53.34743 | 2024-11-27 06:01:00 | AQUA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 952e2e15-c2b9-3235-8c9a-36d69cb62dfa | -2.8994 | -54.1776 | 2024-11-27 06:01:00 | AQUA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| d890ac5e-0c27-370c-809e-9f69f66cd203 | -4.22188 | -48.65192 | 2024-11-27 06:01:00 | AQUA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 28.2 |
| e235694a-a311-36ba-8050-ec63b4d62a1e | -1.78365 | -52.73998 | 2024-11-27 06:01:00 | AQUA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 11.0 |
| e2c6156f-1524-3729-9f85-b40f570388f5 | -3.69198 | -50.21113 | 2024-11-27 06:01:00 | AQUA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 13.4 |
| e8e1b449-10ea-32c7-a254-6e70b5352bf1 | -3.09114 | -53.2613 | 2024-11-27 06:01:00 | AQUA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 36.5 |
| 1ffdf1b2-9ce6-3e46-b7a0-18b82a1a4733 | -2.2489 | -53.46334 | 2024-11-27 06:01:00 | AQUA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 952fa661-7e27-3aa5-8c2c-e408cdc9d980 | -1.76508 | -53.61707 | 2024-11-27 06:01:00 | AQUA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| f0c21428-8322-3592-a4d1-eeb254bad58d | -2.263 | -53.74513 | 2024-11-27 06:01:00 | AQUA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 413c20c1-cc95-3cc7-9327-7f0fef32bfe4 | -1.66817 | -52.70646 | 2024-11-27 06:01:00 | AQUA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 974cd18f-c046-32cb-a5ff-faad4de56967 | -1.79448 | -52.7314 | 2024-11-27 06:01:00 | AQUA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| ef048984-cbee-3d38-b1e0-d82f4ab45820 | -1.15624 | -53.67855 | 2024-11-27 06:01:00 | AQUA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 969f75dc-4134-3a5d-a33b-d58ef084de55 | -3.05917 | -53.28633 | 2024-11-27 06:01:00 | AQUA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| a4a6ef61-aa33-3aa7-a327-3fd088587a50 | -1.06344 | -52.42296 | 2024-11-27 06:01:00 | AQUA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| c688e5f9-d9a6-335c-a279-3c9c70b241d3 | -3.12342 | -53.10628 | 2024-11-27 06:01:00 | AQUA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 69cbfe95-0480-3aa7-967e-2e1d12785665 | -1.98883 | -53.29145 | 2024-11-27 06:01:00 | AQUA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 13.4 |
| 49134c24-3ed5-31ca-80a1-18985f8349ad | -3.49931 | -53.80707 | 2024-11-27 06:01:00 | AQUA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 14.1 |
| 84f91951-e3af-37a6-af3e-70e666422ba2 | -1.37076 | -52.12082 | 2024-11-27 06:01:00 | AQUA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| c4dda63d-019e-3036-8452-7d821bc5c497 | -1.27239 | -52.16444 | 2024-11-27 06:01:00 | AQUA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| fc28d3fe-dc50-395a-afbf-7b1bcfe84861 | -3.1836 | -48.41298 | 2024-11-27 06:01:00 | AQUA_M-M | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 12.5 |
| 83f2ad37-107f-3a90-be06-0a154dbbaa32 | -1.20122 | -51.75289 | 2024-11-27 06:01:00 | AQUA_M-M | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| f655243b-82e6-3dd4-bdc7-e9ade75d4e75 | -2.25392 | -53.6159 | 2024-11-27 06:01:00 | AQUA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 331132a5-efcf-3de7-af7f-f0bf2590e07e | -2.80425 | -54.13885 | 2024-11-27 06:01:00 | AQUA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 16edea75-cbe9-308b-874a-1ec00d1a3e1b | -2.26165 | -53.75429 | 2024-11-27 06:01:00 | AQUA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| f14d59e4-b6e3-335c-b2ee-637f15fb46dc | -1.63589 | -52.49083 | 2024-11-27 06:01:00 | AQUA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 329914ed-2525-30f2-96f4-76a4b777ba60 | -1.44707 | -52.58543 | 2024-11-27 06:01:00 | AQUA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 965a2a3a-a710-3275-be62-841ef9096f16 | -3.68978 | -50.22688 | 2024-11-27 06:01:00 | AQUA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 24.9 |
| 2ff98615-91e7-3b4e-bd0b-4b2fe1d9a1ab | -2.24349 | -53.62384 | 2024-11-27 06:01:00 | AQUA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 44d11697-bdc7-3882-ad4a-e91489634b87 | -1.79301 | -52.74133 | 2024-11-27 06:01:00 | AQUA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 19.0 |
| 78d45db9-3d5d-3fe0-b993-1c1c8c6ac223 | -2.8582 | -53.96171 | 2024-11-27 06:01:00 | AQUA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 9ef6af0a-af55-3a1a-b538-3a2dd512479a | -1.66527 | -52.72633 | 2024-11-27 06:01:00 | AQUA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 6939461a-3f10-3d6d-ada5-421d5706248b | -2.80288 | -53.0355 | 2024-11-27 06:01:00 | AQUA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 2a41402d-fb76-3561-b1dd-374e9cd11de3 | -3.096 | -50.36322 | 2024-11-27 06:01:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 16.1 |
| 518db873-c258-3ab4-b935-a71ff821744c | -1.48431 | -52.52912 | 2024-11-27 06:01:00 | AQUA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| ab436d3d-e86c-3831-bb49-96a1298cc031 | -3.58989 | -50.36359 | 2024-11-27 06:01:00 | AQUA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 14.6 |
| 2089dc3d-11d1-323e-b689-996410785d9e | -1.0596 | -52.4157 | 2024-11-27 06:01:00 | AQUA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| f3d628c5-75a5-32e1-b7f4-a1f1c0656242 | -3.71941 | -50.18334 | 2024-11-27 06:01:00 | AQUA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 5a893c70-1860-34f8-acb4-bc5300222242 | -2.59896 | -54.21598 | 2024-11-27 06:01:00 | AQUA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 15.5 |
| c1f34412-2d99-38be-b12d-0eca0865a57e | -2.77524 | -52.89957 | 2024-11-27 06:01:00 | AQUA_M-M | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| eb4d6291-4123-36e6-865d-5d10c8e9adfa | -2.18555 | -53.76542 | 2024-11-27 06:01:00 | AQUA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 06a8b504-069c-3daf-afd5-de5d70585191 | -3.69196 | -50.22189 | 2024-11-27 06:01:00 | AQUA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 33.9 |
| 340c0f5f-f053-31b3-a396-53f5e1cb3991 | -2.83376 | -54.12473 | 2024-11-27 06:01:00 | AQUA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 45.4 |
| f3325531-f906-3d14-ac80-8e634afd984f | -3.09181 | -54.12579 | 2024-11-27 06:01:00 | AQUA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| a31de082-5897-3f4a-8147-f17f1523b871 | -3.49794 | -53.8163 | 2024-11-27 06:01:00 | AQUA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 0a6d1dc6-273a-3dd5-ac6d-0be11f3d7028 | -2.59799 | -53.97671 | 2024-11-27 06:01:00 | AQUA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| ecf74632-23bd-3530-ace0-7c657281befa | -2.85411 | -53.989 | 2024-11-27 06:01:00 | AQUA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 62133b94-e75a-36db-8d92-a55073933f06 | -4.21892 | -48.6731 | 2024-11-27 06:01:00 | AQUA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 15.2 |
| cc0d19ac-559e-3341-93e7-54ca2aeeb0e8 | -2.60877 | -54.27216 | 2024-11-27 06:01:00 | AQUA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 39881d76-442f-375b-98c4-2430ee9b218f | -3.09817 | -50.34845 | 2024-11-27 06:01:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| b78b1070-3867-35a2-8460-13384bc3436b | -2.54824 | -54.05589 | 2024-11-27 06:01:00 | AQUA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 2a0929c2-7c3c-3c3d-8c1b-b8963aca53d0 | -3.24307 | -50.13415 | 2024-11-27 06:01:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 9871450f-3f99-3ecd-b68f-d298528a8433 | -3.16737 | -48.43217 | 2024-11-27 06:01:00 | AQUA_M-M | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 111.5 |
| ada96baa-488c-3504-bc5f-05949032f721 | -3.08285 | -54.12452 | 2024-11-27 06:01:00 | AQUA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 10.5 |
| bc7e1090-01bf-3d6b-8506-d0824fd03576 | -2.1842 | -53.77456 | 2024-11-27 06:01:00 | AQUA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 58.9 |
| c196b8c6-a1dd-33ba-bdc5-4df4b117fef1 | -2.6155 | -52.53147 | 2024-11-27 06:01:00 | AQUA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| b5629eea-d218-3eea-82ae-dfefdcda0d40 | -2.90074 | -54.16861 | 2024-11-27 06:01:00 | AQUA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 4e24afbc-a952-3f78-be30-bbf105d164c6 | -1.06065 | -53.20132 | 2024-11-27 06:01:00 | AQUA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 610ec13e-b73f-3beb-b2c0-185ac0903b07 | -3.97145 | -48.08065 | 2024-11-27 06:01:00 | AQUA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 64.3 |
| 49648d11-4ee3-3f45-8259-e6a27241fd13 | -3.71419 | -51.79895 | 2024-11-27 06:01:00 | AQUA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 13.3 |
| d37de804-4fca-3f4d-8407-601ee056c575 | -1.31591 | -51.74109 | 2024-11-27 06:01:00 | AQUA_M-M | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 2273169f-8c31-35ba-a26b-0e4810fc66b5 | -2.82752 | -54.1054 | 2024-11-27 06:01:00 | AQUA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| ede9b7b5-c56f-35d6-9c95-e4839eb8b761 | -1.76371 | -53.62624 | 2024-11-27 06:01:00 | AQUA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| dc2cb589-326e-3894-99a2-31c0d4547771 | -1.72136 | -53.60143 | 2024-11-27 06:01:00 | AQUA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 32e3afd7-f4fb-367d-bdf3-2d7369ee04ec | -3.10182 | -53.25292 | 2024-11-27 06:01:00 | AQUA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 93.6 |
| 43630ede-0c98-36ef-8663-42837b5c8008 | -2.8959 | -53.95517 | 2024-11-27 06:01:00 | AQUA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 5daed243-8049-3d95-ba31-da5df05fca8e | -3.96461 | -48.07451 | 2024-11-27 06:01:00 | AQUA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 69.2 |
| e2fc4b47-1736-37c6-8237-aedbf4c0a68d | -3.09257 | -53.25156 | 2024-11-27 06:01:00 | AQUA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 155.2 |
| ad12ed56-c457-3ca7-aa44-56b2f82d9382 | -2.73558 | -54.15985 | 2024-11-27 06:01:00 | AQUA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| b50b289a-b1d6-38f3-ab6a-f1721222073f | -3.05222 | -53.27968 | 2024-11-27 06:01:00 | AQUA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 15.9 |
| c0a08f81-be88-3ac7-a8a7-e62291c31082 | -2.80341 | -52.90358 | 2024-11-27 06:01:00 | AQUA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| dee567f8-c86c-367b-9a5b-a6f1a166f587 | -0.99142 | -51.72145 | 2024-11-27 06:01:00 | AQUA_M-M | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 4b1e59b7-6b31-320f-a076-8c22cb1e5fd9 | -3.70399 | -51.79757 | 2024-11-27 06:01:00 | AQUA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 1cd6febe-4e8e-38db-9e46-dc6e3a0759ff | -2.83511 | -54.11571 | 2024-11-27 06:01:00 | AQUA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 81.3 |
| a5b14dc8-0fb7-39a9-aed0-08eb15a41344 | -2.25264 | -53.75299 | 2024-11-27 06:01:00 | AQUA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 3ae281f1-de86-3b13-9dc8-7da691bcfe38 | -5.98087 | -45.33261 | 2024-11-27 06:01:00 | AQUA_M-M | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 48.1 |
| 7b371757-ef19-3f5a-acd9-6e2c6a72782f | -2.60031 | -54.20697 | 2024-11-27 06:01:00 | AQUA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 41.2 |
| ec3afb1d-6ea1-3454-86a4-ac000766d3da | -1.62539 | -53.86969 | 2024-11-27 06:01:00 | AQUA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 0413fc78-26ee-38ec-bf4c-f4e0bc25f53f | -3.24422 | -50.14299 | 2024-11-27 06:01:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 580900dc-75a3-31a1-90d7-b835a0872c73 | -2.59383 | -51.82711 | 2024-11-27 06:01:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| f5f5772b-3837-3700-a4d3-4b34f6a90b1e | -3.03795 | -48.51317 | 2024-11-27 06:01:00 | AQUA_M-M | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 30.0 |
| 2e95c7ab-58c3-35f2-8584-806ad68f989c | -3.18057 | -48.43402 | 2024-11-27 06:01:00 | AQUA_M-M | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 42.2 |
| b4b02b5e-05f0-3059-b82c-71829b563d46 | -3.60338 | -50.35013 | 2024-11-27 06:01:00 | AQUA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| b1f3e3b8-a606-34bb-8570-bb452e139f3c | -2.258 | -53.46465 | 2024-11-27 06:01:00 | AQUA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |


[Clique aqui para ver as próximas entradas](README81.md)
