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

## Dados Diários - Página 98

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 18afe01a-15b4-32aa-b692-dc6bc05a0e8d | -16.67455 | -55.88739 | 2024-10-07 04:55:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 5f5b07b7-8c0f-34e2-aaed-4bf4d01d40aa | -16.6724 | -55.87954 | 2024-10-07 04:55:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| e208d28e-4cfa-3064-83e7-d31dc26c914b | -16.67181 | -55.88318 | 2024-10-07 04:55:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 7a51293d-ddac-3c42-8690-24b189be1ab4 | -16.67122 | -55.88681 | 2024-10-07 04:55:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 4c1cf96e-ebca-32fb-99af-1d13b6c85e44 | -16.67064 | -55.89045 | 2024-10-07 04:55:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 8923d5fa-542a-3849-b13a-65d96d3c9dc0 | -16.67005 | -55.89408 | 2024-10-07 04:55:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 1dc93f30-9bd8-30be-914a-8344b5592e09 | -16.66966 | -55.87534 | 2024-10-07 04:55:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| c8761460-52fd-39a1-b6d3-23b0523f73bf | -16.66849 | -55.8826 | 2024-10-07 04:55:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.9 |
| b0d8d0f9-86a1-3107-83a1-68dfe33d2da8 | -16.6679 | -55.88624 | 2024-10-07 04:55:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 05722610-6e3d-3e7e-8f85-a7a05311feaf | -16.66731 | -55.88987 | 2024-10-07 04:55:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| ff82a6ce-1c49-3b77-b446-24270cb2a795 | -16.66673 | -55.89351 | 2024-10-07 04:55:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 10.4 |
| 99ef6d28-3ed5-3cf0-9fa1-0ea6cade3a75 | -16.66496 | -55.90442 | 2024-10-07 04:55:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| b70809c0-6bca-3112-95ea-7b028c0190a6 | -16.66399 | -55.8893 | 2024-10-07 04:55:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 573aebb7-1ab6-30da-8eb3-6726caa90f54 | -16.66164 | -55.90384 | 2024-10-07 04:55:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 6821a268-0b44-3b6a-8911-1960d3c9efb8 | -16.66105 | -55.90748 | 2024-10-07 04:55:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| d868c47a-0747-3d1a-b9e8-23f9b7462806 | -17.06654 | -56.67625 | 2024-10-07 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 7de86a18-f9f7-34fd-91f3-5512c75f675b | -17.04506 | -56.68019 | 2024-10-07 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 9f43f84f-95e8-3b3c-8e42-ba0ad3a12b16 | -17.04105 | -56.68335 | 2024-10-07 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| d269d239-1aa7-31ac-96c1-0ef3d6e77c4f | -17.03431 | -56.68215 | 2024-10-07 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 39.1 |
| 062b21eb-132a-3c43-9adf-1ca528fbf6b7 | -17.03156 | -56.6778 | 2024-10-07 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 39.1 |
| ca2169a3-36bc-3059-b48c-cf29ff226b7a | -17.03093 | -56.68155 | 2024-10-07 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 39.1 |
| b6cbed5d-b2da-3e9d-be66-b54c70a77501 | -17.03023 | -56.67793 | 2024-10-07 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 52.7 |
| 15368637-7e8d-3bf8-a964-d8720f901ad3 | -17.02962 | -56.68169 | 2024-10-07 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 52.7 |
| f9ca37c4-c49c-3260-a08e-4f8e358b1836 | -17.02624 | -56.6811 | 2024-10-07 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 52.7 |
| 5bd0adec-057a-3880-bee9-4f9228645bcc | -17.02225 | -56.68426 | 2024-10-07 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 8.9 |
| 36b67f67-876b-377a-845d-a327ddd2fc81 | -17.01949 | -56.6799 | 2024-10-07 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 39.5 |
| 6da2fb1d-15a6-3134-b2e3-b8dc53a5c17a | -17.01888 | -56.68366 | 2024-10-07 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 8.9 |
| 56fb4da2-53f2-3dfc-a820-99a67cb117be | -17.01612 | -56.67929 | 2024-10-07 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 40.0 |
| 0ceb9c4a-cd76-3165-8fdf-23caf093bb09 | -17.0155 | -56.68306 | 2024-10-07 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 17.2 |
| ee2a7f4b-3548-3693-9f74-bb3f56eef7de | -17.01213 | -56.68246 | 2024-10-07 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 17.2 |
| 93e08fee-5887-3327-b17e-9949906aaf44 | -17.01089 | -56.68998 | 2024-10-07 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| df115310-f87a-31ed-b8bf-f2747bf02c78 | -17.01027 | -56.69374 | 2024-10-07 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| 14767f9c-ab0b-38a6-b345-69e63ea8a8c6 | -17.00875 | -56.68186 | 2024-10-07 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 12.4 |
| 948f5686-3e3b-31d9-b525-d5d716764328 | -17.00813 | -56.68562 | 2024-10-07 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 12.4 |
| 458e7ab2-940b-36a0-820a-0cbb855543ea | -17.00752 | -56.68938 | 2024-10-07 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 7.3 |
| d7b0f7d4-ee23-3006-ac4b-533172702965 | -17.00014 | -56.69195 | 2024-10-07 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| fd08d011-a81c-33c1-8efa-114b0e0ec2a1 | -16.99677 | -56.69135 | 2024-10-07 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 3c1b6cd8-3bfc-33d0-83e8-14f52a0ecb5c | -16.99339 | -56.69075 | 2024-10-07 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 74c9b377-9bb3-34b7-bbe6-a4e72fb91577 | -20.26512 | -56.5307 | 2024-10-07 04:55:00 | NOAA-21 | MIRANDA | MATO GROSSO DO SUL | Brasil | 5005608 | 50 | 33 | nan | nan | nan | Pantanal | 2.8 |
| c97577dc-48e2-3348-b37a-53d0d3960d79 | -20.2624 | -56.52641 | 2024-10-07 04:55:00 | NOAA-21 | MIRANDA | MATO GROSSO DO SUL | Brasil | 5005608 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 27e33cbc-5eaa-3bbe-99ff-7f1ab78932b1 | -20.2618 | -56.5301 | 2024-10-07 04:55:00 | NOAA-21 | MIRANDA | MATO GROSSO DO SUL | Brasil | 5005608 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| bf5775e4-c3ad-300e-9b36-ffb49f7ec0bf | -20.25908 | -56.52581 | 2024-10-07 04:55:00 | NOAA-21 | MIRANDA | MATO GROSSO DO SUL | Brasil | 5005608 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 14fb987f-1f34-367a-b17d-bd14b02efe10 | -20.21728 | -55.99781 | 2024-10-07 04:55:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 8ef23591-0cd7-3121-ae54-353606051552 | -19.71385 | -56.48573 | 2024-10-07 04:55:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 0.9 |
| a1284aa8-3d2e-3a3a-9d14-cc349d7a7732 | -19.71325 | -56.48941 | 2024-10-07 04:55:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 664607c1-15cd-31d3-ab0f-6bb33e049a2f | -19.66402 | -56.45818 | 2024-10-07 04:55:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| cb64f020-4adb-39f8-a902-9dbf1a71f0c1 | -19.66343 | -56.46186 | 2024-10-07 04:55:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 7f832bfa-834d-3d7e-bb51-f321ff34c6ef | -19.66295 | -56.50728 | 2024-10-07 04:55:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 0af3d695-3c23-3616-8a71-d25bd1ee6e52 | -19.66236 | -56.51097 | 2024-10-07 04:55:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 0.9 |
| d0c64591-fe47-3161-aeeb-981504cd3207 | -19.66165 | -56.47291 | 2024-10-07 04:55:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 533452d6-6228-31e5-98b3-ccd2408930d0 | -19.66011 | -56.46127 | 2024-10-07 04:55:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.1 |
| c5a4e7a8-4bf0-34e1-81a1-f9bbf9b573ad | -19.65963 | -56.50669 | 2024-10-07 04:55:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.2 |
| e02555a2-641c-3ca1-ada4-e173d97e311f | -19.65904 | -56.51038 | 2024-10-07 04:55:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.2 |
| a4f762c2-0382-3887-b901-9d099018ef3d | -19.65892 | -56.46863 | 2024-10-07 04:55:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| fa1364b4-a121-37f6-9cc0-e8a45db51fbd | -19.65833 | -56.47231 | 2024-10-07 04:55:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| fce180e7-c2b8-35e3-89a1-a0afeaa86541 | -19.65715 | -56.47969 | 2024-10-07 04:55:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.5 |
| d2703385-0b41-336b-8e68-a2356b339249 | -19.64848 | -56.51228 | 2024-10-07 04:55:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 36fe9516-d5b2-3a0f-900e-84c9e4069642 | -19.64481 | -56.49265 | 2024-10-07 04:55:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 472ca904-3942-3aa5-b008-574c182fa3e0 | -19.64149 | -56.49206 | 2024-10-07 04:55:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.8 |
| e58eac10-a4c5-3746-b734-1e0a5a5f9360 | -19.6409 | -56.49575 | 2024-10-07 04:55:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 389f6a9c-7469-3364-8f79-edb7005b5e0a | -19.59056 | -56.53226 | 2024-10-07 04:55:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.7 |
| e5dfdf98-98c4-36ec-a5af-6df7c3f6a327 | -19.58724 | -56.53166 | 2024-10-07 04:55:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 0c4d28ce-2fd1-3ca2-aa1b-0123c7fdc035 | -19.58391 | -56.53106 | 2024-10-07 04:55:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 5c8c0c32-2476-3b15-a315-badb209b7ee3 | -19.58059 | -56.53047 | 2024-10-07 04:55:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| f2456bb2-d4cf-35da-9e4e-2912dbee02a6 | -19.57667 | -56.53357 | 2024-10-07 04:55:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 9678d89d-be9e-3d14-8f8c-554fb91d2fa6 | -20.27462 | -56.93244 | 2024-10-07 04:55:00 | NOAA-21 | BODOQUENA | MATO GROSSO DO SUL | Brasil | 5002159 | 50 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 07e2028e-c0f2-3364-94c9-b081de13651c | -21.41594 | -57.22424 | 2024-10-07 04:55:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 6ff78b6e-412d-30b4-8213-e9c8309b805a | -21.41534 | -57.22796 | 2024-10-07 04:55:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 6d813248-3f66-37ea-91fc-ae20eda0a8ba | -21.41492 | -57.25134 | 2024-10-07 04:55:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 3.6 |
| ab98d6ba-3de8-3cc4-a382-1e82bc271232 | -21.41159 | -57.25068 | 2024-10-07 04:55:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d3bb5606-ef54-3325-a594-b81969b09355 | -21.41139 | -57.23106 | 2024-10-07 04:55:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 35ece411-b93e-3fef-824d-a85503abb075 | -21.41095 | -57.25451 | 2024-10-07 04:55:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 10144f7d-de3e-3a50-8db8-018065a432e1 | -21.40827 | -57.24999 | 2024-10-07 04:55:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a3ed9116-067f-32c7-ab46-d85ae0a5b0ef | -21.40763 | -57.25381 | 2024-10-07 04:55:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 81e6edfa-f774-3afb-ba3a-60ee3e7c4f87 | -21.40569 | -57.2501 | 2024-10-07 04:55:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 3.6 |
| b10d9c9e-c510-3dcb-bee9-e4acfeffc4a9 | -21.40507 | -57.25392 | 2024-10-07 04:55:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 1688b0b8-331f-3457-8b12-df3cd8cf3a8b | -21.40298 | -57.2456 | 2024-10-07 04:55:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 4684e2c6-8579-3afb-b08f-8c6b2152e07a | -21.40236 | -57.24941 | 2024-10-07 04:55:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 1bd4babd-b8cd-3ee3-ab9d-122d5f1b655f | -21.40174 | -57.25322 | 2024-10-07 04:55:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 2cf7311d-a06c-3d6d-9295-864465aae022 | -21.40026 | -57.24115 | 2024-10-07 04:55:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 9e0a150f-43a4-39d5-85ba-54e7d3d6654f | -21.39965 | -57.24494 | 2024-10-07 04:55:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 177556a1-eff3-3723-bbcc-130e8a70db5c | -21.39903 | -57.24874 | 2024-10-07 04:55:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 9032a245-23b4-37ef-a811-d6370782bad6 | -21.39842 | -57.25253 | 2024-10-07 04:55:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 4.8 |
| a083204b-3e65-306c-8502-ac3bd6bf23f6 | -16.44942 | -57.31824 | 2024-10-07 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| d8dfe281-619c-3ee1-9950-b87f2948fb7a | -16.44596 | -57.31762 | 2024-10-07 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 8c11df10-dc54-30e9-9d30-4757b1a62569 | -16.4453 | -57.32157 | 2024-10-07 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 7ae129d6-a451-339c-a31d-18c2b61695e8 | -16.44424 | -57.26431 | 2024-10-07 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 66cb7855-feaf-3bf4-8cc8-1cd67fd8101e | -16.44383 | -57.30909 | 2024-10-07 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 062dc54a-def4-3c90-8a70-1923d91948e7 | -16.44357 | -57.26829 | 2024-10-07 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 2836dcf4-784e-33bb-9b2e-05ff691164de | -16.44316 | -57.31305 | 2024-10-07 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| f4fa1c76-5897-38c3-b615-0993f5f5d87d | -16.4429 | -57.27226 | 2024-10-07 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.6 |
| 44493d84-fde6-357d-ba3f-797cb9ed3033 | -16.4425 | -57.31699 | 2024-10-07 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 57018a49-0d38-391a-9e14-6f05cfca40ba | -16.44078 | -57.26368 | 2024-10-07 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 51a85c01-913d-3f3a-86c8-845d317cb52a | -16.44011 | -57.26767 | 2024-10-07 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 9c506670-55b3-372d-b259-56059894bf9d | -16.43944 | -57.27164 | 2024-10-07 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 79aef45d-6b3f-35f6-8146-1f3dea0b29ba | -16.43878 | -57.27559 | 2024-10-07 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| ab56a60b-27db-3714-a0a0-fed07ef2b551 | -16.43733 | -57.26308 | 2024-10-07 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| b13adfee-ab8c-3b9c-9f98-823ab625ea71 | -16.43666 | -57.26705 | 2024-10-07 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 3a66a618-9884-3129-a442-312953ac1390 | -16.43624 | -57.3118 | 2024-10-07 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 9d624e81-37b9-3f8d-87e5-4895b294dbeb | -16.43599 | -57.27101 | 2024-10-07 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |


[Clique aqui para ver as próximas entradas](README99.md)
