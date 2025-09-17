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

## Dados Diários - Página 41

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 50ee7c65-c6c2-3823-8975-72db8e7d085a | -9.54164 | -46.2956 | 2025-09-17 04:32:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 69e9974f-b74f-362a-ab4a-5c211d8c5de8 | -3.27475 | -52.42281 | 2025-09-17 04:32:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2fbed73e-4849-3c66-b745-3a909e95f528 | -4.92129 | -47.86448 | 2025-09-17 04:32:00 | NOAA-20 | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 3.8 |
| e5ed19c8-6679-335b-bc96-78727786e008 | -8.13393 | -43.64486 | 2025-09-17 04:32:00 | NOAA-20 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3a4b4232-a5a1-362f-b70a-c42bb8e51290 | -5.8896 | -45.73645 | 2025-09-17 04:32:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 18ac19fb-0d40-302a-b00f-24ed2f237ad9 | -9.72303 | -47.40414 | 2025-09-17 04:32:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a23959a4-4f3c-37a3-aab3-3b957e92b0ac | -6.36356 | -44.40546 | 2025-09-17 04:32:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3b9fe25e-3d58-3f56-98a8-0fccb24fb707 | -9.59246 | -45.66482 | 2025-09-17 04:32:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 567a4870-dfd0-3189-9aee-2ffc4148695a | -7.4824 | -47.38843 | 2025-09-17 04:32:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 31beafa2-cdbd-3f34-a870-e08b63716742 | -7.58884 | -44.58043 | 2025-09-17 04:32:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| eeb05346-d2d2-3433-81aa-a936a66363c2 | -8.3485 | -44.72197 | 2025-09-17 04:32:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 92fe0fab-f390-3675-a57c-ca1af781f89f | -8.63145 | -46.43888 | 2025-09-17 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 11f2621d-0b51-353a-a712-91a5f5982367 | -9.11703 | -44.87155 | 2025-09-17 04:32:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3f302538-a1fe-367c-ae58-746e3ae7c1d0 | -5.44731 | -46.67668 | 2025-09-17 04:32:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f37a53a1-3e03-34a1-aaeb-89239718c0cb | -8.00243 | -45.69123 | 2025-09-17 04:32:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 396ba69c-970d-3cca-9fae-31c93235e881 | -8.76336 | -46.15009 | 2025-09-17 04:32:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 994c4d4d-34f1-377f-850a-ff02891a2501 | -8.66115 | -46.40503 | 2025-09-17 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 56a9ff46-6d3b-3701-bf31-d8f6c2f63f8e | -11.02458 | -45.06459 | 2025-09-17 04:32:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 24488f43-6a9e-338c-a18d-e746ab8ec2d2 | -8.01531 | -45.65311 | 2025-09-17 04:32:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1d143a63-c120-3871-bed4-60b767a5ef54 | -10.40408 | -50.64393 | 2025-09-17 04:32:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 55a1cc40-f8cf-333e-b7f9-4112f3ba18ca | -2.70676 | -54.95404 | 2025-09-17 04:32:00 | NOAA-20 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| a80a71d7-5f96-3bbd-b43c-25c3eb8a4362 | -6.39606 | -43.34265 | 2025-09-17 04:32:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 7396832a-9b0a-31a2-b23d-5e396219548a | -8.47366 | -44.72817 | 2025-09-17 04:32:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 64ce9bf8-c964-36b2-b463-980fc9623f0a | -2.71168 | -54.95488 | 2025-09-17 04:32:00 | NOAA-20 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 6441e7ca-4148-3df0-a2ee-c11ee9483e98 | -8.63315 | -46.42783 | 2025-09-17 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| adaf3553-ee7c-3a01-9bfc-368cb10fb22d | -5.61701 | -51.72446 | 2025-09-17 04:32:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 28ed94ee-f60b-3865-b7c2-fb6a3294af72 | -5.78711 | -43.93983 | 2025-09-17 04:32:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f4424c29-d397-3030-b967-e8d4b45f0609 | -7.72516 | -45.29853 | 2025-09-17 04:32:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9e89ab1a-97c2-37dd-adb1-cee40acfad46 | -7.0873 | -49.74898 | 2025-09-17 04:32:00 | NOAA-20 | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3de09dfd-c3cd-37a1-afec-28cd3c2f9ba0 | -7.34067 | -44.59014 | 2025-09-17 04:32:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6707682e-fd56-37c2-9984-c0b2faa57e95 | -6.41535 | -44.3603 | 2025-09-17 04:32:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c86dbaa8-a528-3718-80a3-32c82a63da16 | -6.19778 | -45.12285 | 2025-09-17 04:32:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 7.8 |
| c24d945b-cab7-3002-94c9-e4e413c0be7a | -6.20958 | -43.90767 | 2025-09-17 04:32:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e445db9f-d70c-3ed3-92be-5ec9ac2c9d34 | -9.17369 | -46.94297 | 2025-09-17 04:32:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| a4e34498-7a1a-36a9-b15e-d4fa0cc568ed | -6.15613 | -45.11206 | 2025-09-17 04:32:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 384bbcc8-c2c3-3330-853f-1ae785f4a625 | -6.22838 | -42.02566 | 2025-09-17 04:32:00 | NOAA-20 | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| a03b3e87-90fb-3c76-9673-55419b8b2533 | -5.76849 | -45.90773 | 2025-09-17 04:32:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| a7fc7fae-5413-3bcb-a6bc-a11342082b7e | -7.57003 | -44.55535 | 2025-09-17 04:32:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 9056e8f5-ce94-3b25-bffd-f5c943bf3536 | -7.00242 | -44.5796 | 2025-09-17 04:32:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1cbdfaf3-b54d-327e-8624-ed9dcde96a97 | -11.20859 | -47.67109 | 2025-09-17 04:32:00 | NOAA-20 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 82458fcc-f2ec-3b89-a576-1de3073dd4a1 | -8.89879 | -46.14993 | 2025-09-17 04:32:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 097176af-4f98-3506-a78a-b4bc5316d750 | -3.80047 | -48.6366 | 2025-09-17 04:32:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 86586ec3-7269-3768-8a5a-90579501b6c7 | -9.05679 | -44.87757 | 2025-09-17 04:32:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a1640c64-c08d-3340-be15-01add0cf595f | -7.17206 | -44.34552 | 2025-09-17 04:32:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4e2e73a4-82ab-3c89-bc9c-1e82250db6dd | -10.67905 | -46.5201 | 2025-09-17 04:32:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 40eec495-4c63-383c-93f2-2adf42a0b633 | -7.41072 | -49.98301 | 2025-09-17 04:32:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 062db642-c3fc-30ff-85f4-9eb8180eaaaf | -8.63321 | -46.42763 | 2025-09-17 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 01c8e485-4f74-348d-aba0-9afdad3675e0 | -5.92551 | -47.29063 | 2025-09-17 04:32:00 | NOAA-20 | RIBAMAR FIQUENE | MARANHÃO | Brasil | 2109551 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 9be3a784-2a46-3b23-ac85-359952273e0d | -7.97194 | -45.62715 | 2025-09-17 04:32:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 412efc2c-03cd-3605-93f7-7687e033bb58 | -8.98639 | -46.24114 | 2025-09-17 04:32:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ab50037d-9809-34fa-a680-98ed13321679 | -8.1572 | -46.75092 | 2025-09-17 04:32:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 68ef71a8-179c-384a-ae64-9df7f98f79ee | -7.97467 | -45.67965 | 2025-09-17 04:32:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 9ca3d089-b835-349b-b2f5-9dde3a625ffc | -8.56185 | -46.367 | 2025-09-17 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 35016658-5805-3d7c-8ec5-b5f0cac3e9f5 | -7.65545 | -44.48125 | 2025-09-17 04:32:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 33f002bc-e042-34d3-be65-950dd3e95b63 | -5.79219 | -43.46765 | 2025-09-17 04:32:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d47c1aac-7a4e-314b-b7b1-a20cd7bcb389 | -7.38033 | -49.99725 | 2025-09-17 04:32:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a9c556a7-7ae6-3047-ac63-38be4ed0c539 | -8.96833 | -46.01836 | 2025-09-17 04:32:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a52e5dec-f654-3e2a-9373-b5273a6a1298 | -7.8266 | -46.13948 | 2025-09-17 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| cfe5c4f3-e7d2-3b07-a4d7-f2e064ca37fa | -8.6321 | -46.43501 | 2025-09-17 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| b54e92f4-9525-3d2f-b5d7-a5c48e3845bc | -5.32408 | -44.99656 | 2025-09-17 04:32:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e82bcad2-649d-3c9f-b5fa-d1be27a6f83e | -8.96603 | -46.01001 | 2025-09-17 04:32:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 080f1adf-fc35-3a7c-8a39-32ff0a203897 | -6.92542 | -44.76448 | 2025-09-17 04:32:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 16917d1e-fa25-3451-aa3a-94d688b26666 | -8.90402 | -46.27984 | 2025-09-17 04:32:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| c4c6436d-c3de-353f-a876-fce9071d1bd2 | -6.98203 | -44.61619 | 2025-09-17 04:32:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d7d7e0e5-b0b9-346f-93cf-189f46b46fb6 | -9.54799 | -46.30054 | 2025-09-17 04:32:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 796a399b-9970-3a7d-99a4-58ef0a86001e | -5.54196 | -44.96687 | 2025-09-17 04:32:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 078d60cf-a5ee-3e64-8d2d-e04282976e86 | -8.61987 | -45.71615 | 2025-09-17 04:32:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b9c3dba6-4377-3d4d-80bb-7c16f870bb75 | -7.04342 | -46.31728 | 2025-09-17 04:32:00 | NOAA-20 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d351e4de-35d5-3041-aa79-eb5bf8bdafd1 | -10.3997 | -50.62779 | 2025-09-17 04:32:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ce3b5520-b0fa-3482-9acb-1d788ff9daba | -10.6329 | -48.75441 | 2025-09-17 04:32:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| df3a58d0-b6e0-38db-96d6-19dfd3bfcf91 | -5.43149 | -47.53873 | 2025-09-17 04:32:00 | NOAA-20 | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0f6750bf-08fd-359f-a69f-8867e9e7a839 | -7.83173 | -46.10557 | 2025-09-17 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d66d10fc-0243-3d62-8666-676930ac1772 | -7.83553 | -43.8556 | 2025-09-17 04:32:00 | NOAA-20 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a174cd25-f284-3858-b194-cdca92a6be5a | -9.83093 | -49.9656 | 2025-09-17 04:32:00 | NOAA-20 | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| adb3f50a-3a67-3d1e-be74-be13221fab86 | -6.17273 | -44.50615 | 2025-09-17 04:32:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a1b2a996-aa7f-3776-8a4e-ec5150cea2ce | -6.39875 | -43.35516 | 2025-09-17 04:32:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 91f6b565-652d-3f83-8e1e-dadbb820b335 | -9.11156 | -44.85733 | 2025-09-17 04:32:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3ff366b7-5587-3c66-8f9f-2bb5346797b2 | -6.40805 | -42.66222 | 2025-09-17 04:32:00 | NOAA-20 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 43b8a386-da20-3f2c-b786-f9338b9eb01a | -5.78777 | -43.9354 | 2025-09-17 04:32:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| d379833a-74e4-3052-9fd8-8dd064535880 | -7.41415 | -49.98357 | 2025-09-17 04:32:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4743de91-5875-3290-8b37-c6d37b0ab554 | -10.80852 | -50.65987 | 2025-09-17 04:32:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1cf5eb3f-6420-3199-94a7-f2e7f2f4e22d | -7.20878 | -44.37838 | 2025-09-17 04:32:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 18db065d-4532-3706-9c06-8df5277a494f | -6.35175 | -43.15786 | 2025-09-17 04:32:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 4b8e0bc3-b06e-3eaf-b833-92a8478eeb0c | -6.24642 | -43.4576 | 2025-09-17 04:32:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 769875fd-190e-351f-8ab2-b935cbe28c4e | -6.93269 | -44.76535 | 2025-09-17 04:32:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e929b460-ccf6-3e35-b845-c95da558785a | -9.75984 | -47.34373 | 2025-09-17 04:32:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 4204c4ec-5a18-33d7-a3ee-24c46f7880bb | -6.24255 | -43.45711 | 2025-09-17 04:32:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 085c2b41-492d-3066-a492-aa3321da0f2e | -7.58149 | -44.57931 | 2025-09-17 04:32:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 255bf853-9546-3415-82a9-4af0dc3f8a5a | -6.95406 | -42.44126 | 2025-09-17 04:32:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 36ac1d49-1813-3d74-8aaa-9742585746c0 | -6.93343 | -44.7686 | 2025-09-17 04:32:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ed1dedba-b347-322e-8141-75cfffa4615e | -6.5183 | -51.19827 | 2025-09-17 04:32:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d9596966-c1cd-32e9-a9d7-dd0584460b7e | -4.05484 | -47.50115 | 2025-09-17 04:32:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 10.5 |
| d94c84b7-22ca-372c-bee1-120e8f713074 | -8.98564 | -45.76004 | 2025-09-17 04:32:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cde3186a-1283-3c0c-bd63-f2a6f0b612d0 | -11.49326 | -43.61484 | 2025-09-17 04:32:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 0654fcff-e752-3250-8f6e-29f96d5da30c | -7.53026 | -44.72088 | 2025-09-17 04:32:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| cd424ceb-ad36-302c-9ab7-41bacdc60948 | -8.29828 | -47.98823 | 2025-09-17 04:32:00 | NOAA-20 | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c4ed0c83-baa7-3bae-9652-061a1e51385f | -7.86192 | -48.17165 | 2025-09-17 04:32:00 | NOAA-20 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 968a38fb-6799-3a0c-8952-bb2102544232 | -5.52209 | -42.1893 | 2025-09-17 04:32:00 | NOAA-20 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 9c43329e-adb5-33e9-9cf6-b15db72782da | -7.38941 | -50.00635 | 2025-09-17 04:32:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 880ec2ee-93f6-37d0-b729-8e8f977998a3 | -4.5756 | -48.5244 | 2025-09-17 04:32:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |


[Clique aqui para ver as próximas entradas](README42.md)
