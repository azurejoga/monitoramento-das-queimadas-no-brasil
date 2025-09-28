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

## Dados Diários - Página 37

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 43e665fb-0493-3b79-a3c7-d3e2c415be14 | -3.67109 | -38.79686 | 2025-09-28 04:04:00 | NPP-375D | CAUCAIA | CEARÁ | Brasil | 2303709 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| a8de9ab6-b991-3a15-b4e4-8dbf5d00836c | -4.79508 | -50.80508 | 2025-09-28 04:04:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9beae540-4933-3bed-9f11-c63ccce86e02 | -8.85608 | -46.59816 | 2025-09-28 04:04:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 10a4fd18-7cdf-39f2-b9ef-f02defc085ef | -8.81968 | -46.01096 | 2025-09-28 04:04:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f70297b6-360f-3b30-ab16-d95c3c259a01 | -4.94907 | -45.60471 | 2025-09-28 04:04:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a616f11d-62e2-32f3-825f-131e3d8115e2 | -5.75975 | -42.88572 | 2025-09-28 04:04:00 | NPP-375D | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 6.9 |
| 8c4cdb23-4418-33a1-add1-d4c920b0416b | -5.94092 | -40.25172 | 2025-09-28 04:04:00 | NPP-375D | TAUÁ | CEARÁ | Brasil | 2313302 | 23 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 8954d7e7-1712-36bd-a8c6-052c48a12c62 | -5.70766 | -42.65525 | 2025-09-28 04:04:00 | NPP-375D | MIGUEL LEÃO | PIAUÍ | Brasil | 2206308 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 947c1f7f-4b6f-3610-a839-a953633e4173 | -5.90049 | -43.2962 | 2025-09-28 04:04:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 72f5e8b8-364a-3ea5-a7b0-dea56e62c9b4 | -6.21781 | -42.84634 | 2025-09-28 04:04:00 | NPP-375D | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 4.6 |
| 3c377221-962f-3625-9a75-11f1be1dca8d | -6.14083 | -45.72242 | 2025-09-28 04:04:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 97ea0c77-e36f-35b6-9ab0-d9d818057798 | -7.75366 | -45.74501 | 2025-09-28 04:04:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 248b0d2f-b309-3163-bdf3-02409209cf9a | -6.04107 | -43.58323 | 2025-09-28 04:04:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 7452c23f-99bc-3919-a9b4-6c8468fe7ac8 | -4.15442 | -40.00124 | 2025-09-28 04:04:00 | NPP-375D | SANTA QUITÉRIA | CEARÁ | Brasil | 2312205 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 959eb2cd-cd78-354e-9701-446fd71dcb32 | -4.62026 | -43.10493 | 2025-09-28 04:04:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f3a9fedf-3af2-3174-9ba1-d93d39d816f2 | -5.04776 | -45.31711 | 2025-09-28 04:04:00 | NPP-375D | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| bd8c589b-a7df-339d-aa26-40df9781fbdb | -9.28493 | -45.70901 | 2025-09-28 04:04:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 281a3188-0179-301c-9433-41b52d91cee5 | -6.12699 | -41.80288 | 2025-09-28 04:04:00 | NPP-375D | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| ec32837b-84ac-3bf5-9e05-d9d261a15eea | -5.91421 | -43.6755 | 2025-09-28 04:04:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d606a5ab-a686-3df3-ae1b-908314ce7b69 | -5.18239 | -43.75252 | 2025-09-28 04:04:00 | NPP-375D | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 45f2085b-b795-3506-acc7-e952b637accd | -7.42901 | -40.07796 | 2025-09-28 04:04:00 | NPP-375D | BODOCÓ | PERNAMBUCO | Brasil | 2602001 | 26 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 152a840a-1621-3c8a-a024-e6b6ad18f2b9 | -6.91872 | -39.58712 | 2025-09-28 04:04:00 | NPP-375D | FARIAS BRITO | CEARÁ | Brasil | 2304301 | 23 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 8a84dade-aef0-365a-8942-4d293a855697 | -5.75535 | -41.74424 | 2025-09-28 04:04:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 69616017-13a0-3df2-87ed-effa3b13a332 | -6.25031 | -42.47307 | 2025-09-28 04:04:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 184ee787-d70b-341d-b0a3-024c7148d125 | -9.7761 | -47.76565 | 2025-09-28 04:04:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1494c100-3c14-32e4-9ec6-181e9338d392 | -5.76404 | -42.88219 | 2025-09-28 04:04:00 | NPP-375D | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 6.1 |
| 48606d74-1428-309c-a74c-4e8570fbc23b | -7.65795 | -43.90365 | 2025-09-28 04:04:00 | NPP-375D | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2daf65bc-53f1-3067-8409-7cb34fcab634 | -7.75452 | -47.01735 | 2025-09-28 04:04:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| ab0712e7-b985-3743-afb8-c09f16456e7b | -6.69833 | -44.57591 | 2025-09-28 04:04:00 | NPP-375D | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 75911f59-8c62-3c1a-b072-063b9a98db74 | -5.9707 | -46.45201 | 2025-09-28 04:04:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 21354382-ec9e-357c-aba8-fd435e3550b0 | -5.90741 | -42.93795 | 2025-09-28 04:04:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 5e6e42ad-f217-355c-b2be-ac7d8e1b657d | -9.21589 | -46.78196 | 2025-09-28 04:04:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 7110860e-2252-3a18-87b1-b92ea8ad2d8b | -6.42742 | -43.51711 | 2025-09-28 04:04:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 9.9 |
| f533fd07-5433-3665-a60e-0dde8850b9ed | -7.49079 | -37.13018 | 2025-09-28 04:04:00 | NPP-375D | SÃO JOSÉ DO EGITO | PERNAMBUCO | Brasil | 2613602 | 26 | 33 | nan | nan | nan | Caatinga | 2.2 |
| c59f800d-44d5-3615-978c-2dbc6eca7780 | -9.44984 | -43.70751 | 2025-09-28 04:04:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 321d328f-76fb-38c9-8203-9999c52e3156 | -7.77801 | -47.0187 | 2025-09-28 04:04:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 3a87317c-226b-35cc-9f41-f2c7977f9f00 | -9.22174 | -46.77429 | 2025-09-28 04:04:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 895df24d-c977-3175-b59f-5788419817f6 | -5.1833 | -43.75519 | 2025-09-28 04:04:00 | NPP-375D | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 027d9621-02cf-3554-b873-4e866d20ff8b | -5.82088 | -42.80636 | 2025-09-28 04:04:00 | NPP-375D | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 7.3 |
| c36e1ad2-13f7-3c90-a21c-ff683ee6eb6f | -6.44064 | -45.90249 | 2025-09-28 04:04:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| d765d097-7b42-3b57-bdfc-93b7bb57c852 | -6.4984 | -43.71777 | 2025-09-28 04:04:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 11.4 |
| b4236f7c-1540-31ca-8a3f-6afc6d4d15f3 | -5.65807 | -43.30145 | 2025-09-28 04:04:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 57da4ce5-6733-3a86-b6cd-6fb7539f253f | -11.95295 | -47.97139 | 2025-09-28 04:06:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 1954f356-3093-3888-9aa5-4edce86b9a53 | -11.39185 | -46.93544 | 2025-09-28 04:06:00 | NPP-375D | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 33a0bc35-9d1b-3056-a4ae-28e624c40fb2 | -14.53251 | -48.41718 | 2025-09-28 04:06:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c393b1c8-7eb7-3573-a0e1-854f6582ffd5 | -15.20657 | -44.00595 | 2025-09-28 04:06:00 | NPP-375D | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| fea6135c-3e3a-3ad3-8cac-756765de6479 | -11.77958 | -43.76757 | 2025-09-28 04:06:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 40cde188-7e5b-30ff-bc48-56eddfe0e2ab | -11.36758 | -44.94847 | 2025-09-28 04:06:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e4f8b95a-f45c-3b90-91f3-905e448e24ff | -14.80686 | -45.60378 | 2025-09-28 04:06:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 8655764c-3795-3db2-acd9-2f96c6fa072a | -12.73737 | -46.81931 | 2025-09-28 04:06:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 26a9b49d-1164-334e-873a-88c4163683d5 | -11.99094 | -47.99249 | 2025-09-28 04:06:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f41d4939-6982-37cc-9414-34fe8cac9f02 | -14.54014 | -48.40045 | 2025-09-28 04:06:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 58f758a8-6be8-30e0-a9d6-802f7858f3ff | -13.34989 | -47.29293 | 2025-09-28 04:06:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3d257b35-1b6c-357a-b014-e4ac8ef01a96 | -10.96816 | -49.5733 | 2025-09-28 04:06:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b10e104d-1923-366f-b49d-13fc3701f86c | -11.38767 | -46.9835 | 2025-09-28 04:06:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 91628be1-627d-32ee-a843-3304cb943663 | -11.85586 | -48.24202 | 2025-09-28 04:06:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1c68414b-8939-397e-b74a-11314dc4a14f | -14.81752 | -45.45342 | 2025-09-28 04:06:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2bc77241-c378-3561-92aa-774eab2f9e7e | -11.96679 | -47.99743 | 2025-09-28 04:06:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a107ef9e-959e-3284-b7c5-72fdbf64a9c0 | -11.42557 | -45.03896 | 2025-09-28 04:06:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 15.5 |
| f713c750-a117-3640-b08f-e4688d5e501f | -11.7026 | -44.41547 | 2025-09-28 04:06:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 38252299-a338-367a-809d-4026424d341c | -15.02832 | -47.14691 | 2025-09-28 04:06:00 | NPP-375D | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b9841e08-8bcc-3c18-a65b-7f8131719f65 | -15.53315 | -42.34012 | 2025-09-28 04:06:00 | NPP-375D | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 0f52d630-9646-3441-86da-f70d40013902 | -12.78239 | -47.75278 | 2025-09-28 04:06:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7ece2b3b-abb6-3234-84d2-bdf6287fc64a | -12.95676 | -46.38247 | 2025-09-28 04:06:00 | NPP-375D | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 8bb69d9e-8963-3fa7-b2c2-6657e1ede4c0 | -13.59432 | -47.33102 | 2025-09-28 04:06:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| ba88c50e-ddb7-35e8-94d0-e3cf88f3de0a | -11.53534 | -46.93198 | 2025-09-28 04:06:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b7f483a9-3357-3a42-917a-d339ac064665 | -12.95227 | -45.14408 | 2025-09-28 04:06:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 349dc3cd-7a84-381e-89af-5e5b827e978d | -12.01905 | -47.0843 | 2025-09-28 04:06:00 | NPP-375D | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a8a22cfe-4a12-36b4-8e58-6334237a9d06 | -11.99761 | -47.90411 | 2025-09-28 04:06:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f62f7ed4-5616-331b-a000-fcf86fea6238 | -13.3965 | -48.16121 | 2025-09-28 04:06:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7eb63a97-a4b4-3331-85ff-a84de8811a8a | -12.92664 | -45.17318 | 2025-09-28 04:06:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 49d81aa5-be29-32f4-871c-36195cf6c6f2 | -12.89474 | -45.15815 | 2025-09-28 04:06:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e3d711fb-11ca-375f-8069-25320093a72b | -11.99111 | -47.88903 | 2025-09-28 04:06:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 32113971-2d8a-35d5-bbfc-07e82a1a944e | -12.26003 | -44.09437 | 2025-09-28 04:06:00 | NPP-375D | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 409d0283-b486-3071-812a-9c98b60468eb | -10.90942 | -44.82311 | 2025-09-28 04:06:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9a8c67ae-ad67-339c-88c9-b4813c093b2b | -14.77701 | -45.68787 | 2025-09-28 04:06:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 83c02a9e-175c-3352-b896-3fe404373490 | -11.9924 | -47.03834 | 2025-09-28 04:06:00 | NPP-375D | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 770ceea5-d1d8-3a96-9714-9b6f012ad3c7 | -14.7313 | -46.82959 | 2025-09-28 04:06:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 80290e21-5ca8-34f6-b144-c6408f9be904 | -10.96364 | -49.56924 | 2025-09-28 04:06:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0e94ec3b-6f32-3c92-9347-e5f8a9fc97df | -12.89691 | -45.16782 | 2025-09-28 04:06:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 13.8 |
| 3df994b9-55cf-31c5-8af7-96f84dbeb504 | -15.27951 | -49.48544 | 2025-09-28 04:06:00 | NPP-375D | SANTA ISABEL | GOIÁS | Brasil | 5219357 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1c2a8908-25d5-300e-b1ac-f621eb92e91d | -14.83255 | -45.57471 | 2025-09-28 04:06:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 24b90afe-ff9f-318f-bce5-7f29615ab261 | -12.89397 | -45.16265 | 2025-09-28 04:06:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 5cdd993b-ad7e-3a16-b4ea-e3dc30aead3f | -11.98492 | -47.89771 | 2025-09-28 04:06:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 54a3a676-ebfa-3362-a876-dd6e02adbb28 | -13.24905 | -44.11551 | 2025-09-28 04:06:00 | NPP-375D | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f9cbf5df-d6ad-358b-a7f2-e7e0944f5592 | -11.36834 | -44.9441 | 2025-09-28 04:06:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d7c2fa60-79a8-3ea0-a752-b251aa365e3e | -12.00236 | -47.98061 | 2025-09-28 04:06:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 6bd47d55-ea22-348c-8253-c8c14f060ad7 | -13.63853 | -44.4179 | 2025-09-28 04:06:00 | NPP-375D | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 7.1 |
| d113f4d7-056b-3bfd-8175-d3eac37d687c | -13.80005 | -47.91153 | 2025-09-28 04:06:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 31e34555-a3b3-32a5-a4aa-515d12c6fb89 | -15.89991 | -46.19911 | 2025-09-28 04:06:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2a78b901-70c0-3e9d-af4a-b07d7726215c | -12.91191 | -45.14734 | 2025-09-28 04:06:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 6c771fac-6eed-32ff-af90-a31490ad2ee3 | -12.01743 | -47.92239 | 2025-09-28 04:06:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| a4b81d2f-1ff6-33b2-a132-a3d0ce2ecc8a | -11.62249 | -52.84518 | 2025-09-28 04:06:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| dc630d78-2805-328f-8dfa-84f02591070d | -14.59676 | -48.23886 | 2025-09-28 04:06:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a918798c-df8b-3f24-a446-921094bceb49 | -11.79899 | -44.91145 | 2025-09-28 04:06:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 11000d37-9ead-3acd-914e-020239f8956e | -12.67963 | -46.88042 | 2025-09-28 04:06:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| c82356c8-84e4-381e-aaf9-aea1f868284b | -13.60159 | -47.29089 | 2025-09-28 04:06:00 | NPP-375D | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 698480a2-e141-3c31-821c-88a7721fc505 | -11.51487 | -46.94909 | 2025-09-28 04:06:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 32a49553-fbc8-3705-bdf1-a8c4ccff33a1 | -13.77984 | -47.87565 | 2025-09-28 04:06:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| ecd604e9-7b1d-3726-9d52-bc5844871167 | -10.92419 | -42.84604 | 2025-09-28 04:06:00 | NPP-375D | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |


[Clique aqui para ver as próximas entradas](README38.md)
