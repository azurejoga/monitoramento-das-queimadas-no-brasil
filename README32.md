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
| 6053dce2-d5ed-38a4-a2d0-c8f55a1f0238 | -21.281799 | -48.8797 | 2024-10-04 01:26:08 | METOP-B | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 040c29b1-d891-3a7a-8c1f-9dbb40c6c2e0 | -21.288 | -48.901501 | 2024-10-04 01:26:08 | METOP-B | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 53ae38a4-6723-30f2-8eb2-b6c5ef146799 | -21.278999 | -48.8326 | 2024-10-04 01:26:08 | METOP-B | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 3825ac0d-7026-3454-b4f1-f72ad41ea3c3 | -11.6932 | -64.9785 | 2024-10-04 01:26:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 79.9 |
| 9f1594f1-f2c6-3410-9241-b5f7581218e6 | -11.712 | -64.9777 | 2024-10-04 01:26:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 66.2 |
| 7f94f2c1-0e31-3a37-a0c9-dd814e24eabd | -11.8052 | -56.6024 | 2024-10-04 01:26:13 | GOES-16 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 71.4 |
| 39b8b8fa-c7bb-3333-a411-f843cf97ebc7 | -11.8242 | -56.6009 | 2024-10-04 01:26:13 | GOES-16 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 117.4 |
| 5ecd1955-6b56-3a6b-b4ac-635f1e4ec7be | -11.8244 | -56.5808 | 2024-10-04 01:26:13 | GOES-16 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 65.5 |
| c82a263e-5361-39c4-b13a-32bb81c06e09 | -12.4225 | -63.019 | 2024-10-04 01:26:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 95.4 |
| aa9acb39-e43c-3b38-8908-2c71fa8d0b9b | -12.4227 | -62.9999 | 2024-10-04 01:26:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 73.6 |
| d0c1e4cc-7170-39c5-9293-377c40c61d24 | -12.4414 | -63.018 | 2024-10-04 01:26:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 54.0 |
| b9b46d35-df14-3244-af42-09e50aaccd63 | -12.4416 | -62.9988 | 2024-10-04 01:26:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 55.0 |
| a7ec032b-c7a2-3c3e-ac58-147d6fed197b | -12.5711 | -53.1171 | 2024-10-04 01:26:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 88.2 |
| 25ce5b26-8bd0-3fae-92a8-dcbf490321e6 | -12.5898 | -53.1359 | 2024-10-04 01:26:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 160.8 |
| 36f35409-6b2a-3750-b1fc-1d7a87e25a90 | -12.5901 | -53.115 | 2024-10-04 01:26:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 297.7 |
| 52077d92-cf2f-3dc6-b319-427edc6bb4d5 | -12.6092 | -53.1129 | 2024-10-04 01:26:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 130.1 |
| 288ab439-34c4-36ad-bd8c-9bb8d3f7896a | -12.6295 | -63.1225 | 2024-10-04 01:26:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 119.3 |
| a435a9fc-1643-3a04-9801-1ee38cbaf480 | -12.6296 | -63.1033 | 2024-10-04 01:26:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 106.3 |
| a5c8fee3-f379-304f-a25a-f5addfeb8b87 | -12.6484 | -63.1214 | 2024-10-04 01:26:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 78.0 |
| c5c0fa6c-beb1-3962-ad88-9532d5b17618 | -12.6486 | -63.1022 | 2024-10-04 01:26:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 90.8 |
| f5a2a6d2-139d-37bd-81c3-1f5d966d4ef4 | -12.7256 | -62.925 | 2024-10-04 01:26:19 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 62.8 |
| 9beb9610-524f-3735-8b5e-3c7e5dedb724 | -12.8049 | -62.497 | 2024-10-04 01:26:19 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 60.4 |
| 14ffb8b5-f99c-3493-bff5-7a9a06f606cd | -12.8051 | -62.4777 | 2024-10-04 01:26:19 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 81.9 |
| d39f40bf-686c-30a6-8c90-c141ab35af5a | -12.8238 | -62.4959 | 2024-10-04 01:26:19 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 53.9 |
| 990d5999-d580-3181-8a80-27bd2c144922 | -12.824 | -62.4766 | 2024-10-04 01:26:19 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 92.5 |
| f927da20-686d-38de-81f8-679fcdb0600a | -12.9831 | -51.129 | 2024-10-04 01:26:19 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 159.2 |
| c030acd6-87c9-34e7-bbd8-771624c5766d | -12.881 | -62.4538 | 2024-10-04 01:26:19 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 56.6 |
| 1af4555b-b1de-3c7e-898a-f24049ab5757 | -13.1254 | -46.3063 | 2024-10-04 01:26:20 | GOES-16 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 59.6 |
| 49963f5d-9eb4-325e-9006-0c5c6a3b096b | -13.1447 | -46.3033 | 2024-10-04 01:26:20 | GOES-16 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 70.1 |
| 8eea3af6-7332-3201-a66e-64cdb86f9f78 | -12.8999 | -62.4527 | 2024-10-04 01:26:20 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 49.8 |
| d50b7150-53fb-34e1-933a-0fa3e2b10a92 | -12.9186 | -62.4901 | 2024-10-04 01:26:20 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 76.4 |
| fa2fde37-216a-39b0-824a-f722862fdce7 | -12.9187 | -62.4708 | 2024-10-04 01:26:20 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 62.3 |
| 9d200f5b-8360-3eda-ade0-06afbfc514b3 | -13.0598 | -51.1195 | 2024-10-04 01:26:20 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 81.4 |
| 17d71e78-cee2-385b-8629-dc258b72eed2 | -13.0786 | -51.1385 | 2024-10-04 01:26:20 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 143.1 |
| 475c6b63-636d-3ad0-8aa9-300840be8d96 | -13.0975 | -51.1575 | 2024-10-04 01:26:20 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 98.9 |
| aa032345-9609-393d-9942-9c42cb280367 | -13.1163 | -51.1765 | 2024-10-04 01:26:20 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 85.2 |
| 5306b854-0367-346c-9fcc-d3de695f3980 | -13.1166 | -51.1551 | 2024-10-04 01:26:20 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 142.3 |
| 60c0befe-c3e4-300d-90a9-3a26fb58eb51 | -14.004 | -44.0201 | 2024-10-04 01:26:24 | GOES-16 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 92.3 |
| d5fb38a9-d5df-3f4f-a893-3945af7cd189 | -19.974501 | -48.679401 | 2024-10-04 01:26:28 | METOP-B | PIRAJUBA | MINAS GERAIS | Brasil | 3150703 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| d754c396-6550-36b8-b031-39b0e3128a29 | -14.7744 | -48.0307 | 2024-10-04 01:26:29 | GOES-16 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 86.6 |
| 6c42eb4e-a260-360f-aa2e-4ae6f6e83903 | -14.7939 | -48.0275 | 2024-10-04 01:26:29 | GOES-16 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 155.6 |
| 3325da93-584a-3928-b060-5a93c0b9b82d | -14.7944 | -48.005 | 2024-10-04 01:26:29 | GOES-16 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 84.0 |
| 88cfde77-ebef-3a33-b0e9-f52732187acd | -16.0929 | -50.2983 | 2024-10-04 01:26:36 | GOES-16 | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | 80.5 |
| f46f81b4-92c3-30c1-a61a-4162abb3feeb | -16.0933 | -50.2763 | 2024-10-04 01:26:36 | GOES-16 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 90.1 |
| ce921d84-c683-3ee6-8916-c8a7cb72aae1 | -16.5928 | -57.2397 | 2024-10-04 01:26:39 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 66.8 |
| 72006f81-3e56-398d-a40d-551901d00e6c | -16.4148 | -57.4028 | 2024-10-04 01:26:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 59.4 |
| f0a5ec80-2a7a-366b-a924-7a500ccb6d6c | -16.4151 | -57.3823 | 2024-10-04 01:26:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 65.7 |
| da74a970-e397-3f10-808f-955e82ec5ed9 | -16.573 | -57.2624 | 2024-10-04 01:26:39 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 79.0 |
| 6b425f0c-bf33-3901-85d5-b0df31939680 | -16.5733 | -57.2419 | 2024-10-04 01:26:39 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 94.7 |
| 907ec10f-e5d5-33bf-a2c8-4b718af495d2 | -16.5736 | -57.2215 | 2024-10-04 01:26:39 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 67.9 |
| e28d964e-dc37-3b01-947f-4d518ea8a5ef | -16.5783 | -58.198 | 2024-10-04 01:26:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 51.8 |
| 77a8e364-bab0-3228-a430-b8cc089de365 | -16.5925 | -57.2602 | 2024-10-04 01:26:39 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 67.2 |
| a80f6d05-a5cf-356c-ac8e-df9718a1efdb | -16.5935 | -57.1988 | 2024-10-04 01:26:39 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 63.1 |
| b8909499-8083-3aaa-a944-50f23d58822c | -16.5938 | -57.1783 | 2024-10-04 01:26:39 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 84.4 |
| 91931235-b46d-38f8-8c13-30474c102fe1 | -16.613 | -57.1965 | 2024-10-04 01:26:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 98.5 |
| 38612a06-c3c6-3a88-b7b4-4a4de010de53 | -16.6133 | -57.176 | 2024-10-04 01:26:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 133.5 |
| 8d440ee8-1f50-34e5-8ce6-bb72cb2d2032 | -16.7606 | -57.7512 | 2024-10-04 01:26:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 64.5 |
| b518e918-68fa-377a-a9fc-375a25603331 | -21.399 | -57.221001 | 2024-10-04 01:26:40 | METOP-B | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| d63756a7-7ee5-3394-904c-b219996736be | -16.9283 | -55.8405 | 2024-10-04 01:26:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 85.5 |
| 1433151b-d627-3d3f-ba22-31fe421888c6 | -16.9287 | -55.8197 | 2024-10-04 01:26:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 61.9 |
| 33175a5f-0f7e-348f-ab5f-a6c7c8e0db16 | -16.779 | -57.8306 | 2024-10-04 01:26:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 51.6 |
| 6a008a2f-cdf9-3d50-ab53-9063f6a5705e | -16.7859 | -57.3811 | 2024-10-04 01:26:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 81.6 |
| e955c964-f16e-36b4-bc0f-a63e0426e096 | -16.7985 | -57.8284 | 2024-10-04 01:26:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 49.1 |
| 6f1c520a-ebdc-3960-b45b-ae7fc84d9624 | -16.8055 | -57.3788 | 2024-10-04 01:26:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 64.3 |
| bc4ee7c1-2f0d-33c7-a931-14559b1445a4 | -16.843 | -57.4767 | 2024-10-04 01:26:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 49.6 |
| 3135d323-282b-3d6f-8410-02b474379195 | -16.9087 | -55.843 | 2024-10-04 01:26:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 65.9 |
| 2c16957d-5e65-30ce-a25a-2552e42c20a0 | -17.0616 | -56.0723 | 2024-10-04 01:26:42 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 51.5 |
| a8f517a8-69f2-3a3f-abd7-4ce761b33076 | -17.3844 | -42.6235 | 2024-10-04 01:26:42 | GOES-16 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 97.1 |
| 2a59b575-a6c9-3a81-aa37-4fe432410768 | -17.5339 | -46.7472 | 2024-10-04 01:26:43 | GOES-16 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 70.6 |
| 24a4c232-129d-32cf-a4f3-c164a65ab6f0 | -17.5344 | -46.7239 | 2024-10-04 01:26:43 | GOES-16 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 77.1 |
| 6a305714-d81e-3499-9803-953a339a2857 | -18.8406 | -42.9235 | 2024-10-04 01:26:50 | GOES-16 | GUANHÃES | MINAS GERAIS | Brasil | 3128006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 77.4 |
| e35f7759-132d-3cb2-9f96-38c2fa89ea5b | -18.8413 | -42.8985 | 2024-10-04 01:26:50 | GOES-16 | GUANHÃES | MINAS GERAIS | Brasil | 3128006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 100.9 |
| ae923fc6-c8dc-3815-a0cc-8d3f57aedb0c | -18.8609 | -42.9182 | 2024-10-04 01:26:50 | GOES-16 | GUANHÃES | MINAS GERAIS | Brasil | 3128006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 108.1 |
| da381802-135b-3ff2-b37a-445e4ffa285c | -18.8617 | -42.8932 | 2024-10-04 01:26:50 | GOES-16 | GUANHÃES | MINAS GERAIS | Brasil | 3128006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 135.2 |
| 426a7cb7-e76c-352b-8510-6a33a174eff0 | -18.8613 | -43.5837 | 2024-10-04 01:26:50 | GOES-16 | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 118.7 |
| a732ccea-037c-3f1d-9fae-cad34e8eca2a | -19.0148 | -43.1749 | 2024-10-04 01:26:51 | GOES-16 | CARMÉSIA | MINAS GERAIS | Brasil | 3113800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 79.4 |
| fc257081-e76d-36fc-8119-bc8eb9958870 | -19.2794 | -43.795 | 2024-10-04 01:26:52 | GOES-16 | BALDIM | MINAS GERAIS | Brasil | 3105004 | 31 | 33 | nan | nan | nan | Cerrado | 152.6 |
| 9bf50701-665f-3e6a-9ac2-363f508c2b02 | -19.2801 | -43.7703 | 2024-10-04 01:26:52 | GOES-16 | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 137.5 |
| 2edcff79-ec33-3905-85a4-7fe8c4cb5266 | -19.2998 | -43.7897 | 2024-10-04 01:26:52 | GOES-16 | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 213.6 |
| f147df82-1154-3f0b-9d82-1b311b2b6c0e | -19.3005 | -43.765 | 2024-10-04 01:26:52 | GOES-16 | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 193.1 |
| 633ee59f-1707-301d-96e4-0678f5bece8f | -19.4899 | -42.8746 | 2024-10-04 01:26:53 | GOES-16 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 104.4 |
| 6e7fc46c-c107-3fcc-bc81-c75e08f45c41 | -19.5104 | -42.8691 | 2024-10-04 01:26:53 | GOES-16 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 81.2 |
| f77ad495-3c1a-3a5b-b894-0b578588b4ac | -20.1036 | -43.4276 | 2024-10-04 01:26:56 | GOES-16 | CATAS ALTAS | MINAS GERAIS | Brasil | 3115359 | 31 | 33 | nan | nan | nan | Mata Atlântica | 75.3 |
| 296a1ccf-8580-3af5-ace3-2b306429c7b5 | -19.9907 | -48.6913 | 2024-10-04 01:26:57 | GOES-16 | PLANURA | MINAS GERAIS | Brasil | 3151602 | 31 | 33 | nan | nan | nan | Cerrado | 75.2 |
| fc1b83fd-9f4c-3537-8a58-d40533e9887c | -20.0111 | -48.6869 | 2024-10-04 01:26:57 | GOES-16 | PLANURA | MINAS GERAIS | Brasil | 3151602 | 31 | 33 | nan | nan | nan | Cerrado | 85.0 |
| e6b08959-5d51-3b90-aa61-ddc06154bfdc | -20.4591 | -43.1795 | 2024-10-04 01:26:58 | GOES-16 | DIOGO DE VASCONCELOS | MINAS GERAIS | Brasil | 3121704 | 31 | 33 | nan | nan | nan | Mata Atlântica | 130.2 |
| f4ed5204-0b41-3e75-bfe7-dc27fcb11ef1 | -17.5124 | -46.7103 | 2024-10-04 01:26:58 | METOP-B | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 53cb4f19-bef7-315d-9b90-ac10caca29d6 | -17.502899 | -46.713299 | 2024-10-04 01:26:58 | METOP-B | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| a13673ae-d316-392b-b5a9-0c748003e528 | -21.3534 | -48.8229 | 2024-10-04 01:27:04 | GOES-16 | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Mata Atlântica | 92.5 |
| eae30b3c-c32a-32cc-936f-5bfff5b558d0 | -21.3541 | -48.7996 | 2024-10-04 01:27:04 | GOES-16 | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Mata Atlântica | 107.2 |
| e951a215-dcc5-33ea-9f46-eaa91e45436f | -21.7981 | -48.3926 | 2024-10-04 01:27:06 | GOES-16 | GAVIÃO PEIXOTO | SÃO PAULO | Brasil | 3516853 | 35 | 33 | nan | nan | nan | Cerrado | 92.7 |
| 672c00d8-94b1-3a78-b709-00a76568a302 | -21.7988 | -48.3691 | 2024-10-04 01:27:06 | GOES-16 | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | 115.2 |
| fdff7fc5-b39b-3d5c-93f9-3c19bf72d368 | -21.8175 | -48.4346 | 2024-10-04 01:27:06 | GOES-16 | GAVIÃO PEIXOTO | SÃO PAULO | Brasil | 3516853 | 35 | 33 | nan | nan | nan | Cerrado | 97.4 |
| 58a08796-fbca-3481-be19-8259eca87304 | -21.8189 | -48.3876 | 2024-10-04 01:27:06 | GOES-16 | GAVIÃO PEIXOTO | SÃO PAULO | Brasil | 3516853 | 35 | 33 | nan | nan | nan | Cerrado | 92.8 |
| b2355562-b6d8-38ef-a76d-68e7312e476c | -21.8196 | -48.3641 | 2024-10-04 01:27:06 | GOES-16 | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | 142.0 |
| 9be20392-e176-3447-a2d9-2cae0593dae7 | -21.8383 | -48.4296 | 2024-10-04 01:27:06 | GOES-16 | GAVIÃO PEIXOTO | SÃO PAULO | Brasil | 3516853 | 35 | 33 | nan | nan | nan | Cerrado | 109.2 |
| ab9b5db3-867b-3180-8b54-9be071eaed3a | -18.686399 | -57.286499 | 2024-10-04 01:27:24 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 839c7232-b32a-3e1d-9980-f3c2fa839a80 | -17.054399 | -56.069099 | 2024-10-04 01:27:46 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| b10154d9-23fe-32c6-ae51-357b8a276a4e | -17.0446 | -56.071602 | 2024-10-04 01:27:46 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 2752c71d-83ec-3ff3-b64a-d6a18167ad81 | -16.9226 | -55.823002 | 2024-10-04 01:27:47 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |


[Clique aqui para ver as próximas entradas](README33.md)
