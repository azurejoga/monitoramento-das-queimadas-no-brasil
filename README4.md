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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ac221b94-8e45-325a-ace7-c2c5bde05a52 | -6.9109 | -60.07021 | 2026-08-22 00:28:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 7b427c98-3ec9-3f4e-9cbc-021b72411ebb | -11.13981 | -49.03767 | 2026-08-22 00:28:00 | TERRA_M-M | CRIXÁS DO TOCANTINS | TOCANTINS | Brasil | 1706258 | 17 | 33 | nan | nan | nan | Cerrado | 24.8 |
| 18169b97-8afb-39b1-9169-c32206c57810 | -8.9997 | -50.7455 | 2026-08-22 00:28:00 | TERRA_M-M | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 52.7 |
| 185c6272-0f30-31f4-90a6-068daa250c99 | -6.6756 | -58.74799 | 2026-08-22 00:28:00 | TERRA_M-M | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 15.8 |
| 4c401cb7-afcb-3718-bda5-6c8919aaa102 | -8.68179 | -54.73693 | 2026-08-22 00:28:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 8504c099-4c28-321e-b205-0b35d60fcb97 | -6.80309 | -58.61948 | 2026-08-22 00:28:00 | TERRA_M-M | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 20.1 |
| 59a86563-30af-35f3-9530-65c56652522d | -9.19632 | -59.45086 | 2026-08-22 00:28:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 18.5 |
| da67e3f2-c657-36c1-995a-6256efc81f66 | -5.80485 | -57.55341 | 2026-08-22 00:28:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 12.4 |
| 5a1173a1-d538-3ce3-85e8-df490785e1f1 | -8.02477 | -51.80204 | 2026-08-22 00:28:00 | TERRA_M-M | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 14.5 |
| cc70619e-688c-3de0-828e-71244e0d7e73 | -6.23118 | -55.48617 | 2026-08-22 00:28:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 539e72b1-bbe9-3029-8ad4-4c3882d433c6 | -9.17674 | -59.46685 | 2026-08-22 00:28:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 119.0 |
| 48a8ba22-9c45-36b5-a471-84fd16a5a789 | -11.16413 | -54.02729 | 2026-08-22 00:28:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 23.0 |
| f89c7081-44f5-3041-9ac4-a0226023b182 | -6.72743 | -48.11923 | 2026-08-22 00:28:00 | TERRA_M-M | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Amazônia | 108.7 |
| c8f0d15c-9d9e-39b2-b159-c7a6d9d29efe | -6.5747 | -58.9818 | 2026-08-22 00:28:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 10.7 |
| ec18c866-233d-3a64-9698-5c9540a218c6 | -8.63522 | -54.74078 | 2026-08-22 00:28:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| e503d840-0391-34ce-914d-530c019567ee | -5.75139 | -53.57885 | 2026-08-22 00:28:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| cb283228-295e-3ead-b936-2b28f854c25c | -10.27521 | -50.35136 | 2026-08-22 00:28:00 | TERRA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 68.9 |
| d040a60d-592d-3545-9f48-e02582bfd69d | -6.16331 | -55.4506 | 2026-08-22 00:28:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 90bcffb5-342d-3b39-bb10-cc5102baec9f | -8.63398 | -54.73183 | 2026-08-22 00:28:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 53713486-ae48-360e-8b3a-533ecc37a9e2 | -6.81936 | -59.6658 | 2026-08-22 00:28:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 61.3 |
| 596f27f8-e089-3d6a-8f3d-fbe8cee986d3 | -5.9671 | -51.95864 | 2026-08-22 00:28:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 28.8 |
| c0bf490c-3a59-3f68-adc2-da7a7b4e23ec | -6.83165 | -56.83308 | 2026-08-22 00:28:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 8b698b60-1603-38c5-9f9b-cedc4e2d4795 | -10.25296 | -50.35495 | 2026-08-22 00:28:00 | TERRA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 211.7 |
| f4e4ea68-6c0f-37cc-a503-920cc227a2e1 | -8.56061 | -54.72412 | 2026-08-22 00:28:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| a9cdb16f-e3ca-3ea6-bd0e-0b1b8d049c70 | -6.78622 | -59.41985 | 2026-08-22 00:28:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 20.1 |
| 68bd3948-a103-3c0c-b056-b7740624397c | -8.15707 | -46.71459 | 2026-08-22 00:28:00 | TERRA_M-M | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 46.6 |
| 0e202603-6e94-397a-992b-a5a44921a068 | -6.76904 | -59.44663 | 2026-08-22 00:28:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 59.7 |
| 37ce49fb-6559-36a9-8d0c-11245a2de349 | -8.61887 | -54.68814 | 2026-08-22 00:28:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 17.5 |
| e4d318ff-2884-3de1-ae22-d696ddc2be46 | -9.1722 | -59.47309 | 2026-08-22 00:28:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 43.2 |
| 2b39d691-7dc4-3b8e-b894-a1af2437de94 | -8.62512 | -54.73308 | 2026-08-22 00:28:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| ced1022b-6e91-3102-a386-cb0171c9c24c | -6.23143 | -55.42292 | 2026-08-22 00:28:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 12.7 |
| b5e38b91-8bdd-3610-a240-38ecf2db9936 | -6.13888 | -57.84673 | 2026-08-22 00:28:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| f661cb5f-7a1e-3759-acce-b59e9fce24b4 | -8.59227 | -54.69195 | 2026-08-22 00:28:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 98ed884c-88f7-3bc9-a20d-a0a3c43b8719 | -6.75642 | -58.66505 | 2026-08-22 00:28:00 | TERRA_M-M | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 896.5 |
| e830aab9-1c23-3e4b-a59e-d6e2e2e29d1b | -9.04508 | -60.44608 | 2026-08-22 00:28:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 21.9 |
| ce492285-5cca-3d3c-b347-1879396008b9 | -6.76224 | -58.70839 | 2026-08-22 00:28:00 | TERRA_M-M | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 11.5 |
| 05ad2e21-e9a4-30ec-ac09-db489379771a | -6.88948 | -55.70985 | 2026-08-22 00:28:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 3f332eaf-68a8-3f7f-a162-1e9e71009593 | -10.26409 | -50.35315 | 2026-08-22 00:28:00 | TERRA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 147.6 |
| 02407ddc-0403-37c6-ba8a-7aacd052e32a | -6.54189 | -58.51101 | 2026-08-22 00:28:00 | TERRA_M-M | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 11.9 |
| a9f53ad9-2178-320e-87bc-b32c394b7c19 | -6.13469 | -59.9153 | 2026-08-22 00:28:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 14.4 |
| 51e980d4-2ddb-3bcf-8469-75ae4fdb9498 | -6.41799 | -52.73257 | 2026-08-22 00:28:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 12.4 |
| 9ee81f17-6d03-35f5-8db7-5ad919c8a04d | -7.36601 | -55.69241 | 2026-08-22 00:28:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 47.9 |
| ae5fcc18-f9c5-3ec8-81a7-4796c2134a1b | -8.5392 | -54.8428 | 2026-08-22 00:28:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 5f6e1783-ba59-36c6-a943-4af0be844ed2 | -6.63349 | -53.36733 | 2026-08-22 00:28:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| dc77bb65-c9c5-3df0-96b2-41c8e50a7791 | -7.67619 | -61.12737 | 2026-08-22 00:28:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 14.5 |
| 7f09db4a-897c-3167-978a-885b11564bd9 | -8.99535 | -50.71725 | 2026-08-22 00:28:00 | TERRA_M-M | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 38.7 |
| ee07f71c-07fc-3edb-9a9b-c5d43da86a93 | -6.08145 | -59.96745 | 2026-08-22 00:28:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 8535abde-2cdf-37d5-8bd2-ef843ec770fe | -8.54045 | -54.85175 | 2026-08-22 00:28:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 3cd5c57d-bc98-3555-9d15-2dee86103553 | -6.75787 | -58.67584 | 2026-08-22 00:28:00 | TERRA_M-M | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 222.3 |
| 9373a253-a225-3e0b-a487-6d1f9f2483d4 | -6.80747 | -59.43565 | 2026-08-22 00:28:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 35.9 |
| 3b011fec-a9a4-32b1-beab-b54ab3e7c23d | -8.53036 | -54.84408 | 2026-08-22 00:28:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 14.8 |
| 1ecca2e5-d092-39e3-9d8a-4b074c8b9662 | -8.55053 | -54.85949 | 2026-08-22 00:28:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| cd5e7dd3-4478-3d53-91a3-333dd67c94bf | -8.89891 | -60.55665 | 2026-08-22 00:28:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 55.6 |
| cc61fba3-3b53-3015-b60b-81999a357320 | -10.51975 | -50.82014 | 2026-08-22 00:28:00 | TERRA_M-M | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 19.7 |
| de4fdae8-b541-3b12-9a91-7ac71bca0ca9 | -10.50908 | -50.82193 | 2026-08-22 00:28:00 | TERRA_M-M | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 12f01a25-6512-3429-b474-24667a37d023 | -6.93381 | -59.30264 | 2026-08-22 00:28:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 13.5 |
| cce7a01d-7039-31d8-9f95-4d8c4e8f1ed0 | -8.52538 | -54.80826 | 2026-08-22 00:28:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 60.5 |
| 23888d31-642c-3d3d-88e2-40a866bb1a9f | -6.77972 | -58.66668 | 2026-08-22 00:28:00 | TERRA_M-M | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 34.6 |
| b85cf742-216b-3ec0-b3b9-d158ae9f184e | -10.94612 | -51.40824 | 2026-08-22 00:28:00 | TERRA_M-M | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Cerrado | 18.0 |
| 192ec81f-b34a-35b0-9bd3-152ce54e4681 | -6.89827 | -55.7086 | 2026-08-22 00:28:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 14.8 |
| 21c2ba46-aa80-3cb6-a2e2-afc05663e328 | -6.22236 | -55.48738 | 2026-08-22 00:28:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 6f5ce619-c94c-3738-9804-83f22e3a4956 | -6.64374 | -56.34366 | 2026-08-22 00:28:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 28233a86-4369-3046-abc4-72d3c3307d2a | -6.81612 | -59.42226 | 2026-08-22 00:28:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 78.9 |
| 34110812-912a-3d4d-b680-7d366fd2f2d1 | -10.86417 | -51.05699 | 2026-08-22 00:28:00 | TERRA_M-M | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 12299bfa-8a92-3bff-ba0d-d43fced7f0d4 | -6.25676 | -55.39526 | 2026-08-22 00:28:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 28.5 |
| 4dfd270c-c4a7-3ef8-9a17-79e13a3c331e | -10.52432 | -50.77794 | 2026-08-22 00:28:00 | TERRA_M-M | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 19.6 |
| 58aa5ea5-d71c-3af8-ad6f-ce5c2ac1e9d4 | -11.81793 | -56.59355 | 2026-08-22 00:28:00 | TERRA_M-M | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 18.9 |
| 50623588-3bc5-31de-8dd7-4c1cb0c21118 | -6.80451 | -58.63027 | 2026-08-22 00:28:00 | TERRA_M-M | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 18.0 |
| 49617ffe-fd77-3645-8be0-9c0a8c4ab81b | -9.17048 | -59.45993 | 2026-08-22 00:28:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 179.0 |
| 3e4487c9-fbb3-388b-9242-b67882848fa0 | -7.59729 | -61.22932 | 2026-08-22 00:28:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 13.5 |
| fba90289-1271-3db3-a455-21184d5ce98d | -9.16705 | -59.43368 | 2026-08-22 00:28:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 85abeec6-479a-30c6-8bcb-14031ced4fb0 | -8.5324 | -55.33036 | 2026-08-22 00:28:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 16.9 |
| 515c130e-eb65-3c82-b47a-5b16b012c7fe | -6.38178 | -56.10512 | 2026-08-22 00:28:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| b979087e-c870-3c28-a115-1dac64071b26 | -6.7308 | -48.11214 | 2026-08-22 00:28:00 | TERRA_M-M | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Amazônia | 40.7 |
| 5f6c3369-841b-30ae-9ff1-fc6875a25afa | -8.5897 | -54.73823 | 2026-08-22 00:28:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| c48dbd44-f3d6-3027-8838-8a37ad2161f1 | -8.51903 | -54.82746 | 2026-08-22 00:28:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 39.9 |
| de458ebe-673b-3581-9e31-da170914b203 | -7.02776 | -59.55613 | 2026-08-22 00:28:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 98b1fca3-636b-3ca3-a672-f9668dce9887 | -10.87837 | -50.22637 | 2026-08-22 00:28:00 | TERRA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 19.3 |
| 755cb9f9-63d2-3e9f-94d1-6a38c24a9167 | -6.77869 | -55.70459 | 2026-08-22 00:28:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 15.3 |
| 37596288-9405-3c68-8e4e-23c4ea398a97 | -6.88043 | -56.6457 | 2026-08-22 00:28:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 5f133ec7-8a80-39c4-881b-20f2b44c3447 | -8.62773 | -54.68685 | 2026-08-22 00:28:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 15.7 |
| 9dfba92c-924f-32ff-a76f-81dc99eabd2a | -9.4066 | -60.31314 | 2026-08-22 00:28:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 16.4 |
| 1db5eb2e-6f83-3bbc-87f5-d0f2d12248a7 | -9.21314 | -60.77813 | 2026-08-22 00:28:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 24.9 |
| 6d00f876-f5fc-37d2-b5c3-d8675506bec6 | -6.22308 | -55.62229 | 2026-08-22 00:28:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 23.6 |
| cb57c431-e297-3d75-8f57-4f555091e00b | -6.64495 | -56.35247 | 2026-08-22 00:28:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 8376b0f5-f550-3964-818c-a08388598806 | -10.69604 | -50.31322 | 2026-08-22 00:28:00 | TERRA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 51.0 |
| f5bf17ee-9951-3f27-9e99-66797ed2601c | -9.21517 | -59.77884 | 2026-08-22 00:28:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 13.8 |
| 8d68b65b-f122-35db-8c6f-73b08192b890 | -6.09025 | -59.95318 | 2026-08-22 00:28:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 20.6 |
| 621069fa-dec8-3dcf-a9ca-fb7bff41e3c3 | -8.52912 | -54.83514 | 2026-08-22 00:28:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 456.8 |
| 9d01d6c8-c9a8-3d83-b36c-4039d0f15352 | -10.7584 | -50.26654 | 2026-08-22 00:28:00 | TERRA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 11.1 |
| ec214a21-35ba-3618-9ef8-32524aa1be30 | -8.54169 | -54.8607 | 2026-08-22 00:28:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 89.1 |
| b04ac17a-d45f-33ac-9360-483c5692adb4 | -6.35378 | -58.33761 | 2026-08-22 00:28:00 | TERRA_M-M | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 8524dc0a-4976-36ee-804a-a7a20fcdb915 | -6.43426 | -54.95619 | 2026-08-22 00:28:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 59.8 |
| 96ce7b23-ebb4-364e-a09b-2d8c782058c1 | -10.7473 | -50.26834 | 2026-08-22 00:28:00 | TERRA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 33.0 |
| af556023-29b1-35fd-94a7-e05fcf2120c8 | -6.75498 | -58.6543 | 2026-08-22 00:28:00 | TERRA_M-M | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 316.3 |
| 2b2731c8-07bf-3549-898c-b55486048c51 | -6.81455 | -59.41019 | 2026-08-22 00:28:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 53.5 |
| 0e43117c-b041-31af-a536-7d13876e9c39 | -6.9354 | -59.31458 | 2026-08-22 00:28:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 48.3 |
| dfb71f3b-19b0-3aed-b8f9-8069f8aed23c | -5.9951 | -57.8002 | 2026-08-22 00:28:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| b7dc17f0-32a9-33a3-841f-6f62bfab8f05 | -6.77065 | -59.45872 | 2026-08-22 00:28:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 11.4 |
| 56290e55-89c5-3df9-9e88-bde568620fdc | -6.79936 | -58.98547 | 2026-08-22 00:28:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.7 |


[Clique aqui para ver as próximas entradas](README5.md)
