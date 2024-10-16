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
| 6cb5caff-d226-361c-b2f6-be7252e4f635 | -9.13963 | -69.14091 | 2024-10-16 06:14:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5ba24df0-1a01-37ff-ab31-8c720d9c27f9 | -9.02849 | -69.24586 | 2024-10-16 06:14:00 | NOAA-20 | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a13fb0b9-22d1-3bd5-a5f1-aa2288a6b89d | -10.88708 | -69.39492 | 2024-10-16 06:14:00 | NOAA-20 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d1770d50-8cb5-30f1-a457-e60b5ef6c574 | -10.88469 | -69.39238 | 2024-10-16 06:14:00 | NOAA-20 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e7af2915-4384-3db6-9c42-62bfcb8bcfe9 | -10.88394 | -69.39754 | 2024-10-16 06:14:00 | NOAA-20 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 404e3c2b-d0b6-32ba-940e-c82c7e84801b | -10.88311 | -69.39434 | 2024-10-16 06:14:00 | NOAA-20 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c3ddd591-a777-3c22-b85b-05211b99d256 | -10.88097 | -69.4099 | 2024-10-16 06:14:00 | NOAA-20 | ASSIS BRASIL | ACRE | Brasil | 1200054 | 12 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 48e0b0dc-9a67-36d8-ad5a-3055c8669ef4 | -10.8799 | -69.28434 | 2024-10-16 06:14:00 | NOAA-20 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a5a1a60c-63f5-31de-8b59-899d214b3ba4 | -10.8765 | -69.72952 | 2024-10-16 06:14:00 | NOAA-20 | ASSIS BRASIL | ACRE | Brasil | 1200054 | 12 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d4de94cb-1017-3ce4-ba43-afbc45812b2f | -10.8708 | -69.43253 | 2024-10-16 06:14:00 | NOAA-20 | ASSIS BRASIL | ACRE | Brasil | 1200054 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4eb986a6-adaa-35c9-bec4-c0913c6935cc | -10.87021 | -69.4294 | 2024-10-16 06:14:00 | NOAA-20 | ASSIS BRASIL | ACRE | Brasil | 1200054 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| dada458a-cdd1-36af-b8a9-0b82afe48076 | -10.86684 | -69.43195 | 2024-10-16 06:14:00 | NOAA-20 | ASSIS BRASIL | ACRE | Brasil | 1200054 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d1e6117b-0b03-3560-9031-95856490d4d6 | -10.70953 | -69.43878 | 2024-10-16 06:14:00 | NOAA-20 | ASSIS BRASIL | ACRE | Brasil | 1200054 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bd22e870-d9d1-3dba-81ac-cef80e6c83b9 | -10.68866 | -69.35698 | 2024-10-16 06:14:00 | NOAA-20 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b68a3a23-be74-3a0a-92e6-6a1017ef6f77 | -10.68337 | -69.53894 | 2024-10-16 06:14:00 | NOAA-20 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5c0b3840-3f8b-3a36-b441-d56a9d136c85 | -10.67973 | -69.45023 | 2024-10-16 06:14:00 | NOAA-20 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 51eb5c39-7859-3843-90ce-786a6ce94da3 | -10.66214 | -69.63306 | 2024-10-16 06:14:00 | NOAA-20 | ASSIS BRASIL | ACRE | Brasil | 1200054 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0af72706-e5a0-399d-a5b6-598253f8004e | -10.57246 | -69.32821 | 2024-10-16 06:14:00 | NOAA-20 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0a017cbb-291f-3e0c-8c3c-32c7eb3f8c0b | -10.56947 | -69.33131 | 2024-10-16 06:14:00 | NOAA-20 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 846cf0b9-6617-3998-b3c0-2ff48b98cf63 | -10.56849 | -69.32763 | 2024-10-16 06:14:00 | NOAA-20 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d935bcb1-b286-37f3-8510-3b1ad3d129ec | -10.55551 | -69.17353 | 2024-10-16 06:14:00 | NOAA-20 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| bad21410-ac92-30b0-a699-f219ca65db5a | -10.51349 | -69.3549 | 2024-10-16 06:14:00 | NOAA-20 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f52178ce-4ad2-34a6-aa20-cc410f73bf70 | -10.47926 | -69.25201 | 2024-10-16 06:14:00 | NOAA-20 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 2.1 |
| cde0a570-71ee-358e-b2a9-24f57f454ba9 | -10.47684 | -69.25219 | 2024-10-16 06:14:00 | NOAA-20 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c98f2b78-d2d0-37a8-8924-defd8959d5b2 | -10.46953 | -69.21839 | 2024-10-16 06:14:00 | NOAA-20 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7d6e9455-3fe1-3b85-aa54-c5abba458e99 | -10.46224 | -69.25761 | 2024-10-16 06:14:00 | NOAA-20 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 09b74c2a-2a14-3d4d-a4a9-9069a2776c26 | -10.46015 | -69.25515 | 2024-10-16 06:14:00 | NOAA-20 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 1.7 |
| adcf0116-fc9e-3aa7-824a-ee18b95520ff | -10.44942 | -69.30138 | 2024-10-16 06:14:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f9ca8ddb-a682-3dfd-8ef3-bdf3a8e0292f | -10.32455 | -69.47372 | 2024-10-16 06:14:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f2e83363-1f1e-3545-ae5b-641a1f72185b | -10.32417 | -69.47554 | 2024-10-16 06:14:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fc0abd00-1c2f-3cd0-a5a9-85925f37fdd2 | -10.14962 | -69.32242 | 2024-10-16 06:14:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0d97ff31-7e0b-3481-b166-ca5d9eb4ca51 | -10.11576 | -69.17094 | 2024-10-16 06:14:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5906acb4-3df7-3990-b107-4985f63e51f1 | -10.11178 | -69.17033 | 2024-10-16 06:14:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 50d80b37-65a6-3347-b3bc-5c39208ba14c | -9.57711 | -68.98956 | 2024-10-16 06:14:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bc464c3a-775a-3e4b-956c-162899fbd431 | -10.90553 | -69.63689 | 2024-10-16 06:14:00 | NOAA-20 | ASSIS BRASIL | ACRE | Brasil | 1200054 | 12 | 33 | nan | nan | nan | Amazônia | 13.9 |
| 6d38ceeb-65c1-3da4-aa7b-31ba2db2e061 | -10.90482 | -69.64191 | 2024-10-16 06:14:00 | NOAA-20 | ASSIS BRASIL | ACRE | Brasil | 1200054 | 12 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 99f19c59-04de-37a9-b56c-a4da79aaaedd | -10.90162 | -69.63635 | 2024-10-16 06:14:00 | NOAA-20 | ASSIS BRASIL | ACRE | Brasil | 1200054 | 12 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 97be862e-8ede-3886-a82f-442c3dbc0661 | -10.90091 | -69.64137 | 2024-10-16 06:14:00 | NOAA-20 | ASSIS BRASIL | ACRE | Brasil | 1200054 | 12 | 33 | nan | nan | nan | Amazônia | 5.2 |
| e670ac0e-4c67-3b3e-bd29-51f71977b902 | -9.12666 | -70.78416 | 2024-10-16 06:14:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b6121a16-e9f3-3101-ab1f-c9afa1114e2b | -9.12604 | -70.7883 | 2024-10-16 06:14:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 646142ae-6e2e-3957-93e8-eca2413e407b | -9.12246 | -70.78777 | 2024-10-16 06:14:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c5d4837b-601b-358c-975c-9609140e3d19 | -8.86606 | -70.90693 | 2024-10-16 06:14:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5ecc45b9-3262-30e3-be66-8e9ee6a308ea | -8.80625 | -71.09087 | 2024-10-16 06:14:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 864402b4-2fae-3303-bf26-fef13e75cd66 | -8.69491 | -71.03838 | 2024-10-16 06:14:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c2454dec-172a-3bf2-b93f-050294f5391c | -8.69448 | -71.03896 | 2024-10-16 06:14:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 563bedb0-5675-3752-b015-50bade437a95 | -8.59437 | -70.47253 | 2024-10-16 06:14:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| cfaec6b2-c7a4-3065-bdb3-d83310503703 | -8.51928 | -70.85776 | 2024-10-16 06:14:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 64229314-993c-3231-9d42-5c7c77b2515d | -9.42653 | -71.88385 | 2024-10-16 06:14:00 | NOAA-20 | JORDÃO | ACRE | Brasil | 1200328 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 52e6368e-3c5f-3a61-a4b8-3bc446959564 | -9.42595 | -71.88763 | 2024-10-16 06:14:00 | NOAA-20 | JORDÃO | ACRE | Brasil | 1200328 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e0e76846-a591-3ff2-b6c9-eec9a538d2d9 | -8.1826 | -72.92717 | 2024-10-16 06:14:00 | NOAA-20 | CRUZEIRO DO SUL | ACRE | Brasil | 1200203 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9c54de20-748e-340d-83fd-1d5a10b3a0f5 | -19.6013 | -56.9834 | 2024-10-16 07:36:56 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 60.6 |
| 36e92d17-3725-3a05-b24e-9d825108ce14 | -19.5816 | -56.9653 | 2024-10-16 07:56:56 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 58.9 |
| 9f856b0e-d133-3010-8713-9267000529d4 | -19.6013 | -56.9834 | 2024-10-16 07:56:56 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 67.6 |
| 9c60a492-b089-3942-9b64-009f8f6c4048 | -19.6016 | -56.9625 | 2024-10-16 07:56:56 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 61.9 |
| 1c7c47df-fa50-3413-a28f-03e78757b855 | -15.9258 | -56.3131 | 2024-10-16 08:06:36 | GOES-16 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 61.9 |
| 3ac2c84c-a378-3243-824a-8c0f5c07a594 | -19.6016 | -56.9625 | 2024-10-16 08:06:56 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 58.9 |
| 49b88533-2ec1-30f5-bff6-65c65fdf18f0 | -19.5816 | -56.9653 | 2024-10-16 08:06:56 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 61.7 |
| a5bfc5aa-a452-32f9-8435-135e1cf8cad8 | -19.5816 | -56.9653 | 2024-10-16 08:16:56 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 80.9 |
| d141d6a2-df64-3cdc-b9a0-bcfff157570d | -19.5816 | -56.9653 | 2024-10-16 08:26:56 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 72.1 |
| 2c8ba11c-5739-3399-a869-3a6c07558dea | -19.6016 | -56.9625 | 2024-10-16 08:36:56 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 77.4 |
| 1442c0a7-23fe-3a66-8f68-42ea52d9b25f | -19.5816 | -56.9653 | 2024-10-16 08:36:56 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 85.9 |
| 9180de44-1975-3a22-9665-578ce4ba9beb | -19.5816 | -56.9653 | 2024-10-16 11:26:56 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 122.9 |
| d33a78cc-4e84-3322-af04-9a8bd5f0761b | -19.5816 | -56.9653 | 2024-10-16 11:36:56 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 120.5 |
| eb19ec85-da69-3829-abab-5b84bbc0defd | -6.36302 | -38.14946 | 2024-10-16 11:45:00 | TERRA_M-M | MARCELINO VIEIRA | RIO GRANDE DO NORTE | Brasil | 2407302 | 24 | 33 | nan | nan | nan | Caatinga | 28.5 |
| 428b3c26-3553-3f13-a277-84886c6213ce | -6.65305 | -37.4486 | 2024-10-16 11:45:00 | TERRA_M-M | SERRA NEGRA DO NORTE | RIO GRANDE DO NORTE | Brasil | 2413409 | 24 | 33 | nan | nan | nan | Caatinga | 14.8 |
| c98777d3-2fe6-3d92-b0d2-42f7eb437a43 | -19.5816 | -56.9653 | 2024-10-16 11:46:56 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 155.9 |
| 8eb86847-6f8e-3dd6-b9a5-2f565c80d030 | -19.6013 | -56.9834 | 2024-10-16 11:46:56 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 180.6 |
| ec60c323-377b-388c-b154-aba6b530bfcc | -19.6016 | -56.9625 | 2024-10-16 11:46:56 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 198.7 |
| afac1574-ec56-348a-9a0b-b12570316a3b | -7.45237 | -37.26628 | 2024-10-16 11:47:00 | TERRA_M-M | SÃO JOSÉ DO EGITO | PERNAMBUCO | Brasil | 2613602 | 26 | 33 | nan | nan | nan | Caatinga | 23.0 |
| b0d803b8-7542-3cf7-a594-a12f67183c52 | -7.45456 | -37.25225 | 2024-10-16 11:47:00 | TERRA_M-M | SÃO JOSÉ DO EGITO | PERNAMBUCO | Brasil | 2613602 | 26 | 33 | nan | nan | nan | Caatinga | 24.6 |
| 3740b6e8-23d6-3cbd-b81c-2d789e7a006e | -7.96697 | -38.01901 | 2024-10-16 11:47:00 | TERRA_M-M | FLORES | PERNAMBUCO | Brasil | 2605608 | 26 | 33 | nan | nan | nan | Caatinga | 12.6 |
| 7792e2ec-205d-3deb-a544-41e869b3bf1d | -7.53865 | -36.99587 | 2024-10-16 11:47:00 | TERRA_M-M | AMPARO | PARAÍBA | Brasil | 2500734 | 25 | 33 | nan | nan | nan | Caatinga | 12.5 |
| ab52cc3f-e628-3926-b5fe-28217e2e25a9 | -19.07598 | -40.56195 | 2024-10-16 11:49:00 | TERRA_M-M | SÃO DOMINGOS DO NORTE | ESPÍRITO SANTO | Brasil | 3204658 | 32 | 33 | nan | nan | nan | Mata Atlântica | 21.0 |
| 0ee840e2-8f0f-3ae3-9ced-8510c42bee87 | -19.6013 | -56.9834 | 2024-10-16 11:56:56 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 471.9 |
| 38079cdf-0b47-3017-8260-0f630d71f6a6 | -19.5816 | -56.9653 | 2024-10-16 11:56:56 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 377.1 |
| 82b1ba66-68fc-30de-8d77-29303b28e26b | -19.5812 | -56.9862 | 2024-10-16 11:56:56 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 244.9 |
| db45a060-2669-3c34-9f25-fb51b4fc0c21 | -21.0091 | -55.2249 | 2024-10-16 11:57:03 | GOES-16 | DOIS IRMÃOS DO BURITI | MATO GROSSO DO SUL | Brasil | 5003488 | 50 | 33 | nan | nan | nan | Cerrado | 120.9 |
| cfb39aa0-8d2c-368e-b6b9-7175d9be074b | -18.2383 | -56.3763 | 2024-10-16 12:06:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 131.8 |
| 0447d3b3-4049-3bdc-b419-0db228718819 | -19.6013 | -56.9834 | 2024-10-16 12:06:56 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 532.4 |
| 6470c4b6-ad3e-323d-93d7-61a4f9cb7b2e | -19.5819 | -56.9443 | 2024-10-16 12:06:56 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 142.4 |
| b087de8b-1665-3920-b679-9c557e07cb67 | -19.602 | -56.9415 | 2024-10-16 12:06:56 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 149.1 |
| 29d66856-4ed5-3eb0-8bdc-b9d82df4bb26 | -19.5812 | -56.9862 | 2024-10-16 12:06:56 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 262.1 |
| 6bca7379-c79b-398e-ba94-57c185377ede | -19.5816 | -56.9653 | 2024-10-16 12:06:56 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 498.4 |
| f803a1f6-1718-3afe-9c53-744272779994 | -21.0091 | -55.2249 | 2024-10-16 12:07:03 | GOES-16 | DOIS IRMÃOS DO BURITI | MATO GROSSO DO SUL | Brasil | 5003488 | 50 | 33 | nan | nan | nan | Cerrado | 105.2 |
| 82ad7990-1c71-3c5f-89d4-713bf1029204 | -18.2383 | -56.3763 | 2024-10-16 12:16:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 145.0 |
| b70213fc-d231-30f4-89a9-25c941d3dc5b | -21.0091 | -55.2249 | 2024-10-16 12:17:03 | GOES-16 | DOIS IRMÃOS DO BURITI | MATO GROSSO DO SUL | Brasil | 5003488 | 50 | 33 | nan | nan | nan | Cerrado | 101.7 |
| 4ca10b2b-e219-36f5-92b7-64276acf2b2a | -18.2383 | -56.3763 | 2024-10-16 12:26:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 151.4 |
| 3933a78d-060e-35db-ac86-46e617b762dd | -18.2184 | -56.379 | 2024-10-16 12:36:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 148.4 |
| 0aee11ec-97be-3900-8b3e-15bac2574b85 | -18.2383 | -56.3763 | 2024-10-16 12:36:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 190.3 |
| 889443a7-beaa-3118-8ef1-ea7b01683fdf | -18.2379 | -56.3972 | 2024-10-16 12:36:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 132.4 |
| 91e0373d-45b6-3138-bf8f-f36dfd0c7587 | -18.2184 | -56.379 | 2024-10-16 12:46:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 194.2 |
| 2d4cec26-3417-3a05-9814-05d4c1b8e67b | -18.218 | -56.3998 | 2024-10-16 12:46:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 114.9 |
| 34d07a23-62d1-3440-be7d-1441e06a5db8 | -18.2379 | -56.3972 | 2024-10-16 12:46:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 160.4 |
| f1436a77-7194-3f6f-bfb5-5fb2c81075ae | -19.6 | -56.96 | 2024-10-16 13:03:35 | MSG-03 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 6f7656c8-8a41-370b-8fe7-22bda9c5eee2 | -18.218 | -56.3998 | 2024-10-16 13:06:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 130.5 |
| 6369c162-18c2-3fc7-85a8-25ae528f80c6 | -18.2577 | -56.3946 | 2024-10-16 13:06:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 151.3 |
| e702df64-4b2e-34cf-bd9a-dc344db0f51b | -18.2379 | -56.3972 | 2024-10-16 13:06:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 189.9 |
| 9ee858b1-773a-3bfe-80d2-58cb364b612d | -0.766 | -48.7042 | 2024-10-16 13:15:10 | GOES-16 | SALVATERRA | PARÁ | Brasil | 1506302 | 15 | 33 | nan | nan | nan | Amazônia | 77.3 |
| ee2a4beb-534e-37f0-ab64-e4ab4f689e41 | -0.8583 | -48.7248 | 2024-10-16 13:15:11 | GOES-16 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 66.9 |
| 64fdadd0-e9ae-3f0c-ae3e-de870180106a | -1.1346 | -49.1698 | 2024-10-16 13:15:12 | GOES-16 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 69.5 |


[Clique aqui para ver as próximas entradas](README75.md)
