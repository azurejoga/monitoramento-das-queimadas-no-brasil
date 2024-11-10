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

## Dados Diários - Página 108

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6475937e-3a6e-370f-986e-92045fc2b10e | -3.07895 | -49.09722 | 2024-11-10 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a8c4bf50-1a31-30bb-8ba8-465e7e446bee | -8.38789 | -44.11447 | 2024-11-10 04:38:00 | NPP-375D | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8c32350c-2330-300f-8544-01f87a141b63 | -3.98757 | -46.42238 | 2024-11-10 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 50d18426-096a-3fce-a5a3-21d9caed07f5 | -1.75233 | -55.03602 | 2024-11-10 04:38:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 196a5ab8-7406-3fc0-a89e-0f795b34beb6 | -4.21323 | -48.68404 | 2024-11-10 04:38:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ad5ca29f-a8fd-339e-abc7-141a3abbf67e | -2.65677 | -49.90689 | 2024-11-10 04:38:00 | NPP-375D | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 85b6d1a0-ed2c-30c8-8d99-aec56af15f40 | -10.94998 | -40.81876 | 2024-11-10 04:38:00 | NPP-375D | JACOBINA | BAHIA | Brasil | 2917508 | 29 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 0d281442-fdd4-36af-84cd-10e0cc52b20a | -8.38707 | -44.15015 | 2024-11-10 04:38:00 | NPP-375D | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 2fc82883-aa65-34e5-a6b8-ba7718d9ed78 | -3.51069 | -54.03119 | 2024-11-10 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d5358515-430a-3a25-b033-85713b7b3850 | -3.16471 | -54.48622 | 2024-11-10 04:38:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c5fa969c-cb8b-35c4-ab0d-b91eb6c39bb5 | -2.45106 | -54.04726 | 2024-11-10 04:38:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 205f28cc-2ebe-3e84-a42f-9a45f1a2a1a5 | -3.25062 | -48.7591 | 2024-11-10 04:38:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| e1e80228-ff4e-3ff8-bad4-97d945f1ce24 | -2.64776 | -49.89812 | 2024-11-10 04:38:00 | NPP-375D | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8d5895bb-30f4-39c2-b5c3-55b30b55b27b | -3.54349 | -49.98284 | 2024-11-10 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8e370697-783d-366d-8901-11151b4eb85a | -2.86656 | -47.91026 | 2024-11-10 04:38:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 71f8cbb9-65c7-3843-a1a3-bba156401b25 | -3.96208 | -49.01252 | 2024-11-10 04:38:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 532b8761-159f-3643-9f64-7f5efb31ec91 | -3.98683 | -46.42321 | 2024-11-10 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 237503ff-2022-3c00-bfbf-5f6853672a88 | -2.32075 | -54.3962 | 2024-11-10 04:38:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2b6b6b4b-5280-3570-afa9-a943a7f42661 | -4.1951 | -48.54299 | 2024-11-10 04:38:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 101e14d3-0072-3466-986f-c3dd1a6bd626 | -8.40444 | -44.14882 | 2024-11-10 04:38:00 | NPP-375D | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e8ab8915-3cdf-3bfc-9b3a-03def116ab51 | -3.5139 | -44.03843 | 2024-11-10 04:38:00 | NPP-375D | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 8.5 |
| e1f892fb-3a3b-34fe-bc2e-d09960ff44d3 | -4.77293 | -48.91359 | 2024-11-10 04:38:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5cc6127a-f410-328e-886f-6d81ef288d31 | -2.2057 | -50.28565 | 2024-11-10 04:38:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 9df8e221-1d4d-3776-8d15-0873e872f2ec | -2.22743 | -50.5265 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 215739bb-ad3d-3c05-931e-58e061a711e5 | -1.44392 | -55.50774 | 2024-11-10 04:38:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| dcec7d7a-a303-393b-862b-e3f2dbd168d9 | -3.57949 | -50.27982 | 2024-11-10 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| df66f165-2355-390b-b921-d63e632a9aff | -3.03832 | -50.32264 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d45affd8-c537-37f2-bc2c-0700c7b3bc56 | -1.76421 | -53.75722 | 2024-11-10 04:38:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 244faff4-1f6f-3cfe-a706-46741a5e16a5 | -3.43596 | -49.99842 | 2024-11-10 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c95a9d26-824f-3d90-8964-8c90a61330db | -3.9476 | -48.15313 | 2024-11-10 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 17.8 |
| 8f30e8a9-55ca-3b03-8175-cdff4c41e5db | -2.72376 | -49.28705 | 2024-11-10 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0a231ab2-2c20-3509-a7a1-f18fb55b4370 | -3.35325 | -50.12195 | 2024-11-10 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 4263067d-4551-3eb7-8018-a72d9c8b440d | -2.86089 | -50.31805 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| bda5df48-1193-3cd6-ba00-22032b5c4ea5 | -2.96793 | -48.01815 | 2024-11-10 04:38:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 59b9d928-d46f-3366-b06e-79b80edf9e2d | -4.33001 | -48.60718 | 2024-11-10 04:38:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5a5969ed-1d23-30ed-a4c2-0790f201e710 | -2.91905 | -49.35735 | 2024-11-10 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d52fb085-394c-3532-8d71-bc4e4de82f2b | -2.73261 | -51.74178 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 42a2487c-800a-33c4-b1fe-1ea038f52aa4 | -3.05899 | -51.37915 | 2024-11-10 04:38:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a6b61d7d-e935-38f6-9dba-04d6d936c803 | -2.35634 | -53.75021 | 2024-11-10 04:38:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7ad9cbfa-f574-354f-84de-f39b08c8ed52 | -5.1682 | -50.67966 | 2024-11-10 04:38:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 752af4e0-7d91-3575-be5d-6937b7ef2ae6 | -2.66129 | -49.90025 | 2024-11-10 04:38:00 | NPP-375D | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4ff02bae-8fb8-312a-9297-6b6404e4ad7f | -3.69403 | -51.28721 | 2024-11-10 04:38:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| ec77a423-f1d2-3dc8-a21e-a4c812ad26ca | -3.99166 | -46.41902 | 2024-11-10 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d9c5ef33-3fac-31c4-a011-e2caa33f71b7 | -4.416 | -45.7033 | 2024-11-10 04:38:00 | NPP-375D | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e4a461f8-985b-3928-9d18-d70414ca2d33 | -2.44 | -53.66438 | 2024-11-10 04:38:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 76abab4d-23a9-3698-b35e-5ceb7e18a644 | -4.05712 | -49.28966 | 2024-11-10 04:38:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| fd19936d-92c5-3a10-91a8-0a2a2a69aa2f | -2.15039 | -50.69752 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e10e9fa1-e09a-3967-80df-fe954c60bcdc | -2.64389 | -49.83509 | 2024-11-10 04:38:00 | NPP-375D | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| f937e0e0-c903-3433-83a4-df01df9bc7a7 | -3.07645 | -50.56758 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e7a2ec16-b044-3294-b60e-12a9f35365bf | -1.7516 | -55.04065 | 2024-11-10 04:38:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 79e7727b-b0ac-3fd1-8b5d-d6860b665aba | -3.08605 | -49.56253 | 2024-11-10 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c3e83e1d-3050-3120-9f60-6e63109f9f33 | -2.89993 | -50.7052 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 17bacdb2-43e6-34dc-81e7-c26637eca2f6 | -2.68093 | -49.27678 | 2024-11-10 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bab1d096-fded-348a-83cb-c1ce6a1f16d9 | -2.87257 | -51.47946 | 2024-11-10 04:38:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 29.0 |
| 02894301-3378-3f62-a82a-da1a3d640ba0 | -3.05937 | -48.04004 | 2024-11-10 04:38:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b0817c6f-5cda-367c-aea5-e4b90fa5d65a | -3.77409 | -49.79694 | 2024-11-10 04:38:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4fa8158d-7c05-3656-a1de-b074130a45f1 | -2.87075 | -50.41024 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 0437477e-38bc-364a-9bef-ba686ee776bf | -4.05903 | -48.30922 | 2024-11-10 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 31e4125e-49e1-3b5d-976c-b25c9fb93ccb | -2.4671 | -50.4016 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| ba77451a-a38a-3f05-9d21-21fc87c7b38f | -2.64757 | -51.87815 | 2024-11-10 04:38:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 44be0b31-8ff5-36df-97da-3a150cdbdab0 | -2.58636 | -48.20712 | 2024-11-10 04:38:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5847c17b-ff9c-350d-ac6e-00897237b383 | -3.45876 | -50.35758 | 2024-11-10 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6465f44e-92c3-356c-9ac6-f6f73e864c5c | -2.76781 | -49.3548 | 2024-11-10 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| a2507bac-2698-3c0c-9bb7-0d965417001a | -3.14124 | -48.57278 | 2024-11-10 04:38:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 574cc8e6-4eb6-303f-b9d0-4cfa77bb93ee | -5.14135 | -47.70184 | 2024-11-10 04:38:00 | NPP-375D | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4fd23855-d968-331b-9679-f853801ab666 | -3.95672 | -46.99123 | 2024-11-10 04:38:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 64a277fb-feec-3950-999e-7c373eaddc96 | -2.59048 | -48.28901 | 2024-11-10 04:38:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 238017c0-2ffe-39db-b076-40535be63531 | -3.14449 | -52.97459 | 2024-11-10 04:38:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b6e3e21c-11cb-315f-aa84-c0263632676c | -4.85833 | -43.96951 | 2024-11-10 04:38:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| e9c3fbe2-64e2-3192-ad0d-4c6d3ac88d09 | -8.40613 | -44.13718 | 2024-11-10 04:38:00 | NPP-375D | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 1a3d0878-9e1a-38de-a11c-07ac12c51c53 | -3.23342 | -50.25943 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 204d6727-9031-3196-ad3b-d4f9f9c1841f | -3.19148 | -54.32391 | 2024-11-10 04:38:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1cebf856-c952-37e0-84d8-8563d4967317 | -3.56484 | -53.9482 | 2024-11-10 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| fb0a661f-e621-393f-bc87-c01354fc64c7 | -4.09046 | -49.09977 | 2024-11-10 04:38:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ac01e078-2cfe-3612-8fe2-88f8ca04ad1c | -2.08531 | -54.68363 | 2024-11-10 04:38:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7940b37d-cf24-36f3-8a61-b9f2b339c240 | -2.19824 | -50.22434 | 2024-11-10 04:38:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 46cef465-0b3e-31aa-883a-c2d14544b291 | -3.0151 | -53.2605 | 2024-11-10 04:38:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 020ca41a-0ab0-3a03-b9c8-1633687c96c3 | -4.32758 | -44.65218 | 2024-11-10 04:38:00 | NPP-375D | SÃO LUÍS GONZAGA DO MARANHÃO | MARANHÃO | Brasil | 2111409 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 30f9e188-6080-3931-a397-dd80f9565b93 | -3.97321 | -48.18562 | 2024-11-10 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 175d3398-9d96-3f3b-83f8-b95e71c14ebb | -2.17358 | -50.46403 | 2024-11-10 04:38:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d1df8f21-1252-3a13-98ce-133071712805 | -3.53344 | -50.32843 | 2024-11-10 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 28b97e19-7c55-372a-bf83-f8de04e96b7d | -4.37806 | -48.5828 | 2024-11-10 04:38:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ca066265-df85-38b1-a209-002cb5cf737b | -3.22178 | -50.68126 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| c7aaa4e4-bb9a-36f9-8c80-e4b50c0af6d6 | -5.53171 | -41.70034 | 2024-11-10 04:38:00 | NPP-375D | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| bbc05deb-6863-334e-a01d-8f764146b35a | -2.37391 | -49.82261 | 2024-11-10 04:38:00 | NPP-375D | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ed49020f-e57e-30cc-83cf-c431edfcb9bd | -4.92541 | -45.36401 | 2024-11-10 04:38:00 | NPP-375D | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| a9f26776-fa72-30cb-8547-5af4d3d5f771 | -3.30852 | -49.63376 | 2024-11-10 04:38:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4f2472a5-5146-3d67-92f6-28c10b0a3d4c | -4.51747 | -45.70029 | 2024-11-10 04:38:00 | NPP-375D | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| e59195bf-11a2-3f9e-b038-e5fd31e8e41f | -3.21013 | -46.49931 | 2024-11-10 04:38:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4023a00b-744a-3bc8-b6dd-72474b0d72a1 | -3.24142 | -50.45227 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 469f7f79-7bd0-3307-a443-d3be7ae16422 | -3.16486 | -50.20817 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3589a65a-27e9-37b6-946f-2681cab16315 | -7.43644 | -39.77164 | 2024-11-10 04:38:00 | NPP-375D | EXU | PERNAMBUCO | Brasil | 2605301 | 26 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 81d269bf-e3b4-3c7c-b523-02d3b8c68973 | -1.71351 | -55.16305 | 2024-11-10 04:38:00 | NPP-375D | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 1e32abc4-a18a-3a70-bd8d-16ffee48e28c | -2.83515 | -46.64232 | 2024-11-10 04:38:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ae95b2c2-7ebf-302b-be5a-bca92e4d8883 | -4.34237 | -49.77059 | 2024-11-10 04:38:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 81115013-fef1-307f-bf7a-a6ddbcaafa9b | -2.31322 | -50.66718 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4ff47f76-9a13-38c8-bd27-be8ff20d3054 | -2.90162 | -54.52272 | 2024-11-10 04:38:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c0f91a77-66d1-3b2a-84f8-d8e4d23b39b9 | -3.19789 | -48.66636 | 2024-11-10 04:38:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 42d99ad3-eddb-3010-b3c0-16806eff052b | -2.71475 | -47.72973 | 2024-11-10 04:38:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 91de009a-dfcc-3ce6-a0ce-1a45d6fb6632 | -3.70897 | -53.75431 | 2024-11-10 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |


[Clique aqui para ver as próximas entradas](README109.md)
