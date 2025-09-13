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

## Dados Diários - Página 16

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7f9b5359-5b76-3df1-9856-56902db18944 | -15.1161 | -52.5131 | 2025-09-13 02:30:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 61.8 |
| 6238ecd3-0614-3057-b094-14e0eecedac4 | -9.2505 | -51.2261 | 2025-09-13 02:30:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 83.4 |
| 03a60314-5206-3dd8-ad6a-49b4f54150a2 | -21.5912 | -48.419 | 2025-09-13 02:30:00 | GOES-19 | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 95.8 |
| c9336f56-2ff3-3ac6-9e1d-d252583d66aa | -11.7384 | -46.6231 | 2025-09-13 02:30:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 72.9 |
| b8c1a1f9-a54a-3046-ab86-e25a64d7135d | -9.2658 | -59.3997 | 2025-09-13 02:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 216.4 |
| 5f1c8bd2-8ee0-31c1-b2cd-c8a025a02b67 | -3.2305 | -47.135 | 2025-09-13 02:30:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 72.6 |
| 1852c233-d3ed-330b-90cf-92ec53c4830e | -11.4115 | -45.6241 | 2025-09-13 02:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 42.8 |
| 5700d4aa-9cd8-361c-a455-5aaf41dd3d08 | -3.2283 | -47.6154 | 2025-09-13 02:30:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 58.4 |
| 4f182899-121e-32a7-88ac-498f817e56a3 | -10.7853 | -50.5279 | 2025-09-13 02:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 79.6 |
| 930a5626-d337-3fe4-be01-781ab525c672 | -3.2282 | -47.6371 | 2025-09-13 02:30:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 102.7 |
| 01708cc6-f8b3-3a8d-8a2a-1153aa760e1e | -11.8472 | -50.5598 | 2025-09-13 02:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 83.2 |
| 5b8545fe-df73-36ce-8225-7dd31ca3867a | -11.4306 | -45.6215 | 2025-09-13 02:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 74.1 |
| 278c389d-38b5-3b31-8834-0b968c43a0cd | -11.0752 | -51.4731 | 2025-09-13 02:30:00 | GOES-19 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | 88.8 |
| 45fdf0e6-5714-35ba-afab-13a18bce7367 | -3.2321 | -46.7836 | 2025-09-13 02:30:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 56.2 |
| ab7ccdda-101e-3035-a8b8-274bca8fff6e | -9.5324 | -54.6277 | 2025-09-13 02:30:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 81.4 |
| 5b4ab359-6eaf-3820-87d9-7c9164e70210 | -10.7661 | -50.5513 | 2025-09-13 02:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 99.0 |
| e1d67601-92d3-3288-a610-f21f9be0d9ed | -11.7388 | -46.6005 | 2025-09-13 02:30:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 82.5 |
| 89c3ba3d-25a1-314b-89ac-aa1d753bccca | -11.1426 | -50.7028 | 2025-09-13 02:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 92.2 |
| 855dffff-87b0-3e91-b968-d8a850238957 | -9.5139 | -54.6089 | 2025-09-13 02:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 50.6 |
| d896c526-c3c1-39eb-8cdd-022a259a353d | -9.5006 | -55.9588 | 2025-09-13 02:30:00 | GOES-19 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 94.6 |
| 74e6c07d-7f9a-3ae5-8cc7-0e4c00763810 | -7.9488 | -46.8996 | 2025-09-13 02:40:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 45.3 |
| d60e01e2-ccc2-3089-978f-fbb84d2b82a7 | -9.5324 | -54.6277 | 2025-09-13 02:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 89.1 |
| b5f5e5ec-2a27-3529-a854-0cbc5ed251ce | -12.0056 | -47.7728 | 2025-09-13 02:40:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 75.9 |
| e2ef786c-1a5f-31c6-bc11-bef5e58e9dc1 | -9.2843 | -59.418 | 2025-09-13 02:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 91.2 |
| c7a8af07-2f3f-3273-b990-a64a3955c920 | -8.1004 | -50.1821 | 2025-09-13 02:40:00 | GOES-19 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 54.8 |
| 206c6de0-2b40-390a-9764-89f08fc195ed | -11.0942 | -51.4711 | 2025-09-13 02:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 140.6 |
| 17471dec-90f3-3c73-a9a2-fe9bc8c0be3b | -15.1359 | -52.4892 | 2025-09-13 02:40:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 61.3 |
| 4f905e84-87d1-3052-a844-351767d3cb58 | -9.2505 | -51.2261 | 2025-09-13 02:40:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 76.8 |
| bbf835c6-5964-3ece-abf9-c97cd5a334e9 | -15.1165 | -52.4918 | 2025-09-13 02:40:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 122.0 |
| 74ded307-6e95-3e20-b96c-1de56890e55d | -15.0967 | -52.5157 | 2025-09-13 02:40:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 56.0 |
| 5743fc2d-e295-3205-951c-3d5e18a95750 | -15.0971 | -52.4944 | 2025-09-13 02:40:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 72.5 |
| de1bf523-8023-32d5-88ec-2d436c42dd86 | -9.5137 | -54.6292 | 2025-09-13 02:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 107.8 |
| 4c2eb5bc-fa88-3d3c-8bd4-162f0c1e16fc | -9.232 | -51.2067 | 2025-09-13 02:40:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 71.9 |
| b09843fa-a777-3894-9ffd-4380d1b732f4 | -9.2656 | -59.4191 | 2025-09-13 02:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 175.8 |
| 149ebd57-4055-30cb-84a8-ec2432f685b4 | -11.1131 | -51.4692 | 2025-09-13 02:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 152.9 |
| 7cc48341-05c9-3c5a-a6e6-824bc898f418 | -11.4306 | -45.6215 | 2025-09-13 02:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 95.1 |
| fb3f2dd0-d1c1-3888-b580-128f62fd809e | -11.1318 | -51.4883 | 2025-09-13 02:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 93.3 |
| 8b4dc56a-90c6-35ec-9d93-619429eee44d | -11.431 | -45.5985 | 2025-09-13 02:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 183.0 |
| e69b19ff-93b0-353a-ac39-f55b20069af9 | -9.5135 | -54.6494 | 2025-09-13 02:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 51.0 |
| 41d16e1a-e0c4-361a-83fb-8314b8fd2eb3 | -9.247 | -59.4201 | 2025-09-13 02:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 63.9 |
| d6f986a2-73de-3619-8c20-4e2dbe724621 | -15.253 | -51.382 | 2025-09-13 02:40:00 | GOES-19 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 59.1 |
| 5f01f337-dc16-3f1b-8b65-e5149996ce54 | -11.0945 | -51.45 | 2025-09-13 02:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 94.7 |
| 0b836ad3-1c4e-32ad-88ac-98745942b805 | -16.3418 | -51.5434 | 2025-09-13 02:40:00 | GOES-19 | ARENÓPOLIS | GOIÁS | Brasil | 5202353 | 52 | 33 | nan | nan | nan | Cerrado | 95.4 |
| 57a05a0f-ff6d-3b3d-ba45-49aff275982b | -3.2321 | -46.7836 | 2025-09-13 02:40:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 62.0 |
| bba58717-dfc6-3bcf-9e13-2de617009ebb | -3.2282 | -47.6371 | 2025-09-13 02:40:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 99.9 |
| 4ad732fd-c0c2-3cd4-9515-fff9f1e62aa6 | -3.2305 | -47.135 | 2025-09-13 02:40:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 61.9 |
| 29279117-e923-326c-bfe8-b2bafffac99b | -11.7384 | -46.6231 | 2025-09-13 02:40:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 72.8 |
| 8f658508-5faa-35e6-95bd-9215b9a4c3ca | -11.1134 | -51.448 | 2025-09-13 02:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 114.7 |
| bc32b264-b332-376a-be16-dcdce34b16e5 | -9.5139 | -54.6089 | 2025-09-13 02:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 50.3 |
| 06f00109-e86f-3174-b969-ae319f1e69fa | -11.4115 | -45.6241 | 2025-09-13 02:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 57.1 |
| ab7bd7d0-de46-355d-b77d-bdd0b69ce5f8 | -9.2472 | -59.4007 | 2025-09-13 02:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 77.9 |
| 6c600bfe-34f0-3503-bf8c-089fb1c598ec | 0.6904 | -50.6481 | 2025-09-13 02:40:00 | GOES-19 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 53.0 |
| 2f80b1b5-6485-3b3e-8f4e-afc6e982ae3c | -11.8659 | -50.5791 | 2025-09-13 02:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 159.3 |
| b468b30a-9315-3724-8ded-37d9be29b954 | -9.2658 | -59.3997 | 2025-09-13 02:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 209.2 |
| 39195685-88d8-3e1b-be8d-773fe404e9ff | -13.0891 | -48.2663 | 2025-09-13 02:40:00 | GOES-19 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 65.6 |
| 505eb60f-0c7f-3a05-94e2-2975dcd16ab1 | -11.7388 | -46.6005 | 2025-09-13 02:40:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 93.1 |
| 1ed71724-8df3-35e8-b477-0511302a96a5 | -3.2283 | -47.6154 | 2025-09-13 02:40:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 63.3 |
| 2283411d-355b-3177-8d64-bf8912b72251 | -15.6145 | -47.9341 | 2025-09-13 02:40:00 | GOES-19 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 54.5 |
| 8b97524b-515f-32f9-bcc7-5ec1f407ade9 | -15.615 | -47.9114 | 2025-09-13 02:40:00 | GOES-19 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 53.7 |
| 15a67a13-a2cd-3ca8-9409-bea3c20d100a | -9.2508 | -51.2051 | 2025-09-13 02:40:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 64.8 |
| b206858d-e2f7-3da5-abdd-1b298dac2439 | -9.2317 | -51.2278 | 2025-09-13 02:40:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 69.4 |
| 9f7bd998-d62f-395e-a5ef-8b620d0d8a8c | -11.8468 | -50.5813 | 2025-09-13 02:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 135.6 |
| c148c96c-d01f-3187-a772-e91db3cdafe5 | -11.1508 | -51.4863 | 2025-09-13 02:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 115.0 |
| 9bbe9080-edf2-38dc-ab28-cb1c7c8abc05 | -12.006 | -47.7505 | 2025-09-13 02:40:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 127.9 |
| cb80e076-8585-35a4-a6ab-acac6a974cc5 | -9.2844 | -59.3986 | 2025-09-13 02:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 89.7 |
| 971febbc-ae08-3361-9c92-db1e647f87c6 | -16.3422 | -51.5217 | 2025-09-13 02:40:00 | GOES-19 | ARENÓPOLIS | GOIÁS | Brasil | 5202353 | 52 | 33 | nan | nan | nan | Cerrado | 90.4 |
| b9ad8fbd-d9c6-36c4-a45f-e1fdff3f45ea | -15.1161 | -52.5131 | 2025-09-13 02:40:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 95.1 |
| dde0eb2e-7db6-31b0-b52c-d27c05c0c470 | -9.2503 | -51.2472 | 2025-09-13 02:40:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 67.3 |
| 1c461465-8183-3c6c-bfef-1e9fa369aa86 | -11.4119 | -45.6012 | 2025-09-13 02:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 113.8 |
| bbe180da-0a3d-344a-8423-290134db231a | -11.8656 | -50.6005 | 2025-09-13 02:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 73.2 |
| 695f2c7d-11e2-35c3-b57d-71a07ebbd9f8 | -9.247 | -59.4201 | 2025-09-13 02:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 75.0 |
| bc05f3c1-f0aa-3ecc-b195-bb59d1d4dc77 | -3.2283 | -47.6154 | 2025-09-13 02:50:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 58.5 |
| bc89c9c5-51d9-389c-832b-09e687dde5fb | -16.3418 | -51.5434 | 2025-09-13 02:50:00 | GOES-19 | ARENÓPOLIS | GOIÁS | Brasil | 5202353 | 52 | 33 | nan | nan | nan | Cerrado | 121.0 |
| ef02d9ff-ecab-323d-a5bd-c78744a8f137 | -9.5326 | -54.6075 | 2025-09-13 02:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 50.4 |
| ca556f66-36c7-3ffc-8001-58b5edbe4c71 | -15.7161 | -50.5763 | 2025-09-13 02:50:00 | GOES-19 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 68.8 |
| cd88d951-3312-33dd-9267-8306078eda72 | -9.2472 | -59.4007 | 2025-09-13 02:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 83.1 |
| d7ff858c-3842-3a78-9359-bf8c5f95858b | -9.2656 | -59.4191 | 2025-09-13 02:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 177.1 |
| 75ac94ee-dbb2-32a5-82e2-b27f392b0fc0 | -11.9869 | -47.7531 | 2025-09-13 02:50:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 70.8 |
| 38fcc39e-1b1e-314c-a6e6-d04dfc184b3d | -15.1165 | -52.4918 | 2025-09-13 02:50:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 89.1 |
| e3212699-31d9-3102-ad29-fc8a8f5a5ec6 | -11.7384 | -46.6231 | 2025-09-13 02:50:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 76.8 |
| 5ed39dd4-2ebd-367c-8261-95ceec43c258 | -9.2843 | -59.418 | 2025-09-13 02:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 85.7 |
| 1c50beb6-28f6-3865-b789-8b3bef9493e8 | -11.431 | -45.5985 | 2025-09-13 02:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 66.6 |
| adf8bf65-40b8-31c5-87a4-f4613a60d084 | -8.1004 | -50.1821 | 2025-09-13 02:50:00 | GOES-19 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 51.1 |
| f6bd82ae-d3ac-31be-9629-2f5481193db0 | -9.5137 | -54.6292 | 2025-09-13 02:50:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 146.4 |
| 55990113-948f-3d93-8c2e-ace737a5d07a | -13.0891 | -48.2663 | 2025-09-13 02:50:00 | GOES-19 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 64.8 |
| 2c78376c-db86-3dfe-9ccd-33bd5e39a9b4 | -12.006 | -47.7505 | 2025-09-13 02:50:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 114.8 |
| b2662ba4-adb9-326c-9698-a1e28a5f242f | -12.0056 | -47.7728 | 2025-09-13 02:50:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 77.3 |
| cfde0c06-9879-3686-9dae-fec9abd04a5c | -9.5139 | -54.6089 | 2025-09-13 02:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 68.1 |
| 8eb9704f-b526-3b67-abf0-96368676ebe0 | -11.8472 | -50.5598 | 2025-09-13 02:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 132.9 |
| a91ec62e-ebcc-3824-aec3-d57e37bad248 | -9.2658 | -59.3997 | 2025-09-13 02:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 162.1 |
| 693fbaa2-321f-3fad-a99c-1863b605bcd5 | -9.2503 | -51.2472 | 2025-09-13 02:50:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 71.5 |
| 9e1fdd55-aeb9-3d89-87a2-2ed0f126e8b8 | -11.8468 | -50.5813 | 2025-09-13 02:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 191.6 |
| caea52a2-cf39-3200-b474-696c07c70a3b | -15.1161 | -52.5131 | 2025-09-13 02:50:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 61.2 |
| 5a15ce29-822b-321d-b6b6-6f2bcbcbf7f6 | -15.253 | -51.382 | 2025-09-13 02:50:00 | GOES-19 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 61.8 |
| a3adc7e0-03c6-353e-be25-37a0a32fd9be | -3.2282 | -47.6371 | 2025-09-13 02:50:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 90.9 |
| 3383e6c3-3914-3963-82f0-567abe2ab509 | -16.3422 | -51.5217 | 2025-09-13 02:50:00 | GOES-19 | ARENÓPOLIS | GOIÁS | Brasil | 5202353 | 52 | 33 | nan | nan | nan | Cerrado | 94.8 |
| 0d548a37-ecc1-3c2d-9421-284b958ffe3d | -11.1131 | -51.4692 | 2025-09-13 02:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 78.4 |
| 2f01f671-8b4a-330b-b101-b4f8c75cc55f | -11.8278 | -50.5835 | 2025-09-13 02:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 62.6 |
| 957c8514-d4c6-3a14-bd3e-20742e4f0ad9 | -15.2036 | -56.6803 | 2025-09-13 02:50:00 | GOES-19 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 59.6 |
| 279ce1b5-ff4b-3417-b8c2-1b8fc8a4d77d | -9.2844 | -59.3986 | 2025-09-13 02:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 74.9 |


[Clique aqui para ver as próximas entradas](README17.md)
