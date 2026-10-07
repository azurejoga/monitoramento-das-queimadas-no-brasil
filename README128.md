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

## Dados Diários - Página 128

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a6f7c6b9-8c47-3fdc-a45d-3fa0ee21b1f4 | -10.9953 | -45.4068 | 2026-10-07 13:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 82.6 |
| 8ef303c7-b08d-3848-8955-87bd987f6d83 | -10.4682 | -39.4318 | 2026-10-07 13:00:00 | GOES-19 | MONTE SANTO | BAHIA | Brasil | 2921500 | 29 | 33 | nan | nan | nan | Caatinga | 149.5 |
| 9b3cf3ea-a2d4-3370-9d2d-fc842e374df0 | 1.7671 | -55.5661 | 2026-10-07 13:00:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 71.4 |
| 4799c14e-047b-3711-8803-05b77690f107 | -10.3738 | -46.2146 | 2026-10-07 13:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 97.6 |
| 7b2b8139-4783-36e9-a523-8448a9302dee | -11.3742 | -46.7173 | 2026-10-07 13:00:00 | GOES-19 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 100.2 |
| 0eee56af-0a52-3af2-b28a-e6e3313b9027 | -7.8679 | -44.1922 | 2026-10-07 13:00:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 89.8 |
| 964cfccf-b9a3-36ea-b558-5dbba33305b7 | -11.7943 | -46.7056 | 2026-10-07 13:00:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 193.8 |
| 39aa2e43-b105-3df6-9c2a-b5307dd1db6d | -11.0867 | -45.6459 | 2026-10-07 13:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 171.0 |
| 9fb78a2d-0997-324a-a65e-9fcb4a6efac9 | -7.8676 | -44.2153 | 2026-10-07 13:00:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 158.9 |
| 0e617e6d-0b7d-33cd-bc75-aa9998bac7e3 | -7.7595 | -43.8092 | 2026-10-07 13:00:00 | GOES-19 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Caatinga | 161.4 |
| ec3de3cd-5471-3d19-834d-6919539de5ba | -11.7755 | -46.6856 | 2026-10-07 13:00:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 131.0 |
| ded207a5-4495-37bc-9ef5-425802713318 | -7.7592 | -43.8325 | 2026-10-07 13:00:00 | GOES-19 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 83.2 |
| 55bf68e5-e1a4-38c1-9d6e-139d89e59f03 | -17.5069 | -45.4666 | 2026-10-07 13:00:00 | GOES-19 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 131.4 |
| 04c4cfb0-0227-39a9-9488-736c7ec9b6bb | -7.8865 | -44.2134 | 2026-10-07 13:00:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 102.0 |
| 21c352ca-f193-3cb7-9141-22868cb4e9f9 | -11.3745 | -46.6948 | 2026-10-07 13:00:00 | GOES-19 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 110.0 |
| 8988e98b-af29-3846-8a27-43d982cf1a3a | -9.4317 | -45.8519 | 2026-10-07 13:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 149.7 |
| a819f968-b33c-3f32-a62d-6fb8f884170e | -11.0863 | -45.6688 | 2026-10-07 13:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 116.2 |
| b71a9249-eac7-3711-b101-0e844371fff8 | -7.8789 | -72.3492 | 2026-10-07 13:00:00 | GOES-19 | CRUZEIRO DO SUL | ACRE | Brasil | 1200203 | 12 | 33 | nan | nan | nan | Amazônia | 98.8 |
| a2e8ee13-6561-3032-90c7-1fd80475c567 | -10.3735 | -46.2372 | 2026-10-07 13:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 95.8 |
| 197b6516-7dfb-36ae-aa38-d5798363bbd3 | -8.5356 | -55.383 | 2026-10-07 13:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 98.3 |
| 948d903a-b562-3559-81ed-4846a90f49cd | -11.7751 | -46.7082 | 2026-10-07 13:00:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 134.3 |
| a2ff19a9-fd27-32af-8152-11d46416d5c7 | -9.432 | -45.8293 | 2026-10-07 13:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 300.9 |
| c971249f-1219-3e0c-9871-9ff014eb1cf9 | -11.1051 | -45.689 | 2026-10-07 13:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 138.5 |
| 3059e617-cf39-39b2-9a2d-d9afd7b9bbb1 | -8.5358 | -55.3629 | 2026-10-07 13:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 77.1 |
| d7c35cdf-30e2-387a-8e91-5f46333a8bd4 | 1.7121 | -55.6063 | 2026-10-07 13:10:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 76.7 |
| 1f4e2916-3673-3bda-966d-1e130894049d | -11.0642 | -45.854 | 2026-10-07 13:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 182.4 |
| 137636c4-1c46-3f7e-ae24-5082a871c259 | -11.3742 | -46.7173 | 2026-10-07 13:10:00 | GOES-19 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 122.3 |
| 1b0c3cd8-75d1-371f-983e-ea677dec0ddb | -8.5356 | -55.383 | 2026-10-07 13:10:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 87.3 |
| 80cb2443-6fbd-3b07-ac24-59f0e2d186a8 | 1.7121 | -55.6261 | 2026-10-07 13:10:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 61.0 |
| 56aba31b-a839-3040-af2a-48ada42c5bb6 | -11.7947 | -46.683 | 2026-10-07 13:10:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 101.9 |
| c74d9fe4-929b-320a-8e89-7cd232df7f48 | -8.5051 | -54.6202 | 2026-10-07 13:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 256.5 |
| 27a172de-dfda-3d76-bbd3-6e72a2a88c9f | -7.1814 | -55.1036 | 2026-10-07 13:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 63.8 |
| 018c2bdf-8d31-3411-aa00-71dc1873026d | -7.1813 | -55.1237 | 2026-10-07 13:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 74.9 |
| 9a21c5a5-851a-3d14-ab1d-a35267bfa6b2 | -7.7595 | -43.8092 | 2026-10-07 13:10:00 | GOES-19 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Caatinga | 181.0 |
| 2b4de3a0-5a39-3847-9567-4390aae48d1c | -6.4413 | -55.0224 | 2026-10-07 13:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 95.7 |
| 080cbbce-f67d-32b3-9b21-9d7d3fed9c13 | -8.5238 | -54.619 | 2026-10-07 13:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 77.7 |
| a7212137-6018-3e7e-859a-e99d7ff55004 | -11.3937 | -46.6922 | 2026-10-07 13:10:00 | GOES-19 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 86.2 |
| 2964b922-092f-32b4-ae5d-f6703663f706 | -11.0459 | -45.8109 | 2026-10-07 13:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 156.9 |
| c9082d69-b753-3c7c-9c6f-40899bdce3fe | -7.721 | -45.4645 | 2026-10-07 13:10:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 87.4 |
| ba448fb1-e097-375b-aa13-06810b61a784 | -9.432 | -45.8293 | 2026-10-07 13:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 144.4 |
| 26b9033f-803d-3061-8791-e2a0f0f8fa92 | -11.7335 | -43.649 | 2026-10-07 13:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 93.4 |
| f10131ab-246c-3348-b8da-2d3cf5e710e1 | 1.7671 | -55.5661 | 2026-10-07 13:10:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 79.2 |
| c2a6c4ee-5572-36bf-8eab-be785a061c69 | -7.7213 | -45.4418 | 2026-10-07 13:10:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 103.2 |
| c187425b-2253-3e1e-9e88-d13d336ae7e7 | -11.7943 | -46.7056 | 2026-10-07 13:10:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 90.7 |
| 47067be8-a60d-374c-8885-c0e6464e467c | -7.8146 | -45.5009 | 2026-10-07 13:10:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 67.8 |
| 980bcd27-c96f-36d6-82a4-2781d020d01c | -7.7592 | -43.8325 | 2026-10-07 13:10:00 | GOES-19 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 71.3 |
| dfc734ed-4911-35bf-a029-875736e260a4 | -7.7399 | -45.4627 | 2026-10-07 13:10:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 53.4 |
| 5bcca885-0b82-3ada-967e-78c5089699df | -10.8591 | -50.6692 | 2026-10-07 13:10:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 64.9 |
| 3d5c3be6-3db4-38ee-a7d8-e0a715ca0c4e | -7.8676 | -44.2153 | 2026-10-07 13:10:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 202.6 |
| d7d782f4-25e2-39e7-98e9-f2bddacdfdde | -7.5756 | -46.7112 | 2026-10-07 13:10:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 83.8 |
| 84681a88-977e-3821-be43-75d47060c158 | -7.8789 | -72.3492 | 2026-10-07 13:10:00 | GOES-19 | CRUZEIRO DO SUL | ACRE | Brasil | 1200203 | 12 | 33 | nan | nan | nan | Amazônia | 100.2 |
| 089d9525-c759-3605-9684-a67f866a87f3 | -9.4317 | -45.8519 | 2026-10-07 13:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 122.3 |
| 841d9553-3a50-31f1-bd47-17375de03cab | -10.4682 | -39.4318 | 2026-10-07 13:10:00 | GOES-19 | MONTE SANTO | BAHIA | Brasil | 2921500 | 29 | 33 | nan | nan | nan | Caatinga | 121.5 |
| 25f1bc5a-1b5e-3ed9-9a30-33058c9990c9 | -7.8679 | -44.1922 | 2026-10-07 13:10:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 104.2 |
| 9f8a7c4e-38cc-3664-9595-882b95acaf5a | -11.1051 | -45.689 | 2026-10-07 13:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 133.1 |
| 76f114f8-4729-36ba-bdca-1e71fdff76a8 | -7.2 | -55.1026 | 2026-10-07 13:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 70.7 |
| e1e96151-58df-3f0d-969b-cbcf176d4e14 | -7.8865 | -44.2134 | 2026-10-07 13:10:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 85.6 |
| cd01f550-398d-326d-8f35-9d9f2a4dee11 | -11.0867 | -45.6459 | 2026-10-07 13:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 114.0 |
| c5ed556c-f700-3cd9-9cef-c3ae2ee22d33 | -11.3745 | -46.6948 | 2026-10-07 13:10:00 | GOES-19 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 128.2 |
| cc27687a-24cb-39ee-8f4b-239f2c47855b | -5.73 | -45.18 | 2026-10-07 13:15:00 | MSG-03 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 81e538ab-7f93-3024-a4ef-baaadc8dfe91 | -5.97 | -40.97 | 2026-10-07 13:15:00 | MSG-03 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| cf04f965-1205-3f1f-83e5-767da25f2992 | -5.73 | -45.14 | 2026-10-07 13:15:00 | MSG-03 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 25ec39cb-f98b-3b58-9aaf-d294c8ae71bf | -5.97 | -40.93 | 2026-10-07 13:15:00 | MSG-03 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 8a306940-283a-3fa2-82de-2e924c4dfe12 | -6.22 | -52.82 | 2026-10-07 13:15:00 | MSG-03 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7cf8731f-ef78-34bf-b5d5-a966a869db24 | 3.57351 | -60.18187 | 2026-10-07 13:16:00 | TERRA_M-T | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 34.0 |
| 1771363f-cc8e-3881-b238-8eba9f651f1b | 3.29619 | -60.0117 | 2026-10-07 13:16:00 | TERRA_M-T | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 25.2 |
| 1b854b80-3b74-3d64-8ffb-5a97c75b2b48 | -9.12839 | -64.38129 | 2026-10-07 13:18:00 | TERRA_M-T | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 26.0 |
| 08cdfd1d-7d93-3c6a-b218-e664edd5a66a | -8.97207 | -68.59473 | 2026-10-07 13:18:00 | TERRA_M-T | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 14.6 |
| 52757c56-c9bf-30e5-9650-03daf6cc5e5e | -8.72564 | -70.77631 | 2026-10-07 13:18:00 | TERRA_M-T | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 1a75ec59-27a9-3dca-8631-b7b3071e65bb | -9.14326 | -65.30525 | 2026-10-07 13:18:00 | TERRA_M-T | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 30.0 |
| aa1964cf-5f89-37ff-97ff-c4d3583e08c6 | -9.01588 | -65.70565 | 2026-10-07 13:18:00 | TERRA_M-T | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 20.4 |
| 954fba0a-c971-3ca6-a9d6-e9f8bbb21dbc | -8.74574 | -69.64188 | 2026-10-07 13:18:00 | TERRA_M-T | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 20.2 |
| 383d3e4a-637b-3566-8781-6ca61381a367 | -8.86419 | -69.16879 | 2026-10-07 13:18:00 | TERRA_M-T | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 3f13d5fc-8211-34fe-9a62-4887ed334f4e | -7.89203 | -72.34858 | 2026-10-07 13:18:00 | TERRA_M-T | CRUZEIRO DO SUL | ACRE | Brasil | 1200203 | 12 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 542aaaa9-9a07-36bd-95ee-7c2b6edb1e49 | -9.00333 | -65.70403 | 2026-10-07 13:18:00 | TERRA_M-T | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 21.7 |
| 758538f2-123a-3159-a927-ee4ccf9494c0 | -9.11821 | -67.70887 | 2026-10-07 13:18:00 | TERRA_M-T | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 11.4 |
| ba3efac2-b157-3b38-a70e-53c701429b11 | -9.1451 | -65.29887 | 2026-10-07 13:18:00 | TERRA_M-T | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 35.9 |
| b0951444-9140-31ef-9b42-e4135ffa5a1e | -9.14376 | -65.40909 | 2026-10-07 13:18:00 | TERRA_M-T | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 33.6 |
| 32022c19-0778-37df-bb70-66d69d3db6d3 | -8.75113 | -69.64901 | 2026-10-07 13:18:00 | TERRA_M-T | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 532c3c51-0423-3b4c-b253-77e811403c80 | -8.78286 | -62.86574 | 2026-10-07 13:18:00 | TERRA_M-T | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 34.1 |
| 96c36a24-fe91-3299-b848-0c237afc7ff6 | -9.60678 | -67.48026 | 2026-10-07 13:18:00 | TERRA_M-T | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | 19.4 |
| 782970cf-4f0b-3d02-ab64-701ebf1fd875 | -7.9531 | -71.34041 | 2026-10-07 13:18:00 | TERRA_M-T | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 3bcc1fd3-7544-3a95-b786-7788fff89812 | -7.88189 | -72.35625 | 2026-10-07 13:18:00 | TERRA_M-T | CRUZEIRO DO SUL | ACRE | Brasil | 1200203 | 12 | 33 | nan | nan | nan | Amazônia | 42.5 |
| 267e3c7b-2d7f-3d3d-95aa-820bc30b4072 | -9.14576 | -65.28458 | 2026-10-07 13:18:00 | TERRA_M-T | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 22.1 |
| 2a498389-b887-389e-8b00-9614d98e77f8 | -8.79354 | -66.56187 | 2026-10-07 13:18:00 | TERRA_M-T | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 18.2 |
| 9a82f121-5b3a-3d2f-a9a6-f33863b3e813 | -9.67326 | -65.03126 | 2026-10-07 13:18:00 | TERRA_M-T | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 27.7 |
| b25b8691-46fa-322a-b211-9ecaf84a6077 | -9.1024 | -67.74757 | 2026-10-07 13:18:00 | TERRA_M-T | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 9.8 |
| bf0b459f-635a-36b8-9acf-ad1a23f45a66 | -8.92104 | -67.61008 | 2026-10-07 13:18:00 | TERRA_M-T | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 5b89bdcf-1b24-382e-b7a6-048117c09b8c | -7.88447 | -72.33839 | 2026-10-07 13:18:00 | TERRA_M-T | CRUZEIRO DO SUL | ACRE | Brasil | 1200203 | 12 | 33 | nan | nan | nan | Amazônia | 5.6 |
| e651962f-6940-33dc-89d8-315ded1d15ac | -7.95436 | -71.33157 | 2026-10-07 13:18:00 | TERRA_M-T | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 1821cd2f-b4cd-354b-8715-023b5bdad079 | -9.1113 | -65.3571 | 2026-10-07 13:18:00 | TERRA_M-T | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 21.4 |
| 281ceb86-d141-3506-ab88-6a2c5dc8f2a5 | -7.85751 | -72.46257 | 2026-10-07 13:18:00 | TERRA_M-T | CRUZEIRO DO SUL | ACRE | Brasil | 1200203 | 12 | 33 | nan | nan | nan | Amazônia | 21.6 |
| 8e62dc81-51d8-3ae9-b363-4adcf241950a | -8.77776 | -62.87015 | 2026-10-07 13:18:00 | TERRA_M-T | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 33.2 |
| 680a2a58-b78b-38b1-be3c-b3efa7d60281 | -8.75249 | -69.63893 | 2026-10-07 13:18:00 | TERRA_M-T | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 27.1 |
| d32653fb-6b80-3e08-beaf-454bb3bfc207 | -7.89074 | -72.35751 | 2026-10-07 13:18:00 | TERRA_M-T | CRUZEIRO DO SUL | ACRE | Brasil | 1200203 | 12 | 33 | nan | nan | nan | Amazônia | 70.2 |
| 7007046d-e5ac-33a1-bf47-d3abf9cc23e9 | -7.88318 | -72.34732 | 2026-10-07 13:18:00 | TERRA_M-T | CRUZEIRO DO SUL | ACRE | Brasil | 1200203 | 12 | 33 | nan | nan | nan | Amazônia | 71.2 |
| 33682bbf-60db-32d1-94a0-52b47e88c107 | -9.09634 | -67.75433 | 2026-10-07 13:18:00 | TERRA_M-T | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 2e676b31-2aa2-3fa9-976c-9ae32e6898d4 | -11.1054 | -45.6662 | 2026-10-07 13:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 88.2 |
| b0fecb12-d1d1-3550-b84b-2d9cc43f2cfb | -8.1996 | -46.3415 | 2026-10-07 13:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 60.7 |
| d4e18626-0a19-33ad-8cbf-bfd3c0081c5b | -11.0642 | -45.854 | 2026-10-07 13:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 170.8 |


[Clique aqui para ver as próximas entradas](README129.md)
