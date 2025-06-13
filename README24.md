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

## Dados Diários - Página 24

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0819ab95-39e8-38a8-bf86-6b4f6900caed | -10.9353 | -56.8522 | 2025-06-13 13:20:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 132.4 |
| dc382cd3-e0d9-3542-a303-134de0e92d2d | -12.518 | -57.183 | 2025-06-13 13:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 94.9 |
| fc2f2cd2-f9b1-3747-8ca1-c25198d84134 | -14.0783 | -53.4042 | 2025-06-13 13:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 113.6 |
| bb2ce54a-b2da-3eed-9a2a-a942cd15148d | -7.6485 | -43.6343 | 2025-06-13 13:20:00 | GOES-19 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 95.9 |
| b2bcc26a-8bef-3b30-9b49-601b36a9708b | -10.8696 | -54.2947 | 2025-06-13 13:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 69.6 |
| fdd97a28-a634-3415-b989-6bac37e597a5 | -11.8963 | -47.4537 | 2025-06-13 13:20:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 87.9 |
| 9b087fa7-8e66-3480-a99a-54862a0f8ed7 | -10.9167 | -56.8336 | 2025-06-13 13:20:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 182.7 |
| 6ea243a5-a4d9-335b-afc4-bfcbf09bdfb6 | -11.5779 | -44.8413 | 2025-06-13 13:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 131.7 |
| e33058e7-3ac2-3314-8aa8-8c76988e3b58 | -11.1919 | -47.3896 | 2025-06-13 13:20:00 | GOES-19 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 69.4 |
| 8c8b2fa0-cacf-34fe-9f4e-55d5999c5c60 | -12.4645 | -58.5603 | 2025-06-13 13:30:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 72.0 |
| e6e20047-556e-3343-a4cf-8ab865e21bfa | -12.518 | -57.183 | 2025-06-13 13:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 109.0 |
| 7881ddd4-5d50-3a82-8b84-9adb62720c9e | -10.8696 | -54.2947 | 2025-06-13 13:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 72.0 |
| 5f7134bf-d3a6-33f9-a5dd-27441e5ec030 | -8.7996 | -45.0815 | 2025-06-13 13:30:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 94.6 |
| 0402b004-7ea7-3d40-a937-d17068d2311e | -12.5177 | -57.2031 | 2025-06-13 13:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 95.4 |
| cdf3131d-e2d0-357a-bf90-4db783863d79 | -11.5779 | -44.8413 | 2025-06-13 13:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 119.9 |
| 7fa87d2c-10ed-38a9-a252-ff4cdc081ddd | -11.8963 | -47.4537 | 2025-06-13 13:30:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 83.8 |
| 2ee75306-fa8c-3925-b7a8-844e0649d42c | -14.0783 | -53.4042 | 2025-06-13 13:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 143.6 |
| 256c5ae5-63f4-39ae-8e45-21575a21aff6 | -14.0783 | -53.4042 | 2025-06-13 13:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 138.0 |
| 2046fd50-6d79-3d81-9130-80cfdd8fcd1b | -12.4645 | -58.5603 | 2025-06-13 13:40:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 93.3 |
| 2d36e2ec-8517-35c0-be10-152748470dc9 | -10.8696 | -54.2947 | 2025-06-13 13:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 82.2 |
| 963a4d2a-58cb-3c4b-ade2-b8a3db31c545 | -12.5177 | -57.2031 | 2025-06-13 13:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 98.9 |
| 5945270c-ed99-39d9-9d1f-50b574e3ed0b | -11.8963 | -47.4537 | 2025-06-13 13:40:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 95.9 |
| fa3ed344-54e4-3070-b326-a1e424dd0aed | -12.518 | -57.183 | 2025-06-13 13:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 167.3 |
| 33caef24-f40e-3661-84af-7d8a2dcd3ff1 | -11.5779 | -44.8413 | 2025-06-13 13:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 90.6 |
| 417591ff-acdd-3549-8ede-2be261426971 | -7.6485 | -43.6343 | 2025-06-13 13:40:00 | GOES-19 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 146.6 |
| 9e6ea964-43ee-344d-ab7b-0d2d95045fbe | -11.8963 | -47.4537 | 2025-06-13 13:50:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 90.3 |
| a47ec06f-3b37-3042-9d95-2e4accb37b94 | -7.6485 | -43.6343 | 2025-06-13 13:50:00 | GOES-19 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 129.0 |
| a7f3a3aa-1c39-3a66-b268-85b1a35087e6 | -12.518 | -57.183 | 2025-06-13 13:50:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 192.8 |
| dc1befd5-9305-39d3-9f8a-0fe50e2bbc78 | -12.4645 | -58.5603 | 2025-06-13 13:50:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 91.3 |
| 5eefa60a-c12e-330e-833f-6cf52193da40 | -10.8696 | -54.2947 | 2025-06-13 13:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 108.2 |
| 7b69353d-e834-3429-b373-017c9c0fe375 | -12.5177 | -57.2031 | 2025-06-13 13:50:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 134.1 |
| fe7e2aa1-1618-3ce9-a0d9-41929425c8dc | -14.0328 | -55.13 | 2025-06-13 13:50:00 | GOES-19 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 61.7 |
| 04468d47-2f7e-3f9c-b10f-fc2cd0825e47 | -14.0783 | -53.4042 | 2025-06-13 13:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 132.0 |
| 58ba017d-9d38-37eb-9431-554927dd9434 | -11.5779 | -44.8413 | 2025-06-13 13:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 84.7 |
| f8aed2fb-b69a-3031-8674-79ad8651c551 | -11.9088 | -57.4732 | 2025-06-13 14:00:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 64.9 |
| ef5027bd-a805-3a45-9b9f-720a33db9920 | -14.0328 | -55.13 | 2025-06-13 14:00:00 | GOES-19 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 84.7 |
| 1f09d257-eaff-308a-84cf-76100bce5bef | -11.5779 | -44.8413 | 2025-06-13 14:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 85.6 |
| 5810e37a-9e0a-32ae-bbbb-7b4e5ee6ea22 | -12.518 | -57.183 | 2025-06-13 14:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 205.3 |
| c7a4553e-8b5d-3aa5-9af6-d9e0e7920306 | -13.9059 | -54.6291 | 2025-06-13 14:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 61.2 |
| 1baf3e86-acc9-3d69-98af-f49ac8e4f2c1 | -13.9056 | -54.6498 | 2025-06-13 14:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 65.8 |
| c23041e2-d20d-392a-bfe8-e102a63e7779 | -12.4645 | -58.5603 | 2025-06-13 14:00:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 143.4 |
| fad8ef37-c607-3263-aa05-ae0e1aa60a6e | -11.8963 | -47.4537 | 2025-06-13 14:00:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 98.7 |
| 9b5ce4b5-4763-30ce-a7f4-7178a4be1079 | -14.0783 | -53.4042 | 2025-06-13 14:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 145.0 |
| 72780a6d-6c13-34a4-943c-d4a95bc58cb1 | -10.8696 | -54.2947 | 2025-06-13 14:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 103.0 |
| 62a56bee-5b32-337f-b39f-3a62c857a1ef | -14.0328 | -55.13 | 2025-06-13 14:10:00 | GOES-19 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 92.6 |
| 002f1fb0-04d3-34f3-b268-6826461242bc | -14.0783 | -53.4042 | 2025-06-13 14:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 132.7 |
| c3768282-2973-38ca-8421-17af0d478be0 | -14.0331 | -55.1094 | 2025-06-13 14:10:00 | GOES-19 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 60.0 |
| ea2edd48-b508-3432-b272-866dd95a9569 | -11.9088 | -57.4732 | 2025-06-13 14:10:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 70.0 |
| ca903ea7-aecb-3a6e-a2aa-a655bea56b7b | -12.4645 | -58.5603 | 2025-06-13 14:10:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 195.0 |
| 3de80a09-1449-3e0e-9409-59630861d485 | -12.5177 | -57.2031 | 2025-06-13 14:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 118.6 |
| 2a82fcfe-7e23-3655-9a3d-49831329ce78 | -10.8696 | -54.2947 | 2025-06-13 14:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 118.8 |
| 29ab09c3-db54-3575-85df-fb9516afde1a | -11.9278 | -57.4717 | 2025-06-13 14:10:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 57.4 |
| 32094ea9-118f-31fe-97e2-e3651b9cba64 | -10.8694 | -54.3151 | 2025-06-13 14:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 63.3 |
| 62823785-c1f9-3526-97a6-0ccd4628185a | -11.8963 | -47.4537 | 2025-06-13 14:10:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 107.6 |
| 187a43eb-2394-3519-8509-f2654fca1ea1 | -13.9056 | -54.6498 | 2025-06-13 14:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 78.3 |
| fe7eeb35-9853-3424-a81d-da35ddd0d4a8 | -12.518 | -57.183 | 2025-06-13 14:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 216.9 |
| 0efe3e35-2c1b-31ce-8cb3-51db11d18dc6 | -13.9059 | -54.6291 | 2025-06-13 14:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 68.8 |
| 0e174ea6-caf7-32ab-b270-f968c5d2501c | -11.5779 | -44.8413 | 2025-06-13 14:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 77.5 |
| 910f0422-5341-3860-9465-2581e5acf3ba | -12.4645 | -58.5603 | 2025-06-13 14:20:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 259.1 |
| 226ab674-8499-3dd7-9ebf-7062552d3d18 | -14.0328 | -55.13 | 2025-06-13 14:20:00 | GOES-19 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 144.4 |
| 50ae9933-fa9a-3764-b551-7eb48e82f0cc | -13.9059 | -54.6291 | 2025-06-13 14:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 76.3 |
| 7055bc48-7dfd-3f06-87f9-d835908087f0 | -13.9056 | -54.6498 | 2025-06-13 14:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 81.6 |
| 71025704-559e-3610-b412-6f53029efce8 | -11.9088 | -57.4732 | 2025-06-13 14:20:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 67.4 |
| 3955bdc5-fe22-3609-9b68-f4b4e9b24294 | -14.0783 | -53.4042 | 2025-06-13 14:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 155.7 |
| 50a5a6d4-c32a-31fd-8bea-d7f2d705b511 | -10.8694 | -54.3151 | 2025-06-13 14:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 74.1 |
| 7b54b292-4984-38d4-b7cd-489a87c79e5b | -12.518 | -57.183 | 2025-06-13 14:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 214.2 |
| badaddc2-212e-3263-89fb-9823f87110ac | -11.8963 | -47.4537 | 2025-06-13 14:20:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 101.1 |
| 1b7bcb19-cbff-364d-9290-cbf69b2da1ac | -10.8696 | -54.2947 | 2025-06-13 14:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 121.2 |
| 8b18be00-bea7-38b2-baf7-f9a2f2677898 | -11.9278 | -57.4717 | 2025-06-13 14:20:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 65.7 |
| 627fd1b9-9af6-3600-bb51-c01f12f5b149 | -14.0331 | -55.1094 | 2025-06-13 14:20:00 | GOES-19 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 77.8 |
| 7ff99a11-e534-3d63-8e19-855b1ed95f52 | -12.4645 | -58.5603 | 2025-06-13 14:30:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 276.8 |
| 58368d94-c3a8-3160-9554-abb71c2f6c06 | -11.9091 | -57.4533 | 2025-06-13 14:30:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 57.1 |
| 7c81099c-423a-3ea2-a274-9e3cbf5b65d9 | -14.0331 | -55.1094 | 2025-06-13 14:30:00 | GOES-19 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 105.2 |
| 4e3f7f54-7070-3cbd-a597-5317b982f3a1 | -11.8963 | -47.4537 | 2025-06-13 14:30:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 82.2 |
| e888df78-f02b-3966-8631-92b26fcfa0fa | -14.0783 | -53.4042 | 2025-06-13 14:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 190.4 |
| a2746344-b6fc-3e3e-9890-a64351eaff91 | -11.9088 | -57.4732 | 2025-06-13 14:30:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 104.6 |
| cc8a3c84-5ad9-35e4-ae77-5fd285b48e13 | -10.8507 | -54.2963 | 2025-06-13 14:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 67.2 |
| cc6e8cf6-4452-38d7-8759-af05d776030a | -10.8694 | -54.3151 | 2025-06-13 14:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 62.8 |
| 5bf44350-c38d-3a83-8157-ee38024c8bc9 | -11.5779 | -44.8413 | 2025-06-13 14:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 74.0 |
| 85566703-b001-329a-8e2b-35de0cf7e31b | -14.0328 | -55.13 | 2025-06-13 14:30:00 | GOES-19 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 166.8 |
| 03c86aa5-6433-37fe-9694-4d3999e4d35e | -12.518 | -57.183 | 2025-06-13 14:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 180.8 |
| c68fa767-a27d-322e-9057-4d3dc85fb0e9 | -13.9059 | -54.6291 | 2025-06-13 14:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 77.2 |
| 4ae02468-bfdf-333f-84de-ac15e9337ac2 | -13.9056 | -54.6498 | 2025-06-13 14:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 72.4 |
| b8441759-0ccc-39e6-acd1-c90b41440c68 | -10.8696 | -54.2947 | 2025-06-13 14:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 128.3 |


