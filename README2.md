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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 710cc3e0-6b3c-379d-a9b7-4160709baad2 | -8.29415 | -45.00917 | 2025-07-27 00:26:00 | TERRA_M-M | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 0b685686-023d-3541-ba6d-76df3a399a0e | -12.39112 | -48.78534 | 2025-07-27 00:26:00 | TERRA_M-M | TALISMÃ | TOCANTINS | Brasil | 1720978 | 17 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 831c68a2-4c04-3946-8d54-a3fb78f62532 | -7.80288 | -46.57668 | 2025-07-27 00:26:00 | TERRA_M-M | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 37550901-264f-3bcb-9625-a2e6230875ac | -9.57806 | -43.86731 | 2025-07-27 00:26:00 | TERRA_M-M | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 8.5 |
| b2e5d741-61c8-387d-925b-37f8e8866531 | -9.99972 | -44.37009 | 2025-07-27 00:26:00 | TERRA_M-M | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 5.7 |
| b44c6411-9bc2-3c1f-bcfb-bdd527980416 | -5.78698 | -43.60828 | 2025-07-27 00:26:00 | TERRA_M-M | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 29.8 |
| 3b993410-869a-30bd-b792-bb4e877ddddf | -4.06203 | -42.53596 | 2025-07-27 00:26:00 | TERRA_M-M | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 28.0 |
| 8c508d87-12df-3488-8daf-891b5333fbb6 | -9.92085 | -48.90676 | 2025-07-27 00:26:00 | TERRA_M-M | MONTE SANTO DO TOCANTINS | TOCANTINS | Brasil | 1713700 | 17 | 33 | nan | nan | nan | Cerrado | 16.5 |
| 8029e76e-3383-3dc1-9d9b-352da695cd0b | -3.92674 | -42.41397 | 2025-07-27 00:26:00 | TERRA_M-M | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 10.0 |
| a03709b6-67e0-36db-b113-377e515fe28d | -5.1816 | -44.95881 | 2025-07-27 00:26:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| b7dbcd90-1bde-3091-91ba-81d9a2dfbe7b | -7.09089 | -44.90816 | 2025-07-27 00:26:00 | TERRA_M-M | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 547c3f3b-110f-3c1c-8df1-21adbb12b345 | -6.66976 | -43.97091 | 2025-07-27 00:26:00 | TERRA_M-M | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 24.0 |
| ecba0a1e-6775-3b41-aec8-11014e803fce | -7.25084 | -49.6225 | 2025-07-27 00:26:00 | TERRA_M-M | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 15.0 |
| e0592cff-eb66-3cd1-be6c-e6af857f954d | -7.09219 | -44.9173 | 2025-07-27 00:26:00 | TERRA_M-M | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| ef37b081-5c69-35cb-9f74-6e14fba13db9 | -6.98916 | -47.09146 | 2025-07-27 00:26:00 | TERRA_M-M | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 10.0 |
| a8c918fc-4d36-34c4-abb7-d6833c49b995 | -7.10122 | -44.91605 | 2025-07-27 00:26:00 | TERRA_M-M | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 11.4 |
| ae8a2729-a29f-36d1-8824-aca4e0ffc740 | -12.38288 | -48.77951 | 2025-07-27 00:26:00 | TERRA_M-M | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 7405f45e-8f95-3d6e-9dc4-bd8000ee1339 | -10.01408 | -48.22651 | 2025-07-27 00:26:00 | TERRA_M-M | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 5ac41257-6d2e-3fad-a79c-39ae29576640 | -9.92041 | -48.90126 | 2025-07-27 00:26:00 | TERRA_M-M | MONTE SANTO DO TOCANTINS | TOCANTINS | Brasil | 1713700 | 17 | 33 | nan | nan | nan | Cerrado | 17.2 |
| 9d3984fb-e31d-36df-b2b1-587cb79c8b78 | -7.51157 | -44.4318 | 2025-07-27 00:26:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 9bf5d94e-e299-32a1-8d56-f92fa4f71f45 | -5.77415 | -43.60478 | 2025-07-27 00:26:00 | TERRA_M-M | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 16.4 |
| a2f263c7-f61c-3b28-a2ae-a534317903eb | -5.74453 | -43.94691 | 2025-07-27 00:26:00 | TERRA_M-M | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 8ba34c8e-c4c9-3553-97d5-65a31da67dae | -6.89018 | -43.11 | 2025-07-27 00:26:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 540e7d4e-482f-38e8-97b1-702cc72a968c | -7.24065 | -49.62381 | 2025-07-27 00:26:00 | TERRA_M-M | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 18.8 |
| 2b51ddbe-3e10-32e3-be0c-11e11bc8e2a7 | -6.38774 | -47.33891 | 2025-07-27 00:26:00 | TERRA_M-M | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 19.3 |
| 156bf91c-1345-3148-8ce5-cf1d9d9a32d9 | -5.68128 | -43.66952 | 2025-07-27 00:26:00 | TERRA_M-M | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 21.1 |
| 0710463d-529a-3f47-92b5-5156968588d5 | -5.60503 | -45.08444 | 2025-07-27 00:26:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 11.3 |
| b394ef61-2ed4-32c7-8f10-96e18c312c0f | -10.64672 | -46.64551 | 2025-07-27 00:26:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 14.0 |
| 8921e874-dc3d-344b-9140-8af50701c906 | -5.29118 | -45.40889 | 2025-07-27 00:26:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 4ca74850-6266-34b8-a814-4cd4a1b49d9f | -11.30296 | -55.14262 | 2025-07-27 00:26:00 | TERRA_M-M | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 43.7 |
| 269d5f40-acfb-31fe-a296-d1140d244c0c | -4.06806 | -42.52772 | 2025-07-27 00:26:00 | TERRA_M-M | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 21.0 |
| a24fea19-4783-35e4-bdeb-7109504c54c9 | -5.66254 | -46.35121 | 2025-07-27 00:26:00 | TERRA_M-M | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |
| c7309367-379e-3ad9-bf70-19447c30a766 | -10.64797 | -46.65484 | 2025-07-27 00:26:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 3a800cad-43db-38f4-8397-f11a69fe42bc | -10.51625 | -42.55765 | 2025-07-27 00:26:00 | TERRA_M-M | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 21.5 |
| 3b043483-03ff-3661-942e-a1f30aa3c4e0 | -5.78546 | -43.61436 | 2025-07-27 00:26:00 | TERRA_M-M | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 15.3 |
| dfa4bbae-d5b6-3b0c-b00a-320674d1f75e | -8.00916 | -48.17465 | 2025-07-27 00:26:00 | TERRA_M-M | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 4967c8a9-4786-3042-8c8d-f92d9ae1108f | -4.10323 | -47.93057 | 2025-07-27 00:28:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 19.4 |
| 3eaf5554-7077-3633-8b1c-18b76d196fcc | -3.57061 | -49.50727 | 2025-07-27 00:28:00 | TERRA_M-M | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 14.7 |
| 60215dcc-a670-3ae0-98f5-137acf818d5a | -4.1375 | -47.64903 | 2025-07-27 00:28:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 16.0 |
| 5c3d0091-9694-3300-a5b0-894ede8f998e | -4.12857 | -47.65025 | 2025-07-27 00:28:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 14.8 |
| 0d4b0e6b-74f1-365e-a9c3-0b6b756da5c2 | -3.27729 | -48.81876 | 2025-07-27 00:28:00 | TERRA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 0c7e66a9-76b6-3a3e-ac66-643822d228fb | -3.39893 | -47.49508 | 2025-07-27 00:28:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 23.8 |
| af3cf73c-a09d-32a1-8455-2001300be7bf | -4.10316 | -48.19943 | 2025-07-27 00:28:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 8d583628-6c34-31da-8566-ab681e0d0ade | -3.42288 | -49.48632 | 2025-07-27 00:28:00 | TERRA_M-M | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 31.4 |
| 122193c4-bb59-3c75-ae3f-9361ff994c3f | -4.11346 | -47.93839 | 2025-07-27 00:28:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 33.8 |
| 47fef095-86db-32b8-869f-30b54f76429e | -3.75711 | -47.42062 | 2025-07-27 00:28:00 | TERRA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 0b6bbcb7-8245-3157-9425-de489b211ed4 | -3.43246 | -49.48499 | 2025-07-27 00:28:00 | TERRA_M-M | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 1f9c66ca-a634-3934-80a7-b5290fe48d39 | -3.43103 | -49.47456 | 2025-07-27 00:28:00 | TERRA_M-M | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 32.3 |
| 4c8fb583-0734-3833-9ea8-0b02a84d0a3d | -2.81398 | -49.0022 | 2025-07-27 00:28:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 82e22b8c-7777-30e7-85c7-f0679f5cbda1 | -3.40015 | -47.50395 | 2025-07-27 00:28:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 21.2 |
| de0154d7-cf53-385b-88cc-4bb8916054d7 | -3.33258 | -49.03365 | 2025-07-27 00:28:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 9e05aff9-da53-3c8a-b3bb-dac07dcd1c5d | -3.06597 | -49.49633 | 2025-07-27 00:28:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 13.0 |
| 5281cddb-5b36-3767-b9b6-74208e4afa03 | -3.42146 | -49.47588 | 2025-07-27 00:28:00 | TERRA_M-M | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 91.3 |
| 7bb814d1-8929-3b4a-8c7e-2cbbd9659dce | -3.56615 | -49.50339 | 2025-07-27 00:28:00 | TERRA_M-M | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 1f626e62-6e71-35e7-9b24-aab9d9e2530d | -4.10447 | -47.93966 | 2025-07-27 00:28:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 13.5 |
| 270cba14-a44f-38da-a350-de49ceab46dc | -3.06739 | -49.50671 | 2025-07-27 00:28:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 15.1 |
| 1399cadb-5d3f-30ad-86c8-d6db03c1086d | -2.90352 | -48.24836 | 2025-07-27 00:28:00 | TERRA_M-M | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 4b64dae4-4e6e-3b79-97aa-aad30d930017 | -2.74304 | -48.68985 | 2025-07-27 00:28:00 | TERRA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 10.5 |
| c6c63b4c-eb64-378e-9543-92d42e70c667 | -3.39006 | -47.49632 | 2025-07-27 00:28:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 16.9 |
| 9856c70c-8f53-34c7-8002-ac6581c93f71 | -2.74175 | -48.68041 | 2025-07-27 00:28:00 | TERRA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 2b989770-cdf7-3b60-b25b-4fe676fa1fbb | -4.10445 | -48.20878 | 2025-07-27 00:28:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 9354cb69-9cee-37ed-8207-30b135b567ac | -4.11222 | -47.92927 | 2025-07-27 00:28:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 39.3 |
| 6147eaf2-dbd3-3744-8b59-38d9bb711a91 | -4.0754 | -42.5344 | 2025-07-27 00:30:00 | GOES-19 | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 56.5 |
| 3916e794-0eac-39d5-9b0e-ecf41cab689b | -3.4235 | -49.4773 | 2025-07-27 00:30:00 | GOES-19 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 91.8 |
| 2ee82eee-90b0-3720-ade5-aa2d45afe6f1 | -20.9616 | -48.9126 | 2025-07-27 00:30:00 | GOES-19 | NOVAIS | SÃO PAULO | Brasil | 3533254 | 35 | 33 | nan | nan | nan | Mata Atlântica | 54.2 |
| 3a934eb0-e8fb-3f8d-89e3-dd05e7928063 | -6.5445 | -56.1915 | 2025-07-27 00:30:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 47.3 |
| 9da50719-4188-3b9b-947e-45bff880b1c0 | -17.9828 | -53.1615 | 2025-07-27 00:30:00 | GOES-19 | ALTO TAQUARI | MATO GROSSO | Brasil | 5100607 | 51 | 33 | nan | nan | nan | Cerrado | 67.4 |
| 9eedbb42-ba14-3aba-a0f0-2e1578cf973c | -17.963 | -53.1646 | 2025-07-27 00:30:00 | GOES-19 | ALTO TAQUARI | MATO GROSSO | Brasil | 5100607 | 51 | 33 | nan | nan | nan | Cerrado | 66.7 |
| a8f3188b-0e6b-3ce4-9958-86028563396d | -3.4235 | -49.4773 | 2025-07-27 00:40:00 | GOES-19 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 84.7 |
| cc0496c1-f24c-34b4-8e62-fb843ec8c519 | -16.4162 | -48.9164 | 2025-07-27 00:40:00 | GOES-19 | ANÁPOLIS | GOIÁS | Brasil | 5201108 | 52 | 33 | nan | nan | nan | Cerrado | 46.6 |
| 0c990028-18ad-369d-b5a9-782a1ab4182c | -4.8393 | -42.9579 | 2025-07-27 00:40:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 95.7 |
| dbdf6982-c3d6-3dd2-bd58-d05275782bfc | -4.8391 | -42.9813 | 2025-07-27 00:40:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 141.6 |
| da2e1131-3f19-374b-981a-3fe551c9b9ad | -4.8204 | -42.9825 | 2025-07-27 00:40:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 51.5 |
| 2ee220da-3972-3c2d-bc5f-54d7062ed669 | -17.9828 | -53.1615 | 2025-07-27 00:40:00 | GOES-19 | ALTO TAQUARI | MATO GROSSO | Brasil | 5100607 | 51 | 33 | nan | nan | nan | Cerrado | 58.1 |
| 69a44cf4-c38c-3714-b670-d84d6995d380 | -18.0027 | -53.1584 | 2025-07-27 00:40:00 | GOES-19 | ALTO TAQUARI | MATO GROSSO | Brasil | 5100607 | 51 | 33 | nan | nan | nan | Cerrado | 70.1 |
| f6270e79-da0d-363e-8c11-45f853090f2b | -18.0027 | -53.1584 | 2025-07-27 00:50:00 | GOES-19 | ALTO TAQUARI | MATO GROSSO | Brasil | 5100607 | 51 | 33 | nan | nan | nan | Cerrado | 94.0 |
| 0e0888c3-b41c-303c-9c24-c4ef6a534af8 | -9.4952 | -40.3834 | 2025-07-27 00:50:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 62.8 |
| 436f7364-0f75-3e09-ae2e-47bebeaaf3f4 | -16.4162 | -48.9164 | 2025-07-27 00:50:00 | GOES-19 | ANÁPOLIS | GOIÁS | Brasil | 5201108 | 52 | 33 | nan | nan | nan | Cerrado | 52.0 |
| 890bd1e9-5779-3d13-9e9e-ca984784f6c7 | -18.0023 | -53.1799 | 2025-07-27 00:50:00 | GOES-19 | ALTO TAQUARI | MATO GROSSO | Brasil | 5100607 | 51 | 33 | nan | nan | nan | Cerrado | 47.4 |
| bfa02a8c-a6a7-3e0a-8f62-05a5b8f17137 | -3.4235 | -49.4773 | 2025-07-27 00:50:00 | GOES-19 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 66.0 |
| 52b68402-6081-33c6-84c1-70348dfd6d10 | -9.4765 | -40.3613 | 2025-07-27 00:50:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 98.4 |
| 25b178bb-7d32-39ac-8bb2-7e44c690daa3 | -18.0226 | -53.1553 | 2025-07-27 00:50:00 | GOES-19 | ALTO TAQUARI | MATO GROSSO | Brasil | 5100607 | 51 | 33 | nan | nan | nan | Cerrado | 40.9 |
| e0932a09-120a-380c-8f54-b4004bc5a16f | -9.4761 | -40.3862 | 2025-07-27 00:50:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 89.4 |
| e62a47e5-1421-31a6-9055-789340744f41 | -9.4956 | -40.3586 | 2025-07-27 00:50:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 68.6 |
| e5850854-a5f5-3469-9c3d-6c39221eb297 | -3.4235 | -49.4773 | 2025-07-27 01:00:00 | GOES-19 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 52.9 |
| 92bbf230-5bd9-314d-91ea-8bad83f14ec7 | -7.5657 | -61.4001 | 2025-07-27 01:00:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 61.0 |
| 19b0be21-a146-3ce4-b427-2a0b6ca0e596 | -6.6575 | -58.8468 | 2025-07-27 01:00:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 80.2 |
| 8cbd60ab-bc98-3e0a-b985-a90f1b4ea43d | -6.639 | -58.8475 | 2025-07-27 01:00:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 77.3 |
| e56d46ed-693b-375d-af2b-8ab7686e89ab | -9.4765 | -40.3613 | 2025-07-27 01:00:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 59.6 |
| 45ecc11a-95c4-30f3-84a9-1bff9b891b2d | -6.6206 | -58.8483 | 2025-07-27 01:10:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 85.9 |
| cd41867f-cc22-3074-b3cc-cfb3ca8f2b46 | -7.5657 | -61.4001 | 2025-07-27 01:10:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 58.4 |
| c500aae7-4811-3abc-a84a-8d51366b147d | -9.4765 | -40.3613 | 2025-07-27 01:10:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 57.3 |
| 8e89e915-b45f-33db-aef8-44fcc5e37f72 | -17.9828 | -53.1615 | 2025-07-27 01:10:00 | GOES-19 | ALTO TAQUARI | MATO GROSSO | Brasil | 5100607 | 51 | 33 | nan | nan | nan | Cerrado | 37.2 |
| f233f2d2-cb75-3cc5-81c6-f96bfc458e47 | -6.6391 | -58.8282 | 2025-07-27 01:10:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 70.4 |
| 666bfcb6-df46-3c77-a61b-d1bf6e643705 | -6.639 | -58.8475 | 2025-07-27 01:10:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 158.1 |
| 0b598890-34dc-3f14-b5b8-1b2386091ed1 | -6.6389 | -58.8669 | 2025-07-27 01:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 89.3 |
| 934cd1e6-c429-3dde-a31f-428c24c33af3 | -6.6575 | -58.8468 | 2025-07-27 01:10:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 78.5 |
| c1de464c-785e-3e3d-9aff-7398a16aff16 | -9.4765 | -40.3613 | 2025-07-27 01:20:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 71.7 |
| baaf731b-2cc8-399f-a7d5-5593aa29c9b5 | -15.7676 | -49.9555 | 2025-07-27 01:20:00 | GOES-19 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 58.4 |
| 1f91ca7c-a06d-3e2c-98f2-0656ba385730 | -9.4956 | -40.3586 | 2025-07-27 01:20:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 62.8 |


[Clique aqui para ver as próximas entradas](README3.md)
