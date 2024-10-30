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

## Dados Diários - Página 98

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2b551777-284c-3bbf-a4f1-0779ccc79220 | -2.833 | -49.2413 | 2024-10-30 05:35:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 39.4 |
| c59a9a61-cda3-3f06-ba68-a0d27b9ba812 | -3.0734 | -54.167 | 2024-10-30 05:35:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 44.3 |
| 253022de-f3fd-38c9-8451-f9f3dfb30d3a | -3.1097 | -54.2865 | 2024-10-30 05:35:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 43.0 |
| 4d6c9750-4024-32f4-91d4-96c56c71dbcb | -3.1098 | -54.2665 | 2024-10-30 05:35:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 41.7 |
| d3e80f7b-29c5-3ccb-b2e7-c3fc02f0d5ba | -3.2719 | -50.3473 | 2024-10-30 05:35:25 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 95.4 |
| 2b7cc1bc-3bce-3463-9054-780e0528c3ee | -3.2534 | -50.3689 | 2024-10-30 05:35:25 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 32.7 |
| 72d47421-af62-3b3d-971d-45180204f00d | -3.2535 | -50.3479 | 2024-10-30 05:35:25 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 120.2 |
| 32d3f479-5fd2-328e-8f8e-c5b873c1f374 | -3.2718 | -50.3683 | 2024-10-30 05:35:25 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 27.0 |
| f5502860-7860-31cf-b7f1-f93d27ff4b07 | -3.5631 | -47.3847 | 2024-10-30 05:35:26 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 38.6 |
| da15866b-2dcd-38a3-a093-6cee8c99a6cb | -3.5817 | -47.384 | 2024-10-30 05:35:26 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 29.3 |
| e6919c49-0f2c-3057-951b-6766e4c41491 | -3.9486 | -48.1291 | 2024-10-30 05:35:28 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 29.8 |
| a19f499a-5678-3a8e-b9a9-b2e177b25751 | -4.0681 | -50.024 | 2024-10-30 05:35:29 | GOES-16 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 42.5 |
| 2bf5c18b-529e-3d1f-becd-35b51893572b | -4.0682 | -50.0029 | 2024-10-30 05:35:29 | GOES-16 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 40.5 |
| 3143e127-ee81-3d0a-9401-bde9a1c678c2 | -4.2749 | -43.4357 | 2024-10-30 05:35:30 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 61.0 |
| 3bbe5aab-ac5d-3a0b-b891-14656a247f35 | -4.2496 | -50.6677 | 2024-10-30 05:35:30 | GOES-16 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 57.4 |
| 2747746a-319f-38a8-9128-8f903a7e2358 | -4.2681 | -50.6669 | 2024-10-30 05:35:30 | GOES-16 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 66.0 |
| 52bf53b3-9a0b-3a21-a774-e76a999fa17b | 1.7483 | -55.8428 | 2024-10-30 05:44:56 | GOES-16 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 45.3 |
| 0845ab57-9a41-3c12-a03a-d4dad0f36dce | -2.833 | -49.2413 | 2024-10-30 05:45:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 52.8 |
| 89eb4aaa-eca5-3404-8ee5-7e11321068e7 | -3.1097 | -54.2865 | 2024-10-30 05:45:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 44.5 |
| 33c83575-7fbf-36d7-8694-43607fee3989 | -3.1098 | -54.2665 | 2024-10-30 05:45:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 40.0 |
| 22553c72-30f6-3999-9f43-3c0ee3c5da56 | -3.1281 | -54.266 | 2024-10-30 05:45:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 39.4 |
| 318f050a-b55e-3615-a224-bb8cfb578c48 | -3.2534 | -50.3689 | 2024-10-30 05:45:25 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 26.6 |
| 3a4138df-6237-3916-8815-fea5ca370bb4 | -3.2535 | -50.3479 | 2024-10-30 05:45:25 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 101.9 |
| 8a4165d4-fd08-3924-a858-ef9deeee0d7f | -3.2718 | -50.3683 | 2024-10-30 05:45:25 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 25.9 |
| 71f21c96-3664-3290-8131-aaff2c9a028d | -3.2719 | -50.3473 | 2024-10-30 05:45:25 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 93.6 |
| c48d828f-0c79-3372-8b04-2d42d3d99fa9 | -3.5817 | -47.384 | 2024-10-30 05:45:26 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 29.0 |
| e7982ea8-ebba-3674-8175-ded5305bec1b | -3.9486 | -48.1291 | 2024-10-30 05:45:28 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 32.7 |
| 7bb9b8a6-13d7-342d-a804-94de2c3c1b96 | -4.0681 | -50.024 | 2024-10-30 05:45:29 | GOES-16 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 37.5 |
| 9df5a324-3ec5-319b-8146-21eba93f2970 | -4.2748 | -43.4589 | 2024-10-30 05:45:30 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 58.3 |
| 777a1ce4-b829-3269-aaad-852c58e593fd | -4.2749 | -43.4357 | 2024-10-30 05:45:30 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 68.9 |
| 36c5cf48-a722-3117-a6c8-6e88707394d0 | -4.2496 | -50.6677 | 2024-10-30 05:45:30 | GOES-16 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 51.3 |
| b5e1c58b-4567-3a6a-b761-30fe018ff105 | -4.2681 | -50.6669 | 2024-10-30 05:45:30 | GOES-16 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 77.5 |
| ab186d14-8333-33f7-9227-87635457ce70 | -2.833 | -49.2413 | 2024-10-30 05:55:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 46.3 |
| e11c129c-98d2-3c6f-92f0-16c771d97a80 | -3.0913 | -54.287 | 2024-10-30 05:55:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 45.5 |
| 5619ebf7-af76-309c-9f4c-a0826056f70b | -3.1097 | -54.2865 | 2024-10-30 05:55:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 49.3 |
| 44f110bf-04d5-3483-91e7-ef3efda338d2 | -3.1098 | -54.2665 | 2024-10-30 05:55:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 44.7 |
| 02b541e8-1672-3826-9559-436f848f1b93 | -3.1281 | -54.266 | 2024-10-30 05:55:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 45.7 |
| 86bc809e-dd69-3833-ada6-7387a9709938 | -3.2534 | -50.3689 | 2024-10-30 05:55:25 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 29.6 |
| 9fb40d96-5f8c-3737-871e-1fc09d13ce10 | -3.2535 | -50.3479 | 2024-10-30 05:55:25 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 96.2 |
| 1e77dee6-69c0-352e-9f4f-9b78aa6e424d | -3.2718 | -50.3683 | 2024-10-30 05:55:25 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 38.9 |
| 4df7d46b-b187-39f7-b22b-3d4040950f54 | -3.2719 | -50.3473 | 2024-10-30 05:55:25 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 107.3 |
| d39eb586-c979-3a2d-83df-1bf362608727 | -4.2748 | -43.4589 | 2024-10-30 05:55:30 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 51.0 |
| f45f1bfa-95e5-3b00-9f4d-bea8b459ecab | -4.2749 | -43.4357 | 2024-10-30 05:55:30 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 69.0 |
| cf891655-a355-3760-bb19-f09c85381bf3 | -4.2681 | -50.6669 | 2024-10-30 05:55:30 | GOES-16 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 77.0 |
| afcfedde-4c2f-3943-84e0-8c8b5b442882 | 3.55999 | -61.8405 | 2024-10-30 05:57:00 | NOAA-21 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3e449826-8148-331d-be8a-6cd0ad5066cc | 3.17961 | -64.20753 | 2024-10-30 05:59:00 | NOAA-21 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6070a2e4-b326-3d0d-b548-94f1b027fb15 | 3.17592 | -64.20815 | 2024-10-30 05:59:00 | NOAA-21 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 1a4e2af3-bacb-36a0-926b-0d52af547101 | 2.02662 | -61.2301 | 2024-10-30 05:59:00 | NOAA-21 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2ca40155-53ad-3db1-8ff0-0572212cd32b | 1.74979 | -55.84565 | 2024-10-30 05:59:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| a2a10b58-59a6-391b-b2f4-14806eaf4f4a | 1.74917 | -55.84622 | 2024-10-30 05:59:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 43406146-1037-3b93-b682-979d7fd00303 | 1.74889 | -55.83998 | 2024-10-30 05:59:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| f9eb5315-bdde-3fbe-baef-1d641ed554cc | 1.74822 | -55.84056 | 2024-10-30 05:59:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 73c54185-f931-3af1-9422-93a9fbc1ab71 | 1.6904 | -55.81032 | 2024-10-30 05:59:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e72e3f5a-34f4-3f4b-a9e8-f82a3193d0ab | 1.68295 | -55.80592 | 2024-10-30 05:59:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2e6c1e83-27c4-329f-a2fc-26c38318ef53 | 1.67538 | -55.84172 | 2024-10-30 05:59:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 13.4 |
| 8b90aee4-bd63-351d-a483-e27a27f21dba | 1.67069 | -55.85399 | 2024-10-30 05:59:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 0984810c-07b3-314d-957e-c6fa1460901d | 1.66885 | -55.84284 | 2024-10-30 05:59:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 32c070b4-cff7-3425-9662-a1bc9569e676 | 1.60117 | -55.62597 | 2024-10-30 05:59:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5769d714-483c-30ed-804f-d71546c7171e | 1.59933 | -55.62745 | 2024-10-30 05:59:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| cd74c103-0a37-3ffb-8a4d-775dea005ba3 | 1.59837 | -55.62166 | 2024-10-30 05:59:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 51c5f5c6-c4da-354f-81ca-e1eae07c503f | 1.59453 | -55.62703 | 2024-10-30 05:59:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 37d0e3c9-e3c3-3f8a-9292-6bdd3ce99e3b | 1.12744 | -59.4458 | 2024-10-30 05:59:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e1eac1ab-03d7-3fc6-a0dd-71bcccb323d8 | 1.12693 | -59.44267 | 2024-10-30 05:59:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0096d2a5-de94-3c15-b0ba-d506017d4fb7 | 1.12649 | -59.44361 | 2024-10-30 05:59:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a5061795-616c-367b-a3df-a2109b1ce3ee | 1.126 | -59.44046 | 2024-10-30 05:59:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 849011f5-72e8-3105-9a4c-06115e45e792 | 1.1217 | -59.4435 | 2024-10-30 05:59:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0f85305f-a0f3-3888-8aac-9e52b60eea8d | 0.99442 | -59.45831 | 2024-10-30 05:59:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 22c35cea-dbbd-3269-9133-91462561bad6 | 0.92461 | -59.55713 | 2024-10-30 05:59:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 45cb1a1f-b8ed-354a-b6cd-b37c1a605b1d | 0.92346 | -59.55657 | 2024-10-30 05:59:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7b8115f3-c9aa-3fbf-af21-5b696c072df6 | 0.63803 | -59.62054 | 2024-10-30 05:59:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 97f1abf8-fa62-340a-888a-8d680eff43e3 | 0.63752 | -59.61738 | 2024-10-30 05:59:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d578bcbe-8b60-3af2-b750-a148a602e0e1 | 0.12205 | -62.58925 | 2024-10-30 05:59:00 | NOAA-21 | BARCELOS | AMAZONAS | Brasil | 1300409 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b65e589c-96ff-383b-bf73-7c27ae013dd3 | -3.55224 | -58.67554 | 2024-10-30 05:59:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b71e0bed-a182-38c2-8376-dcb8817859d6 | -3.55162 | -58.67984 | 2024-10-30 05:59:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7483d67f-5899-33b5-85e3-425e79ea7040 | -3.4969 | -59.29256 | 2024-10-30 05:59:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f8103b1c-9f62-3ba3-85b1-494bb295910a | -3.49123 | -59.29171 | 2024-10-30 05:59:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4260cd19-3532-3b67-af78-31fcef50b9b8 | -2.73495 | -57.47989 | 2024-10-30 05:59:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b049d797-af6c-3aa5-ac2c-d1c4a1148dc9 | -2.73184 | -57.47871 | 2024-10-30 05:59:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| a970759b-c23f-33b3-af61-cb0c4cf544d7 | -2.73107 | -57.48375 | 2024-10-30 05:59:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 6f583c6b-1500-33bb-be43-23ed497439ad | -2.72865 | -57.47886 | 2024-10-30 05:59:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ade126df-9b1d-345d-9a1b-1366e9b7907d | -2.72554 | -57.47773 | 2024-10-30 05:59:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 5c419e98-2ee5-31ce-bdb4-d9f7c0b773a6 | -2.72236 | -57.47786 | 2024-10-30 05:59:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 37d83f3d-70a9-3b1c-a2e1-6d62aeda4747 | -2.71848 | -57.48177 | 2024-10-30 05:59:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d8a907ce-3623-31dc-949d-c559a0a77dd4 | -2.08495 | -59.93256 | 2024-10-30 05:59:00 | NOAA-21 | PRESIDENTE FIGUEIREDO | AMAZONAS | Brasil | 1303536 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b700794f-9c53-36c4-93ee-7953c0c5613f | -1.42953 | -60.28839 | 2024-10-30 05:59:00 | NOAA-21 | PRESIDENTE FIGUEIREDO | AMAZONAS | Brasil | 1303536 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7f7fd76b-e189-3109-976c-b7f4a803f1e7 | -1.42703 | -60.28975 | 2024-10-30 05:59:00 | NOAA-21 | PRESIDENTE FIGUEIREDO | AMAZONAS | Brasil | 1303536 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2d9564b5-91f8-3f85-ac63-76548f600967 | -1.42483 | -60.28454 | 2024-10-30 05:59:00 | NOAA-21 | PRESIDENTE FIGUEIREDO | AMAZONAS | Brasil | 1303536 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 15f2843d-9ff7-3dab-b419-a4e2c05fe1df | -1.42438 | -60.28762 | 2024-10-30 05:59:00 | NOAA-21 | PRESIDENTE FIGUEIREDO | AMAZONAS | Brasil | 1303536 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 56fbec3f-79da-32d2-8064-d82eef3de933 | -1.42236 | -60.28592 | 2024-10-30 05:59:00 | NOAA-21 | PRESIDENTE FIGUEIREDO | AMAZONAS | Brasil | 1303536 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 8582a4b7-b940-37f7-93fc-8135add9c0c7 | -1.30154 | -55.72239 | 2024-10-30 05:59:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 838ff834-2889-3bdc-9376-d0206417c8f3 | -1.00673 | -62.7964 | 2024-10-30 05:59:00 | NOAA-21 | BARCELOS | AMAZONAS | Brasil | 1300409 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 2e9e6700-8d35-3f3f-a5a0-6f4a4676b7a5 | -0.77532 | -62.89112 | 2024-10-30 05:59:00 | NOAA-21 | BARCELOS | AMAZONAS | Brasil | 1300409 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1e14550a-d5c8-38b4-b698-fbbbbec46a39 | -0.77107 | -62.89046 | 2024-10-30 05:59:00 | NOAA-21 | BARCELOS | AMAZONAS | Brasil | 1300409 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 53438727-98a7-346c-ab11-3490370b2431 | -0.76868 | -62.87786 | 2024-10-30 05:59:00 | NOAA-21 | BARCELOS | AMAZONAS | Brasil | 1300409 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 0ba5bf79-3248-33cf-bcaa-9edba644147d | -0.7662 | -62.89375 | 2024-10-30 05:59:00 | NOAA-21 | BARCELOS | AMAZONAS | Brasil | 1300409 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 178fdb88-361b-32a5-a7e7-e267dc2937d9 | -0.76559 | -62.89772 | 2024-10-30 05:59:00 | NOAA-21 | BARCELOS | AMAZONAS | Brasil | 1300409 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| fba6cff1-a4a8-385c-8433-45d23c2df035 | -0.76319 | -62.88515 | 2024-10-30 05:59:00 | NOAA-21 | BARCELOS | AMAZONAS | Brasil | 1300409 | 13 | 33 | nan | nan | nan | Amazônia | 5.3 |
| b181f69b-2d73-39cd-9125-659b0fc430c8 | -0.76134 | -62.89705 | 2024-10-30 05:59:00 | NOAA-21 | BARCELOS | AMAZONAS | Brasil | 1300409 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1440be4a-0fc1-3aca-aaa6-0e43a859bb2f | -0.75771 | -62.89241 | 2024-10-30 05:59:00 | NOAA-21 | BARCELOS | AMAZONAS | Brasil | 1300409 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8e5460d8-7237-31b7-b1be-cd131185bdc0 | -0.75709 | -62.89637 | 2024-10-30 05:59:00 | NOAA-21 | BARCELOS | AMAZONAS | Brasil | 1300409 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |


[Clique aqui para ver as próximas entradas](README99.md)
