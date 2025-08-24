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

## Dados Diários - Página 60

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d98c857f-d27e-3756-8332-d321df044e2b | -5.74475 | -57.58669 | 2025-08-24 04:59:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| e978556c-35f3-36b4-9c7f-fc50abad5bf6 | -7.25774 | -43.66679 | 2025-08-24 04:59:00 | NPP-375D | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 75b00257-35b6-3f7b-b449-e2b9222123ea | -6.43587 | -53.38556 | 2025-08-24 04:59:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0dba2079-d525-3f53-a143-ae6d2836b953 | -4.95694 | -55.81549 | 2025-08-24 04:59:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 94eb0285-9d73-395f-a988-1f93010cd9d0 | -5.74848 | -57.58727 | 2025-08-24 04:59:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| ef0dffe5-0b0b-33e3-bc4d-3adf95419309 | -6.10022 | -44.69534 | 2025-08-24 04:59:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| cdf1eefc-2778-311d-9070-fad98d1582af | -5.87496 | -57.75981 | 2025-08-24 04:59:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ce7b5ff2-4a33-3643-b243-9ac6b3ebbf71 | -5.6538 | -51.83657 | 2025-08-24 04:59:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 77a6b1dd-1e67-354c-b8cd-fc635cb80e61 | -6.18803 | -45.43094 | 2025-08-24 04:59:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 11.4 |
| d7359dc5-bb3c-31e8-a9f3-8761dd10422b | -6.45758 | -53.39971 | 2025-08-24 04:59:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3df76fc5-e415-3fbd-a936-a3b340fa663a | -6.89503 | -45.68397 | 2025-08-24 04:59:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4bc28c92-8a9b-3a93-b023-f4a44a003a3b | -7.60593 | -45.24362 | 2025-08-24 04:59:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1e9710c9-096e-3dba-bcd2-bd21636da621 | -7.02123 | -44.644 | 2025-08-24 04:59:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 7469d4f5-975d-31a9-aa65-00560aa2a168 | -5.87487 | -57.75739 | 2025-08-24 04:59:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 47f00943-4168-3676-97c8-558327990985 | -6.08892 | -44.69703 | 2025-08-24 04:59:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 33a55759-796f-3d87-b58b-36fe0f76e636 | -7.01618 | -44.64024 | 2025-08-24 04:59:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 35d85d95-57e3-37bd-b5b9-2a1e570104ea | -6.46146 | -53.39672 | 2025-08-24 04:59:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6055e9a2-5116-3b9e-a1bd-231c05690d04 | -7.0222 | -44.63683 | 2025-08-24 04:59:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| efaf7758-0aa5-37dc-91a8-97eb427624e9 | -5.75002 | -57.6012 | 2025-08-24 04:59:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d19890d0-bac9-322a-bb3d-3fb30941e5b5 | -6.72103 | -43.19977 | 2025-08-24 04:59:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 1.5 |
| b942651c-68a4-344a-8d40-3b54b8bdbc30 | -5.75075 | -57.59674 | 2025-08-24 04:59:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 59730047-affa-3e92-8f80-f49d9f6dddac | -4.96609 | -55.82472 | 2025-08-24 04:59:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 21.4 |
| 1eee470c-dfea-3a69-81ff-edce3c25b802 | -5.66297 | -45.14751 | 2025-08-24 04:59:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 55974f57-83fa-35c0-9da6-04c6bba93839 | -6.88603 | -45.67339 | 2025-08-24 04:59:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| bc7754aa-aa6d-3e52-addb-9450645fb74a | -5.74548 | -57.58224 | 2025-08-24 04:59:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| e85971a6-f889-3d18-8207-f6b5074673f5 | -6.58956 | -44.56424 | 2025-08-24 04:59:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bd1f94ec-d48c-3b42-8c49-d8f43afb9f05 | -6.46425 | -53.40075 | 2025-08-24 04:59:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cead2c8a-7f2a-3853-85c5-3effef027140 | -6.6085 | -48.05136 | 2025-08-24 04:59:00 | NPP-375D | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Amazônia | 1.8 |
| dbfaa474-2a2b-377b-99ee-488dc240fa77 | -6.91919 | -43.77913 | 2025-08-24 04:59:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1db920b0-f628-350a-b013-70f15431e2e9 | -7.62235 | -45.24302 | 2025-08-24 04:59:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ab5391af-f980-3432-9d8e-6537e6babcc9 | -6.43254 | -53.38503 | 2025-08-24 04:59:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a24a5ba4-9c99-3356-a5dd-abfae767e8e4 | -6.0894 | -44.69361 | 2025-08-24 04:59:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| aead75f0-c1f5-3853-a6c2-8d69c3539e0b | -5.88325 | -57.75639 | 2025-08-24 04:59:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fb3db2ed-8bd8-3179-930e-819fe5193790 | -7.02172 | -44.64043 | 2025-08-24 04:59:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| fcf0938d-2190-3caa-8b42-c8b2e47ec648 | -5.75447 | -57.59736 | 2025-08-24 04:59:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ec19d7bc-8d6f-3805-8019-ce28a3cb27ad | -4.04689 | -56.31762 | 2025-08-24 04:59:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4f6f607a-59fd-357b-8455-925002067b69 | -4.94192 | -55.82078 | 2025-08-24 04:59:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 36c8b150-c050-36cb-94aa-22cd1624f500 | -6.4648 | -53.39725 | 2025-08-24 04:59:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 57ffda4a-9838-330e-a7e1-48a225a135f3 | -6.0953 | -44.69102 | 2025-08-24 04:59:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c8458c9b-5dae-30ca-940a-ed9394e9a2ba | -6.16016 | -53.82708 | 2025-08-24 04:59:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2178c6a5-5ed1-3ae0-83b5-c57e68849155 | -6.59007 | -44.5607 | 2025-08-24 04:59:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a60383e0-18a2-3fd2-9dd1-110d7d1fee09 | -5.42275 | -60.17564 | 2025-08-24 04:59:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 1820f47f-a6a0-30e7-94d4-f35aadc03641 | -4.96325 | -55.82035 | 2025-08-24 04:59:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| fb82dd6c-7a52-377d-98f0-4c2c1f7ab1e5 | -5.42788 | -60.17212 | 2025-08-24 04:59:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 9.3 |
| bbf3adf3-d1ba-370b-9cb5-c735dd85761b | -7.01668 | -44.63671 | 2025-08-24 04:59:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 1c03123f-11a1-37cb-9826-054c67ecedf9 | -6.26578 | -53.64783 | 2025-08-24 04:59:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d9719bab-1bb0-37af-8d80-bf8d9c6dd791 | -5.74175 | -57.58167 | 2025-08-24 04:59:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 97074b97-5dae-3d3b-8850-65d147a6d409 | -7.6062 | -46.27277 | 2025-08-24 04:59:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0a24c809-9466-3588-a14e-d3e2931655ef | -5.87948 | -57.75587 | 2025-08-24 04:59:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cd82d10e-7e08-3c35-95a9-28abef50bf41 | -5.74775 | -57.59168 | 2025-08-24 04:59:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5efc2b47-8a3b-36c0-9876-7036bd8eff5c | -6.89248 | -45.66462 | 2025-08-24 04:59:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 03ffa4aa-7f1a-3bc5-a730-3693802672d4 | -7.61125 | -45.24455 | 2025-08-24 04:59:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| eb00e71b-67b6-3e35-9015-0fc85c533b12 | -4.94251 | -55.81706 | 2025-08-24 04:59:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a1f3b3c1-5f71-37fc-b7bc-f8f86f66e881 | -6.61342 | -48.04807 | 2025-08-24 04:59:00 | NPP-375D | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d7533be7-1aac-3e95-b939-719757e968e9 | -6.59056 | -44.55724 | 2025-08-24 04:59:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 644d9213-85d1-3cd1-b065-b1c84c50181a | -5.64919 | -51.84357 | 2025-08-24 04:59:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 35dc7fbd-350a-3d2f-bbb1-a517d5addc1e | -6.11315 | -44.36306 | 2025-08-24 04:59:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 6291dae1-9a85-3bdb-9e68-c7b8991995c6 | -6.46036 | -53.40373 | 2025-08-24 04:59:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b0322f97-3e76-31f1-a13f-00c9a5b46322 | -5.45149 | -60.19379 | 2025-08-24 04:59:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 505020ff-aa06-33d8-aabb-7c3f2b19218c | -7.02981 | -44.6636 | 2025-08-24 04:59:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 3db29a8f-912e-3af8-889c-6aaedaa56d9b | -5.42716 | -60.17639 | 2025-08-24 04:59:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 9.3 |
| dc60f59f-1f14-352c-9c48-2c14d47bb7bd | -5.88239 | -57.75853 | 2025-08-24 04:59:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cd17041e-0f79-3bb2-9bff-764528f9868e | -6.4292 | -53.38451 | 2025-08-24 04:59:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| f1ec8662-77ba-3779-80b5-2890f173f319 | -7.16961 | -44.66321 | 2025-08-24 04:59:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 779580ff-1a30-31c2-9c3d-fb2be182be43 | -6.60971 | -48.04315 | 2025-08-24 04:59:00 | NPP-375D | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 28604e2c-4f6a-3af5-8d23-13322acd8c2d | -6.09481 | -44.69452 | 2025-08-24 04:59:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 04d3c2f8-11db-3257-80ad-6715cd6aee11 | -6.08989 | -44.69015 | 2025-08-24 04:59:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 46df1d0c-fc5d-3f5c-81e8-343403db34e0 | -5.41834 | -60.1749 | 2025-08-24 04:59:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5b2e3a35-a750-33ae-8fee-5d87a6da3468 | -7.19034 | -45.16741 | 2025-08-24 04:59:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| ca809cef-2491-3910-8a80-7b38f554a6bd | -7.6286 | -45.23724 | 2025-08-24 04:59:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 20faa77e-91cb-3926-92fc-4d528f1bc3ba | -6.88053 | -45.67532 | 2025-08-24 04:59:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a36fa162-363c-3141-a983-d64a88259f82 | -6.90071 | -45.68077 | 2025-08-24 04:59:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b3e32cba-8326-3529-9276-6d994748ce05 | -5.66386 | -45.14118 | 2025-08-24 04:59:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6acd6a15-ced9-3439-9932-165f9eabcf42 | -5.87414 | -57.76192 | 2025-08-24 04:59:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 282188cf-46c2-321d-866b-0d28210828fa | -6.89339 | -45.6958 | 2025-08-24 04:59:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 173356a7-9b85-395f-a2cd-b95c5c3cd706 | -7.63148 | -46.27736 | 2025-08-24 04:59:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9d6ab12f-7244-3ff8-94c3-c2c943ed8637 | -5.86003 | -52.08509 | 2025-08-24 04:59:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 13.6 |
| 151736e6-c8a7-3545-a664-9385c0a232dd | -5.7463 | -57.60057 | 2025-08-24 04:59:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| fedf91c5-8cc8-38ab-9793-0206b1ecdb75 | -7.70199 | -42.13086 | 2025-08-24 04:59:00 | NPP-375D | SIMPLÍCIO MENDES | PIAUÍ | Brasil | 2210805 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| ed9e2759-b529-3c7f-bf67-386bc4d2cbbe | -5.4286 | -60.16783 | 2025-08-24 04:59:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 48a201aa-482f-38da-8d58-006f4dcf028c | -5.44707 | -60.19304 | 2025-08-24 04:59:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 0897d4e6-71ba-30cd-a921-501337be93fe | -5.10557 | -56.97532 | 2025-08-24 04:59:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3beb64f8-4478-3428-afa2-c92e6d665804 | -7.25433 | -43.66685 | 2025-08-24 04:59:00 | NPP-375D | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| aab4c009-4470-366f-a8c9-fc83f99b1b77 | -6.88993 | -45.68304 | 2025-08-24 04:59:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| a405306f-f3a9-3a64-93ac-4b82eb65bf51 | -4.94131 | -55.82453 | 2025-08-24 04:59:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 86cec5df-4fb2-3944-821f-5e9bc3f0e7df | -5.74257 | -57.59998 | 2025-08-24 04:59:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 31c94a05-341a-326a-86ff-fe63fdbb353e | -5.66378 | -45.13946 | 2025-08-24 04:59:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 28382a71-b2d0-3260-a00b-66ec999f7ca5 | -7.70269 | -42.12547 | 2025-08-24 04:59:00 | NPP-375D | SIMPLÍCIO MENDES | PIAUÍ | Brasil | 2210805 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| aa89deec-8f46-3c0b-8b39-9aed6dfde750 | -6.95557 | -44.42443 | 2025-08-24 04:59:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 868489fc-075a-3673-aec6-7da1a4350ad5 | -4.93785 | -55.82398 | 2025-08-24 04:59:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8aa6effc-bb1f-3bd0-bf5b-34ae27a6d883 | -6.11263 | -44.36679 | 2025-08-24 04:59:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fc08ec21-c995-3c35-ae9d-cdb993447db9 | -5.7522 | -57.58786 | 2025-08-24 04:59:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| e6b99d4d-c457-3cd5-b635-e7db01c672df | -6.20289 | -42.98374 | 2025-08-24 04:59:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 36ab1bf6-ca60-39d2-9b98-e4e612710c8e | -6.60478 | -48.04653 | 2025-08-24 04:59:00 | NPP-375D | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9af2c05f-1ec3-3496-9566-c181a1d0c55a | -6.6091 | -48.0473 | 2025-08-24 04:59:00 | NPP-375D | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a3368c07-ecec-3edc-a86d-a0dbd57fb06b | -4.9604 | -55.81603 | 2025-08-24 04:59:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 051c7ed8-09ec-3b2d-a136-e62b41496066 | -6.43544 | -44.54648 | 2025-08-24 04:59:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4dec0b9e-49fb-3ce4-8850-0eb1762fd75d | -5.65717 | -45.14809 | 2025-08-24 04:59:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| bfb60ea7-c29f-3b8d-8a19-7c01dfe210bc | -4.95634 | -55.81927 | 2025-08-24 04:59:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 056ffbed-7904-368f-8f94-96dcde34b8c3 | -5.95341 | -52.20488 | 2025-08-24 04:59:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |


[Clique aqui para ver as próximas entradas](README61.md)
