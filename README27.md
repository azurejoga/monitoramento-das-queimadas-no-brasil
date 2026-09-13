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

## Dados Diários - Página 27

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7af266e6-099e-3eca-8f8f-5882b819b7ac | -13.29421 | -43.67551 | 2026-09-13 04:17:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5d845af8-010e-3cd0-9ab6-4b1130df639b | -10.31099 | -45.29723 | 2026-09-13 04:17:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a4649c88-6659-3046-8477-fd38cc45f937 | -15.2386 | -42.78407 | 2026-09-13 04:17:00 | NOAA-21 | SANTO ANTÔNIO DO RETIRO | MINAS GERAIS | Brasil | 3160454 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d7a0ccc1-ff3e-3c49-ba0a-3fee6b23572d | -8.05846 | -54.85361 | 2026-09-13 04:17:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 330d497f-9158-3e5b-b45b-260c9a99d16d | -11.93844 | -49.755 | 2026-09-13 04:17:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 20976ef6-ca37-3bc2-b81f-d5068040c24f | -13.44973 | -48.50097 | 2026-09-13 04:17:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 371bd187-e235-3a4a-82bc-40506f25cd2c | -10.30993 | -45.28232 | 2026-09-13 04:17:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1e5a723d-34fe-3a50-b7ed-f9ec8132e3b7 | -9.78884 | -43.44195 | 2026-09-13 04:17:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ee03b10d-006f-374c-b481-5de4ae01a2fc | -13.7538 | -42.59915 | 2026-09-13 04:17:00 | NOAA-21 | CAETITÉ | BAHIA | Brasil | 2905206 | 29 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 94e38a4a-5246-3100-9d39-5462023877af | -10.62577 | -45.2206 | 2026-09-13 04:17:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a0770de3-0240-3e3d-ae15-1260934059fc | -10.45908 | -48.65173 | 2026-09-13 04:17:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| c5e6c198-827e-34d8-a234-9be1fdfe9ea9 | -11.18512 | -42.79491 | 2026-09-13 04:17:00 | NOAA-21 | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 6.9 |
| 81b8b2d5-713f-3f1a-bdb6-8a7b693600b2 | -9.43266 | -47.86982 | 2026-09-13 04:17:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 7.7 |
| a1f63179-036d-316e-9266-13a7183b5ada | -10.45988 | -48.64706 | 2026-09-13 04:17:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 6021be70-de72-3cb4-8284-96deb7fd0d09 | -13.60584 | -47.88095 | 2026-09-13 04:17:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c659d549-5227-3e37-9840-5b1ab1c62fe4 | -11.18795 | -42.79911 | 2026-09-13 04:17:00 | NOAA-21 | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 5.4 |
| f73ce419-cdbf-3541-bf4d-d6d768302bb5 | -9.70421 | -43.39583 | 2026-09-13 04:17:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 04273761-2fa1-3301-a8a9-cd9af28081b6 | -10.7301 | -54.00508 | 2026-09-13 04:17:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| add94cff-6b74-3982-8d2e-20c94889bb92 | -10.30764 | -45.2967 | 2026-09-13 04:17:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9e60f9be-8237-39fc-92ba-15390a86e2cf | -10.29255 | -45.30539 | 2026-09-13 04:17:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5df807fe-78c9-3fb6-9a68-9bede9d3f608 | -8.02652 | -54.85741 | 2026-09-13 04:17:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 730a241d-f3c5-3b07-8099-8fa535861b0c | -12.49055 | -48.03948 | 2026-09-13 04:17:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2e5dbdfe-3a96-3dff-9f53-05b49372ed0e | -11.36903 | -46.91071 | 2026-09-13 04:17:00 | NOAA-21 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 13a843bd-29f5-3d2a-8beb-8b2bb8d550c6 | -10.68269 | -54.1657 | 2026-09-13 04:17:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 9808d78f-bc5a-3aa5-9b0b-d60feffa721c | -10.21554 | -45.19057 | 2026-09-13 04:17:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 89fcdc49-ea04-3db5-970a-c41a7241e695 | -10.5469 | -45.20422 | 2026-09-13 04:17:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a6f382d5-d97b-321b-9ae9-331fe4f03454 | -10.54123 | -51.38023 | 2026-09-13 04:17:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 6029a5e0-e1f6-3698-926a-462730cc22ac | -7.87327 | -54.72436 | 2026-09-13 04:17:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| bb95af44-d9d7-3a06-9d92-1ea72fc6bd01 | -11.2014 | -42.77872 | 2026-09-13 04:17:00 | NOAA-21 | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 2.7 |
| a960ee6f-f165-3c9a-ae7d-3d547c49ff2b | -13.61862 | -47.88679 | 2026-09-13 04:17:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| a839a821-0d11-33e6-95b6-652fecbeb7f3 | -10.54546 | -51.33028 | 2026-09-13 04:17:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 32eae863-ec41-3ec3-8df4-6460bfe77f39 | -10.22277 | -45.18812 | 2026-09-13 04:17:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e220e382-2e64-37aa-a8aa-027e083c7609 | -8.7964 | -46.94958 | 2026-09-13 04:17:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1399bd34-255c-3b2d-a257-fa812d4f840b | -9.85251 | -48.51806 | 2026-09-13 04:17:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b1c124de-e4d9-309f-9402-ff912dd99725 | -10.94178 | -48.35398 | 2026-09-13 04:17:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 88349430-8f5b-394a-ae5d-a934b0aa7589 | -12.85838 | -44.3882 | 2026-09-13 04:17:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 27.0 |
| bc55deac-247d-3a8a-b213-54138822be13 | -13.61304 | -47.87663 | 2026-09-13 04:17:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 7.5 |
| d9bf56f6-bbbf-331b-9d7f-638195e43188 | -10.68608 | -54.178 | 2026-09-13 04:17:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 13.2 |
| 94e30c37-74c7-37b4-99ae-ac1b4890c4b1 | -11.80944 | -46.38253 | 2026-09-13 04:17:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4d4ea760-0a01-37ec-9a64-bba0072eff6a | -10.53466 | -51.36386 | 2026-09-13 04:17:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 3ccb1b29-070b-37af-a3ad-8ba8df82877f | -10.9266 | -48.35192 | 2026-09-13 04:17:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8c369ed9-692a-38a6-800b-e036cd89c135 | -10.5591 | -51.3335 | 2026-09-13 04:17:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 299256e9-823c-3e12-bf8d-a24bb015e2f6 | -8.12364 | -54.80417 | 2026-09-13 04:17:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 66f271aa-0303-35db-8d52-cbc4e2722451 | -10.68893 | -54.16296 | 2026-09-13 04:17:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 10.2 |
| d20e3d1e-ea06-3068-baeb-bafa8d971ff5 | -13.39169 | -48.00396 | 2026-09-13 04:17:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6c4efc0d-09b4-3c2b-94aa-49a9b02d89ba | -10.49138 | -48.09463 | 2026-09-13 04:17:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d170f364-ef6d-3bdb-b9d7-28764764e2d6 | -12.85507 | -44.38766 | 2026-09-13 04:17:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 27.0 |
| 9c268b97-bdc9-3cd5-8540-ee0f00fa7801 | -8.11327 | -54.79294 | 2026-09-13 04:17:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ce3101ef-da06-35a2-80c5-c51f5d28f599 | -10.47607 | -51.37635 | 2026-09-13 04:17:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 18c74a55-86a0-36ef-b408-02a89162a3d3 | -9.59311 | -46.71938 | 2026-09-13 04:17:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1977faab-3ad8-36bb-a138-4e068a9b763c | -9.89597 | -47.58823 | 2026-09-13 04:17:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 042e7afa-9b9e-313e-ac73-0f92d8e38431 | -8.8141 | -46.90929 | 2026-09-13 04:17:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a88bd6c7-120d-36c5-99af-f662148f7d72 | -13.45202 | -48.48754 | 2026-09-13 04:17:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 6df765c7-f1e1-3015-a659-11634c1d1a33 | -13.60158 | -47.88459 | 2026-09-13 04:17:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 606d3733-c03c-3a49-b53a-fbc226b0f941 | -8.11443 | -54.79801 | 2026-09-13 04:17:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0af55cae-617c-3cdb-849f-72157b540a45 | -10.56576 | -51.34934 | 2026-09-13 04:17:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 0bf2809c-bfa7-31f7-9545-5933dfd3554a | -13.1064 | -44.63071 | 2026-09-13 04:17:00 | NOAA-21 | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| bbcb4e54-82a0-320a-959c-05687269f882 | -8.03241 | -54.8513 | 2026-09-13 04:17:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 3c3467f3-c3f1-3d80-89eb-d050cba222d2 | -9.8989 | -47.59324 | 2026-09-13 04:17:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| f6348f16-ce96-3559-8b5c-28aac1d795ab | -14.91247 | -44.66917 | 2026-09-13 04:17:00 | NOAA-21 | CÔNEGO MARINHO | MINAS GERAIS | Brasil | 3117836 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9c7085e4-7df3-34f8-a01d-6fe82e5b5f78 | -10.9258 | -48.35657 | 2026-09-13 04:17:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 795b82fd-0e95-364b-baf3-5d86f8ba0e73 | -13.0203 | -48.64268 | 2026-09-13 04:17:00 | NOAA-21 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 3508b571-09e9-39db-9eaf-f109b99e3272 | -15.26472 | -42.80062 | 2026-09-13 04:17:00 | NOAA-21 | MONTE AZUL | MINAS GERAIS | Brasil | 3142908 | 31 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 8856c8dd-4dca-37b5-b596-a2d935be9a61 | -10.62402 | -46.10805 | 2026-09-13 04:17:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6b071a3e-14fe-392a-b737-4aab27d51e38 | -9.37292 | -50.09932 | 2026-09-13 04:17:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 27b9fd34-2623-38a9-b538-3179a8a4ae80 | -11.72386 | -46.73645 | 2026-09-13 04:17:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8458b610-faa6-3a14-8412-31bb7e96881f | -10.6841 | -54.15827 | 2026-09-13 04:17:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 14.7 |
| bdf91aef-9af3-315c-9d6d-5c5e2380d702 | -10.55085 | -51.32668 | 2026-09-13 04:17:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d1c0e0f1-f8e9-3467-bced-76ba8043d8fa | -10.96897 | -48.35382 | 2026-09-13 04:17:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 69fbbf6f-0b99-33ff-b086-fb346aaddc48 | -13.60516 | -47.88505 | 2026-09-13 04:17:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 2bfd87ad-603e-38b6-ae3f-29b7d0f6b8db | -11.93781 | -49.75863 | 2026-09-13 04:17:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| efb711f4-8f92-38fe-a27c-07140ae440bd | -9.70089 | -43.39531 | 2026-09-13 04:17:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| c89ae913-c722-3913-a76a-1a4e8ec6004d | -10.35992 | -46.67094 | 2026-09-13 04:17:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a263d46e-ee58-328d-b119-967e7eb95d67 | -11.34868 | -46.79419 | 2026-09-13 04:17:00 | NOAA-21 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| e22cc490-cbc1-324a-9922-a8ee80a262eb | -14.0335 | -48.01209 | 2026-09-13 04:17:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6d7b1b1a-87e9-3b7d-ae88-b6b34c12585d | -8.05326 | -54.84803 | 2026-09-13 04:17:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e10c9fb3-a7cf-375e-b78a-dbe1683cf43f | -8.02048 | -54.85629 | 2026-09-13 04:17:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c02eafce-6849-35bc-9676-0ac0f513908e | -10.45603 | -48.64634 | 2026-09-13 04:17:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| ef356b19-30d8-3bd6-9d88-913a0e165ccb | -14.12348 | -42.12146 | 2026-09-13 04:17:00 | NOAA-21 | LAGOA REAL | BAHIA | Brasil | 2918753 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 0cad85f4-332c-386a-841c-3d70ce7a3622 | -8.12195 | -54.8134 | 2026-09-13 04:17:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 24a6a469-a797-3519-8eec-45b8bd762f8c | -10.63156 | -46.01749 | 2026-09-13 04:17:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| ccd59823-9a2b-31f1-83cc-781dfd5d23c2 | -7.85938 | -54.69898 | 2026-09-13 04:17:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| aa168898-7a21-38ca-9956-41f7fffb05fb | -9.58619 | -55.15751 | 2026-09-13 04:17:00 | NOAA-21 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 66308e3d-4b52-34ac-9d33-3cbed8e0eecd | -10.62802 | -46.10489 | 2026-09-13 04:17:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4d5a7c87-271d-3fdf-8de3-2de253219ede | -8.54045 | -54.71178 | 2026-09-13 04:17:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 70209b1a-8704-3010-8389-0887fa2088ff | -12.14903 | -48.95893 | 2026-09-13 04:17:00 | NOAA-21 | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 1e8b3246-1dba-3617-9454-b1bf8cdf707d | -10.74708 | -43.66522 | 2026-09-13 04:17:00 | NOAA-21 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| af990d03-4725-3ae2-ba2e-6b657fd17008 | -9.57933 | -55.1608 | 2026-09-13 04:17:00 | NOAA-21 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c13ecb10-0b90-3ea6-8750-366544eb1d23 | -8.54558 | -54.71724 | 2026-09-13 04:17:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 0fa19aed-d4a8-36f3-bb70-00f6a65cc160 | -13.60948 | -47.87611 | 2026-09-13 04:17:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 7.5 |
| c857432f-c938-3ec1-8f74-730d854aaf6f | -9.60236 | -46.72919 | 2026-09-13 04:17:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3adc9a26-acfd-3c56-84b3-b5dfe732e496 | -10.03975 | -48.21562 | 2026-09-13 04:17:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fe62f16d-6016-3025-9871-282e1a6345b6 | -14.91579 | -44.66971 | 2026-09-13 04:17:00 | NOAA-21 | CÔNEGO MARINHO | MINAS GERAIS | Brasil | 3117836 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5b49576b-5b7d-3984-bb5f-342b0511ec7b | -13.75032 | -42.59866 | 2026-09-13 04:17:00 | NOAA-21 | CAETITÉ | BAHIA | Brasil | 2905206 | 29 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 3a10bbd6-b018-3037-be2b-4b502f100785 | -10.50309 | -51.30269 | 2026-09-13 04:17:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 961cc293-4fe9-36ce-b225-230304b37fff | -13.37259 | -51.71441 | 2026-09-13 04:17:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 622f6ab8-c5f7-36cb-a828-c71978f9dcc5 | -11.80541 | -46.38575 | 2026-09-13 04:17:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 3064a3f9-777a-30db-887b-b67796349d96 | -8.12044 | -54.7991 | 2026-09-13 04:17:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c083cf42-b919-3b08-8a02-e846e4655a9a | -10.64878 | -46.00169 | 2026-09-13 04:17:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8b21bfba-9aa8-35c6-b3d3-40db06232d7c | -13.43329 | -43.83057 | 2026-09-13 04:17:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |


[Clique aqui para ver as próximas entradas](README28.md)
