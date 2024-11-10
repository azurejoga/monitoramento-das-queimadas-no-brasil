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

## Dados Diários - Página 25

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 959ec2e4-9e26-312c-ba71-83e5a5c38ead | -2.17083 | -46.40907 | 2024-11-10 04:14:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c86c0eb5-e4b8-321b-a2e4-7ea107acd254 | -3.95144 | -48.15534 | 2024-11-10 04:14:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| a298e98f-cbea-350f-bab5-c0d0fed1130b | -2.73316 | -49.02288 | 2024-11-10 04:14:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ed29b122-0456-3148-b562-93d44b30b92e | -2.52853 | -46.30839 | 2024-11-10 04:14:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1174c62c-4c15-30c5-a3bf-aa000348bb88 | -2.47182 | -50.23421 | 2024-11-10 04:14:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 76eae874-d0b2-318b-9ec6-f47a1ae7f303 | -3.62465 | -50.61911 | 2024-11-10 04:14:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 6d3fb706-f0c3-3b35-b730-28e0a4b1ab3d | -4.20736 | -47.87073 | 2024-11-10 04:14:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a6d5b6c8-bff4-35bf-b359-4264ae5449ba | -2.08856 | -48.83127 | 2024-11-10 04:14:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 1592138c-42e8-3e6c-8bac-9eb7013300e2 | -2.15962 | -48.06934 | 2024-11-10 04:14:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 68929441-b4a5-3f8c-abb4-420b876b6476 | -6.2282 | -42.91949 | 2024-11-10 04:14:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d5989208-a5f0-3788-be7e-3ca0cc083679 | -1.53004 | -52.20047 | 2024-11-10 04:14:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 46d9ca07-46e5-332a-8215-bdc61539a182 | -3.22878 | -50.25986 | 2024-11-10 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 5ad46510-593c-3da4-b1cd-776fa233dc53 | -4.90602 | -45.86445 | 2024-11-10 04:14:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d4947deb-bf1c-3fdf-8dae-f861d9a9cfb2 | -2.92758 | -51.48302 | 2024-11-10 04:14:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| dc4e0851-a71a-37a8-a951-351502cb1494 | -2.12813 | -46.38572 | 2024-11-10 04:14:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d8a81f2f-dc66-3f6d-bf8b-710ac4f96216 | -3.23192 | -50.27113 | 2024-11-10 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| fdc31e36-6f3c-3c1a-ad86-f3491d5a667d | -2.37224 | -46.85691 | 2024-11-10 04:14:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3aa098e5-9dbb-3af2-bd0f-682b7aba7e62 | -3.24802 | -48.74494 | 2024-11-10 04:14:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3be8f2ab-9bdb-37de-903b-27df07375fa3 | -4.51927 | -42.88366 | 2024-11-10 04:14:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7e9f0a8d-0ab4-3669-8710-0606ef6d5b6d | -4.51902 | -45.69888 | 2024-11-10 04:14:00 | NOAA-21 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 481b747c-0fac-3ca5-902b-f8cfde17af61 | -2.2495 | -53.66763 | 2024-11-10 04:14:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d9543c59-5a68-360f-bf6a-daf98b4b7656 | -3.25741 | -48.74213 | 2024-11-10 04:14:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 25e2a64b-30ad-3bb6-a3a3-4397bf8323cf | -3.07473 | -50.57584 | 2024-11-10 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bc297300-77b4-37d5-a431-1eb50b5c68e6 | -4.28051 | -48.18804 | 2024-11-10 04:14:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 57eb8ab1-8691-30e4-ac9c-46d18fa86cf8 | -4.13176 | -46.84327 | 2024-11-10 04:14:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f7e735a9-4d9a-3754-b692-d068d918267f | -4.86452 | -49.97813 | 2024-11-10 04:14:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| fba42e39-faeb-350b-9dbe-b80f92db7ff7 | -4.8475 | -48.64676 | 2024-11-10 04:14:00 | NOAA-21 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| f7a7c79d-1157-301a-bcd4-0be9c34b8b0c | -2.3668 | -46.8661 | 2024-11-10 04:14:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| bf7741f0-068d-32a7-87fa-6ba1fba4138a | -3.48934 | -54.5863 | 2024-11-10 04:14:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4f6d0b38-b351-30b9-95b0-40567e365054 | -2.45202 | -47.16107 | 2024-11-10 04:14:00 | NOAA-21 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| ee56245e-199a-33ef-94fd-795f1b4b1f9a | -3.21451 | -50.37864 | 2024-11-10 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 34cb2b87-62bd-3bc1-9625-57c4a97282a8 | -4.38559 | -47.27278 | 2024-11-10 04:14:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 4.1 |
| af1d5e2c-8d3d-3c45-ae41-ccf8934a2f5e | -2.07073 | -48.62729 | 2024-11-10 04:14:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8195066b-5843-3cc9-bb7d-17d66350e3af | -4.28525 | -48.18499 | 2024-11-10 04:14:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e79c21e3-0288-3a9b-8053-50b04c1d6464 | -2.50805 | -49.88723 | 2024-11-10 04:14:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| df2bd428-3df2-33fa-a5d4-0c8cf8ab29e7 | -5.53275 | -41.6975 | 2024-11-10 04:14:00 | NOAA-21 | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 5b77a3b8-4192-3785-bb0e-26bc6636718e | -4.2799 | -48.19175 | 2024-11-10 04:14:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 6bd83e29-39ce-329c-a839-06bb4abf3d55 | -2.93212 | -52.77171 | 2024-11-10 04:14:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 28.7 |
| 7eb8b2ea-e6b2-3d66-aab1-29c25e269d4b | -3.23158 | -50.30399 | 2024-11-10 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7dd998f6-bcad-388e-936f-f74e3f3f36f2 | -2.4598 | -53.68996 | 2024-11-10 04:14:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9b3c634c-3d08-302e-a782-c56bf06b9fe7 | -2.6045 | -48.18943 | 2024-11-10 04:14:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f902f376-8fe0-3c78-aa5b-03f877c4c682 | -2.79981 | -45.97092 | 2024-11-10 04:14:00 | NOAA-21 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b7755d69-e245-3e15-aaa3-db6c354149fc | -2.29073 | -48.55021 | 2024-11-10 04:14:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e4c96241-3093-3dd6-906c-a96240854cee | -2.85325 | -48.44872 | 2024-11-10 04:14:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 80235ea0-519c-3760-88f6-71f7ac1dc13d | -3.95665 | -48.17535 | 2024-11-10 04:14:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 13.1 |
| dbec3512-1a87-334b-94a5-146a828ad487 | -2.62656 | -46.77184 | 2024-11-10 04:14:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 16.9 |
| 091efe99-dfcb-3562-97cc-ea78d56cdf90 | -3.12585 | -50.44675 | 2024-11-10 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 51.7 |
| 287bb8a8-2977-324c-831c-1b71ff37d2ae | -3.22586 | -50.30857 | 2024-11-10 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| c2710a5b-6318-3258-862a-d614ab7311b1 | -3.90033 | -51.91985 | 2024-11-10 04:14:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 27c7e790-91f5-346b-bb12-3b784f05501f | -6.73519 | -40.81654 | 2024-11-10 04:14:00 | NOAA-21 | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 009cce59-c7ca-3445-9fc6-a1d1d2f894c4 | -2.26672 | -51.89169 | 2024-11-10 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 51ce242f-52cc-366a-8651-0bf1fe24b6c8 | -3.04001 | -50.32681 | 2024-11-10 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 1763c8e5-5fd5-3333-aee7-ec8d5bb80925 | -5.21112 | -48.34397 | 2024-11-10 04:14:00 | NOAA-21 | SÃO SEBASTIÃO DO TOCANTINS | TOCANTINS | Brasil | 1720309 | 17 | 33 | nan | nan | nan | Amazônia | 6.7 |
| e73596b5-22af-397f-b6bb-0e00cf643be8 | -2.12032 | -50.15526 | 2024-11-10 04:14:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b0c8003a-2d3a-3d0c-aba0-5219eaba5d6c | -1.87479 | -50.78941 | 2024-11-10 04:14:00 | NOAA-21 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 445c8680-e842-3f48-b7bd-dd4b2da302c2 | -5.45155 | -43.27387 | 2024-11-10 04:14:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0da70b32-3cdc-32a9-8cad-f85412d08410 | -5.13587 | -48.2448 | 2024-11-10 04:14:00 | NOAA-21 | SÃO PEDRO DA ÁGUA BRANCA | MARANHÃO | Brasil | 2111532 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| d0e7ccf5-6e31-36dd-a2e0-f712cf6b709a | -3.46529 | -50.19529 | 2024-11-10 04:14:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 390f838b-fe91-33fa-840e-aa10a4b2e0d9 | -2.14771 | -50.4584 | 2024-11-10 04:14:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 353d4ae4-486f-32df-8b74-c427df046402 | -4.07133 | -50.0145 | 2024-11-10 04:14:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 0c0269df-f489-30f1-8334-da2098242d78 | -2.92282 | -51.47895 | 2024-11-10 04:14:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 12.6 |
| ae5697d5-a0db-3865-8be2-bf331fb37b1e | -2.88843 | -45.36893 | 2024-11-10 04:14:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 1992c3bf-891d-3f5d-b2fa-84d9243a8c44 | -4.68876 | -49.62197 | 2024-11-10 04:14:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 01f0c5ad-9c55-3ce2-8328-4659eb877d32 | -2.04637 | -46.5316 | 2024-11-10 04:14:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 33aaebc4-31c7-3864-88e0-40d58f6238dc | -4.43389 | -47.25248 | 2024-11-10 04:14:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 10a04b8b-10de-3ccc-94fc-ad9cd56de59e | -3.24298 | -51.23762 | 2024-11-10 04:14:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| d2bd147f-a976-3f58-959c-b134379099d8 | -3.10361 | -49.40672 | 2024-11-10 04:14:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 7d5882d6-5b12-3d64-bdec-6c42719bc98f | -3.99346 | -46.41519 | 2024-11-10 04:14:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.4 |
| c6d4e809-c999-304c-a20b-16d061808b11 | -3.51909 | -44.03038 | 2024-11-10 04:14:00 | NOAA-21 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 01fa9e95-4f1e-327f-aa74-a9db93591dd8 | -3.70213 | -47.63938 | 2024-11-10 04:14:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d4fb9654-1d70-33f3-9fb8-807aa237c032 | -2.11358 | -46.47877 | 2024-11-10 04:14:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| abd3b0db-e6ea-39d0-a27d-090ebc155a7a | -3.01228 | -51.04214 | 2024-11-10 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 807b4244-059b-3e5e-81a2-fea852ffd270 | -2.57085 | -47.34928 | 2024-11-10 04:14:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e2a77cb3-d92d-3171-b1f6-eac56a17b378 | -2.4692 | -50.25053 | 2024-11-10 04:14:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| da438cc3-7a45-3777-aaa4-f77af5a1d784 | -3.22749 | -50.43854 | 2024-11-10 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 79146080-f471-3eaa-a386-4b58234b1518 | -3.84462 | -44.12511 | 2024-11-10 04:14:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ed8258dd-27a2-3f96-aff1-48cf3ee54aba | -5.56688 | -43.97146 | 2024-11-10 04:14:00 | NOAA-21 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| e56837c6-45ca-39d2-b42f-85e6beea24c3 | -2.69241 | -49.8734 | 2024-11-10 04:14:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6a5ad123-85f5-370e-bc30-6904d16e71bb | -3.9502 | -48.16287 | 2024-11-10 04:14:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 15.3 |
| 496e9db2-7f7f-32da-8f64-f0206a816a06 | -2.38251 | -46.59188 | 2024-11-10 04:14:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7604a130-2dd8-378e-89c8-c1c3d4018954 | -5.55668 | -41.65359 | 2024-11-10 04:14:00 | NOAA-21 | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 51925079-8360-35fc-84e0-75380a7df69d | -2.30236 | -46.74615 | 2024-11-10 04:14:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8310dd5e-c51b-3219-94ae-57759da809af | -2.3117 | -46.08906 | 2024-11-10 04:14:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6f8d3a4d-c716-3f68-a963-54ba9ba7261d | -2.92864 | -51.47648 | 2024-11-10 04:14:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 15.5 |
| 4ae70552-e61e-3cd3-8748-2fc69ef5771e | -4.36151 | -47.22433 | 2024-11-10 04:14:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f37efe6b-c296-3961-87e0-616bf6edd03d | -2.26614 | -51.89524 | 2024-11-10 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 7a4e2f13-7aad-34a7-9185-028e680257b8 | -2.36907 | -46.82641 | 2024-11-10 04:14:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ed8243b3-dd9e-3c70-b620-7a7296a64b53 | -2.73836 | -49.01916 | 2024-11-10 04:14:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 8790181a-7c91-3334-b05f-f0c8360e553b | -3.1474 | -45.95533 | 2024-11-10 04:14:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 57dadd44-4527-3958-9426-983478b631a3 | -2.73202 | -51.71722 | 2024-11-10 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c942854a-fa06-390e-95a3-3394b982ee96 | -2.71894 | -51.99969 | 2024-11-10 04:14:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ea3c91a7-8d50-357e-b4cf-b84db2ecbba8 | -3.23747 | -50.29055 | 2024-11-10 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 2c4ba36b-ea4b-396a-b95f-fcdbadde0d5b | -3.25842 | -53.70253 | 2024-11-10 04:14:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0e1847d7-c5b6-3821-a1a8-cc06e1cffa60 | -2.62346 | -46.76639 | 2024-11-10 04:14:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| a4d1cd78-fee5-3c0a-b810-e3d72f898ad4 | -2.46079 | -46.31837 | 2024-11-10 04:14:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 35c05e71-144f-3932-b7ca-237d1ac9bd4b | -3.22933 | -50.28712 | 2024-11-10 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 19389b99-fc72-3ad3-b97d-53dac0b6d82f | -3.09372 | -51.29395 | 2024-11-10 04:14:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6668edc4-a052-3375-82ac-86374337977b | -1.67355 | -52.05407 | 2024-11-10 04:14:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 352c96f5-3ab7-371e-9c2c-5fde564c1f9a | -2.93794 | -52.77798 | 2024-11-10 04:14:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 25.6 |
| 4587c9a8-8f2c-3fc2-ae56-d13df7f7be96 | -0.458 | -52.02832 | 2024-11-10 04:14:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 0.7 |


[Clique aqui para ver as próximas entradas](README26.md)
