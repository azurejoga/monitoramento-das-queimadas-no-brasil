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

## Dados Diários - Página 24

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f2625228-35a2-3046-9f3e-ffe2356fe3d4 | -6.58851 | -44.56045 | 2025-08-24 03:42:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a2d74daf-ed09-36c1-9418-b9e3bf0bcbb2 | -6.31311 | -43.76446 | 2025-08-24 03:42:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2b54b35e-6928-310b-82be-694dd2192746 | -10.54821 | -47.14207 | 2025-08-24 03:42:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f018cb9d-e044-3526-aa1c-e2e2c6bf46f2 | -10.81725 | -46.39683 | 2025-08-24 03:42:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| db679fbf-8824-388c-91bf-aec85b020379 | -10.41151 | -47.19711 | 2025-08-24 03:42:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6e9c3483-1c63-3f3e-8685-7fd2632b5d64 | -6.43829 | -44.55092 | 2025-08-24 03:42:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b77e6817-38f5-3fb3-a1a0-7e378ad04dec | -7.2562 | -43.6726 | 2025-08-24 03:42:00 | NOAA-20 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a1b88a6d-9583-36cf-adf3-2a750d93cc3b | -4.48457 | -47.67042 | 2025-08-24 03:42:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 093346ae-4153-300d-949b-0a3ad8a7bfef | -6.95701 | -44.4208 | 2025-08-24 03:42:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 137ce30e-22ac-3702-a406-437411fc0d4f | -6.50441 | -43.41032 | 2025-08-24 03:42:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 424a7b67-3e59-3780-8264-fdfcb6a125c2 | -6.4697 | -43.46167 | 2025-08-24 03:42:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| c76cb060-4f13-3475-994a-e0fdafe9ce6f | -6.91746 | -44.40381 | 2025-08-24 03:42:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| cbdb1b78-4868-33c5-8e0e-4b9ea630d56e | -8.05926 | -49.65589 | 2025-08-24 03:42:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3080c72e-61ce-3b98-9d6c-1e7d32bf3e55 | -10.40552 | -47.19621 | 2025-08-24 03:42:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7dae02d6-9b30-35fe-98d0-f6fef3ee5feb | -6.19146 | -45.43609 | 2025-08-24 03:42:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 9d7118fc-fc40-310e-90a6-979930dd96fa | -5.4888 | -41.40516 | 2025-08-24 03:42:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 84ed9a03-7ffd-30ec-aefe-faaeac19dffd | -8.05562 | -45.0027 | 2025-08-24 03:42:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4edfdc9c-722c-3de6-a5bb-0d6e65011e44 | -5.58314 | -45.80636 | 2025-08-24 03:42:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 43f1657b-f12b-38eb-bdc7-dd6ce96bd9e4 | -9.24584 | -48.20338 | 2025-08-24 03:42:00 | NOAA-20 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 8fc63d27-d965-3632-aedc-bc3aa797c77d | -8.53623 | -37.72193 | 2025-08-24 03:42:00 | NOAA-20 | IBIMIRIM | PERNAMBUCO | Brasil | 2606606 | 26 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 318f81a2-2b8e-3f4e-92ab-0db7561cc96a | -6.88823 | -45.68561 | 2025-08-24 03:42:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 12.8 |
| e7489952-3860-3d8f-85cf-a7c1d157c0fb | -7.61886 | -45.24822 | 2025-08-24 03:42:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a3e9feb2-c062-3a60-9818-ac2f4b83c11c | -6.03852 | -44.00346 | 2025-08-24 03:42:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3c37f1df-0f7e-303f-b7b8-b6a87d0f0c44 | -6.31 | -43.76558 | 2025-08-24 03:42:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4f090f86-c270-3acd-b974-4caf7bd575de | -9.68069 | -48.34602 | 2025-08-24 03:42:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9dbb12af-1aeb-3a18-991f-bdcdd0baa86d | -7.01749 | -44.63575 | 2025-08-24 03:42:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 740ac74f-20b7-30d2-9ba5-735668263951 | -7.57579 | -43.84575 | 2025-08-24 03:42:00 | NOAA-20 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 93108262-99a5-34f9-8a88-b917023de144 | -6.08975 | -44.69376 | 2025-08-24 03:42:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 42dbe93b-8d2f-3465-9cf4-a2c1868bde5a | -9.24575 | -48.20216 | 2025-08-24 03:42:00 | NOAA-20 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 7ceeb102-129a-3aad-8b4d-6b4b2bdd388d | -7.75067 | -47.35747 | 2025-08-24 03:42:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3aa7ed16-b1bb-3945-9e7d-6e29e5b8387f | -10.82692 | -46.40701 | 2025-08-24 03:42:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 31696d8c-a0c8-3f59-8926-0c091989c636 | -7.8105 | -46.62784 | 2025-08-24 03:42:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 1c9e80ab-1c3d-3c8e-82bf-98c83542ed92 | -9.01996 | -47.64882 | 2025-08-24 03:42:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 49319f99-4f7d-3dd0-8d39-d2d580e6f9ca | -9.11808 | -45.18847 | 2025-08-24 03:42:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 945747c0-34b1-38be-bdfc-5dffa191bfd3 | -10.80764 | -46.41628 | 2025-08-24 03:42:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 71f8d93b-2d1c-3410-b9d7-af3dfe3009a7 | -6.43288 | -44.55021 | 2025-08-24 03:42:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 3326d97f-8fad-38b6-a8e9-0b16ceef6852 | -8.22104 | -45.11514 | 2025-08-24 03:42:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b3e7cc60-028c-36e2-90f9-c8edd887dae2 | -6.137 | -43.15461 | 2025-08-24 03:42:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 2.1 |
| d5dc64f0-4e73-3a11-9df4-bed0c12a152a | -10.08354 | -38.42899 | 2025-08-24 03:42:00 | NOAA-20 | JEREMOABO | BAHIA | Brasil | 2918100 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| fd63b12e-4c33-3472-b5b9-678827eeead5 | -11.06135 | -44.60151 | 2025-08-24 03:42:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| bcd0f8bb-6e85-3f88-ae8b-cabd72eefeec | -6.03954 | -43.99773 | 2025-08-24 03:42:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 23145ac7-ecfe-3280-930c-711b07cd62cf | -6.23164 | -44.13065 | 2025-08-24 03:42:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 10f866bf-d8b2-36ab-9787-d010948b3546 | -10.41292 | -40.60891 | 2025-08-24 03:42:00 | NOAA-20 | CAMPO FORMOSO | BAHIA | Brasil | 2906006 | 29 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 680132ac-1d4d-32c8-8f19-962d98f2248c | -10.41231 | -47.17757 | 2025-08-24 03:42:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| fc3e4bf3-47ff-37bb-a18a-47159455b011 | -10.55289 | -47.13591 | 2025-08-24 03:42:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 132d2d22-c961-38ba-b693-fb337299f115 | -10.48265 | -46.45069 | 2025-08-24 03:42:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| eb267f98-c30e-38cf-a65a-ce522ebcd8ca | -6.08912 | -44.69733 | 2025-08-24 03:42:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ade6fb87-944c-31d2-b3e2-8600a14b4dcd | -7.91256 | -45.90738 | 2025-08-24 03:42:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9290b894-f339-3c6c-bf89-2fe535f951d1 | -8.18105 | -45.08942 | 2025-08-24 03:42:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9e845529-3cc2-34bb-824c-c90113d06c8a | -8.8349 | -49.89989 | 2025-08-24 03:42:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c14b7c77-f23d-38c5-9eda-0f884b600fb2 | -6.89474 | -45.68233 | 2025-08-24 03:42:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 76b7d957-8ef4-3e68-9ac5-f951770d72fd | -4.47782 | -47.66935 | 2025-08-24 03:42:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| cbf24b9a-e999-362b-a114-a04f3b04ac41 | -7.49882 | -43.89957 | 2025-08-24 03:42:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c72544d8-9395-3b5a-8561-156f373b23fe | -7.60159 | -45.24936 | 2025-08-24 03:42:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6d9be301-50bd-3252-b066-c327dc5b853d | -7.5808 | -43.84671 | 2025-08-24 03:42:00 | NOAA-20 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2bdc872c-0a1f-3ff5-8ba3-2d2d2055ac79 | -10.55501 | -47.13853 | 2025-08-24 03:42:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 37b8e04a-ca91-3b27-9bca-cc987b9809c2 | -6.50542 | -43.40458 | 2025-08-24 03:42:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 3f8586af-46b5-3ee9-be3f-d29b92018581 | -7.01924 | -44.64394 | 2025-08-24 03:42:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 7.6 |
| c7fd1594-8219-3e1a-bd16-5ec9d569cb46 | -7.17841 | -44.66489 | 2025-08-24 03:42:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0a514dbc-0837-3c5b-b80d-8014e8545842 | -7.94879 | -42.66553 | 2025-08-24 03:42:00 | NOAA-20 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 5c14b16b-819d-3cc1-9830-b768b39629e4 | -9.5281 | -41.70017 | 2025-08-24 03:42:00 | NOAA-20 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| e0e0f145-0740-3daf-acf8-5b4002e65e81 | -6.58912 | -44.55695 | 2025-08-24 03:42:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a8053e55-88f9-3b8f-89a8-0f11a3eec1be | -7.17247 | -44.66731 | 2025-08-24 03:42:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fecf3047-b873-39ca-817b-363eb9d79546 | -6.09522 | -44.69462 | 2025-08-24 03:42:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3f5b8fd3-1b78-32d7-9639-6a81756ef5eb | -5.40873 | -44.99342 | 2025-08-24 03:42:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 27a84b99-2c40-3ed2-8a34-58379b4d3db2 | -7.17309 | -44.6638 | 2025-08-24 03:42:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a8823de4-f1e6-3ae4-8343-55da1973f241 | -8.22043 | -45.11858 | 2025-08-24 03:42:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d56cd320-bf30-323b-befb-0cef2bb6036e | -10.54146 | -47.14535 | 2025-08-24 03:42:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 656cd4ea-2c89-37a7-95f7-ddaeb58bdc37 | -8.74896 | -46.75115 | 2025-08-24 03:42:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f803ec39-95b6-3b4c-a1c1-c75c8bf70714 | -7.01801 | -44.6507 | 2025-08-24 03:42:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| d11cd440-1d93-354c-893c-7b177f8dad8e | -11.10672 | -44.77209 | 2025-08-24 03:42:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 48c6ff0b-719e-3c4c-a449-a0271c5a20e4 | -10.80139 | -46.40143 | 2025-08-24 03:42:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 51e62978-6e18-30b1-85a3-acdde8f76cfe | -8.76445 | -49.99043 | 2025-08-24 03:42:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 057573a8-7d00-32e8-ba9e-0abb6f57aaf4 | -7.02108 | -44.64679 | 2025-08-24 03:42:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| af76e02a-bddb-3f77-bf39-e13ff106e4cc | -6.88395 | -45.67654 | 2025-08-24 03:42:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 27a5fe50-6bfd-39a5-a4c8-cbb9d44c5c92 | -6.89184 | -45.66556 | 2025-08-24 03:42:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| cfd919f8-145a-31b4-a6b8-dd5f1370b9a7 | -6.19075 | -45.44011 | 2025-08-24 03:42:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| cf8485f1-6c74-3b23-b92d-9e63b618d324 | -11.14018 | -44.78772 | 2025-08-24 03:42:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c4c2c173-5172-3b14-b09e-7e3506e7c40a | -6.91829 | -43.78093 | 2025-08-24 03:42:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1d34a1ca-35bf-3806-8428-07eb766e8330 | -10.29273 | -46.75047 | 2025-08-24 03:42:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b71f392e-8428-3ff6-b1c2-4c74bcb51e65 | -5.65841 | -45.1453 | 2025-08-24 03:42:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 26a9ae6d-2ba8-30d1-af68-9fde3c9fcedd | -7.62019 | -45.24083 | 2025-08-24 03:42:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 107ffe47-1f75-3137-8ff8-21f6ca768e27 | -10.80422 | -46.40393 | 2025-08-24 03:42:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 24c98603-01cd-3fc0-9a6d-f72205301adb | -6.20091 | -42.98708 | 2025-08-24 03:42:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2266ab4c-aadf-3b60-a4e1-6a4b495d0b4f | -8.76529 | -49.97409 | 2025-08-24 03:42:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 234b08e4-b64b-3526-9819-c856c5214df4 | -7.07774 | -44.625 | 2025-08-24 03:42:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c900d88f-93d2-3eb6-833e-80b9b9fee875 | -7.02226 | -44.63999 | 2025-08-24 03:42:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 8649339f-5454-3060-b89f-13f7db00bc72 | -7.62084 | -45.23721 | 2025-08-24 03:42:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| bd28c1ff-cdbb-3470-a71e-2084f661c9a3 | -7.92825 | -45.91851 | 2025-08-24 03:42:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6ba47e7d-492e-3097-a655-c8f334a63d3c | -8.0579 | -49.66282 | 2025-08-24 03:42:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d2eaf7ac-92d7-3113-b5b5-2ad2e74babdc | -9.79796 | -46.42159 | 2025-08-24 03:42:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 59d9a7e2-eff4-37c0-9afc-7f89a1734ff7 | -6.77512 | -44.9871 | 2025-08-24 03:42:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 61573bc1-a62d-379a-8174-8f286d69276a | -10.55201 | -47.14034 | 2025-08-24 03:42:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fd0e2071-cef6-39dd-adb8-f02472a12d79 | -6.5053 | -42.9585 | 2025-08-24 03:42:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8ef1e504-009f-3904-9025-514143cf4664 | -8.11934 | -47.14394 | 2025-08-24 03:42:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| cb8b4928-eb5e-3ee6-bee0-80e562eca75e | -7.69976 | -42.12439 | 2025-08-24 03:42:00 | NOAA-20 | SIMPLÍCIO MENDES | PIAUÍ | Brasil | 2210805 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 6a12f460-d8c7-34c2-a1ca-5aeabedef3a3 | -7.614 | -45.24363 | 2025-08-24 03:42:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3a807273-06e4-3f31-b0f9-e38c68a63fe6 | -9.14172 | -40.32173 | 2025-08-24 03:42:00 | NOAA-20 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 4.5 |
| 863fc3dd-109d-3545-8526-a625352780d4 | -5.48736 | -41.41381 | 2025-08-24 03:42:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| f2430a01-ab63-363a-aad0-ae8d4eebe3be | -10.40985 | -47.17356 | 2025-08-24 03:42:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |


[Clique aqui para ver as próximas entradas](README25.md)
