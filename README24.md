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

## Dados Diários - Página 24

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f64c07e8-6575-324f-aaf4-e09874f04d13 | -24.17219 | -49.57155 | 2025-08-29 03:30:00 | NPP-375D | SENGÉS | PARANÁ | Brasil | 4126306 | 41 | 33 | nan | nan | nan | Cerrado | 10.8 |
| a173d2e8-d09a-3b01-a3e9-675c443f7d6d | -20.23868 | -45.74006 | 2025-08-29 03:30:00 | NPP-375D | IGUATAMA | MINAS GERAIS | Brasil | 3130309 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 916815d2-8f06-32ad-86f2-0875a65a7311 | -24.16348 | -49.57634 | 2025-08-29 03:30:00 | NPP-375D | SENGÉS | PARANÁ | Brasil | 4126306 | 41 | 33 | nan | nan | nan | Cerrado | 18.5 |
| 44a3065e-7258-31d1-a657-3e0e570a9fd5 | -24.16707 | -49.56277 | 2025-08-29 03:30:00 | NPP-375D | SENGÉS | PARANÁ | Brasil | 4126306 | 41 | 33 | nan | nan | nan | Cerrado | 10.6 |
| c11b8676-5623-39e6-9403-1b9f9add7ff1 | -24.1704 | -49.57834 | 2025-08-29 03:30:00 | NPP-375D | SENGÉS | PARANÁ | Brasil | 4126306 | 41 | 33 | nan | nan | nan | Cerrado | 27.7 |
| 06e88735-fea7-3ebf-bbfa-eae0777d1d65 | -24.17651 | -49.57146 | 2025-08-29 03:30:00 | NPP-375D | SENGÉS | PARANÁ | Brasil | 4126306 | 41 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 893cdb72-3de1-3d3e-9bd8-9e15b5890bb0 | -24.16538 | -49.56914 | 2025-08-29 03:30:00 | NPP-375D | SENGÉS | PARANÁ | Brasil | 4126306 | 41 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 5531e601-e430-3e63-89bd-5d103270ee66 | -19.90482 | -43.84184 | 2025-08-29 03:30:00 | NPP-375D | SABARÁ | MINAS GERAIS | Brasil | 3156700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 0f79bb54-bdd7-3b36-88e6-d3204169f7f8 | -20.35759 | -41.37804 | 2025-08-29 03:30:00 | NPP-375D | MUNIZ FREIRE | ESPÍRITO SANTO | Brasil | 3203700 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 666351e6-b73c-34e2-a38d-39e84140d3ef | -24.17383 | -49.56533 | 2025-08-29 03:30:00 | NPP-375D | SENGÉS | PARANÁ | Brasil | 4126306 | 41 | 33 | nan | nan | nan | Cerrado | 10.8 |
| fe76a29a-8ed7-30b9-bef2-6324fd0e917a | -20.35352 | -41.37907 | 2025-08-29 03:30:00 | NPP-375D | MUNIZ FREIRE | ESPÍRITO SANTO | Brasil | 3203700 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| e414902d-1b84-3027-9141-da288277d060 | -12.4345 | -63.9173 | 2025-08-29 03:40:00 | GOES-19 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 53.1 |
| e99505d1-75f2-3090-8ea9-8bb5449676c7 | -6.9867 | -59.3354 | 2025-08-29 03:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 38.0 |
| 8c8e974c-d097-38c5-a348-71b39145bd4f | -3.4254 | -49.0517 | 2025-08-29 03:40:00 | GOES-19 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 51.8 |
| a42e31f4-2413-3eb8-84ce-16570ec324df | -6.5358 | -43.9237 | 2025-08-29 03:40:00 | GOES-19 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 83.3 |
| 2f983493-3668-3b9f-9097-b12515346ec7 | -9.462 | -60.549 | 2025-08-29 03:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 78.5 |
| 23628f2c-5805-36da-9c17-71d6a074c744 | -9.4618 | -60.5682 | 2025-08-29 03:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 74.1 |
| 05d57f6f-30bc-33bd-8dac-6b351d207904 | -9.9328 | -59.9247 | 2025-08-29 03:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 60.5 |
| bf11546c-b47c-3877-a390-2e26f15c0124 | -8.1758 | -61.3755 | 2025-08-29 03:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 66.6 |
| 3e6339dc-fc9b-35bb-a1ba-7dddbb571cc1 | -5.6268 | -45.0025 | 2025-08-29 03:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 97.1 |
| 477492d2-bbdf-3eea-9c35-865dcb48e887 | -9.1154 | -65.7886 | 2025-08-29 03:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 68.9 |
| e2b22e1b-2539-3c85-bc29-13ab8aa86f49 | -9.1155 | -65.7699 | 2025-08-29 03:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 122.2 |
| f2d6552b-1965-3b8e-b194-9cb0f646d020 | -9.4432 | -60.5692 | 2025-08-29 03:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 77.3 |
| 2b7559f6-0640-3f58-a869-1d0a9f8fe7f3 | -9.4433 | -60.5499 | 2025-08-29 03:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 90.3 |
| 0f9ca2ef-d234-3406-b725-ae61f4392a2b | -9.0969 | -65.7705 | 2025-08-29 03:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 55.5 |
| fd127aa7-ef99-3d90-9ec0-3ddadee23c96 | -9.4263 | -47.6384 | 2025-08-29 03:40:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 53.7 |
| 9a29fcf8-c03e-3ce8-afd7-4cf1999b2bfe | -10.3812 | -57.8245 | 2025-08-29 03:40:00 | GOES-19 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 55.3 |
| 9f95cde5-1896-3586-aa72-34c03475c354 | -7.61995 | -42.69319 | 2025-08-29 03:47:00 | NOAA-20 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| c35240f3-420d-30e3-87c1-b413a16c2f9b | -7.03896 | -44.38208 | 2025-08-29 03:47:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 79021840-95ee-3f7e-818f-9bb4fef584a5 | -7.72107 | -50.29736 | 2025-08-29 03:47:00 | NOAA-20 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 4a31e951-b532-3838-a8a1-7619b25c74b8 | -6.53151 | -44.10688 | 2025-08-29 03:47:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f1d62216-c902-3f82-bf99-50951642eda0 | -7.21379 | -45.31145 | 2025-08-29 03:47:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1236a2d3-047e-37c6-ab9b-e27af2d7390f | -7.04452 | -44.37812 | 2025-08-29 03:47:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 4abba617-4616-3498-ad03-067584a6cabd | -9.51474 | -46.54094 | 2025-08-29 03:47:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| a42a5b3e-e3fd-3c5f-beb3-8d4a160e9a09 | -6.70908 | -43.14437 | 2025-08-29 03:47:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b1081224-2fef-3da4-9415-0b800afee261 | -7.01551 | -42.01887 | 2025-08-29 03:47:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 521bbe21-2c2f-3d27-9375-83b7affb5939 | -4.13004 | -38.25053 | 2025-08-29 03:47:00 | NOAA-20 | CASCAVEL | CEARÁ | Brasil | 2303501 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| c86ea578-068c-3d17-a3b3-65dffc34fc09 | -7.21504 | -45.45078 | 2025-08-29 03:47:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 35c47dea-e00c-3726-814a-50e5bfc768fa | -8.47737 | -43.68183 | 2025-08-29 03:47:00 | NOAA-20 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f8b488d4-99c9-377c-afbf-1c24bd243de1 | -6.79045 | -43.56502 | 2025-08-29 03:47:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9ce6e337-e572-368b-9fc6-8c94d448bcb1 | -9.49178 | -45.39467 | 2025-08-29 03:47:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3f12af16-75e4-38e4-ab09-ff450225a4d9 | -7.65108 | -42.69424 | 2025-08-29 03:47:00 | NOAA-20 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 50c08a63-a639-3613-836e-2f1edb232070 | -7.72756 | -50.30027 | 2025-08-29 03:47:00 | NOAA-20 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 4f30e8fe-368b-3603-a8f9-c329aa3ad83c | -8.09986 | -45.01005 | 2025-08-29 03:47:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c4705cb3-fae6-35f2-bc6d-b49ab114048c | -9.42288 | -47.651 | 2025-08-29 03:47:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 461013b3-f6b4-3927-9322-6efc92fd6a0f | -9.93861 | -46.3573 | 2025-08-29 03:47:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e7ebb41b-c1da-37d9-a879-681a490e1957 | -7.07514 | -44.28666 | 2025-08-29 03:47:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 09d5a0ed-49d4-3902-8d4e-afd88b30e735 | -6.83446 | -42.82578 | 2025-08-29 03:47:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 480cac5a-a079-37c8-b9db-0603fbc818fb | -7.4081 | -43.38687 | 2025-08-29 03:47:00 | NOAA-20 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 41ce1d04-9edf-3efc-aa56-5d49a1cda297 | -6.78789 | -43.77128 | 2025-08-29 03:47:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 46db216d-36e1-307f-83fa-6205ef46ae3e | -8.10079 | -45.00469 | 2025-08-29 03:47:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 043e57d5-7fb7-3736-8c37-982d68bb5999 | -7.64801 | -42.66262 | 2025-08-29 03:47:00 | NOAA-20 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 11c691ab-17e8-3aea-84e8-e764bc09b8c1 | -7.65827 | -42.65287 | 2025-08-29 03:47:00 | NOAA-20 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| d1338e62-1587-306a-901a-280d5ee7f64a | -7.62826 | -46.54506 | 2025-08-29 03:47:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f0e65fe1-056d-3d36-8628-111b04c88c9d | -7.07128 | -44.28112 | 2025-08-29 03:47:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| dfd2f9d9-57fb-3561-8f32-49bbfc8a746e | -7.04364 | -44.38312 | 2025-08-29 03:47:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 5c6f3f21-8ca5-3285-9e16-fcc0afe03040 | -6.44423 | -44.57253 | 2025-08-29 03:47:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a698cddf-62c4-35e4-b4f0-7f3c4bfb1033 | -9.59791 | -40.35826 | 2025-08-29 03:47:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 3.4 |
| adbd3d25-d6ab-3a9d-bd1a-674c44317468 | -7.02605 | -44.6796 | 2025-08-29 03:47:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| ec5035db-48ae-361f-854a-1043653cf727 | -7.21828 | -45.31532 | 2025-08-29 03:47:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5728abd7-6bfd-3a8c-8fab-54dca4650331 | -9.43562 | -47.64523 | 2025-08-29 03:47:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 9c9f0c73-520d-3708-9e71-9203b124dde7 | -9.69154 | -47.06707 | 2025-08-29 03:47:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8dab1b0b-c5b0-38d2-8e2b-4ca889ef7213 | -7.41213 | -42.06506 | 2025-08-29 03:47:00 | NOAA-20 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 61c742b2-b0c0-3db4-99c8-d2f4cea1b391 | -6.16565 | -47.2774 | 2025-08-29 03:47:00 | NOAA-20 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 22.7 |
| 0ba4c8f7-d240-3164-94a9-145de30f9412 | -7.0183 | -42.02681 | 2025-08-29 03:47:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 69fc5971-4955-3f80-be30-f379a4e54b03 | -9.93256 | -46.70864 | 2025-08-29 03:47:00 | NOAA-20 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| dc87a3cc-36a1-3e1a-9465-d8e1724db072 | -6.7091 | -49.46501 | 2025-08-29 03:47:00 | NOAA-20 | SAPUCAIA | PARÁ | Brasil | 1507755 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 404ac22e-1b7f-3d3c-9f86-8a65162edd6f | -8.44513 | -43.71393 | 2025-08-29 03:47:00 | NOAA-20 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 68c55652-ca6d-3ca9-a652-c20632319943 | -7.62383 | -42.67014 | 2025-08-29 03:47:00 | NOAA-20 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 4eab54cb-2a39-320b-aeb3-dfab4454e2f2 | -7.72878 | -50.29389 | 2025-08-29 03:47:00 | NOAA-20 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 191834bd-e9e9-39da-ae9a-2344a4d5642b | -6.48333 | -44.40764 | 2025-08-29 03:47:00 | NOAA-20 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9770ef51-b900-3df0-b1c8-9b0fdedce0e5 | -2.98486 | -48.60883 | 2025-08-29 03:47:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6e5e6096-aa23-3ceb-ba0c-5ac105a7f119 | -6.97596 | -44.12552 | 2025-08-29 03:47:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 365ebca9-7f92-311d-a892-afcfa3f3f3c8 | -6.9437 | -46.18464 | 2025-08-29 03:47:00 | NOAA-20 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0bd8ce13-ee61-3bc2-bfb0-4c315d84870b | -6.88164 | -43.61166 | 2025-08-29 03:47:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 9e02a64e-4034-3b13-b625-44d2be6c8008 | -7.41731 | -42.05874 | 2025-08-29 03:47:00 | NOAA-20 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| e32ebaec-909e-3eb3-87f0-4d9c7a3d7fc6 | -6.537 | -44.10302 | 2025-08-29 03:47:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 5fe83ab0-45e9-3172-ad4d-14d246bdb2c6 | -3.61698 | -43.54852 | 2025-08-29 03:47:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f380142e-c2ec-311c-97f9-c56fc6dcce86 | -3.97842 | -43.24453 | 2025-08-29 03:47:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| b804b09a-f616-3497-b91d-2703762e96ba | -8.48691 | -43.67909 | 2025-08-29 03:47:00 | NOAA-20 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 66b45d3c-b73b-3391-82f3-a5ced600903b | -7.40833 | -43.38519 | 2025-08-29 03:47:00 | NOAA-20 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 914e18ce-b58f-3c87-b125-66567efb46e2 | -5.07011 | -37.71737 | 2025-08-29 03:47:00 | NOAA-20 | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 0.7 |
| b89e5e6c-664c-3c62-ab04-0364409b78d6 | -7.08286 | -44.29783 | 2025-08-29 03:47:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ba169223-ad7a-328d-a749-70c7148b8f02 | -7.04745 | -44.38913 | 2025-08-29 03:47:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 00a8d6fd-2e7c-3ec7-9ff9-45d03cf36661 | -8.08344 | -45.01831 | 2025-08-29 03:47:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 8ad67ff2-fb9a-3b06-bedc-be29bf8ade14 | -9.9442 | -46.70444 | 2025-08-29 03:47:00 | NOAA-20 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b7b682a6-fa9f-3fef-ba11-f83ba0bec522 | -8.45048 | -43.65471 | 2025-08-29 03:47:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e8950394-86f9-384f-b54f-0e74cee929f9 | -6.53617 | -44.10778 | 2025-08-29 03:47:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c1e8bc8e-5de2-33c1-99b5-48781a111ed0 | -7.62799 | -42.72215 | 2025-08-29 03:47:00 | NOAA-20 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| f875035e-45f3-33a4-8e5d-f376c160dd4f | -6.8134 | -44.34997 | 2025-08-29 03:47:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| f72c8b64-c332-3141-b095-69f7c7ff39ab | -6.94432 | -46.1812 | 2025-08-29 03:47:00 | NOAA-20 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f5839446-768b-320f-b334-075252b0dea0 | -7.22945 | -45.42825 | 2025-08-29 03:47:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| b78ab8b4-01f9-32e8-9908-5e6276278f8d | -7.60679 | -42.69487 | 2025-08-29 03:47:00 | NOAA-20 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| e3db1f31-74b6-31f4-b56d-cebc7d483b68 | -6.71344 | -43.14514 | 2025-08-29 03:47:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f976b877-ab24-3672-a1b5-22820460c510 | -7.96903 | -46.37365 | 2025-08-29 03:47:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| b1d75d43-35ce-33d5-8856-6c2b05f6067c | -9.50925 | -45.38109 | 2025-08-29 03:47:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 98922904-4fe4-3f81-9804-aa0309e6dd2c | -6.87872 | -43.60178 | 2025-08-29 03:47:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 1cc13aad-7959-3424-9524-f2c262aa9a27 | -8.43727 | -43.65375 | 2025-08-29 03:47:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| da2a247e-84c5-381c-8be5-fde230d1090d | -6.71015 | -49.45934 | 2025-08-29 03:47:00 | NOAA-20 | SAPUCAIA | PARÁ | Brasil | 1507755 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 53b0bcaf-3dd6-3696-a48c-12c2d8e05e92 | -9.93842 | -46.70629 | 2025-08-29 03:47:00 | NOAA-20 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |


[Clique aqui para ver as próximas entradas](README25.md)
