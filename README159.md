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

## Dados Diários - Página 159

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b13e2cd0-1db2-3776-893e-6feab0f8afd8 | -8.98277 | -44.15348 | 2026-09-28 17:09:00 | NOAA-21 | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 24.8 |
| 792aca6e-0083-3cb3-9678-e4bbcb7e61a6 | -7.49115 | -45.96005 | 2026-09-28 17:09:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 09869fb1-959d-3365-ba92-60075e2357dd | -8.62938 | -54.672 | 2026-09-28 17:09:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| a6ff0aac-2cb9-36c4-8a5c-a5a984f4603b | -8.65315 | -45.34564 | 2026-09-28 17:09:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 55ad702d-ee48-3e59-8e1f-6dbecf2ba6ce | -7.43931 | -55.6277 | 2026-09-28 17:09:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 134.0 |
| f363b062-18da-3bc5-892f-335aa14a1727 | -9.85415 | -44.9434 | 2026-09-28 17:09:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 28.4 |
| 25749975-897c-3695-9165-632e4f675c2d | -7.71315 | -44.90333 | 2026-09-28 17:09:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 59aa0324-b96e-37e1-9b20-9b537e0bdfc3 | -7.68443 | -44.8848 | 2026-09-28 17:09:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 16.0 |
| 81574e2a-1a5b-3057-82b1-5c26c3177f2f | -8.02538 | -42.85266 | 2026-09-28 17:09:00 | NOAA-21 | PAJEÚ DO PIAUÍ | PIAUÍ | Brasil | 2207355 | 22 | 33 | nan | nan | nan | Caatinga | 11.5 |
| be73192d-07bb-3dba-aa6f-8ad066ff21d1 | -11.04861 | -47.66717 | 2026-09-28 17:09:00 | NOAA-21 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 15.3 |
| 64705aa1-4f4a-3f00-b7b7-ab56228bd8a9 | -9.32887 | -45.36182 | 2026-09-28 17:09:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 99.3 |
| 368575ab-e29c-3461-a156-8ab73b392d28 | -12.08141 | -48.55062 | 2026-09-28 17:09:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 57.2 |
| 6719f77e-53b7-37fb-b68f-6d20adc76cbd | -7.59606 | -55.6996 | 2026-09-28 17:09:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 69fda3dc-3a7a-3879-9a61-61c6b3df214f | -12.84761 | -54.03101 | 2026-09-28 17:09:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 8fa5b9e7-93fc-31ea-bdf9-35c9b1b6008e | -12.85071 | -54.02605 | 2026-09-28 17:09:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 32.0 |
| 4b01d336-298d-3dbd-81f8-03b0c22c03e7 | -8.18954 | -54.79565 | 2026-09-28 17:09:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 1e874fab-0c6b-354d-b033-c57f3b9e81da | -6.3399 | -55.32743 | 2026-09-28 17:09:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| d8517cff-2d23-3192-b9ad-b7b9e2510781 | -9.73087 | -53.87777 | 2026-09-28 17:09:00 | NOAA-21 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 00b363e3-3e10-30f3-9edc-07bf76399369 | -10.89564 | -53.93368 | 2026-09-28 17:09:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| fd319752-ae80-361a-b735-bd13550ab41f | -6.16031 | -52.8226 | 2026-09-28 17:09:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| e0e77c0a-6741-374e-928c-036a3d4f09b6 | -12.15813 | -50.39865 | 2026-09-28 17:09:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 215253e7-c543-3067-8cff-9dd9388e35a7 | -10.08132 | -50.38506 | 2026-09-28 17:09:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| fc336d11-8748-386f-b60f-7c63ca08e043 | -12.16259 | -50.41336 | 2026-09-28 17:09:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 20.7 |
| 31d08fac-1ec0-3108-9b9d-bde487ca9a3e | -8.93102 | -61.4916 | 2026-09-28 17:09:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 16.5 |
| db140a1e-a92f-3488-9608-88070ece8b01 | -6.13495 | -53.05556 | 2026-09-28 17:09:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 062e9e8c-2dae-3430-ad96-d3e5ff4756b0 | -10.82594 | -60.7267 | 2026-09-28 17:09:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 10.6 |
| b4674dcf-47cc-3f04-908c-954a981320fc | -9.2592 | -47.36506 | 2026-09-28 17:09:00 | NOAA-21 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 14.8 |
| 29ccbd99-dbb2-3ecd-9de7-9a84e70b0bc1 | -9.77612 | -44.82751 | 2026-09-28 17:09:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 944dedae-fc55-302a-9770-6dc27eff7dc2 | -11.21699 | -44.80079 | 2026-09-28 17:09:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 9.5 |
| f42e22b5-bdbf-3a47-80f0-89e1f24c186d | -7.82585 | -55.13021 | 2026-09-28 17:09:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 25.8 |
| c2eba666-0b83-3068-a2e9-b615e0e1ba78 | -11.06722 | -60.68756 | 2026-09-28 17:09:00 | NOAA-21 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 53.6 |
| 7ca6ec4c-16f5-392f-a265-67b56bda3fa1 | -9.5759 | -45.49615 | 2026-09-28 17:09:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 11.3 |
| d23be18a-c170-3ecf-9301-bc0a75eb7d9f | -9.52162 | -46.37899 | 2026-09-28 17:09:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 333f852b-32ea-3abf-97de-669e3c07e715 | -10.81607 | -42.75028 | 2026-09-28 17:09:00 | NOAA-21 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 9.9 |
| 9f8493f2-ac9b-37d5-acdf-85069670e2eb | -8.97643 | -44.15731 | 2026-09-28 17:09:00 | NOAA-21 | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 20.9 |
| ac256210-35ca-36bd-ba2d-90ebdba4ca62 | -10.93909 | -43.90782 | 2026-09-28 17:09:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 25.4 |
| b883b175-db7a-3703-889d-3c33ffced2ed | -9.82529 | -44.9407 | 2026-09-28 17:09:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 52721bac-4ba7-3ce7-af8d-b38cda387f66 | -6.03488 | -49.57041 | 2026-09-28 17:09:00 | NOAA-21 | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 838c6ee7-4b2e-3c42-8c79-990325fcdf30 | -8.5827 | -44.85551 | 2026-09-28 17:09:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 95e37071-c655-3758-beec-2f77fcab3629 | -9.46148 | -45.96298 | 2026-09-28 17:09:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 2b8898b9-6f06-3914-bcfa-ebb2ec302bb7 | -6.15252 | -51.56805 | 2026-09-28 17:09:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 6b87532d-968a-3c6a-8563-55cfe71f28a7 | -3.92845 | -43.12587 | 2026-09-28 17:09:00 | NOAA-21 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 9.5 |
| b160b955-961e-3d5e-bb2b-0320fb758765 | -8.91017 | -50.63395 | 2026-09-28 17:09:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 7ee55e3f-235d-317f-8e9f-4419bc7529e4 | -10.82046 | -60.71888 | 2026-09-28 17:09:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 28.3 |
| d1a7329e-fa34-34a9-b295-b06fbbcce787 | -12.15886 | -50.40316 | 2026-09-28 17:09:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 7.6 |
| bec5944b-8c58-3ee2-9a3c-9576f7cdf1bf | -10.54458 | -57.43418 | 2026-09-28 17:09:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2f35fc41-2e24-3baa-ac49-e8e1f1376be1 | -10.10642 | -43.94621 | 2026-09-28 17:09:00 | NOAA-21 | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 14.5 |
| 2614c181-0601-310e-a0b9-96e43ef63696 | -6.15341 | -52.89259 | 2026-09-28 17:09:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 15.2 |
| 322cb60d-a252-3d5a-9730-30d3071a1e56 | -9.14807 | -49.97154 | 2026-09-28 17:09:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 14.3 |
| 2ed9a075-06bb-3905-b800-4f6ad7ff5029 | -6.15467 | -52.90047 | 2026-09-28 17:09:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 12.4 |
| e18f1bac-b3c4-3796-a365-51b0ec880ad1 | -6.87764 | -55.55746 | 2026-09-28 17:09:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 3c4b7951-aa2d-3a5e-b4be-2368e5287f99 | -12.3882 | -50.23291 | 2026-09-28 17:09:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 22.2 |
| c3efe74c-98f1-3c3f-87ae-317c7e07c970 | -7.3755 | -64.35063 | 2026-09-28 17:09:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 09a666ca-f7a0-3d10-9a17-d5ced055a15f | -10.20218 | -49.99195 | 2026-09-28 17:09:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 20.5 |
| b8bb1ec8-cc89-3b71-b9d7-06e4a8faf18f | -5.90564 | -53.58736 | 2026-09-28 17:09:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 8850f970-5cff-3389-bda7-b3cc23279631 | -8.98144 | -44.1518 | 2026-09-28 17:09:00 | NOAA-21 | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 18.7 |
| 0072ee01-a42c-32fa-bec1-cee4f364032c | -8.27743 | -54.72871 | 2026-09-28 17:09:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| f0a9e33c-5856-3c64-a231-ea8ac2c7f76b | -12.7691 | -52.81509 | 2026-09-28 17:09:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 6c90acbd-475d-3ee8-a9ad-1e22c0088855 | -9.51055 | -46.37516 | 2026-09-28 17:09:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 350af01f-9f1f-3620-b0d8-ec4cc6276bbe | -10.51934 | -57.43278 | 2026-09-28 17:09:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 171.9 |
| 0963d70d-ce69-3605-b1e0-fdc9dece7d73 | -8.37246 | -45.48513 | 2026-09-28 17:09:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 14.5 |
| 8c22fb96-5d6c-36de-9785-4699b93f7e17 | -6.72298 | -55.07542 | 2026-09-28 17:09:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 2ed3fb4a-84d4-304f-87e7-883291d1fece | -9.50827 | -46.35905 | 2026-09-28 17:09:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 23.7 |
| e82905a4-f87d-36ef-9df3-636fbefa68e5 | -10.08897 | -50.38376 | 2026-09-28 17:09:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 3ac52871-443b-3176-86ee-cf4a544d30a2 | -6.14998 | -53.12888 | 2026-09-28 17:09:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 12.3 |
| c77f4289-ce48-36f5-99a2-bcd395c03533 | -4.83545 | -48.36228 | 2026-09-28 17:09:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 044521eb-7e1c-3cb5-8414-a4288202cdcd | -6.06704 | -57.80727 | 2026-09-28 17:09:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 13.8 |
| 9e8a4414-a175-3329-ba6d-624782afdfa3 | -9.51194 | -46.06549 | 2026-09-28 17:09:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 9.3 |
| b1f33231-f476-32be-acb8-77ec2d6888cf | -11.53782 | -47.39075 | 2026-09-28 17:09:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 19.6 |
| d2752e84-ab1b-3562-91ec-328b7bb39c97 | -6.52421 | -55.3799 | 2026-09-28 17:09:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 90a2b3e5-8d8f-3ef3-9808-c782d6638715 | -10.81795 | -41.3289 | 2026-09-28 17:09:00 | NOAA-21 | OUROLÂNDIA | BAHIA | Brasil | 2923357 | 29 | 33 | nan | nan | nan | Caatinga | 22.5 |
| a3501bb4-e5d6-398f-8aca-ab613ea442e8 | -12.06828 | -48.54902 | 2026-09-28 17:09:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 163.2 |
| 0460ad02-3b23-31d4-a324-1b6b00cf4635 | -10.38965 | -46.53067 | 2026-09-28 17:09:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 49ab00ec-f2ac-3563-b520-b01743e61d1a | -10.02013 | -52.09892 | 2026-09-28 17:09:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 7c2a685e-7607-3780-987e-dc1a3a4d7ad8 | -7.70369 | -44.92666 | 2026-09-28 17:09:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 9.0 |
| b3a48761-45ea-3f6e-8255-a916481ee8ff | -7.23099 | -44.85929 | 2026-09-28 17:09:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 14.0 |
| 3d0f7f0d-36f3-3704-a269-d22c1d076cc8 | -11.86669 | -50.88833 | 2026-09-28 17:09:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 116ea9ae-e363-333a-9c1e-ea417d726fc1 | -7.38265 | -60.5905 | 2026-09-28 17:09:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 685ac017-e850-3364-a68d-ddef4b9d5208 | -7.12928 | -47.60868 | 2026-09-28 17:09:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 30.6 |
| 4d167e90-1268-39b5-94dc-7f77612268a9 | -8.97618 | -44.15055 | 2026-09-28 17:09:00 | NOAA-21 | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 15.5 |
| c9e439cb-e4e5-35af-a6a8-d85ddf4e629e | -7.84542 | -46.93223 | 2026-09-28 17:09:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 18.5 |
| ec598d28-c8ad-385d-84ba-d873d3e7e322 | -7.26793 | -46.93036 | 2026-09-28 17:09:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 51722d46-2917-3fde-85df-a6e5c9d38275 | -11.06905 | -48.88714 | 2026-09-28 17:09:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 15.8 |
| 6dc5a3c4-c878-3549-835d-5e177a8794b6 | -11.30788 | -58.33627 | 2026-09-28 17:09:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 9.5 |
| c39fb61c-0443-32ee-b1f7-570c895ea0a5 | -10.7015 | -48.74929 | 2026-09-28 17:09:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 6543f82f-5da5-36a2-bde6-832f2d3bd327 | -7.17297 | -44.80363 | 2026-09-28 17:09:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| b4239137-21cc-3217-a220-e4bcfaaf7a45 | -10.20162 | -50.01266 | 2026-09-28 17:09:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 36.6 |
| c90b6a6f-b89d-3d65-afc3-b65b09c8c597 | -11.20302 | -47.71602 | 2026-09-28 17:09:00 | NOAA-21 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 19230532-0f26-3622-8e67-a9568b31fe02 | -7.89802 | -45.44432 | 2026-09-28 17:09:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 691fa4ce-b059-3396-a003-7ace81692989 | -7.27807 | -45.33874 | 2026-09-28 17:09:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 10.6 |
| f3387986-9873-3a82-a24a-aff70ccd4f1f | -12.60826 | -51.94896 | 2026-09-28 17:09:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 19.8 |
| 83261b7c-fafb-3300-b28e-2055a9c42c22 | -7.68778 | -54.76212 | 2026-09-28 17:09:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 14.5 |
| 9413ebc7-3587-3ea9-91a6-572055fc3385 | -9.14353 | -49.96875 | 2026-09-28 17:09:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 7b43f726-1fe6-3f03-8f3a-675d6622d51a | -7.67306 | -44.88716 | 2026-09-28 17:09:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 43.6 |
| d3fbdb3c-e478-3854-8bee-4d676580eb94 | -10.82564 | -57.22565 | 2026-09-28 17:09:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 8.0 |
| d0e6a60d-dcea-399a-9944-c392b85368d3 | -11.52794 | -47.38784 | 2026-09-28 17:09:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 236.4 |
| 54b7949b-4c90-3cf9-80e0-988c84a40427 | -10.26664 | -44.61879 | 2026-09-28 17:09:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 20.0 |
| 9361e58f-415c-306d-b76a-48b563b45667 | -7.27716 | -44.31437 | 2026-09-28 17:09:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 1802f9c7-00bf-3067-966d-e3c62f696c88 | -6.74397 | -50.92729 | 2026-09-28 17:09:00 | NOAA-21 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| d9ce0554-843d-371f-9869-8a362905bd7a | -8.67036 | -45.37909 | 2026-09-28 17:09:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 25.2 |


[Clique aqui para ver as próximas entradas](README160.md)
