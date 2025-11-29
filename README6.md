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

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ba1eb4ee-39fc-3d1f-a524-65ca9c780297 | -4.63854 | -49.36149 | 2025-11-29 00:34:00 | TERRA_M-M | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 7f64f7d6-8ced-30a6-8184-bd267dadeca8 | -3.52734 | -51.24152 | 2025-11-29 00:34:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| d4837f81-b959-3450-9f02-b95fd39349fa | -2.88156 | -49.11569 | 2025-11-29 00:34:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| f1607826-9aa4-3a44-b8be-34330521ff95 | -2.78619 | -47.42575 | 2025-11-29 00:34:00 | TERRA_M-M | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 47.7 |
| 20e18bd8-3ca0-39df-8aa7-72837851656d | -4.12106 | -44.9036 | 2025-11-29 00:34:00 | TERRA_M-M | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Amazônia | 46.8 |
| 68b76fb1-e924-30c4-bd6c-6bd6ac6ad33d | -3.48016 | -51.37084 | 2025-11-29 00:34:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| ab14c0ee-4a8a-3649-a7a5-86ac7823c77d | -4.06813 | -54.82098 | 2025-11-29 00:34:00 | TERRA_M-M | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| aaaab05f-c771-35e3-b744-188ab6cf2fe1 | -4.04601 | -48.87949 | 2025-11-29 00:34:00 | TERRA_M-M | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| b96a5b29-02e4-3d54-943f-0d5ab3258c07 | -3.8796 | -54.19723 | 2025-11-29 00:34:00 | TERRA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 17.6 |
| 7f04834f-25f9-309b-abbb-90bed77da1a6 | -3.28144 | -48.88653 | 2025-11-29 00:34:00 | TERRA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| a78af63e-2ba3-307a-8f36-605c2ae1ae92 | -3.3198 | -50.27771 | 2025-11-29 00:34:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 11.7 |
| 700bec5e-d36a-37e3-be68-1c029025c7ae | -3.67759 | -50.67004 | 2025-11-29 00:34:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| b33b247d-ae05-3ed0-90b1-92d8d6508ad9 | -1.48399 | -45.80124 | 2025-11-29 00:34:00 | TERRA_M-M | GODOFREDO VIANA | MARANHÃO | Brasil | 2104305 | 21 | 33 | nan | nan | nan | Amazônia | 70.2 |
| 2f7e39a3-66df-3166-8164-c043d0064c44 | -2.42884 | -50.29995 | 2025-11-29 00:34:00 | TERRA_M-M | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| c0881e1f-344a-39ed-bc2a-f7ab3b688dcd | -3.46189 | -47.64094 | 2025-11-29 00:34:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 13.4 |
| 24531fec-906d-3036-89f5-d48e570032a3 | -4.40178 | -48.92371 | 2025-11-29 00:34:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| b4dfd8df-1e67-3886-8417-f2984b4a6b46 | -3.4741 | -45.89959 | 2025-11-29 00:34:00 | TERRA_M-M | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 75ff5270-7b2e-35d5-a37b-a9251ddbf19b | -3.13779 | -49.8953 | 2025-11-29 00:34:00 | TERRA_M-M | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| d44ce1eb-5e71-366c-9411-e6e21d025636 | -2.5928 | -46.87827 | 2025-11-29 00:34:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 32b120dc-0b2c-3cf0-a74a-b3ae1510da77 | -2.7477 | -45.2737 | 2025-11-29 00:34:00 | TERRA_M-M | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 152ce690-29ea-30a8-8994-afbece493f54 | -2.77193 | -45.4748 | 2025-11-29 00:34:00 | TERRA_M-M | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 17.0 |
| 0202364f-9c8c-36db-a44d-fee797123398 | -2.92404 | -45.30817 | 2025-11-29 00:34:00 | TERRA_M-M | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 18.8 |
| 13f44d1f-d277-39d7-acb1-3a460c3d1e4a | -3.66937 | -47.29264 | 2025-11-29 00:34:00 | TERRA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 0bdb3fbd-86f5-3cad-a9e5-5596dffc584a | -1.37969 | -52.50105 | 2025-11-29 00:34:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 2179ec60-e971-36ce-b291-51a002bb0256 | -2.6366 | -48.54043 | 2025-11-29 00:34:00 | TERRA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 143.7 |
| 01bf5989-d498-35d9-9d6a-bf6b7f05abd1 | -4.54418 | -44.1282 | 2025-11-29 00:34:00 | TERRA_M-M | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 28.8 |
| f31e93c2-3b8a-3ba9-8635-5526f3ef5e48 | -3.51247 | -47.20856 | 2025-11-29 00:34:00 | TERRA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 20.6 |
| ae962369-5654-31a2-9d57-1cd1ffdae49e | -2.22593 | -47.51796 | 2025-11-29 00:34:00 | TERRA_M-M | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 40.1 |
| ae2c98ca-79a1-3d0a-b1cb-84ccceb3d10f | -2.62697 | -48.54182 | 2025-11-29 00:34:00 | TERRA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 84.1 |
| b7c2199e-d005-31b8-83ee-e48e6af3a780 | -3.32314 | -53.32111 | 2025-11-29 00:34:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 10.5 |
| d12b9900-3d23-35db-8d5e-85abbe29d27a | -4.04701 | -49.08754 | 2025-11-29 00:34:00 | TERRA_M-M | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 86f2b00f-dc6a-3e93-8bf9-1a00c55e16d7 | -2.74221 | -45.26266 | 2025-11-29 00:34:00 | TERRA_M-M | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 17.6 |
| 0a99a89c-c2c5-3076-8d0f-b17546260e57 | -4.16213 | -43.7473 | 2025-11-29 00:34:00 | TERRA_M-M | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 32.9 |
| 713c9944-34d7-3e20-a87b-b910c195c9e4 | -4.0154 | -49.11802 | 2025-11-29 00:34:00 | TERRA_M-M | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 13.7 |
| e5f550cd-853f-3fa6-a7ad-cb3c0bb431df | -1.95579 | -54.40386 | 2025-11-29 00:34:00 | TERRA_M-M | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 457f605a-dd28-34c2-a842-e80c057a86bd | -3.11192 | -45.79327 | 2025-11-29 00:34:00 | TERRA_M-M | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 8d9838a4-2500-384f-b35f-63a9e4ff6e11 | -2.57557 | -49.10697 | 2025-11-29 00:34:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| a6114161-917f-32db-8d4f-10a3242c8089 | -2.72733 | -45.22126 | 2025-11-29 00:34:00 | TERRA_M-M | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 359035a3-53a4-3930-9e3e-54ad36796924 | -2.97713 | -45.58286 | 2025-11-29 00:34:00 | TERRA_M-M | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 48.4 |
| 7b0d75c2-a3e1-3e07-a5bc-7192c3cbae13 | -2.36686 | -46.27712 | 2025-11-29 00:34:00 | TERRA_M-M | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 14.3 |
| 7d518c8e-c10a-3c39-9c9f-d0fb402a3ffe | -2.97746 | -45.24572 | 2025-11-29 00:34:00 | TERRA_M-M | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 21.8 |
| deb26ecd-340a-3ee5-b618-7640f1a4eeed | -3.01061 | -49.57966 | 2025-11-29 00:34:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 9677f265-bfaf-3ed0-b99a-dcd7ba94bb45 | -3.85993 | -54.35449 | 2025-11-29 00:34:00 | TERRA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| f927ea3b-a70b-3b45-b921-0aa7437a2670 | -4.16541 | -43.76981 | 2025-11-29 00:34:00 | TERRA_M-M | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 19.4 |
| 4022b387-9888-337f-b43d-6f86c00428e4 | -2.7019 | -47.40597 | 2025-11-29 00:34:00 | TERRA_M-M | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 22df84f0-d7f0-3112-b789-293c22b841fc | -2.92525 | -45.26013 | 2025-11-29 00:34:00 | TERRA_M-M | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 15.3 |
| 40f7e181-f4d0-30eb-9b00-c558ae61ea66 | -2.4276 | -50.29094 | 2025-11-29 00:34:00 | TERRA_M-M | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 21.3 |
| 75c2c18c-4671-3071-85a5-4dbef256d0da | -2.34342 | -45.6903 | 2025-11-29 00:34:00 | TERRA_M-M | PRESIDENTE MÉDICI | MARANHÃO | Brasil | 2109239 | 21 | 33 | nan | nan | nan | Amazônia | 27.1 |
| c1144e8a-f039-36ae-9235-1f9dfe2c4256 | -0.96535 | -47.56482 | 2025-11-29 00:34:00 | TERRA_M-M | MARACANÃ | PARÁ | Brasil | 1504307 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| f64667ec-e713-31ce-831c-df2216b6fed1 | -3.5805 | -50.29547 | 2025-11-29 00:34:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| d0487bc4-2880-33ab-80de-b5d6a3708921 | -3.42922 | -52.06633 | 2025-11-29 00:34:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| ebdc6be9-a6d9-37dc-a1e0-8ef24f088b9b | -3.67637 | -50.66123 | 2025-11-29 00:34:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| fe0b7c88-e913-327e-8aca-26a18875e896 | -2.96668 | -50.98937 | 2025-11-29 00:34:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 52e86e18-ed54-3b70-9f70-ae95ff1aa90b | -2.43855 | -46.37444 | 2025-11-29 00:34:00 | TERRA_M-M | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 8.8 |
| bc82c736-adf7-3dac-9c28-dd0f71980d4e | -3.52107 | -47.19437 | 2025-11-29 00:34:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 18.9 |
| 9b73d2a0-9d5a-3168-b691-da1921a4db7c | -2.22413 | -47.50556 | 2025-11-29 00:34:00 | TERRA_M-M | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 18.7 |
| 255d1fca-65dd-345d-933d-e1d7011da533 | -3.56998 | -50.41485 | 2025-11-29 00:34:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| b2270a19-e7ac-3dae-af09-c9eb760a3cda | -2.46697 | -45.86388 | 2025-11-29 00:34:00 | TERRA_M-M | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 13.5 |
| 1c87db4e-b501-3934-9b27-c59f14959eb6 | -3.00665 | -49.55152 | 2025-11-29 00:34:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| ddb46e36-5827-33fe-b1e3-c9f04efbf528 | -1.4028 | -54.47065 | 2025-11-29 00:34:00 | TERRA_M-M | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 5feb68af-d38f-3043-b77b-a8ad42a56441 | -2.31711 | -45.84787 | 2025-11-29 00:34:00 | TERRA_M-M | PRESIDENTE MÉDICI | MARANHÃO | Brasil | 2109239 | 21 | 33 | nan | nan | nan | Amazônia | 19.7 |
| 60b7154f-67be-3ad9-8ed7-1f54651beaea | -2.84277 | -51.81874 | 2025-11-29 00:34:00 | TERRA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| f446eb4a-2978-3830-87c0-5a170920131e | -3.52288 | -47.20706 | 2025-11-29 00:34:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 48.0 |
| 350151e8-cd84-3fcf-bec2-5ecd87fc90f0 | -1.35953 | -53.09417 | 2025-11-29 00:34:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| db66c8ad-e246-3081-a877-ca7fbf2bcc49 | -3.11504 | -49.21298 | 2025-11-29 00:34:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| bef94bcf-1498-31e9-9d12-b1637696b90b | -3.22382 | -50.31573 | 2025-11-29 00:34:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 21.2 |
| bff21c71-6675-3b22-8e1d-9583aa257c7e | -2.44297 | -47.0694 | 2025-11-29 00:34:00 | TERRA_M-M | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 375e28cd-7861-3745-9004-5e0ae737d78d | -4.47326 | -50.08978 | 2025-11-29 00:34:00 | TERRA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 8c07bd11-1748-3694-aab5-8f2fcc6ea04f | -2.79656 | -47.4243 | 2025-11-29 00:34:00 | TERRA_M-M | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 11.6 |
| da7395f0-0379-35c6-94aa-6688b2658ab6 | -3.53618 | -51.24028 | 2025-11-29 00:34:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| d4690b3c-73c1-3c14-914e-3e3e2ad1261e | -2.74546 | -49.32578 | 2025-11-29 00:34:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| d3a01724-63fe-3bdf-a73f-4084e17b4ab6 | -2.78441 | -47.41342 | 2025-11-29 00:34:00 | TERRA_M-M | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 15.3 |
| 64bd9ffe-187f-3ee8-ac06-3d6f3fc9c78a | -3.59184 | -47.2667 | 2025-11-29 00:34:00 | TERRA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 16.0 |
| 7116bbd1-54c2-337a-82c5-6ef1876a0185 | -2.25216 | -46.51946 | 2025-11-29 00:34:00 | TERRA_M-M | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 7f1a4e96-ab6f-3342-b3f9-1fe8c30424bc | -2.7115 | -45.69798 | 2025-11-29 00:34:00 | TERRA_M-M | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 9.0 |
| c11b0571-2ec7-3829-9e2c-8215b4a1274a | -2.74752 | -49.87213 | 2025-11-29 00:34:00 | TERRA_M-M | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| ca8105e3-85f1-3d5e-8f12-bd26ed9d5b84 | -3.09783 | -45.7788 | 2025-11-29 00:34:00 | TERRA_M-M | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 141.0 |
| ea006964-cb65-3063-a902-ae5b90a8303e | -2.85966 | -50.28208 | 2025-11-29 00:34:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 355d86f1-3825-3f5d-b6d6-d46578c31d1e | -3.56871 | -47.18082 | 2025-11-29 00:34:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| ed106b1e-dedf-3380-a19c-934979858fab | -3.43046 | -52.07541 | 2025-11-29 00:34:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| dedb07c9-0bb2-3e72-a077-19895d0eef40 | -2.6389 | -48.48602 | 2025-11-29 00:34:00 | TERRA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 15.5 |
| 7a701a7d-ac25-3c82-8ed9-026da9dd9866 | -3.59362 | -47.27898 | 2025-11-29 00:34:00 | TERRA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 17.7 |
| 9ddcc423-5647-329c-8cef-9740940924d8 | -4.86116 | -50.82786 | 2025-11-29 00:34:00 | TERRA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| da52c3a9-e97f-3a4e-94e7-0236ef83c984 | -2.76682 | -45.48675 | 2025-11-29 00:34:00 | TERRA_M-M | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 24.4 |
| bc272a1e-c826-3f8d-8f31-faf021ddeade | -2.31474 | -45.83133 | 2025-11-29 00:34:00 | TERRA_M-M | PRESIDENTE MÉDICI | MARANHÃO | Brasil | 2109239 | 21 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 14efe007-4d86-37ac-b32a-01c8e4e5dac1 | -2.7468 | -49.33543 | 2025-11-29 00:34:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 55358d9d-4d7c-3f79-ab5e-24773a204512 | -2.92215 | -53.07711 | 2025-11-29 00:34:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| d7d4f38b-f038-35fa-83dc-4fcb251de725 | -2.92083 | -53.06738 | 2025-11-29 00:34:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 511bde79-069c-32f3-aaa1-82534724c384 | -3.59781 | -50.41997 | 2025-11-29 00:34:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 7b427d72-5acf-32d7-9252-320e48bbfaa7 | -3.48996 | -50.24141 | 2025-11-29 00:34:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| fdbbb45f-af8b-3d5f-bcee-a35297c78764 | -3.56676 | -50.92482 | 2025-11-29 00:34:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 86fac121-0ef2-344a-8deb-9d2e902630dc | -3.38045 | -50.11694 | 2025-11-29 00:34:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| db6e62c9-7c27-3693-b89c-71499b44527f | -1.764 | -54.78784 | 2025-11-29 00:34:00 | TERRA_M-M | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| b7e4790a-2630-3534-abb2-1899efa80b71 | -3.0287 | -51.43775 | 2025-11-29 00:34:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 73e87171-5d7e-38c4-b4ac-2f7a9e577b8a | -3.24289 | -47.25327 | 2025-11-29 00:34:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 17.3 |
| 725c26b5-6a59-382d-838a-21649305a5a8 | -4.06636 | -54.80822 | 2025-11-29 00:34:00 | TERRA_M-M | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| df587543-0dae-391d-ad1a-f1823eec2d61 | -2.38484 | -49.38181 | 2025-11-29 00:34:00 | TERRA_M-M | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 80d0b852-7e70-3f4c-8b4a-5e6859ee01d5 | -3.17945 | -45.62625 | 2025-11-29 00:34:00 | TERRA_M-M | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 28.5 |
| f9786135-2dc0-37ff-8608-cebf51a5139c | -3.7635 | -46.9586 | 2025-11-29 00:34:00 | TERRA_M-M | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 18.9 |
| 39aa15c0-87b1-34ee-8f9c-492117bc6d45 | -2.92837 | -45.25305 | 2025-11-29 00:34:00 | TERRA_M-M | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 8.9 |


[Clique aqui para ver as próximas entradas](README7.md)
