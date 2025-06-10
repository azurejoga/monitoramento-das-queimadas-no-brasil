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

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7167be32-895d-3de5-99ad-08127d4517f6 | -9.5954 | -40.34219 | 2025-06-10 03:49:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 809ca7e8-6b2d-3d54-a98d-814c6ee9cfdb | -17.75252 | -42.8934 | 2025-06-10 03:49:00 | NOAA-20 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d73b7b50-9f49-37bf-a3d4-38b98210c510 | -14.20422 | -45.48095 | 2025-06-10 03:49:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5a7a9caa-bd4f-3a23-b58a-3c008410967c | -9.3313 | -40.69266 | 2025-06-10 03:49:00 | NOAA-20 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 279fe71f-90cb-310b-89a8-87047444afc7 | -17.77891 | -42.80655 | 2025-06-10 03:49:00 | NOAA-20 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| cee0c786-5055-336f-bc47-091975793db0 | -14.20697 | -45.49117 | 2025-06-10 03:49:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| be75c777-ff4f-3992-aeac-c8730ea8780d | -14.19797 | -45.48933 | 2025-06-10 03:49:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 955ac110-5a10-38ac-a9cc-c161ecdf9b8e | -8.60571 | -46.58262 | 2025-06-10 03:49:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| dd7f2177-8c69-3265-b88e-49e2101cb45a | -12.29219 | -50.10464 | 2025-06-10 03:49:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| bd93cdca-8308-3e39-8794-2d0c66640cf3 | -7.00921 | -44.61866 | 2025-06-10 03:49:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| a60a868f-9c0e-373e-a5ba-83a7a1cfc711 | -14.2106 | -45.49674 | 2025-06-10 03:49:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b5d643e5-6f20-36f9-9ea1-96fd5be6013a | -8.60098 | -46.57816 | 2025-06-10 03:49:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d3ac70ca-f3c6-3e89-bc74-c58e235bc2b4 | -18.81742 | -46.43615 | 2025-06-10 03:49:00 | NOAA-20 | LAGOA FORMOSA | MINAS GERAIS | Brasil | 3137502 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 2263e2fc-2b8b-3264-a374-3bc8a46b2760 | -15.45235 | -40.93295 | 2025-06-10 03:49:00 | NOAA-20 | ENCRUZILHADA | BAHIA | Brasil | 2910404 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 75980c77-06f9-361c-b55f-3b22c1388add | -13.17198 | -44.9878 | 2025-06-10 03:49:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b5c10f1a-6023-32eb-b9df-55260ceaa325 | -13.55158 | -43.49699 | 2025-06-10 03:49:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| fbd0304d-e2ae-34c3-b6d5-0c3b57c4faef | -19.22677 | -43.75714 | 2025-06-10 03:49:00 | NOAA-20 | BALDIM | MINAS GERAIS | Brasil | 3105004 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 6c328755-a286-3b90-acf9-e8c0bf839ee4 | -12.28594 | -50.10328 | 2025-06-10 03:49:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| faf3b5e4-b355-3c93-89de-c5278c4aa34f | -13.08882 | -52.2909 | 2025-06-10 03:49:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 547576b2-0335-34ec-8e9b-482e734c9025 | -15.08451 | -44.82264 | 2025-06-10 03:49:00 | NOAA-20 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d5c2f00c-e4ab-3324-8926-b3f60442450a | -15.83312 | -42.5924 | 2025-06-10 03:49:00 | NOAA-20 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| f0654fbb-b5fb-3ce4-b9a8-bbf9051adcef | -8.6016 | -46.57477 | 2025-06-10 03:49:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 73d159d5-9ad3-3a92-908a-81f8c5e3fa54 | -18.05725 | -39.91488 | 2025-06-10 03:49:00 | NOAA-20 | MUCURI | BAHIA | Brasil | 2922003 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| e564663e-ca4f-348d-96d6-d91dfb9756b4 | -16.99949 | -40.83505 | 2025-06-10 03:49:00 | NOAA-20 | ÁGUAS FORMOSAS | MINAS GERAIS | Brasil | 3100906 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 29505bb0-dc1f-3b7e-9c24-38c858e7c94c | -8.40333 | -36.12933 | 2025-06-10 03:49:00 | NOAA-20 | ALTINHO | PERNAMBUCO | Brasil | 2600807 | 26 | 33 | nan | nan | nan | Caatinga | 0.7 |
| d1142fdb-285e-3b95-bc4c-973847a12f79 | -14.23575 | -45.48714 | 2025-06-10 03:49:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 02668a21-b335-33e1-a9a8-63a2d20e8473 | -17.26952 | -48.60915 | 2025-06-10 03:49:00 | NOAA-20 | SANTA CRUZ DE GOIÁS | GOIÁS | Brasil | 5219209 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e7232333-92e1-3149-82e1-b4f7f7e003e5 | -8.34994 | -36.62504 | 2025-06-10 03:49:00 | NOAA-20 | SANHARÓ | PERNAMBUCO | Brasil | 2612406 | 26 | 33 | nan | nan | nan | Caatinga | 0.4 |
| fbdaa8a6-57cc-3520-ae11-0f5c16f10c72 | -14.20334 | -45.48561 | 2025-06-10 03:49:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bc34a3b7-9366-30a9-bd0e-7ae3b27a7fee | -7.77613 | -43.05526 | 2025-06-10 03:49:00 | NOAA-20 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| d11791f4-72f3-399d-94d0-5f58d06b3eae | -13.09579 | -52.29248 | 2025-06-10 03:49:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ad32d4e3-fc03-33c7-9407-812d756b7b5e | -7.47067 | -45.50854 | 2025-06-10 03:49:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 0c7c4a53-88d4-3776-8e97-e98b5c33e935 | -15.91306 | -41.36664 | 2025-06-10 03:49:00 | NOAA-20 | CACHOEIRA DE PAJEÚ | MINAS GERAIS | Brasil | 3102704 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 3877dc54-fadb-3908-b728-7f747fda933b | -14.70504 | -40.97373 | 2025-06-10 03:49:00 | NOAA-20 | ANAGÉ | BAHIA | Brasil | 2901205 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| e0121636-4666-3528-b9e9-85c8a5221edc | -9.59185 | -40.34159 | 2025-06-10 03:49:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 16.4 |
| 8eb1555d-cc56-3819-b073-a1e43db41fb7 | -15.56948 | -47.85724 | 2025-06-10 03:49:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3c025dec-2358-3bab-96d9-13f8378a1672 | -13.86946 | -42.54782 | 2025-06-10 03:49:00 | NOAA-20 | CAETITÉ | BAHIA | Brasil | 2905206 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| f64b204a-03ec-3984-89fe-cd0db5f0259a | -8.60284 | -46.56797 | 2025-06-10 03:49:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1695a5c1-1ae9-382e-90f6-877e986de7e3 | -14.49993 | -43.80867 | 2025-06-10 03:49:00 | NOAA-20 | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 0b41a7fa-e9a2-3184-bbe8-02ac7bca707f | -8.77377 | -37.02048 | 2025-06-10 03:49:00 | NOAA-20 | BUÍQUE | PERNAMBUCO | Brasil | 2602803 | 26 | 33 | nan | nan | nan | Caatinga | 0.4 |
| c7774f77-1d19-308c-bc09-740eed7d29f4 | -14.18984 | -45.48285 | 2025-06-10 03:49:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 358590cf-f512-312d-869e-346c253faa9c | -14.18896 | -45.4875 | 2025-06-10 03:49:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6e942ab7-aa37-3928-b6ce-f349eb20d827 | -14.19346 | -45.48841 | 2025-06-10 03:49:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b8057639-df31-3d5a-9c8d-f1382589a74c | -14.23489 | -45.49182 | 2025-06-10 03:49:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| eea07f33-b5ae-3419-814b-cf846104b72c | -17.27471 | -48.61037 | 2025-06-10 03:49:00 | NOAA-20 | SANTA CRUZ DE GOIÁS | GOIÁS | Brasil | 5219209 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 189cd471-3cd3-3d62-a7b4-937ef91be72e | -14.21323 | -45.48271 | 2025-06-10 03:49:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2db95ebf-4cc8-3f40-b08c-0f5a424dfd6c | -14.21147 | -45.49208 | 2025-06-10 03:49:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fb873a1a-14e1-37e7-a6f4-609f93cd72b0 | -8.6051 | -46.58597 | 2025-06-10 03:49:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4b363ab2-eb45-3858-9074-ab10f2154dd8 | -18.05667 | -39.91851 | 2025-06-10 03:49:00 | NOAA-20 | MUCURI | BAHIA | Brasil | 2922003 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 75609ae4-07d9-3421-a4b3-8bc4474bd514 | -12.28843 | -50.10613 | 2025-06-10 03:49:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 80a9e85e-dfe7-3753-abd1-33e3ae8f12a6 | -8.60879 | -46.5657 | 2025-06-10 03:49:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6443442c-9eed-39cf-85c5-67195e247cb9 | -14.21598 | -45.49297 | 2025-06-10 03:49:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b82841be-e3b7-335a-8361-928247679e6f | -9.59252 | -40.33752 | 2025-06-10 03:49:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 16.4 |
| 1ff281a5-5f46-3fc6-991a-4d314c5719a5 | -7.43066 | -45.79172 | 2025-06-10 03:49:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 721d3d7b-f84b-3c6a-b7e8-c89f2941ac09 | -7.01409 | -44.61924 | 2025-06-10 03:49:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 1479913c-000e-309a-8e69-88801ea8cde7 | -14.20247 | -45.49025 | 2025-06-10 03:49:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 023c81f4-44b7-35ee-af96-4c0a37d13f18 | -7.00829 | -44.62397 | 2025-06-10 03:49:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 59bf6b47-d643-33e5-a677-784b55c5a8b0 | -8.33809 | -48.44962 | 2025-06-10 03:49:00 | NOAA-20 | BRASILÂNDIA DO TOCANTINS | TOCANTINS | Brasil | 1703602 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 2677e891-fa1e-3a06-95aa-2b4e2c5532a7 | -18.81653 | -46.44065 | 2025-06-10 03:49:00 | NOAA-20 | LAGOA FORMOSA | MINAS GERAIS | Brasil | 3137502 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4d0ce5f7-3c95-374b-a7d1-6bb1bcbe7749 | -19.00451 | -43.52394 | 2025-06-10 03:49:00 | NOAA-20 | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 5b4247ae-f6a9-33e3-b487-5f37b94a2666 | -15.77823 | -39.35642 | 2025-06-10 03:49:00 | NOAA-20 | MASCOTE | BAHIA | Brasil | 2920908 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| ffe43046-7730-3a28-87a8-54fe808ba811 | -12.28489 | -50.10836 | 2025-06-10 03:49:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 7d152564-2740-39d8-b398-348e49bbe67d | -6.86624 | -47.85949 | 2025-06-10 03:49:00 | NOAA-20 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 3b1e688f-0d80-345b-948f-3caaf5ef4b53 | -12.28945 | -50.10104 | 2025-06-10 03:49:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 2dbd49ae-e637-3f7e-a18d-7ec39da2bdc3 | -15.08876 | -44.82347 | 2025-06-10 03:49:00 | NOAA-20 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 88530709-88e4-390e-b998-12527885a5f1 | -14.21511 | -45.49765 | 2025-06-10 03:49:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a38b5701-868c-397b-9ce4-c0c4c20784bb | -14.23939 | -45.49271 | 2025-06-10 03:49:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0cf29e98-72f3-33d4-88ed-09ba8cbb470b | -17.00012 | -40.8313 | 2025-06-10 03:49:00 | NOAA-20 | ÁGUAS FORMOSAS | MINAS GERAIS | Brasil | 3100906 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 0c71bfa4-33b2-3af3-bbc8-96997977cd55 | -6.86025 | -47.85844 | 2025-06-10 03:49:00 | NOAA-20 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4681240d-4192-30dd-a048-23b39ce8d25a | -14.19258 | -45.49307 | 2025-06-10 03:49:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 85dd3b33-ff7a-39b9-91ad-ba92f50ae088 | -17.59416 | -43.19717 | 2025-06-10 03:49:00 | NOAA-20 | CARBONITA | MINAS GERAIS | Brasil | 3113503 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 97228ba6-6866-3fcd-9210-23272e4ac01b | -7.015 | -44.61396 | 2025-06-10 03:49:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| eed43e8d-86b3-3c44-a3bb-f4d1564cc4f4 | -7.47174 | -45.50256 | 2025-06-10 03:49:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 75137c08-a821-35d2-b5fb-e68e5578612a | -14.19434 | -45.48376 | 2025-06-10 03:49:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6730e91d-5d24-3dc0-9218-da11024e2121 | -8.61045 | -46.58704 | 2025-06-10 03:49:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ee3ee347-be76-367b-a4d0-dd0acec9d940 | -7.4712 | -45.50553 | 2025-06-10 03:49:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| cde4c115-8776-31c1-9dce-f429022bcb33 | -15.90958 | -41.36604 | 2025-06-10 03:49:00 | NOAA-20 | CACHOEIRA DE PAJEÚ | MINAS GERAIS | Brasil | 3102704 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 43de1176-f1d2-3320-97ca-c555431cfb29 | -14.50059 | -43.80503 | 2025-06-10 03:49:00 | NOAA-20 | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| c70ee84e-e1a7-3167-b906-a745cfe9ff2c | -7.0205 | -44.58216 | 2025-06-10 03:49:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 1167dc3b-3e1a-321d-8d4c-aa638f4d399b | -14.19709 | -45.49398 | 2025-06-10 03:49:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ba0d5804-73bb-3fac-bda5-f59ddb987441 | -14.19884 | -45.48469 | 2025-06-10 03:49:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c4054905-0d4f-3635-96fe-aab9e25d179a | -12.29114 | -50.10973 | 2025-06-10 03:49:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 96278fb5-7922-32af-83b7-8b824f0e2953 | -9.58542 | -40.33632 | 2025-06-10 03:49:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 0f392529-6086-3b15-bd05-36838cd2b849 | -14.20785 | -45.4865 | 2025-06-10 03:49:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8d3e05d1-0a5b-3843-abde-3cd497eddc87 | -8.60037 | -46.58154 | 2025-06-10 03:49:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| edab3e17-ce7c-33ac-8ae5-f624bcd7874d | -16.11708 | -41.25869 | 2025-06-10 03:49:00 | NOAA-20 | PEDRA AZUL | MINAS GERAIS | Brasil | 3148707 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 7ab70911-0f3f-318d-a6d7-8e8375b38dfe | -7.27459 | -49.57101 | 2025-06-10 03:49:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 453906a0-60a3-3079-8cf6-74a5e72aa369 | -14.20872 | -45.48183 | 2025-06-10 03:49:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5b3ce0df-81b7-3780-83f4-4ffa0befb4ad | -10.0545 | -48.667 | 2025-06-10 03:50:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 48.6 |
| 1152cda3-8889-328b-aff5-d33d62171fc8 | -23.40572 | -46.5571 | 2025-06-10 03:51:00 | NOAA-20 | SÃO PAULO | SÃO PAULO | Brasil | 3550308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| b5419ea4-9cae-3d17-82a5-d9e7de188dbb | -23.3378 | -46.77261 | 2025-06-10 03:51:00 | NOAA-20 | CAIEIRAS | SÃO PAULO | Brasil | 3509007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| e5d51836-5bb3-38dc-a471-52c76045c988 | -22.53892 | -48.8121 | 2025-06-10 03:51:00 | NOAA-20 | MACATUBA | SÃO PAULO | Brasil | 3528007 | 35 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3adc5528-fc98-39d3-83a7-5206484d8c19 | -23.40648 | -46.42234 | 2025-06-10 03:51:00 | NOAA-20 | GUARULHOS | SÃO PAULO | Brasil | 3518800 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 89853a85-24fc-3901-be19-1541809b3405 | -22.538 | -48.81395 | 2025-06-10 03:51:00 | NOAA-20 | MACATUBA | SÃO PAULO | Brasil | 3528007 | 35 | 33 | nan | nan | nan | Cerrado | 1.9 |
| dd83cf0d-0ca6-39d2-acd4-7a2dfe067907 | -23.23569 | -51.28464 | 2025-06-10 03:51:00 | NOAA-20 | CAMBÉ | PARANÁ | Brasil | 4103701 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 495abe82-4d4f-369a-9495-3e57339c1058 | -5.2108 | -43.3067 | 2025-06-10 04:00:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 119.6 |
| b4a95275-e935-353c-9626-ecc4844fab00 | -5.2106 | -43.33 | 2025-06-10 04:00:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 68.9 |
| 77929cba-2c0a-3260-98cb-3104cc6049a9 | -5.1921 | -43.308 | 2025-06-10 04:00:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 60.9 |
| 0469adc8-9a81-3710-b486-f40c4ce1c912 | -5.2108 | -43.3067 | 2025-06-10 04:10:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 62.3 |
| 10752fc8-a649-3d7a-a3c8-63c8ea2226e2 | -5.2108 | -43.3067 | 2025-06-10 04:20:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 85.7 |


[Clique aqui para ver as próximas entradas](README7.md)
