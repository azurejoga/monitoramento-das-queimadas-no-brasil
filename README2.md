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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4ce36351-e86f-34b3-842d-739656049777 | 3.1275 | -60.8026 | 2026-03-15 01:10:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 96.4 |
| de439d45-bb2b-351e-a9d1-d1f7303284c8 | 3.1093 | -60.8029 | 2026-03-15 01:10:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 98.4 |
| cc6f0c0e-f141-3723-9376-f4563bd20431 | -11.9512 | -41.3251 | 2026-03-15 01:20:00 | GOES-19 | BONITO | BAHIA | Brasil | 2904050 | 29 | 33 | nan | nan | nan | Caatinga | 52.8 |
| 293f2b83-ed53-3048-9690-7470b8879386 | 3.1276 | -60.7836 | 2026-03-15 01:20:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 178.8 |
| 497703ae-30b5-3836-85f9-9c21e3380e39 | 3.1093 | -60.784 | 2026-03-15 01:20:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 123.5 |
| 73a647b4-f6d8-30aa-b697-74d93db26db6 | 3.1093 | -60.8029 | 2026-03-15 01:20:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 120.1 |
| d12dd887-9e0b-34ca-abcd-2d15c5ba406a | 3.1275 | -60.8026 | 2026-03-15 01:20:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 138.8 |
| c0d17034-9119-3060-8499-e0c89f522eca | 3.1275 | -60.8026 | 2026-03-15 01:30:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 234.9 |
| d58eeb67-0b9a-3d34-929f-a09ca8a53e97 | 3.1093 | -60.8029 | 2026-03-15 01:30:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 198.9 |
| a7b29bdf-c1cb-3153-b140-7f3113d5d120 | 3.1276 | -60.7836 | 2026-03-15 01:30:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 201.7 |
| aac80d08-2edf-3b34-a77c-c529d1237303 | -11.9512 | -41.3251 | 2026-03-15 01:30:00 | GOES-19 | BONITO | BAHIA | Brasil | 2904050 | 29 | 33 | nan | nan | nan | Caatinga | 63.7 |
| 166c50dc-28da-3806-aaf4-b48a3d04b308 | 3.1093 | -60.784 | 2026-03-15 01:30:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 167.5 |
| 707e516b-b46d-3771-9525-dc25205c953f | 3.1275 | -60.8026 | 2026-03-15 01:40:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 384.5 |
| 2f53417c-a339-39ea-b115-350d0280b015 | -6.5631 | -51.1126 | 2026-03-15 01:40:00 | GOES-19 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 55.5 |
| 92ebbf59-e39d-3336-a3c8-19ed4df5e1c6 | -11.9512 | -41.3251 | 2026-03-15 01:40:00 | GOES-19 | BONITO | BAHIA | Brasil | 2904050 | 29 | 33 | nan | nan | nan | Caatinga | 60.5 |
| 02d7e308-bf3f-3afc-81a2-eaf217b57674 | 3.1275 | -60.8215 | 2026-03-15 01:40:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 52.0 |
| fb43422a-96f2-33da-984a-69a92274d744 | 3.1093 | -60.8029 | 2026-03-15 01:40:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 310.8 |
| acb3ab7a-b5e2-36eb-92a3-d9f5640a236b | 3.1276 | -60.7836 | 2026-03-15 01:40:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 227.1 |
| d0453f0e-047c-3766-9c11-164b8186e30d | 3.1093 | -60.784 | 2026-03-15 01:40:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 184.2 |
| 3fc99f87-1c5c-3cfe-8959-bc2a90541d70 | 3.1093 | -60.784 | 2026-03-15 01:50:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 166.0 |
| 3e5702aa-ce2e-30a5-8f47-b0f5a154485b | -11.9512 | -41.3251 | 2026-03-15 01:50:00 | GOES-19 | BONITO | BAHIA | Brasil | 2904050 | 29 | 33 | nan | nan | nan | Caatinga | 62.4 |
| 70a054cb-6fa7-325a-8275-a09822c16bc6 | 3.1276 | -60.7836 | 2026-03-15 01:50:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 211.0 |
| 73cfefa5-5fab-398e-96e4-0a23177d5f4b | 3.1092 | -60.8218 | 2026-03-15 01:50:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 63.7 |
| 93cbbc73-05c7-350a-b3db-26646a3b1a39 | 3.1275 | -60.8026 | 2026-03-15 01:50:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 334.3 |
| 03ae2642-9273-38a8-a6be-acf361217e4e | 3.091 | -60.8032 | 2026-03-15 01:50:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 53.2 |
| f020c83c-49b3-3b3f-a33f-41f848c56c9f | 3.1093 | -60.8029 | 2026-03-15 01:50:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 293.9 |
| fedc8180-be7d-3309-897b-c2ce6ccc03f6 | 3.1092 | -60.8218 | 2026-03-15 02:00:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 63.7 |
| 7c62725e-a75d-30b8-a13a-f7c827875b37 | 3.1093 | -60.784 | 2026-03-15 02:00:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 129.0 |
| 9b23b25d-e659-3129-bf8c-b739ab7ee9bd | 3.1093 | -60.8029 | 2026-03-15 02:00:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 237.2 |
| d4b4f2b3-b8c7-30da-9131-c3361cdb04cb | 3.1276 | -60.7836 | 2026-03-15 02:00:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 159.1 |
| 54f1c980-2432-3e06-acd9-b39098089741 | -11.9512 | -41.3251 | 2026-03-15 02:00:00 | GOES-19 | BONITO | BAHIA | Brasil | 2904050 | 29 | 33 | nan | nan | nan | Caatinga | 59.7 |
| 851531c2-b893-342a-9291-2f29e31d8aeb | 3.1275 | -60.8026 | 2026-03-15 02:00:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 263.1 |
| b3ead194-bc9a-3690-811e-07e98a764215 | 3.1093 | -60.784 | 2026-03-15 02:10:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 102.8 |
| def2afda-8532-3951-a13c-962efdbcf257 | 3.1092 | -60.8218 | 2026-03-15 02:10:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 78.4 |
| 26bd2719-599a-3125-84a3-47c346a2c4fb | 3.1276 | -60.7836 | 2026-03-15 02:10:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 131.7 |
| fd8d89d5-f7f8-38da-83cc-1f0deffb9d77 | 3.1275 | -60.8026 | 2026-03-15 02:10:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 182.0 |
| f96ab154-4587-37f4-9bc1-a03b9d88d019 | 3.1093 | -60.8029 | 2026-03-15 02:10:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 196.7 |
| fc0ca36a-7208-30a3-8679-95e2cbf67049 | 3.1093 | -60.784 | 2026-03-15 02:20:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 68.2 |
| 7ec3158b-77bc-32eb-81ab-9c0d18bc79fb | 3.1093 | -60.8029 | 2026-03-15 02:20:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 163.6 |
| 67255148-2c09-3359-9438-5f7002d279f6 | 3.1092 | -60.8218 | 2026-03-15 02:20:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 87.6 |
| 2aa27e2c-94cf-3cbb-bf07-db8303a6189c | 3.1276 | -60.7836 | 2026-03-15 02:20:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 74.3 |
| c4bb6c90-239b-3b71-afcd-0ca6261d3dc1 | 3.1275 | -60.8026 | 2026-03-15 02:20:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 126.0 |
| db74798a-3b6e-38cd-b73a-f119046472cc | 3.1093 | -60.784 | 2026-03-15 02:30:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 70.7 |
| 727b5424-9de4-3680-a07d-0da0b976b6af | 3.1093 | -60.8029 | 2026-03-15 02:30:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 168.9 |
| 9e557103-073d-3de5-b7ae-751c61f5a204 | 3.1276 | -60.7836 | 2026-03-15 02:30:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 69.6 |
| 326fb687-92f9-3c22-8b4e-23ace33f31a4 | 3.1092 | -60.8218 | 2026-03-15 02:30:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 111.4 |
| 384b3117-277f-31df-aec0-28d503ebd016 | 3.1275 | -60.8026 | 2026-03-15 02:30:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 103.1 |
| 6403ba93-0612-33b1-b1a0-e1f1aedfd4fc | 3.1093 | -60.8029 | 2026-03-15 02:40:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 150.7 |
| d30a2abb-3a66-3cf4-84e1-e56f12217726 | 3.1275 | -60.8026 | 2026-03-15 02:40:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 104.3 |
| 1beee699-0e1e-37ac-8ca5-9c1c4c69ec2d | 2.9633 | -60.7484 | 2026-03-15 02:40:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 60.4 |
| 6027b898-dd80-3035-a815-076c565cb53c | 3.1276 | -60.7836 | 2026-03-15 02:40:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 63.0 |
| 6bf54651-a301-3ca0-b946-bb45465558c3 | 3.1093 | -60.784 | 2026-03-15 02:40:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 55.9 |
| fbb906a2-1f82-3e27-9c60-a5f48b1af85f | 3.1092 | -60.8218 | 2026-03-15 02:40:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 131.4 |
| 084d847c-8741-3eb9-9ec3-c8c75a9e61bb | 3.1275 | -60.8026 | 2026-03-15 02:50:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 92.1 |
| 08ea646a-b83f-3459-a30a-55fb6c8ffba5 | 2.9633 | -60.7484 | 2026-03-15 02:50:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 64.7 |
| a3c1239c-c04b-3f83-a361-ee5b0981573c | 3.1276 | -60.7836 | 2026-03-15 02:50:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 59.8 |
| 476aa284-ab00-3602-a02d-425eae488f5c | 3.1092 | -60.8218 | 2026-03-15 02:50:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 101.0 |
| cddda368-e873-3569-869d-8c6cc5ba1d19 | 3.1093 | -60.8029 | 2026-03-15 02:50:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 113.5 |
| 803a8158-4a3b-3823-b18f-ceb5868137ae | 3.1092 | -60.8218 | 2026-03-15 03:00:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 88.0 |
| 6cfbf410-2aa9-36ac-8814-b1d18d5d01e0 | 3.1275 | -60.8026 | 2026-03-15 03:00:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 73.3 |
| b1dcc633-4da4-3606-93b4-d92ab5263e3a | 3.1093 | -60.8029 | 2026-03-15 03:00:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 108.3 |
| 91c39d8f-c139-3187-9664-0bd552fe0f44 | 3.1092 | -60.8218 | 2026-03-15 03:10:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 117.0 |
| 74b907a4-ca73-3a33-b718-bad3f02f8114 | 3.1093 | -60.8029 | 2026-03-15 03:10:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 98.2 |
| 32ac16fc-1db6-3417-9d44-58dcc7f4c611 | 3.1275 | -60.8026 | 2026-03-15 03:10:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 71.8 |
| 3c491ca1-6930-33d0-a481-b409e57a58b2 | -11.9465 | -41.33506 | 2026-03-15 03:17:00 | NPP-375D | BONITO | BAHIA | Brasil | 2904050 | 29 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 69328a63-5844-32df-bb5c-52630df04e03 | -11.94767 | -41.32937 | 2026-03-15 03:17:00 | NPP-375D | BONITO | BAHIA | Brasil | 2904050 | 29 | 33 | nan | nan | nan | Caatinga | 2.6 |
| de50745d-f1e3-3eda-841c-194e80ed0e9a | -11.94108 | -41.32792 | 2026-03-15 03:17:00 | NPP-375D | BONITO | BAHIA | Brasil | 2904050 | 29 | 33 | nan | nan | nan | Caatinga | 2.6 |
| fcab90d6-40b0-3217-aef0-522ef2e2ff02 | -11.93991 | -41.33362 | 2026-03-15 03:17:00 | NPP-375D | BONITO | BAHIA | Brasil | 2904050 | 29 | 33 | nan | nan | nan | Caatinga | 3.0 |
| cfbbc5e9-e4f7-39a5-bade-a8d54be8dc99 | -10.03288 | -36.25516 | 2026-03-15 03:17:00 | NPP-375D | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| f3bf0f45-6950-3d9f-82cb-d5aac9dbe03b | 3.1093 | -60.8029 | 2026-03-15 03:20:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 87.7 |
| 19454043-3be2-3ed9-a54a-408886af6534 | 3.1092 | -60.8218 | 2026-03-15 03:20:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 104.9 |
| de8d1201-d918-3607-8b24-1f9bc8bad511 | 3.091 | -60.8222 | 2026-03-15 03:20:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 51.9 |
| f1498fc3-1bf1-3616-8527-15dc1ce83d30 | 3.1275 | -60.8026 | 2026-03-15 03:20:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 69.2 |
| fd70222b-9502-3480-8cd3-e7cfe7c61185 | 3.1093 | -60.8029 | 2026-03-15 03:30:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 72.2 |
| 38603396-3b80-378b-8198-5c97f74d9a50 | 3.091 | -60.8222 | 2026-03-15 03:30:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 55.8 |
| 45d3096e-7fa1-3364-b71c-7cce8383e5c4 | 3.1092 | -60.8218 | 2026-03-15 03:30:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 108.5 |
| 451e8471-c8e8-391c-baff-c874d202da60 | 3.1275 | -60.8026 | 2026-03-15 03:30:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 56.2 |
| 4475f693-6088-37a9-832c-c3987c5acfc5 | -8.79552 | -44.80988 | 2026-03-15 03:38:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d8855820-5c1a-32fe-85ab-4133d05c33bb | -5.95522 | -38.629 | 2026-03-15 03:38:00 | NOAA-20 | JAGUARIBE | CEARÁ | Brasil | 2306900 | 23 | 33 | nan | nan | nan | Caatinga | 2.2 |
| a5ce8176-f613-307f-8569-13755abca448 | -5.95463 | -38.63256 | 2026-03-15 03:38:00 | NOAA-20 | JAGUARIBE | CEARÁ | Brasil | 2306900 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| f0531b6c-ed80-300c-9b57-8a9e5daf9813 | -8.79607 | -44.80733 | 2026-03-15 03:38:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e3d37214-f595-38d2-88fe-ea623b42fefc | -9.61068 | -37.04949 | 2026-03-15 03:38:00 | NOAA-20 | MAJOR ISIDORO | ALAGOAS | Brasil | 2704401 | 27 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 2937c9c3-2d5d-335e-bb4c-20c71ec4ebdc | -8.80129 | -44.81104 | 2026-03-15 03:38:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 91922881-de7a-3da1-a995-b573107a2fa6 | -8.80107 | -44.81271 | 2026-03-15 03:38:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c7a50651-77ea-3adf-95ff-3e07bca0121a | -9.11849 | -40.58709 | 2026-03-15 03:38:00 | NOAA-20 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 1.2 |
| c54a1b8e-5952-3f18-ada1-80fd25d88280 | -8.80209 | -44.80684 | 2026-03-15 03:38:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 78ae3fb8-4f1e-3c55-93ad-5ce8da0b0154 | -8.79632 | -44.8057 | 2026-03-15 03:38:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5708e56c-2b73-3ee7-9ccb-6a98100c093d | -9.11978 | -40.58562 | 2026-03-15 03:38:00 | NOAA-20 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 046195be-ebeb-39a0-90e0-0302ecb3a719 | -6.92905 | -38.74577 | 2026-03-15 03:38:00 | NOAA-20 | CACHOEIRA DOS ÍNDIOS | PARAÍBA | Brasil | 2503308 | 25 | 33 | nan | nan | nan | Caatinga | 2.1 |
| b2ab3300-3fdc-367d-84a6-dbb792ddbc5d | -8.80184 | -44.80849 | 2026-03-15 03:38:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c178ab63-3b9e-3d0b-bc42-b0599b45047e | -10.08651 | -36.24271 | 2026-03-15 03:38:00 | NOAA-20 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| f95cb27e-5a0b-3f95-a3d9-dded9a860f15 | -5.95061 | -38.63191 | 2026-03-15 03:38:00 | NOAA-20 | JAGUARIBE | CEARÁ | Brasil | 2306900 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 2e6d49c9-b690-3ef2-91fb-b251d3f40123 | 3.1275 | -60.8026 | 2026-03-15 03:40:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 57.1 |
| 0c792ac6-c05b-3671-a5bf-c740d4bf59f0 | 3.091 | -60.8222 | 2026-03-15 03:40:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 48.9 |
| 11d4dfeb-a5e7-38ce-8c6b-93cc9f9685fd | 3.1093 | -60.8029 | 2026-03-15 03:40:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 68.3 |
| 8ffc180c-1a2c-33c9-aabf-d9df00e6e0c4 | 3.1092 | -60.8218 | 2026-03-15 03:40:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 86.6 |
| dab59b6a-07e1-38ae-8db8-750dbca31049 | -11.9578 | -41.29507 | 2026-03-15 03:40:00 | NOAA-20 | BONITO | BAHIA | Brasil | 2904050 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 2447e359-460c-3eab-a58d-063a2c32e652 | -12.33577 | -38.42199 | 2026-03-15 03:40:00 | NOAA-20 | CATU | BAHIA | Brasil | 2907509 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 45da74e7-134d-332f-8155-fb314480f973 | -12.65743 | -47.09503 | 2026-03-15 03:40:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| afe612ed-e306-3825-a1cf-b04a86e5b77d | -11.93851 | -41.32686 | 2026-03-15 03:40:00 | NOAA-20 | BONITO | BAHIA | Brasil | 2904050 | 29 | 33 | nan | nan | nan | Caatinga | 5.4 |


[Clique aqui para ver as próximas entradas](README3.md)
