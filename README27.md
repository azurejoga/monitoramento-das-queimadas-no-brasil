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

## Dados Diários - Página 27

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5a605bfd-c338-35c1-9b97-f50113d03a2d | -8.03922 | -54.8977 | 2025-09-22 04:38:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 676bfe47-dc2b-30de-bac4-3de552276033 | -3.84696 | -51.33811 | 2025-09-22 04:38:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 52830dc2-755b-3a2b-94d5-d208e83ff107 | -7.59798 | -44.48012 | 2025-09-22 04:38:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1cabf1be-e79d-3822-bc5d-3c01044a5bdb | -3.75995 | -54.81127 | 2025-09-22 04:38:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c28c3929-1717-37dc-9816-e868875d385f | -7.8154 | -46.48488 | 2025-09-22 04:38:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7ab55e19-1ed6-3f7d-8b29-19cc55cb8b04 | -7.93932 | -44.1104 | 2025-09-22 04:38:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 95e14cf5-762f-3b20-b495-7e25ee32e67a | -9.14174 | -44.83086 | 2025-09-22 04:38:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f77cd19d-eb44-3514-aabb-4f80f2ec5fa2 | -5.3293 | -44.82339 | 2025-09-22 04:38:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| dca7e558-f97b-3797-bad4-747834825541 | -7.84979 | -45.14618 | 2025-09-22 04:38:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e31e1491-0aed-32e9-b284-e630f91e2985 | -5.6487 | -51.46981 | 2025-09-22 04:38:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0fc2f941-a8f6-3796-b18c-5cf211748868 | -5.65563 | -51.47092 | 2025-09-22 04:38:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 5322b155-7a32-34d7-92c7-3e6c4e03d831 | -7.6132 | -44.48988 | 2025-09-22 04:38:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7feb78db-4b63-3e03-a5b5-b50ca609c012 | -6.71785 | -47.20226 | 2025-09-22 04:38:00 | NOAA-20 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 3ca22715-37c3-39bd-9d03-2f01abd7787e | -8.84717 | -43.01833 | 2025-09-22 04:38:00 | NOAA-20 | SÃO BRAZ DO PIAUÍ | PIAUÍ | Brasil | 2209559 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| bab67e25-0306-3f00-92ec-b71338ee70d1 | -7.80262 | -46.19861 | 2025-09-22 04:38:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f280ba45-f56f-3cd6-858e-ac490ea91f5f | -3.49334 | -52.90405 | 2025-09-22 04:38:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 39f18299-7e0c-3c79-9aab-e73440722817 | -7.96199 | -43.89684 | 2025-09-22 04:38:00 | NOAA-20 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f2ffee11-0154-3e87-b01a-85ae2cc94b14 | -8.84963 | -46.15488 | 2025-09-22 04:38:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 72d66225-fdf7-376b-9808-d910d9437ebf | -10.25645 | -46.06094 | 2025-09-22 04:38:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 168f2595-3f4e-33bd-9e5b-a118e113e8d7 | -7.62582 | -46.82395 | 2025-09-22 04:38:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a44edf57-1e3b-32da-a935-3973f31fd549 | -6.38789 | -50.91325 | 2025-09-22 04:38:00 | NOAA-20 | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0cf66206-695f-3c99-8fdc-d727dcf40877 | -6.03599 | -44.1387 | 2025-09-22 04:38:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2bd0e7e3-5178-3201-a3f4-d87ee30239ae | -3.681 | -45.38444 | 2025-09-22 04:38:00 | NOAA-20 | SANTA INÊS | MARANHÃO | Brasil | 2109908 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 43c40186-a481-3a2b-9977-11e59434b2c9 | -7.66509 | -61.1264 | 2025-09-22 04:38:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8d1c2036-79cb-3989-b0d6-6c93e11ca872 | -7.9357 | -44.1059 | 2025-09-22 04:38:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2df66d2d-2b10-37b1-a1e2-f50e693b5311 | -6.01133 | -44.33452 | 2025-09-22 04:38:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 039dfe4f-515e-39b9-8e42-071d72624572 | -10.37747 | -46.0802 | 2025-09-22 04:38:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| a9856d07-ec0e-3db0-8d6a-ad9afacfd44b | -7.35531 | -44.55125 | 2025-09-22 04:38:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 965577b5-1afa-3bc6-804b-74b6370be804 | -5.55819 | -46.28051 | 2025-09-22 04:38:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f677d92f-076b-3e70-8198-9bd2c081030b | -10.37949 | -46.06599 | 2025-09-22 04:38:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 069c1640-6a31-3cf8-9db3-83e4bd765d59 | -4.31162 | -48.09216 | 2025-09-22 04:38:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 94cb127e-b030-3c47-aca7-52358e95423a | -3.55423 | -52.20083 | 2025-09-22 04:38:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 32360fa9-9dee-32a8-a0cf-eda30a77925e | -6.59008 | -62.92487 | 2025-09-22 04:38:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| df60319a-2eee-3737-98e2-3b22f97b4152 | -10.32436 | -46.10426 | 2025-09-22 04:38:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 25e8f944-e828-30c4-8e12-9831bcb803bc | -4.25518 | -48.60173 | 2025-09-22 04:38:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 8678b0ff-75f0-3f5f-b3ef-b3c46f5c6c4a | -4.07969 | -55.79578 | 2025-09-22 04:38:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5c492bf4-14fc-39e1-91d1-f869ef12b060 | -6.55571 | -43.82965 | 2025-09-22 04:38:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| af5275c7-e86f-379e-9b5b-fe90f47f9147 | -4.77596 | -43.72142 | 2025-09-22 04:38:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 39438307-aee0-37c5-8b3d-bed8d1ef66a4 | -7.47505 | -44.38524 | 2025-09-22 04:38:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9fd2ed44-5f98-3399-ac1e-bdbf86067e2e | -10.36706 | -46.05263 | 2025-09-22 04:38:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7c9f2c7b-18d7-3ec2-a0f9-8d155cd2b316 | -7.3568 | -44.54084 | 2025-09-22 04:38:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1653c9b7-4bb1-3ec7-9b50-175c795f0add | -5.06386 | -40.47477 | 2025-09-22 04:38:00 | NOAA-20 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 88a1e62c-45a2-3d4d-8b1a-2b5800227b1c | -6.11895 | -51.73594 | 2025-09-22 04:38:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b816b902-fd08-3092-ae26-388c1d3760fb | -5.10604 | -49.47445 | 2025-09-22 04:38:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f4b77c61-39c1-396c-8772-382bf79d01a0 | -5.66817 | -51.65803 | 2025-09-22 04:38:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3a2df876-9c1a-3e5a-bbb6-c2b5f5beed96 | -4.87177 | -45.81016 | 2025-09-22 04:38:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5427962d-fcff-3eb8-8a3a-4e35e23b55c8 | -10.28159 | -46.67965 | 2025-09-22 04:38:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a837508d-0b79-3f94-818b-e1a9d4607eda | -7.35432 | -44.55812 | 2025-09-22 04:38:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9d6c1f08-61bc-3783-8615-378dcaa1eb69 | -10.65403 | -44.23745 | 2025-09-22 04:38:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7327b58c-a29d-3e59-838f-e942ec47e642 | -10.25355 | -46.06319 | 2025-09-22 04:38:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d7a790e9-7d99-3163-adf7-614d6e85f186 | -8.17367 | -46.26677 | 2025-09-22 04:38:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 03ed725a-a45b-36e3-8a9c-a33f0abe684c | -7.79716 | -46.18475 | 2025-09-22 04:38:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 0d0d17ea-3f1f-34f1-be69-435dc8998eb8 | -8.29919 | -55.1109 | 2025-09-22 04:38:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ccb34009-5a3a-3543-b7c6-7559f2166924 | -5.65278 | -51.46656 | 2025-09-22 04:38:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 3a5047ed-24c6-3c90-98b1-db234ad05dd8 | -7.38103 | -44.57299 | 2025-09-22 04:38:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ddf55706-9c7c-3df1-afe4-3e8baefecf5e | -10.39276 | -46.08255 | 2025-09-22 04:38:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 92b3aaa0-5db1-36ce-bc0f-d7c7cc9892b7 | -3.61729 | -51.55057 | 2025-09-22 04:38:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| beeda5c3-112f-35d3-8aec-c44e91d64cf7 | -9.70406 | -47.63213 | 2025-09-22 04:38:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 744434ab-f379-3159-a30f-8d50c6ebdb60 | -10.38511 | -46.08138 | 2025-09-22 04:38:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9b4ae376-ff22-3eb9-b590-47f9e2bf81cc | -6.61214 | -44.60301 | 2025-09-22 04:38:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| c9ff5430-e04b-3ecc-9c39-ef4a5bd549a6 | -7.37295 | -44.5719 | 2025-09-22 04:38:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 730bc62f-5b9f-3ba3-a27c-c71548485986 | -5.43035 | -51.43165 | 2025-09-22 04:38:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| fafaa3a4-bbf1-3c64-934c-6b24e3894d96 | -6.39244 | -50.9065 | 2025-09-22 04:38:00 | NOAA-20 | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6f79ef9e-bca4-38d5-befd-a08bf477cb53 | -7.22826 | -45.17641 | 2025-09-22 04:38:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 29ba2e56-4d27-318b-b3c2-957bb2b92894 | -4.44079 | -55.3951 | 2025-09-22 04:38:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7729f179-5e30-36a9-913c-3e03f9fa823a | -8.02891 | -54.88493 | 2025-09-22 04:38:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b5f42d1f-ad9a-30f4-b6ff-945babb2a01d | -4.31217 | -48.08867 | 2025-09-22 04:38:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ee7a0461-1d0c-399c-8d7e-a50cea332001 | -4.4718 | -55.09362 | 2025-09-22 04:38:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cb7d3761-d644-3247-bbea-4be3b671da53 | -1.94024 | -56.60043 | 2025-09-22 04:38:00 | NOAA-20 | FARO | PARÁ | Brasil | 1503002 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b8781567-f7d8-37fc-85e4-910c3057dca3 | -3.62787 | -51.90964 | 2025-09-22 04:38:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 08ee2c14-9640-3b4d-a74d-e8eacaeb6d53 | -5.42031 | -51.44956 | 2025-09-22 04:38:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cbf6e469-6fbf-3555-9a4a-66b1855df1ac | -3.05407 | -46.93014 | 2025-09-22 04:38:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f8730c91-fef3-39d4-b163-7ac189e5f7f8 | -5.65625 | -51.46712 | 2025-09-22 04:38:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 61f96195-4375-3b11-8327-f701a0b9f463 | -3.33415 | -50.09002 | 2025-09-22 04:38:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d6b0d8c4-6c87-3d9e-ab53-d69391bdc2e9 | -10.38445 | -46.08605 | 2025-09-22 04:38:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3491d651-f4f6-3c16-ada4-c2cf18fa5f0e | -8.84704 | -43.0211 | 2025-09-22 04:38:00 | NOAA-20 | SÃO BRAZ DO PIAUÍ | PIAUÍ | Brasil | 2209559 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| c8517a64-25bf-38c6-9a07-8228b67f9158 | -10.36802 | -46.06417 | 2025-09-22 04:38:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| adbe585c-fe23-3957-a0fa-dd61eb421c60 | -5.91585 | -50.0017 | 2025-09-22 04:38:00 | NOAA-20 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8bf7a7f0-855a-3b85-be9c-ab9970afc680 | -6.38847 | -50.90961 | 2025-09-22 04:38:00 | NOAA-20 | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4ac500c0-2bf7-3fb2-9e60-026e753099ef | -3.84984 | -51.34258 | 2025-09-22 04:38:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1d4a904b-94d9-3701-ad58-f5daedbbe7d0 | -10.25285 | -46.06793 | 2025-09-22 04:38:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 13.2 |
| eada3db1-433b-3f9c-9aaf-6bdc94645f6b | -10.34513 | -46.06889 | 2025-09-22 04:38:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a4ea99cc-0da0-31f5-a744-a0273a361550 | -6.45708 | -45.67958 | 2025-09-22 04:38:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 61ca5405-dfe5-38e1-88d8-cde660171158 | -10.50414 | -44.05219 | 2025-09-22 04:38:00 | NOAA-20 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 37cb0211-9926-39c1-bfbc-6a6ee596a7b2 | -10.37019 | -46.05795 | 2025-09-22 04:38:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 254b87d2-f238-361d-b944-1bb75aaf2338 | -3.05124 | -46.92598 | 2025-09-22 04:38:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9e05644f-c53e-3db9-ab50-affc43439e2d | -10.38378 | -46.09077 | 2025-09-22 04:38:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9cffe5a4-69b4-390a-a065-519ef72bbb2a | -10.46276 | -44.19118 | 2025-09-22 04:38:00 | NOAA-20 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| c5670f4a-0df4-39c9-91ca-85b1657c5582 | -4.99254 | -45.15638 | 2025-09-22 04:38:00 | NOAA-20 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 98ff4df9-8bac-3047-9632-bcb80a132af7 | -7.35536 | -44.60824 | 2025-09-22 04:38:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d2e014cb-6511-3dce-a17b-a79eb98ee488 | -6.41492 | -43.8504 | 2025-09-22 04:38:00 | NOAA-20 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| de37f663-be11-3ca8-a40d-3e8adcd56743 | -7.62937 | -46.8245 | 2025-09-22 04:38:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f119f58a-2dea-3f62-87c5-db6006853bd8 | -6.44633 | -45.70068 | 2025-09-22 04:38:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| cf7548c3-80ad-3caf-861a-40d52ce54439 | -5.57269 | -42.13356 | 2025-09-22 04:38:00 | NOAA-20 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 3d281cdc-3056-3802-98d6-f4645242ccdd | -7.02421 | -46.30749 | 2025-09-22 04:38:00 | NOAA-20 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 288b0689-8fdd-3f09-b2a7-c507a953e977 | -7.35481 | -44.55472 | 2025-09-22 04:38:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6058e184-eeaa-3b03-a857-a0f545ef8764 | -7.79652 | -46.18909 | 2025-09-22 04:38:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 8900bca8-3715-3eaa-8000-ff074002657e | -7.60913 | -44.48925 | 2025-09-22 04:38:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2fbc1c5b-d1a9-3967-96f5-91d9787363c8 | -10.35489 | -46.05563 | 2025-09-22 04:38:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| dd3d47de-bd2e-370f-85b7-4eb0ba71512b | -17.27173 | -43.45271 | 2025-09-22 04:40:00 | NOAA-20 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 7.9 |


[Clique aqui para ver as próximas entradas](README28.md)
