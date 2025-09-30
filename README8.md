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

## Dados Diários - Página 8

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8e3f8bae-24b7-3c28-9358-fe7eaf2a8baf | -10.38359 | -48.15461 | 2025-09-30 00:33:00 | TERRA_M-M | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 7d89492b-75ac-31d0-82ba-80530ddb0c73 | -15.32602 | -46.25828 | 2025-09-30 00:33:00 | TERRA_M-M | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 4.5 |
| a9df5b54-f9f1-3b49-835f-bebd81fcd4ab | -12.96206 | -48.40526 | 2025-09-30 00:33:00 | TERRA_M-M | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| c7dbaf40-f584-3cf9-9de4-41f19035fda8 | -13.21453 | -50.97202 | 2025-09-30 00:33:00 | TERRA_M-M | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 16.8 |
| cb7817bb-6dce-3441-936c-9d1cf39a38b3 | -12.79657 | -46.88966 | 2025-09-30 00:33:00 | TERRA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| db0d3a12-5b46-33ee-8df5-5ad11099c0ed | -14.72523 | -45.24404 | 2025-09-30 00:33:00 | TERRA_M-M | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 13.2 |
| 947937cb-d1db-377f-a2df-6d6f9ee0a786 | -14.08877 | -44.0972 | 2025-09-30 00:33:00 | TERRA_M-M | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 14.2 |
| 8c23bc61-8f15-35bf-886d-b46029ccae6e | -14.5849 | -48.28403 | 2025-09-30 00:33:00 | TERRA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 39.3 |
| d5db44f6-cdf9-3503-87e3-4e812f6fc082 | -14.70511 | -48.157 | 2025-09-30 00:33:00 | TERRA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 60.0 |
| 169c81ba-c53c-3f10-8a5c-215893213435 | -9.023 | -51.71268 | 2025-09-30 00:33:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 11.3 |
| e679d280-9be1-31d3-b234-5eb8cf950185 | -14.53803 | -48.4861 | 2025-09-30 00:33:00 | TERRA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 54.7 |
| 3521815e-dec3-32ec-b57e-ed15da5faf0a | -11.20314 | -47.22945 | 2025-09-30 00:33:00 | TERRA_M-M | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 1c08d607-9ad3-3796-83b0-16105c516aec | -11.74632 | -44.73915 | 2025-09-30 00:33:00 | TERRA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 67.0 |
| 1970422a-d236-335a-b3f5-2492eb0aca3e | -8.72613 | -50.04424 | 2025-09-30 00:33:00 | TERRA_M-M | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 008bcc8d-5047-304b-a92f-fcb5f168e351 | -8.25742 | -45.53363 | 2025-09-30 00:33:00 | TERRA_M-M | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 35.8 |
| 8ce55617-60a6-34d7-8a12-54615374c41c | -13.67162 | -44.31816 | 2025-09-30 00:33:00 | TERRA_M-M | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 14.8 |
| b523b788-71b8-3776-9b42-781be5fc2482 | -14.85647 | -48.32653 | 2025-09-30 00:33:00 | TERRA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 7d3b9897-6ed0-36eb-9704-3cf4c40404e9 | -9.29089 | -54.50666 | 2025-09-30 00:33:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 14.9 |
| bec97646-ce06-342a-b26e-96c9dab72b21 | -11.74929 | -46.85106 | 2025-09-30 00:33:00 | TERRA_M-M | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 11.0 |
| fe107e2a-2e46-39a5-93f7-52a8f944d5d6 | -11.42324 | -44.91079 | 2025-09-30 00:33:00 | TERRA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 21.2 |
| 5b52886b-37ab-353d-95b9-1031e14778f4 | -11.13971 | -54.1301 | 2025-09-30 00:33:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 13.9 |
| c1e3e0ca-13d8-3aff-98d2-a82393c69ec4 | -11.89971 | -48.04853 | 2025-09-30 00:33:00 | TERRA_M-M | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 7521dad3-81f1-32eb-9b2b-03204b64bfee | -9.58972 | -54.59988 | 2025-09-30 00:33:00 | TERRA_M-M | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 12.5 |
| 16b93eca-e6dc-3c55-9a45-762e5f1f335a | -9.59162 | -54.59387 | 2025-09-30 00:33:00 | TERRA_M-M | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 11.5 |
| 3fa9c7b3-d59e-307d-a86a-f3c4b0154d9e | -11.42323 | -44.90481 | 2025-09-30 00:33:00 | TERRA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 32.8 |
| 7465fd2b-a247-3b7d-a52d-4a15c450dc78 | -13.23523 | -48.44963 | 2025-09-30 00:33:00 | TERRA_M-M | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 9.1 |
| e780e121-0bfa-3fb7-b030-00f474f81382 | -13.23353 | -47.31037 | 2025-09-30 00:33:00 | TERRA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 9.6 |
| b991eb12-3773-3a23-8a10-857679c6ad06 | -8.90279 | -50.59732 | 2025-09-30 00:33:00 | TERRA_M-M | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 5ebf2543-9e05-3ae0-ac1c-5d021c81876b | -11.46035 | -45.01591 | 2025-09-30 00:33:00 | TERRA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 02bb8e21-66e5-3e55-b751-e7210afdd25b | -8.96587 | -47.44487 | 2025-09-30 00:33:00 | TERRA_M-M | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 29.3 |
| 85c5f043-f45a-3d88-a901-38fb0df291ea | -8.2474 | -45.53474 | 2025-09-30 00:33:00 | TERRA_M-M | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 36.4 |
| 026be47d-a779-37f4-8998-e78a87e57071 | -10.06726 | -48.19184 | 2025-09-30 00:33:00 | TERRA_M-M | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 21.1 |
| 3955e12d-c907-3ed1-b6a9-7313a2946320 | -11.49695 | -43.53296 | 2025-09-30 00:33:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 3003c05c-856b-3f3f-8391-0fb92412ddb8 | -15.60211 | -46.25364 | 2025-09-30 00:33:00 | TERRA_M-M | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 7.1 |
| a8c017a0-2cd7-32ca-853e-6a583aa13bfb | -7.91479 | -44.60813 | 2025-09-30 00:33:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 20.7 |
| c940728f-ab3e-3d4b-a16d-9e34b51c0c3b | -15.29225 | -46.41189 | 2025-09-30 00:33:00 | TERRA_M-M | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 35492823-1bbf-3cdd-9bdf-44d2d3a3663f | -8.44152 | -46.93814 | 2025-09-30 00:33:00 | TERRA_M-M | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 13.3 |
| c3a3500b-db4a-31b7-acea-1a61ad7e5edb | -8.14807 | -46.38397 | 2025-09-30 00:33:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 24.2 |
| f7cbfa85-cea9-3270-a38c-199ab04482d0 | -11.71192 | -44.43937 | 2025-09-30 00:33:00 | TERRA_M-M | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 10.0 |
| af554773-fe98-3377-a0f8-eb836ec5a040 | -14.55467 | -48.47433 | 2025-09-30 00:33:00 | TERRA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 057fb110-a313-3e36-921a-2d228140818b | -9.42297 | -54.72875 | 2025-09-30 00:33:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 30.0 |
| c331b98d-cf32-306c-9845-99160ce837af | -11.20057 | -47.21117 | 2025-09-30 00:33:00 | TERRA_M-M | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 35.2 |
| ab650bcd-cc36-36fc-970f-2cb1bd77cd3d | -13.01768 | -49.44172 | 2025-09-30 00:33:00 | TERRA_M-M | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 107fdce9-cb5e-35bf-946a-89806ecc89ff | -14.52436 | -48.38395 | 2025-09-30 00:33:00 | TERRA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 5be57eb4-eea3-3431-8db2-8680cf2530b0 | -9.93646 | -47.46509 | 2025-09-30 00:33:00 | TERRA_M-M | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 15.9 |
| 21a01be7-7cec-344f-92cb-fc47e151ccfa | -12.76459 | -47.76914 | 2025-09-30 00:33:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 8e48f4d2-0677-31a7-bed1-4e777fbfa739 | -11.22137 | -47.22086 | 2025-09-30 00:33:00 | TERRA_M-M | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 43.5 |
| 693e4938-299b-341d-82ae-90d085348a75 | -13.00627 | -44.12618 | 2025-09-30 00:33:00 | TERRA_M-M | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 13.7 |
| f8d4443e-0973-360d-9e4d-191e97d2d377 | -14.59381 | -48.28281 | 2025-09-30 00:33:00 | TERRA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 0aa5b78c-c7f7-3623-b072-7a270b438983 | -11.74798 | -46.84195 | 2025-09-30 00:33:00 | TERRA_M-M | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| f130b6b3-9cd2-3056-bd4d-92a0227d9e2a | -14.68491 | -48.14147 | 2025-09-30 00:33:00 | TERRA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 716bec7c-e172-3d93-a2c6-5c6895f17485 | -12.838 | -46.98022 | 2025-09-30 00:33:00 | TERRA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 14.6 |
| 3fc9dc58-d565-3d77-a5f9-f3fb722f00fb | -8.5306 | -44.66651 | 2025-09-30 00:33:00 | TERRA_M-M | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 17.1 |
| d6973a5e-cf22-3153-8207-55ae11a1b187 | -11.89214 | -48.05877 | 2025-09-30 00:33:00 | TERRA_M-M | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 14.3 |
| 09deba1d-2781-38f2-99c5-1fe55692e51b | -14.53929 | -48.4956 | 2025-09-30 00:33:00 | TERRA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.2 |
| f9c26439-2e43-3d30-a55e-482df54379b1 | -14.19534 | -46.60689 | 2025-09-30 00:33:00 | TERRA_M-M | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 09d4bef6-c739-3503-9918-f39245de1aab | -13.40486 | -47.53964 | 2025-09-30 00:33:00 | TERRA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 19.1 |
| a08313fb-b689-3c31-86e9-8a10647cb481 | -12.95319 | -48.4065 | 2025-09-30 00:33:00 | TERRA_M-M | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 626a189c-f728-31d9-8a9f-b87dd27f2909 | -14.68864 | -48.16912 | 2025-09-30 00:33:00 | TERRA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 04a65508-4f32-3283-addd-ac95e8702491 | -12.95876 | -46.40948 | 2025-09-30 00:33:00 | TERRA_M-M | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 109bda76-6b87-3514-b96a-06ff55769e99 | -14.60396 | -48.29077 | 2025-09-30 00:33:00 | TERRA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 4dd6ef35-fb15-3a67-afda-a83605387abe | -14.51521 | -48.4516 | 2025-09-30 00:33:00 | TERRA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 18.3 |
| 5231c191-3a73-3eec-9c57-69d243a65d7d | -9.40801 | -54.71117 | 2025-09-30 00:33:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 52.4 |
| 299b71af-0416-3919-b169-bb2b43279f2a | -11.20186 | -47.22031 | 2025-09-30 00:33:00 | TERRA_M-M | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 42.4 |
| c7885ac4-df82-3c0a-98ef-1de660c9743a | -12.96328 | -48.4143 | 2025-09-30 00:33:00 | TERRA_M-M | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| c8accfc3-f3fa-3b7b-a582-8d10d3d38527 | -7.91686 | -44.62189 | 2025-09-30 00:33:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 32.4 |
| b5766047-cf6b-3de6-8d86-ccabbe79e2d6 | -13.61058 | -48.03694 | 2025-09-30 00:33:00 | TERRA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 8.3 |
| fdadefb7-f8e5-3d5b-8459-8e15f08a132e | -13.81233 | -47.95205 | 2025-09-30 00:33:00 | TERRA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 19e33b05-5b77-3630-a731-e3f510e3a3ca | -14.5229 | -48.441 | 2025-09-30 00:33:00 | TERRA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 17.5 |
| a53e429d-1909-3631-b64a-e7ada5ba6a85 | -12.96013 | -46.41898 | 2025-09-30 00:33:00 | TERRA_M-M | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 5834778f-2ebd-353f-a5f6-cb9471e34b68 | -13.80242 | -47.87967 | 2025-09-30 00:33:00 | TERRA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 9b6ef1b7-0e95-32f9-828d-177cdc33b2f9 | -13.28213 | -48.46174 | 2025-09-30 00:33:00 | TERRA_M-M | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 18.7 |
| 6210c78c-75a9-3730-9bee-c193fb79ad01 | -8.52686 | -44.67389 | 2025-09-30 00:33:00 | TERRA_M-M | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 0cd9dc65-048d-3d97-ba21-98e0171308db | -15.48604 | -48.55769 | 2025-09-30 00:33:00 | TERRA_M-M | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 9de70305-99ab-398c-b418-b84ee91ef11a | -14.39122 | -47.1497 | 2025-09-30 00:33:00 | TERRA_M-M | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 5.7 |
| a11a949a-06d7-30fc-bb6c-6fd38ab553b8 | -11.44178 | -44.96003 | 2025-09-30 00:33:00 | TERRA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 11.0 |
| c8e22fba-17d0-3983-b6e9-61bda2f0f281 | -12.82095 | -46.99791 | 2025-09-30 00:33:00 | TERRA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 205967b2-e076-38b1-8b76-0811b9e12ede | -13.28088 | -48.4526 | 2025-09-30 00:33:00 | TERRA_M-M | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 25.0 |
| 8b3c365a-3e2a-3544-9b8e-96bed3ed8063 | -15.12222 | -48.38437 | 2025-09-30 00:33:00 | TERRA_M-M | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 5.7 |
| efb3ee30-405a-3ebb-b3ad-00be8a7bdf14 | -15.37754 | -47.0816 | 2025-09-30 00:33:00 | TERRA_M-M | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| b54579b4-07fb-3902-8203-983f6c7c210c | -10.18992 | -44.88422 | 2025-09-30 00:33:00 | TERRA_M-M | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 515.0 |
| e3aa9796-37c2-3ada-996d-0a7b5d932a04 | -13.21587 | -47.31298 | 2025-09-30 00:33:00 | TERRA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 984cc837-ff9f-3753-8a6b-f521c5104242 | -12.16484 | -47.77188 | 2025-09-30 00:33:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 7.4 |
| ed1cf4b8-f4e1-37bf-a315-fbfeacc32f2d | -14.65054 | -46.96195 | 2025-09-30 00:33:00 | TERRA_M-M | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 42.0 |
| c9008d71-67f5-355d-a5bb-14cb1fe5f4b8 | -15.32716 | -47.38313 | 2025-09-30 00:33:00 | TERRA_M-M | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 14.9 |
| 7825b4a7-3f05-33f2-af6c-d0201a532d70 | -10.83634 | -47.96742 | 2025-09-30 00:33:00 | TERRA_M-M | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 19.3 |
| 6120cda5-7784-3b55-b371-f6147fec19e1 | -8.77228 | -50.59193 | 2025-09-30 00:33:00 | TERRA_M-M | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 68c968fb-7dcd-34e9-8a8e-140ef000e1c1 | -10.39364 | -48.16224 | 2025-09-30 00:33:00 | TERRA_M-M | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 5d3f9bcb-b864-37fa-87e4-c0d543263322 | -10.09556 | -49.06701 | 2025-09-30 00:33:00 | TERRA_M-M | MONTE SANTO DO TOCANTINS | TOCANTINS | Brasil | 1713700 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| a527f517-fd19-33e8-84d2-2f3f45d0656d | -10.3957 | -49.04298 | 2025-09-30 00:33:00 | TERRA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 10.6 |
| d3c6ec3c-3c41-3c7f-b908-1b027908fa46 | -12.87093 | -46.95658 | 2025-09-30 00:33:00 | TERRA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| e910b4fe-79ee-331d-af9f-0a53c30134cf | -14.79032 | -48.30769 | 2025-09-30 00:33:00 | TERRA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 0587d72f-f175-3fd0-b990-8b325fa3023e | -11.13151 | -48.36092 | 2025-09-30 00:33:00 | TERRA_M-M | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 2a1ec4f7-ac56-3032-8b53-353a4c58a356 | -11.73161 | -44.44282 | 2025-09-30 00:33:00 | TERRA_M-M | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 10.3 |
| ad9ab8f3-9fed-3872-8785-764a81a5477d | -14.51669 | -48.39455 | 2025-09-30 00:33:00 | TERRA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 1656fbb4-a9f7-3954-8746-cceb30c43622 | -13.77973 | -47.86157 | 2025-09-30 00:33:00 | TERRA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 7fda7efc-e641-3ca0-8c1f-50788ef3915c | -13.81048 | -47.48249 | 2025-09-30 00:33:00 | TERRA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 69f4e713-cd08-3f72-ac0f-7c3638b26d9b | -13.01645 | -44.1245 | 2025-09-30 00:33:00 | TERRA_M-M | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 41.1 |
| 8b562476-4306-3f43-9779-112c2bfdb11e | -14.54128 | -48.24018 | 2025-09-30 00:33:00 | TERRA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 0c6bc924-886d-3abb-a022-7d22689178cb | -2.4417 | -47.33149 | 2025-09-30 00:35:00 | TERRA_M-M | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |


[Clique aqui para ver as próximas entradas](README9.md)
