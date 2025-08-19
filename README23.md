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
| 21787bcd-1f1a-3fd9-a58f-44014a7249bd | -2.90444 | -48.29542 | 2025-08-19 04:25:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f983b0d1-9400-3eb7-b2c7-bde9d475ba6d | -6.561 | -44.46095 | 2025-08-19 04:25:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| bb7272ff-96a5-3c35-bdb6-a9a8399e0b9c | -7.14207 | -44.60431 | 2025-08-19 04:25:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 88e61923-33ac-33cb-8c8c-c55fd1f9f94c | -6.05916 | -44.12027 | 2025-08-19 04:25:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b51725c0-f4d2-3dcc-9776-4ba49703384f | -3.9871 | -47.88557 | 2025-08-19 04:25:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| a0696e1b-e27b-3dc2-aab7-3cb31c45db4b | -6.68834 | -44.05849 | 2025-08-19 04:25:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e4679815-08b1-3218-acd7-d09f4117061f | -6.36403 | -43.27478 | 2025-08-19 04:25:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| bc0869c3-1910-3f6f-a220-03a39cd6b8da | -6.67963 | -43.68245 | 2025-08-19 04:25:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| cfe58003-e62b-3507-a7df-f0e89d61c8a0 | -6.94263 | -43.59024 | 2025-08-19 04:25:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| a3029399-1102-3b29-a00c-4f4ad9fed166 | -5.57358 | -44.08328 | 2025-08-19 04:25:00 | NOAA-21 | GOVERNADOR LUIZ ROCHA | MARANHÃO | Brasil | 2104628 | 21 | 33 | nan | nan | nan | Cerrado | 10.1 |
| b62116ee-a86a-3b95-b96a-c4a4007286d5 | -6.93918 | -43.59559 | 2025-08-19 04:25:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 12.7 |
| ce6d02a7-f554-361d-8394-170d4417cd39 | -3.58629 | -49.43312 | 2025-08-19 04:25:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| fc97d1cf-394d-3fae-90ee-86238c625088 | -7.3179 | -47.12164 | 2025-08-19 04:25:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a4f9b2c2-7524-3dbf-8a36-03aceb52c4b8 | -6.27142 | -43.70216 | 2025-08-19 04:25:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 85eeddb9-0357-3bf1-8498-de651402885c | -6.23652 | -44.45077 | 2025-08-19 04:25:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 77677cfa-49a8-3af7-9ec6-cc24d67174b7 | -5.75156 | -46.67715 | 2025-08-19 04:25:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 87ff2bde-fa64-3235-912e-a648ff0fe46c | -6.5198 | -43.44912 | 2025-08-19 04:25:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Caatinga | 4.8 |
| eea02e81-efe7-3554-8d94-1b6bf05fe950 | -3.44676 | -48.96786 | 2025-08-19 04:25:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 233312e1-a88a-30c0-9056-10d5561ced4f | -6.75629 | -41.55653 | 2025-08-19 04:25:00 | NOAA-21 | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 901fc240-dd22-339a-8006-d9f062aaae19 | -6.24519 | -44.83113 | 2025-08-19 04:25:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| da20bd1c-8578-3508-b539-a918ad5c4e73 | -6.37225 | -43.31852 | 2025-08-19 04:25:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| bec40d01-31ed-33d3-a6a9-df527e792ac3 | -6.94324 | -43.58614 | 2025-08-19 04:25:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 9.8 |
| a5fd303b-586e-3f08-9269-439f50275bb9 | -6.53061 | -43.44166 | 2025-08-19 04:25:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Caatinga | 1.2 |
| bc10fc7d-29a2-36ea-9fab-b6b0e3e03821 | -4.14686 | -46.4552 | 2025-08-19 04:25:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 0a728253-f681-3589-88da-1897a20b9a8b | -6.06551 | -44.12505 | 2025-08-19 04:25:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| e0ca9145-c3a7-3c82-8ac4-dfdf7f0bdc2a | -7.63195 | -46.22308 | 2025-08-19 04:25:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0284f6d5-096b-301f-b7ff-2ac18dcbac2a | -3.9844 | -42.52196 | 2025-08-19 04:25:00 | NOAA-21 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 5.3 |
| 4db4de37-3e46-3374-af0e-01bc57e963a6 | -6.19571 | -53.52194 | 2025-08-19 04:25:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 01cc618b-1e57-3425-a7e8-7afd6cd8b747 | -6.06494 | -44.12878 | 2025-08-19 04:25:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| be9fe316-e57c-3d79-8746-1bb38c95242b | -6.96886 | -43.58588 | 2025-08-19 04:25:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 35.1 |
| a4dad3a2-1090-35ea-b1b4-af92240a9320 | -3.9741 | -42.516 | 2025-08-19 04:25:00 | NOAA-21 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 3df47b9c-30cf-3bfa-b73c-c42058a19bf9 | -6.08588 | -44.58719 | 2025-08-19 04:25:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d31a17e9-efd4-3fd4-bf62-0ec5fbdd2925 | -6.94973 | -43.61639 | 2025-08-19 04:25:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| fa42da8a-f5ee-315f-885e-d79f0b1ffd53 | -5.87802 | -48.11662 | 2025-08-19 04:25:00 | NOAA-21 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8e81a4be-c650-3460-b48c-12e8cf21b883 | -3.1326 | -48.98608 | 2025-08-19 04:25:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 82a78027-ad2c-33d4-bfe4-74a934195b11 | -4.72539 | -37.84457 | 2025-08-19 04:25:00 | NOAA-21 | ITAIÇABA | CEARÁ | Brasil | 2306207 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| a3d7d8cc-099d-32eb-b60a-f260d1b5fa8e | -2.90858 | -48.29204 | 2025-08-19 04:25:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| c3b77d28-77a1-3313-b0e5-ec6899a13774 | -3.48303 | -47.67829 | 2025-08-19 04:25:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 50d3e29c-e605-3b5c-80ff-251a72b3bcf2 | -7.6281 | -46.22604 | 2025-08-19 04:25:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| dfd7a888-dbd5-3592-9e68-58685cbc602d | -5.98103 | -44.10524 | 2025-08-19 04:25:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d961055f-0b28-3dfe-acd5-bd7e46485a80 | -6.39855 | -44.28661 | 2025-08-19 04:25:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ee4c0869-bda8-3356-9d88-82f1d84830e5 | -6.55777 | -38.80024 | 2025-08-19 04:25:00 | NOAA-21 | ICÓ | CEARÁ | Brasil | 2305407 | 23 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 549b35e8-4ec8-3dce-a77d-c2b02ca3cc07 | -6.93313 | -43.61129 | 2025-08-19 04:25:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| db006878-fad5-3482-bd85-36836d1b169c | -6.59514 | -41.40398 | 2025-08-19 04:25:00 | NOAA-21 | SÃO JOÃO DA CANABRAVA | PIAUÍ | Brasil | 2209856 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 0f7f9a4c-7a4b-37c0-af3e-12b91321d41a | -3.48315 | -51.18942 | 2025-08-19 04:25:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 430e622e-8c1c-399b-a91a-3f60a3106774 | -3.25423 | -43.2744 | 2025-08-19 04:25:00 | NOAA-21 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 027f9d17-0747-3b94-8b33-60c33b53c354 | -6.53121 | -43.43755 | 2025-08-19 04:25:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 0869afa1-12fd-30bc-80dc-fbf65ffe1ddd | -5.57253 | -46.53877 | 2025-08-19 04:25:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 91087ec1-a54e-384a-9ac2-20174c0730e5 | -5.87462 | -48.11611 | 2025-08-19 04:25:00 | NOAA-21 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 952f0bfb-8e22-3d8a-9d0a-344cc4b69c23 | -4.92111 | -43.24839 | 2025-08-19 04:25:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 55acee88-9c36-3ffa-a7c0-84b21a4e8be0 | -2.44696 | -47.32641 | 2025-08-19 04:25:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| eed6672a-ce39-3c37-a4fa-a3b166dff409 | -6.68379 | -43.67895 | 2025-08-19 04:25:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 83535ef7-09ae-3e46-9f03-740b9dcf03ef | -5.65382 | -43.38174 | 2025-08-19 04:25:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2aeda9ed-de8f-32d8-93d1-8b4f1f13c5ef | -4.9236 | -43.25219 | 2025-08-19 04:25:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c08696e9-804e-3f08-97f1-7954a6c87d7e | -6.96529 | -43.58533 | 2025-08-19 04:25:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 35.1 |
| 936ca29f-f045-34c3-bac6-e82feb714ce8 | -6.55867 | -38.79849 | 2025-08-19 04:25:00 | NOAA-21 | ICÓ | CEARÁ | Brasil | 2305407 | 23 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 240a4cd3-f987-3c2c-bed9-630515629936 | -6.27497 | -43.70259 | 2025-08-19 04:25:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 33884827-e22e-3315-90da-dfb16f07f20f | -4.81751 | -47.31675 | 2025-08-19 04:25:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e781d4cd-e7e2-305d-8a91-8684ccd3d0ab | -4.59243 | -43.31192 | 2025-08-19 04:25:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8025b3b3-0ba2-393b-83de-af2206c7288c | -5.76257 | -46.67179 | 2025-08-19 04:25:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7d41f40d-5333-36b6-9695-533cee97ec71 | -5.78825 | -43.61635 | 2025-08-19 04:25:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 10.5 |
| a820077b-85e1-3621-a291-12f899f2b0f2 | -7.13629 | -44.39156 | 2025-08-19 04:25:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| fcc5748f-d344-3880-ac4b-09521a75e83a | -7.00994 | -44.27483 | 2025-08-19 04:25:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e29c9fa6-8d13-314f-a3ef-27e3ec69f05c | -6.93079 | -43.60266 | 2025-08-19 04:25:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 4bb979b3-2b56-32f4-b1ee-a4cbb2006efc | -6.9444 | -43.603 | 2025-08-19 04:25:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8b9464f4-e792-3947-9921-9e72691008d4 | -5.98162 | -44.10144 | 2025-08-19 04:25:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 964864d4-e000-3470-a5f4-e265d84e3e21 | -6.9438 | -43.60709 | 2025-08-19 04:25:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 88a60dca-eb09-3dea-98e6-de68eb30498b | -3.98504 | -42.51771 | 2025-08-19 04:25:00 | NOAA-21 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 5.3 |
| 55089a3d-b648-3f23-a0c9-393ff40fdb2b | -6.93308 | -43.60549 | 2025-08-19 04:25:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d7424c25-be41-369e-8dd5-8ccd22ea6d43 | -5.97981 | -44.13615 | 2025-08-19 04:25:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 1876612c-4869-388a-ac74-b7116138a126 | -5.41502 | -47.47321 | 2025-08-19 04:25:00 | NOAA-21 | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d0a446f9-4889-3ea0-b921-5d2306d7fd95 | -7.59872 | -45.42509 | 2025-08-19 04:25:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 0cb74ef4-24db-3a15-bbc5-fc991637313a | -6.93368 | -43.60142 | 2025-08-19 04:25:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e75954af-d2eb-3a56-8d3f-23a742d8417c | -6.06436 | -44.13255 | 2025-08-19 04:25:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f9965e1c-8bcc-3c7f-8d0b-40f3192c3516 | -5.64965 | -43.38523 | 2025-08-19 04:25:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8f7d4e2f-3ed8-3bdb-9250-29549f090398 | -5.97708 | -44.28922 | 2025-08-19 04:25:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 10c82be3-d5ee-3dfe-bc64-b147a6a79d2e | -7.57243 | -45.41727 | 2025-08-19 04:25:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 2059aa34-8c5c-32c8-836c-d20f0c2e6858 | -4.9188 | -43.2398 | 2025-08-19 04:25:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 99e69f1d-f245-3ebc-848d-dd0bc20104a1 | -6.62008 | -43.88522 | 2025-08-19 04:25:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 54311248-b650-331b-95d5-04f3ac86ff51 | -2.54273 | -47.71753 | 2025-08-19 04:25:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| fa45cc46-94eb-376b-801c-7a20cc57837f | -7.14263 | -44.6006 | 2025-08-19 04:25:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 2a4ae087-b23f-38c4-b354-86a6176dfede | -5.65786 | -43.40289 | 2025-08-19 04:25:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c98d8bfd-4778-338e-956d-5e3f78d7e223 | -6.9398 | -43.59149 | 2025-08-19 04:25:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 12.7 |
| bb57070d-4a8a-3f99-bcb7-200d6fe0e1a6 | -6.06261 | -44.12082 | 2025-08-19 04:25:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1373dc5b-3dad-3e5a-9bba-f05e3748a986 | -3.04596 | -49.43742 | 2025-08-19 04:25:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6b44f8f4-da5d-3dfc-b21e-0ff6a591b8f5 | -5.33951 | -41.26057 | 2025-08-19 04:25:00 | NOAA-21 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 044a9dfe-00e7-32e9-aa17-ac8a000afc46 | -7.37814 | -44.2779 | 2025-08-19 04:25:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5bdbf5bc-00df-3e31-9db0-fc06883fc439 | -5.38119 | -41.2278 | 2025-08-19 04:25:00 | NOAA-21 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 0260c761-d896-3276-baf9-96c0799212af | -4.27582 | -48.18741 | 2025-08-19 04:25:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7be0727e-8266-30ff-a834-4d207a8d9baa | -5.66574 | -43.37528 | 2025-08-19 04:25:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 475f9a3f-d8cd-3e35-b010-3c401ad16f20 | -5.88425 | -48.12136 | 2025-08-19 04:25:00 | NOAA-21 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8f87a50c-eb2e-3b6d-a994-cf30113dc906 | -6.96408 | -43.59353 | 2025-08-19 04:25:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 18.8 |
| 97bd9db7-f893-3ff3-83fa-4a847d4330e9 | -6.74681 | -41.5372 | 2025-08-19 04:25:00 | NOAA-21 | SÃO JOSÉ DO PIAUÍ | PIAUÍ | Brasil | 2210201 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 101b256e-1b62-323d-a4e9-802473e179eb | -5.97927 | -44.11673 | 2025-08-19 04:25:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ed2172af-e888-364f-8d1f-b1b14a375f6e | -4.15675 | -50.22691 | 2025-08-19 04:25:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c005ffed-da32-309e-811c-24f468d36c0b | -6.09021 | -44.39831 | 2025-08-19 04:25:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 14e0eac7-6026-341f-80fb-d647525ad565 | -5.54816 | -49.06891 | 2025-08-19 04:25:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 907c2627-bcf4-30b5-8242-35128635eb5d | -6.55025 | -43.9842 | 2025-08-19 04:25:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 353e92f4-3897-3152-94cf-853ceabfd5f7 | -6.95753 | -43.58833 | 2025-08-19 04:25:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2b94a361-ca88-3958-8f33-23a089ab3995 | -6.68084 | -43.67443 | 2025-08-19 04:25:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |


[Clique aqui para ver as próximas entradas](README24.md)
