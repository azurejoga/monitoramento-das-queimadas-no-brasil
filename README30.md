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

## Dados Diários - Página 30

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3e66a5a7-d80d-3e8e-94e6-4422b4c99857 | 4.4618 | -60.9842 | 2024-12-17 05:50:00 | GOES-16 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 105.6 |
| 09eabe4a-9ca5-3d3c-b6d6-eb29de04a7ce | 4.4435 | -60.9657 | 2024-12-17 05:50:00 | GOES-16 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 67.0 |
| ecee4c9c-5f06-39f2-9657-faa61af52a01 | 4.4434 | -61.0036 | 2024-12-17 05:50:00 | GOES-16 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 72.4 |
| d45c43da-e0dd-305a-b4e6-889c88531529 | -6.214 | -46.2202 | 2024-12-17 05:50:00 | GOES-16 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 50.3 |
| 5edc4588-a13c-3f1d-96d7-c1abf00eeb9e | 4.4435 | -60.9846 | 2024-12-17 05:50:00 | GOES-16 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 191.2 |
| 709f20fd-5406-30f5-ade4-90808e6847f1 | -6.214 | -46.2202 | 2024-12-17 06:00:00 | GOES-16 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 51.4 |
| 4d9ca7e6-2915-33da-9a81-4c2872e9580a | 4.4435 | -60.9846 | 2024-12-17 06:00:00 | GOES-16 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 133.6 |
| 4e1b5a9f-22d5-3857-b293-649c135d15d1 | 4.4435 | -60.9657 | 2024-12-17 06:00:00 | GOES-16 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 57.9 |
| 9d5f46fd-9f1b-3527-8787-a0597d2b04ae | 4.4618 | -60.9842 | 2024-12-17 06:00:00 | GOES-16 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 75.5 |
| 31f93e8a-8ba4-32dd-9359-48fa605e44c5 | -6.9349 | -43.4934 | 2024-12-17 06:00:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 56.2 |
| 1e36f715-83e4-363d-b128-200c2be1e078 | -6.9346 | -43.5168 | 2024-12-17 06:00:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 59.3 |
| 5eb15880-0e2c-3c5f-b60a-06c2c9c122ce | 4.43831 | -60.97501 | 2024-12-17 06:01:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 09bc6682-2a56-3a37-bd2c-5909f1ccda7d | 4.43607 | -60.98984 | 2024-12-17 06:01:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 20.3 |
| 786b4fc6-7356-35e8-b9ec-a4c1d98bb4c8 | 4.44067 | -60.98947 | 2024-12-17 06:01:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 20.3 |
| 51af77f5-c8a0-3825-8062-0e731de5dab2 | 4.44979 | -60.98825 | 2024-12-17 06:01:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 15.8 |
| 9bb58e7b-6ce0-3cd3-a4f1-74e18d2cce50 | 4.45281 | -60.97813 | 2024-12-17 06:01:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 3.1 |
| df82583a-e1a9-3c1f-ac62-73611b8d1a5f | 3.31959 | -60.63052 | 2024-12-17 06:01:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b0afbd20-9641-388a-867a-9e10d2e0fa15 | 4.45631 | -60.9655 | 2024-12-17 06:01:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 2.5 |
| acfc56c1-244c-3ac0-8bc0-0804af184447 | 4.45789 | -60.97478 | 2024-12-17 06:01:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c3e676bc-6881-3f5b-a017-e040fbac9f91 | 4.45553 | -60.96086 | 2024-12-17 06:01:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 21d6bedf-f424-392e-99be-d43cd3422fb3 | 4.44134 | -60.96496 | 2024-12-17 06:01:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 85dece5e-134d-3160-b1af-be6c9f350b1b | 4.44901 | -60.98343 | 2024-12-17 06:01:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 15.8 |
| 49b3622b-a8e1-3392-a590-cba1255b8e2f | 4.44434 | -60.95463 | 2024-12-17 06:01:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 892a0918-9d4c-3ed4-98fe-118045b39bbe | 4.45727 | -60.9768 | 2024-12-17 06:01:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 3.1 |
| e549db91-9f19-3eb9-927b-c94552d2d7bc | 4.43989 | -60.98471 | 2024-12-17 06:01:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 20.3 |
| fc162b03-1316-3236-bc16-332e93fbf824 | 4.44058 | -60.96027 | 2024-12-17 06:01:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 25ec9a49-2d74-38bf-82db-36a63d7bef79 | 3.32033 | -60.62918 | 2024-12-17 06:01:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 2.8 |
| a0d8f05c-1f64-34c5-9a84-3f89b8411bc8 | 4.43979 | -60.95544 | 2024-12-17 06:01:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 6b0edaa2-d0cb-3385-81c5-427e8e4b8e9c | -6.99287 | -71.11862 | 2024-12-17 06:01:00 | NOAA-21 | IPIXUNA | AMAZONAS | Brasil | 1301803 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 045685d5-fc69-3f74-8351-aaad27d5c57e | 4.44444 | -60.98404 | 2024-12-17 06:01:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 15.8 |
| b26cc88f-23a0-317d-81aa-f4d078f1eaad | 4.45652 | -60.9722 | 2024-12-17 06:01:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 3.1 |
| bec2dadd-0e11-3485-94ae-a6fa864251f5 | 4.45358 | -60.98285 | 2024-12-17 06:01:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 58.6 |
| 55e94600-6a8e-3091-82d1-e315d6eea07b | 4.43521 | -60.95596 | 2024-12-17 06:01:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f725672d-50ec-3e59-a328-891cfae8ae4f | 4.45203 | -60.97329 | 2024-12-17 06:01:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 3.1 |
| ab4a146c-0892-38ee-9969-4ad9e9536e80 | 4.43678 | -60.96561 | 2024-12-17 06:01:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 5ff5e974-83af-3904-8404-9474d9e27a0e | 4.44523 | -60.98889 | 2024-12-17 06:01:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 15.8 |
| 9287c1da-7a71-38d0-8d6a-6f0979500b22 | 4.44822 | -60.97858 | 2024-12-17 06:01:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 957ede20-299b-3271-9b8d-8c60ec0d044f | 4.43601 | -60.96089 | 2024-12-17 06:01:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d313f501-e450-342b-8fbb-0829ee144139 | -9.30061 | -69.43892 | 2024-12-17 06:03:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 47e215fd-06a4-300a-84f3-7ba438553020 | 4.44134 | -60.99621 | 2024-12-17 06:07:00 | AQUA_M-M | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 17.3 |
| 9c4c2a96-d80d-3218-be5c-9ef09038f270 | 4.43887 | -60.97871 | 2024-12-17 06:07:00 | AQUA_M-M | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 24.7 |
| 8f290af8-eb31-3866-bd7f-dd835462f3b9 | 4.45114 | -60.97652 | 2024-12-17 06:07:00 | AQUA_M-M | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 125.6 |
| aeb3690a-d5e7-352c-a243-ff84f7502447 | 4.45368 | -60.99437 | 2024-12-17 06:07:00 | AQUA_M-M | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 32.6 |
| 6abe3119-289f-3623-8ebf-073691f2af3e | 4.4637 | -60.97635 | 2024-12-17 06:07:00 | AQUA_M-M | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 52.5 |
| c87863a2-a193-3cc7-b36c-223a52181665 | -3.14703 | -53.17472 | 2024-12-17 06:09:00 | AQUA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 1794ef97-8fec-303c-8897-e486a7a8103e | -1.37178 | -53.47234 | 2024-12-17 06:09:00 | AQUA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| cb4c34d9-95e4-32b6-b758-2f964a8e9463 | 4.4435 | -60.9846 | 2024-12-17 06:10:00 | GOES-16 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 151.6 |
| 85c2f5a2-eb94-3deb-932f-3468d51b0f85 | 4.4618 | -60.9842 | 2024-12-17 06:10:00 | GOES-16 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 87.4 |
| 6d401981-b434-3c93-8338-08a7e8a6d8cb | 4.4435 | -60.9657 | 2024-12-17 06:10:00 | GOES-16 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 66.7 |
| bee792e2-d664-3fd3-a12c-b80515142c13 | 4.4434 | -61.0036 | 2024-12-17 06:10:00 | GOES-16 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 66.3 |
| 58046e78-95b0-3c21-99f0-f66a8d00d44c | -6.214 | -46.2202 | 2024-12-17 06:10:00 | GOES-16 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 52.3 |
| 0a0faeec-3688-393a-836b-c22749767de5 | -19.09315 | -52.85981 | 2024-12-17 06:14:00 | AQUA_M-M | CHAPADÃO DO SUL | MATO GROSSO DO SUL | Brasil | 5002951 | 50 | 33 | nan | nan | nan | Cerrado | 46.0 |
| 59c9901d-e00d-3176-ab19-fa59f8cc24b2 | -18.88961 | -56.04642 | 2024-12-17 06:14:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 9.8 |
| 6ad1b74f-911f-36f7-b0b0-954e57976c52 | -18.89688 | -56.0394 | 2024-12-17 06:14:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 14.9 |
| 436d9a0e-fdd0-319c-afae-f37194b73336 | -18.89522 | -56.05285 | 2024-12-17 06:14:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 12.8 |
| 2d1b55a2-8da7-3a39-9ca6-e95a3e9ae53e | -18.90014 | -56.04786 | 2024-12-17 06:14:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 13.6 |
| 59f23bf6-1569-398b-8994-84501f80f0b8 | -19.08839 | -52.86451 | 2024-12-17 06:14:00 | AQUA_M-M | CHAPADÃO DO SUL | MATO GROSSO DO SUL | Brasil | 5002951 | 50 | 33 | nan | nan | nan | Cerrado | 40.5 |
| 747a380a-07bd-3c9c-9ac5-eb0dfb127695 | -19.09088 | -52.84085 | 2024-12-17 06:14:00 | AQUA_M-M | CHAPADÃO DO SUL | MATO GROSSO DO SUL | Brasil | 5002951 | 50 | 33 | nan | nan | nan | Cerrado | 31.8 |
| 2403c62a-1439-3700-bece-2d4e6c822617 | 4.4618 | -60.9842 | 2024-12-17 06:20:00 | GOES-16 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 94.2 |
| 9b0c18a1-f0d2-3819-b4d8-a9ea371248ab | 4.4434 | -61.0036 | 2024-12-17 06:20:00 | GOES-16 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 71.6 |
| 4d95ead0-db3a-3cdf-8db1-ba352ff5bb5c | -6.214 | -46.2202 | 2024-12-17 06:20:00 | GOES-16 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 50.7 |
| 2f0b71de-ace8-397d-abbd-cb4d8d9e90db | -6.9349 | -43.4934 | 2024-12-17 06:20:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 76.6 |
| 8cebb2ed-b983-339d-9d6b-676009dc9911 | -6.9346 | -43.5168 | 2024-12-17 06:20:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 80.8 |
| ca20a2bd-3e42-3713-bfc9-e0ba7cc313ef | 4.4435 | -60.9657 | 2024-12-17 06:20:00 | GOES-16 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 63.9 |
| d6afd423-dae8-369c-96e9-bd71563f315f | 4.4435 | -60.9846 | 2024-12-17 06:20:00 | GOES-16 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 160.5 |
| 32daa608-ecc2-3878-bcb1-12e3693794f3 | 4.45616 | -60.97179 | 2024-12-17 06:22:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 09b10ba1-73b1-316e-94fe-ce1e152b978b | 4.44492 | -60.98746 | 2024-12-17 06:22:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 48.8 |
| 1966a5b0-bab5-31d2-baa2-33e967b743ed | 4.45829 | -60.98357 | 2024-12-17 06:22:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 9.8 |
| c5283acb-3a3a-355f-bed8-85955f889fc3 | 4.44614 | -60.99417 | 2024-12-17 06:22:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 48.8 |
| 3c98c5dd-2e39-3584-9f54-b8338822fbd1 | 4.44937 | -60.97319 | 2024-12-17 06:22:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 16.5 |
| 4881dd55-77b8-3afd-8fb6-ba89a0006782 | 4.45545 | -60.96826 | 2024-12-17 06:22:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 6.8 |
| a69d38fc-6627-3a20-a083-36f529cf7e06 | 4.44012 | -60.96103 | 2024-12-17 06:22:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 82b2b856-b2a8-3c57-9785-99a674d05dc2 | 4.45301 | -60.99324 | 2024-12-17 06:22:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 48.8 |
| 5cfd47ea-902f-36cc-83db-5f0214c85b82 | 4.44572 | -60.95301 | 2024-12-17 06:22:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5576a1dc-3d30-3333-8dd9-9979faf7a2d6 | 4.43944 | -60.95723 | 2024-12-17 06:22:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 25d97fb8-265a-3711-a748-5413da72b805 | 4.438 | -60.9881 | 2024-12-17 06:22:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 8eece1eb-b32b-3d45-b737-c1f81a875af0 | 4.44526 | -60.99052 | 2024-12-17 06:22:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 10.7 |
| e2fdd737-a6bf-34bb-8e55-b8d837870250 | 4.45062 | -60.98005 | 2024-12-17 06:22:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 16.5 |
| 23493ed5-cd93-386d-a464-3583f3421c2d | 4.4383 | -60.99094 | 2024-12-17 06:22:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 540957e3-aaf1-3751-8fb2-8d1d280da2ac | 4.45099 | -60.98306 | 2024-12-17 06:22:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 46.2 |
| fe46d804-9a76-38e6-9e08-755d825f5fe8 | 4.45856 | -60.98615 | 2024-12-17 06:22:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 46.2 |
| efe35766-7af9-3218-92c1-75a6ebc848d2 | 4.43913 | -60.99435 | 2024-12-17 06:22:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 51efe288-1d16-36bd-bb58-bc83c11bec99 | 4.45215 | -60.98972 | 2024-12-17 06:22:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 46.2 |
| 2359ca10-b683-3d01-8a06-1fd758e38cca | 4.4498 | -60.97622 | 2024-12-17 06:22:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 6.8 |
| cf0bbbde-99ea-313c-b5a8-6711be1a066d | 4.44406 | -60.98363 | 2024-12-17 06:22:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 7f41e562-105a-3cbb-b22e-844b48e0de29 | 4.45726 | -60.97784 | 2024-12-17 06:22:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 5.5 |
| c599f657-c15b-36de-965d-1ac6ac209eb0 | 4.43888 | -60.95422 | 2024-12-17 06:22:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| afab6160-7e78-35e6-b886-ffa9851234c5 | 4.45183 | -60.98677 | 2024-12-17 06:22:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 48.8 |
| c3943988-9ada-3c2e-8e68-3c49175d10a7 | 4.45654 | -60.97454 | 2024-12-17 06:22:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 6.8 |
| d644b4be-3c9d-3f1f-98c4-e821dc503126 | 4.44625 | -60.95585 | 2024-12-17 06:22:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 3dcb4f2a-9c44-30cc-8618-a3f3d1b14963 | 4.44365 | -60.98048 | 2024-12-17 06:22:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 16.5 |
| ce1a4881-fca3-3414-9a3c-9d39e771cc1b | 4.43305 | -60.96095 | 2024-12-17 06:22:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d584e4c1-baa2-3698-ade8-24db08e5cfb9 | 4.44124 | -60.96721 | 2024-12-17 06:22:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 4.1 |
| cfaad86a-67b4-3e92-87c1-a473f86a40ef | 4.4406 | -60.96383 | 2024-12-17 06:22:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 24a34c8b-17c4-3e8b-9205-48e87d4420d8 | 4.45758 | -60.9805 | 2024-12-17 06:22:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 46.2 |
| b07380af-3934-315c-802f-cc998a86fc06 | 4.43357 | -60.96394 | 2024-12-17 06:22:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7ad76fb2-6a5c-3cbe-9012-a97896856a31 | -6.9346 | -43.5168 | 2024-12-17 06:30:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 77.3 |
| afdaca3d-e482-3f0b-a579-e3cac22f5e84 | 4.4618 | -60.9842 | 2024-12-17 06:30:00 | GOES-16 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 66.5 |
| db52e0fa-75cf-30f7-928a-0fe25c07075f | 4.4435 | -60.9846 | 2024-12-17 06:30:00 | GOES-16 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 116.1 |
| c58e8bc3-d35f-34fd-a005-7a47f7202361 | 4.4435 | -60.9846 | 2024-12-17 06:40:00 | GOES-16 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 78.4 |


[Clique aqui para ver as próximas entradas](README31.md)
