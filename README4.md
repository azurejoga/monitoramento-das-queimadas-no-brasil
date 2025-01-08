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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 539460e3-401c-36f3-b2dd-4632e0c583da | -20.95595 | -49.75449 | 2025-01-08 04:59:00 | NOAA-20 | JOSÉ BONIFÁCIO | SÃO PAULO | Brasil | 3525706 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| f8e081bf-2e8d-37f9-8972-559e32dd45b0 | -20.64724 | -49.30199 | 2025-01-08 04:59:00 | NOAA-20 | ONDA VERDE | SÃO PAULO | Brasil | 3534005 | 35 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 26e89914-d83d-3114-8d52-038c205af4f8 | -23.79312 | -50.27943 | 2025-01-08 04:59:00 | NOAA-20 | IBAITI | PARANÁ | Brasil | 4109708 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| f91a401c-6d53-32af-9c0d-34fe365d0d22 | -20.96167 | -49.75183 | 2025-01-08 04:59:00 | NOAA-20 | JOSÉ BONIFÁCIO | SÃO PAULO | Brasil | 3525706 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.3 |
| d8e7fe81-8434-377f-81e2-88ec4e664367 | -20.65149 | -49.30836 | 2025-01-08 04:59:00 | NOAA-20 | ONDA VERDE | SÃO PAULO | Brasil | 3534005 | 35 | 33 | nan | nan | nan | Cerrado | 3.5 |
| c8480b3d-7fdd-3df7-8925-fde417d227c0 | -23.79784 | -50.2811 | 2025-01-08 04:59:00 | NOAA-20 | IBAITI | PARANÁ | Brasil | 4109708 | 41 | 33 | nan | nan | nan | Mata Atlântica | 5.1 |
| f02ea753-a7b9-314e-93ac-df3b96a63d83 | -20.9611 | -49.75721 | 2025-01-08 04:59:00 | NOAA-20 | JOSÉ BONIFÁCIO | SÃO PAULO | Brasil | 3525706 | 35 | 33 | nan | nan | nan | Mata Atlântica | 7.0 |
| d2327634-5ae3-31c1-8e60-86c41aca88c4 | -21.5561 | -54.19769 | 2025-01-08 04:59:00 | NOAA-20 | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1976c1fb-9a99-3a94-9305-d9caacf4e812 | -20.65698 | -49.30345 | 2025-01-08 04:59:00 | NOAA-20 | ONDA VERDE | SÃO PAULO | Brasil | 3534005 | 35 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d19c1a44-4c9f-318e-b94e-3ca2f650b859 | -23.79733 | -50.28522 | 2025-01-08 04:59:00 | NOAA-20 | IBAITI | PARANÁ | Brasil | 4109708 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 8d4c6251-8ec7-30b3-b1e1-122e3fd150b0 | -20.9607 | -49.7552 | 2025-01-08 04:59:00 | NOAA-20 | JOSÉ BONIFÁCIO | SÃO PAULO | Brasil | 3525706 | 35 | 33 | nan | nan | nan | Mata Atlântica | 11.1 |
| 6b846751-b9e0-35b7-bbb3-3a0f0bdd1d92 | -23.79306 | -50.28059 | 2025-01-08 04:59:00 | NOAA-20 | IBAITI | PARANÁ | Brasil | 4109708 | 41 | 33 | nan | nan | nan | Mata Atlântica | 5.1 |
| f7dac6d6-f713-3772-8cda-5beb7741c984 | -20.65211 | -49.30272 | 2025-01-08 04:59:00 | NOAA-20 | ONDA VERDE | SÃO PAULO | Brasil | 3534005 | 35 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 56f2cd09-dd2d-3b9e-9d01-42ebbe81df91 | -23.7979 | -50.27993 | 2025-01-08 04:59:00 | NOAA-20 | IBAITI | PARANÁ | Brasil | 4109708 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| e22d82a0-62e6-31b5-a885-5b11f651b75a | -20.47737 | -53.67676 | 2025-01-08 04:59:00 | NOAA-20 | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d20f78fa-faa0-3ff6-b5f0-8b4114e69dd5 | -20.64662 | -49.30767 | 2025-01-08 04:59:00 | NOAA-20 | ONDA VERDE | SÃO PAULO | Brasil | 3534005 | 35 | 33 | nan | nan | nan | Cerrado | 1.9 |
| de9b50df-bfbb-3d9c-9203-bbdcc6be3e2f | -24.07854 | -51.0196 | 2025-01-08 04:59:00 | NOAA-20 | ORTIGUEIRA | PARANÁ | Brasil | 4117305 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 8372284d-5b3a-337f-81e0-e497e09bdea1 | -30.32116 | -53.41595 | 2025-01-08 05:01:00 | NOAA-20 | CAÇAPAVA DO SUL | RIO GRANDE DO SUL | Brasil | 4302808 | 43 | 33 | nan | nan | nan | Pampa | 2.3 |
| 8f6390ff-5037-38d1-9bb6-bb40b8ef1d8f | 1.05478 | -59.55745 | 2025-01-08 05:46:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 7eabe6d2-fd1f-3e1b-b7fe-02ca95a79c73 | 3.45818 | -60.2117 | 2025-01-08 05:46:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 11a3252c-cc27-3667-8a4b-62a3a783f203 | 3.92726 | -59.72954 | 2025-01-08 05:46:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a6162601-b2bd-3755-856c-258abce8335f | 1.34805 | -60.03145 | 2025-01-08 05:46:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a42589ac-db7b-3743-950c-5557760fee54 | 4.31963 | -60.9911 | 2025-01-08 05:46:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 73ab5a15-1825-34df-8e92-5786bdbe0d0f | 4.31596 | -60.99172 | 2025-01-08 05:46:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a0dd51a4-ac70-3c5e-a241-433c0c5cb2e1 | 3.45898 | -60.21662 | 2025-01-08 05:46:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 59c25d60-3838-3ffa-8224-7044b946f5d8 | 2.98527 | -61.18398 | 2025-01-08 05:46:00 | NOAA-21 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 49c742f2-d704-30f0-93d3-3c2eee78e6c3 | 1.05416 | -59.55356 | 2025-01-08 05:46:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 0b61e47a-2512-3c96-b248-ebf09b7bb0af | 3.58207 | -60.85847 | 2025-01-08 05:46:00 | NOAA-21 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f4caef7f-fdd9-3337-a1b7-8b312dc73b3e | 4.31989 | -60.98895 | 2025-01-08 05:46:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 1e67402e-e9aa-3493-94c6-12d74a063b47 | 3.57905 | -60.86358 | 2025-01-08 05:46:00 | NOAA-21 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f8bd8545-3cb5-3f80-9299-b32e42ce56e9 | 2.42948 | -60.64761 | 2025-01-08 05:46:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 84a9a239-cc36-303f-a8a7-9535d2fea52a | 4.40183 | -60.25267 | 2025-01-08 05:46:00 | NOAA-21 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 11faa3f1-1c58-34d5-9dd9-84abc8c45804 | 4.13124 | -60.6277 | 2025-01-08 05:46:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4a2e356c-ed20-3df6-a810-db222d05f6e3 | 4.4011 | -60.24812 | 2025-01-08 05:46:00 | NOAA-21 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 564ff809-7825-319c-a219-63f6be4bf46a | 3.21141 | -61.58667 | 2025-01-08 05:46:00 | NOAA-21 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 7e05aef9-c22b-36c3-ae69-95cbe8a3685b | 3.20966 | -61.58518 | 2025-01-08 05:46:00 | NOAA-21 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d9d8671e-5f30-387e-9dea-c0590fcc7504 | 4.47756 | -60.57003 | 2025-01-08 06:09:00 | NPP-375D | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| dc3aeaa0-e682-33d5-995b-f358c94590c8 | 3.93239 | -59.72988 | 2025-01-08 06:09:00 | NPP-375D | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 6aa9258e-4201-30b5-9dd4-280665462ab4 | 3.92621 | -59.73091 | 2025-01-08 06:09:00 | NPP-375D | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 989daa06-d8f6-3b26-8ed2-9e6c544db163 | 4.47873 | -60.57237 | 2025-01-08 06:09:00 | NPP-375D | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 191e8e7f-3119-3026-a281-d8304683e5d3 | 4.48352 | -60.56998 | 2025-01-08 06:09:00 | NPP-375D | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 46cee0c4-d54f-34ac-8b8d-b81e6c913a7e | 3.57751 | -60.86214 | 2025-01-08 06:12:00 | NPP-375D | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 274210e8-1490-37a7-89de-05366e8b01d0 | 3.57671 | -60.86056 | 2025-01-08 06:12:00 | NPP-375D | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 1b024b9a-c1ed-3042-b0a3-51879efc4ce2 | 1.34765 | -60.0388 | 2025-01-08 06:12:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9e2f5496-9c64-3681-8763-f5bd93eea382 | 3.45657 | -60.21308 | 2025-01-08 06:12:00 | NPP-375D | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 45371bf0-45a7-3fe1-8bc1-ca43c2222aad | 3.58258 | -60.85714 | 2025-01-08 06:12:00 | NPP-375D | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 92840d71-09a3-32e1-a514-0cc66b719bcc | 3.45732 | -60.21757 | 2025-01-08 06:12:00 | NPP-375D | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ff967427-b90f-3040-9333-e40ab1b3bc85 | 3.58328 | -60.86116 | 2025-01-08 06:12:00 | NPP-375D | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d7f4673f-aad9-39ff-a1e0-9a8da64a67be | 3.57821 | -60.86615 | 2025-01-08 06:12:00 | NPP-375D | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 2260b056-7444-3733-834c-e1d681ab7b0c | 1.05524 | -59.55267 | 2025-01-08 06:12:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 458c5abe-2a7f-3250-afc7-b6df1d9ba57a | 3.58248 | -60.85956 | 2025-01-08 06:12:00 | NPP-375D | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a291441e-f30d-3910-b29a-10cd4edcf688 | 3.57738 | -60.86459 | 2025-01-08 06:12:00 | NPP-375D | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 9d2e74f7-6a32-39c5-ab52-dfbef2201ab4 | 1.34682 | -60.03379 | 2025-01-08 06:12:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 460a2a51-a749-32bf-812f-eb6871b83d98 | -6.58491 | -37.7671 | 2025-01-08 11:57:00 | TERRA_M-M | MATO GROSSO | PARAÍBA | Brasil | 2509370 | 25 | 33 | nan | nan | nan | Caatinga | 19.4 |
| ea6f50ea-80fd-3d42-9113-cef1f1b2f4af | -7.72942 | -37.38432 | 2025-01-08 11:57:00 | TERRA_M-M | INGAZEIRA | PERNAMBUCO | Brasil | 2607109 | 26 | 33 | nan | nan | nan | Caatinga | 15.1 |
| db6cc64a-0866-3ed4-9b1b-e42ddf82c866 | -9.05463 | -35.32903 | 2025-01-08 11:57:00 | TERRA_M-M | JAPARATINGA | ALAGOAS | Brasil | 2703601 | 27 | 33 | nan | nan | nan | Mata Atlântica | 8.5 |
| d8b8819a-21eb-3f4f-a922-dee466cf871e | -6.93494 | -35.20392 | 2025-01-08 11:57:00 | TERRA_M-M | CUITÉ DE MAMANGUAPE | PARAÍBA | Brasil | 2505238 | 25 | 33 | nan | nan | nan | Mata Atlântica | 12.1 |
| 2d6443f5-a1e9-3bfc-ad8b-d1366556137f | -6.78711 | -35.53299 | 2025-01-08 11:57:00 | TERRA_M-M | PIRPIRITUBA | PARAÍBA | Brasil | 2511806 | 25 | 33 | nan | nan | nan | Caatinga | 6.7 |
| db2c25bb-c02a-3e36-a13a-a46f0ac47ba8 | -7.79519 | -35.24996 | 2025-01-08 11:57:00 | TERRA_M-M | NAZARÉ DA MATA | PERNAMBUCO | Brasil | 2609501 | 26 | 33 | nan | nan | nan | Mata Atlântica | 14.6 |
| fa87681c-bb1f-3349-87c4-4257e621feb2 | -9.32274 | -37.08234 | 2025-01-08 11:57:00 | TERRA_M-M | SANTANA DO IPANEMA | ALAGOAS | Brasil | 2708006 | 27 | 33 | nan | nan | nan | Caatinga | 7.9 |
| 0b6a8f1f-95b1-335e-9f2d-532e6c9e5117 | -7.64618 | -37.64505 | 2025-01-08 11:57:00 | TERRA_M-M | AFOGADOS DA INGAZEIRA | PERNAMBUCO | Brasil | 2600104 | 26 | 33 | nan | nan | nan | Caatinga | 8.4 |
| 4b9d20c5-db9b-3132-a8b4-20a79660f150 | -7.20838 | -38.423 | 2025-01-08 11:57:00 | TERRA_M-M | MONTE HOREBE | PARAÍBA | Brasil | 2509602 | 25 | 33 | nan | nan | nan | Caatinga | 9.8 |
| 5c95aa45-a408-3b8b-a055-06abc71cb134 | -6.58357 | -37.77624 | 2025-01-08 11:57:00 | TERRA_M-M | MATO GROSSO | PARAÍBA | Brasil | 2509370 | 25 | 33 | nan | nan | nan | Caatinga | 13.9 |
| 343569f2-cf17-3d60-9783-fead6632aabd | -7.65375 | -37.65526 | 2025-01-08 11:57:00 | TERRA_M-M | AFOGADOS DA INGAZEIRA | PERNAMBUCO | Brasil | 2600104 | 26 | 33 | nan | nan | nan | Caatinga | 7.0 |
| c1972de6-90e0-3278-956b-28e62881a868 | -7.45296 | -37.50734 | 2025-01-08 11:57:00 | TERRA_M-M | TABIRA | PERNAMBUCO | Brasil | 2614600 | 26 | 33 | nan | nan | nan | Caatinga | 7.3 |
| d9b63b6e-264d-37a1-86dc-bc42ba0763ad | -6.27124 | -37.58377 | 2025-01-08 11:57:00 | TERRA_M-M | BREJO DO CRUZ | PARAÍBA | Brasil | 2502805 | 25 | 33 | nan | nan | nan | Caatinga | 49.6 |
| 263614b4-bea3-35bb-84e7-2a8a31ff7325 | -8.12751 | -38.2597 | 2025-01-08 11:57:00 | TERRA_M-M | SERRA TALHADA | PERNAMBUCO | Brasil | 2613909 | 26 | 33 | nan | nan | nan | Caatinga | 8.3 |
| 5ff44bbf-e8dc-3234-82ed-382c5b04543e | -6.51698 | -35.55275 | 2025-01-08 11:57:00 | TERRA_M-M | TACIMA | PARAÍBA | Brasil | 2516409 | 25 | 33 | nan | nan | nan | Caatinga | 11.6 |
| fcd95b23-6af1-3338-baab-805621519681 | -8.3259 | -35.66125 | 2025-01-08 11:57:00 | TERRA_M-M | SAIRÉ | PERNAMBUCO | Brasil | 2612000 | 26 | 33 | nan | nan | nan | Mata Atlântica | 9.1 |
| 5eb0adf7-9f6e-3cb2-8899-0f8031ef4220 | -6.83275 | -35.07537 | 2025-01-08 11:57:00 | TERRA_M-M | RIO TINTO | PARAÍBA | Brasil | 2512903 | 25 | 33 | nan | nan | nan | Mata Atlântica | 14.6 |
| cdab1fa3-ecf3-3d3b-b31b-a252e29c648c | -6.27256 | -37.57477 | 2025-01-08 11:57:00 | TERRA_M-M | BREJO DO CRUZ | PARAÍBA | Brasil | 2502805 | 25 | 33 | nan | nan | nan | Caatinga | 26.1 |
| 6f5269fb-6afc-374c-8464-0dd831dbdad7 | -7.01351 | -35.36636 | 2025-01-08 11:57:00 | TERRA_M-M | MARI | PARAÍBA | Brasil | 2509107 | 25 | 33 | nan | nan | nan | Caatinga | 12.4 |
| b5b3ad13-2ae1-39c6-8fb0-794072dc9378 | -8.90365 | -35.34305 | 2025-01-08 11:57:00 | TERRA_M-M | MARAGOGI | ALAGOAS | Brasil | 2704500 | 27 | 33 | nan | nan | nan | Mata Atlântica | 10.4 |
| b4543872-81f7-3438-b50a-6ef032cec520 | -7.72813 | -37.39318 | 2025-01-08 11:57:00 | TERRA_M-M | INGAZEIRA | PERNAMBUCO | Brasil | 2607109 | 26 | 33 | nan | nan | nan | Caatinga | 8.2 |
| 4e8fee11-668e-3574-b528-18a194000861 | -8.60841 | -36.07761 | 2025-01-08 11:57:00 | TERRA_M-M | PANELAS | PERNAMBUCO | Brasil | 2610202 | 26 | 33 | nan | nan | nan | Mata Atlântica | 16.5 |
| c7696f0d-8c57-33ba-ac9b-b399137d5172 | -9.46426 | -36.99029 | 2025-01-08 11:57:00 | TERRA_M-M | CACIMBINHAS | ALAGOAS | Brasil | 2701209 | 27 | 33 | nan | nan | nan | Caatinga | 9.4 |
| d3f07316-5f61-30c3-8fac-162bec6958d7 | -7.64487 | -37.65399 | 2025-01-08 11:57:00 | TERRA_M-M | AFOGADOS DA INGAZEIRA | PERNAMBUCO | Brasil | 2600104 | 26 | 33 | nan | nan | nan | Caatinga | 33.5 |
| abbf7324-6fe8-381c-892f-be7dfe9b8a59 | -8.48037 | -36.39801 | 2025-01-08 11:57:00 | TERRA_M-M | SÃO BENTO DO UNA | PERNAMBUCO | Brasil | 2613008 | 26 | 33 | nan | nan | nan | Caatinga | 17.0 |
| d38191cd-4773-3076-a994-ec0e54646606 | -8.33125 | -35.30117 | 2025-01-08 11:57:00 | TERRA_M-M | ESCADA | PERNAMBUCO | Brasil | 2605202 | 26 | 33 | nan | nan | nan | Mata Atlântica | 9.1 |
| 69249a06-8c3f-3bdf-9f68-59559a8165ee | -4.19102 | -38.37071 | 2025-01-08 11:57:00 | TERRA_M-M | CASCAVEL | CEARÁ | Brasil | 2303501 | 23 | 33 | nan | nan | nan | Caatinga | 12.8 |
| 499c0ce5-00c0-35c6-aebe-9f10dac3d722 | -8.11854 | -38.25836 | 2025-01-08 11:57:00 | TERRA_M-M | SERRA TALHADA | PERNAMBUCO | Brasil | 2613909 | 26 | 33 | nan | nan | nan | Caatinga | 7.7 |
| e83e1adf-edf6-37e6-bc6c-d61110f94bc3 | -9.35839 | -36.95975 | 2025-01-08 11:57:00 | TERRA_M-M | IATI | PERNAMBUCO | Brasil | 2606507 | 26 | 33 | nan | nan | nan | Caatinga | 8.8 |
| 7686f630-094f-3cab-89b6-58726c01372b | -11.21674 | -38.38817 | 2025-01-08 11:59:00 | TERRA_M-M | ITAPICURU | BAHIA | Brasil | 2916500 | 29 | 33 | nan | nan | nan | Caatinga | 12.0 |
| 6a348683-6fde-38d0-8f44-10c5c235a709 | -10.29559 | -38.51149 | 2025-01-08 11:59:00 | TERRA_M-M | CANUDOS | BAHIA | Brasil | 2906824 | 29 | 33 | nan | nan | nan | Caatinga | 7.1 |
| a65d4a19-8d90-31ac-9674-7e9f1540795a | -11.06082 | -39.26064 | 2025-01-08 11:59:00 | TERRA_M-M | ARACI | BAHIA | Brasil | 2902104 | 29 | 33 | nan | nan | nan | Caatinga | 8.6 |
| 16b0b5ab-7522-3d05-a135-a3de0df98fda | -12.04209 | -37.8578 | 2025-01-08 11:59:00 | TERRA_M-M | ESPLANADA | BAHIA | Brasil | 2910602 | 29 | 33 | nan | nan | nan | Mata Atlântica | 8.4 |
| 9a75cfe7-91bb-39f7-b3a1-8dabea5670c4 | -10.1148 | -38.35498 | 2025-01-08 11:59:00 | TERRA_M-M | JEREMOABO | BAHIA | Brasil | 2918100 | 29 | 33 | nan | nan | nan | Caatinga | 8.4 |
| 831eaa6e-ddac-30c7-9083-df44710a3c4e | -11.41492 | -39.17463 | 2025-01-08 11:59:00 | TERRA_M-M | CONCEIÇÃO DO COITÉ | BAHIA | Brasil | 2908408 | 29 | 33 | nan | nan | nan | Caatinga | 11.9 |
| 3dea8921-bb62-3011-9447-fe8ff0c252d9 | -9.75221 | -37.23851 | 2025-01-08 11:59:00 | TERRA_M-M | BELO MONTE | ALAGOAS | Brasil | 2700904 | 27 | 33 | nan | nan | nan | Caatinga | 13.7 |
| f43c3f69-50f0-3674-8e36-4cff81deb125 | -10.39357 | -39.53034 | 2025-01-08 11:59:00 | TERRA_M-M | MONTE SANTO | BAHIA | Brasil | 2921500 | 29 | 33 | nan | nan | nan | Caatinga | 8.2 |


