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

## Dados Diários - Página 23

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 81bf5f10-41e4-3b08-a970-527f94d3e286 | -4.42 | -45.88214 | 2024-12-10 04:53:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 980c6f4a-675f-31e0-86c4-257585d89eef | -2.83068 | -53.06806 | 2024-12-10 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| e7bbd465-8a7d-3ae4-aceb-90e4e8198174 | -2.78957 | -53.24214 | 2024-12-10 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 6c4d4935-526a-3dd5-acbb-f00d42a3f2c2 | -10.02668 | -53.74982 | 2024-12-10 04:53:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 6276b9ad-259e-3f0b-bbf0-a4ce04e91837 | -6.82724 | -44.38582 | 2024-12-10 04:53:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 7184ecf6-37f6-32fe-be3e-4b80c9753e6a | -2.38137 | -48.60194 | 2024-12-10 04:53:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3b2b9667-f4fc-380c-a756-76555711f032 | -11.41982 | -54.32269 | 2024-12-10 04:53:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5f26c692-7a66-3bf7-9931-5e1ff710b479 | -3.29774 | -51.12206 | 2024-12-10 04:53:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 757b57c1-2212-38db-8cdd-b6b22accc5cd | -1.72568 | -52.47827 | 2024-12-10 04:53:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b0c0f2c0-4a1c-39c1-b2e6-6866b2b02d8f | -1.4265 | -60.07273 | 2024-12-10 04:53:00 | NOAA-21 | PRESIDENTE FIGUEIREDO | AMAZONAS | Brasil | 1303536 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 730bf95b-0b1d-3b35-87d1-627e737d3555 | -3.09265 | -53.21724 | 2024-12-10 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e1a415ae-25b0-3449-a5f8-645a3e97cb15 | -2.62418 | -48.0654 | 2024-12-10 04:53:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 285dce3f-1ff2-3140-ab64-1f95a49ebd58 | -6.91208 | -43.51295 | 2024-12-10 04:53:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 4de578bc-41b8-349b-bd1b-fe754c4cb614 | -2.83402 | -53.06858 | 2024-12-10 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 00d9113e-57a5-355a-a435-dd9bb1829624 | -2.81676 | -53.04795 | 2024-12-10 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c1045bf6-4b00-3be4-9e0e-e53c3ff2581a | -11.88716 | -54.68017 | 2024-12-10 04:53:00 | NOAA-21 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0d42a883-2f32-39b0-b170-788ab67f12ac | -3.7759 | -50.05527 | 2024-12-10 04:53:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 47a2bcde-b1fc-3693-a570-4f7281d4b141 | -3.69971 | -50.93856 | 2024-12-10 04:53:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 957658c7-4d77-37e5-83de-4219284cf884 | -1.64681 | -54.61647 | 2024-12-10 04:53:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 944a2d29-3b90-31eb-a40e-1bff47246ad8 | -2.99172 | -53.01774 | 2024-12-10 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 54f7d875-7d18-367d-9bb9-23fe37b81ba0 | -3.27328 | -53.04409 | 2024-12-10 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5aba19d0-f6b1-3b94-b30d-998af1b39130 | -2.5539 | -53.97656 | 2024-12-10 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a0280182-780f-3956-979e-325bce82f72c | -2.41294 | -53.66848 | 2024-12-10 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3b1fe3a0-0dd8-3fbb-b3c3-3314fd370346 | -10.35794 | -57.25105 | 2024-12-10 04:53:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 3987512d-90e5-3f05-b7f5-20dc58f7ec55 | -2.95248 | -53.11571 | 2024-12-10 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 1baea772-cb08-3fa7-badf-3d2994e8efc1 | -3.51398 | -52.18019 | 2024-12-10 04:53:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 94263775-63fc-306a-8d33-4d98d60373a5 | -2.85635 | -52.55598 | 2024-12-10 04:53:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5d6d90b4-c85e-3409-8ef4-87995d83d35a | -3.07212 | -54.07468 | 2024-12-10 04:53:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c6450489-69c0-37c4-ac7a-469eea0d48c2 | -3.37088 | -51.19826 | 2024-12-10 04:53:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7ca45060-0fa4-3363-93a3-6eb559424bee | -1.49294 | -52.31419 | 2024-12-10 04:53:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2ad7b5fe-34eb-3237-8c5f-9c76f0b1daad | -2.77372 | -44.99752 | 2024-12-10 04:53:00 | NOAA-21 | SÃO BENTO | MARANHÃO | Brasil | 2110500 | 21 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 3db632c5-836d-3bfd-979f-e14db1699b8e | -10.42588 | -56.26284 | 2024-12-10 04:53:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a33b47bd-4130-3082-add8-6af73a872efd | -6.83795 | -44.38394 | 2024-12-10 04:53:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 10.8 |
| e988ed04-58cc-315a-9a40-e00b8cb0d073 | -3.08984 | -54.07359 | 2024-12-10 04:53:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 01d2e144-ef03-332f-8722-002679108ef9 | -3.08816 | -53.35397 | 2024-12-10 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e09f9325-4f25-36a8-83e2-72c19dad8d91 | -6.45597 | -45.75497 | 2024-12-10 04:53:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 601674e7-ecbb-3fda-b748-40d5bea214ba | -3.09823 | -53.24692 | 2024-12-10 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 377bc222-f4f6-3647-bdca-db7dd0518c5c | -2.55735 | -53.42126 | 2024-12-10 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 11f429df-e795-3440-80fa-b380e8bc2d87 | -6.91 | -43.51752 | 2024-12-10 04:53:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 33b8aa4d-f459-3a0b-ad05-21b3d03c4dd6 | -2.96298 | -53.72006 | 2024-12-10 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 191877b3-eb7c-36f5-9eff-61ce97f01d8f | -1.88386 | -53.28774 | 2024-12-10 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b560959f-8fed-30c3-9341-bab022cb7272 | -2.8013 | -53.23299 | 2024-12-10 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9bb06d06-e61f-3b00-af49-7bf0c3d9f308 | -2.99505 | -53.01825 | 2024-12-10 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 7d36d469-a201-3949-8751-495b576881b0 | -2.96583 | -53.11776 | 2024-12-10 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a3cac3b4-d9e5-3f40-beaf-c0da652e5a09 | -3.30241 | -53.85825 | 2024-12-10 04:53:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7de62683-3c88-3bd7-b7f6-053c83a736a9 | -3.8544 | -40.44151 | 2024-12-10 04:53:00 | NOAA-21 | CARIRÉ | CEARÁ | Brasil | 2303105 | 23 | 33 | nan | nan | nan | Caatinga | 2.1 |
| bf51098e-9aec-3055-a426-55fe5b61822d | -11.41927 | -54.3262 | 2024-12-10 04:53:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| de644824-5d92-3179-a34a-2afef98d543d | -3.24642 | -53.64204 | 2024-12-10 04:53:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 105a1b35-e2d2-3529-9a3d-f68ba7bdfee6 | -3.71701 | -52.44748 | 2024-12-10 04:53:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2b6a1ad6-685b-3243-bf97-1aa82c35e9a7 | -2.55342 | -53.42432 | 2024-12-10 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 192200a6-e13d-387b-aba0-fb4b8db8dff6 | -2.42195 | -46.30434 | 2024-12-10 04:53:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3e857e59-edff-395f-ad24-5aa7e0fd02c3 | -3.82072 | -52.24244 | 2024-12-10 04:53:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 942077a4-e7b9-3b95-85bc-035a4da5c016 | -2.37414 | -54.46693 | 2024-12-10 04:53:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2f61815a-533b-30a9-9f48-289288a7929c | -3.81677 | -52.35445 | 2024-12-10 04:53:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fef04fb9-35b1-3fe7-8203-065b117387c6 | -2.55848 | -53.4141 | 2024-12-10 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 96b93752-1fa3-3d4d-bd49-950f85b1a171 | -2.77952 | -53.2406 | 2024-12-10 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 336a6c6c-6369-33e0-b8d2-1ad4e9e11ffc | -1.42268 | -53.49365 | 2024-12-10 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| cfe4791d-5b09-3257-8018-c1a0f7c76fc2 | -2.44908 | -49.0239 | 2024-12-10 04:53:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 03307d9a-d91b-3cb8-8218-c98643faeb28 | -3.09969 | -53.74105 | 2024-12-10 04:53:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e5c3c75f-f6cc-3b0d-8fde-f0b0fda78f4d | -12.85536 | -51.93499 | 2024-12-10 04:53:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| e5422ea2-3e91-3a1c-8831-9f7a928373b4 | -3.06248 | -54.24542 | 2024-12-10 04:53:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| bc2d14cb-4acb-32ad-a833-a18b86aba0ba | -3.00122 | -53.04427 | 2024-12-10 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 10f2bfba-54d0-395d-a1ac-ef356752af43 | -2.75266 | -54.59093 | 2024-12-10 04:53:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| fab72a37-7520-399c-a2ed-1d22fdf626b9 | -10.50913 | -44.93499 | 2024-12-10 04:53:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a860d0b7-bdf5-3adb-8aa7-d7606e9d244d | -1.46404 | -52.45481 | 2024-12-10 04:53:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1764f285-f0cf-3ef7-987c-f5cfc6697c4f | -6.02527 | -46.24916 | 2024-12-10 04:53:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5f770bf9-5be4-354f-a33b-1a522227d0d8 | -3.20441 | -46.81048 | 2024-12-10 04:53:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| e0c0570d-41ec-38a8-8f2d-04b2e05fc43e | -3.76399 | -54.40734 | 2024-12-10 04:53:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 33f1e992-bfe4-34e6-8ca8-d552112532ea | -3.39332 | -52.66812 | 2024-12-10 04:53:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| ed5c143a-5e0b-31ab-8fda-c7edfad97dfa | -6.91705 | -43.51731 | 2024-12-10 04:53:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 0dfe7adb-5665-398d-be0d-194e0dff0d01 | -3.79617 | -50.01572 | 2024-12-10 04:53:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4c7b6f9a-c1ac-3a92-bf88-513f0defe50e | -2.78118 | -54.049 | 2024-12-10 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| aaaff790-c0ac-3ed2-92e7-6cbdbc9ac752 | -2.82346 | -53.07054 | 2024-12-10 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| ebb3adf4-fbe6-3faf-8c7d-9bc9e54b84cc | -2.88597 | -49.12813 | 2024-12-10 04:53:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4fb12603-37aa-360e-aaf3-581b38b839fc | -12.37737 | -54.15731 | 2024-12-10 04:53:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b9dcb76b-9158-3a44-bc8e-bda3e1312446 | -10.38299 | -51.99974 | 2024-12-10 04:53:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0489d0c3-468a-3c50-90be-ab4c7bff4577 | -3.68863 | -51.82328 | 2024-12-10 04:53:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f2590fe8-ba4d-3de5-931e-992b32a9869b | -3.00755 | -48.04195 | 2024-12-10 04:53:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 121e7851-6114-336d-8175-6477cdde172e | -2.47962 | -47.61362 | 2024-12-10 04:53:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| a2fd7587-9a25-3418-bc28-e146f053bdca | -3.012 | -49.61051 | 2024-12-10 04:53:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 855e1952-fa7c-3ca5-953e-281eb1c01c74 | -3.79265 | -50.95243 | 2024-12-10 04:53:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f086319d-151e-3ba7-8b69-0f775f7d0db7 | -3.3424 | -53.2528 | 2024-12-10 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c687beef-c9a2-34fb-858d-2738f5e6db96 | -13.93817 | -44.36172 | 2024-12-10 04:53:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| ae2cf65f-9357-346d-bce8-d1f9457edccf | -4.0399 | -50.80364 | 2024-12-10 04:53:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| fd99c8d1-9af5-34ac-998a-75370fc3eee3 | -2.45594 | -53.7049 | 2024-12-10 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4d3f1bc8-9668-3133-89b9-360e4507ff21 | -4.54932 | -48.00537 | 2024-12-10 04:53:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 12f31c23-64ea-3309-9efe-50a9ba04f262 | -2.83281 | -53.01107 | 2024-12-10 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2a99ddde-65bd-327a-80ee-12edabe1316a | -3.08949 | -53.22031 | 2024-12-10 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 785dedac-e00d-3102-b310-9510079e420b | -3.42736 | -52.56105 | 2024-12-10 04:53:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| a4baf467-57ab-3110-9100-e23fdd9f7198 | -2.45537 | -53.70856 | 2024-12-10 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 304f7e8f-a5c0-3819-9472-ea2d623840ce | -3.20959 | -46.8038 | 2024-12-10 04:53:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 49ca524d-f328-34c2-bcbc-3d47775bb8df | -3.2776 | -51.0758 | 2024-12-10 04:53:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 381027a0-759f-3363-9544-e1ed43ec7cef | -2.41237 | -53.67213 | 2024-12-10 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| dff054cc-d5fc-3798-877f-a56fd6343bba | -3.47462 | -49.84764 | 2024-12-10 04:53:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 50fb6c71-f903-3847-bd1f-c5c24d973bbd | -3.8722 | -50.36388 | 2024-12-10 04:53:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 436a499f-b264-3e38-a4e6-83bba0c70f2a | -3.789 | -50.10744 | 2024-12-10 04:53:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| de71b8d8-8292-303a-abec-5e78a895a95f | -3.52849 | -54.58995 | 2024-12-10 04:53:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 4bba4487-5759-3a44-91c2-6b15cde75eba | -6.45133 | -45.75434 | 2024-12-10 04:53:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 39ed0f65-4e2d-3729-9540-f14fc24b3884 | -4.39256 | -47.76079 | 2024-12-10 04:53:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 19.5 |
| 332e957d-3ff9-3d82-b97d-f583349594c9 | -12.24614 | -52.45154 | 2024-12-10 04:53:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |


[Clique aqui para ver as próximas entradas](README24.md)
