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

## Dados Diários - Página 40

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9f581ba9-ea8d-3fb2-8291-b1d71872df9e | -6.49313 | -43.3368 | 2024-10-14 04:19:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8177be5c-c15d-340f-9232-5345258c28d6 | -6.47181 | -43.31898 | 2024-10-14 04:19:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| cbd01755-d5cb-3599-8325-16daf736b12d | -6.47127 | -43.32259 | 2024-10-14 04:19:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b3966bbb-da6c-39c1-a644-a304041da998 | -6.45957 | -43.33863 | 2024-10-14 04:19:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| fc78e64d-9ee2-3ca0-9788-85983d1974f3 | -6.45622 | -43.33809 | 2024-10-14 04:19:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ad8c3eee-60e3-3fe4-88f9-d2b50240afd3 | -6.45452 | -43.3269 | 2024-10-14 04:19:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| a901179c-0a85-3719-819c-6e49325e6a91 | -6.45397 | -43.33045 | 2024-10-14 04:19:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 3fb82172-13cc-34fb-a352-752f9bd013fa | -7.24218 | -43.48446 | 2024-10-14 04:19:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 6f2bcb7e-78a6-3beb-9838-2fbb600b9947 | -7.95105 | -42.67677 | 2024-10-14 04:19:00 | NOAA-21 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 419f0268-1dfe-3d22-9c2a-116b1c420889 | -7.75339 | -43.30329 | 2024-10-14 04:19:00 | NOAA-21 | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| ea1b517c-9e3f-3176-9b3b-1cd5d011bd60 | -7.72798 | -43.28811 | 2024-10-14 04:19:00 | NOAA-21 | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 2eaf382d-3125-3dc9-901d-c1db0641dbdc | -7.72671 | -43.20548 | 2024-10-14 04:19:00 | NOAA-21 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| e48b5f60-4e14-39d9-b1e4-a315afc53dd0 | -7.72615 | -43.20914 | 2024-10-14 04:19:00 | NOAA-21 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 812c9fd8-de01-3399-8b0f-c49256324578 | -7.7256 | -43.2128 | 2024-10-14 04:19:00 | NOAA-21 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 4f1508bc-43ef-35f8-a9de-5d53f11763f2 | -7.72504 | -43.21647 | 2024-10-14 04:19:00 | NOAA-21 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 7532ef17-d036-35d6-8260-7ef085e206e5 | -7.7246 | -43.28758 | 2024-10-14 04:19:00 | NOAA-21 | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| addb750f-7106-37f0-a84e-7132a4557783 | -7.72448 | -43.22015 | 2024-10-14 04:19:00 | NOAA-21 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 0f23fc77-9801-368b-b25f-d901c4af74f0 | -7.72392 | -43.22382 | 2024-10-14 04:19:00 | NOAA-21 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| fed7b691-a301-3704-9b88-95e287b3c041 | -7.72388 | -43.20126 | 2024-10-14 04:19:00 | NOAA-21 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 50afc5e6-1166-3f36-aa10-bfa04e7a16b8 | -7.72332 | -43.20494 | 2024-10-14 04:19:00 | NOAA-21 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 12d2ddfe-22ff-3e66-906c-5f26236aa5c9 | -7.72109 | -43.21959 | 2024-10-14 04:19:00 | NOAA-21 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 56f6ca7c-2d5c-3616-ac9a-1d930eefcb7f | -7.72104 | -43.19703 | 2024-10-14 04:19:00 | NOAA-21 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 1268b2dc-7f3d-3c18-9575-b5f3d3864639 | -7.72053 | -43.22327 | 2024-10-14 04:19:00 | NOAA-21 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 879f4a5d-baf7-3650-967a-bfe324086466 | -7.72048 | -43.20073 | 2024-10-14 04:19:00 | NOAA-21 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 3139dda4-bc89-3a00-be22-094d1a2d3458 | -7.71821 | -43.19281 | 2024-10-14 04:19:00 | NOAA-21 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| ad5697b5-00a0-3e1e-a255-380b547d9185 | -7.71765 | -43.1965 | 2024-10-14 04:19:00 | NOAA-21 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 526c2d54-f851-3f23-94d5-a5f9f7c4465c | -7.70757 | -43.23997 | 2024-10-14 04:19:00 | NOAA-21 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| bfbcd68d-c58c-3fd9-bb9d-d351459a3495 | -7.70701 | -43.24362 | 2024-10-14 04:19:00 | NOAA-21 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| c91ce957-cc8c-3458-ac9b-52bb2ab415cf | -7.70585 | -43.22842 | 2024-10-14 04:19:00 | NOAA-21 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 1ba62dd9-bfe5-32e9-8fc0-c6b20af36e50 | -7.70346 | -43.17538 | 2024-10-14 04:19:00 | NOAA-21 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 301473d4-41fb-35e9-a2c4-76b0c4730b63 | -7.7029 | -43.17908 | 2024-10-14 04:19:00 | NOAA-21 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| fb40b9e1-1312-3550-91c8-3dcbed7770c7 | -7.70246 | -43.22789 | 2024-10-14 04:19:00 | NOAA-21 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 562252f8-760c-352e-b6f4-0d23f0c023ad | -7.69894 | -43.18227 | 2024-10-14 04:19:00 | NOAA-21 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 2453427d-ebe2-3a54-ab6c-4348fa53b552 | -7.69048 | -43.19225 | 2024-10-14 04:19:00 | NOAA-21 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 2ed14f1f-d0c6-34e9-98ce-5055be59d338 | -7.55195 | -42.90173 | 2024-10-14 04:19:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 40c32333-9068-3cd9-a554-32fa9ea208df | -7.55138 | -42.9055 | 2024-10-14 04:19:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 388b5822-7227-36f4-a029-376ea3d74ffe | -8.33627 | -42.74571 | 2024-10-14 04:19:00 | NOAA-21 | BREJO DO PIAUÍ | PIAUÍ | Brasil | 2201988 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 6a32c48c-85c8-35d8-b682-3e7cbc34500c | -8.33396 | -42.73744 | 2024-10-14 04:19:00 | NOAA-21 | BREJO DO PIAUÍ | PIAUÍ | Brasil | 2201988 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 386cafcf-737b-31e0-91f4-29a767dce21a | -8.33338 | -42.7413 | 2024-10-14 04:19:00 | NOAA-21 | BREJO DO PIAUÍ | PIAUÍ | Brasil | 2201988 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 27dcb8d3-cc54-3301-92bd-d5ef88d2d3ce | -8.3328 | -42.74516 | 2024-10-14 04:19:00 | NOAA-21 | BREJO DO PIAUÍ | PIAUÍ | Brasil | 2201988 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 6f129f8d-6d9f-3cb5-a266-a91394370e87 | -8.33222 | -42.74902 | 2024-10-14 04:19:00 | NOAA-21 | BREJO DO PIAUÍ | PIAUÍ | Brasil | 2201988 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 8ee213c4-8e82-30ee-8760-7c66c5f9329e | -8.33164 | -42.75287 | 2024-10-14 04:19:00 | NOAA-21 | BREJO DO PIAUÍ | PIAUÍ | Brasil | 2201988 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 11a4482b-46f6-3063-bfc2-50bae58d8655 | -8.32933 | -42.74462 | 2024-10-14 04:19:00 | NOAA-21 | BREJO DO PIAUÍ | PIAUÍ | Brasil | 2201988 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| eb90c56b-41c0-3695-8386-81b6853bbb95 | -8.32875 | -42.74848 | 2024-10-14 04:19:00 | NOAA-21 | BREJO DO PIAUÍ | PIAUÍ | Brasil | 2201988 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 2c22c885-14e2-375b-812b-e9c617f93c07 | -8.32701 | -42.73635 | 2024-10-14 04:19:00 | NOAA-21 | BREJO DO PIAUÍ | PIAUÍ | Brasil | 2201988 | 22 | 33 | nan | nan | nan | Caatinga | 5.4 |
| 9e11a4aa-fe5c-31d7-845f-c173c12f63bd | -8.32644 | -42.74022 | 2024-10-14 04:19:00 | NOAA-21 | BREJO DO PIAUÍ | PIAUÍ | Brasil | 2201988 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |
| b25c594b-562f-3906-8117-77a6469c125f | -8.32586 | -42.74408 | 2024-10-14 04:19:00 | NOAA-21 | BREJO DO PIAUÍ | PIAUÍ | Brasil | 2201988 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 81788422-51bd-3ef0-9354-f27f06ab0516 | -8.32528 | -42.74793 | 2024-10-14 04:19:00 | NOAA-21 | BREJO DO PIAUÍ | PIAUÍ | Brasil | 2201988 | 22 | 33 | nan | nan | nan | Caatinga | 5.4 |
| 1179e48b-4fa2-390a-8c1a-b2a90063c12d | -8.32297 | -42.73967 | 2024-10-14 04:19:00 | NOAA-21 | BREJO DO PIAUÍ | PIAUÍ | Brasil | 2201988 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 1f0b7c50-65d6-368e-a39e-9a7f59117624 | -8.32239 | -42.74353 | 2024-10-14 04:19:00 | NOAA-21 | BREJO DO PIAUÍ | PIAUÍ | Brasil | 2201988 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |
| ca6e9fc7-7027-3d65-8065-8c824ac7eea7 | -8.1384 | -43.01228 | 2024-10-14 04:19:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 4a645c93-fec9-3e6d-b535-79d8425b676c | -8.13783 | -43.01604 | 2024-10-14 04:19:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 84b9ec54-80fd-3f96-a628-4ee3f89db131 | -8.13668 | -43.02354 | 2024-10-14 04:19:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 4c5e7748-cb0d-3e3e-8651-9f1bf5ec662d | -8.13555 | -43.00801 | 2024-10-14 04:19:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| adb013f9-071c-322b-8c3d-9090f838d58f | -3.4329 | -43.06935 | 2024-10-14 04:19:00 | NOAA-21 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| f4c9dc74-f281-3d76-b1af-83b4e23acbbf | -3.43235 | -43.07284 | 2024-10-14 04:19:00 | NOAA-21 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| d6944f5d-5bf5-3952-9d83-99350b537780 | -3.42957 | -43.06883 | 2024-10-14 04:19:00 | NOAA-21 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| daa9cd5d-5d30-3f41-b1a9-fb420ea12609 | -3.42903 | -43.07233 | 2024-10-14 04:19:00 | NOAA-21 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 37d4c2d9-1043-3f80-8231-74734d305bc3 | -3.42625 | -43.06831 | 2024-10-14 04:19:00 | NOAA-21 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| c992fb00-9aac-3610-9b10-9afbca50a42c | -3.41313 | -43.34725 | 2024-10-14 04:19:00 | NOAA-21 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 84603e28-b1ce-3d2e-887f-5cc6f7378e30 | -3.41259 | -43.35071 | 2024-10-14 04:19:00 | NOAA-21 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 89a31cd6-0402-36d0-8960-914692df8781 | -3.40597 | -43.34969 | 2024-10-14 04:19:00 | NOAA-21 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b73c28dc-c03a-3e73-9c65-a12dfdb13704 | -3.40543 | -43.35314 | 2024-10-14 04:19:00 | NOAA-21 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 58805cfa-fcc7-34cd-aa83-7db4c1d66db6 | -3.40266 | -43.34917 | 2024-10-14 04:19:00 | NOAA-21 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| dbac043d-3747-337e-998f-76f7f57a420d | -3.38778 | -42.98721 | 2024-10-14 04:19:00 | NOAA-21 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0c4f69b1-e3c9-3285-99d5-e1863ba839f2 | -3.38724 | -42.99071 | 2024-10-14 04:19:00 | NOAA-21 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6e5f507e-d4a4-3eaf-85cc-75c29c04a9ee | -3.38391 | -42.9902 | 2024-10-14 04:19:00 | NOAA-21 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 06cc23a7-b706-313a-8cb8-d33d9cc0b465 | -3.31923 | -44.18783 | 2024-10-14 04:19:00 | NOAA-21 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2efe8d51-ca7e-38de-a945-437db5ae0e08 | -3.31593 | -44.18732 | 2024-10-14 04:19:00 | NOAA-21 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| db71d638-4a3b-391e-9b00-0bf6794009b5 | -5.05014 | -43.41018 | 2024-10-14 04:19:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| ae5b1013-3555-3dc4-a222-008e430c6756 | -3.95016 | -44.43898 | 2024-10-14 04:19:00 | NOAA-21 | SÃO MATEUS DO MARANHÃO | MARANHÃO | Brasil | 2111508 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7839917f-7953-353b-baf9-235c0e5f2b20 | -4.81779 | -44.35485 | 2024-10-14 04:19:00 | NOAA-21 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 58f1b589-2679-3641-a170-0813846f32a6 | -4.5483 | -43.5748 | 2024-10-14 04:19:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 09646f68-389b-37ed-8a94-d868c819cd0a | -4.54445 | -43.57775 | 2024-10-14 04:19:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f0909b5d-e7c2-371c-91c8-48d591bfde7c | -4.43219 | -43.92795 | 2024-10-14 04:19:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9ac0ebee-588c-336f-a2df-d856ae76caaf | -4.46722 | -44.3557 | 2024-10-14 04:19:00 | NOAA-21 | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a0a43108-bc58-353d-a072-28cc2fc6d7c0 | -4.04265 | -44.28519 | 2024-10-14 04:19:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e674210b-2ac5-35ac-a24e-0ba214d39102 | -4.04211 | -44.28863 | 2024-10-14 04:19:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2f207dcc-2299-33d0-8712-952c8d701196 | -4.03935 | -44.28468 | 2024-10-14 04:19:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e61c5e30-abb0-35d3-ae18-a66e0dc16a7c | -4.03881 | -44.28811 | 2024-10-14 04:19:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7aba3227-8d66-3f6e-8b87-c34009f0b73a | -6.1711 | -44.60108 | 2024-10-14 04:19:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 6ee0e905-8f63-3a35-806b-69ff92eae12e | -6.16835 | -44.59711 | 2024-10-14 04:19:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 0f5dcac8-d02c-3407-8125-7e969a4d8a37 | -6.16515 | -44.46247 | 2024-10-14 04:19:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 53010205-0b16-3bef-8848-2a3e0d4459fe | -6.14974 | -44.453 | 2024-10-14 04:19:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a4e352de-0640-3740-a092-5e7ce2041f49 | -6.13069 | -44.72517 | 2024-10-14 04:19:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2974a4bf-491d-359b-a36f-a2f26ce0f79c | -6.11609 | -44.60292 | 2024-10-14 04:19:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 78b63318-e58e-321b-a0ea-c120a3377179 | -6.11555 | -44.60637 | 2024-10-14 04:19:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5421d0bd-677b-3ca3-9e49-7dba27dab20d | -5.10319 | -43.81445 | 2024-10-14 04:19:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 07e76f9f-483e-3f5f-b2a3-6438705ec0e3 | -5.09988 | -43.81394 | 2024-10-14 04:19:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 35ec6465-1bc7-3071-baaf-a2b49095ce0a | -5.09934 | -43.8174 | 2024-10-14 04:19:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 39709837-47d2-3283-a349-dd4816c31b90 | -5.35275 | -44.41524 | 2024-10-14 04:19:00 | NOAA-21 | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 50e0724f-81f4-3e06-bf5e-06abc69a527c | -5.28033 | -44.09655 | 2024-10-14 04:19:00 | NOAA-21 | SENADOR ALEXANDRE COSTA | MARANHÃO | Brasil | 2111748 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d672d8f0-78f3-3206-8b56-6192d835e880 | -5.14434 | -44.11407 | 2024-10-14 04:19:00 | NOAA-21 | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 35ed9d6d-6700-3b0e-99de-69ca786e4961 | -5.1438 | -44.11751 | 2024-10-14 04:19:00 | NOAA-21 | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9c3ffc45-1cdb-3210-a187-327c906bc1bc | -6.5661 | -43.79015 | 2024-10-14 04:19:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 2be3039c-7576-3597-a64a-7b5635155907 | -6.27003 | -43.90124 | 2024-10-14 04:19:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 76857258-09a2-3d27-a57b-2f6036ae31d5 | -6.31749 | -44.27083 | 2024-10-14 04:19:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 144d0e7f-c602-3006-888d-180b12a5c8c2 | -6.26572 | -44.0821 | 2024-10-14 04:19:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 83cf9a5f-384b-3659-8a0f-bfb266069ff2 | -6.26295 | -44.07813 | 2024-10-14 04:19:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1dbd04f0-0f85-3b6d-abac-ebcab9742b39 | -6.22212 | -44.21 | 2024-10-14 04:19:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |


[Clique aqui para ver as próximas entradas](README41.md)
