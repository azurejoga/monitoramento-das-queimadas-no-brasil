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

## Dados Diários - Página 17

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 79a27d36-9e40-3c0d-b013-2c25d99a62f3 | -12.57029 | -44.64963 | 2025-09-11 03:55:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 132d533c-91aa-3dbb-900a-76c7e5f05331 | -6.53756 | -44.78248 | 2025-09-11 03:55:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a3f1ae5f-4250-36a6-b6cf-4af998f3befc | -6.7326 | -43.39568 | 2025-09-11 03:55:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 1de6c0a9-ab3b-36d5-8c8c-cc7f7be4fc21 | -11.25406 | -41.90408 | 2025-09-11 03:55:00 | NOAA-21 | IRECÊ | BAHIA | Brasil | 2914604 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| ce960c8d-3647-3ac0-8162-bbb785d95001 | -5.57561 | -47.60117 | 2025-09-11 03:55:00 | NOAA-21 | SÍTIO NOVO DO TOCANTINS | TOCANTINS | Brasil | 1720804 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5d8ec647-9787-3739-8e77-e524adfda308 | -11.80925 | -46.7592 | 2025-09-11 03:55:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1b98f65c-46b6-37e2-951e-ef01bfc26a0f | -12.1318 | -44.84958 | 2025-09-11 03:55:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2ea8a7f3-fce3-3284-8991-1eb3dd0c3f39 | -13.25493 | -43.78831 | 2025-09-11 03:55:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 49947986-60e0-3ae5-96a5-740281fc6368 | -6.25743 | -44.85761 | 2025-09-11 03:55:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 28fb680f-f50f-3b16-a5c0-7ad34da487dd | -7.46522 | -45.28025 | 2025-09-11 03:55:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e855c80a-b2ad-3bee-a84e-4d5fc66efd48 | -11.64806 | -46.91696 | 2025-09-11 03:55:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 18468821-6d65-3a63-a8be-dc62f75715aa | -6.40334 | -42.61229 | 2025-09-11 03:55:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 5.7 |
| c92cf96d-d0b1-3c6f-b692-d65549295136 | -7.07778 | -43.88379 | 2025-09-11 03:55:00 | NOAA-21 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| c7020256-35e4-3d5c-b7c2-c9ab146d2eaf | -11.4641 | -43.60241 | 2025-09-11 03:55:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 6.0 |
| b28a75ff-7d6b-3a58-a389-dd1c6c1f2404 | -12.13918 | -44.8545 | 2025-09-11 03:55:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bd486028-a8f8-308e-ad75-f270d79ed2bf | -13.1591 | -40.68464 | 2025-09-11 03:55:00 | NOAA-21 | MARCIONÍLIO SOUZA | BAHIA | Brasil | 2920809 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 665c2b93-490e-39de-bf92-64671197df8e | -10.26766 | -48.82156 | 2025-09-11 03:55:00 | NOAA-21 | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| a3d7fca9-67e9-37db-80fd-30345259e484 | -9.75385 | -47.85719 | 2025-09-11 03:55:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 15ed63ac-dc97-33f7-abc7-536a9ae38ff9 | -11.72941 | -50.63749 | 2025-09-11 03:55:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 18.2 |
| 2492c43e-1672-3bed-a75b-7c473f84cc65 | -11.42103 | -43.55407 | 2025-09-11 03:55:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 9.6 |
| a31f7fce-e9a4-3057-acbb-882ca50181b8 | -8.01787 | -44.49947 | 2025-09-11 03:55:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 8cb075dc-52c1-3e58-8967-83bdbfd3673b | -7.99389 | -45.79632 | 2025-09-11 03:55:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 446e696c-43e2-3ebe-940a-45d7b6021291 | -5.74753 | -51.69585 | 2025-09-11 03:55:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 0a35e2b0-2153-30b3-bf35-61eef0da121d | -7.33242 | -49.6045 | 2025-09-11 03:55:00 | NOAA-21 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 2cc4ab8d-fcb9-3686-8882-3d2f4d603a65 | -9.94079 | -46.05884 | 2025-09-11 03:55:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| cc9462fe-66f3-3b3a-aa73-b924429a5784 | -12.02781 | -47.53743 | 2025-09-11 03:55:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 039b926d-b31a-3072-8f43-21367f862012 | -6.41447 | -44.49214 | 2025-09-11 03:55:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ddb40d58-c0d0-3a95-9edb-c32dcf09dd59 | -13.15366 | -45.28118 | 2025-09-11 03:55:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ba16071c-ccf1-3bd2-9f85-a3add24d4ddc | -5.9469 | -45.72127 | 2025-09-11 03:55:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| cbd88598-63d0-3fed-bf5f-912bfc525032 | -8.42521 | -47.27055 | 2025-09-11 03:55:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 32cd319b-3c7a-319b-bdf4-41aedb28c32f | -11.77612 | -46.51945 | 2025-09-11 03:55:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 7.2 |
| fa68c2b8-76a9-3b28-bfa6-83b84f10e3c8 | -12.014 | -47.58408 | 2025-09-11 03:55:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 199740b1-3c57-3b3a-ad69-82edc5b8161a | -11.64443 | -46.91071 | 2025-09-11 03:55:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 884eac4c-72cc-32a6-9d68-ef67f34a83ab | -7.16435 | -44.14125 | 2025-09-11 03:55:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 5.8 |
| d9b1d5d1-14fd-3224-8456-32f1b41664ff | -8.0258 | -48.65345 | 2025-09-11 03:55:00 | NOAA-21 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 4a0908dd-fef9-3276-973f-a1ca134fac8c | -9.72594 | -48.09742 | 2025-09-11 03:55:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 888e893a-58a2-3440-885b-487d30140230 | -9.09564 | -45.69565 | 2025-09-11 03:55:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c6937ce1-133d-3c9b-8345-fca5ab131aa3 | -12.47755 | -47.48767 | 2025-09-11 03:55:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 15.3 |
| 33513ba4-0015-3c53-bf25-880bc45a0a9c | -11.71312 | -41.73929 | 2025-09-11 03:55:00 | NOAA-21 | CANARANA | BAHIA | Brasil | 2906204 | 29 | 33 | nan | nan | nan | Caatinga | 5.6 |
| 66cc0894-6b21-3e28-8798-1dee735193a7 | -5.59433 | -48.1131 | 2025-09-11 03:55:00 | NOAA-21 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f4d9585d-8e8e-3a40-b0cb-8a06aa3f2f6e | -7.99361 | -45.79391 | 2025-09-11 03:55:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1e05fe09-f476-3fdf-a86f-30bc25f984a0 | -6.18048 | -43.49681 | 2025-09-11 03:55:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| f1e60c66-75c0-3708-96a1-e3b9d08d4949 | -11.34547 | -46.48081 | 2025-09-11 03:55:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 11ace230-cb09-3060-ba0c-1f697bbe2739 | -5.59986 | -48.11417 | 2025-09-11 03:55:00 | NOAA-21 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 533ef7e5-933d-3b93-aafe-51b2f939f15a | -6.81743 | -44.88857 | 2025-09-11 03:55:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 578e4e25-9d4b-33ad-a580-42315a8a76fa | -11.45582 | -43.60571 | 2025-09-11 03:55:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 17.7 |
| 869aec5c-c7f4-3a4e-aefa-89536e835318 | -9.09864 | -46.95813 | 2025-09-11 03:55:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 15caeed3-c045-300f-9052-3be8a0f744ed | -6.74813 | -45.93709 | 2025-09-11 03:55:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 08b047f8-5b3a-3820-82b9-f0d84587944a | -7.22799 | -43.98372 | 2025-09-11 03:55:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f16e2a6b-705d-3cba-ab73-fddbd91a1f2e | -11.02726 | -45.05947 | 2025-09-11 03:55:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 17.7 |
| 7fbba644-ebac-3eaf-923b-a0a4c52a126f | -6.80613 | -43.43536 | 2025-09-11 03:55:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 2.6 |
| ce8a07e5-623e-3721-a52e-e3e66012cc96 | -6.6956 | -44.94107 | 2025-09-11 03:55:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 332c2715-cfbc-3542-8699-4cc5123512ad | -6.66482 | -44.12086 | 2025-09-11 03:55:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0134a067-0ede-3a2a-a345-7a369d75d35f | -12.42695 | -47.8064 | 2025-09-11 03:55:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 66559a50-2cf9-3e58-99f0-54467be60f98 | -11.3942 | -43.53071 | 2025-09-11 03:55:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 41f9e616-0f46-33a2-b564-0ed90980caa7 | -9.67845 | -47.53475 | 2025-09-11 03:55:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 978b26a0-36f3-3cd8-9e9a-7aac243ecdf2 | -8.03525 | -44.49838 | 2025-09-11 03:55:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2eb5cba7-4c3a-3dc5-9635-49ad70634f2e | -5.5445 | -45.52467 | 2025-09-11 03:55:00 | NOAA-21 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| dee19994-a3d5-365d-933a-bf2560bd450d | -8.48363 | -47.29021 | 2025-09-11 03:55:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| bced6ae2-1a38-35df-9bf3-995b58293698 | -11.37618 | -45.57825 | 2025-09-11 03:55:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 2d70cb9c-1815-3f2e-aa99-22504b35cc44 | -9.06648 | -47.07164 | 2025-09-11 03:55:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 67228811-a060-34c0-9282-7613a7561346 | -12.42769 | -47.80912 | 2025-09-11 03:55:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| d91b083b-f71e-32ba-aee9-cff968ce9cd2 | -12.42999 | -47.79037 | 2025-09-11 03:55:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| f889b18c-278e-3b48-9204-0ff0def46ff7 | -10.38092 | -50.52473 | 2025-09-11 03:55:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d7832390-aade-384f-be80-d9a3f6e863d8 | -7.2661 | -44.90895 | 2025-09-11 03:55:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e5f7c1e5-5d72-3983-8697-5e9068ca9fe8 | -11.72601 | -50.65479 | 2025-09-11 03:55:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 5d4f618c-f9f5-3506-bf7e-2505d1a2b004 | -6.21506 | -43.49558 | 2025-09-11 03:55:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 7a273d9c-3db9-3f4a-a323-78267df8d513 | -8.73338 | -47.10177 | 2025-09-11 03:55:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 3b8f727d-ed08-3de4-9f5f-d573d376f981 | -8.03983 | -48.67068 | 2025-09-11 03:55:00 | NOAA-21 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 2fc7974d-d325-3e12-be1d-200eeba12206 | -8.44129 | -49.11635 | 2025-09-11 03:55:00 | NOAA-21 | COUTO MAGALHÃES | TOCANTINS | Brasil | 1706001 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 57d5517a-9929-34b4-af3b-9ed3465b560d | -9.06337 | -47.04484 | 2025-09-11 03:55:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 36565a6d-1cab-3dbb-b872-c8a174f291ba | -11.48028 | -43.64339 | 2025-09-11 03:55:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 34.5 |
| 2a5f69d7-4815-34d8-afaf-424f24d5cb65 | -12.42414 | -47.79485 | 2025-09-11 03:55:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 8e2699e3-743b-32e4-b545-89c9852b14bb | -6.02085 | -45.89724 | 2025-09-11 03:55:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6b3c7ab5-17f3-3612-b837-15b3bcb12851 | -6.56312 | -42.93703 | 2025-09-11 03:55:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6d2aa705-d971-32ea-b357-45a7cf540692 | -6.39447 | -44.0443 | 2025-09-11 03:55:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 558637e6-7256-330d-975e-32beaf8fce14 | -7.91717 | -38.70924 | 2025-09-11 03:55:00 | NOAA-21 | SÃO JOSÉ DO BELMONTE | PERNAMBUCO | Brasil | 2613503 | 26 | 33 | nan | nan | nan | Caatinga | 0.7 |
| ee6ff721-0a2c-3dc6-a53e-2f2e821373cc | -11.47396 | -43.68053 | 2025-09-11 03:55:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c0b7f759-f8b0-3919-9be8-e57d3368a358 | -8.87021 | -49.55436 | 2025-09-11 03:55:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 86fd066e-7a3f-3870-bef4-f56b1e237580 | -12.13519 | -44.85375 | 2025-09-11 03:55:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a10c2811-83f2-3ae4-a013-7d3f08e39b55 | -11.48699 | -43.64938 | 2025-09-11 03:55:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 958a3b86-e951-364e-8427-fb76ceece3da | -9.45892 | -46.42895 | 2025-09-11 03:55:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 7d9ad597-4cdc-3a55-8745-c67bc0524835 | -10.31049 | -48.80059 | 2025-09-11 03:55:00 | NOAA-21 | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 25b83e85-0b4b-37f8-950b-09f76cad4799 | -11.70368 | -48.26066 | 2025-09-11 03:55:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0c84fbdc-1275-35a0-bf85-8d2b79fc284a | -11.39674 | -45.58574 | 2025-09-11 03:55:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| d3fa8f7c-8241-3292-b2d5-ff56b2168da7 | -6.82658 | -45.61358 | 2025-09-11 03:55:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b4c38880-f7ea-3f2e-a6f7-570784073eb0 | -11.48342 | -43.62486 | 2025-09-11 03:55:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 1cc4b09f-8573-3577-8c4c-641ff1f0c3d1 | -9.71242 | -43.53651 | 2025-09-11 03:55:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4e088ee5-0586-3b31-9da1-03d27411f0ed | -7.38806 | -50.88506 | 2025-09-11 03:55:00 | NOAA-21 | BANNACH | PARÁ | Brasil | 1501253 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| bf1b768c-b268-35e8-890d-649f4d1ccd33 | -7.38853 | -47.36462 | 2025-09-11 03:55:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| bdb4ab85-3409-3bcf-91ac-d5cbdc502a1f | -9.03363 | -49.76886 | 2025-09-11 03:55:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 67fdb359-099d-3f6a-880a-de4eed7796de | -6.18892 | -45.65503 | 2025-09-11 03:55:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 30d138ae-dc8c-332c-a447-6f199a0a1874 | -9.3043 | -46.7692 | 2025-09-11 03:55:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 520bbc50-89cd-361b-9d15-5bb4dfa095fa | -8.20157 | -50.10786 | 2025-09-11 03:55:00 | NOAA-21 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 13.4 |
| f72d4828-6444-39a1-b179-c742136daee7 | -9.68342 | -43.52913 | 2025-09-11 03:55:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 41bddab7-9a86-3d3e-bcef-df06a769e5b3 | -12.61644 | -44.66303 | 2025-09-11 03:55:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| dcc2a759-eb00-313e-b8d1-119eb606de3d | -6.97262 | -44.80622 | 2025-09-11 03:55:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7faa9516-7c1e-3887-b35c-e0ec84b1815e | -9.02118 | -49.77089 | 2025-09-11 03:55:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| de46e805-8ab6-3e0e-8e2f-5bc354c4e2fc | -5.73198 | -45.28701 | 2025-09-11 03:55:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 76683725-8283-36b4-9c93-3c97223bf072 | -11.7692 | -46.48045 | 2025-09-11 03:55:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |


[Clique aqui para ver as próximas entradas](README18.md)
