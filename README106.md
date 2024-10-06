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

## Dados Diários - Página 106

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e0740e9e-c7aa-3cf6-a59f-df4d91d5de50 | -12.56021 | -53.46963 | 2024-10-06 05:12:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a4e938ef-f23a-34bd-b2a0-0a3856325e43 | -12.55664 | -53.46534 | 2024-10-06 05:12:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 08e28341-be58-3016-b79c-f5a5eaa62bfc | -12.50789 | -53.5182 | 2024-10-06 05:12:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 69dd9c38-6167-3f6f-8753-889d16594f8f | -12.50739 | -53.52188 | 2024-10-06 05:12:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 6d219046-5bf5-3038-a7bf-79cbc5efd5ab | -12.5069 | -53.52555 | 2024-10-06 05:12:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 0.2 |
| 69e06b89-0564-34fb-8697-fd160fb82330 | -12.48432 | -53.14418 | 2024-10-06 05:12:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5dad669c-19b7-33ba-a01c-a5f454e37499 | -8.70508 | -54.827 | 2024-10-06 05:12:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ddfd5eec-8a73-37e5-89df-d0300ec26255 | -8.70199 | -54.83231 | 2024-10-06 05:12:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 02df8dc6-f278-3216-a026-6d2e76dfc418 | -8.62859 | -54.5741 | 2024-10-06 05:12:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a11202b3-9f16-3ff3-a2b4-e5313de5e4d5 | -8.70447 | -54.83123 | 2024-10-06 05:12:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a5a6353c-142d-3daa-b0ee-e586e3daf143 | -8.70262 | -54.82813 | 2024-10-06 05:12:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b8d8aab4-351d-31c4-9ee4-3cecd39392a8 | -10.69187 | -54.48543 | 2024-10-06 05:12:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b170f77f-d25a-3fc4-b319-77b63055e3d2 | -10.69121 | -54.48992 | 2024-10-06 05:12:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a0cec39a-ef8d-31dc-9913-2646f3e0e642 | -10.68814 | -54.48486 | 2024-10-06 05:12:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 56953563-1a3a-342c-a7b5-17168d314281 | -10.59288 | -54.34169 | 2024-10-06 05:12:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ea396a82-1bf8-33e0-b683-c11dde2ec3d1 | -12.15115 | -54.26832 | 2024-10-06 05:12:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c1aa7e96-a73f-3cc4-b0d2-4be81d42048c | -12.14974 | -54.26463 | 2024-10-06 05:12:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c17525f6-ffba-33db-ac22-2f74c73c6f47 | -12.14906 | -54.26959 | 2024-10-06 05:12:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7550e7fb-d6f2-38c5-ac0e-f9adaa0b8631 | -11.69557 | -54.55949 | 2024-10-06 05:12:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 356ebd43-f8f2-3399-8403-416e6450d544 | -11.69181 | -54.55891 | 2024-10-06 05:12:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b87f0dfc-4894-3d80-829c-114d9af8e8f7 | -11.65337 | -54.52739 | 2024-10-06 05:12:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 59c9e47b-f0da-30aa-8cd9-bd6fb5bc1a21 | -11.65269 | -54.53208 | 2024-10-06 05:12:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c80d14b7-3a93-3535-9970-575081fe091b | -11.65027 | -54.52215 | 2024-10-06 05:12:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 333a8861-1402-31b4-af97-a71bdca2b6a4 | -11.64959 | -54.52685 | 2024-10-06 05:12:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2e4b0591-01f5-349b-881c-2633c377f7c6 | -11.64892 | -54.53153 | 2024-10-06 05:12:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ed336f55-aef9-3d20-bfd0-cd778e182f82 | -11.64825 | -54.53621 | 2024-10-06 05:12:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0dbff311-f14d-3b4b-968e-087f0bbcf831 | -11.64582 | -54.5263 | 2024-10-06 05:12:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 0083d6a3-88a5-3b9b-8d53-443e19d5d024 | -11.64515 | -54.53098 | 2024-10-06 05:12:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| e7582d33-c4ee-3284-9370-dbdec1771b49 | -11.38344 | -54.35823 | 2024-10-06 05:12:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| edb929fe-1475-3dc1-9751-5fab0114f6cf | -11.38337 | -54.36113 | 2024-10-06 05:12:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 282b78d3-540a-3959-b397-03dd4d2b5b9d | -11.38278 | -54.36298 | 2024-10-06 05:12:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 2ba4dde5-6089-3ad2-9122-ae6e88d57846 | -11.37368 | -54.321 | 2024-10-06 05:12:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 03c8555f-5bc0-3cfc-b40e-f8c16937ecd6 | -11.37299 | -54.32576 | 2024-10-06 05:12:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cfe39574-f9d3-3ec1-9e0b-444cbe67617d | -11.34827 | -55.42516 | 2024-10-06 05:12:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c649e902-9689-33d3-9c42-b50a9c51afff | -11.34201 | -55.07556 | 2024-10-06 05:12:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5c200761-06cd-375e-8599-1cbb6dcb039a | -11.31125 | -54.26791 | 2024-10-06 05:12:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 039273b2-17d1-3b8d-80a9-f95022561cb0 | -11.16947 | -54.77079 | 2024-10-06 05:12:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 003b90f4-129f-3cee-ac6a-fbcafdab2ecd | -11.16882 | -54.77526 | 2024-10-06 05:12:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| af11fb78-8f62-32d4-90b1-6bca740dc739 | -11.1082 | -54.22832 | 2024-10-06 05:12:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0f4b9193-071f-3ac2-a7f4-040922d5be57 | -11.10753 | -54.23303 | 2024-10-06 05:12:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 5c9b51af-36f1-3131-8c15-8504767f641d | -11.10687 | -54.23775 | 2024-10-06 05:12:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| ed9f9032-a623-3861-9f64-933128da95cf | -11.10506 | -54.22301 | 2024-10-06 05:12:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 821c048b-09d8-3d7e-a6f7-b4243ca116c6 | -11.10439 | -54.22775 | 2024-10-06 05:12:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9f4b77cd-5236-3483-a463-2fa1a5e73989 | -11.10372 | -54.23246 | 2024-10-06 05:12:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| b308885e-915d-36ab-93aa-1723906bb8ac | -11.10306 | -54.23717 | 2024-10-06 05:12:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 7271c028-cb86-3aa6-a73e-22a8a76d2f59 | -11.10125 | -54.2224 | 2024-10-06 05:12:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 18aab5d0-2294-30cd-8a07-500df52cd60d | -11.10058 | -54.22712 | 2024-10-06 05:12:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c75d4023-747f-3fdc-97b0-57406c649e44 | -11.09992 | -54.23185 | 2024-10-06 05:12:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| dabbd4a8-f13f-3a93-8a94-bf2d1e9addde | -11.09925 | -54.23658 | 2024-10-06 05:12:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| b263691f-5db6-3a44-897b-aaf2bd3a07e8 | -11.09611 | -54.23124 | 2024-10-06 05:12:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| d9b5a826-4fbc-3588-96ef-f08d2193de22 | -11.09545 | -54.23598 | 2024-10-06 05:12:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 20177fcd-3bdf-3d27-bb80-c46f9403b882 | -11.08707 | -54.77438 | 2024-10-06 05:12:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| febfac62-520a-33b4-8978-31e1357c5dd8 | -11.08641 | -54.77884 | 2024-10-06 05:12:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5d96f8e0-81fd-3bcb-84e2-f5dca710ef36 | -11.08576 | -54.78332 | 2024-10-06 05:12:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| df3dcbe7-5397-3c6b-91d1-4dfafb969a5c | -11.08338 | -54.7738 | 2024-10-06 05:12:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 97b773bc-23bc-3381-9765-82619e6dd9a4 | -11.08274 | -54.03112 | 2024-10-06 05:12:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 8.8 |
| c569cf05-c1c6-3167-a6c1-5947a21d494f | -11.08272 | -54.77826 | 2024-10-06 05:12:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 86738b42-d149-3d95-a82a-66ef0936a50a | -11.08207 | -54.78272 | 2024-10-06 05:12:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 87390afa-9f0e-3e52-a682-c46878747d03 | -11.07889 | -54.03056 | 2024-10-06 05:12:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 06ca8f4f-6bea-339a-9003-eebdc442c2a1 | -11.07839 | -54.78214 | 2024-10-06 05:12:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1cd43b40-9706-33b4-aaf5-a4b6b5ded90d | -11.07535 | -54.77711 | 2024-10-06 05:12:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| db07b506-acb5-3e83-98eb-ea95b43e4b0f | -11.0747 | -54.78157 | 2024-10-06 05:12:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| dde87bbd-5cdc-354e-a95e-aeebb7e749e6 | -10.97785 | -54.0081 | 2024-10-06 05:12:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| d73e146e-b244-3a92-81b3-3f2678e21328 | -10.97329 | -54.01238 | 2024-10-06 05:12:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 914cf28c-c314-3d55-8616-9bdd8ee07510 | -10.9726 | -54.01719 | 2024-10-06 05:12:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 06b98b04-1f1d-3368-84bf-5d336bbaad6a | -10.97191 | -54.022 | 2024-10-06 05:12:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| bb751598-4627-30c2-b985-d792b4a39d44 | -10.96805 | -54.02145 | 2024-10-06 05:12:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 15bd7a0e-95d9-3b41-8b7c-4216b5fb3f1d | -7.96559 | -54.76551 | 2024-10-06 05:12:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| dabe6470-5eaa-3889-a05d-4931ffed1358 | -7.97985 | -54.76771 | 2024-10-06 05:12:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9e7b407b-681c-31f3-be64-88db4c808f28 | -7.97749 | -54.75901 | 2024-10-06 05:12:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 109c10f9-b5f0-3ad9-ba54-08f392c25184 | -7.97688 | -54.76309 | 2024-10-06 05:12:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a32f24b2-2ae8-3c8a-9c71-8a857359972c | -7.97628 | -54.76716 | 2024-10-06 05:12:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 69504ac9-b15a-380f-8d98-1546b74e1397 | -7.97573 | -54.74617 | 2024-10-06 05:12:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b642871b-03ce-3dcd-86c4-f9587a649054 | -7.97568 | -54.77124 | 2024-10-06 05:12:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| dc4f9386-baf1-3cdb-9dc0-19814e37d139 | -7.97513 | -54.75027 | 2024-10-06 05:12:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4c3967d5-7b5e-3481-8deb-b6baec5d50af | -7.97507 | -54.77533 | 2024-10-06 05:12:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 297e0b89-40b1-3993-ae6a-1ddc07ff0f33 | -7.97212 | -54.7707 | 2024-10-06 05:12:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 941353bd-ccfa-3b8e-ab1a-e4f44c613787 | -7.97151 | -54.77479 | 2024-10-06 05:12:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1f79bc67-edfd-3a7c-a2f1-3408312ec647 | -7.97096 | -54.75383 | 2024-10-06 05:12:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 33b27209-26bf-382d-a81f-fe97781fb8f0 | -7.97036 | -54.75789 | 2024-10-06 05:12:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a2e7572b-2656-36e6-969a-54613858b4be | -7.96976 | -54.76196 | 2024-10-06 05:12:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 95924b17-28b3-3794-a87e-20d9903c96db | -7.96916 | -54.76606 | 2024-10-06 05:12:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 8494f320-2482-3ba9-b2ea-30aa9348481b | -7.96855 | -54.77016 | 2024-10-06 05:12:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ae1b14cc-545d-38b4-9adb-0673ea58150a | -7.90913 | -54.75783 | 2024-10-06 05:12:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7e73ffbf-c398-3bb7-81a4-d588a383150d | -7.90618 | -54.75321 | 2024-10-06 05:12:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fb542d26-aa12-323b-b3f1-03e117bcbd02 | -7.88145 | -54.89414 | 2024-10-06 05:12:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 941f11b4-3941-3e3e-bef9-765baf2525da | -7.87737 | -54.87299 | 2024-10-06 05:12:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 225a30fc-dd70-3569-be28-b5b409df6698 | -7.87617 | -54.88104 | 2024-10-06 05:12:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 50c18f01-8d97-3e1b-b89c-583a9d22d504 | -7.87496 | -54.8891 | 2024-10-06 05:12:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| bbaf434e-bae7-3470-848c-18b1428ced7c | -7.86789 | -54.88803 | 2024-10-06 05:12:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| f3adac31-e41f-3a25-a5ad-52ae803e7542 | -7.86729 | -54.89202 | 2024-10-06 05:12:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d0eb24cf-3514-322c-8a06-ba385af0a309 | -6.93976 | -55.11607 | 2024-10-06 05:12:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9bf54b07-132a-33e9-b30c-5e3a0edb9dde | -7.98045 | -54.76365 | 2024-10-06 05:12:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d598aa7c-12d2-3e29-b284-2acd925c0d64 | -7.97924 | -54.77177 | 2024-10-06 05:12:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 44210409-8bb1-3aa0-8efe-ec75ef4e51ed | -7.97864 | -54.77588 | 2024-10-06 05:12:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d0a43cc3-f214-3743-9956-063446726711 | -7.97809 | -54.75491 | 2024-10-06 05:12:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8aae577e-b2b5-3078-8d34-79adbc4e364a | -7.97803 | -54.77998 | 2024-10-06 05:12:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a0d0cd89-e3ac-300f-ae68-fea60725cc3b | -7.97452 | -54.75437 | 2024-10-06 05:12:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ec3e0c83-7060-392c-a0c0-a00260e402ac | -7.97392 | -54.75845 | 2024-10-06 05:12:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4ba7968e-cbc5-3349-bbcc-1ca65360a981 | -7.97332 | -54.76252 | 2024-10-06 05:12:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |


[Clique aqui para ver as próximas entradas](README107.md)
