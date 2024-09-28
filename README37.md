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

## Dados Diários - Página 37

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1a829031-0dce-32a2-99bd-6c056f9453b0 | -5.65429 | -43.37208 | 2024-09-28 04:19:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a7d236fc-cf8f-3245-9123-1a6e9387a7c5 | -6.36709 | -43.48956 | 2024-09-28 04:19:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| f3081454-c047-317e-b89d-b1705e1565a1 | -6.33086 | -43.41875 | 2024-09-28 04:19:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 666ebb61-4036-3b0e-a941-adbea4dc4b26 | -6.32752 | -43.41825 | 2024-09-28 04:19:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 299c96b4-6acb-349e-8de8-1b325bd1e9cb | -6.31804 | -43.41314 | 2024-09-28 04:19:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d4e4338e-63ff-3ccb-824f-10f71d31f2f1 | -6.31748 | -43.41671 | 2024-09-28 04:19:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| b6849c87-a3ff-321f-ab01-06769be68026 | -6.31693 | -43.42028 | 2024-09-28 04:19:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 3b3e7132-beaa-3c21-b86e-96d17dc4e667 | -6.31638 | -43.42384 | 2024-09-28 04:19:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 62b88b54-5b45-37ca-b037-43f7cec8efa8 | -6.31414 | -43.41619 | 2024-09-28 04:19:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 38fa1f33-e0e6-3acf-ab17-ede2e41fe6b7 | -6.31359 | -43.41975 | 2024-09-28 04:19:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 647c6715-ca48-3202-9588-dcb438919fdf | -6.17611 | -43.44976 | 2024-09-28 04:19:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 58474e0a-6fdb-32a5-8fe9-018d2a2b560f | -6.17556 | -43.45326 | 2024-09-28 04:19:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 940016ba-fbea-3c3a-b4ca-459f6affe3af | -6.17277 | -43.44923 | 2024-09-28 04:19:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 5648085f-c13b-36d2-b550-4f8a718b5a09 | -6.17053 | -43.44162 | 2024-09-28 04:19:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 2883e0ab-e135-3690-a58f-d74ee9c83108 | -6.16719 | -43.44109 | 2024-09-28 04:19:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 279de41c-56f2-33c3-acb4-b50311aaa5b2 | -6.16664 | -43.44463 | 2024-09-28 04:19:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 93956b23-7a9c-39aa-8ca8-4681ad6c921a | -6.16385 | -43.44055 | 2024-09-28 04:19:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 682a91a9-ec93-3fe5-a1fa-f2dcf859e220 | -5.34923 | -42.77662 | 2024-09-28 04:19:00 | NOAA-21 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 4.3 |
| bfc46da7-5474-3684-94d6-7c1af5ff974c | -5.26919 | -42.75692 | 2024-09-28 04:19:00 | NOAA-21 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 3cfa9823-7364-3253-8eb9-e4e204ae607e | -5.40343 | -43.10489 | 2024-09-28 04:19:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2f878cc9-b9d6-3b29-85e6-495dcd4e62f9 | -5.31123 | -43.07972 | 2024-09-28 04:19:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 74db862b-3440-3c67-a33b-e6259b4d9078 | -5.30788 | -43.07919 | 2024-09-28 04:19:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f386b2a4-ff1f-31bf-b146-1dcb7ba9adb8 | -5.30666 | -43.07191 | 2024-09-28 04:19:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 80d73b7b-4fc6-350d-b27e-b27352faa635 | -5.3061 | -43.07547 | 2024-09-28 04:19:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1c511973-bebf-3a74-8622-3da1c23a2b5b | -5.3033 | -43.07138 | 2024-09-28 04:19:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c7aec57d-c8e3-31a7-8d72-5cc5353c8493 | -5.30275 | -43.07495 | 2024-09-28 04:19:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a66f4e95-f7e7-3787-a829-9953b408bd74 | -5.13909 | -42.89553 | 2024-09-28 04:19:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 482b9f56-9d8b-30f0-b83d-471048152942 | -5.13628 | -42.89141 | 2024-09-28 04:19:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 8665f8f5-3e06-3813-a16a-5260260984f1 | -5.13573 | -42.89501 | 2024-09-28 04:19:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b3abfbc3-86ef-3f2f-8784-6693b2cb30fd | -6.49544 | -42.7885 | 2024-09-28 04:19:00 | NOAA-21 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 121ae952-95c2-3d61-9b85-f871ecd76198 | -6.41186 | -42.91901 | 2024-09-28 04:19:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 45a7282f-c768-3e6c-8752-456c9496add4 | -6.43172 | -43.22599 | 2024-09-28 04:19:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 07504b21-8e6f-3f93-af48-61e7bc1dd0d6 | -6.40733 | -42.99296 | 2024-09-28 04:19:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 60851d3a-fe57-3ffe-b63f-d0af35ef765a | -7.98639 | -42.8311 | 2024-09-28 04:19:00 | NOAA-21 | PAJEÚ DO PIAUÍ | PIAUÍ | Brasil | 2207355 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 7cf4f182-63d8-3d1c-99c7-8101a5ab002d | -7.96632 | -42.8475 | 2024-09-28 04:19:00 | NOAA-21 | PAJEÚ DO PIAUÍ | PIAUÍ | Brasil | 2207355 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 54516653-1966-34bb-ab9a-0e20807c10e2 | -7.94406 | -42.71988 | 2024-09-28 04:19:00 | NOAA-21 | PAJEÚ DO PIAUÍ | PIAUÍ | Brasil | 2207355 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| d1a5d7ea-ef83-3662-96b5-811332d29dc9 | -7.90142 | -42.67399 | 2024-09-28 04:19:00 | NOAA-21 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 9d49ea92-0895-3ab2-99b7-c4bad8cf1742 | -7.89853 | -42.66958 | 2024-09-28 04:19:00 | NOAA-21 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 11ac3c85-42b7-3f76-9e45-490db9790588 | -7.89796 | -42.67344 | 2024-09-28 04:19:00 | NOAA-21 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| b807983f-35f0-3ae8-96cc-8fdeceb0a04a | -7.89507 | -42.66904 | 2024-09-28 04:19:00 | NOAA-21 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| dc875aec-70fe-3910-a7aa-4a5081c3284b | -7.89449 | -42.6729 | 2024-09-28 04:19:00 | NOAA-21 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 31a5a60e-86ce-394f-a05f-c537a91b65e7 | -7.88988 | -42.68008 | 2024-09-28 04:19:00 | NOAA-21 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| caec7004-3e4e-3b2f-9403-a936576dfb84 | -7.87833 | -42.68623 | 2024-09-28 04:19:00 | NOAA-21 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 469c9eb3-78d6-3f80-ae93-8d7e665d7b39 | -7.87776 | -42.69007 | 2024-09-28 04:19:00 | NOAA-21 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| e2ed6674-d43f-3234-9dd0-1c14ed14f861 | -7.87488 | -42.68567 | 2024-09-28 04:19:00 | NOAA-21 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| d959c443-4e36-35a8-b337-0aed390ec657 | -7.87237 | -43.14365 | 2024-09-28 04:19:00 | NOAA-21 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| b32770dd-040c-381f-9f93-684ec46e64e0 | -7.7561 | -43.76648 | 2024-09-28 04:19:00 | NOAA-21 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 7d9113fe-02a2-3c27-9e7e-3a0c57bc5a72 | -7.4657 | -43.75423 | 2024-09-28 04:19:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| d63ca691-bcc6-338b-bc02-96c60cf7507e | -7.46181 | -43.75726 | 2024-09-28 04:19:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 1d5e7bc9-4b93-3bbf-a2cf-3a2c472e8a93 | -7.46126 | -43.76081 | 2024-09-28 04:19:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| c701ba02-bdbc-3ec3-803c-515f4c8ea560 | -7.30286 | -43.03828 | 2024-09-28 04:19:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 2a43d841-a260-395d-9a73-141742e57676 | -7.2285 | -43.289 | 2024-09-28 04:19:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| cefaefb5-9611-3d96-8f32-dbac10743079 | -7.21207 | -42.48269 | 2024-09-28 04:19:00 | NOAA-21 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 64ffed31-2a31-3c31-b1a2-43c431c4feba | -7.21148 | -42.48656 | 2024-09-28 04:19:00 | NOAA-21 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 72145019-ea22-342a-8c25-23a53ab8f3a0 | -7.21089 | -42.49041 | 2024-09-28 04:19:00 | NOAA-21 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| cc605c5d-6ff9-33c5-8f12-90c082c8ecf9 | -7.21031 | -42.49424 | 2024-09-28 04:19:00 | NOAA-21 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 9dc95660-84a4-340e-8256-d88f5f93eb39 | -7.47465 | -43.78465 | 2024-09-28 04:19:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ab641a48-1619-3aa8-87f6-dfd7b72cf91f | -7.39006 | -43.36141 | 2024-09-28 04:19:00 | NOAA-21 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ff893b0a-af78-3762-827e-bd8620f61de1 | -7.38383 | -43.33451 | 2024-09-28 04:19:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9069f66c-bf33-3863-bf0c-9b0c9f154257 | -7.38046 | -43.33398 | 2024-09-28 04:19:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 83ffbffb-96f2-333b-8177-e9ff955e5a16 | -7.28871 | -43.33501 | 2024-09-28 04:19:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 212675f2-d224-3533-899a-71a4d0860a98 | -7.28815 | -43.33863 | 2024-09-28 04:19:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 4.4 |
| b8085c28-68c2-399e-a809-b13d6ec2a9ac | -6.64171 | -42.08701 | 2024-09-28 04:19:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 25d9af53-4de7-397b-8cc8-ad353315ef9e | -6.85423 | -43.12797 | 2024-09-28 04:19:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b50a6b29-709d-3596-930b-12fa884b3649 | -6.83844 | -43.11806 | 2024-09-28 04:19:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| af79212d-b20d-3ed9-8f29-3ed273202e85 | -6.83506 | -43.11753 | 2024-09-28 04:19:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e61e28a1-35ed-324a-8cd7-b67a9ab5efb8 | -6.55919 | -43.14992 | 2024-09-28 04:19:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| bc5675ad-6169-369a-99f9-35c57b22bc42 | -6.55864 | -43.15353 | 2024-09-28 04:19:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| a6ea3e86-1bd5-3039-a761-a846c49c7392 | -6.55582 | -43.14941 | 2024-09-28 04:19:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| abd45559-4bd4-3111-a7f9-b16c5562e22a | -6.55189 | -43.15251 | 2024-09-28 04:19:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 16d5af31-26b7-3723-894d-a0abd66bb553 | -6.72389 | -43.55907 | 2024-09-28 04:19:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| df0f38eb-6cd5-3626-8459-c1ee88e7a830 | -6.72055 | -43.55856 | 2024-09-28 04:19:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 7.6 |
| db90f52f-c08b-367c-8645-b5bd00d748a3 | -6.67137 | -43.50021 | 2024-09-28 04:19:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| efb7dda8-98a4-30c3-9f9c-f5e4c26801b4 | -6.62864 | -43.5374 | 2024-09-28 04:19:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ea5d8840-139f-3ea0-b9d9-0d376e810c19 | -9.28852 | -43.474 | 2024-09-28 04:19:00 | NOAA-21 | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 549739ca-373f-3b88-ad74-6ad6f15b763c | -9.28512 | -43.47349 | 2024-09-28 04:19:00 | NOAA-21 | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 1e06f642-2d10-3d00-b274-124492416c22 | -9.12955 | -43.15509 | 2024-09-28 04:19:00 | NOAA-21 | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 5db45bab-eda4-3909-92c2-1cbfc80592dc | -9.12669 | -43.15073 | 2024-09-28 04:19:00 | NOAA-21 | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| bd6c2641-8857-3738-b494-fa54f78880cc | -9.12612 | -43.15453 | 2024-09-28 04:19:00 | NOAA-21 | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | 4.7 |
| 1486bbf5-b18f-3dc9-8ef5-b826c97a28fd | -8.50392 | -43.92213 | 2024-09-28 04:19:00 | NOAA-21 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| b6d4deff-9c25-3e6a-ab5d-e70d2311fac4 | -8.50058 | -43.9216 | 2024-09-28 04:19:00 | NOAA-21 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| ccf5b11d-cb34-39d5-bf49-d3ebaddb246b | -8.28597 | -42.96043 | 2024-09-28 04:19:00 | NOAA-21 | TAMBORIL DO PIAUÍ | PIAUÍ | Brasil | 2210953 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| fb8bc3ca-7bb2-3b14-bc57-6ea347d4efd2 | -8.08196 | -42.8953 | 2024-09-28 04:19:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 4e0bc03f-eaa6-39da-83f1-20f516597541 | -8.07622 | -42.8867 | 2024-09-28 04:19:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| b32ccf6d-88bb-3f31-90be-65797370b0e7 | -8.07569 | -42.91362 | 2024-09-28 04:19:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| dddb45f1-a2ef-3fb8-86a4-98458ccf3d81 | -8.07391 | -42.8786 | 2024-09-28 04:19:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 90bea8e4-1d90-3efe-936d-34ede6f5a823 | -8.07334 | -42.88242 | 2024-09-28 04:19:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 1af898b7-ffa2-338a-962a-6857aa6eba9a | -8.07047 | -42.87812 | 2024-09-28 04:19:00 | NOAA-21 | PAJEÚ DO PIAUÍ | PIAUÍ | Brasil | 2207355 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| e75bda23-4b52-3e48-92a2-e59c9d55d071 | -8.06303 | -42.88078 | 2024-09-28 04:19:00 | NOAA-21 | PAJEÚ DO PIAUÍ | PIAUÍ | Brasil | 2207355 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 2b831eb0-560f-330a-9d2e-87f3af3f4df0 | -8.89024 | -44.08424 | 2024-09-28 04:19:00 | NOAA-21 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 16e38b25-ef4e-3df4-85a7-087eb9f9c6b8 | -8.8897 | -44.08778 | 2024-09-28 04:19:00 | NOAA-21 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3a5a28d5-b9b0-3785-b50e-1d27daade717 | -8.25901 | -43.85484 | 2024-09-28 04:19:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 68894e21-cd45-3950-8a27-70b99291216a | -9.51598 | -43.24355 | 2024-09-28 04:19:00 | NOAA-21 | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 967c6a15-807c-3f71-a497-7ec4f7de0546 | -7.77176 | -44.67197 | 2024-09-28 04:19:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 39.0 |
| 711f5ef6-1677-38f2-b19d-1a49c15336e3 | -3.47304 | -43.35341 | 2024-09-28 04:19:00 | NOAA-21 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f46f4053-afdb-3322-ad30-7a35d7769a9a | -3.4725 | -43.35686 | 2024-09-28 04:19:00 | NOAA-21 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| cd289891-6d78-3f47-89eb-31be80dcd141 | -3.46973 | -43.3529 | 2024-09-28 04:19:00 | NOAA-21 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| bdfe8b06-7cb7-31f1-9bca-d150cd73ef5b | -3.30066 | -43.52102 | 2024-09-28 04:19:00 | NOAA-21 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 9e4339a1-2040-33c4-8fc0-2fd1b8cddda4 | -3.29789 | -43.51706 | 2024-09-28 04:19:00 | NOAA-21 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| d8110ec7-bd0c-3095-8b69-f73d9e1d6e32 | -3.29736 | -43.52051 | 2024-09-28 04:19:00 | NOAA-21 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |


[Clique aqui para ver as próximas entradas](README38.md)
