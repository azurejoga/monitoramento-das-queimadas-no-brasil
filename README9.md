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

## Dados Diários - Página 9

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9d6d7691-072f-36c6-b17d-acc3835d79b1 | -2.85169 | -53.33852 | 2024-10-19 01:24:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 31.2 |
| 33df0160-01f1-34a1-a13a-e097055f449c | -2.85022 | -53.32825 | 2024-10-19 01:24:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 18.1 |
| 94a59e9c-1da6-32c8-9334-d751d45b2cb9 | -2.83422 | -51.31132 | 2024-10-19 01:24:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 33.4 |
| 5191149f-78cd-3046-88cd-8f5e300e59bd | -2.83218 | -51.29741 | 2024-10-19 01:24:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 24.9 |
| 7e6e6c28-1f76-35f8-939c-0a960aec6bf7 | -2.8292 | -54.87165 | 2024-10-19 01:24:00 | TERRA_M-M | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 47e232ec-a3d7-331a-9450-4f484dcf076a | -2.82794 | -54.86268 | 2024-10-19 01:24:00 | TERRA_M-M | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 4ac3554d-e0a8-39d8-9bec-7aa012728574 | -2.81851 | -51.35602 | 2024-10-19 01:24:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 4e3eda04-c61d-3295-82a4-8db4215441a9 | -2.81647 | -51.34224 | 2024-10-19 01:24:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 21.7 |
| 26ec7897-b6d5-3312-88ee-d4859876d432 | -2.81454 | -51.34919 | 2024-10-19 01:24:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 24.4 |
| e85b95d3-af19-3db5-8ddc-f9be932770c4 | -2.80752 | -53.99268 | 2024-10-19 01:24:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| dea68404-471d-3e11-94ab-6eccb1f871f1 | -2.80618 | -53.9831 | 2024-10-19 01:24:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 93bf1fa9-ac7b-3e67-8fcc-8074976ffb56 | -2.80559 | -51.36459 | 2024-10-19 01:24:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| f41b101f-b545-3bca-98c8-b833df4dd3cc | -2.79833 | -53.994 | 2024-10-19 01:24:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 1215e162-8ee4-323b-8bbc-301d19bf3b77 | -2.79699 | -53.98442 | 2024-10-19 01:24:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 1270ca88-86f1-34c4-b9f7-c7f6f68318eb | -2.79469 | -51.36617 | 2024-10-19 01:24:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 96.0 |
| a184d554-04f9-3fc8-a500-77dbf32c6499 | -2.79272 | -51.35235 | 2024-10-19 01:24:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 23.5 |
| 48863a9f-9d94-35ed-8f7a-26619f72f276 | -2.78401 | -54.02528 | 2024-10-19 01:24:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| fe12f9cc-4db1-3ab3-9ae9-13161d1bbf34 | -2.74015 | -51.62797 | 2024-10-19 01:24:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 19.7 |
| 272b417e-4890-36dd-98b3-7c248983572d | -2.7315 | -52.57388 | 2024-10-19 01:24:00 | TERRA_M-M | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 95d65505-6ebd-35e6-a41e-fd6b284fd025 | -2.71889 | -48.83474 | 2024-10-19 01:24:00 | TERRA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 50.9 |
| 75ea462d-dff8-3241-9223-d317b2cc0787 | -2.71714 | -48.85162 | 2024-10-19 01:24:00 | TERRA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 18.2 |
| c4767276-32f0-3110-8e22-b6c3d3135756 | -2.71536 | -53.9919 | 2024-10-19 01:24:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 0e9b8625-1423-3b62-8307-512cd888c8ca | -2.71379 | -48.82973 | 2024-10-19 01:24:00 | TERRA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 36.5 |
| 58e4499e-1aae-3615-a575-8e2fe1df914a | -2.71259 | -49.16062 | 2024-10-19 01:24:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 11.7 |
| ee8e97c1-658b-33ea-8cd8-97b0c10e64ff | -2.6604 | -52.57813 | 2024-10-19 01:24:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 19.1 |
| 781b5e0a-d756-351c-944b-18b825562ae5 | -2.65619 | -48.4985 | 2024-10-19 01:24:00 | TERRA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 27.4 |
| 5c87fd17-0d23-37cf-b99e-173eb7772ae0 | -2.62525 | -51.77156 | 2024-10-19 01:24:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 11.7 |
| 8ed62bd6-c6d2-3044-8b58-96535e15cc8e | -2.62336 | -51.75858 | 2024-10-19 01:24:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 11.0 |
| fa86e0b0-3e36-338f-ac73-729affe5572c | -2.57069 | -54.01931 | 2024-10-19 01:24:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 467d393a-b7d9-3f7d-bd08-912b28be430f | -2.56943 | -47.09159 | 2024-10-19 01:24:00 | TERRA_M-M | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 17.0 |
| 9f3444ce-4cd0-39d1-8566-4492c014a742 | -2.56933 | -54.00973 | 2024-10-19 01:24:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 11.7 |
| 887a1167-5b44-31f7-ba52-7aec0e4d15eb | -2.56922 | -47.06713 | 2024-10-19 01:24:00 | TERRA_M-M | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 42.2 |
| 74b3110c-2877-3cf5-bf7e-ae8a4453e954 | -2.56477 | -47.06108 | 2024-10-19 01:24:00 | TERRA_M-M | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 31.7 |
| 4a9e45ab-865f-3c33-aaef-0e10fe165089 | -2.52985 | -47.22668 | 2024-10-19 01:24:00 | TERRA_M-M | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 25.1 |
| 6a99eedb-5eca-3ee4-af2d-bcf727d03d9e | -2.51859 | -51.81919 | 2024-10-19 01:24:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 11.3 |
| df0021f6-fce3-3850-8a88-9f5648ca4d9b | -2.51374 | -51.82626 | 2024-10-19 01:24:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 15.5 |
| 9004d5d4-d7db-3dda-bb62-714c6a990aa9 | -2.51192 | -51.8133 | 2024-10-19 01:24:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 12.3 |
| efb1af64-8f87-3055-bfc1-325ba9814f3c | -2.48645 | -49.75214 | 2024-10-19 01:24:00 | TERRA_M-M | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 11.8 |
| 9997a437-219e-3e27-9a3c-c618069dc169 | -2.46429 | -50.25766 | 2024-10-19 01:24:00 | TERRA_M-M | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 1e12538c-767e-33f2-984f-31ac96f44c82 | -2.36576 | -48.29222 | 2024-10-19 01:24:00 | TERRA_M-M | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 20.0 |
| 6897fb9a-3767-33a3-ba1c-ac7f4325f714 | -2.35444 | -49.66854 | 2024-10-19 01:24:00 | TERRA_M-M | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 3278b732-9b6b-3695-85b9-a57f4a887e40 | -2.2588 | -48.82142 | 2024-10-19 01:24:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 20.1 |
| f73fadc3-9c51-3095-b43f-796715d2b566 | -2.06356 | -55.86187 | 2024-10-19 01:24:00 | TERRA_M-M | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 4b278085-fd56-3aec-8f12-118a99f14167 | -1.98017 | -48.69549 | 2024-10-19 01:24:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 14.6 |
| 36492ab2-9bba-30e3-b6d7-6f3c74e23bce | -1.97263 | -48.69073 | 2024-10-19 01:24:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 20.8 |
| be5bd093-b6e1-3d11-b58f-dc0195cd21d3 | -1.84963 | -56.37622 | 2024-10-19 01:24:00 | TERRA_M-M | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 1e72b84a-e308-325c-8689-64bee4783ca1 | -1.70949 | -52.51459 | 2024-10-19 01:24:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 764884ee-fae9-301c-b144-cfd53d9a2904 | -1.33443 | -54.66224 | 2024-10-19 01:24:00 | TERRA_M-M | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 4fe0d367-3564-3c62-8b99-44254ffd44a0 | -1.14507 | -47.31418 | 2024-10-19 01:24:00 | TERRA_M-M | PEIXE-BOI | PARÁ | Brasil | 1505601 | 15 | 33 | nan | nan | nan | Amazônia | 102.3 |
| e8b4f822-4fe0-3882-8f4e-9a1b5ccb137a | -1.14483 | -47.33884 | 2024-10-19 01:24:00 | TERRA_M-M | PEIXE-BOI | PARÁ | Brasil | 1505601 | 15 | 33 | nan | nan | nan | Amazônia | 39.4 |
| 86c74f59-d278-3db6-9374-8ee2b2bc563d | -1.14024 | -47.30805 | 2024-10-19 01:24:00 | TERRA_M-M | PEIXE-BOI | PARÁ | Brasil | 1505601 | 15 | 33 | nan | nan | nan | Amazônia | 77.2 |
| a4d31ac4-e389-3a9d-a3b9-353f9bce5905 | -0.87917 | -52.93294 | 2024-10-19 01:24:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 16.8 |
| c7d4c4ed-0371-3acc-92e4-c15119e0ffe6 | -1.1375 | -47.3179 | 2024-10-19 01:25:12 | GOES-16 | PEIXE-BOI | PARÁ | Brasil | 1505601 | 15 | 33 | nan | nan | nan | Amazônia | 58.0 |
| 8d1f6ea5-43d3-376f-a9d1-992ab3b96350 | -1.156 | -47.3176 | 2024-10-19 01:25:12 | GOES-16 | PEIXE-BOI | PARÁ | Brasil | 1505601 | 15 | 33 | nan | nan | nan | Amazônia | 56.6 |
| eb27d1e4-8d7d-3af1-acb3-df4a0a60af97 | -2.7885 | -51.3618 | 2024-10-19 01:25:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 65.5 |
| a0c86fe0-a31c-39de-849c-bfd37dcb5753 | -2.8069 | -51.3613 | 2024-10-19 01:25:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 69.8 |
| d2ac4fe0-a070-3a7d-8654-906d12782aeb | -2.9489 | -52.9174 | 2024-10-19 01:25:23 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 93.4 |
| 0859c173-54cd-36df-86ad-db98bae5d7ef | -2.9489 | -52.897 | 2024-10-19 01:25:23 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 65.1 |
| d9d65687-4090-3bec-ad43-cf3601c8fd2d | -2.9674 | -47.9931 | 2024-10-19 01:25:23 | GOES-16 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 67.2 |
| d8e6ce9f-f03e-3e85-9841-cd5cec1a653a | -2.9673 | -52.9169 | 2024-10-19 01:25:23 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 64.5 |
| b103c510-87ff-3ff7-9a9f-f95bcb3bd1b8 | -2.9859 | -52.8554 | 2024-10-19 01:25:23 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 64.2 |
| b8f49aa4-7da1-390a-883c-a163fbff4a86 | -3.4202 | -50.2164 | 2024-10-19 01:25:25 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 65.2 |
| 4ce0802a-3bfb-3324-af39-4192736ed3bd | -3.4387 | -50.2158 | 2024-10-19 01:25:25 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 94.8 |
| 104bc93a-667e-3332-b0a8-7e32f020b2a1 | -3.4388 | -50.1948 | 2024-10-19 01:25:25 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 61.3 |
| a656d93a-d513-3275-8a23-b6417a200468 | -4.4167 | -50.535 | 2024-10-19 01:25:31 | GOES-16 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 60.2 |
| cbadef15-c8c3-3ea7-ac47-3affbd97ae26 | -4.6028 | -44.6133 | 2024-10-19 01:25:32 | GOES-16 | PEDREIRAS | MARANHÃO | Brasil | 2108207 | 21 | 33 | nan | nan | nan | Cerrado | 96.3 |
| c568b62f-6c58-3d8a-a414-211be5ae3e05 | -4.6873 | -45.8504 | 2024-10-19 01:25:32 | GOES-16 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 97.9 |
| d994f5fa-3ea8-3f0e-89d3-53815cd2ae80 | -4.6875 | -45.828 | 2024-10-19 01:25:32 | GOES-16 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 74.7 |
| 6e3e8097-693b-3d2e-af15-d6c1dc2b2cb4 | -4.706 | -45.8493 | 2024-10-19 01:25:33 | GOES-16 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 285.7 |
| 67d430e5-ac3b-3972-ba56-d5b2c4d81a1c | -4.7061 | -45.8269 | 2024-10-19 01:25:33 | GOES-16 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 201.8 |
| 064d9c58-0dc6-36c5-bdd4-dc696f152ea9 | -4.7246 | -45.8482 | 2024-10-19 01:25:33 | GOES-16 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 79.6 |
| 31878608-e345-3220-a8ab-e6dd986d64d8 | -7.6815 | -47.3213 | 2024-10-19 01:25:49 | GOES-16 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 76.2 |
| a4bd115f-e387-3033-92b1-d36652bc58ce | -9.0344 | -67.4641 | 2024-10-19 01:25:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 150.0 |
| a217349c-b69d-377a-b997-dfe51cfec83b | -9.0345 | -67.4455 | 2024-10-19 01:25:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 105.0 |
| cb5e86d3-f4ad-3ad4-8973-81f349fa377d | -9.053 | -67.4636 | 2024-10-19 01:25:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 78.4 |
| 92ebc4f0-313e-3da9-ae6b-2c12b12b9781 | -9.053 | -67.4451 | 2024-10-19 01:25:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 70.2 |
| a1561cbf-0b8f-3afd-8d11-3e016baf4a87 | 5.05614 | -60.11134 | 2024-10-19 01:26:00 | TERRA_M-M | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 6da5313f-4fc8-3778-bf67-2a62fcfa7bd6 | 5.05461 | -60.12205 | 2024-10-19 01:26:00 | TERRA_M-M | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 29.7 |
| 817059b7-c35e-3c1b-b304-717b2785e1a0 | -12.004 | -63.5199 | 2024-10-19 01:26:15 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 59.7 |
| f7035b6a-a829-3f46-8c41-6852cb6371ba | -12.0041 | -63.5008 | 2024-10-19 01:26:15 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 63.5 |
| 54fe0916-a657-3ac0-8c76-baf3d2711a17 | -12.023 | -63.4998 | 2024-10-19 01:26:15 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 65.4 |
| 09d3acb4-010f-3fc0-a629-97bb4a441936 | -12.5147 | -63.3014 | 2024-10-19 01:26:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 92.5 |
| 132f6f22-f710-3a5f-9b3b-d78883c691c7 | -12.5149 | -63.2822 | 2024-10-19 01:26:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 67.4 |
| fb228aa4-dcc0-3c53-984d-a225e31e4b6f | -12.5336 | -63.3003 | 2024-10-19 01:26:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 69.1 |
| fc2f9dc7-836b-3099-af61-6d6b3a6f27b5 | -2.5635 | -47.0694 | 2024-10-19 01:35:20 | GOES-16 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 62.3 |
| cc69e1f0-229e-3a8c-a644-0f087664cbf0 | -2.5821 | -47.0688 | 2024-10-19 01:35:21 | GOES-16 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 70.3 |
| c17b6139-ebbd-3507-be3f-fed0e1f29185 | -2.8069 | -51.3613 | 2024-10-19 01:35:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 58.5 |
| fa5d778c-d8a6-3fdf-9840-c775759af486 | -2.7885 | -51.3618 | 2024-10-19 01:35:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 69.9 |
| 1495343c-37c8-360c-bab7-becf82ded18a | -2.9489 | -52.9174 | 2024-10-19 01:35:23 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 81.4 |
| a6c451af-bbf4-3f6a-91ff-ab01774071c0 | -2.9489 | -52.897 | 2024-10-19 01:35:23 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 57.9 |
| 59456639-27fa-36d8-89a9-77400a9ee6f2 | -2.9674 | -47.9931 | 2024-10-19 01:35:23 | GOES-16 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 46.2 |
| 0b3dd837-6240-3ef3-8eb7-547202c9d99f | -2.9673 | -52.9169 | 2024-10-19 01:35:23 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 78.6 |
| 27233eb9-801e-3087-891f-cc5df9406341 | -2.9859 | -52.8554 | 2024-10-19 01:35:23 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 59.4 |
| 6cb678b9-ba83-3c6e-b405-81390f09ca2c | -3.4202 | -50.2164 | 2024-10-19 01:35:25 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 61.6 |
| 9a162fb1-d6f2-3dc8-ba3c-b5c0e1b03b8d | -3.4387 | -50.2158 | 2024-10-19 01:35:25 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 84.1 |
| f1d6284b-26de-3a9b-8534-6c90f3e181a9 | -3.4388 | -50.1948 | 2024-10-19 01:35:25 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 53.8 |
| 233960b9-63bc-3ce4-989a-480b2b5a62fb | -4.4167 | -50.535 | 2024-10-19 01:35:31 | GOES-16 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 63.4 |
| d5c6df65-3e10-3791-b3eb-6d0445105a85 | -4.6873 | -45.8504 | 2024-10-19 01:35:32 | GOES-16 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 100.7 |
| cae7f045-144c-3dbb-92d9-c7bb9d209d10 | -4.6875 | -45.828 | 2024-10-19 01:35:32 | GOES-16 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 79.1 |
| 496e85af-28db-3e28-ae99-32d4659aa878 | -4.706 | -45.8493 | 2024-10-19 01:35:33 | GOES-16 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 275.3 |


[Clique aqui para ver as próximas entradas](README10.md)
