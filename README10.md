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

## Dados Diários - Página 10

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| babd3ee1-283f-3f52-ae4b-37d464a38c50 | -12.4086 | -49.9978 | 2025-05-26 12:50:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 144.6 |
| ce02a5d1-8141-3c9f-93ca-6b4175d4f0e4 | -12.3522 | -49.94 | 2025-05-26 12:50:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 95.3 |
| 756d1d73-cb94-3c49-801e-1905646fc3df | -12.3526 | -49.9184 | 2025-05-26 12:50:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 246.7 |
| 736d602b-fc3c-3d79-a9c5-49bbf3be50f1 | -12.4089 | -49.9762 | 2025-05-26 12:50:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 291.3 |
| 96c6ac56-e750-37c9-b9f5-2641d9cf97e4 | -12.3717 | -49.916 | 2025-05-26 12:50:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 126.3 |
| 1f96d1d5-eab4-35af-b8a3-a9026210d24d | -8.0312 | -43.1964 | 2025-05-26 12:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 255.8 |
| 5a966c5c-50e7-3607-aa6f-9a9b94443efd | -14.6615 | -45.0992 | 2025-05-26 12:50:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 99.3 |
| abae3263-10f3-3a1f-913a-088a64106c2b | -12.0699 | -47.3632 | 2025-05-26 12:50:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 99.7 |
| 935fb33e-b862-34b6-a65e-3f65607cf081 | -12.0703 | -47.3408 | 2025-05-26 12:50:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 124.1 |
| aa4eab84-936c-3b89-9d2d-b0fa26e038cd | -12.3898 | -49.9786 | 2025-05-26 12:50:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 127.2 |
| f3e4ca67-9fac-341b-b71f-7702b6ae19ad | -12.0894 | -47.3382 | 2025-05-26 12:50:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 92.2 |
| 8ead9653-00cf-3a3c-9922-4445eb9a46b1 | -6.15447 | -48.04766 | 2025-05-26 12:59:00 | TERRA_M-T | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 36.2 |
| 6d11f5b5-430e-398a-bea5-0cf51b94b627 | -6.16112 | -48.05536 | 2025-05-26 12:59:00 | TERRA_M-T | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 180.3 |
| 2cd53165-a966-3cca-aa15-e147474e89a8 | -1.8813 | -55.13563 | 2025-05-26 12:59:00 | TERRA_M-T | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 17.7 |
| 10b38006-0194-302c-a3be-9197527b073c | -1.88 | -55.14456 | 2025-05-26 12:59:00 | TERRA_M-T | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| c10db637-041e-3e27-95a6-06327977db62 | -6.16819 | -48.04944 | 2025-05-26 12:59:00 | TERRA_M-T | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 103.0 |
| fd222653-79a0-35ab-b95d-0bce3840ad02 | -14.6615 | -45.0992 | 2025-05-26 13:00:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 86.8 |
| ebb18689-e6c1-3c4f-960e-ee21125de489 | -12.3526 | -49.9184 | 2025-05-26 13:00:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 330.7 |
| b6f4e24b-8ddc-3a93-88af-fe9282af18b1 | -12.0894 | -47.3382 | 2025-05-26 13:00:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 102.5 |
| 8fb234de-d850-3907-9d18-1f53dc2648f4 | -12.3894 | -50.0002 | 2025-05-26 13:00:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 90.1 |
| cbcd6f98-236d-3d5e-add8-9d758fd3f5fe | -12.0699 | -47.3632 | 2025-05-26 13:00:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 100.5 |
| ed4b83c9-192c-325a-a376-50b4148301a7 | -12.4086 | -49.9978 | 2025-05-26 13:00:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 106.8 |
| 07486aeb-afb9-3f48-84e7-556d172b5ed3 | -8.0123 | -43.1984 | 2025-05-26 13:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 152.0 |
| 5ed0fca9-91c1-348d-b5c3-b99fe108699b | -12.3522 | -49.94 | 2025-05-26 13:00:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 116.1 |
| a01d712c-e838-340b-bc89-04bee22b20f8 | -12.3717 | -49.916 | 2025-05-26 13:00:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 105.5 |
| a1219ad7-a0c9-3ed2-8ab6-53cabe9e24d2 | -12.4089 | -49.9762 | 2025-05-26 13:00:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 275.5 |
| 3890f711-30b6-3937-8880-29fc6691db65 | -8.0312 | -43.1964 | 2025-05-26 13:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 207.9 |
| 69a1e46a-e719-35b8-b1d2-4805395ccf35 | -13.6871 | -45.2487 | 2025-05-26 13:00:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 91.7 |
| bf83ce86-59f1-3c37-85a5-9311f0ada3b5 | -12.0703 | -47.3408 | 2025-05-26 13:00:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 114.7 |
| 7cee0c93-32ec-34fb-bc9c-42d1be926043 | -12.3898 | -49.9786 | 2025-05-26 13:00:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 228.2 |
| dd49d140-3faa-30bc-9701-8026af6eea54 | -12.51461 | -57.22859 | 2025-05-26 13:01:00 | TERRA_M-T | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 32.5 |
| 644c2acb-740d-31ec-b90c-73dbd0176898 | -10.51332 | -53.6584 | 2025-05-26 13:01:00 | TERRA_M-T | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 13.5 |
| 01385ff4-8c7f-31e8-b84a-4be44b79b6da | -9.28884 | -50.44164 | 2025-05-26 13:01:00 | TERRA_M-T | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 13.6 |
| 33a79d8a-7d45-3b0c-ad1f-d5534586a931 | -11.58076 | -47.61306 | 2025-05-26 13:01:00 | TERRA_M-T | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 37.1 |
| c71f0edc-2ff7-3a8f-991e-3e249228761e | -7.16163 | -47.09328 | 2025-05-26 13:01:00 | TERRA_M-T | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 214.5 |
| bf90f9ba-ae04-32bb-b96c-d5253a9c7159 | -7.66743 | -46.09068 | 2025-05-26 13:01:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 31.4 |
| 2ab6d6cb-6eec-37bf-9279-8041cd38ced9 | -7.67394 | -46.09837 | 2025-05-26 13:01:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 36.1 |
| 8d66cc29-7aea-34ef-b991-921bfa1120db | -11.5772 | -47.64334 | 2025-05-26 13:01:00 | TERRA_M-T | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 26.8 |
| cba4afc4-3017-3344-b1a0-30dbd424f574 | -10.51916 | -46.8336 | 2025-05-26 13:01:00 | TERRA_M-T | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 46.9 |
| 4b5c620e-cf77-3e0b-8e29-d0af7464729f | -8.48424 | -47.04616 | 2025-05-26 13:01:00 | TERRA_M-T | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 30.9 |
| 210fe670-c992-34ec-baf9-41e18a45b73f | -8.61951 | -51.5453 | 2025-05-26 13:01:00 | TERRA_M-T | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 38.9 |
| e166332f-3047-3c64-a99c-0f2ff56e7327 | -7.96741 | -50.73711 | 2025-05-26 13:01:00 | TERRA_M-T | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 12.7 |
| bb1c23c9-24a0-3aab-97f3-8304db616241 | -12.41343 | -49.98285 | 2025-05-26 13:01:00 | TERRA_M-T | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 28.3 |
| 62dc759a-fab6-32e2-9f69-8da57c3d47ae | -12.34448 | -49.9061 | 2025-05-26 13:01:00 | TERRA_M-T | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 19.8 |
| f8159807-12f6-38e4-947b-153d26ea0c4c | -13.93744 | -54.49407 | 2025-05-26 13:01:00 | TERRA_M-T | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| eef4b1c3-4ad7-34f1-ae85-16ed8b1702e1 | -12.37168 | -52.48175 | 2025-05-26 13:01:00 | TERRA_M-T | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 15.0 |
| 0e734d8b-f98b-3346-85de-f46ec99dd46b | -10.93368 | -54.68167 | 2025-05-26 13:01:00 | TERRA_M-T | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 14.5 |
| 7c13ddf3-04b4-3911-8972-e78610ee7a71 | -12.39945 | -49.99643 | 2025-05-26 13:01:00 | TERRA_M-T | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 120.6 |
| c58c491f-c614-3664-96d0-f22402168986 | -12.07742 | -47.37743 | 2025-05-26 13:01:00 | TERRA_M-T | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 42.9 |
| 62bdd99b-3cf6-3ca9-845c-a013cb953fab | -7.68378 | -46.09275 | 2025-05-26 13:01:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 44.4 |
| 7ce363a2-994c-3937-8d97-55510686213a | -13.78768 | -54.31024 | 2025-05-26 13:01:00 | TERRA_M-T | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 15.9 |
| b5e8792c-7acb-3507-96e6-f15668868b09 | -7.65758 | -46.09634 | 2025-05-26 13:01:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 58.8 |
| cb9831dd-7645-3945-9a10-b66007416316 | -12.35752 | -49.90762 | 2025-05-26 13:01:00 | TERRA_M-T | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 230.0 |
| a41e5060-903b-31ed-bfb6-fd4e3b307212 | -12.13314 | -54.66091 | 2025-05-26 13:01:00 | TERRA_M-T | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| a025778a-7fde-367e-87c9-3e2c1c0b4f12 | -8.61458 | -51.55191 | 2025-05-26 13:01:00 | TERRA_M-T | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 45.8 |
| dcc3781c-ebcf-33e6-b676-bda439731c07 | -11.9163 | -54.41578 | 2025-05-26 13:01:00 | TERRA_M-T | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 23.2 |
| ba14b992-469c-37e2-ae7b-04f313880215 | -11.36869 | -55.12636 | 2025-05-26 13:01:00 | TERRA_M-T | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 5.8 |
| c4863e82-67db-3ae6-a4b7-d5ac221cea91 | -11.58543 | -54.88982 | 2025-05-26 13:01:00 | TERRA_M-T | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 1c4b29ea-9428-3be7-98f9-801ccf545d6e | -11.57689 | -47.61818 | 2025-05-26 13:01:00 | TERRA_M-T | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 46.3 |
| c2431996-6ae7-32a1-ab74-962a23f9faf9 | -14.16146 | -50.73688 | 2025-05-26 13:01:00 | TERRA_M-T | NOVA CRIXÁS | GOIÁS | Brasil | 5214838 | 52 | 33 | nan | nan | nan | Cerrado | 24.0 |
| 69186bc8-0aef-3a37-8f20-14ce7d0e5e38 | -8.31543 | -48.04943 | 2025-05-26 13:01:00 | TERRA_M-T | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 37.7 |
| 20a9e13b-d043-3ced-b69b-6984ac7f2146 | -12.34203 | -49.92685 | 2025-05-26 13:01:00 | TERRA_M-T | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 47.3 |
| e3a62809-9cae-3ab1-8fba-638cb3d5a757 | -12.52483 | -57.22082 | 2025-05-26 13:01:00 | TERRA_M-T | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 594d0516-3369-3308-97b5-0ba32168641c | -10.51142 | -46.82528 | 2025-05-26 13:01:00 | TERRA_M-T | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 39.5 |
| 9ad30944-11ec-30a5-bea3-ca8338d37dbf | -8.48817 | -47.03981 | 2025-05-26 13:01:00 | TERRA_M-T | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 45.2 |
| 9e5d191a-8c3a-37aa-a4e3-b97c4ee11f6d | -10.24138 | -47.42831 | 2025-05-26 13:01:00 | TERRA_M-T | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 37.3 |
| d0569ecc-71cf-3c6f-9a5e-6aacdfef54d5 | -12.63601 | -54.06173 | 2025-05-26 13:01:00 | TERRA_M-T | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 6f3b8e0b-9d9c-31d6-9573-c3aeddd4d6af | -12.07827 | -47.31792 | 2025-05-26 13:01:00 | TERRA_M-T | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 31.5 |
| fa078763-a8ae-3830-9395-8b94d87cd1f4 | -10.23806 | -47.43474 | 2025-05-26 13:01:00 | TERRA_M-T | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 29.5 |
| cb65bc2f-7c03-3574-a0d6-aa204898d7a7 | -12.40284 | -49.96083 | 2025-05-26 13:01:00 | TERRA_M-T | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 69.9 |
| 5171bd68-5ae1-3d34-9455-4ddc3e3e090b | -12.07469 | -47.35085 | 2025-05-26 13:01:00 | TERRA_M-T | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 303.4 |
| 76d610a2-6078-3f1a-91cb-59e4401d338b | -11.91765 | -54.40569 | 2025-05-26 13:01:00 | TERRA_M-T | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 11.1 |
| a201262e-2eb2-3968-b1ad-62660516c491 | -7.16357 | -47.07092 | 2025-05-26 13:01:00 | TERRA_M-T | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 89.7 |
| c4b2ac40-92b8-3d3d-b38b-37f58b7eb3f0 | -10.24152 | -47.40424 | 2025-05-26 13:01:00 | TERRA_M-T | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 24.0 |
| f7e81675-f050-3f1d-a993-643379258d72 | -11.99354 | -57.20378 | 2025-05-26 13:01:00 | TERRA_M-T | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 6.2 |
| df66a062-cd01-3d3f-8fa4-43d69c62df0f | -7.16016 | -47.09945 | 2025-05-26 13:01:00 | TERRA_M-T | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 144.8 |
| a436bc29-1657-3deb-9dd9-251a8a02648d | -11.13997 | -53.92538 | 2025-05-26 13:01:00 | TERRA_M-T | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 13.3 |
| a7c4be78-919c-326e-b362-01415106e1c5 | -11.59612 | -47.86114 | 2025-05-26 13:01:00 | TERRA_M-T | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 22.2 |
| e5fe510b-6a7e-3ed4-bcd8-f065420a4145 | -12.40198 | -49.97604 | 2025-05-26 13:01:00 | TERRA_M-T | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 502.4 |
| 1b6e6486-9bab-3bb5-8892-5cec211423ae | -12.06535 | -47.34301 | 2025-05-26 13:01:00 | TERRA_M-T | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 35.1 |
| 2fce73cc-1aba-3a69-a409-f2bfbb0be662 | -12.08121 | -47.34488 | 2025-05-26 13:01:00 | TERRA_M-T | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 298.2 |
| e2b17beb-74f9-38bb-b841-01fdd4fbcd8f | -8.62533 | -51.55337 | 2025-05-26 13:01:00 | TERRA_M-T | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 22.1 |
| 4b9a6ff2-f211-3097-b333-717e260b9571 | -12.40044 | -49.98146 | 2025-05-26 13:01:00 | TERRA_M-T | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 493.2 |
| 967afde1-51ef-3f79-9987-bdfd10a65a74 | -7.16524 | -47.06485 | 2025-05-26 13:01:00 | TERRA_M-T | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 36.6 |
| 860dd5e3-72a7-3305-8fb1-ba5f66b9739f | -7.96943 | -50.72198 | 2025-05-26 13:01:00 | TERRA_M-T | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 20.7 |
| 918dd4e4-a872-3fa5-bb1f-53161fe973b4 | -12.09056 | -47.35269 | 2025-05-26 13:01:00 | TERRA_M-T | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 30.9 |
| 47c7acc0-f3c5-3522-ab03-11ab20dfa0eb | -11.36999 | -55.11702 | 2025-05-26 13:01:00 | TERRA_M-T | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 9.1 |
| b95343d7-763c-309d-871b-9ddd4bd5bc30 | -10.6467 | -48.09117 | 2025-05-26 13:01:00 | TERRA_M-T | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 77.2 |
| e90de9a6-e616-3e84-8c47-4774f23f0c74 | -12.35503 | -49.92852 | 2025-05-26 13:01:00 | TERRA_M-T | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 300.7 |
| 806db98d-a192-3312-b813-cc1763629676 | -8.61778 | -51.55878 | 2025-05-26 13:01:00 | TERRA_M-T | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 25.6 |
| 4e11aaf5-926e-3432-ac21-0961cf9ddfce | -18.35648 | -55.18233 | 2025-05-26 13:04:00 | TERRA_M-T | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Pantanal | 5.4 |
| 4f08b18a-8b45-3982-92a2-042dd7e0c2ca | -22.62809 | -52.91438 | 2025-05-26 13:04:00 | TERRA_M-T | DIAMANTE DO NORTE | PARANÁ | Brasil | 4107108 | 41 | 33 | nan | nan | nan | Mata Atlântica | 21.2 |
| babedc20-dc84-3ae9-95c3-16b1713333e8 | -14.83715 | -50.95736 | 2025-05-26 13:04:00 | TERRA_M-T | ARUANÃ | GOIÁS | Brasil | 5202502 | 52 | 33 | nan | nan | nan | Cerrado | 15.7 |
| d6e3dc4d-f225-333d-86c3-d194170ea086 | -16.28188 | -48.64339 | 2025-05-26 13:04:00 | TERRA_M-T | ABADIÂNIA | GOIÁS | Brasil | 5200100 | 52 | 33 | nan | nan | nan | Cerrado | 35.5 |
| f2f1e255-6f7e-3859-8bb3-2a95da511272 | -19.12616 | -51.95919 | 2025-05-26 13:04:00 | TERRA_M-T | CASSILÂNDIA | MATO GROSSO DO SUL | Brasil | 5002902 | 50 | 33 | nan | nan | nan | Cerrado | 67.6 |
| 5805d804-7634-3b69-a0e8-0b00cf423f4d | -14.02702 | -55.1304 | 2025-05-26 13:04:00 | TERRA_M-T | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 10.4 |
| a50ff06b-09ec-3803-b0bc-40842b6abe67 | -19.79379 | -53.82413 | 2025-05-26 13:04:00 | TERRA_M-T | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 41.2 |
| 17c89cf7-ee72-3f7f-8f91-d27d2fb26dbe | -14.02569 | -55.1403 | 2025-05-26 13:04:00 | TERRA_M-T | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 13.9 |
| d771e7a6-2571-308b-9f2b-634ae87e653f | -19.29672 | -55.94077 | 2025-05-26 13:04:00 | TERRA_M-T | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.7 |
| d5c6588f-855d-3099-b967-baa79864a4dc | -14.01935 | -55.13303 | 2025-05-26 13:04:00 | TERRA_M-T | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 14.3 |


[Clique aqui para ver as próximas entradas](README11.md)
