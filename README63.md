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

## Dados Diários - Página 63

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 056dca8c-2031-3e7b-8f98-88f52097dbf9 | -5.4042 | -47.68877 | 2024-10-10 04:17:00 | NPP-375D | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| a91c93e7-2bf9-357c-a923-89b4928551fa | -6.36028 | -47.54236 | 2024-10-10 04:17:00 | NPP-375D | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6274aaab-ccbf-3030-8542-13f6ca4c80c7 | -6.35711 | -47.40363 | 2024-10-10 04:17:00 | NPP-375D | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 52e77f35-05df-3f78-8219-97e3db3ac222 | -6.29137 | -46.9894 | 2024-10-10 04:17:00 | NPP-375D | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 25816b12-788b-3485-abc5-4722c954863b | -6.29073 | -46.9933 | 2024-10-10 04:17:00 | NPP-375D | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b22e6733-6a65-3417-baff-08b55c527ab8 | -6.29009 | -46.99722 | 2024-10-10 04:17:00 | NPP-375D | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 4334e9aa-9da5-38dc-9dbb-283f567c5ab6 | -6.28786 | -46.98884 | 2024-10-10 04:17:00 | NPP-375D | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 82201bd5-65e6-3b0a-a5c2-309ed96b253f | -6.28722 | -46.99274 | 2024-10-10 04:17:00 | NPP-375D | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6aa79608-4757-3181-b97f-d8de34f8fbc0 | -6.07568 | -47.27432 | 2024-10-10 04:17:00 | NPP-375D | RIBAMAR FIQUENE | MARANHÃO | Brasil | 2109551 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5ede32f3-9630-38bc-afce-3d5388692f59 | -6.05119 | -46.60052 | 2024-10-10 04:17:00 | NPP-375D | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a0792dcf-1da0-3a17-b7d5-0ba386b17689 | -6.05057 | -46.60432 | 2024-10-10 04:17:00 | NPP-375D | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 9c0ed0e1-8bf1-30ad-896c-49b5be3da8db | -6.04834 | -46.59615 | 2024-10-10 04:17:00 | NPP-375D | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 802c5d2f-41e3-32db-9199-f286221497f1 | -6.04773 | -46.59994 | 2024-10-10 04:17:00 | NPP-375D | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 242d89eb-be95-32af-8539-6fefed4a5378 | -6.04427 | -46.59938 | 2024-10-10 04:17:00 | NPP-375D | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b104ebc6-6f38-39a3-8129-6e3bf9472d33 | -6.04365 | -46.60317 | 2024-10-10 04:17:00 | NPP-375D | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a9757e87-e32a-36a9-8474-ab70f173201e | -6.03329 | -47.96579 | 2024-10-10 04:17:00 | NPP-375D | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5cbf16a7-e3e8-3e38-bed9-09733d626492 | -5.96629 | -46.67752 | 2024-10-10 04:17:00 | NPP-375D | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5163e23a-e8e0-3493-bee8-27b3501a33fc | -5.91746 | -47.7199 | 2024-10-10 04:17:00 | NPP-375D | ITAGUATINS | TOCANTINS | Brasil | 1710706 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5e38f424-5ec5-32e3-9f4e-b296d772bac3 | -5.83905 | -47.42178 | 2024-10-10 04:17:00 | NPP-375D | RIBAMAR FIQUENE | MARANHÃO | Brasil | 2109551 | 21 | 33 | nan | nan | nan | Cerrado | 10.6 |
| fd4ad505-b234-3c1b-9d02-08ca82b43265 | -5.83478 | -47.42533 | 2024-10-10 04:17:00 | NPP-375D | RIBAMAR FIQUENE | MARANHÃO | Brasil | 2109551 | 21 | 33 | nan | nan | nan | Cerrado | 10.6 |
| c1d3bafe-0ace-3017-98af-4da66f5dab43 | -5.83411 | -47.42949 | 2024-10-10 04:17:00 | NPP-375D | RIBAMAR FIQUENE | MARANHÃO | Brasil | 2109551 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 39f6ca73-1c08-3fe4-84c1-e36d9ec2ce88 | -5.57396 | -47.25586 | 2024-10-10 04:17:00 | NPP-375D | DAVINÓPOLIS | MARANHÃO | Brasil | 2103752 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3f11f5b5-8c97-37c0-a344-3499908a1434 | -5.5481 | -46.69585 | 2024-10-10 04:17:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3d264f20-8394-39b6-b5ad-d5c5e2c087cb | -5.53825 | -46.69026 | 2024-10-10 04:17:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 238bcee3-cbcb-3dd2-99f6-3497ca3522fb | -5.53763 | -46.69413 | 2024-10-10 04:17:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 949d764b-d5fb-3976-bc04-002ceaf58d8e | -5.49204 | -46.91095 | 2024-10-10 04:17:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f9da0b01-c86d-30fd-b110-52293056915f | -5.4914 | -46.91491 | 2024-10-10 04:17:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 2025ae5d-eaa2-3a7d-85b0-72a78bc369b4 | -5.44034 | -47.83007 | 2024-10-10 04:17:00 | NPP-375D | AUGUSTINÓPOLIS | TOCANTINS | Brasil | 1702554 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 44e02a3b-9421-38c7-a142-f996c3865829 | -5.43418 | -47.68293 | 2024-10-10 04:17:00 | NPP-375D | SÃO MIGUEL DO TOCANTINS | TOCANTINS | Brasil | 1720200 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0cbca0b4-257f-3180-8e6f-11346a49e1d4 | -5.40711 | -47.68736 | 2024-10-10 04:17:00 | NPP-375D | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 341a354b-da00-3cba-be23-9bb74387aa94 | -5.40488 | -47.68449 | 2024-10-10 04:17:00 | NPP-375D | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| a882c20e-02f4-3dc4-9dd6-1eb0c4db95a6 | -5.40415 | -47.68247 | 2024-10-10 04:17:00 | NPP-375D | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 938269d2-04d3-3de5-8ed9-2a73941a4dc7 | -5.40344 | -47.68675 | 2024-10-10 04:17:00 | NPP-375D | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0c2784c4-1d53-3b03-8ef3-63367b6acd2a | -5.39755 | -47.68328 | 2024-10-10 04:17:00 | NPP-375D | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6bc0440e-4067-3ce7-81b5-12630ac4b456 | -5.27288 | -47.69081 | 2024-10-10 04:17:00 | NPP-375D | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 36d44367-c349-33bd-baa4-0ec74fb1e42f | -5.27357 | -47.68653 | 2024-10-10 04:17:00 | NPP-375D | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d9b536f9-9ceb-3d16-a22e-f715a1aa1e18 | -5.15642 | -47.60317 | 2024-10-10 04:17:00 | NPP-375D | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| edc0685f-e5f2-3bf1-9b19-42a0c99ec559 | -6.46485 | -47.16563 | 2024-10-10 04:17:00 | NPP-375D | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 28d44c06-bca9-3f86-9895-37f7a62d2246 | -6.46471 | -47.1646 | 2024-10-10 04:17:00 | NPP-375D | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2bd2c992-b100-3ff2-a4a0-2c9fdce3409c | -6.46132 | -47.16507 | 2024-10-10 04:17:00 | NPP-375D | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3479c7c9-408f-3ba7-b2b4-b396e320b96f | -6.46118 | -47.16405 | 2024-10-10 04:17:00 | NPP-375D | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c6408ce3-b031-375b-8bb4-209d4da372b4 | -6.42108 | -46.6739 | 2024-10-10 04:17:00 | NPP-375D | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 9ee31186-1e0b-328b-81ad-196fe0584a33 | -2.48549 | -48.054 | 2024-10-10 04:17:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 84855c54-48ad-3193-9491-f2bee007db53 | -2.48082 | -48.0582 | 2024-10-10 04:17:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 75d9642f-a192-3aea-9baf-24f874ac7d7d | -2.4777 | -48.05271 | 2024-10-10 04:17:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 61f3da1e-4316-3163-9740-10d3239016ce | -2.46083 | -47.81453 | 2024-10-10 04:17:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d894bbcf-947d-34bb-9977-7d1cd40df0d3 | -2.46007 | -47.84322 | 2024-10-10 04:17:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 56a66e70-6358-39c6-8e87-075e06e526f3 | -2.40892 | -48.8619 | 2024-10-10 04:17:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ec8cb956-53f1-3409-a964-c94342bf41d4 | -2.36639 | -48.5908 | 2024-10-10 04:17:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 068850f8-92b0-3b56-8ce1-e127adc7cdcb | -3.45962 | -47.65869 | 2024-10-10 04:17:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 7e02532c-d9cf-3252-89d8-c97e63cc755e | -3.45934 | -47.66098 | 2024-10-10 04:17:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b846cb59-f27c-3658-bfbe-bae721ff09e1 | -3.45892 | -47.66312 | 2024-10-10 04:17:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| dd3f5705-be49-316d-8fbd-a395f80b21d9 | -3.17567 | -48.58932 | 2024-10-10 04:17:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0db9242e-7a4e-3ce0-9869-25f26af52401 | -3.10367 | -48.60401 | 2024-10-10 04:17:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6eed2ee7-0b2d-31a9-9e35-465cce66ffe1 | -3.10265 | -48.60237 | 2024-10-10 04:17:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4682cdab-d882-35d4-8a2a-0c8aae3ef692 | -2.97161 | -47.99472 | 2024-10-10 04:17:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5f59c19d-7411-30fb-910c-5a10197f2dde | -2.97008 | -47.99738 | 2024-10-10 04:17:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d855dbbe-92d3-3937-a1ce-c65a56e53f81 | -2.94834 | -48.60905 | 2024-10-10 04:17:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 026ad04a-fb34-33b8-ba26-161a557c7c72 | -2.94778 | -48.61251 | 2024-10-10 04:17:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 371e068b-42c6-3842-95f7-829db8717866 | -2.94433 | -48.60839 | 2024-10-10 04:17:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 6294ffc0-7793-3ae1-8537-6da39fc8ca41 | -2.89093 | -47.81335 | 2024-10-10 04:17:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 781a89eb-a2f6-32d1-b3ca-f2a75c8091b0 | -2.88927 | -47.81539 | 2024-10-10 04:17:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b2b4bda3-a415-37c1-aa54-60b70ecac2f5 | -2.84647 | -48.64985 | 2024-10-10 04:17:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8ecc23fc-0926-32ee-9c7e-dc6564dc7c04 | -2.84245 | -48.64922 | 2024-10-10 04:17:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ef0a4153-ed3a-34fa-b7a5-9d6854ea3421 | -2.79598 | -48.68119 | 2024-10-10 04:17:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1ac6a5a9-bff3-3554-b730-4ca673718090 | -2.79358 | -48.56939 | 2024-10-10 04:17:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 177795be-e6c6-3a02-886e-7c3e5a308647 | -2.78958 | -48.56873 | 2024-10-10 04:17:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c398658a-0d06-398a-a536-804b7748bb65 | -2.78888 | -48.57301 | 2024-10-10 04:17:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 30f90a75-b6fe-3fb6-9a64-377b7ba489a7 | -2.78694 | -48.09383 | 2024-10-10 04:17:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 18173ae6-48a4-3548-8231-d26b2063b987 | -2.76027 | -48.64671 | 2024-10-10 04:17:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 52ff0d8d-06ad-3295-b99c-1d71d9443e81 | -2.76007 | -48.64323 | 2024-10-10 04:17:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 59abbfec-c6b6-387a-a604-4cb22b9001d6 | -2.75952 | -48.64672 | 2024-10-10 04:17:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bfa1a1c5-34dc-310c-bc5c-6f6c044c2731 | -2.75621 | -48.6964 | 2024-10-10 04:17:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 9d386e0d-2beb-335b-94d2-0295bca60cf0 | -2.75605 | -48.64257 | 2024-10-10 04:17:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 03f96cc6-1cca-336b-b205-7352702fe4e7 | -2.75581 | -48.69653 | 2024-10-10 04:17:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| a02be4fc-c4cb-3250-8337-c9a9e9db8bc0 | -2.75563 | -48.69994 | 2024-10-10 04:17:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 51618597-7c11-3045-a638-fb89e518426c | -2.75525 | -48.70008 | 2024-10-10 04:17:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 0f0df291-e8ae-334c-b6e4-b76cd9a40680 | -2.75217 | -48.69575 | 2024-10-10 04:17:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 29e75f4a-4b07-328e-95c8-bd3a934c7de5 | -2.75177 | -48.69588 | 2024-10-10 04:17:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 17c6776d-a887-300e-9b67-3d47e649a9f0 | -2.75158 | -48.6993 | 2024-10-10 04:17:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 0d8ebd1e-84a0-338b-9e83-2169e589cc82 | -2.75121 | -48.69942 | 2024-10-10 04:17:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| b56ba3c3-157f-3a00-b10d-4c001a7b7d72 | -2.74995 | -48.68113 | 2024-10-10 04:17:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 06684dd3-be20-3de4-be40-e61e99c091b5 | -2.7494 | -48.68465 | 2024-10-10 04:17:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8edfcd8d-fdc5-3112-b4e5-1a69d8ad9540 | -2.74536 | -48.68398 | 2024-10-10 04:17:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 58a36bbe-76a7-390e-ab83-8b664b621941 | -2.74425 | -48.69103 | 2024-10-10 04:17:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c5855d22-5d8d-3b66-84eb-558f22d27133 | -2.743 | -48.67278 | 2024-10-10 04:17:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| ac8835d9-2dfa-30ab-9572-b2d652666176 | -2.74244 | -48.67629 | 2024-10-10 04:17:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| de818f86-3916-3082-baba-fe0e43d71522 | -2.72021 | -48.73788 | 2024-10-10 04:17:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| daddf92b-c81b-3bd8-b8b0-4c1d4f60021c | -2.69582 | -48.70859 | 2024-10-10 04:17:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 50f6417e-93c6-341b-9f4d-cd2a3aa93fd5 | -2.69163 | -48.63219 | 2024-10-10 04:17:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 78bc504a-2bff-3359-a343-fa1ec6a1b945 | -2.60404 | -47.93714 | 2024-10-10 04:17:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1c8d5e06-c61d-3ba1-a510-1ca2ea677fa1 | -2.56726 | -48.24133 | 2024-10-10 04:17:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c714baf2-a3cd-30eb-9b86-850dc0a3b795 | -5.06461 | -48.44402 | 2024-10-10 04:17:00 | NPP-375D | ABEL FIGUEIREDO | PARÁ | Brasil | 1500131 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f8b4d99f-4723-3326-87a5-c81e0656d30c | -5.06382 | -48.44877 | 2024-10-10 04:17:00 | NPP-375D | ABEL FIGUEIREDO | PARÁ | Brasil | 1500131 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| abda4394-31e1-31f0-a45f-8d82ee12eb97 | -4.83795 | -48.94385 | 2024-10-10 04:17:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 679a1829-f35e-3a32-a7df-e4d0a8cadfa2 | -4.7851 | -48.89315 | 2024-10-10 04:17:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| ef2492fc-8e95-3732-9aa0-9f69ebec3143 | -4.78284 | -48.89556 | 2024-10-10 04:17:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 9c82369c-a513-3aef-b9e9-ce7fa3b66eed | -4.74086 | -48.87801 | 2024-10-10 04:17:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| a8b31553-2d72-3ac6-9980-93f04f5527da | -4.74003 | -48.88308 | 2024-10-10 04:17:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 1d88fbd4-a7fa-37c3-9800-fe9c8102fbd4 | -4.68747 | -47.87405 | 2024-10-10 04:17:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |


[Clique aqui para ver as próximas entradas](README64.md)
