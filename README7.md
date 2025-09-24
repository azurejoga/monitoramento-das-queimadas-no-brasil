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

## Dados Diários - Página 7

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1e7c4795-a80e-3046-8487-04f3687b5299 | -4.73656 | -42.10058 | 2025-09-24 04:00:00 | NOAA-20 | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| d2c89c71-ebb8-3a1c-a942-6d83fdb2f9df | -6.90654 | -45.67902 | 2025-09-24 04:00:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 8bb0fc6d-73f8-3eac-bfd7-115bae1c855a | -8.18213 | -46.37016 | 2025-09-24 04:00:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b535cd10-ed3e-319f-84a0-a231f008da22 | -5.38429 | -42.28411 | 2025-09-24 04:00:00 | NOAA-20 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 669da9f5-9232-30e7-852a-245a5971282e | -3.80263 | -47.58905 | 2025-09-24 04:00:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e95ae7a5-2c1e-33b7-8e5b-1d4ffb0668e5 | -7.8539 | -46.78323 | 2025-09-24 04:00:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| babec22d-ef9f-3890-bf10-e52d19a64f2e | -5.17726 | -46.12331 | 2025-09-24 04:00:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| ca4f40b9-d94c-3230-bf25-7090961e49c3 | -8.54819 | -44.95972 | 2025-09-24 04:00:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d16735a1-f25f-3d88-a87a-9364933adaac | -2.96468 | -49.57516 | 2025-09-24 04:00:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| a408bfc0-cfe0-3f5d-81c2-65848bc50c65 | -5.25014 | -44.46314 | 2025-09-24 04:00:00 | NOAA-20 | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 16f9140e-474a-3ca9-9b5c-075ca23ce3d9 | -7.81678 | -40.16956 | 2025-09-24 04:00:00 | NOAA-20 | OURICURI | PERNAMBUCO | Brasil | 2609907 | 26 | 33 | nan | nan | nan | Caatinga | 1.5 |
| a4e04b3e-b499-35fe-83a2-73afe926bed3 | -7.28138 | -41.86635 | 2025-09-24 04:00:00 | NOAA-20 | WALL FERRAZ | PIAUÍ | Brasil | 2211704 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| ae21c804-c187-319f-99ef-9feee1869f39 | -5.95804 | -44.11244 | 2025-09-24 04:00:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 07281240-9801-3224-9b6d-08f469304327 | -5.79196 | -42.76222 | 2025-09-24 04:00:00 | NOAA-20 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 43e07445-c141-344a-bd16-5a78a6662573 | -9.86914 | -38.87897 | 2025-09-24 04:00:00 | NOAA-20 | JEREMOABO | BAHIA | Brasil | 2918100 | 29 | 33 | nan | nan | nan | Caatinga | 0.4 |
| f476e1a6-710d-3dda-9b30-f737bb4e5fcd | -6.06796 | -43.79428 | 2025-09-24 04:00:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 5ad1b9fe-5868-3a1a-b425-d776383286a1 | -5.78225 | -42.55778 | 2025-09-24 04:00:00 | NOAA-20 | BARRO DURO | PIAUÍ | Brasil | 2201408 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 7c4c9c4d-d282-3e89-8373-23035c9e95d4 | -6.08152 | -44.86723 | 2025-09-24 04:00:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c7465813-e78f-3b07-b451-ce5030b06d6b | -4.70594 | -46.47089 | 2025-09-24 04:00:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ef842418-9ea9-3e83-8a2e-3ee227c4aec5 | -5.15818 | -45.24408 | 2025-09-24 04:00:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9c7f4300-7569-34e5-a4d5-734d95eabe89 | -5.77905 | -41.76661 | 2025-09-24 04:00:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 32aac363-f47d-3298-8d50-4264cddc47b5 | -6.20364 | -37.62396 | 2025-09-24 04:00:00 | NOAA-20 | CATOLÉ DO ROCHA | PARAÍBA | Brasil | 2504306 | 25 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 7b8e1df0-3a63-3b67-939c-2ff4bfa98d28 | -4.56871 | -43.88423 | 2025-09-24 04:00:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0c948b3a-743a-3c3f-b60a-c8b5bce52e0b | -7.76956 | -46.19384 | 2025-09-24 04:00:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 1a3c9633-602f-3d79-a85b-2362c036f0d6 | -6.32512 | -46.29968 | 2025-09-24 04:00:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| eb853766-550e-3352-87bd-4c08a36fd553 | -6.42696 | -43.0929 | 2025-09-24 04:00:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 4aa1e6f7-6139-309a-992d-76dae44f1b86 | -5.16959 | -45.43571 | 2025-09-24 04:00:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3c1aaa7e-7fb1-31c8-a95b-5f094c2a06e6 | -6.53617 | -44.22077 | 2025-09-24 04:00:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| a31248d4-4659-3fbd-9b3a-fd7d5ac00d3c | -4.30983 | -48.0918 | 2025-09-24 04:00:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 11.5 |
| 40397995-04c6-3692-b520-bc7805084629 | -8.13707 | -44.46328 | 2025-09-24 04:00:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 64f770c4-7d00-3d4a-937a-1d301ba6287a | -7.91978 | -44.11303 | 2025-09-24 04:00:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 258ef065-6dbc-3fb3-8a8b-b94674508a20 | -8.17292 | -46.24292 | 2025-09-24 04:00:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.3 |
| cb772cbc-7f52-30da-b19d-fb7a9abb1138 | -7.82351 | -47.85808 | 2025-09-24 04:00:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 52bad7bb-481c-3482-9abb-a0f9068e404f | -3.61097 | -47.5382 | 2025-09-24 04:00:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8baff31a-eb18-30af-a265-31718ac38d22 | -8.79233 | -43.0737 | 2025-09-24 04:00:00 | NOAA-20 | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 9c3f1528-39f4-3ad1-8137-969008dde780 | -3.69621 | -49.019 | 2025-09-24 04:00:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| dfead319-f355-37b6-b818-19d99e595e76 | -5.75991 | -43.97179 | 2025-09-24 04:00:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 59fac708-8abf-3bd3-8762-9c3423aa2773 | -4.6478 | -43.3713 | 2025-09-24 04:00:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 995906b5-9347-3512-ad9d-9a2173c2efd2 | -5.92192 | -43.92509 | 2025-09-24 04:00:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 13c0f6ec-243c-31f1-a832-d0c8110e532a | -7.94411 | -44.11069 | 2025-09-24 04:00:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f343e658-2bd4-3e7a-8f0e-5136ec0291eb | -5.63709 | -43.91509 | 2025-09-24 04:00:00 | NOAA-20 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 59cefa3b-6a12-34a6-a90e-9561f185ba45 | -8.54647 | -44.96967 | 2025-09-24 04:00:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e13c3914-20a7-3f72-8227-76d018b16188 | -6.32002 | -43.63032 | 2025-09-24 04:00:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 64471f8e-1361-3073-9191-8997d0f5c493 | -7.94716 | -44.09267 | 2025-09-24 04:00:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 24829c0d-c4e6-3e5e-ac33-7e7129249649 | -5.78995 | -41.76457 | 2025-09-24 04:00:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 9158c978-74f5-3b77-9213-32d0beb2ccd4 | -6.14111 | -45.97339 | 2025-09-24 04:00:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4143bb63-4b48-3915-be54-961bdc851424 | -7.50009 | -43.67589 | 2025-09-24 04:00:00 | NOAA-20 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| eac7c81e-437f-3ab2-a505-e37ed25ef24a | -5.72914 | -42.61549 | 2025-09-24 04:00:00 | NOAA-20 | MIGUEL LEÃO | PIAUÍ | Brasil | 2206308 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| e9e369bf-1986-36c4-929d-8538dd50c463 | -3.69682 | -49.01536 | 2025-09-24 04:00:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2d1a8616-28fc-30de-b958-1290f7930b09 | -7.94266 | -44.0965 | 2025-09-24 04:00:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 9cf06895-2279-320c-8389-8b09c172fa53 | -8.18288 | -46.36572 | 2025-09-24 04:00:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 520640c2-d94d-37ce-bbeb-b14bada84a7a | -6.83734 | -44.14102 | 2025-09-24 04:00:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 8afe15ac-969f-3ceb-ab12-ec175614c0df | -8.1401 | -44.46861 | 2025-09-24 04:00:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 041b11d9-f588-3e77-bfd3-384af205f7c8 | -7.92008 | -44.11596 | 2025-09-24 04:00:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 23645a43-fe90-322c-ab8c-0299f7cf7153 | -5.39034 | -42.26888 | 2025-09-24 04:00:00 | NOAA-20 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| c3b21938-683a-3387-af8d-ce77920f9ee4 | -4.79656 | -42.75331 | 2025-09-24 04:00:00 | NOAA-20 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 19af57cb-6ecd-3214-846b-e0a3374d4bd4 | -8.17852 | -46.36533 | 2025-09-24 04:00:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| aed6b64f-5284-39fc-8e5b-3d53378060b9 | -5.62612 | -45.73493 | 2025-09-24 04:00:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 00be0001-789e-3730-bb03-f71e08d6d6d2 | -5.84471 | -42.64118 | 2025-09-24 04:00:00 | NOAA-20 | LAGOINHA DO PIAUÍ | PIAUÍ | Brasil | 2205540 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 3c788db0-f81a-304b-8236-616a432673c4 | -7.19418 | -46.67788 | 2025-09-24 04:00:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c0be6595-27c7-3698-8370-5b4547a74b41 | -3.3916 | -47.49841 | 2025-09-24 04:00:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a0747b16-b24c-34c4-b0cb-ad77981d9d35 | -5.38844 | -42.28072 | 2025-09-24 04:00:00 | NOAA-20 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 6d4918dc-e2e4-3169-af00-0628c9d98fc9 | -4.79533 | -43.53696 | 2025-09-24 04:00:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 15.4 |
| a5e97bec-83ef-3b2f-bf72-fdfee4dcd7bc | -5.64437 | -43.61116 | 2025-09-24 04:00:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ece2abd5-6e0f-3a4f-8660-828fdec9685a | -6.4161 | -43.09115 | 2025-09-24 04:00:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 17.1 |
| 652e1fc0-ede7-31cd-87d2-9abb0b424e59 | -3.64584 | -48.32175 | 2025-09-24 04:00:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 18e71e0b-2037-3e70-b8c3-f830dab0086f | -6.11162 | -41.79155 | 2025-09-24 04:00:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 12.6 |
| ecfffdb4-dd63-3e3e-802a-d00dcbf6b8fd | -6.89091 | -44.76863 | 2025-09-24 04:00:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 74466381-85d1-3830-a650-b4a0b19f5238 | -3.64525 | -48.32514 | 2025-09-24 04:00:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5f1868b3-8c34-3543-8e25-baf391d379bd | -5.46444 | -44.68848 | 2025-09-24 04:00:00 | NOAA-20 | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a759b006-bb32-327a-a2c1-e32d1b371352 | -5.30339 | -45.00008 | 2025-09-24 04:00:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 938f5372-0e66-3237-a68b-a47834b47ebe | -5.95882 | -44.1077 | 2025-09-24 04:00:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 32ac4f00-3399-3cb0-962f-27058f2c9ac5 | -5.8953 | -43.45476 | 2025-09-24 04:00:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 0664a953-600f-3751-8a3b-fd8eeb958ac2 | -5.51633 | -43.86908 | 2025-09-24 04:00:00 | NOAA-20 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 3b01a1f9-3b10-37a0-a331-a3c7f0279722 | -5.23799 | -43.72398 | 2025-09-24 04:00:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 458adeb0-0a58-383f-9905-5e722587aa79 | -5.38203 | -42.27565 | 2025-09-24 04:00:00 | NOAA-20 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 322c6c8f-44d6-3ad7-9947-308d0a5a4501 | -5.42208 | -41.32382 | 2025-09-24 04:00:00 | NOAA-20 | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| a25b7382-43aa-386a-af51-41d58be7654c | -7.94189 | -44.10102 | 2025-09-24 04:00:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ee1ecf0e-decb-31da-a052-336e9b500a77 | -4.31964 | -48.09678 | 2025-09-24 04:00:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 252859d9-9225-350b-ab37-aafc64ebb958 | -7.77247 | -46.20279 | 2025-09-24 04:00:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 374e9fb1-66b1-327a-883d-278fde9a03b6 | -4.40162 | -44.37238 | 2025-09-24 04:00:00 | NOAA-20 | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3656b578-7ebf-3d89-8f68-8c2231675832 | -5.0295 | -43.59935 | 2025-09-24 04:00:00 | NOAA-20 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 60073284-f4fa-333d-9ded-726225c66956 | -6.32373 | -43.63107 | 2025-09-24 04:00:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 3e0a87dc-93a7-36b1-b318-f1ec70dae839 | -3.81424 | -41.55434 | 2025-09-24 04:00:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| a44401b9-8762-310c-a032-1c61e69f5ec8 | -5.62747 | -45.72697 | 2025-09-24 04:00:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 48be8ad9-98cb-366b-9f15-138e843078a2 | -5.89183 | -46.16536 | 2025-09-24 04:00:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 151ccf0a-7734-3d5f-9909-773b501936a4 | -5.90994 | -43.8564 | 2025-09-24 04:00:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c9f8b71e-87d5-3268-98ca-7a2277f4c813 | -4.315 | -48.09273 | 2025-09-24 04:00:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 11.5 |
| 701204a8-4cb9-382d-bbf5-8f22dea4ff65 | -7.82351 | -47.86197 | 2025-09-24 04:00:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b3cd76e5-9bf2-3dbd-b818-fbd3bd20b5c4 | -7.64227 | -45.21815 | 2025-09-24 04:00:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 2bb58a0f-8459-3927-b322-70463162414b | -5.90916 | -43.86103 | 2025-09-24 04:00:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4f210939-1530-3a03-a1e0-4d43d3316d06 | -5.84405 | -42.64522 | 2025-09-24 04:00:00 | NOAA-20 | LAGOINHA DO PIAUÍ | PIAUÍ | Brasil | 2205540 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| e91f58dd-6409-3d9a-a774-cade9de1b0f8 | -5.47193 | -44.69318 | 2025-09-24 04:00:00 | NOAA-20 | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| fa0e88f5-f8c0-3e39-bf52-597190ab2ea5 | -8.52999 | -45.01825 | 2025-09-24 04:00:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4daea9a5-a7bb-3a66-8d3a-69ebfcb83384 | -8.81478 | -43.06909 | 2025-09-24 04:00:00 | NOAA-20 | SÃO BRAZ DO PIAUÍ | PIAUÍ | Brasil | 2209559 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 18d93051-6442-3693-b57b-802e73c71cbf | -5.64473 | -43.91648 | 2025-09-24 04:00:00 | NOAA-20 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 33.1 |
| 461927ce-4c57-3231-82f4-5f5dab580119 | -8.82956 | -44.33775 | 2025-09-24 04:00:00 | NOAA-20 | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e14ec5d9-e315-318e-919e-887b1ab52769 | -5.24179 | -43.72461 | 2025-09-24 04:00:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 4cf08af8-482a-3fe6-a69a-55d570ac85d2 | -5.75451 | -42.59415 | 2025-09-24 04:00:00 | NOAA-20 | OLHO D'ÁGUA DO PIAUÍ | PIAUÍ | Brasil | 2207108 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| e03c2456-01c7-3d92-9a15-4c29e41a85a6 | -3.18774 | -48.81285 | 2025-09-24 04:00:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |


[Clique aqui para ver as próximas entradas](README8.md)
