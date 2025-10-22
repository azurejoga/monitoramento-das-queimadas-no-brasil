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

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ce896347-9611-38ed-a824-ee07d9b3cfbf | -18.3384 | -49.5042 | 2025-10-22 03:38:00 | NOAA-20 | ITUMBIARA | GOIÁS | Brasil | 5211503 | 52 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 1b8d925f-5ab2-3c0b-9ce2-771b9fea74ff | -20.03729 | -46.70342 | 2025-10-22 03:38:00 | NOAA-20 | TAPIRA | MINAS GERAIS | Brasil | 3168101 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 494208af-78b7-3781-9c97-fd1748892553 | -16.62793 | -43.48828 | 2025-10-22 03:38:00 | NOAA-20 | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 728f15c3-8cd2-3f34-be40-b2353d9d9ec5 | -18.64926 | -49.09309 | 2025-10-22 03:38:00 | NOAA-20 | CENTRALINA | MINAS GERAIS | Brasil | 3115805 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4da9596d-a566-3a97-a22e-265d77059c95 | -17.61994 | -46.62099 | 2025-10-22 03:38:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 46739a28-16c1-3a20-baf9-20c829a8bf9f | -19.90707 | -46.11464 | 2025-10-22 03:38:00 | NOAA-20 | TAPIRAÍ | MINAS GERAIS | Brasil | 3168200 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 1f02c8d0-c7c3-3116-a28b-b7554ae29051 | -20.56624 | -45.89513 | 2025-10-22 03:38:00 | NOAA-20 | PIMENTA | MINAS GERAIS | Brasil | 3150505 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| fc98fc76-b348-31fd-b08a-3bd6abd92d3b | -17.6454 | -46.63959 | 2025-10-22 03:38:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9ef653c2-cb52-3f35-bb0f-79c7816aa3bd | -19.08618 | -44.34848 | 2025-10-22 03:38:00 | NOAA-20 | CORDISBURGO | MINAS GERAIS | Brasil | 3118908 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1cebc3b9-3056-3542-951c-1c5dbb5f72db | -18.64345 | -49.09481 | 2025-10-22 03:38:00 | NOAA-20 | CENTRALINA | MINAS GERAIS | Brasil | 3115805 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c3824b39-f26c-3738-8e07-d53dc3d41c35 | -17.64455 | -46.64356 | 2025-10-22 03:38:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 71c3dc94-5121-35e1-9ba2-895e7890d9b0 | -4.4632 | -43.2386 | 2025-10-22 03:40:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 143.8 |
| 8daf2b63-15d6-374e-878b-e052b7609a9b | -4.463 | -43.2619 | 2025-10-22 03:40:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 67.2 |
| 3c9adc80-9e17-3591-92d1-71344b6a2d09 | -9.0036 | -65.9412 | 2025-10-22 03:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 75.1 |
| 37a6cb90-1943-3ca0-a884-ed0425b66130 | -4.4445 | -43.2397 | 2025-10-22 03:40:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 177.2 |
| 07137ca5-2001-3ec9-85d1-8444a1d579a1 | -9.0036 | -65.9226 | 2025-10-22 03:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 74.9 |
| b0cfbc6b-e1ad-3ff2-a7e8-aa084392729b | -4.4443 | -43.263 | 2025-10-22 03:40:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 82.1 |
| 5a901034-36ce-3320-84a1-46539428f07b | -21.09766 | -47.15854 | 2025-10-22 03:40:00 | NOAA-20 | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 509c6caa-707a-3f19-a1a4-4620115fa62c | -21.05484 | -46.9862 | 2025-10-22 03:40:00 | NOAA-20 | ITAMOGI | MINAS GERAIS | Brasil | 3132909 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| bd35e1fb-8631-39d3-9a72-181a43b08193 | -20.97555 | -47.21622 | 2025-10-22 03:40:00 | NOAA-20 | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 600deb4a-d066-3999-bf2d-a19e9ae4a1e6 | -20.97747 | -47.20758 | 2025-10-22 03:40:00 | NOAA-20 | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9211c64d-3658-36f6-a11c-83815ed76ca6 | -21.09681 | -47.16235 | 2025-10-22 03:40:00 | NOAA-20 | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 3422b7da-40d6-3c6c-b0df-4e971dd0abac | -25.03902 | -51.02058 | 2025-10-22 03:40:00 | NOAA-20 | PRUDENTÓPOLIS | PARANÁ | Brasil | 4120606 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 1607b83d-6d05-3483-bc99-3c0c262bef5b | -20.97831 | -47.2038 | 2025-10-22 03:40:00 | NOAA-20 | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 576b9604-3334-3c48-a2c6-8a0919fb99dc | -21.05403 | -46.9899 | 2025-10-22 03:40:00 | NOAA-20 | ITAMOGI | MINAS GERAIS | Brasil | 3132909 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 15a05f05-f83a-3923-bb8f-9238357a209b | -22.38037 | -46.91714 | 2025-10-22 03:40:00 | NOAA-20 | MOGI GUAÇU | SÃO PAULO | Brasil | 3530706 | 35 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 2e2a2882-c4a3-3a2c-875e-8f7499cff933 | -22.37962 | -46.92059 | 2025-10-22 03:40:00 | NOAA-20 | MOGI GUAÇU | SÃO PAULO | Brasil | 3530706 | 35 | 33 | nan | nan | nan | Cerrado | 7.9 |
| a7a3b541-cf10-3d49-80dc-475b13ee6ead | -22.08184 | -42.98958 | 2025-10-22 03:40:00 | NOAA-20 | SAPUCAIA | RIO DE JANEIRO | Brasil | 3305406 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 45cc4a30-5647-3976-b05e-6110ba19e17a | -20.97654 | -47.21174 | 2025-10-22 03:40:00 | NOAA-20 | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8c218029-7226-3c38-9f81-e5bdede6a46d | -28.20389 | -52.45828 | 2025-10-22 03:42:00 | NOAA-20 | PASSO FUNDO | RIO GRANDE DO SUL | Brasil | 4314100 | 43 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 8232782e-a7ae-389d-a248-1bdd08b2be32 | -28.20007 | -52.45448 | 2025-10-22 03:42:00 | NOAA-20 | PASSO FUNDO | RIO GRANDE DO SUL | Brasil | 4314100 | 43 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| d9e85e08-632f-3b09-b618-aea3a249805e | -28.2054 | -52.45255 | 2025-10-22 03:42:00 | NOAA-20 | PASSO FUNDO | RIO GRANDE DO SUL | Brasil | 4314100 | 43 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 2989f443-4e20-31af-ab7e-13c33215150e | -28.20164 | -52.44866 | 2025-10-22 03:42:00 | NOAA-20 | PASSO FUNDO | RIO GRANDE DO SUL | Brasil | 4314100 | 43 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| 1d7dcaf9-ec5e-3cbf-8c61-cd57e3bab945 | -28.19927 | -52.45018 | 2025-10-22 03:42:00 | NOAA-20 | PASSO FUNDO | RIO GRANDE DO SUL | Brasil | 4314100 | 43 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| a45b67d0-e17c-35b5-a0b2-217d2432ed01 | -4.4443 | -43.263 | 2025-10-22 03:50:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 62.9 |
| 2c2b0ae0-a7b8-3984-9ee5-62addfc10353 | -4.4632 | -43.2386 | 2025-10-22 03:50:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 148.7 |
| 87180f50-9c02-37d0-89c2-a3297573dd49 | -4.4445 | -43.2397 | 2025-10-22 03:50:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 239.9 |
| c6a9e7bc-4e43-3f4d-8c4c-86b09ec81a19 | -9.0036 | -65.9412 | 2025-10-22 03:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 66.1 |
| 84d6c43b-e4b6-3eeb-973f-0ecc6c9f4ec1 | -9.0036 | -65.9226 | 2025-10-22 03:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 74.0 |
| 1e62f879-66a5-3667-8e8b-46833f0d4fe6 | -4.4445 | -43.2397 | 2025-10-22 04:00:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 198.8 |
| 7a87d662-0e01-3080-bd0a-1c3ca6f254cf | -4.4443 | -43.263 | 2025-10-22 04:00:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 60.3 |
| cb68a894-6763-3cac-ae79-68ce8279f363 | -9.0036 | -65.9412 | 2025-10-22 04:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 69.3 |
| ee89877e-f5d0-3e42-acea-ca71b6b9b600 | -4.4446 | -43.2164 | 2025-10-22 04:00:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 65.8 |
| ddfbfd95-b65c-3dbd-8b74-01fbacdc45f8 | -9.0036 | -65.9226 | 2025-10-22 04:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 78.4 |
| bd681c6a-4014-3a9e-abbc-b424a46de4d6 | -4.4632 | -43.2386 | 2025-10-22 04:00:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 135.8 |
| b2d67746-e538-392d-8a60-52adcb0615d6 | -9.0036 | -65.9412 | 2025-10-22 04:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 61.8 |
| cbd7928f-7012-3d24-86f8-7767a2af5ca6 | -4.4445 | -43.2397 | 2025-10-22 04:10:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 235.8 |
| 6a87b6b2-16f2-3dbf-ade9-1283f72b356a | -4.4446 | -43.2164 | 2025-10-22 04:10:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 67.0 |
| 1221c1e5-f404-3a98-9647-7326973135e3 | -9.0036 | -65.9226 | 2025-10-22 04:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 73.4 |
| 70687d31-423a-3453-a2fb-031a366e06f6 | -4.4632 | -43.2386 | 2025-10-22 04:10:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 132.5 |
| 9109eef2-9e9b-37b2-9072-d8ca0b390095 | -4.4446 | -43.2164 | 2025-10-22 04:20:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 64.9 |
| 6eba8f87-fea0-3fd1-83d5-d6c3f39bdd5d | -4.4445 | -43.2397 | 2025-10-22 04:20:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 208.8 |
| 24f2b686-1f9d-35c3-9da6-45080ca54c97 | -9.0036 | -65.9226 | 2025-10-22 04:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 75.3 |
| 308f16e2-9e0a-35d8-b5ba-46f20f6ee379 | -4.4632 | -43.2386 | 2025-10-22 04:20:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 111.7 |
| f5801f7f-574b-38a8-8377-3b45155eef73 | -9.0036 | -65.9412 | 2025-10-22 04:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 61.5 |
| 93ac88e0-5aa4-3192-9b28-48291b8acf8d | -3.23443 | -42.07425 | 2025-10-22 04:23:00 | NOAA-21 | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 94741ee5-193a-3d7e-8c9f-37a4d9ccaae7 | -2.36082 | -47.9803 | 2025-10-22 04:23:00 | NOAA-21 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| a4bf93cc-2cfd-3f17-8a83-0f453d04197a | 1.52787 | -56.06343 | 2025-10-22 04:23:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 679e9f52-9481-3023-aa49-c433b2e2b0cd | -3.75006 | -39.26997 | 2025-10-22 04:23:00 | NOAA-21 | PENTECOSTE | CEARÁ | Brasil | 2310704 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 278d1fca-3220-34ff-a577-509a17f76afa | 1.67282 | -55.73949 | 2025-10-22 04:23:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| b00b7e6a-8bdc-30d3-9156-f3e5036b7673 | 1.67355 | -55.7443 | 2025-10-22 04:23:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f888a0f6-c236-319c-bb14-ea2387128993 | 0.35327 | -51.06847 | 2025-10-22 04:23:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 416c16b3-002a-3ab2-aef0-f5a87ece7c61 | -3.44919 | -41.84782 | 2025-10-22 04:23:00 | NOAA-21 | CAXINGÓ | PIAUÍ | Brasil | 2202653 | 22 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 9fe6ef73-b2be-302d-8dc4-783edbac468d | -2.25712 | -47.87974 | 2025-10-22 04:23:00 | NOAA-21 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| cffa7c65-af48-30d7-a418-aa078e859ffe | 1.71902 | -55.67208 | 2025-10-22 04:23:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 470c7444-02e1-392e-909a-df7af3ac733d | -1.43856 | -47.16949 | 2025-10-22 04:23:00 | NOAA-21 | OURÉM | PARÁ | Brasil | 1505403 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 607c3855-96a5-32d6-bf4b-cfa07393b5d2 | -3.23808 | -42.07479 | 2025-10-22 04:23:00 | NOAA-21 | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1cab1ab8-2d48-343c-8831-3be4595d7728 | -3.44548 | -41.84728 | 2025-10-22 04:23:00 | NOAA-21 | CAXINGÓ | PIAUÍ | Brasil | 2202653 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| b85c933d-d124-3024-891a-be9fcdafb179 | -1.49539 | -47.81011 | 2025-10-22 04:23:00 | NOAA-21 | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d2d56e66-612d-3d1f-9ae2-25f55b2f94cc | -0.63844 | -47.65427 | 2025-10-22 04:23:00 | NOAA-21 | MARAPANIM | PARÁ | Brasil | 1504406 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e6900035-ebe1-39f7-9a0e-74f3b41357db | 1.53416 | -56.0625 | 2025-10-22 04:23:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2f9023f5-a197-3023-a67d-6cbbfd24b662 | -2.99087 | -39.96535 | 2025-10-22 04:23:00 | NOAA-21 | ITAREMA | CEARÁ | Brasil | 2306553 | 23 | 33 | nan | nan | nan | Caatinga | 3.2 |
| cebc47fb-2f26-35f3-a3b1-c894b625c66b | -2.38046 | -47.72023 | 2025-10-22 04:23:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8f152086-3c85-3bfd-a848-bcab940d939a | -2.26063 | -47.88029 | 2025-10-22 04:23:00 | NOAA-21 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 537830c2-5e59-34bc-adb1-aa1d13f52bd5 | 1.69636 | -55.68743 | 2025-10-22 04:23:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0fd3d83e-0859-3f01-babb-cf6a7ba90f2a | -2.36652 | -47.65129 | 2025-10-22 04:23:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 93d634c5-49a9-3290-85dd-c3cf5c2929e3 | -0.83177 | -48.73666 | 2025-10-22 04:23:00 | NOAA-21 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 03a754b8-ce44-373a-8848-fcced3c3dd7e | -3.14072 | -39.65349 | 2025-10-22 04:23:00 | NOAA-21 | AMONTADA | CEARÁ | Brasil | 2300754 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 00528d46-4547-3027-b341-9afcf03d7b82 | 0.27588 | -51.32112 | 2025-10-22 04:23:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 83a3713d-6ad5-3ef0-8399-19b8cdd4e6c1 | -1.49186 | -47.80957 | 2025-10-22 04:23:00 | NOAA-21 | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 8f7e903e-f1b6-3289-9a12-6021bdf35e20 | -3.4529 | -41.84835 | 2025-10-22 04:23:00 | NOAA-21 | CAXINGÓ | PIAUÍ | Brasil | 2202653 | 22 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 6a51caaa-2367-3679-bb68-c7225c9eadfd | -1.43855 | -47.16934 | 2025-10-22 04:23:00 | NOAA-21 | OURÉM | PARÁ | Brasil | 1505403 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 610e1041-cf58-3c5e-a35e-4b8ff59c5fce | -2.36434 | -47.98084 | 2025-10-22 04:23:00 | NOAA-21 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 3c817d37-9e9b-3dba-8cfd-9ab11d5b3ab6 | -2.83897 | -40.1768 | 2025-10-22 04:23:00 | NOAA-21 | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| f35c2ad5-8e22-3540-83a7-a2f4e88b1def | -2.42701 | -48.60943 | 2025-10-22 04:23:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 63fc6d58-8f58-3869-bd80-6d55c29b1f77 | -3.66802 | -40.48035 | 2025-10-22 04:23:00 | NOAA-21 | SOBRAL | CEARÁ | Brasil | 2312908 | 23 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 75378f2c-b127-3a7c-b631-d25c26cdb5b5 | -1.49124 | -47.81352 | 2025-10-22 04:23:00 | NOAA-21 | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| d3a17c07-74d6-3841-b644-cc6e1eb7f7c2 | 1.6721 | -55.73475 | 2025-10-22 04:23:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 9c8389b7-5865-31bb-8ff8-747538e1496e | -2.98885 | -39.96247 | 2025-10-22 04:23:00 | NOAA-21 | ITAREMA | CEARÁ | Brasil | 2306553 | 23 | 33 | nan | nan | nan | Caatinga | 2.8 |
| fe01793d-13ad-3bf8-aed4-aeca5f7ac7c9 | 1.67682 | -55.72429 | 2025-10-22 04:23:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 0916c21b-904d-3594-bbc4-87c22cd7dc27 | -3.74999 | -39.26823 | 2025-10-22 04:23:00 | NOAA-21 | PENTECOSTE | CEARÁ | Brasil | 2310704 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| b52680d2-458c-330c-bdd4-17fe18bf7c08 | -3.13649 | -39.65284 | 2025-10-22 04:23:00 | NOAA-21 | AMONTADA | CEARÁ | Brasil | 2300754 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 0c832db6-27af-3b02-bc75-c60fe300b319 | -3.66889 | -40.47999 | 2025-10-22 04:23:00 | NOAA-21 | SOBRAL | CEARÁ | Brasil | 2312908 | 23 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 73b10fdc-5668-3457-a412-25609811a525 | 1.67827 | -55.7338 | 2025-10-22 04:23:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f8288ea0-98cc-36ab-b746-5d615416a426 | 1.67754 | -55.72905 | 2025-10-22 04:23:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| fcc895eb-b9db-3606-ba81-e2ca233af438 | -3.521 | -40.67729 | 2025-10-22 04:23:00 | NOAA-21 | COREAÚ | CEARÁ | Brasil | 2304004 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| cf7a367d-1806-39d1-8172-0e86dac60009 | -1.82593 | -47.09608 | 2025-10-22 04:23:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cc5aebd4-7e0b-3393-b06d-f24003360156 | -4.28726 | -48.25548 | 2025-10-22 04:25:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| eb38e7fa-3001-3365-9a11-4f72391bc809 | -7.07759 | -44.11005 | 2025-10-22 04:25:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1d05d4a0-ece3-38d6-a102-91f06b679f8b | -6.55119 | -44.02071 | 2025-10-22 04:25:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |


[Clique aqui para ver as próximas entradas](README7.md)
