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
| 78ec3787-95e5-3d90-af45-577d69236cec | -13.1704 | -51.3831 | 2026-08-24 04:40:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 52.9 |
| 8fdb5e6b-7906-3bae-af18-d582592a7887 | -12.1132 | -50.5929 | 2026-08-24 04:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 165.4 |
| 6d26da13-23d8-31ee-8283-a97bb670e9a8 | -12.0938 | -50.6166 | 2026-08-24 04:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 71.4 |
| 7ceb6083-9c09-3ebd-9865-9fa3c6193980 | -12.0941 | -50.5951 | 2026-08-24 04:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 88.5 |
| fa335fc7-dd6e-3659-956c-1a53f328a5ec | -17.4435 | -48.8425 | 2026-08-24 04:40:00 | GOES-19 | PIRACANJUBA | GOIÁS | Brasil | 5217104 | 52 | 33 | nan | nan | nan | Cerrado | 119.7 |
| 8ca08ac4-7078-3b96-b2df-b7f354cba178 | -12.1128 | -50.6143 | 2026-08-24 04:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 174.1 |
| fed32a6e-6a98-3fbe-a479-0c292280e6af | -17.444 | -48.8199 | 2026-08-24 04:40:00 | GOES-19 | PIRACANJUBA | GOIÁS | Brasil | 5217104 | 52 | 33 | nan | nan | nan | Cerrado | 58.3 |
| e50055d3-8f0b-3aed-b44e-bedc6bcacc7e | -4.5361 | -55.51426 | 2026-08-24 04:44:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d6c52f34-2932-3f18-bc2e-1e8350cdbce0 | -6.75453 | -45.25004 | 2026-08-24 04:44:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ac6a52ea-b1a5-39a2-92ff-771e80cd649c | -6.34484 | -54.74903 | 2026-08-24 04:44:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1150ab9f-9f3d-3e87-bbce-59323f958027 | -6.3384 | -54.76259 | 2026-08-24 04:44:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3f7377a2-daa9-388f-8945-644c21d9ff62 | -6.18381 | -53.53056 | 2026-08-24 04:44:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 621783ba-7402-3d44-9859-9c24c234684b | -6.37966 | -54.98663 | 2026-08-24 04:44:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5fcbc17e-2c38-39df-8fec-be9cd55abfdc | -7.36857 | -45.82676 | 2026-08-24 04:44:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 3e0727ae-c71e-34a6-91e8-c19b4646be10 | -3.5395 | -48.18395 | 2026-08-24 04:44:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| b1501b22-4eb3-331f-93df-93bbd8d5678a | -4.92971 | -55.77402 | 2026-08-24 04:44:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| b837f985-8a45-37b5-890a-84c0fea9c620 | -5.86416 | -57.56647 | 2026-08-24 04:44:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 7c46b255-0761-3628-a27a-f006693bf2fb | -7.28577 | -45.36897 | 2026-08-24 04:44:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6954c8a3-772c-3155-a12f-2dc69c03ddec | -7.18366 | -42.7434 | 2026-08-24 04:44:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 3723f976-d6a9-3c31-b220-a08a84becbf2 | -6.80558 | -42.66865 | 2026-08-24 04:44:00 | NOAA-20 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| a1f753eb-cb34-376c-8e3d-77f3fbefb8b4 | -7.89702 | -46.32865 | 2026-08-24 04:44:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| bc417f70-ff7d-3991-b8cf-77d4422e0cec | -7.17441 | -42.742 | 2026-08-24 04:44:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| c30e2056-e43a-39b7-86e3-7e8568bdc4e4 | -6.43918 | -54.95901 | 2026-08-24 04:44:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 68bd3d67-e69e-3969-8eba-9382e7a4a4f1 | -7.14549 | -42.81133 | 2026-08-24 04:44:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| a5dc12e4-cc11-39df-a05c-9be575c24fc9 | -6.51179 | -51.44036 | 2026-08-24 04:44:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4c4da341-0d8f-37a3-9542-b9d76762d389 | -7.24451 | -49.86901 | 2026-08-24 04:44:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 6fa1fd7f-47fb-33fb-8cfa-d283326ed585 | -5.00383 | -56.13519 | 2026-08-24 04:44:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 216b1f4e-6b5f-3b12-a1b1-0c883606da2d | -6.55374 | -55.09967 | 2026-08-24 04:44:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f74ebd43-6e35-32d2-a44e-e4a49d423992 | -5.92641 | -53.65242 | 2026-08-24 04:44:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c8cefc9d-1f9d-3149-8c1e-544d2903f43f | -7.45176 | -46.91217 | 2026-08-24 04:44:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 48150a9d-3ead-389d-b9fa-21c7dd7ad5a4 | -7.26715 | -49.91875 | 2026-08-24 04:44:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 790062d5-009d-3043-8393-a3948ac60d23 | -6.84027 | -52.50826 | 2026-08-24 04:44:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 15.2 |
| b8f8f6d4-f4d2-3f2c-8681-c38b6099e79a | -7.83485 | -47.65118 | 2026-08-24 04:44:00 | NOAA-20 | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 8771f56b-6671-3dd0-b48f-8b9136aa8bf4 | -3.5323 | -48.18639 | 2026-08-24 04:44:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 91e2a7a3-56a4-3747-878a-2109ec3615fb | -6.20558 | -53.08866 | 2026-08-24 04:44:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f1afacbc-c5ef-304c-8cda-2ac925e4ae52 | -6.78702 | -44.66074 | 2026-08-24 04:44:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| dba0cec5-be81-3517-ab81-603866b9f43f | -7.3555 | -45.81065 | 2026-08-24 04:44:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| b742e4f2-be9c-3f04-8e3e-ac678524c682 | -7.24727 | -49.873 | 2026-08-24 04:44:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 1826b89a-a84c-3537-a17b-0eaf51987136 | -7.97946 | -45.25507 | 2026-08-24 04:44:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6c6bcbf2-7911-38ae-b3ed-c9b46e366c95 | -5.77839 | -57.55582 | 2026-08-24 04:44:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| aaa0c659-8608-39ec-a59d-1fff16e9e3db | -7.24782 | -49.86954 | 2026-08-24 04:44:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 16.4 |
| a8afc994-26d5-3bb3-b7b1-83682e73f0c9 | -7.25498 | -49.86713 | 2026-08-24 04:44:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1bd1e59a-2568-3cf2-afa8-0d6ff8817925 | -7.97568 | -45.28056 | 2026-08-24 04:44:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| bb142256-f0d0-3844-8390-f602e7ed50da | -7.97079 | -45.25901 | 2026-08-24 04:44:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 495087b4-4f70-3a81-9c7f-4d1149d2b154 | -6.34305 | -54.7597 | 2026-08-24 04:44:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ae10c920-9335-3a24-9cd6-f942c9fe71dd | -6.84511 | -52.50085 | 2026-08-24 04:44:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| e042a65f-c096-3813-a1ed-f3186ff4eba4 | -7.30854 | -42.97935 | 2026-08-24 04:44:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 5.1 |
| 8a350c7b-92da-365f-8d39-279cbb27d571 | -6.18758 | -53.53118 | 2026-08-24 04:44:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| df41b567-fde5-3722-8c00-6e1f11d158e7 | -6.4327 | -52.75772 | 2026-08-24 04:44:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4be8a966-29f5-3ccd-ba69-a95297c68f13 | -6.18305 | -53.53513 | 2026-08-24 04:44:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8b0d7d6a-a9be-3321-a244-45eabdf5ed27 | -5.57361 | -45.29284 | 2026-08-24 04:44:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b436b53c-2be4-3fee-aec2-23ead456e84b | -7.48427 | -45.13202 | 2026-08-24 04:44:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 804e7dfe-87e6-3743-9c5c-06e57aab5401 | -6.15299 | -57.94956 | 2026-08-24 04:44:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 8acce7f4-762b-3932-9307-410956b23f51 | -6.33977 | -55.87507 | 2026-08-24 04:44:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| eece3c8c-4e8e-3ba7-8804-4ec35661578a | -6.43612 | -54.97729 | 2026-08-24 04:44:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1cee7152-8e2e-30f5-a0a3-5e990270aad6 | -3.04556 | -50.26956 | 2026-08-24 04:44:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6b4cceae-30fe-3190-b63f-a5586023ce90 | -6.55312 | -55.10339 | 2026-08-24 04:44:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a3980f9a-a679-3dbe-80d5-f9e99e73b832 | -6.35115 | -54.76105 | 2026-08-24 04:44:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 554ecd3c-ba0b-3478-a6b1-d58ab367cae5 | -6.8049 | -42.67342 | 2026-08-24 04:44:00 | NOAA-20 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| cc6a5856-ceaa-3f68-aebe-3c746ba8fe0b | -6.3471 | -54.76038 | 2026-08-24 04:44:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 405e5197-940e-3856-a1ca-1d683577145f | -4.61033 | -55.73989 | 2026-08-24 04:44:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a2854ae4-bc00-384e-97ac-333c0ec9308e | -4.7356 | -49.27932 | 2026-08-24 04:44:00 | NOAA-20 | NOVA IPIXUNA | PARÁ | Brasil | 1504976 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c1e0ff97-30bf-3701-8ce2-abb7a17c3e18 | -6.3315 | -54.7541 | 2026-08-24 04:44:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e5be369a-877e-3e17-8443-dc1dd0f5e751 | -3.52952 | -48.18239 | 2026-08-24 04:44:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e8b4ce9a-8670-3425-9dca-de8e1d35d47d | -7.30465 | -42.97394 | 2026-08-24 04:44:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.5 |
| 30bc8ec5-059f-3f0b-adcd-d3aff398eb37 | -7.17837 | -42.74027 | 2026-08-24 04:44:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 4c1ac218-aad5-3254-adaf-22937a5cb2cc | -7.75202 | -46.15562 | 2026-08-24 04:44:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2818ac6d-eeac-33db-9773-a53eabdba382 | -6.82679 | -52.50181 | 2026-08-24 04:44:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 28d0d1a3-ba35-31eb-a4c8-2beb0515ab67 | -1.47483 | -54.9635 | 2026-08-24 04:44:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7136cc6b-fe5d-3aeb-b1a5-c93305e03c73 | -7.26991 | -49.92274 | 2026-08-24 04:44:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 7752be64-3abf-3bf9-8398-208f6a50c647 | -5.06428 | -49.36982 | 2026-08-24 04:44:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a8c2264a-3156-34f8-9714-769c9516a7a6 | -5.57293 | -55.81708 | 2026-08-24 04:44:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a418d4d8-a701-39aa-a5e5-ccbc5979b247 | -7.26439 | -49.91476 | 2026-08-24 04:44:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c454ba33-0059-3225-ac89-0c31bf03159e | -7.44757 | -46.91576 | 2026-08-24 04:44:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7f61c5a1-602e-36f9-8852-ed4ab20ebdb9 | -3.52897 | -48.18587 | 2026-08-24 04:44:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 218d005e-64b7-3a31-a388-e972748b677e | -4.48148 | -54.86552 | 2026-08-24 04:44:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0e4d535b-8457-38c6-afd2-6514f435215b | -6.44393 | -56.05787 | 2026-08-24 04:44:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6927cea6-cad9-3c55-b539-22576541a9ba | -7.18758 | -42.74896 | 2026-08-24 04:44:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| dbcabbe3-7345-3ca1-9fc4-3d8ba272a78c | -7.2826 | -45.3635 | 2026-08-24 04:44:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 5011c48b-b6bd-332a-8e31-f638dd937f3b | -3.26527 | -49.53031 | 2026-08-24 04:44:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4a568d20-92c5-3f67-8935-e7d1d34bfcca | -6.33615 | -54.75123 | 2026-08-24 04:44:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 682a5fed-d58c-390e-a7f0-1d54a2fc2fe3 | -7.19157 | -42.74726 | 2026-08-24 04:44:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 53d8e69e-e79a-3a7b-b00b-4cbcfd77afed | -3.4273 | -50.09312 | 2026-08-24 04:44:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 33a82c60-ee69-3529-9632-bd31aba4414c | -6.12699 | -57.83118 | 2026-08-24 04:44:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a2408b10-5300-36dc-819d-e94f94b6f7dd | -4.60779 | -55.73691 | 2026-08-24 04:44:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b56a9dea-ff81-352c-bdd2-6cd82d9d28f1 | -6.14795 | -57.9487 | 2026-08-24 04:44:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 1f7e34ff-bc31-3e17-88c6-6a6d2534ad0e | -7.48564 | -45.12983 | 2026-08-24 04:44:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 3e07d1ae-1e0d-3d2b-a08d-6a65ea3f5cc7 | -2.11275 | -48.99836 | 2026-08-24 04:44:00 | NOAA-20 | IGARAPÉ-MIRI | PARÁ | Brasil | 1503309 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ba5a4c82-f366-3d7c-9ce5-7a537c153898 | -7.29029 | -43.00958 | 2026-08-24 04:44:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 85ef8223-4108-34fe-9045-59f65f12bcac | -6.11992 | -57.84209 | 2026-08-24 04:44:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4e668482-de4b-3ccc-884a-6238d2351e75 | -7.18231 | -42.74589 | 2026-08-24 04:44:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 84e28fe6-cdd7-3e6f-a3f8-68915e2e9cf2 | -7.97474 | -45.25961 | 2026-08-24 04:44:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 5a466dd8-0656-383e-ab02-8401c57bee40 | -5.60613 | -51.78998 | 2026-08-24 04:44:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| fd1d4178-c9d2-3f34-ad26-887425de3010 | -7.25112 | -49.87007 | 2026-08-24 04:44:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 16.4 |
| 5b04d149-2ce5-36d5-93eb-95acc7dd7c39 | -7.36519 | -45.79781 | 2026-08-24 04:44:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 486084f8-6971-3e1c-83ef-352fe893d8b7 | -6.1921 | -53.52724 | 2026-08-24 04:44:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 79a60ca0-80cf-39af-aa93-2d7dbbe4c025 | -7.26383 | -49.89692 | 2026-08-24 04:44:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d8366c23-5b8f-3b8f-994c-b1ac5c668b5e | -7.36898 | -45.79839 | 2026-08-24 04:44:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| ea24b707-6ee0-3f8d-badc-8c49ed0c9ad1 | -7.4817 | -45.12911 | 2026-08-24 04:44:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| f64dd8a0-ebef-3454-a244-7b7e4602d808 | -6.84092 | -52.5043 | 2026-08-24 04:44:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 10.5 |


[Clique aqui para ver as próximas entradas](README26.md)
