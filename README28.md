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

## Dados Diários - Página 28

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 668409c9-36d6-3093-8cb0-8c541f8df06e | -16.941401 | -56.615299 | 2024-10-06 01:40:55 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 81d396b3-a943-36e4-8a1b-3fa644f10d81 | -16.943501 | -56.624001 | 2024-10-06 01:40:55 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| b628bde5-89bb-3c0a-9b12-370582c2632d | -16.972601 | -56.744801 | 2024-10-06 01:40:55 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| bff49973-5b6c-36c6-ab47-56a652d8bd6e | -16.974701 | -56.753399 | 2024-10-06 01:40:55 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 65c8bd3b-2b3d-36cd-a33c-8892f7ce9134 | -16.9767 | -56.762001 | 2024-10-06 01:40:55 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 9a51b6d7-edd1-33a0-9cce-aa5a8f51d054 | -16.9788 | -56.7705 | 2024-10-06 01:40:55 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| e28d214f-70c1-3daa-ac0e-b6135b27f4f0 | -16.980801 | -56.779099 | 2024-10-06 01:40:55 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 44595921-ebe0-3ff6-8185-8e5bc5b988ff | -16.982901 | -56.787601 | 2024-10-06 01:40:55 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| acd0b9ff-e4ba-3732-827c-79f3a140db13 | -16.985001 | -56.7962 | 2024-10-06 01:40:55 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 8f059ebe-38b1-30c6-9f48-49d4451546d2 | -16.987 | -56.804699 | 2024-10-06 01:40:55 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 725051b6-9aab-3e21-9ba6-b047323a6d3b | -16.989 | -56.813202 | 2024-10-06 01:40:55 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| ec8f4a85-26c8-3546-949b-67088196d2b9 | -16.9911 | -56.821701 | 2024-10-06 01:40:55 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| a4fd5e7b-c638-3f1b-a5d1-4e371fb48bea | -17.121201 | -57.3675 | 2024-10-06 01:40:55 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 86e9c69a-070a-319e-94c7-4dd6b0b4beaf | -17.1231 | -57.3755 | 2024-10-06 01:40:55 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| d2fbf387-50e0-381f-a41d-35200a83ffbe | -17.1308 | -57.4077 | 2024-10-06 01:40:55 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 29672622-3ced-367c-bc86-b6139d2572f2 | -17.1327 | -57.415699 | 2024-10-06 01:40:55 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| a4459a16-ff5c-3486-b819-933edd1f3530 | -17.1346 | -57.423698 | 2024-10-06 01:40:55 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| b265580b-b0ec-3af3-83e1-32321be9b95f | -16.929501 | -56.6091 | 2024-10-06 01:40:55 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| b0b51988-022a-340a-9722-eb0129846e56 | -16.931601 | -56.617802 | 2024-10-06 01:40:55 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 41796040-0d1d-3356-bf27-b0bd0ce235ed | -16.962799 | -56.747299 | 2024-10-06 01:40:55 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| fbd37062-4e86-3efb-b8ef-4e51dcb04b78 | -16.964899 | -56.755901 | 2024-10-06 01:40:55 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 1073193f-8a40-3210-b0fc-b0dfd56cfac2 | -16.9669 | -56.7645 | 2024-10-06 01:40:55 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 034f1df6-6126-3654-9356-6c7f7a3579fe | -16.969 | -56.772999 | 2024-10-06 01:40:55 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 2b27fda9-27a4-36d1-838a-0bf0b97090c5 | -16.9711 | -56.781601 | 2024-10-06 01:40:55 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 38ec0ac9-a93c-34c6-b510-3eea3400ece7 | -16.973101 | -56.7901 | 2024-10-06 01:40:55 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 434e5282-6d42-3c18-b5c0-5d8da5d473a4 | -16.975201 | -56.798698 | 2024-10-06 01:40:55 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| b47bf536-dd55-3d61-a2b1-3928fe4b03c8 | -16.9772 | -56.807201 | 2024-10-06 01:40:55 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| be807de8-1fb8-355c-90b1-fc9a5472f56e | -17.1115 | -57.369999 | 2024-10-06 01:40:55 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 24ab82ef-0a32-3813-a5eb-5259fe1d4853 | -17.1134 | -57.377998 | 2024-10-06 01:40:55 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 6e9a998c-10f7-3e6a-baf2-81ea7ba48ec3 | -17.115299 | -57.386101 | 2024-10-06 01:40:55 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 7dc053ed-4951-3ca3-b948-05bb0a7f7600 | -17.117201 | -57.3941 | 2024-10-06 01:40:55 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 73746789-e96a-365e-b0a2-32d0b72cdd53 | -17.119101 | -57.402199 | 2024-10-06 01:40:55 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| e62f2b82-ab39-34be-be3a-bb39543fc1e9 | -17.121 | -57.410198 | 2024-10-06 01:40:55 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 30904b72-f102-3b24-9132-ad1043d598de | -17.1229 | -57.418201 | 2024-10-06 01:40:55 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 187f969d-3509-3282-bde5-63ff2b71066a | -17.1248 | -57.426201 | 2024-10-06 01:40:55 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 677663a2-710e-3a95-9041-4b4b5aea1255 | -16.659401 | -55.5448 | 2024-10-06 01:40:55 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 6debcfae-67ba-3d4f-a694-0b0034b9a368 | -16.9552 | -56.7584 | 2024-10-06 01:40:55 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| df581ad1-35c8-3641-bcdf-20497036d6b1 | -16.957199 | -56.766998 | 2024-10-06 01:40:55 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 468da281-cb59-313e-adba-10eafbd5e83d | -16.959299 | -56.775501 | 2024-10-06 01:40:55 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| ac04fd58-8c70-333c-9d28-5cc7890d43b5 | -16.9613 | -56.7841 | 2024-10-06 01:40:55 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 32332b33-7e68-3f5f-a982-815b580b437a | -16.9634 | -56.792599 | 2024-10-06 01:40:55 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| ad1b84c8-5e89-3412-b991-ddef61f5b1a7 | -16.9655 | -56.801201 | 2024-10-06 01:40:55 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| a6585351-b026-3dc0-9717-4fd44ce9623b | -17.1017 | -57.372398 | 2024-10-06 01:40:55 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 588a4f08-6fed-3c75-b916-191fd4fc2d0d | -17.1036 | -57.380501 | 2024-10-06 01:40:55 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 3e4fbd50-9684-3e9a-9417-58094a104d96 | -17.105499 | -57.3885 | 2024-10-06 01:40:55 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 49458b2e-af55-3e10-ad7a-38eda472dc69 | -17.107401 | -57.3965 | 2024-10-06 01:40:55 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| c6681923-16e7-336e-9fdb-0b1ba148a5fc | -17.109301 | -57.404598 | 2024-10-06 01:40:55 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 0cafaad2-927d-3335-a931-a8052f99650a | -17.1112 | -57.412601 | 2024-10-06 01:40:55 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 83e58178-280f-3167-aaab-945eaa38822e | -17.1131 | -57.420601 | 2024-10-06 01:40:55 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| ed58d528-3baa-3187-a99b-40b4b656d8b6 | -16.6422 | -55.517502 | 2024-10-06 01:40:55 | METOP-C | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| ad3b4332-a760-30a1-a503-d1b0a57c0c8d | -16.6446 | -55.5275 | 2024-10-06 01:40:55 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 89297e04-5f3c-3561-b471-7e3222fa20a5 | -16.6471 | -55.537498 | 2024-10-06 01:40:55 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 9de827f4-d50b-3472-a920-f6134128bb75 | -16.649599 | -55.547401 | 2024-10-06 01:40:55 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| dd3e04ce-3545-3587-96f9-bcff68acb6c2 | -17.0996 | -57.407101 | 2024-10-06 01:40:55 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| ebf8f226-838b-39b9-99e2-f5054016ec5e | -17.1015 | -57.4151 | 2024-10-06 01:40:55 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 63115e2f-1b06-3c18-a5eb-e75671345a1a | -16.629999 | -55.510101 | 2024-10-06 01:40:55 | METOP-C | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 2a7cfc60-9af3-301b-9180-b8719eb1265a | -16.6325 | -55.5201 | 2024-10-06 01:40:55 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| eddba574-5b2d-3d7a-9bd9-25fd7771cfbf | -16.634899 | -55.529999 | 2024-10-06 01:40:55 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 11028e8b-0687-3099-85a1-3ee50e31c11e | -16.6374 | -55.540001 | 2024-10-06 01:40:55 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 191a6040-925e-3407-ad57-f9ebbe96aed9 | -16.6399 | -55.5499 | 2024-10-06 01:40:55 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 3d4013ea-ec50-3994-8df8-6475c4d91d5b | -16.6423 | -55.559898 | 2024-10-06 01:40:55 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 0190080b-76c7-3915-a229-97278e706bd9 | -16.622801 | -55.522701 | 2024-10-06 01:40:56 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 4622b840-36a9-3e4f-b649-5439910079e2 | -16.6252 | -55.5326 | 2024-10-06 01:40:56 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 8f33ff87-9705-3793-a8ea-a3231f610790 | -16.627701 | -55.542599 | 2024-10-06 01:40:56 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 03fe6393-e140-3456-a002-14915eded6ee | -16.630199 | -55.552502 | 2024-10-06 01:40:56 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 2d982d2d-a04b-31c4-ae70-0697b224b8b6 | -16.632601 | -55.5625 | 2024-10-06 01:40:56 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| fba02aa2-b938-3578-8404-79c7550e26e5 | -16.677601 | -55.871601 | 2024-10-06 01:40:56 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 5df612e5-9e4d-337b-a945-45d1af1b4152 | -16.679899 | -55.8811 | 2024-10-06 01:40:56 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 38154942-27d5-3093-a878-1e25bf89441a | -16.682301 | -55.890701 | 2024-10-06 01:40:56 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| bad0143f-3ecf-31b0-b1ad-305e94483cd7 | -16.684601 | -55.9002 | 2024-10-06 01:40:56 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 1af0d0f1-a6d0-3b33-8ce1-e35575c8d9b4 | -16.686899 | -55.909698 | 2024-10-06 01:40:56 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 0e396056-4317-3bee-a1cb-0b07a3ca0290 | -16.6726 | -55.8932 | 2024-10-06 01:40:56 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 7694a0e1-6614-3174-8c83-bbee92495b5e | -16.8606 | -56.709702 | 2024-10-06 01:40:56 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 04211d0c-bcc3-3537-b3a5-f2689e5bff02 | -16.8627 | -56.7183 | 2024-10-06 01:40:56 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| ab4fce0a-917c-3c25-8401-b03c43245a18 | -16.864799 | -56.726898 | 2024-10-06 01:40:56 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| e0a433b7-e2c1-33c6-87cb-deea624eab5c | -16.653099 | -55.8983 | 2024-10-06 01:40:57 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| b75201ae-8d80-30d5-92cc-16fd6faa6913 | -16.8508 | -56.7122 | 2024-10-06 01:40:57 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 5575abc3-0e19-3a31-a863-7ee8d13d1268 | -16.8529 | -56.720798 | 2024-10-06 01:40:57 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| bd402dc0-1fed-352a-ad61-5e6d035c7e6f | -16.855 | -56.729401 | 2024-10-06 01:40:57 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 23ae656e-a32a-311f-8d0e-83dd6f6f9628 | -16.641001 | -55.8913 | 2024-10-06 01:40:57 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 6fd5f4a2-baf0-3502-9ac0-d8ffb95b1734 | -16.6434 | -55.900799 | 2024-10-06 01:40:57 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 0f041503-da36-30c1-b51c-64954eceabe8 | -16.845301 | -56.731899 | 2024-10-06 01:40:57 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| e9f21202-6082-3e09-9946-ee8e6d21880e | -16.6336 | -55.9034 | 2024-10-06 01:40:57 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 46e3388c-d016-38cd-95ec-348e86e36222 | -16.6215 | -55.8964 | 2024-10-06 01:40:57 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 00338bad-a027-335f-aea0-cad73aa4b160 | -16.623899 | -55.905899 | 2024-10-06 01:40:57 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| f99710a7-125c-3503-9e87-ff0e9da8b421 | -16.611799 | -55.898998 | 2024-10-06 01:40:57 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| f26a1de1-2289-3d90-a3fc-e252ef396aef | -16.614201 | -55.908501 | 2024-10-06 01:40:57 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 6117ff00-b76a-326e-aa3e-e09e1b2455c2 | -16.616501 | -55.917999 | 2024-10-06 01:40:57 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 949e6e75-7902-32c1-9135-f05250689fed | -16.601999 | -55.901501 | 2024-10-06 01:40:57 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 35205665-3237-32f4-9d3c-fb711a5fc539 | -16.604401 | -55.910999 | 2024-10-06 01:40:57 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 0e8b82bf-e888-3bd6-ae48-cbc850dc7233 | -16.606701 | -55.920502 | 2024-10-06 01:40:57 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 626fae31-f92b-38c3-8721-16f2e8776f79 | -16.563101 | -55.911701 | 2024-10-06 01:40:58 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 1b98be6d-a3ff-3fc7-8909-8479877d6486 | -16.5534 | -55.914299 | 2024-10-06 01:40:58 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| abbebe23-25e8-3a98-82ff-73c78b06f9fb | -16.5557 | -55.923801 | 2024-10-06 01:40:58 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 49e4b310-27d4-37f1-9021-699bdc09bff4 | -16.5581 | -55.9333 | 2024-10-06 01:40:58 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 5ce00c83-ffd0-303b-a8b8-0357cefb282a | -16.585699 | -56.046398 | 2024-10-06 01:40:58 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 8c53eb0f-d917-3eff-9980-bf31d3e91286 | -16.543699 | -55.916801 | 2024-10-06 01:40:58 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 24ce1457-a599-3523-9925-591cb37ae361 | -16.546 | -55.9263 | 2024-10-06 01:40:58 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| c78b5eec-e89b-335b-846e-7160e95b92f8 | -16.548401 | -55.935799 | 2024-10-06 01:40:58 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| b678e032-d545-3afe-b94b-ee9e05a3cc06 | -16.9296 | -57.694099 | 2024-10-06 01:40:59 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |


[Clique aqui para ver as próximas entradas](README29.md)
