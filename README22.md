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

## Dados Diários - Página 22

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 871809ed-8aff-3618-bc6e-566dbb0543c7 | -6.37183 | -45.75903 | 2025-10-19 04:10:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 19.3 |
| 513bc8a9-d041-31a2-a57a-2106793fb215 | -7.04951 | -41.82993 | 2025-10-19 04:10:00 | NPP-375D | SÃO JOÃO DA VARJOTA | PIAUÍ | Brasil | 2209955 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 132d45d8-7d16-3222-a807-0c76c2827d4f | -2.70403 | -49.86967 | 2025-10-19 04:10:00 | NPP-375D | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9f7fad37-379b-3e5e-977a-df5efdbd65aa | -6.85432 | -46.92887 | 2025-10-19 04:10:00 | NPP-375D | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d50f3c7f-7de1-36fd-a94e-3028d22ae7a6 | -2.43991 | -49.36821 | 2025-10-19 04:10:00 | NPP-375D | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1bea6976-ccc6-39de-a610-be80ce8736ec | -8.04642 | -41.1033 | 2025-10-19 04:10:00 | NPP-375D | PAULISTANA | PIAUÍ | Brasil | 2207801 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 003e1b09-b38a-3791-bfd7-05328001bed0 | -3.64168 | -49.97007 | 2025-10-19 04:10:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 33cd1a31-409d-3fcb-974a-6fbd6077674d | -2.70572 | -49.85968 | 2025-10-19 04:10:00 | NPP-375D | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 43fa235c-e9d0-3a9c-bf1f-40b084d50a41 | -4.93128 | -43.40989 | 2025-10-19 04:10:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1de41875-624a-3b9a-a025-fbbe7c54ffab | -3.12508 | -50.21219 | 2025-10-19 04:10:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 57fdfeba-6bca-386d-b72b-6e631abfc147 | -5.95966 | -44.19462 | 2025-10-19 04:10:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f97eb934-993c-3277-bfa4-1c406b8cba5f | -5.37466 | -42.79985 | 2025-10-19 04:10:00 | NPP-375D | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 76e190f4-3484-3700-be07-53b9172dbbcb | -5.04989 | -49.64921 | 2025-10-19 04:10:00 | NPP-375D | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7d5d5888-8a19-3eaf-8f0b-fd30b6320674 | -4.03444 | -43.18134 | 2025-10-19 04:10:00 | NPP-375D | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| bd52fc4a-3605-37d5-81eb-ae79ad8aae84 | -7.04725 | -41.82252 | 2025-10-19 04:10:00 | NPP-375D | SÃO JOÃO DA VARJOTA | PIAUÍ | Brasil | 2209955 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 0754c4f1-688f-3bc3-a5c2-ad580e8687c3 | -6.25955 | -42.6857 | 2025-10-19 04:10:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| d75a009d-217f-3da2-bcf6-60718a79b31d | -2.91386 | -52.72435 | 2025-10-19 04:10:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 13.7 |
| d8ce3143-10f0-3616-99bd-7caec67d010a | -3.14117 | -50.25023 | 2025-10-19 04:10:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 779fd7c7-0db7-3cfa-ad64-67f051c1ed1f | -4.11303 | -38.1738 | 2025-10-19 04:10:00 | NPP-375D | CASCAVEL | CEARÁ | Brasil | 2303501 | 23 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 722ffcf1-7e1f-3e33-ab5a-ce61c2c7d066 | -2.24949 | -51.91397 | 2025-10-19 04:10:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f848fdf4-cfee-3d00-9505-1b25aec8ef72 | -7.3411 | -43.86362 | 2025-10-19 04:10:00 | NPP-375D | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 07b4abb8-0fac-35fb-929f-1e4317a6ca38 | -4.9555 | -45.09225 | 2025-10-19 04:10:00 | NPP-375D | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 3fa0bc4d-2b44-3c2d-8598-0e281f700753 | -6.8995 | -39.7468 | 2025-10-19 04:10:00 | NPP-375D | ASSARÉ | CEARÁ | Brasil | 2301604 | 23 | 33 | nan | nan | nan | Caatinga | 0.4 |
| c8cd477d-c2fa-33eb-9a3a-705ecae7f397 | -5.48428 | -48.65155 | 2025-10-19 04:10:00 | NPP-375D | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 77a0ded2-e18c-368b-b763-ed374e7ac15b | -7.49926 | -42.13338 | 2025-10-19 04:10:00 | NPP-375D | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| f3b6b8a9-9f24-3004-b628-7f022bab133c | -4.14445 | -47.65629 | 2025-10-19 04:10:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 65d1e658-6d37-3b19-a3ea-b330ef64ebaf | -7.40875 | -44.80422 | 2025-10-19 04:10:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 89e74c0d-3739-3e9a-a44c-634a7678a7c9 | -4.58431 | -45.64882 | 2025-10-19 04:10:00 | NPP-375D | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f0a2f868-159b-3d80-9a91-5264ae1a2a2d | -7.1828 | -46.56434 | 2025-10-19 04:10:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0046a305-3ecf-3f7f-95d8-c8d026b11be6 | -5.86515 | -42.8103 | 2025-10-19 04:10:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 6ee55149-f02b-3734-abaf-aadb0fb0870d | -6.38647 | -43.45504 | 2025-10-19 04:10:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 5999bb4e-a75a-3a27-a800-ccc592184280 | -5.66719 | -44.70721 | 2025-10-19 04:10:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0154c4e3-a470-3546-b364-3d1392e27400 | -6.31643 | -44.32603 | 2025-10-19 04:10:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 82b39d55-f11b-3030-aaf5-a9df682ef72e | -4.24829 | -40.34994 | 2025-10-19 04:10:00 | NPP-375D | SANTA QUITÉRIA | CEARÁ | Brasil | 2312205 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 75688b06-7b3d-3009-90b3-927ba644c127 | -4.27234 | -44.46993 | 2025-10-19 04:10:00 | NPP-375D | ALTO ALEGRE DO MARANHÃO | MARANHÃO | Brasil | 2100436 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 96febc7d-0f20-34a2-922f-4df349bb4f72 | -4.40282 | -44.0859 | 2025-10-19 04:10:00 | NPP-375D | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 65a3673e-ced8-39b9-99c1-831486240404 | -6.43701 | -43.92161 | 2025-10-19 04:10:00 | NPP-375D | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 6957f7ca-565c-3acc-9cad-64177e1ac9f1 | -4.48675 | -50.56345 | 2025-10-19 04:10:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f03d6498-a303-3095-b84f-e37335e52dae | -3.16149 | -49.16557 | 2025-10-19 04:10:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 09504b84-ea82-37fa-9a78-1199c946ad57 | -7.84005 | -41.7527 | 2025-10-19 04:10:00 | NPP-375D | SIMPLÍCIO MENDES | PIAUÍ | Brasil | 2210805 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| fac4ecb6-ec5f-37ba-93eb-98c57eeb8f5d | -5.70969 | -43.82122 | 2025-10-19 04:10:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 8fe60e89-6b27-383f-a226-d1eed769c5bb | -7.1959 | -42.20686 | 2025-10-19 04:10:00 | NPP-375D | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 3090404f-223c-30e8-a4eb-10035fd04a96 | -3.04494 | -40.11219 | 2025-10-19 04:10:00 | NPP-375D | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| c562959b-fde6-342c-bda4-ce005b044507 | -3.11853 | -49.2166 | 2025-10-19 04:10:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bb8dbb38-36d8-3f70-95d3-fc3c1a6c4a75 | -7.19534 | -42.21035 | 2025-10-19 04:10:00 | NPP-375D | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| b50f9a23-ee19-3a9d-99cf-5bf7bfc4c563 | -7.41694 | -40.07545 | 2025-10-19 04:10:00 | NPP-375D | BODOCÓ | PERNAMBUCO | Brasil | 2602001 | 26 | 33 | nan | nan | nan | Caatinga | 2.2 |
| ac5fb350-cf57-3e00-8099-228d7543c86b | -5.70907 | -43.8251 | 2025-10-19 04:10:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 4cd38be6-6363-3a8b-833a-791589dab3ca | -2.72814 | -48.34555 | 2025-10-19 04:10:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fa00978f-8c27-3b7c-a008-0979aa0aa1d4 | -5.17636 | -46.10795 | 2025-10-19 04:10:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4c26dbe2-ddb9-39ac-958b-1e86c8eda5ee | -2.70643 | -49.54174 | 2025-10-19 04:10:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5c9cac43-64af-3a46-9334-6e44451afae3 | -3.03202 | -47.81076 | 2025-10-19 04:10:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cfc96319-bf23-38e5-a337-80ff56de7538 | -4.23725 | -43.1016 | 2025-10-19 04:10:00 | NPP-375D | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6f04c798-aa98-31c7-bad4-82d5ae3b1704 | -6.4301 | -43.35917 | 2025-10-19 04:10:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 71ff5497-4974-3481-80bb-1b9a1059026c | -4.94055 | -43.06525 | 2025-10-19 04:10:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ee2433fa-9208-393e-b34d-f648c0374b62 | -7.93967 | -39.8506 | 2025-10-19 04:10:00 | NPP-375D | BODOCÓ | PERNAMBUCO | Brasil | 2602001 | 26 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 2fe3d9d4-1195-346a-80c8-86be55b6b025 | -6.53371 | -47.57405 | 2025-10-19 04:10:00 | NPP-375D | PALMEIRAS DO TOCANTINS | TOCANTINS | Brasil | 1713809 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b5e4eaf4-0814-3728-8489-4f78594670fe | -3.08648 | -49.22041 | 2025-10-19 04:10:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 65b81510-c929-3e06-a53c-90cedd2df891 | -5.71257 | -43.82564 | 2025-10-19 04:10:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| ff7b1217-469b-3fa6-9a22-822c9015d69c | -5.30931 | -44.79431 | 2025-10-19 04:10:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9fad208b-dd80-3846-a0a9-3fd62738032a | -4.30526 | -48.06933 | 2025-10-19 04:10:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| bfe52a8b-880c-32da-8a2d-c26568e71511 | -5.46648 | -44.8902 | 2025-10-19 04:10:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 352958e5-f0be-3f2e-9b4a-2750662ced8b | -4.31211 | -43.02101 | 2025-10-19 04:10:00 | NPP-375D | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| f2ab4d7f-e35c-396e-ab40-2f1b1b214f17 | -3.51991 | -49.9367 | 2025-10-19 04:10:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 1a7a3a85-fa15-37fd-a354-a0630d5170bb | -7.62978 | -42.80251 | 2025-10-19 04:10:00 | NPP-375D | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| d659ad90-4c04-3716-9b6f-82cffa486cf3 | -7.18435 | -42.17966 | 2025-10-19 04:10:00 | NPP-375D | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 3d98e332-1b90-3e5d-9bff-ebbc8148c5fc | -4.92126 | -45.98635 | 2025-10-19 04:10:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 27d7f261-04d0-30c8-a9cf-1bb40992e74b | -7.16104 | -42.36948 | 2025-10-19 04:10:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 58c05377-2d06-382f-bd20-49a26d1b7db1 | -3.45456 | -50.09716 | 2025-10-19 04:10:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 80e76fa2-1933-3be1-846c-d7d37e7dfa94 | -5.57811 | -41.32027 | 2025-10-19 04:10:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 5aa48ae5-5c3d-35a4-bec0-9e8e248639ee | -4.31728 | -38.36724 | 2025-10-19 04:10:00 | NPP-375D | CASCAVEL | CEARÁ | Brasil | 2303501 | 23 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 74421263-d5ef-3f1b-8925-d3bd30f1e82b | -5.87659 | -48.17764 | 2025-10-19 04:10:00 | NPP-375D | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f08729dc-7bb2-3148-a11b-d119c6257909 | -5.6034 | -42.67713 | 2025-10-19 04:10:00 | NPP-375D | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| d2171e40-d972-34bf-8388-ec66fa582978 | -5.99361 | -42.79379 | 2025-10-19 04:10:00 | NPP-375D | ANGICAL DO PIAUÍ | PIAUÍ | Brasil | 2200608 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| aeb9c4c1-004b-3ac4-9274-001b646274ac | -6.31487 | -44.31341 | 2025-10-19 04:10:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 8167adcb-5908-3f11-99c3-b22a1ba7d084 | -2.69019 | -49.54221 | 2025-10-19 04:10:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 87e3da18-809d-3e6b-b701-9708b27510d6 | -4.22065 | -48.36271 | 2025-10-19 04:10:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9de11b70-171c-35b9-9652-0fdb175bb884 | -5.59761 | -50.05891 | 2025-10-19 04:10:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 8aee2b36-158d-3aba-b3a5-b96faf391b58 | -7.33764 | -43.86308 | 2025-10-19 04:10:00 | NPP-375D | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e356fe22-ae46-3a70-a6f2-37111263835a | -2.6949 | -49.5463 | 2025-10-19 04:10:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| f7d661e6-5a55-3c7b-abe4-a2d387581bfa | -5.36683 | -44.94138 | 2025-10-19 04:10:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c8d1d144-295a-3ffb-a532-6c9d80b0ac5a | -5.54492 | -41.33635 | 2025-10-19 04:10:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 1db13d08-4101-35b6-84cc-12e583144ec0 | -5.36549 | -45.27733 | 2025-10-19 04:10:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| d834071b-c299-3e87-8234-55bd4508926b | -4.44303 | -43.22091 | 2025-10-19 04:10:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e46b6b97-58cc-3e25-bbf2-514d65c9b492 | -7.08453 | -46.87347 | 2025-10-19 04:10:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d79b370c-cf12-3638-9262-419df7546489 | -5.59433 | -42.7124 | 2025-10-19 04:10:00 | NPP-375D | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| ee899637-eb69-31a3-bca1-5ba30ce7c3f8 | -5.92387 | -45.44986 | 2025-10-19 04:10:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 11d80072-28c6-317f-9aa2-46648b4cd377 | -2.44563 | -49.36593 | 2025-10-19 04:10:00 | NPP-375D | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ddcee1e4-a8bb-3f56-aced-ea19bd150db7 | -6.86767 | -47.9966 | 2025-10-19 04:10:00 | NPP-375D | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8dd4ec6f-62d1-3946-8249-7d5b78b58fc3 | -5.89274 | -46.69685 | 2025-10-19 04:10:00 | NPP-375D | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 5ff9d0e2-5ed3-341e-af3a-b7eb17fc66f0 | -4.7624 | -50.6994 | 2025-10-19 04:10:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 61eb2984-88e4-3e5c-ab9c-5ee568c1aae8 | -5.43454 | -47.69231 | 2025-10-19 04:10:00 | NPP-375D | SÃO MIGUEL DO TOCANTINS | TOCANTINS | Brasil | 1720200 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f62eab5b-279a-3c3c-9a7b-a07aa5584d46 | -4.48772 | -43.65691 | 2025-10-19 04:10:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2c01d97a-15a4-36cb-99e6-8a312a180b99 | -5.2171 | -43.74495 | 2025-10-19 04:10:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d4de4d3a-f32f-3c25-b5a7-6dce50f193c6 | -3.14175 | -50.24669 | 2025-10-19 04:10:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b8c49958-7681-390d-9bf6-dc47be040d86 | -4.83351 | -43.01481 | 2025-10-19 04:10:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 488aaa45-2901-3abb-a59d-f61918a9e8ae | -4.58753 | -45.38235 | 2025-10-19 04:10:00 | NPP-375D | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ad42d4d6-4c44-3521-a836-68c24d028bea | -5.4604 | -44.89156 | 2025-10-19 04:10:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 53b83250-33ed-33a6-9af3-bdcb8dab5074 | -5.34122 | -42.55174 | 2025-10-19 04:10:00 | NPP-375D | BENEDITINOS | PIAUÍ | Brasil | 2201606 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| d5d73238-a5db-3e15-be69-e38a2556f085 | -6.10722 | -44.8472 | 2025-10-19 04:10:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| f2c80aef-ee74-38b6-aafb-a862b76f3078 | -5.78126 | -42.72383 | 2025-10-19 04:10:00 | NPP-375D | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |


[Clique aqui para ver as próximas entradas](README23.md)
