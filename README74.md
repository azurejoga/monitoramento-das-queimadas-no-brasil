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

## Dados Diários - Página 74

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8faa7305-dccf-385b-83e4-daa9ad5aea64 | -17.1238 | -57.49769 | 2024-11-20 05:18:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| 5e157f72-c4bd-3a7b-85d8-f7cbfc50529f | -15.29947 | -56.53104 | 2024-11-20 05:18:00 | NOAA-20 | JANGADA | MATO GROSSO | Brasil | 5104906 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cacc048c-47da-3938-8d42-00526eb6f1c7 | -2.7501 | -51.8171 | 2024-11-20 05:20:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 67.1 |
| b6e2679c-299a-3a70-a53b-e62bc9ca6964 | -2.7402 | -49.3502 | 2024-11-20 05:20:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 36.9 |
| a5d63de6-95e7-359c-930f-5e7cddcc66d4 | -2.9115 | -53.0809 | 2024-11-20 05:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 56.4 |
| 1fb99599-a712-3354-ade5-b2494c5856ca | -2.9299 | -53.0805 | 2024-11-20 05:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 67.7 |
| e5bd7145-5fc5-3479-903e-518a7690439a | -3.8205 | -47.8096 | 2024-11-20 05:20:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 34.5 |
| 9ff3dc05-5653-34ff-8d50-f2ca82f4b806 | -11.1109 | -54.6204 | 2024-11-20 05:20:00 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 75.7 |
| 10f6ab86-c0a1-36b2-842e-fe80d678fc1a | -4.0202 | -45.3695 | 2024-11-20 05:20:00 | GOES-16 | VITORINO FREIRE | MARANHÃO | Brasil | 2113009 | 21 | 33 | nan | nan | nan | Amazônia | 113.0 |
| 920f5f48-daf8-3417-bc9c-e43bb622f636 | -4.4404 | -46.5975 | 2024-11-20 05:20:00 | GOES-16 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 56.2 |
| 750cff88-c760-34cc-bf4d-be5fc4516247 | -11.1106 | -54.6408 | 2024-11-20 05:20:00 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 62.2 |
| ccbcd9f8-2e80-33aa-97c7-8224453334da | -2.7217 | -49.3508 | 2024-11-20 05:20:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 52.1 |
| 4851d94c-191d-36d4-8d07-8ed5edf653d6 | -2.75 | -51.8377 | 2024-11-20 05:20:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 66.1 |
| e6829a6e-c7bd-3beb-8783-c86500dcbea2 | -11.092 | -54.6221 | 2024-11-20 05:20:00 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 66.8 |
| fe285355-2659-320d-bcaa-ba160e10b87b | -4.0203 | -45.347 | 2024-11-20 05:20:00 | GOES-16 | VITORINO FREIRE | MARANHÃO | Brasil | 2113009 | 21 | 33 | nan | nan | nan | Amazônia | 56.1 |
| 374e8739-daa4-38ab-aa86-e22d2b60747d | -2.9116 | -53.0606 | 2024-11-20 05:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 77.9 |
| 54e40bf7-1e0d-39ce-b049-1c57d2b83ca0 | -2.93 | -53.0601 | 2024-11-20 05:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 72.8 |
| 1f6ae54d-05df-3acd-a9ad-cfa5c0dfec86 | -4.4405 | -46.5754 | 2024-11-20 05:20:00 | GOES-16 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 58.7 |
| 47fa0cea-1d4c-36dd-b901-36c177a7675c | -23.25895 | -54.93227 | 2024-11-20 05:20:00 | NOAA-20 | AMAMBAI | MATO GROSSO DO SUL | Brasil | 5000609 | 50 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| d412dc2a-c908-33b4-9446-965f7a49cd75 | -22.0545 | -56.01258 | 2024-11-20 05:20:00 | NOAA-20 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7bfec29e-d24f-3343-92fc-023b16cb01d2 | -21.31468 | -56.01047 | 2024-11-20 05:20:00 | NOAA-20 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| cfa8ca68-b53d-3890-847a-d2526dd375bb | -23.25835 | -54.938 | 2024-11-20 05:20:00 | NOAA-20 | AMAMBAI | MATO GROSSO DO SUL | Brasil | 5000609 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 6bed0a58-8b09-33e0-864b-ea458848284f | -23.26371 | -54.93286 | 2024-11-20 05:20:00 | NOAA-20 | AMAMBAI | MATO GROSSO DO SUL | Brasil | 5000609 | 50 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 73e8a477-3f15-340f-b151-c307eb310781 | -2.9116 | -53.0606 | 2024-11-20 05:30:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 97.4 |
| ca5a1265-b754-31ac-9d87-f445b290c6fa | -11.092 | -54.6221 | 2024-11-20 05:30:00 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 65.9 |
| ae42acba-ed15-3e68-a677-ef4e0bcc764e | -1.2017 | -53.6769 | 2024-11-20 05:30:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 45.8 |
| 6d512999-bfbd-3957-8ddf-bf707d2b1f62 | -11.1106 | -54.6408 | 2024-11-20 05:30:00 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 63.5 |
| 90b5bcfa-6968-3650-804e-4f34344c2eff | -2.9115 | -53.0809 | 2024-11-20 05:30:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 75.1 |
| 6552908c-efef-31eb-9340-cc46e7647a2c | -2.93 | -53.0601 | 2024-11-20 05:30:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 84.6 |
| 0dcea274-d34b-36ba-8bcd-9cc444efad81 | -2.9299 | -53.0805 | 2024-11-20 05:30:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 77.5 |
| 9cadc44e-ff7b-3a38-829a-821c8fc39277 | -11.1109 | -54.6204 | 2024-11-20 05:30:00 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 77.7 |
| 358583a9-7d13-30e4-a702-bdbe9dac05d0 | -4.4405 | -46.5754 | 2024-11-20 05:30:00 | GOES-16 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 62.2 |
| 71d4bae8-905c-3845-9bd1-56cf4723012b | -2.7402 | -49.3502 | 2024-11-20 05:30:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 35.3 |
| ef14f689-6b7f-3339-bf7c-bb3586b3682a | -2.7217 | -49.3508 | 2024-11-20 05:30:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 53.3 |
| cc583060-d4e6-3514-9714-95c4f6e21b45 | -4.4404 | -46.5975 | 2024-11-20 05:30:00 | GOES-16 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 60.2 |
| b3480c2e-1544-3890-8d10-0cc780ce82c2 | -2.93 | -53.0601 | 2024-11-20 05:40:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 116.2 |
| 3c86c75d-64f0-328c-b25c-6d729ecdde6c | -11.1106 | -54.6408 | 2024-11-20 05:40:00 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 70.2 |
| 8c81ca9f-a080-3d0c-a79f-3ac2af7a26d9 | -3.1463 | -45.2954 | 2024-11-20 05:40:00 | GOES-16 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 47.3 |
| 1b025108-46f7-3fd4-b4ef-59d5bb2c86d1 | -4.459 | -46.5966 | 2024-11-20 05:40:00 | GOES-16 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 60.5 |
| a3faff3e-e60c-348b-98fd-2d232ee8751b | -1.2017 | -53.6769 | 2024-11-20 05:40:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 52.2 |
| a6116cdc-918b-3774-b87f-7d176420e6c2 | -2.57 | -45.3606 | 2024-11-20 05:40:00 | GOES-16 | PRESIDENTE SARNEY | MARANHÃO | Brasil | 2109270 | 21 | 33 | nan | nan | nan | Amazônia | 60.4 |
| f2c191a9-2c53-3434-b5e2-cce769ea10fc | -11.1109 | -54.6204 | 2024-11-20 05:40:00 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 83.9 |
| e5ea7938-37b6-32f8-bd47-e44d2129c33b | -2.9115 | -53.0809 | 2024-11-20 05:40:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 56.3 |
| c15cc52b-876e-3a04-8f17-170d2e4fc6ac | -2.7217 | -49.3508 | 2024-11-20 05:40:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 55.8 |
| d335d897-3000-3fb6-9ed6-1fd258ef53fb | -2.9116 | -53.0606 | 2024-11-20 05:40:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 80.8 |
| 22f3d154-cfde-30a7-94e2-82fa0cd51d5d | -2.5514 | -45.3612 | 2024-11-20 05:40:00 | GOES-16 | PRESIDENTE SARNEY | MARANHÃO | Brasil | 2109270 | 21 | 33 | nan | nan | nan | Amazônia | 52.7 |
| 81b70cf6-4ba5-30b0-9b99-b711ead86ba6 | -2.7402 | -49.3502 | 2024-11-20 05:40:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 44.2 |
| 627314c9-559c-3a6e-b575-f3caebce3f8c | -2.9299 | -53.0805 | 2024-11-20 05:40:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 104.0 |
| 72d4c6b4-f58a-31cf-810f-7e6ab5b29f2c | -4.4592 | -46.5745 | 2024-11-20 05:40:00 | GOES-16 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 60.5 |
| 42f0ec71-84a1-390b-9e37-4b00f5918fe5 | -2.9116 | -53.0606 | 2024-11-20 05:50:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 80.5 |
| a2f29473-7ad6-3bb5-8c2e-edbf17a66a7b | -1.2017 | -53.6769 | 2024-11-20 05:50:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 52.9 |
| 858dc6cd-9254-3e1d-b46b-b910bee2e491 | -2.7217 | -49.3508 | 2024-11-20 05:50:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 42.0 |
| b760096b-74e1-3c20-9ca1-451f2046ec87 | -2.57 | -45.3606 | 2024-11-20 05:50:00 | GOES-16 | PRESIDENTE SARNEY | MARANHÃO | Brasil | 2109270 | 21 | 33 | nan | nan | nan | Amazônia | 70.9 |
| d7c2835c-71c6-3c7f-8dac-78f444dcd5a4 | -2.9299 | -53.0805 | 2024-11-20 05:50:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 95.2 |
| d42f4932-da68-3d38-ab34-afc042f4f3ec | -2.93 | -53.0601 | 2024-11-20 05:50:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 108.5 |
| 7ea088a9-4185-3ba1-ae94-33548e1229d1 | -2.9115 | -53.0809 | 2024-11-20 05:50:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 54.4 |
| fead46d5-aa3f-3ae3-bff9-544d7908d9a3 | -2.5514 | -45.3612 | 2024-11-20 05:50:00 | GOES-16 | PRESIDENTE SARNEY | MARANHÃO | Brasil | 2109270 | 21 | 33 | nan | nan | nan | Amazônia | 68.6 |
| 406fe849-daa2-36af-b878-ef59b07dc768 | -2.7218 | -49.3295 | 2024-11-20 06:00:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 34.9 |
| 051d7a47-04a3-3f76-89b4-5deb95774aa0 | -6.9233 | -41.1879 | 2024-11-20 06:00:00 | GOES-16 | SANTO ANTÔNIO DE LISBOA | PIAUÍ | Brasil | 2209401 | 22 | 33 | nan | nan | nan | Caatinga | 41.8 |
| 26634dc5-531b-3e65-be9f-90ae851c94ad | -2.9116 | -53.0606 | 2024-11-20 06:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 82.0 |
| e36e9199-f8a2-320c-bec9-b5232a821ec5 | -2.9299 | -53.0805 | 2024-11-20 06:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 88.5 |
| 9657db4c-8dea-3298-b8b3-f7ba16d0b855 | -1.2017 | -53.6769 | 2024-11-20 06:00:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 51.4 |
| eaf50ee6-c9f3-302b-99ca-0cfb63c6ca48 | -2.7217 | -49.3508 | 2024-11-20 06:00:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 67.2 |
| c8bfe36c-838d-3cc8-842b-bbe7d919f345 | -2.9115 | -53.0809 | 2024-11-20 06:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 58.7 |
| 173a6e97-8126-31ec-a345-3dbb3d93a936 | -2.93 | -53.0601 | 2024-11-20 06:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 98.2 |
| 9ce1aceb-a8ac-3693-8997-75b46ccc85f5 | -2.7217 | -49.3508 | 2024-11-20 06:10:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 55.6 |
| 4e3a5230-d12f-32c4-b5a5-e4c8c1a078ae | -2.9299 | -53.0805 | 2024-11-20 06:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 93.8 |
| 33358ba5-04f4-3c15-a143-58411da2c03d | -2.7402 | -49.3502 | 2024-11-20 06:10:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 42.6 |
| 3a8a242c-302d-3cdd-b695-f65ce42a8f31 | -6.9421 | -41.1859 | 2024-11-20 06:10:00 | GOES-16 | SANTO ANTÔNIO DE LISBOA | PIAUÍ | Brasil | 2209401 | 22 | 33 | nan | nan | nan | Caatinga | 46.1 |
| 9d9da4fc-4aa6-3300-9180-76894ef95059 | -2.93 | -53.0601 | 2024-11-20 06:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 98.5 |
| bf6a5463-bd72-34c6-8d75-0323de8d9e4c | -2.9115 | -53.0809 | 2024-11-20 06:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 58.7 |
| 21d9c674-4f40-3878-b306-082036c0daed | -2.9116 | -53.0606 | 2024-11-20 06:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 84.1 |
| c3fdf346-654b-3531-bd35-0aaab78ffa59 | -2.7218 | -49.3295 | 2024-11-20 06:10:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 29.3 |
| 3edcc6b9-e003-3040-87a8-9d9c4b30c8f7 | -2.73121 | -49.33255 | 2024-11-20 06:16:00 | AQUA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 63.4 |
| 8ccbb547-c2c3-3c00-8ceb-90934b5ef3bb | -1.4497 | -52.66354 | 2024-11-20 06:16:00 | AQUA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 13.1 |
| c5d80ab6-35cb-3817-8e69-fe08564909aa | -1.85369 | -54.26238 | 2024-11-20 06:16:00 | AQUA_M-M | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 0568b22b-d382-38d6-84c6-1ad0cefde95a | -1.51535 | -55.48184 | 2024-11-20 06:16:00 | AQUA_M-M | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 3fc930b0-0427-3b17-b8ee-d41db223b1ab | -1.47387 | -53.47824 | 2024-11-20 06:16:00 | AQUA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 90fa228d-9635-348d-b7ae-9e523b0d1420 | -1.85154 | -54.26902 | 2024-11-20 06:16:00 | AQUA_M-M | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 27.6 |
| a5c63b09-c1d0-3824-9d1d-7313c7176c31 | -1.1935 | -53.67656 | 2024-11-20 06:16:00 | AQUA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 31.7 |
| 997434c2-e8f9-3e9a-a0e8-7aba644b0630 | -2.71647 | -49.33827 | 2024-11-20 06:16:00 | AQUA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 105.2 |
| a3348186-2e5e-3122-8c69-577de4687d99 | -1.85147 | -54.27721 | 2024-11-20 06:16:00 | AQUA_M-M | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 30.7 |
| 2edc04dc-f251-37f0-8527-140fbf42579f | -1.64616 | -52.66327 | 2024-11-20 06:16:00 | AQUA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 15.4 |
| e0ded285-a06f-3d1d-8c05-443edb33f00b | -1.64375 | -52.67787 | 2024-11-20 06:16:00 | AQUA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 0ae49219-ab32-3483-b4c3-89be0dd4e4b7 | -1.14991 | -53.51217 | 2024-11-20 06:16:00 | AQUA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| b05f4c50-c8b5-3855-acb1-c5f3aa506ec7 | -1.25339 | -53.35849 | 2024-11-20 06:16:00 | AQUA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 13.9 |
| 6b5c3b3d-9eee-334a-a9a7-6eea0ced2191 | -2.71418 | -49.33017 | 2024-11-20 06:16:00 | AQUA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 52.5 |
| 832d50e6-efe8-3d90-a8e0-6c80edae5c90 | -1.19595 | -53.66018 | 2024-11-20 06:16:00 | AQUA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 21.8 |
| 3e417ba6-0937-310a-b6f6-d8246f7cc3b0 | -1.84942 | -54.28396 | 2024-11-20 06:16:00 | AQUA_M-M | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 358a538e-8284-3338-8dda-3877400eb7f8 | -2.90076 | -53.04787 | 2024-11-20 06:18:00 | AQUA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 19.6 |
| 345e1213-6cf8-390c-a033-e8fc67ac1bc7 | -3.19951 | -54.3285 | 2024-11-20 06:18:00 | AQUA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 1da597d9-cf8e-3d8c-b94e-91f86d64aefd | -3.2825 | -53.84124 | 2024-11-20 06:18:00 | AQUA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 11.5 |
| d86976db-7315-3328-80c5-db049750ab42 | -3.10226 | -53.73323 | 2024-11-20 06:18:00 | AQUA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 9.9 |
| dea86fe4-9fd9-33d6-83b5-f4c0baae590e | -3.08159 | -54.66658 | 2024-11-20 06:18:00 | AQUA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 3a83641c-04fb-318a-8039-ee3aa0669d55 | -2.91065 | -53.06963 | 2024-11-20 06:18:00 | AQUA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 42.3 |
| bb50ca5f-722a-395f-924b-c4837c48ea3f | -2.92346 | -53.07097 | 2024-11-20 06:18:00 | AQUA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 141.5 |
| b91c6d1f-6320-3372-81a7-5859457b41ba | -2.91355 | -53.04953 | 2024-11-20 06:18:00 | AQUA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 41.2 |
| 588c9910-e258-3483-9819-e2a8df1b487d | -3.08276 | -54.65978 | 2024-11-20 06:18:00 | AQUA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 14.1 |
| 720424de-1f3f-3622-a0a1-19fe1e21ddf6 | -3.28501 | -53.82404 | 2024-11-20 06:18:00 | AQUA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 34.4 |
| 469f6bb1-e079-3f58-89fb-bb8ded4de8f4 | -3.09976 | -53.75047 | 2024-11-20 06:18:00 | AQUA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |


[Clique aqui para ver as próximas entradas](README75.md)
