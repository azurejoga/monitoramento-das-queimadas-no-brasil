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

## Dados Diários - Página 43

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f4ff7487-060c-3b5f-b7d2-f191999f2e6a | -7.96748 | -50.68394 | 2024-11-30 04:40:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 01f4d7dd-a274-3337-8020-04f13f4259d6 | -2.009 | -51.16356 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 363f88dc-5f2a-3754-9f9a-e5b34c7ba50e | -3.22406 | -54.17788 | 2024-11-30 04:40:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| abe4dd06-b592-378a-bbdd-053c811b38fd | -2.56842 | -47.35606 | 2024-11-30 04:40:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 84852085-c8f0-38d2-8e01-61ac1194e70a | -2.72358 | -48.67686 | 2024-11-30 04:40:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 73c5d88c-c92a-322b-9f76-87fafed11292 | -1.09928 | -53.36512 | 2024-11-30 04:40:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 76af2c82-9a85-3469-9e40-ba7dfa94156e | -1.50772 | -52.56503 | 2024-11-30 04:40:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| cd2153be-c61d-351d-86c6-5b258c83ff86 | -3.29457 | -54.1305 | 2024-11-30 04:40:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| afa05730-82ba-3f44-8c7d-dfa521af03fe | -4.07352 | -46.69168 | 2024-11-30 04:40:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b19be44c-2201-3c81-a5df-e3de852b36bd | -4.36111 | -43.69437 | 2024-11-30 04:40:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a2e38be6-bd6c-3889-bc45-e700d969c5ac | -4.65532 | -43.92418 | 2024-11-30 04:40:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 76c03134-036d-36ec-872a-63c926fbd527 | -2.92838 | -49.43454 | 2024-11-30 04:40:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 76a17e03-7245-3d55-ba86-90aa7518904f | -3.27991 | -50.53399 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 690ce499-9cb8-351e-9813-0cee579cf8f0 | -3.07892 | -48.66918 | 2024-11-30 04:40:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5d6adfdb-1073-3620-8c75-9b96a05fa4cd | -2.9947 | -49.53334 | 2024-11-30 04:40:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 41ef9a5e-0443-3d7e-a7b8-93a707cf9207 | -0.98877 | -51.74938 | 2024-11-30 04:40:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 5.5 |
| f5c7d42b-b991-35a8-ad43-f90cf4c98678 | -3.9583 | -46.73424 | 2024-11-30 04:40:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f27e8b9d-6838-369c-89ea-96f467373627 | -2.47049 | -50.36446 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e9b8dfec-c8fc-393e-aa9c-54c69ed07ab5 | -1.32235 | -51.75028 | 2024-11-30 04:40:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| b2372e62-bc58-32db-ad8c-8fe04b6ba2d9 | -2.72626 | -48.65969 | 2024-11-30 04:40:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 550925c4-7e7e-3ecb-83e6-5865273a9d2b | -3.42989 | -50.31569 | 2024-11-30 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b8aac3f3-7db8-3407-8085-1deebec1b205 | -2.60329 | -48.24944 | 2024-11-30 04:40:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 68f6e07d-7762-3abb-9324-6afb2e87695c | -3.41311 | -50.24764 | 2024-11-30 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6b6bd412-8bf8-37b6-97de-88fc0a347399 | -4.18878 | -50.6756 | 2024-11-30 04:40:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5d249f43-786b-361a-a62b-5f7065d132ed | -3.99221 | -48.93895 | 2024-11-30 04:40:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| e681e770-2772-3db6-b82a-2275ecac59f8 | -3.9344 | -46.89087 | 2024-11-30 04:40:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 969df994-c114-34df-b26a-afa6444e3ea8 | -2.98986 | -53.355 | 2024-11-30 04:40:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b58e9093-17a3-31b2-b12e-6abe9484c301 | -4.01026 | -46.94431 | 2024-11-30 04:40:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| af444098-c188-3592-ab28-eee72144a03e | -3.81251 | -46.68581 | 2024-11-30 04:40:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 00711e86-2a9d-3231-bdf9-0119d751eee0 | -2.98181 | -53.2798 | 2024-11-30 04:40:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e54c7d01-672a-39f3-be4d-5ea5809dda73 | -3.85097 | -52.10384 | 2024-11-30 04:40:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 32ae447d-5fc0-3b9e-bba6-ce26863455c2 | -2.84505 | -46.61349 | 2024-11-30 04:40:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 17217c29-b2de-356d-8e75-51e0d4cb25c6 | -1.16059 | -50.68377 | 2024-11-30 04:40:00 | NOAA-21 | BREVES | PARÁ | Brasil | 1501808 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a9857eeb-d12e-3c9a-ad28-53678d4596d0 | -2.8376 | -49.53739 | 2024-11-30 04:40:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0ceb74e4-36e8-3b0c-8804-b6eaef1760e6 | -3.46737 | -48.92699 | 2024-11-30 04:40:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 11c5eb47-5d58-3533-9646-95428c1bcd5d | -1.09271 | -53.64651 | 2024-11-30 04:40:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9384bde3-f8d6-3a46-abd5-b39200447dce | -1.5346 | -51.62078 | 2024-11-30 04:40:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7782e979-06e5-3416-b4af-47845ba30024 | -3.35851 | -49.1001 | 2024-11-30 04:40:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 109a91e0-eab8-3498-bc88-8dd3c8debbab | -4.1508 | -47.8536 | 2024-11-30 04:40:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e647c8b2-4216-3474-969b-49d9ba0a5c0d | -3.24402 | -53.92728 | 2024-11-30 04:40:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 0f446e26-3a44-3029-9ebc-7324fe95164b | -4.19382 | -50.6874 | 2024-11-30 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 2a6020df-79c2-3334-ab91-5fd9a3b51473 | -3.59708 | -49.98766 | 2024-11-30 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 3e356da7-afff-387e-905b-4814c8f26e7a | -2.61728 | -54.21699 | 2024-11-30 04:40:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 422a3af4-8fa8-3e23-a486-bb2fc85e2b78 | -1.39595 | -46.49828 | 2024-11-30 04:40:00 | NOAA-21 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 09571441-75c7-38ac-afe3-a7d77a50cded | -4.356 | -48.69944 | 2024-11-30 04:40:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 023f63f3-b9e9-3573-863a-8181607b1b72 | -3.95599 | -49.75887 | 2024-11-30 04:40:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 2f753c1e-c114-3405-bf6d-2cabacdb1919 | -2.83219 | -54.09702 | 2024-11-30 04:40:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a79cf531-2efa-3028-b669-745660575169 | -3.43256 | -49.47454 | 2024-11-30 04:40:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6432a78a-49c1-3536-99d7-03303173070a | -3.12439 | -53.27701 | 2024-11-30 04:40:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| cae896c2-af72-3442-8aba-43e3afd84393 | -6.99292 | -45.62083 | 2024-11-30 04:40:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 93cd4573-0676-3d35-b8cb-fdb29fbc8d81 | -3.0664 | -50.33202 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 520dc446-e486-3246-961f-09ce8994dfa3 | -2.26264 | -50.3548 | 2024-11-30 04:40:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a38ada63-7ffc-375a-b38c-43bc274d6d17 | -1.66797 | -54.0224 | 2024-11-30 04:40:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 42aa0229-bbba-3d17-b39f-ae7489b14f56 | -1.32005 | -51.74141 | 2024-11-30 04:40:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2b13aa0d-0d4a-336e-9ea8-f2cb51885b21 | -2.61031 | -51.812 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| e2410422-ce87-3735-838c-1aca580d0630 | -8.37793 | -44.47561 | 2024-11-30 04:40:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| faa03f8c-6bdc-3a14-92b4-8c9ebdd63feb | -2.34693 | -53.81466 | 2024-11-30 04:40:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f294aa3b-3f65-36f5-8033-84dd004f53a9 | -3.28412 | -50.15825 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9e817c13-3b0b-31b3-ba57-734d938bb2e1 | -4.0449 | -46.83293 | 2024-11-30 04:40:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 154489c3-22a9-3e7a-b50e-0784200ba998 | -3.42439 | -45.34397 | 2024-11-30 04:40:00 | NOAA-21 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1faf5c5a-8963-3c8f-a9d1-83649ec6947c | -0.96804 | -51.71614 | 2024-11-30 04:40:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 4.3 |
| d409d71f-e724-36d0-a447-76095de58138 | -2.70018 | -46.12517 | 2024-11-30 04:40:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 185afaff-aefe-3abe-ab65-ad06b9acfe18 | -1.08917 | -53.64247 | 2024-11-30 04:40:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| daeb5e20-a661-39af-b289-17a59a7d60ba | -2.96034 | -50.57771 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| bc4d5aa7-d3db-330f-be72-143db7eff466 | -3.1174 | -50.29239 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 070a1bb1-1ed5-3687-81ff-b97ef10dbf4a | -2.71235 | -46.30681 | 2024-11-30 04:40:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8f101c28-7459-3b27-8bd9-9b8efef7efb0 | -2.66939 | -46.25337 | 2024-11-30 04:40:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| d0287f7f-d345-3e57-ab4e-1a70afbc7559 | -3.1136 | -53.27048 | 2024-11-30 04:40:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 261e6002-463c-370c-a7de-9f4066db1bd9 | -3.0612 | -48.5184 | 2024-11-30 04:40:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1f257bb8-50ba-3838-b6b1-d9d4d38617bc | -2.8338 | -49.84329 | 2024-11-30 04:40:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2d58d244-2800-38e3-b94c-d0bb614fede1 | -2.53376 | -46.24116 | 2024-11-30 04:40:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 00c95f1e-caec-3c71-8b9c-f64f8fe08649 | -3.23041 | -48.74251 | 2024-11-30 04:40:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b9072a70-eeb9-3f4a-bd7d-a3631b11a758 | -4.10431 | -51.02761 | 2024-11-30 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1c8517ec-5fa6-3490-8475-87908d147da5 | -3.93807 | -47.97682 | 2024-11-30 04:40:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 36d29ca8-1f66-3229-8cf7-8272c28e40bb | -3.25157 | -50.62589 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 68d438a8-f41c-3790-8baa-cc72a50945c0 | -2.46318 | -46.53748 | 2024-11-30 04:40:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 109b8c84-90b5-3d13-ac32-c3be94d88482 | -3.69656 | -47.13872 | 2024-11-30 04:40:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a5c25227-da6e-3958-abf4-3a13158c765f | -3.08135 | -53.28741 | 2024-11-30 04:40:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| cf060f30-9035-3012-b6be-32485ad89d2a | -1.31939 | -51.74557 | 2024-11-30 04:40:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 5c492e39-50df-344f-a764-293506ad64e5 | -3.20596 | -51.16074 | 2024-11-30 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e6b189b0-ddbe-3932-9e6e-2e2bb81e7049 | -2.79724 | -54.05457 | 2024-11-30 04:40:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 46b6e915-5959-36f7-9f96-e6e93c654265 | -2.94475 | -47.99969 | 2024-11-30 04:40:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| bc7c614b-dc65-3f1a-a46e-c9850accecf5 | -3.12054 | -45.98362 | 2024-11-30 04:40:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f7285209-a51f-3787-b72d-8304f69d4aab | -6.86934 | -47.23527 | 2024-11-30 04:40:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 837779ae-d7c5-30c8-81ef-f24ee61e0ebb | -2.61282 | -46.54847 | 2024-11-30 04:40:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2535882c-b7db-3c41-9a36-8e60297a4fa5 | -3.80935 | -46.61409 | 2024-11-30 04:40:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4865a170-4b9a-32a9-9dde-e269ddf2eebd | -1.35185 | -51.96652 | 2024-11-30 04:40:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 6c274bba-4d21-3bdf-b4db-3fa1ae8766f4 | -1.71083 | -52.47898 | 2024-11-30 04:40:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 01bf2e90-28f7-31c6-8e42-93b959354c86 | -2.91076 | -48.59031 | 2024-11-30 04:40:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 19e0db7f-d056-303a-9671-90bb326ccf55 | -0.82278 | -51.61081 | 2024-11-30 04:40:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 73e9a7c4-27e0-3687-9ddf-a1c5baf17a92 | -2.77251 | -48.56137 | 2024-11-30 04:40:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d818f17d-806a-336d-bbc2-b780331ca8ff | -5.17055 | -46.1695 | 2024-11-30 04:40:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2b92af37-3480-3170-9306-e216bf95fffa | -1.83019 | -54.53287 | 2024-11-30 04:40:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| a58c5000-225b-3b12-a81e-e8af99be3391 | -1.48815 | -52.41531 | 2024-11-30 04:40:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| d691367a-0229-3f58-992d-1ddc6620aa42 | -2.37663 | -48.61214 | 2024-11-30 04:40:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7f70b0dd-1cfa-37c2-8d70-29c3b4957930 | -2.5757 | -47.01593 | 2024-11-30 04:40:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d57c9ecf-f38c-3bcd-94d2-d0441401752b | -1.00297 | -51.73007 | 2024-11-30 04:40:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 40fc1f1c-6f45-3d9b-b998-f8ad3722456a | -4.0068 | -46.94378 | 2024-11-30 04:40:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d90bc8e2-3157-3e21-9fb9-6854df388f5e | -2.95695 | -50.57717 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 6d7d296f-8154-3753-b702-e60a90d6f5a4 | -3.94609 | -41.49373 | 2024-11-30 04:40:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |


[Clique aqui para ver as próximas entradas](README44.md)
