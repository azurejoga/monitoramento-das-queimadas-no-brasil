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

## Dados Diários - Página 11

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 798e54db-e281-38d9-b249-262689ec05e4 | -3.82542 | -41.56689 | 2025-07-29 04:19:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 1bf39ba5-6b55-3dea-911e-561cf8f696b8 | -3.36317 | -49.16305 | 2025-07-29 04:19:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| baf424f2-e237-370e-863b-2ff3a308757b | -2.8291 | -52.35555 | 2025-07-29 04:19:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ca3881dd-25e4-34ce-a6f8-6f31877c8286 | -3.25827 | -43.27388 | 2025-07-29 04:19:00 | NOAA-21 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a28e03af-124f-313f-a29d-63d4315ec84d | -7.46027 | -49.39885 | 2025-07-29 04:19:00 | NOAA-21 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 680c1064-f476-3004-8f3d-f677497d4dba | -6.39311 | -53.33507 | 2025-07-29 04:19:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| bd3e3ce3-847b-3416-98b5-b3f432b5a04f | -7.94198 | -44.09245 | 2025-07-29 04:19:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f83e44a7-74cb-3a4a-a1bc-4e1d2e4b4213 | -3.9323 | -43.15892 | 2025-07-29 04:19:00 | NOAA-21 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1acb0904-9cab-3b19-8076-0c689e7fb54a | -7.4582 | -49.40102 | 2025-07-29 04:19:00 | NOAA-21 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 84469816-38a1-3167-9233-64a9b010848a | -6.40571 | -53.35269 | 2025-07-29 04:19:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5fdff288-dd93-3d29-8732-7a3809cd98ad | -2.89561 | -48.28899 | 2025-07-29 04:19:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e5a53ec8-931a-33e6-8bea-e7970a4ae959 | -2.77345 | -49.19881 | 2025-07-29 04:19:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 74b59926-bcd5-3a70-8c04-2caedf2d3908 | -6.17297 | -44.42913 | 2025-07-29 04:19:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5e864a99-dc94-303d-9511-7a652b86ea4f | -6.17351 | -44.42567 | 2025-07-29 04:19:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| fe2b12b0-e311-3c97-a5b9-766c2f8a57ee | -6.64925 | -43.03207 | 2025-07-29 04:19:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 07f8b10c-c070-3bd7-a5f6-77fd5efcf972 | -7.92526 | -44.08984 | 2025-07-29 04:19:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 13d6be4c-ab4f-3cc4-94ba-0977fca4851f | -7.86129 | -46.73278 | 2025-07-29 04:19:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 3959cc25-c7d6-3770-9601-2d6563f67633 | -5.27813 | -44.4754 | 2025-07-29 04:19:00 | NOAA-21 | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ecddbfec-0f23-3a2a-96ed-c0415147ee87 | -3.04184 | -49.42377 | 2025-07-29 04:19:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3f83cc4b-3f32-31c4-a5e6-2bf11a939b9a | -7.93973 | -44.0848 | 2025-07-29 04:19:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 72d8e0ce-fc25-3e67-8254-5be7f51af501 | -7.24368 | -43.06414 | 2025-07-29 04:19:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 6.6 |
| 1a8c0487-9381-3fba-a407-a0cc33a19995 | -7.92472 | -44.09341 | 2025-07-29 04:19:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 42ecd504-0d27-33af-a277-546f8079dcd3 | -8.81949 | -43.9296 | 2025-07-29 04:19:00 | NOAA-21 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 20b8af2e-8e8e-3dce-93fe-a7556458e3cb | -9.51757 | -40.35534 | 2025-07-29 04:19:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 60c4aa25-4e9b-3999-a01c-1fe16e125dcc | -4.01595 | -41.79065 | 2025-07-29 04:19:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| c49cda9b-dd92-3a0d-9336-f9f37748bb9f | -6.49453 | -56.20737 | 2025-07-29 04:19:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 79a27405-ef97-35c3-841e-01b73e7e538a | -2.99615 | -49.31979 | 2025-07-29 04:19:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bb7473a3-1752-36fc-968d-60e9fe6a2767 | -8.2232 | -44.91198 | 2025-07-29 04:19:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 410a95b1-f88c-3874-b4b8-e99b056d263b | -6.40639 | -53.31883 | 2025-07-29 04:19:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b7b2de55-0975-3cf7-9bad-a248a0a9e8d8 | -8.51259 | -43.3178 | 2025-07-29 04:19:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 19cc241d-34f8-371c-a3b4-30e1e0d31f84 | -6.38751 | -53.33717 | 2025-07-29 04:19:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e459f7c5-543b-33be-b3c8-4f0b6ccac484 | -2.89868 | -48.29428 | 2025-07-29 04:19:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| acaf1e9b-6cf4-3a97-8546-09e29f120302 | -7.85849 | -46.7286 | 2025-07-29 04:19:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 2d43a00f-bd35-3884-be61-a68d74f78085 | -4.10548 | -48.20313 | 2025-07-29 04:19:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 02e1f58c-0913-3e3a-b14d-ddd2f4c1831f | -11.4201 | -45.1181 | 2025-07-29 04:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 65.2 |
| a098a53d-ea58-34da-88ed-cc97acb3f43c | -11.4393 | -45.1154 | 2025-07-29 04:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 86.0 |
| 439f8b74-3025-32b0-a455-e08c59aaf398 | -11.7508 | -48.1825 | 2025-07-29 04:20:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 47.7 |
| e975cdb8-adbf-31cd-bb54-88db13a1d6f7 | -11.4389 | -45.1385 | 2025-07-29 04:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 51.4 |
| e34240d4-80b4-394b-884c-91f8efb50823 | -13.48449 | -45.59474 | 2025-07-29 04:21:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| d3e137de-84b0-3ace-bc5a-4405cab04a3b | -13.48782 | -45.59526 | 2025-07-29 04:21:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| ba1f2414-8016-3fbe-bbd3-4f4f18f2fcb3 | -12.70676 | -47.79215 | 2025-07-29 04:21:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 50d2d041-2058-3e6d-810a-824f196b61c8 | -13.00699 | -44.88841 | 2025-07-29 04:21:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f0ad69cf-ee45-3c98-8176-604c0182ee1a | -11.43565 | -45.12805 | 2025-07-29 04:21:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| ae4b70e4-8801-3ee6-a32d-d19a28cc3d6c | -13.13532 | -47.34566 | 2025-07-29 04:21:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 67adb767-4376-3a50-977f-69c00d71a960 | -14.5103 | -46.54461 | 2025-07-29 04:21:00 | NOAA-21 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| b1376fa3-e41b-3480-b5e7-69a13e9615ce | -8.74934 | -48.04599 | 2025-07-29 04:21:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f3bf9f2e-34c5-3742-b11a-e85bf9ace573 | -9.36326 | -45.73471 | 2025-07-29 04:21:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| fb6b862c-29a0-398a-a5f1-bb7e7238bed9 | -12.16168 | -47.34706 | 2025-07-29 04:21:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 631ba0af-3d24-3d7f-9041-b7c65213bd82 | -14.35549 | -47.09811 | 2025-07-29 04:21:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 298fc15d-1029-3618-9f67-1af1b7c3f655 | -9.4019 | -45.48774 | 2025-07-29 04:21:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 6.3 |
| a18bfd36-981e-3806-bb83-1c0dc0f1b710 | -10.63177 | -45.22937 | 2025-07-29 04:21:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d4d04cf9-053c-3ea3-b82b-81ab815af495 | -12.00039 | -46.97464 | 2025-07-29 04:21:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 87f57e5d-75e9-32be-be55-1949578fed03 | -9.57611 | -43.86513 | 2025-07-29 04:21:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| c5f3c2aa-c2d1-3793-8111-8d956e46c734 | -9.22978 | -43.15816 | 2025-07-29 04:21:00 | NOAA-21 | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 00012202-791c-3b28-a1e1-98f0d7323872 | -12.99803 | -44.90209 | 2025-07-29 04:21:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d5367b69-1563-3810-9034-61028dfadfaa | -11.7434 | -48.18617 | 2025-07-29 04:21:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 22.4 |
| c4490722-7163-3a45-bfdc-08643972d263 | -15.1304 | -45.32954 | 2025-07-29 04:21:00 | NOAA-21 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 2e1c3f59-89d6-3419-84aa-ab2df0124931 | -14.22354 | -43.94432 | 2025-07-29 04:21:00 | NOAA-21 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 11435a22-8277-3022-9766-517fab9cbb4b | -9.32776 | -47.5947 | 2025-07-29 04:21:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 4eb37ed7-62bd-35a2-a7da-af3b079ea863 | -11.55709 | -47.32148 | 2025-07-29 04:21:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4d9589d5-299b-3809-9e0f-9255e8561e9a | -11.27297 | -44.65466 | 2025-07-29 04:21:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| af25b622-ac84-3f26-9917-5e8c9e42459f | -10.93551 | -45.79104 | 2025-07-29 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 787dec6f-c37f-3a70-840b-5be3d7713ba2 | -13.12798 | -47.37358 | 2025-07-29 04:21:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7eb32919-f374-3f4d-813e-418ad289762b | -10.93275 | -45.78702 | 2025-07-29 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 884fdd31-32a9-399e-a601-bcfb584d5719 | -8.94765 | -46.74756 | 2025-07-29 04:21:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 10.1 |
| e07273bf-3ac3-38a7-8041-fefe2011c10b | -9.45377 | -57.84922 | 2025-07-29 04:21:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| ebf1fb16-dfff-3403-966e-9f5b7be5b123 | -11.98197 | -46.96445 | 2025-07-29 04:21:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 74dc0f6f-4ead-3b99-988a-3e1b98ab3065 | -9.4602 | -57.85043 | 2025-07-29 04:21:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 812371c0-6832-3356-9e63-9c415c26cc4c | -12.0021 | -46.96396 | 2025-07-29 04:21:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d709e700-5942-39bd-9714-6d55f260648e | -14.3755 | -50.32589 | 2025-07-29 04:21:00 | NOAA-21 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| cb80ec08-9691-3a6b-ad6b-652352a1ffa3 | -9.74804 | -48.66502 | 2025-07-29 04:21:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6a6c906b-01a7-35f4-bb08-0c8af04f495f | -11.9981 | -46.94884 | 2025-07-29 04:21:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c04b6cfa-7a66-3f7b-9182-3b21a3fdfbd4 | -14.12874 | -45.28414 | 2025-07-29 04:21:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c8fa448b-3b90-33c1-8ac3-f860aec30a41 | -13.06566 | -47.37796 | 2025-07-29 04:21:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1f3bc018-4db0-3114-bda3-b7641fe19903 | -14.34886 | -47.09702 | 2025-07-29 04:21:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 41e36681-7d81-3527-accb-788e554159b8 | -9.40135 | -45.49122 | 2025-07-29 04:21:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 7.7 |
| c12cad6d-516b-348d-80b0-3ace9a25c97c | -13.00864 | -44.87735 | 2025-07-29 04:21:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 60cd6efa-b9bd-3657-b1f9-513d1d14eacf | -13.08938 | -47.31539 | 2025-07-29 04:21:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3beb8b6a-e491-3a4f-a2bf-6b113816fcfe | -11.34176 | -51.24913 | 2025-07-29 04:21:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 7420bbfb-5725-3915-8896-d965a282656e | -12.00324 | -46.95684 | 2025-07-29 04:21:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d8dc0cdc-e0bb-3a2b-8ed7-ea0dd6dd417f | -11.99706 | -46.97409 | 2025-07-29 04:21:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 247a45a6-f5e4-3303-a022-4137634134fd | -10.96957 | -42.17376 | 2025-07-29 04:21:00 | NOAA-21 | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 6182cfb7-ebb1-305e-8917-5367be003ef3 | -13.50782 | -45.59841 | 2025-07-29 04:21:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d3ff0c23-2dac-3e9e-80d6-6e1ac888d85e | -13.00141 | -44.90261 | 2025-07-29 04:21:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6fe0ba80-6fbf-323a-8bdf-eb456004a0f7 | -9.08369 | -50.85148 | 2025-07-29 04:21:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 65a28edf-ed0e-337d-81fe-e8906be0112b | -11.56977 | -44.84846 | 2025-07-29 04:21:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d615e2e4-7cfc-3fb6-90bd-b84eabbfe5cf | -14.49762 | -46.53888 | 2025-07-29 04:21:00 | NOAA-21 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 6d84c1d8-70c8-37b6-8f6c-5797ebe7f28c | -13.09051 | -47.30828 | 2025-07-29 04:21:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 90b9e426-1cfb-3180-be27-ce83a42a8a88 | -13.13865 | -47.34625 | 2025-07-29 04:21:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a24c9336-eaf5-3043-a605-a7b496b23641 | -12.94612 | -44.7322 | 2025-07-29 04:21:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 168b3a1e-bc54-3649-8bf2-30c1ab980af2 | -10.93221 | -45.79052 | 2025-07-29 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4c8ca65b-31fb-3965-8169-218f8eddd301 | -13.06794 | -47.3637 | 2025-07-29 04:21:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 73763415-d656-3864-8b77-c88515fd158e | -11.73997 | -48.1856 | 2025-07-29 04:21:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 22.4 |
| f51f0068-391e-357c-8d27-617dcc119084 | -11.24135 | -40.97966 | 2025-07-29 04:21:00 | NOAA-21 | VÁRZEA NOVA | BAHIA | Brasil | 2933158 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 92d60c41-de29-30ba-aa42-06a72411a0ec | -14.74553 | -46.29883 | 2025-07-29 04:21:00 | NOAA-21 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d34180c1-7b11-30ca-ab3d-86e5cb26bd12 | -13.00644 | -44.89209 | 2025-07-29 04:21:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a495e78e-59d4-3f61-93e4-516f810eec6a | -13.06624 | -47.37438 | 2025-07-29 04:21:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5e8fd258-c6d2-3051-a2b1-438f34e88bde | -13.49452 | -45.61837 | 2025-07-29 04:21:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f5061ec6-1190-381a-8d4a-286cb29e410d | -14.57837 | -52.87679 | 2025-07-29 04:21:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ce952f81-75b7-32af-be55-a70aec725d8f | -11.34645 | -51.24622 | 2025-07-29 04:21:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |


[Clique aqui para ver as próximas entradas](README12.md)
