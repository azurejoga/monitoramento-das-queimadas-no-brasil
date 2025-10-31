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

## Dados Diários - Página 33

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 96f2c3f3-3bca-3473-8405-c0ba7656486a | -5.21332 | -50.67558 | 2025-10-31 04:55:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6ae17a75-8575-3082-b6a7-4709b66992b7 | -4.85771 | -42.73385 | 2025-10-31 04:55:00 | NOAA-21 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 50924027-9515-364f-aeb2-55eb44fe9f09 | -3.77011 | -51.71191 | 2025-10-31 04:55:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 56e724fb-b465-3d41-b569-bdaffdf9db89 | -2.66873 | -49.12744 | 2025-10-31 04:55:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cbb124b8-d06a-377b-a954-8bd4ab1524d8 | -6.05525 | -44.86415 | 2025-10-31 04:55:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1b8e59ee-dd80-3758-9e62-a36b83a4d18c | -5.71169 | -44.53308 | 2025-10-31 04:55:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 16aae4db-6c35-3b03-a5e3-44302b59d87b | -4.86765 | -48.59687 | 2025-10-31 04:55:00 | NOAA-21 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b67bea20-8865-3879-ac90-ad9144a1c0ef | -5.41869 | -47.94622 | 2025-10-31 04:55:00 | NOAA-21 | SAMPAIO | TOCANTINS | Brasil | 1718808 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| f6921a61-d77d-3aaf-b684-8a2182315f7c | -4.67874 | -45.8063 | 2025-10-31 04:55:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 452f3df0-66d5-3824-9783-49ffb443684d | -5.41988 | -47.93815 | 2025-10-31 04:55:00 | NOAA-21 | SAMPAIO | TOCANTINS | Brasil | 1718808 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| bd357fed-f86b-3e70-8a76-ac271ec6095a | -3.92994 | -52.2327 | 2025-10-31 04:55:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 4e78682d-e183-398d-a3ca-dc325ecf1586 | -2.42209 | -49.29945 | 2025-10-31 04:55:00 | NOAA-21 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 87eb596a-e988-32dc-b16a-84cffefccd2d | -5.23304 | -45.47086 | 2025-10-31 04:55:00 | NOAA-21 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2f5e3138-af54-3a32-b793-7c6a825cf9c2 | -6.55398 | -44.02274 | 2025-10-31 04:55:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8c63f7df-77e8-306b-ad71-618032efb749 | -4.43052 | -48.01289 | 2025-10-31 04:55:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 19c67c6f-f926-33cf-8737-2e19ad06743c | -2.49324 | -48.15052 | 2025-10-31 04:55:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 1aed965e-2fe4-3065-b53a-9dba3e07bf39 | -2.76281 | -45.39156 | 2025-10-31 04:55:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c13fe12c-f47d-3be4-beb5-82d59b015701 | -2.3239 | -48.58579 | 2025-10-31 04:55:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 11.8 |
| e21aa659-3578-304a-8821-9ae37f82cf32 | -4.25741 | -50.67429 | 2025-10-31 04:55:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| caa5f7da-e336-3911-95e6-8ff7e66ad073 | -5.41929 | -47.94219 | 2025-10-31 04:55:00 | NOAA-21 | SAMPAIO | TOCANTINS | Brasil | 1718808 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 4437ce5c-1794-31f4-893b-8197eb6768a1 | -4.65505 | -46.47619 | 2025-10-31 04:55:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c1be9d71-a046-3b40-a6af-a4dd443586d8 | -2.04647 | -52.07471 | 2025-10-31 04:55:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 29342e5b-428c-3134-abe7-1d0fab2f0de8 | -3.24366 | -48.88059 | 2025-10-31 04:55:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0b1f8119-697b-3053-af2d-bbab682f63eb | -5.17147 | -45.33192 | 2025-10-31 04:55:00 | NOAA-21 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 65a37959-35a2-327f-86b0-5662d9d71fad | -3.77483 | -48.92665 | 2025-10-31 04:55:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 820db11a-adb1-3094-8118-9a5a11610d79 | -3.89482 | -52.13254 | 2025-10-31 04:55:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 46b07444-70b2-3230-8157-f3208b4b127d | -3.59615 | -51.54306 | 2025-10-31 04:55:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| be14d31f-7202-380a-8948-1c17cc97ff7f | -2.09734 | -54.39869 | 2025-10-31 04:55:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2d5026d1-ea4c-3ddf-9f15-af8ab4222411 | -2.20191 | -51.36591 | 2025-10-31 04:55:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d2e98b54-5475-3e1c-824e-b81484290618 | -3.53446 | -47.5514 | 2025-10-31 04:55:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 70f62dcf-6f08-3533-9b6d-22da144d328f | -3.2501 | -51.37741 | 2025-10-31 04:55:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| cee57bd1-dd87-3741-a40e-7a403935bb55 | -6.07004 | -47.28687 | 2025-10-31 04:55:00 | NOAA-21 | RIBAMAR FIQUENE | MARANHÃO | Brasil | 2109551 | 21 | 33 | nan | nan | nan | Cerrado | 30.1 |
| 19ee79bb-07a5-33f4-9360-b042c3b9179e | -2.92043 | -48.72811 | 2025-10-31 04:55:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 86bb294a-ac90-395e-9af1-9719582d02f6 | -3.52177 | -51.52786 | 2025-10-31 04:55:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 98bcb222-3bda-3788-a9d5-a0fb6475ec3e | -3.49271 | -52.35598 | 2025-10-31 04:55:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 3efc19b0-fee2-3912-97c6-d371b73fdf00 | -4.47762 | -46.56253 | 2025-10-31 04:55:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c854e12b-dfb5-39c6-b4f4-c6093432eacc | -6.19723 | -42.52139 | 2025-10-31 04:55:00 | NOAA-21 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 5.3 |
| c88b96ae-7a61-3d04-8e57-1ea40b29e9cb | -4.79797 | -46.46454 | 2025-10-31 04:55:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 5ecd6279-d7c5-391a-8510-6c296a079a9f | -5.71394 | -44.53366 | 2025-10-31 04:55:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a41dc859-1548-352a-a05b-9c9679a307fd | -5.31848 | -44.84141 | 2025-10-31 04:55:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c34cb740-57b9-3287-9839-4244ac88ea3b | 0.34561 | -50.92518 | 2025-10-31 04:55:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b8b927fb-7fa1-35aa-9143-62a7a5669531 | -4.85109 | -42.73725 | 2025-10-31 04:55:00 | NOAA-21 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 9.2 |
| b66f33b8-48af-3928-8465-eba029a6e63d | -4.67228 | -46.42432 | 2025-10-31 04:55:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 3.4 |
| ffeeffcc-7ff3-367d-bfe3-188aa6546185 | -5.25772 | -45.5132 | 2025-10-31 04:55:00 | NOAA-21 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| cde806fe-e986-390f-8215-bed918cc083b | -3.66449 | -51.71403 | 2025-10-31 04:55:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c3379e53-518e-3ffa-bf57-9a0053696e69 | -3.00646 | -44.96468 | 2025-10-31 04:55:00 | NOAA-21 | OLINDA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2107456 | 21 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 0c4779a1-121b-34a7-b120-dcaf1196bd44 | -4.89228 | -45.86642 | 2025-10-31 04:55:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ea3fe598-662e-3401-9491-7de9767a2b19 | -3.54553 | -49.32686 | 2025-10-31 04:55:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5799ec59-4c25-343e-a37f-b45af4bf8c98 | -3.30267 | -51.91753 | 2025-10-31 04:55:00 | NOAA-21 | VITÓRIA DO XINGU | PARÁ | Brasil | 1508357 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 450c2382-1af1-3f14-b9ea-21c3c94de537 | -1.82211 | -55.35892 | 2025-10-31 04:55:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| fed387b3-96c9-39fb-b9e9-3ce4b94f13db | -3.65041 | -48.97354 | 2025-10-31 04:55:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 00b98d31-a06a-3e26-a769-7a87352eac1a | -2.32464 | -48.58089 | 2025-10-31 04:55:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 11.8 |
| 0812771a-e7be-34e0-9310-e7f08547dff4 | -4.71834 | -45.87752 | 2025-10-31 04:55:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e669c108-6aff-3f6c-9586-d3b0ca1c6fe2 | -3.24672 | -48.87911 | 2025-10-31 04:55:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5b12f91a-c69c-38b9-a779-ad7ca6fd062f | -2.83755 | -48.10451 | 2025-10-31 04:55:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a3e7bce0-fa6f-309a-bcdb-6f32f3ea0b95 | -2.91686 | -53.95023 | 2025-10-31 04:55:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a045c8e4-1b63-3e56-875f-a19d360de53d | -3.60458 | -50.63006 | 2025-10-31 04:55:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 6b612b35-a7ca-33a8-b443-3510bcb0a38a | -1.71126 | -55.26059 | 2025-10-31 04:55:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| aa63cf72-af3c-3e83-8c91-811ab5651b08 | -5.31277 | -44.84372 | 2025-10-31 04:55:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e20da78c-6ee9-385d-9848-32984b0bb673 | -4.31027 | -49.29062 | 2025-10-31 04:55:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 516a0d2e-bf46-3df2-89d2-56da5fe39373 | -3.14705 | -49.42094 | 2025-10-31 04:55:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 6f8a066f-3882-31bb-9f2a-1935f604b7ac | -6.09435 | -47.2159 | 2025-10-31 04:55:00 | NOAA-21 | LAJEADO NOVO | MARANHÃO | Brasil | 2105989 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 932f7eec-d078-3495-a46e-14a35948219b | -4.90615 | -42.97599 | 2025-10-31 04:55:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| add3e4c6-ad08-3878-adcf-cb7c1e04dbcd | -6.0153 | -41.96694 | 2025-10-31 04:55:00 | NOAA-21 | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| b0cbf5ae-e051-3e47-8a71-6f2e9cfdea28 | 1.28749 | -60.43897 | 2025-10-31 04:55:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 94cd62e0-6c3b-3be1-b448-9089fb76baaf | -4.66023 | -55.95342 | 2025-10-31 04:55:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fdf9d0f8-8702-33cb-9e82-e89d877bd3e7 | -4.31596 | -48.08242 | 2025-10-31 04:55:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| aee77d99-70b8-32a1-9482-301f678c931b | -4.9269 | -48.56455 | 2025-10-31 04:55:00 | NOAA-21 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 835ce92e-bf75-316c-a473-620b4886afe1 | -5.70766 | -48.88566 | 2025-10-31 04:55:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 08a709e2-7609-3a8d-9a52-68ea5a12f812 | -5.28567 | -45.42042 | 2025-10-31 04:55:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 85b618b5-9d95-32d7-ae5d-0c3a48bb5f9f | -2.64136 | -48.50251 | 2025-10-31 04:55:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 29bdde8f-4e3f-3c12-86b3-e095331e5df1 | -5.31894 | -44.83819 | 2025-10-31 04:55:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7d1c2676-1cac-3544-89cc-62b9636bd4f8 | -3.1142 | -53.23123 | 2025-10-31 04:55:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c9d9f8f1-36f7-3691-9ffc-8209c4a6bc27 | -4.83443 | -45.32462 | 2025-10-31 04:55:00 | NOAA-21 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 34a6a2ca-2367-3dc4-bc1f-e275c32f0188 | -6.10893 | -41.71603 | 2025-10-31 04:55:00 | NOAA-21 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 34da5755-503c-3564-82e9-a259ca5de225 | -5.23262 | -45.47377 | 2025-10-31 04:55:00 | NOAA-21 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| beab1760-d917-39b2-9887-fac91d9fb7df | -6.13183 | -41.69302 | 2025-10-31 04:55:00 | NOAA-21 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 905c6dd7-158a-34cd-b7c1-7181b87d8523 | -6.25419 | -42.55949 | 2025-10-31 04:55:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 11b73dec-8239-3bae-84e9-dc05d5d18d95 | -5.47262 | -44.31619 | 2025-10-31 04:55:00 | NOAA-21 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 530ba699-b402-30f4-a3d3-0b115cb995f4 | -5.26205 | -45.51564 | 2025-10-31 04:55:00 | NOAA-21 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 601e34cc-f0d6-3eaf-b4ca-342777a68fa1 | -6.13034 | -41.70428 | 2025-10-31 04:55:00 | NOAA-21 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 1c55f7e7-006c-39d4-b574-a2d67579b055 | -5.41502 | -47.94154 | 2025-10-31 04:55:00 | NOAA-21 | SAMPAIO | TOCANTINS | Brasil | 1718808 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 2a98407b-32e0-34c9-a64e-2d4692fb1701 | -4.67024 | -45.81025 | 2025-10-31 04:55:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 41c74775-3e4a-3c82-941d-8365d1d05486 | -2.44735 | -49.02953 | 2025-10-31 04:55:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 62934efb-7ffe-3bac-9259-0f76a866a652 | -2.05312 | -52.07574 | 2025-10-31 04:55:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b31a3b4e-a2ad-3a89-9eea-da658a820863 | -3.29875 | -51.9206 | 2025-10-31 04:55:00 | NOAA-21 | VITÓRIA DO XINGU | PARÁ | Brasil | 1508357 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| adb6be57-b27d-3f46-a77a-df04a68da935 | -3.9383 | -46.9693 | 2025-10-31 04:55:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 3.4 |
| d6f51de1-273f-341f-9ded-b04aa8847d2a | -3.1501 | -49.42606 | 2025-10-31 04:55:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 65a0a1a0-3c82-3a64-82fe-7392f490c754 | -6.09096 | -47.2173 | 2025-10-31 04:55:00 | NOAA-21 | LAJEADO NOVO | MARANHÃO | Brasil | 2105989 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 9b0bd4cc-e0d0-3bc5-9013-156f871a4a7c | -4.57185 | -46.94476 | 2025-10-31 04:55:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 315a2a9a-81e4-338e-9ab5-7e430ab81307 | -3.52655 | -47.54617 | 2025-10-31 04:55:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| e7cdda06-324c-3841-99a6-d81fefdac6b0 | -3.91958 | -52.2599 | 2025-10-31 04:55:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bf66997e-f0a7-3f97-b139-87fc23919a93 | -5.79107 | -40.80627 | 2025-10-31 04:55:00 | NOAA-21 | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 65f009d1-44a3-3ff4-ad69-a8eef2ddbaf1 | -3.04093 | -49.51495 | 2025-10-31 04:55:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5af8434a-8067-3d33-b5f7-a2395b8db557 | -3.88138 | -51.19482 | 2025-10-31 04:55:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 4ca103cc-3a10-30ac-aa2e-9e66fb32541c | -4.2328 | -55.66302 | 2025-10-31 04:55:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9b85da3e-55c1-30a4-9d14-08671c4e4cf3 | -3.48149 | -52.79948 | 2025-10-31 04:55:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 0595224a-6a6f-313e-8ebf-71bc904c3b09 | -0.3873 | -52.04396 | 2025-10-31 04:55:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0d14f9ec-ecf3-3fce-8b1f-436f48349aa0 | -5.74432 | -45.58148 | 2025-10-31 04:55:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0d8fac21-e452-3770-8522-d35a60e08812 | -2.45043 | -49.03479 | 2025-10-31 04:55:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |


[Clique aqui para ver as próximas entradas](README34.md)
