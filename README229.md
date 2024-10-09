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

## Dados Diários - Página 229

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 686fb91e-aa63-3da7-8aaf-6050ba0fbcfa | -16.9413 | -57.4449 | 2024-10-09 11:26:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 309.9 |
| 8df59e79-7076-30ba-b925-80985ce603b7 | -16.9609 | -57.4426 | 2024-10-09 11:26:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1486.9 |
| 5f87210a-ab10-3899-88b4-4f9ba69fa06f | -18.6199 | -57.2188 | 2024-10-09 11:26:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 209.7 |
| 76aa156e-f4ed-3e16-a0da-e8f97de6f7e9 | -6.7798 | -60.0552 | 2024-10-09 11:35:45 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 94.4 |
| a22258fd-eea9-326c-bba1-9584d1a7359f | -10.5746 | -48.0178 | 2024-10-09 11:36:06 | GOES-16 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 78.3 |
| a1ddf162-61ff-35ae-bcdb-ef6d5fc56b85 | -12.011 | -51.0531 | 2024-10-09 11:36:14 | GOES-16 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 84.1 |
| 5b5415fe-eece-31cd-9213-1dca9c751259 | -11.9729 | -51.0575 | 2024-10-09 11:36:14 | GOES-16 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 77.7 |
| 748b2350-1187-3a5a-a17b-34cbdb0ea013 | -13.3786 | -61.9582 | 2024-10-09 11:36:23 | GOES-16 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 91.1 |
| d8cda765-4ef8-3356-bd99-1797986c2a1a | -13.9353 | -44.5046 | 2024-10-09 11:36:24 | GOES-16 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 157.9 |
| 6187ed05-9265-35c0-aaa2-03d7111da40c | -13.9158 | -44.5081 | 2024-10-09 11:36:24 | GOES-16 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 93.7 |
| 9d928750-4293-37c7-b7f1-1b861db633b3 | -13.8963 | -44.5116 | 2024-10-09 11:36:24 | GOES-16 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 194.6 |
| bfd9225a-bf40-35ae-a10e-2a20865519d1 | -13.8958 | -44.5351 | 2024-10-09 11:36:24 | GOES-16 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 83.6 |
| 1fc7a6bd-9bcf-3d96-86a5-13f59d0d96a9 | -13.9348 | -44.5282 | 2024-10-09 11:36:24 | GOES-16 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 133.4 |
| 213870e5-eeb8-384d-b141-3e1250209eed | -14.0971 | -51.1134 | 2024-10-09 11:36:26 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 99.3 |
| f1864a82-b213-35fe-ab60-e2e53159ed96 | -14.0778 | -51.116 | 2024-10-09 11:36:26 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 102.4 |
| eba3e523-7b43-3635-8c32-97cc3de28329 | -14.0975 | -51.0918 | 2024-10-09 11:36:26 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 98.3 |
| b1dd52b1-f522-38cc-a1d9-d031db6c8f96 | -16.9094 | -55.8014 | 2024-10-09 11:36:42 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 114.1 |
| d53fda62-8193-3f6c-8642-a285f729c4f5 | -17.1471 | -56.8256 | 2024-10-09 11:36:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 107.1 |
| 84ce8a3d-46f6-3ca8-8f4e-71342f9e5a32 | -6.7798 | -60.0552 | 2024-10-09 11:45:45 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 99.4 |
| b62c006a-b9fc-3a51-8c05-0a214f3ba048 | -10.5746 | -48.0178 | 2024-10-09 11:46:06 | GOES-16 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 88.5 |
| 3ef4aecf-f47e-316b-a632-4b665d83be16 | -12.011 | -51.0531 | 2024-10-09 11:46:14 | GOES-16 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 87.1 |
| d3e99965-524e-3ad4-b8a8-89506e47ec7f | -12.9919 | -46.2359 | 2024-10-09 11:46:19 | GOES-16 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 79.0 |
| 02eff43d-6699-33bf-afa6-c62236c7aa5b | -13.3786 | -61.9582 | 2024-10-09 11:46:23 | GOES-16 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 140.4 |
| e4ed554b-1962-3326-8c7b-7a2a37b4a86e | -13.3976 | -61.957 | 2024-10-09 11:46:23 | GOES-16 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 71.5 |
| d7d9c959-7f40-3c89-8858-5a5520ea6554 | -13.398 | -61.9182 | 2024-10-09 11:46:23 | GOES-16 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 77.1 |
| d9fa4629-5549-3a75-a249-1904ad900bb6 | -14.0971 | -51.1134 | 2024-10-09 11:46:26 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 88.7 |
| 92a6d118-77c3-34f6-b406-32f427657b60 | -14.0778 | -51.116 | 2024-10-09 11:46:26 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 119.1 |
| 2e740eab-4d47-3812-b96c-b53d84be6573 | -14.0975 | -51.0918 | 2024-10-09 11:46:26 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 108.9 |
| 34de04d8-437c-3539-a87d-7bd24ac19e5c | -16.9094 | -55.8014 | 2024-10-09 11:46:42 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 123.7 |
| d4bf5c78-48ae-3212-be41-08747b14a35d | -17.1467 | -56.8463 | 2024-10-09 11:46:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 108.8 |
| 7c916f46-9520-30ec-87e1-14038690d0fb | -17.1471 | -56.8256 | 2024-10-09 11:46:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 138.5 |
| ce4b7328-2c81-36ac-8c80-618ce0ab28c4 | -6.7798 | -60.0552 | 2024-10-09 11:55:45 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 103.0 |
| ffb91d97-92ba-3e9e-bc52-78360574da34 | -10.5746 | -48.0178 | 2024-10-09 11:56:06 | GOES-16 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 103.6 |
| 8e396805-fe9c-35fc-80f0-1ff6aff54ff6 | -11.7749 | -44.5335 | 2024-10-09 11:56:12 | GOES-16 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 86.8 |
| 4fcea1ab-1c96-3e42-8b02-b1289538f5ad | -11.9923 | -51.034 | 2024-10-09 11:56:14 | GOES-16 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 74.4 |
| e3c07073-ed81-327d-ad33-75d42e9964bc | -12.011 | -51.0531 | 2024-10-09 11:56:14 | GOES-16 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 132.4 |
| 11f8680a-1a27-3591-9c38-cffdb50a5b1d | -11.992 | -51.0553 | 2024-10-09 11:56:14 | GOES-16 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 71.2 |
| defe863c-9266-36d3-bf65-9703145fff86 | -12.9919 | -46.2359 | 2024-10-09 11:56:19 | GOES-16 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 127.5 |
| 690f203a-8cdc-30f8-8659-721c170d4ad0 | -13.3976 | -61.957 | 2024-10-09 11:56:23 | GOES-16 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 72.6 |
| 1a7084f2-53a8-31ac-96ea-f428ac317f8f | -13.3786 | -61.9582 | 2024-10-09 11:56:23 | GOES-16 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 106.7 |
| 8736933a-29cb-3996-b0b5-d0058f79c9b0 | -13.398 | -61.9182 | 2024-10-09 11:56:23 | GOES-16 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 87.7 |
| d1e7789e-40ba-3060-b5dd-33fb21020b7c | -13.8963 | -44.5116 | 2024-10-09 11:56:24 | GOES-16 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 135.8 |
| 0a81207e-116c-3e19-a8de-0e3062ca71ef | -13.9158 | -44.5081 | 2024-10-09 11:56:24 | GOES-16 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 79.7 |
| 64e2cb3e-52e6-3dc0-b025-7f2d26988bb0 | -14.0778 | -51.116 | 2024-10-09 11:56:26 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 103.8 |
| bb6ff2e3-aeda-326c-a8dc-c8470aa73222 | -15.6882 | -59.3745 | 2024-10-09 11:56:35 | GOES-16 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 194.4 |
| 5ef728fa-f61c-35ed-bc35-fee6f3d0e130 | -15.7076 | -59.3726 | 2024-10-09 11:56:35 | GOES-16 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 275.1 |
| 322f312e-8927-3017-b697-1fe1dc7d7964 | -17.1467 | -56.8463 | 2024-10-09 11:56:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 114.5 |
| cae2da89-d944-36e8-9a22-e9e55ef7e85a | -7.46342 | -38.76855 | 2024-10-09 12:00:00 | TERRA_M-T | MAURITI | CEARÁ | Brasil | 2308104 | 23 | 33 | nan | nan | nan | Caatinga | 12.5 |
| c11223a8-21f3-328e-83c0-0561ac35b461 | -7.7231 | -37.35192 | 2024-10-09 12:00:00 | TERRA_M-T | INGAZEIRA | PERNAMBUCO | Brasil | 2607109 | 26 | 33 | nan | nan | nan | Caatinga | 13.0 |
| c17ffbd7-332e-3867-a05c-10cb791a536d | -7.72175 | -37.36108 | 2024-10-09 12:00:00 | TERRA_M-T | INGAZEIRA | PERNAMBUCO | Brasil | 2607109 | 26 | 33 | nan | nan | nan | Caatinga | 27.0 |
| dfdb62a5-d87e-3454-b0e3-c2c7ebe2d3df | -7.50435 | -37.77425 | 2024-10-09 12:00:00 | TERRA_M-T | JURU | PARAÍBA | Brasil | 2508000 | 25 | 33 | nan | nan | nan | Caatinga | 20.2 |
| 29779f05-86f9-340a-ae1f-0e88dab99481 | -7.50295 | -37.7838 | 2024-10-09 12:00:00 | TERRA_M-T | JURU | PARAÍBA | Brasil | 2508000 | 25 | 33 | nan | nan | nan | Caatinga | 11.4 |
| ae900e95-d353-331f-8568-952f3bf029b6 | -6.84909 | -42.80962 | 2024-10-09 12:00:00 | TERRA_M-T | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 33.3 |
| 18a39f29-6546-383e-bd33-7d19521fd8db | -6.83951 | -42.80119 | 2024-10-09 12:00:00 | TERRA_M-T | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 32.3 |
| e26e49db-7c68-35e8-bb78-aef424e2d81d | -6.83629 | -42.82204 | 2024-10-09 12:00:00 | TERRA_M-T | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 62.4 |
| 0a6ffddb-9ec2-3bb6-a9ea-09502f52ff13 | -6.83592 | -42.80765 | 2024-10-09 12:00:00 | TERRA_M-T | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 39.7 |
| 72a7aedd-a8ee-3306-a369-f3cd6a602713 | -6.76593 | -37.46386 | 2024-10-09 12:00:00 | TERRA_M-T | SÃO JOSÉ DE ESPINHARAS | PARAÍBA | Brasil | 2514404 | 25 | 33 | nan | nan | nan | Caatinga | 8.5 |
| ce4facb0-36e4-36f1-83fb-8205af0f0a76 | -6.57406 | -37.70389 | 2024-10-09 12:00:00 | TERRA_M-T | PAULISTA | PARAÍBA | Brasil | 2510907 | 25 | 33 | nan | nan | nan | Caatinga | 11.7 |
| 0f4fe5c0-32de-3898-84ae-e55e2b77f297 | -6.56486 | -37.70261 | 2024-10-09 12:00:00 | TERRA_M-T | PAULISTA | PARAÍBA | Brasil | 2510907 | 25 | 33 | nan | nan | nan | Caatinga | 18.8 |
| 367d3e62-75d5-3947-b381-6e1862e93660 | -6.36956 | -37.96902 | 2024-10-09 12:00:00 | TERRA_M-T | ALEXANDRIA | RIO GRANDE DO NORTE | Brasil | 2400505 | 24 | 33 | nan | nan | nan | Caatinga | 8.3 |
| fec4abcf-1dca-3832-ac6d-e6198f3a739b | -6.3681 | -37.97894 | 2024-10-09 12:00:00 | TERRA_M-T | ALEXANDRIA | RIO GRANDE DO NORTE | Brasil | 2400505 | 24 | 33 | nan | nan | nan | Caatinga | 9.6 |
| 3760864c-a228-3b49-9941-7bd192734d4b | -6.3061 | -41.84129 | 2024-10-09 12:00:00 | TERRA_M-T | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 23.7 |
| 74371d70-9f86-34d2-88a6-b4fd970ba353 | -5.84309 | -38.02399 | 2024-10-09 12:00:00 | TERRA_M-T | RODOLFO FERNANDES | RIO GRANDE DO NORTE | Brasil | 2411007 | 24 | 33 | nan | nan | nan | Caatinga | 21.6 |
| 50867b1a-64e9-3865-8f9a-0e478afe1c1e | -3.86865 | -40.79077 | 2024-10-09 12:00:00 | TERRA_M-T | MUCAMBO | CEARÁ | Brasil | 2309003 | 23 | 33 | nan | nan | nan | Caatinga | 15.9 |
| a6f26834-66ae-3e47-a32c-e98214e276ee | -7.34529 | -37.78406 | 2024-10-09 12:00:00 | TERRA_M-T | OLHO D'ÁGUA | PARAÍBA | Brasil | 2510402 | 25 | 33 | nan | nan | nan | Caatinga | 10.3 |
| 5ffb2185-70fb-371c-8a0b-9e56176bdcfa | -3.82455 | -41.59674 | 2024-10-09 12:00:00 | TERRA_M-T | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 138.6 |
| 0c6869f2-b80b-39b8-8c68-a48e1d807c7e | -3.82162 | -41.61573 | 2024-10-09 12:00:00 | TERRA_M-T | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 73.0 |
| 55cd3e64-f690-39f6-a781-573fbe951dd3 | -3.82095 | -41.6096 | 2024-10-09 12:00:00 | TERRA_M-T | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 157.3 |
| f0dd9554-e912-3323-96dc-66bbd12c15bc | -8.61973 | -41.45825 | 2024-10-09 12:00:00 | TERRA_M-T | QUEIMADA NOVA | PIAUÍ | Brasil | 2208650 | 22 | 33 | nan | nan | nan | Caatinga | 22.0 |
| 2171b7e2-47ad-3300-ac18-12509bf63ac3 | -8.87105 | -40.97068 | 2024-10-09 12:00:00 | TERRA_M-T | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 29.8 |
| a1fa6454-edaf-311d-a696-08c7b07b8c2b | -8.86951 | -40.96423 | 2024-10-09 12:00:00 | TERRA_M-T | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 14.3 |
| 431e1adc-ee9c-34cb-874d-ac81c8d5f60d | -8.86881 | -40.98462 | 2024-10-09 12:00:00 | TERRA_M-T | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 16.8 |
| dd31c6bf-afc2-39ee-a5a1-4cf428a2ff31 | -8.86735 | -40.97831 | 2024-10-09 12:00:00 | TERRA_M-T | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 51.1 |
| e3bcc730-e127-3bd7-814f-f7b23caa7a50 | -8.83452 | -40.97301 | 2024-10-09 12:00:00 | TERRA_M-T | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 54.7 |
| 1b569081-bd0b-3fe9-b199-04444b6f2ce1 | -8.80743 | -36.81161 | 2024-10-09 12:00:00 | TERRA_M-T | PEDRA | PERNAMBUCO | Brasil | 2610806 | 26 | 33 | nan | nan | nan | Caatinga | 8.1 |
| 90b5017d-4944-32de-8be4-65411f6ec914 | -8.80613 | -36.82055 | 2024-10-09 12:00:00 | TERRA_M-T | PEDRA | PERNAMBUCO | Brasil | 2610806 | 26 | 33 | nan | nan | nan | Caatinga | 11.0 |
| fad6fac0-ecac-36d2-b291-5a286dadadb2 | -8.73905 | -40.92309 | 2024-10-09 12:00:00 | TERRA_M-T | AFRÂNIO | PERNAMBUCO | Brasil | 2600203 | 26 | 33 | nan | nan | nan | Caatinga | 17.8 |
| 24760e37-5c32-3b10-a1ea-4ba487cb788c | -8.62212 | -41.44341 | 2024-10-09 12:00:00 | TERRA_M-T | QUEIMADA NOVA | PIAUÍ | Brasil | 2208650 | 22 | 33 | nan | nan | nan | Caatinga | 27.0 |
| fec4b181-c670-3d78-b61a-574396005476 | -8.62191 | -41.45281 | 2024-10-09 12:00:00 | TERRA_M-T | QUEIMADA NOVA | PIAUÍ | Brasil | 2208650 | 22 | 33 | nan | nan | nan | Caatinga | 33.1 |
| f9458625-ee0e-3e0a-a773-3f1318cb0cf4 | -8.50283 | -39.93573 | 2024-10-09 12:00:00 | TERRA_M-T | SANTA MARIA DA BOA VISTA | PERNAMBUCO | Brasil | 2612604 | 26 | 33 | nan | nan | nan | Caatinga | 40.9 |
| e217d772-c5a6-3486-b823-fab08e4a3fa0 | -8.4904 | -39.89088 | 2024-10-09 12:00:00 | TERRA_M-T | SANTA MARIA DA BOA VISTA | PERNAMBUCO | Brasil | 2612604 | 26 | 33 | nan | nan | nan | Caatinga | 24.5 |
| 5c220a8b-d60d-38fd-b514-6a65e0ceff66 | -8.48994 | -39.8847 | 2024-10-09 12:00:00 | TERRA_M-T | SANTA MARIA DA BOA VISTA | PERNAMBUCO | Brasil | 2612604 | 26 | 33 | nan | nan | nan | Caatinga | 13.2 |
| 6806aaa8-2d49-3a19-91be-e7d56e71af34 | -8.48807 | -39.89666 | 2024-10-09 12:00:00 | TERRA_M-T | SANTA MARIA DA BOA VISTA | PERNAMBUCO | Brasil | 2612604 | 26 | 33 | nan | nan | nan | Caatinga | 10.6 |
| 3e4525ec-83d7-3a79-b451-8ac43b583097 | -8.3493 | -44.09916 | 2024-10-09 12:00:00 | TERRA_M-T | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 54.3 |
| 755f8463-633f-35b2-94e4-4d5b3b3af4c3 | -8.34526 | -44.12403 | 2024-10-09 12:00:00 | TERRA_M-T | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 41.2 |
| 6363fc10-cda8-3117-8d9a-5187ef8ce3d1 | -8.33511 | -44.09698 | 2024-10-09 12:00:00 | TERRA_M-T | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 134.5 |
| 56103b24-d498-373e-9c67-bf39f42e2b05 | -8.32083 | -44.09528 | 2024-10-09 12:00:00 | TERRA_M-T | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 300.2 |
| ed410f0e-0826-36f8-b099-e7f81dd1d982 | -8.29372 | -38.54226 | 2024-10-09 12:00:00 | TERRA_M-T | FLORESTA | PERNAMBUCO | Brasil | 2605707 | 26 | 33 | nan | nan | nan | Caatinga | 7.7 |
| 83655d1b-affc-30bb-b426-32356bd7ec8f | -8.29221 | -38.55234 | 2024-10-09 12:00:00 | TERRA_M-T | CARNAUBEIRA DA PENHA | PERNAMBUCO | Brasil | 2603926 | 26 | 33 | nan | nan | nan | Caatinga | 7.3 |
| d466cd3a-0d68-3b9f-a0a4-b94400d9e249 | -8.12924 | -44.42772 | 2024-10-09 12:00:00 | TERRA_M-T | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 35.5 |
| 9a24ce0a-7ea2-3312-a9f1-4e6d9f9c966a | -8.12832 | -44.42109 | 2024-10-09 12:00:00 | TERRA_M-T | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 42.5 |
| 2a3b5275-4144-3560-9c0e-a0e3dd21f035 | -7.82942 | -37.94393 | 2024-10-09 12:00:00 | TERRA_M-T | FLORES | PERNAMBUCO | Brasil | 2605608 | 26 | 33 | nan | nan | nan | Caatinga | 12.5 |
| 8983d6d8-c783-34d7-b236-4a943025245c | -7.82453 | -37.66301 | 2024-10-09 12:00:00 | TERRA_M-T | AFOGADOS DA INGAZEIRA | PERNAMBUCO | Brasil | 2600104 | 26 | 33 | nan | nan | nan | Caatinga | 6.8 |
| e19c0c34-1869-38b2-baf2-d0f01c87a972 | -7.7912 | -43.08624 | 2024-10-09 12:00:00 | TERRA_M-T | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 27.7 |
| 6ece944b-bf59-369b-91b3-7d71a8edb366 | -7.78975 | -37.14707 | 2024-10-09 12:00:00 | TERRA_M-T | MONTEIRO | PARAÍBA | Brasil | 2509701 | 25 | 33 | nan | nan | nan | Caatinga | 22.9 |
| caa928c9-ecca-3772-9e64-9bb389227ff2 | -7.78842 | -37.15619 | 2024-10-09 12:00:00 | TERRA_M-T | TUPARETAMA | PERNAMBUCO | Brasil | 2615904 | 26 | 33 | nan | nan | nan | Caatinga | 15.2 |
| 18d9b0ba-e4c4-3c6c-9ff9-72942f19a3cb | -7.78738 | -43.09175 | 2024-10-09 12:00:00 | TERRA_M-T | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 23.7 |
| ac1b098e-efd4-3e4b-82c9-80c53ea1168c | -7.67089 | -42.51775 | 2024-10-09 12:00:00 | TERRA_M-T | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 29.1 |
| dd897e7e-14aa-3878-a86f-8777859dc261 | -7.65827 | -42.51556 | 2024-10-09 12:00:00 | TERRA_M-T | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 23.5 |
| 3a10f787-0b75-3b8f-adc0-d84034fb4dcb | -7.25611 | -39.85496 | 2024-10-09 12:00:00 | TERRA_M-T | SANTANA DO CARIRI | CEARÁ | Brasil | 2312106 | 23 | 33 | nan | nan | nan | Caatinga | 38.3 |


[Clique aqui para ver as próximas entradas](README230.md)
