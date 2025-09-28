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

## Dados Diários - Página 16

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2a0c253d-2613-3731-a5f0-9e0ee20b16cf | -5.74489 | -42.84831 | 2025-09-28 03:36:00 | NOAA-21 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 8.0 |
| 41d5f016-df1b-3564-9dd5-acc724823a35 | -6.46427 | -44.22007 | 2025-09-28 03:36:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 70a6dcf1-8a56-3db2-8de7-a0199a83634f | -6.7112 | -42.7637 | 2025-09-28 03:36:00 | NOAA-21 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| f29528fa-d85d-3f91-9cca-84ba0d6663ae | -6.87302 | -39.26538 | 2025-09-28 03:36:00 | NOAA-21 | VÁRZEA ALEGRE | CEARÁ | Brasil | 2314003 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 2ba55b18-4d8f-32e1-9492-86a8d294f9f2 | -5.81166 | -42.8138 | 2025-09-28 03:36:00 | NOAA-21 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 9.5 |
| 8b472208-19a7-3d58-b2cd-59faff45a965 | -8.836 | -46.20453 | 2025-09-28 03:36:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 5811c0e2-1029-37b5-a4bd-810069d11a51 | -5.90424 | -42.93438 | 2025-09-28 03:36:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 9.0 |
| 1e926565-958b-3e85-bd2c-6c8a5a1052c7 | -6.05455 | -44.86592 | 2025-09-28 03:36:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ce936dbd-cc30-3ea1-9956-2642cc3f5eb7 | -8.27178 | -45.47142 | 2025-09-28 03:36:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 4420474d-7b52-32ab-bcbd-bdf20551f3be | -7.14975 | -34.81208 | 2025-09-28 03:36:00 | NOAA-21 | JOÃO PESSOA | PARAÍBA | Brasil | 2507507 | 25 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| a788bda5-c695-3f84-b2c6-9d49959ac941 | -5.88645 | -43.20075 | 2025-09-28 03:36:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Caatinga | 8.9 |
| e3fdcda5-362c-30fe-bffe-8b4e5dbdbc00 | -7.3114 | -42.94848 | 2025-09-28 03:36:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 20f19643-f922-3465-9040-30f7cbde788d | -4.86786 | -45.76044 | 2025-09-28 03:36:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 1b8db6dc-6676-3a1f-abdf-d94de0051606 | -4.87621 | -45.85769 | 2025-09-28 03:36:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 9162073b-5b12-385c-879c-2a7fd1e10aaa | -7.00349 | -45.62407 | 2025-09-28 03:36:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 589faa25-a982-3a93-bb23-69131e1b919f | -6.7825 | -44.0447 | 2025-09-28 03:36:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 44488d69-257c-3e2b-b008-55119759d427 | -4.18198 | -38.11707 | 2025-09-28 03:36:00 | NOAA-21 | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 01e8c1fd-52dc-3506-9fe8-2026d039872a | -8.04136 | -35.24157 | 2025-09-28 03:36:00 | NOAA-21 | CHÃ DE ALEGRIA | PERNAMBUCO | Brasil | 2604403 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 096dc34c-339f-3b1e-81fc-8302ee597412 | -7.03173 | -34.8909 | 2025-09-28 03:36:00 | NOAA-21 | SANTA RITA | PARAÍBA | Brasil | 2513703 | 25 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| b4a65386-7753-34a5-9cac-745dbe7c5622 | -6.40332 | -44.29343 | 2025-09-28 03:36:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 76c825f0-3979-3f71-948d-e88abfbfbd0d | -5.8075 | -42.83793 | 2025-09-28 03:36:00 | NOAA-21 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 3c43d021-b7de-37ec-944f-2ae7585afadc | -7.03991 | -44.77285 | 2025-09-28 03:36:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 7687a2a2-9eec-3ddd-b606-531843a38bd3 | -5.74247 | -42.30896 | 2025-09-28 03:36:00 | NOAA-21 | SÃO MIGUEL DA BAIXA GRANDE | PIAUÍ | Brasil | 2210383 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| d44abe37-ae8b-3f39-a77d-87b4bb80e9c8 | -8.64755 | -44.85733 | 2025-09-28 03:36:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 1b7ed586-6636-3e36-b0c2-27739381f9f5 | -7.71696 | -41.29239 | 2025-09-28 03:36:00 | NOAA-21 | PATOS DO PIAUÍ | PIAUÍ | Brasil | 2207777 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 38d1853c-a5fb-3b68-924f-848e2277b485 | -7.92621 | -42.6768 | 2025-09-28 03:36:00 | NOAA-21 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| fe330760-115d-3bd5-ad87-dd7c853253a4 | -7.87109 | -44.55241 | 2025-09-28 03:36:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| c905f86b-e1ef-3346-8e90-d6b3177b6473 | -7.75959 | -45.74323 | 2025-09-28 03:36:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 85132508-5a2e-3a6f-af69-f714bf7e078b | -8.8289 | -46.20747 | 2025-09-28 03:36:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ddc444fb-1c94-33db-a6ba-01e7b0fe2ee7 | -8.28635 | -45.46447 | 2025-09-28 03:36:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 508e09fd-2a49-335f-8e8e-ab650142d7d0 | -6.32199 | -41.88452 | 2025-09-28 03:36:00 | NOAA-21 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 3b65f3dc-0626-30fa-a97f-385ec949084a | -5.73611 | -42.6573 | 2025-09-28 03:36:00 | NOAA-21 | AGRICOLÂNDIA | PIAUÍ | Brasil | 2200103 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| b25619c2-e14a-3d92-aacc-6c81f713fa3b | -7.53983 | -46.0986 | 2025-09-28 03:36:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| eddab800-4150-335a-816d-daa84e93f206 | -5.73563 | -42.85339 | 2025-09-28 03:36:00 | NOAA-21 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 6.4 |
| 69526216-bb57-3657-b350-76fd9e4444b9 | -4.86128 | -45.75949 | 2025-09-28 03:36:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 03d768a1-604c-31ae-92f5-3a7daec790ce | -7.75867 | -45.74818 | 2025-09-28 03:36:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| d4dc8a1d-2f0b-30bf-90dd-f38481fbc816 | -7.14619 | -45.5027 | 2025-09-28 03:36:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d7a23513-0d17-30d9-a19f-648f80560e63 | -5.82802 | -44.43296 | 2025-09-28 03:36:00 | NOAA-21 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 8.9 |
| a78b0927-184c-3678-a48b-b107f9e35674 | -7.10176 | -44.23959 | 2025-09-28 03:36:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 10.0 |
| e96201cf-5ac8-3d61-873d-b84f43b1eac7 | -7.24416 | -44.76712 | 2025-09-28 03:36:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6b70751c-32d3-3d7e-954b-4e8fef8a6279 | -5.76464 | -42.79899 | 2025-09-28 03:36:00 | NOAA-21 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 1d84edb0-de26-3a00-b466-105534d998ed | -7.85418 | -43.79884 | 2025-09-28 03:36:00 | NOAA-21 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| cc5e45ab-1b98-3876-aa06-22fe6956117b | -6.69397 | -44.57533 | 2025-09-28 03:36:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 65e9d1c5-3432-3eca-9feb-9868a6d51d60 | -5.04637 | -45.31659 | 2025-09-28 03:36:00 | NOAA-21 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 72283306-3c55-3983-baa4-e25cca958f8b | -5.80508 | -42.81996 | 2025-09-28 03:36:00 | NOAA-21 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 77d30939-d40b-3a3b-be27-ed7cd63d1a90 | -8.49825 | -44.7258 | 2025-09-28 03:36:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 8.6 |
| f9abedea-ce42-3bc7-b9f3-7b6020b97367 | -8.49748 | -44.73001 | 2025-09-28 03:36:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 69c5b190-abdf-3110-a5b5-b6c27b264aa2 | -7.7967 | -47.00093 | 2025-09-28 03:36:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 10.5 |
| ccaab788-dbae-3b08-96e7-db5407aed507 | -3.80442 | -41.57161 | 2025-09-28 03:36:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 11.6 |
| 8fa82657-29f4-31f7-83d0-735c95ff0c80 | -5.6969 | -42.63159 | 2025-09-28 03:36:00 | NOAA-21 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 904e069d-ee5e-36b8-88d5-208921c43a9f | -7.80225 | -47.00828 | 2025-09-28 03:36:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 10.5 |
| e40974b9-a19a-37eb-8643-1408e6785a39 | -5.72893 | -42.66731 | 2025-09-28 03:36:00 | NOAA-21 | MIGUEL LEÃO | PIAUÍ | Brasil | 2206308 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| a3406d8e-35e5-395e-9d5d-3656136c89bf | -5.73231 | -42.85683 | 2025-09-28 03:36:00 | NOAA-21 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 6.1 |
| 1481a96a-8358-33a8-b020-95131dec1fa5 | -8.27416 | -45.46232 | 2025-09-28 03:36:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 8.6 |
| d5ac17ad-0e72-33ff-b188-9c928e327f00 | -6.9008 | -44.75971 | 2025-09-28 03:36:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 15.7 |
| efc97132-3ecc-34c2-884e-8db129a229fe | -5.91444 | -42.93957 | 2025-09-28 03:36:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 5.4 |
| c600d63b-b457-3197-98e0-9c2c92944cc0 | -5.53756 | -42.83057 | 2025-09-28 03:36:00 | NOAA-21 | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 4c021a3b-1db3-39b7-a6e2-b922caed1f82 | -6.69368 | -42.77294 | 2025-09-28 03:36:00 | NOAA-21 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 6f8c4d36-ab6d-32ed-9e25-55e8a0873996 | -6.0724 | -43.76225 | 2025-09-28 03:36:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| c7180169-ef98-3b29-be53-37ac65319f22 | -7.53778 | -46.10946 | 2025-09-28 03:36:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| a4be71fc-e6c6-346a-9b0d-325eec6b1431 | -3.79983 | -41.56785 | 2025-09-28 03:36:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 8.6 |
| b3925466-fb55-387c-9c4a-3b0ef7317906 | -5.54355 | -42.828 | 2025-09-28 03:36:00 | NOAA-21 | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 14debbbd-da91-394e-bd37-709a7e4c6597 | -11.43614 | -46.64862 | 2025-09-28 03:38:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 555e84e1-ced8-3de1-8c35-5c367365e404 | -12.89904 | -45.16518 | 2025-09-28 03:38:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c1f8a6fa-82b3-3926-993b-fc34e44f9e3d | -11.71707 | -44.42703 | 2025-09-28 03:38:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 13.3 |
| 3cc2a0fe-3655-39ea-8a0d-021c28ed70c3 | -13.64047 | -48.06596 | 2025-09-28 03:38:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 681726f7-4e1e-3fb2-8945-d83c01ad7635 | -13.62694 | -47.31602 | 2025-09-28 03:38:00 | NOAA-21 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6273a9d0-dc9b-3fb1-be83-2f64ae0029b0 | -11.58117 | -45.4938 | 2025-09-28 03:38:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 6dc865b1-930e-301f-8d50-19e39241fd10 | -11.37068 | -45.02343 | 2025-09-28 03:38:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 943dea1b-a694-3023-8ba0-98557e6d150e | -15.88452 | -46.20068 | 2025-09-28 03:38:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4ea65e6c-ff47-39f0-ad47-e89c2b454c9e | -11.44508 | -44.98814 | 2025-09-28 03:38:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| e8f8484d-36cb-32a4-bde8-15ddcda6420f | -12.69075 | -45.47501 | 2025-09-28 03:38:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 64fe6a75-2eed-3e20-8c46-b1a29993431e | -11.98039 | -47.88498 | 2025-09-28 03:38:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 19060e93-b196-31a4-b422-525edcc4d97d | -11.69352 | -44.40436 | 2025-09-28 03:38:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c88c0621-c22e-3a26-871e-aede30e822b0 | -13.61819 | -48.07523 | 2025-09-28 03:38:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| aabb2dc2-83f6-32d9-bec7-b48342dc1a09 | -15.19788 | -50.09633 | 2025-09-28 03:38:00 | NOAA-21 | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 7c911c58-bfc5-33da-88e5-06493d07e3e9 | -15.55351 | -47.89228 | 2025-09-28 03:38:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a1c46294-eb16-3c59-a071-47c5db12d5f8 | -12.43951 | -45.20678 | 2025-09-28 03:38:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b253da27-82c8-3090-9af2-656895b9e947 | -11.99056 | -48.00439 | 2025-09-28 03:38:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 47c0f58b-aee1-3a1b-aad7-d447d3e732d9 | -10.90929 | -45.74067 | 2025-09-28 03:38:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 029907b5-a1df-3f92-a289-a114db427a3f | -15.5366 | -47.91903 | 2025-09-28 03:38:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 10.8 |
| bd1468e9-8495-3349-89b2-bfea3da2c560 | -13.79762 | -47.92783 | 2025-09-28 03:38:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 5.3 |
| acc9d238-f964-3a76-bcb0-330568ba89d9 | -15.25476 | -43.08583 | 2025-09-28 03:38:00 | NOAA-21 | MONTE AZUL | MINAS GERAIS | Brasil | 3142908 | 31 | 33 | nan | nan | nan | Caatinga | 39.1 |
| 81ea265e-aa92-35bd-a2a3-a4bffbc3c8d8 | -12.9159 | -45.19579 | 2025-09-28 03:38:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 678f1f43-d04f-3fdb-814a-abf8b04af3ee | -10.90579 | -45.7589 | 2025-09-28 03:38:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 3a169d5b-a573-3f74-8118-2f3ef6b47013 | -11.00162 | -45.60001 | 2025-09-28 03:38:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 26c66441-ab84-3b13-b476-812fa6136d65 | -13.61162 | -48.10604 | 2025-09-28 03:38:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 41fc729f-6ced-38d9-bd94-ddc271286705 | -11.99241 | -47.88149 | 2025-09-28 03:38:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 77e055ea-ea62-3522-88c4-19859be48a7a | -13.51551 | -47.3954 | 2025-09-28 03:38:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 1897df4f-eaa6-301d-8052-563a2b79afc1 | -9.05059 | -46.72921 | 2025-09-28 03:38:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| a31386a6-6272-33fc-a840-b6afdbd3f1b4 | -11.37511 | -44.96972 | 2025-09-28 03:38:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| cb99d2ae-b53c-35d2-85bb-263a31b67fbf | -11.99626 | -47.04942 | 2025-09-28 03:38:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| c45a84c7-cf99-3431-9c49-71f10d50540e | -12.01512 | -47.08552 | 2025-09-28 03:38:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| a9d98138-1a0e-357d-8b84-3628ffb5e591 | -14.58643 | -48.25317 | 2025-09-28 03:38:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 1c0db495-de33-3109-9c10-0d90f7cdafb1 | -12.73643 | -46.81849 | 2025-09-28 03:38:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 184a62ca-0370-3b21-bae6-8a32a8ee9ea2 | -11.71773 | -44.42354 | 2025-09-28 03:38:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 3f747e0b-dbe5-3091-b4a7-c3ddf8c7137d | -11.37864 | -44.97163 | 2025-09-28 03:38:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 2f263904-4b97-36e7-9b1f-864e601279b5 | -15.61611 | -43.88129 | 2025-09-28 03:38:00 | NOAA-21 | VARZELÂNDIA | MINAS GERAIS | Brasil | 3170909 | 31 | 33 | nan | nan | nan | Caatinga | 2.2 |
| a905831e-02e2-3df4-b514-8801bb6793a2 | -10.90478 | -45.74979 | 2025-09-28 03:38:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 6b00bcfd-8ba4-3f48-a96f-ccfb3ae47069 | -10.54318 | -43.63091 | 2025-09-28 03:38:00 | NOAA-21 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |


[Clique aqui para ver as próximas entradas](README17.md)
