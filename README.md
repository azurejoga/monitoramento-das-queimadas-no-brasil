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
| 99ec4141-97ee-3a5e-a3ba-da3fba604085 | -8.0947 | -44.1456 | 2026-05-15 00:00:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 77.9 |
| 97e1e4ee-c498-3477-bcd7-ad479df76b64 | -8.7211 | -48.3222 | 2026-05-15 00:00:00 | GOES-19 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 62.1 |
| a92cc49c-bd8f-30fc-be59-b374a055cdf6 | -8.0947 | -44.1456 | 2026-05-15 00:10:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 89.1 |
| 975d6bfa-129f-3ee3-b660-9d14a7c57fe8 | -9.3045 | -45.4809 | 2026-05-15 00:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 61.4 |
| 17832cd4-319b-3fd2-bff7-a8ceb90fdb97 | -8.7211 | -48.3222 | 2026-05-15 00:20:00 | GOES-19 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 77.5 |
| 91d70f6b-025c-3581-8708-efacb4936d14 | -8.0947 | -44.1456 | 2026-05-15 00:20:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 82.3 |
| b5e4bc2e-03cc-38c0-b3ac-3fa9881b5ba2 | -8.0947 | -44.1456 | 2026-05-15 00:30:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 84.8 |
| 68cdfd6e-6e0c-37f0-9b64-0942873305e6 | -8.7211 | -48.3222 | 2026-05-15 00:30:00 | GOES-19 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 56.5 |
| 1997fe69-5b1e-3a60-ac3c-d2f3e5c6904b | -15.6537 | -47.9272 | 2026-05-15 00:30:00 | GOES-19 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 56.1 |
| 352debd1-ae47-3435-a282-a01cd3fea76a | -8.7211 | -48.3222 | 2026-05-15 00:40:00 | GOES-19 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 53.5 |
| cad4c2cd-441d-3d17-aeb3-b3b625da0e27 | -8.0947 | -44.1456 | 2026-05-15 00:40:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 80.9 |
| 95e5fee7-1dab-3a63-98c0-16403671c309 | -15.6537 | -47.9272 | 2026-05-15 00:40:00 | GOES-19 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 49.4 |
| f18a04d6-158a-3f46-ac0f-24fa8d54cb7c | -14.176 | -52.859299 | 2026-05-15 00:40:00 | METOP-B | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 91cc250f-20f2-338a-b16f-ba5523a41d9c | -13.0334 | -49.933498 | 2026-05-15 00:40:00 | METOP-B | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 252c997a-bc04-3e55-809d-9d5dd003bc4e | -8.0752 | -44.140301 | 2026-05-15 00:40:00 | METOP-B | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| de422cb9-63d1-3d17-987d-960a45cecfd3 | -19.1887 | -49.1101 | 2026-05-15 00:40:00 | METOP-B | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| e81427f1-c861-31b4-8d8f-13d1e99ce881 | -8.722 | -48.321602 | 2026-05-15 00:40:00 | METOP-B | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 2c877217-b443-3beb-9628-ec1c275b527c | -8.7123 | -48.324001 | 2026-05-15 00:40:00 | METOP-B | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 4e8ba2b4-b9d3-3e12-a3f6-4f9c62623531 | -9.291 | -45.462601 | 2026-05-15 00:40:00 | METOP-B | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| b3dacd9d-8689-30fb-b939-f767e0b90fd2 | -15.6345 | -47.917801 | 2026-05-15 00:40:00 | METOP-B | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | nan |
| ef9b757c-4c46-3038-9d8b-e432fce46e6d | -19.1912 | -49.120399 | 2026-05-15 00:40:00 | METOP-B | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 1c2de3dd-733c-3efe-bfa8-85e02cafe5b1 | -11.4378 | -55.0956 | 2026-05-15 00:40:00 | METOP-B | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 31f9cced-f24c-345a-9103-5725230a3136 | -12.0814 | -51.250198 | 2026-05-15 00:40:00 | METOP-B | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 566c27a4-4c35-3cac-88e6-d60930168e8f | -12.0791 | -51.2407 | 2026-05-15 00:40:00 | METOP-B | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 99dd2bb1-c20f-3cee-94d6-4d13ca0d9e05 | -11.308 | -54.027302 | 2026-05-15 00:40:00 | METOP-B | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 78d880e1-02fb-31d5-b333-907cd366b3ae | -10.6623 | -49.702999 | 2026-05-15 00:40:00 | METOP-B | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 68052fb3-d9e4-3f97-ae4b-b1c8cd97e4f9 | -10.6689 | -49.688099 | 2026-05-15 00:40:00 | METOP-B | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 7c706f09-a7e1-338a-9e7f-1f9c4a3149b1 | -11.1791 | -55.916698 | 2026-05-15 00:40:00 | METOP-B | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 3d2275bf-4cdc-3e30-9bc6-cf2890c24b10 | -11.9422 | -54.0937 | 2026-05-15 00:40:00 | METOP-B | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a8263992-f9f6-368e-8cdc-04ac17d8443f | -10.6659 | -49.675701 | 2026-05-15 00:40:00 | METOP-B | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 4c9a843d-cbbe-3ed4-bd63-5e6865f614d2 | -11.9405 | -54.086498 | 2026-05-15 00:40:00 | METOP-B | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 19ff34c1-8cb1-3eeb-9568-4d72f8c703da | -8.5405 | -45.975101 | 2026-05-15 00:40:00 | METOP-B | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 1a1589d8-3d22-3fe9-b331-ef448f39b7ce | -10.672 | -49.7005 | 2026-05-15 00:40:00 | METOP-B | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| eadd6b3a-1234-3979-9831-a05626dd4b75 | -8.7261 | -48.338001 | 2026-05-15 00:40:00 | METOP-B | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| aa19e6df-a981-3b76-8bf6-ff88ef8a04e7 | -19.201 | -49.117699 | 2026-05-15 00:40:00 | METOP-B | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| a46d9ec8-d051-3659-8656-db68ad3761ca | -14.1777 | -52.867001 | 2026-05-15 00:40:00 | METOP-B | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| fadd2ec5-39b9-3a0a-89e0-5bbc069d07dd | -9.2976 | -45.487701 | 2026-05-15 00:40:00 | METOP-B | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| c1c1d5b1-abe6-3da5-b3dd-823c1ed07cfa | -11.1776 | -55.909698 | 2026-05-15 00:40:00 | METOP-B | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 078048e0-f73a-328f-8571-965c47a27b76 | -8.0947 | -44.1456 | 2026-05-15 00:50:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 73.0 |
| 2203fcb6-4891-3549-8b83-880ada31923d | -15.6537 | -47.9272 | 2026-05-15 00:50:00 | GOES-19 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 55.3 |
| 68746300-9484-38b5-ab5b-093e1ba7e678 | -8.7211 | -48.3222 | 2026-05-15 00:50:00 | GOES-19 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 67.2 |
| df9a911e-7cb1-34bb-9f71-578633fd61a5 | -15.6537 | -47.9272 | 2026-05-15 01:00:00 | GOES-19 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 81.0 |
| e97d4403-a6ab-39c6-9cbb-81167c8f2095 | -15.6537 | -47.9272 | 2026-05-15 01:10:00 | GOES-19 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 82.8 |
| 9561154c-47cf-3371-823d-778fa51ca211 | -14.1802 | -52.8689 | 2026-05-15 01:10:00 | METOP-C | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| f5631d1f-ec47-36d7-8f0d-027306d33f3f | -19.1982 | -49.1315 | 2026-05-15 01:10:00 | METOP-C | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 2e17539f-54ee-31a5-8f9a-751429a86e71 | -9.146 | -49.840199 | 2026-05-15 01:10:00 | METOP-C | CASEARA | TOCANTINS | Brasil | 1703909 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 5831159a-03ce-3383-9197-aff76233b4a9 | -11.3123 | -54.038799 | 2026-05-15 01:10:00 | METOP-C | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c0cce964-a39b-3127-ad17-3f4d56ae621d | -10.6707 | -49.6982 | 2026-05-15 01:10:00 | METOP-C | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| ba7932b8-58f4-30d1-9139-f6e4cd965fab | -9.3122 | -45.480099 | 2026-05-15 01:10:00 | METOP-C | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 7a59fe53-f1e6-3c13-a541-349150c16829 | -15.6481 | -47.918598 | 2026-05-15 01:10:00 | METOP-C | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | nan |
| fdb7f680-1a6e-3291-80d3-3dfb948343e4 | -11.3107 | -54.0317 | 2026-05-15 01:10:00 | METOP-C | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 01f27205-2080-33bf-afe3-30da70395738 | -19.195801 | -49.121899 | 2026-05-15 01:10:00 | METOP-C | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 0d9d7a37-3fbd-37a0-add2-9d102aadf384 | -12.0835 | -51.255901 | 2026-05-15 01:10:00 | METOP-C | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| c851e00c-8884-3cc5-b2bc-2a9043ac887e | -15.6384 | -47.9212 | 2026-05-15 01:10:00 | METOP-C | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | nan |
| 79881431-b135-3703-a2ad-60715d055026 | -15.6513 | -47.931301 | 2026-05-15 01:10:00 | METOP-C | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | nan |
| 26c15652-f715-3651-8b23-2adc27d1c5fc | -10.6805 | -49.695801 | 2026-05-15 01:10:00 | METOP-C | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| a7399a78-d380-3712-8281-09ea3bcb6e73 | -12.0813 | -51.246899 | 2026-05-15 01:10:00 | METOP-C | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 4f4671e7-8a72-3f10-8774-2e753add8211 | -15.6416 | -47.933899 | 2026-05-15 01:10:00 | METOP-C | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | nan |
| cff9157d-548a-3c29-a52d-46c335950aeb | -9.5721 | -40.3475 | 2026-05-15 01:30:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 73.1 |
| 08e90abd-de9e-3bda-963b-d9a89542bc2c | -15.6537 | -47.9272 | 2026-05-15 02:10:00 | GOES-19 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 78.0 |
| e73e8223-b851-36cc-9ee8-4b3c4b0f7399 | -15.6537 | -47.9272 | 2026-05-15 02:20:00 | GOES-19 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 99.9 |
| b94c5c96-6313-3531-9e3f-998efe7c14a8 | -15.6537 | -47.9272 | 2026-05-15 02:30:00 | GOES-19 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 87.1 |
| 32074786-f36d-3d03-b6fe-509cae98bb34 | -15.6341 | -47.9307 | 2026-05-15 02:30:00 | GOES-19 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 65.6 |
| 5336791a-a421-32fb-afce-e4418545cf4c | -15.6537 | -47.9272 | 2026-05-15 02:40:00 | GOES-19 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 63.5 |
| 008a54fb-ae58-3627-a0da-c9040b196eef | -9.553 | -40.3503 | 2026-05-15 03:00:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 82.3 |
| c28e0add-0a61-363c-9b0b-39b2d5f4d0d2 | -9.5721 | -40.3475 | 2026-05-15 03:00:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 70.2 |
| ebaaa173-0672-3002-ae1d-69a17c18fdb0 | -8.54795 | -45.98143 | 2026-05-15 03:45:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 37625670-0608-3dfc-90de-bd724bec283a | -10.56018 | -42.43403 | 2026-05-15 03:45:00 | NOAA-21 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 2c249eff-7f5d-3e67-93c7-e2ecdfee27e2 | -12.04679 | -45.28348 | 2026-05-15 03:45:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 72fc9ae8-df6b-3ec9-9a68-ed60993134a0 | -10.66839 | -49.69985 | 2026-05-15 03:45:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 7b6e9028-d2ad-358f-853b-9d706041c026 | -10.67032 | -49.69301 | 2026-05-15 03:45:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 85da3e02-6b02-3bb0-a049-b20f355f2a14 | -10.66562 | -49.71303 | 2026-05-15 03:45:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 7c6fa965-3a33-3a4c-aa8e-1bbbb410bfdc | -11.74105 | -44.52015 | 2026-05-15 03:45:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 335eea2d-2c76-3f78-a892-71049c997c54 | -8.55218 | -45.99056 | 2026-05-15 03:45:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 06133bba-7a7c-3d12-b246-f9207dc3fa1e | -12.47752 | -45.44179 | 2026-05-15 03:45:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4d2af87a-5116-3c3a-84b6-b88e225c4b0e | -6.38682 | -44.17163 | 2026-05-15 03:45:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5da89601-1a94-3ebe-8c48-c8a5ccc86e8d | -10.39239 | -46.66456 | 2026-05-15 03:45:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8f0b2c73-c442-3ccb-bdc8-9cc9c6a15b4b | -12.50186 | -43.767 | 2026-05-15 03:45:00 | NOAA-21 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 2817ce75-1152-375f-ae96-f502375f44ab | -8.55294 | -45.98649 | 2026-05-15 03:45:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| daee03ae-276d-39ca-b6a9-0e4a2dcd4fbf | -10.66898 | -49.69961 | 2026-05-15 03:45:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 1a0fd2f4-9d07-3253-8941-6c4b1c5e4c95 | -10.55971 | -42.43451 | 2026-05-15 03:45:00 | NOAA-21 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 2.1 |
| e94ddf50-752f-3107-abad-ce28441d301f | -8.54222 | -45.98036 | 2026-05-15 03:45:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 391509a7-0a83-38f5-b320-57eebef60ac8 | -10.30805 | -46.26287 | 2026-05-15 03:45:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9003ec6c-0ae7-3f53-bd25-7e9eb77506e3 | -14.08337 | -42.11942 | 2026-05-15 03:45:00 | NOAA-21 | LAGOA REAL | BAHIA | Brasil | 2918753 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 5e1d52a9-69b9-3109-acb3-9784ce122d80 | -12.60298 | -44.50668 | 2026-05-15 03:45:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 3880cd5a-76ad-32f6-9b5d-0d10cbd57cd4 | -12.85266 | -43.75767 | 2026-05-15 03:45:00 | NOAA-21 | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 13.6 |
| de56bfe9-808a-3656-9c86-7e4af892dc16 | -8.089 | -44.15403 | 2026-05-15 03:45:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| cc4fb575-debd-39d1-8b80-e1ee6b69d2a6 | -8.09247 | -44.16407 | 2026-05-15 03:45:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 187c856c-dfa8-39cd-981e-25c5f003933f | -12.50097 | -43.77194 | 2026-05-15 03:45:00 | NOAA-21 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 26b3fcce-3c1e-32bb-978c-01b85f0ccc63 | -12.47234 | -45.44086 | 2026-05-15 03:45:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e0f53013-cb4c-3f9d-b9ae-5e3df04cc496 | -10.66976 | -49.69328 | 2026-05-15 03:45:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 3093dde7-75e7-373e-a254-69c052b55582 | -8.70114 | -47.97458 | 2026-05-15 03:45:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6a77ba3e-e647-39f4-8063-50f66c6f8cc6 | -8.08583 | -44.1587 | 2026-05-15 03:45:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6cd35952-416e-334f-9947-02e8591547ac | -8.50295 | -46.38474 | 2026-05-15 03:45:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e5cebd17-ab7b-38b9-8a41-6c8748495333 | -12.48271 | -45.44273 | 2026-05-15 03:45:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 343a4ebf-45d5-376d-8aab-5ff31f340356 | -8.08845 | -44.15708 | 2026-05-15 03:45:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4f650bfe-5a21-3b16-bc3c-f276f0ba5e25 | -6.39095 | -44.17913 | 2026-05-15 03:45:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 0f8c6959-7028-3e2f-a330-5890f977fb69 | -6.39153 | -44.1758 | 2026-05-15 03:45:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 13031087-1b7e-32ba-874f-c8a43a6a6932 | -10.95646 | -44.17648 | 2026-05-15 03:45:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 8ccbbfac-dd02-363e-8c2c-2f05cfe1b27d | -11.73998 | -44.52584 | 2026-05-15 03:45:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 6.8 |


[Clique aqui para ver as próximas entradas](README2.md)
