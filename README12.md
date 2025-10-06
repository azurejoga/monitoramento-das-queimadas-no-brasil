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

## Dados Diários - Página 12

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9efa324d-9135-3622-b09b-e93e51ee7522 | -6.40029 | -43.62922 | 2025-10-06 03:34:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f1c3e88f-6e30-3024-b5d4-39a63281b781 | -7.78165 | -42.61307 | 2025-10-06 03:34:00 | NOAA-20 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| e6d738cb-f811-30a2-a4a3-4c18ccb22a9a | -7.79888 | -42.57693 | 2025-10-06 03:34:00 | NOAA-20 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 2e3055d3-9220-3358-a6be-d75cfd3c062e | -5.19574 | -46.15942 | 2025-10-06 03:34:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 80164239-5482-3566-b328-24cd2ab83c74 | -7.00958 | -42.79492 | 2025-10-06 03:34:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 406edd74-46db-38e7-977e-1a0e3ec5fef6 | -5.41677 | -41.34981 | 2025-10-06 03:34:00 | NOAA-20 | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 8a6b6243-864a-3abd-9daf-96f1394128c3 | -6.18319 | -42.71498 | 2025-10-06 03:34:00 | NOAA-20 | ANGICAL DO PIAUÍ | PIAUÍ | Brasil | 2200608 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| c12ec43a-ac66-3c8b-b992-748b25aaf1cc | -6.05954 | -43.48734 | 2025-10-06 03:34:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 6b9763a5-1e7b-32d2-a67f-94cd8517751c | -6.69391 | -42.16952 | 2025-10-06 03:34:00 | NOAA-20 | TANQUE DO PIAUÍ | PIAUÍ | Brasil | 2210979 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| c3e653aa-be78-3cb8-a0c3-15f710a70f83 | -5.46196 | -42.79022 | 2025-10-06 03:34:00 | NOAA-20 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| fe29ad99-029a-3d32-a562-ec03e7b595cc | -6.69096 | -42.15617 | 2025-10-06 03:34:00 | NOAA-20 | TANQUE DO PIAUÍ | PIAUÍ | Brasil | 2210979 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 973d6d5d-b512-3405-ad22-8ea159458313 | -7.0109 | -42.29886 | 2025-10-06 03:34:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| babdc362-b8fc-3c10-9ceb-ba21e79de734 | -5.32761 | -43.36872 | 2025-10-06 03:34:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 87ff3a83-c009-3ed8-8d1c-5698ab64e751 | -7.707 | -42.3988 | 2025-10-06 03:34:00 | NOAA-20 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 863cda29-1644-3e4c-9c46-595f2283373e | -6.70055 | -42.16182 | 2025-10-06 03:34:00 | NOAA-20 | TANQUE DO PIAUÍ | PIAUÍ | Brasil | 2210979 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 0d9fd10e-b452-3dd8-a7d7-e103b7616e06 | -6.36493 | -44.65454 | 2025-10-06 03:34:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 1bf6de0f-e8d6-3f79-a0bf-7fe223566deb | -6.25522 | -43.90163 | 2025-10-06 03:34:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| d236c770-a6c6-3a04-a8ae-c3238bcaa280 | -6.07405 | -44.0421 | 2025-10-06 03:34:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8f54d6eb-3f62-3c85-a90c-d92dddc16e39 | -7.25277 | -44.13532 | 2025-10-06 03:34:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 5.4 |
| c69d827c-949b-3793-8685-a4726647131c | -6.10099 | -43.52994 | 2025-10-06 03:34:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 5dbb7ceb-d433-3409-bf73-3b7cbe5e05ad | -6.11377 | -43.52393 | 2025-10-06 03:34:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| fd346e1f-0435-311e-9a87-954c18a3d604 | -6.0733 | -44.04615 | 2025-10-06 03:34:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 787747e7-bd26-358f-a01a-0dd1d580e500 | -6.62889 | -41.98349 | 2025-10-06 03:34:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 0af1d4c6-460d-3098-bad8-ede04a18bbb8 | -4.89728 | -41.50454 | 2025-10-06 03:34:00 | NOAA-20 | JUAZEIRO DO PIAUÍ | PIAUÍ | Brasil | 2205516 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 05be3d4c-605d-3986-9862-70ef28687cda | -6.2753 | -40.62268 | 2025-10-06 03:34:00 | NOAA-20 | PARAMBU | CEARÁ | Brasil | 2310308 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 321173c2-3323-3588-b06a-bbccc287b1a9 | -6.62381 | -41.9826 | 2025-10-06 03:34:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 4e263338-d19e-3470-98c4-62ae08e88f41 | -7.02673 | -42.79116 | 2025-10-06 03:34:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| c1fc8ed1-9e1e-3a06-b759-0c3db908eb1c | -6.31296 | -44.69719 | 2025-10-06 03:34:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| dc71b3ef-db33-37dc-8f5b-261de94d6ddf | -7.02613 | -42.79455 | 2025-10-06 03:34:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 50eb324e-bf4b-3c2b-8256-629646e439c9 | -6.05928 | -42.55485 | 2025-10-06 03:34:00 | NOAA-20 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 7a2f8097-0e56-35df-9958-2b32e7026d71 | -6.07456 | -44.04715 | 2025-10-06 03:34:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 31881688-6135-3950-8c30-2e7a20cbbdc8 | -6.22774 | -44.39539 | 2025-10-06 03:34:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 470bbf94-ddfd-3211-ac69-4680833ff0aa | -6.0374 | -42.55435 | 2025-10-06 03:34:00 | NOAA-20 | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| fc3ec424-06da-359b-b492-f108515b4939 | -7.72563 | -42.38339 | 2025-10-06 03:34:00 | NOAA-20 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 0391493e-3d84-37cc-8893-51366161476d | -5.40208 | -41.06988 | 2025-10-06 03:34:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 0a5cc104-896b-30b0-86a2-f258d30e1608 | -7.1842 | -41.69371 | 2025-10-06 03:34:00 | NOAA-20 | PAQUETÁ | PIAUÍ | Brasil | 2207553 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 5dfd3773-9bae-397a-a69c-dcfa9fd0f211 | -6.61871 | -41.98182 | 2025-10-06 03:34:00 | NOAA-20 | NOVO ORIENTE DO PIAUÍ | PIAUÍ | Brasil | 2206902 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| a48714bc-cba1-3234-86b8-b1843b59212a | -6.69271 | -41.38506 | 2025-10-06 03:34:00 | NOAA-20 | SÃO JOÃO DA CANABRAVA | PIAUÍ | Brasil | 2209856 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| a5f936d3-9740-3968-9672-41164f765b7a | -6.06519 | -42.55248 | 2025-10-06 03:34:00 | NOAA-20 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 4e1185fd-6a55-37b4-a48e-f5590ddeeb7b | -7.36308 | -45.24029 | 2025-10-06 03:34:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e7ea62b1-826a-380b-86fe-e471e2c6d9d8 | -6.05807 | -42.5617 | 2025-10-06 03:34:00 | NOAA-20 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 341304f4-3e3e-3a79-8948-59caa3440883 | -7.00362 | -42.82833 | 2025-10-06 03:34:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| ed906e2d-077a-3bcc-8da0-de17d3512484 | -7.42739 | -41.12275 | 2025-10-06 03:34:00 | NOAA-20 | MASSAPÊ DO PIAUÍ | PIAUÍ | Brasil | 2206050 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 4599fb05-cbdd-36e6-8e2a-e118d389a854 | -7.0167 | -42.78577 | 2025-10-06 03:34:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| ea556009-7651-3173-9ad0-07c2a7e6ab3b | -7.02622 | -42.76307 | 2025-10-06 03:34:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 521acab8-07e6-32d6-b6a0-e20a4bc13d8f | -7.25224 | -44.13902 | 2025-10-06 03:34:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 7b9b3de0-6226-3df2-9901-28a64952bbb1 | -6.40471 | -43.60474 | 2025-10-06 03:34:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 017d204d-e7cb-3221-8e15-b1e2829cd325 | -5.97857 | -38.25821 | 2025-10-06 03:34:00 | NOAA-20 | ERERÊ | CEARÁ | Brasil | 2304277 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 087a3aaa-3956-309f-a710-0c110019e427 | -5.91529 | -42.52229 | 2025-10-06 03:34:00 | NOAA-20 | OLHO D'ÁGUA DO PIAUÍ | PIAUÍ | Brasil | 2207108 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| e92cc087-bd93-3dbf-871e-3a5b2ada97c7 | -7.7167 | -42.40369 | 2025-10-06 03:34:00 | NOAA-20 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| e8a4525e-9611-3afb-bcec-f2377975b449 | -7.46041 | -43.04157 | 2025-10-06 03:34:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 981f86e3-032c-3970-867a-5fa11742436b | -6.24438 | -44.26683 | 2025-10-06 03:34:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| c5ce565d-45b0-3be0-a431-1efc714e02fa | -7.77461 | -42.62238 | 2025-10-06 03:34:00 | NOAA-20 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 2801615d-249f-3b6b-a43c-b2046624fc26 | -6.70109 | -42.15873 | 2025-10-06 03:34:00 | NOAA-20 | TANQUE DO PIAUÍ | PIAUÍ | Brasil | 2210979 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 97da54ec-a7f9-32ec-882e-3a9853a08964 | -7.35582 | -45.2376 | 2025-10-06 03:34:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1b3256d2-1834-3026-ba46-2947cc4b0f69 | -6.72603 | -42.16749 | 2025-10-06 03:34:00 | NOAA-20 | TANQUE DO PIAUÍ | PIAUÍ | Brasil | 2210979 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 0bfc67e3-33c4-326e-9b6c-27c32094c814 | -7.00241 | -42.83511 | 2025-10-06 03:34:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 9985acca-424e-38bc-988f-d021f02d9162 | -9.32128 | -46.00408 | 2025-10-06 03:36:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| f7e2c6fe-3fdc-33fb-8dd0-25cac27b7a74 | -12.90112 | -47.29644 | 2025-10-06 03:36:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 5f72c701-4410-3915-9f9d-7995d5bd2e5b | -13.23643 | -47.81856 | 2025-10-06 03:36:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| b0cc60ea-ebbc-32ea-92a0-a2d0f9567251 | -11.80462 | -45.118 | 2025-10-06 03:36:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3eecb56b-64f7-3a38-a073-bebac724dde1 | -10.34317 | -47.02308 | 2025-10-06 03:36:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d5f3cd5e-d0f9-3de2-9e7f-6b79eaa51934 | -11.54659 | -47.04626 | 2025-10-06 03:36:00 | NOAA-20 | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 22a19532-84d1-3a8d-8a9e-0637415d05c8 | -11.93806 | -46.44279 | 2025-10-06 03:36:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| ed3e17c8-1b0c-3288-89a7-901c8b5994ad | -9.31848 | -46.01857 | 2025-10-06 03:36:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 9c985007-3747-3ba1-b6f3-3ccecc3b354e | -13.31815 | -47.17063 | 2025-10-06 03:36:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0020fd83-bdce-369e-8636-e59a6b33e42c | -8.52144 | -46.32554 | 2025-10-06 03:36:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4a54c6fc-3573-3285-8553-eb21b0f694dd | -11.50131 | -44.97999 | 2025-10-06 03:36:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8a05a3f2-6b48-3257-8ace-916dabf81a6e | -11.84835 | -44.936 | 2025-10-06 03:36:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 835f39cd-6965-3399-9de7-7440dd55a56c | -13.22337 | -47.82344 | 2025-10-06 03:36:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 410b17c5-45cb-303b-a7bd-c8d19afccdab | -11.84107 | -45.0611 | 2025-10-06 03:36:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 298006c7-54ee-3a32-9590-c5afa3012d5a | -13.27213 | -47.5871 | 2025-10-06 03:36:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 40fedeec-5981-3c4c-94ac-03ebb27da320 | -12.90317 | -47.29247 | 2025-10-06 03:36:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| ffe60623-5dc9-382b-9eee-bc5bae047604 | -12.44898 | -45.56657 | 2025-10-06 03:36:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| b14e280f-37a9-3037-9494-0d8111b9c52c | -13.26423 | -47.59273 | 2025-10-06 03:36:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 5.4 |
| a54d572e-d9b8-3797-8186-ff4062344b83 | -13.29245 | -47.8114 | 2025-10-06 03:36:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6610677e-0bdd-374c-8954-5d0f0ebbfa05 | -8.61778 | -46.31167 | 2025-10-06 03:36:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 8f6fd5c3-90f4-3777-95ec-99bb0e2ccc45 | -12.44072 | -45.57784 | 2025-10-06 03:36:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 57ca34f9-5ea6-314d-aaa4-951fbcffe167 | -12.90835 | -47.29949 | 2025-10-06 03:36:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 2609bded-f359-372d-a7bf-2312390ba350 | -8.53847 | -46.30666 | 2025-10-06 03:36:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ff5c193d-4151-3106-a21f-bbbb9d0f070b | -9.31939 | -46.01385 | 2025-10-06 03:36:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 94d062cb-18b4-3be0-8eb1-d2f32b0f0331 | -8.54781 | -46.25767 | 2025-10-06 03:36:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 392ea4a6-43dd-3672-8175-87fe800e61c6 | -11.83973 | -45.05817 | 2025-10-06 03:36:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 1de5ab6b-79ca-3ea7-ae50-5d0fb051722c | -11.84543 | -44.93652 | 2025-10-06 03:36:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 95462c57-8fa5-3760-8e22-7ff20a7e9ec0 | -13.13086 | -48.00377 | 2025-10-06 03:36:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| cca485d2-f13a-3b09-926d-556630b39f05 | -9.96118 | -43.77766 | 2025-10-06 03:36:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 86707c7e-8daf-3b12-aa91-1c57a8c6ca29 | -13.25846 | -47.84342 | 2025-10-06 03:36:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 954abe66-2d20-39f6-9d33-35b6aa4bf2aa | -13.12284 | -48.00903 | 2025-10-06 03:36:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 2dd35a5b-246f-3780-832d-de2bf3aff43c | -8.56757 | -46.25922 | 2025-10-06 03:36:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 10c5962b-bf3b-3893-84b8-28d7f0d091d3 | -11.25816 | -47.78461 | 2025-10-06 03:36:00 | NOAA-20 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e1dfe82b-d282-3cc6-bc4b-7197e6071e1a | -7.79302 | -44.1281 | 2025-10-06 03:36:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 90419db5-d401-36ed-8f97-e7c870e84fa6 | -11.83902 | -45.06187 | 2025-10-06 03:36:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3be95842-c1a2-347e-bdcd-06961eb9fa3a | -13.27315 | -47.58212 | 2025-10-06 03:36:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 13b83237-65fb-30eb-9954-0fd428ae419e | -12.48111 | -45.55614 | 2025-10-06 03:36:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 15.3 |
| be28396a-b66f-3f7e-9101-9fcf6cb0aa3b | -8.62743 | -46.33126 | 2025-10-06 03:36:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 15.1 |
| 49f68033-29e1-3e8b-adb1-3ebaacf70cba | -11.79332 | -45.11528 | 2025-10-06 03:36:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 22042fbe-22d8-397a-bae2-0b820c3120d8 | -11.03336 | -47.79144 | 2025-10-06 03:36:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 05fba286-725e-3759-a91c-f822d81cffc5 | -13.09821 | -47.93009 | 2025-10-06 03:36:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 182a906a-85ce-3148-a399-6b3cfb1f57f9 | -8.55526 | -46.25436 | 2025-10-06 03:36:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e0300be8-29d8-3198-abff-8d3e9c348d94 | -12.24793 | -49.20879 | 2025-10-06 03:36:00 | NOAA-20 | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |


[Clique aqui para ver as próximas entradas](README13.md)
