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
| 3bebd107-e52c-33b3-bd44-e2181ca7b4e5 | -10.8826 | -45.3075 | 2026-09-03 02:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 82.0 |
| ae5cf934-341b-3ede-b185-eddf8e50c5af | -18.776 | -48.9226 | 2026-09-03 02:20:00 | GOES-19 | MONTE ALEGRE DE MINAS | MINAS GERAIS | Brasil | 3142809 | 31 | 33 | nan | nan | nan | Cerrado | 137.7 |
| 59ad26ce-b7a6-34c8-baf2-4999e80eb797 | -6.6542 | -59.426 | 2026-09-03 02:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 71.7 |
| dd28f355-220f-3ce5-8b3b-9b8b922e5924 | -12.4225 | -44.8059 | 2026-09-03 02:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 70.6 |
| c734c32b-e55c-38ab-8765-973a716e2613 | -6.6357 | -59.4459 | 2026-09-03 02:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 155.3 |
| cec076b1-ac12-3620-84c4-4c87bc8b423a | -6.6358 | -59.4267 | 2026-09-03 02:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 57.3 |
| de985b23-7d9c-311d-8de8-c1da66021fdb | -6.6883 | -59.9436 | 2026-09-03 02:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 86.3 |
| 200b3251-0085-3822-8a05-4331650f93f0 | -3.2485 | -47.2657 | 2026-09-03 02:20:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 91.0 |
| 0a94df0c-5d84-34da-9af9-7ba05859e332 | -6.4208 | -58.3137 | 2026-09-03 02:20:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 32.3 |
| c715d340-8682-3fa4-8745-d22207724032 | -6.7648 | -59.4408 | 2026-09-03 02:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 51.1 |
| d47ecfad-41e0-3887-95fa-30d94682c2df | -6.7463 | -59.4416 | 2026-09-03 02:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 53.0 |
| 3eb20eb8-78f1-3a45-b606-f4c415b3dae0 | -3.2486 | -47.2438 | 2026-09-03 02:20:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 104.8 |
| c817f73d-7feb-3b74-bea4-c7ec3ade1d76 | -6.6356 | -59.4652 | 2026-09-03 02:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 66.8 |
| 7325f17a-4dd6-3f51-a905-f19481ea17cd | -18.7766 | -48.8999 | 2026-09-03 02:20:00 | GOES-19 | MONTE ALEGRE DE MINAS | MINAS GERAIS | Brasil | 3142809 | 31 | 33 | nan | nan | nan | Cerrado | 78.7 |
| 56032429-eb2b-3fd3-b74d-f42882cf4b39 | -6.6698 | -59.9443 | 2026-09-03 02:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 66.1 |
| c7081f20-f608-3fb4-8925-71fc595c8a9d | -8.5916 | -67.1788 | 2026-09-03 02:20:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 65.4 |
| 3aa84b53-3b4f-3ecc-b9b8-169dbabfbbe6 | -6.654 | -59.4645 | 2026-09-03 02:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 62.2 |
| 795fad55-5cd9-3e6c-9457-0557c102dac9 | -6.6882 | -59.9628 | 2026-09-03 02:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 47.1 |
| e3eb4b02-8974-372c-9508-089141c10469 | -6.3237 | -56.0434 | 2026-09-03 02:20:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 46.4 |
| 5718ddb3-eef3-3c2b-9f1f-f4feb2a0fbc9 | -11.0006 | -45.0847 | 2026-09-03 02:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 185.7 |
| 67fe3a34-baba-3397-b41f-695b2acbee9a | -18.7967 | -48.8958 | 2026-09-03 02:20:00 | GOES-19 | MONTE ALEGRE DE MINAS | MINAS GERAIS | Brasil | 3142809 | 31 | 33 | nan | nan | nan | Cerrado | 56.6 |
| e1c55bdf-2c0d-348d-ba88-253eb80ddc0d | -18.1704 | -51.7904 | 2026-09-03 02:20:00 | GOES-19 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 47.4 |
| ca70c913-5e59-3d57-9485-5446c1c5d7dd | -6.6541 | -59.4452 | 2026-09-03 02:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 155.2 |
| f489e32e-3207-3c26-a5cc-db66fe8f926f | -18.7962 | -48.9186 | 2026-09-03 02:20:00 | GOES-19 | MONTE ALEGRE DE MINAS | MINAS GERAIS | Brasil | 3142809 | 31 | 33 | nan | nan | nan | Cerrado | 105.3 |
| 8b77bf7c-3764-3e84-9f55-593f3580c41c | -9.0415 | -65.7349 | 2026-09-03 02:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 57.3 |
| 08864bf0-f8fa-3606-8204-59c9f5cb66e5 | -6.3237 | -56.0434 | 2026-09-03 02:30:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 57.9 |
| 5d5b9560-9d29-3923-b7b6-e961fa82edf1 | -8.4675 | -54.6631 | 2026-09-03 02:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 90.5 |
| c272443f-50c3-3a67-a4b3-9dd69c7b2f55 | -18.7962 | -48.9186 | 2026-09-03 02:30:00 | GOES-19 | MONTE ALEGRE DE MINAS | MINAS GERAIS | Brasil | 3142809 | 31 | 33 | nan | nan | nan | Cerrado | 61.3 |
| fda24124-99e8-36dd-bc64-76a04774ca94 | -6.7463 | -59.4416 | 2026-09-03 02:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 56.0 |
| 9389380b-59dd-3f26-9762-4655816f1221 | -18.7766 | -48.8999 | 2026-09-03 02:30:00 | GOES-19 | MONTE ALEGRE DE MINAS | MINAS GERAIS | Brasil | 3142809 | 31 | 33 | nan | nan | nan | Cerrado | 99.1 |
| 536fdcf0-ef75-3fcc-b68f-68d39f5056b4 | -6.6358 | -59.4267 | 2026-09-03 02:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 51.7 |
| 5b02450e-ff39-3aa4-8e39-dae731bcc006 | -6.6356 | -59.4652 | 2026-09-03 02:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 72.5 |
| e21b5039-9aed-38b8-8b4f-535277d59965 | -18.1704 | -51.7904 | 2026-09-03 02:30:00 | GOES-19 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 47.7 |
| 7960a861-f534-3c26-b43c-235d38caaf70 | -6.6357 | -59.4459 | 2026-09-03 02:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 199.7 |
| aedde915-3d9e-353a-9d70-b9284a969df2 | -6.6883 | -59.9436 | 2026-09-03 02:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 79.5 |
| 89669078-81da-3fd0-b34b-0ac573a8dd94 | -12.4033 | -44.8089 | 2026-09-03 02:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 131.4 |
| 04850cfa-eec4-390c-9b7e-dbca576d5311 | -6.6542 | -59.426 | 2026-09-03 02:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 53.3 |
| 40775b54-2bcf-3f5f-b59b-c0bfc9ffe962 | -3.2485 | -47.2657 | 2026-09-03 02:30:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 62.1 |
| c413ad92-1b8e-3b97-8645-a24e892d3036 | -6.6882 | -59.9628 | 2026-09-03 02:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 40.8 |
| 9db5275a-056b-3d1f-bc28-0efc7deda858 | -6.7648 | -59.4408 | 2026-09-03 02:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 49.4 |
| d8a5d318-3ada-3120-9204-4007b57fc37a | -8.4677 | -54.6429 | 2026-09-03 02:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 107.7 |
| 2b4b8023-ac3b-3d42-b92e-ce45656df397 | -6.3052 | -56.0442 | 2026-09-03 02:30:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 48.6 |
| 18006ef7-f0b1-392d-aa40-049f1043bf6e | -6.6541 | -59.4452 | 2026-09-03 02:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 125.6 |
| 1e66b08e-8ae0-311a-8b8c-eaf7089c4a60 | -10.8826 | -45.3075 | 2026-09-03 02:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 84.2 |
| 723e22ac-292e-3cc3-9fad-0ac08761e31f | -10.9815 | -45.0874 | 2026-09-03 02:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 105.3 |
| f6657f41-9c31-3a06-9f0d-1a537686c28b | -3.23 | -47.2445 | 2026-09-03 02:30:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 56.4 |
| 4fde9128-3c41-384d-98cb-e79ce9326d9f | -11.0006 | -45.0847 | 2026-09-03 02:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 160.4 |
| 489f1e87-f77c-3998-ba7a-99505cf06b54 | -6.6698 | -59.9443 | 2026-09-03 02:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 43.6 |
| 26c191a3-dea3-34ce-82a3-b3faed0661f0 | -3.2486 | -47.2438 | 2026-09-03 02:30:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 100.5 |
| 67e08798-b04d-3cbc-9187-13f8faf7339f | -12.4037 | -44.7856 | 2026-09-03 02:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 80.9 |
| 0ec19d51-0d0d-355f-abf4-809dc7f9db95 | -6.654 | -59.4645 | 2026-09-03 02:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 48.0 |
| 22b7e33f-82cf-356e-a79e-6201265ff931 | -7.2926 | -60.7243 | 2026-09-03 02:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 65.9 |
| 53706ce5-587e-3fb5-8f10-a92bd6ab61ad | -8.43 | -54.6858 | 2026-09-03 02:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 70.6 |
| b0a54a6a-39e7-3a35-a0b8-25a35f44690c | -18.776 | -48.9226 | 2026-09-03 02:30:00 | GOES-19 | MONTE ALEGRE DE MINAS | MINAS GERAIS | Brasil | 3142809 | 31 | 33 | nan | nan | nan | Cerrado | 208.3 |
| 10a1dddf-04da-3efb-8857-64eb3367d8ba | -7.2926 | -60.7243 | 2026-09-03 02:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 112.4 |
| 9531fa88-b9e4-30a3-862a-8eb6d2395bb6 | -6.6542 | -59.426 | 2026-09-03 02:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 64.0 |
| c9ab3a86-833d-31ae-83fa-3f11ff788cc5 | -18.7962 | -48.9186 | 2026-09-03 02:40:00 | GOES-19 | MONTE ALEGRE DE MINAS | MINAS GERAIS | Brasil | 3142809 | 31 | 33 | nan | nan | nan | Cerrado | 95.5 |
| c9db4801-25b8-3bf1-9b2b-3aa400063be2 | -6.7648 | -59.4408 | 2026-09-03 02:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 37.8 |
| 0a83f85d-26c1-3652-a9b6-a195f7a7fb08 | -6.3052 | -56.0442 | 2026-09-03 02:40:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 58.4 |
| d04b8f6a-48b6-34be-84ac-876da194fd2f | -6.7463 | -59.4416 | 2026-09-03 02:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 40.1 |
| fb43650d-879a-3a50-81bd-96990b904300 | -12.4033 | -44.8089 | 2026-09-03 02:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 164.2 |
| 6523761d-168b-3c1a-a4cd-a8c3251f45b5 | -6.6357 | -59.4459 | 2026-09-03 02:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 130.2 |
| baeaf2a8-af7d-3c76-92da-8a2dd6ba6337 | -6.3237 | -56.0434 | 2026-09-03 02:40:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 42.5 |
| 5a8073db-3ae6-3b74-bd9e-759ee2eff9af | -6.6358 | -59.4267 | 2026-09-03 02:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 47.3 |
| 0911080b-3ecc-3854-950f-81dd8fc40d8b | -6.6356 | -59.4652 | 2026-09-03 02:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 58.0 |
| 0ced75e8-501d-3087-b7c5-8f304a69ed67 | -6.4209 | -58.2943 | 2026-09-03 02:40:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 31.3 |
| 98cf2ae3-1ed1-31e6-8983-63e6a21a1413 | -6.4208 | -58.3137 | 2026-09-03 02:40:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 33.0 |
| 6b70670b-440f-3c97-b1ec-f77b9b0af0ce | -18.7967 | -48.8958 | 2026-09-03 02:40:00 | GOES-19 | MONTE ALEGRE DE MINAS | MINAS GERAIS | Brasil | 3142809 | 31 | 33 | nan | nan | nan | Cerrado | 79.2 |
| e563a454-7a5d-3798-87f8-31ad65a5ccc7 | -3.2485 | -47.2657 | 2026-09-03 02:40:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 90.4 |
| e779da45-6e6c-3e15-8691-c407760ad2e8 | -8.5916 | -67.1788 | 2026-09-03 02:40:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 73.3 |
| 1f48e676-f4f8-39c9-8c97-c234d22d78f8 | -3.2486 | -47.2438 | 2026-09-03 02:40:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 141.9 |
| 791423bf-2406-3658-aac6-58962a64f789 | -10.9815 | -45.0874 | 2026-09-03 02:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 94.7 |
| 2342e994-8e8c-3aa1-b1cd-227a54343f66 | -6.6883 | -59.9436 | 2026-09-03 02:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 58.7 |
| 4ada24d5-2831-3d49-9c85-fc93314b4a66 | -18.7766 | -48.8999 | 2026-09-03 02:40:00 | GOES-19 | MONTE ALEGRE DE MINAS | MINAS GERAIS | Brasil | 3142809 | 31 | 33 | nan | nan | nan | Cerrado | 96.6 |
| 4a8a9520-5758-3b8e-9f95-9e8355442523 | -8.4675 | -54.6631 | 2026-09-03 02:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 113.5 |
| e3092d4c-1a2f-302f-b8da-4e9d2db3abe7 | -12.4225 | -44.8059 | 2026-09-03 02:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 133.7 |
| 6a0e4922-5d24-3e59-847a-562d3b1b28c4 | -10.8826 | -45.3075 | 2026-09-03 02:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 83.6 |
| 9fd984d5-eff1-3c14-9f4d-f9367eb8f316 | -8.0737 | -50.9656 | 2026-09-03 02:40:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 56.6 |
| 15980608-003f-34ac-ae74-42b4bd236ce5 | -6.6541 | -59.4452 | 2026-09-03 02:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 173.4 |
| 83d1e0e3-c791-3607-ab44-5c09aad493f9 | -7.2927 | -60.7052 | 2026-09-03 02:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 71.3 |
| dc11c816-dcea-3ca5-a0fb-e279ba2184a1 | -6.654 | -59.4645 | 2026-09-03 02:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 67.1 |
| 10ecb1a0-e40f-3f7d-8a42-8b7edc472955 | -12.4037 | -44.7856 | 2026-09-03 02:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 72.0 |
| e08c957e-86f0-3c20-ac65-3a52d9410f0f | -6.6698 | -59.9443 | 2026-09-03 02:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 54.4 |
| 32f6b78c-6832-36c6-a31e-94923bade04e | -8.4677 | -54.6429 | 2026-09-03 02:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 139.1 |
| ef7b36cb-5928-3662-bd85-5e427e0f81ed | -11.0006 | -45.0847 | 2026-09-03 02:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 187.4 |
| 243ee945-5360-3342-8c85-c9d70076c1dd | -18.776 | -48.9226 | 2026-09-03 02:40:00 | GOES-19 | MONTE ALEGRE DE MINAS | MINAS GERAIS | Brasil | 3142809 | 31 | 33 | nan | nan | nan | Cerrado | 115.9 |
| 34955d2b-2fb5-3e9a-bac2-6fe9d071a2d4 | -8.0924 | -50.9642 | 2026-09-03 02:50:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 62.2 |
| 960c8a65-e4dd-317f-81ac-8b7a7e9252d5 | -7.2926 | -60.7243 | 2026-09-03 02:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 76.6 |
| fef86598-10f9-3f2b-98fb-7858f36cb11e | -3.2486 | -47.2438 | 2026-09-03 02:50:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 94.2 |
| 468235bb-dcb3-3de8-9f99-1de0c97abfb4 | -7.311 | -60.7236 | 2026-09-03 02:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 51.9 |
| c8fad4fc-e780-3550-b636-7ff1b5fa4eb1 | -11.0006 | -45.0847 | 2026-09-03 02:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 160.3 |
| 3c96c3eb-7cab-399a-a2b8-402e5f72e55a | -7.2927 | -60.7052 | 2026-09-03 02:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 49.8 |
| c7ad0a8b-c5d0-3146-aa75-3bf250676c3d | -18.7766 | -48.8999 | 2026-09-03 02:50:00 | GOES-19 | MONTE ALEGRE DE MINAS | MINAS GERAIS | Brasil | 3142809 | 31 | 33 | nan | nan | nan | Cerrado | 130.5 |
| 2eb8932f-7222-3741-9f72-21877fc21fb6 | -6.6883 | -59.9436 | 2026-09-03 02:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 56.3 |
| 6f72f5f1-a4d8-3aea-a8ad-00af367590f8 | -8.4677 | -54.6429 | 2026-09-03 02:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 107.3 |
| 96077bb6-150a-34eb-ac6f-409868bcb2e8 | -3.23 | -47.2445 | 2026-09-03 02:50:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 48.4 |
| be2e923a-65df-3dcd-b24e-750cb337161d | -8.5916 | -67.1788 | 2026-09-03 02:50:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 65.4 |
| 60370bb9-3a2d-39e3-bbcf-3c12fede662c | -6.3052 | -56.0442 | 2026-09-03 02:50:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 64.4 |
| 1bcea340-f2d6-3637-b60b-3b405fdb1ab4 | -8.4675 | -54.6631 | 2026-09-03 02:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 99.2 |
| 81bd6532-0903-3fff-8c3e-b076b855bc4f | -6.6356 | -59.4652 | 2026-09-03 02:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 67.8 |


[Clique aqui para ver as próximas entradas](README15.md)
