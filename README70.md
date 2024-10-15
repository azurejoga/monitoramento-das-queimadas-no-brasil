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

## Dados Diários - Página 70

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 39f6ae20-fe17-3c89-b238-0ce3470062fa | -12.44728 | -63.03376 | 2024-10-15 04:51:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3c82e692-6963-3f06-97b8-30283936bb88 | -12.44147 | -63.0359 | 2024-10-15 04:51:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| da121069-7b05-3fe1-89f0-f6d32c99a63d | -12.95982 | -62.79892 | 2024-10-15 04:51:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1c9ad136-2154-3524-b352-8393742ee050 | -12.66013 | -63.0821 | 2024-10-15 04:51:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d2af2e19-ae50-3cd5-be3e-118893e1d40b | -12.6589 | -63.08857 | 2024-10-15 04:51:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 21fb4f45-d49d-377d-a8c0-21b719289254 | -12.65371 | -63.08753 | 2024-10-15 04:51:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 273b822a-3bbc-38af-aa84-7b7d78c75d2d | -12.52198 | -63.2691 | 2024-10-15 04:51:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b94bce74-ac03-3702-94d1-af74eb2be322 | -12.5214 | -63.2655 | 2024-10-15 04:51:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8a95da1d-e1a5-349c-aaeb-7fb0afeeb553 | -12.52074 | -63.26883 | 2024-10-15 04:51:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| bc4360e3-af10-390b-9eb0-069333242cca | -12.51671 | -63.26802 | 2024-10-15 04:51:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 88a129fa-eda6-323e-a1eb-34fcc4346707 | -12.51608 | -63.27136 | 2024-10-15 04:51:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e47fb370-3ebc-3aba-84cb-f97898b08f9e | -12.50953 | -63.27698 | 2024-10-15 04:51:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 3707e30e-8ac6-3a17-8f53-6f1b1db4df5c | -12.46161 | -62.98636 | 2024-10-15 04:51:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 31348860-aa32-3dc5-89ea-8b0c5522f901 | -12.45981 | -63.02758 | 2024-10-15 04:51:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 4.1 |
| ffe114d9-a06d-3ce1-b6e4-c358501e3d84 | -12.45917 | -63.0308 | 2024-10-15 04:51:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 5bbb8bc4-9002-3676-98c2-d8a897a6a17d | -12.45583 | -62.98851 | 2024-10-15 04:51:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| d3fa8d5c-07a1-3221-9d37-b0c0328f2be5 | -12.45491 | -63.02192 | 2024-10-15 04:51:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5a049453-b687-303a-9ffe-985f15270aac | -12.45247 | -63.03485 | 2024-10-15 04:51:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9cd7672f-c423-3981-8839-98943b98d2f3 | -12.44789 | -63.03053 | 2024-10-15 04:51:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 240e18b8-c2b8-3387-b151-0ffce58866a0 | -9.35079 | -63.58165 | 2024-10-15 04:51:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ded995c1-097a-3fde-b987-7de3675a33bb | -9.34971 | -63.57742 | 2024-10-15 04:51:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 295b71e2-2ede-33cd-b1b8-5f53ea829b48 | -9.34899 | -63.58137 | 2024-10-15 04:51:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7f88e571-9bb5-3bd0-999f-7bcbb435fec5 | -9.34586 | -63.57655 | 2024-10-15 04:51:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| d08a552b-c1ef-3d7e-9c28-f255ef401da1 | -9.34511 | -63.58049 | 2024-10-15 04:51:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 88f00767-9809-35b5-9081-7795f13dde75 | -19.55077 | -56.98122 | 2024-10-15 04:53:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 0599c56c-e9e4-3456-8b73-a87d0984a77e | -19.55015 | -56.98499 | 2024-10-15 04:53:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 73716fc9-3173-34a0-8cf7-15d58b692e1d | -20.38615 | -54.85924 | 2024-10-15 04:53:00 | NOAA-20 | TERENOS | MATO GROSSO DO SUL | Brasil | 5008008 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8121c616-8563-32ac-b6aa-4b44300c532b | -21.88388 | -50.50233 | 2024-10-15 04:53:00 | NOAA-20 | TUPÃ | SÃO PAULO | Brasil | 3555000 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| cd4510f3-fb8d-36b4-b659-0b4b69b28b61 | -21.88222 | -50.50142 | 2024-10-15 04:53:00 | NOAA-20 | TUPÃ | SÃO PAULO | Brasil | 3555000 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| c63b1f04-e08d-3097-bb0c-fbfbf8045500 | -21.87975 | -50.50172 | 2024-10-15 04:53:00 | NOAA-20 | TUPÃ | SÃO PAULO | Brasil | 3555000 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| c3347040-00da-33d6-9344-b3d6b88d6285 | -24.24311 | -50.74142 | 2024-10-15 04:53:00 | NOAA-20 | ORTIGUEIRA | PARANÁ | Brasil | 4117305 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 9fc0847c-0715-3fa6-b4ce-d6474febd496 | -19.54617 | -56.98813 | 2024-10-15 04:53:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.0 |
| c0731fa9-4995-39e3-b356-997212fe3d0f | -19.54555 | -56.9919 | 2024-10-15 04:53:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.7 |
| 57d03208-0123-3718-8cb6-22f16732a60f | -19.54406 | -56.97999 | 2024-10-15 04:53:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.4 |
| 45bfb3c4-c445-35ef-a937-70020c0387c5 | -22.77854 | -54.40749 | 2024-10-15 04:53:00 | NOAA-20 | JUTI | MATO GROSSO DO SUL | Brasil | 5005152 | 50 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 62c80e64-5694-3344-975c-5fc5cdaaa140 | -19.54344 | -56.98376 | 2024-10-15 04:53:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.0 |
| 52cb3fcb-bf84-300b-9677-7a2c49066553 | -19.54952 | -56.98875 | 2024-10-15 04:53:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 5e292273-be61-3236-a134-39b1a712bdec | -19.54741 | -56.98061 | 2024-10-15 04:53:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.4 |
| bf26c926-c446-3aba-a9dd-bc66f51409b5 | -19.54679 | -56.98437 | 2024-10-15 04:53:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.0 |
| 3924e6a0-9a27-3107-ac6f-eccd5b61c779 | -19.54281 | -56.98752 | 2024-10-15 04:53:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.0 |
| d28e020b-89bc-3e8a-843e-159fa5e52078 | -19.54242 | -56.98034 | 2024-10-15 04:53:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 1fb60549-2c4a-3df8-933f-840f26f9fe2f | -19.54181 | -56.9841 | 2024-10-15 04:53:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.3 |
| cdd856fe-dba6-325a-b025-c7d99c996bec | -19.54119 | -56.98787 | 2024-10-15 04:53:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.3 |
| f08595db-b198-3c9d-8b75-a52112eae7b5 | 1.0016 | -52.2164 | 2024-10-15 04:54:59 | GOES-16 | PEDRA BRANCA DO AMAPARI | AMAPÁ | Brasil | 1600154 | 16 | 33 | nan | nan | nan | Amazônia | 80.0 |
| fbbf0fe9-d084-3e3f-9c67-2a59efb2429a | -3.1283 | -54.2259 | 2024-10-15 04:55:22 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 33.8 |
| 540e4549-411c-3430-a98b-45b4821c92ab | -3.1099 | -54.2263 | 2024-10-15 04:55:22 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 36.5 |
| 45ba8edb-0ae5-34f1-96d2-d2a8714328c0 | -3.9267 | -42.401 | 2024-10-15 04:55:26 | GOES-16 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 184.3 |
| 96b557b2-8c97-3ae8-824d-53e8259ea257 | -3.9265 | -42.4246 | 2024-10-15 04:55:26 | GOES-16 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 75.1 |
| 50e0d514-07a1-3f7b-b7ee-a318481f05f2 | -3.908 | -42.402 | 2024-10-15 04:55:26 | GOES-16 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 97.2 |
| 2e737f8d-250c-30ed-9faa-7fdffb2551fe | -3.9103 | -48.3466 | 2024-10-15 04:55:27 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 63.9 |
| 9c2deb71-91ba-3b4b-9dcb-1b03ffe73916 | -3.9289 | -48.3458 | 2024-10-15 04:55:27 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 65.5 |
| 5819d99d-4522-33f9-9da6-6aac5495071d | -6.5691 | -48.2395 | 2024-10-15 04:55:42 | GOES-16 | PIRAQUÊ | TOCANTINS | Brasil | 1717206 | 17 | 33 | nan | nan | nan | Amazônia | 197.7 |
| 36b68d46-7723-3ca4-a981-823bdc28a193 | -6.5693 | -48.2178 | 2024-10-15 04:55:42 | GOES-16 | PIRAQUÊ | TOCANTINS | Brasil | 1717206 | 17 | 33 | nan | nan | nan | Amazônia | 84.2 |
| 137894fd-71f9-352a-ad40-14d6d723c60d | -6.5878 | -48.2381 | 2024-10-15 04:55:42 | GOES-16 | PIRAQUÊ | TOCANTINS | Brasil | 1717206 | 17 | 33 | nan | nan | nan | Amazônia | 90.0 |
| cb665f06-0170-35fd-aa19-440722930679 | -10.3711 | -61.1935 | 2024-10-15 04:56:04 | GOES-16 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 91.0 |
| 9f6877fd-4921-38c6-bda7-9b95343a0508 | -10.3713 | -61.1743 | 2024-10-15 04:56:04 | GOES-16 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 79.8 |
| a5024db1-bacb-3c95-ae02-5f20e523fb69 | -11.6915 | -65.2432 | 2024-10-15 04:56:11 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 44.7 |
| f655040b-ee25-39f3-a30e-8ec2a0cccfd3 | -11.6917 | -65.2243 | 2024-10-15 04:56:11 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 55.1 |
| 5ad2e67c-0c31-3c5a-8826-5ac9136e5dc6 | -12.515 | -63.263 | 2024-10-15 04:56:16 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 73.4 |
| c93350ac-7e7b-3286-af06-184555ad45d8 | 1.0016 | -52.2164 | 2024-10-15 05:05:00 | GOES-16 | PEDRA BRANCA DO AMAPARI | AMAPÁ | Brasil | 1600154 | 16 | 33 | nan | nan | nan | Amazônia | 66.5 |
| ff80109a-d2a6-3b2d-b078-3bb18058ddb3 | -3.1099 | -54.2263 | 2024-10-15 05:05:23 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 38.9 |
| 6db703e5-b6ae-3e5f-80fd-260083a50695 | -3.1283 | -54.2259 | 2024-10-15 05:05:23 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 35.1 |
| 1b534d11-4471-3b79-aca4-83ebeff1df59 | -3.9289 | -48.3458 | 2024-10-15 05:05:28 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 59.5 |
| ff02dcdb-31c5-30a4-9214-af4a37f91232 | -3.9103 | -48.3466 | 2024-10-15 05:05:28 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 56.6 |
| 6799afd6-7468-3191-9bd8-a55b70d2c8f9 | 1.00721 | -52.21744 | 2024-10-15 05:14:00 | AQUA_M-M | PEDRA BRANCA DO AMAPARI | AMAPÁ | Brasil | 1600154 | 16 | 33 | nan | nan | nan | Amazônia | 27.6 |
| dbb8c13b-7d13-33d1-8358-f7810e104c1f | 1.0016 | -52.2164 | 2024-10-15 05:15:00 | GOES-16 | PEDRA BRANCA DO AMAPARI | AMAPÁ | Brasil | 1600154 | 16 | 33 | nan | nan | nan | Amazônia | 75.2 |
| 69f7d243-9451-38df-b716-a126614f2a0f | -3.1283 | -54.2259 | 2024-10-15 05:15:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 36.5 |
| d318a365-0559-36a3-a80d-0d9d07b330d6 | -3.1099 | -54.2263 | 2024-10-15 05:15:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 39.3 |
| e9764544-9649-3372-b810-9720644f0a3f | -9.46247 | -45.50676 | 2024-10-15 05:16:00 | AQUA_M-M | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 3e25db54-26bc-397c-a73f-47fc186338bc | -9.45343 | -44.1859 | 2024-10-15 05:16:00 | AQUA_M-M | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 8.9 |
| ecc57568-a298-3fed-b1a5-e66165e50319 | -9.44561 | -44.17477 | 2024-10-15 05:16:00 | AQUA_M-M | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 188124cb-46f6-385c-b279-07c0743e79eb | -9.43779 | -44.16365 | 2024-10-15 05:16:00 | AQUA_M-M | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 3093b63c-eaef-3d6e-b1f9-40fc5cfa65fb | -8.32625 | -42.77564 | 2024-10-15 05:16:00 | AQUA_M-M | BREJO DO PIAUÍ | PIAUÍ | Brasil | 2201988 | 22 | 33 | nan | nan | nan | Caatinga | 5.4 |
| 6427ff0e-052e-368a-ab12-187adeb4c2ad | -7.89043 | -44.53555 | 2024-10-15 05:16:00 | AQUA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 7.1 |
| e14555e0-0f30-3218-8066-4d7cd14bce86 | -7.73325 | -43.20248 | 2024-10-15 05:16:00 | AQUA_M-M | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 5.2 |
| bda72065-062c-3a85-997d-b65fd505594a | -7.71346 | -43.27304 | 2024-10-15 05:16:00 | AQUA_M-M | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 5.4 |
| b155734f-aad9-39b3-a3f5-8c8bdf2a3078 | -7.17758 | -42.64643 | 2024-10-15 05:16:00 | AQUA_M-M | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 6.1 |
| 67f36f27-9259-3f12-bcbb-427f76cd2e98 | -7.0728 | -42.66941 | 2024-10-15 05:16:00 | AQUA_M-M | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 4.7 |
| cc485e0e-0146-32e0-b40d-58d94ae6f700 | -6.19037 | -43.41566 | 2024-10-15 05:16:00 | AQUA_M-M | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 13.3 |
| 39a21d31-10b7-3ed3-b3d7-e2913b44daa1 | -3.92625 | -42.39513 | 2024-10-15 05:16:00 | AQUA_M-M | ESPERANTINA | PIAUÍ | Brasil | 2203701 | 22 | 33 | nan | nan | nan | Caatinga | 20.3 |
| 1cbc1d00-0c42-3ff7-8dea-23e1ffc10ef7 | -3.92473 | -42.40541 | 2024-10-15 05:16:00 | AQUA_M-M | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 333.5 |
| 7657d443-22b3-3aa0-a9ba-b1fee32126fb | -3.92321 | -42.41566 | 2024-10-15 05:16:00 | AQUA_M-M | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 98.4 |
| 3d3c825e-e0de-331a-82e0-3de934124190 | -3.91522 | -42.40405 | 2024-10-15 05:16:00 | AQUA_M-M | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 7.7 |
| 158141fd-ad42-3048-9260-5222ba75b451 | -9.2071 | -47.56107 | 2024-10-15 05:16:00 | AQUA_M-M | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 896bca5c-bd7f-342a-a09b-0a7af92ace43 | -8.71964 | -47.1881 | 2024-10-15 05:16:00 | AQUA_M-M | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 6b60c602-28aa-3de3-bbac-277dda76b29d | -8.46865 | -47.80463 | 2024-10-15 05:16:00 | AQUA_M-M | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| aaa7cddf-287b-3d6b-a21a-b7e520bc435f | -8.46714 | -47.81448 | 2024-10-15 05:16:00 | AQUA_M-M | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 99ab61f4-959e-3e23-97ad-f4cd8a1c233f | -1.86115 | -47.84578 | 2024-10-15 05:16:00 | AQUA_M-M | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 3455ed55-de12-3b95-a921-a7113070f67b | -2.63268 | -49.27135 | 2024-10-15 05:16:00 | AQUA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| c2ff8c9a-f5b9-3ac2-aacc-2fe0e0e68c7d | -2.81265 | -45.28722 | 2024-10-15 05:16:00 | AQUA_M-M | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 9ec681f3-b0c0-3efb-a8fc-8c38ceec30fb | -3.04239 | -53.23727 | 2024-10-15 05:16:00 | AQUA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 24.2 |
| d2dfe814-0472-3e84-9727-4dddbd52e0b9 | -3.04441 | -53.23264 | 2024-10-15 05:16:00 | AQUA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 23.6 |
| b21b4a39-0a10-3f22-a170-d95c0cf93c0b | -3.84219 | -46.47528 | 2024-10-15 05:16:00 | AQUA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.6 |
| cc5b8e4e-af9f-317b-b89a-b7f573c5eaf4 | -3.85959 | -46.91045 | 2024-10-15 05:16:00 | AQUA_M-M | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 6.9 |
| ceac522e-57dc-3dea-b602-5089722fb27e | -3.90361 | -48.35573 | 2024-10-15 05:16:00 | AQUA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 14cd05be-2114-3d86-942a-9beef1662b2c | -3.91383 | -48.35733 | 2024-10-15 05:16:00 | AQUA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 13.3 |
| 18b2fae0-c66e-3462-8a1c-7e5a3394909e | -3.91754 | -48.33324 | 2024-10-15 05:16:00 | AQUA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| a6f4b275-195a-3b05-935b-d6f6b3a37c72 | -2.4415 | -50.22042 | 2024-10-15 05:16:00 | AQUA_M-M | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 12.9 |
| 8e1de8f0-eb43-3cce-9de3-4bd7ae46c00d | -2.43882 | -50.23786 | 2024-10-15 05:16:00 | AQUA_M-M | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 26.3 |
| 79202993-c69c-3f16-b63c-776362909534 | -2.32419 | -48.57701 | 2024-10-15 05:16:00 | AQUA_M-M | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 13.2 |


[Clique aqui para ver as próximas entradas](README71.md)
