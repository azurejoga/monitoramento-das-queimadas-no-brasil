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

## Dados Diários - Página 31

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7fd8019e-b5ed-31dc-912e-3227847eb856 | -8.83046 | -62.37103 | 2025-09-18 05:53:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 47cf86dc-c697-3d0b-9ada-6690b24e145f | -3.19374 | -54.97643 | 2025-09-18 05:53:00 | NOAA-20 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c03cde71-34c4-3d51-822d-5419e4559000 | -10.94776 | -68.49245 | 2025-09-18 05:55:00 | NOAA-20 | EPITACIOLÂNDIA | ACRE | Brasil | 1200252 | 12 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 6d2c7c7f-81c8-364c-84c5-e7cea797e3fd | -9.42358 | -67.61485 | 2025-09-18 05:55:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| facd6af8-0216-3136-aa33-f028237c9627 | -10.9969 | -68.45545 | 2025-09-18 05:55:00 | NOAA-20 | EPITACIOLÂNDIA | ACRE | Brasil | 1200252 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 2ef5e5f5-988e-3422-9a57-35c8fe911e41 | -10.05424 | -68.45377 | 2025-09-18 05:55:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 81693e45-6325-30a6-b478-6047a828ad62 | -9.78635 | -65.05761 | 2025-09-18 05:55:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f319a31d-a9fc-3f8b-b450-abba47038b49 | -13.29765 | -61.79399 | 2025-09-18 05:55:00 | NOAA-20 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9f6ca06f-8b56-3706-8c2c-2fd4cdf2ba4f | -15.81328 | -59.39981 | 2025-09-18 05:55:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 43bc5d47-8f00-387c-8888-8b28110691ea | -15.81082 | -59.40379 | 2025-09-18 05:55:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ed703bd3-451d-3c05-8457-2feff19388f4 | -15.81125 | -59.39981 | 2025-09-18 05:55:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 35fce614-37de-3fc7-8b0f-e38c0d318395 | -13.2982 | -61.79586 | 2025-09-18 05:55:00 | NOAA-20 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 48a2d5d6-50cf-37ac-8650-8f4c85fdedb0 | -13.29415 | -61.78181 | 2025-09-18 05:55:00 | NOAA-20 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| dd715534-c281-3c5f-a599-d027762bf500 | -10.55071 | -62.74007 | 2025-09-18 05:55:00 | NOAA-20 | GOVERNADOR JORGE TEIXEIRA | RONDÔNIA | Brasil | 1101005 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8252f771-ee83-3836-8658-bbb0d8d6c8c6 | -15.31318 | -59.4215 | 2025-09-18 05:55:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5695ee1b-15e3-3d3b-a1f0-37236f5760bb | -10.53454 | -68.1337 | 2025-09-18 05:55:00 | NOAA-20 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 33818eed-0288-3d4b-b2ea-cd5fa9255d42 | -10.64891 | -69.29691 | 2025-09-18 05:55:00 | NOAA-20 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 0.3 |
| e953cb49-f196-3912-9a81-2c0742ae6b72 | -9.76744 | -64.29295 | 2025-09-18 05:55:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c02c97e1-b813-3a92-a3a0-92d0da772fb4 | -10.99635 | -68.45904 | 2025-09-18 05:55:00 | NOAA-20 | EPITACIOLÂNDIA | ACRE | Brasil | 1200252 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 61ab44c2-70de-34bf-87ac-8ec4a94b20cd | -15.32657 | -59.4094 | 2025-09-18 05:55:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| df0e0e4d-278f-357d-bd95-e7d200f8c685 | -15.81683 | -59.40444 | 2025-09-18 05:55:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 50d0b894-c45a-38a8-a4a5-b439eb35fd5b | -9.75847 | -64.29875 | 2025-09-18 05:55:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b2b07578-708b-3609-adfa-df8fbe6d1ec7 | -9.75895 | -64.2953 | 2025-09-18 05:55:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c7ae0dee-03a4-31eb-9d1e-ea59c947d4f0 | -9.76295 | -64.29587 | 2025-09-18 05:55:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 00361ce1-58d2-3576-86ad-7df4877d5965 | -10.26689 | -67.13423 | 2025-09-18 05:55:00 | NOAA-20 | PLÁCIDO DE CASTRO | ACRE | Brasil | 1200385 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| cf80d6f0-9f82-3286-a338-95f6ed2979b4 | -10.67333 | -68.7071 | 2025-09-18 05:55:00 | NOAA-20 | EPITACIOLÂNDIA | ACRE | Brasil | 1200252 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 634b96e7-79cb-3817-b83d-edcd5fd926c0 | -15.32008 | -59.41357 | 2025-09-18 05:55:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 2bfcf8ea-025f-3abc-b3bd-0c701860e041 | -10.27189 | -67.28689 | 2025-09-18 05:55:00 | NOAA-20 | PLÁCIDO DE CASTRO | ACRE | Brasil | 1200385 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2e23f665-583b-38af-9704-348f6f368433 | -15.31274 | -59.42561 | 2025-09-18 05:55:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bf8c8c6e-1f9b-343d-8a94-ad23c8f2cccb | -15.30673 | -59.42529 | 2025-09-18 05:55:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 11f2322b-388f-3612-b676-9cbd135c4ac0 | -12.40397 | -63.88989 | 2025-09-18 05:55:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a609d390-8d3a-3bbc-a636-0fcbf4faabba | -9.38282 | -68.77571 | 2025-09-18 05:55:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| cc20cd27-845a-3b10-8718-25657bebe0a5 | -12.40823 | -63.8905 | 2025-09-18 05:55:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fb471abb-fb0f-3051-9507-a9735c6e22d8 | -9.93467 | -66.72861 | 2025-09-18 05:55:00 | NOAA-20 | ACRELÂNDIA | ACRE | Brasil | 1200013 | 12 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2099adac-a7e9-327c-ab01-cd2e2dbe0c06 | -15.3192 | -59.42172 | 2025-09-18 05:55:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 79860b40-166f-3d75-8715-f65bd4b5861e | -10.06924 | -68.467 | 2025-09-18 05:55:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ea7e6881-6114-3fba-83d6-6e5e3662b40d | -10.43124 | -67.73093 | 2025-09-18 05:55:00 | NOAA-20 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 337d790e-b235-3ec7-9a9d-890a2d5ee211 | -15.30112 | -59.42118 | 2025-09-18 05:55:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b7b5c1a5-0c74-37c8-a971-696947a28cc6 | -10.17009 | -68.42839 | 2025-09-18 05:55:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3a466a8a-561f-3b4d-aa04-769655007784 | -9.37951 | -68.77518 | 2025-09-18 05:55:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 0.4 |
| e7a4dd15-c315-3127-9ac3-e2706f57d5be | -10.0904 | -68.52827 | 2025-09-18 05:55:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 5c476d2d-37e1-368a-b501-de28572a4087 | -15.30716 | -59.42129 | 2025-09-18 05:55:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| aa06e4af-d152-34ff-88bf-ccbef16e0702 | -9.81199 | -65.04208 | 2025-09-18 05:55:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a66677a6-9b9f-3da7-8421-55ae959e0564 | -9.93374 | -66.72942 | 2025-09-18 05:55:00 | NOAA-20 | ACRELÂNDIA | ACRE | Brasil | 1200013 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a753d07d-5ae2-39d6-b485-c19567008562 | -10.20197 | -67.90847 | 2025-09-18 05:55:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 46b7c2e1-d1a3-38b9-bc4e-d84a648b9252 | -10.07202 | -68.47107 | 2025-09-18 05:55:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| dfe2fe83-0c7f-3ed8-b7f3-c991b2039eb5 | -9.76695 | -64.29642 | 2025-09-18 05:55:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 93490fcf-66c8-3c79-9cc1-35f09363d687 | -15.8137 | -59.39569 | 2025-09-18 05:55:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 017b2f1f-72d9-3873-b4d2-1deca1ef6bd1 | -9.42696 | -67.61537 | 2025-09-18 05:55:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| ed6490fd-89b5-3785-88ff-725db3374d41 | -15.81771 | -59.3964 | 2025-09-18 05:55:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9ed82fbc-7210-3991-8406-4340c450398c | -10.06869 | -68.47054 | 2025-09-18 05:55:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a1700064-80bd-3d8e-bc5b-01067de56291 | -15.32059 | -59.40879 | 2025-09-18 05:55:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 49face67-65c9-3506-aabf-526fa3fbcecf | -10.26845 | -67.28637 | 2025-09-18 05:55:00 | NOAA-20 | PLÁCIDO DE CASTRO | ACRE | Brasil | 1200385 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3fdd06ea-3480-38f7-a5b2-74fbef5ae3cb | -10.26343 | -67.13372 | 2025-09-18 05:55:00 | NOAA-20 | PLÁCIDO DE CASTRO | ACRE | Brasil | 1200385 | 12 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 66f8e9de-46f7-309b-a305-8eae6fcd3838 | -10.43204 | -67.73062 | 2025-09-18 05:55:00 | NOAA-20 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 0ef71330-37ba-38c5-99d1-304b47d55d88 | -15.81287 | -59.40379 | 2025-09-18 05:55:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d3fcb2c2-b749-348d-8a1f-0aa67c2ff9d4 | -19.56333 | -57.7913 | 2025-09-18 05:57:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 6de876f4-c0d4-306c-836b-7eaa5b0dd41b | -19.59262 | -57.77392 | 2025-09-18 05:57:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.8 |
| d589470a-95e3-3d44-aa91-f7c36ac52c1a | -19.58573 | -57.77328 | 2025-09-18 05:57:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.8 |
| af53f2b4-a29b-37f8-9097-c6744c29ed6d | -19.56397 | -57.7846 | 2025-09-18 05:57:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.4 |
| d9655bb6-0750-3d64-95fd-c2d1cd14eb90 | -19.58627 | -57.76662 | 2025-09-18 05:57:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.8 |
| b58cc9b8-ec4e-306f-8b9e-ba4dd55aadc3 | -19.58465 | -57.78656 | 2025-09-18 05:57:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.1 |
| 72a6e7c0-f20e-393a-bbbf-c175c04eac85 | -19.56344 | -57.79123 | 2025-09-18 05:57:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 11ef8d95-d412-34b3-8fa1-703595f6abdd | -22.9714 | -51.5902 | 2025-09-18 06:00:00 | GOES-19 | GUARACI | PARANÁ | Brasil | 4109203 | 41 | 33 | nan | nan | nan | Mata Atlântica | 68.8 |
| 27b7791b-bbec-333a-a5da-5a615bef94e4 | -22.9714 | -51.5902 | 2025-09-18 06:10:00 | GOES-19 | GUARACI | PARANÁ | Brasil | 4109203 | 41 | 33 | nan | nan | nan | Mata Atlântica | 55.6 |
| 79abe3de-b76c-3f5c-9192-87d53dc0578b | -22.9714 | -51.5902 | 2025-09-18 06:20:00 | GOES-19 | GUARACI | PARANÁ | Brasil | 4109203 | 41 | 33 | nan | nan | nan | Mata Atlântica | 56.5 |
| a8ff21d4-05fc-394c-81c2-3d3f79cbc127 | -10.4085 | -61.1915 | 2025-09-18 06:30:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 56.8 |
| 47851906-44a6-3309-9611-5ef33dab68d9 | -10.4084 | -61.2108 | 2025-09-18 06:30:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 58.4 |
| f728101f-16e2-3b2f-a4d0-7d2e107c578b | -10.4085 | -61.1915 | 2025-09-18 06:40:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 66.8 |
| 89d9875b-1650-3913-a398-d617f44505de | -10.4084 | -61.2108 | 2025-09-18 06:40:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 63.3 |
| 75fdf4a0-6eea-3ebe-9ec8-34108ed2f42d | -22.9714 | -51.5902 | 2025-09-18 06:40:00 | GOES-19 | GUARACI | PARANÁ | Brasil | 4109203 | 41 | 33 | nan | nan | nan | Mata Atlântica | 55.8 |
| 2569a101-8c24-34a5-9498-9a4ad2adf349 | -3.50743 | -52.74929 | 2025-09-18 06:42:00 | AQUA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 11.8 |
| 520a3cf4-baf1-3dab-a849-9f0a89d53f2a | -3.94207 | -55.84239 | 2025-09-18 06:42:00 | AQUA_M-M | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 15.4 |
| 7b7a2255-10dd-3ebd-b7c1-626d5dc76519 | -14.74809 | -60.19642 | 2025-09-18 06:44:00 | AQUA_M-M | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 5.9 |
| c65810c3-c6ce-3121-aa15-be17e805a9e1 | -10.41482 | -61.20144 | 2025-09-18 06:44:00 | AQUA_M-M | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 29.4 |
| c743dacf-8ce2-33c2-8c5c-dfdc58b088d9 | -15.80849 | -59.39482 | 2025-09-18 06:44:00 | AQUA_M-M | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 472a33f1-2c21-3a13-b054-c468f26a82d7 | -10.40403 | -61.20982 | 2025-09-18 06:44:00 | AQUA_M-M | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 14.9 |
| bc908179-09a7-3eb7-97bc-c4944c76ba41 | -10.41638 | -61.19156 | 2025-09-18 06:44:00 | AQUA_M-M | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 24.8 |
| eef60ce7-53e4-3555-bbda-a78e93ec3c7b | -10.40714 | -61.19011 | 2025-09-18 06:44:00 | AQUA_M-M | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 21.2 |
| 52427504-23c1-3999-9afe-01e855b964e8 | -10.40558 | -61.19996 | 2025-09-18 06:44:00 | AQUA_M-M | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 13.2 |
| 1d5028a7-baaf-3f1c-ad9a-edb21d4bdd9d | -22.96157 | -51.58258 | 2025-09-18 06:46:00 | AQUA_M-M | JAGUAPITÃ | PARANÁ | Brasil | 4111902 | 41 | 33 | nan | nan | nan | Mata Atlântica | 68.6 |
| 40992c00-e952-310e-9e21-f69dc087d380 | -10.4085 | -61.1915 | 2025-09-18 06:50:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 56.2 |
| 492e39ce-3fd5-340b-b775-3d91d2d0ebc4 | -10.4084 | -61.2108 | 2025-09-18 06:50:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 53.8 |
| 27e9e3fa-55e6-3909-a3ba-79c3581947db | -22.9714 | -51.5902 | 2025-09-18 06:50:00 | GOES-19 | GUARACI | PARANÁ | Brasil | 4109203 | 41 | 33 | nan | nan | nan | Mata Atlântica | 57.7 |
| 620c2a7a-af9e-331e-b370-2ef57072a12b | -10.4084 | -61.2108 | 2025-09-18 07:00:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 68.0 |
| 486d36e3-5c14-3444-9c2a-b1d9b256b8f8 | -10.4085 | -61.1915 | 2025-09-18 07:00:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 71.8 |
| 403d44db-1888-303c-82ca-60181370df35 | -10.4085 | -61.1915 | 2025-09-18 07:10:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 59.3 |
| 4dc43436-fe91-3845-9404-d492957ee04c | -10.4084 | -61.2108 | 2025-09-18 07:10:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 59.8 |
| 041dcae3-86b7-3263-a92c-e5db83aaaf69 | -10.4084 | -61.2108 | 2025-09-18 07:20:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 60.9 |
| 4ebedee3-2cc6-324d-bf90-085e1a5957e3 | -10.4085 | -61.1915 | 2025-09-18 07:20:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 72.1 |
| a20b1a2d-85ac-3053-ac9b-7838794ed1c6 | -10.4085 | -61.1915 | 2025-09-18 07:30:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 81.3 |
| 940d88d8-ebd3-3dd3-b61f-f631c984c644 | -13.0747 | -42.1261 | 2025-09-18 07:30:00 | GOES-19 | RIO DO PIRES | BAHIA | Brasil | 2926905 | 29 | 33 | nan | nan | nan | Caatinga | 52.2 |
| b5129013-5564-3787-8e85-c0a78e48a71b | -10.4084 | -61.2108 | 2025-09-18 07:30:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 60.5 |
| 3d195d8f-f971-36ec-95cd-27b3d1e8c6dd | -12.9068 | -44.658 | 2025-09-18 07:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 53.4 |
| 7cb1473d-85fa-31bc-895e-035a4bc4e4ee | -12.9068 | -44.658 | 2025-09-18 07:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 85.7 |
| e9e97477-779d-320e-90a6-014685625640 | -10.4084 | -61.2108 | 2025-09-18 07:50:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 57.0 |
| a60df562-dfe4-3cea-8b5f-e3da1595ca2c | -12.9068 | -44.658 | 2025-09-18 07:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 94.7 |
| ac605d72-b467-3835-9185-94eba6e640c5 | -12.8874 | -44.6612 | 2025-09-18 07:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 51.1 |
| 4e2cae69-8533-30e8-be10-fc0fdbbadaa7 | -10.4085 | -61.1915 | 2025-09-18 07:50:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 62.9 |
| 749540fa-d2dd-3797-aa54-8fb84486a19a | -10.4084 | -61.2108 | 2025-09-18 08:00:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 60.0 |


[Clique aqui para ver as próximas entradas](README32.md)
