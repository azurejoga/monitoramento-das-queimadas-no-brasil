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

## Dados Diários - Página 42

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4c242fdf-87c1-3837-abc3-bba4e49fe864 | -3.40429 | -52.49715 | 2025-11-14 04:44:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 97931242-755b-3b6f-b44e-9cfcfb493651 | -6.48459 | -39.34805 | 2025-11-14 04:44:00 | NOAA-20 | IGUATU | CEARÁ | Brasil | 2305506 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 52894182-6838-30a5-8d67-281f1464218a | -3.82082 | -44.25268 | 2025-11-14 04:44:00 | NOAA-20 | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7ed1ca10-b155-3d8b-834d-1698615cce08 | -4.21951 | -49.12078 | 2025-11-14 04:44:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 16.6 |
| 29d50f4f-0fc6-38ce-b4e0-a47b39205aef | -3.32003 | -52.08191 | 2025-11-14 04:44:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 4aa0b25a-72a6-33f2-8d84-b424fac00289 | -2.88465 | -45.29036 | 2025-11-14 04:44:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 2c302108-e4b6-3ce6-b100-b10eca5e11e9 | -6.20833 | -47.26701 | 2025-11-14 04:44:00 | NOAA-20 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 078f5162-c691-3ee6-b86d-9c59b609a119 | -3.71782 | -54.46166 | 2025-11-14 04:44:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0b903d32-3105-3f70-b87d-8654a60553f6 | -4.41755 | -47.59967 | 2025-11-14 04:44:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 54ad0bf2-e1c8-3f31-a598-8640e8905174 | -2.84246 | -52.36855 | 2025-11-14 04:44:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e7402d23-23f4-3339-bfe7-56579be4a1c3 | -2.88064 | -45.28978 | 2025-11-14 04:44:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 6825bd85-61e9-3a63-a241-9a16d6015a27 | -6.48157 | -43.75713 | 2025-11-14 04:44:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| bb4ab04b-c45a-304a-8ac2-02049c5041c2 | -5.54012 | -49.36711 | 2025-11-14 04:44:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f5270dd4-3be8-3e5e-98bc-d0688cc6878d | -6.4259 | -47.29912 | 2025-11-14 04:44:00 | NOAA-20 | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a3d3708e-c18d-3597-8fd4-d5359206684f | -4.71638 | -40.81519 | 2025-11-14 04:44:00 | NOAA-20 | ARARENDÁ | CEARÁ | Brasil | 2301257 | 23 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 271619e1-a48d-3fbf-84e0-a4ee776f41d6 | -1.92393 | -54.5144 | 2025-11-14 04:44:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9acebee3-3d51-3222-8888-7b3a2d2f6b3a | -2.95947 | -41.5813 | 2025-11-14 04:44:00 | NOAA-20 | LUÍS CORREIA | PIAUÍ | Brasil | 2205706 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 482ae2f7-ba7f-341e-8c4b-f39c0d9e85d3 | -4.77464 | -48.6797 | 2025-11-14 04:44:00 | NOAA-20 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 16e714cc-cff4-3c9b-bf43-e3ac03fbb979 | -3.2126 | -50.19291 | 2025-11-14 04:44:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fa8eae88-7cbc-315d-9bc4-068e168b7723 | -5.52828 | -43.68486 | 2025-11-14 04:44:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| b7e70789-123d-3e1c-a90b-e0734369a196 | -4.70778 | -46.45304 | 2025-11-14 04:44:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 698c055a-ea05-3fc5-88b1-22a59b5f2155 | -4.32503 | -48.64192 | 2025-11-14 04:44:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7f2f7db8-a3e0-30fb-85a6-294ed0ac47b5 | -5.74536 | -42.72625 | 2025-11-14 04:44:00 | NOAA-20 | AGRICOLÂNDIA | PIAUÍ | Brasil | 2200103 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 9dac2588-bd19-3486-86b6-a30b5fd5cf37 | -4.33329 | -50.82045 | 2025-11-14 04:44:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f4c451d0-2a3a-3c26-afd3-744605820a42 | -2.62964 | -49.98844 | 2025-11-14 04:44:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5f01506a-1609-3dbe-a788-6bc83ef5c5cd | -3.76212 | -47.74303 | 2025-11-14 04:44:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6086d808-aba3-3b6e-a08b-6390145d17b4 | -2.63979 | -47.29977 | 2025-11-14 04:44:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 85beb589-f6c4-3538-a7b1-15a0bf3acbef | -4.96267 | -47.71708 | 2025-11-14 04:44:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 6478010f-9e3b-3018-822f-f40683e93ab3 | -5.36622 | -46.29504 | 2025-11-14 04:44:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 15.7 |
| 4ac2ad6d-b20c-3f6a-b339-9ee1f242ce45 | -5.06654 | -49.87431 | 2025-11-14 04:44:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e615576e-4cfa-3f90-a776-6c177efa8a00 | -6.61153 | -47.63649 | 2025-11-14 04:44:00 | NOAA-20 | PALMEIRAS DO TOCANTINS | TOCANTINS | Brasil | 1713809 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| dc29c9d5-9ee3-381a-abff-41952e369bb3 | -5.69517 | -45.97005 | 2025-11-14 04:44:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4667cf9b-cb06-3d7b-80c9-8690cf15f132 | -1.83856 | -51.91324 | 2025-11-14 04:44:00 | NOAA-20 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| cace3453-8b2b-3838-89af-32de20c3c3ca | -2.96288 | -48.58615 | 2025-11-14 04:44:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d98083c5-4e2e-324c-9965-e44af8e93337 | -3.60813 | -54.71151 | 2025-11-14 04:44:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8ffeedb2-132b-37b7-afa1-bed2dc6ac0ed | -1.8336 | -53.78895 | 2025-11-14 04:44:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ccd6260a-4bcf-3e49-81c6-32d7cff889f7 | -2.27791 | -53.642 | 2025-11-14 04:44:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1326ca02-9158-3cc7-b441-3368cab1bfd7 | -3.34177 | -48.38405 | 2025-11-14 04:44:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 80f60b30-8918-308c-aaec-e6b062210659 | -5.95341 | -45.35724 | 2025-11-14 04:44:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c67419fc-98f2-31a5-9cfc-9910a5c81cad | -4.37067 | -50.88674 | 2025-11-14 04:44:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 80d1e825-f94c-3e95-bb04-241a7f4b32f9 | -1.34237 | -54.6116 | 2025-11-14 04:44:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| ce1e1dcc-227f-3dc4-9b66-b87269064635 | -3.95143 | -47.49902 | 2025-11-14 04:44:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 3720c437-002e-39ae-ba8b-a2bb33165a36 | -1.83128 | -53.79526 | 2025-11-14 04:44:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 62dd3d4c-f9ac-3d9c-81e9-c0c4b5d0c467 | -7.35414 | -43.35421 | 2025-11-14 04:44:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d3cdb488-2de1-36af-b44e-aa3e55b6e4ee | -6.2394 | -46.24732 | 2025-11-14 04:44:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ea562d49-d78b-385e-b317-d99b8803ee01 | -5.87421 | -48.88424 | 2025-11-14 04:44:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e64b5452-4c35-357d-a03c-c0c62207e639 | -3.42685 | -50.17054 | 2025-11-14 04:44:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f448e927-9a96-3ce3-90cd-e9fefc5a3d6d | -4.23951 | -42.73636 | 2025-11-14 04:44:00 | NOAA-20 | MIGUEL ALVES | PIAUÍ | Brasil | 2206209 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b842e704-6491-3249-88bc-4fe17a0e6c88 | -5.69075 | -49.20844 | 2025-11-14 04:44:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d6ed40b9-79f9-37d9-81e4-9edb2f2c4566 | -3.60736 | -54.7163 | 2025-11-14 04:44:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 17f0f8fc-dc3f-3856-82bd-8cfd99b64bd1 | -3.76504 | -47.74754 | 2025-11-14 04:44:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 446e0d29-b50c-39dc-88cc-5d498a136088 | -4.70087 | -46.44712 | 2025-11-14 04:44:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 331d623e-356f-3673-8efe-225e46789dfb | -3.16076 | -50.62823 | 2025-11-14 04:44:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4027e826-f8f4-3005-8f46-ea3d3413b0c2 | -6.71953 | -42.95607 | 2025-11-14 04:44:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 5.1 |
| a3fd5960-2405-34b1-9f80-d6437d08ab1c | -2.1736 | -48.36984 | 2025-11-14 04:44:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 457389e3-0382-3442-a725-7162eb9c5d76 | -5.97372 | -42.59393 | 2025-11-14 04:44:00 | NOAA-20 | SÃO GONÇALO DO PIAUÍ | PIAUÍ | Brasil | 2209807 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 7932a68a-9c08-377d-81a9-6abccdcfe46e | -5.2553 | -46.18004 | 2025-11-14 04:44:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9fdade1c-4e44-3b76-bc96-b4b5dd4eff97 | -5.84467 | -47.88722 | 2025-11-14 04:44:00 | NOAA-20 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f32ced57-35d6-3b08-939e-a47c8174dcbb | 2.75374 | -60.37137 | 2025-11-14 04:44:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 10f15824-44fb-34a9-b8a0-92c908469c5a | -4.42548 | -47.26133 | 2025-11-14 04:44:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7fb0b297-adfa-3671-9d35-9c3af58e2289 | -4.57219 | -50.44896 | 2025-11-14 04:44:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d000db7b-0865-3b73-ba68-1912289db099 | -1.90373 | -52.61879 | 2025-11-14 04:44:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 77e9c255-0dc9-37bc-80d1-74aac7462f85 | -4.22007 | -49.1172 | 2025-11-14 04:44:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 16.2 |
| 3413f142-082a-314f-9d21-8e7f0de24302 | -2.71552 | -47.39743 | 2025-11-14 04:44:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 16fac7df-7e84-3811-b7ee-72a098ea050d | -3.35827 | -45.34748 | 2025-11-14 04:44:00 | NOAA-20 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 5.8 |
| f30b185f-2cec-353a-9fda-1dc0264766c3 | -2.63685 | -47.30048 | 2025-11-14 04:44:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 03b60d61-4537-3ee8-a6fe-e3d176923ed4 | -5.63486 | -48.24627 | 2025-11-14 04:44:00 | NOAA-20 | BREJO GRANDE DO ARAGUAIA | PARÁ | Brasil | 1501758 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 09cea1da-6274-3540-ad4d-fe045c992e7e | -2.54992 | -47.80458 | 2025-11-14 04:44:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d0151922-6eb3-3a62-acb5-de3a49f7a35a | -5.01212 | -50.91367 | 2025-11-14 04:44:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b5b65d85-429d-39ea-9f2a-b91599c32361 | -3.36628 | -48.40681 | 2025-11-14 04:44:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8a6c6c74-4aa9-3190-9508-b6b208554ecf | -5.02632 | -49.7857 | 2025-11-14 04:44:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| cd76de11-338c-3234-9892-525cb8114946 | -4.52911 | -46.40012 | 2025-11-14 04:44:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 40d585d7-56b4-39e5-a238-46915facadba | -3.74486 | -44.27683 | 2025-11-14 04:44:00 | NOAA-20 | CANTANHEDE | MARANHÃO | Brasil | 2102705 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3c060968-a3c8-3672-b1ac-3a6e0a0584f5 | -4.70851 | -46.44836 | 2025-11-14 04:44:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 9.4 |
| e187d749-b672-3432-93f9-6f0fd84bb70d | -3.15746 | -50.62772 | 2025-11-14 04:44:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8e5fdd26-6349-3d14-961b-2d70b2890457 | -2.94207 | -49.36497 | 2025-11-14 04:44:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 29c7d909-70cd-3322-92b8-e78fb61ea6a5 | -3.42354 | -50.17002 | 2025-11-14 04:44:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| dcb95a94-1cb4-3a80-8679-37db56c191df | -1.93575 | -52.09545 | 2025-11-14 04:44:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f96f65ff-6634-35fd-b600-d9d149fdbd83 | -2.44987 | -48.82018 | 2025-11-14 04:44:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2a4294dc-c109-3059-9895-b2c2dea5a3a6 | -6.52237 | -43.40616 | 2025-11-14 04:44:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Caatinga | 5.6 |
| b9842072-4bcc-3bee-8c8b-2cbae201f23a | -6.09709 | -41.60037 | 2025-11-14 04:44:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 42162b41-2b33-314a-abc4-35de54b56c18 | -7.46684 | -42.57131 | 2025-11-14 04:44:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 3e89b17a-2dbe-3104-a526-3440b47858ab | -4.11648 | -50.06327 | 2025-11-14 04:44:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8897fd6a-91d0-3bb2-9af2-6fb45c098c12 | -2.63329 | -47.29992 | 2025-11-14 04:44:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2193a4f3-03c0-3b85-b7cc-ca1381ba49fa | -5.0239 | -44.51207 | 2025-11-14 04:44:00 | NOAA-20 | SÃO JOSÉ DOS BASÍLIOS | MARANHÃO | Brasil | 2111250 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ad23a62d-aea5-33ae-854f-eb33c68484ee | -3.46198 | -43.188 | 2025-11-14 04:44:00 | NOAA-20 | ANAPURUS | MARANHÃO | Brasil | 2100808 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 94f185a6-ea31-3bb7-a23f-3d2757d1f692 | -5.36696 | -46.29018 | 2025-11-14 04:44:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 15.7 |
| 18ea9724-e2f1-3223-9fa2-11bf6fd994fc | -4.70397 | -46.45242 | 2025-11-14 04:44:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 3.3 |
| b5ca077f-c7ce-3e37-a90a-fd908aeea610 | -4.71137 | -46.44628 | 2025-11-14 04:44:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 5.2 |
| a0a30f3b-66ea-3950-a892-2914020319b9 | -4.38788 | -50.60348 | 2025-11-14 04:44:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d17e78ff-e405-325c-b37f-7d074f9d30ad | -5.40234 | -48.31725 | 2025-11-14 04:44:00 | NOAA-20 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b8d5aa7a-5e25-3842-8695-1078d752da17 | -3.63086 | -49.11139 | 2025-11-14 04:44:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 603bad15-3174-3c6c-86c1-04a5d27aa5d5 | -7.45647 | -42.56995 | 2025-11-14 04:44:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 4493cb00-1632-3423-9a9b-04097054df4e | -3.24886 | -43.29451 | 2025-11-14 04:44:00 | NOAA-20 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d4cde1ca-8c6b-3885-b8fc-5715230fe10a | -4.28897 | -41.81318 | 2025-11-14 04:44:00 | NOAA-20 | PIRIPIRI | PIAUÍ | Brasil | 2208403 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| ee3df601-9040-390e-898b-483a80814e1b | -2.45323 | -48.8207 | 2025-11-14 04:44:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 4eccaa96-0f7e-396c-9d3e-e45aef4b0eac | -3.80312 | -44.39843 | 2025-11-14 04:44:00 | NOAA-20 | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 223fd37e-60d0-3696-9db5-8e87a38ba8ec | -2.96088 | -41.58282 | 2025-11-14 04:44:00 | NOAA-20 | LUÍS CORREIA | PIAUÍ | Brasil | 2205706 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d04d6772-9846-3871-8503-0d2f222f8100 | -3.35479 | -45.34335 | 2025-11-14 04:44:00 | NOAA-20 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ce4e56c8-79ac-3e83-b240-297dfe196154 | -2.63623 | -47.29923 | 2025-11-14 04:44:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |


[Clique aqui para ver as próximas entradas](README43.md)
