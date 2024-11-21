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

## Dados Diários - Página 65

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2d5bf033-8d81-3c88-ba65-b6ba30f95ff3 | -2.79106 | -52.54853 | 2024-11-21 04:55:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| bfeeb905-5257-33b3-9887-cc5ad78628d0 | -3.27886 | -50.21547 | 2024-11-21 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 38666c8e-2c7a-3a3c-a472-4a08c29509d8 | -3.06228 | -53.28779 | 2024-11-21 04:55:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cc70cf26-7577-3f4a-b84a-7c54a62c0df3 | -2.7136 | -53.17317 | 2024-11-21 04:55:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 61b512c2-8f2a-361f-adaa-ecf16adcc233 | -3.60204 | -51.47164 | 2024-11-21 04:55:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a40bfcc6-e8d9-30c5-bd89-81239183b411 | -3.28355 | -53.82588 | 2024-11-21 04:55:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 90c0a7b6-bd01-305d-bd24-a8259aefcb9d | -3.57352 | -50.41821 | 2024-11-21 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| c554815a-c974-3a8f-a9ab-ae19e8b0c3f5 | -6.93023 | -42.82614 | 2024-11-21 04:55:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 87007131-bde3-3cdd-90b2-dab0e6846adf | -2.76737 | -52.11032 | 2024-11-21 04:55:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| abf95449-1079-341c-9e8a-c8f400ca5270 | -3.61413 | -54.74508 | 2024-11-21 04:55:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 38737150-5b0d-35c2-91da-25fb675f19da | -2.7603 | -54.06202 | 2024-11-21 04:55:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6aef0194-131e-3ef3-bfe1-b76a2f292771 | -3.48465 | -50.3129 | 2024-11-21 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 069bfd17-c452-36a6-93ab-ab227d5dc9d1 | -3.46574 | -54.56247 | 2024-11-21 04:55:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| d647e4c1-098c-33fe-bb6b-cde3e9674742 | -10.69927 | -48.81345 | 2024-11-21 04:55:00 | NOAA-20 | OLIVEIRA DE FÁTIMA | TOCANTINS | Brasil | 1715507 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| a32cb15b-b654-31b2-925d-cbdf73ee92d8 | -2.7497 | -54.02134 | 2024-11-21 04:55:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d7dd0519-8e3a-3674-b531-07d736e159cf | -2.79836 | -54.01505 | 2024-11-21 04:55:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 24decffa-2efd-3b98-afb7-cf329430745e | -4.04105 | -46.22457 | 2024-11-21 04:55:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| da34c5a3-7d1f-3e29-8587-cbb49868ef7e | -2.74259 | -51.72632 | 2024-11-21 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| af39dfbb-3fec-38c8-b2f1-56cda28c7fa7 | -5.42813 | -45.34501 | 2024-11-21 04:55:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 9ab87efe-9ff4-3faf-85a0-606583246d8d | -3.28468 | -53.84016 | 2024-11-21 04:55:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| df71971e-a445-3535-95ee-31489bb01a26 | -2.78208 | -51.71758 | 2024-11-21 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 1e78a6af-e839-37bc-99f1-33c44927dbc3 | -2.82157 | -54.01868 | 2024-11-21 04:55:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 637dbea7-2f6b-3743-a4b7-f7f162627f84 | -3.49859 | -48.22562 | 2024-11-21 04:55:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8b2c1ea5-2fe2-37f5-9ab9-2c64b4fafae8 | -2.91006 | -53.06653 | 2024-11-21 04:55:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| e7f0733d-1f73-3d27-94b5-d2ec22901490 | -3.29222 | -49.1862 | 2024-11-21 04:55:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 11.9 |
| 15095147-aaf2-3c04-ad81-472373c8a00f | -2.34535 | -54.4097 | 2024-11-21 04:55:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b4dda1ba-f8db-3623-9d3c-f70cc6a2d770 | -6.18304 | -43.41073 | 2024-11-21 04:55:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7fd5319a-ba7b-343a-9079-b8dc17fea049 | -3.64614 | -52.35803 | 2024-11-21 04:55:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6b7b3f50-03e5-3c54-bb6a-1ed4ec41857a | -5.19083 | -47.73803 | 2024-11-21 04:55:00 | NOAA-20 | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 800cf10c-fa0f-33dc-81df-2a55529ba2d8 | -4.76626 | -46.44782 | 2024-11-21 04:55:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8c4ddc22-8799-387b-913f-4a7b5cae2647 | -3.81366 | -52.3473 | 2024-11-21 04:55:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| f391028a-dd72-3d75-980c-2cce33b52061 | -2.75902 | -52.11992 | 2024-11-21 04:55:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c0a0a249-a445-3dd4-b7a1-acef8b6333e6 | -4.08948 | -51.08678 | 2024-11-21 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 26805479-b5aa-3a8c-979e-07225315b733 | -2.33958 | -53.92883 | 2024-11-21 04:55:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 4cef5940-8a57-3217-9091-c870817af474 | -3.74943 | -52.32706 | 2024-11-21 04:55:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6d0d66b5-a265-315e-9250-705c0f4232b8 | -4.66554 | -46.40191 | 2024-11-21 04:55:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| fdaf3ed4-1a31-36eb-af43-576d16c813a9 | -4.13254 | -53.61066 | 2024-11-21 04:55:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| e1cb40a7-45f7-3790-8cd4-09cd88db2306 | -4.20971 | -48.72207 | 2024-11-21 04:55:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| abf936bc-714b-3a00-ae13-a69b4082d2dc | -6.30184 | -45.34141 | 2024-11-21 04:55:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ea699c0b-37c2-3b33-8094-c21b90b7c38b | -4.58095 | -48.01088 | 2024-11-21 04:55:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| af49cff6-3eac-3695-a430-57f62e5b2208 | -3.38187 | -52.46149 | 2024-11-21 04:55:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| e7a066c3-93da-3e3e-b7c7-a4f5720708bf | -4.0583 | -50.61359 | 2024-11-21 04:55:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b9f0ce07-0f17-3f5e-9e45-64f6c5127613 | -3.30416 | -51.29332 | 2024-11-21 04:55:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| c6a390cb-bc5a-3d07-a93a-01a78ee6082d | -5.94821 | -44.25026 | 2024-11-21 04:55:00 | NOAA-20 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 4a7e49e7-77f5-386b-a227-ff3035cde307 | -4.17534 | -53.57841 | 2024-11-21 04:55:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ec98d4db-1a67-3335-bb2c-db623fb19964 | -4.96408 | -45.51802 | 2024-11-21 04:55:00 | NOAA-20 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| af25881c-77dd-32c3-b8be-94b9278eea34 | -4.36846 | -46.09409 | 2024-11-21 04:55:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 12157445-890c-3976-956e-35a9ceae876e | -2.7912 | -54.03878 | 2024-11-21 04:55:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 84be0e28-b192-30f7-889e-677669ca87f4 | -3.35724 | -53.40085 | 2024-11-21 04:55:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f2c6c4c5-9f81-395a-a41e-2a1492be984a | -3.46763 | -50.00817 | 2024-11-21 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| a1e287b2-13c0-3727-960f-554698dcae8e | -2.61488 | -53.97183 | 2024-11-21 04:55:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fb98b0c2-e8ca-332a-89c4-108185019e75 | -3.5765 | -50.42287 | 2024-11-21 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 17b7fb6d-e8a3-31eb-a26b-1b71fe77121a | -3.35427 | -50.18396 | 2024-11-21 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 2eee430d-4906-3190-b834-40fb117533e9 | -2.74925 | -54.0674 | 2024-11-21 04:55:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c4fc8fa1-5143-3e95-a402-8976d1f2c8ef | -4.64171 | -49.546 | 2024-11-21 04:55:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| e98e6491-d62c-31a6-b751-0bbddada5d5a | -3.51806 | -54.68617 | 2024-11-21 04:55:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 55065f94-5370-3b36-a7d9-2659f6940d0d | -2.79051 | -52.55201 | 2024-11-21 04:55:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f8226336-f871-3dc1-9559-8f2e523a8bb7 | -6.31495 | -49.67507 | 2024-11-21 04:55:00 | NOAA-20 | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 2448c40b-841e-3458-8fac-180a526de704 | -3.27949 | -50.21131 | 2024-11-21 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 2473fbd2-4438-31bb-8743-063ddaebcba2 | -3.54119 | -50.53479 | 2024-11-21 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 2eb01b62-d720-36fc-9a3f-3660700d1c49 | -2.74492 | -54.11655 | 2024-11-21 04:55:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 13a3865c-5908-38e5-acf7-05c7b106f3cf | -2.80121 | -51.77236 | 2024-11-21 04:55:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 950cffdd-da6a-3696-adb8-9375ea6b11d5 | -4.99073 | -47.23956 | 2024-11-21 04:55:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5e525912-3874-3644-ad98-beab2c1ad8ad | -3.29519 | -53.85945 | 2024-11-21 04:55:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 7eba7d44-c5e6-36ee-9cce-717c5cba072d | -6.18475 | -43.41533 | 2024-11-21 04:55:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 06a8dfda-032a-34b3-9b75-1707b50bb4b8 | -3.80355 | -52.22258 | 2024-11-21 04:55:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e63c785d-d6a2-3b70-92ef-9efdcc1fa553 | -4.21024 | -48.71858 | 2024-11-21 04:55:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1f5fa0e9-1203-3170-bff6-6b6d8523d8b4 | -3.36605 | -53.06401 | 2024-11-21 04:55:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c3744214-f59f-3dcd-84a5-e3e4b5e1a651 | -3.37685 | -50.28503 | 2024-11-21 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 20a12678-d194-3665-bb07-e7665feab604 | -3.28426 | -53.67102 | 2024-11-21 04:55:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.2 |
| 706e55d9-d7f1-3dc1-9bb4-f47789830267 | -2.34834 | -53.89468 | 2024-11-21 04:55:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7ab5eff4-c073-3e5b-868e-01517f84c62f | -3.27879 | -48.80438 | 2024-11-21 04:55:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 87742458-a9b6-3745-91c3-1c77a1f22355 | -2.5834 | -53.97755 | 2024-11-21 04:55:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 09ae96f5-e1cc-3b76-8b8b-72742ed5c107 | -4.34646 | -46.14381 | 2024-11-21 04:55:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f7ab4e08-4476-33f1-b151-7522733fed35 | -2.78958 | -54.0705 | 2024-11-21 04:55:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 61c955a6-89ca-3871-bf69-a4675d8e79d8 | -2.58839 | -51.72129 | 2024-11-21 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d7bf2222-308f-3c9f-be60-375cd9124ae8 | -4.98296 | -48.75374 | 2024-11-21 04:55:00 | NOAA-20 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cbcc2e32-825f-3d93-be4a-f14c72f2fc4a | -2.45782 | -53.69638 | 2024-11-21 04:55:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 21a2413f-6f77-3bf8-9e45-e9b398692125 | -4.15558 | -42.02105 | 2024-11-21 04:55:00 | NOAA-20 | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 9.8 |
| 7e164835-5356-36c1-a077-0a88f1d278f4 | -2.57345 | -53.97599 | 2024-11-21 04:55:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a1f59007-7989-377d-ac69-ed324ebe80af | -3.10984 | -53.17901 | 2024-11-21 04:55:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 71bd890a-2471-3fd5-844a-64b8b0f7e72f | -3.54213 | -50.53645 | 2024-11-21 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e805e940-cfcd-3d0e-88b7-e4d85b4aca69 | -4.76628 | -44.4929 | 2024-11-21 04:55:00 | NOAA-20 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 30485de0-f521-36ec-87fe-664a5463ac62 | -2.45397 | -53.69931 | 2024-11-21 04:55:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 725bbbba-ecea-3c0b-89b2-4b613a786346 | -2.62204 | -54.29392 | 2024-11-21 04:55:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bd0c426e-cc14-3fcd-8ac0-18b82627b19d | -3.11203 | -53.74928 | 2024-11-21 04:55:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 30fc2143-17b3-3eee-aab1-18be985bff9b | -2.28742 | -53.63416 | 2024-11-21 04:55:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f8b3caa8-ec2f-3df9-bc0f-6d60ab709f58 | -4.39035 | -47.77779 | 2024-11-21 04:55:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e9dcef46-9fb4-30f9-816f-d44e3f99c354 | -2.78966 | -54.15593 | 2024-11-21 04:55:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c3fe6efd-7c07-3249-8ece-5870ecffcf18 | -3.71587 | -51.84362 | 2024-11-21 04:55:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| aa994f31-e81e-3952-898b-e7aa5cbe78b1 | -2.67128 | -51.88472 | 2024-11-21 04:55:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 09248a36-e391-34de-9a09-0c9c6d57f780 | -4.19545 | -53.49344 | 2024-11-21 04:55:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6154f6db-b847-3b83-a74c-64d3dbe27576 | -3.04919 | -54.40379 | 2024-11-21 04:55:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a1387026-f6b7-371f-a69a-3589157fc15e | -6.11724 | -42.51578 | 2024-11-21 04:55:00 | NOAA-20 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 10.4 |
| fc06e5d1-ecfd-3f5a-b099-ca484590c407 | -3.5679 | -51.35118 | 2024-11-21 04:55:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0a293903-46ca-3e80-b5ea-87bf662b2735 | -2.59952 | -54.04758 | 2024-11-21 04:55:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c8659d66-a734-3f41-87e4-ea9298916b9e | -3.49914 | -48.22203 | 2024-11-21 04:55:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2ad0a1e0-0978-30e0-962a-9f65f4ebb7be | -2.5729 | -53.97946 | 2024-11-21 04:55:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 58b1165a-a920-36ea-9751-d5b9fb25159b | -2.79945 | -54.00812 | 2024-11-21 04:55:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4959497a-6c61-3f90-aa4d-7c87d3b00114 | -4.2471 | -46.12205 | 2024-11-21 04:55:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 25.0 |


[Clique aqui para ver as próximas entradas](README66.md)
