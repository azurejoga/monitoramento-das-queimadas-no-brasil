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

## Dados Diários - Página 15

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7f82becf-27f0-35a8-98c2-549fb98d1297 | -3.9854 | -48.1708 | 2024-11-09 02:10:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 93.6 |
| ac8e3160-f697-381e-8343-f9c128acbf0d | -4.2487 | -47.5511 | 2024-11-09 02:10:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 55.4 |
| 2faab445-3e56-3d42-84bf-a74c3d0bbce1 | -5.4699 | -43.6603 | 2024-11-09 02:10:00 | GOES-16 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 74.0 |
| d83d54fe-a361-3901-b491-1cfb7461013e | -3.5819 | -47.3403 | 2024-11-09 02:10:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 278.0 |
| 1c7f2cfc-9115-392e-9c63-643663755319 | -3.967 | -48.15 | 2024-11-09 02:10:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 54.3 |
| a045d67c-e46b-37c2-a340-1991258147d3 | -3.6005 | -47.3177 | 2024-11-09 02:10:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 63.2 |
| e32db841-13e1-3c07-b086-51cb61757515 | -3.0865 | -50.5625 | 2024-11-09 02:10:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 66.3 |
| 8500f1ac-7965-3afa-85e8-7e1deddfce89 | -12.41835 | -64.14287 | 2024-11-09 02:15:00 | TERRA_M-M | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 23bbcd23-7854-3b48-9ad9-b8ddcf6e3f84 | -3.6005 | -47.3177 | 2024-11-09 02:20:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 59.6 |
| e7b29c6a-dc52-30d5-a519-3d1a32f43794 | -2.2295 | -53.7631 | 2024-11-09 02:20:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 64.9 |
| 4bb4e5fd-d82c-32b7-a589-f0f6a2b98321 | -2.2295 | -53.7832 | 2024-11-09 02:20:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 65.5 |
| 3b235887-c2db-3cf9-b8e2-89fbf129740e | -3.6003 | -47.3614 | 2024-11-09 02:20:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 374.9 |
| cf9f0b95-9517-3f55-a4ff-a9543cd2b28b | -3.0865 | -50.5625 | 2024-11-09 02:20:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 61.3 |
| 1c71e931-d227-338f-930b-34ca2593cdf1 | -3.5462 | -43.5663 | 2024-11-09 02:20:00 | GOES-16 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 62.8 |
| a8e6c9fb-77be-3668-82e4-c2618b6b742e | -3.1511 | -52.9731 | 2024-11-09 02:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 209.8 |
| df6d9b2c-44c9-3876-8de1-6bb451c6bac5 | -3.6004 | -47.3395 | 2024-11-09 02:20:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 498.3 |
| bb738e63-2e76-3679-b26d-655fcf4c3fe7 | -4.2486 | -47.5729 | 2024-11-09 02:20:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 251.9 |
| 9e4ec991-ccf3-3fd6-94ac-281224eb8daa | -3.9854 | -48.1708 | 2024-11-09 02:20:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 102.5 |
| e387c4c6-c026-3192-840c-2e19358aabd0 | -1.5164 | -52.1696 | 2024-11-09 02:20:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 71.0 |
| 4bb96d4e-ab7c-306d-b66b-dcb9066737a1 | -2.6764 | -51.8189 | 2024-11-09 02:20:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 56.7 |
| fa55e270-def2-34ba-bee3-2272b411817b | -3.5818 | -47.3621 | 2024-11-09 02:20:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 158.7 |
| a41285e4-0475-342e-a25e-fc56e7939759 | -3.1327 | -52.9736 | 2024-11-09 02:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 109.6 |
| 97e18e93-d6eb-3f1e-b2e7-6dde945fbfe1 | -3.9669 | -48.1716 | 2024-11-09 02:20:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 202.8 |
| 73d75b60-b139-31dd-9eff-ddc465df2c33 | -3.9853 | -48.1924 | 2024-11-09 02:20:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 87.0 |
| 8cce1c45-6323-3caf-9b3d-4a8ee1eac882 | -2.2382 | -50.5217 | 2024-11-09 02:20:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 49.0 |
| 346f3b38-2b4e-3db2-92db-aa4ed4ab28eb | -12.0122 | -44.1466 | 2024-11-09 02:20:00 | GOES-16 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 55.9 |
| db649a72-2217-3396-85ef-512c87bb892d | -3.151 | -52.9934 | 2024-11-09 02:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 73.5 |
| 7a0e392f-2c3b-3eb6-810b-1332ae386199 | -3.967 | -48.15 | 2024-11-09 02:20:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 53.5 |
| cb6012a8-5167-3665-8c5f-b5c6c90ea58e | -3.5649 | -43.5654 | 2024-11-09 02:20:00 | GOES-16 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 55.0 |
| c0873d19-f91c-3e5d-ba4b-d0e5dc7cd915 | -4.2671 | -47.572 | 2024-11-09 02:20:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 64.9 |
| adcec20a-c355-3153-8671-227630a42d23 | -1.1467 | -53.6573 | 2024-11-09 02:20:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 49.7 |
| 7901d319-e2cc-3964-bd4c-798ba4433ac8 | -3.9483 | -48.1724 | 2024-11-09 02:20:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 61.3 |
| b3efc371-afdc-3903-8e00-f557fbd90dd3 | -4.2484 | -47.5947 | 2024-11-09 02:20:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 84.5 |
| 1805dc6b-ad12-3261-944a-0026009adb49 | -3.9668 | -48.1932 | 2024-11-09 02:20:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 125.0 |
| b7898e42-27a8-3101-8b8b-1e4115d7cd93 | -4.2058 | -48.5491 | 2024-11-09 02:20:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 77.7 |
| 597dd867-0ed9-3d1c-93a2-1f7d8d8a56f3 | -3.0947 | -53.3196 | 2024-11-09 02:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 56.0 |
| 89d67fb0-ebdb-3527-a6a9-3f5aa81c5005 | -2.2479 | -53.7627 | 2024-11-09 02:20:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 59.5 |
| 894135db-33af-30ac-8ba8-d8fe42576a43 | -2.2479 | -53.7829 | 2024-11-09 02:20:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 71.1 |
| 7ddfa04b-93b2-37bd-92d0-f278b927c854 | -3.068 | -50.5631 | 2024-11-09 02:20:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 55.0 |
| 837c8d2e-434a-3243-bcdb-2f6a40029ba9 | -5.4699 | -43.6603 | 2024-11-09 02:20:00 | GOES-16 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 60.9 |
| e3766117-2489-35ab-8178-b1e027af83de | -3.5819 | -47.3403 | 2024-11-09 02:20:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 222.3 |
| 4fadaa0b-83f0-360a-beb1-14bda6ff9315 | -1.5163 | -52.1901 | 2024-11-09 02:20:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 66.6 |
| 82c00687-17d7-3fd9-8401-aeab629b3f05 | -4.2033 | -45.8538 | 2024-11-09 02:20:00 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 72.5 |
| e1faa734-f758-3535-811f-35fc513dc243 | -1.5163 | -52.1901 | 2024-11-09 02:30:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 70.6 |
| f2c20424-a301-3ece-84df-639ce28e5f41 | -3.6003 | -47.3614 | 2024-11-09 02:30:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 330.3 |
| 39526718-286a-3497-92f3-521f5fe2fa51 | -3.9854 | -48.1708 | 2024-11-09 02:30:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 84.3 |
| 24e60b63-2b76-352d-871e-9dbc204c3f90 | -1.5164 | -52.1696 | 2024-11-09 02:30:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 64.0 |
| 96e2655f-cc1a-3150-a985-39a0408468fa | -3.1327 | -52.9736 | 2024-11-09 02:30:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 116.5 |
| e92766bd-acec-3c2e-b1f3-7c361f04751a | -4.2671 | -47.572 | 2024-11-09 02:30:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 63.2 |
| d98007c3-474d-3338-a67d-ecbd9473cd2c | -3.9669 | -48.1716 | 2024-11-09 02:30:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 243.3 |
| 93a4bdf8-e3d1-3b75-ba01-8cfbcc89b7b7 | -4.2058 | -48.5491 | 2024-11-09 02:30:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 92.2 |
| e73146a8-e5a0-39a0-a9da-c64fa828a6f7 | -2.2479 | -53.7829 | 2024-11-09 02:30:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 70.6 |
| b48fb6af-d87a-340c-9d05-39432f25b903 | -2.4104 | -48.5265 | 2024-11-09 02:30:00 | GOES-16 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 61.4 |
| 38109da1-6e19-37bd-9de4-bb156dd97d84 | -3.9668 | -48.1932 | 2024-11-09 02:30:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 181.1 |
| 4cbef126-a721-3567-91e4-f1848d4f07de | -3.5462 | -43.5663 | 2024-11-09 02:30:00 | GOES-16 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 61.9 |
| 89eb3618-72e7-3a0e-80b2-f8a55b7ece5e | -2.2382 | -50.5217 | 2024-11-09 02:30:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 49.9 |
| e76384d5-76be-3202-a7f2-55bd68d7e9a0 | -3.9853 | -48.1924 | 2024-11-09 02:30:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 68.0 |
| c7d41974-998e-32c4-a71e-ac26ea61bb65 | -3.0865 | -50.5625 | 2024-11-09 02:30:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 89.1 |
| b1b5be47-5924-346c-be04-bde84f4d49b9 | -2.2479 | -53.7627 | 2024-11-09 02:30:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 59.6 |
| 42353534-2924-38c7-ac2e-af4776a7900e | -4.2484 | -47.5947 | 2024-11-09 02:30:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 63.3 |
| c6cd1b5e-1a54-32e7-ae3f-7867a5d08ff9 | -3.6004 | -47.3395 | 2024-11-09 02:30:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 461.7 |
| fc70ca41-7697-3a11-92bd-a963aece0294 | -4.2486 | -47.5729 | 2024-11-09 02:30:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 228.0 |
| 5f54c71d-925f-3b1d-b5c4-a382dfe46a79 | -2.2295 | -53.7832 | 2024-11-09 02:30:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 68.3 |
| 24141ff3-60a6-33cf-bfde-dad33a70bc15 | -4.23 | -47.5738 | 2024-11-09 02:30:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 50.9 |
| 7a037872-9de7-377f-a735-9ad533031ce0 | -4.2033 | -45.8538 | 2024-11-09 02:30:00 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 62.9 |
| 89413bb8-2f1f-31c5-8b0a-536485c0d3a4 | -3.5819 | -47.3403 | 2024-11-09 02:30:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 232.5 |
| a4df06c4-7d68-3cf7-a328-db982c707812 | -2.2295 | -53.7631 | 2024-11-09 02:30:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 57.1 |
| c78ecdb6-5833-3e89-8f18-2e3b2771d08c | -2.379 | -46.8552 | 2024-11-09 02:30:00 | GOES-16 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 42.8 |
| 73e1ee3d-e2e9-38ff-a379-ad9268303b9e | -3.1511 | -52.9731 | 2024-11-09 02:30:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 148.6 |
| b31f3fd7-f890-34a4-9a71-2e0e6dfa89a2 | -3.5818 | -47.3621 | 2024-11-09 02:30:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 173.1 |
| 337de392-dd18-3a8c-b97e-c45698aa5a43 | -4.2487 | -47.5511 | 2024-11-09 02:30:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 51.6 |
| 36368f8f-8100-3820-82d2-ff7d109131bc | -3.9668 | -48.1932 | 2024-11-09 02:40:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 163.8 |
| 863bdb40-a318-3a9f-b09f-96640bf40497 | -4.2484 | -47.5947 | 2024-11-09 02:40:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 61.0 |
| 87d9d01e-fe78-368c-a398-0bb260c2b047 | -1.5164 | -52.1696 | 2024-11-09 02:40:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 72.9 |
| 2130bf81-bba9-33cb-841c-869ada9a9b36 | -3.9669 | -48.1716 | 2024-11-09 02:40:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 253.0 |
| dad7f39b-8c3f-3feb-b53c-06b35f408305 | -4.2032 | -45.8762 | 2024-11-09 02:40:00 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 59.6 |
| 7d2ca1be-3934-339e-b827-ed648ef73500 | -2.2295 | -53.7832 | 2024-11-09 02:40:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 67.1 |
| cadfa5da-91f5-3de8-89ea-ccb5b52600be | -12.0126 | -44.1231 | 2024-11-09 02:40:00 | GOES-16 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 53.6 |
| 139d35de-eb80-3ed5-97f0-e6cfe62ce0f2 | -3.151 | -52.9934 | 2024-11-09 02:40:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 65.2 |
| 2b1b371e-99ba-3e26-ba12-1612686816ff | -3.967 | -48.15 | 2024-11-09 02:40:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 48.5 |
| 7ccbf7ef-4902-33a4-88e2-8586f2e34d97 | -3.619 | -47.3388 | 2024-11-09 02:40:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 64.3 |
| cc3b3206-cc50-3cb4-8d38-4683bd2a6193 | -3.5462 | -43.5663 | 2024-11-09 02:40:00 | GOES-16 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 63.1 |
| 0523ab17-1cad-3f75-b375-43f1ef22ef8f | -3.6189 | -47.3606 | 2024-11-09 02:40:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 54.8 |
| cd8e1b6d-a156-3700-bcb4-1300ffc0359e | -4.2671 | -47.572 | 2024-11-09 02:40:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 115.1 |
| 7063262a-2634-3328-85c8-ac86c80a0506 | -3.1327 | -52.9736 | 2024-11-09 02:40:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 67.1 |
| 7c337975-73c9-3e7b-9a09-8aab749b3cf8 | -1.5163 | -52.1901 | 2024-11-09 02:40:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 59.9 |
| 30cde878-c1ea-3d72-9b58-b275b1b2e727 | -3.5818 | -47.3621 | 2024-11-09 02:40:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 170.1 |
| 4f059b3c-5236-346b-bb5e-28e0adf8851e | -4.2486 | -47.5729 | 2024-11-09 02:40:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 176.3 |
| 24cba941-7577-32e1-ba28-d2465c2baff7 | -4.2058 | -48.5491 | 2024-11-09 02:40:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 50.2 |
| fecff947-47b5-30b0-9e81-b1bd95b58032 | -2.2295 | -53.7631 | 2024-11-09 02:40:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 66.7 |
| f262fb82-97d2-3e53-8fb0-e6f8ea4d39a2 | -4.2033 | -45.8538 | 2024-11-09 02:40:00 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 77.6 |
| 56752dd1-be64-3243-a9ba-782007897526 | -3.1511 | -52.9731 | 2024-11-09 02:40:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 187.1 |
| 6735e190-a292-3c98-85d2-1b46570c6102 | -2.4104 | -48.5265 | 2024-11-09 02:40:00 | GOES-16 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 59.3 |
| 60215453-3ed5-30a5-8108-56cb7ee69fd3 | -3.9854 | -48.1708 | 2024-11-09 02:40:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 83.8 |
| 60cacac9-5c08-3553-a076-a41d930e3799 | -3.6004 | -47.3395 | 2024-11-09 02:40:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 335.1 |
| c55096b1-f048-3bc1-b5cc-3d4d8d0a920c | -3.5819 | -47.3403 | 2024-11-09 02:40:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 245.8 |
| 87e9bd7e-7b61-3f43-b889-0e32c8f34e7a | -12.0122 | -44.1466 | 2024-11-09 02:40:00 | GOES-16 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 70.7 |
| 23aae440-dfe6-37ca-9138-0c9a7dc679b3 | -3.9853 | -48.1924 | 2024-11-09 02:40:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 74.3 |
| 5cdac95b-ad4d-3eb1-8837-8714d3bb31b6 | -2.6764 | -51.8189 | 2024-11-09 02:40:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 55.3 |
| ba0027db-d536-348a-9b0a-5a98d05f04d4 | -3.6003 | -47.3614 | 2024-11-09 02:40:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 250.4 |


[Clique aqui para ver as próximas entradas](README16.md)
