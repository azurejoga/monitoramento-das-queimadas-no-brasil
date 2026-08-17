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
| 556fb2af-62e6-3dfe-93d6-1ad660921134 | -13.78538 | -53.80971 | 2026-08-17 04:21:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 20a34178-8de0-356c-bf21-2cc2eb7afe78 | -11.05077 | -47.22672 | 2026-08-17 04:21:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d1c07e7c-da06-3c4c-a619-3516fde736bf | -13.28384 | -48.69837 | 2026-08-17 04:21:00 | NOAA-21 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| ad9fa2ff-f52e-3ea1-b513-be0c7b478e2a | -15.15284 | -48.08149 | 2026-08-17 04:21:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c1e096c0-172f-359a-bdcd-91100111229f | -13.78839 | -53.80111 | 2026-08-17 04:21:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| f4bbf255-095e-36ca-a001-9c334bf4e367 | -9.12214 | -45.17972 | 2026-08-17 04:21:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 2525b629-dc91-37e8-ac7e-1260a5073e16 | -14.4964 | -45.67876 | 2026-08-17 04:21:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4abeae1e-a27b-35f2-abc9-8c6e7b0a635d | -7.36413 | -55.4984 | 2026-08-17 04:21:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| b117f5bf-a549-3dd0-8862-b0d11c37aeb9 | -12.03977 | -46.48464 | 2026-08-17 04:21:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| bdb53d49-2dd8-31b7-8dbc-ea8c6cf01fa2 | -11.47198 | -46.59068 | 2026-08-17 04:21:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2495904e-c514-3c45-a16c-d7e92e493cab | -9.12299 | -45.97914 | 2026-08-17 04:21:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 402b7d32-d8c5-3fdc-acaa-1e7ee347addf | -12.2454 | -47.03143 | 2026-08-17 04:21:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f61dc8d3-49f5-3166-8c68-9bf2729867a9 | -12.55234 | -47.87011 | 2026-08-17 04:21:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ed838c38-990d-3b47-96f9-6e21c634958e | -7.37903 | -55.51654 | 2026-08-17 04:21:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| fd6d442e-b11c-39ea-9743-e6554a4d3bcd | -7.38152 | -55.50133 | 2026-08-17 04:21:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 90c85729-1abc-3c71-96e1-d4b54faf58a3 | -9.30519 | -49.10285 | 2026-08-17 04:21:00 | NOAA-21 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 34718c63-b760-35a5-9ef2-2f4124945642 | -9.12269 | -45.17624 | 2026-08-17 04:21:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a6684940-117d-3334-923b-a61ff07584cd | -9.47685 | -51.66063 | 2026-08-17 04:21:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| b2ca070b-0464-398c-8fa7-0441bb0c38de | -13.51387 | -46.25512 | 2026-08-17 04:21:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| cab2481a-e054-3fb6-81f2-57be9db2439f | -14.4953 | -45.68598 | 2026-08-17 04:21:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 10a8ded5-271f-3815-a91a-669d82b4c49a | -11.79502 | -51.78101 | 2026-08-17 04:21:00 | NOAA-21 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 714f1a73-9ae3-34ca-a968-5684242c7940 | -10.50406 | -50.40087 | 2026-08-17 04:21:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 78541b38-1596-3592-92ce-83515d66e9e5 | -15.16663 | -48.64305 | 2026-08-17 04:21:00 | NOAA-21 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 11a78ea1-5158-3cc0-b55c-a2ac6c62f0ab | -6.86819 | -56.42194 | 2026-08-17 04:21:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| a4e4802b-2a15-33ac-879a-cef444b5cb1a | -11.40809 | -46.41406 | 2026-08-17 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 68a88ee4-ac6c-3f9c-9089-212799510ebf | -8.51028 | -54.90621 | 2026-08-17 04:21:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6d094b9f-8372-30fa-aa51-262097a8ca12 | -10.94104 | -57.15028 | 2026-08-17 04:21:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 55bc293f-acb9-39f7-a4ee-cc590dbbc49e | -11.44432 | -46.59339 | 2026-08-17 04:21:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| bdf67f01-4157-35d4-8243-034663fbca28 | -13.27324 | -51.68791 | 2026-08-17 04:21:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 24bcf3d1-5e62-3f2e-8c8b-bf160cac0467 | -13.51717 | -46.25566 | 2026-08-17 04:21:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9335c69c-bc8e-33a7-9eec-d76aa1dc470e | -12.26351 | -45.87923 | 2026-08-17 04:21:00 | NOAA-21 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 3c9ec9db-c47a-357a-aed7-899c826ac5bd | -8.67195 | -54.7668 | 2026-08-17 04:21:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7e5e2f95-721f-3cff-a70e-00f9ac9975ad | -11.49967 | -46.58781 | 2026-08-17 04:21:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 32bb9d7d-c2da-3871-a7a0-43c5bb9347c1 | -7.36486 | -55.49436 | 2026-08-17 04:21:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 1b5d621a-0217-38c5-84b0-1621db562056 | -11.71066 | -54.61727 | 2026-08-17 04:21:00 | NOAA-21 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0701e112-191b-3408-845c-1952ef04a8b2 | -14.48306 | -45.67662 | 2026-08-17 04:21:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 5a43c90b-f230-374f-95f5-68b3812ea0e4 | -12.0061 | -46.4612 | 2026-08-17 04:21:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 8cbdbe99-7564-38e9-a353-e9c77e174d72 | -12.24605 | -47.00593 | 2026-08-17 04:21:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a9ca6a53-cd9b-3f61-bd28-2bda049e990f | -13.53428 | -46.27653 | 2026-08-17 04:21:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5b987725-35ff-3630-92bf-bba7e74f51fc | -12.32658 | -47.24717 | 2026-08-17 04:21:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7bc6309c-a644-3424-9e49-4a1b71aad215 | -12.24718 | -43.15194 | 2026-08-17 04:21:00 | NOAA-21 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| b42483f7-16cd-3f50-8288-68b599025430 | -15.72482 | -45.97402 | 2026-08-17 04:21:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e3f10049-8d59-3612-96c5-b5b868585aa5 | -7.38363 | -55.49186 | 2026-08-17 04:21:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 327de897-9c8b-3d9e-88ba-547e098dba77 | -12.17875 | -45.15097 | 2026-08-17 04:21:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2e9374b8-ee3f-3799-81f1-62307e5d2022 | -7.37932 | -55.51359 | 2026-08-17 04:21:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f8c7bcc2-82a5-3458-897e-885be7f86173 | -10.94186 | -57.14604 | 2026-08-17 04:21:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 523a3fd3-9712-3bf0-808f-8295889ca974 | -14.90091 | -46.62675 | 2026-08-17 04:21:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f578d287-5611-3f66-ade7-060c06bad430 | -7.39026 | -55.48582 | 2026-08-17 04:21:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| c3981112-ac0f-326b-af71-1fbda2b0d980 | -14.45912 | -53.07774 | 2026-08-17 04:21:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bc74c5f3-816f-3f4c-bc99-9e65f35e4285 | -10.19127 | -46.40771 | 2026-08-17 04:21:00 | NOAA-21 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 490f47d8-b1bb-3987-9e48-dce7ddbd076d | -12.71734 | -48.4724 | 2026-08-17 04:21:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| f7eaeeeb-b8bf-314a-95f2-2c87819b22c1 | -11.32903 | -55.22507 | 2026-08-17 04:21:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ac0ce705-897b-3918-a685-047b4a08ac8b | -11.4659 | -46.58609 | 2026-08-17 04:21:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 26.4 |
| 5c6f5b1c-f247-3d84-aaaa-b694ca5dc7e9 | -6.54366 | -58.50162 | 2026-08-17 04:21:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 68c275ad-6c4f-3f67-a19c-9642127711ca | -7.77671 | -48.2729 | 2026-08-17 04:21:00 | NOAA-21 | NOVA OLINDA | TOCANTINS | Brasil | 1714880 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| dc5a6943-0052-31e9-b9d9-1c821e5c7f0e | -12.75888 | -48.43519 | 2026-08-17 04:21:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 36c00bd4-87bc-384b-a5d9-5a137dcb5c74 | -11.40478 | -46.41351 | 2026-08-17 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8e577cd2-e677-3e68-8167-23b139529b56 | -13.50833 | -46.2253 | 2026-08-17 04:21:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| dee59690-dbf0-31ab-a2fb-1420fac02dec | -7.37497 | -55.50454 | 2026-08-17 04:21:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| d18a7139-0e11-374e-8a74-175c1134a138 | -11.3954 | -46.40837 | 2026-08-17 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ef2df41f-a6d7-356a-8d17-f15f51f57dd1 | -11.71967 | -54.59724 | 2026-08-17 04:21:00 | NOAA-21 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d675299b-6e30-3b39-8198-ee4d3a13de4c | -7.07236 | -56.65697 | 2026-08-17 04:21:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 6ae467a9-4876-3571-96e4-12f76ab107f5 | -11.72416 | -54.60123 | 2026-08-17 04:21:00 | NOAA-21 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 33be705c-f993-3921-8f37-351812b3a12e | -10.27585 | -48.28546 | 2026-08-17 04:21:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 803239fe-2afa-35c9-93ee-cd8c1084da05 | -7.39749 | -55.47867 | 2026-08-17 04:21:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 97686bb4-284b-35c9-a4e0-1e4052e3e9a6 | -11.20761 | -54.81313 | 2026-08-17 04:21:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 410966bd-5337-36e2-a614-4d1ea7653749 | -13.78731 | -53.79957 | 2026-08-17 04:21:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 06714009-4d8d-3ea5-bf9d-dcefc9bad05c | -12.5526 | -47.8472 | 2026-08-17 04:21:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4b453ccc-47de-33c1-beed-7b488b48c5b2 | -15.1694 | -48.64749 | 2026-08-17 04:21:00 | NOAA-21 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2e507588-fd52-3b30-a3cf-53026885d40d | -11.40753 | -46.41756 | 2026-08-17 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c0bf7b0f-4205-3a12-982b-b45583f46694 | -14.32307 | -53.0504 | 2026-08-17 04:21:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| a28e498f-0855-39a4-bcc5-82eafb6f8310 | -6.84621 | -56.43747 | 2026-08-17 04:21:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4ff5146f-4878-38e7-a593-9d2a03030f5f | -12.0459 | -46.44576 | 2026-08-17 04:21:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0725145f-26cf-35ed-a37a-b57d7a9f074a | -14.45832 | -53.082 | 2026-08-17 04:21:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8520adc7-6fb8-3271-bf4c-19d857864137 | -14.3075 | -53.11095 | 2026-08-17 04:21:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 1c749220-fb45-360e-b8c2-bf2a71b433ed | -11.49691 | -46.58373 | 2026-08-17 04:21:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| d4d9ced8-a087-3be7-bb98-81458039cb77 | -15.06117 | -47.01484 | 2026-08-17 04:21:00 | NOAA-21 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 716ccb90-4d9b-3c33-b674-c97e8805fb63 | -12.6605 | -48.51513 | 2026-08-17 04:21:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| ec98a746-0a2c-3656-82d0-8ae8c8f4eab7 | -9.12672 | -46.0199 | 2026-08-17 04:21:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b20bda6b-5ff9-35bd-a748-421d09115c1b | -14.8903 | -46.6288 | 2026-08-17 04:21:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 47b50597-6ad9-3473-969a-3a92403f0b2b | -12.54616 | -47.86526 | 2026-08-17 04:21:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 05293223-9480-34e5-bc2d-4fd935a30736 | -12.23482 | -47.03337 | 2026-08-17 04:21:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 83634e70-641e-3e9f-9567-8033747a523e | -10.47229 | -50.37463 | 2026-08-17 04:21:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 64829563-cd9a-3237-80b8-529be6809444 | -13.63278 | -56.99183 | 2026-08-17 04:21:00 | NOAA-21 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| e90823dc-c256-3a76-b8ec-d6506fe494a4 | -7.39677 | -55.48274 | 2026-08-17 04:21:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 774cd59f-3b01-3ef4-a72a-1fb0f8c2dbb8 | -8.58899 | -54.68949 | 2026-08-17 04:21:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| a41e5607-ce4c-306c-bb70-5b4188ccdaf4 | -7.38439 | -55.48777 | 2026-08-17 04:21:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 56e66fe8-4f3e-34ea-ae28-f8bee0d80af3 | -14.44117 | -51.97476 | 2026-08-17 04:21:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8c3759d8-2d3e-3289-8bde-96432571a2a1 | -11.714 | -54.6274 | 2026-08-17 04:21:00 | NOAA-21 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 293a4773-78ca-3506-a9d9-10d8a9441d78 | -15.2879 | -48.78114 | 2026-08-17 04:21:00 | NOAA-21 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0f3102e0-e208-397e-8a1e-6f95463f7fc5 | -8.02867 | -55.1443 | 2026-08-17 04:21:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2868fa69-77d6-35c6-8e2a-15169fd3d386 | -7.77962 | -48.27768 | 2026-08-17 04:21:00 | NOAA-21 | NOVA OLINDA | TOCANTINS | Brasil | 1714880 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7abdd355-e062-3640-84c3-8d74453b6fae | -11.13332 | -46.49556 | 2026-08-17 04:21:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 79e4d7f0-abf0-34c6-9e8c-fbfc7d0064df | -11.3202 | -46.21564 | 2026-08-17 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 4851487d-44bf-3959-bb9c-2ef4514bfb49 | -8.51104 | -45.32789 | 2026-08-17 04:21:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a8648e5c-ae8a-388e-a397-ed5f4b3a7fa4 | -6.86907 | -56.41712 | 2026-08-17 04:21:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| db404441-87f2-37b8-915b-faaed7c6e0e0 | -7.38226 | -55.49717 | 2026-08-17 04:21:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e74b8455-8e13-35c3-9aa9-5352e9443264 | -11.47811 | -46.57346 | 2026-08-17 04:21:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9f3acb49-da73-3626-91cc-11f0bc0b91ce | -12.55599 | -47.84777 | 2026-08-17 04:21:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7bb9d721-e0ca-3f76-89b5-5134abc1e7a6 | -10.46672 | -46.30079 | 2026-08-17 04:21:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |


[Clique aqui para ver as próximas entradas](README15.md)
