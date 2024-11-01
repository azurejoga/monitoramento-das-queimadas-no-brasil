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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b82bdc24-bd2c-3628-92aa-bd1b8059f34e | -4.04855 | -46.07342 | 2024-11-01 00:13:00 | TERRA_M-M | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 23.1 |
| f03b42d4-e34e-33ae-866d-19caceb5df7d | -4.04573 | -46.08023 | 2024-11-01 00:13:00 | TERRA_M-M | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 24.2 |
| 326c0d91-0b21-33c0-857e-4ec44fa77278 | -3.94425 | -48.35888 | 2024-11-01 00:13:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 25.2 |
| 6d1fb511-a9fd-30c5-82b1-e55af5406e52 | -3.94127 | -48.36591 | 2024-11-01 00:13:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 26.4 |
| f6391bc0-7e00-3db2-a6a7-f8f96d3990e9 | -3.88431 | -46.21302 | 2024-11-01 00:13:00 | TERRA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 20.2 |
| 987d2c7a-bc4d-3f82-8294-36d0c8cb50f1 | -3.88221 | -46.21961 | 2024-11-01 00:13:00 | TERRA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 21.2 |
| 210c65b9-686d-34ae-a6ff-80f81a677afa | -3.56626 | -47.39371 | 2024-11-01 00:13:00 | TERRA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 41.0 |
| 03e613ae-93c2-3c99-a92d-96abfe2ca1fd | -3.55649 | -47.40078 | 2024-11-01 00:13:00 | TERRA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 40.5 |
| f3be38a4-57e8-308b-8ea7-2cc54e90b78d | -3.3786 | -46.05366 | 2024-11-01 00:13:00 | TERRA_M-M | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 15.3 |
| 6ed8d824-8ce2-3aa8-b8fc-c78fd813456e | -3.35062 | -44.05384 | 2024-11-01 00:13:00 | TERRA_M-M | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 30.0 |
| 9162a68a-9579-3cee-8d95-b14be6671bcd | -3.28641 | -45.97809 | 2024-11-01 00:13:00 | TERRA_M-M | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 20.6 |
| a607dfa0-1c0a-36a9-97c6-5df92ba2962b | -3.27696 | -45.97299 | 2024-11-01 00:13:00 | TERRA_M-M | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 16.7 |
| fa48451b-3bdc-38c7-b890-1d9efb223a36 | -3.27407 | -45.78628 | 2024-11-01 00:13:00 | TERRA_M-M | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 18.6 |
| 5e557c52-07c6-3b1a-a6a8-db82c8f655a2 | -3.26924 | -45.80433 | 2024-11-01 00:13:00 | TERRA_M-M | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 17.1 |
| 4027d1d6-3d5d-3aab-b76f-72605d858568 | -3.25833 | -45.98195 | 2024-11-01 00:13:00 | TERRA_M-M | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 14.7 |
| b1ec84ee-6de7-36fd-9a41-246e14311279 | -3.16062 | -45.52942 | 2024-11-01 00:13:00 | TERRA_M-M | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 44.7 |
| ab60287a-39f7-3f9e-82e4-a21d6a218911 | -3.15803 | -45.54681 | 2024-11-01 00:13:00 | TERRA_M-M | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 13.9 |
| a9d50e3a-6b5e-3eaf-8ece-65fc3aad3d27 | -3.15509 | -45.52456 | 2024-11-01 00:13:00 | TERRA_M-M | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 39.5 |
| 7fa8c451-3479-3781-b6a1-e43aea98e5fb | -3.14785 | -44.40243 | 2024-11-01 00:13:00 | TERRA_M-M | SANTA RITA | MARANHÃO | Brasil | 2110203 | 21 | 33 | nan | nan | nan | Amazônia | 46.2 |
| 00213327-d591-37c0-b5ef-661869c6f161 | -3.14538 | -44.38446 | 2024-11-01 00:13:00 | TERRA_M-M | SANTA RITA | MARANHÃO | Brasil | 2110203 | 21 | 33 | nan | nan | nan | Amazônia | 83.9 |
| c3d91f66-a9e1-32ed-b2bb-7f38e573efc5 | -3.13309 | -44.38616 | 2024-11-01 00:13:00 | TERRA_M-M | SANTA RITA | MARANHÃO | Brasil | 2110203 | 21 | 33 | nan | nan | nan | Amazônia | 14.7 |
| e414c7c8-b00e-394a-84d3-5c46c76bc928 | -3.11959 | -46.05597 | 2024-11-01 00:13:00 | TERRA_M-M | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 14.5 |
| 0ad3db22-7b1e-375d-9dcc-88b932e0b310 | -3.09902 | -45.58278 | 2024-11-01 00:13:00 | TERRA_M-M | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 267.2 |
| 3486c897-41ab-30da-afb6-72b0032570bd | -3.09723 | -44.12328 | 2024-11-01 00:13:00 | TERRA_M-M | ROSÁRIO | MARANHÃO | Brasil | 2109601 | 21 | 33 | nan | nan | nan | Amazônia | 20.4 |
| 02db5cec-079d-32fe-98d2-87b4dd4bb48a | -3.09293 | -45.74543 | 2024-11-01 00:13:00 | TERRA_M-M | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 14.9 |
| 367f4940-138f-3077-bd1f-e03638bebc1b | -3.09602 | -45.56048 | 2024-11-01 00:13:00 | TERRA_M-M | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 547.5 |
| 584a2d7f-64bd-3d42-a4d7-826de87c0b2d | -2.36786 | -48.68327 | 2024-11-01 00:13:00 | TERRA_M-M | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 44.8 |
| 44d5d381-23c6-3676-a85d-df3a0c4fa57c | -3.04866 | -45.11092 | 2024-11-01 00:13:00 | TERRA_M-M | MATINHA | MARANHÃO | Brasil | 2106508 | 21 | 33 | nan | nan | nan | Amazônia | 14.6 |
| 29099fb9-4026-3150-876e-18441e7df629 | -3.04589 | -45.09059 | 2024-11-01 00:13:00 | TERRA_M-M | MATINHA | MARANHÃO | Brasil | 2106508 | 21 | 33 | nan | nan | nan | Amazônia | 18.2 |
| 91b57021-53ba-3898-8b08-1d67ac2165c0 | -2.63583 | -45.95628 | 2024-11-01 00:13:00 | TERRA_M-M | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 14.7 |
| 955e7855-4c0c-3b60-ba6e-57d53e04059d | -2.6237 | -45.15791 | 2024-11-01 00:13:00 | TERRA_M-M | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 32.0 |
| f3037254-07dc-32da-81da-17cffcffb1cd | -2.62197 | -45.15166 | 2024-11-01 00:13:00 | TERRA_M-M | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 59.0 |
| fb2fb26a-c552-3278-a8c7-6b6eb7665ded | -2.62089 | -45.13774 | 2024-11-01 00:13:00 | TERRA_M-M | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 41.8 |
| a52b2520-8691-30a7-816c-a7f10c517e87 | -2.61931 | -45.13147 | 2024-11-01 00:13:00 | TERRA_M-M | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 19.1 |
| 53517707-521e-39ef-9aaf-ade58526df6a | -2.61512 | -45.58881 | 2024-11-01 00:13:00 | TERRA_M-M | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 14.8 |
| bf73d48d-e58b-3b48-8e33-6c28f8339ad4 | -2.46889 | -48.50812 | 2024-11-01 00:13:00 | TERRA_M-M | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 36.2 |
| 7b887028-ea10-3f87-a7dc-5d244b85ffc3 | -2.45626 | -48.50497 | 2024-11-01 00:13:00 | TERRA_M-M | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 50.8 |
| 96daab54-05ad-3d42-99bb-ef69f1fea618 | -6.10656 | -39.15352 | 2024-11-01 00:13:00 | TERRA_M-M | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 5.8 |
| 5591f031-a99d-3532-87f1-c90f47111161 | -7.03503 | -39.67578 | 2024-11-01 00:13:00 | TERRA_M-M | NOVA OLINDA | CEARÁ | Brasil | 2309201 | 23 | 33 | nan | nan | nan | Caatinga | 24.0 |
| 7f331b25-aa16-3191-83bc-9a4b495de260 | -7.03371 | -39.66612 | 2024-11-01 00:13:00 | TERRA_M-M | NOVA OLINDA | CEARÁ | Brasil | 2309201 | 23 | 33 | nan | nan | nan | Caatinga | 35.6 |
| e26f85a8-207f-361f-aebd-c2af8df7f99c | -7.02574 | -39.67701 | 2024-11-01 00:13:00 | TERRA_M-M | NOVA OLINDA | CEARÁ | Brasil | 2309201 | 23 | 33 | nan | nan | nan | Caatinga | 7.4 |
| 08830aad-c17b-3f6f-9009-98e56e5e3e78 | -7.02441 | -39.66727 | 2024-11-01 00:13:00 | TERRA_M-M | NOVA OLINDA | CEARÁ | Brasil | 2309201 | 23 | 33 | nan | nan | nan | Caatinga | 15.3 |
| 886dc7a0-a20e-338e-a394-c0b75310d5e5 | -7.00222 | -38.77027 | 2024-11-01 00:13:00 | TERRA_M-M | BARRO | CEARÁ | Brasil | 2302008 | 23 | 33 | nan | nan | nan | Caatinga | 6.0 |
| 7c2d0a13-b24a-338e-b58f-f3faafd740c7 | -6.92859 | -39.24001 | 2024-11-01 00:13:00 | TERRA_M-M | GRANJEIRO | CEARÁ | Brasil | 2304806 | 23 | 33 | nan | nan | nan | Caatinga | 6.0 |
| 1f48a8ac-3181-3075-a676-e6fe494aabc0 | -6.92731 | -39.23065 | 2024-11-01 00:13:00 | TERRA_M-M | CARIRIAÇU | CEARÁ | Brasil | 2303204 | 23 | 33 | nan | nan | nan | Caatinga | 8.6 |
| 1f4bac40-14fb-3e81-803b-6bbcf0253929 | -6.9118 | -40.47836 | 2024-11-01 00:13:00 | TERRA_M-M | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 6.7 |
| 60f15126-08b6-36e5-95ce-c8edd98ecea6 | -6.91036 | -40.46762 | 2024-11-01 00:13:00 | TERRA_M-M | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 11.9 |
| d74aa6b7-79c7-3d4d-ace3-d50bcee174a6 | -6.79753 | -40.16764 | 2024-11-01 00:13:00 | TERRA_M-M | CAMPOS SALES | CEARÁ | Brasil | 2302701 | 23 | 33 | nan | nan | nan | Caatinga | 7.7 |
| dc81e04c-daed-36b7-8239-4c6678cfc30e | -6.793 | -38.38308 | 2024-11-01 00:13:00 | TERRA_M-M | SÃO JOÃO DO RIO DO PEIXE | PARAÍBA | Brasil | 2500700 | 25 | 33 | nan | nan | nan | Caatinga | 5.3 |
| 96f8a971-943c-3f5e-b515-2972fcc84a39 | -6.76933 | -37.54821 | 2024-11-01 00:13:00 | TERRA_M-M | SÃO JOSÉ DE ESPINHARAS | PARAÍBA | Brasil | 2514404 | 25 | 33 | nan | nan | nan | Caatinga | 3.3 |
| b3189049-a988-32d8-b919-0a0723f31a74 | -6.70523 | -37.49148 | 2024-11-01 00:13:00 | TERRA_M-M | PAULISTA | PARAÍBA | Brasil | 2510907 | 25 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 37894788-6c09-3ffc-9759-a7851f1f0c67 | -6.54505 | -39.66516 | 2024-11-01 00:13:00 | TERRA_M-M | JUCÁS | CEARÁ | Brasil | 2307403 | 23 | 33 | nan | nan | nan | Caatinga | 35.5 |
| 37b53ad4-bb29-3fe1-a445-388566fe58fe | -6.51225 | -39.35768 | 2024-11-01 00:13:00 | TERRA_M-M | CARIÚS | CEARÁ | Brasil | 2303303 | 23 | 33 | nan | nan | nan | Caatinga | 5.4 |
| d9f54089-6cc9-30fd-8a5c-200b340e84c1 | -6.50273 | -42.85213 | 2024-11-01 00:13:00 | TERRA_M-M | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 25.5 |
| 8b94b9f9-aa60-3b72-b8b1-ab457de56fff | -6.47786 | -37.71347 | 2024-11-01 00:13:00 | TERRA_M-M | RIACHO DOS CAVALOS | PARAÍBA | Brasil | 2512804 | 25 | 33 | nan | nan | nan | Caatinga | 9.5 |
| ca5fc245-e898-3608-aca3-f2a42436a2b4 | -6.25567 | -43.57468 | 2024-11-01 00:13:00 | TERRA_M-M | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 21.7 |
| 5fdcb683-f84a-3fd1-b30e-98d18e177135 | -6.25328 | -43.55677 | 2024-11-01 00:13:00 | TERRA_M-M | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 816845ea-9064-39f4-ae21-4c2cc6ad566f | -6.12297 | -43.95395 | 2024-11-01 00:13:00 | TERRA_M-M | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 66.9 |
| e69ffca0-67fe-3cbf-b923-9e3ccc888c46 | -6.11292 | -43.97401 | 2024-11-01 00:13:00 | TERRA_M-M | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 153.9 |
| b08b3b6a-e975-30e2-8b90-397d4e13e067 | -6.11045 | -43.95529 | 2024-11-01 00:13:00 | TERRA_M-M | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 242.3 |
| 1d52cf2e-4ab1-37d5-9a9e-553a3a360e4d | -5.9457 | -43.77894 | 2024-11-01 00:13:00 | TERRA_M-M | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 1c323628-804e-3879-9d63-e8c68872f5b1 | -5.93989 | -43.35847 | 2024-11-01 00:13:00 | TERRA_M-M | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Caatinga | 15.4 |
| e7afaa24-4efc-32dc-add2-3af5a85c3b39 | -5.9377 | -43.34198 | 2024-11-01 00:13:00 | TERRA_M-M | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Caatinga | 24.0 |
| b235d0da-5be3-36d6-a574-d5d12c63d96e | -5.67084 | -39.86659 | 2024-11-01 00:13:00 | TERRA_M-M | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 7.0 |
| 1dfc4b50-669e-30e3-a29b-0a40120fd9f7 | -5.6276 | -43.95544 | 2024-11-01 00:13:00 | TERRA_M-M | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 23.1 |
| ea8a2107-92f2-3dff-9d26-c2127ed2b978 | -5.4685 | -43.17239 | 2024-11-01 00:13:00 | TERRA_M-M | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 15.7 |
| 2847e5cc-1def-3f59-99ba-188545c0f92b | -4.94223 | -42.57509 | 2024-11-01 00:13:00 | TERRA_M-M | ALTOS | PIAUÍ | Brasil | 2200400 | 22 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 538a93e2-f040-34e0-97af-7e30d612ef40 | -4.87853 | -42.61828 | 2024-11-01 00:13:00 | TERRA_M-M | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Cerrado | 7.1 |
| bd11d9d8-a676-372e-b4a1-4f181ae26aae | -4.74564 | -43.2548 | 2024-11-01 00:13:00 | TERRA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 085a2327-4d11-3ca7-a651-d786493be212 | -4.72174 | -42.65152 | 2024-11-01 00:13:00 | TERRA_M-M | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 13.7 |
| 126f0483-b423-381c-9849-7cbea8599398 | -4.55332 | -43.10587 | 2024-11-01 00:13:00 | TERRA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 25.6 |
| df62b3ad-e776-3f4b-837e-51cb0ffd9429 | -4.55192 | -43.09973 | 2024-11-01 00:13:00 | TERRA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 25.8 |
| 81798083-ff6b-30f1-947a-9e8284db9cd3 | -4.53748 | -40.46649 | 2024-11-01 00:13:00 | TERRA_M-M | NOVA RUSSAS | CEARÁ | Brasil | 2309300 | 23 | 33 | nan | nan | nan | Caatinga | 5.6 |
| 1ce888ea-683b-3db1-95c1-2957a4f6e6df | -4.45261 | -43.65473 | 2024-11-01 00:13:00 | TERRA_M-M | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 8311b634-e720-356d-98c0-9efd2b0e71ce | -4.44623 | -43.66233 | 2024-11-01 00:13:00 | TERRA_M-M | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 0d3b86f8-1e51-3ac5-8511-87d604b23f54 | -4.43664 | -43.68045 | 2024-11-01 00:13:00 | TERRA_M-M | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 11.3 |
| a4abecb6-3233-3d8f-9f12-60c8c15f96e4 | -4.39826 | -43.48633 | 2024-11-01 00:13:00 | TERRA_M-M | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 80.5 |
| 79f3cb48-352f-3c36-a485-bc97dd1b4c15 | -4.3961 | -43.47036 | 2024-11-01 00:13:00 | TERRA_M-M | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 664.2 |
| 92e17539-a443-3bac-b88e-8ebc6538f73e | -4.38658 | -43.48774 | 2024-11-01 00:13:00 | TERRA_M-M | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 10.3 |
| f85f1c71-81ce-378b-a7f2-f2615338a17f | -4.38443 | -43.47183 | 2024-11-01 00:13:00 | TERRA_M-M | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 91.3 |
| 25be0aa6-4408-39ce-b0b7-7953848439b5 | -4.27514 | -43.42782 | 2024-11-01 00:13:00 | TERRA_M-M | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 6f6bba8d-3646-32da-83c7-c5a7b10b61af | -4.26565 | -43.44518 | 2024-11-01 00:13:00 | TERRA_M-M | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 039c61f4-3600-383e-8714-7a0800ee6cfc | -4.26354 | -43.42933 | 2024-11-01 00:13:00 | TERRA_M-M | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 16.4 |
| f6796cf4-c1d2-3e3f-9bbf-1b05c0d38201 | -4.19054 | -38.15592 | 2024-11-01 00:13:00 | TERRA_M-M | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 5.6 |
| 0043f42d-ee4b-357b-a1d9-3590538d125b | -4.10638 | -38.74607 | 2024-11-01 00:13:00 | TERRA_M-M | GUAIÚBA | CEARÁ | Brasil | 2304954 | 23 | 33 | nan | nan | nan | Caatinga | 15.1 |
| 00691fde-e9e9-31ea-ba8e-18a9c2b6043b | -4.10515 | -38.73723 | 2024-11-01 00:13:00 | TERRA_M-M | GUAIÚBA | CEARÁ | Brasil | 2304954 | 23 | 33 | nan | nan | nan | Caatinga | 7.7 |
| dff39f58-00cb-3a4b-b136-7b0102f1ceae | -4.08323 | -43.95828 | 2024-11-01 00:13:00 | TERRA_M-M | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 15.9 |
| 51fd0e8e-53ce-3544-8c25-cdb67ac13a50 | -3.94738 | -42.62961 | 2024-11-01 00:13:00 | TERRA_M-M | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 8.4 |
| a6bae510-cb79-3e77-9fa6-6aa87dc0f9dc | -3.94627 | -41.52155 | 2024-11-01 00:13:00 | TERRA_M-M | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 9.7 |
| 190c1337-0384-32a7-aab0-d8f0b0617ade | -3.94471 | -41.51016 | 2024-11-01 00:13:00 | TERRA_M-M | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 23.1 |
| 82ed7284-b952-3f91-a3ba-7119bf251393 | -3.94159 | -41.48747 | 2024-11-01 00:13:00 | TERRA_M-M | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 6.2 |
| cbd9cf0e-99cf-3f3a-ba3b-bd7b08a16c1b | -3.94129 | -42.63795 | 2024-11-01 00:13:00 | TERRA_M-M | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 9.7 |
| f2691734-7def-3fcc-9081-994b0a2bd7af | -3.87619 | -43.96339 | 2024-11-01 00:13:00 | TERRA_M-M | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 19.9 |
| 7df99b22-5fb7-3580-89fd-0bc23747407d | -3.87394 | -43.94648 | 2024-11-01 00:13:00 | TERRA_M-M | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 18.8 |
| f3c327b6-0d04-3769-aa52-3caeba9c40e0 | -3.85425 | -40.71307 | 2024-11-01 00:13:00 | TERRA_M-M | MUCAMBO | CEARÁ | Brasil | 2309003 | 23 | 33 | nan | nan | nan | Caatinga | 6.1 |
| 4826231e-241f-33a3-916d-f360a544f8df | -3.77421 | -43.53229 | 2024-11-01 00:13:00 | TERRA_M-M | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 82adf2ae-bc35-34a5-a766-de57023c7a47 | -3.76474 | -43.54939 | 2024-11-01 00:13:00 | TERRA_M-M | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 57.6 |
| 1649e12c-7cd4-3939-9656-7ac41fa67c1d | -3.76262 | -43.53384 | 2024-11-01 00:13:00 | TERRA_M-M | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 104.9 |
| 5e691592-c009-33ac-9510-d80894045518 | -3.57182 | -43.2295 | 2024-11-01 00:13:00 | TERRA_M-M | MATA ROMA | MARANHÃO | Brasil | 2106409 | 21 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 871bdda1-39a1-3631-88bd-4e6b36102eb4 | -3.55749 | -42.70704 | 2024-11-01 00:13:00 | TERRA_M-M | MILAGRES DO MARANHÃO | MARANHÃO | Brasil | 2106672 | 21 | 33 | nan | nan | nan | Cerrado | 9.0 |


[Clique aqui para ver as próximas entradas](README3.md)
