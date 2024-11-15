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

## Dados Diários - Página 32

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7f2408f5-b8ee-3f92-95c6-ab4853188910 | -17.22865 | -57.194 | 2024-11-15 05:12:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 81289689-2d72-398c-8d58-f266b05799b5 | -19.77124 | -55.41331 | 2024-11-15 05:12:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 9b6336b8-3325-3c1f-b230-dba40cba8f89 | -17.69449 | -57.52217 | 2024-11-15 05:12:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| c38da383-3d97-36c4-896c-6b8d9efbb862 | -17.25942 | -57.47556 | 2024-11-15 05:12:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 20.8 |
| 51b5301f-8a42-339c-a049-2333bb790d50 | -17.70151 | -57.54794 | 2024-11-15 05:12:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 39d4a42d-2494-390c-9a20-78e6bc581e44 | -17.5994 | -57.47924 | 2024-11-15 05:12:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| e3af2e1c-080c-32cf-b509-393bcf2cb79c | -17.57646 | -57.55474 | 2024-11-15 05:12:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 7.9 |
| 6096cca7-9460-3f14-8904-f29a6eaf397f | -17.59649 | -57.47466 | 2024-11-15 05:12:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 7.6 |
| b9d5675e-2e6e-3d3d-8b3e-40176428c201 | -18.65211 | -57.32966 | 2024-11-15 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 4b89eff8-208e-344e-8f80-f60d922b6174 | -17.56431 | -57.54057 | 2024-11-15 05:12:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 15.7 |
| 09308b28-65ef-368f-991e-67bb7bb386be | -17.5747 | -57.56673 | 2024-11-15 05:12:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 40.1 |
| 7bf62d71-8e67-3475-bf8f-aa2cdd2e41be | -17.26637 | -57.47665 | 2024-11-15 05:12:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| bbfaef64-741c-38cc-945a-7427224ebbc3 | -17.65057 | -57.446 | 2024-11-15 05:12:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 93f16932-70fd-3281-99e3-1b2332900d1b | -17.29407 | -57.31236 | 2024-11-15 05:12:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 91cc0f3f-dc20-33b3-a718-5f71b4376027 | -16.95559 | -57.63571 | 2024-11-15 05:12:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 1e22856a-117a-3054-b2e5-a95a5ec79d0b | -17.56317 | -57.52401 | 2024-11-15 05:12:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 11.1 |
| 73737ff2-ab02-3121-9a0d-eee120ea9d29 | -17.57361 | -57.52564 | 2024-11-15 05:12:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 8.7 |
| cf813898-cd6f-30bc-805a-43e6fbbeeb50 | -17.58595 | -57.44122 | 2024-11-15 05:12:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| d72ff5ed-8a89-3564-a9ff-4ff06227621f | -21.08217 | -47.47991 | 2024-11-15 05:12:00 | NOAA-20 | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3de95000-99c0-3f9f-99a3-ba06d27fd8c7 | -15.88764 | -59.27648 | 2024-11-15 05:12:00 | NOAA-20 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 797d7458-3c25-3294-83d8-226f0f44c4fe | -17.57181 | -57.5622 | 2024-11-15 05:12:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 8.1 |
| f06fd738-9069-3fce-97ea-d26ae6c4ec6a | -17.25133 | -57.45794 | 2024-11-15 05:12:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 21.3 |
| 3715da70-7e9c-331d-b67c-90f349719fdb | -16.01382 | -59.38186 | 2024-11-15 05:12:00 | NOAA-20 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6d2b042c-0f6c-3aaa-9b83-712704df3b16 | -17.57357 | -57.55021 | 2024-11-15 05:12:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 7.9 |
| a9936481-8afc-3056-8d2c-ec12514b181e | -17.69296 | -57.52272 | 2024-11-15 05:12:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 66105354-de38-3c66-a038-27f11fe02267 | -17.70442 | -57.5525 | 2024-11-15 05:12:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| a8610eaf-f5c7-3858-8a48-c14a9301bade | -17.56141 | -57.53603 | 2024-11-15 05:12:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 11.0 |
| 8a21ed60-5d42-3879-a849-255304a46322 | -17.59128 | -57.48621 | 2024-11-15 05:12:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 2f93decb-7057-30ec-ac67-b1258239d71b | -17.27044 | -57.4732 | 2024-11-15 05:12:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 89869754-3e31-3bbe-9809-e77f1778a06d | -17.24668 | -57.46539 | 2024-11-15 05:12:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 11.4 |
| cd2c4557-6faf-31df-b6a7-5fc55b0391ec | -16.94582 | -57.63017 | 2024-11-15 05:12:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 51bbefc7-7a3f-35c4-b236-19249f52260b | -16.95847 | -57.64018 | 2024-11-15 05:12:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 4bee55ef-bb99-3a7f-b596-3f590c1b1cd7 | -17.62445 | -57.55299 | 2024-11-15 05:12:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 42a84760-e94a-36c2-9719-98894ecf7a96 | -17.59166 | -57.49974 | 2024-11-15 05:12:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 9b1d45e1-cfdb-3817-ab86-04b282b94e96 | -17.2432 | -57.46485 | 2024-11-15 05:12:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 10.4 |
| 1db55bd4-b1e6-3727-8309-12e592036ea8 | -15.89916 | -59.31142 | 2024-11-15 05:12:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| b97926d0-3c6a-35b1-a4be-529def1be390 | -17.56951 | -57.55365 | 2024-11-15 05:12:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 16.1 |
| 6b704b2b-44ce-3e92-be78-a7f640f74ec7 | -17.69798 | -57.52271 | 2024-11-15 05:12:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 433e9eb3-ae4d-3ded-897a-21f6e9556cf5 | -17.80624 | -57.54675 | 2024-11-15 05:12:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 428fb692-bb33-390b-b627-9b34fa3b3e97 | -17.60648 | -57.55425 | 2024-11-15 05:12:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 0c8ee8c7-034f-3a83-a361-eb24893388ab | -17.5894 | -57.4665 | 2024-11-15 05:12:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.8 |
| a92a0e6c-f9f1-3cfb-8eab-70c214167afb | -17.58822 | -57.47454 | 2024-11-15 05:12:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.1 |
| af7b0188-b2f3-3ee1-81a1-f88942f6d568 | -17.26172 | -57.48409 | 2024-11-15 05:12:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| fc37f5b4-4db2-3796-96da-53b82c067e17 | -16.93778 | -57.63691 | 2024-11-15 05:12:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.5 |
| b2095fb2-6a7e-3de3-9fd1-b9f66c561409 | -16.10075 | -60.10148 | 2024-11-15 05:12:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f1ac0956-3551-305e-86bc-888f75894446 | -17.66506 | -57.54298 | 2024-11-15 05:12:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| bd390d8c-f956-3e22-a65d-f5082946298c | -17.60996 | -57.55481 | 2024-11-15 05:12:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.2 |
| 49fd44b6-7f5c-3e87-8a93-13c9f02b1c3f | -16.21736 | -57.52277 | 2024-11-15 05:12:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.6 |
| 8f28e47c-dbda-31d7-928f-25024f9ec2b2 | -17.64359 | -57.54371 | 2024-11-15 05:12:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 23.3 |
| 8f54b097-3d21-3698-b119-f9d76cccc6d1 | -16.21792 | -59.94058 | 2024-11-15 05:12:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 00c413aa-3ab8-30b8-809a-7ea236e4986a | -17.71653 | -57.49268 | 2024-11-15 05:12:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| fd55e575-7115-35cc-bc8a-ae2afafdf167 | -17.56892 | -57.55765 | 2024-11-15 05:12:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| f20b4a45-a27f-335d-aafb-e272c617729c | -17.61749 | -57.5519 | 2024-11-15 05:12:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| a9cda91e-8fef-32a2-97cf-852207886529 | -15.51959 | -58.82684 | 2024-11-15 05:12:00 | NOAA-20 | FIGUEIRÓPOLIS D'OESTE | MATO GROSSO | Brasil | 5103809 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4217dd07-9ee0-3ef4-ab74-cabeec0e98ce | -17.70438 | -57.52784 | 2024-11-15 05:12:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.6 |
| c01f2ea8-57f9-3fc2-aca5-11ad489108bd | -17.81049 | -57.36205 | 2024-11-15 05:12:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.9 |
| 0b1f90db-20d2-36f3-95df-d4fff06a942b | -17.71023 | -57.56162 | 2024-11-15 05:12:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 0bb6763e-d560-33a0-8482-03711d5300a9 | -21.07549 | -47.4793 | 2024-11-15 05:12:00 | NOAA-20 | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 979b630d-f8a0-3901-9661-dc4c49f762c2 | -17.58053 | -57.5513 | 2024-11-15 05:12:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.1 |
| 2927c6d1-e4c3-3496-97aa-03915f372725 | -17.57876 | -57.56328 | 2024-11-15 05:12:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 11.2 |
| f6b9350e-f530-3fcd-8530-cfbbd97466d8 | -17.63431 | -57.55864 | 2024-11-15 05:12:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 12.9 |
| fb7e0101-af51-3b25-b858-af175d4f5a10 | -15.89811 | -59.2746 | 2024-11-15 05:12:00 | NOAA-20 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| effb45e7-a32f-3b09-9a6d-3879b66a7855 | -17.64824 | -57.46215 | 2024-11-15 05:12:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 9ac85bef-9e2c-38be-bec0-d6edde14813c | -17.66564 | -57.53897 | 2024-11-15 05:12:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 3462ca4c-6ac0-3df7-8a6e-89f03415da83 | -17.57416 | -57.5462 | 2024-11-15 05:12:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 7.1 |
| 45e11f2b-a164-357f-971a-4e5290f22ba5 | -17.62155 | -57.54844 | 2024-11-15 05:12:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| f00b4200-a64c-3f93-bbfd-b5c30f161d7a | -17.57371 | -57.45169 | 2024-11-15 05:12:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 66bcb476-4cce-3b71-8ac5-9e5564751af9 | -17.60938 | -57.55882 | 2024-11-15 05:12:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.2 |
| 78cf6079-2ea0-3279-b31e-102eb390c050 | -15.91135 | -59.27678 | 2024-11-15 05:12:00 | NOAA-20 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7981937e-6181-3a74-a412-4684c1e48b4f | -17.2687 | -57.4722 | 2024-11-15 05:12:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 0733c23f-522c-395e-aded-c7ea80702370 | -16.9418 | -57.63354 | 2024-11-15 05:12:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 8.0 |
| 36444688-a3b7-37e9-a99a-9a9d75e733cb | -16.02206 | -59.39425 | 2024-11-15 05:12:00 | NOAA-20 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1098cdbb-f1a2-389f-be20-14125678d93d | -17.57064 | -57.57018 | 2024-11-15 05:12:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 40.1 |
| 9af71270-f2ea-317a-a840-4f3a78c03f45 | -21.30317 | -56.02435 | 2024-11-15 05:14:00 | NOAA-20 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| dd2df849-319c-3771-b34a-9146efce07d7 | -23.65172 | -55.23181 | 2024-11-15 05:14:00 | NOAA-20 | PARANHOS | MATO GROSSO DO SUL | Brasil | 5006358 | 50 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| c556b60d-78ea-3902-94cf-deac825390d4 | -22.05392 | -56.01301 | 2024-11-15 05:14:00 | NOAA-20 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 11487e5a-35aa-3fb8-8053-fe14d9eda409 | -22.86516 | -54.66092 | 2024-11-15 05:14:00 | NOAA-20 | JUTI | MATO GROSSO DO SUL | Brasil | 5005152 | 50 | 33 | nan | nan | nan | Mata Atlântica | 7.2 |
| c41c1c08-cdf0-3cf5-9e40-1725a0dab445 | -23.71085 | -55.17002 | 2024-11-15 05:14:00 | NOAA-20 | TACURU | MATO GROSSO DO SUL | Brasil | 5007950 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| f4dd90ec-3cd2-3d19-8b94-46763a792b77 | -22.0546 | -56.00766 | 2024-11-15 05:14:00 | NOAA-20 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 4b7dde5b-c5f6-33b5-b296-0b06e16fbca6 | -21.5555 | -55.82802 | 2024-11-15 05:14:00 | NOAA-20 | GUIA LOPES DA LAGUNA | MATO GROSSO DO SUL | Brasil | 5004106 | 50 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c629cb99-a9a0-35c7-b3de-1265aa5ed160 | -21.90476 | -56.4614 | 2024-11-15 05:14:00 | NOAA-20 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1711fe0e-1109-3665-bb6c-adc200deece4 | -22.86898 | -54.66616 | 2024-11-15 05:14:00 | NOAA-20 | JUTI | MATO GROSSO DO SUL | Brasil | 5005152 | 50 | 33 | nan | nan | nan | Mata Atlântica | 7.2 |
| 2759cf69-144c-3d58-8659-2261b2787238 | -23.65121 | -55.23612 | 2024-11-15 05:14:00 | NOAA-20 | PARANHOS | MATO GROSSO DO SUL | Brasil | 5006358 | 50 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 49874627-40e5-3202-b379-4b2393a98b69 | -23.73211 | -55.38718 | 2024-11-15 05:14:00 | NOAA-20 | PARANHOS | MATO GROSSO DO SUL | Brasil | 5006358 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 6c05afa5-127a-30aa-a3f9-956608144656 | -21.55618 | -55.82261 | 2024-11-15 05:14:00 | NOAA-20 | GUIA LOPES DA LAGUNA | MATO GROSSO DO SUL | Brasil | 5004106 | 50 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 89583523-53b6-3535-a17e-5529ce1eb95c | -23.71136 | -55.16579 | 2024-11-15 05:14:00 | NOAA-20 | TACURU | MATO GROSSO DO SUL | Brasil | 5007950 | 50 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 2cf79f73-3176-3c35-a959-ab23718b8251 | -24.23955 | -50.74228 | 2024-11-15 05:14:00 | NOAA-20 | ORTIGUEIRA | PARANÁ | Brasil | 4117305 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 66b27b35-705a-3617-a2f1-c93cbf1c57f6 | -23.70983 | -55.16805 | 2024-11-15 05:14:00 | NOAA-20 | TACURU | MATO GROSSO DO SUL | Brasil | 5007950 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 611b7d69-19b7-3be3-a1a6-6c2a88be9174 | -21.36252 | -55.89872 | 2024-11-15 05:14:00 | NOAA-20 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| baac1088-1f4f-389b-af85-b2ac3a75fb21 | -23.59672 | -54.73825 | 2024-11-15 05:14:00 | NOAA-20 | TACURU | MATO GROSSO DO SUL | Brasil | 5007950 | 50 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 78407ff6-790a-3226-82d0-c55182da709a | -22.86952 | -54.66151 | 2024-11-15 05:14:00 | NOAA-20 | JUTI | MATO GROSSO DO SUL | Brasil | 5005152 | 50 | 33 | nan | nan | nan | Mata Atlântica | 7.2 |
| aaee57c5-5ad7-3c19-b7e6-866454471933 | -21.30709 | -56.02493 | 2024-11-15 05:14:00 | NOAA-20 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 14b65b67-1a07-3ee7-9574-390839a67191 | -2.8534 | -53.9915 | 2024-11-15 05:40:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 54.2 |
| dc560a2a-6ac3-31fb-8dd8-b0760ddb2dee | -2.8535 | -53.9714 | 2024-11-15 05:40:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 70.2 |
| 5ed0eb6f-de55-3a6e-8241-75939636b009 | 1.30252 | -60.39936 | 2024-11-15 05:59:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 41484764-69ba-3307-a334-4452b8c9a6de | 2.57595 | -60.69624 | 2024-11-15 05:59:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4495ed64-2a97-319f-aac8-cbd0a5ac25c8 | 1.3034 | -60.40503 | 2024-11-15 05:59:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 32e523d4-64fd-3e58-861b-1622b28c67d9 | 1.30296 | -60.40219 | 2024-11-15 05:59:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3990fd8f-4daf-3718-bfda-d9b336af621a | 1.30021 | -60.41726 | 2024-11-15 05:59:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| dc8d208a-121f-3f93-9969-8f4829aaaffb | 1.30385 | -60.40789 | 2024-11-15 05:59:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |


[Clique aqui para ver as próximas entradas](README33.md)
