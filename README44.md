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

## Dados Diários - Página 44

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| bf2b1b3f-191f-3430-a433-8dd048ba5f76 | -10.5139 | -49.9684 | 2024-10-13 03:47:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 59f33dd8-d3a5-30e3-87b5-074e2eff904f | -10.51333 | -49.96724 | 2024-10-13 03:47:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 301c71b8-1fec-33cd-ad6f-8533a2568fed | -10.48243 | -49.95501 | 2024-10-13 03:47:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 40f391cf-bf73-3b45-ab44-0480430f55a2 | -9.62013 | -48.98664 | 2024-10-13 03:47:00 | NOAA-20 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b7959310-7c3e-341d-a3aa-f40f1d434a9e | -9.6192 | -48.9916 | 2024-10-13 03:47:00 | NOAA-20 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 56b49657-0333-3bb2-813c-50d74bd74cfe | -9.61911 | -48.98837 | 2024-10-13 03:47:00 | NOAA-20 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 4459d20b-feac-324c-a3c1-b984337e42d2 | -10.52076 | -49.9632 | 2024-10-13 03:47:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 86f783c8-76cf-38d6-b4ef-39f598c0ba2b | -10.51867 | -49.97402 | 2024-10-13 03:47:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 391d3651-f0e0-3e10-97f2-6397ea5d9eee | -10.51812 | -49.98053 | 2024-10-13 03:47:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| e1c0c735-6d28-356c-91d7-53d50c34af0a | -10.51762 | -49.97943 | 2024-10-13 03:47:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| c2441dfa-28bb-3460-b0f5-552e156d64d9 | -10.51498 | -49.96301 | 2024-10-13 03:47:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 38306420-39b3-3cae-abfb-2e0dbffd50fa | -10.51281 | -49.97379 | 2024-10-13 03:47:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 15f11936-c59f-3aa5-b537-5d1ec30567e2 | -10.51228 | -49.97264 | 2024-10-13 03:47:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| a3175ddb-103c-3e41-be80-ec009f55756f | -10.51173 | -49.97919 | 2024-10-13 03:47:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 6d3b3ffe-8afc-3073-a344-95bbf13ead53 | -10.51123 | -49.97806 | 2024-10-13 03:47:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 842dec12-a542-35b3-87c1-810d52efc3e3 | -10.50859 | -49.96165 | 2024-10-13 03:47:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| df453fea-873f-343c-9ea5-a1a078bafb92 | -10.48882 | -49.95637 | 2024-10-13 03:47:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 02712377-11fe-3a90-8ef4-d21b082141eb | -10.48303 | -49.9563 | 2024-10-13 03:47:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 4bdf2a72-907d-3335-89f8-be8b585d2cd2 | -2.17315 | -48.84956 | 2024-10-13 03:47:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e7bdfa66-527a-3a5b-ac0a-e9d955e00b35 | -2.17241 | -48.84942 | 2024-10-13 03:47:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 0488644e-ad58-3a5c-adfd-54f4ec381ffd | -2.16632 | -48.84839 | 2024-10-13 03:47:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4d296fc2-c349-37c4-b05e-0939c10398db | -2.16558 | -48.84823 | 2024-10-13 03:47:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8574ea99-6248-37ae-a3e7-14eeb4192b02 | -2.79172 | -49.29704 | 2024-10-13 03:47:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 4be51b61-a4f3-388f-b1cb-66fec4d9bc40 | -2.79107 | -49.29548 | 2024-10-13 03:47:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 11.6 |
| db537296-f583-3f4d-b80c-af8129e74216 | -2.79061 | -49.3036 | 2024-10-13 03:47:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 14.5 |
| c6afba70-ca87-3739-b083-0862b39674e7 | -2.78992 | -49.30202 | 2024-10-13 03:47:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 11.6 |
| 83d8aead-d903-30b4-8eb6-82dad94de252 | -2.78477 | -49.29584 | 2024-10-13 03:47:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 85a12419-161f-32cb-a0ab-a453349e8517 | -2.77234 | -49.36908 | 2024-10-13 03:47:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 3268d86d-e51d-36c0-8926-b9c2f2d65856 | -2.98646 | -49.52851 | 2024-10-13 03:47:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| af316ac4-9e3d-38cf-b38b-1cb1945b1596 | -2.98533 | -49.5352 | 2024-10-13 03:47:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 19549632-f4d0-3b5b-a986-4165e1272a81 | -3.69751 | -50.11668 | 2024-10-13 03:47:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 03d5ca4d-65f1-3104-9b2b-a8f7e5a8696e | -3.69629 | -50.12365 | 2024-10-13 03:47:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| d988d1fa-cc8b-3822-8ab1-c3963e7104d2 | -3.69505 | -50.13076 | 2024-10-13 03:47:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| d0a62362-4ee3-3981-adb0-b1cc9ed4dc5a | -3.68911 | -50.12233 | 2024-10-13 03:47:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 7ccb685e-180c-3dfd-84f1-e8a86e5031bf | -3.68783 | -50.12964 | 2024-10-13 03:47:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 5753d553-f455-3ea0-ad84-b184358fd932 | -10.79199 | -51.1359 | 2024-10-13 03:47:00 | NOAA-20 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 71653f39-e154-3bc2-8106-dffe00c51e1f | -10.79159 | -51.13366 | 2024-10-13 03:47:00 | NOAA-20 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 11b9a066-a833-3d0b-ba7c-a8bb82fbae9c | -10.78651 | -51.12809 | 2024-10-13 03:47:00 | NOAA-20 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ab0b78f4-d163-3fbd-9ac3-43e010ac590d | -10.78608 | -51.12577 | 2024-10-13 03:47:00 | NOAA-20 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ed256f50-46fd-3a37-8b04-1cce343ea9b1 | -10.78479 | -51.13216 | 2024-10-13 03:47:00 | NOAA-20 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e3fdac2c-02c9-351c-87cb-2e6ad874403b | -9.30433 | -35.60241 | 2024-10-13 03:49:00 | NOAA-20 | SÃO LUÍS DO QUITUNDE | ALAGOAS | Brasil | 2708501 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 1e5626d7-4ae9-309b-b3c5-0a71cf39d992 | -9.30375 | -35.60614 | 2024-10-13 03:49:00 | NOAA-20 | SÃO LUÍS DO QUITUNDE | ALAGOAS | Brasil | 2708501 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 66810b51-7597-3864-b878-4d42f15857f7 | -9.30092 | -35.60189 | 2024-10-13 03:49:00 | NOAA-20 | SÃO LUÍS DO QUITUNDE | ALAGOAS | Brasil | 2708501 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 9d83fb77-149d-3ed2-9541-4baa2e83fef4 | -9.71504 | -36.43626 | 2024-10-13 03:49:00 | NOAA-20 | LIMOEIRO DE ANADIA | ALAGOAS | Brasil | 2704203 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| f245fc5e-a802-3120-b99a-b15c785ed1e7 | -9.71452 | -36.46165 | 2024-10-13 03:49:00 | NOAA-20 | LIMOEIRO DE ANADIA | ALAGOAS | Brasil | 2704203 | 27 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| e3365b77-e6f4-3c2d-a1c6-9bb9a0330410 | -9.71061 | -36.44282 | 2024-10-13 03:49:00 | NOAA-20 | LIMOEIRO DE ANADIA | ALAGOAS | Brasil | 2704203 | 27 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 49044a68-0205-3398-9885-5cdd0180d71e | -10.36092 | -36.36304 | 2024-10-13 03:49:00 | NOAA-20 | PIAÇABUÇU | ALAGOAS | Brasil | 2706802 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 3a65b8d9-fe20-3022-914c-22fff6c987f2 | -9.91996 | -39.03313 | 2024-10-13 03:49:00 | NOAA-20 | CANUDOS | BAHIA | Brasil | 2906824 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 6556b923-e5e8-390b-92d6-92b53075ca9a | -9.91659 | -39.03259 | 2024-10-13 03:49:00 | NOAA-20 | CANUDOS | BAHIA | Brasil | 2906824 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| c33e7e1d-fcd7-303b-b732-85fbe400d575 | -14.71119 | -40.36368 | 2024-10-13 03:49:00 | NOAA-20 | PLANALTO | BAHIA | Brasil | 2925006 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 476c833c-7eed-388a-b5ba-82ce09b75deb | -14.71058 | -40.36742 | 2024-10-13 03:49:00 | NOAA-20 | PLANALTO | BAHIA | Brasil | 2925006 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 0ba2ba6d-f278-3cdb-9f48-d742d8e774cc | -8.86105 | -40.87595 | 2024-10-13 03:49:00 | NOAA-20 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 1.1 |
| ca3653d4-09d0-334e-9714-d86ebaadb209 | -8.66931 | -40.40638 | 2024-10-13 03:49:00 | NOAA-20 | LAGOA GRANDE | PERNAMBUCO | Brasil | 2608750 | 26 | 33 | nan | nan | nan | Caatinga | 60.7 |
| 323dbeff-e76b-3e25-bf52-9819f8a52e60 | -8.66862 | -40.41053 | 2024-10-13 03:49:00 | NOAA-20 | LAGOA GRANDE | PERNAMBUCO | Brasil | 2608750 | 26 | 33 | nan | nan | nan | Caatinga | 14.4 |
| e8b91531-4475-390f-8d36-c867c88ace9d | -8.51796 | -40.81778 | 2024-10-13 03:49:00 | NOAA-20 | DORMENTES | PERNAMBUCO | Brasil | 2605152 | 26 | 33 | nan | nan | nan | Caatinga | 1.6 |
| bf0763e9-0e92-33dc-bc9a-739e60c16b33 | -10.63635 | -40.52997 | 2024-10-13 03:49:00 | NOAA-20 | CAMPO FORMOSO | BAHIA | Brasil | 2906006 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| a4b67bc6-a4e7-32a6-a14c-e0b116197207 | -14.75073 | -41.68883 | 2024-10-13 03:49:00 | NOAA-20 | PRESIDENTE JÂNIO QUADROS | BAHIA | Brasil | 2925709 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 244c7a1d-1c6d-3d7b-a359-c234dfbf89f8 | -16.55438 | -41.82251 | 2024-10-13 03:49:00 | NOAA-20 | ITINGA | MINAS GERAIS | Brasil | 3134004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| e553e660-58f3-3c2b-abe6-ef186a5ee42b | -15.32776 | -41.90678 | 2024-10-13 03:49:00 | NOAA-20 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 043d47b3-173e-3f20-9b7d-ee59913553d1 | -15.32635 | -41.89341 | 2024-10-13 03:49:00 | NOAA-20 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| e28f1fef-4ab1-38f6-b667-ac4693f5eb99 | -15.32563 | -41.89767 | 2024-10-13 03:49:00 | NOAA-20 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| dd425bcf-0bb1-3290-b942-12f99d21d9cd | -15.32418 | -41.90618 | 2024-10-13 03:49:00 | NOAA-20 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 820d6bda-f364-34b7-b404-80f321ed2c77 | -15.32278 | -41.89275 | 2024-10-13 03:49:00 | NOAA-20 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 87a8c06a-2afc-3a3f-8670-d15bd2a58d11 | -15.32205 | -41.897 | 2024-10-13 03:49:00 | NOAA-20 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 466f1081-2920-34fe-a676-b3734bfe8ec8 | -15.32133 | -41.90129 | 2024-10-13 03:49:00 | NOAA-20 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 3f60a207-7791-3673-869a-91cdb0ff3842 | -15.3206 | -41.90556 | 2024-10-13 03:49:00 | NOAA-20 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 05ecb2db-74f0-38d1-9d60-da551d9fdda2 | -15.31988 | -41.90979 | 2024-10-13 03:49:00 | NOAA-20 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 148c4f50-17c3-38fc-95f6-968721268f27 | -15.3192 | -41.89211 | 2024-10-13 03:49:00 | NOAA-20 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 2bc7351b-2ae6-3571-a533-e40ed1f8e6e0 | -15.31916 | -41.91401 | 2024-10-13 03:49:00 | NOAA-20 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| ae3016d3-63e3-36b3-8993-b272ffe6fedb | -15.31848 | -41.89636 | 2024-10-13 03:49:00 | NOAA-20 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| d7f0ee2c-b578-3631-a4f2-b4a564eab8eb | -15.31775 | -41.90063 | 2024-10-13 03:49:00 | NOAA-20 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 07bd664d-5053-307f-8570-f4fccf17690f | -15.31703 | -41.90487 | 2024-10-13 03:49:00 | NOAA-20 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 4a57c11d-d428-30f1-b69f-68978edc9608 | -15.31631 | -41.90908 | 2024-10-13 03:49:00 | NOAA-20 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 5935e30f-e9f6-324c-9235-d211924a8604 | -15.31562 | -41.89149 | 2024-10-13 03:49:00 | NOAA-20 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 03ddb7c0-ce53-3274-9b9a-9f893756c8e5 | -15.31559 | -41.91329 | 2024-10-13 03:49:00 | NOAA-20 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 81d5ae54-de5f-33b2-80fe-43859a55a085 | -15.3149 | -41.89574 | 2024-10-13 03:49:00 | NOAA-20 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 33.7 |
| a9b3924f-1734-3589-b0b7-7e8da959dd64 | -15.31487 | -41.91751 | 2024-10-13 03:49:00 | NOAA-20 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 19373951-8cf0-345b-a16f-d7b7fbbb3d9c | -15.31417 | -41.89997 | 2024-10-13 03:49:00 | NOAA-20 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 33.7 |
| bbe033d5-4658-3681-a0da-8913d17722f1 | -15.31345 | -41.90418 | 2024-10-13 03:49:00 | NOAA-20 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 6b6b6cac-44e2-370e-b7cc-da22c3575be2 | -15.31274 | -41.90838 | 2024-10-13 03:49:00 | NOAA-20 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| b8c1c207-b388-3221-9cb0-7f517c49caae | -15.31202 | -41.91259 | 2024-10-13 03:49:00 | NOAA-20 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| f2381e3d-8641-3d64-b781-e0454432c947 | -15.31132 | -41.89509 | 2024-10-13 03:49:00 | NOAA-20 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 33.7 |
| d8281f68-1a1a-34ae-9eb9-5712e84040cf | -15.3106 | -41.8993 | 2024-10-13 03:49:00 | NOAA-20 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 33.7 |
| 937962e2-dfbc-3d18-95d9-f5ae07fc3214 | -15.30988 | -41.9035 | 2024-10-13 03:49:00 | NOAA-20 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| d15c7afc-273c-33d5-b279-b7f80c77cb44 | -15.30917 | -41.9077 | 2024-10-13 03:49:00 | NOAA-20 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| f0e3e306-4611-3850-8496-538f994094ed | -15.30848 | -41.89017 | 2024-10-13 03:49:00 | NOAA-20 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 5154b472-1742-3342-bac7-d2d31ca71ed1 | -15.30844 | -41.91191 | 2024-10-13 03:49:00 | NOAA-20 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| cdfd18a4-876c-3109-986e-8de28d29dc0d | -15.30775 | -41.8944 | 2024-10-13 03:49:00 | NOAA-20 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 5693b83d-3aa6-31de-98d0-a06cf90071b1 | -15.30703 | -41.8986 | 2024-10-13 03:49:00 | NOAA-20 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 15d222e1-de0e-3ab9-b645-56fef118b3eb | -15.30631 | -41.90281 | 2024-10-13 03:49:00 | NOAA-20 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| e4b485a8-03d7-35e7-8ce9-42b26dd6455f | -15.30559 | -41.90702 | 2024-10-13 03:49:00 | NOAA-20 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| a33842b3-e0b6-37e8-88ba-a2cc6c45bd8b | -15.3049 | -41.88951 | 2024-10-13 03:49:00 | NOAA-20 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 0a62383a-0b8a-3747-a706-04416b1cdd0d | -15.30487 | -41.91124 | 2024-10-13 03:49:00 | NOAA-20 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 254e2732-553d-359d-9f88-3bb346627353 | -15.30418 | -41.8937 | 2024-10-13 03:49:00 | NOAA-20 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 40e83d10-13a5-3b35-a6c2-c89a7d0a54dd | -15.30346 | -41.89791 | 2024-10-13 03:49:00 | NOAA-20 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 568c49a9-50cb-371f-aad5-692335ba297f | -15.30274 | -41.90213 | 2024-10-13 03:49:00 | NOAA-20 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 4917b593-bc76-3d78-8bd7-482bce4fccc9 | -15.30129 | -41.91058 | 2024-10-13 03:49:00 | NOAA-20 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| c23ed3b8-f240-3fa0-ba6b-337ed729ac27 | -20.41811 | -43.55396 | 2024-10-13 03:49:00 | NOAA-20 | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 0660eabf-e2e8-38b9-976a-aeb674567db8 | -8.92181 | -41.18733 | 2024-10-13 03:49:00 | NOAA-20 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 2723f899-8e18-3597-9535-e1d85684df2a | -10.2114 | -42.44451 | 2024-10-13 03:49:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 3.0 |


[Clique aqui para ver as próximas entradas](README45.md)
