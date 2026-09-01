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

## Dados Diários - Página 86

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 15cc5d7d-f559-3938-935d-ba3bea470787 | -14.41068 | -52.50085 | 2026-09-01 05:38:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 6bef8ee2-ce0f-3c9b-a437-a675ec5fbd75 | -14.40398 | -52.50472 | 2026-09-01 05:38:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| dd11b706-3e4c-368c-a4ea-487f41dba9b6 | -14.38972 | -52.53016 | 2026-09-01 05:38:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 2f78f448-2458-3e1b-83e8-46ff418d6a55 | -15.251 | -53.85789 | 2026-09-01 05:38:00 | NOAA-20 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 40e6484a-a4d4-38ff-bce3-d26a52b98a20 | -14.38844 | -52.53276 | 2026-09-01 05:38:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| fb1182c5-f532-3517-aa7f-6bd1eced6595 | -11.49666 | -60.58635 | 2026-09-01 05:38:00 | NOAA-20 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ae947421-0e9c-3534-ad9b-19d567ebf252 | -14.38863 | -52.53981 | 2026-09-01 05:38:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 12bbc761-d71e-34dc-b320-e3f331e30534 | -15.24658 | -53.84507 | 2026-09-01 05:38:00 | NOAA-20 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| fecc00c2-f7a7-344b-9bb5-4f72faa48dc3 | -14.38946 | -52.52307 | 2026-09-01 05:38:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 59d7d6de-1e61-3781-bf64-fc71c532c471 | -14.39813 | -52.51129 | 2026-09-01 05:38:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 6.3 |
| df313f9e-8cf6-3cdb-85dc-6bd0b13515dd | -15.24775 | -53.88702 | 2026-09-01 05:38:00 | NOAA-20 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5aeeff63-6745-383b-a3ea-c359c2024315 | -15.25145 | -53.85381 | 2026-09-01 05:38:00 | NOAA-20 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cc11724a-0cf4-3d89-8572-39f0536ca0b0 | -16.04706 | -54.38078 | 2026-09-01 05:38:00 | NOAA-20 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 11.4 |
| a53120cb-e25d-30a3-aa45-7dfa4a08bfd8 | -14.38302 | -52.53388 | 2026-09-01 05:38:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| c688db70-3d09-3e58-a97b-aad257c18be2 | -10.25151 | -68.21581 | 2026-09-01 05:38:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c7a59386-1319-3870-af32-0ee6cc547d5f | -18.24505 | -52.70902 | 2026-09-01 05:38:00 | NOAA-20 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3ac37e74-9c00-3469-b1df-445a17bade23 | -16.0466 | -54.38492 | 2026-09-01 05:38:00 | NOAA-20 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 16.1 |
| 602d63e3-daf9-3706-a2b2-a54ed116503b | -14.43506 | -52.50816 | 2026-09-01 05:38:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3374b79c-fa38-34a2-82d3-b9873bd5b6fd | -18.24942 | -52.73086 | 2026-09-01 05:38:00 | NOAA-20 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| af882084-7058-3c69-805b-c4573b4f3c79 | -14.39137 | -52.51548 | 2026-09-01 05:38:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 654af76f-cf9c-354c-b2b5-93d655658499 | -14.67378 | -53.54441 | 2026-09-01 05:38:00 | NOAA-20 | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a68fc5a5-5bf6-330a-86bd-50077d54c1b4 | -15.86845 | -56.47577 | 2026-09-01 05:38:00 | NOAA-20 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e3534548-acf9-3e27-9be0-8f4a2e45057c | -17.22335 | -53.26659 | 2026-09-01 05:38:00 | NOAA-20 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fe6881ee-3bf1-3c24-a946-0f02221c2952 | -15.75793 | -56.09826 | 2026-09-01 05:38:00 | NOAA-20 | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Pantanal | 5.4 |
| a3e47cb4-307b-3a0c-badd-465efd086434 | -14.26168 | -52.88995 | 2026-09-01 05:38:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0164bdd8-d0fe-33dc-9d6d-3985656fb4f8 | -14.4122 | -52.4982 | 2026-09-01 05:38:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 5.4 |
| a983f84b-07da-3663-a68d-95976668a7b3 | -15.48972 | -56.00154 | 2026-09-01 05:38:00 | NOAA-20 | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2015835f-03ff-3ea7-a51c-c8d207f43212 | -14.66748 | -53.54773 | 2026-09-01 05:38:00 | NOAA-20 | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 3651d09f-f81b-34ed-bd87-911c29ef41a5 | -15.63941 | -56.37642 | 2026-09-01 05:38:00 | NOAA-20 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 6288f39f-4f56-30bb-bad5-651618ed5f58 | -18.25631 | -52.74318 | 2026-09-01 05:38:00 | NOAA-20 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 2de49fb5-ae74-3848-ac26-792862ff26f6 | -15.60569 | -56.3885 | 2026-09-01 05:38:00 | NOAA-20 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 5e0a3b77-fc58-3dfe-9ec7-b5d1eeee0b3b | -15.43497 | -52.68518 | 2026-09-01 05:38:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 0b3e8584-d3ec-390f-b95b-57597a1a76a5 | -14.25919 | -52.86831 | 2026-09-01 05:38:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| f54b083a-e5d8-3c12-a88e-e0f24dbf6ca5 | -14.38178 | -52.5364 | 2026-09-01 05:38:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1c821efe-55b1-3308-bb02-dffced37b543 | -16.5489 | -52.51417 | 2026-09-01 05:38:00 | NOAA-20 | DOVERLÂNDIA | GOIÁS | Brasil | 5207253 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c0d49dbf-8ba0-3464-a487-390e2f9bcb11 | -15.48833 | -56.01355 | 2026-09-01 05:38:00 | NOAA-20 | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 9ff8956f-e0d6-3781-ba56-4710c16b15f8 | -10.08734 | -68.29584 | 2026-09-01 05:38:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f38a45c7-e183-3383-82ec-d63026fcccaf | -11.49605 | -60.59038 | 2026-09-01 05:38:00 | NOAA-20 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fab775f5-cd61-3f71-81a9-9837757c90f6 | -14.44184 | -52.5037 | 2026-09-01 05:38:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c10931b5-4db3-371e-a65a-9326eeb49054 | -14.38809 | -52.54462 | 2026-09-01 05:38:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8b6c93a3-95b9-38de-88c4-b50ef28ae5b6 | -15.76435 | -56.08725 | 2026-09-01 05:38:00 | NOAA-20 | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Pantanal | 6.9 |
| 2b16d340-a5fd-3045-8f22-b075fd3c18f8 | -14.26433 | -52.86706 | 2026-09-01 05:38:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| ba4538e3-be20-3e9e-8622-714bcdd99dca | -10.07475 | -68.26913 | 2026-09-01 05:38:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 769a9749-f0db-33b3-be2b-e8c1ba63ad3e | -14.2567 | -52.89128 | 2026-09-01 05:38:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3792890f-0a08-34ed-bd0d-b8113209af0c | -16.35786 | -51.02164 | 2026-09-01 05:38:00 | NOAA-20 | ISRAELÂNDIA | GOIÁS | Brasil | 5210307 | 52 | 33 | nan | nan | nan | Cerrado | 10.0 |
| b72a2cd1-ea73-35e4-b104-502ba93a52dc | -14.13545 | -52.7984 | 2026-09-01 05:38:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| a7cebdac-1e9b-35d2-9130-008b74f7195d | -15.01569 | -52.7676 | 2026-09-01 05:38:00 | NOAA-20 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c217f05f-d320-3600-a3d9-38b64542a767 | -18.2489 | -52.73631 | 2026-09-01 05:38:00 | NOAA-20 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b29c56c3-db3a-3130-8b21-879b83a820a6 | -14.37686 | -52.53283 | 2026-09-01 05:38:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 55692c72-c889-37d6-8ef0-0cbe5cf26ebc | -14.1299 | -52.79301 | 2026-09-01 05:38:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1849136f-818c-33d5-97d8-6e689b8f8126 | -15.76935 | -56.08796 | 2026-09-01 05:38:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 6.9 |
| 50347130-6f0c-3012-aea6-3f7d8c30c2f3 | -13.3831 | -51.75176 | 2026-09-01 05:38:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 08b398ce-7d23-330d-9b29-151382dea3c5 | -14.2572 | -52.88668 | 2026-09-01 05:38:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 7b4bfe8c-38b0-37d0-b32d-438b53e60961 | -10.4363 | -67.84435 | 2026-09-01 05:38:00 | NOAA-20 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4af78e54-f994-35ff-9d4e-7797a483c134 | -10.07563 | -68.26806 | 2026-09-01 05:38:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2fc44555-c6b6-31c1-8593-1730e7352084 | -14.73337 | -53.59045 | 2026-09-01 05:38:00 | NOAA-20 | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0990ee7b-9bae-333e-b966-e4a39c04cbf4 | -15.24612 | -53.84923 | 2026-09-01 05:38:00 | NOAA-20 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6ec5c9ed-31a2-3867-ab2a-26127c0709ed | -14.40547 | -52.50201 | 2026-09-01 05:38:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 9fc3ff18-76d5-311a-b040-394c51d2591d | -14.4582 | -52.52665 | 2026-09-01 05:38:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b1feeb22-3428-33be-bdd9-b6b0b59cafe6 | -14.46508 | -52.52126 | 2026-09-01 05:38:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 88a94ba5-4870-373c-8310-306f14f0280f | -10.27705 | -68.86512 | 2026-09-01 05:38:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d0d5cc3f-e071-3261-844b-df3c9d1e7f80 | -14.3967 | -52.514 | 2026-09-01 05:38:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 414aebb3-f545-3ee2-bc15-d6d629f430ea | -16.54839 | -52.51927 | 2026-09-01 05:38:00 | NOAA-20 | DOVERLÂNDIA | GOIÁS | Brasil | 5207253 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8d0846f1-47c0-347b-a653-14b5d8b88c3e | -14.39026 | -52.52533 | 2026-09-01 05:38:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 5.5 |
| ae06a216-ae22-3f83-918e-a76d7717cd5a | -14.43563 | -52.50286 | 2026-09-01 05:38:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 451a7ac4-f60d-36f3-a51e-e44bf7bd38b9 | -16.35849 | -51.0153 | 2026-09-01 05:38:00 | NOAA-20 | ISRAELÂNDIA | GOIÁS | Brasil | 5210307 | 52 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 5e030cb6-7285-34ca-8dcd-14cb08ce263e | -14.72845 | -53.58153 | 2026-09-01 05:38:00 | NOAA-20 | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 5129fc47-c783-302c-820c-5088de902002 | -14.25616 | -52.88457 | 2026-09-01 05:38:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d2915c6d-e72f-3671-8a75-992c60ccaeaa | -10.13219 | -68.58601 | 2026-09-01 05:38:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 37973dd8-2b9e-3594-9653-a46c80b652bb | -14.50643 | -59.83373 | 2026-09-01 05:38:00 | NOAA-20 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 8e112fef-7d08-3cb4-a5a2-2983eecd45b0 | -18.25204 | -52.70364 | 2026-09-01 05:38:00 | NOAA-20 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| cb773453-70e8-39d6-a70d-6361b2b8274e | -11.52031 | -60.50121 | 2026-09-01 05:38:00 | NOAA-20 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2a45d288-a4d3-30e9-b4b6-e0342719e16b | -15.25191 | -53.84967 | 2026-09-01 05:38:00 | NOAA-20 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c65002c5-f930-30ad-964e-041581a13fc4 | -14.45937 | -52.51594 | 2026-09-01 05:38:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c3db1290-8cad-3aae-9725-ec64c321865e | -14.66166 | -53.54694 | 2026-09-01 05:38:00 | NOAA-20 | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3c89fad2-8c83-3e5f-8de7-1cefa03bc125 | -15.98293 | -55.95961 | 2026-09-01 05:38:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 5a34a9aa-2408-3e1c-bda6-5a1f67459db4 | -15.6475 | -50.1062 | 2026-09-01 05:40:00 | GOES-19 | GUARAÍTA | GOIÁS | Brasil | 5209291 | 52 | 33 | nan | nan | nan | Cerrado | 70.4 |
| b2bcd661-9308-34c4-9e6e-3036118da538 | -7.5895 | -60.4636 | 2026-09-01 05:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 39.3 |
| 9d4e1159-899e-3d1f-baf4-fb4b87102c32 | -10.3574 | -50.0171 | 2026-09-01 05:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 71.1 |
| ec706ec9-5551-3cb0-965e-4796fa1b6278 | -6.9552 | -55.635 | 2026-09-01 05:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 46.3 |
| df383273-63ba-33c0-93a0-f845ce6c1ab7 | -8.111 | -54.9684 | 2026-09-01 05:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 108.3 |
| f6768cd1-0c58-359e-ae75-bf3fc71ac39d | -8.1296 | -54.9672 | 2026-09-01 05:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 175.8 |
| a1741d26-a07c-31b8-9187-18bae7956526 | -8.1298 | -54.9471 | 2026-09-01 05:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 61.1 |
| 4a38093d-5ac0-33ef-8e7f-3c61c07a0d51 | -7.5894 | -60.4827 | 2026-09-01 05:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 46.7 |
| dbbb1288-ecba-3fd5-99e9-d4a6febb78d7 | -7.3487 | -60.5883 | 2026-09-01 05:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 55.6 |
| 3a23e40d-1bcc-3027-acd5-058e127cea9b | -7.571 | -60.4643 | 2026-09-01 05:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 44.0 |
| eac00119-cad7-3f62-9079-3023176457b0 | -7.5709 | -60.4835 | 2026-09-01 05:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 42.3 |
| f678c35c-74d8-3079-8667-7687bbdb7848 | -7.3487 | -60.5883 | 2026-09-01 05:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 64.3 |
| bb468a1c-12b1-3d9a-bece-17ad418e8bff | -7.5895 | -60.4636 | 2026-09-01 05:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 42.7 |
| 4d840e63-8a7b-312b-9378-f65b28105c11 | -8.111 | -54.9684 | 2026-09-01 05:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 61.5 |
| 7f1d4f63-0ece-3126-b093-787373c7823a | -7.571 | -60.4643 | 2026-09-01 05:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 46.6 |
| 9876ff14-ea10-30e4-8766-5025226124a8 | -7.5894 | -60.4827 | 2026-09-01 05:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 80.0 |
| 027ffce3-0e0a-30b8-8856-897040babf8a | -10.3574 | -50.0171 | 2026-09-01 05:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 62.1 |
| c5f2054a-fdc0-3297-a7e0-c638bbc5c803 | -7.5709 | -60.4835 | 2026-09-01 05:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 60.0 |
| 5a174ea5-4e28-32f9-a86a-b7671b8cff5a | -16.0547 | -54.3908 | 2026-09-01 05:50:00 | GOES-19 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 86.4 |
| a67a21f6-f931-3551-99f5-99f289e20a0f | -8.1296 | -54.9672 | 2026-09-01 05:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 98.8 |
| e955dbde-4bb4-3833-858f-7df5425a59f9 | -7.5894 | -60.4827 | 2026-09-01 06:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 75.3 |
| 3f10e0d5-4f6e-39d3-ac25-dd4f1dd31925 | -7.571 | -60.4643 | 2026-09-01 06:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 48.4 |
| 31a7af80-b01e-3215-9b56-e0b2a3b06d61 | -7.5709 | -60.4835 | 2026-09-01 06:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 65.3 |
| 631eda13-7278-3261-af6b-55b2944a5c9d | -16.0547 | -54.3908 | 2026-09-01 06:00:00 | GOES-19 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 45.9 |


[Clique aqui para ver as próximas entradas](README87.md)
