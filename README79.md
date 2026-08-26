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

## Dados Diários - Página 79

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c88d9ddd-c8cd-3f0b-a790-5938208f292e | -14.64339 | -45.11313 | 2026-08-26 12:14:00 | TERRA_M-T | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 46.1 |
| cd2428cb-1431-387f-ae66-1f2f96288a60 | -13.20477 | -51.2924 | 2026-08-26 12:14:00 | TERRA_M-T | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 87.7 |
| 9335e285-f1f1-3250-b733-f4500d5f2125 | -13.22242 | -51.30121 | 2026-08-26 12:14:00 | TERRA_M-T | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 103.2 |
| 31c6dde9-0484-3b9f-9108-d011ef718c76 | -12.6521 | -48.43054 | 2026-08-26 12:14:00 | TERRA_M-T | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 41.4 |
| 4f4491c8-71c5-35e4-97d1-793c03de2589 | -13.21339 | -51.30603 | 2026-08-26 12:14:00 | TERRA_M-T | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 75.7 |
| c67bdc2c-fb9b-345e-8ce2-4df178d0cd02 | -9.09598 | -59.39774 | 2026-08-26 12:14:00 | TERRA_M-T | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 12.5 |
| d73f5665-d0a4-3af2-8fd4-04b1bcab6a10 | -14.58813 | -52.02908 | 2026-08-26 12:14:00 | TERRA_M-T | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 12.8 |
| f94ba8d8-581a-39f1-accf-689839931e88 | -11.43621 | -44.55593 | 2026-08-26 12:14:00 | TERRA_M-T | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 65.1 |
| a2d51712-647f-39d0-b271-91640a7e66ad | -13.65222 | -51.84938 | 2026-08-26 12:14:00 | TERRA_M-T | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 82f8a4cf-e1c9-3c0e-af4c-1a6c8343a1c0 | -13.98761 | -54.00863 | 2026-08-26 12:14:00 | TERRA_M-T | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 21.8 |
| 28df1f3a-3ab0-3cfa-abf9-7402812342a6 | -14.3681 | -51.75333 | 2026-08-26 12:14:00 | TERRA_M-T | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 14.4 |
| f685eae0-baa1-38fa-aea3-0274bc2f44e6 | -10.76901 | -54.03215 | 2026-08-26 12:14:00 | TERRA_M-T | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 51.2 |
| 7b74fcab-afa7-351e-b72b-6566c3ffd919 | -12.67965 | -48.41526 | 2026-08-26 12:14:00 | TERRA_M-T | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 43.3 |
| a66cfc0a-58bc-35d6-9097-990abea37d27 | -14.64737 | -45.1207 | 2026-08-26 12:14:00 | TERRA_M-T | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 46.9 |
| 920f69bb-b581-3336-b648-e0a1d5224331 | -16.41705 | -51.83125 | 2026-08-26 12:14:00 | TERRA_M-T | PIRANHAS | GOIÁS | Brasil | 5217203 | 52 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 33a36027-060e-3559-b374-3a3136595c42 | -11.42336 | -44.5615 | 2026-08-26 12:14:00 | TERRA_M-T | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 243.5 |
| bd493aee-ccf6-379c-b7dd-83a4a5f40d59 | -14.43687 | -53.08177 | 2026-08-26 12:14:00 | TERRA_M-T | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 709c9c31-11fc-3114-b00e-12db214de049 | -13.21933 | -51.32582 | 2026-08-26 12:14:00 | TERRA_M-T | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 199.8 |
| ba247794-7c6e-3b26-bb37-3a0d9802e4d3 | -13.31691 | -51.44366 | 2026-08-26 12:14:00 | TERRA_M-T | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 208.5 |
| d1188b60-2ec3-36c7-b3b2-f48e905d6f04 | -13.1677 | -51.33752 | 2026-08-26 12:14:00 | TERRA_M-T | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 12.3 |
| f25de8d4-8767-3887-9887-ce54fb06aa89 | -13.87517 | -54.0904 | 2026-08-26 12:14:00 | TERRA_M-T | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 15.6 |
| 75a84e08-c05c-3297-845d-c820d562f503 | -13.34181 | -48.20584 | 2026-08-26 12:14:00 | TERRA_M-T | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 21.7 |
| 7c71849c-eac9-34ec-a600-637858389beb | -14.48692 | -53.51699 | 2026-08-26 12:14:00 | TERRA_M-T | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 844a1360-b732-39fc-87ec-2f4f2e67e978 | -13.21064 | -51.31217 | 2026-08-26 12:14:00 | TERRA_M-T | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 28.7 |
| b2d6a1be-756d-335e-a798-7d2850b74a0e | -15.78523 | -56.45815 | 2026-08-26 12:14:00 | TERRA_M-T | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 7a3ee465-81eb-3089-9ac6-6b71b775ec47 | -12.63913 | -48.42302 | 2026-08-26 12:14:00 | TERRA_M-T | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 14.3 |
| 0963e239-a3c9-3c50-8010-7820e71c81e4 | -10.56398 | -50.43243 | 2026-08-26 12:14:00 | TERRA_M-T | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 26.2 |
| b701556c-d21a-36de-baf6-f604364128ff | -11.84403 | -47.67737 | 2026-08-26 12:14:00 | TERRA_M-T | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 33.3 |
| ad7c5053-5d0f-321d-a3d5-83e7d0d06aa9 | -14.58666 | -52.03436 | 2026-08-26 12:14:00 | TERRA_M-T | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 15.6 |
| 38639c37-117f-3ae4-9130-4c99db485a5b | -13.21218 | -51.29985 | 2026-08-26 12:14:00 | TERRA_M-T | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 65.1 |
| cbcc6788-b2ac-396c-80ce-74c2df9da74a | -12.15225 | -50.58918 | 2026-08-26 12:14:00 | TERRA_M-T | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 731db477-6450-304c-a68a-372c2620cb0c | -13.27909 | -51.3461 | 2026-08-26 12:14:00 | TERRA_M-T | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 24.7 |
| 73d5bdac-7a70-30e3-bce9-a4c14af5354e | -11.3012 | -47.0696 | 2026-08-26 12:14:00 | TERRA_M-T | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 25.1 |
| fb612d62-3245-3251-b8ad-5e1ce7c9fd14 | -12.76338 | -46.45982 | 2026-08-26 12:14:00 | TERRA_M-T | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 27.6 |
| 44493da5-a3f8-36d6-bd81-fd0bcf785e50 | -11.44043 | -44.51776 | 2026-08-26 12:14:00 | TERRA_M-T | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 68.4 |
| 5db3dfa8-db72-306d-bf6e-1a33e1e59672 | -11.74784 | -54.53279 | 2026-08-26 12:14:00 | TERRA_M-T | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 080ba224-9033-3ecb-a67c-565aad0485fd | -13.2867 | -51.44607 | 2026-08-26 12:14:00 | TERRA_M-T | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 7.6 |
| d69f2497-d082-386b-96aa-cb56ab39be57 | -10.7596 | -54.0384 | 2026-08-26 12:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 70.6 |
| ba015952-eb25-38db-ac33-ab61d2dbbcb4 | -11.4306 | -44.5148 | 2026-08-26 12:20:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 87.3 |
| 58520fa6-2434-3e10-8399-1ceea30c3bba | -8.1484 | -47.4998 | 2026-08-26 12:20:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 88.4 |
| c199c587-2980-338b-967d-dc3ebd11901f | -6.2676 | -53.3768 | 2026-08-26 12:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 64.6 |
| 1d6127f2-642f-37ab-8ae1-24e6e5246e2b | -4.8002 | -43.1709 | 2026-08-26 12:20:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 72.3 |
| bdf6de2b-bb73-36db-abf3-6fa24c44821e | -8.1482 | -47.5218 | 2026-08-26 12:20:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 158.9 |
| b304aeb0-63de-3a43-922d-44b912b4cd1c | -8.1857 | -54.9435 | 2026-08-26 12:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 64.9 |
| 08eaf993-a12e-394c-8d20-ba80a20aee2c | -9.5748 | -49.2799 | 2026-08-26 12:20:00 | GOES-19 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 80.7 |
| 7b33c65d-028e-37e4-aa6f-d68cf62ecee6 | -11.4302 | -44.5382 | 2026-08-26 12:20:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 296.0 |
| 41735c2d-a51d-3ba4-b107-6140f92d69e9 | -8.1671 | -54.9447 | 2026-08-26 12:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 69.9 |
| 848315c9-5553-3a38-9ef7-2a8f21e97d99 | -13.2668 | -51.3497 | 2026-08-26 12:20:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 127.0 |
| ce7623cb-bd2d-3acd-b52f-5f9062808da8 | -7.385 | -55.1523 | 2026-08-26 12:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 69.8 |
| 677a9343-0ce8-361e-985b-a9b503790efc | -11.411 | -44.541 | 2026-08-26 12:20:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 142.6 |
| 24519814-7651-3ed2-a1cd-e3cd7bb612a2 | -14.3945 | -51.7585 | 2026-08-26 12:20:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 82.7 |
| a17f8354-d6d7-3114-bff6-652e7b31cad1 | -13.2095 | -51.3356 | 2026-08-26 12:20:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 186.0 |
| 5c039c2d-5857-36e1-984b-44d084291ef1 | -13.2664 | -51.3711 | 2026-08-26 12:20:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 149.4 |
| 611dc3c6-5f16-3d2e-a800-6a3eff34e28b | -13.2661 | -51.3925 | 2026-08-26 12:20:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 116.8 |
| 8e418a13-e033-3be2-9556-cfacf837ac6f | -11.4298 | -44.5615 | 2026-08-26 12:20:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 88.5 |
| a907fb8b-fc41-3149-9a3c-5637b2e9e32a | -13.1906 | -51.3166 | 2026-08-26 12:20:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 75.4 |
| d1058f1a-dd9c-31c7-a7ca-8255cfd767c9 | -9.5936 | -49.278 | 2026-08-26 12:30:00 | GOES-19 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 371.9 |
| f7edbbb1-2d93-30f1-8071-c8b3bb6737aa | -10.7596 | -54.0384 | 2026-08-26 12:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 88.5 |
| 7b3b5a0d-7e3b-30d6-8cf6-0ff75a99c190 | -14.3945 | -51.7585 | 2026-08-26 12:30:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 80.2 |
| 9ef7d767-c2c4-3abe-b6d6-f8af0895f7ca | -12.6836 | -48.4116 | 2026-08-26 12:30:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 65.2 |
| c9bfd788-7dbc-3115-a735-3ec232e76ca3 | -9.5748 | -49.2799 | 2026-08-26 12:30:00 | GOES-19 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 239.2 |
| 3b2756cf-ec25-3601-bc61-f179d55ccfad | -7.385 | -55.1523 | 2026-08-26 12:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 90.0 |
| b9e4630e-8e14-3894-b90a-8185c36cf736 | -4.8002 | -43.1709 | 2026-08-26 12:30:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 177.3 |
| 2287d20a-2ea2-330a-96e9-45eb411102ee | -8.1484 | -47.4998 | 2026-08-26 12:30:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 88.8 |
| 56a96bd9-1609-33a9-a48d-d1f2fe203c52 | -11.4298 | -44.5615 | 2026-08-26 12:30:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 126.7 |
| b2c42864-4c56-31ff-9570-0c0966f620c5 | -13.2095 | -51.3356 | 2026-08-26 12:30:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 136.0 |
| 0c73291f-3557-321f-ade7-5cc24324c0e2 | -13.2661 | -51.3925 | 2026-08-26 12:30:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 87.2 |
| 02adfbac-6f04-3aba-94d7-3d5902413b5e | -8.1482 | -47.5218 | 2026-08-26 12:30:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 130.3 |
| 60c4c99f-154f-3739-8dae-1a22255f3f58 | -11.2923 | -47.0644 | 2026-08-26 12:30:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 75.9 |
| ea65b684-c1e9-3872-9d38-9f18b14c4f29 | -11.4306 | -44.5148 | 2026-08-26 12:30:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 106.8 |
| 56f8a72a-4bac-345c-bdce-82aeb2a801f1 | -11.4302 | -44.5382 | 2026-08-26 12:30:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 336.5 |
| 98164961-4b64-3f4b-a893-0bb4af27e2be | -12.6452 | -48.4168 | 2026-08-26 12:30:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 66.1 |
| ee81a83c-34f6-3f13-ae7f-2cc4aa933885 | -8.1484 | -47.4998 | 2026-08-26 12:40:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 102.4 |
| 3b160bbd-14aa-3cbe-8b9a-64ecbd8fc142 | -11.2923 | -47.0644 | 2026-08-26 12:40:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 69.7 |
| 61170254-9326-329d-a324-aca7594bda45 | -12.6644 | -48.4142 | 2026-08-26 12:40:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 69.7 |
| 8af8a1e2-6c6b-31b2-9cfa-26a805732b9b | -4.8002 | -43.1709 | 2026-08-26 12:40:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 389.8 |
| 0f763024-4d60-304d-874a-0c49283ff05f | -10.5596 | -50.4449 | 2026-08-26 12:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 107.8 |
| ce0d6efc-51aa-31a0-804a-c7e4150993f1 | -9.5748 | -49.2799 | 2026-08-26 12:40:00 | GOES-19 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 92.2 |
| 65684abc-b03e-38bb-b2e7-1580102d5651 | -14.3179 | -51.726 | 2026-08-26 12:40:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 89.5 |
| 8e365335-33e5-3318-bb54-d44e2581a0d7 | -9.7249 | -49.3296 | 2026-08-26 12:40:00 | GOES-19 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 92.9 |
| 68e4c0ed-7710-3766-905e-5a7106f9e339 | -11.4302 | -44.5382 | 2026-08-26 12:40:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 308.3 |
| 9350cdfc-dfee-30ed-899f-8ddb2cbc2c55 | -10.7596 | -54.0384 | 2026-08-26 12:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 77.4 |
| 1b186325-b002-3a3b-b492-a01c80f8351f | -11.4306 | -44.5148 | 2026-08-26 12:40:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 91.5 |
| b525c423-2d8d-341e-92b0-950e5c5cae69 | -14.3941 | -51.7799 | 2026-08-26 12:40:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 80.1 |
| 3e6d962e-b0fa-3302-a850-d68a7a9bba14 | -13.2661 | -51.3925 | 2026-08-26 12:40:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 82.0 |
| d06a8a31-fcec-3aa5-8d1a-3f7b4156c554 | -8.1482 | -47.5218 | 2026-08-26 12:40:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 123.2 |
| 92642a4b-9d20-3a1a-8644-9e01395d5423 | -7.385 | -55.1523 | 2026-08-26 12:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 80.0 |
| 4f151005-eb2f-31db-966e-e012289aa71d | -12.6836 | -48.4116 | 2026-08-26 12:40:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 97.1 |
| 781b337a-11b1-391a-aa74-bda71c70322d | -9.5936 | -49.278 | 2026-08-26 12:40:00 | GOES-19 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 80.1 |
| bdb52d0a-6cf8-3f09-ba80-30b3e9b7c14e | -11.4298 | -44.5615 | 2026-08-26 12:40:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 146.3 |
| 5dca799e-13be-3e01-bb10-0ab79c1dad03 | -4.8004 | -43.1476 | 2026-08-26 12:40:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 278.7 |
| 1bc0222c-f043-34ba-af41-eca80f629397 | -12.6452 | -48.4168 | 2026-08-26 12:40:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 76.1 |
| cdbc1135-00b4-38c0-a5c2-206727495555 | -14.3945 | -51.7585 | 2026-08-26 12:40:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 122.0 |
| bd2bd3f9-281d-309b-9938-62cd0a116283 | -13.2095 | -51.3356 | 2026-08-26 12:40:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 151.4 |
| ab402f4e-b077-3bc3-ab31-c9adc980b93b | -11.4306 | -44.5148 | 2026-08-26 12:50:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 76.2 |
| 51c02abf-a10d-35f6-8b98-39301507e323 | -10.7596 | -54.0384 | 2026-08-26 12:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 101.7 |
| 9104e969-4bdd-32de-82e3-108be09f046d | -8.1671 | -54.9447 | 2026-08-26 12:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 75.7 |
| 07b6cef6-a8da-3af7-9818-7cb1a30dec7b | -9.5748 | -49.2799 | 2026-08-26 12:50:00 | GOES-19 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 83.3 |
| 7d451baa-4e91-3040-9ec5-3453346bdd6c | -11.2923 | -47.0644 | 2026-08-26 12:50:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 69.8 |
| 57b489e3-9e8f-3307-bda5-4f0b56aa453e | -4.8004 | -43.1476 | 2026-08-26 12:50:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 87.2 |


[Clique aqui para ver as próximas entradas](README80.md)
