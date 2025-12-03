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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2b7dc3dd-fefb-3127-9bed-b5d03fa02caa | -2.9797 | -49.5342 | 2025-12-03 00:00:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 74.7 |
| 24b31bbb-4d74-33c6-bdc4-c3767d451b8f | -2.6267 | -45.1111 | 2025-12-03 00:00:00 | GOES-19 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 79.6 |
| bb7639ea-38dd-3e6a-9fe8-8006d9966602 | -1.9167 | -54.0901 | 2025-12-03 00:00:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 92.6 |
| 920d92fc-d7bc-3bdb-acb7-d8eaca48753e | -3.6268 | -49.4912 | 2025-12-03 00:00:00 | GOES-19 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 66.1 |
| 59a2167f-e804-3a99-b269-363126dd2b28 | -1.8984 | -54.0903 | 2025-12-03 00:00:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 54.7 |
| b62f8bee-a3c4-3fa4-be82-8849463ecf75 | -2.2087 | -47.9929 | 2025-12-03 00:00:00 | GOES-19 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 193.1 |
| 3ee83f81-c459-3d5e-83db-e5595dc13aec | -8.1075 | -43.1411 | 2025-12-03 00:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 78.8 |
| 2ec3d5c9-f7b7-3fd9-8901-37765b94a9ad | -11.1377 | -53.9634 | 2025-12-03 00:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 62.8 |
| fb5dcd3b-1814-3886-b6e1-31f69a5cdc74 | -2.9623 | -44.8733 | 2025-12-03 00:00:00 | GOES-19 | SÃO JOÃO BATISTA | MARANHÃO | Brasil | 2111003 | 21 | 33 | nan | nan | nan | Amazônia | 60.8 |
| 6a082ed7-a367-3092-a938-8efdce54c9d9 | -1.4737 | -45.7907 | 2025-12-03 00:00:00 | GOES-19 | GODOFREDO VIANA | MARANHÃO | Brasil | 2104305 | 21 | 33 | nan | nan | nan | Amazônia | 74.1 |
| 0a7a553a-924c-31ef-85f3-45179637e05c | -2.4763 | -45.5655 | 2025-12-03 00:00:00 | GOES-19 | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 97.2 |
| 236b38fc-daef-300f-be70-286a9a9c0bf9 | -2.4578 | -45.566 | 2025-12-03 00:00:00 | GOES-19 | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 96.4 |
| ac6e4e02-5f3d-32bb-8336-a4727f108ab1 | -2.2086 | -48.0145 | 2025-12-03 00:00:00 | GOES-19 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 112.9 |
| 96a1bd4d-a420-3258-9cb6-4e5b639c849d | -2.4577 | -45.5885 | 2025-12-03 00:00:00 | GOES-19 | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 144.8 |
| 9b02930b-2db5-3187-ad93-6a7e9933357c | -3.5481 | -50.5267 | 2025-12-03 00:00:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 66.3 |
| 6a342736-ed60-3e52-ac17-2546ca50e22e | -2.9983 | -49.5124 | 2025-12-03 00:00:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 74.1 |
| f64e16b3-aafb-35db-9363-349dda542c14 | -3.2195 | -45.5398 | 2025-12-03 00:00:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 173.8 |
| 619bfe56-b38f-3519-a2b5-2741d97d56b6 | -11.1188 | -53.9652 | 2025-12-03 00:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 73.9 |
| 84687006-bfff-33dd-86bd-c043ab15caf2 | -2.9798 | -49.513 | 2025-12-03 00:00:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 97.3 |
| c7cafe07-a129-3bc2-b9e2-781cc7a43550 | -2.6079 | -45.1568 | 2025-12-03 00:00:00 | GOES-19 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 121.1 |
| 9ee8d02d-ee6f-334f-8e09-29d933443233 | -11.2702 | -52.4605 | 2025-12-03 00:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 81.4 |
| 7cc5acd7-0373-3d00-91fe-b4ecc91e1825 | -4.2243 | -45.4717 | 2025-12-03 00:00:00 | GOES-19 | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 99.2 |
| b9a12abf-514b-3907-94f2-3495362b46f7 | -2.4763 | -45.5879 | 2025-12-03 00:00:00 | GOES-19 | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 147.0 |
| cb1aa28b-2563-3c14-b14c-2706617078f5 | -3.2196 | -45.5173 | 2025-12-03 00:00:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 85.4 |
| d63e06dd-90fd-3748-bea8-5007c4220b44 | -11.119 | -53.9446 | 2025-12-03 00:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 151.8 |
| 41c75ca4-93b8-3e45-b2a1-b16130e5432d | -2.6266 | -45.1336 | 2025-12-03 00:00:00 | GOES-19 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 566.1 |
| a7597abe-8829-323d-ad82-6da0a1ed03c2 | -2.608 | -45.1342 | 2025-12-03 00:00:00 | GOES-19 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 168.5 |
| 8c6ba445-5aba-3994-ae73-54d37976a09e | -2.6265 | -45.1562 | 2025-12-03 00:00:00 | GOES-19 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 353.7 |
| ea585aa9-f11d-3d11-a9d3-5224c11d9f58 | -3.2009 | -45.5405 | 2025-12-03 00:00:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 106.2 |
| e0e212ab-efcc-3d41-a260-85fe46911377 | -2.9809 | -44.8726 | 2025-12-03 00:00:00 | GOES-19 | SÃO JOÃO BATISTA | MARANHÃO | Brasil | 2111003 | 21 | 33 | nan | nan | nan | Amazônia | 54.7 |
| ea37ac96-9587-35a7-9472-0bdb6832b3de | -1.9168 | -54.07 | 2025-12-03 00:00:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 45.8 |
| 86900418-22f9-3942-b64e-4a0ad52097cc | -2.6452 | -45.133 | 2025-12-03 00:00:00 | GOES-19 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 87.1 |
| 75763c54-2545-3435-824a-85681a5929de | -11.1379 | -53.9429 | 2025-12-03 00:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 117.9 |
| 3ada72e9-20e6-3b55-bd2e-90d3de916a6d | -21.622 | -56.1312 | 2025-12-03 00:00:00 | GOES-19 | JARDIM | MATO GROSSO DO SUL | Brasil | 5005004 | 50 | 33 | nan | nan | nan | Cerrado | 91.2 |
| 29c7c829-05b8-3abb-88ae-2958e03b894c | -4.2243 | -45.4717 | 2025-12-03 00:10:00 | GOES-19 | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 153.1 |
| 761ff40e-edaf-350c-afef-5deb48f8f57f | -2.2086 | -48.0145 | 2025-12-03 00:10:00 | GOES-19 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 111.0 |
| f004d732-f1df-373b-b516-4f5c59fce74e | -2.6265 | -45.1562 | 2025-12-03 00:10:00 | GOES-19 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 303.9 |
| 7532d4c1-e420-3279-9f4c-5e9e1aef273a | -4.2913 | -43.7822 | 2025-12-03 00:10:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 63.3 |
| 0aaecbc3-f12c-32fc-8515-bc823b71b08e | -4.2057 | -45.4727 | 2025-12-03 00:10:00 | GOES-19 | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 62.4 |
| f39c47b2-9624-38e2-9ef3-d8fa8d0bd50f | -1.4923 | -45.7903 | 2025-12-03 00:10:00 | GOES-19 | GODOFREDO VIANA | MARANHÃO | Brasil | 2104305 | 21 | 33 | nan | nan | nan | Amazônia | 69.2 |
| 5d58d0da-9015-32ac-852e-dc5dccc00ac9 | -2.9798 | -49.513 | 2025-12-03 00:10:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 97.5 |
| 426e2003-9b8b-3e8b-aefa-b070e12ca062 | -4.2429 | -45.4707 | 2025-12-03 00:10:00 | GOES-19 | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 73.6 |
| cfb887fd-f4df-3057-8728-2c6ba42f1a25 | -2.2087 | -47.9929 | 2025-12-03 00:10:00 | GOES-19 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 164.1 |
| 2685d84d-65dc-3306-a6e4-9584443c5812 | -2.6266 | -45.1336 | 2025-12-03 00:10:00 | GOES-19 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 616.4 |
| e7ed06af-dccd-3aab-9c5a-d89693318981 | -21.622 | -56.1312 | 2025-12-03 00:10:00 | GOES-19 | JARDIM | MATO GROSSO DO SUL | Brasil | 5005004 | 50 | 33 | nan | nan | nan | Cerrado | 85.7 |
| a5b5cb69-6086-3258-be8a-b81bcb73e2a7 | -2.608 | -45.1342 | 2025-12-03 00:10:00 | GOES-19 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 137.6 |
| 7792fff5-fe8a-3777-8ee1-f81e24a5bc7a | -3.2195 | -45.5398 | 2025-12-03 00:10:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 157.5 |
| e7e8eddb-3c54-3459-b1f8-921629dcec8f | -11.2702 | -52.4605 | 2025-12-03 00:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 67.1 |
| 6d6187f6-e0c8-3d75-ba1c-6c3c32367ba9 | -2.6079 | -45.1568 | 2025-12-03 00:10:00 | GOES-19 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 87.1 |
| a68edc1c-fe4b-3733-8afd-1769cdc95f04 | -2.961 | -45.1672 | 2025-12-03 00:10:00 | GOES-19 | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 61.1 |
| ce98affa-eacf-385b-a389-cd741560bf92 | -11.119 | -53.9446 | 2025-12-03 00:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 133.7 |
| c68fb68b-aebc-375d-a741-b338aa674d74 | -11.1377 | -53.9634 | 2025-12-03 00:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 64.1 |
| 0dd00190-6ae5-32c8-ac2f-e89c3edba1da | -1.4737 | -45.7907 | 2025-12-03 00:10:00 | GOES-19 | GODOFREDO VIANA | MARANHÃO | Brasil | 2104305 | 21 | 33 | nan | nan | nan | Amazônia | 97.7 |
| 21ecc2a5-1872-3048-977a-46bb61b56fa7 | -11.1188 | -53.9652 | 2025-12-03 00:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 77.0 |
| 2cd50961-3693-3bda-823a-396674dd485a | -1.8984 | -54.0903 | 2025-12-03 00:10:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 51.7 |
| 62d3314b-6616-3de0-8e87-59840f5c57a0 | -11.1379 | -53.9429 | 2025-12-03 00:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 108.3 |
| f980b621-5c8e-3e5d-9a50-8e26fc9dc934 | -4.2242 | -45.4942 | 2025-12-03 00:10:00 | GOES-19 | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 70.2 |
| aed7733e-b8ae-33d9-97bf-a8707632f6e4 | -8.1075 | -43.1411 | 2025-12-03 00:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 84.2 |
| 41a90efe-5a30-3ba4-8113-df8219eba70a | -3.2196 | -45.5173 | 2025-12-03 00:10:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 92.0 |
| cb342c87-c337-3e76-9704-04922eeea6cc | -4.2914 | -43.7591 | 2025-12-03 00:10:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 62.4 |
| 38c06ded-c6a5-3b18-9787-d62cab445531 | -2.6452 | -45.133 | 2025-12-03 00:10:00 | GOES-19 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 81.4 |
| 5cf2ba91-6ad8-372a-9aba-cc0700f8e177 | -4.2244 | -45.4492 | 2025-12-03 00:10:00 | GOES-19 | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 55.8 |
| e0f39736-c146-38b1-9661-4a54466cc632 | -1.9167 | -54.0901 | 2025-12-03 00:10:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 75.4 |
| fc8c160f-827d-3114-ad8d-22a104191c45 | -4.2243 | -45.4717 | 2025-12-03 00:20:00 | GOES-19 | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 61.4 |
| c26728f2-698a-32cb-8cc7-291ff6310c4b | -1.4923 | -45.768 | 2025-12-03 00:20:00 | GOES-19 | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 63.9 |
| baaf84a5-1582-3d16-96af-45e2f2ac7077 | -11.2702 | -52.4605 | 2025-12-03 00:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 57.5 |
| 2b7e69df-839d-39d6-a93e-765c44311d24 | -2.9798 | -49.513 | 2025-12-03 00:20:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 72.6 |
| 6f47e4a0-aaeb-3de4-8ea8-c6e3e346dfda | -3.2195 | -45.5398 | 2025-12-03 00:20:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 144.7 |
| 3013fcc5-74bb-3ed6-a5a3-9290dd9edd52 | -1.4738 | -45.7684 | 2025-12-03 00:20:00 | GOES-19 | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 70.8 |
| 34eb0ab0-96be-3928-9531-5711d2787ed0 | -11.1379 | -53.9429 | 2025-12-03 00:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 100.8 |
| 8bf2c384-d17a-3a28-85ae-b0d05d3c945a | -11.1377 | -53.9634 | 2025-12-03 00:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 64.0 |
| d9048ca1-81fc-3f02-a05b-b40f53004707 | -11.119 | -53.9446 | 2025-12-03 00:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 84.0 |
| 6446f0ec-0c4c-347c-8b83-14ef4d86265f | -21.622 | -56.1312 | 2025-12-03 00:20:00 | GOES-19 | JARDIM | MATO GROSSO DO SUL | Brasil | 5005004 | 50 | 33 | nan | nan | nan | Cerrado | 79.9 |
| 044cf082-374b-37ba-97c0-ddd9289228f2 | -1.9167 | -54.0901 | 2025-12-03 00:20:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 40.3 |
| 677c1e4e-0502-3d5f-9f71-986e9d0924b2 | -11.2892 | -52.4586 | 2025-12-03 00:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 54.4 |
| 9837970c-d2d3-33e9-a973-cf99fb7409f4 | 2.8731 | -60.2563 | 2025-12-03 00:20:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 52.8 |
| e6479ab5-0cdc-3b40-b5f4-727c472b3ebd | -2.6265 | -45.1562 | 2025-12-03 00:20:00 | GOES-19 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 218.4 |
| e85b9417-e3ce-3999-87f7-05c356853b9f | -2.6079 | -45.1568 | 2025-12-03 00:20:00 | GOES-19 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 93.6 |
| e2442528-0173-3997-9840-76d7af386d04 | -3.2196 | -45.5173 | 2025-12-03 00:20:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 90.3 |
| 3618b0d6-eaba-3499-8ac0-8aa15124b425 | -1.4923 | -45.7903 | 2025-12-03 00:20:00 | GOES-19 | GODOFREDO VIANA | MARANHÃO | Brasil | 2104305 | 21 | 33 | nan | nan | nan | Amazônia | 122.7 |
| 36c1c911-7c00-3f78-850d-b7f8fc1755fb | -2.6266 | -45.1336 | 2025-12-03 00:20:00 | GOES-19 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 471.8 |
| 3e355e3f-7a72-351c-a001-8a9aa75855ad | -2.1902 | -47.9934 | 2025-12-03 00:20:00 | GOES-19 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 64.0 |
| 82bf6baf-23e9-3e74-a5df-f84a262f2ec6 | -2.2087 | -47.9929 | 2025-12-03 00:20:00 | GOES-19 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 129.1 |
| 5172f5fc-7320-3870-a2e8-1ce90faa7a0c | -2.2086 | -48.0145 | 2025-12-03 00:20:00 | GOES-19 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 101.4 |
| 4bb83b2a-2756-3488-853e-b0616a511783 | -1.4737 | -45.7907 | 2025-12-03 00:20:00 | GOES-19 | GODOFREDO VIANA | MARANHÃO | Brasil | 2104305 | 21 | 33 | nan | nan | nan | Amazônia | 141.4 |
| d2b8b2df-e1b1-3389-853a-25a3b242290a | -2.608 | -45.1342 | 2025-12-03 00:20:00 | GOES-19 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 166.1 |
| 560348ef-df5e-3d27-be43-8f5a1ef7e135 | -11.1188 | -53.9652 | 2025-12-03 00:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 60.0 |
| aec7cf3b-cf24-37aa-bf4f-353969ba6274 | -21.622 | -56.1312 | 2025-12-03 00:30:00 | GOES-19 | JARDIM | MATO GROSSO DO SUL | Brasil | 5005004 | 50 | 33 | nan | nan | nan | Cerrado | 81.1 |
| 62a731c2-a7a5-39bc-9541-b92747abc1d6 | -11.1188 | -53.9652 | 2025-12-03 00:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 60.7 |
| a6497290-28ed-3d42-ad4b-ebcd833d0485 | -2.2086 | -48.0145 | 2025-12-03 00:30:00 | GOES-19 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 91.6 |
| 780ee8ee-cca1-3982-a466-f15953a4bd6e | -2.608 | -45.1342 | 2025-12-03 00:30:00 | GOES-19 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 129.0 |
| 93da9175-2766-360a-bf46-61cd2b4eb852 | -2.2087 | -47.9929 | 2025-12-03 00:30:00 | GOES-19 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 119.6 |
| 7535626e-52e1-3d48-841e-2d07a88146d2 | -1.9167 | -54.0901 | 2025-12-03 00:30:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 35.2 |
| 1f27d963-2ba2-3e34-b84f-0b9494d67da8 | -1.4738 | -45.7684 | 2025-12-03 00:30:00 | GOES-19 | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 65.0 |
| 48c05851-8760-32f7-a1f3-afcc043dd1a3 | -3.2195 | -45.5398 | 2025-12-03 00:30:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 109.7 |
| aed5160c-35c6-3486-b184-b8a039eaee93 | -11.2892 | -52.4586 | 2025-12-03 00:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 53.6 |
| 0de4a7f9-a842-3ad8-a298-fe8e48ab4af8 | -1.4923 | -45.7903 | 2025-12-03 00:30:00 | GOES-19 | GODOFREDO VIANA | MARANHÃO | Brasil | 2104305 | 21 | 33 | nan | nan | nan | Amazônia | 126.4 |
| 173d9f10-6c2f-389c-9df9-9baa75f51e10 | 2.8731 | -60.2563 | 2025-12-03 00:30:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 55.6 |
| 02f5dd36-a940-3ab0-8c61-5a6f5fc2853d | -2.6265 | -45.1562 | 2025-12-03 00:30:00 | GOES-19 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 189.3 |
| f9808977-9188-3556-9911-47fc2aaac315 | -4.346 | -49.949 | 2025-12-03 00:30:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 64.5 |


[Clique aqui para ver as próximas entradas](README2.md)
