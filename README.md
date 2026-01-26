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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 894e3a90-1070-3559-979e-ccc745058682 | -19.6148 | -57.3362 | 2026-01-26 00:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 62.0 |
| 94b08112-1712-328e-8c5c-38eb47eaaade | -20.3497 | -57.8197 | 2026-01-26 00:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 120.7 |
| 38973152-d29f-3e3b-a3ac-fb7767b79f49 | -20.3298 | -57.8015 | 2026-01-26 00:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 130.3 |
| 84d665c3-47fb-3815-ad1b-6d02084eff8c | -18.8499 | -57.7064 | 2026-01-26 00:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 119.0 |
| f1514dbb-65e0-36ca-8ff3-b12a004add49 | -18.8296 | -57.7296 | 2026-01-26 00:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 110.5 |
| 8bd11045-ce15-3d7d-93a4-fd667151b115 | -20.3294 | -57.8224 | 2026-01-26 00:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 195.5 |
| 76130bbd-03d9-3534-9673-f975bbdc2a99 | -20.35 | -57.7988 | 2026-01-26 00:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 81.5 |
| c75b49fc-d115-3b3d-8a60-4dff8d2331be | -18.83 | -57.7089 | 2026-01-26 00:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 141.5 |
| bc440212-3f2f-3a58-b79e-e4ff34c119fe | -19.6349 | -57.3335 | 2026-01-26 00:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 54.5 |
| 8b91ed1e-d92c-372d-a960-32ba46de3f5b | -18.8495 | -57.7271 | 2026-01-26 00:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 113.0 |
| 4585086f-69ed-3abc-91e2-60b1cdec650e | -18.8495 | -57.7271 | 2026-01-26 00:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 112.1 |
| 2fa48a7d-c381-3b5a-9c0f-11c2aacf7f1b | -18.8499 | -57.7064 | 2026-01-26 00:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 97.7 |
| e81f012f-8819-36d7-b215-7aabeafdcdb7 | -19.7037 | -56.8646 | 2026-01-26 00:10:00 | GOES-19 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 110.5 |
| 5511fcd1-9039-3bf1-be90-07e895b1a0fc | -20.3294 | -57.8224 | 2026-01-26 00:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 111.7 |
| 3e494beb-852b-3916-b779-e058484432a0 | -19.684 | -56.8464 | 2026-01-26 00:10:00 | GOES-19 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 87.1 |
| 0b8cfae2-2286-3340-9343-a5021cbfe71a | -19.7238 | -56.8618 | 2026-01-26 00:10:00 | GOES-19 | MIRANDA | MATO GROSSO DO SUL | Brasil | 5005608 | 50 | 33 | nan | nan | nan | Pantanal | 93.1 |
| 855ebd97-a641-3826-a873-b49683ff72d4 | -19.7045 | -56.8226 | 2026-01-26 00:10:00 | GOES-19 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 140.4 |
| c7fe5b90-2e0c-3232-9acc-898208bfaf86 | -19.7041 | -56.8436 | 2026-01-26 00:10:00 | GOES-19 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 305.3 |
| db6b607e-527f-3163-8143-1657c179d95e | -19.7242 | -56.8408 | 2026-01-26 00:10:00 | GOES-19 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 170.1 |
| 62555176-0800-341e-b990-d8904ed9b429 | -19.7045 | -56.8226 | 2026-01-26 00:20:00 | GOES-19 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 69.5 |
| fd5ab355-51f5-32ac-941a-a52384af1b17 | -18.8296 | -57.7296 | 2026-01-26 00:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 82.5 |
| afb6a3d8-87ef-32e0-a049-246564524a7e | -19.7238 | -56.8618 | 2026-01-26 00:20:00 | GOES-19 | MIRANDA | MATO GROSSO DO SUL | Brasil | 5005608 | 50 | 33 | nan | nan | nan | Pantanal | 100.5 |
| b2b9b79b-415a-3543-b871-686780d358d9 | -19.7041 | -56.8436 | 2026-01-26 00:20:00 | GOES-19 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 187.2 |
| f7cf60e1-9016-3b2c-a3b6-842b53c3523a | -20.3298 | -57.8015 | 2026-01-26 00:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 90.8 |
| 54c93206-1a48-33ba-8b3c-1241b3e43ddb | -18.8499 | -57.7064 | 2026-01-26 00:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 89.8 |
| 925a3ef3-756b-388c-beaf-6750e9aea0cd | -18.83 | -57.7089 | 2026-01-26 00:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 87.9 |
| 3b378354-4050-3cb3-a921-a4af6319ca09 | -20.3294 | -57.8224 | 2026-01-26 00:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 112.1 |
| 2b9f2dcc-8015-3207-8954-93f99fc0aec4 | -19.7242 | -56.8408 | 2026-01-26 00:20:00 | GOES-19 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 135.4 |
| e314a9ed-e9af-3040-abcf-f252ac5ee05f | -19.7037 | -56.8646 | 2026-01-26 00:20:00 | GOES-19 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 120.3 |
| 5da37724-363e-39b0-a01f-6150d2a53394 | -18.8495 | -57.7271 | 2026-01-26 00:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 88.3 |
| ce407585-0bb6-308c-aeef-f04cbaff88f1 | -6.7809 | -35.189301 | 2026-01-26 00:24:00 | METOP-C | MAMANGUAPE | PARAÍBA | Brasil | 2508901 | 25 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 0fd5cbc0-714e-3b99-88b3-d7bab9d7d047 | -6.7754 | -35.1675 | 2026-01-26 00:24:00 | METOP-C | MAMANGUAPE | PARAÍBA | Brasil | 2508901 | 25 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 22a409f6-5645-3d54-8c20-c70668ac2943 | -5.2707 | -37.716702 | 2026-01-26 00:24:00 | METOP-C | GOVERNADOR DIX-SEPT ROSADO | RIO GRANDE DO NORTE | Brasil | 2404309 | 24 | 33 | nan | nan | nan | Caatinga | nan |
| 07814c16-dcd0-34d6-8ace-274d727a0126 | -6.2056 | -39.2826 | 2026-01-26 00:24:00 | METOP-C | IGUATU | CEARÁ | Brasil | 2305506 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 3edf9646-1c4f-301b-a2cb-6d838bd0e222 | -5.2744 | -37.731998 | 2026-01-26 00:24:00 | METOP-C | GOVERNADOR DIX-SEPT ROSADO | RIO GRANDE DO NORTE | Brasil | 2404309 | 24 | 33 | nan | nan | nan | Caatinga | nan |
| 26a72caf-3204-3c96-bf13-4d3a83e9afc6 | -19.7037 | -56.8646 | 2026-01-26 00:30:00 | GOES-19 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 111.1 |
| 3b9d76fe-f962-38eb-af55-6b9ac75ad97f | -19.7045 | -56.8226 | 2026-01-26 00:30:00 | GOES-19 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 53.2 |
| 488ead35-c258-3b3e-b185-4b7e4a3509dc | -18.8499 | -57.7064 | 2026-01-26 00:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 118.3 |
| 88c50875-3152-3101-b3df-5a7c58e68fc4 | -19.7041 | -56.8436 | 2026-01-26 00:30:00 | GOES-19 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 146.0 |
| 9031433b-610b-357f-a132-13ebf4ce16b3 | -19.6546 | -57.3516 | 2026-01-26 00:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 96.6 |
| 35ec028b-d6ea-318d-be53-179407f42fc6 | -19.7242 | -56.8408 | 2026-01-26 00:30:00 | GOES-19 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 103.6 |
| d39337cf-138e-3dac-ba5b-08e6eaeb1b8c | -19.655 | -57.3307 | 2026-01-26 00:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 109.8 |
| 0a0707e0-f4ae-3c11-b421-56f67f62f97b | -20.3298 | -57.8015 | 2026-01-26 00:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 265.0 |
| 9e4a02fd-7692-3d16-9f6c-b6779bdcbd06 | -20.3294 | -57.8224 | 2026-01-26 00:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 291.4 |
| 9c179078-af32-31e8-8323-1192dc71a24b | -18.83 | -57.7089 | 2026-01-26 00:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 75.8 |
| 9ace67fa-33c1-3c36-9618-ae35ecd86223 | -20.3497 | -57.8197 | 2026-01-26 00:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 88.0 |
| 6ce5bf1a-27ef-317f-8ed5-b5c505928a81 | -19.6349 | -57.3335 | 2026-01-26 00:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 118.3 |
| 1bd5949b-1cd3-3dbb-8e0a-361706d3faa4 | -19.6345 | -57.3544 | 2026-01-26 00:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 111.0 |
| a5abf9f1-5f9c-3977-b497-78f55ce5e47a | -19.7238 | -56.8618 | 2026-01-26 00:30:00 | GOES-19 | MIRANDA | MATO GROSSO DO SUL | Brasil | 5005608 | 50 | 33 | nan | nan | nan | Pantanal | 77.0 |
| 2e0e21f6-bb81-357c-b904-c5a6d4b57582 | -18.8495 | -57.7271 | 2026-01-26 00:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 122.4 |
| c796a0fd-9ec4-3ecc-8fd0-c1bffa625388 | -18.8495 | -57.7271 | 2026-01-26 00:40:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 147.2 |
| 6120c2bb-532a-3fec-a32b-a16db11dae66 | -18.83 | -57.7089 | 2026-01-26 00:40:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 69.6 |
| ed8dec10-fe65-3edb-b9dc-3160faf7d2b6 | -20.3298 | -57.8015 | 2026-01-26 00:40:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 208.4 |
| b2d824e4-7095-3630-9b40-6a12786c159b | -20.3497 | -57.8197 | 2026-01-26 00:40:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 138.1 |
| 730cab74-091b-3098-93ec-6fdd0cafa567 | -20.35 | -57.7988 | 2026-01-26 00:40:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 103.8 |
| 7d6b56fe-d4bd-3ed2-9680-2f99c3bf3e39 | -18.8499 | -57.7064 | 2026-01-26 00:40:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 113.1 |
| 33a57af4-3410-3f74-b8b9-19cf2cd25c03 | -20.3294 | -57.8224 | 2026-01-26 00:40:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 284.0 |
| 0d6305a9-52a8-3e91-ae4f-1be3c96b8483 | -20.3092 | -57.8252 | 2026-01-26 00:40:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 91.7 |
| cac7d2b5-eaf6-3972-8fa5-544090c8b1cf | -28.10502 | -50.50457 | 2026-01-26 00:43:00 | TERRA_M-M | CAPÃO ALTO | SANTA CATARINA | Brasil | 4203253 | 42 | 33 | nan | nan | nan | Mata Atlântica | 13.5 |
| e08b80a5-edde-3942-a12e-c7796054e177 | -26.05761 | -53.58071 | 2026-01-26 00:43:00 | TERRA_M-M | SANTO ANTÔNIO DO SUDOESTE | PARANÁ | Brasil | 4124400 | 41 | 33 | nan | nan | nan | Mata Atlântica | 7.6 |
| 46622212-0e77-3c2b-ac99-bd1d39511325 | -25.20657 | -51.3859 | 2026-01-26 00:43:00 | TERRA_M-M | GUARAPUAVA | PARANÁ | Brasil | 4109401 | 41 | 33 | nan | nan | nan | Mata Atlântica | 12.6 |
| c25660de-eb69-3a95-b932-e52133c4e839 | -25.20794 | -51.39564 | 2026-01-26 00:43:00 | TERRA_M-M | GUARAPUAVA | PARANÁ | Brasil | 4109401 | 41 | 33 | nan | nan | nan | Mata Atlântica | 12.8 |
| 2d036670-cd6e-3aa9-bcc8-366752c3548e | -27.57545 | -50.35122 | 2026-01-26 00:43:00 | TERRA_M-M | CORREIA PINTO | SANTA CATARINA | Brasil | 4204558 | 42 | 33 | nan | nan | nan | Mata Atlântica | 10.2 |
| 8332d2dc-1ff2-3357-9c67-60e2aa5056f6 | -22.3221 | -47.13268 | 2026-01-26 00:45:00 | TERRA_M-M | CONCHAL | SÃO PAULO | Brasil | 3512209 | 35 | 33 | nan | nan | nan | Cerrado | 30.7 |
| 0f2f6c58-847d-3264-96ab-8908d21916dd | -22.32484 | -47.14857 | 2026-01-26 00:45:00 | TERRA_M-M | CONCHAL | SÃO PAULO | Brasil | 3512209 | 35 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 87677afe-ef94-35e4-a695-14a86fc6f050 | -20.91635 | -56.376 | 2026-01-26 00:45:00 | TERRA_M-M | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 14.4 |
| b5a8d787-0169-3941-80c3-8d5c9c2d2c2f | -22.48507 | -47.00469 | 2026-01-26 00:45:00 | TERRA_M-M | MOGI MIRIM | SÃO PAULO | Brasil | 3530805 | 35 | 33 | nan | nan | nan | Cerrado | 10.9 |
| fdf0c45c-0e8c-3637-af33-df3252151ee0 | -20.32867 | -57.81188 | 2026-01-26 00:47:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 490.6 |
| 6ebfb207-93f3-352c-ba0e-1319687bce68 | -19.60945 | -57.30267 | 2026-01-26 00:47:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 9.9 |
| 760f5772-630c-3eeb-a4ee-afad80ee9df7 | -18.80628 | -57.69683 | 2026-01-26 00:47:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 8.7 |
| bb357764-fee1-3694-ba0c-3101debb6976 | -18.79778 | -57.69205 | 2026-01-26 00:47:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 7.8 |
| cb382c05-d34c-3dae-8eb5-39c0147c8d8f | -19.6464 | -57.34056 | 2026-01-26 00:47:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 32.7 |
| 0548f4c6-4a70-3eeb-9f5f-a1272b29298a | -19.34501 | -54.18055 | 2026-01-26 00:47:00 | TERRA_M-M | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 6cc4d1a8-6913-3180-ad06-f8583f879c5c | -19.60786 | -57.28873 | 2026-01-26 00:47:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 7.9 |
| 07443ce0-5494-3ea2-86f9-58a43f1b21af | -18.84456 | -57.71539 | 2026-01-26 00:47:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 155.3 |
| 2faed8cd-87e8-3a5c-99f6-edb86499c023 | -20.34165 | -57.82607 | 2026-01-26 00:47:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 41.6 |
| f2a51c04-e5a2-3843-aa0c-1c1dfa78d78f | -19.64804 | -57.35463 | 2026-01-26 00:47:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 37.7 |
| f0e01a40-4e7c-3e2e-805f-67cda6342db9 | -19.34373 | -54.17087 | 2026-01-26 00:47:00 | TERRA_M-M | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 13.6 |
| 9a65dc77-258a-36cb-b970-b9c85d3da24d | -20.30795 | -57.8303 | 2026-01-26 00:47:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 10.4 |
| 196f9c22-2d75-36ac-be4d-20bcf9a3eea5 | -20.33989 | -57.81048 | 2026-01-26 00:47:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 45.3 |
| 448648b2-df31-3673-aa01-7de9459d3dd5 | -18.84622 | -57.7299 | 2026-01-26 00:47:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 95.5 |
| f55e4297-7e35-3249-832e-98d325104884 | -20.33041 | -57.82748 | 2026-01-26 00:47:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 154.9 |
| 43bdf9e5-278c-38a1-9afc-1d45b7e0ed12 | -19.63731 | -57.35601 | 2026-01-26 00:47:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 42.3 |
| ed4f200c-5f8e-3425-8832-c50235fc1c1a | -19.63568 | -57.34194 | 2026-01-26 00:47:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 64.0 |
| 22699e50-1767-3421-a2ac-6ba298f634d8 | -19.61264 | -57.33066 | 2026-01-26 00:47:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 15.4 |
| 6d10487a-1434-3567-b944-3ae9f3a19a3f | -19.71051 | -56.8655 | 2026-01-26 00:47:00 | TERRA_M-M | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 32.6 |
| 7e5cafbd-b1c0-31b4-a94c-3bd7d6a8eccc | -18.83367 | -57.71678 | 2026-01-26 00:47:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 12.9 |
| 8cc36a2f-091b-3eda-9e7e-db9567c60825 | -19.61105 | -57.31665 | 2026-01-26 00:47:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 13.0 |
| 8c95af6f-fb6b-3689-89f2-be261f6332f0 | -20.3294 | -57.8224 | 2026-01-26 00:50:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 299.2 |
| 2eb268f2-6425-3249-af6f-619a16848e60 | -6.2083 | -39.2848 | 2026-01-26 00:50:00 | GOES-19 | IGUATU | CEARÁ | Brasil | 2305506 | 23 | 33 | nan | nan | nan | Caatinga | 60.5 |
| 1d2ddbaa-4c37-36b6-9957-969e9428549c | -18.8495 | -57.7271 | 2026-01-26 00:50:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 154.3 |
| 72bdfdd7-fd36-3957-afb3-2bf1232ee374 | -18.8499 | -57.7064 | 2026-01-26 00:50:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 104.9 |
| 747b8b70-581a-3f5e-880c-7928a6e758cd | -20.3298 | -57.8015 | 2026-01-26 00:50:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 132.5 |
| 29818fc1-00d6-3811-8d66-0200fee1f6ca | 3.37817 | -60.51448 | 2026-01-26 00:52:00 | TERRA_M-M | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 4efdacac-da68-3e37-9dfe-d67e6b5971a7 | 3.31813 | -60.42456 | 2026-01-26 00:52:00 | TERRA_M-M | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 6c0312e8-fbfa-3df4-aae7-2c17f0bcbca8 | 3.96731 | -60.32906 | 2026-01-26 00:52:00 | TERRA_M-M | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 904eb749-0658-31a4-903a-d274469884b9 | 3.38115 | -60.49342 | 2026-01-26 00:52:00 | TERRA_M-M | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 9be55e76-3f7f-3b9a-92ae-07f5bc79a8f0 | -18.8495 | -57.7271 | 2026-01-26 01:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 114.2 |
| 4bc86200-f589-3a81-9cb4-6d86c0cdfacc | -20.3294 | -57.8224 | 2026-01-26 01:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 91.6 |
| a795cbc5-7eaa-3575-bcb7-5b4ffc1ee574 | -18.83 | -57.7089 | 2026-01-26 01:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 83.7 |


[Clique aqui para ver as próximas entradas](README2.md)
