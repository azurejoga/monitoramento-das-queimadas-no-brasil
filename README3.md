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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e0b61684-09eb-34e6-a567-d63edee6c305 | -16.49608 | -47.95037 | 2026-08-22 00:26:00 | TERRA_M-M | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 29.5 |
| a176cbb7-6f25-396d-b1f6-93ce6d58a9b1 | -8.4975 | -54.86709 | 2026-08-22 00:28:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 8ddb2ccc-2db4-364a-b4e5-453cef3d198a | -6.8668 | -59.02784 | 2026-08-22 00:28:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 55.2 |
| a6fbc807-f710-3c9f-a0b3-69bb810dbcf8 | -6.12753 | -57.69217 | 2026-08-22 00:28:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| d11bde8a-e375-37ab-bb43-76217d1da07a | -10.74475 | -50.26022 | 2026-08-22 00:28:00 | TERRA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 82.1 |
| 6062d822-43aa-30c0-a933-6ffad2c292b6 | -6.01342 | -57.79767 | 2026-08-22 00:28:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 104dc295-22f7-3350-8c5a-903ac4eb3757 | -10.75586 | -50.25841 | 2026-08-22 00:28:00 | TERRA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 21.1 |
| c0ed5cfe-6c25-39c9-adf2-62aff73553ec | -6.53372 | -58.52273 | 2026-08-22 00:28:00 | TERRA_M-M | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 24.4 |
| 284b8664-0363-393a-9418-d7e74cb70127 | -6.79416 | -59.41299 | 2026-08-22 00:28:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 401.3 |
| 27bdcb71-36f4-3db4-96e1-591453d0931a | -7.6057 | -60.83006 | 2026-08-22 00:28:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 20.9 |
| f000f7e0-1d51-39f2-9424-957666c75d9f | -6.25041 | -55.41423 | 2026-08-22 00:28:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 46cc12dc-a8d0-3031-b86d-b75f0ebfa777 | -8.22483 | -55.02489 | 2026-08-22 00:28:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 13.4 |
| ac47d9cd-09c2-3948-850c-9ddf83fa475c | -7.54912 | -61.18988 | 2026-08-22 00:28:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 33.1 |
| 4055363e-d6d9-3e19-ae3f-1a46f5f1a49a | -6.8106 | -59.4599 | 2026-08-22 00:28:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.7 |
| d3c9130c-be2c-3ffb-bf1f-eb53f232de08 | -6.81769 | -59.43435 | 2026-08-22 00:28:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 680d70ad-36c3-3f7a-b885-938530fa21a6 | -6.86337 | -59.46516 | 2026-08-22 00:28:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 13.5 |
| 38737c1c-ca30-39ff-94ec-46703e9e3820 | -10.74497 | -50.25365 | 2026-08-22 00:28:00 | TERRA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 79.1 |
| 6791bc0b-c30b-3a6f-960f-a23ef23ccd1e | -6.43552 | -54.96523 | 2026-08-22 00:28:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 17.0 |
| 785a8bac-aa21-3993-897f-8de59e6deb89 | -6.77725 | -58.67325 | 2026-08-22 00:28:00 | TERRA_M-M | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 24.4 |
| 6295a678-b4bb-3f80-a108-cd0342f2cd43 | -6.79484 | -58.63155 | 2026-08-22 00:28:00 | TERRA_M-M | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 36.4 |
| a8a762c1-ab40-3906-b662-775efdc1d7de | -6.76077 | -58.69748 | 2026-08-22 00:28:00 | TERRA_M-M | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 16.2 |
| d8b7ead1-cc0f-3fcb-a407-9fdd78d5fe2e | -6.13521 | -57.74943 | 2026-08-22 00:28:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| e07fc4ce-3e00-3286-ad6c-acdce220da65 | -10.24413 | -50.3715 | 2026-08-22 00:28:00 | TERRA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 47.8 |
| 5463a314-fa21-388d-a8f0-ba66ff2c92df | -6.09194 | -59.9659 | 2026-08-22 00:28:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 16.5 |
| b2aebd50-6c81-31d5-8ccb-b3eaa3ed9542 | -6.15351 | -57.74689 | 2026-08-22 00:28:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 5977fbbd-02e8-3261-9545-c51dc4cee73f | -6.79725 | -59.43702 | 2026-08-22 00:28:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 264.9 |
| 7807b606-840b-3d6c-8e58-41179156ea3b | -7.3648 | -55.6836 | 2026-08-22 00:28:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 22.9 |
| eee01b35-caad-380d-91b8-0d54b2d0a700 | -7.50511 | -60.06588 | 2026-08-22 00:28:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 16dea5bb-792f-3a4a-91bb-d335e99d8940 | -9.40854 | -60.42337 | 2026-08-22 00:28:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 19.8 |
| dbfb58b5-a93f-3288-b392-0d40c34853e0 | -6.63499 | -53.37773 | 2026-08-22 00:28:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| a9f81a46-5fe7-32f0-b802-dd81bba72c59 | -6.82632 | -59.42087 | 2026-08-22 00:28:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 185.9 |
| d5689ffd-5651-3d3d-b149-8fe1ff478f73 | -6.5433 | -58.52148 | 2026-08-22 00:28:00 | TERRA_M-M | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 25.9 |
| a86bcaf4-3097-3bb6-8207-652ae84869bf | -6.77047 | -58.69614 | 2026-08-22 00:28:00 | TERRA_M-M | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 33.7 |
| a3292d77-5bd2-35ed-b73b-f64f67e6c137 | -8.53671 | -54.8249 | 2026-08-22 00:28:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 107.6 |
| b0b428d4-9b09-30af-ad4b-453af325e82b | -8.62387 | -54.7241 | 2026-08-22 00:28:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 654ee319-24bb-34c0-89e4-5a85303a3c8b | -7.08627 | -55.45665 | 2026-08-22 00:28:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| d1481655-0241-3d4c-877a-d493f6230ae5 | -8.58719 | -54.72026 | 2026-08-22 00:28:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 45691dfd-6bb0-31d6-ae41-f68adfb9edcd | -5.8036 | -57.54409 | 2026-08-22 00:28:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 21.6 |
| d1a2b167-be43-32ac-88f8-d145cad69884 | -8.61501 | -54.72536 | 2026-08-22 00:28:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 12.0 |
| b51de620-ab10-3170-a577-3017cf336d13 | -8.5821 | -54.74852 | 2026-08-22 00:28:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| edc03de3-924f-330a-b740-40e646b30129 | -9.17585 | -57.00753 | 2026-08-22 00:28:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 14.6 |
| cdd94f4f-5725-3881-b205-617fac76389e | -6.79881 | -59.44916 | 2026-08-22 00:28:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 13.2 |
| 7ad0f156-11a4-3e5d-b87d-85e7f589431d | -7.34479 | -55.66848 | 2026-08-22 00:28:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 78.0 |
| 27499946-491c-3844-a83b-5550276e6c96 | -7.87469 | -63.74084 | 2026-08-22 00:28:00 | TERRA_M-M | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 22.8 |
| 378df84e-17d0-370b-9cc3-8015e37af1cf | -8.57826 | -54.78563 | 2026-08-22 00:28:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 91b3a2c1-3108-36e6-94aa-ad00709fef8c | -9.18408 | -59.43911 | 2026-08-22 00:28:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 11.6 |
| dbc7c6f4-27ad-3ca0-84b0-87eb1204c178 | -8.53796 | -54.83385 | 2026-08-22 00:28:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 104.1 |
| 7cbbe58e-ad27-38fb-9c1d-c656f7d10bb4 | -6.00293 | -57.85782 | 2026-08-22 00:28:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| a80e9beb-964e-34fa-88bc-f75f4335013a | -6.7758 | -58.66249 | 2026-08-22 00:28:00 | TERRA_M-M | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 23.8 |
| 0cdaf591-cf6a-3e3e-8596-70411d682d11 | -5.96901 | -51.97162 | 2026-08-22 00:28:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 681bb685-bb50-3557-a3a0-91b35f5163c0 | -6.71653 | -48.11407 | 2026-08-22 00:28:00 | TERRA_M-M | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Amazônia | 65.0 |
| ef0bf274-45ca-3ddb-b322-64ed921cb91b | -8.89693 | -60.54084 | 2026-08-22 00:28:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 148.2 |
| 469aff29-ccdf-310a-924a-aa5aeb8b2d08 | -6.16208 | -55.44175 | 2026-08-22 00:28:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 9a5261dd-6510-3ce5-bc38-d627ca4449ee | -8.68304 | -54.74587 | 2026-08-22 00:28:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| cf096a04-d5dc-354f-9682-2ad2b86221a7 | -8.52662 | -54.81722 | 2026-08-22 00:28:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 80.7 |
| 7962a0b2-3935-35dd-983e-5ed9eeadeb7d | -8.57952 | -54.79459 | 2026-08-22 00:28:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 16.1 |
| 9ebb2a96-ac36-3dde-9f13-0968dc8c50ef | -8.54819 | -54.77754 | 2026-08-22 00:28:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| a3bf74f4-5e1c-3460-a4ae-8f64c4c2c187 | -7.87397 | -63.74637 | 2026-08-22 00:28:00 | TERRA_M-M | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 29.6 |
| 893a2137-a29b-3199-b2ef-4f14b726973b | -11.16156 | -54.00905 | 2026-08-22 00:28:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 21.7 |
| 2d3cbb2d-5752-37c3-9409-e77466aada32 | -8.52239 | -55.32277 | 2026-08-22 00:28:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 25.7 |
| c9930bfa-6b71-3aa5-b839-dcfdacf55922 | -5.79407 | -57.54176 | 2026-08-22 00:28:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 18.9 |
| 51dea973-c9e5-3d08-a48e-f47412923694 | -9.11176 | -60.3382 | 2026-08-22 00:28:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 13.5 |
| e1b1dc8a-7ac9-31d4-9ddc-c8345eec5057 | -8.19091 | -54.99049 | 2026-08-22 00:28:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| e09cac6b-e7cc-3fd5-8c3c-eb8daf9be1ff | -8.62262 | -54.71511 | 2026-08-22 00:28:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 12.0 |
| 03d6f3b1-c9db-31fe-8989-d6a8957aa5cb | -9.40662 | -60.40766 | 2026-08-22 00:28:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 32.6 |
| 848cbdb5-cd8d-3add-8c7f-266c14afc4b3 | -6.77434 | -58.65171 | 2026-08-22 00:28:00 | TERRA_M-M | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 9c733dc2-8e6d-37e3-8f7c-edce20a0cd5a | -9.21097 | -59.77086 | 2026-08-22 00:28:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 22.3 |
| 9ae86ce4-1496-37d8-ba0b-899f6e745c1e | -7.60294 | -60.82416 | 2026-08-22 00:28:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 31.1 |
| 3d92e62f-fc83-3d69-b4fa-d3618e82f528 | -10.80012 | -50.98773 | 2026-08-22 00:28:00 | TERRA_M-M | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 17.1 |
| e1ce4f2f-d23a-3bba-b4e7-dd3e6182ae9d | -6.84833 | -59.43023 | 2026-08-22 00:28:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 24.8 |
| 76d84011-3a8c-35a4-b0a2-3eccc3279a33 | -6.55148 | -58.50982 | 2026-08-22 00:28:00 | TERRA_M-M | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 18.7 |
| b651f14a-6ae3-3f68-b6d7-46cdda22fbef | -6.90196 | -58.98839 | 2026-08-22 00:28:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 499e38d0-2b32-3560-bab5-3ae42c74e065 | -10.73364 | -50.26204 | 2026-08-22 00:28:00 | TERRA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 8460fb7c-f21d-3e9d-b718-25834a58ff60 | -8.45604 | -51.55506 | 2026-08-22 00:28:00 | TERRA_M-M | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 108a4f15-c8da-3684-8f2c-caba243627cd | -6.81853 | -59.68544 | 2026-08-22 00:28:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 10.2 |
| c6ca86eb-ea25-395e-8e75-4f8a9108853f | -6.80729 | -59.65464 | 2026-08-22 00:28:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 9.7 |
| e60d21e5-e2ae-362e-9709-3b14bfea5fb8 | -6.67291 | -56.34225 | 2026-08-22 00:28:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 4cfe2ab8-6700-3e9e-a7bb-d5122adc6c6b | -6.85152 | -59.45438 | 2026-08-22 00:28:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 23.7 |
| f5e118f3-0f0a-32a5-aefa-0c7b25287190 | -6.81535 | -59.66049 | 2026-08-22 00:28:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 36.3 |
| 25989735-3693-3b0b-b0a7-98249f61019c | -6.80037 | -59.4613 | 2026-08-22 00:28:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 19.8 |
| 4a666c53-2a69-3aff-9ebf-17ab9a5ab357 | -9.15817 | -59.44819 | 2026-08-22 00:28:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 44.7 |
| b7cc5bd8-0c88-33c2-a28b-96c9c47a955f | -11.04756 | -49.11517 | 2026-08-22 00:28:00 | TERRA_M-M | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 16.0 |
| c43e39eb-5ee8-3a2c-814c-28c2851b07fd | -11.17045 | -54.00773 | 2026-08-22 00:28:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 10.9 |
| c5477038-32c2-33c2-b403-f23a5c3912f0 | -5.79535 | -57.55108 | 2026-08-22 00:28:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 55.2 |
| 63014d2f-e8da-3684-9d64-8369f7575cc3 | -9.15987 | -59.46131 | 2026-08-22 00:28:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 203.8 |
| db7fe100-ea2b-3c6e-a781-bdb37fa1c5a0 | -6.80063 | -59.60486 | 2026-08-22 00:28:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 10.2 |
| c7189a0c-40ee-3b08-ad22-002305111100 | -6.26047 | -55.42188 | 2026-08-22 00:28:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 31759c43-3c29-3394-9098-16ee550f2ec6 | -8.59479 | -54.70996 | 2026-08-22 00:28:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 12.4 |
| bfecdebe-bb6d-3efe-8f5c-19374bcec957 | -9.42002 | -60.42182 | 2026-08-22 00:28:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 14.8 |
| 9c69c392-ba1b-344f-bfe7-ffde742ed01c | -8.16163 | -55.38061 | 2026-08-22 00:28:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| ce91a2ed-8456-3872-8ecc-24c6742b3943 | -8.53363 | -55.3392 | 2026-08-22 00:28:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 1f5e4f6f-0071-3769-a418-841a1eaf0b14 | -6.57323 | -58.97059 | 2026-08-22 00:28:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 5f248a7a-1750-3e70-954b-d1b1b0a0c5a4 | -6.36941 | -54.94707 | 2026-08-22 00:28:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 65.3 |
| 77d4b0bc-e8b3-3ad1-abb6-18d98ddfc1bc | -6.38849 | -54.95353 | 2026-08-22 00:28:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 24.1 |
| ef00bf0c-251c-3c2b-aba4-e85a1752b920 | -6.76611 | -58.66376 | 2026-08-22 00:28:00 | TERRA_M-M | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 170.7 |
| f348acb4-307f-3ce5-b849-6a7960c15af9 | -8.08694 | -51.66859 | 2026-08-22 00:28:00 | TERRA_M-M | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 17ffd3dd-b278-3417-8783-4c798745619b | -10.5136 | -50.77967 | 2026-08-22 00:28:00 | TERRA_M-M | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 13.5 |
| 8c5a2041-e7d8-3bf9-9040-5c30409eebc5 | -9.17936 | -59.4454 | 2026-08-22 00:28:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 60.8 |
| 9d600b6e-d3a9-3c0a-a9f3-1264d501b242 | -9.24757 | -60.80124 | 2026-08-22 00:28:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 17.5 |
| ee8e1555-892e-3e88-88c6-b21156c0dae2 | -7.50694 | -60.0797 | 2026-08-22 00:28:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 26.5 |


[Clique aqui para ver as próximas entradas](README4.md)
