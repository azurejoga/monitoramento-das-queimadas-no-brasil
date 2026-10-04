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

## Dados Diários - Página 13

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 16cee60e-0a05-3c89-8173-15835fe1ed32 | -2.81097 | -54.10423 | 2026-10-04 00:37:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 100.7 |
| 7939340f-aaa6-3222-9924-e73d6bdc2185 | -10.99492 | -59.14677 | 2026-10-04 00:37:00 | TERRA_M-M | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 16.5 |
| ed306d7e-5476-38dc-a805-3642dbacb20b | -5.51375 | -56.06487 | 2026-10-04 00:37:00 | TERRA_M-M | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 9e58bbaa-0e75-33f1-81dc-1c73b9e1c9f7 | -3.47735 | -55.43258 | 2026-10-04 00:37:00 | TERRA_M-M | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 515e453f-02cd-3eb2-8d67-4268ecb85939 | -3.61377 | -55.51464 | 2026-10-04 00:37:00 | TERRA_M-M | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 73760aff-f64f-31e1-9a65-997a89ac0832 | -10.83023 | -57.20709 | 2026-10-04 00:37:00 | TERRA_M-M | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| bf100955-be9c-3ff5-96ef-ace2d84e801c | -4.28268 | -50.26665 | 2026-10-04 00:37:00 | TERRA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 195.2 |
| 9af13492-11dd-3ee0-9ff9-7628037810fe | -5.87322 | -55.7179 | 2026-10-04 00:37:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 6c0b1783-571f-3952-aea6-e917e19a8a06 | -2.82551 | -54.11959 | 2026-10-04 00:37:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 70.8 |
| f12884c3-ca7d-3a05-bf48-4a1be09bea1f | -9.90287 | -65.02411 | 2026-10-04 00:37:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 16.4 |
| 2360a589-f39e-3f41-820a-a5b265617b6b | -3.50753 | -54.60991 | 2026-10-04 00:37:00 | TERRA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 56.0 |
| f0303e30-0a52-3cc0-9835-77499ca9b8f6 | -3.51673 | -54.60184 | 2026-10-04 00:37:00 | TERRA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 14.0 |
| 59e043dc-4e8d-338f-b3c9-1cd761457a48 | -6.07774 | -53.48377 | 2026-10-04 00:37:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 30.1 |
| c4a402f6-02ad-39d9-84ae-3a6d0dc128be | -8.34105 | -62.8313 | 2026-10-04 00:37:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 14.7 |
| b50f9edc-2d7b-3dda-831f-da1dd53e59fb | -9.3649 | -60.30821 | 2026-10-04 00:37:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 13.6 |
| bd9503bf-a8f1-3ce7-89eb-186782ba04b4 | -5.89027 | -57.66971 | 2026-10-04 00:37:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 5b2cc99a-cd35-3c36-b80f-171d86e0c38f | -2.81823 | -54.10873 | 2026-10-04 00:37:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 94.2 |
| 6fdf9a9a-76eb-35af-8f29-5f34db5d7445 | -3.12003 | -53.7095 | 2026-10-04 00:37:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 33.8 |
| ad895af1-ef1a-3f0b-8976-81c4439c3375 | -8.876 | -66.76334 | 2026-10-04 00:37:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 18.1 |
| 46bb6bf2-184f-3404-86d3-733666dbae38 | -9.09114 | -61.16435 | 2026-10-04 00:37:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 50.2 |
| fa039ea0-e782-34f0-9928-1d5086eca70d | -3.18934 | -54.09365 | 2026-10-04 00:37:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 64.2 |
| 43dc66f8-af0f-360b-b8bd-ff77421f5f84 | -4.11483 | -53.62987 | 2026-10-04 00:37:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 12.0 |
| 0bab6259-8c68-3405-b055-31605baab134 | -3.12543 | -53.74578 | 2026-10-04 00:37:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 41.1 |
| eb61c82e-1037-3fca-a7a6-36dadf55ea9b | -2.816 | -54.13829 | 2026-10-04 00:37:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 73.8 |
| a06cf2a8-0a5a-3719-b682-b9ec1326d6d6 | -5.86315 | -55.71942 | 2026-10-04 00:37:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 14.2 |
| 66aad3cf-7896-35d5-830f-0edf6756b495 | -2.90771 | -54.13593 | 2026-10-04 00:37:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 24.3 |
| 7328b6ae-87b1-39ed-8288-c7566849b7d8 | -3.12019 | -53.73394 | 2026-10-04 00:37:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 198.7 |
| f4a361b8-cc7e-3c4a-877b-66388ee4ebe2 | -2.82061 | -54.12585 | 2026-10-04 00:37:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 83.1 |
| b99fa06a-d436-37a9-8239-e780f5cfe368 | -3.05207 | -54.16099 | 2026-10-04 00:37:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 19.3 |
| 964b9478-e309-3491-b74a-2d8796c77d6f | -5.55101 | -49.76204 | 2026-10-04 00:37:00 | TERRA_M-M | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 29.5 |
| c4658fcb-f409-3d65-a927-1537742aa51d | -6.0757 | -57.81052 | 2026-10-04 00:37:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 38f1319b-d29b-300d-8244-b1e3f82494d1 | -6.44932 | -55.45622 | 2026-10-04 00:37:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 13.3 |
| 1d5815b6-57c1-3e5c-8f6e-eb0e4cd3d8e1 | -2.96514 | -54.10999 | 2026-10-04 00:37:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 13.9 |
| e6f457d2-5cf7-36f8-aa99-f8f45853bcad | -8.34611 | -62.83809 | 2026-10-04 00:37:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 35.1 |
| ef246686-36e9-37d5-91d1-37afa6d2a940 | -3.20764 | -50.76249 | 2026-10-04 00:37:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 50.3 |
| 887750a6-6348-3bbd-b1de-997dacdc6474 | -4.07458 | -59.33376 | 2026-10-04 00:37:00 | TERRA_M-M | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 10.8 |
| d7d20e67-8c6c-3409-aeec-15231de97f09 | -3.7647 | -49.57515 | 2026-10-04 00:37:00 | TERRA_M-M | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 68.8 |
| 96f74cdb-b094-3572-9ec6-1713af974cfa | -3.69645 | -50.65641 | 2026-10-04 00:37:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 36.9 |
| 53d67c94-84a5-37c5-818f-3d49c4308faa | -10.59739 | -57.58225 | 2026-10-04 00:37:00 | TERRA_M-M | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 98346ec2-4510-3e0a-98bd-37ff375d5cb3 | -8.57939 | -66.8178 | 2026-10-04 00:37:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 19.8 |
| 082b3b5a-d49d-325f-9248-6450944951ae | -4.7878 | -55.70735 | 2026-10-04 00:37:00 | TERRA_M-M | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 06123e9d-d827-3a77-99cc-4d61ebe5f8ba | -9.13634 | -65.48264 | 2026-10-04 00:37:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 13.2 |
| 4e7f7968-e19b-362f-88e0-00d754e5f0a3 | -8.71392 | -61.39454 | 2026-10-04 00:37:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 47.9 |
| 0d3193dc-54a7-39c1-91c9-035def2d7c47 | -4.71789 | -56.15513 | 2026-10-04 00:37:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 7faea01b-4d79-33f0-8254-17aeb3fd2a9b | -9.4851 | -64.69205 | 2026-10-04 00:37:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 20.7 |
| c9cf44ce-2052-380c-aad3-30d3e364cf8f | -2.82801 | -54.13663 | 2026-10-04 00:37:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 28.8 |
| 3805b7c7-859c-3b11-b98a-fa82102623f7 | -3.3064 | -53.8409 | 2026-10-04 00:37:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 42.6 |
| a3161732-1655-338c-b92a-0afdb1fbc18b | -3.11044 | -53.75391 | 2026-10-04 00:37:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 165.7 |
| db0176a5-af0c-3012-bbad-2ebb4084ad9c | -9.87943 | -65.14237 | 2026-10-04 00:37:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 13.2 |
| 2e6e3565-3ef7-3932-8dd4-6441e5472a84 | -3.31284 | -53.85238 | 2026-10-04 00:37:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 10.7 |
| e7a3a153-1105-3dd9-bd47-c9564b1e6dec | -3.73382 | -57.15043 | 2026-10-04 00:37:00 | TERRA_M-M | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 5.6 |
| b4bc4fe9-c302-37ab-8b57-cecea7979d07 | -9.1645 | -61.4057 | 2026-10-04 00:37:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 13.6 |
| 5b970b85-c6c7-3ddb-813c-ccd40160f7aa | -2.88799 | -54.12801 | 2026-10-04 00:37:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 14.9 |
| f3a87e2c-e5fd-3f01-b04a-4611d0245d90 | -3.79577 | -59.38234 | 2026-10-04 00:37:00 | TERRA_M-M | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 987de93e-279a-319d-b117-b89aa0cb3dbd | -8.23552 | -61.17232 | 2026-10-04 00:37:00 | TERRA_M-M | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 5.1 |
| cd8c9335-4195-3b28-b133-56166e5d0455 | -3.01283 | -50.47401 | 2026-10-04 00:37:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 39.8 |
| 361c4450-fa1a-3f84-8a71-df1ff729fc44 | -2.8062 | -54.11051 | 2026-10-04 00:37:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 80.6 |
| 43fc248f-4c49-3a5c-912b-839bf9aa7ac6 | -3.12275 | -53.75209 | 2026-10-04 00:37:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 55.2 |
| 33e7349e-d2f1-3cd7-b3be-acd1cc47ea5c | -9.48187 | -64.33862 | 2026-10-04 00:37:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 22.0 |
| d64ede45-9c81-3447-8a71-3083bbc1562e | -3.79456 | -59.37356 | 2026-10-04 00:37:00 | TERRA_M-M | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 0dd4b06d-0b92-3be9-8244-0bd5b3d3866c | -3.07364 | -49.56777 | 2026-10-04 00:37:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 88.3 |
| 11722c10-b9e7-3d38-98a0-8cffb37ebef3 | -2.80149 | -54.12312 | 2026-10-04 00:37:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 49.6 |
| 5abb24dd-39f8-3f4b-9cfc-109db712e34d | -2.80401 | -54.14007 | 2026-10-04 00:37:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 17.2 |
| 8bbde52a-9946-3448-89ae-1a6f82bdbefe | -3.04744 | -54.2131 | 2026-10-04 00:37:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 50.1 |
| cc4ec06a-570e-38f8-825c-3a3fe2439013 | -3.01226 | -53.88446 | 2026-10-04 00:37:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 14.7 |
| 077f841b-95a9-3398-9ce3-3bf0f829a31a | -3.12273 | -53.72768 | 2026-10-04 00:37:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 233.6 |
| 427ada72-61c7-3868-b8a6-1b1fe8cbd86e | -3.20829 | -50.73576 | 2026-10-04 00:37:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 32.1 |
| def39baa-5b20-3780-98c8-cb20febca3ae | -3.19187 | -54.11081 | 2026-10-04 00:37:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 34.5 |
| f8aa7ea3-8a16-3a4e-865d-f2517d214dcf | -2.82297 | -54.14281 | 2026-10-04 00:37:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 29.5 |
| 6ddc04ab-2dbc-3f74-b59f-e90d0d195337 | -9.91856 | -65.04381 | 2026-10-04 00:37:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 39.4 |
| b4dea433-cee5-3a19-a626-49a08b824b19 | -3.78695 | -59.38358 | 2026-10-04 00:37:00 | TERRA_M-M | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 99919f71-dcb5-31e5-a7ca-ee3e86d72e8d | -2.823 | -54.10249 | 2026-10-04 00:37:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 35.8 |
| e2a6645a-bcdb-3b3a-aa5f-04a3aaec41d4 | -3.50969 | -54.62516 | 2026-10-04 00:37:00 | TERRA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 14.0 |
| 78057756-76a1-3ab3-bbb1-3898ce3cf8dd | -3.46146 | -50.09495 | 2026-10-04 00:37:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 132.6 |
| 42075b48-3562-37df-842a-ba630be0aef4 | -2.84974 | -51.306 | 2026-10-04 00:37:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 22.5 |
| b37ecf3c-a3b9-39c2-a79f-fdb5d9a791b9 | -5.79044 | -57.81368 | 2026-10-04 00:37:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 956b71ef-c74a-3964-90aa-07d58f6d304c | -3.08245 | -49.53124 | 2026-10-04 00:37:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 46.8 |
| 407821ad-8182-3859-a4be-e932cef4b322 | -9.91605 | -65.02248 | 2026-10-04 00:37:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 33.8 |
| 0df149e7-a86f-359a-aa8b-5a50be0d6a49 | -10.22204 | -59.08603 | 2026-10-04 00:37:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 53756d74-25e4-3452-a5d1-8be8ff26b709 | -8.564 | -67.08208 | 2026-10-04 00:37:00 | TERRA_M-M | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 44.6 |
| 1bbab1f5-4bfb-37e0-910e-6e1d36a63671 | -10.18086 | -57.9652 | 2026-10-04 00:37:00 | TERRA_M-M | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 3af36281-48c2-32d9-9e80-f8d913b41185 | -9.15903 | -68.26353 | 2026-10-04 00:37:00 | TERRA_M-M | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 21.2 |
| 5f80acac-c3ae-3bbb-af0c-8e46a023c5e5 | -5.96243 | -55.34892 | 2026-10-04 00:37:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 53d141c5-466b-3ee2-a17e-7e3781a9d1e8 | -2.94363 | -54.1306 | 2026-10-04 00:37:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 42.8 |
| 9e39db48-015b-307e-8b82-99a1e5930138 | -2.59346 | -51.85261 | 2026-10-04 00:37:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 102.5 |
| 3572f964-3f9d-3e0c-aa6a-3074884eb891 | -8.57098 | -66.99783 | 2026-10-04 00:37:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 18.3 |
| 130126b8-58fa-3d22-bfb5-e411746874cc | -3.11039 | -53.72945 | 2026-10-04 00:37:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 260.6 |
| fb33fd7f-b135-3df6-990d-97982bfb847a | -3.46673 | -50.12992 | 2026-10-04 00:37:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 27.9 |
| 4c711492-7586-3d2d-a64e-54efe5461019 | -3.16978 | -54.08548 | 2026-10-04 00:37:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 19.5 |
| dc49f67a-ed3d-3289-a5d4-5e485fbbc219 | -3.8721 | -55.81402 | 2026-10-04 00:37:00 | TERRA_M-M | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 10.4 |
| ba97be87-09da-3cdc-9bbf-d3795b80aef5 | -2.97714 | -54.10833 | 2026-10-04 00:37:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 18.9 |
| 234bb12a-ec3a-378f-ba31-b7e5f4bbeaf8 | -3.29421 | -53.84267 | 2026-10-04 00:37:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 56.5 |
| 82bcabef-2369-3202-be05-bf908e563f53 | -3.13774 | -53.74395 | 2026-10-04 00:37:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 26.4 |
| 97056335-2772-31ff-9f84-907cbe49a8f2 | -3.52108 | -54.6235 | 2026-10-04 00:37:00 | TERRA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 27.1 |
| 30ad76aa-5ab0-3ab1-aedc-33ca1597f670 | -4.70795 | -56.15664 | 2026-10-04 00:37:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| a2f945ec-c498-34a9-a1a8-1d708252522a | -3.70175 | -50.66238 | 2026-10-04 00:37:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 53.0 |
| fda88327-272f-33a6-b6eb-b26c30010633 | -8.34442 | -62.82454 | 2026-10-04 00:37:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 22.0 |
| b85601b7-78cb-34d4-861f-11d21290028f | -2.98235 | -54.10192 | 2026-10-04 00:37:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 25.4 |
| 651109a5-2266-3cc4-81a3-c750f39f5ea1 | -2.89998 | -54.12625 | 2026-10-04 00:37:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 19.9 |
| a54c5fb0-8ae2-398e-9771-92e50b5ee8c9 | -9.05274 | -65.43056 | 2026-10-04 00:37:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 18.4 |


[Clique aqui para ver as próximas entradas](README14.md)
