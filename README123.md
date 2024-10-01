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

## Dados Diários - Página 123

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6a5a3301-d935-3275-9825-d7dc641c957b | -17.07548 | -56.74836 | 2024-10-01 05:08:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 15a98cdb-1ce1-3e52-9e05-d0ef79453612 | -17.07492 | -56.7291 | 2024-10-01 05:08:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 7fded5dc-6f81-3b2b-ba0f-d51f4059509b | -17.07436 | -56.73285 | 2024-10-01 05:08:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| cd6aac29-76ef-3bd4-9fab-2f243f11e966 | -17.0738 | -56.73659 | 2024-10-01 05:08:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.2 |
| 3e834d5c-fd1f-350a-914e-550d3edca4d9 | -17.0738 | -56.71358 | 2024-10-01 05:08:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 5d7cbc33-2e78-3930-9a73-ac5535456835 | -17.07379 | -56.75958 | 2024-10-01 05:08:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 04997c48-4837-3164-b5e5-b8f726613653 | -17.07324 | -56.71733 | 2024-10-01 05:08:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 68cb0f2c-06a9-3951-bef0-00f11f3ed890 | -17.07323 | -56.74033 | 2024-10-01 05:08:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.2 |
| e4ca881d-64d8-33ab-b7f0-368f66b4a4bb | -17.07267 | -56.72107 | 2024-10-01 05:08:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| c079ee28-e3ab-3ef6-a661-ec8c4def0714 | -17.07211 | -56.72482 | 2024-10-01 05:08:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 73577d0c-b730-335c-a13a-47cd076d3cc6 | -17.07155 | -56.72856 | 2024-10-01 05:08:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 66d75ca3-d12f-3088-82dc-fb27584f2df2 | -17.07099 | -56.75529 | 2024-10-01 05:08:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 2260cd35-e318-36a4-93d3-4c1ec991915b | -17.07099 | -56.7323 | 2024-10-01 05:08:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 6fe98f9b-353c-34de-a52c-2f67ec7998a5 | -17.07043 | -56.71303 | 2024-10-01 05:08:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 511e1811-44c6-32a0-931e-4efdc1d17414 | -17.06986 | -56.71678 | 2024-10-01 05:08:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| a9bb04e5-cde7-3c53-8753-dbc9e457dd40 | -17.0693 | -56.74353 | 2024-10-01 05:08:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 2dac693c-c40a-3806-8f88-9251655e8575 | -17.0693 | -56.72053 | 2024-10-01 05:08:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| d0c7ba71-12db-3342-b313-915892d0fcc5 | -17.06874 | -56.74727 | 2024-10-01 05:08:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 6d389272-69da-3876-a5d8-fb16db8f7072 | -17.06874 | -56.72427 | 2024-10-01 05:08:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 7f26ea2e-81ec-31e6-a048-6bfc00c1af70 | -17.06818 | -56.72801 | 2024-10-01 05:08:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 7e9cb7f0-b3f4-3071-96c4-2c45965faba8 | -17.06762 | -56.75475 | 2024-10-01 05:08:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 13b6ab56-9688-367e-91ac-f8ad52ee5864 | -17.06762 | -56.73176 | 2024-10-01 05:08:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 1dd67e18-acc5-3f41-9ee8-c2b1c935767f | -16.89711 | -57.69466 | 2024-10-01 05:08:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 1db33118-b78f-3295-9c36-4f50f2356d67 | -16.89656 | -57.69826 | 2024-10-01 05:08:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 41a77b96-c0b2-3d28-998c-f095c3aa86d9 | -16.896 | -57.70186 | 2024-10-01 05:08:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 3d331664-0eb2-3cb0-8d49-5ff20912b200 | -16.89544 | -57.70546 | 2024-10-01 05:08:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 5f7c306d-b1b1-344e-bf3c-26363471104a | -16.8938 | -57.69411 | 2024-10-01 05:08:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| fe61ab93-51a4-3cc6-aae5-b95154ce6995 | -16.89377 | -57.71627 | 2024-10-01 05:08:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 0a590d78-ae35-3221-8d92-47a506612914 | -16.89325 | -57.69771 | 2024-10-01 05:08:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 27488c82-f466-3907-bb10-5f3c9ca9b030 | -16.89269 | -57.70132 | 2024-10-01 05:08:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 26dce6b0-b492-3519-ab0c-a80267f61444 | -16.89213 | -57.70491 | 2024-10-01 05:08:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 973adeed-254b-3202-87c0-27889787e09f | -16.89158 | -57.70851 | 2024-10-01 05:08:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 955f4248-a054-3eb3-9578-483fcf770ca5 | -16.89046 | -57.71571 | 2024-10-01 05:08:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 5c3b9482-576b-351d-a306-ca8dedca6d27 | -16.88991 | -57.71932 | 2024-10-01 05:08:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.7 |
| 00956cbb-1375-3b4e-bbaf-d25dd677e528 | -16.88938 | -57.70076 | 2024-10-01 05:08:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 31cf1ac3-aae8-36b9-9409-74944c402ec0 | -16.88882 | -57.70435 | 2024-10-01 05:08:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 5114a75a-d9ee-3900-91f1-eaca14e04bbd | -16.88826 | -57.70796 | 2024-10-01 05:08:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| ad51f11e-1902-374f-b70a-28dc39c241db | -16.88771 | -57.71156 | 2024-10-01 05:08:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.7 |
| 84df5ae7-dcf9-30f5-aa60-304abaa5b291 | -16.88715 | -57.71516 | 2024-10-01 05:08:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.7 |
| 511736f4-e3d1-33a6-9d25-10272b5369d9 | -16.8866 | -57.71877 | 2024-10-01 05:08:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 5c8cb610-e32d-34f0-a973-929b0591fa75 | -16.88607 | -57.7002 | 2024-10-01 05:08:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 1c5629ef-c3c2-3492-82b2-b2b7605e9548 | -16.88551 | -57.7038 | 2024-10-01 05:08:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 637d072c-7453-352a-815d-2403a8f75724 | -16.88495 | -57.70741 | 2024-10-01 05:08:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| e5efd766-b539-3e9f-820f-030c2a0d6f94 | -16.8844 | -57.71101 | 2024-10-01 05:08:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.7 |
| 8d8ade7f-77eb-31eb-8397-bd997f263c6a | -16.88384 | -57.71461 | 2024-10-01 05:08:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.7 |
| 78d81e53-6f81-3078-be5d-0ce9cea42dec | -16.88328 | -57.71821 | 2024-10-01 05:08:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 9309a9ae-3813-39f9-9e41-c0a83c1fd32e | -16.88276 | -57.69965 | 2024-10-01 05:08:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 92113ae5-308d-3e2f-8415-8bba9c718e09 | -16.87889 | -57.7027 | 2024-10-01 05:08:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| ebd93a27-a7a7-314a-b066-e6457432125d | -16.87833 | -57.7063 | 2024-10-01 05:08:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 57b3f70b-954e-3c40-afda-9c7b5d6efcb7 | -16.87613 | -57.69855 | 2024-10-01 05:08:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 10.0 |
| eceaa6fb-92cb-345d-86ef-9ea87c83d016 | -16.87558 | -57.70215 | 2024-10-01 05:08:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.1 |
| 2969ef34-d156-33b0-8887-93c37969701f | -16.87282 | -57.698 | 2024-10-01 05:08:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 10.0 |
| 7a89cb6f-37c4-3132-a9ab-f6d4eb0de1b1 | -16.87227 | -57.7016 | 2024-10-01 05:08:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.1 |
| 29c6cb0d-6fb0-35a7-be6d-1b39f304f53c | -16.87007 | -57.69385 | 2024-10-01 05:08:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.1 |
| 72207578-21e1-398c-9fea-bfa41418bbad | -16.86675 | -57.6933 | 2024-10-01 05:08:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.1 |
| 1d6b221c-741d-3683-b148-3f420966f369 | -16.8662 | -57.6969 | 2024-10-01 05:08:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.1 |
| f6fd0e8f-bda6-35d8-9a33-7d33853351f0 | -16.86289 | -57.69635 | 2024-10-01 05:08:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| ba795ca7-7159-38c1-b0b0-0e4c7c3154d9 | -16.85682 | -57.69164 | 2024-10-01 05:08:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 21e8dcb0-39e1-377b-908c-59678d1c9f7f | -16.85626 | -57.69524 | 2024-10-01 05:08:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 3964b2f6-8c3c-386f-91a6-f7d52b4bd735 | -16.85571 | -57.69884 | 2024-10-01 05:08:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 36f62a65-f6b7-34a8-af91-16258296e85d | -16.85295 | -57.69468 | 2024-10-01 05:08:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 32329c39-add4-3960-ab01-34fe07b9c619 | -16.8524 | -57.69829 | 2024-10-01 05:08:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 17f99028-fba7-31e1-81c6-ec841d5d5503 | -16.85184 | -57.70189 | 2024-10-01 05:08:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| a1f2e69e-fb70-34e5-88a7-520d7b8cf196 | -16.84964 | -57.69414 | 2024-10-01 05:08:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 6ad4667d-e04d-37cb-87a8-a6c317e90333 | -16.84909 | -57.69774 | 2024-10-01 05:08:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 573fafe1-9879-390a-b128-061fd8300b75 | -16.84853 | -57.70134 | 2024-10-01 05:08:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| b96b119e-76b0-3974-bb29-7d6432b6dc1b | -19.16564 | -57.47631 | 2024-10-01 05:08:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 6df1dc7c-92e9-36a5-866e-9f9d4976688a | -19.16507 | -57.48013 | 2024-10-01 05:08:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 231c6b6d-69c7-3fbb-8c98-31f6922077b0 | -19.16228 | -57.47575 | 2024-10-01 05:08:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 7931d2ce-9dc9-3c57-83f5-24496acd5fe7 | -19.16172 | -57.47956 | 2024-10-01 05:08:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| cb1f3fa3-fe78-3653-a1b7-f6447f41ca03 | -19.15837 | -57.47899 | 2024-10-01 05:08:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 4cf96851-463d-3944-83f2-8ab5b1153b71 | -19.15558 | -57.47463 | 2024-10-01 05:08:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| af66d38d-925b-3410-b0dc-e291b4d0252a | -19.15502 | -57.47843 | 2024-10-01 05:08:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| cdd0c95e-4aae-3a47-b974-e426e88a4b0f | -19.15353 | -57.47422 | 2024-10-01 05:08:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| dba884f0-f098-3363-a501-1f16b0882531 | -19.15295 | -57.47803 | 2024-10-01 05:08:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 0252123d-029b-33e1-96af-d87c45dd461b | -19.13343 | -57.47084 | 2024-10-01 05:08:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 13.6 |
| bdc3789b-456f-3404-aaac-b9b440d483f7 | -19.13064 | -57.46652 | 2024-10-01 05:08:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.3 |
| a7658a5c-cfe1-3f92-834b-1318828dabee | -19.13008 | -57.47027 | 2024-10-01 05:08:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 13.6 |
| fa6d1668-3f36-32d4-a206-9190932ab20a | -19.12729 | -57.46597 | 2024-10-01 05:08:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 48.5 |
| c5b4e806-e0d0-382a-8b8c-b9a7b5925548 | -19.12673 | -57.46971 | 2024-10-01 05:08:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 24.3 |
| 9b8b1925-30b8-3cfd-8cc2-79b180c16990 | -19.12616 | -57.4735 | 2024-10-01 05:08:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 24.3 |
| 30ab939e-79af-311a-8aed-75c87a33a7d9 | -19.12394 | -57.46541 | 2024-10-01 05:08:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 48.5 |
| 954dde5b-f68f-3c68-8928-252744bbcf32 | -19.12337 | -57.46915 | 2024-10-01 05:08:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 24.3 |
| 2c97fcc6-a2a0-3357-88d9-cb3bd88a87ad | -19.1228 | -57.47294 | 2024-10-01 05:08:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 24.3 |
| 72fc60b5-e6f2-3ab4-b660-3072eb4a4fa9 | -19.12058 | -57.46485 | 2024-10-01 05:08:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 12.0 |
| af9eb49a-a158-3577-9afc-7c46afb717e2 | -19.11768 | -57.507 | 2024-10-01 05:08:00 | NOAA-21 | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 3.5 |
| c7474f4d-0513-3bfa-830e-647fb1cebf70 | -19.1161 | -57.47184 | 2024-10-01 05:08:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 38.9 |
| ae37e032-02a3-368e-8e80-d9e0bf4428a0 | -19.11495 | -57.47948 | 2024-10-01 05:08:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.2 |
| fff3a60e-5fed-3089-ace0-601483f9399e | -19.1138 | -57.51001 | 2024-10-01 05:08:00 | NOAA-21 | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 3.2 |
| eaf32a39-cbf4-37e2-90eb-e9418d3e7827 | -19.1116 | -57.47892 | 2024-10-01 05:08:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.2 |
| b0851f09-f8fc-3493-8889-10e37bd853d7 | -19.11154 | -57.50221 | 2024-10-01 05:08:00 | NOAA-21 | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 3.5 |
| fca65bad-8cf0-39c5-89a0-ae5d9c952001 | -19.11102 | -57.48282 | 2024-10-01 05:08:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| be01f162-deb1-3b4b-8671-55f1449824e7 | -19.11044 | -57.48672 | 2024-10-01 05:08:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 68818d48-1ea0-36b7-a71f-0b65020d966a | -18.7119 | -57.31486 | 2024-10-01 05:08:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.8 |
| 3952376a-9d34-38d6-9091-ce5faeadadba | -18.71134 | -57.3186 | 2024-10-01 05:08:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.2 |
| c0b81ee7-dd8b-3bae-b466-b30ae3415b7d | -18.70854 | -57.3143 | 2024-10-01 05:08:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 17.8 |
| 23bcc8da-9563-3c89-b236-d67a5e1f6648 | -18.70798 | -57.31804 | 2024-10-01 05:08:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 9.1 |
| 75ee711e-5d69-3c0f-a07f-9576468262c7 | -18.7035 | -57.32497 | 2024-10-01 05:08:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 7.5 |
| 9d73aaab-8efc-3cb9-a572-b53b39495a06 | -18.70015 | -57.32441 | 2024-10-01 05:08:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.7 |
| 2bf2bf54-794b-34e4-888d-819fa17cad6e | -18.69959 | -57.32815 | 2024-10-01 05:08:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.7 |


[Clique aqui para ver as próximas entradas](README124.md)
