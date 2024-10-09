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

## Dados Diários - Página 196

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ca84d137-cbd3-36cd-8a26-36967db33cb3 | -16.54784 | -57.71077 | 2024-10-09 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 0e8b17a8-0ae4-39eb-8b4e-3a367aa5c4d9 | -16.53233 | -57.74501 | 2024-10-09 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| adf9bc5c-aa6b-3cf2-8595-6ac58e76ecfc | -16.52957 | -57.74087 | 2024-10-09 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 00d86507-1406-33cc-af4d-328527c986a4 | -16.52901 | -57.74446 | 2024-10-09 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 26120ada-0b19-3a11-8120-1f25bddd18d5 | -16.52626 | -57.74031 | 2024-10-09 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 3b809d14-842d-39c2-b7c4-08cf5877d96e | -16.5257 | -57.74391 | 2024-10-09 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 00335cf2-71c4-3a76-a156-5bdc3a4fee90 | -16.52295 | -57.73976 | 2024-10-09 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 530bd303-c5d3-3585-a70e-589a6330505e | -16.49219 | -57.74222 | 2024-10-09 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 751a9743-75d3-3739-982b-c2814ba9f297 | -16.49163 | -57.74582 | 2024-10-09 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 8b5dced6-bbd7-3713-97de-c91df679f784 | -16.48943 | -57.73808 | 2024-10-09 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| e3ee8f1e-b82d-35b8-9474-03fbae5bc383 | -16.48888 | -57.74167 | 2024-10-09 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 9.3 |
| cc6313f1-b820-3697-a72b-69b9c5b48110 | -16.48832 | -57.74525 | 2024-10-09 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 9.3 |
| 50dfa1e2-9297-300f-9747-f4f03dd65e4b | -16.48612 | -57.73752 | 2024-10-09 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 3eeefc89-b8ea-3033-a10d-7f53d3edebc0 | -16.48557 | -57.74112 | 2024-10-09 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 9.3 |
| d24e0cf8-d5f0-3b01-bc54-801b768918e3 | -16.485 | -57.74471 | 2024-10-09 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 9.3 |
| 8c4d7ec2-f2e8-3225-b0dc-32a04b146130 | -16.64456 | -57.14779 | 2024-10-09 05:06:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 25752a78-eebc-3157-af27-f5e253b6a68e | -16.62563 | -57.11475 | 2024-10-09 05:06:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 256db486-ff7d-3cbe-ac1b-67ec471c366a | -16.62284 | -57.11055 | 2024-10-09 05:06:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| eefe02de-9d5a-3cae-995c-c2bc22765e81 | -16.62174 | -57.11786 | 2024-10-09 05:06:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| e71733a0-78fb-353b-84f4-385a333cb6b5 | -16.61951 | -57.11 | 2024-10-09 05:06:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| ee88e6d1-5e46-308e-9ad4-6d5977aaafe1 | -16.6184 | -57.11731 | 2024-10-09 05:06:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.3 |
| 5b2f6301-51ff-361c-a14c-352881e28cb6 | -16.60506 | -57.13758 | 2024-10-09 05:06:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 84671d3d-c55f-3131-925e-5923d0e9cbc2 | -16.60451 | -57.14123 | 2024-10-09 05:06:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| c9dec140-cd37-3dde-b2d0-13a7e52dd0ba | -16.60209 | -57.1412 | 2024-10-09 05:06:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 61408e82-1898-3e0b-90d2-fe58318a5c43 | -16.58097 | -57.12279 | 2024-10-09 05:06:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| adaccaa5-8daf-3ba4-8c91-85c9f0ce5e6e | -16.16524 | -57.41963 | 2024-10-09 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 99a742e3-8f21-3b7a-ad79-5e0bb8dc6e2a | -16.15917 | -57.41491 | 2024-10-09 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2350bbbf-c73c-3b47-87e5-14c54373787d | -16.15861 | -57.41855 | 2024-10-09 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 751ca742-f9f7-35f5-b0a7-67cbd4c7cee6 | -16.13925 | -57.41167 | 2024-10-09 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 476090b1-5ca8-34d7-a6d7-65eefc44b79c | -15.95842 | -57.21941 | 2024-10-09 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 624819d5-b934-3c0d-939e-907fa2914ba8 | -15.95565 | -57.21525 | 2024-10-09 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| cda7f888-03ec-33c4-aba9-020a6216aeec | -15.95509 | -57.21888 | 2024-10-09 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 740ecf9c-13df-30b4-9b49-c03ff82961e1 | -15.95288 | -57.21109 | 2024-10-09 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a9129d7e-42a6-3c58-8502-34fd9f06edeb | -15.95232 | -57.21473 | 2024-10-09 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 90d6bab6-35ff-345d-8dab-0350df81ec3c | -15.95177 | -57.21834 | 2024-10-09 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 48da6151-f87a-36b7-88ee-1912c6a556cf | -15.95122 | -57.22195 | 2024-10-09 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 9b020e3e-0f80-35e2-9f88-7c3be28c9b6e | -15.949 | -57.2142 | 2024-10-09 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a0121b2a-b10d-3e14-b992-a6d780ad96d5 | -15.94844 | -57.21781 | 2024-10-09 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 97936fac-f8de-3c09-af92-9073ea84957c | -15.94789 | -57.22141 | 2024-10-09 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 3a336813-8f2e-328c-9295-84399ca63569 | -15.94567 | -57.21367 | 2024-10-09 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 4.2 |
| a909cc02-abd7-385f-ad56-5c14347ba73a | -15.94512 | -57.21727 | 2024-10-09 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 4.9 |
| b9b4cc7d-5ce7-354e-95c4-5de34081dd65 | -15.94457 | -57.22087 | 2024-10-09 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 4.9 |
| abee096f-8a0f-3e68-a1a7-8209a9aaf241 | -15.94235 | -57.21311 | 2024-10-09 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 4.2 |
| e8ab1fd7-2314-3602-b894-9eef06258698 | -15.9418 | -57.21671 | 2024-10-09 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 5d7f5397-de16-37c9-a043-272adc2daf14 | -15.94125 | -57.22031 | 2024-10-09 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 3fe1e656-f7cd-3424-9189-cd01a1687841 | -15.93953 | -57.21294 | 2024-10-09 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 0faa3e15-cf0e-396f-ae3d-cbfec76e2c12 | -15.93897 | -57.21654 | 2024-10-09 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 4b319fef-d8d6-370f-92fe-7937ccda7cb1 | -15.93621 | -57.21238 | 2024-10-09 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 28c3e0d6-a7e9-35d5-9cbf-fdf906535f40 | -15.87457 | -57.47873 | 2024-10-09 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2504a698-b4c1-3ebf-ba1d-c93361d676ce | -15.87125 | -57.47817 | 2024-10-09 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8b886e11-825f-31ac-847b-f9adc02fb70f | -15.66764 | -57.39021 | 2024-10-09 05:06:00 | NOAA-20 | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 848de4fb-bcad-362c-b948-75f8933ea2c8 | -17.06813 | -56.84183 | 2024-10-09 05:06:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 67ea665c-fa16-3d35-ab2c-b7ede5c6eb65 | -17.06587 | -56.85671 | 2024-10-09 05:06:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 997ee41d-5f7e-3c40-8fc7-1d3cc50efe1b | -17.06532 | -56.83756 | 2024-10-09 05:06:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| dabd2b4a-0b60-34ed-8642-8b453b3cee9c | -17.06476 | -56.84128 | 2024-10-09 05:06:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 26294cf6-5727-3d56-b987-28343779c0ce | -17.0642 | -56.84501 | 2024-10-09 05:06:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| fdffd35e-e492-3e68-b578-074f4204e6b8 | -17.06364 | -56.84872 | 2024-10-09 05:06:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| c889a037-666c-39fc-a789-1b0c83859c21 | -17.06307 | -56.85244 | 2024-10-09 05:06:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 07c781fc-ad04-3762-9573-b2957abb9c12 | -17.06196 | -56.83701 | 2024-10-09 05:06:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| de6f0cff-3272-3334-b702-204d133c02b4 | -17.0614 | -56.84074 | 2024-10-09 05:06:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 37d3aaf5-dbfb-3e2d-9b8a-3d570da47bd5 | -17.06083 | -56.84446 | 2024-10-09 05:06:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| e8cf733a-5eff-3017-bea7-3de47343e266 | -17.05691 | -56.84763 | 2024-10-09 05:06:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| c08de570-514b-3c2b-8061-e246ae2302e8 | -17.05467 | -56.83965 | 2024-10-09 05:06:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| dd3d16d0-c514-3643-9ace-4c575496d0be | -17.0513 | -56.8391 | 2024-10-09 05:06:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 7e757a26-2833-35de-b02a-d0089e05e0da | -17.04401 | -56.84173 | 2024-10-09 05:06:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 365219de-843a-39df-a255-687e2dfae184 | -17.01934 | -56.84536 | 2024-10-09 05:06:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| 3f5b5060-57ad-3fb5-8e77-94d8e34ca20a | -17.01878 | -56.84908 | 2024-10-09 05:06:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| c6f24723-a181-3071-bbdf-fef3488b0892 | -16.96378 | -56.81367 | 2024-10-09 05:06:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| cc5158a8-6970-326a-b50b-1f6584bd4592 | -16.96268 | -56.75242 | 2024-10-09 05:06:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |
| cf7dab3d-8aea-3198-977f-17fecf87eebd | -16.96267 | -56.79824 | 2024-10-09 05:06:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| b8093250-4beb-391d-9169-78d003441bd8 | -16.9621 | -56.80196 | 2024-10-09 05:06:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| eacde72f-1097-30ca-924a-a1925f77e787 | -16.96155 | -56.7828 | 2024-10-09 05:06:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| c3dfc2bc-cfa6-3704-a95f-abfedbb175bf | -16.96154 | -56.80569 | 2024-10-09 05:06:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 39bd4ab8-9ee9-3cfe-abc2-a80a01853c07 | -16.96042 | -56.79025 | 2024-10-09 05:06:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.0 |
| 268ff725-74e6-3f12-9c25-30d294c16744 | -16.95875 | -56.75561 | 2024-10-09 05:06:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |
| fd878fab-8135-3f15-86a3-bfd7ab34b811 | -16.95762 | -56.78598 | 2024-10-09 05:06:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.0 |
| f8123edd-af7b-3f79-9bc0-dd8bb77c442b | -16.9565 | -56.7476 | 2024-10-09 05:06:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 25cf4cf4-2efb-36d4-acd5-798a1c2472da | -16.95481 | -56.78171 | 2024-10-09 05:06:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 16af9e4a-5160-38c0-aff7-0e4b25eb812a | -16.95425 | -56.78543 | 2024-10-09 05:06:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.0 |
| cfa816b8-3585-3941-81bf-05d896ea493b | -16.95369 | -56.78916 | 2024-10-09 05:06:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.0 |
| 9ae7eddb-4685-3546-8674-011622f5c9e3 | -16.95313 | -56.76999 | 2024-10-09 05:06:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| ceb2b8ea-3683-34e6-a010-dac1a4577aab | -16.95257 | -56.77371 | 2024-10-09 05:06:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 7f7eda13-ea5f-3cfe-9230-f99b02d110ca | -16.95201 | -56.77744 | 2024-10-09 05:06:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 68ee8a12-91bf-386b-a6a1-49846d962db0 | -16.95144 | -56.78117 | 2024-10-09 05:06:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| de9e0417-026a-32d1-98ae-ba9676520592 | -16.95089 | -56.76198 | 2024-10-09 05:06:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 0.7 |
| ddc4f8a0-c6e0-32ca-9ae0-b491ecfe7ea3 | -16.95088 | -56.78489 | 2024-10-09 05:06:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.0 |
| ef2114b6-a072-39aa-9d72-be19aec05837 | -16.95032 | -56.78862 | 2024-10-09 05:06:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.0 |
| b5146101-5331-38e3-b6a9-531f8866a03c | -16.94976 | -56.76944 | 2024-10-09 05:06:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| ac89827e-f8d3-3b2a-a18f-fddaad59ffb7 | -16.9492 | -56.77317 | 2024-10-09 05:06:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| e682a0ca-d3f8-34a3-8d67-49ffa7d6b031 | -16.94864 | -56.7769 | 2024-10-09 05:06:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 6659cb84-fc41-3086-afc7-d3a93a810812 | -16.94808 | -56.78062 | 2024-10-09 05:06:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| ff59fe4a-d0d5-3826-9f4e-167ceb8c5410 | -16.94752 | -56.78434 | 2024-10-09 05:06:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| 92a04beb-a922-316f-a220-ba01e349a7a7 | -16.94752 | -56.76143 | 2024-10-09 05:06:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 0.7 |
| 0f5eb298-7172-362e-817e-61d97e1e7d60 | -16.94696 | -56.78807 | 2024-10-09 05:06:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| e24e4f9f-5d96-316f-bcef-cd2a3c6ea747 | -16.94695 | -56.76516 | 2024-10-09 05:06:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 0.7 |
| 671e3b7f-7978-36b8-baa9-f4d2fd0b3e0a | -16.94527 | -56.77635 | 2024-10-09 05:06:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| d4d17492-14b2-3ad5-884a-d04255d74834 | -16.94134 | -56.77953 | 2024-10-09 05:06:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| 74e8e30b-98be-3d55-af17-303ffe821d2f | -16.94078 | -56.78326 | 2024-10-09 05:06:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 7f06ecea-dc01-3fcb-99af-2dde2dc9a7a1 | -16.87888 | -57.80955 | 2024-10-09 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 4ce85ef3-70e2-374c-8b5f-0a9ca4aa2bd9 | -16.87556 | -57.80899 | 2024-10-09 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |


[Clique aqui para ver as próximas entradas](README197.md)
