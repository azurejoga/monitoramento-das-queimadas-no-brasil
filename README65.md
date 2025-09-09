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

## Dados Diários - Página 65

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 49f22de1-37ef-319c-8c16-b83c363566fd | -12.03082 | -51.08138 | 2025-09-09 05:25:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d245a124-4c11-3cd7-a2f1-572c9022af07 | -16.33444 | -52.932 | 2025-09-09 05:25:00 | NOAA-20 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 2fe67e9e-464a-3b65-bb59-9ac3404c5384 | -9.23828 | -60.44147 | 2025-09-09 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1fd9f942-ab4e-34a6-b403-b0634c8033fe | -9.94741 | -60.12977 | 2025-09-09 05:25:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| df03bcd9-a41a-3347-a764-4cd9f300275c | -9.1826 | -59.37853 | 2025-09-09 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6c3fefdc-f4ba-3441-a497-86df79a4a676 | -9.54209 | -59.06614 | 2025-09-09 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ebc90269-2e83-35c2-ac45-23d7647b8e24 | -9.08902 | -65.39257 | 2025-09-09 05:25:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e8bf4ca8-e499-34dd-8cdc-7da9511a351c | -9.22265 | -60.82359 | 2025-09-09 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 9b6abb5f-80cb-3a67-8127-b9f7418e4437 | -9.10804 | -60.99084 | 2025-09-09 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 012e17e0-68bc-37c9-a1cf-6b976f667b03 | -8.7688 | -61.44009 | 2025-09-09 05:25:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 35ad56a2-0087-336f-b1e1-c9fac47d8002 | -9.29727 | -59.52379 | 2025-09-09 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9b70cd68-f7d8-3eca-b298-63b4de276a79 | -9.45771 | -60.51253 | 2025-09-09 05:25:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5281e4d6-2dbf-30f1-8e9a-c1115610f531 | -10.77584 | -59.85782 | 2025-09-09 05:25:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 57ed85de-2b4f-341a-bcb4-e4b1a2d13b58 | -11.21511 | -55.00232 | 2025-09-09 05:25:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 6f327e22-3122-3dfe-9e7e-da632aeb7695 | -9.29879 | -60.85712 | 2025-09-09 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ebb548e5-6232-3d23-a861-56aae9c33b14 | -10.08864 | -59.16916 | 2025-09-09 05:25:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 08a04e18-8461-38e5-83af-7a70e0d63b05 | -10.88808 | -56.35453 | 2025-09-09 05:25:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 28ac8ee2-e4ae-341d-b977-f1cf68280234 | -11.30836 | -50.41478 | 2025-09-09 05:25:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d26fbe06-f747-36b2-9791-e20d9ac2ce4e | -9.1398 | -60.52687 | 2025-09-09 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 37542e29-5a37-394a-9647-16711de1caed | -10.41376 | -60.82546 | 2025-09-09 05:25:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 451e40cc-7443-36d5-b2ef-747fe1fabc5b | -9.17237 | -59.37695 | 2025-09-09 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a92932f4-6f15-3d79-92ab-1e337aea3edd | -11.94751 | -50.97387 | 2025-09-09 05:25:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 95966bfb-3900-3442-be86-eae4d2edfb9d | -9.16518 | -60.79986 | 2025-09-09 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e69eb0dd-b718-3caf-b6b2-22089d410589 | -10.51772 | -64.29113 | 2025-09-09 05:25:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 77db238f-3f33-37c1-8c03-132341dd6e7f | -10.00775 | -64.91795 | 2025-09-09 05:25:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 12.6 |
| 304cd146-0c5d-3dd6-984d-ff026b86283a | -9.45384 | -60.51553 | 2025-09-09 05:25:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1cc6b923-3301-3390-9360-95f86a4d051e | -10.14375 | -61.14186 | 2025-09-09 05:25:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9cde695b-759d-3caf-876f-52f85565f4fb | -10.25387 | -59.37761 | 2025-09-09 05:25:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e99961c2-11e8-3db0-a2b9-d06858f35653 | -9.17068 | -59.36525 | 2025-09-09 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 74627834-62bc-352e-b75b-2791336a0fdd | -9.20561 | -67.55592 | 2025-09-09 05:25:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 106d314a-9e5b-3eac-977b-b8ce45dff095 | -9.4743 | -60.49348 | 2025-09-09 05:25:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7233c395-b15a-399c-bece-0c6a8ff79c24 | -9.18723 | -60.76755 | 2025-09-09 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8f297a09-af0e-346e-a629-1dc1baa9d531 | -11.45437 | -49.27774 | 2025-09-09 05:25:00 | NOAA-20 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 6b2aa84d-151c-3664-be34-86ab7de3ce49 | -11.98981 | -51.02347 | 2025-09-09 05:25:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 617dbf02-30fb-3f07-a4ed-1a69a1cb8a8c | -9.21711 | -60.81555 | 2025-09-09 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8bbd1a45-7564-3997-8f66-0cf35b87c310 | -10.09038 | -59.18124 | 2025-09-09 05:25:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| df5e6419-5ec6-338d-bf51-41ec6e1cf27e | -9.43705 | -60.51627 | 2025-09-09 05:25:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 38742a11-5941-37e6-b1d0-53a52e8f8f94 | -9.12224 | -61.50392 | 2025-09-09 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4a1115e4-e1af-33ca-8823-04b38ebdaa07 | -9.46104 | -60.51306 | 2025-09-09 05:25:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ee8b51a2-3585-3469-9da1-384ffc3b46bc | -11.94492 | -50.96672 | 2025-09-09 05:25:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 02d71832-b93c-378f-93ca-887b55404efc | -8.9821 | -65.45006 | 2025-09-09 05:25:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 46806c25-11e4-3868-8d5d-f8eef08b78d3 | -9.61336 | -55.01062 | 2025-09-09 05:25:00 | NOAA-20 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 68f00482-11e4-3074-8cb7-f5853cb0a0a9 | -10.08984 | -59.16976 | 2025-09-09 05:25:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 42952d12-97f2-3146-9b71-2bd4c34d2ae9 | -11.97359 | -51.00815 | 2025-09-09 05:25:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ff8cf930-c3ee-35f3-80fa-9e1ca137d7f9 | -9.46546 | -60.50654 | 2025-09-09 05:25:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 16e0ce70-ac83-3f31-851a-82b264085688 | -11.16303 | -57.17989 | 2025-09-09 05:25:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 70fe6450-6aae-3e39-bd9d-3e3aefee6596 | -9.17351 | -59.36951 | 2025-09-09 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7493baeb-4688-3e4a-8e3b-2a7516c98cc6 | -10.14706 | -61.14238 | 2025-09-09 05:25:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 83df1e40-82c6-3a61-9ca6-7b49489557b9 | -9.23883 | -60.43796 | 2025-09-09 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5c2166bb-ef47-3e70-9a4d-d2c0218154a0 | -8.71973 | -62.38068 | 2025-09-09 05:25:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 47928524-85d5-3a38-b93b-32fb81ed7531 | -19.81989 | -50.94901 | 2025-09-09 05:25:00 | NOAA-20 | CARNEIRINHO | MINAS GERAIS | Brasil | 3114550 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| e41b3a22-85c8-3f6a-9cfe-32b508dd3425 | -9.05966 | -60.4537 | 2025-09-09 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 433ef7c8-208b-3861-9891-9dad0e565bf9 | -9.46988 | -60.5 | 2025-09-09 05:25:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0e167a0e-f987-35aa-9f98-c20c5b5fe068 | -10.89389 | -55.69868 | 2025-09-09 05:25:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 277e0fbf-89f3-3c71-9799-88e71db16726 | -8.45215 | -62.55249 | 2025-09-09 05:25:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 9991d770-f462-3e0b-bb6a-1de73b13b1b8 | -12.83145 | -47.98896 | 2025-09-09 05:25:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2beb966c-b396-3365-aee9-d44c7baea4d0 | -9.17235 | -60.79742 | 2025-09-09 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b1b83a9d-52c0-31f8-981e-337c8ca23804 | -9.94857 | -60.14468 | 2025-09-09 05:25:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1d181489-f92e-3a98-a40e-adac60ccd8ae | -10.38296 | -56.52714 | 2025-09-09 05:25:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6afefc02-2116-3790-9f8f-9312f14b3cb1 | -11.20615 | -55.00105 | 2025-09-09 05:25:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 342e18c5-5723-3a71-9106-22b9fe16b781 | -19.8339 | -50.93886 | 2025-09-09 05:25:00 | NOAA-20 | CARNEIRINHO | MINAS GERAIS | Brasil | 3114550 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 72278817-2484-34dc-9ac3-4d085313f2e9 | -18.81949 | -49.68962 | 2025-09-09 05:25:00 | NOAA-20 | ITUIUTABA | MINAS GERAIS | Brasil | 3134202 | 31 | 33 | nan | nan | nan | Cerrado | 14.1 |
| 0a6db14c-1c03-3ded-8588-111c85c8e6a7 | -9.08192 | -65.41088 | 2025-09-09 05:25:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 27b03c39-2b66-352d-93fd-6a4cab2ed6da | -9.3834 | -65.94912 | 2025-09-09 05:25:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d2ffa6a8-aca7-3dca-b1c0-162349791e0a | -9.80013 | -57.4522 | 2025-09-09 05:25:00 | NOAA-20 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bfffa9fb-7bc3-3702-a342-c91486020333 | -16.69995 | -48.63836 | 2025-09-09 05:25:00 | NOAA-20 | SILVÂNIA | GOIÁS | Brasil | 5220603 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 18d1a2ef-bf82-3887-bc46-54f5f61c5791 | -16.32306 | -52.93358 | 2025-09-09 05:25:00 | NOAA-20 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 786f9ffb-3953-3feb-a6fa-b6a70fdb4880 | -9.22097 | -60.81258 | 2025-09-09 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5bfd2b07-c6f0-3656-99bd-7ad7d2ae4b19 | -9.69537 | -57.80099 | 2025-09-09 05:25:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ff119fc3-ff6b-3027-8a68-8b819f2e8bc4 | -18.83239 | -49.697 | 2025-09-09 05:25:00 | NOAA-20 | ITUIUTABA | MINAS GERAIS | Brasil | 3134202 | 31 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 5f6e9c6f-ef57-36f6-8b15-9eb5d2801324 | -9.17919 | -59.378 | 2025-09-09 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9d9cda43-b0f4-3b34-a57f-039650781b3d | -9.27688 | -60.91088 | 2025-09-09 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 33679d00-4628-3ea0-ab5e-473f3f784492 | -9.05634 | -60.45319 | 2025-09-09 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5a6ae61f-810e-3fef-ad24-480f0a04f564 | -9.71072 | -57.79885 | 2025-09-09 05:25:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2ba590de-59fa-31be-b025-2951e64a1b2c | -10.17299 | -61.12859 | 2025-09-09 05:25:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 25515bd0-40df-3c0d-bab7-14af1034fdd0 | -10.57835 | -52.03402 | 2025-09-09 05:25:00 | NOAA-20 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d1e81a18-27f6-3d8d-97b7-a0ccfc5e3cf7 | -16.62804 | -51.85203 | 2025-09-09 05:25:00 | NOAA-20 | PIRANHAS | GOIÁS | Brasil | 5217203 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ab30f3c1-9131-33f2-8464-9d6da53a8427 | -9.07992 | -65.40788 | 2025-09-09 05:25:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 69935a76-ce24-3d6a-9f0e-6564cfd31a47 | -9.70832 | -57.78963 | 2025-09-09 05:25:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8197936d-3cd1-3907-9db5-91e277081381 | -9.22122 | -59.51678 | 2025-09-09 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e6edf855-bce4-3b9b-9cb9-625d98747209 | -10.05323 | -59.36285 | 2025-09-09 05:25:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e3f71c3c-ae67-37fa-8565-6e3e7c6b2314 | -9.45439 | -60.512 | 2025-09-09 05:25:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b7600c44-b1dc-3900-aef4-9d9c9acadea0 | -9.10583 | -60.98335 | 2025-09-09 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4a2a6918-2ff6-37ea-9e8b-d6c52129ae9e | -9.17135 | -60.27908 | 2025-09-09 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.2 |
| 38d3f5bf-618a-351b-94a0-3c1426421f58 | -9.75003 | -65.0223 | 2025-09-09 05:25:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2db4133d-bf90-3449-b23d-466f40d2ae8d | -9.92405 | -65.23391 | 2025-09-09 05:25:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 65b2faff-7a4e-3b62-bf8f-3e34b59f793e | -8.54492 | -64.03876 | 2025-09-09 05:25:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 28f76dac-cc59-31f9-a32b-7661ac9e0618 | -9.71135 | -57.79457 | 2025-09-09 05:25:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b53b24d6-38b1-3485-a993-08a76474fb10 | -9.45608 | -60.52311 | 2025-09-09 05:25:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ae482a2a-4514-3bed-b8d6-0051ecd506ea | -9.94212 | -60.49798 | 2025-09-09 05:25:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4c5ea034-4a7f-3a72-abf1-b05340ec5689 | -9.19438 | -60.39488 | 2025-09-09 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 12532ded-d755-334e-8de4-f568669babd7 | -9.47266 | -60.50406 | 2025-09-09 05:25:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 41c6a64b-683f-3e5a-9c3f-965c8c783e96 | -9.44888 | -60.52559 | 2025-09-09 05:25:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fe732727-26f6-3869-9119-e12abc388e3c | -9.38821 | -65.94466 | 2025-09-09 05:25:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ffbbf8b6-e3a1-3f07-8d3f-e278c6387ce5 | -9.16305 | -61.31046 | 2025-09-09 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 26c3ce4e-6ecc-3ef3-8f06-4e34e63cde42 | -9.08492 | -65.4163 | 2025-09-09 05:25:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5e3169d1-b4f6-3eac-8c90-1f4bc42e9c71 | -10.17797 | -61.14013 | 2025-09-09 05:25:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fdf8437c-554a-3803-82c3-88190ede2dde | -10.10282 | -65.13697 | 2025-09-09 05:25:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 77058f46-1bee-3485-9eb1-ab3276213df5 | -9.18318 | -59.37482 | 2025-09-09 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 91fc814c-6282-3e04-a33d-8d23b4cadac9 | -9.44309 | -67.67159 | 2025-09-09 05:25:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |


[Clique aqui para ver as próximas entradas](README66.md)
