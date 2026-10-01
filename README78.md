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

## Dados Diários - Página 78

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 20c7a548-cae0-38ab-af82-58b11a42eeaa | -8.26784 | -54.75423 | 2026-10-01 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| a5fd3044-7646-3049-935c-b50348d0ea12 | -9.95258 | -51.46148 | 2026-10-01 05:18:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 50228fe9-1200-336b-80c0-9b46a80ae35d | -7.72115 | -54.78968 | 2026-10-01 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 14adb642-d7c7-3f9a-92c7-63fca854bf73 | -7.69976 | -55.05564 | 2026-10-01 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b19ce784-8e47-3215-8641-c343d919c36c | -8.22423 | -54.7477 | 2026-10-01 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 0804d689-b4a7-3261-923d-f0ea486c3074 | -7.49918 | -55.02677 | 2026-10-01 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| b75d1680-5eb3-3497-8f6f-9254c63d35f4 | -6.13526 | -53.29368 | 2026-10-01 05:18:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 70049145-0cea-3129-8128-a71c055c3b1f | -11.74785 | -50.40389 | 2026-10-01 05:18:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 6dc9c300-78ef-3fc8-b1f8-5f02c6a6e8f6 | -9.96245 | -59.2585 | 2026-10-01 05:18:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bcad8361-e63c-3efc-943b-9224f8da3f81 | -9.06335 | -49.86585 | 2026-10-01 05:18:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bf9c8718-755d-3f9e-8add-bc30c82ad5ca | -8.23216 | -54.74888 | 2026-10-01 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ea638154-7f14-3e54-97a9-a91941146d2f | -9.54193 | -56.15868 | 2026-10-01 05:18:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c4b75b95-a01e-3740-bc9d-86a42b689bb9 | -9.78526 | -59.01775 | 2026-10-01 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f402a7a5-691a-3969-824f-d6ef862b3f5b | -7.69908 | -55.06049 | 2026-10-01 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 09cd34b7-4619-31d4-b23c-2711d27538d9 | -10.53658 | -57.78382 | 2026-10-01 05:18:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2932fa9d-3665-3f48-bd6a-c369e785face | -6.08058 | -53.31372 | 2026-10-01 05:18:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f3725f9f-7354-3c2d-9fdf-fb64c182cf8f | -5.85832 | -57.75817 | 2026-10-01 05:18:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| fe95d572-ada9-3542-a93e-9aa36e81e26c | -6.51217 | -55.88292 | 2026-10-01 05:18:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f37f0e44-041e-3b2e-88f5-8ccb431b2635 | -8.84507 | -50.50625 | 2026-10-01 05:18:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3828b329-dc5a-3a75-878e-df38ad518fc6 | -7.78654 | -49.8772 | 2026-10-01 05:18:00 | NOAA-21 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4acb8d97-fce9-3057-8860-d632bae7a5ef | -7.72407 | -49.54686 | 2026-10-01 05:18:00 | NOAA-21 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 34165f56-d6c7-30cc-a4dc-0bf3c47aded4 | -7.49311 | -54.98615 | 2026-10-01 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 16f6141d-f85d-3b99-a8f5-11606a488c3c | -11.29175 | -50.97205 | 2026-10-01 05:18:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 15.7 |
| 219e0fed-2c41-3eea-929b-6b3f26beb44b | -6.68246 | -58.8703 | 2026-10-01 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 46.9 |
| 7e4db2c6-159b-3b75-b058-aca44f5d54d6 | -11.17243 | -54.11466 | 2026-10-01 05:18:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0f8696da-7e36-3c85-ab74-ff24324c3919 | -8.16883 | -54.80105 | 2026-10-01 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| be5e85c0-0c59-3738-9a86-e387f66107d1 | -9.00524 | -65.70318 | 2026-10-01 05:18:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| dcb7b18a-4597-333b-95a7-ff580af3ae2e | -7.73537 | -54.8021 | 2026-10-01 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 934362c7-10fa-315e-9ff6-d18225ee7337 | -5.86056 | -57.76583 | 2026-10-01 05:18:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| c3a79568-1af6-3fc1-9579-0a57a8e0a285 | -10.24667 | -59.02421 | 2026-10-01 05:18:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b5c8d7bd-b2d6-3196-9633-5070bd441df9 | -10.07083 | -63.07759 | 2026-10-01 05:18:00 | NOAA-21 | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c7dcca13-f8cb-334b-b79e-f47c1738e7c2 | -5.12629 | -56.00651 | 2026-10-01 05:18:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| d945d2cd-4f52-3939-93ef-b840381e7b8b | -6.51822 | -55.3597 | 2026-10-01 05:18:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9a20326f-355e-3efd-9fb3-05c5d09095f6 | -6.35075 | -55.33493 | 2026-10-01 05:18:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 78a4a0c1-b956-3a2b-9318-82f5aec83912 | -10.8089 | -57.24206 | 2026-10-01 05:18:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 86c64b3c-0878-3e62-bedb-36401837ec65 | -6.10368 | -57.66731 | 2026-10-01 05:18:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fabbe096-5fe6-38d2-a97c-466d6aa41cc9 | -11.40799 | -51.02706 | 2026-10-01 05:18:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| b2edc120-206f-3aab-8f9e-2f1b278b4fe0 | -11.30218 | -54.88052 | 2026-10-01 05:18:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 03a48398-cbfb-3d7b-8c42-3dc55bd110ea | -6.67201 | -58.87222 | 2026-10-01 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 089605dd-4ca2-34ee-969c-8de0d6971538 | -10.07441 | -63.07821 | 2026-10-01 05:18:00 | NOAA-21 | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 294dd77d-656e-3f9c-8b34-277c3d9955ae | -10.46485 | -59.1313 | 2026-10-01 05:18:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c7d1db02-5d4b-3158-889d-6f519c76a751 | -10.89715 | -56.17582 | 2026-10-01 05:18:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 09578db5-eccf-3ccf-8707-3326d336ff06 | -11.41375 | -51.02438 | 2026-10-01 05:18:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 144ae2f4-3e2e-391b-a81e-c9e36736cbb6 | -10.53831 | -57.77229 | 2026-10-01 05:18:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 221802da-541b-323d-a22d-88e5bc8053f7 | -7.43121 | -55.18098 | 2026-10-01 05:18:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 78dd9144-1e5a-3b90-9c48-d00170096a55 | -6.11629 | -55.69988 | 2026-10-01 05:18:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 728164ea-d019-35c7-97b7-021fb81d07b0 | -12.17987 | -47.38222 | 2026-10-01 05:18:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 48caa28b-75e4-38b3-ba68-5c79d5446dd7 | -11.83875 | -50.95193 | 2026-10-01 05:18:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f8224ddf-15a4-3712-814a-b71cb50d03f5 | -11.28283 | -50.972 | 2026-10-01 05:18:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 20.7 |
| 625b190a-8a6d-3ae1-bd41-9278fa7b59f7 | -7.85404 | -45.82659 | 2026-10-01 05:18:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 1ef77650-662f-372a-bb6d-38ebac687c5e | -6.34702 | -55.33438 | 2026-10-01 05:18:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 681f3fdb-6392-370b-b5ca-92b9b242588f | -7.5507 | -55.02497 | 2026-10-01 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 82ca5f92-75c0-345a-8655-0f781313baa8 | -9.70292 | -58.13016 | 2026-10-01 05:18:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0f75604d-447c-3889-be56-877444b7d41a | -7.3438 | -55.22382 | 2026-10-01 05:18:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ebc091ec-949b-3006-83c5-a63f228aa2c8 | -5.86347 | -53.49333 | 2026-10-01 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5bea261f-4414-31f8-a65c-7434e0e9a06a | -5.86557 | -57.75563 | 2026-10-01 05:18:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| c55f1946-c62c-3ba0-8978-7404ef07019b | -9.02154 | -60.55529 | 2026-10-01 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7a05d12a-596a-306c-9ffd-5e05f4b742f0 | -11.28063 | -50.974 | 2026-10-01 05:18:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| ac850634-80ad-3263-8571-121331e727f0 | -6.36437 | -55.14189 | 2026-10-01 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1e6546f2-2d2f-373a-a70c-fe146930508a | -7.0422 | -50.73022 | 2026-10-01 05:18:00 | NOAA-21 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 877c22f4-8655-399b-99e2-353a73174947 | -6.34329 | -55.33384 | 2026-10-01 05:18:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 56100c7b-6367-3f55-8a00-3b6435ce8fa4 | -7.78599 | -49.87506 | 2026-10-01 05:18:00 | NOAA-21 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 176a0f51-1df3-3bfe-bb79-f2bf93454d0f | -6.10296 | -55.68912 | 2026-10-01 05:18:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6be9cf9f-5aac-349e-b597-7b1743336697 | -11.73574 | -50.41 | 2026-10-01 05:18:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 978d6533-183f-3639-9959-139aace82e85 | -8.88404 | -50.65258 | 2026-10-01 05:18:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a7aeed90-abd7-3f5a-a167-3d6afae974eb | -6.0875 | -56.47297 | 2026-10-01 05:18:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b1779c20-f7c7-37c8-a85e-6369fb7673f8 | -7.73598 | -54.79852 | 2026-10-01 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| efbdc3c8-e62d-39e6-b0ac-9e4efec0f685 | -5.85497 | -57.75764 | 2026-10-01 05:18:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c8357ccd-2bff-34c0-8fb7-e8ae82884a37 | -9.00453 | -65.70727 | 2026-10-01 05:18:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 746b5dcf-6756-339a-9b08-b3950e05333b | -7.84924 | -45.82554 | 2026-10-01 05:18:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 58e42e8b-2cb1-36a6-8d0e-b9b7c5f74b55 | -6.34023 | -55.32879 | 2026-10-01 05:18:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 077f8802-ec74-3d99-b5ea-4dc16eb0f803 | -5.85722 | -57.76532 | 2026-10-01 05:18:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 8a6ea939-8dcb-3e75-a8d6-e9ab5e1c49f0 | -9.02265 | -60.54826 | 2026-10-01 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f94275d9-69bb-3223-b058-1f222c6d03c1 | -11.79181 | -50.50143 | 2026-10-01 05:18:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a0d5ef79-0da2-3a06-abec-7cc7cb810026 | -7.71575 | -54.79915 | 2026-10-01 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 52d24a0d-9ac3-31d1-9c7a-78675d5d6273 | -6.59083 | -52.11861 | 2026-10-01 05:18:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| dc019712-a1b8-39c4-b052-d24107960807 | -6.01012 | -49.55647 | 2026-10-01 05:18:00 | NOAA-21 | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | 20.2 |
| e0cbdd54-c3e5-3003-aa41-bb5f02383519 | -12.19047 | -48.42942 | 2026-10-01 05:18:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 18.7 |
| 2a2a5401-1946-3c42-a943-412468d8552c | -6.01457 | -49.56437 | 2026-10-01 05:18:00 | NOAA-21 | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | 12.1 |
| 09d3f51e-eecb-3fc1-b1a8-9a2b6c2d1276 | -6.83812 | -55.26619 | 2026-10-01 05:18:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6c61a810-a0b8-32b7-ae85-556e70579089 | -11.28239 | -50.97541 | 2026-10-01 05:18:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 10.4 |
| ed30c08a-42be-3592-9311-b84daadf71e9 | -10.81635 | -48.7566 | 2026-10-01 05:18:00 | NOAA-21 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 996711b0-0256-3bea-b59f-4ddad3d05509 | -7.72238 | -54.75386 | 2026-10-01 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d9f5e721-27f7-3cfd-8d33-7302d3046c08 | -6.35381 | -55.33997 | 2026-10-01 05:18:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fc2e361e-f120-3192-a0bd-dbc61aaa1c33 | -6.67916 | -58.86979 | 2026-10-01 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 46.9 |
| 35e7210e-2ee0-3f43-bcd2-2ca6a8d509b1 | -9.12174 | -60.39571 | 2026-10-01 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6910e85d-ad59-30ea-af9f-33fb3b06118c | -10.35345 | -55.44562 | 2026-10-01 05:18:00 | NOAA-21 | NOVA GUARITA | MATO GROSSO | Brasil | 5108808 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 11c7ee11-4d79-37a3-baa8-3fc00c1c0d24 | -7.71649 | -54.79412 | 2026-10-01 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 17a5e4c0-09d0-347f-a337-7e5e4574967e | -7.34345 | -55.59559 | 2026-10-01 05:18:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6981fe2b-576e-3cbd-82f2-eec930f6430f | -7.7209 | -54.76396 | 2026-10-01 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| fa9316d1-a46a-3d75-8714-b9bc947617a9 | -6.92724 | -59.28727 | 2026-10-01 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 6419fe51-83b7-3452-acbb-b883eb6429af | -9.71032 | -65.05898 | 2026-10-01 05:18:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cdc04044-b7ec-3ad3-a3e0-d3e5a6877729 | -9.34159 | -57.17969 | 2026-10-01 05:18:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ccf0e087-097f-3413-9852-57edbe17f006 | -10.53716 | -57.77998 | 2026-10-01 05:18:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fbdf81a5-c259-3d44-a89a-fe10eb61f01c | -7.84698 | -45.82558 | 2026-10-01 05:18:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| cce92e7d-405c-3e46-968d-f63ef01b78d5 | -5.86651 | -53.50151 | 2026-10-01 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 0bfefd52-02a9-3a7f-86a5-fb6c246e4498 | -8.06195 | -55.34089 | 2026-10-01 05:18:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| ef4435da-3080-393c-95fa-3bce1cf75a7b | -11.34659 | -50.9691 | 2026-10-01 05:18:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f3039669-56fc-31e8-a8a5-f4a0a18f365e | -7.34279 | -55.60011 | 2026-10-01 05:18:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 160a2dcd-1fa3-3aca-84ba-9ba43fae6657 | -7.73611 | -54.79707 | 2026-10-01 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |


[Clique aqui para ver as próximas entradas](README79.md)
