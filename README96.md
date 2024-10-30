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

## Dados Diários - Página 96

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a456f2de-3bac-3033-8ab3-316b3fe5507f | -3.5631 | -47.3847 | 2024-10-30 05:15:26 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 39.0 |
| 99c8b5db-3f8e-342a-aa08-23cc1efae2ba | -3.5632 | -47.3629 | 2024-10-30 05:15:26 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 28.0 |
| cc5e325e-2eda-3de3-a687-036a97837246 | -3.9486 | -48.1291 | 2024-10-30 05:15:28 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 34.1 |
| 7fc71bd3-a716-31ea-9935-5883a1a816d9 | -4.0681 | -50.024 | 2024-10-30 05:15:29 | GOES-16 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 46.7 |
| f40b8d3f-661b-3bde-ba21-2f070e29359e | -4.0682 | -50.0029 | 2024-10-30 05:15:29 | GOES-16 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 45.0 |
| cec837b9-0672-35af-9eda-06c164b939a7 | -4.2563 | -43.4368 | 2024-10-30 05:15:30 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 59.4 |
| da18d2da-3246-3cf6-9d6a-f332e0024f21 | -4.2749 | -43.4357 | 2024-10-30 05:15:30 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 70.4 |
| 52b831d1-f742-352e-ac66-508b9bdfcd56 | -4.2496 | -50.6677 | 2024-10-30 05:15:30 | GOES-16 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 46.8 |
| feac91bd-b911-334a-b0e9-5ab38ee1ca8f | -4.2681 | -50.6669 | 2024-10-30 05:15:30 | GOES-16 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 77.3 |
| 7f6a4d14-c71d-3764-92a3-9fced4e88c85 | -10.3434 | -49.6536 | 2024-10-30 05:16:05 | GOES-16 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 91.7 |
| f1231a84-c0fb-3f3c-8214-7807482b70ab | -10.3437 | -49.6321 | 2024-10-30 05:16:05 | GOES-16 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 52.6 |
| d84ea81d-3ace-36fd-bfcd-3361cd6f85ce | 1.7483 | -55.8428 | 2024-10-30 05:24:56 | GOES-16 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 52.4 |
| 28f760f6-347f-3ca9-9357-897fbf906089 | 3.54988 | -51.27361 | 2024-10-30 05:25:00 | AQUA_M-M | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 12.9 |
| 8d77e677-c938-377b-a2b7-53c92b3e6690 | -2.833 | -49.2413 | 2024-10-30 05:25:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 49.8 |
| ef073aa8-dd2b-34f3-b169-f7f077f0734f | -3.0734 | -54.167 | 2024-10-30 05:25:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 38.7 |
| f4b4e000-7070-3a32-bc71-c721f613b40d | -3.0913 | -54.287 | 2024-10-30 05:25:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 39.9 |
| dce0d8fc-f4c9-38f5-bb34-a6a984f7015b | -3.1097 | -54.2865 | 2024-10-30 05:25:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 43.2 |
| f990d8f4-cd4f-3485-be39-d2557549e44c | -3.1098 | -54.2665 | 2024-10-30 05:25:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 41.9 |
| 8749bb25-5944-3a34-a550-a3777f9e201d | -3.1281 | -54.266 | 2024-10-30 05:25:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 42.5 |
| 5fd3a44b-db16-35ca-b9f5-89fa919f3eb6 | -3.1786 | -50.6016 | 2024-10-30 05:25:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 38.5 |
| ba42b914-517f-37c0-9b8e-c91ed6dba713 | -3.1787 | -50.5807 | 2024-10-30 05:25:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 33.7 |
| 3700914d-7b16-3a25-8cc4-31254b0e36ca | -3.2534 | -50.3689 | 2024-10-30 05:25:25 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 29.2 |
| 84d8e586-57aa-3a6f-b2f5-789d0fb543d8 | -3.2535 | -50.3479 | 2024-10-30 05:25:25 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 89.8 |
| 0836a263-8a85-3f3f-bcb1-5daa8f6a8d54 | -3.2535 | -50.3269 | 2024-10-30 05:25:25 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 28.4 |
| 124a86d7-6c5d-3ff7-9b2b-e10e74cb5bc7 | -3.2718 | -50.3683 | 2024-10-30 05:25:25 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 33.6 |
| 5cb0a2c4-a37f-304f-b2e0-f9ea46cdf11f | -3.2719 | -50.3473 | 2024-10-30 05:25:25 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 137.0 |
| c026de46-77e9-3dc3-8e9e-fe2f85737a35 | -3.272 | -50.3263 | 2024-10-30 05:25:25 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 37.7 |
| d82fbd14-a9bb-39dd-8af5-dce5716d9ef4 | -3.5631 | -47.3847 | 2024-10-30 05:25:26 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 40.6 |
| 7686a9ca-7486-39d9-932f-659e582223e7 | -3.5817 | -47.384 | 2024-10-30 05:25:26 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 32.6 |
| 36600118-3a73-3c63-b926-017d89bdc8fe | -3.9486 | -48.1291 | 2024-10-30 05:25:28 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 42.3 |
| 793acde0-331a-32a2-afb9-27c3203a056c | -4.2749 | -43.4357 | 2024-10-30 05:25:30 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 77.0 |
| a9d7d1e6-c7c2-347c-a47b-96ab001c27fc | -4.2681 | -50.6669 | 2024-10-30 05:25:30 | GOES-16 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 83.6 |
| 00bb6587-5f55-3873-be1a-cb5c41eb2848 | -10.3434 | -49.6536 | 2024-10-30 05:26:05 | GOES-16 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 91.7 |
| 9b01dbef-2428-3ae0-acb5-f7a5af1601a5 | -10.3437 | -49.6321 | 2024-10-30 05:26:05 | GOES-16 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 57.5 |
| 2c2a0c6d-5b51-3721-81e0-90e4f58cacd2 | -1.58453 | -53.10132 | 2024-10-30 05:27:00 | AQUA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 14.5 |
| c86d9514-cef7-361e-bffe-d1499b41a779 | -1.46046 | -52.30456 | 2024-10-30 05:27:00 | AQUA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| efbbc811-385f-3bac-823f-bf4a4e0c732e | -1.42706 | -49.21035 | 2024-10-30 05:27:00 | AQUA_M-M | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| c3e879ae-7b84-3264-b630-7ce3de9f8081 | -6.41919 | -42.09007 | 2024-10-30 05:27:00 | AQUA_M-M | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 16.4 |
| 7a5e560c-84b5-3508-ab65-c595d53e02d4 | -6.17702 | -43.18044 | 2024-10-30 05:27:00 | AQUA_M-M | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 14.1 |
| 5089ccd0-6d04-33d1-a0cc-9c9198ef3b1c | -4.93349 | -43.18913 | 2024-10-30 05:27:00 | AQUA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| dbf9b2cb-15ec-351b-aea2-0c61c4d1a14a | -4.27499 | -43.43903 | 2024-10-30 05:27:00 | AQUA_M-M | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 76.5 |
| 67526138-5cba-3cd9-bd12-c91bcf518887 | -4.27314 | -43.45153 | 2024-10-30 05:27:00 | AQUA_M-M | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 32.8 |
| 8ee5ca36-c56d-31a7-8850-4cdb98c4b58a | -4.27116 | -43.4323 | 2024-10-30 05:27:00 | AQUA_M-M | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 31.0 |
| c576cc73-0ffe-3491-bead-e352ea539b73 | -4.26939 | -43.44496 | 2024-10-30 05:27:00 | AQUA_M-M | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 72.7 |
| 9873fa9f-fbf5-310c-b9bb-c95000515e9b | -4.2645 | -43.43758 | 2024-10-30 05:27:00 | AQUA_M-M | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 48.1 |
| 6e9ddc70-b666-3122-af67-c615eca3371f | -4.26267 | -43.4501 | 2024-10-30 05:27:00 | AQUA_M-M | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 18.9 |
| 6ebf16ec-4df3-398a-a4c7-ae882b8d8568 | -3.93592 | -41.48663 | 2024-10-30 05:27:00 | AQUA_M-M | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 18.0 |
| 2caf550a-53d9-30f6-a61e-5b965868ce31 | -3.54035 | -43.61895 | 2024-10-30 05:27:00 | AQUA_M-M | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 19.0 |
| 6263ef37-b0c4-3b96-b730-7ad6ba379383 | 1.74685 | -55.8218 | 2024-10-30 05:27:00 | AQUA_M-M | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 34.9 |
| 2d897512-e303-3f5a-bf0b-397ad2c1be10 | 1.74106 | -55.82767 | 2024-10-30 05:27:00 | AQUA_M-M | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 38.8 |
| 05d3ece5-4f71-3f11-8041-1ede3869ea58 | 1.67387 | -55.83714 | 2024-10-30 05:27:00 | AQUA_M-M | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 38.4 |
| 75e1b9d9-6917-31ac-aa5c-984199d9d2a1 | -5.97932 | -45.36642 | 2024-10-30 05:27:00 | AQUA_M-M | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 55.6 |
| 06224368-f61d-38da-8af3-c12aed8e259f | -5.97785 | -45.37658 | 2024-10-30 05:27:00 | AQUA_M-M | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| abe73dea-fb3a-341b-b131-e6467c2d49cb | -5.96988 | -45.36498 | 2024-10-30 05:27:00 | AQUA_M-M | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| d000258c-b95d-359d-8db1-cd51dfa9f82c | -4.91184 | -48.638 | 2024-10-30 05:27:00 | AQUA_M-M | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 672cf118-14d9-39d1-888b-0be223eea9cf | -4.59909 | -48.07151 | 2024-10-30 05:27:00 | AQUA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| f4e82acb-4499-3b74-a464-f524ec0689ae | -4.56649 | -50.40694 | 2024-10-30 05:27:00 | AQUA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 7c84554a-9d89-3120-996b-09a5e9f893fe | -4.5009 | -46.45397 | 2024-10-30 05:27:00 | AQUA_M-M | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 5.5 |
| a167c667-3ec2-39f3-9173-461f627e0896 | -4.35691 | -48.15138 | 2024-10-30 05:27:00 | AQUA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 75f56ff6-c824-31bf-a6b3-f1e480c2a29d | -4.27223 | -50.65823 | 2024-10-30 05:27:00 | AQUA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 12.4 |
| 2723a4df-b79f-3c54-a5bd-309fe2728ebf | -4.27046 | -50.66983 | 2024-10-30 05:27:00 | AQUA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 68.9 |
| 0691b356-e28c-35a2-9edd-0daea595d332 | -4.26213 | -50.65678 | 2024-10-30 05:27:00 | AQUA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 20.8 |
| 4fb9f033-f5b2-3249-ab3c-befed3f041e2 | -4.26034 | -50.66842 | 2024-10-30 05:27:00 | AQUA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 61.4 |
| faf0acbe-b126-3636-8023-7775592ca0f5 | -4.1383 | -48.13433 | 2024-10-30 05:27:00 | AQUA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 4a5a151f-9a01-3d14-b5b8-519003f35501 | -4.10867 | -48.5105 | 2024-10-30 05:27:00 | AQUA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 8177bf8e-36db-3098-b271-6539bb273b25 | -4.07456 | -50.00524 | 2024-10-30 05:27:00 | AQUA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 34.5 |
| fb6a1cc3-13d1-3547-8b8b-f9149a1a0e62 | -4.07291 | -50.01597 | 2024-10-30 05:27:00 | AQUA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 46.4 |
| d16acfb0-6761-384d-a9de-9991d9603679 | -4.06962 | -50.03744 | 2024-10-30 05:27:00 | AQUA_M-M | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| f47441d2-a13d-3b20-bb75-6cc00273eaf6 | -4.06321 | -50.01453 | 2024-10-30 05:27:00 | AQUA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 7d654526-b58d-32bf-93f1-3ce2e71e8d07 | -4.04239 | -50.55168 | 2024-10-30 05:27:00 | AQUA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 80a8fb1c-6706-37fa-942f-6be95cc4c712 | -4.04104 | -50.55751 | 2024-10-30 05:27:00 | AQUA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| c3cdf187-9535-3af2-9815-7c6d271db544 | -3.95534 | -48.1227 | 2024-10-30 05:27:00 | AQUA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 23.6 |
| ac46abf3-70b6-3781-8993-ff62d7d9d136 | -3.95397 | -48.1317 | 2024-10-30 05:27:00 | AQUA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 34.6 |
| cecb928e-fc9c-3075-bebc-d4be7f63e9b9 | -3.94027 | -48.34246 | 2024-10-30 05:27:00 | AQUA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 6524f2b4-b7ca-3230-b907-7ab51179fe97 | -3.93889 | -48.35156 | 2024-10-30 05:27:00 | AQUA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| b61040cf-0263-3d0c-aa34-620ba21b6af9 | -3.9313 | -48.34109 | 2024-10-30 05:27:00 | AQUA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| d048531c-8b44-3821-bafa-0eaedbf04fa4 | -3.909 | -48.36845 | 2024-10-30 05:27:00 | AQUA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 35a9b6e5-8998-3f52-884a-f46141349631 | -3.9021 | -49.07894 | 2024-10-30 05:27:00 | AQUA_M-M | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 1d3d562b-7115-38e8-8890-a69c181027b5 | -3.89552 | -51.91238 | 2024-10-30 05:27:00 | AQUA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 22.7 |
| 4d637d49-8726-3fc3-9003-135c98ba146e | -3.8049 | -51.16131 | 2024-10-30 05:27:00 | AQUA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 13.7 |
| a013c76d-697a-35d7-b3f1-e10a79eba630 | -3.661 | -50.16315 | 2024-10-30 05:27:00 | AQUA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 7a4c2f71-40c8-3369-bd1a-f84c6488e896 | -3.65116 | -50.16166 | 2024-10-30 05:27:00 | AQUA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 40226b65-a9b1-3019-82d5-ba6a3c4877a5 | -3.62002 | -47.28963 | 2024-10-30 05:27:00 | AQUA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 06d1530c-6a33-38f2-b54a-30811bdde370 | -3.6187 | -47.29842 | 2024-10-30 05:27:00 | AQUA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| bf38d6be-8d48-3fa5-a019-0e39780b5a47 | -3.61474 | -47.24733 | 2024-10-30 05:27:00 | AQUA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 00d3b6ae-643b-35b2-b03b-65bd9fc77ee7 | -3.57728 | -47.37671 | 2024-10-30 05:27:00 | AQUA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 51.3 |
| 0acea1fc-f837-3bcc-8049-4203747fb372 | -3.57596 | -47.38552 | 2024-10-30 05:27:00 | AQUA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 69c158f4-e2f4-39a3-9f8d-1f65ecef0644 | -3.56998 | -50.03048 | 2024-10-30 05:27:00 | AQUA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| e0c53069-14d6-307b-8a5f-69b05b0852c7 | -3.56844 | -47.37542 | 2024-10-30 05:27:00 | AQUA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 40.0 |
| 45071850-22cc-36a4-bbcc-f83173cc8adf | -3.56712 | -47.38422 | 2024-10-30 05:27:00 | AQUA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 15.3 |
| 191b68e9-2795-3807-9c4c-c6e96a68debb | -3.56623 | -50.03543 | 2024-10-30 05:27:00 | AQUA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| bf114327-0593-3424-a078-3f87eaeb0815 | -3.52873 | -49.22864 | 2024-10-30 05:27:00 | AQUA_M-M | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 3ec20a30-496d-3512-a447-20cc67b7d2f1 | -3.39411 | -49.75596 | 2024-10-30 05:27:00 | AQUA_M-M | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 25d841ea-f62a-3a42-80c6-6b90de2602e4 | -3.3781 | -49.54061 | 2024-10-30 05:27:00 | AQUA_M-M | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| d5e068f9-cb37-3a26-aaf6-ef9fd97e0ad0 | -3.36567 | -50.15659 | 2024-10-30 05:27:00 | AQUA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| d8ca1bdc-c260-3a7a-b124-cebb48848d0c | -3.35987 | -50.259 | 2024-10-30 05:27:00 | AQUA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 5f02dfb2-e01d-35a5-a7fa-234a01bcb521 | -3.27391 | -50.34538 | 2024-10-30 05:27:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 85.1 |
| df8b8a0f-d40c-305b-b13e-f174dd7b0489 | -3.27214 | -50.35688 | 2024-10-30 05:27:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 20.5 |
| c0f66625-5388-3ea3-8dad-ffa78004216c | -3.26389 | -50.3439 | 2024-10-30 05:27:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 163.0 |
| fae35794-57a3-3cdd-8bef-dcdd455fe4df | -3.2621 | -50.3554 | 2024-10-30 05:27:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 40.4 |


[Clique aqui para ver as próximas entradas](README97.md)
