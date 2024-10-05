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

## Dados Diários - Página 134

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2815b231-6a04-32be-9e44-091cd880bb36 | -7.13838 | -59.30165 | 2024-10-05 05:29:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 5a3c36e5-5cfc-3256-b0f5-fbc18fadc02c | -7.13709 | -59.31562 | 2024-10-05 05:29:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 20018fd0-735d-3320-b618-17a6ad6e133b | -7.13657 | -59.31393 | 2024-10-05 05:29:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b3d7eeab-3dc0-31bd-a1b4-93ecf74a1623 | -7.13602 | -59.29876 | 2024-10-05 05:29:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 20da9eb2-17f3-37c5-84e3-5d05eb5d94c3 | -7.13597 | -59.31798 | 2024-10-05 05:29:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 100f6645-ebc5-32aa-8d13-1316f7be1032 | -7.13541 | -59.29701 | 2024-10-05 05:29:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f054e5fe-feb4-33bb-ae22-75fcd6398116 | -7.1354 | -59.30285 | 2024-10-05 05:29:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| f6e723ad-ec2d-3185-a82c-0e25f445abb2 | -7.13481 | -59.3011 | 2024-10-05 05:29:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ed6fb6ec-9c5b-3464-a874-2c1d7d4f6cd0 | -7.13058 | -59.31047 | 2024-10-05 05:29:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a9d6fcd1-8399-3282-a9cb-eb6e261c00b3 | -7.06709 | -59.27152 | 2024-10-05 05:29:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8bdfaa79-86a1-3ccf-b037-88ed19b60a24 | -7.06352 | -59.27095 | 2024-10-05 05:29:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e4b9d1a6-404c-3248-9250-126a435e4244 | -7.06282 | -59.30012 | 2024-10-05 05:29:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e18d55b7-ba39-39ca-9f39-184c27824962 | -7.06055 | -59.26633 | 2024-10-05 05:29:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 51c04d0e-9c7e-3798-8261-3ffad98e3034 | -7.05995 | -59.27042 | 2024-10-05 05:29:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 828d53d3-4c80-3cf2-9c61-5da8841aeb7b | -7.05926 | -59.29957 | 2024-10-05 05:29:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0a53cfc0-65d5-3450-9805-00fc6f522ff3 | -7.05865 | -59.30365 | 2024-10-05 05:29:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e051ab40-b6a6-3d36-86bf-8992132399df | -7.05638 | -59.26986 | 2024-10-05 05:29:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e105220e-df79-3b2a-901a-70d4d44b61cc | -7.05569 | -59.29903 | 2024-10-05 05:29:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 81a46cea-a433-3855-8706-2c5f9c8ad875 | -7.05508 | -59.30311 | 2024-10-05 05:29:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c6ae6132-63ba-33a1-beb2-c40089327317 | -7.0541 | -59.23592 | 2024-10-05 05:29:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3508f05d-d27d-39b6-9ecd-bd0d3a5cb5ee | -7.05052 | -59.23537 | 2024-10-05 05:29:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b18d617a-f568-312e-bc73-6b310e0b84d4 | -7.04735 | -59.30608 | 2024-10-05 05:29:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4502f50c-b78e-324f-9d91-3558e6633448 | -7.02285 | -59.39772 | 2024-10-05 05:29:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 452bc1d9-79fc-3d8b-8efe-182490e1a3c6 | -7.02225 | -59.40173 | 2024-10-05 05:29:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c070f7d5-a5f8-3caa-9735-00f2e3e06cf2 | -7.02166 | -59.40575 | 2024-10-05 05:29:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c7df8b47-d3e1-304a-9c58-b8d0e17d055d | -7.02094 | -59.36502 | 2024-10-05 05:29:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a708892f-583b-3f03-bf3a-bd72ed32c293 | -7.02053 | -59.36431 | 2024-10-05 05:29:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cdc20967-ea45-3c53-87a4-b181a60fc6e4 | -7.0193 | -59.39717 | 2024-10-05 05:29:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c33f1e46-1871-3230-9a83-683c8b00f51c | -7.0187 | -59.40118 | 2024-10-05 05:29:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 81c5db45-af74-384f-9954-1f30f3d1e944 | -7.01811 | -59.40521 | 2024-10-05 05:29:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 5fb39e7a-37df-3b33-8a76-c2656bc9d7e3 | -7.01785 | -59.38521 | 2024-10-05 05:29:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5cc292c2-ef0f-353b-ae69-ac282cf72d75 | -7.01754 | -59.38453 | 2024-10-05 05:29:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8729012e-7a42-325b-b475-562248a813ba | -7.01739 | -59.36446 | 2024-10-05 05:29:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d984e2dd-6a83-3c12-8ac2-aef814e4846d | -7.01697 | -59.36375 | 2024-10-05 05:29:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5011205b-cc11-343b-9635-eb3eb52da4d9 | -7.01694 | -59.38858 | 2024-10-05 05:29:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 236c77cd-5d5d-35c2-8749-a3b9f673bc73 | -7.01538 | -59.40129 | 2024-10-05 05:29:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b19441d7-9621-3df1-8c89-813c74d5a282 | -7.01516 | -59.40065 | 2024-10-05 05:29:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9212ef75-6cea-3a5b-be81-0585c0561f80 | -7.01492 | -59.38061 | 2024-10-05 05:29:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9248ba08-0988-3189-8f68-3f7a7978166c | -7.01459 | -59.37992 | 2024-10-05 05:29:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c66de7cb-6db8-3823-a591-9f5c67d40fdc | -7.01456 | -59.40466 | 2024-10-05 05:29:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d576ea5a-2170-3e1c-90cc-b17cb9acde79 | -7.0143 | -59.38467 | 2024-10-05 05:29:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a5ca4918-f332-3c6e-936e-61ba23461bca | -7.01399 | -59.38399 | 2024-10-05 05:29:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 21d36f27-ad24-3ac9-b05f-36134ae972e3 | -7.01368 | -59.38871 | 2024-10-05 05:29:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0dba6d2a-d14c-329a-8b3c-bfce2c8bb047 | -7.01339 | -59.38804 | 2024-10-05 05:29:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6f5dfee2-ac2c-3c41-a5cf-92f87d42d3b1 | -7.01184 | -59.40074 | 2024-10-05 05:29:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d5292875-5527-3df7-9bc6-bb2bbb2f5fe6 | -7.01161 | -59.4001 | 2024-10-05 05:29:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3896dc8b-2cb2-3583-9694-1dabb907e905 | -7.01137 | -59.38007 | 2024-10-05 05:29:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3c714962-bce3-3978-845f-5369abaea073 | -7.01075 | -59.38412 | 2024-10-05 05:29:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 76f0f43f-c741-3565-8348-6a9e2448af7f | -7.00782 | -59.37953 | 2024-10-05 05:29:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9acf14ca-623d-3498-b7c1-35d13ccf04e1 | -7.0072 | -59.38358 | 2024-10-05 05:29:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d7d6d8f0-5c46-3216-abc7-3c598d9b0b1e | -7.00658 | -59.38761 | 2024-10-05 05:29:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 53114317-dabe-3b04-b530-e212370f7684 | -6.95302 | -59.89025 | 2024-10-05 05:29:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ba9a2a30-71a0-387d-8c5f-e164ff451067 | -6.95245 | -59.8941 | 2024-10-05 05:29:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e67324c1-2a47-371e-b5fe-bbaf16f7c9de | -6.91715 | -59.45204 | 2024-10-05 05:29:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 42e0832f-0b4e-3a35-bb14-7dd89e6346c3 | -6.91421 | -59.44748 | 2024-10-05 05:29:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 185357d0-aba6-3d7f-8c76-bc68283bea45 | -6.91361 | -59.45148 | 2024-10-05 05:29:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b5d9a93c-def4-329a-8c7c-8237a71923ab | -6.87804 | -59.92606 | 2024-10-05 05:29:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 625e1dff-6d7a-3cda-aefd-84c809d045f5 | -6.79256 | -59.36589 | 2024-10-05 05:29:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d1b624f4-9f21-3667-a865-847b52fa4ccf | -6.78962 | -59.36137 | 2024-10-05 05:29:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d4c6be37-d764-36aa-808b-34d373cfbb69 | -6.78901 | -59.36539 | 2024-10-05 05:29:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4d586e1a-c9db-346f-afab-5d6a2bfa584a | -6.71078 | -60.10283 | 2024-10-05 05:29:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 71b46465-96c6-3681-9675-3de520ebc383 | -6.71021 | -60.10656 | 2024-10-05 05:29:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| afab4080-87ec-39a4-aa56-f734f34dbcdc | -6.70735 | -60.10229 | 2024-10-05 05:29:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ea0a1204-41d3-37fb-8985-043c29bb248e | -6.68201 | -59.47568 | 2024-10-05 05:29:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b49a248d-b42c-3235-b18d-26472dee403e | -6.64859 | -60.05146 | 2024-10-05 05:29:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| bf496a18-e970-3a4c-ae1d-60330a648e2d | -6.6463 | -60.04341 | 2024-10-05 05:29:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a4f130ff-3ea5-3eb7-99fb-be638987f71a | -6.64573 | -60.04716 | 2024-10-05 05:29:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4798c49b-8a14-3c7a-9975-b926245128d1 | -6.64287 | -60.04287 | 2024-10-05 05:29:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 848511c4-6c74-307b-814d-937a249522e8 | -6.64229 | -60.04663 | 2024-10-05 05:29:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3960ab9f-63f5-327d-bb5b-8f13a4256565 | -3.0765 | -61.06798 | 2024-10-05 05:29:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3e2981cd-fbcf-3172-9916-dbc2f73f1c89 | -3.24022 | -60.65185 | 2024-10-05 05:29:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6a7f227a-769e-3414-9798-7febbb2032f8 | -2.95489 | -60.01531 | 2024-10-05 05:29:00 | NOAA-21 | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 01f326da-7818-3733-aca5-726253fc9d22 | -3.78196 | -60.12006 | 2024-10-05 05:29:00 | NOAA-21 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1ace0c56-f383-3ab5-85f6-0f4fe02d3804 | -3.78141 | -60.12363 | 2024-10-05 05:29:00 | NOAA-21 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 12c92d4d-8ac2-3c45-8b11-5c9926d357f0 | -5.87478 | -61.25573 | 2024-10-05 05:29:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d3608964-e464-3309-aed6-64a366e900ea | -5.83146 | -61.2276 | 2024-10-05 05:29:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 36c52bbc-e35b-3b72-ab48-81972153d2b7 | -5.76131 | -61.54689 | 2024-10-05 05:29:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3ba295d9-03c7-3e07-9afc-c961369b2770 | -7.96677 | -61.53947 | 2024-10-05 05:29:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 955de109-a887-3651-b421-5356a5fe3580 | -7.93025 | -61.5554 | 2024-10-05 05:29:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| bcfc6630-9a9a-3ab3-a7f0-c516017a6d22 | -7.92692 | -61.55488 | 2024-10-05 05:29:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b8e04038-398c-3418-9ea4-1711fd00fea2 | -7.89353 | -61.4634 | 2024-10-05 05:29:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 5471da38-6996-3c8a-beeb-11628cea8430 | -7.89299 | -61.46692 | 2024-10-05 05:29:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 6df28d33-805f-3bb8-98cb-49c80f8013ac | -7.8902 | -61.46287 | 2024-10-05 05:29:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 7.2 |
| f8d7a51d-3dba-3226-ae4e-34c5ea14b92f | -7.88966 | -61.4664 | 2024-10-05 05:29:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| f14826c3-3f5e-317b-8ec2-5ecaa85085d7 | -7.28155 | -61.08916 | 2024-10-05 05:29:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| e14e2e80-91b7-36ea-8f79-9c28940f3662 | -7.281 | -61.09272 | 2024-10-05 05:29:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| a58d9ba6-5e88-3c59-b570-be992feba1fb | -7.27821 | -61.08865 | 2024-10-05 05:29:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9eebe0df-41e8-3dfd-98af-f7c4e239e02d | -7.27766 | -61.09221 | 2024-10-05 05:29:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 118a1103-0cb2-36d1-8530-c5328286889d | -8.84416 | -61.49496 | 2024-10-05 05:29:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7eb27197-079c-3fe3-857e-3b2066d3ffaf | -8.84082 | -61.49443 | 2024-10-05 05:29:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 5d33356f-170e-35cd-b4be-7024186d6e31 | -8.66817 | -62.1054 | 2024-10-05 05:29:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 64f0e08f-ac91-3463-8e0b-27c582b83e99 | -8.60393 | -62.40511 | 2024-10-05 05:29:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3f816bfa-7cf2-3c4e-8ae3-dd9763ab4a18 | -8.60339 | -62.40857 | 2024-10-05 05:29:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ea381f27-e312-3ca2-ab52-8515a48da817 | -8.60009 | -62.40805 | 2024-10-05 05:29:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ec4cfccc-1a92-3e9e-bf73-a8a910de0ea9 | -8.56066 | -62.48706 | 2024-10-05 05:29:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2eb0eb54-c0c2-3fcd-8ea1-a89fd6bd511c | -8.55736 | -62.48654 | 2024-10-05 05:29:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ceb91485-e475-386d-90a7-11815189b1b4 | -8.22747 | -61.2167 | 2024-10-05 05:29:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.4 |
| d114929d-00e1-3f5f-9f39-a93c34fd96c5 | -8.22692 | -61.22028 | 2024-10-05 05:29:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9c25943a-f318-31f3-8fd8-4eca374438e0 | -8.22636 | -61.22386 | 2024-10-05 05:29:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c12c6f6f-8f91-3709-8228-a9e77911418a | -8.22467 | -61.21259 | 2024-10-05 05:29:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |


[Clique aqui para ver as próximas entradas](README135.md)
