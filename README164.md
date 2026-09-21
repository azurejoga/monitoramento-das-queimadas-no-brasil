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

## Dados Diários - Página 164

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| df704f7b-97aa-3982-8b61-19756d59b39c | -5.98792 | -45.075 | 2026-09-21 16:03:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| a055682d-56b5-3f9a-b0de-d8f613b788fe | -6.99048 | -44.7022 | 2026-09-21 16:03:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 13.8 |
| 4a56c309-775f-3fb4-a4d8-b20ed0776575 | -5.53704 | -47.42863 | 2026-09-21 16:03:00 | NOAA-21 | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 190ac8c5-ef9a-306e-8ed5-546202136d24 | -6.99244 | -44.71663 | 2026-09-21 16:03:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| c5497f9f-f2b3-3ff7-aa5a-5825fbed97cc | -7.11977 | -43.08139 | 2026-09-21 16:03:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 9.4 |
| 5645be4a-1d80-3ee1-beea-d5d139b3888e | -1.70981 | -49.79312 | 2026-09-21 16:03:00 | NOAA-21 | CURRALINHO | PARÁ | Brasil | 1502806 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 3582b7f9-d35c-3b49-8b82-e9627f097554 | -5.76348 | -43.70911 | 2026-09-21 16:03:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 61dfbca0-8853-3676-84a6-fbf634405458 | -7.73808 | -49.38921 | 2026-09-21 16:03:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 3f654fb5-ebab-3ab7-ba8d-b417a99f94af | -5.99336 | -45.24946 | 2026-09-21 16:03:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |
| fa31da2d-bf45-31ec-b708-cbe0cc994538 | -8.80374 | -48.74731 | 2026-09-21 16:03:00 | NOAA-21 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 68.4 |
| fb9f2fca-6a5b-3c1c-909b-b44a8c983ae4 | -6.50759 | -44.97292 | 2026-09-21 16:03:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 830a2605-df43-3fa0-a7de-b55133628854 | -6.88117 | -41.70311 | 2026-09-21 16:03:00 | NOAA-21 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 8.3 |
| 7e72f435-e453-3a80-a2d0-11edeb25e3c9 | -7.34431 | -44.20345 | 2026-09-21 16:03:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 19.1 |
| 565b9b6d-a1c5-3c7c-8aba-1e77d156824a | -5.79749 | -43.87621 | 2026-09-21 16:03:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 32.4 |
| 2ab3464f-d382-3148-b651-3d81ddc042aa | -5.85881 | -49.78332 | 2026-09-21 16:03:00 | NOAA-21 | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 240f2cc4-9a7f-3d8c-b556-19823316d48e | -6.86121 | -44.56402 | 2026-09-21 16:03:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 16.4 |
| 4e8b01af-5fb5-303b-b510-ac11baa33d2e | -6.56005 | -45.56614 | 2026-09-21 16:03:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 41.2 |
| fc4a9d75-908d-30d7-89c9-d73744e63f4b | -8.37897 | -47.27233 | 2026-09-21 16:03:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 11.5 |
| d3c8a129-4e82-39eb-874d-2fbdce7e895b | -6.74951 | -46.62714 | 2026-09-21 16:03:00 | NOAA-21 | SÃO PEDRO DOS CRENTES | MARANHÃO | Brasil | 2111573 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 8da450bb-09be-302c-9d42-d5b57ae714e6 | -6.5456 | -44.12101 | 2026-09-21 16:03:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 5b37d379-962f-3637-bd34-2bc318bf8bd4 | -2.61583 | -51.73236 | 2026-09-21 16:03:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 20.4 |
| d08cad44-edc1-3044-a7e8-3053b9c518dd | -3.39153 | -50.44067 | 2026-09-21 16:03:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 24.3 |
| df841021-2d3d-3711-831b-f2afcd20e47a | -8.48234 | -47.02384 | 2026-09-21 16:03:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 15.3 |
| 95ee4b61-9266-30ba-86cc-59665b6e28ba | -7.67707 | -44.75966 | 2026-09-21 16:03:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 6.3 |
| b6e8707d-fec6-306b-a1b3-59464b8b6ef6 | -6.56853 | -42.55657 | 2026-09-21 16:03:00 | NOAA-21 | ARRAIAL | PIAUÍ | Brasil | 2201002 | 22 | 33 | nan | nan | nan | Caatinga | 6.2 |
| 2b5eea84-f74c-3ac4-90f9-343cde9dbc46 | -3.20343 | -42.6439 | 2026-09-21 16:03:00 | NOAA-21 | SANTANA DO MARANHÃO | MARANHÃO | Brasil | 2110237 | 21 | 33 | nan | nan | nan | Cerrado | 8.8 |
| c83584ca-6d2e-3f60-83d6-b6115d7e2dad | -8.79754 | -48.74025 | 2026-09-21 16:03:00 | NOAA-21 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 17.1 |
| b0dd9051-e0fb-3a17-9ff7-4c9620060ae1 | -3.36511 | -50.76058 | 2026-09-21 16:03:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 20.3 |
| 76f6a413-9a3b-3d06-a28c-6cba45f83d08 | -3.86344 | -38.54704 | 2026-09-21 16:03:00 | NOAA-21 | PACATUBA | CEARÁ | Brasil | 2309706 | 23 | 33 | nan | nan | nan | Caatinga | 7.2 |
| b9bec976-89f1-3387-a1dc-ce8bb7211545 | -6.93418 | -42.89367 | 2026-09-21 16:03:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 10.0 |
| 344ba91d-5f20-300c-8b89-37d6db2f96cf | -8.80484 | -48.74917 | 2026-09-21 16:03:00 | NOAA-21 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 54.8 |
| a6eea91d-be35-3d55-9701-e77492f50850 | -5.79694 | -43.87231 | 2026-09-21 16:03:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 32.4 |
| e9bc1035-7906-373b-b892-d99d4e3fe897 | -4.86738 | -43.56304 | 2026-09-21 16:03:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 4e8e03f9-c53b-36c6-8eed-f2d6a35a6002 | -6.67866 | -47.27908 | 2026-09-21 16:03:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 13.9 |
| 687031de-38a9-329c-8a86-7676f302fea1 | -7.82376 | -45.26494 | 2026-09-21 16:03:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 9196d0bb-baa3-3772-b1e5-102bf06923fc | -7.37407 | -44.70372 | 2026-09-21 16:03:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| d5bbbe63-d5c7-35f8-abb2-9d7ece26cae4 | -3.38297 | -42.96666 | 2026-09-21 16:03:00 | NOAA-21 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 16.7 |
| c7843207-415c-3a19-9c9d-c0376d07edf2 | -7.42109 | -49.84102 | 2026-09-21 16:03:00 | NOAA-21 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 1482371a-9042-38e4-bf8f-45bec4add3c3 | -6.98301 | -47.47897 | 2026-09-21 16:03:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 48d3c43c-3b9f-39e0-8596-e19382176247 | -5.23016 | -49.32129 | 2026-09-21 16:03:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 11.4 |
| e142892e-318c-336f-9d8d-a2ddeae1b54a | -3.58414 | -49.57877 | 2026-09-21 16:03:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| dc2e5ebc-d068-339b-93f8-6f1311c10979 | -8.37248 | -47.18156 | 2026-09-21 16:03:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 4209bea0-5af6-3038-bd11-b47710cbc56f | -8.30332 | -46.86921 | 2026-09-21 16:03:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 6783b8c5-35a1-3dd4-a6a4-ecd54b88b6ea | -6.44883 | -48.4493 | 2026-09-21 16:03:00 | NOAA-21 | XAMBIOÁ | TOCANTINS | Brasil | 1722107 | 17 | 33 | nan | nan | nan | Amazônia | 5.3 |
| c2d0fe4e-46ec-3861-8c59-5efae50f5646 | -6.45035 | -45.16561 | 2026-09-21 16:03:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 12.9 |
| e1019e1e-3506-3add-80b3-f4b37f8f8d68 | -6.15649 | -47.49379 | 2026-09-21 16:03:00 | NOAA-21 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 10.3 |
| d4b37236-162c-3841-8f3d-6cf94dcd6034 | -8.34087 | -47.54562 | 2026-09-21 16:03:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 11.2 |
| dbbd7fad-dffe-342c-a162-0fa121da97f8 | -3.3293 | -42.54594 | 2026-09-21 16:03:00 | NOAA-21 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 14.2 |
| 98f47ec4-691c-314f-b2c9-6000c0016991 | -6.8207 | -43.7196 | 2026-09-21 16:03:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 5713ffd3-032e-3642-8cf9-848185760b34 | -7.51663 | -45.44704 | 2026-09-21 16:03:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 3e9d3ca7-d735-367b-9013-31bbb532dd49 | -6.53881 | -44.86294 | 2026-09-21 16:03:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 17.7 |
| c9c2cfa2-fdc8-3d23-a4a7-ff15aaefc6d7 | -7.7374 | -49.38414 | 2026-09-21 16:03:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 68c3cf4b-e513-382b-902f-1e029046956e | -4.60436 | -45.04297 | 2026-09-21 16:03:00 | NOAA-21 | LAGO DO JUNCO | MARANHÃO | Brasil | 2105807 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 9d6b91e5-facf-30bc-88ad-6ac8782c9533 | -5.37256 | -43.19439 | 2026-09-21 16:03:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| d65ec789-7a8f-3a08-820a-495278e34a38 | -5.02012 | -42.97095 | 2026-09-21 16:03:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| ac0341ee-8d41-3ce8-8c91-8dcea9a54b2a | -3.57295 | -43.46673 | 2026-09-21 16:03:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 23.6 |
| 038863bd-e887-32af-84c4-44df4e73256b | -7.40689 | -44.80452 | 2026-09-21 16:03:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 29.9 |
| 9ffa3e27-a4d1-3a77-a2ad-6ec73a59ea8b | -7.54763 | -47.32828 | 2026-09-21 16:03:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 21.9 |
| 6ee3b48c-74b1-31d0-b5dc-40ea0a67d1a0 | -6.50644 | -35.72462 | 2026-09-21 16:03:00 | NOAA-21 | ARARUNA | PARAÍBA | Brasil | 2501005 | 25 | 33 | nan | nan | nan | Caatinga | 14.3 |
| 42633fe9-e668-3755-bbbc-7bd7f4e625f1 | -3.36888 | -49.16697 | 2026-09-21 16:03:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| ec392dbf-7a5b-3ceb-90e7-40671d719c71 | -5.99882 | -45.24723 | 2026-09-21 16:03:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 14.1 |
| 05f3538f-ce5b-3ace-a5b5-c239c7db97a3 | -5.3343 | -42.78658 | 2026-09-21 16:03:00 | NOAA-21 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 72ad9f60-3e3a-3e48-be27-7c0e4651bc09 | -7.57688 | -45.38764 | 2026-09-21 16:03:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 20.1 |
| 07e35793-b7bc-3ecf-8e1b-9cb5e9b9961f | -3.86291 | -38.54361 | 2026-09-21 16:03:00 | NOAA-21 | PACATUBA | CEARÁ | Brasil | 2309706 | 23 | 33 | nan | nan | nan | Caatinga | 7.2 |
| a1c2cd8c-e100-3bc0-a4ea-5239aa296325 | -8.31627 | -46.00666 | 2026-09-21 16:03:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 21.0 |
| 117798d8-f635-383e-88ec-0b90f8bec173 | -8.3725 | -45.631 | 2026-09-21 16:03:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 8c6524d7-3e9c-38b2-989f-5f3ee616fa35 | -6.17655 | -43.35001 | 2026-09-21 16:03:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 1d2dd0e9-5ec1-3851-bd1c-03e7d6f9e8b0 | -6.82127 | -43.72352 | 2026-09-21 16:03:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 149a6276-4ebd-3036-ba20-f70c58f9f0bd | -6.14258 | -47.51322 | 2026-09-21 16:03:00 | NOAA-21 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4f30ba34-7dd8-35b5-bb1e-bd5bb7877106 | -4.40798 | -43.06471 | 2026-09-21 16:03:00 | NOAA-21 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 17.4 |
| df4ab855-38f0-3a63-9b59-26c96cfb9da6 | -6.22771 | -43.74115 | 2026-09-21 16:03:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 6539e5a8-a8eb-3786-97ff-fa96e0995986 | -1.48569 | -49.96442 | 2026-09-21 16:03:00 | NOAA-21 | CURRALINHO | PARÁ | Brasil | 1502806 | 15 | 33 | nan | nan | nan | Amazônia | 63.0 |
| 3a7edd0d-ac17-36f5-9fad-622f2add5db2 | -5.4114 | -42.95868 | 2026-09-21 16:03:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Caatinga | 7.0 |
| 98e091d4-b5f3-3bb8-8247-bb7821d12dcb | -3.67201 | -38.82999 | 2026-09-21 16:03:00 | NOAA-21 | CAUCAIA | CEARÁ | Brasil | 2303709 | 23 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 281f29a2-1885-31b4-aa37-e387bbc3e287 | -3.44428 | -50.66478 | 2026-09-21 16:03:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| e9e8e0ae-9c86-356b-88c9-efd3641cfedd | -8.31282 | -46.01932 | 2026-09-21 16:03:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 23.5 |
| 30afdb61-0845-36c4-9d25-6975843b7481 | -6.53165 | -44.87804 | 2026-09-21 16:03:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 24.3 |
| 38eaabbf-8791-32ed-ab47-6791f7b40c86 | -6.98551 | -44.71043 | 2026-09-21 16:03:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 24.7 |
| b158994c-b5e7-33af-874a-0749196da210 | -6.20276 | -45.3637 | 2026-09-21 16:03:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 20.0 |
| cd0f6c22-7cca-3ab4-943c-643a2d8ae6e7 | -7.3999 | -46.1491 | 2026-09-21 16:03:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 0c2ee861-cd94-30d0-b5e0-28cd1304ab77 | -7.09362 | -43.93199 | 2026-09-21 16:03:00 | NOAA-21 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 513aa0a4-0ffc-3f49-91fe-973925c228a7 | -5.83483 | -43.86683 | 2026-09-21 16:03:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 22.4 |
| a3a08f53-db44-3dfb-bf9f-afd171947f17 | -6.64166 | -44.82698 | 2026-09-21 16:03:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 16.4 |
| 437d3a95-8221-3fc8-9432-23450e7b289e | -6.1925 | -47.59226 | 2026-09-21 16:03:00 | NOAA-21 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 116b9e2c-399a-30f7-832f-9535e257d358 | -6.18565 | -47.49133 | 2026-09-21 16:03:00 | NOAA-21 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 29.2 |
| 62bb9b91-7e80-3b1b-af8e-49baa06394e1 | -6.6404 | -44.8181 | 2026-09-21 16:03:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 23.4 |
| 0d486f80-9bed-3151-936d-6ac2805cd87e | -3.50475 | -40.14564 | 2026-09-21 16:03:00 | NOAA-21 | SANTANA DO ACARAÚ | CEARÁ | Brasil | 2312007 | 23 | 33 | nan | nan | nan | Caatinga | 4.0 |
| d4532165-0612-3ab9-8add-9bffaed00862 | -5.22914 | -38.11691 | 2026-09-21 16:03:00 | NOAA-21 | TABULEIRO DO NORTE | CEARÁ | Brasil | 2313104 | 23 | 33 | nan | nan | nan | Caatinga | 9.8 |
| 11fb0d52-e471-3892-8899-c5bc9bb95932 | -5.74485 | -43.72695 | 2026-09-21 16:03:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 27.4 |
| beb9b742-47a6-3d3e-8db7-acb1c3e8d392 | -6.30451 | -43.79753 | 2026-09-21 16:03:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 2cfdaa89-dda6-3b38-a77f-dd236d46d709 | -3.18453 | -42.80047 | 2026-09-21 16:03:00 | NOAA-21 | SANTANA DO MARANHÃO | MARANHÃO | Brasil | 2110237 | 21 | 33 | nan | nan | nan | Cerrado | 33.9 |
| 896bb4b7-5526-355d-a102-e05d2d839439 | -7.18476 | -39.36051 | 2026-09-21 16:03:00 | NOAA-21 | JUAZEIRO DO NORTE | CEARÁ | Brasil | 2307304 | 23 | 33 | nan | nan | nan | Caatinga | 34.4 |
| 15634f84-b891-3738-b433-b9c560d38cc7 | -7.75555 | -43.89227 | 2026-09-21 16:03:00 | NOAA-21 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 50d65a7d-93f0-3b3e-8cfc-3b93a40f7606 | -8.61899 | -47.29987 | 2026-09-21 16:03:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 7.8 |
| e478ee45-bc51-3f3f-b3b5-f8c207772105 | -5.66193 | -42.64055 | 2026-09-21 16:03:00 | NOAA-21 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 6.3 |
| 6f1679a5-7b6f-3ebb-9976-8d4900978938 | -7.25194 | -44.05551 | 2026-09-21 16:03:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 7.4 |
| fd0bd310-4bbb-30e8-8a01-83b1280ce567 | -7.57785 | -46.3695 | 2026-09-21 16:03:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 0e57cec4-d083-36ad-82f5-226f8b13a6d7 | -5.14355 | -37.33443 | 2026-09-21 16:03:00 | NOAA-21 | MOSSORÓ | RIO GRANDE DO NORTE | Brasil | 2408003 | 24 | 33 | nan | nan | nan | Caatinga | 7.5 |
| 075a7de7-7f66-3748-b3e6-e3980686bff5 | -7.51794 | -46.22075 | 2026-09-21 16:03:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 76cc0ec5-02c0-38b3-9ccb-9ff137fc7c88 | -5.82585 | -43.86414 | 2026-09-21 16:03:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 22.5 |


[Clique aqui para ver as próximas entradas](README165.md)
