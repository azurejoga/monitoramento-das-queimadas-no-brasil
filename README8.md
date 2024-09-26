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

## Dados Diários - Página 8

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 26d7b17f-e6f2-38aa-bfdb-a2f44846793b | -7.7333 | -55.712 | 2024-09-26 00:35:50 | GOES-16 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 54.3 |
| 39fa74de-6541-305e-aa10-06c86645a28b | -7.797 | -54.7263 | 2024-09-26 00:35:51 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 117.1 |
| c32f487f-ec70-348b-af0b-3dc2b5172faf | -7.8154 | -54.7453 | 2024-09-26 00:35:51 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 85.6 |
| 1d7971e9-dcdc-3e19-a7a4-0d86e4562251 | -7.8156 | -54.7252 | 2024-09-26 00:35:51 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 143.4 |
| 4c4a4464-3402-3b7d-94de-b39324506d4f | -8.1572 | -61.3953 | 2024-09-26 00:35:53 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 61.3 |
| 635f1816-4aef-3641-972d-af694a54dc4e | -8.3153 | -55.0157 | 2024-09-26 00:35:54 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 84.4 |
| a7a4b600-5066-36c5-8493-5b4165376169 | -8.3155 | -54.9956 | 2024-09-26 00:35:54 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 114.0 |
| 8affd6c9-24a3-3766-91de-ed059d73d07d | -8.5542 | -63.1814 | 2024-09-26 00:35:55 | GOES-16 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 53.4 |
| bcb2cf36-4115-351f-bc69-c414a575109c | -8.7087 | -54.7881 | 2024-09-26 00:35:56 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 105.7 |
| 843e7c21-3c0f-3c1b-b60a-f76a7eb7f515 | -8.8098 | -58.2172 | 2024-09-26 00:35:57 | GOES-16 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 69.4 |
| 854b455c-a28a-3274-aa79-24548957e597 | -8.8292 | -63.7179 | 2024-09-26 00:35:57 | GOES-16 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 49.6 |
| 9c033cc3-aaba-31a5-a792-7177be717cba | -8.9301 | -57.1488 | 2024-09-26 00:35:57 | GOES-16 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 33.5 |
| a4db2d50-5dab-357d-8d0d-ccf7e127e92d | -9.0657 | -61.3743 | 2024-09-26 00:35:58 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 69.3 |
| 57466368-bf6d-3537-af4a-38afb696980b | -9.086 | -61.1245 | 2024-09-26 00:35:58 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 74.8 |
| 9fdaa6f7-0f8c-38ba-9fba-b041a0b9297f | -9.1046 | -61.1237 | 2024-09-26 00:35:58 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 97.3 |
| 165f6c6b-e5b4-32ce-96a0-9d1aa095f078 | -9.1349 | -65.564 | 2024-09-26 00:35:59 | GOES-16 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 47.0 |
| 91b60cb2-a2b3-3336-b79a-73fb5b6da65e | -9.4353 | -51.4829 | 2024-09-26 00:36:00 | GOES-16 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 92.9 |
| 38a37b6a-b28f-3674-8397-19164c45be8b | -9.5827 | -50.1584 | 2024-09-26 00:36:01 | GOES-16 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 100.4 |
| ace7b7a4-1ef0-3963-be44-8cbe5f022562 | -9.5829 | -50.137 | 2024-09-26 00:36:01 | GOES-16 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 86.7 |
| beb40fd5-01db-37d8-8874-06b12309272f | -9.6015 | -50.1566 | 2024-09-26 00:36:01 | GOES-16 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 165.2 |
| 4267ef34-6153-35f2-a874-3d340f6716d4 | -9.6018 | -50.1352 | 2024-09-26 00:36:01 | GOES-16 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 96.4 |
| 6e42cda3-adcf-3181-b49a-3e3fe2e9a021 | -9.806 | -53.5664 | 2024-09-26 00:36:02 | GOES-16 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 101.8 |
| 7c133dce-534d-31df-89d7-db8f5a6aa79a | -9.8083 | -68.8152 | 2024-09-26 00:36:03 | GOES-16 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 57.7 |
| 1023334d-b697-36f8-a85a-0f64ebff3ba1 | -10.0506 | -68.5875 | 2024-09-26 00:36:04 | GOES-16 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 46.2 |
| 8b3be069-2c90-328c-a282-250c70561d5d | -10.0692 | -68.5871 | 2024-09-26 00:36:04 | GOES-16 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 53.2 |
| 4e245d35-ec71-3e23-a4e7-79bf739815a7 | -10.39 | -58.9044 | 2024-09-26 00:36:06 | GOES-16 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 67.1 |
| 577fda21-7e04-3a1a-a41f-d7cd995f536b | -10.448 | -53.3058 | 2024-09-26 00:36:06 | GOES-16 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 72.5 |
| 9bdfed08-d952-3fb4-b358-c1271818de30 | -10.3882 | -67.8737 | 2024-09-26 00:36:06 | GOES-16 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 73.9 |
| 932ff280-df49-38fd-b39c-2b0441916a23 | -10.4068 | -67.8732 | 2024-09-26 00:36:06 | GOES-16 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 63.1 |
| 166be432-149f-3b02-94b6-26b57632599b | -10.9928 | -44.415 | 2024-09-26 00:36:08 | GOES-16 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 81.1 |
| 039c5ed5-07a1-3811-8b93-f29ac2273701 | -10.8915 | -57.4521 | 2024-09-26 00:36:08 | GOES-16 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 66.9 |
| 9aa260e5-27b2-3e41-b36e-b0e70cb7e8e2 | -10.8917 | -57.4322 | 2024-09-26 00:36:08 | GOES-16 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 74.3 |
| eea2b16b-4522-35c4-bff0-0dfd3943eaef | -10.9105 | -57.4308 | 2024-09-26 00:36:08 | GOES-16 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 67.8 |
| d9a0b92b-ee3f-3ac5-84b2-3d7bf71f74d7 | -10.9107 | -57.411 | 2024-09-26 00:36:08 | GOES-16 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 65.7 |
| c658bf8b-9c58-38b5-ab39-44d1c4fd76fd | -11.1845 | -54.7769 | 2024-09-26 00:36:10 | GOES-16 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 53.4 |
| 94bcc456-be1e-3d79-8e94-5e3e4aaae066 | -11.2034 | -54.7752 | 2024-09-26 00:36:10 | GOES-16 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 103.1 |
| 2113b0e8-14e1-3abe-aa4b-fbb09827274d | -11.2036 | -54.7548 | 2024-09-26 00:36:10 | GOES-16 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 53.1 |
| a573214c-f10b-3b2b-a8f4-d2c72dc5cff3 | -11.2412 | -65.2997 | 2024-09-26 00:36:11 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 47.2 |
| caea3f0e-58d1-373c-aecc-84fc3dfbe5e9 | -11.2413 | -65.2809 | 2024-09-26 00:36:11 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 51.4 |
| 717267e3-18e4-3a8c-9471-d0a7544b8914 | -11.2599 | -65.299 | 2024-09-26 00:36:11 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 80.5 |
| 9a1070ef-9a23-32cb-874c-ddfa59f371ce | -11.26 | -65.2801 | 2024-09-26 00:36:11 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 96.6 |
| 0478d2bc-73b4-3ad8-8e1e-641471636376 | -11.2786 | -65.2982 | 2024-09-26 00:36:11 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 49.2 |
| ef9ea628-6256-375c-a787-4558b373ddc7 | -11.2788 | -65.2793 | 2024-09-26 00:36:11 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 57.0 |
| 49c8c3f4-f7af-36c9-8f68-fe3101d1f7ce | -11.4789 | -47.3082 | 2024-09-26 00:36:11 | GOES-16 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 92.9 |
| 56339039-1450-3f33-9196-4ba4189a4f69 | -11.7179 | -47.8551 | 2024-09-26 00:36:12 | GOES-16 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 74.9 |
| 1108b658-84d1-351b-8caf-b26a66109da4 | -12.2175 | -45.5074 | 2024-09-26 00:36:15 | GOES-16 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 71.5 |
| 56744636-8343-3c3d-957d-438a71228872 | -12.2367 | -45.5045 | 2024-09-26 00:36:15 | GOES-16 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 69.8 |
| 0d830f28-0720-3f5a-a704-f4db164ffbf3 | -12.5276 | -53.496 | 2024-09-26 00:36:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 101.2 |
| 5a6b9365-0c3e-3980-8353-f5e2348ea9a1 | -12.7877 | -51.3873 | 2024-09-26 00:36:18 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 73.4 |
| 2dcb90c4-07f2-3c7b-957b-1298edff2534 | -12.7881 | -51.366 | 2024-09-26 00:36:18 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 260.3 |
| d4aed945-be6d-342f-81d1-74a46146e235 | -12.7884 | -51.3446 | 2024-09-26 00:36:18 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 99.9 |
| 75f7ef1f-8590-3a6e-b89a-8c39dabd7a6b | -12.7898 | -51.2593 | 2024-09-26 00:36:18 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 147.0 |
| d52fa706-9829-3436-99c1-4f77b12c5077 | -12.7901 | -51.238 | 2024-09-26 00:36:18 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 97.4 |
| c4fb4851-0122-35be-bdec-32525ed0fcd7 | -12.8072 | -51.3637 | 2024-09-26 00:36:19 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 211.8 |
| c214f78b-f00a-3eda-ac91-14655b921443 | -12.8076 | -51.3423 | 2024-09-26 00:36:19 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 84.7 |
| d00555c2-94d2-3dbf-96d4-56faa924ba81 | -12.8086 | -51.2783 | 2024-09-26 00:36:19 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 58.1 |
| d7f23c48-171b-386a-9c5f-991d58e59052 | -12.8089 | -51.257 | 2024-09-26 00:36:19 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 117.3 |
| e6407a86-1909-33c1-be66-bc94d273183b | -12.8065 | -60.2846 | 2024-09-26 00:36:19 | GOES-16 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 79.5 |
| b67d1731-dc27-3b80-8f04-d2d454b5daa5 | -12.822 | -62.7078 | 2024-09-26 00:36:19 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 64.7 |
| b2e4e7a8-f0a8-3d6c-870e-b825e98dd1bd | -12.8222 | -62.6886 | 2024-09-26 00:36:19 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 42.1 |
| 7ad96066-865b-3b9b-ace5-6e72560dc8ff | -12.841 | -62.7067 | 2024-09-26 00:36:19 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 75.1 |
| 21cf57c4-8271-3ecd-9b2b-40cbee00a1d8 | -12.8411 | -62.6874 | 2024-09-26 00:36:19 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 48.4 |
| d3d8df4c-764b-3cd2-b202-0a497f4de9fd | -13.1958 | -45.6539 | 2024-09-26 00:36:20 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 64.9 |
| 934fecac-1e9a-3c21-804d-2249c8c2a3c5 | -13.1963 | -45.6308 | 2024-09-26 00:36:20 | GOES-16 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 87.5 |
| 679ba28c-2225-348d-aa76-f27d51f64ae2 | -13.0295 | -57.2985 | 2024-09-26 00:36:20 | GOES-16 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 73.6 |
| 220d2cfc-82de-39b9-bd1e-32eb75630c99 | -14.4639 | -45.2286 | 2024-09-26 00:36:27 | GOES-16 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 68.5 |
| a74215db-844a-34c9-9a96-5a1a656331b3 | -14.896 | -57.9873 | 2024-09-26 00:36:31 | GOES-16 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | 161.0 |
| f453c649-3a98-3172-9315-c4c89b3969c0 | -14.8963 | -57.9671 | 2024-09-26 00:36:31 | GOES-16 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | 43.7 |
| 2c6efa9c-0e73-37af-8799-45b9264e9168 | -14.915 | -58.0055 | 2024-09-26 00:36:31 | GOES-16 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | 73.8 |
| b28f3506-694e-3951-8598-22826d30bc02 | -14.9153 | -57.9854 | 2024-09-26 00:36:31 | GOES-16 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | 227.5 |
| 27de8ed5-09c6-3670-9b75-f2df66dc53c8 | -14.9156 | -57.9653 | 2024-09-26 00:36:31 | GOES-16 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | 57.4 |
| 5c27fa71-bd03-3824-ba5e-d2033cc555c7 | -14.8957 | -58.0074 | 2024-09-26 00:36:31 | GOES-16 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | 58.2 |
| 0418f815-4e2b-30aa-82a3-38f9eb5ae4b1 | -15.2981 | -58.1891 | 2024-09-26 00:36:33 | GOES-16 | RIO BRANCO | MATO GROSSO | Brasil | 5107206 | 51 | 33 | nan | nan | nan | Amazônia | 44.1 |
| 14c61ecc-7781-37ad-820f-84da821305c0 | -16.9729 | -57.931 | 2024-09-26 00:36:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 131.1 |
| 36e9d37c-9a15-3f05-b05d-0306bdb4d54c | -16.9925 | -57.9288 | 2024-09-26 00:36:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 105.4 |
| c88a2337-83c2-3173-867b-97aaca69e6f3 | -16.9732 | -57.9106 | 2024-09-26 00:36:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 89.7 |
| 19d879cc-9f56-3a57-8cef-1a1dbcc2e3ba | -16.9928 | -57.9084 | 2024-09-26 00:36:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 69.0 |
| 4c8e5386-1f81-343c-b8ea-ce13550a4442 | -19.929 | -43.7959 | 2024-09-26 00:36:56 | GOES-16 | SABARÁ | MINAS GERAIS | Brasil | 3156700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 82.6 |
| b636f464-79d6-3097-bcfa-94259e9dcf52 | -19.9298 | -43.7711 | 2024-09-26 00:36:56 | GOES-16 | SABARÁ | MINAS GERAIS | Brasil | 3156700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 76.2 |
| 7ce99ded-b8ae-3db4-9c76-6a350cc85c26 | -20.3999 | -41.8602 | 2024-09-26 00:36:58 | GOES-16 | ALTO JEQUITIBÁ | MINAS GERAIS | Brasil | 3153509 | 31 | 33 | nan | nan | nan | Mata Atlântica | 56.8 |
| c506b236-a10b-3ad7-91ff-f7b69c5eae28 | -20.4197 | -41.8798 | 2024-09-26 00:36:58 | GOES-16 | ALTO JEQUITIBÁ | MINAS GERAIS | Brasil | 3153509 | 31 | 33 | nan | nan | nan | Mata Atlântica | 96.6 |
| 455212f8-2b4e-3935-a26d-ab47c3183503 | -20.4206 | -41.8541 | 2024-09-26 00:36:58 | GOES-16 | ALTO CAPARAÓ | MINAS GERAIS | Brasil | 3102050 | 31 | 33 | nan | nan | nan | Mata Atlântica | 93.0 |
| d9f59752-b9fd-3143-a857-fca1f2c3b984 | -20.5881 | -51.4802 | 2024-09-26 00:37:00 | GOES-16 | ITAPURA | SÃO PAULO | Brasil | 3523008 | 35 | 33 | nan | nan | nan | Mata Atlântica | 99.6 |
| 3dd0d3a4-f4cd-306a-b49f-a4da61e66164 | -20.608 | -51.4986 | 2024-09-26 00:37:00 | GOES-16 | ITAPURA | SÃO PAULO | Brasil | 3523008 | 35 | 33 | nan | nan | nan | Mata Atlântica | 100.1 |
| a72d39ed-e986-3b29-be9b-9da036e4247b | -20.6086 | -51.4762 | 2024-09-26 00:37:00 | GOES-16 | ITAPURA | SÃO PAULO | Brasil | 3523008 | 35 | 33 | nan | nan | nan | Mata Atlântica | 166.5 |
| 4d3fca73-c256-33a3-8f64-fa6482839a37 | -22.74033 | -44.78621 | 2024-09-26 00:39:00 | TERRA_M-M | SILVEIRAS | SÃO PAULO | Brasil | 3552007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.7 |
| 5dabe664-fc85-314b-af7f-29a6308825f1 | -23.34951 | -47.00127 | 2024-09-26 00:39:00 | TERRA_M-M | PIRAPORA DO BOM JESUS | SÃO PAULO | Brasil | 3539103 | 35 | 33 | nan | nan | nan | Mata Atlântica | 18.7 |
| 6792c231-3102-3dc3-b53a-4ace71654040 | -22.87957 | -47.83894 | 2024-09-26 00:39:00 | TERRA_M-M | PIRACICABA | SÃO PAULO | Brasil | 3538709 | 35 | 33 | nan | nan | nan | Mata Atlântica | 30.7 |
| dd9d4177-5eb2-3c21-b6e4-7e939804ba37 | -22.87758 | -47.81967 | 2024-09-26 00:39:00 | TERRA_M-M | PIRACICABA | SÃO PAULO | Brasil | 3538709 | 35 | 33 | nan | nan | nan | Mata Atlântica | 14.3 |
| d06e0f96-2860-30fc-8bdc-b66ae604450a | -22.78432 | -44.1334 | 2024-09-26 00:39:00 | TERRA_M-M | RIO CLARO | RIO DE JANEIRO | Brasil | 3304409 | 33 | 33 | nan | nan | nan | Mata Atlântica | 8.8 |
| 8f5920ea-fcbe-3c0d-b704-3bc22d9a9cab | -22.67068 | -43.72445 | 2024-09-26 00:39:00 | TERRA_M-M | SEROPÉDICA | RIO DE JANEIRO | Brasil | 3305554 | 33 | 33 | nan | nan | nan | Mata Atlântica | 6.3 |
| daeea7ab-e490-3e75-b2f0-9a25311ac03a | -22.60129 | -42.21661 | 2024-09-26 00:39:00 | TERRA_M-M | ARARUAMA | RIO DE JANEIRO | Brasil | 3300209 | 33 | 33 | nan | nan | nan | Mata Atlântica | 6.2 |
| 3d172b76-203f-3197-b85b-f6bbf21c5d44 | -22.36745 | -47.64132 | 2024-09-26 00:39:00 | TERRA_M-M | RIO CLARO | SÃO PAULO | Brasil | 3543907 | 35 | 33 | nan | nan | nan | Cerrado | 14.3 |
| 98970c3b-9644-37b8-97db-662384ba6103 | -22.35621 | -47.77321 | 2024-09-26 00:39:00 | TERRA_M-M | ITIRAPINA | SÃO PAULO | Brasil | 3523602 | 35 | 33 | nan | nan | nan | Cerrado | 15.5 |
| bb541ef3-85f8-3438-849b-020c8c3d38b3 | -22.35438 | -47.75488 | 2024-09-26 00:39:00 | TERRA_M-M | IPEÚNA | SÃO PAULO | Brasil | 3521101 | 35 | 33 | nan | nan | nan | Cerrado | 14.0 |
| d74cc42e-bca5-3d29-83c0-9974b03e1786 | -22.35247 | -47.77935 | 2024-09-26 00:39:00 | TERRA_M-M | ITIRAPINA | SÃO PAULO | Brasil | 3523602 | 35 | 33 | nan | nan | nan | Cerrado | 16.1 |
| c20c0a0a-09ad-32b4-90ec-a3836d414717 | -22.35046 | -47.76048 | 2024-09-26 00:39:00 | TERRA_M-M | IPEÚNA | SÃO PAULO | Brasil | 3521101 | 35 | 33 | nan | nan | nan | Cerrado | 45.6 |
| 0c22a8f3-e25c-3999-8bcc-75fd9e7ca6f1 | -22.34396 | -47.77425 | 2024-09-26 00:39:00 | TERRA_M-M | ITIRAPINA | SÃO PAULO | Brasil | 3523602 | 35 | 33 | nan | nan | nan | Cerrado | 16.6 |
| 824212d4-f13c-3c6e-91c9-2fa4c9a17d2a | -22.34217 | -47.75626 | 2024-09-26 00:39:00 | TERRA_M-M | IPEÚNA | SÃO PAULO | Brasil | 3521101 | 35 | 33 | nan | nan | nan | Cerrado | 19.8 |
| 2f01d3a0-f85c-3b2a-b778-c12301dfdce5 | -22.24545 | -43.91282 | 2024-09-26 00:39:00 | TERRA_M-M | VALENÇA | RIO DE JANEIRO | Brasil | 3306107 | 33 | 33 | nan | nan | nan | Mata Atlântica | 6.8 |


[Clique aqui para ver as próximas entradas](README9.md)
