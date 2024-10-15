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

## Dados Diários - Página 54

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6fb0b833-1a7d-3b0d-abc0-33eb79d1db35 | -2.65066 | -49.5165 | 2024-10-15 04:46:00 | NOAA-20 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| e817dc1a-f025-36ba-89d8-fc0fc3a11cf2 | -2.65007 | -49.52029 | 2024-10-15 04:46:00 | NOAA-20 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 77418aaa-b16a-35d8-978a-deabae72442f | -2.63069 | -49.27854 | 2024-10-15 04:46:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7bee81ea-97f6-315a-b746-f2c2cca0906d | -2.6284 | -49.07905 | 2024-10-15 04:46:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f0a35e97-32db-3cd8-a72f-60f182b044c6 | -2.62779 | -49.27415 | 2024-10-15 04:46:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| dea66e26-1e15-31cb-861a-f76b0bf786f8 | -2.62778 | -49.08298 | 2024-10-15 04:46:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d55482aa-60a3-3d72-8829-c8be10f0267c | -2.6272 | -49.278 | 2024-10-15 04:46:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ab4b366c-3774-3cbd-b3b4-85e5f62e8bb3 | -2.62371 | -49.27745 | 2024-10-15 04:46:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| bd2968cb-2d89-37a1-bd61-94656ed73e94 | -2.61951 | -49.08976 | 2024-10-15 04:46:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c161ef76-6f93-31fb-aa42-2d0b57ce9bde | -2.6166 | -49.08529 | 2024-10-15 04:46:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c223cd9c-da24-369f-9719-09f18f459571 | -2.61599 | -49.08923 | 2024-10-15 04:46:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0a742543-e79c-3784-a0c9-6b1bede771ea | -2.61581 | -49.11332 | 2024-10-15 04:46:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 05cc5608-8841-3c0c-bd16-3deb948fd32f | -2.6152 | -49.11724 | 2024-10-15 04:46:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9de12984-9ca4-3094-870e-022af37561aa | -2.6123 | -49.11278 | 2024-10-15 04:46:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5515963b-75f4-3a2c-8ecc-1f2eff361bfe | -2.61168 | -49.1167 | 2024-10-15 04:46:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 959ce08d-e240-3eb8-80ce-33d1ff7a9ae7 | -2.6094 | -49.1083 | 2024-10-15 04:46:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b5cf3aa6-b8ed-3618-8cba-4c37af460aca | -2.60817 | -49.11615 | 2024-10-15 04:46:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ebfab76e-dfcb-3994-9377-d85923f79eb4 | -2.60466 | -49.11561 | 2024-10-15 04:46:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2a54baef-dadb-3a65-856e-2ec43f4714be | -2.60401 | -49.49772 | 2024-10-15 04:46:00 | NOAA-20 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9a88e512-9b4b-3f8d-b6c4-df349fdfa070 | -2.60114 | -49.11507 | 2024-10-15 04:46:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 9c1c0b5b-6faf-3019-bac3-b491cf579f81 | -2.59364 | -49.79124 | 2024-10-15 04:46:00 | NOAA-20 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1c8eefa5-207a-3197-a8d4-794487e5dec6 | -2.58918 | -48.95956 | 2024-10-15 04:46:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 928638a7-bbac-31cf-af7f-4e5128646971 | -2.58857 | -48.96353 | 2024-10-15 04:46:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0a049f20-4fd4-351d-b26f-89be1eae3ce2 | -2.58282 | -49.14029 | 2024-10-15 04:46:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 1f00ade5-e50e-32db-aa6a-5717c98298e5 | -2.57917 | -48.95395 | 2024-10-15 04:46:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7e10570e-29b8-3856-aaba-657a94be88f5 | -2.57856 | -48.95792 | 2024-10-15 04:46:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4114c372-1fd3-3236-98d9-e1ef98c04fc7 | -2.57714 | -49.76217 | 2024-10-15 04:46:00 | NOAA-20 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 81360c91-4d05-3ba0-8cb2-12635b0aacd9 | -2.57436 | -49.07883 | 2024-10-15 04:46:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9f0e9616-4f45-378e-abc6-6fa6f88da496 | -2.56391 | -48.93528 | 2024-10-15 04:46:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2d8e6e87-2beb-3efa-8df0-db994044d051 | -2.56036 | -48.93473 | 2024-10-15 04:46:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 77a1442b-2d98-3c53-97ee-f02967ac19ab | -2.53264 | -49.02088 | 2024-10-15 04:46:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9d3a30cb-4b23-346d-9977-ad26d83c970d | -2.52849 | -49.02429 | 2024-10-15 04:46:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e260cf43-8f6a-3cb1-a11d-9e93b208da9f | -2.49932 | -49.07227 | 2024-10-15 04:46:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 16.3 |
| 5aef12a0-4d69-33e9-b44f-611f3cb233a9 | -2.49581 | -49.07173 | 2024-10-15 04:46:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 16.3 |
| 685eb677-8831-3c8a-8e78-dc3dc2153daa | -2.49125 | -49.29309 | 2024-10-15 04:46:00 | NOAA-20 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a53b1fbe-8caf-3413-9c3c-47a2e0f4062c | -2.48969 | -49.29362 | 2024-10-15 04:46:00 | NOAA-20 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 41c12d51-8c82-3c9f-bfdc-fa75981272da | -2.48617 | -49.11042 | 2024-10-15 04:46:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6811492f-beba-3f73-a661-06135edcfefe | -2.48018 | -49.03312 | 2024-10-15 04:46:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 493bd6b0-cfd3-3227-8d54-a1327a5985e3 | -2.47666 | -49.03258 | 2024-10-15 04:46:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e5a030dd-2a3a-3135-b62f-abfe5e51953d | -2.47166 | -49.62794 | 2024-10-15 04:46:00 | NOAA-20 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e53b71e5-ccad-38c4-8dca-b2c2f0a9ffc8 | -2.43219 | -48.94538 | 2024-10-15 04:46:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a6ddfdc1-64ff-3ca3-9116-726e0a0dde44 | -2.42096 | -48.94773 | 2024-10-15 04:46:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 647b39c2-5a6f-364c-b4ef-beb1a43358d5 | -2.41961 | -49.73855 | 2024-10-15 04:46:00 | NOAA-20 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f15a849b-d946-3276-824c-2d92f75ed7b5 | -2.41036 | -48.94612 | 2024-10-15 04:46:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ed282b33-6bfa-3bc7-b3ab-2e70cb5e8240 | -2.40974 | -48.95008 | 2024-10-15 04:46:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d0f45291-c8ae-324e-a841-169e2f54d210 | -2.39913 | -48.94846 | 2024-10-15 04:46:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| f7c73bc5-98f7-39cf-b3cc-17a774f1a96d | -2.39044 | -49.18794 | 2024-10-15 04:46:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 596f000d-180b-386d-a445-e355a16af76a | -2.38983 | -49.19181 | 2024-10-15 04:46:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| a7903305-63c0-3e36-a535-90bfa61b17fd | -2.38954 | -49.14806 | 2024-10-15 04:46:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cd03dc60-d2c7-3f7f-84e9-9a5680b07a2a | -2.38694 | -49.18741 | 2024-10-15 04:46:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cfa77c5a-a79d-34fa-bc12-af025fbb499a | -2.38633 | -49.19128 | 2024-10-15 04:46:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5eddb042-ff6f-363d-9ae0-16c227a3afc0 | -2.38497 | -49.13141 | 2024-10-15 04:46:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5407d71e-d095-3968-b58a-111b2114cf9f | -2.38436 | -49.1353 | 2024-10-15 04:46:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4782fa5c-4b6a-3a45-a2ef-8975523ab9f6 | -2.35787 | -49.84234 | 2024-10-15 04:46:00 | NOAA-20 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b692c426-fc25-365d-ae46-54846d6e984a | -2.84137 | -49.86557 | 2024-10-15 04:46:00 | NOAA-20 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ac41d8d5-5632-3188-8205-429dfd9a385f | -2.83716 | -49.53196 | 2024-10-15 04:46:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 773ca581-b9d7-334e-a8c6-e552f13d47d2 | -2.83311 | -49.5352 | 2024-10-15 04:46:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 8140ab74-1887-3603-978b-adcc6c0c771a | -2.80719 | -49.51953 | 2024-10-15 04:46:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 34b98427-dbb8-3107-9c13-5bbfd755e737 | -2.77918 | -49.43427 | 2024-10-15 04:46:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 14ce7291-c04a-34a6-91a9-ea4b4876b2bc | -2.7763 | -49.42992 | 2024-10-15 04:46:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 192c3eb0-7e74-3b11-9747-c787cd7b4152 | -2.77571 | -49.43375 | 2024-10-15 04:46:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 57e8576c-0c32-3049-b58e-0f6a6c370d80 | -2.22717 | -50.67882 | 2024-10-15 04:46:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| baa6f542-da98-31db-83ca-2b8911f463df | -2.22662 | -50.68232 | 2024-10-15 04:46:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3d7d01fb-6268-3af0-893a-85844a49b0d1 | -2.18925 | -50.81229 | 2024-10-15 04:46:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6c01eb6c-0fa6-33ac-a6af-07c86ce3b5b1 | -1.48451 | -51.58068 | 2024-10-15 04:46:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 28c5462c-382b-3aca-bd33-0137d581118e | -2.64615 | -51.88605 | 2024-10-15 04:46:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b2226543-345e-3650-a97e-3f2c18de0796 | -2.59108 | -51.84541 | 2024-10-15 04:46:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6dd3dde0-c2d0-30e3-8159-e08d6cd9eca5 | -2.58286 | -51.85467 | 2024-10-15 04:46:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d61942b6-9842-34e3-8129-7e67a4a46b3b | -2.58232 | -51.8581 | 2024-10-15 04:46:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c48bfe5b-2d4f-3ef1-b5e7-f78d40ad1848 | -2.58009 | -51.85073 | 2024-10-15 04:46:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d62e1899-ded6-3d5e-aefb-20cbdab67fee | -2.57955 | -51.85416 | 2024-10-15 04:46:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 112d2c96-f67a-301e-b64f-4bf64edbf2ae | -2.57902 | -51.85759 | 2024-10-15 04:46:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6d72a350-a4c3-327d-85ec-7d3fb8eb7811 | -2.57625 | -51.85365 | 2024-10-15 04:46:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a5a5f5bf-5236-3d2e-8a27-e406a28a1c77 | -2.57571 | -51.85708 | 2024-10-15 04:46:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 89298694-a835-3c01-87de-46e414004e56 | -2.51547 | -50.72354 | 2024-10-15 04:46:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8f008fd3-9fca-399d-9794-972513a8b21f | -2.51492 | -50.72704 | 2024-10-15 04:46:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 42ee142a-25c6-374a-8340-8492523c3a27 | 1.01078 | -52.21924 | 2024-10-15 04:46:00 | NOAA-20 | PEDRA BRANCA DO AMAPARI | AMAPÁ | Brasil | 1600154 | 16 | 33 | nan | nan | nan | Amazônia | 78.8 |
| 4c9c45eb-a97d-387a-aaa7-b45b71081872 | 1.01023 | -52.2157 | 2024-10-15 04:46:00 | NOAA-20 | PEDRA BRANCA DO AMAPARI | AMAPÁ | Brasil | 1600154 | 16 | 33 | nan | nan | nan | Amazônia | 23.0 |
| 1388a7f3-fac7-3e8b-8a90-35e9246c7f87 | 1.00865 | -52.21939 | 2024-10-15 04:46:00 | NOAA-20 | PEDRA BRANCA DO AMAPARI | AMAPÁ | Brasil | 1600154 | 16 | 33 | nan | nan | nan | Amazônia | 60.8 |
| 3b41ea69-a2a8-360a-bc70-e68784ace9e1 | 1.00809 | -52.21585 | 2024-10-15 04:46:00 | NOAA-20 | PEDRA BRANCA DO AMAPARI | AMAPÁ | Brasil | 1600154 | 16 | 33 | nan | nan | nan | Amazônia | 22.6 |
| d79cfd7f-bcf6-3c37-9527-be3e714ef48b | 0.71047 | -51.42701 | 2024-10-15 04:46:00 | NOAA-20 | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 399db831-cf62-3681-9641-83a9d848b78f | -1.96867 | -52.90515 | 2024-10-15 04:46:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4c17ca0f-3125-3e40-8e2e-4c571e6a00c5 | -1.84707 | -52.51442 | 2024-10-15 04:46:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 417e155c-0c64-3771-8d93-eccb3d0bf660 | -1.71155 | -52.51186 | 2024-10-15 04:46:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| cf0fc76b-1c52-3b3b-8000-a21bf135e155 | -1.70987 | -52.50085 | 2024-10-15 04:46:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 40d6af67-5a5c-379c-bbdc-84708420185a | -1.70876 | -52.50784 | 2024-10-15 04:46:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1d091241-2cab-34c2-a7a4-7175dac30dfd | -1.70821 | -52.51134 | 2024-10-15 04:46:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c9fb873a-228e-3a63-b9a7-982f6719c5a2 | -1.70599 | -52.50383 | 2024-10-15 04:46:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 07a0b7f5-23eb-3cac-8618-ef670d01356b | -1.64943 | -53.28035 | 2024-10-15 04:46:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ed5e5710-a019-38fe-a71f-883d284060f5 | -1.44779 | -52.28798 | 2024-10-15 04:46:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 6a295dde-fb9b-3578-955f-d396006159bb | -1.39729 | -53.10344 | 2024-10-15 04:46:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1db339fb-14f3-3e0e-85b2-dfda256fd467 | -1.39671 | -53.10706 | 2024-10-15 04:46:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8c1377a4-ec68-37f6-b6cc-316b567edec6 | -1.20557 | -52.94072 | 2024-10-15 04:46:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3673926f-6060-3552-a917-3bb714753bb3 | -1.20219 | -52.94019 | 2024-10-15 04:46:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c4e090b3-d843-3884-9c3c-5b8be36c18f1 | -1.20163 | -52.94377 | 2024-10-15 04:46:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 07d62db4-e7ca-32f9-b9c1-1e6d68d0b6d4 | -2.32458 | -52.95681 | 2024-10-15 04:46:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0ad0f4a0-7ce5-3e96-8a5a-1b30abd06c2f | -2.32402 | -52.96035 | 2024-10-15 04:46:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8dbcc4a9-04bb-3f77-a129-d4800ac84da7 | -1.5971 | -53.34721 | 2024-10-15 04:46:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d73c7b38-b1a3-3b49-9539-2e8a35cddcf5 | -1.59653 | -53.35088 | 2024-10-15 04:46:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 223ecb87-3960-340e-ae02-61fc8d7ae3fd | -1.82123 | -53.41516 | 2024-10-15 04:46:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |


[Clique aqui para ver as próximas entradas](README55.md)
