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

## Dados Diários - Página 56

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1519470c-72a1-3964-bb44-0f3600fbcbc7 | -4.03573 | -48.29975 | 2024-11-28 04:25:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9fe2378d-c8a2-3010-bdcf-b60ffcf89e92 | -4.68475 | -47.49377 | 2024-11-28 04:25:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a39712b1-0485-3859-b3b3-70f9059252dd | -2.86601 | -46.86652 | 2024-11-28 04:25:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0eddf33e-4ff4-36e7-b87d-145120a758ab | -2.82916 | -54.05857 | 2024-11-28 04:25:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b35fc45a-7cfe-3d06-8adf-8b9530eb1aff | -3.29089 | -45.5117 | 2024-11-28 04:25:00 | NOAA-20 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 67.8 |
| b4d60ede-05cb-335c-bf94-9e710e746c25 | -3.46822 | -51.6266 | 2024-11-28 04:25:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e6e63fa9-34d2-3e1c-afbe-7090e57e34e6 | -3.14327 | -48.53327 | 2024-11-28 04:25:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8e65de1a-f82c-3b0d-a2e6-5c09ea77deb6 | -2.74091 | -51.65567 | 2024-11-28 04:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0e1d6093-3ae7-31fa-ba3e-601d1af31214 | -2.16792 | -52.13995 | 2024-11-28 04:25:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 7d69afb0-453e-3baf-b4ea-d50b3569b312 | -3.24538 | -53.64611 | 2024-11-28 04:25:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 633b4cfe-6c58-3df4-884a-3848984283cf | -3.39543 | -50.30424 | 2024-11-28 04:25:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 17ff69f1-6c38-305c-b6d6-eaae554403c9 | -2.83573 | -46.83971 | 2024-11-28 04:25:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 907e7999-4d36-3605-9ffd-7bb7d1476529 | -3.49198 | -44.70518 | 2024-11-28 04:25:00 | NOAA-20 | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 526c84ed-cd03-3f7c-af10-b951ced85e09 | -3.48777 | -50.08224 | 2024-11-28 04:25:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6fe5ff76-2918-3d48-9df0-dab2bb802ced | -3.9749 | -46.73013 | 2024-11-28 04:25:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1d094f8c-6e6f-3405-baac-283110dd889b | -4.77779 | -44.42886 | 2024-11-28 04:25:00 | NOAA-20 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 3747c638-0743-3e95-b514-dac1b3df2ee8 | -4.22696 | -50.88195 | 2024-11-28 04:25:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 73d24781-9103-3206-844f-c80218ddf55e | -3.80077 | -44.46873 | 2024-11-28 04:25:00 | NOAA-20 | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4b24e939-5995-3e62-9387-9325f968b8bc | -2.85818 | -46.85054 | 2024-11-28 04:25:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 35a8c07e-f8e4-301a-9d17-c8717cf1e81f | -3.46714 | -51.59447 | 2024-11-28 04:25:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d0005668-9f49-3164-a0f4-594c90f3a3cd | -4.18761 | -40.55968 | 2024-11-28 04:25:00 | NOAA-20 | VARJOTA | CEARÁ | Brasil | 2313955 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 2acac0ec-859b-365c-86b0-c7f0fff673fb | -3.41064 | -50.16157 | 2024-11-28 04:25:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 5c37a54d-c3a7-3cfd-9703-921551de26c2 | -3.49525 | -53.81189 | 2024-11-28 04:25:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9b4cb045-6b8d-33be-8bc0-cf90788fa959 | -2.89138 | -48.27571 | 2024-11-28 04:25:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ee1a9039-5559-3f12-8042-f8d5b1f37047 | -1.49726 | -54.46532 | 2024-11-28 04:25:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 13.7 |
| 0118fa2a-75bc-37df-a020-89fb4c74a941 | -2.84635 | -46.85975 | 2024-11-28 04:25:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c0806b01-eb84-3f44-886d-2eb701329f10 | -2.85756 | -46.87622 | 2024-11-28 04:25:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c14cbfdf-ced3-39ec-8133-551c054f8c21 | -3.13084 | -50.25632 | 2024-11-28 04:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 12.6 |
| 22165df2-9c30-3e31-bebd-5e89e32821c1 | -3.08946 | -50.36158 | 2024-11-28 04:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ab69b36d-0b05-3060-baea-d736172828a4 | -4.06084 | -48.83772 | 2024-11-28 04:25:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 45e39902-bdda-3f89-991a-46caa88947d1 | -3.38352 | -50.10617 | 2024-11-28 04:25:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 65bf1a26-3544-3b80-86ec-495c3bd867f1 | -5.21274 | -41.28321 | 2024-11-28 04:25:00 | NOAA-20 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 0528869d-246b-3938-a4b1-683c5a45d7df | -3.44489 | -44.59384 | 2024-11-28 04:25:00 | NOAA-20 | ANAJATUBA | MARANHÃO | Brasil | 2100709 | 21 | 33 | nan | nan | nan | Amazônia | 0.4 |
| a817a764-15a8-37c6-93d7-3f989a766f0d | -2.87118 | -46.81225 | 2024-11-28 04:25:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0fbfe11e-ef1e-3e87-bc6c-56181df747be | -2.84025 | -46.83308 | 2024-11-28 04:25:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cb6b91a4-8f88-3759-b275-123127507399 | -3.02898 | -54.02448 | 2024-11-28 04:25:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 45cc449e-7361-32ef-8c8f-e0731ad55c3c | -2.84749 | -54.01094 | 2024-11-28 04:25:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b555bfbf-4ebf-36ac-99bf-ea6388eb86ec | -3.01427 | -48.05004 | 2024-11-28 04:25:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 09ca1012-8c6d-369d-b1a0-b8b11966a63c | -2.84265 | -54.0736 | 2024-11-28 04:25:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d9eb4939-7dea-330f-9a51-c9917a8edbcc | -3.59483 | -49.99163 | 2024-11-28 04:25:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| e9e5f40e-a064-39d4-92d9-b7dbf237fc80 | -4.81991 | -44.49024 | 2024-11-28 04:25:00 | NOAA-20 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ad2fdaf4-121f-39db-9762-ad5adf335e5e | -3.94873 | -46.72243 | 2024-11-28 04:25:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 060b0070-b4e6-3bc1-b100-8f46dddd9d20 | -15.56999 | -47.85615 | 2024-11-28 04:25:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2f28e359-de42-39ed-b4dc-59116782080a | -4.81007 | -43.30618 | 2024-11-28 04:25:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c26e6d04-2428-3a82-a076-5c0503273d87 | -3.34709 | -50.52434 | 2024-11-28 04:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| ed44a633-8e80-3f13-8535-6d285c2cdb73 | -3.2878 | -50.75725 | 2024-11-28 04:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1fc9308f-e24c-3e5f-a8ce-8cc9062a6965 | -3.94911 | -41.49461 | 2024-11-28 04:25:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 11c5bbed-aef7-32b3-9e66-24c4ac41ab37 | -2.86444 | -46.81121 | 2024-11-28 04:25:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0082ca53-cccc-3f99-8ee3-2960bf2c2cbb | -3.43676 | -50.12482 | 2024-11-28 04:25:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c43fc3d4-c9e1-3c7f-a732-5e59e3a2d648 | -1.75111 | -52.66065 | 2024-11-28 04:25:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 973617ed-e64f-336b-89f8-7bcdd32cce1a | -3.28374 | -45.51411 | 2024-11-28 04:25:00 | NOAA-20 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 6b081c24-2523-3f53-a0ea-efaa4fea1061 | -2.8475 | -46.85257 | 2024-11-28 04:25:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8afb39e6-2253-3296-b5fb-fc87cf170d8c | -3.53017 | -50.7556 | 2024-11-28 04:25:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e53f7ba3-9958-311b-8fe8-382ca6342e53 | -3.95964 | -46.91268 | 2024-11-28 04:25:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fff7a108-757c-30d7-a8f4-352a31a897c9 | -3.60148 | -52.54294 | 2024-11-28 04:25:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| e375be99-f56a-38b5-b4ce-6a3816ec8d51 | -3.50647 | -50.31411 | 2024-11-28 04:25:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6cfb5f2f-4039-3ff2-89a5-8b5ea0d0bc3a | -2.86838 | -46.80816 | 2024-11-28 04:25:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 169874e4-bf0a-3f73-8582-a4251d5a7aa2 | -2.75716 | -52.10357 | 2024-11-28 04:25:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3cf99bc8-9264-3324-8ed6-f95bc796b839 | -2.95949 | -53.88818 | 2024-11-28 04:25:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 546a8976-ed52-3d3a-b0b2-9023acc2345a | -4.21823 | -50.88433 | 2024-11-28 04:25:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b73cdba8-20ec-37aa-8c74-1844ff70845c | -4.35375 | -48.68818 | 2024-11-28 04:25:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1e033c6b-0039-33ab-aea2-bf796bcb026e | -3.6718 | -45.78984 | 2024-11-28 04:25:00 | NOAA-20 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f58662f4-a065-366b-b756-31f4bcae57d1 | -3.82447 | -46.54447 | 2024-11-28 04:25:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 09188709-79c2-3d75-b146-94f8d3adde54 | -5.57893 | -43.14996 | 2024-11-28 04:25:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Caatinga | 4.1 |
| a45aa570-9303-3bd1-9946-9ebe79af09d2 | -2.81676 | -46.84064 | 2024-11-28 04:25:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0e1fed4e-4b06-3f24-a5f9-eaa9a3cbf8b4 | -3.69367 | -51.36884 | 2024-11-28 04:25:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| dca32679-2d53-3a94-b23b-662518dd8338 | -3.09207 | -53.25954 | 2024-11-28 04:25:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 81511504-891a-3f41-a050-cf35ec9ee00e | -3.34787 | -46.6138 | 2024-11-28 04:25:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 47cba309-9784-34d5-94b1-adb74a286805 | -4.92264 | -47.14058 | 2024-11-28 04:25:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 02f72938-af7f-3a8f-99a3-b8774e01af14 | -3.84693 | -51.38464 | 2024-11-28 04:25:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1de0cfea-33c3-375a-bf85-3ab923f28988 | -2.54329 | -53.99418 | 2024-11-28 04:25:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 872c24a2-0c6a-34f4-af73-ca6ce20b8d4d | -2.30895 | -51.96191 | 2024-11-28 04:25:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 2d98c3f1-983c-3cdf-8e64-42d764f45883 | -3.2472 | -53.63483 | 2024-11-28 04:25:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| c02b3caa-ece9-3aa7-bf0f-f0aa3dfd3643 | -3.03809 | -50.98062 | 2024-11-28 04:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| e889711d-62cb-3c20-9f1f-740e8f251907 | -4.84122 | -44.28759 | 2024-11-28 04:25:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c0537bdb-25e1-302f-a497-a24f5865256b | -3.97212 | -46.72607 | 2024-11-28 04:25:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fe66a5f8-e72a-31e8-9f7e-a8fa9f7df7ac | -3.11334 | -53.75916 | 2024-11-28 04:25:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5da884b7-3a0d-39b6-9bf0-eaaa8feb17f1 | -2.60578 | -53.97784 | 2024-11-28 04:25:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ff66dba7-7877-375f-bb43-2b18d7e69196 | -3.82622 | -47.46586 | 2024-11-28 04:25:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d52271b4-a83e-3afd-8982-9f4813e7a1f9 | -3.27727 | -50.59321 | 2024-11-28 04:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e0154930-e2af-3859-9489-b005f9f1e84f | -3.89829 | -50.20267 | 2024-11-28 04:25:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2d1f27f0-55ea-3ce6-adcc-82fa0b153474 | -4.36334 | -47.21767 | 2024-11-28 04:25:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 16eb2d5b-7fbe-37c5-abd5-92639550870a | -3.29387 | -50.54147 | 2024-11-28 04:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8e0dad6b-7206-3432-8b0c-ce4ac8677a02 | -3.85971 | -40.44379 | 2024-11-28 04:25:00 | NOAA-20 | CARIRÉ | CEARÁ | Brasil | 2303105 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 29bfb044-df51-3a8a-8d1a-b43378f25cc3 | -3.8478 | -46.65257 | 2024-11-28 04:25:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2cfe22f6-3069-3b7a-be5c-5f97464cf701 | -2.8401 | -52.54305 | 2024-11-28 04:25:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 95f9eb24-ec16-30f3-bfd3-1ce77e568328 | -3.09385 | -51.03266 | 2024-11-28 04:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6c030f53-a542-3f77-bf1e-6641b55b0e56 | -4.77166 | -45.92414 | 2024-11-28 04:25:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f1dd64cb-99f1-3670-8c29-e8ccf8929e46 | -2.62386 | -53.99696 | 2024-11-28 04:25:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 22d8bac9-cdc5-3f90-b6d4-cc46e9e8179d | -3.10442 | -53.8191 | 2024-11-28 04:25:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 218e25b6-4459-3811-98d4-88c5cacbf691 | -3.02486 | -54.01751 | 2024-11-28 04:25:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a505dd3c-a9bc-389c-959c-a57805ffa68f | -2.59083 | -53.97216 | 2024-11-28 04:25:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 01ba6d0d-a2b3-3a1f-bd37-e2fb4eeec5a2 | -4.2556 | -48.07469 | 2024-11-28 04:25:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a80e96bf-7dda-3934-be9f-c8ee9cc85cf0 | -2.91634 | -51.7139 | 2024-11-28 04:25:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c80f858b-d81f-34d2-8fe2-d4bf67a128de | -3.04495 | -48.51429 | 2024-11-28 04:25:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b3df7369-8fa5-367c-bfb9-49e6fc5e042f | -2.92807 | -49.43554 | 2024-11-28 04:25:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ecd5c5a5-920f-37e6-b1f0-33a9846c91a0 | -2.84305 | -46.83717 | 2024-11-28 04:25:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 37eab263-beee-3233-b761-84a3376af4f6 | -3.24624 | -46.41865 | 2024-11-28 04:25:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 01ac7320-02a0-3723-afee-2ba91caa0805 | -2.69092 | -51.71507 | 2024-11-28 04:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4acb052c-4daf-31da-847a-958bf600fe54 | -5.08505 | -45.98407 | 2024-11-28 04:25:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |


[Clique aqui para ver as próximas entradas](README57.md)
