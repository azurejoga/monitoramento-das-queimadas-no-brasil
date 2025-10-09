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

## Dados Diários - Página 36

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9a736d35-930e-3bc6-a494-449520518bc3 | -3.95473 | -44.29513 | 2025-10-09 04:17:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 49a0c881-002a-3976-a8d8-4496f9db0d1b | -5.40539 | -44.48919 | 2025-10-09 04:17:00 | NOAA-20 | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d6864958-89cb-37ee-a6d6-f925ece5cdec | -7.48388 | -43.09362 | 2025-10-09 04:17:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| dd1bc96b-ee2a-3d14-b6c1-a0cfd6250469 | -5.15517 | -46.09871 | 2025-10-09 04:17:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9b6df497-3871-3585-b05f-84c8c5229283 | -5.13286 | -46.25883 | 2025-10-09 04:17:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 919c459d-5c5c-340f-8bed-183900a423cf | -3.47108 | -50.02721 | 2025-10-09 04:17:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a3b11247-c414-3de1-aa41-4082ca031c59 | -3.38545 | -50.13855 | 2025-10-09 04:17:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e9593f81-f7b3-3962-aec5-c470a56607b5 | -3.58967 | -49.34796 | 2025-10-09 04:17:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 1ed7d219-6632-3cea-8645-a8a44037f1f8 | -5.23681 | -45.39776 | 2025-10-09 04:17:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8b9c0cca-899b-3227-af51-e03a07b6134e | -4.442 | -43.22914 | 2025-10-09 04:17:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 10112b07-c9b0-3ae7-b341-f402006781ad | -4.44255 | -43.22565 | 2025-10-09 04:17:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 8d396ceb-cbd7-3faf-948b-aacbce5a5067 | -6.57295 | -44.14993 | 2025-10-09 04:17:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 48d88d22-ce05-340f-ab2a-66058dbe2c56 | -4.73779 | -42.79371 | 2025-10-09 04:17:00 | NOAA-20 | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 21afd386-d29b-3d63-be00-1f736bdacbb1 | -12.2293 | -43.78644 | 2025-10-09 04:19:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 89757e84-ec1c-3c84-9b37-867c06e9f1c5 | -2.5324 | -48.48197 | 2025-10-09 04:19:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| de7fbe00-0b9c-3f5c-84ec-a4df2ac0a21e | -8.19771 | -43.34785 | 2025-10-09 04:19:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| e8e12298-b3b4-395e-a028-f907df4da256 | -7.79471 | -42.40866 | 2025-10-09 04:19:00 | NOAA-20 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 2bd4ad5c-8add-330c-9d48-f35c10df50b3 | -11.48121 | -43.4842 | 2025-10-09 04:19:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 16b8f97e-1785-39af-ac19-4ad40864ae99 | -13.78451 | -45.84639 | 2025-10-09 04:19:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e96dc9b4-03fe-3cc5-8e19-6b038dc8d276 | -11.72292 | -44.29312 | 2025-10-09 04:19:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 349906f0-d9a0-30fe-afa8-53c6ad8a0edc | -14.96479 | -42.85323 | 2025-10-09 04:19:00 | NOAA-20 | ESPINOSA | MINAS GERAIS | Brasil | 3124302 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 365e11fb-9fe7-3c59-bf15-eff31bf8fb67 | -7.76623 | -42.4082 | 2025-10-09 04:19:00 | NOAA-20 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| a3116d5d-e46d-3fb3-9ac3-4710668508f2 | -7.31597 | -44.86733 | 2025-10-09 04:19:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7a704be0-2994-33e3-b8de-74b30361cbca | -7.75938 | -44.0329 | 2025-10-09 04:19:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 058f8b69-d0fb-3a97-9381-85bc57ff802d | -14.41728 | -43.98211 | 2025-10-09 04:19:00 | NOAA-20 | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 47f4784a-153e-3922-8c71-e471d936088d | -11.8763 | -44.93292 | 2025-10-09 04:19:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5382d15a-78ea-3ec8-b424-1483bc0c8eeb | -8.43661 | -47.18985 | 2025-10-09 04:19:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 5b71f914-17b6-3d9f-bb71-63f2b02dc5eb | -13.80053 | -45.8308 | 2025-10-09 04:19:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b448f224-a81c-319d-b082-92ddde6e569e | -10.8732 | -44.28438 | 2025-10-09 04:19:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 38f44adf-3dd2-3798-879b-afff1e3ade8b | -13.79389 | -45.85155 | 2025-10-09 04:19:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8d54f4f4-f956-325c-972f-1c1743c39c97 | -8.5312 | -46.19717 | 2025-10-09 04:19:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 56166b42-98a2-371e-b5f4-09c56f0dc922 | -13.82538 | -45.82394 | 2025-10-09 04:19:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 26176bf9-3d00-3a88-a637-95e8bf4e5479 | -7.6181 | -45.4676 | 2025-10-09 04:19:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f48e252f-1204-39ee-9d11-c0cdc8d7b343 | -13.80285 | -43.9323 | 2025-10-09 04:19:00 | NOAA-20 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bc022e29-c58c-3158-9e94-6139f7637894 | -13.36968 | -47.21519 | 2025-10-09 04:19:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5cb1dda3-1af2-3543-83c0-c2ab4b944f94 | -7.79362 | -46.72461 | 2025-10-09 04:19:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6051d065-d815-300a-94ca-8fa87aa3b929 | -7.79789 | -44.20034 | 2025-10-09 04:19:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 9.0 |
| ae5bba12-d87e-30a1-a4fe-89c45790ac76 | -11.13272 | -47.74262 | 2025-10-09 04:19:00 | NOAA-20 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5d797994-576b-3aac-85cd-54a5eeb223f5 | -7.48436 | -47.15772 | 2025-10-09 04:19:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 97fc83e7-c918-30c0-9e04-eb3196eda83e | -8.67346 | -43.91845 | 2025-10-09 04:19:00 | NOAA-20 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d3446d2e-5498-3a7b-ba19-13373a6b11d7 | -7.73557 | -42.412 | 2025-10-09 04:19:00 | NOAA-20 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 1df715fa-6af4-3034-a070-7f5a0d447179 | -11.52146 | -43.31208 | 2025-10-09 04:19:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2fa3e293-fe53-3180-98ca-266b73265d94 | -11.13208 | -47.74657 | 2025-10-09 04:19:00 | NOAA-20 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| aaf43ac1-8a02-3293-9890-cecea1f2f7e7 | -7.19992 | -45.49055 | 2025-10-09 04:19:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 6afd5816-a539-321a-8e17-106e7d513897 | -9.18904 | -47.85729 | 2025-10-09 04:19:00 | NOAA-20 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| aecadbff-f09b-3856-b5cc-1a021448e034 | -11.76775 | -45.15244 | 2025-10-09 04:19:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d5350a32-0b04-33ac-be05-1b5dc557826a | -14.40521 | -46.02403 | 2025-10-09 04:19:00 | NOAA-20 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0c61cf84-ba10-3a05-9af0-f03ae1cb2bd9 | -9.98352 | -43.59952 | 2025-10-09 04:19:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| be267eaf-298e-3c4a-b9de-796613f29837 | -9.40383 | -45.94619 | 2025-10-09 04:19:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 84e41350-4d70-31dd-a2bb-e60eff38a9cd | -10.65802 | -44.15937 | 2025-10-09 04:19:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4a7476ab-df9c-350e-970f-c793d865a78b | -8.5693 | -48.87587 | 2025-10-09 04:19:00 | NOAA-20 | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 393741b8-94ef-30e1-9544-d756946ce4c4 | -8.55725 | -44.62061 | 2025-10-09 04:19:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1deb660f-c645-3168-978c-49656daa24ad | -10.19635 | -44.55937 | 2025-10-09 04:19:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5a8f8863-0ef0-3e5c-b608-90c9742ef822 | -8.44007 | -47.19041 | 2025-10-09 04:19:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 7.3 |
| f429923c-8deb-3178-8d06-b5a80e087a61 | -10.09374 | -40.89487 | 2025-10-09 04:19:00 | NOAA-20 | CAMPO FORMOSO | BAHIA | Brasil | 2906006 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 30b0a4bb-fbae-3b4f-95e6-b54d64405f12 | -12.05089 | -43.50349 | 2025-10-09 04:19:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 29e00f98-b2eb-3dca-8c03-b5424252566e | -11.78544 | -45.14804 | 2025-10-09 04:19:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 42751994-6ff0-344c-9ce1-3c2b385136b7 | -8.17342 | -43.3254 | 2025-10-09 04:19:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 1c268c89-016e-3b31-a909-f48aeb285148 | -12.65046 | -43.42669 | 2025-10-09 04:19:00 | NOAA-20 | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 81005ac1-ac0f-3f39-997a-26fa40d0ba73 | -7.78839 | -48.04204 | 2025-10-09 04:19:00 | NOAA-20 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d38c4911-e11e-3a5d-b2dc-d8f922ac5ccc | -14.41844 | -43.97423 | 2025-10-09 04:19:00 | NOAA-20 | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 14.8 |
| 3455b9a0-a3d1-38f8-8677-df1dc6a34465 | -2.4909 | -47.57571 | 2025-10-09 04:19:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3a4c5013-07e0-3938-8d10-6bfc266ba2d8 | -11.13629 | -47.94872 | 2025-10-09 04:19:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| d714c8d6-b7de-313b-8b7f-3f09291434d5 | -7.79295 | -42.42028 | 2025-10-09 04:19:00 | NOAA-20 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 567d6898-ee3f-35a5-85f0-65caa69193a6 | -13.25371 | -46.47749 | 2025-10-09 04:19:00 | NOAA-20 | DIVINÓPOLIS DE GOIÁS | GOIÁS | Brasil | 5208301 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 40531a2d-5f41-3888-9409-2d8d9a302dbc | -11.47834 | -43.47982 | 2025-10-09 04:19:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 900e40ca-f85b-34e7-837a-c6cdc4f9dbae | -14.70893 | -45.18061 | 2025-10-09 04:19:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2acd7705-25dc-3634-858d-4c7942abedb4 | -14.79021 | -46.10178 | 2025-10-09 04:19:00 | NOAA-20 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7aade223-538e-3786-bc62-3f19a1155295 | -7.71591 | -42.37714 | 2025-10-09 04:19:00 | NOAA-20 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 44d4abaa-4572-32eb-ab4b-ed3241e66dfa | -10.19525 | -44.56645 | 2025-10-09 04:19:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a336c047-2f3c-3f8a-9528-14e16e356980 | -11.78931 | -45.14503 | 2025-10-09 04:19:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 2a2156ae-d41e-3150-bf35-fd9ed68012ef | -7.80398 | -44.20488 | 2025-10-09 04:19:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| bb0376fa-6a6e-3125-b07e-b90819b179de | -13.82096 | -45.83048 | 2025-10-09 04:19:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c116c092-6403-3e8e-a292-4f7cc16ccc7f | -9.78693 | -47.75036 | 2025-10-09 04:19:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 6ca4fee9-0f47-3ace-bb2c-bafb72d89642 | -2.28949 | -47.40192 | 2025-10-09 04:19:00 | NOAA-20 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8896e8de-345f-3198-9cd3-9f57850bb8ad | -13.81378 | -45.83295 | 2025-10-09 04:19:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 80557095-3f08-3e34-bf85-1f09469da064 | -13.12783 | -43.90767 | 2025-10-09 04:19:00 | NOAA-20 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 8.0 |
| e6287c4b-a725-3be8-ae69-e9dc5e574d87 | -8.50907 | -44.23295 | 2025-10-09 04:19:00 | NOAA-20 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 359b3d82-cc4c-3554-a3a0-1389081f7a8a | -2.3619 | -48.53619 | 2025-10-09 04:19:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b81e88df-a056-3a13-8d87-7f7e87d106bd | -14.42192 | -43.97477 | 2025-10-09 04:19:00 | NOAA-20 | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 14.8 |
| c8fe65a9-19ea-39b6-b6fe-fa541c3d33c1 | -8.00092 | -44.46457 | 2025-10-09 04:19:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 46360207-ab2b-3320-9597-a3069d469106 | -11.78489 | -45.15156 | 2025-10-09 04:19:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| bf31fb1c-3156-3728-a110-0719690125d5 | -8.53224 | -46.21207 | 2025-10-09 04:19:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| bff843bc-ec43-3fe9-809c-9f591d80bff8 | -7.68389 | -42.4 | 2025-10-09 04:19:00 | NOAA-20 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 581993c9-40a8-341b-a465-0c6c3738c300 | -10.82607 | -42.8201 | 2025-10-09 04:19:00 | NOAA-20 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 17e3117e-815d-3e33-9857-8370659dd331 | -8.00038 | -44.46804 | 2025-10-09 04:19:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 2c39b69d-b564-3204-afbf-3574ee244ec4 | -7.55837 | -44.2986 | 2025-10-09 04:19:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| fd2f20b2-31b3-3bad-be53-add447cba2f3 | -3.36181 | -43.38036 | 2025-10-09 04:19:00 | NOAA-20 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 773ab041-cf05-3b0e-a78a-04bc2f5db19a | -7.17733 | -46.71899 | 2025-10-09 04:19:00 | NOAA-20 | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| c3170ec9-a99d-31f8-93db-06cf5d25da33 | -10.92739 | -42.8426 | 2025-10-09 04:19:00 | NOAA-20 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 1f156af2-699b-3a7f-b1af-bb1a4b8f8045 | -7.45269 | -47.17643 | 2025-10-09 04:19:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ca54f802-fe6e-37c1-99b6-0b2ee04ffea5 | -9.19129 | -43.12205 | 2025-10-09 04:19:00 | NOAA-20 | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 7e1ad7e7-1acb-32f1-af4b-dc6ad9b93958 | -13.79168 | -45.86573 | 2025-10-09 04:19:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 74382a74-f5e7-3e88-8ab5-0478cef16fd1 | -10.09464 | -40.77738 | 2025-10-09 04:19:00 | NOAA-20 | CAMPO FORMOSO | BAHIA | Brasil | 2906006 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 8fb4f920-e1c6-3cbb-afe7-4f2f5d99f5c5 | -11.74893 | -45.1422 | 2025-10-09 04:19:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 5e50dece-7253-35d2-ae0b-c3e00febd19f | -11.99689 | -45.18514 | 2025-10-09 04:19:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 9df3f1b6-954a-388c-a7fe-79f3f5923f66 | -7.76363 | -44.20207 | 2025-10-09 04:19:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| eb1dc9d0-98d8-3b3e-bab1-56c76b123879 | -7.79458 | -44.19982 | 2025-10-09 04:19:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 4b43a2e6-7393-3763-996f-ae2cc455cd76 | -11.98584 | -45.21236 | 2025-10-09 04:19:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 667588c3-c987-3913-942c-8c8ea29d2730 | -14.08331 | -46.08432 | 2025-10-09 04:19:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |


[Clique aqui para ver as próximas entradas](README37.md)
