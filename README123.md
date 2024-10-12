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

## Dados Diários - Página 123

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 863ca1ff-8cbc-31b2-9413-b69c91b1e1c5 | -17.84662 | -57.30197 | 2024-10-12 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.4 |
| ad6b57a5-7646-34bd-b1c9-0c2866d6ffef | -17.84611 | -57.30596 | 2024-10-12 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.4 |
| 2e40a0f0-a031-351d-9ca4-8f7a3487e674 | -17.84458 | -57.31787 | 2024-10-12 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.0 |
| 4c6da971-0073-347c-bacd-40ba25a3ee8a | -17.84406 | -57.32185 | 2024-10-12 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.0 |
| 3c71a126-c776-3c8c-9a25-5ed2cc36ce88 | -17.84356 | -57.32581 | 2024-10-12 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 17.8 |
| 0e8595c3-46a4-3e02-9a23-98f7e455f573 | -17.84345 | -57.29342 | 2024-10-12 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 68cb7129-c8a2-3c9b-aaec-fd909d92042b | -17.84294 | -57.29739 | 2024-10-12 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 85ae5f67-40e6-392b-9d33-1c2c0e9de309 | -17.84254 | -57.33374 | 2024-10-12 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 6d6af900-6877-3126-99cf-8c8acd81dbec | -17.84243 | -57.30138 | 2024-10-12 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 030304b6-6c67-347c-8cb4-139199147e5a | -17.84192 | -57.30537 | 2024-10-12 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 6a6c37cb-0be0-33e5-afcb-a4dd51aa1644 | -17.84141 | -57.30935 | 2024-10-12 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 852c7647-2a4c-37f4-8df6-f59f7c2586ad | -17.8409 | -57.31332 | 2024-10-12 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 2e471e1a-5dc1-3a17-8184-32d599796e9f | -17.84039 | -57.31729 | 2024-10-12 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 5f52f5c7-68e1-325d-8a8d-3f498ef494af | -17.83988 | -57.32125 | 2024-10-12 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 10469fe2-6865-30cc-a2ac-9be1feb5e6a9 | -17.83937 | -57.32522 | 2024-10-12 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 30.1 |
| a532c84d-8fc1-33de-890e-3b867ef7812a | -17.83875 | -57.2968 | 2024-10-12 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 43231f5d-1638-3fe7-b005-69a8da923ce8 | -17.83823 | -57.3008 | 2024-10-12 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 826548d3-6710-331a-a9f5-0ea9dd8c0bc2 | -17.83772 | -57.30478 | 2024-10-12 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 97994ec3-4a4f-3e0b-be66-246fb0b2124c | -17.83721 | -57.30877 | 2024-10-12 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| c5d96abd-d609-3dfa-93fd-876d9bc91d06 | -17.8367 | -57.31274 | 2024-10-12 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| a773fdc9-cb54-3df2-b359-0f5c34a2fcb9 | -17.83569 | -57.32067 | 2024-10-12 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 349a35aa-da93-3ef0-96c6-5ae1c628cc3d | -17.83518 | -57.32464 | 2024-10-12 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 30.1 |
| 5d744c92-0fc3-3d71-b542-8816984e233b | -17.83467 | -57.32861 | 2024-10-12 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 30.1 |
| 98211752-56e4-3383-afb4-9db6ccb1a756 | -17.83455 | -57.29622 | 2024-10-12 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.6 |
| 513a7d6c-aeeb-3311-a336-4a93c9686fbc | -17.83404 | -57.30021 | 2024-10-12 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 7fdc874b-1395-38e9-8f3e-6bc67d94c654 | -17.83365 | -57.33654 | 2024-10-12 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 86.1 |
| d4c69f59-c4ee-3fe9-8b5f-a7370929be3e | -17.83353 | -57.30419 | 2024-10-12 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 01575aba-4080-3e27-bf05-227b7d6eaf58 | -17.83302 | -57.30818 | 2024-10-12 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.1 |
| df1010b1-2306-30f6-9231-d1ec5d8a9552 | -17.83251 | -57.31215 | 2024-10-12 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.1 |
| a3a3c896-2b51-3cc6-ab50-e4329fd9b7e7 | -17.832 | -57.31612 | 2024-10-12 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 3c4c7a62-a766-3a70-bd44-5e06f27fd5da | -17.8315 | -57.32009 | 2024-10-12 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.7 |
| c3618de0-df94-37f0-8a43-9a09dbc00b0b | -17.83099 | -57.32405 | 2024-10-12 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 40ddb588-2ae6-3d03-8f63-17d8cea7ea45 | -17.83048 | -57.32804 | 2024-10-12 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 8fb7e0c7-0ebf-3d0b-94fc-91e76616cd52 | -17.82933 | -57.30361 | 2024-10-12 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 1233753a-5ea6-3475-ba53-9fe8ac6d14c1 | -17.82997 | -57.33199 | 2024-10-12 05:25:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.5 |
| b89b5694-c04b-3b84-9476-966660a92780 | -17.82947 | -57.33596 | 2024-10-12 05:25:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.5 |
| 6ccb3940-d192-3d72-960b-a244ef618508 | -17.21586 | -57.30745 | 2024-10-12 05:25:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 0.7 |
| fd287f04-bb14-36c3-9a73-07ff6448ab79 | -17.21535 | -57.31133 | 2024-10-12 05:25:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 0.7 |
| 1e40c640-cd53-3601-acbc-9c0ed926e35c | -17.21484 | -57.31521 | 2024-10-12 05:25:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| cb875c16-677a-341a-bbdc-d8a98b168253 | -17.20602 | -57.31792 | 2024-10-12 05:25:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 245d68ff-85bd-3efd-9a7c-f12257a48d8c | -17.98375 | -57.37084 | 2024-10-12 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.0 |
| 77e961ea-4bb1-3c2e-b21d-5b480b36a97c | -17.98326 | -57.36807 | 2024-10-12 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.1 |
| 4ae6a566-3afd-35f2-b557-e86a2a507b76 | -17.98325 | -57.37481 | 2024-10-12 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| f577c312-9000-3507-948f-547ff29c6db6 | -17.98276 | -57.37877 | 2024-10-12 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 4cc1e9fe-3252-3983-9ca9-3bd303413ace | -17.98222 | -57.37598 | 2024-10-12 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.8 |
| f96ac27b-be7d-3743-8073-1e5bda3356f2 | -17.98005 | -57.36628 | 2024-10-12 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.2 |
| 39a0d213-7711-353a-ba04-294b7b127713 | -17.97956 | -57.37025 | 2024-10-12 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.2 |
| 17969cfa-f3a6-31c5-b24c-c43662f2b939 | -17.97908 | -57.36749 | 2024-10-12 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.1 |
| 869c5080-10b9-3251-8005-19ab2adc949e | -17.97907 | -57.37422 | 2024-10-12 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.4 |
| ea499609-722d-3002-9225-106f4263258d | -17.97858 | -57.37818 | 2024-10-12 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.4 |
| ed15883c-a477-37a8-9ba6-82f2c351ba0c | -17.97856 | -57.37145 | 2024-10-12 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.1 |
| 4c4e4ea0-4a75-314f-98d2-92945a878686 | -17.97537 | -57.36966 | 2024-10-12 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.2 |
| e3014d36-d5a6-3e1b-a3da-add7b7de3a46 | -17.97488 | -57.37363 | 2024-10-12 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 94f261e5-9195-3290-9336-38650fcbf4f3 | -17.97439 | -57.37759 | 2024-10-12 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 0fc39193-fab3-337e-bae1-73ce87d14081 | -17.97437 | -57.37086 | 2024-10-12 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 24.2 |
| de9b08f2-5cb9-3a83-a104-09874b05ccf3 | -17.97386 | -57.37482 | 2024-10-12 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.6 |
| c27f9333-8c5c-3bcd-a34a-d2687a6b4ad2 | -17.97334 | -57.37877 | 2024-10-12 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.6 |
| 3f8a5d06-159f-379c-8dc6-fd8293f4e406 | -17.97019 | -57.37029 | 2024-10-12 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 24.2 |
| 9482e3a2-eac8-304b-99f5-2e144bf4ee38 | -17.96968 | -57.37424 | 2024-10-12 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.6 |
| 0c43f8c5-fc6b-3399-a63e-64b2df446626 | -17.96916 | -57.37819 | 2024-10-12 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.6 |
| 6e0d8bdc-faf9-3a98-ad85-36b7f5324429 | -17.96864 | -57.38214 | 2024-10-12 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.5 |
| b8e017b9-8c42-3ddb-869a-014e5c93d875 | -17.96549 | -57.37365 | 2024-10-12 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.6 |
| 1f7cfb1a-dd92-35ff-a5d0-3da978cac18a | -17.96498 | -57.37761 | 2024-10-12 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.6 |
| c6a02ccd-f673-3cb0-bfb7-c9bf4bc2f164 | -17.96446 | -57.38155 | 2024-10-12 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.0 |
| 9a0a0a7d-cae6-3226-81d6-c652b7745b7d | -17.89318 | -57.33931 | 2024-10-12 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.6 |
| 797b0d43-9e9a-31bc-9bec-95f8a4161174 | -17.89268 | -57.34328 | 2024-10-12 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.6 |
| 6193e636-fcee-3684-8af6-210aae18822e | -17.88898 | -57.33873 | 2024-10-12 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.6 |
| 7388d7f3-1b33-39e0-8b7c-f471c4995e68 | -17.88849 | -57.3427 | 2024-10-12 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.6 |
| 5a2f936d-73ff-30f6-a8f2-f811e0e79c2b | -17.8848 | -57.33815 | 2024-10-12 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 1d9859cb-67f8-30ed-aa52-3f3f052ef5a8 | -17.8843 | -57.34212 | 2024-10-12 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 53112c1c-db14-3afb-a12b-4de7116b6a20 | -17.88381 | -57.34608 | 2024-10-12 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 843056ac-80a0-377a-bbd7-e3395e6201ca | -17.88011 | -57.34152 | 2024-10-12 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 7693cdfc-1200-3228-a470-c6c713eb3afb | -17.8797 | -57.34297 | 2024-10-12 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| adf56acb-42d8-3b15-8d7c-b645761e68aa | -17.87962 | -57.34549 | 2024-10-12 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 8bda7db6-72b5-3b18-bc6a-f036e7c17e74 | -17.87918 | -57.34693 | 2024-10-12 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 3b1924b6-6eeb-38b9-9fc9-ade0286aabc1 | -17.87543 | -57.34489 | 2024-10-12 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 0f3181db-ec4a-3190-bd5b-e4559e3ea60c | -17.87499 | -57.34634 | 2024-10-12 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 427f5943-5c32-3e9e-a243-4d5442726c2c | -17.87494 | -57.34886 | 2024-10-12 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 66ef6751-41f3-39a8-9b57-94674e4023c6 | -17.87448 | -57.3503 | 2024-10-12 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.3 |
| e0492adb-8051-38e8-8051-3ed39425e963 | -17.87076 | -57.34826 | 2024-10-12 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 5fee1f48-0f6c-367d-b24b-800a605222a1 | -17.87029 | -57.34971 | 2024-10-12 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.9 |
| 18ce03f9-5a4d-3644-bb2c-b0545aee30bd | -17.87027 | -57.35223 | 2024-10-12 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.0 |
| 020d7804-facd-30d5-b317-2fb440cd24f4 | -17.86559 | -57.35308 | 2024-10-12 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 8.1 |
| 64051185-b12b-30b1-987b-74e838598317 | -17.86141 | -57.35251 | 2024-10-12 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 82c4629b-ef6a-3625-bc16-1e8de97d54b8 | -17.86089 | -57.35646 | 2024-10-12 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| b28537df-87b7-395e-98ac-49f48870a412 | -17.86038 | -57.36042 | 2024-10-12 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.2 |
| 7db50872-5e4d-3a9a-9d1b-0fe3d8a9853f | -17.85671 | -57.3559 | 2024-10-12 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 21437339-a03e-33e6-b8fd-6f8bd3e68ecf | -17.85458 | -57.33948 | 2024-10-12 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 77ede8ea-c74f-3633-a013-6bbe2d5661e8 | -17.85304 | -57.35136 | 2024-10-12 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| d5ac7def-eb0b-3db3-a5d5-0240ac6908c4 | -17.85253 | -57.35531 | 2024-10-12 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| bf325a37-5c94-370d-8371-df5506e8ac61 | -17.85201 | -57.35926 | 2024-10-12 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.8 |
| 4fcf6f58-9908-3d8d-88db-fc7c60d0864d | -17.83529 | -57.35691 | 2024-10-12 05:25:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.9 |
| 2e12b031-10e0-3976-9be0-60833ead80b0 | -17.83263 | -57.34446 | 2024-10-12 05:25:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| dd9e52b5-d1a0-330d-8c40-95d1f41de7e3 | -17.83213 | -57.34843 | 2024-10-12 05:25:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 07b5c50e-8efa-3086-8741-1f2c46c0c150 | -17.82896 | -57.33992 | 2024-10-12 05:25:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 332e9119-c276-3e64-beaf-436b797e4898 | -17.82845 | -57.34388 | 2024-10-12 05:25:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 7533a1e1-6ce3-36cc-8b4d-c5b21d6cd38d | -17.87077 | -57.31343 | 2024-10-12 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 154.0 |
| ea5bddc1-e1d9-3528-8477-26f33257f967 | -17.87025 | -57.3174 | 2024-10-12 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 154.0 |
| 9bb09696-0631-3fad-acce-c8491b34486c | -17.86973 | -57.32137 | 2024-10-12 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.5 |
| fe4a64ad-6b60-3f6d-b14a-b57381cbbff2 | -17.86921 | -57.32535 | 2024-10-12 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.5 |


[Clique aqui para ver as próximas entradas](README124.md)
