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

## Dados Diários - Página 14

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| dae060dc-b2ea-3edc-9eae-9eee73f4fe15 | -5.70215 | -43.53922 | 2025-08-22 03:55:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6f321811-6dec-3418-9c2b-0b4481bfed18 | -6.51714 | -43.41336 | 2025-08-22 03:55:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 50bd9d47-19d1-3b5d-8126-95e7f7e707b7 | -3.98937 | -42.515 | 2025-08-22 03:55:00 | NPP-375D | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 4367e74a-0aff-3c30-aa2e-9060021a7774 | -6.57584 | -44.73222 | 2025-08-22 03:55:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 10c3df47-4322-3cfd-bc61-668afb5e67a1 | -3.26566 | -46.91883 | 2025-08-22 03:55:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1b67153f-9576-33cf-b0e1-7d2014068d7c | -6.29621 | -43.88719 | 2025-08-22 03:55:00 | NPP-375D | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 2ebcde59-381e-3e75-adbc-34598e0b09dd | -7.27576 | -43.66915 | 2025-08-22 03:55:00 | NPP-375D | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ac3ea136-b880-3ad1-b77a-838e04d4dfaa | -2.69156 | -48.21034 | 2025-08-22 03:55:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 68f79957-2d80-32aa-89a3-6ae4d9e0dbee | -4.1445 | -46.45742 | 2025-08-22 03:55:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ce64ac5c-f291-3428-a1f7-764fcf723925 | -7.02526 | -44.6296 | 2025-08-22 03:55:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0829f82d-3ed3-309d-9574-3e9b9b0a8d8f | -4.40065 | -44.08647 | 2025-08-22 03:55:00 | NPP-375D | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 324c6e83-a16f-3be1-ad7b-df4e19135507 | -6.20776 | -43.56625 | 2025-08-22 03:55:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4bc9cfcf-4995-3ccc-bd87-5ec1097748a3 | -7.5116 | -44.96522 | 2025-08-22 03:55:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 229e9d9d-3f74-3120-a50d-8203487d069a | -4.39551 | -44.09001 | 2025-08-22 03:55:00 | NPP-375D | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 32a35218-9f8d-320d-93e4-8330315a4468 | -7.02963 | -44.63047 | 2025-08-22 03:55:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| dec989e5-f98c-3e44-8eb3-22a869c46e4d | -6.06561 | -44.10551 | 2025-08-22 03:55:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| fdc3c56f-5627-3262-a9b4-d4b35053e135 | -5.38021 | -41.21849 | 2025-08-22 03:55:00 | NPP-375D | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 07d535e0-1538-3b9a-8a59-64ee280f933e | -7.09729 | -43.69611 | 2025-08-22 03:55:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 9bc8465a-d03f-3e9d-b733-1ad310bc7f63 | -5.73244 | -38.98566 | 2025-08-22 03:55:00 | NPP-375D | SOLONÓPOLE | CEARÁ | Brasil | 2313005 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 5b745721-0380-3c08-8dac-8969643330dc | -7.94337 | -42.65704 | 2025-08-22 03:55:00 | NPP-375D | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| c7d84372-7733-3eb0-935c-34a8b305a523 | -7.46058 | -44.45509 | 2025-08-22 03:55:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d1124725-c237-3355-b3e0-636e4133374e | -6.51997 | -45.88356 | 2025-08-22 03:55:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 15f5f699-e139-35b9-97b1-0056eaa3bcc6 | -6.44574 | -44.52155 | 2025-08-22 03:55:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e7ead105-e331-3d8a-b36d-bb8c2e20e3f5 | -6.03628 | -44.36226 | 2025-08-22 03:55:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9b8302de-b64a-32c0-990c-bb0cd9b36f2e | -7.02598 | -44.62541 | 2025-08-22 03:55:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d65ff12e-5430-3634-8f8a-4f75fa335bce | -6.11356 | -44.38231 | 2025-08-22 03:55:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 805634b8-aa8c-333f-8b81-83cf5d3673f5 | -2.91354 | -48.30707 | 2025-08-22 03:55:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1eecf0fb-9c74-3b3d-a37c-4ebe245d4794 | -5.46266 | -46.47025 | 2025-08-22 03:55:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f10a8c6b-5c0d-3504-a099-9ac039246a1a | -3.63222 | -43.54511 | 2025-08-22 03:55:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| cc56bdb1-008e-3620-9399-c2e8fba028ab | -6.03401 | -42.84487 | 2025-08-22 03:55:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| f5483e8f-4021-3154-84c8-4fee81d8eee1 | -6.50737 | -45.52612 | 2025-08-22 03:55:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 90f2ae39-0334-3e65-a69b-794c66d875fc | -3.39077 | -47.61127 | 2025-08-22 03:55:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f39d9821-01a9-3e64-81cf-56270588908a | -7.27103 | -43.67212 | 2025-08-22 03:55:00 | NPP-375D | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1a5a13db-09bf-3a8b-ac24-220f2565430a | -6.86411 | -44.41341 | 2025-08-22 03:55:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7930f4fb-9ecb-3b49-9771-5deaad019e73 | -4.43048 | -47.75591 | 2025-08-22 03:55:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8318ee8b-33dd-3762-b550-c6c1f5fc52ca | -7.63306 | -45.23966 | 2025-08-22 03:55:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 201a0633-fe99-3e8e-8875-02adac27c0ba | -7.6123 | -44.37968 | 2025-08-22 03:55:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| becce6f4-3e48-39b5-8572-b2e74a564e33 | -5.42855 | -46.36292 | 2025-08-22 03:55:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 51f61b0c-46a7-3505-905a-833bd9ff3baa | -4.07585 | -46.93022 | 2025-08-22 03:55:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e57010bd-0c88-3e7c-9192-5a9016c299b0 | -3.83264 | -47.73658 | 2025-08-22 03:55:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5fa488f3-d001-3650-8d11-fd53a799aabb | -6.03905 | -44.36949 | 2025-08-22 03:55:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f8e73472-9cda-3ecc-9113-08ee9e9f0047 | -3.81957 | -41.55919 | 2025-08-22 03:55:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| db1b45da-1f4e-3f7d-b847-901107ca3ba0 | -4.14551 | -46.45144 | 2025-08-22 03:55:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4c8c1bdf-e36a-3e6f-a85e-5b42571bd43a | -6.82373 | -44.23485 | 2025-08-22 03:55:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 37ce52e9-3b93-3d06-87a5-2f70bddb5da1 | -2.69398 | -48.20892 | 2025-08-22 03:55:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 692fe2a7-9b1f-3c49-a7be-60a5aad11a47 | -2.91529 | -48.30761 | 2025-08-22 03:55:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d0159679-2e69-386e-beed-be2c54ef7ab8 | -6.03487 | -44.37073 | 2025-08-22 03:55:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 74c8ebc9-8af8-3c2a-8793-02de75086a12 | -2.39064 | -47.66192 | 2025-08-22 03:55:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| acf204dc-fa4a-3c29-a631-bafe452e692f | -6.03487 | -42.83965 | 2025-08-22 03:55:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| eea5cda1-516f-3630-86d1-68eaab00c8a7 | -4.64271 | -41.41486 | 2025-08-22 03:55:00 | NPP-375D | MILTON BRANDÃO | PIAUÍ | Brasil | 2206357 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| efce13d4-b567-3379-9a64-1e6b236c3e38 | -3.98464 | -43.24321 | 2025-08-22 03:55:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| b6cd64b3-cdad-3c9f-bfd4-77522c74c6e1 | -6.29276 | -43.70337 | 2025-08-22 03:55:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 5641b35f-a1d4-3dac-9dd9-b9497e0ce433 | -5.24561 | -37.69699 | 2025-08-22 03:55:00 | NPP-375D | GOVERNADOR DIX-SEPT ROSADO | RIO GRANDE DO NORTE | Brasil | 2404309 | 24 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 1421c830-f407-3cc5-9c69-14d6f7123171 | -2.25402 | -47.85209 | 2025-08-22 03:55:00 | NPP-375D | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e72f39ad-e015-39fa-bb52-d1a9ccb4ea28 | -7.21888 | -35.03461 | 2025-08-22 03:55:00 | NPP-375D | SANTA RITA | PARAÍBA | Brasil | 2513703 | 25 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| ac56f706-0a4f-3562-afec-b13badad9bb1 | -6.04571 | -44.35975 | 2025-08-22 03:55:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2482e379-ad45-37b0-952e-eee305009f6e | -6.04488 | -44.36188 | 2025-08-22 03:55:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 71e342e2-3ef3-3cbf-994d-32019fe9e8c6 | -6.02468 | -44.37773 | 2025-08-22 03:55:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 967e35ec-2631-3c05-ab6a-b184389f8b1b | -4.13979 | -46.4535 | 2025-08-22 03:55:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 305fe09d-6876-3027-8416-fb7da1b92550 | -6.08364 | -44.1304 | 2025-08-22 03:55:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2a09ae25-cb69-3829-a903-ab054558c7d1 | -6.43762 | -44.51596 | 2025-08-22 03:55:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 9f3079bf-7f06-3347-81f6-13e151d174a8 | -4.72596 | -38.3958 | 2025-08-22 03:55:00 | NPP-375D | MORADA NOVA | CEARÁ | Brasil | 2308708 | 23 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 5e776fe1-40fe-336a-b0f2-843f85938c38 | -4.6552 | -41.40833 | 2025-08-22 03:55:00 | NPP-375D | MILTON BRANDÃO | PIAUÍ | Brasil | 2206357 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 3b948aab-795d-3fbc-ba99-801cbccb281a | -6.02027 | -44.37708 | 2025-08-22 03:55:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4cd511ab-cfe7-3465-bf41-380aa16890f0 | -4.77452 | -45.32669 | 2025-08-22 03:55:00 | NPP-375D | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a1ce2ae6-0da7-315b-a410-87a8999af802 | -6.04065 | -44.36308 | 2025-08-22 03:55:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d0cbbb46-ab9a-325a-acb4-7e34cbab615c | -6.0456 | -44.35774 | 2025-08-22 03:55:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 41ade0e0-40d6-397f-abfc-a3660b85f558 | -3.23646 | -46.79001 | 2025-08-22 03:55:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 73d32074-0213-353d-936f-2c98872e7531 | -4.72263 | -38.39528 | 2025-08-22 03:55:00 | NPP-375D | MORADA NOVA | CEARÁ | Brasil | 2308708 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 91c72638-f8c1-35ad-a3b0-6fe0c57cb854 | -5.78673 | -45.06923 | 2025-08-22 03:55:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| ec1121d8-0d19-3454-9147-d0a853cd5cbb | -6.34799 | -43.37842 | 2025-08-22 03:55:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 660aa37a-5c0a-3200-ba11-242db6402a26 | -7.64213 | -45.2432 | 2025-08-22 03:55:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| d9566577-9d58-3722-b485-57c7ea00471d | -7.16659 | -44.67127 | 2025-08-22 03:55:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 791eac33-a30b-3dae-b28d-6921759c67f9 | -6.4996 | -43.09609 | 2025-08-22 03:55:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a6a84d30-1bb0-3ec3-b19d-72cc0ec7e05d | -6.03348 | -44.37912 | 2025-08-22 03:55:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| beda3de4-447a-33ce-83bd-57ca8c8191cb | -6.48894 | -43.45658 | 2025-08-22 03:55:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 4e9eb592-13bc-3a23-aea6-05c077c07cb2 | -7.46558 | -44.45183 | 2025-08-22 03:55:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6aaa081d-9ba6-3b6a-920f-78ac205464de | -6.04415 | -44.36612 | 2025-08-22 03:55:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 784caba1-9259-368f-90c7-361c5b072c3a | -2.46887 | -47.76849 | 2025-08-22 03:55:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 61379a51-1cab-39ff-af34-3a6725ea4765 | -5.39266 | -41.2336 | 2025-08-22 03:55:00 | NPP-375D | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 6d5117e9-691e-307a-871b-44db54e738be | -6.03049 | -44.36995 | 2025-08-22 03:55:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 1543f9da-a4e7-3453-973d-b76c55e5b9b3 | -6.93944 | -44.29173 | 2025-08-22 03:55:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 668ab7d8-e342-3dd8-a7e5-99a7e46d1f85 | -6.94443 | -44.28847 | 2025-08-22 03:55:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a21872f9-abc7-3a10-a38f-7f8428cd1fb4 | -6.41235 | -35.02885 | 2025-08-22 03:55:00 | NPP-375D | BAÍA FORMOSA | RIO GRANDE DO NORTE | Brasil | 2401404 | 24 | 33 | nan | nan | nan | Mata Atlântica | 13.9 |
| 33f7e195-b563-39c8-8066-766664039841 | -6.94563 | -44.165 | 2025-08-22 03:55:00 | NPP-375D | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 1c4944a8-8618-3743-ab24-7811ed3b9e30 | -2.87603 | -40.09193 | 2025-08-22 03:55:00 | NPP-375D | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 83612938-1528-3693-acfe-125061d80ec6 | -5.49011 | -42.16295 | 2025-08-22 03:55:00 | NPP-375D | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 75efa715-4036-35af-ba80-f869e5ea99cd | -6.03979 | -44.36525 | 2025-08-22 03:55:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| bc45c0d2-a433-3521-a214-54fa2f37b7f8 | -5.76083 | -43.39105 | 2025-08-22 03:55:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a7d7c60c-6fc6-3c3b-b52f-29fef51693cb | -6.42164 | -44.68039 | 2025-08-22 03:55:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b5c167ca-36f0-3056-a06e-09d9abf01579 | -6.94829 | -44.55243 | 2025-08-22 03:55:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a8ebc3a3-8550-3aa9-851a-df7f0c69ce11 | -7.45987 | -44.45916 | 2025-08-22 03:55:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| dfff50b6-5529-314a-a4f8-981608d6959d | -5.79136 | -45.06996 | 2025-08-22 03:55:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 08f2b4fc-aacb-3f69-9a76-55307347bcd9 | -6.44132 | -44.52091 | 2025-08-22 03:55:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9029efec-b817-3cf0-93f3-db1947f9f7f3 | -6.20301 | -43.56913 | 2025-08-22 03:55:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c506f1b9-6ffc-3935-a20d-9753ede9931f | -5.14158 | -45.17694 | 2025-08-22 03:55:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 3f6110c7-69ef-3b7a-9409-146599119f73 | -6.50617 | -44.58695 | 2025-08-22 03:55:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 9.9 |
| ff40b942-0551-3def-a95b-f3a3d07568eb | -6.29551 | -43.89132 | 2025-08-22 03:55:00 | NPP-375D | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f0534841-805f-3fb7-a1d7-912d31d552cb | -5.52639 | -46.41769 | 2025-08-22 03:55:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8786b47a-f7d5-374f-886e-9ed10828f203 | -3.81881 | -41.56376 | 2025-08-22 03:55:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 4.9 |


[Clique aqui para ver as próximas entradas](README15.md)
