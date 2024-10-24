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

## Dados Diários - Página 114

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1e1effe9-3df8-3dbe-b34b-d6337bad90ba | -17.2383 | -57.2462 | 2024-10-24 11:56:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 281.6 |
| 173a97f0-83ee-3b4f-9ee2-d1fea30d07c6 | -17.2186 | -57.2485 | 2024-10-24 11:56:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 93.3 |
| b3650b62-98ad-357b-9874-f1b1d0cde912 | -17.2579 | -57.2439 | 2024-10-24 11:56:44 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 188.2 |
| 18babdce-dc4a-3b75-a744-687c8cdb53c2 | -17.2773 | -57.2621 | 2024-10-24 11:56:44 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 76.5 |
| 1346b71c-ae2f-3610-a789-96c7ff1178e7 | -17.2583 | -57.2233 | 2024-10-24 11:56:44 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 160.9 |
| 31908bb6-eb4b-35ee-98d6-a23300a49cfc | -17.6868 | -57.4593 | 2024-10-24 11:56:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 75.7 |
| 8f0dea7d-ae60-3e08-bbf3-9aedbef2158b | -17.7644 | -57.532 | 2024-10-24 11:56:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 97.5 |
| e4874fee-05b9-3c85-bc28-976ba982a1bc | -17.6671 | -57.4616 | 2024-10-24 11:56:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 75.4 |
| 95bfeac6-e62d-3175-a3eb-5aa0a6a773ba | -17.764 | -57.5526 | 2024-10-24 11:56:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 72.5 |
| 1f7dbb5b-55da-316d-ba73-687a67cf011a | -17.6865 | -57.4798 | 2024-10-24 11:56:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 82.7 |
| 026dfd20-205e-3457-a991-619d9b6d74b5 | -18.0837 | -57.3076 | 2024-10-24 11:56:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 75.7 |
| 5144671c-ffd1-3267-a5b1-7b0552544ca7 | -18.284 | -56.0367 | 2024-10-24 11:56:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 121.0 |
| fa5f479b-bb41-3cb3-89f7-3fa8bc1fbaab | -18.2641 | -56.0394 | 2024-10-24 11:56:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 362.3 |
| 792a650a-b7d1-33ac-9f65-92cb6da7aeca | -18.2637 | -56.0603 | 2024-10-24 11:56:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 218.4 |
| 86fce3ae-0459-3c40-be6e-a69ddf99be3b | -18.2836 | -56.0576 | 2024-10-24 11:56:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 73.6 |
| 730e2a1d-c712-3dfb-9cbf-99171c611d7f | -19.5693 | -56.5484 | 2024-10-24 11:56:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 85.3 |
| 06b41ac3-5e79-3098-a90a-f830236b5ab4 | -19.5681 | -56.6114 | 2024-10-24 11:56:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 94.6 |
| 4c4fe6a6-a27c-3a37-bd93-44161408088d | -19.6438 | -56.8521 | 2024-10-24 11:56:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 97.4 |
| 17ba9088-d6d0-36f4-b9d1-49a78c76ef77 | -16.9596 | -57.5245 | 2024-10-24 12:06:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 105.2 |
| 59376a93-fc5c-3aaf-87ca-4b82103af3a0 | -17.0188 | -57.4973 | 2024-10-24 12:06:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 77.0 |
| e80c0a89-6dec-366d-84c1-0fc2b7f52c5f | -17.0184 | -57.5178 | 2024-10-24 12:06:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 74.0 |
| 10bf8724-313e-325e-b3fe-818e757d7b91 | -17.0387 | -57.4745 | 2024-10-24 12:06:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 79.3 |
| a9e50045-1a1d-3839-9d2d-40371f16f4ad | -17.0384 | -57.495 | 2024-10-24 12:06:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 71.8 |
| 2e5b850b-2d1e-39db-b3be-0fc739694a8b | -16.9792 | -57.5223 | 2024-10-24 12:06:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 117.8 |
| 34dae839-148f-301d-9a17-4093cd8f262e | -17.039 | -57.454 | 2024-10-24 12:06:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 71.1 |
| 9c2e6597-c5f9-3b44-9a5e-1e196f522259 | -17.6865 | -57.4798 | 2024-10-24 12:06:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 151.2 |
| 215ca632-2962-3eff-b091-57a0be359b8e | -17.7644 | -57.532 | 2024-10-24 12:06:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 79.8 |
| ac05f1ac-2c47-3d62-99df-36e33734b57e | -17.6868 | -57.4593 | 2024-10-24 12:06:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 147.0 |
| e3f8c7dc-f44d-3679-bdac-7beb968c308f | -17.7062 | -57.4774 | 2024-10-24 12:06:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 76.8 |
| 2b93eea3-c694-3622-bd21-a8bd5e313ab7 | -17.764 | -57.5526 | 2024-10-24 12:06:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 74.5 |
| 033c5c85-7806-3e7a-9cdc-7a8089fe4ee2 | -17.7082 | -57.3539 | 2024-10-24 12:06:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 75.0 |
| d97121d6-85ac-3fde-bff7-0629c806eb25 | -17.6671 | -57.4616 | 2024-10-24 12:06:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 71.8 |
| 16217c00-b7b2-3ad8-81e3-0a5de1fc7ec3 | -18.0837 | -57.3076 | 2024-10-24 12:06:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 95.1 |
| 1d8d3205-5f07-34ac-aa31-0af32252bc19 | -18.0834 | -57.3283 | 2024-10-24 12:06:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 74.1 |
| 22530cd6-a020-3e15-a5b0-c447493c60bc | -18.2836 | -56.0576 | 2024-10-24 12:06:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 234.3 |
| 1dbc6a8d-e46f-3881-a6cc-6050589312de | -18.2637 | -56.0603 | 2024-10-24 12:06:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 319.5 |
| 1a2e13b1-e252-3f5e-9c6a-9b445d1a8389 | -18.2641 | -56.0394 | 2024-10-24 12:06:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 556.8 |
| 1cb9b90f-d803-3db7-8eef-7c59c464d9dc | -18.2439 | -56.063 | 2024-10-24 12:06:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 68.8 |
| fc2c003b-a1a9-3d68-bd33-9b2beaf2b68a | -18.284 | -56.0367 | 2024-10-24 12:06:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 459.3 |
| 16e2e29a-2003-3a53-8d91-6a8c512866a2 | -19.5492 | -56.5512 | 2024-10-24 12:06:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 65.6 |
| 2c397868-099d-3406-933c-223a3f97b6ea | -19.5681 | -56.6114 | 2024-10-24 12:06:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 91.0 |
| 87625c9e-0ac0-3224-85e2-ee70ea6191b4 | -19.5693 | -56.5484 | 2024-10-24 12:06:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 74.7 |
| 95985507-48b3-3623-861f-7e65fa499116 | -19.548 | -56.6143 | 2024-10-24 12:06:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 71.3 |
| 9c7e644c-9f40-38cf-a791-2cdb2f140d67 | -19.6438 | -56.8521 | 2024-10-24 12:06:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 92.1 |
| d3c62b78-20e4-34d3-bde5-82f89165bb52 | -4.43855 | -39.35301 | 2024-10-24 12:10:00 | TERRA_M-T | CANINDÉ | CEARÁ | Brasil | 2302800 | 23 | 33 | nan | nan | nan | Caatinga | 10.6 |
| 2c76bc9c-7db8-32f3-bb1f-cda49696b6f4 | -4.43724 | -39.36198 | 2024-10-24 12:10:00 | TERRA_M-T | CANINDÉ | CEARÁ | Brasil | 2302800 | 23 | 33 | nan | nan | nan | Caatinga | 8.6 |
| 28e2c7f8-fec1-3210-82ad-9819fe83c62b | -3.53598 | -41.62563 | 2024-10-24 12:10:00 | TERRA_M-T | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 32.6 |
| 7d9a08c7-2946-32c1-95ff-a49a7406f28f | -3.67231 | -42.36446 | 2024-10-24 12:10:00 | TERRA_M-T | LUZILÂNDIA | PIAUÍ | Brasil | 2205805 | 22 | 33 | nan | nan | nan | Caatinga | 14.8 |
| bd958318-c3da-31bd-9365-ed626bd8467e | -4.14192 | -43.07064 | 2024-10-24 12:10:00 | TERRA_M-T | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 14.9 |
| b87a637f-1397-320d-8999-92250cbc8237 | -3.41254 | -43.18417 | 2024-10-24 12:10:00 | TERRA_M-T | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 19.7 |
| 9846ce04-102f-3404-b2a6-3bbe2846dc56 | -3.41114 | -43.19318 | 2024-10-24 12:10:00 | TERRA_M-T | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 17.0 |
| 15fbc16f-a273-389d-b960-8c87bc01ae5c | -8.27835 | -37.63122 | 2024-10-24 12:12:00 | TERRA_M-T | CUSTÓDIA | PERNAMBUCO | Brasil | 2605103 | 26 | 33 | nan | nan | nan | Caatinga | 132.2 |
| 80bc3757-3fbf-3a3b-8aae-ea95de70c622 | -8.27701 | -37.64092 | 2024-10-24 12:12:00 | TERRA_M-T | CUSTÓDIA | PERNAMBUCO | Brasil | 2605103 | 26 | 33 | nan | nan | nan | Caatinga | 9.1 |
| 36427064-4e32-39dd-8bcc-c0eb81bc9873 | -8.27196 | -37.62439 | 2024-10-24 12:12:00 | TERRA_M-T | CUSTÓDIA | PERNAMBUCO | Brasil | 2605103 | 26 | 33 | nan | nan | nan | Caatinga | 72.8 |
| c7848b9c-bc3a-37a2-8a08-9ce68be657c5 | -8.27058 | -37.63412 | 2024-10-24 12:12:00 | TERRA_M-T | CUSTÓDIA | PERNAMBUCO | Brasil | 2605103 | 26 | 33 | nan | nan | nan | Caatinga | 172.4 |
| 17a7fcc9-e6ca-36c2-85ee-91f56006c1ea | -6.49237 | -37.43665 | 2024-10-24 12:12:00 | TERRA_M-T | SÃO BENTO | PARAÍBA | Brasil | 2513901 | 25 | 33 | nan | nan | nan | Caatinga | 8.1 |
| ef149067-edfb-3034-928b-8fbe4f22a60b | -6.29168 | -37.68441 | 2024-10-24 12:12:00 | TERRA_M-T | CATOLÉ DO ROCHA | PARAÍBA | Brasil | 2504306 | 25 | 33 | nan | nan | nan | Caatinga | 9.3 |
| a3dedb41-6e7e-3b64-80c4-28788393a56d | -6.19537 | -38.42189 | 2024-10-24 12:12:00 | TERRA_M-T | SÃO MIGUEL | RIO GRANDE DO NORTE | Brasil | 2412500 | 24 | 33 | nan | nan | nan | Caatinga | 13.4 |
| b4a95890-c536-3c3c-a748-2911412b8306 | -7.86241 | -37.91288 | 2024-10-24 12:12:00 | TERRA_M-T | FLORES | PERNAMBUCO | Brasil | 2605608 | 26 | 33 | nan | nan | nan | Caatinga | 9.1 |
| 7fb86f81-3d2a-31ac-af5e-555a2732dad0 | -7.76279 | -38.80859 | 2024-10-24 12:12:00 | TERRA_M-T | SÃO JOSÉ DO BELMONTE | PERNAMBUCO | Brasil | 2613503 | 26 | 33 | nan | nan | nan | Caatinga | 15.3 |
| 4125d613-a6d2-3b92-a4b0-bb61510286ac | -7.13862 | -37.81985 | 2024-10-24 12:12:00 | TERRA_M-T | PIANCÓ | PARAÍBA | Brasil | 2511301 | 25 | 33 | nan | nan | nan | Caatinga | 21.5 |
| ccd9d048-f9ba-32d5-bd38-18d7ebc55c38 | -10.24849 | -39.34376 | 2024-10-24 12:12:00 | TERRA_M-T | MONTE SANTO | BAHIA | Brasil | 2921500 | 29 | 33 | nan | nan | nan | Caatinga | 28.4 |
| 50a8d45d-c015-38e3-9646-7981140f6422 | -10.24721 | -39.35271 | 2024-10-24 12:12:00 | TERRA_M-T | MONTE SANTO | BAHIA | Brasil | 2921500 | 29 | 33 | nan | nan | nan | Caatinga | 14.5 |
| c382bc09-6515-351f-9e7d-7e985497c164 | -11.95232 | -38.95088 | 2024-10-24 12:12:00 | TERRA_M-T | SANTA BÁRBARA | BAHIA | Brasil | 2927507 | 29 | 33 | nan | nan | nan | Caatinga | 11.1 |
| 886ee9d7-cc5a-3607-bc61-cb5dc3bf1e42 | -5.45259 | -39.09608 | 2024-10-24 12:12:00 | TERRA_M-T | QUIXERAMOBIM | CEARÁ | Brasil | 2311405 | 23 | 33 | nan | nan | nan | Caatinga | 13.7 |
| 9f1365c5-aa0e-3b97-898b-34ab05106b3f | -5.31618 | -39.15178 | 2024-10-24 12:12:00 | TERRA_M-T | QUIXERAMOBIM | CEARÁ | Brasil | 2311405 | 23 | 33 | nan | nan | nan | Caatinga | 6.0 |
| 458529ed-4b1a-3b44-a1fb-c75e8a8d1722 | -5.1212 | -39.41101 | 2024-10-24 12:12:00 | TERRA_M-T | QUIXERAMOBIM | CEARÁ | Brasil | 2311405 | 23 | 33 | nan | nan | nan | Caatinga | 6.1 |
| d7ab2a51-75a1-3fd9-a7b8-5a09aae8edab | -8.794 | -40.84243 | 2024-10-24 12:12:00 | TERRA_M-T | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 6.2 |
| 51de95cf-7906-3304-b867-36385ece9be7 | -8.46957 | -40.47812 | 2024-10-24 12:12:00 | TERRA_M-T | DORMENTES | PERNAMBUCO | Brasil | 2605152 | 26 | 33 | nan | nan | nan | Caatinga | 7.6 |
| 9b1b4bf4-6a7a-3479-9d21-9b0659506bfa | -8.2076 | -39.87173 | 2024-10-24 12:12:00 | TERRA_M-T | PARNAMIRIM | PERNAMBUCO | Brasil | 2610400 | 26 | 33 | nan | nan | nan | Caatinga | 11.9 |
| 4f4c4f31-8620-3167-9415-8819836535f7 | -10.77347 | -40.48877 | 2024-10-24 12:12:00 | TERRA_M-T | MIRANGABA | BAHIA | Brasil | 2921401 | 29 | 33 | nan | nan | nan | Caatinga | 6.1 |
| f2caf2e6-102b-3b0b-acd5-c34b931f8842 | -10.42778 | -40.57917 | 2024-10-24 12:12:00 | TERRA_M-T | CAMPO FORMOSO | BAHIA | Brasil | 2906006 | 29 | 33 | nan | nan | nan | Caatinga | 5.2 |
| 8434cfdc-843c-337e-9d83-6626e3ad34f3 | -11.53162 | -41.4132 | 2024-10-24 12:12:00 | TERRA_M-T | MORRO DO CHAPÉU | BAHIA | Brasil | 2921708 | 29 | 33 | nan | nan | nan | Caatinga | 13.2 |
| e0d08644-9c2f-3dd0-be77-6d21d0ca04c7 | -11.41932 | -41.05175 | 2024-10-24 12:12:00 | TERRA_M-T | MORRO DO CHAPÉU | BAHIA | Brasil | 2921708 | 29 | 33 | nan | nan | nan | Caatinga | 9.0 |
| 50a0e10f-7080-3fb8-a576-01cdbc9ae7f1 | -6.90875 | -41.4786 | 2024-10-24 12:12:00 | TERRA_M-T | SÃO JOSÉ DO PIAUÍ | PIAUÍ | Brasil | 2210201 | 22 | 33 | nan | nan | nan | Caatinga | 14.1 |
| 54e2c727-749f-3e70-af22-da1268a38cc1 | -6.7764 | -40.89322 | 2024-10-24 12:12:00 | TERRA_M-T | ALAGOINHA DO PIAUÍ | PIAUÍ | Brasil | 2200251 | 22 | 33 | nan | nan | nan | Caatinga | 11.1 |
| 11e96b54-a2e9-3fa6-855a-74d05326fcda | -6.46188 | -41.77709 | 2024-10-24 12:12:00 | TERRA_M-T | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 13.5 |
| c17de09e-3d91-39fd-b6db-1145ed94799d | -8.83591 | -41.05635 | 2024-10-24 12:12:00 | TERRA_M-T | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 15.6 |
| e221a8f1-0356-38ff-b4cc-8b74ed801a2f | -8.7606 | -41.30886 | 2024-10-24 12:12:00 | TERRA_M-T | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 7.7 |
| f5f31840-1b21-31da-b74b-9a650ce0267c | -8.75283 | -41.311 | 2024-10-24 12:12:00 | TERRA_M-T | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 8.7 |
| cdebe878-b105-3b3c-9bbb-ad5bf12030ac | -8.46603 | -41.37976 | 2024-10-24 12:12:00 | TERRA_M-T | QUEIMADA NOVA | PIAUÍ | Brasil | 2208650 | 22 | 33 | nan | nan | nan | Caatinga | 19.4 |
| e94beaf7-9550-37d4-a42a-adce21b51e53 | -8.0035 | -41.39087 | 2024-10-24 12:12:00 | TERRA_M-T | JACOBINA DO PIAUÍ | PIAUÍ | Brasil | 2205151 | 22 | 33 | nan | nan | nan | Caatinga | 6.9 |
| 4fe8800e-a75c-385e-902a-27a253f9d3ee | -10.49573 | -42.54518 | 2024-10-24 12:12:00 | TERRA_M-T | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 6.8 |
| 31284ca9-142f-3f1c-bd93-d453e0214141 | -10.16412 | -42.4536 | 2024-10-24 12:12:00 | TERRA_M-T | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 7.7 |
| 53a3a517-297a-3a46-a3c5-d851e979d40d | -12.08222 | -42.77276 | 2024-10-24 12:12:00 | TERRA_M-T | OLIVEIRA DOS BREJINHOS | BAHIA | Brasil | 2923209 | 29 | 33 | nan | nan | nan | Caatinga | 11.8 |
| 36739514-213e-3f52-a1d9-d6ee123e3d4c | -11.47684 | -42.83111 | 2024-10-24 12:12:00 | TERRA_M-T | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 16.1 |
| b1ca4270-d80b-329e-a4ed-44ba79a7630b | -11.46718 | -42.82965 | 2024-10-24 12:12:00 | TERRA_M-T | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 58.2 |
| 6c04329c-bd9b-37cb-8181-a5dab8d999f3 | -11.46554 | -42.84045 | 2024-10-24 12:12:00 | TERRA_M-T | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 8.3 |
| 5ee833af-eee5-39cd-9e02-d09424c401ac | -12.17065 | -42.54702 | 2024-10-24 12:12:00 | TERRA_M-T | BROTAS DE MACAÚBAS | BAHIA | Brasil | 2904506 | 29 | 33 | nan | nan | nan | Caatinga | 7.2 |
| 075f6d29-69f7-3655-8078-9a58536fc963 | -12.1646 | -42.55052 | 2024-10-24 12:12:00 | TERRA_M-T | BROTAS DE MACAÚBAS | BAHIA | Brasil | 2904506 | 29 | 33 | nan | nan | nan | Caatinga | 10.3 |
| bc73b01d-16ce-3ac1-bc80-29d409560542 | -11.63876 | -41.68694 | 2024-10-24 12:12:00 | TERRA_M-T | CANARANA | BAHIA | Brasil | 2906204 | 29 | 33 | nan | nan | nan | Caatinga | 6.1 |
| 3c65acc5-3950-35dd-bc5b-5c20c8e8e36c | -11.56433 | -42.18547 | 2024-10-24 12:12:00 | TERRA_M-T | IBIPEBA | BAHIA | Brasil | 2912400 | 29 | 33 | nan | nan | nan | Caatinga | 74.2 |
| 70033e04-0b6d-38c2-a0c4-1b4cc5d562f6 | -5.7715 | -42.6353 | 2024-10-24 12:12:00 | TERRA_M-T | AGRICOLÂNDIA | PIAUÍ | Brasil | 2200103 | 22 | 33 | nan | nan | nan | Caatinga | 12.5 |
| cc4e1fb6-1a3a-30a9-b337-2bf0123d88f1 | -5.23012 | -43.17851 | 2024-10-24 12:12:00 | TERRA_M-T | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 14.4 |
| adebc891-b852-33e4-b892-2ae30140c83e | -6.86127 | -42.81088 | 2024-10-24 12:12:00 | TERRA_M-T | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 32.0 |
| 9f0c2fa1-59e8-39fe-8bbf-fb943f02244d | -7.38006 | -43.43035 | 2024-10-24 12:12:00 | TERRA_M-T | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 18.0 |
| d4c14119-859f-3682-8959-5a3174a117e8 | -7.37802 | -43.44362 | 2024-10-24 12:12:00 | TERRA_M-T | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 28.1 |
| 44e89b41-4f83-36a6-9e75-d488d1cced9e | -9.05213 | -43.07571 | 2024-10-24 12:12:00 | TERRA_M-T | SÃO BRAZ DO PIAUÍ | PIAUÍ | Brasil | 2209559 | 22 | 33 | nan | nan | nan | Caatinga | 11.0 |
| 7fb740e3-ccb4-3815-a0ca-ac67242ba6db | -9.05025 | -43.08773 | 2024-10-24 12:12:00 | TERRA_M-T | SÃO BRAZ DO PIAUÍ | PIAUÍ | Brasil | 2209559 | 22 | 33 | nan | nan | nan | Caatinga | 11.6 |
| 712e1233-d812-3298-a4b8-39e497826ec8 | -9.04401 | -42.66611 | 2024-10-24 12:12:00 | TERRA_M-T | SÃO RAIMUNDO NONATO | PIAUÍ | Brasil | 2210607 | 22 | 33 | nan | nan | nan | Caatinga | 13.1 |


[Clique aqui para ver as próximas entradas](README115.md)
