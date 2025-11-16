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

## Dados Diários - Página 66

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 881acd66-58a2-3c9d-adc0-6bd5fd0ad648 | -2.5238 | -47.8115 | 2025-11-16 07:10:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 60.5 |
| fd275808-4c88-3d04-87e3-7d9f5662f57d | -3.4786 | -45.7532 | 2025-11-16 07:10:00 | GOES-19 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 43.0 |
| 53670d47-66d6-315f-b3ce-edc58018ce4e | -3.4972 | -45.7524 | 2025-11-16 07:10:00 | GOES-19 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 52.4 |
| da8f2888-5891-3107-b57c-39cb6b68d639 | -3.4785 | -45.7756 | 2025-11-16 07:10:00 | GOES-19 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 50.4 |
| 1fcf76cf-cdeb-3b13-ac24-8f9ab582853b | -3.4971 | -45.7748 | 2025-11-16 07:20:00 | GOES-19 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 118.4 |
| cdc01633-6b3a-3653-9830-622bca949edb | -3.4972 | -45.7524 | 2025-11-16 07:20:00 | GOES-19 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 99.4 |
| dddc86e3-db0f-339b-acf6-2d8f92b8793c | -3.2211 | -45.2024 | 2025-11-16 07:20:00 | GOES-19 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 45.2 |
| d03db181-47f1-396d-a60b-3b5a88089be6 | -2.5238 | -47.8115 | 2025-11-16 07:20:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 52.5 |
| 4fcfa358-0cbb-318c-b67d-a8531effe894 | -3.4785 | -45.7756 | 2025-11-16 07:20:00 | GOES-19 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 131.6 |
| fd3b7533-8014-3a10-9629-584de3479aac | -3.4786 | -45.7532 | 2025-11-16 07:20:00 | GOES-19 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 109.1 |
| f2595cc9-5478-384d-9c8c-e534ca78ba60 | -3.2211 | -45.2024 | 2025-11-16 07:30:00 | GOES-19 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 66.5 |
| 240a5f4f-ada2-3818-911b-dd5dc28f1132 | -3.4786 | -45.7532 | 2025-11-16 07:30:00 | GOES-19 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 119.9 |
| ef2db2d1-aa37-31bd-a2ce-cc4906a922ad | -3.4785 | -45.7756 | 2025-11-16 07:30:00 | GOES-19 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 96.1 |
| 929d1050-bb64-3d0a-918e-f137fd485c13 | -3.4972 | -45.7524 | 2025-11-16 07:30:00 | GOES-19 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 90.9 |
| e6b45a70-af0c-3819-ab17-85ce029e00b2 | -3.4971 | -45.7748 | 2025-11-16 07:30:00 | GOES-19 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 72.9 |
| d1d0c285-408d-3519-a1e9-e9bce9ac2563 | -2.5238 | -47.8115 | 2025-11-16 07:30:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 51.6 |
| 4bdf032b-5a7c-3b13-8411-5187af99bedd | -3.4785 | -45.7756 | 2025-11-16 07:40:00 | GOES-19 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 62.7 |
| e3b16f2a-7f15-3fb2-a42d-282b95dceac3 | -2.5238 | -47.8115 | 2025-11-16 07:40:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 53.0 |
| ad1704d9-3429-3809-9bc3-0e484b44bd43 | -3.4971 | -45.7748 | 2025-11-16 07:40:00 | GOES-19 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 53.6 |
| da0169cb-2ef7-3b7f-bcc1-cefdb8d94f36 | -3.4786 | -45.7532 | 2025-11-16 07:40:00 | GOES-19 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 71.9 |
| 631bda2b-b827-357d-8907-bc87c483e7ed | -3.4972 | -45.7524 | 2025-11-16 07:40:00 | GOES-19 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 62.8 |
| 0301ea5a-59b9-391f-ab56-e27f47a76b4e | -2.5238 | -47.8115 | 2025-11-16 07:50:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 52.5 |
| 4a451995-d4c4-3280-acac-0cb2f74d30c0 | -2.5238 | -47.8115 | 2025-11-16 08:10:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 49.1 |
| c56d3468-29e6-35a5-b6f4-2c9fcff1685c | -2.8505 | -44.9226 | 2025-11-16 10:10:00 | GOES-19 | SÃO VICENTE FERRER | MARANHÃO | Brasil | 2111706 | 21 | 33 | nan | nan | nan | Amazônia | 165.1 |
| f8cac103-66fd-3666-80e9-bc6665eaee16 | -2.8504 | -44.9453 | 2025-11-16 10:10:00 | GOES-19 | SÃO VICENTE FERRER | MARANHÃO | Brasil | 2111706 | 21 | 33 | nan | nan | nan | Amazônia | 151.8 |
| 005fcb77-a3c4-3695-826b-fd23f43aa80b | -2.7011 | -45.086 | 2025-11-16 10:10:00 | GOES-19 | PALMEIRÂNDIA | MARANHÃO | Brasil | 2107605 | 21 | 33 | nan | nan | nan | Amazônia | 105.3 |
| 7653b4d5-b25e-3758-8658-dccf2bf9a0a2 | -2.8505 | -44.9226 | 2025-11-16 10:20:00 | GOES-19 | SÃO VICENTE FERRER | MARANHÃO | Brasil | 2111706 | 21 | 33 | nan | nan | nan | Amazônia | 138.8 |
| 52c1ef1e-fc06-360a-b1b0-f704d879230e | -2.8504 | -44.9453 | 2025-11-16 10:20:00 | GOES-19 | SÃO VICENTE FERRER | MARANHÃO | Brasil | 2111706 | 21 | 33 | nan | nan | nan | Amazônia | 163.4 |
| 6ee2f8fe-dd38-3f10-b5d0-ffefe177a3a7 | -2.7011 | -45.086 | 2025-11-16 10:20:00 | GOES-19 | PALMEIRÂNDIA | MARANHÃO | Brasil | 2107605 | 21 | 33 | nan | nan | nan | Amazônia | 136.1 |
| 28ee6688-f757-3c23-839c-8c076b939b60 | -2.7011 | -45.086 | 2025-11-16 10:30:00 | GOES-19 | PALMEIRÂNDIA | MARANHÃO | Brasil | 2107605 | 21 | 33 | nan | nan | nan | Amazônia | 96.2 |
| 4cf9b3e8-1b72-3b2f-8a0a-f40fed35c59f | -2.8505 | -44.9226 | 2025-11-16 10:30:00 | GOES-19 | SÃO VICENTE FERRER | MARANHÃO | Brasil | 2111706 | 21 | 33 | nan | nan | nan | Amazônia | 155.6 |
| e1335ce0-9040-3c5d-83a8-f3376bc6599c | -2.8504 | -44.9453 | 2025-11-16 10:30:00 | GOES-19 | SÃO VICENTE FERRER | MARANHÃO | Brasil | 2111706 | 21 | 33 | nan | nan | nan | Amazônia | 137.8 |
| 33b0062d-9942-329f-b284-14584e115e72 | -2.7011 | -45.086 | 2025-11-16 10:40:00 | GOES-19 | PALMEIRÂNDIA | MARANHÃO | Brasil | 2107605 | 21 | 33 | nan | nan | nan | Amazônia | 145.8 |
| d92a30f4-d730-3cae-af41-6293c34fdbf8 | -2.8504 | -44.9453 | 2025-11-16 10:40:00 | GOES-19 | SÃO VICENTE FERRER | MARANHÃO | Brasil | 2111706 | 21 | 33 | nan | nan | nan | Amazônia | 168.4 |
| 2c115506-875b-38c2-baef-9aa81474eb7d | -2.8504 | -44.9453 | 2025-11-16 10:50:00 | GOES-19 | SÃO VICENTE FERRER | MARANHÃO | Brasil | 2111706 | 21 | 33 | nan | nan | nan | Amazônia | 134.5 |
| 6e0d4a60-59c4-34e9-a634-0e15c15b7ffb | -2.7011 | -45.086 | 2025-11-16 10:50:00 | GOES-19 | PALMEIRÂNDIA | MARANHÃO | Brasil | 2107605 | 21 | 33 | nan | nan | nan | Amazônia | 114.9 |
| 933851fb-0429-3e07-b927-7a2acca94aab | -3.3672 | -42.1928 | 2025-11-16 11:10:00 | GOES-19 | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Caatinga | 160.8 |
| 94343a0c-ca1d-3f67-8620-b990c3a60ed8 | -3.3486 | -42.17 | 2025-11-16 11:10:00 | GOES-19 | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Caatinga | 76.5 |
| dbfd5dbe-33ca-3939-9897-6d8fcf7f4f66 | -3.3672 | -42.1928 | 2025-11-16 11:20:00 | GOES-19 | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Caatinga | 78.8 |
| 49153de3-d10b-378a-bf0b-cc2b920d62ba | -3.3672 | -42.1928 | 2025-11-16 11:30:00 | GOES-19 | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Caatinga | 142.5 |
| f70c3ae0-4316-3c35-991f-afcbfa6d3aff | -3.3673 | -42.1691 | 2025-11-16 11:30:00 | GOES-19 | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Caatinga | 108.1 |
| 89379c80-30e2-3f17-94f6-0360c6780664 | -2.5238 | -47.8115 | 2025-11-16 11:50:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 83.9 |
| e6bc4571-4699-30b2-9c87-e27c900f581a | -3.4089 | -41.4273 | 2025-11-16 11:50:00 | GOES-19 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 95.2 |
| 0c5b1f62-bded-3746-b9f4-b888a26bcd61 | -4.4246 | -43.4038 | 2025-11-16 12:10:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 97.2 |
| 8cdbbaa5-8de3-3028-898a-82d33ebfa1ff | -4.4059 | -43.4049 | 2025-11-16 12:10:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 112.5 |
| 86fc7df1-ad9a-3f88-868a-4940a697debd | -4.8117 | -41.7043 | 2025-11-16 12:20:00 | GOES-19 | SIGEFREDO PACHECO | PIAUÍ | Brasil | 2210656 | 22 | 33 | nan | nan | nan | Caatinga | 75.2 |
| 3052b56a-2913-3a43-85ed-7f0f03bcde40 | -4.4059 | -43.4049 | 2025-11-16 12:20:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 117.4 |
| 52eeaa74-492c-379f-9d3c-0db3a69876cd | -4.8119 | -41.6803 | 2025-11-16 12:20:00 | GOES-19 | SIGEFREDO PACHECO | PIAUÍ | Brasil | 2210656 | 22 | 33 | nan | nan | nan | Caatinga | 82.0 |
| fdc41f05-b3cd-3452-91ba-eabfb11e3cc0 | -4.4246 | -43.4038 | 2025-11-16 12:20:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 98.7 |
| 93fc12c2-9b7d-37c9-a719-16e69d67694b | -3.2304 | -43.3486 | 2025-11-16 12:20:00 | GOES-19 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 164.7 |
| 1bc0cc83-bd8f-3fbb-90f8-dda060406f5d | -3.2304 | -43.3486 | 2025-11-16 12:30:00 | GOES-19 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 233.7 |
| d5c10e94-6a11-3076-aec4-bf1afc62b563 | -4.4246 | -43.4038 | 2025-11-16 12:30:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 131.7 |
| cda47707-161e-3bf2-ac93-15a2fd80c72a | -6.3705 | -41.7477 | 2025-11-16 12:30:00 | GOES-19 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 71.7 |
| c8ea77d2-1025-317f-ba6f-ae933fbbe592 | -3.2744 | -42.0785 | 2025-11-16 12:30:00 | GOES-19 | MURICI DOS PORTELAS | PIAUÍ | Brasil | 2206696 | 22 | 33 | nan | nan | nan | Cerrado | 103.7 |
| 8ba68cb4-6290-3176-9eab-096b76154974 | -4.4059 | -43.4049 | 2025-11-16 12:30:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 168.4 |
| fc7a4f6d-ea4c-3de9-bfc1-d3eeaf625a34 | -1.9887 | -47.354 | 2025-11-16 12:36:00 | TERRA_M-T | IRITUIA | PARÁ | Brasil | 1503507 | 15 | 33 | nan | nan | nan | Amazônia | 32.8 |
| fbccda1e-8f46-3da5-a485-ef3f92771610 | -1.99072 | -47.33951 | 2025-11-16 12:36:00 | TERRA_M-T | IRITUIA | PARÁ | Brasil | 1503507 | 15 | 33 | nan | nan | nan | Amazônia | 22.3 |
| b9556443-4f40-33d3-872f-5439e59b464d | -1.16648 | -49.19714 | 2025-11-16 12:36:00 | TERRA_M-T | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 14.7 |
| 55ad7670-1884-3ca1-a4a0-acbca10034c2 | -0.82951 | -48.04065 | 2025-11-16 12:36:00 | TERRA_M-T | SÃO CAETANO DE ODIVELAS | PARÁ | Brasil | 1507102 | 15 | 33 | nan | nan | nan | Amazônia | 29.8 |
| 3d3313fd-f42b-3f90-ad1a-11d167d8c157 | -1.34884 | -47.74776 | 2025-11-16 12:36:00 | TERRA_M-T | CASTANHAL | PARÁ | Brasil | 1502400 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 787acd7a-2e29-3699-9767-35239fc5c867 | 1.62537 | -55.882 | 2025-11-16 12:36:00 | TERRA_M-T | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 5e0aa673-7d11-3d9e-af34-5c681a9c1016 | 1.61527 | -55.81065 | 2025-11-16 12:36:00 | TERRA_M-T | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 12.0 |
| 17ab99f8-9061-3530-a197-1d33d019216f | -1.20986 | -47.58085 | 2025-11-16 12:36:00 | TERRA_M-T | IGARAPÉ-AÇU | PARÁ | Brasil | 1503200 | 15 | 33 | nan | nan | nan | Amazônia | 18.7 |
| 502534c3-240c-3268-b802-66e68320f043 | -0.89525 | -48.57943 | 2025-11-16 12:36:00 | TERRA_M-T | SALVATERRA | PARÁ | Brasil | 1506302 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 95f1d515-5a5b-3384-9c21-8931d480f2ec | -1.50168 | -47.62527 | 2025-11-16 12:36:00 | TERRA_M-T | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | 22.6 |
| e733fe73-058e-34ea-a04c-1aae6ab6fd7b | -2.42792 | -45.70061 | 2025-11-16 12:36:00 | TERRA_M-T | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 24.0 |
| 16284ca6-2688-3253-95c4-1e5b107824e4 | -1.19537 | -47.60617 | 2025-11-16 12:36:00 | TERRA_M-T | IGARAPÉ-AÇU | PARÁ | Brasil | 1503200 | 15 | 33 | nan | nan | nan | Amazônia | 13.5 |
| 94946bab-ecb7-3074-8f4f-00b81190dc6b | -2.42516 | -45.72034 | 2025-11-16 12:36:00 | TERRA_M-T | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 19.5 |
| 305cbbb7-ec91-33ee-aa9f-3e9ace91455e | 0.92297 | -50.84227 | 2025-11-16 12:36:00 | TERRA_M-T | CUTIAS | AMAPÁ | Brasil | 1600212 | 16 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 9baaf914-ac6d-306e-84f7-23bb09361d59 | -1.18285 | -48.85352 | 2025-11-16 12:36:00 | TERRA_M-T | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| f73f2b61-9508-3137-b98a-c0d591d5372e | 1.6274 | -55.89635 | 2025-11-16 12:36:00 | TERRA_M-T | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 24.5 |
| 9f025462-20c2-343a-93ad-28304876bdbd | -1.13076 | -47.87058 | 2025-11-16 12:36:00 | TERRA_M-T | CASTANHAL | PARÁ | Brasil | 1502400 | 15 | 33 | nan | nan | nan | Amazônia | 14.2 |
| 1cefe831-5bbe-3679-b340-09c4a1a16357 | 1.61727 | -55.82479 | 2025-11-16 12:36:00 | TERRA_M-T | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 16.3 |
| e50888fe-d023-3ab0-a042-c6723b9efee1 | -2.41512 | -45.69887 | 2025-11-16 12:36:00 | TERRA_M-T | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 25.8 |
| 72e2273f-7ccb-31ee-b2a1-3c1779c72d79 | -1.34273 | -47.75379 | 2025-11-16 12:36:00 | TERRA_M-T | CASTANHAL | PARÁ | Brasil | 1502400 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 54548905-fc27-3667-8787-9db6c3425ea8 | -1.13608 | -47.87774 | 2025-11-16 12:36:00 | TERRA_M-T | CASTANHAL | PARÁ | Brasil | 1502400 | 15 | 33 | nan | nan | nan | Amazônia | 30.1 |
| 32aef7c8-208d-3b8a-a4b6-2607efd1c0d0 | -1.19723 | -47.59281 | 2025-11-16 12:36:00 | TERRA_M-T | IGARAPÉ-AÇU | PARÁ | Brasil | 1503200 | 15 | 33 | nan | nan | nan | Amazônia | 26.0 |
| 73856c07-5479-3996-8522-998fdc91015c | -4.41194 | -43.41548 | 2025-11-16 12:38:00 | TERRA_M-T | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 181.1 |
| b4fe5bc3-2ba2-3c6c-8331-82fd2a161b6a | -3.44097 | -49.47867 | 2025-11-16 12:38:00 | TERRA_M-T | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 16.5 |
| 0fb93280-6069-3530-9b5b-a291d2bdc4ad | -8.67831 | -43.88671 | 2025-11-16 12:38:00 | TERRA_M-T | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 79.7 |
| b7bd1b1b-4d17-3a90-9f58-068f06021e45 | -3.21635 | -42.22514 | 2025-11-16 12:38:00 | TERRA_M-T | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Cerrado | 65.2 |
| a35362a4-960f-3b29-b769-e107bd4530b9 | -5.97873 | -47.99415 | 2025-11-16 12:38:00 | TERRA_M-T | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 15.7 |
| 190a6a5b-2851-3621-ae23-f6374f8435df | -6.03312 | -48.1858 | 2025-11-16 12:38:00 | TERRA_M-T | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Amazônia | 22.6 |
| 51391b32-b33e-3c6e-82a0-8533dd464547 | -6.81562 | -48.78939 | 2025-11-16 12:38:00 | TERRA_M-T | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 2ee82344-45b2-3911-8668-ae7ff2698811 | -3.06024 | -42.36044 | 2025-11-16 12:38:00 | TERRA_M-T | TUTÓIA | MARANHÃO | Brasil | 2112506 | 21 | 33 | nan | nan | nan | Cerrado | 92.7 |
| c1ba7325-4766-33eb-80e5-33d37057a1e8 | -3.23302 | -42.38972 | 2025-11-16 12:38:00 | TERRA_M-T | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 46.6 |
| c7d02b49-de70-32d7-879d-b62bacd6a14c | -9.8489 | -47.0384 | 2025-11-16 12:38:00 | TERRA_M-T | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 42.8 |
| 3566ab4c-5d46-384e-b8a4-5f6972459157 | -1.637 | -53.64171 | 2025-11-16 12:38:00 | TERRA_M-T | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 26.7 |
| 13bd881d-7b1f-3116-b7c0-684401a7f474 | -9.35573 | -46.59896 | 2025-11-16 12:38:00 | TERRA_M-T | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 27.6 |
| 0ac00be1-0c4f-33b5-9fcd-237083126108 | -8.52262 | -45.35193 | 2025-11-16 12:38:00 | TERRA_M-T | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 32.7 |
| effbd673-be6c-3aea-893f-31ad64d8e25b | -8.66712 | -43.91515 | 2025-11-16 12:38:00 | TERRA_M-T | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 221.9 |
| fc4167fe-6d26-33c8-b6a3-b14dc60da44f | -7.39424 | -45.50605 | 2025-11-16 12:38:00 | TERRA_M-T | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 58.5 |
| 52a54c4a-c795-3c49-8e91-e29ccb99f342 | -4.74289 | -46.38605 | 2025-11-16 12:38:00 | TERRA_M-T | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 34.5 |
| 38004715-0493-39fa-90bc-fc76bf4ac32d | -9.84633 | -47.05893 | 2025-11-16 12:38:00 | TERRA_M-T | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 35.3 |
| a3b1ae41-6132-3a1a-a255-2acbe3f95538 | -10.16519 | -44.50866 | 2025-11-16 12:38:00 | TERRA_M-T | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 46.0 |
| fc008759-dd51-3379-b176-e940b485a41a | -4.01554 | -48.80888 | 2025-11-16 12:38:00 | TERRA_M-T | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 33.1 |
| 419a3107-ffb0-3003-8740-88f10fc9b8b6 | -3.65968 | -42.43066 | 2025-11-16 12:38:00 | TERRA_M-T | LUZILÂNDIA | PIAUÍ | Brasil | 2205805 | 22 | 33 | nan | nan | nan | Caatinga | 59.2 |
| 7411eca3-0187-3e7c-bbe4-cc47ddd5938a | -7.2274 | -47.11143 | 2025-11-16 12:38:00 | TERRA_M-T | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 50.3 |
| 65e8f849-fee8-3490-8f2d-9bd118c5fbd3 | -2.85278 | -44.92579 | 2025-11-16 12:38:00 | TERRA_M-T | SÃO VICENTE FERRER | MARANHÃO | Brasil | 2111706 | 21 | 33 | nan | nan | nan | Amazônia | 33.3 |
| 2fa02fc9-c7bf-31d9-8824-035f2e3a9c0c | -9.748 | -43.97174 | 2025-11-16 12:38:00 | TERRA_M-T | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 41.7 |


[Clique aqui para ver as próximas entradas](README67.md)
