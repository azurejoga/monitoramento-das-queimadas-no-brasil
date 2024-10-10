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

## Dados Diários - Página 89

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 64a90fec-5865-3e9d-bcab-c11c35209725 | -3.58497 | -49.92238 | 2024-10-10 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bac9cad5-fdb4-37fb-b6a4-b75aa470f52b | -3.58166 | -49.92187 | 2024-10-10 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| d10f4f36-a7c0-3b0a-a503-1cc93495c21d | -3.53763 | -49.18417 | 2024-10-10 04:42:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a7a5b8a4-768e-34ac-926b-9858a42409ed | -3.5083 | -50.38958 | 2024-10-10 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cce5ed7f-0fd0-3376-af04-0cd0342a53f9 | -3.50776 | -50.39302 | 2024-10-10 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e5540f8a-987b-3cdd-bc5e-50eba192c5ff | -3.50245 | -50.27605 | 2024-10-10 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 83fb06e6-4ded-3963-addb-db4ce8120ab1 | -3.49914 | -50.27554 | 2024-10-10 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 13212970-2c15-3d78-8b12-5b0281dd27c4 | -3.46372 | -49.69851 | 2024-10-10 04:42:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0ab0ad1f-3de3-3b44-a89b-0f52af4809ff | -3.43182 | -50.14178 | 2024-10-10 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 038c1ef1-1fbb-340e-9b79-d7bfddda2455 | -3.40876 | -50.33177 | 2024-10-10 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| aca81d22-7673-3e78-91f6-605e7b248e6a | -3.40546 | -50.33125 | 2024-10-10 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b463f81f-304d-3e12-83e7-08a033830b19 | -3.40216 | -50.33074 | 2024-10-10 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| e2fc0d9d-8bab-3844-8f6d-6af81bb98808 | -2.77781 | -49.24301 | 2024-10-10 04:42:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 58a65901-c039-3b78-ac79-43f0b383a7db | -2.77727 | -49.24651 | 2024-10-10 04:42:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| a185e70f-b912-3144-98b1-422b8ef63fb0 | -2.77448 | -49.2425 | 2024-10-10 04:42:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 43626daf-be74-33cc-a92a-f1182b087946 | -2.77394 | -49.24599 | 2024-10-10 04:42:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 31923b37-4a6f-3432-84e1-6111c6c7c228 | -2.7717 | -49.23849 | 2024-10-10 04:42:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d76c4d0f-1b83-3b80-a558-bd487b512443 | -2.77115 | -49.24198 | 2024-10-10 04:42:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0189d504-e6a2-306e-bcfd-01d696c431a6 | -2.77061 | -49.24548 | 2024-10-10 04:42:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3ebcb30e-aff0-3e89-a9bd-465a6d5049ab | -2.76837 | -49.23798 | 2024-10-10 04:42:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 7325bc91-5cbe-3b69-ab8e-99877098deb0 | -2.76782 | -49.24147 | 2024-10-10 04:42:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7d0f56d5-f6d8-3749-aed7-0163a1eb1995 | -2.71207 | -49.13969 | 2024-10-10 04:42:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a9e6ec98-9196-3fd7-998d-e3cc6d72022a | -2.70928 | -49.13567 | 2024-10-10 04:42:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 182ac637-fe37-39cf-b52d-15ab45f307f3 | -2.70873 | -49.13918 | 2024-10-10 04:42:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f5b2b4d3-f139-3c53-86ae-5a1fd1257f0e | -2.62399 | -49.24753 | 2024-10-10 04:42:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| afe273a8-2cce-3536-ab80-74ec12a8e20f | -2.62247 | -49.08247 | 2024-10-10 04:42:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 90183c39-1150-35f0-807d-37c2a3f2e846 | -2.62066 | -49.24702 | 2024-10-10 04:42:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ecc55292-3b0a-327c-aa7c-496a77535808 | -2.57971 | -49.26925 | 2024-10-10 04:42:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5b33f77b-0dfa-366b-9fbb-908fca37e973 | -2.53356 | -49.02206 | 2024-10-10 04:42:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1714b3ad-3754-3e49-be17-33ccb5d3d19d | -2.53301 | -49.02558 | 2024-10-10 04:42:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ae568e4e-fdb3-3d7d-b516-313657983838 | -2.5044 | -49.14325 | 2024-10-10 04:42:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| aaa8860d-6d07-3b57-a1d6-b05e9041e679 | -2.50107 | -49.14274 | 2024-10-10 04:42:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 22be1192-27c4-3100-93cf-85e20ffbc558 | -2.50053 | -49.14624 | 2024-10-10 04:42:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 53df4577-e060-3280-8240-573761b4939d | -2.49374 | -49.10218 | 2024-10-10 04:42:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d13c8405-dcf5-3884-b32f-00637853455b | -2.48486 | -49.29026 | 2024-10-10 04:42:00 | NOAA-20 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2a1dedb6-8974-3408-bf4c-c29c4033fffc | -2.48154 | -49.28975 | 2024-10-10 04:42:00 | NOAA-20 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 46f25aa5-b948-360c-a500-ede4b2530028 | -2.42659 | -48.94462 | 2024-10-10 04:42:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1805495d-2a3f-3e5b-9f6c-ff64f07285d2 | -2.39765 | -48.95459 | 2024-10-10 04:42:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c35d4e0a-b770-3a62-b869-7b6165be1c62 | -2.3891 | -49.07558 | 2024-10-10 04:42:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d08f4fe7-cc32-3337-b078-9afcf660fde0 | -2.35408 | -48.99836 | 2024-10-10 04:42:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 19fafc87-ceff-3ec7-88d6-e796d83255dd | -2.35074 | -48.99784 | 2024-10-10 04:42:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 094c8e58-d288-3139-8071-ac2ce3f65020 | -3.37715 | -49.49307 | 2024-10-10 04:42:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3812d658-1f9f-38d9-8a8c-bb048216a87f | -3.37661 | -49.49656 | 2024-10-10 04:42:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b7dada9b-1d18-343c-9bc7-676ed2080a9f | -3.37606 | -49.50003 | 2024-10-10 04:42:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 32c29599-aa31-3455-9abc-90dffe637b3d | -3.37383 | -49.49257 | 2024-10-10 04:42:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 444084d1-8680-3d45-bab3-61d038ad8553 | -3.33153 | -49.15586 | 2024-10-10 04:42:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b274f3c7-da6b-3f36-9a49-7769c9acdfbd | -3.32985 | -49.14477 | 2024-10-10 04:42:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f9a9da93-6467-3fd5-a18b-bb01058419ba | -3.3293 | -49.1483 | 2024-10-10 04:42:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 629fe111-5561-3905-b329-e34039256057 | -3.32874 | -49.15182 | 2024-10-10 04:42:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 08ab3ff3-109d-3358-8be0-e85f06a9895e | -3.32819 | -49.15535 | 2024-10-10 04:42:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| e5fd86a8-a76f-3dd7-84aa-2e7c46beb898 | -3.32706 | -49.14073 | 2024-10-10 04:42:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d25ef31e-0e59-3181-9e22-20f92d0e0281 | -3.3265 | -49.14426 | 2024-10-10 04:42:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 638fce1a-eee6-3eba-a179-d58197d4a210 | -3.30862 | -49.10531 | 2024-10-10 04:42:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 296e787f-53fc-346c-ad45-1b94afcbf99a | -3.28798 | -49.10578 | 2024-10-10 04:42:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 59ce45ba-c0ef-34bf-a9d9-f38a2565893e | -3.28518 | -49.10173 | 2024-10-10 04:42:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5b7fd7fe-9e15-3e39-8aa8-c1882d202327 | -3.28239 | -49.09768 | 2024-10-10 04:42:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2700d70e-b887-3874-8ea6-77f85319c077 | -3.28184 | -49.10122 | 2024-10-10 04:42:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 15d5b7b4-b284-3f33-94f3-af18209ad5cf | -3.27904 | -49.09717 | 2024-10-10 04:42:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 77753149-add8-3927-9af5-a0c30633aca6 | -3.27849 | -49.10071 | 2024-10-10 04:42:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f2b1827e-da68-314d-a25b-b1d00e626b6c | -3.27514 | -49.10019 | 2024-10-10 04:42:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7661b1be-50a5-3acc-afdf-b6f668e97028 | -3.2718 | -49.09967 | 2024-10-10 04:42:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6a7d7a0d-21cd-3339-bbc8-63e0e36e04c4 | -3.27125 | -49.10321 | 2024-10-10 04:42:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c79ba9b7-e86f-3534-81fe-425c8d12483c | -3.26845 | -49.09916 | 2024-10-10 04:42:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4b6b8cac-f274-3542-ae88-786e49b979eb | -3.2679 | -49.10269 | 2024-10-10 04:42:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 1abb253d-38d9-327e-8f01-0f16ea34a82f | -3.26455 | -49.10217 | 2024-10-10 04:42:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a36c89f2-cc72-3c73-beb0-127490888329 | -3.26401 | -49.1057 | 2024-10-10 04:42:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 2bb7b751-715b-3bd9-9c4c-048b64c4baac | -3.26346 | -49.10923 | 2024-10-10 04:42:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7b517505-4b79-3386-8556-5d0d1dde0161 | -3.26176 | -49.09811 | 2024-10-10 04:42:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0a808b92-e022-319c-a6c8-37ee266c938d | -3.26121 | -49.10165 | 2024-10-10 04:42:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e74ac0fb-3266-30c0-8094-48fe2b83389e | -3.26066 | -49.10518 | 2024-10-10 04:42:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e16facde-304e-3df3-89f1-1a04982ae49e | -3.25731 | -49.10466 | 2024-10-10 04:42:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c8b7b5bd-73e0-328b-ab26-5bf6a018bcee | -3.24077 | -49.5606 | 2024-10-10 04:42:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| a7a7936c-9033-335a-bcc5-e6655e63b506 | -3.14154 | -49.60911 | 2024-10-10 04:42:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 22f6ecbc-d333-3c49-8015-eae2665e9962 | -3.13773 | -49.21965 | 2024-10-10 04:42:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 018ac295-540c-3aa3-8095-7613b546ca6e | -3.13154 | -49.19353 | 2024-10-10 04:42:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 647be974-69fc-3b73-886e-64207fe57327 | -2.7506 | -49.52365 | 2024-10-10 04:42:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ae6725e9-5608-393d-9973-376bb644cc2e | -2.74952 | -49.53057 | 2024-10-10 04:42:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bb0db4d1-df1a-3480-babd-cfc3c6b72712 | -2.74898 | -49.53403 | 2024-10-10 04:42:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 796dd2ed-27eb-3efd-ba58-60a5a146b83c | -2.74729 | -49.52314 | 2024-10-10 04:42:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8bcf6b49-8dfc-3172-abea-52f91a65b77b | -2.73715 | -49.95576 | 2024-10-10 04:42:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 2301dc5b-15fa-3caa-92a8-257590483314 | -2.73182 | -49.83875 | 2024-10-10 04:42:00 | NOAA-20 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8130a431-c649-3b97-95f3-01f9c5620334 | -2.72474 | -49.53732 | 2024-10-10 04:42:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 64d86306-d798-3a1e-8821-a6b20aecfd2e | -2.72311 | -49.5477 | 2024-10-10 04:42:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8995e9f1-d740-30ed-aa4d-0911b385543d | -2.60642 | -49.79453 | 2024-10-10 04:42:00 | NOAA-20 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1c3e1b36-a2b0-3113-a0d4-59cbc9961c80 | -2.60365 | -49.79058 | 2024-10-10 04:42:00 | NOAA-20 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 445dda21-bebc-3db2-baa7-177e4491785e | -2.60311 | -49.79402 | 2024-10-10 04:42:00 | NOAA-20 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7a499b58-01e7-3cbd-aa6b-4e6a8bcf7142 | -2.60258 | -49.79746 | 2024-10-10 04:42:00 | NOAA-20 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 564c89f8-b922-3e1d-bee7-e9d4fc9fd3f2 | -2.59981 | -49.79351 | 2024-10-10 04:42:00 | NOAA-20 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c5a1d3ab-b0d1-3d1c-b843-0a317692e3d8 | -2.59927 | -49.79695 | 2024-10-10 04:42:00 | NOAA-20 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 277935fc-573e-324c-b731-78a474c463a7 | -2.57089 | -49.45642 | 2024-10-10 04:42:00 | NOAA-20 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 284cb525-3ab0-310f-a41c-e35f235a42e9 | -2.47429 | -50.24492 | 2024-10-10 04:42:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 2152927e-2130-3279-91a8-c128c13276a5 | -2.47375 | -50.24835 | 2024-10-10 04:42:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e01fb7e9-dd37-3534-be32-1ab852fc6b50 | -2.47321 | -50.25179 | 2024-10-10 04:42:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b9e30bec-2372-3d57-9efe-7f1ed3c5dff6 | -2.47152 | -50.24097 | 2024-10-10 04:42:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 6bdc40ee-10bc-370c-af70-1111acd80ed4 | -2.47098 | -50.2444 | 2024-10-10 04:42:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| b1f14905-a05d-3212-8190-59cfb93284b9 | -2.47044 | -50.24784 | 2024-10-10 04:42:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cf92c952-96be-320a-b752-01f8ab0fe8cb | -2.46043 | -49.61979 | 2024-10-10 04:42:00 | NOAA-20 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 75915079-82a4-3259-85bb-1729ed1d3f5f | -2.43227 | -49.60483 | 2024-10-10 04:42:00 | NOAA-20 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| d0061da0-6958-36ea-819d-800bbca0995d | -3.34156 | -50.13149 | 2024-10-10 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 99560c8e-e54e-3fce-9a35-1e5a87120e67 | -3.33933 | -50.1241 | 2024-10-10 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |


[Clique aqui para ver as próximas entradas](README90.md)
