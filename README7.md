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

## Dados Diários - Página 7

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 663cc073-fcdc-3ec8-a40a-fb2beb0348aa | -3.07096 | -51.25159 | 2025-11-02 04:18:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 58c5c6d6-b268-3348-8a07-9fc99f8464a5 | -4.67946 | -44.61621 | 2025-11-02 04:18:00 | NOAA-21 | BERNARDO DO MEARIM | MARANHÃO | Brasil | 2101939 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| fd440395-819b-35f1-8c0c-9416f83a221b | -3.57086 | -45.21127 | 2025-11-02 04:18:00 | NOAA-21 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e28ed430-273d-3bd2-ba2b-33be7aa488ce | -4.71665 | -45.69158 | 2025-11-02 04:18:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 94f7821d-cce7-3b5c-b413-3324fdd05701 | -4.54485 | -45.79464 | 2025-11-02 04:18:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6c9c4778-3e2f-35e3-851e-f3c2c3cb74fa | -3.56619 | -54.58511 | 2025-11-02 04:18:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 286fc262-1705-3c86-9c00-f037678c5c26 | -3.65914 | -50.7066 | 2025-11-02 04:18:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| ea7db3d4-9835-3bab-ba1c-36cdb191ee56 | -0.45977 | -51.75721 | 2025-11-02 04:18:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 96329273-a06c-3e88-aeee-1dc77256d52c | -3.02008 | -49.44385 | 2025-11-02 04:18:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 3b5d5ebe-863b-3425-855a-2465a68f5503 | -4.62893 | -45.84122 | 2025-11-02 04:18:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 3.3 |
| a7b20fe8-072c-399d-8c70-c86d55758b06 | -2.2558 | -47.67517 | 2025-11-02 04:18:00 | NOAA-21 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e088db4a-aa26-3852-9eb8-f19914b9bd8e | -3.02681 | -51.22378 | 2025-11-02 04:18:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 0cb0fcbb-be6f-3720-98ee-55392b675c57 | -3.36091 | -49.24885 | 2025-11-02 04:18:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9e4990ff-23e3-3c64-9011-431b14c22571 | -0.84215 | -48.61422 | 2025-11-02 04:18:00 | NOAA-21 | SALVATERRA | PARÁ | Brasil | 1506302 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 6e82bcae-0dc3-3034-96a2-999d47bf189d | -3.89507 | -52.21156 | 2025-11-02 04:18:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| e9454247-7471-3609-9ffd-3c0900895a3c | -4.58343 | -44.79251 | 2025-11-02 04:18:00 | NOAA-21 | BERNARDO DO MEARIM | MARANHÃO | Brasil | 2101939 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2647a7a9-45ce-30f2-8c1e-59f00d4fb2c0 | -5.30624 | -41.90408 | 2025-11-02 04:18:00 | NOAA-21 | NOVO SANTO ANTÔNIO | PIAUÍ | Brasil | 2206951 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| df0b13d2-25ba-35d1-9511-8067e98703e5 | -4.32366 | -45.64078 | 2025-11-02 04:18:00 | NOAA-21 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 523cfedd-139d-3221-9599-6289ba8afcf8 | -4.13537 | -51.13986 | 2025-11-02 04:18:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 58476726-49cf-31e0-b3ff-d3f6dfc7f941 | -2.44796 | -49.03564 | 2025-11-02 04:18:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b74359ef-4eda-3e02-9127-b8e5f45527ad | -4.6846 | -45.66402 | 2025-11-02 04:18:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d29b2640-5cd5-3243-881b-776975a56f99 | -4.33529 | -40.18776 | 2025-11-02 04:18:00 | NOAA-21 | SANTA QUITÉRIA | CEARÁ | Brasil | 2312205 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| cbe9f3eb-df14-3c7b-867b-c4600864ab97 | -2.83595 | -49.40038 | 2025-11-02 04:18:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3c893822-20e2-3a1a-aeae-947c64216caa | -4.00191 | -47.73058 | 2025-11-02 04:18:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d803f1d6-6159-37da-82eb-c5c3908c0bb1 | -4.29684 | -45.89798 | 2025-11-02 04:18:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5f78457e-e10d-36d0-9b8f-bb59fa9c6265 | -2.44856 | -49.03193 | 2025-11-02 04:18:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| c58440c0-cc8c-3da0-a1fd-b0341fd21951 | -3.37986 | -49.97617 | 2025-11-02 04:18:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 584e8e91-fd09-38a5-9cad-7e5d010f53cd | -3.30943 | -50.01642 | 2025-11-02 04:18:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 846da126-6757-38cd-bda1-a0a6e1ed414c | -4.50081 | -45.78777 | 2025-11-02 04:18:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 33f74e6f-14c4-3c61-85cc-797934c8b740 | -4.14272 | -51.145 | 2025-11-02 04:18:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5b13cef7-2da0-3d07-8252-19eb4d87be34 | -3.50679 | -54.37622 | 2025-11-02 04:18:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 2c424263-ccdc-324d-9d1e-1529a421c797 | -2.83114 | -49.40346 | 2025-11-02 04:18:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 21e3aea4-2a06-38ca-99af-cd9a18d50709 | -4.13455 | -51.14497 | 2025-11-02 04:18:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 4f259ad5-9f7d-3172-ab2b-07d74367ac6e | -4.27027 | -48.7182 | 2025-11-02 04:18:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 70509a9d-3062-3154-8d46-c8114a6ca775 | -3.79555 | -48.91589 | 2025-11-02 04:18:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7cd2d9fb-2c24-3eba-960b-15ec1a20eef3 | -6.0974 | -35.36472 | 2025-11-02 04:18:00 | NOAA-21 | MONTE ALEGRE | RIO GRANDE DO NORTE | Brasil | 2407807 | 24 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 417f64bb-2eab-309a-8717-d99c01697218 | -3.24055 | -50.79295 | 2025-11-02 04:18:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| a960711b-9e3d-3205-b365-52be206d6ecf | -3.91254 | -50.03571 | 2025-11-02 04:18:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 71e2da4c-c312-387d-ad9d-53971daea1b5 | -2.31167 | -48.58607 | 2025-11-02 04:18:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6cfee58b-9e8f-3e81-81a6-14bf9e65072a | -5.0725 | -43.6696 | 2025-11-02 04:18:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c2ec9513-b300-330e-b7b5-51334de1c224 | -3.77406 | -51.34664 | 2025-11-02 04:18:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 67b9cf98-a2d9-3152-af9c-1bd5d6bd49fe | -6.09786 | -35.36148 | 2025-11-02 04:18:00 | NOAA-21 | MONTE ALEGRE | RIO GRANDE DO NORTE | Brasil | 2407807 | 24 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 31ac7f4a-3de9-3b8b-a0cc-ce56c51a062d | -4.37328 | -49.74511 | 2025-11-02 04:18:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 94ed6d02-daf1-3ff5-a360-0945f72207ee | -4.54204 | -45.79047 | 2025-11-02 04:18:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e6c4d8b1-a1ef-3c80-9be8-cc1dabf6769d | -4.90073 | -44.63721 | 2025-11-02 04:18:00 | NOAA-21 | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 29fee423-b8fe-3731-b5d8-43445d01dc7a | -4.13806 | -51.14439 | 2025-11-02 04:18:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 23d2860d-5966-3c00-8c89-1701d955cb34 | -4.01893 | -50.46117 | 2025-11-02 04:18:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7c0fe3f0-14a3-35b6-8113-6cdd62809ea7 | -3.57131 | -50.26844 | 2025-11-02 04:18:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| fad68aee-1190-3063-b2a1-dd82b6e340b6 | -3.41054 | -44.26719 | 2025-11-02 04:18:00 | NOAA-21 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b211f56b-63e4-33c2-a470-3e921bb87039 | -3.71143 | -53.37288 | 2025-11-02 04:18:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 54df0b39-867e-396f-9204-19879f7f1dab | -5.52552 | -41.09489 | 2025-11-02 04:18:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 26041c47-a648-3698-b50e-3bc86bf107b8 | -3.36152 | -49.24517 | 2025-11-02 04:18:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 18d7003d-7abe-31f0-9a89-ff7f00677e88 | -3.01168 | -49.44254 | 2025-11-02 04:18:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5941a3db-af8c-3b2d-b7af-f0ee2c04bc77 | -3.5216 | -50.32254 | 2025-11-02 04:18:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 33a9d172-afd5-3ff1-a3f6-7600376dfb4f | -0.83861 | -48.60991 | 2025-11-02 04:18:00 | NOAA-21 | SALVATERRA | PARÁ | Brasil | 1506302 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 17bfa41c-ac44-3721-8cbf-200900231799 | -5.20623 | -40.97791 | 2025-11-02 04:18:00 | NOAA-21 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| d2995c2f-c599-396c-869c-381fd8212c21 | -2.31223 | -48.58256 | 2025-11-02 04:18:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 3c42c8e4-16ac-32da-aa1e-74f8042c18ef | -0.46443 | -51.76109 | 2025-11-02 04:18:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9abdc0e4-5ec7-31c5-bbc9-9903ebc5d3a8 | -4.71943 | -45.69576 | 2025-11-02 04:18:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 6.2 |
| d8d5e896-a649-322a-bbcc-64c56a992d33 | -4.83953 | -45.75541 | 2025-11-02 04:18:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| abc3184e-d7dd-35ab-9b3c-6f740fdc5119 | -5.12176 | -43.37495 | 2025-11-02 04:18:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 643422fe-06da-3997-8eb1-e3d008a31309 | -3.82268 | -52.36431 | 2025-11-02 04:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 156b1fd2-18ab-3626-a4bc-f043c6b4ebc8 | -4.30024 | -45.89855 | 2025-11-02 04:18:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 4.5 |
| b4cf8969-7773-31df-8688-6a2edf77e751 | -3.50635 | -50.46931 | 2025-11-02 04:18:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 2f84e272-58dd-3959-bbc2-41e88bf6160c | -5.06919 | -43.66909 | 2025-11-02 04:18:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e8aa583e-6562-3822-af9e-b20bd016eaf7 | -3.9349 | -52.1884 | 2025-11-02 04:18:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 343af82b-6ae8-3c47-9471-6711bb896708 | -4.65813 | -45.67852 | 2025-11-02 04:18:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b1f1e3be-24b7-3650-a418-76fb09756bda | -3.65461 | -50.70583 | 2025-11-02 04:18:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 62da57e6-f3e4-3420-ab61-559cf56028de | -2.26867 | -47.85748 | 2025-11-02 04:18:00 | NOAA-21 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0d1d575a-9ef2-3c9b-b6a5-2a19415725b1 | -4.66151 | -45.67902 | 2025-11-02 04:18:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8f38ccb3-8534-3450-a87d-4aa280e42081 | -4.73243 | -45.67927 | 2025-11-02 04:18:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a8bf6714-79fb-3623-a5fa-b6e058d83e38 | -5.13118 | -43.37999 | 2025-11-02 04:18:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ebdbcd9a-3a88-3ae7-aeed-d32fd2838d47 | -4.31633 | -45.64336 | 2025-11-02 04:18:00 | NOAA-21 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 08cf9b52-e997-3306-8437-32b79e3083a1 | -3.66785 | -51.71743 | 2025-11-02 04:18:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9027f490-31b1-3e0a-97cc-793a748df5c5 | -3.77493 | -51.34148 | 2025-11-02 04:18:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| aae4a6ef-e853-335f-839e-abe5dd36c5d1 | -3.78085 | -43.92469 | 2025-11-02 04:18:00 | NOAA-21 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d0928137-9add-3924-aa5d-2d5af7dbf287 | -4.48371 | -46.07109 | 2025-11-02 04:18:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e171e7c0-2e95-3c93-8407-0afff59d0165 | -4.11956 | -49.1578 | 2025-11-02 04:18:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8b2e3785-6402-3db4-a013-9bbdf77d573a | -6.10317 | -35.36234 | 2025-11-02 04:18:00 | NOAA-21 | MONTE ALEGRE | RIO GRANDE DO NORTE | Brasil | 2407807 | 24 | 33 | nan | nan | nan | Caatinga | 0.6 |
| e6bb6039-7316-3e12-ad94-9887e6e8e833 | -5.43138 | -43.17531 | 2025-11-02 04:18:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 054b5e12-ac1d-3776-8cd3-436a4405cc30 | -5.52253 | -41.09016 | 2025-11-02 04:18:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 1213b92d-a87b-3e9a-86bd-9f23267a8cdc | -4.50361 | -45.79198 | 2025-11-02 04:18:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| bb169d5a-c8ef-3057-8088-f7689c41d72e | -3.58593 | -50.26196 | 2025-11-02 04:18:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0281b5cd-1bf6-3107-8f8b-db8974aec3f2 | -4.23427 | -45.8095 | 2025-11-02 04:18:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fa09af9c-73a9-3638-aab7-11ddb40e5e09 | -4.69535 | -43.40427 | 2025-11-02 04:18:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 14e3851e-cb4d-33ff-aa3b-a184561a51f5 | -4.30699 | -45.746 | 2025-11-02 04:18:00 | NOAA-21 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a388a1c1-c23b-311b-8bcb-defa8619c73f | -3.24592 | -50.78898 | 2025-11-02 04:18:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| a33de48d-93f7-3f20-9086-545f0a87e189 | -4.58121 | -44.78505 | 2025-11-02 04:18:00 | NOAA-21 | BERNARDO DO MEARIM | MARANHÃO | Brasil | 2101939 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a196c22c-bef9-35a2-bcab-e26fbb132067 | -4.12284 | -49.16656 | 2025-11-02 04:18:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f455b11f-037b-3d3a-b3a3-37020e5f09f3 | -2.37672 | -47.72041 | 2025-11-02 04:18:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| ae5ba221-9655-37af-9da3-12110b5acb93 | -3.57029 | -45.21483 | 2025-11-02 04:18:00 | NOAA-21 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1f998a51-b536-3417-92f0-8565d3cc6e9e | -2.34268 | -47.5455 | 2025-11-02 04:18:00 | NOAA-21 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ae4cabeb-2ce3-3ed7-96de-9c381f41b6a4 | -3.45634 | -45.57293 | 2025-11-02 04:18:00 | NOAA-21 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ee6c12e4-6bd0-3dae-89fb-2c41972ea68c | -3.77319 | -51.34296 | 2025-11-02 04:18:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 4a501489-43a8-3cb3-9c86-afa52f10f8d1 | -3.41619 | -49.9988 | 2025-11-02 04:18:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8626982c-009d-3765-bc5b-3566566257d1 | -4.89742 | -44.6367 | 2025-11-02 04:18:00 | NOAA-21 | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 38da8e9c-e3d8-3ad3-ad53-f97de40dd6a6 | -3.16001 | -50.82535 | 2025-11-02 04:18:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ed85f7ad-9d67-307e-81b8-e5cc1bbbe9c0 | -4.72619 | -45.69674 | 2025-11-02 04:18:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e0c86714-4bd2-3e23-84ae-79875a2993dd | -5.13014 | -42.87793 | 2025-11-02 04:18:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ad53c596-cd70-3223-a977-efac235a0add | -5.81625 | -35.57136 | 2025-11-02 04:18:00 | NOAA-21 | IELMO MARINHO | RIO GRANDE DO NORTE | Brasil | 2404606 | 24 | 33 | nan | nan | nan | Caatinga | 1.5 |


[Clique aqui para ver as próximas entradas](README8.md)
