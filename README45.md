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

## Dados Diários - Página 45

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8dfe54ef-0d3f-3e30-a449-d5f3b93e07a7 | -11.96783 | -51.88498 | 2024-09-30 04:32:00 | NOAA-20 | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9cc95063-b89d-35e2-b6c6-5f330049f8e4 | -11.34806 | -50.80482 | 2024-09-30 04:32:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2282c72c-9788-3647-865d-a13cda28ef9a | -13.2402 | -51.27194 | 2024-09-30 04:32:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 252b9732-5734-3737-8a42-19f00b6cdf94 | -13.21564 | -51.22871 | 2024-09-30 04:32:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a4e43f1e-0b91-378d-9ad0-adf4b804c0fd | -13.21501 | -51.2325 | 2024-09-30 04:32:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| be23aa9f-0d43-37b9-a73e-9cd0f678d4a8 | -13.2116 | -51.23192 | 2024-09-30 04:32:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| b2257bae-35a3-3b6f-9caf-aeb2ffa183fd | -13.12897 | -51.39008 | 2024-09-30 04:32:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 02311f0f-910a-310e-991c-fb5e42b78802 | -12.72533 | -51.95428 | 2024-09-30 04:32:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4cb6e558-2fee-359b-a843-e6124dad734e | -12.72464 | -51.95835 | 2024-09-30 04:32:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b931fcc7-5005-3c93-9970-a10f91ea30ea | -12.72385 | -51.94156 | 2024-09-30 04:32:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| efe29160-9da2-3fb2-a54f-3cca2d77f29b | -12.721 | -51.93692 | 2024-09-30 04:32:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 02f4dec2-88e4-3432-807a-276d04ba7592 | -12.71369 | -51.91626 | 2024-09-30 04:32:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9ad02a13-c8ed-3ba4-9878-a285055eed49 | -12.71314 | -51.91906 | 2024-09-30 04:32:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| fb87f91d-d8e5-3c5a-ba5b-c0f4ac35614a | -12.71303 | -51.92027 | 2024-09-30 04:32:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0b37d7b1-8605-37bb-95bc-70781475db2c | -12.70989 | -51.98099 | 2024-09-30 04:32:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 557b5156-3c70-3d77-ae36-f6548cc3c247 | -12.70636 | -51.98038 | 2024-09-30 04:32:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1ca0e391-28ef-37f7-914f-2e282fad020e | -12.703 | -51.98109 | 2024-09-30 04:32:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9a9a23bf-09bd-3e05-afe9-4c0b391bb4fd | -12.70282 | -51.97977 | 2024-09-30 04:32:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| cb41cbdf-777e-3d42-ab19-4a9a6e8c3605 | -12.57972 | -51.91453 | 2024-09-30 04:32:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 9aca25a0-2111-3e09-b782-e6e3e1668617 | -12.57619 | -51.91391 | 2024-09-30 04:32:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8dc8ca10-0948-3c0c-92b7-9a5c4eea8fda | -7.38332 | -52.02058 | 2024-09-30 04:32:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4bee5fca-f2c0-3e0e-8e79-cc60d4d6d81e | -9.10907 | -53.29008 | 2024-09-30 04:32:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c6bd5484-5207-399c-af66-97795318bf73 | -9.10694 | -53.29007 | 2024-09-30 04:32:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3f788979-6be9-3470-808f-d3b677f2d18e | -9.10508 | -53.28937 | 2024-09-30 04:32:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c2dcd893-39bc-3ba6-b928-e41b2d19f14c | -9.01439 | -52.13322 | 2024-09-30 04:32:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e4d62b26-4d4b-322c-8827-4ba8261acc3a | -9.01365 | -52.1376 | 2024-09-30 04:32:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 02f40d8d-0183-339e-96fa-70526c651c3e | -9.00994 | -52.13688 | 2024-09-30 04:32:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 660495a8-860c-3420-8e5b-d090668df06d | -8.93108 | -52.79055 | 2024-09-30 04:32:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 83be8f94-e105-3736-b954-29896a9714f2 | -8.9292 | -52.82544 | 2024-09-30 04:32:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bb95882f-8da3-3f04-948c-5c4ca623b4a0 | -8.92839 | -52.83026 | 2024-09-30 04:32:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e698fd0c-3f46-3dd8-9622-ce51409fc63a | -8.92804 | -52.78492 | 2024-09-30 04:32:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 6691a078-3ee5-3bda-b44e-2d15078e2c10 | -8.9272 | -52.78988 | 2024-09-30 04:32:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| df33b93a-9091-3e65-8d3d-6721b461ae55 | -8.89686 | -53.04145 | 2024-09-30 04:32:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cbfa2c39-470c-3535-82ee-0ad7b38eb7c1 | -8.89113 | -53.00343 | 2024-09-30 04:32:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 72c080d5-f773-3a7b-a6b3-5ce84f5cfac9 | -8.88636 | -53.00776 | 2024-09-30 04:32:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f3a43a8a-1f00-300a-8475-af759b2e0fa3 | -8.88549 | -53.01286 | 2024-09-30 04:32:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 47bc9c6c-8bf3-37d0-bb61-22e38b1db83a | -8.88242 | -53.0071 | 2024-09-30 04:32:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0e9821b4-c21d-377b-9bde-e4d8bd5a847f | -8.88155 | -53.01225 | 2024-09-30 04:32:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d20e2af3-0275-3422-a4ae-f7d20f56893b | -8.87722 | -53.03774 | 2024-09-30 04:32:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 503e5794-0d48-370f-a80d-e8f2bda028fc | -8.87673 | -53.01677 | 2024-09-30 04:32:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4833945d-dd18-3197-a024-ca8d0976c424 | -8.87414 | -53.03203 | 2024-09-30 04:32:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 82a568c8-7db4-35a3-8f82-0438fa901d02 | -8.87329 | -53.03703 | 2024-09-30 04:32:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| fa7daec9-a4b4-3d02-afb4-9d533c92989e | -10.23339 | -52.73231 | 2024-09-30 04:32:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 43122e7a-ac72-397e-924e-0ea57cb9471f | -10.2326 | -52.73701 | 2024-09-30 04:32:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c3791d6f-a196-3bf4-a8b3-4b4840a06f4d | -10.2304 | -52.72696 | 2024-09-30 04:32:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7ad25887-cb8a-3244-a0a7-67d72a20759a | -10.22961 | -52.73164 | 2024-09-30 04:32:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b0d8098c-f5b2-3a5f-9f16-8e47b170007e | -10.22581 | -52.731 | 2024-09-30 04:32:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3b528165-55b6-3dcf-82f8-614c404b58fd | -10.2244 | -52.71635 | 2024-09-30 04:32:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 078132ef-5071-350b-a4b7-5ca56142e875 | -10.22361 | -52.72102 | 2024-09-30 04:32:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 94e636d5-9a93-3cc2-a246-0ef3ac385389 | -10.22281 | -52.72569 | 2024-09-30 04:32:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ce663720-f499-314a-bd86-a1849053db22 | -10.22202 | -52.73037 | 2024-09-30 04:32:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 57612e29-40ce-356d-8387-0da21023f033 | -10.22062 | -52.7157 | 2024-09-30 04:32:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| cceb3dfa-c429-3ca1-ae84-f077d7c673f9 | -10.21982 | -52.72037 | 2024-09-30 04:32:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1eed97b1-577c-3418-84dc-a8ceba260475 | -10.21902 | -52.72504 | 2024-09-30 04:32:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 16dfc235-539d-3326-9c1f-8e24da7e3349 | -10.04948 | -53.48504 | 2024-09-30 04:32:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e90b5b8d-6da4-3e8c-a021-9394ba37fd96 | -10.0278 | -53.4199 | 2024-09-30 04:32:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7b2b75fb-45fb-3deb-861e-412f42c843b6 | -10.02692 | -53.42505 | 2024-09-30 04:32:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4b1c8181-6627-3c77-98a9-664b5bdc253f | -10.02604 | -53.4302 | 2024-09-30 04:32:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a9dbf9c2-fefd-3fbf-b539-1e34a861e6a0 | -10.02384 | -53.41916 | 2024-09-30 04:32:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| d8af789e-e721-3ddb-8040-35b72aba8292 | -10.02296 | -53.42431 | 2024-09-30 04:32:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 14.2 |
| 8fca03e7-2512-30cc-ade6-1bf89d262399 | -10.02208 | -53.42948 | 2024-09-30 04:32:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 14.2 |
| 00c330d9-8048-3697-83cb-3081c0511c87 | -10.0212 | -53.43464 | 2024-09-30 04:32:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| bbf3e573-124f-3d05-87e8-0963a2b77626 | -10.01988 | -53.41842 | 2024-09-30 04:32:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 6566a7ce-baf7-3673-987e-23758c9d26d9 | -10.019 | -53.42357 | 2024-09-30 04:32:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 14.2 |
| ba00be24-9605-3e18-a537-55d1751513e1 | -10.01812 | -53.42873 | 2024-09-30 04:32:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 14.2 |
| 8d33b969-acdb-32db-92be-7a6c77339609 | -10.01724 | -53.4339 | 2024-09-30 04:32:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| acf4639e-822a-320e-9247-0650b3a0dfa0 | -10.01592 | -53.4177 | 2024-09-30 04:32:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 02fb9431-6c03-3b9c-847c-428e3b44dda5 | -10.01505 | -53.42282 | 2024-09-30 04:32:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4c1ff6df-625f-3149-b572-9d9d2b38f826 | -10.01416 | -53.42797 | 2024-09-30 04:32:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 97d46db8-7455-3f3c-a50b-53df842da29f | -9.90416 | -52.21912 | 2024-09-30 04:32:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9035e995-5dae-35e1-8991-9a02e30ebdd9 | -9.90269 | -52.2051 | 2024-09-30 04:32:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4f87e9b5-e7ac-33ad-90a3-db2b9f7afb26 | -9.90195 | -52.20956 | 2024-09-30 04:32:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 3f27bc35-8617-3948-83fc-ebfaeb085d3d | -9.9012 | -52.21402 | 2024-09-30 04:32:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 6889305e-9fa7-3dab-bb04-e79b7b2932c1 | -9.899 | -52.20445 | 2024-09-30 04:32:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d9f9aeff-7adb-3e42-84e4-24d2fa808b41 | -11.44961 | -53.83292 | 2024-09-30 04:32:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| a2827f07-01ec-3c02-9653-8b9935096ac6 | -11.09128 | -52.49987 | 2024-09-30 04:32:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e5ec38b0-6bc9-3ac3-a35b-44a4f95bb0ad | -11.08996 | -52.49755 | 2024-09-30 04:32:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 95b929e7-93ce-3cb5-9a06-d357016f0a95 | -11.08919 | -52.50202 | 2024-09-30 04:32:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 418e529c-73d8-34e8-bb30-332c93d86422 | -11.08833 | -52.49471 | 2024-09-30 04:32:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5ff884fb-cc8a-3f3d-982a-cf2f4582b965 | -11.08759 | -52.49918 | 2024-09-30 04:32:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7000f6d6-e89c-3d30-b2bc-dc4df2dc3b1a | -11.08703 | -52.49242 | 2024-09-30 04:32:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b7219632-e166-3a7e-b3c6-12bdced9ccf7 | -11.08684 | -52.50367 | 2024-09-30 04:32:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 174683b9-7a04-33ae-87d3-148f97bc6a0d | -11.08627 | -52.49686 | 2024-09-30 04:32:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 026a306b-e41b-3168-a5df-6a2351b6839e | -11.0861 | -52.50814 | 2024-09-30 04:32:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f5123bf9-8a37-35b7-9bbc-1c54a950ecf5 | -11.08549 | -52.50134 | 2024-09-30 04:32:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4b7be29f-8966-3030-9a43-870277252e03 | -11.08538 | -52.48959 | 2024-09-30 04:32:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0300ca70-5265-3c4d-a006-27029f9ca371 | -11.08472 | -52.50582 | 2024-09-30 04:32:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fc311606-3d68-348f-b05d-d9dcab28adb0 | -11.08464 | -52.49403 | 2024-09-30 04:32:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d61624f7-d156-33c2-8b41-e83ed06f92c4 | -11.08389 | -52.4985 | 2024-09-30 04:32:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4aa1aaf5-bf84-3a9a-9798-6f2d7b2fb812 | -11.08315 | -52.50299 | 2024-09-30 04:32:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 58002c99-cc1e-3c7f-9b00-ed782fb5bc3f | -11.0824 | -52.50747 | 2024-09-30 04:32:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fc01b238-ac26-3617-8275-aee11cf43458 | -11.08169 | -52.4889 | 2024-09-30 04:32:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| eb4bcc09-8762-32f9-8877-1dc7082f28b9 | -11.08166 | -52.51193 | 2024-09-30 04:32:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b7741059-0774-3b69-8e7e-a8ce5c6dc694 | -11.0787 | -52.50679 | 2024-09-30 04:32:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f504f4fc-a329-3b61-9252-d83eba921ac3 | -11.07796 | -52.51124 | 2024-09-30 04:32:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a236aa4d-b58b-3220-b8ff-4d9ca07457c8 | -11.07427 | -52.51057 | 2024-09-30 04:32:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b4f6162e-98c0-3572-80f2-d0592d9f4f13 | -11.07057 | -52.50991 | 2024-09-30 04:32:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b9b25084-300d-3710-94c6-69ef7609debd | -11.06982 | -52.51439 | 2024-09-30 04:32:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ef58e206-92c6-3004-95f5-a716223611a2 | -11.06686 | -52.50929 | 2024-09-30 04:32:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2db3ba55-3fba-3fd5-a61e-d0010a431205 | -11.06611 | -52.51377 | 2024-09-30 04:32:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |


[Clique aqui para ver as próximas entradas](README46.md)
