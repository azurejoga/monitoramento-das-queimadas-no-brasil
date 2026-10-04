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
| 0afb0723-665a-3056-ba3b-79aa484a025e | -3.4762 | -50.0883 | 2026-10-04 02:50:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 60.7 |
| 09d09714-cc01-3d4d-94a7-6a7ad6a6694d | -2.8164 | -54.0929 | 2026-10-04 02:50:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 49.7 |
| 69441fce-ce6a-3ef2-aa55-cc48aa961cc5 | -3.1299 | -53.7431 | 2026-10-04 02:50:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 81.7 |
| e4369ba5-22a3-37ce-b7bf-35b85a500c26 | -3.1116 | -53.7234 | 2026-10-04 02:50:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 192.1 |
| 6174dc8f-445a-33a8-a741-eec4fbb5e4fd | -2.7979 | -54.1134 | 2026-10-04 02:50:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 66.0 |
| 747e49f0-4cd2-3b1e-b1ee-4c30f4a8ed4c | -2.2297 | -53.7026 | 2026-10-04 02:50:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 49.4 |
| 0e95ede0-a947-3a03-a59e-d223d845907d | -4.2886 | -50.2886 | 2026-10-04 02:50:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 272.8 |
| 60e47313-9b67-31b4-a410-ac1a5823ef72 | -4.2558 | -46.3855 | 2026-10-04 02:50:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 57.5 |
| 82424d1b-6d96-31cb-a48f-bbed8904b39c | -4.2702 | -50.2683 | 2026-10-04 02:50:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 125.8 |
| 7d30d56d-b349-3b28-840f-ea621607805d | -3.2951 | -53.8395 | 2026-10-04 02:50:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 53.4 |
| 915812f8-a0a2-3125-b0c2-1aeb7d13421e | -3.13 | -53.7229 | 2026-10-04 03:00:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 122.4 |
| 05a429ee-6d7a-3ebc-9e43-a9c4845abaec | -2.2297 | -53.7026 | 2026-10-04 03:00:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 54.4 |
| 1a80727d-438b-31a8-ab8a-f20f677f2b21 | -3.1116 | -53.7234 | 2026-10-04 03:00:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 193.5 |
| 56d63b93-0902-3826-95cf-a1ca89f1328d | -3.0721 | -49.5313 | 2026-10-04 03:00:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 53.6 |
| fc13c38a-bdb7-3c4a-ad84-2f30191cfc3f | -4.2744 | -46.3846 | 2026-10-04 03:00:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 64.0 |
| 46427ce4-f244-3a0b-b423-3295dda342ad | -4.3072 | -50.2668 | 2026-10-04 03:00:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 105.6 |
| 5943eb9d-88e8-327d-96c3-d1994efb8f6c | -4.2701 | -50.2894 | 2026-10-04 03:00:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 73.3 |
| 42963cea-241e-3a1b-8adf-7d9968fdc44c | -4.2886 | -50.2886 | 2026-10-04 03:00:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 145.5 |
| 51df3118-389b-3cc0-9ea4-fcf72205cbaa | -4.2887 | -50.2675 | 2026-10-04 03:00:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 583.1 |
| 6a92e38a-72dc-3561-b730-fb9317a7e01c | -3.1116 | -53.7436 | 2026-10-04 03:00:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 147.6 |
| a0a36153-e9bb-351d-b2ca-eec70b939ec1 | -3.8757 | -55.7986 | 2026-10-04 03:00:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 69.5 |
| 8da47b9e-1eda-3048-b1f6-f785d5cabd7f | -3.1299 | -53.7431 | 2026-10-04 03:00:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 90.4 |
| b3941f6e-2d3e-3d76-a7bc-a531113b2c78 | -3.8756 | -55.8184 | 2026-10-04 03:00:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 67.6 |
| a46ddb96-f7c8-30f1-b741-2d9ba01ccb69 | -4.2745 | -46.3624 | 2026-10-04 03:00:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 107.4 |
| 119b547d-edd3-3140-b105-b017f0085954 | -2.8164 | -54.0929 | 2026-10-04 03:00:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 47.9 |
| 00d6050b-22d6-3c3a-b97d-49b938ae583d | -2.8163 | -54.1129 | 2026-10-04 03:00:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 110.4 |
| 62771613-5f2c-3f41-9576-fdf6749adf6b | -4.2888 | -50.2465 | 2026-10-04 03:00:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 111.9 |
| 2af9d2d0-2e13-3b1a-b55e-a9efab451eae | -3.2951 | -53.8395 | 2026-10-04 03:00:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 54.2 |
| 65d15dd0-9ef5-327b-9ae9-3bfc1cd6d341 | -4.2559 | -46.3633 | 2026-10-04 03:00:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 72.6 |
| fde7976e-9d2d-3992-bcb8-ea6c5b31700f | -3.072 | -49.5525 | 2026-10-04 03:00:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 52.0 |
| e36a2353-fd91-3f4f-9c3e-68d9d028015d | -4.2702 | -50.2683 | 2026-10-04 03:00:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 185.6 |
| e92a5a16-5fe5-364a-9a06-32630755f892 | -2.5842 | -51.8623 | 2026-10-04 03:00:00 | GOES-19 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 68.5 |
| b66da559-7f85-32ac-83fe-3640153038b6 | -2.7979 | -54.1134 | 2026-10-04 03:00:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 65.4 |
| 4aac61a9-e981-37d7-8a73-46d5391c570a | -2.8163 | -54.133 | 2026-10-04 03:00:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 82.4 |
| d02a08f9-d20b-316e-bb11-eacfd6fbd162 | -3.4762 | -50.0883 | 2026-10-04 03:00:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 52.4 |
| 1c6390df-8d45-372e-bf30-5c28aa0d39e2 | -3.4761 | -50.1094 | 2026-10-04 03:00:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 48.9 |
| c36bc4ae-bd48-3009-b033-b3c011927f73 | -4.2888 | -50.2465 | 2026-10-04 03:10:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 131.7 |
| cfceb74f-53a5-3c45-bf90-1e44fde2545a | -2.8164 | -54.0929 | 2026-10-04 03:10:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 48.1 |
| d3f0f595-831f-3912-a3bb-397fec953ed2 | -3.4762 | -50.0883 | 2026-10-04 03:10:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 54.8 |
| 4ce559e7-cb5b-39c6-81da-8f16599babfb | -2.8163 | -54.1129 | 2026-10-04 03:10:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 105.6 |
| b13c53a1-e0e6-3c67-9ff4-d170aa15b9ed | -4.2744 | -46.3846 | 2026-10-04 03:10:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 52.4 |
| b03c1b65-75cf-34d8-8f24-3937415eb84b | -4.2701 | -50.2894 | 2026-10-04 03:10:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 54.3 |
| c0f6f019-1b6a-38ca-ad81-ce2087197851 | -3.1116 | -53.7234 | 2026-10-04 03:10:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 197.7 |
| 6ec3060e-58f1-3e24-b90f-b188dda1f81c | -3.1116 | -53.7436 | 2026-10-04 03:10:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 158.6 |
| f14d9952-5db5-378c-bdaf-9bbb465e3768 | -3.8757 | -55.7986 | 2026-10-04 03:10:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 57.3 |
| c87ee8e7-555d-3a4f-beab-f32ab0d155a2 | -4.2887 | -50.2675 | 2026-10-04 03:10:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 547.8 |
| 3668b929-30c0-33f7-91ac-970b29f2671b | -3.13 | -53.7229 | 2026-10-04 03:10:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 131.7 |
| 4ae4377d-db76-389b-bb35-5fbd6f89d587 | -3.0721 | -49.5313 | 2026-10-04 03:10:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 50.5 |
| 46dd72bb-e1e1-36b4-b899-0f52dcc47ee4 | -3.072 | -49.5525 | 2026-10-04 03:10:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 44.0 |
| 76057ea7-f6bd-300a-a81b-555dd6912448 | -4.2886 | -50.2886 | 2026-10-04 03:10:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 190.8 |
| cfdf574f-375d-38f9-96a8-c0c887ed9f16 | -4.2559 | -46.3633 | 2026-10-04 03:10:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 120.7 |
| 08f813df-8b79-3aad-b283-598ea83054dd | -4.2702 | -50.2683 | 2026-10-04 03:10:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 133.8 |
| 4f9d78c6-71cf-3aaa-ba8e-39aac146e790 | -4.2745 | -46.3624 | 2026-10-04 03:10:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 97.4 |
| d77dd144-402f-3da9-98b7-68e1526c2438 | -4.2558 | -46.3855 | 2026-10-04 03:10:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 64.4 |
| 16331ba8-4964-311e-b1d9-6870786575f3 | -2.2297 | -53.7026 | 2026-10-04 03:10:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 51.9 |
| 97f8433c-f4cf-306b-ae8f-ed1f644de4b5 | -3.8756 | -55.8184 | 2026-10-04 03:10:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 66.8 |
| e9fb4bad-5794-3e79-a128-b9649dece3cb | -3.1299 | -53.7431 | 2026-10-04 03:10:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 76.5 |
| b0d33d64-d098-317f-95b9-792d6f6b6d49 | -2.8163 | -54.133 | 2026-10-04 03:10:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 78.9 |
| 29b06877-a19a-3fce-ba00-8f3caac15315 | -2.5842 | -51.8623 | 2026-10-04 03:10:00 | GOES-19 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 78.2 |
| 1ba1806f-7808-3af3-b759-69f785038bf8 | -4.3072 | -50.2668 | 2026-10-04 03:10:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 58.7 |
| b417df95-aec4-35ee-b59a-ee7151284201 | -2.7979 | -54.1134 | 2026-10-04 03:10:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 64.3 |
| 86cd5343-f535-381b-80de-6d81495f1306 | -4.28 | -50.26 | 2026-10-04 03:15:00 | MSG-03 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 09eb98d1-b5b9-3c7e-96d6-7dd5a89f1459 | -4.28 | -50.32 | 2026-10-04 03:15:00 | MSG-03 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1a583901-dacc-39c7-affd-ff26c834d032 | -4.1193 | -38.34798 | 2026-10-04 03:15:00 | NPP-375D | CASCAVEL | CEARÁ | Brasil | 2303501 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 83ab99a4-eeb3-308d-b3f8-4446e634f9df | -4.11812 | -38.35454 | 2026-10-04 03:15:00 | NPP-375D | CASCAVEL | CEARÁ | Brasil | 2303501 | 23 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 1e5c7728-ad6c-3ae7-b385-91d206797e3d | -4.2559 | -46.3633 | 2026-10-04 03:20:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 85.7 |
| 0c3cc9a2-eb0e-32ca-a359-69a9460fa2e3 | -2.8163 | -54.1129 | 2026-10-04 03:20:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 102.5 |
| 24f9b84c-8a8d-3a1f-bd53-cb7afcfbd52c | -4.2886 | -50.2886 | 2026-10-04 03:20:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 177.3 |
| 71156785-27ad-38a0-875f-a360c7ef5d6d | -2.7979 | -54.1134 | 2026-10-04 03:20:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 62.6 |
| 80d7e00a-89b6-326d-a497-0e5ceb47e51d | -4.2888 | -50.2465 | 2026-10-04 03:20:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 110.4 |
| 4ef32b7c-0a73-346c-af85-1063104bd5da | -4.2701 | -50.2894 | 2026-10-04 03:20:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 85.0 |
| 8e960b20-c327-3474-9ee6-a57dbd94cf67 | -3.1299 | -53.7431 | 2026-10-04 03:20:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 82.6 |
| f6f7027c-5c33-3530-bccb-8ddd5f6ce3ac | -4.2702 | -50.2683 | 2026-10-04 03:20:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 179.0 |
| b1eb1e4e-17f6-34b3-be2f-a440812d9faa | -3.8756 | -55.8184 | 2026-10-04 03:20:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 56.7 |
| 95720c05-d735-3209-950e-76a668cdfcac | -4.2744 | -46.3846 | 2026-10-04 03:20:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 59.7 |
| b2e3049f-7ec0-3a54-9246-f6e16fb40290 | -2.8164 | -54.0929 | 2026-10-04 03:20:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 44.3 |
| ed37d942-0842-3094-9e45-835dff94387a | -3.0721 | -49.5313 | 2026-10-04 03:20:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 52.1 |
| a34f24fc-870a-35a5-9a6e-0bbda95e3c00 | -4.2887 | -50.2675 | 2026-10-04 03:20:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 466.4 |
| fd2a6554-bb62-3b28-b99d-bcf914c595db | -3.1116 | -53.7436 | 2026-10-04 03:20:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 132.4 |
| 1554eaa3-1ca0-3b68-aada-85fa4bb1d425 | -3.1116 | -53.7234 | 2026-10-04 03:20:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 199.7 |
| 0fa631ec-2f84-312b-bfb7-9e4b72c5cc86 | -2.8163 | -54.133 | 2026-10-04 03:20:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 76.9 |
| 02c92218-79e5-3cb1-9654-9d784d4ec572 | -3.0548 | -54.2277 | 2026-10-04 03:20:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 47.9 |
| c40c5387-0d84-3762-91f8-222ef911b45c | -3.4762 | -50.0883 | 2026-10-04 03:20:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 57.1 |
| 5264dc44-9f89-3df8-9432-683b3f2e8878 | -4.2745 | -46.3624 | 2026-10-04 03:20:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 122.7 |
| 5627825d-8619-3ceb-9010-856ff68df26a | -2.5842 | -51.8623 | 2026-10-04 03:20:00 | GOES-19 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 69.9 |
| a0d187da-f813-3af3-b8ab-ca652842d116 | -4.3072 | -50.2668 | 2026-10-04 03:20:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 90.3 |
| d8d81d41-8bd8-3ffd-bbae-47e4ac4284d9 | -3.072 | -49.5525 | 2026-10-04 03:20:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 43.5 |
| 1a2b2879-4de3-3fbe-8ccd-ea528d3c1dcb | -3.13 | -53.7229 | 2026-10-04 03:20:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 130.5 |
| f5e5cb50-5a3d-3db8-9270-e3d8bb70e550 | -3.0364 | -54.2282 | 2026-10-04 03:20:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 48.8 |
| 742fc45e-d2fb-3d56-bef7-6fbbae883fb4 | -4.2701 | -50.2894 | 2026-10-04 03:30:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 90.6 |
| b3b2dc49-01c3-37ad-ba57-d82fc7990cbe | -2.8163 | -54.133 | 2026-10-04 03:30:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 83.8 |
| 6e0258ad-febd-3500-b383-efb131fba644 | -4.2559 | -46.3633 | 2026-10-04 03:30:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 98.7 |
| edd158d6-6571-3892-b538-ef86c3bd3fac | -3.072 | -49.5525 | 2026-10-04 03:30:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 46.8 |
| 8d214c44-86eb-3265-8e42-e41717c96765 | -2.2297 | -53.7026 | 2026-10-04 03:30:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 44.4 |
| cf4fb6e0-cff9-398b-b8d1-f77e087424aa | -3.0548 | -54.2277 | 2026-10-04 03:30:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 91.2 |
| 83d05773-5507-31cb-8cf2-782c83423a2c | -4.2744 | -46.3846 | 2026-10-04 03:30:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 65.7 |
| e276885c-7bcd-3902-9c11-2a01371a2a6c | -3.1116 | -53.7436 | 2026-10-04 03:30:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 157.3 |
| ccaf314f-2a35-3d2a-a847-6fdf8a140b58 | -3.13 | -53.7229 | 2026-10-04 03:30:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 117.7 |
| d104f506-98b1-351b-bb9f-56cf07b4c8b7 | -3.4762 | -50.0883 | 2026-10-04 03:30:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 50.5 |
| 45908d70-a052-306e-88ee-7518df7889ae | -3.0364 | -54.2282 | 2026-10-04 03:30:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 62.0 |


[Clique aqui para ver as próximas entradas](README21.md)
