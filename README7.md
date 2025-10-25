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

## Dados Diários - Página 7

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b5ac1daf-5927-3a9a-8433-ffb8038b8713 | 1.63704 | -55.73166 | 2025-10-25 00:37:00 | TERRA_M-M | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| e49b88c3-14ff-3389-9a1e-b357fc0c64ba | 0.44906 | -51.02691 | 2025-10-25 00:37:00 | TERRA_M-M | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 14.4 |
| 9b1bc016-6412-375e-bd1f-b0117179558c | -4.7018 | -46.4508 | 2025-10-25 00:40:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 55.2 |
| c4e3bba4-df55-3c67-8f83-8842a996d9cd | -14.3551 | -51.8064 | 2025-10-25 00:40:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 62.0 |
| 67a88330-0ebb-326f-9262-ffab31ea3625 | -2.7964 | -49.1572 | 2025-10-25 00:40:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 48.5 |
| d5992d6d-62fe-32c0-9176-1487d083a10c | -2.8888 | -49.1545 | 2025-10-25 00:40:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 85.8 |
| 1903ee44-5dfc-3015-bfc3-0f9dcec6ca0b | -5.2601 | -44.1368 | 2025-10-25 00:40:00 | GOES-19 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 55.9 |
| 7a722ad0-7af3-3798-a8ee-3150e10755ff | -4.8746 | -43.2361 | 2025-10-25 00:40:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 37.8 |
| 1fbc7b65-f6b8-30d9-9ceb-d81a7bdeea4c | -2.8149 | -49.1354 | 2025-10-25 00:40:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 84.9 |
| 3bbf74b8-ec20-3ed0-8491-4f2a0856aa6f | -18.1913 | -51.7432 | 2025-10-25 00:40:00 | GOES-19 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 51.7 |
| 28b4ced2-78e0-3d59-8339-77e4577349e1 | -18.1714 | -51.7466 | 2025-10-25 00:40:00 | GOES-19 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 134.7 |
| 91eb63fe-fbfa-3836-b653-cc37f58bda40 | -3.8268 | -50.2019 | 2025-10-25 00:40:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 51.9 |
| 7cbb09e5-2cb7-3546-bd72-5b5cb1b5f12d | -19.7581 | -48.3056 | 2025-10-25 00:40:00 | GOES-19 | CONCEIÇÃO DAS ALAGOAS | MINAS GERAIS | Brasil | 3117306 | 31 | 33 | nan | nan | nan | Cerrado | 135.9 |
| 7fb5370a-ff39-3d85-b9f2-c12e52af5693 | -2.7964 | -49.136 | 2025-10-25 00:40:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 103.0 |
| e5d7c89e-a51e-324e-b8db-0de9bfe6057b | -2.8887 | -49.1758 | 2025-10-25 00:40:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 128.7 |
| 7c1766da-b62b-38bf-912a-2ec84f4d81fa | -19.7791 | -48.278 | 2025-10-25 00:40:00 | GOES-19 | CONCEIÇÃO DAS ALAGOAS | MINAS GERAIS | Brasil | 3117306 | 31 | 33 | nan | nan | nan | Cerrado | 158.0 |
| aa2acc4f-7908-3ce7-96fa-6a116879c849 | -4.8933 | -43.2349 | 2025-10-25 00:40:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 81.6 |
| fa14dc9b-7914-36a7-9c17-820637054e79 | -2.9073 | -49.154 | 2025-10-25 00:40:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 49.5 |
| d8a2b587-f616-37c2-a1a0-50cd8199e140 | -18.1514 | -51.75 | 2025-10-25 00:40:00 | GOES-19 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 50.0 |
| 86ab75ff-ea94-3658-ab8b-15f91239d5d2 | -14.3744 | -51.8038 | 2025-10-25 00:40:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 60.5 |
| 0ba36a24-6c20-304b-9f91-0b339d90a5fa | -15.2436 | -47.9302 | 2025-10-25 00:40:00 | GOES-19 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 55.4 |
| 14881655-2e31-3b13-a86a-042898a096e0 | -2.9072 | -49.1753 | 2025-10-25 00:40:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 69.9 |
| ccf9cbff-43bb-30f7-8bee-0f9e8c7cc7ea | -19.7784 | -48.3011 | 2025-10-25 00:40:00 | GOES-19 | CONCEIÇÃO DAS ALAGOAS | MINAS GERAIS | Brasil | 3117306 | 31 | 33 | nan | nan | nan | Cerrado | 117.0 |
| bf87e1c4-943b-3601-a2f3-899336f85558 | -18.1709 | -51.7685 | 2025-10-25 00:40:00 | GOES-19 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 83.1 |
| d469589b-c6b9-3f7b-a5d5-11dc1dfb2a37 | -4.8399 | -50.9345 | 2025-10-25 00:40:00 | GOES-19 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 78.6 |
| e4162001-4893-3a30-97ff-4be2638b0e68 | -19.7587 | -48.2824 | 2025-10-25 00:40:00 | GOES-19 | CONCEIÇÃO DAS ALAGOAS | MINAS GERAIS | Brasil | 3117306 | 31 | 33 | nan | nan | nan | Cerrado | 189.7 |
| 87ddc3ea-5ead-342b-b2b8-90ffcf08de95 | -19.7581 | -48.3056 | 2025-10-25 00:50:00 | GOES-19 | CONCEIÇÃO DAS ALAGOAS | MINAS GERAIS | Brasil | 3117306 | 31 | 33 | nan | nan | nan | Cerrado | 103.4 |
| e3d5c37e-9b81-3594-9432-58b23c822692 | -2.8887 | -49.1758 | 2025-10-25 00:50:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 143.0 |
| b55fcf53-b89a-3530-b191-f17905b3ca5f | -2.8149 | -49.1354 | 2025-10-25 00:50:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 77.2 |
| 326862f2-9050-3856-81ce-1fa862d4b468 | -19.7784 | -48.3011 | 2025-10-25 00:50:00 | GOES-19 | CONCEIÇÃO DAS ALAGOAS | MINAS GERAIS | Brasil | 3117306 | 31 | 33 | nan | nan | nan | Cerrado | 130.0 |
| c0cc4b11-ec4b-3568-bb0c-f536f5443b47 | -19.7791 | -48.278 | 2025-10-25 00:50:00 | GOES-19 | CONCEIÇÃO DAS ALAGOAS | MINAS GERAIS | Brasil | 3117306 | 31 | 33 | nan | nan | nan | Cerrado | 185.3 |
| 005868db-250c-3075-ac9e-6d0e7f22da6a | -2.9072 | -49.1753 | 2025-10-25 00:50:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 89.0 |
| 04f04217-9916-39f3-a23a-f97d9d572c58 | -2.9073 | -49.154 | 2025-10-25 00:50:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 65.0 |
| bdc43ce0-236e-3643-a9d6-c2339916f0c5 | -2.8888 | -49.1545 | 2025-10-25 00:50:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 101.6 |
| f84f662f-fe7c-348a-8000-0f4cd1697688 | -14.3547 | -51.8278 | 2025-10-25 00:50:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 48.6 |
| 003747da-8892-36e0-b1e5-aa558b4de54a | -2.7964 | -49.1572 | 2025-10-25 00:50:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 52.0 |
| 7393f9fa-c7e0-373d-a110-38fe0f158471 | -14.3551 | -51.8064 | 2025-10-25 00:50:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 63.7 |
| 9c7362c8-0088-3323-ae40-c9660ebe7716 | -20.3203 | -55.2083 | 2025-10-25 00:50:00 | GOES-19 | TERENOS | MATO GROSSO DO SUL | Brasil | 5008008 | 50 | 33 | nan | nan | nan | Cerrado | 78.2 |
| 72e8a901-8e7b-349c-92e0-b2a952f28faf | -4.8399 | -50.9345 | 2025-10-25 00:50:00 | GOES-19 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 74.4 |
| c2b0d333-778e-3e08-bc55-0cc94cfc3720 | -2.7964 | -49.136 | 2025-10-25 00:50:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 101.3 |
| 67806a1a-be57-361c-8fd9-5cbe0e3e9074 | -18.1709 | -51.7685 | 2025-10-25 00:50:00 | GOES-19 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 90.5 |
| 0c0a7274-fe6c-369c-8ac8-e5899fca37df | -20.3198 | -55.2297 | 2025-10-25 00:50:00 | GOES-19 | TERENOS | MATO GROSSO DO SUL | Brasil | 5008008 | 50 | 33 | nan | nan | nan | Cerrado | 68.2 |
| 1746a0aa-fafd-357f-8f23-48f29ffaaf5f | -19.7587 | -48.2824 | 2025-10-25 00:50:00 | GOES-19 | CONCEIÇÃO DAS ALAGOAS | MINAS GERAIS | Brasil | 3117306 | 31 | 33 | nan | nan | nan | Cerrado | 156.2 |
| 7953e138-0adb-3cb6-a87e-e2d60b6d0442 | -18.1714 | -51.7466 | 2025-10-25 00:50:00 | GOES-19 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 149.0 |
| 3f091224-1e98-3c1d-a802-b1d9cc424eb7 | -2.8888 | -49.1545 | 2025-10-25 01:00:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 62.2 |
| 667174da-6359-38fd-a62b-c0ddadb9efe3 | -14.3551 | -51.8064 | 2025-10-25 01:00:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 88.8 |
| 6638a78f-eafb-31eb-aca7-b707cc90d490 | -2.7964 | -49.1572 | 2025-10-25 01:00:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 50.0 |
| 1e9e4791-1241-3444-9181-8930cf634ceb | -14.3357 | -51.809 | 2025-10-25 01:00:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 94.6 |
| 0e3c60f3-7749-3fe1-83f3-a44536e596fc | -2.9072 | -49.1753 | 2025-10-25 01:00:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 70.1 |
| 6f8a8e80-ffe7-393e-953a-483d831a9d7b | -14.3744 | -51.8038 | 2025-10-25 01:00:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 76.6 |
| b370f047-a364-3660-9001-a20eef96960e | -18.1714 | -51.7466 | 2025-10-25 01:00:00 | GOES-19 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 133.5 |
| eca15804-88d0-308d-82bb-2ef53f42b1e9 | -19.7791 | -48.278 | 2025-10-25 01:00:00 | GOES-19 | CONCEIÇÃO DAS ALAGOAS | MINAS GERAIS | Brasil | 3117306 | 31 | 33 | nan | nan | nan | Cerrado | 226.1 |
| 246ea5e0-0632-306e-a849-831b8e2625ab | -19.7784 | -48.3011 | 2025-10-25 01:00:00 | GOES-19 | CONCEIÇÃO DAS ALAGOAS | MINAS GERAIS | Brasil | 3117306 | 31 | 33 | nan | nan | nan | Cerrado | 96.4 |
| b21d0405-dd15-33d0-8f6a-b0e773f1c62c | -19.7581 | -48.3056 | 2025-10-25 01:00:00 | GOES-19 | CONCEIÇÃO DAS ALAGOAS | MINAS GERAIS | Brasil | 3117306 | 31 | 33 | nan | nan | nan | Cerrado | 74.8 |
| a455f4b0-a38e-3964-b99f-19198cae208b | -2.9073 | -49.154 | 2025-10-25 01:00:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 50.0 |
| e347d373-d013-349b-af24-88a5b4dc9c86 | -18.1709 | -51.7685 | 2025-10-25 01:00:00 | GOES-19 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 94.5 |
| baf8edbc-9a81-3b93-914d-f5417540a49f | -14.3354 | -51.8303 | 2025-10-25 01:00:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 54.6 |
| 9c9194c9-9458-3b4b-874e-032ec1bdfba0 | -15.2436 | -47.9302 | 2025-10-25 01:00:00 | GOES-19 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 55.3 |
| dc29f0f4-6763-355a-876a-844415fa0db5 | -19.7587 | -48.2824 | 2025-10-25 01:00:00 | GOES-19 | CONCEIÇÃO DAS ALAGOAS | MINAS GERAIS | Brasil | 3117306 | 31 | 33 | nan | nan | nan | Cerrado | 179.1 |
| 64417797-f85a-3bcf-8d4f-8b1ab8e1cfd3 | -2.8887 | -49.1758 | 2025-10-25 01:00:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 89.9 |
| f7cbd0a7-2dd7-3815-aa6e-33828a7d8d79 | -9.6295 | -40.3392 | 2025-10-25 01:00:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 70.8 |
| 0e4935a9-1ed2-3bbb-989c-976cb1e20c85 | -4.8933 | -43.2349 | 2025-10-25 01:00:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 54.8 |
| 0e191087-dd3a-3882-9e3d-e10db4200c32 | -2.7964 | -49.136 | 2025-10-25 01:00:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 109.3 |
| 891d46e3-e4d8-373d-bc9d-2004c96426fc | -14.3547 | -51.8278 | 2025-10-25 01:00:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 58.6 |
| 63805a51-9e14-31b6-bfd5-e9494b34f1e8 | -2.8149 | -49.1354 | 2025-10-25 01:00:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 82.9 |
| 57fe9fa3-37d3-344c-ac9d-e7faf31a129a | -4.8399 | -50.9345 | 2025-10-25 01:00:00 | GOES-19 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 63.4 |
| 81e56762-9432-30e1-ae4d-1a3d947fd39e | -14.3547 | -51.8278 | 2025-10-25 01:10:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 58.7 |
| 1a8e8751-ea6a-3892-8377-024b468be51a | -2.8887 | -49.1758 | 2025-10-25 01:10:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 68.8 |
| 7a9c2148-800d-3ea7-80e9-40ac2ac8e656 | -18.1709 | -51.7685 | 2025-10-25 01:10:00 | GOES-19 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 78.4 |
| a1b89465-a829-3b28-9ada-91d55e83bc68 | -19.7791 | -48.278 | 2025-10-25 01:10:00 | GOES-19 | CONCEIÇÃO DAS ALAGOAS | MINAS GERAIS | Brasil | 3117306 | 31 | 33 | nan | nan | nan | Cerrado | 153.9 |
| 7b91b75e-a449-3da7-80fc-87af9aa138ba | -2.7964 | -49.136 | 2025-10-25 01:10:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 94.1 |
| a1532c5f-0dc2-3629-bbfb-46c9c092c731 | -19.7587 | -48.2824 | 2025-10-25 01:10:00 | GOES-19 | CONCEIÇÃO DAS ALAGOAS | MINAS GERAIS | Brasil | 3117306 | 31 | 33 | nan | nan | nan | Cerrado | 134.5 |
| 176484a7-a432-30f9-9ff2-cc4fc06ec9b7 | -2.8149 | -49.1354 | 2025-10-25 01:10:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 74.2 |
| b044e646-18e0-329f-b57c-24a9018d32fd | -14.3551 | -51.8064 | 2025-10-25 01:10:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 55.8 |
| fc4463ad-5a90-380c-9c31-45b49ceac008 | -19.7581 | -48.3056 | 2025-10-25 01:10:00 | GOES-19 | CONCEIÇÃO DAS ALAGOAS | MINAS GERAIS | Brasil | 3117306 | 31 | 33 | nan | nan | nan | Cerrado | 77.9 |
| 9aa63841-5734-395d-9e70-b1dfd9aa373f | -4.8399 | -50.9345 | 2025-10-25 01:10:00 | GOES-19 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 69.6 |
| 47e84644-a6a1-346c-b1d0-e4708c568680 | -2.8888 | -49.1545 | 2025-10-25 01:10:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 46.6 |
| 2e2d523f-c2e9-3b5f-9833-941da57dfd6c | -18.1714 | -51.7466 | 2025-10-25 01:10:00 | GOES-19 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 134.4 |
| 3bfaad16-b4e0-3115-b012-635fa20110ca | -14.3354 | -51.8303 | 2025-10-25 01:10:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 55.3 |
| 79105db0-cef9-3a2f-92fc-e2d89f376f58 | -19.7784 | -48.3011 | 2025-10-25 01:10:00 | GOES-19 | CONCEIÇÃO DAS ALAGOAS | MINAS GERAIS | Brasil | 3117306 | 31 | 33 | nan | nan | nan | Cerrado | 93.4 |
| 3a9a3a32-667f-3dda-b6a6-e83010ec763d | -14.3357 | -51.809 | 2025-10-25 01:10:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 54.0 |
| dc0149fe-59b6-3831-9a56-f3e31087af4a | -15.2436 | -47.9302 | 2025-10-25 01:10:00 | GOES-19 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 51.6 |
| 1235ddec-aa12-3c23-b6e7-b9212c1d667f | -18.1714 | -51.7466 | 2025-10-25 01:20:00 | GOES-19 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 116.8 |
| 6bdfce3c-cca5-352f-bb00-1875a2c76b40 | -19.7587 | -48.2824 | 2025-10-25 01:20:00 | GOES-19 | CONCEIÇÃO DAS ALAGOAS | MINAS GERAIS | Brasil | 3117306 | 31 | 33 | nan | nan | nan | Cerrado | 124.2 |
| a5efa4ca-1418-316c-b908-8d33a1bc76cc | -19.7784 | -48.3011 | 2025-10-25 01:20:00 | GOES-19 | CONCEIÇÃO DAS ALAGOAS | MINAS GERAIS | Brasil | 3117306 | 31 | 33 | nan | nan | nan | Cerrado | 77.4 |
| 819ed1c5-e501-3f16-bf3d-73cc2a961a78 | -14.8706 | -48.0822 | 2025-10-25 01:20:00 | GOES-19 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 52.4 |
| fd3ad3f4-fbbf-3d68-aa85-d84a748720ed | -5.2601 | -44.1368 | 2025-10-25 01:20:00 | GOES-19 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 44.0 |
| d7702a28-3a62-3c23-96d9-cc3cb3ea06c1 | -4.8399 | -50.9345 | 2025-10-25 01:20:00 | GOES-19 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 66.9 |
| 0f004a13-3d96-3e69-a78d-34259d144a9b | -19.7581 | -48.3056 | 2025-10-25 01:20:00 | GOES-19 | CONCEIÇÃO DAS ALAGOAS | MINAS GERAIS | Brasil | 3117306 | 31 | 33 | nan | nan | nan | Cerrado | 76.6 |
| 39d69971-971e-3be4-963d-4aefe9157117 | -19.7791 | -48.278 | 2025-10-25 01:20:00 | GOES-19 | CONCEIÇÃO DAS ALAGOAS | MINAS GERAIS | Brasil | 3117306 | 31 | 33 | nan | nan | nan | Cerrado | 117.3 |
| b6d66493-8110-3dba-a99c-4f94eae559ec | -18.1709 | -51.7685 | 2025-10-25 01:20:00 | GOES-19 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 63.8 |
| 2daba7f2-4b46-33f9-8bb8-37a7ba6e261e | -18.1709 | -51.7685 | 2025-10-25 01:30:00 | GOES-19 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 61.5 |
| 01c3473a-cc35-301d-87e6-2d402761314e | -19.7581 | -48.3056 | 2025-10-25 01:30:00 | GOES-19 | CONCEIÇÃO DAS ALAGOAS | MINAS GERAIS | Brasil | 3117306 | 31 | 33 | nan | nan | nan | Cerrado | 74.1 |
| 0f5bfb69-78dd-3424-90d4-9b724b3e1bd0 | -18.1514 | -51.75 | 2025-10-25 01:30:00 | GOES-19 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 46.4 |
| 37d12478-a8f5-3ce6-ac83-44ca55c41a79 | -2.8148 | -49.1567 | 2025-10-25 01:30:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 50.1 |
| c2760944-b6a9-3f81-abc9-8a49c5e33e23 | -18.1714 | -51.7466 | 2025-10-25 01:30:00 | GOES-19 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 114.0 |
| 9130cb9c-bdf4-3212-b12f-b903e0503d60 | -19.7784 | -48.3011 | 2025-10-25 01:30:00 | GOES-19 | CONCEIÇÃO DAS ALAGOAS | MINAS GERAIS | Brasil | 3117306 | 31 | 33 | nan | nan | nan | Cerrado | 61.6 |
| 99dd5f9e-6ddb-327a-b181-e5f4614d7690 | -4.8399 | -50.9345 | 2025-10-25 01:30:00 | GOES-19 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 63.0 |
| a8ef1606-0fb0-3760-a862-5f1b25a3042f | -14.8706 | -48.0822 | 2025-10-25 01:30:00 | GOES-19 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 68.0 |
| bf8dd740-d948-3683-bbb2-f847090713d7 | -5.2601 | -44.1368 | 2025-10-25 01:30:00 | GOES-19 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 48.6 |


[Clique aqui para ver as próximas entradas](README8.md)
