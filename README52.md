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

## Dados Diários - Página 52

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| bee342b3-5f8d-370e-a42d-0ca060a72df6 | -3.57869 | -50.39553 | 2024-10-08 04:32:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b6365c3d-11fb-3d28-bd45-20609c5c95f2 | -5.4236 | -49.96018 | 2024-10-08 04:32:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a43cead0-285d-3627-8c47-5d3796937e00 | -5.42075 | -49.95578 | 2024-10-08 04:32:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 36ee0d3a-9b3a-3939-b4b8-8f656dcc7a08 | -5.42013 | -49.95962 | 2024-10-08 04:32:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cdd3f2ed-adbf-38b7-bedd-024876b88725 | -5.29496 | -50.21775 | 2024-10-08 04:32:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 24961a33-ecb6-3e3c-998c-deee1dd641ac | -5.15306 | -50.75785 | 2024-10-08 04:32:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 383a5476-d330-3756-a238-a7b38004eb67 | -5.06732 | -50.6606 | 2024-10-08 04:32:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b22d1343-43c9-3cf8-b571-d1fe2ff19272 | -5.06665 | -50.66472 | 2024-10-08 04:32:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2be02563-d084-3b2f-9325-9b284abd727c | -5.02902 | -50.87287 | 2024-10-08 04:32:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 704a8e3a-8af3-3a70-b803-26dcb6ad403b | -5.02539 | -50.87228 | 2024-10-08 04:32:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d52b2af8-f0b2-3798-b3f0-8ebb014b3d1e | -2.15511 | -50.88195 | 2024-10-08 04:32:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5009fb57-0ad3-373a-9768-c69e7211dbd0 | -2.14103 | -50.70355 | 2024-10-08 04:32:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9f33a85b-1006-346c-9fdf-9d7108810be3 | -2.1373 | -50.70297 | 2024-10-08 04:32:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 364fee75-6805-3efd-b3d2-a8b78a34584a | -2.09033 | -50.67472 | 2024-10-08 04:32:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b9006cd9-8d84-3f81-9083-5561d7907660 | -1.69243 | -50.41444 | 2024-10-08 04:32:00 | NOAA-21 | BREVES | PARÁ | Brasil | 1501808 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9c25d937-4e69-39d4-915f-ff3a2627348f | -1.69167 | -50.41338 | 2024-10-08 04:32:00 | NOAA-21 | BREVES | PARÁ | Brasil | 1501808 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 00aebc6e-07bd-395b-9e82-dc88f606845a | -1.62341 | -50.53931 | 2024-10-08 04:32:00 | NOAA-21 | BREVES | PARÁ | Brasil | 1501808 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 952f1fbb-d8e1-3da3-b50c-33893c436b63 | -1.25125 | -51.21254 | 2024-10-08 04:32:00 | NOAA-21 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0b221439-2025-3d4f-af7c-93544b94d682 | -1.25023 | -51.21421 | 2024-10-08 04:32:00 | NOAA-21 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fd3cb59d-7346-399a-a0c5-13277f8875b9 | -3.63078 | -51.17326 | 2024-10-08 04:32:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| bc521b3b-6178-302a-8d1e-e12b5dc46877 | -3.59933 | -51.3714 | 2024-10-08 04:32:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a2b4ead5-e554-3d1f-857d-702d9da58453 | -3.59859 | -51.37607 | 2024-10-08 04:32:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 754f27c0-49f2-3e3f-ba73-13d23a218dc6 | -3.59552 | -51.3708 | 2024-10-08 04:32:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5ea81a8a-9a35-3668-a389-82b8a59439fb | -3.59478 | -51.37548 | 2024-10-08 04:32:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f79cfc3f-0906-38a6-b317-93ad6b0ea1a1 | -3.486 | -50.81015 | 2024-10-08 04:32:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f8106542-fef2-33e1-9900-eced54b94890 | -3.4591 | -51.20384 | 2024-10-08 04:32:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| c6298bf8-e260-39da-a231-c7929d428444 | -3.45533 | -51.20324 | 2024-10-08 04:32:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 6cd42b51-bc28-3745-bff4-36175d2846c8 | -3.43389 | -50.66431 | 2024-10-08 04:32:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f3bd018a-d91e-3706-94ae-a0d1e4c73fdc | -3.38599 | -51.46038 | 2024-10-08 04:32:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 11.8 |
| 1ae2d738-dfcf-3ad1-b913-07b288048c45 | -3.38405 | -51.45759 | 2024-10-08 04:32:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| c7c17653-5e86-3ee6-8f65-a336871afbd3 | -3.3833 | -51.46235 | 2024-10-08 04:32:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 1b526bcb-f1bb-384f-8d48-be87b7c57b72 | -3.23706 | -50.84132 | 2024-10-08 04:32:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9ca57613-4654-373e-8c74-5bfe9a21c489 | -3.23635 | -50.84576 | 2024-10-08 04:32:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a26b1616-85dc-3c19-9fe3-c79b1ec95fb9 | -3.23265 | -50.84513 | 2024-10-08 04:32:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 95ae3fd5-19bf-3787-b6de-ae160e347e36 | -3.22063 | -50.92073 | 2024-10-08 04:32:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| cb75fa41-d3de-377f-977a-199be29d74bc | -3.2169 | -50.92015 | 2024-10-08 04:32:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| afcb9f54-2171-3d61-b059-75244b3abdc1 | -3.1455 | -51.19762 | 2024-10-08 04:32:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 04fb81c4-d2b4-3a75-9abf-04aef2df1136 | -3.05235 | -51.10023 | 2024-10-08 04:32:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a17328e4-11db-3b68-8f11-2d1eae07ac71 | -3.04933 | -51.09494 | 2024-10-08 04:32:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 60c940ee-4f53-3cb8-bbea-40926a39034e | -3.04877 | -51.14661 | 2024-10-08 04:32:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5753c87e-101b-3cf7-b603-a781ebda04c0 | -3.04859 | -51.09958 | 2024-10-08 04:32:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0ce20909-e554-3461-99de-1f6cf50a9cdc | -2.97442 | -51.02889 | 2024-10-08 04:32:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 2b2a9923-7643-3376-a301-a897f922f656 | -2.97066 | -51.02831 | 2024-10-08 04:32:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| b49c5b6b-b982-3c10-af24-145bb1708b81 | -2.96882 | -51.11257 | 2024-10-08 04:32:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 176d012e-129d-3ff8-9acf-24a7fdc84d7f | -2.58542 | -51.82352 | 2024-10-08 04:32:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f8056085-25f0-356c-8ecd-dcd86325e28c | -2.556 | -50.63945 | 2024-10-08 04:32:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9b95f6c5-2e5a-3ec4-917a-0022df21405b | -2.45252 | -50.96526 | 2024-10-08 04:32:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| abcd0970-6697-3b53-afd0-3add62a34377 | -2.32025 | -50.52179 | 2024-10-08 04:32:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| afec15b6-5ec5-3a41-9c93-0366dd81c8c1 | -2.28591 | -50.54772 | 2024-10-08 04:32:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f21cef95-4fa3-323f-a11f-430ef95a8b4c | -2.28222 | -50.54716 | 2024-10-08 04:32:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| bfbddd6b-37ab-3ccd-8bc1-744f9c491a44 | -2.26504 | -50.60745 | 2024-10-08 04:32:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 7e4c1ae6-c317-3c65-b1ce-7ec1388acadb | -2.89801 | -50.70665 | 2024-10-08 04:32:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f9222547-c45b-3ee0-b5c2-6704a4e104c7 | -2.8973 | -50.71104 | 2024-10-08 04:32:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8104da2a-c40d-3214-9176-e3df2d12df31 | -2.8966 | -50.71542 | 2024-10-08 04:32:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 82b5c264-0443-3a1f-9822-bcea9b93400a | -2.8929 | -50.71485 | 2024-10-08 04:32:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ef7a3f89-98ec-3bc2-81eb-c3180ac1d7c0 | -2.88621 | -50.7093 | 2024-10-08 04:32:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6733bdb6-a4b6-37f8-b720-6ad153474cc0 | -2.80764 | -51.3923 | 2024-10-08 04:32:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| cc9e4767-69ff-38d2-9717-91594e461d0e | -4.65256 | -50.94896 | 2024-10-08 04:32:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3782048d-b13a-3e06-a6a8-ec27bf359ed1 | -4.63672 | -50.97757 | 2024-10-08 04:32:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2828af3a-22c2-332c-a486-1a577c53e10a | -4.63306 | -50.97698 | 2024-10-08 04:32:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8347965d-a125-3579-b77e-b83f6d022c8c | -4.63236 | -50.9813 | 2024-10-08 04:32:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 87d4f15e-897c-31b6-81f2-5ded41574007 | -4.63168 | -50.98558 | 2024-10-08 04:32:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 500bca52-ff1d-3bee-a503-ec8c5b00b60d | -4.62869 | -50.98072 | 2024-10-08 04:32:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| f8b593ca-4d13-3aa4-8faa-f95b4cc1eb37 | -4.62801 | -50.985 | 2024-10-08 04:32:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 782d86c3-ec0b-3f62-8132-5195bcaaf569 | -4.15672 | -51.04512 | 2024-10-08 04:32:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 0d261b40-9fef-38d1-9f74-9b01e1141447 | -4.15601 | -51.0495 | 2024-10-08 04:32:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 539d90d9-9617-3f22-860e-9d5b45d5313f | -4.1553 | -51.05392 | 2024-10-08 04:32:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d2d95f6a-0d56-3beb-af99-c6499874bfe7 | -4.15302 | -51.04446 | 2024-10-08 04:32:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 27b86a6e-220d-33f0-b3be-82867fc7ee1c | -4.15231 | -51.04885 | 2024-10-08 04:32:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 2d080ee3-7c13-3e6c-b8ef-f936a6417f2b | -4.09829 | -51.09978 | 2024-10-08 04:32:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8e6119c9-5a4a-3d55-a867-0ad376d057cf | -4.0629 | -51.11841 | 2024-10-08 04:32:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c6a8e394-bef7-3827-9bdd-9690bb88f38e | -4.05918 | -51.11777 | 2024-10-08 04:32:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3a061256-fc93-3dff-92fb-4ba7305b4055 | -4.05848 | -51.12219 | 2024-10-08 04:32:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| c8d3620e-5bd5-3f99-8a7f-b8053feb1402 | -4.05546 | -51.11713 | 2024-10-08 04:32:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8482de98-0ee9-31e4-b039-26ed4fec7ab4 | -2.20341 | -51.9577 | 2024-10-08 04:32:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 65e1ca00-eff2-35d5-aa8e-d3757a4d121e | -2.19937 | -51.95708 | 2024-10-08 04:32:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a1456d03-21f1-3c9a-8835-4d601603f4a8 | -1.63676 | -52.5831 | 2024-10-08 04:32:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| cc36274d-b20f-31cb-8ac2-9c2cdf94fb9d | -1.63315 | -52.5785 | 2024-10-08 04:32:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 3b4bd88f-58a1-3c13-a014-db0b4d22de7f | -1.63252 | -52.58243 | 2024-10-08 04:32:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 06b682c2-346d-34d4-b339-f48d86bfac5f | -1.32217 | -52.80833 | 2024-10-08 04:32:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 983f4659-fc0a-315c-b7aa-0ba1ac0a6a1d | -3.54527 | -53.14838 | 2024-10-08 04:32:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 9f4baf5e-9d7d-38d6-8141-632fc864bd64 | -3.54221 | -53.14763 | 2024-10-08 04:32:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6d2e8628-b068-3e36-b52c-3036ac471cdc | -3.54201 | -53.01257 | 2024-10-08 04:32:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| dea2af2a-1d94-3cdd-bc26-1407f879ee76 | -3.41938 | -52.72828 | 2024-10-08 04:32:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3df5fb0b-1337-330e-a0c9-3379d441454f | -3.33177 | -53.39492 | 2024-10-08 04:32:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3c82fcf0-b3db-30d2-8118-ee9ff51b00de | -3.3281 | -53.39005 | 2024-10-08 04:32:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 29b645f2-a332-349e-8452-4f6c9493dcc8 | -3.3274 | -53.39428 | 2024-10-08 04:32:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3c3b0094-8909-3309-a6bb-af69b9c3a634 | -3.32373 | -53.38942 | 2024-10-08 04:32:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 392e17ac-314c-3a06-9885-7748c7509b1b | -3.20403 | -53.14584 | 2024-10-08 04:32:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b25328f0-7afd-35a7-8dad-77a01a1b999d | -3.04703 | -53.03857 | 2024-10-08 04:32:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| e598f055-5165-3772-ac13-20db07448b58 | -3.03782 | -53.04123 | 2024-10-08 04:32:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 50b9fb82-c966-36e3-bf68-9d50b916b4b0 | -3.03716 | -53.04525 | 2024-10-08 04:32:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f48df770-7e92-3fea-82c4-107c6c967c8c | -3.03354 | -53.04058 | 2024-10-08 04:32:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 49ab3f86-482d-3479-9815-65a540aed5c1 | -3.03287 | -53.04462 | 2024-10-08 04:32:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 77f1929a-3bd9-31f2-9e6d-00df03d51494 | -2.32304 | -52.17817 | 2024-10-08 04:32:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d050e43a-c320-382f-ad32-fe579d95d616 | -2.87911 | -52.89819 | 2024-10-08 04:32:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9cb64a0b-10d8-3ddb-a952-70fc934c56ac | -2.87847 | -52.90213 | 2024-10-08 04:32:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7257e026-80e7-30fa-8f7c-84b51271fed1 | -2.87784 | -52.90607 | 2024-10-08 04:32:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bb17a5d9-6ca2-34d9-a3f9-18a78ec72989 | -2.8772 | -52.91003 | 2024-10-08 04:32:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ac1f3c9d-e916-31b4-9c53-7a6830b38ec7 | -2.87485 | -52.89759 | 2024-10-08 04:32:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |


[Clique aqui para ver as próximas entradas](README53.md)
