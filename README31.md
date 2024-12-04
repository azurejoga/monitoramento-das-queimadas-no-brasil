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
| 38b9f1d2-7a04-366b-bc15-5959fa287bc4 | -2.98566 | -53.90949 | 2024-12-04 05:03:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 7def744a-2fa5-3ad0-bd30-68ca39023bab | -1.27739 | -54.55128 | 2024-12-04 05:03:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2a7ef370-a670-3caa-8641-46e5019d51c7 | -1.6517 | -53.82773 | 2024-12-04 05:03:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ca66490a-b1f5-3f79-8c58-4aeb44b164d0 | -3.10789 | -53.75565 | 2024-12-04 05:03:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 2147a87f-b3e1-347a-b0bc-ea76ca98353a | -3.22598 | -53.82908 | 2024-12-04 05:03:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bece2520-bb4d-3aa3-82ef-482c61823ee6 | -2.98334 | -53.87996 | 2024-12-04 05:03:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| fdd8023c-2f19-3365-b501-c9bc16f929a1 | -2.55003 | -53.41206 | 2024-12-04 05:03:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 50104408-319c-383f-a9e6-11fcb121b0b7 | -1.74853 | -52.62719 | 2024-12-04 05:03:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f4703241-9c4c-3dbc-884c-4931b03dff9a | -4.05347 | -46.98656 | 2024-12-04 05:03:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 240def0a-3d15-3fbf-bea4-ebb672cefcb5 | -4.38298 | -43.36538 | 2024-12-04 05:03:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| f38d1875-485e-3895-adb7-38cf05cba608 | -2.45745 | -53.71938 | 2024-12-04 05:03:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 06660bd0-7088-38e6-8b5b-119797fd5024 | -2.78885 | -55.37157 | 2024-12-04 05:03:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ecc09a97-25bc-380d-8177-fc79e06a431c | -3.54941 | -51.3373 | 2024-12-04 05:03:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 39fa9ff5-a822-35a0-8548-16dffc11ed0a | -2.98676 | -53.90239 | 2024-12-04 05:03:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| db9c0ccc-a8af-3155-8e98-620899a9453c | -3.48239 | -53.80164 | 2024-12-04 05:03:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b755d691-8a2f-3930-bd58-9079a1705a7b | -3.88916 | -50.07359 | 2024-12-04 05:03:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 22ade062-8d2f-339f-890d-7f7e111fbb3e | -1.59185 | -52.25451 | 2024-12-04 05:03:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 045d8cb4-6f79-3ed8-81e2-52eb604c8ce0 | -2.80303 | -54.03794 | 2024-12-04 05:03:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| dea23be6-4522-3b09-bf60-31a1e395f777 | -2.79664 | -53.04277 | 2024-12-04 05:03:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7c99078e-68d0-3aa9-b8ad-0128600290c2 | -3.35719 | -51.14374 | 2024-12-04 05:03:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6a41e463-4e2d-308d-ade7-e72fdce0c3dc | -3.13591 | -54.18995 | 2024-12-04 05:03:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c4df766c-0199-30be-adef-15b49d2c69e2 | -1.34235 | -54.96225 | 2024-12-04 05:03:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0c228023-a976-30c3-b737-d885555adda8 | -3.35219 | -53.53597 | 2024-12-04 05:03:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 90007b0d-69c7-3ccd-92c7-b7608644109a | -2.5489 | -53.41935 | 2024-12-04 05:03:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 56fb1045-1b6a-3d95-91de-a260c6213fcb | -2.87835 | -54.1215 | 2024-12-04 05:03:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 20dcdfe7-3aed-37a6-8e59-0f198b05b120 | -2.52377 | -54.03791 | 2024-12-04 05:03:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| dbe85bab-08d7-3ca7-9116-c6639bd6e588 | 1.96997 | -60.9163 | 2024-12-04 05:03:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 90ed13cb-528f-3e38-a5c5-0abf220c511f | -3.07166 | -54.03509 | 2024-12-04 05:03:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8d7c052f-8658-3ba0-975f-64b48bc333f1 | -2.20769 | -53.77195 | 2024-12-04 05:03:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| b314673f-994b-3d37-aacd-c39e43714633 | -3.20861 | -54.26924 | 2024-12-04 05:03:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e30705db-9f2a-3af5-b920-824bbf458047 | -2.61507 | -54.041 | 2024-12-04 05:03:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| c558877f-3778-37c5-be7e-9be7de0c22ef | -3.92435 | -52.39994 | 2024-12-04 05:03:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 4f6ea70a-c007-3b6f-beaa-d47d0649f153 | -2.42201 | -54.01513 | 2024-12-04 05:03:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 40160486-1ccf-32e9-86e2-7250d76f0ec7 | -2.61782 | -54.35325 | 2024-12-04 05:03:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 14847946-400f-3d3f-9f96-e01a2f1d041c | -2.94359 | -54.20343 | 2024-12-04 05:03:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3f3b02b0-99d8-3633-be9b-b256895cdda5 | -3.10631 | -54.055 | 2024-12-04 05:03:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f8639014-0ab1-3af9-b47b-32ed80d825ba | -2.88968 | -51.82344 | 2024-12-04 05:03:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f716970c-ef10-39e1-9b3a-720c04bdffbc | -1.38467 | -53.55473 | 2024-12-04 05:03:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 13555071-bfeb-3e78-ad98-d5e26f5b88fa | -1.35141 | -51.37964 | 2024-12-04 05:03:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d5dfb249-1ae9-39ab-b37a-5134dc4b5bc9 | -3.07151 | -51.26942 | 2024-12-04 05:03:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0b5e062e-c0ae-36db-a7d6-24f3d6eb4289 | -2.80409 | -53.06319 | 2024-12-04 05:03:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| d6c0b3c5-6a36-3121-98b3-011b162de93a | -2.80847 | -54.04215 | 2024-12-04 05:03:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f6ee5929-d770-30e3-af4b-c29dede111a9 | -3.264 | -53.62799 | 2024-12-04 05:03:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f941df8f-c989-3b1c-9cef-851521b73753 | -2.79997 | -54.14182 | 2024-12-04 05:03:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d854d54e-cc69-3274-86e1-994334b466ae | -3.37953 | -51.09868 | 2024-12-04 05:03:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 7bcf1d06-db68-3373-8d55-7e445d82d9d6 | -2.92529 | -54.36531 | 2024-12-04 05:03:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1de0630a-86c4-3b35-adf8-199a1491afb7 | -0.82488 | -51.61202 | 2024-12-04 05:03:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e604094a-e318-3acf-a127-d3a1ee060868 | -3.25555 | -53.66016 | 2024-12-04 05:03:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| c604c7e2-dbcd-3a83-a2d0-59e77137e807 | -2.81272 | -53.05296 | 2024-12-04 05:03:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e694a453-4776-34a2-b19d-9f13eb1acefc | -2.85197 | -54.04884 | 2024-12-04 05:03:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9450e053-421b-34c4-b33f-2bf7f4ca402a | -2.73205 | -51.82722 | 2024-12-04 05:03:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 23.7 |
| f41a761e-01d6-3398-b6e4-a966090e9d32 | -3.27603 | -54.14264 | 2024-12-04 05:03:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3c787c84-445d-35da-b582-327185acf4ab | -2.23656 | -53.69625 | 2024-12-04 05:03:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| b51a6765-2e54-33ce-9243-831056803a11 | -2.86322 | -54.0867 | 2024-12-04 05:03:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 79fe36eb-d7d2-3e30-97a1-24c17722d5a7 | -2.88197 | -51.80043 | 2024-12-04 05:03:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 1a7357a1-ffe1-3d79-8566-891ca6f615bd | -3.10452 | -53.75513 | 2024-12-04 05:03:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| f27f4736-a2fa-3e81-a40f-5e39deb0cceb | -2.82535 | -53.06261 | 2024-12-04 05:03:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b6ee0b7a-cb8a-3309-b06e-2f22d3e3b295 | -3.49198 | -53.82893 | 2024-12-04 05:03:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| dd313b47-ee31-36c0-9e4b-67c5eed2beef | -2.77706 | -50.29711 | 2024-12-04 05:03:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0088d49f-50f8-3c57-a7c5-603656446c2d | -2.82132 | -53.06585 | 2024-12-04 05:03:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 6bed82b5-7f3b-3eeb-b6a9-0202fb5e6fbb | -3.2029 | -50.64149 | 2024-12-04 05:03:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| f99b32bf-8fb3-3e31-9fa5-1e4c786d6090 | -3.24541 | -50.41771 | 2024-12-04 05:03:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 89c33f2c-470c-3b94-a621-d5c230112e89 | -2.52937 | -54.04598 | 2024-12-04 05:03:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d11ad753-5285-384d-8d8e-635c855a5245 | -3.02857 | -53.40491 | 2024-12-04 05:03:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 92a0b0e3-2136-3ee4-88b5-594733c703fd | -3.29567 | -53.66992 | 2024-12-04 05:03:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 3d5e9896-03c2-392d-a74e-ff12bf4c65fd | -3.56064 | -51.51939 | 2024-12-04 05:03:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1a2b48a9-700e-3178-b0c0-bb9fd71125c6 | -3.11576 | -54.0383 | 2024-12-04 05:03:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 8b276ae0-5980-3171-b276-263f046902b0 | -3.02479 | -53.87902 | 2024-12-04 05:03:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e93e1004-c83d-330f-bedb-0e110a741972 | -2.73859 | -54.10019 | 2024-12-04 05:03:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f1c448cf-e737-3afc-8672-fa3d01bfcb1e | -2.86091 | -54.05745 | 2024-12-04 05:03:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 0ece8c15-27ae-3e68-8c6d-99f62b1da3ad | -2.38494 | -54.36361 | 2024-12-04 05:03:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a8b1a6bd-7805-3fc1-8ebc-26ae70c7f4f6 | -2.77407 | -54.04794 | 2024-12-04 05:03:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1fc31070-a3d9-3a9d-a5fc-23dbc6a1da02 | -3.30924 | -52.16145 | 2024-12-04 05:03:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 0fbbee3e-0dbe-382f-a3b6-63fb4c039fbc | -3.553 | -50.178 | 2024-12-04 05:03:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 230f47a3-5272-3bda-a988-b2c72111f1ae | -2.38194 | -53.65981 | 2024-12-04 05:03:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a6b0f8af-7ece-3636-893e-3ea615763c80 | -2.85811 | -54.0534 | 2024-12-04 05:03:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 84e7c016-c64b-36aa-a156-7792ab397d68 | -3.11596 | -54.6263 | 2024-12-04 05:03:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1cdaa477-c414-349d-8176-19ab3874576c | -2.30134 | -53.86979 | 2024-12-04 05:03:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 03c5d4a2-f360-3467-a719-a92ae6282c09 | -2.54423 | -53.99431 | 2024-12-04 05:03:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b88b3e8e-89f4-303f-b67a-f1eae7f39295 | -2.8687 | -54.05142 | 2024-12-04 05:03:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| ac31c41c-d1cd-3045-ba1d-777a8ab483e6 | -3.72151 | -53.75251 | 2024-12-04 05:03:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8fb578bf-8c07-36b8-b85c-da1c231b99a0 | -3.02491 | -54.07146 | 2024-12-04 05:03:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3647043a-0c51-3b7a-8dc0-a72af2aaae32 | -1.94584 | -54.23474 | 2024-12-04 05:03:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ab77717f-ba1d-3fb5-8d9a-042b2fb26164 | -2.46583 | -53.70972 | 2024-12-04 05:03:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ac10754f-40a7-3822-83fc-bf2e66a7da9f | -2.99854 | -53.37068 | 2024-12-04 05:03:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 946da473-ad5e-3263-8b61-14fe78884c13 | -3.51066 | -54.55943 | 2024-12-04 05:03:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f691c405-aafe-3af9-ba7c-18d4b9236aa6 | -2.98957 | -53.90648 | 2024-12-04 05:03:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8557ad89-7a76-3829-9f85-6440f8cf6438 | -3.50041 | -54.03203 | 2024-12-04 05:03:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 71f746a5-a72f-3be8-8280-38940fe07809 | -4.37495 | -43.37511 | 2024-12-04 05:03:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 18da33ea-067e-39f5-9cb2-bdedd0ef240d | -1.65155 | -52.38023 | 2024-12-04 05:03:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 117405f7-ab78-3a04-8aa4-6e9ba95a2c52 | -1.11614 | -53.11226 | 2024-12-04 05:03:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9554326e-dab9-365c-b2c9-079fb99f26ff | -2.68804 | -54.25028 | 2024-12-04 05:03:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| d4984aa2-b5c9-39bf-8abf-39deb394d76c | -3.02516 | -53.40441 | 2024-12-04 05:03:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 86273671-3eb7-3efa-85c4-0d939860c3bd | -1.65772 | -52.39283 | 2024-12-04 05:03:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| aa492baa-4ee5-3ef1-b8e1-1357fe5f1b75 | -2.98621 | -53.90594 | 2024-12-04 05:03:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8fd391fe-8037-3e73-be41-dc5d07128808 | -3.06084 | -54.50012 | 2024-12-04 05:03:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| b81092d1-3fc6-3210-b9cc-be6b095b082c | -3.64335 | -54.21014 | 2024-12-04 05:03:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e59f7374-0cbe-3881-9969-b3e98adc65b9 | -2.446 | -54.03684 | 2024-12-04 05:03:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 2dcdd373-04ce-3d33-b509-845f66371e46 | -1.89977 | -52.85552 | 2024-12-04 05:03:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8e92ad3d-61d7-3159-8cd0-fe52e50501f4 | -3.24931 | -53.63314 | 2024-12-04 05:03:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |


[Clique aqui para ver as próximas entradas](README32.md)
