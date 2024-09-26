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

## Dados Diários - Página 58

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0efc0778-6aec-3ee1-8c02-a99ea4a41874 | -2.95461 | -49.36665 | 2024-09-26 04:04:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| eacd92e0-03ac-32e9-8947-1b580967c1ba | -2.95046 | -49.35944 | 2024-09-26 04:04:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c0eb330b-dea7-3633-9215-a0be70288327 | -2.94993 | -49.36261 | 2024-09-26 04:04:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 37ff1bd3-3a5e-35d1-a6ee-703e02cd39fe | -2.9494 | -49.36576 | 2024-09-26 04:04:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a69ac6b3-e38e-3658-a964-07136f3f0765 | -2.82868 | -49.14553 | 2024-09-26 04:04:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 83fc45e1-6ed7-3223-a242-24f464a19bab | -2.82817 | -49.14867 | 2024-09-26 04:04:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| da6fdea4-c68a-3a6f-83f8-cbe51bf77768 | -4.51223 | -50.81447 | 2024-09-26 04:04:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4de90353-3042-3823-a5a3-e6e8db9200af | -4.5116 | -50.81821 | 2024-09-26 04:04:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| db3521a1-ac45-3992-990e-a047e509d6cc | -4.51013 | -50.81633 | 2024-09-26 04:04:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2a0fd417-1bf5-3f72-bb4a-4f1dbf599550 | -3.67379 | -49.80251 | 2024-09-26 04:04:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 2462cd1d-7153-3cd9-a66a-dd15b7fe9bd5 | -3.66852 | -49.80141 | 2024-09-26 04:04:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c39fd56c-6f67-3b23-8824-472754296bb7 | -3.57252 | -50.378 | 2024-09-26 04:04:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 96ecd44d-a44a-3702-b98f-785e3bd47948 | -3.56843 | -50.57479 | 2024-09-26 04:04:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ed5cc4ee-9572-3bd7-b5a3-c7bca7cc539d | -3.56783 | -50.57846 | 2024-09-26 04:04:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 5542a90d-afb7-3339-a9ff-3a1a46181268 | -3.567 | -50.37706 | 2024-09-26 04:04:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f71ff49f-7311-376d-90f5-bc3591ee7ee4 | -3.56675 | -50.57353 | 2024-09-26 04:04:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 57cc6c88-6ca7-340b-b745-e617f437ecad | -3.5664 | -50.3807 | 2024-09-26 04:04:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7aa1297d-1ac0-3351-b2a6-b8807d62a879 | -3.56612 | -50.57718 | 2024-09-26 04:04:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 0dab4086-8f4e-3c43-bb37-70cae82f9c8a | -3.56577 | -50.38448 | 2024-09-26 04:04:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 875aed03-00a9-39bf-b7d8-d94cd3693b1b | -3.56226 | -50.57738 | 2024-09-26 04:04:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 2acad70c-1a79-38d5-b385-817d7483183b | -3.56146 | -50.37627 | 2024-09-26 04:04:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 11.9 |
| 6ba5ece5-2ef1-3976-9a4e-64e9def73b0d | -3.56087 | -50.37984 | 2024-09-26 04:04:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 11.9 |
| 23145479-3fc2-34ce-99e9-75831effb0c9 | -3.56054 | -50.57619 | 2024-09-26 04:04:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| be19e32e-8eaa-3242-a7ef-24210ec2cf1c | -3.56024 | -50.38356 | 2024-09-26 04:04:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 10.6 |
| cd34f504-0e76-3cb3-8892-01b64564c067 | -3.55962 | -50.38728 | 2024-09-26 04:04:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 2c0b124a-b75f-3e87-ac6e-cfd23ea75f6b | -3.55534 | -50.37891 | 2024-09-26 04:04:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 11.9 |
| 25f0e023-6b9b-3dae-ac7a-7647c49a0925 | -3.55472 | -50.38261 | 2024-09-26 04:04:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 2d263c4a-94f3-33a9-91e1-2ab0f6d7de9d | -3.20014 | -51.14363 | 2024-09-26 04:04:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1e716219-8037-3cc6-8eaf-ff75480de4a2 | -3.19944 | -51.14777 | 2024-09-26 04:04:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2cf9dbd2-583d-3ee0-be47-6e72fb89a6a0 | -3.19875 | -51.1519 | 2024-09-26 04:04:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 45ef1c43-3f80-3a1d-aa15-cd5e7bd5daea | -3.19432 | -51.14256 | 2024-09-26 04:04:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b10c949f-8fd3-37aa-9269-ff5064dab41c | -3.19362 | -51.1467 | 2024-09-26 04:04:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 09af2f3a-5adf-3132-b4f7-7a907a5ca0dd | -3.19293 | -51.15079 | 2024-09-26 04:04:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| de2a2828-170d-359e-91a2-c7336def8225 | -3.48964 | -51.1921 | 2024-09-26 04:04:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f2ee0ba6-b8ef-38ac-a896-124f83a2fa42 | -3.09241 | -51.28975 | 2024-09-26 04:04:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ec25e071-c965-310c-ac46-c4edcb1eabf9 | -3.09169 | -51.29406 | 2024-09-26 04:04:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| babedb09-36f0-385d-b95d-f3e15fd9d4ae | -3.01297 | -51.08821 | 2024-09-26 04:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 1c9f3032-cc31-3647-b8f1-b97618368ee2 | -3.00783 | -51.08308 | 2024-09-26 04:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 6c658469-b5f6-339e-ab6d-81ecda8f47e9 | -3.00709 | -51.08749 | 2024-09-26 04:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| df60124d-761e-3c78-b632-f090a87b8ab8 | -3.00637 | -51.0918 | 2024-09-26 04:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| fa82c58a-84bc-3f1d-b3bd-a03b55119d51 | -3.00126 | -51.08649 | 2024-09-26 04:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 541af7f2-a4b8-32b0-902e-5f497a956d83 | -2.87325 | -51.66299 | 2024-09-26 04:04:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| a81785c3-2d07-3635-80b0-9418e7f3b1a3 | -2.87247 | -51.66757 | 2024-09-26 04:04:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| cc3c61db-b899-3dac-97d2-332207edc6f4 | -2.8719 | -51.66405 | 2024-09-26 04:04:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 2a10ab16-1781-3ca7-bffe-de776e16151d | -2.87169 | -51.67217 | 2024-09-26 04:04:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 5bfe40ab-11a5-3e18-bc21-cac3be601130 | -2.87115 | -51.66869 | 2024-09-26 04:04:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 2466ca4a-d727-3367-af05-d407e46df8e0 | -2.8704 | -51.67329 | 2024-09-26 04:04:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 9bdb7064-bce6-384d-8998-7bbdb71d9b21 | -2.86641 | -51.66655 | 2024-09-26 04:04:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| b732899e-fea1-3b25-8f1a-c1dcccc21dde | -2.86562 | -51.67117 | 2024-09-26 04:04:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 1c37cedd-9f84-3588-a8f1-7ff8595b1a8e | -2.86508 | -51.66767 | 2024-09-26 04:04:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| e5a0aeaf-2c57-3650-a519-5eb1bc29032e | -2.86433 | -51.67229 | 2024-09-26 04:04:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 599f3904-596a-3400-bf0e-e4451041a79d | -2.39915 | -51.28306 | 2024-09-26 04:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| cfd57e13-1a7c-35d6-89de-da5516ff317a | -2.39845 | -51.28741 | 2024-09-26 04:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| aea0afa7-ae88-3975-84d7-09dd2db0e456 | -2.39556 | -51.28458 | 2024-09-26 04:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e8f80aa9-bf48-3a61-86ca-db5d8fe13487 | -2.39483 | -51.28892 | 2024-09-26 04:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c567ce4a-6b93-3109-a1a7-e0254fc9753f | -2.3925 | -51.28634 | 2024-09-26 04:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 45315c0e-9781-3da4-8f13-4e182738e54c | -2.39179 | -51.29073 | 2024-09-26 04:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fc23e518-cc8f-3f2b-9c96-12251e898044 | -2.38961 | -51.28353 | 2024-09-26 04:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7a021f8a-9357-3f03-92b7-7571b6c5e2aa | -2.38887 | -51.28789 | 2024-09-26 04:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3050d3ec-473a-3878-95a8-1c5a87ac7c76 | -2.38725 | -51.28092 | 2024-09-26 04:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 6a0d3e34-0427-3567-af3e-7e2b786a35de | -2.38654 | -51.28529 | 2024-09-26 04:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 8efa598d-ae96-3e37-bf5a-731cee4afec7 | -2.38583 | -51.28968 | 2024-09-26 04:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 7467d809-da2f-372c-8228-0e96a4d380f4 | -2.38366 | -51.28248 | 2024-09-26 04:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9c63a840-485a-37cc-a8c7-ff97ae0d456a | -2.38292 | -51.28685 | 2024-09-26 04:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d2ad3e35-d9e5-3bce-946d-24e35db85fdd | -3.40994 | -53.20594 | 2024-09-26 04:04:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6e42bd9c-c133-3c3e-8b29-139a1f5bb0a5 | -3.39327 | -53.72081 | 2024-09-26 04:04:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 21a39734-9120-352b-b3d5-dd217eb95374 | -3.39223 | -53.72683 | 2024-09-26 04:04:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 620df261-eae5-3137-a2c4-a676ec0d6ba5 | -3.32487 | -53.22523 | 2024-09-26 04:04:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f9c954b8-0f80-3d0a-a00e-4a624b81ee99 | -3.32186 | -53.21817 | 2024-09-26 04:04:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 796ae438-094b-3f55-a960-c354fb9f502b | -3.32087 | -53.22401 | 2024-09-26 04:04:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 1c1f4c9c-fcb1-3f64-9748-ec31852810e4 | -3.31924 | -53.21845 | 2024-09-26 04:04:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 8beafe2a-c6a2-3c1b-a69b-6684c4cbf327 | -3.31821 | -53.22429 | 2024-09-26 04:04:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 8044a188-560a-313a-8673-5aa2b475cc93 | -3.25643 | -53.321 | 2024-09-26 04:04:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 21595015-da1b-307e-aa14-b3338dc731d2 | -3.2554 | -53.32699 | 2024-09-26 04:04:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| cd5a736a-4659-38b6-abaf-32ac13b28061 | -3.24981 | -53.3196 | 2024-09-26 04:04:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c5133d89-44ac-3551-a0f9-120dd0d746b8 | -2.85806 | -53.32048 | 2024-09-26 04:04:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 041bb3ea-e4fd-341f-8f10-a389821f3c78 | -2.85137 | -53.31924 | 2024-09-26 04:04:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9dd2a9b7-9824-3a8c-823c-305c7db7ab94 | -1.04554 | -53.35613 | 2024-09-26 04:04:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 4c4a6774-dc70-3c1f-a5a4-c41b715ff6eb | -1.04448 | -53.36264 | 2024-09-26 04:04:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| dea0560d-c5fd-3d5a-8163-3919f55a7e8c | -3.35392 | -53.78504 | 2024-09-26 04:04:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 03613a10-61c6-3a68-bd28-d4a374104e88 | -3.35346 | -53.78278 | 2024-09-26 04:04:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1050ea66-9a9c-3c00-9240-8e04b491c06b | -3.35234 | -53.78939 | 2024-09-26 04:04:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| f2d460e2-988a-3067-953b-18526d912f68 | -3.34708 | -53.7839 | 2024-09-26 04:04:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6615f795-6f6b-3b07-ac7d-a638dc82f62d | -3.34595 | -53.79031 | 2024-09-26 04:04:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d9868759-4f18-31de-ad54-521bc14e87da | -3.34549 | -53.78829 | 2024-09-26 04:04:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cd512a36-3233-392d-baef-49305012202f | -6.61301 | -39.58503 | 2024-09-26 04:04:00 | NOAA-20 | CARIÚS | CEARÁ | Brasil | 2303303 | 23 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 55df3393-f142-3415-a6c6-e24849340269 | -4.72025 | -38.45842 | 2024-09-26 04:04:00 | NOAA-20 | MORADA NOVA | CEARÁ | Brasil | 2308708 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 05237632-f909-368f-a609-13d82595f30b | -4.56856 | -38.48395 | 2024-09-26 04:04:00 | NOAA-20 | OCARA | CEARÁ | Brasil | 2309458 | 23 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 151575b1-e3c3-352f-8d3e-30d70c49ed88 | -4.53549 | -38.03402 | 2024-09-26 04:04:00 | NOAA-20 | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 0ceac024-d2e6-3f3a-8a27-3f23865f1457 | -4.53193 | -38.03348 | 2024-09-26 04:04:00 | NOAA-20 | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 80b44672-561d-3054-b9dd-f1078b1c4f51 | -5.34765 | -38.09509 | 2024-09-26 04:04:00 | NOAA-20 | TABULEIRO DO NORTE | CEARÁ | Brasil | 2313104 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| ff67915d-0089-333b-8ada-55897869a25e | -5.1567 | -37.73203 | 2024-09-26 04:04:00 | NOAA-20 | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 1f4b50e5-738e-33ca-8aee-9d7533593e10 | -5.1524 | -37.73575 | 2024-09-26 04:04:00 | NOAA-20 | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 3.3 |
| df606bcc-3e2b-327a-8e00-4f6030f8aec5 | -6.04437 | -40.38707 | 2024-09-26 04:04:00 | NOAA-20 | TAUÁ | CEARÁ | Brasil | 2313302 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 8dc0f6c9-9241-3b7a-82d7-395f0fc3b8dc | -6.61981 | -39.58617 | 2024-09-26 04:04:00 | NOAA-20 | CARIÚS | CEARÁ | Brasil | 2303303 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 9d0e9d43-9e00-344c-a63b-7accc338b6c7 | -6.61641 | -39.5856 | 2024-09-26 04:04:00 | NOAA-20 | CARIÚS | CEARÁ | Brasil | 2303303 | 23 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 71a34029-5711-3420-b297-24e85debab31 | -6.61585 | -39.58927 | 2024-09-26 04:04:00 | NOAA-20 | CARIÚS | CEARÁ | Brasil | 2303303 | 23 | 33 | nan | nan | nan | Caatinga | 5.8 |
| bddfeebf-0c0a-3875-b918-e4065c49b051 | -6.61245 | -39.58869 | 2024-09-26 04:04:00 | NOAA-20 | CARIÚS | CEARÁ | Brasil | 2303303 | 23 | 33 | nan | nan | nan | Caatinga | 5.8 |
| addea46b-e3e9-3e11-9f4e-b4cee8adebd1 | -6.6096 | -39.58447 | 2024-09-26 04:04:00 | NOAA-20 | CARIÚS | CEARÁ | Brasil | 2303303 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 0ec2c698-4372-35bc-bc50-877e2ce8bc1e | -6.60502 | -39.54607 | 2024-09-26 04:04:00 | NOAA-20 | CARIÚS | CEARÁ | Brasil | 2303303 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |


[Clique aqui para ver as próximas entradas](README59.md)
