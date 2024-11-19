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

## Dados Diários - Página 26

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ab6ef622-2992-3f30-9e7c-2ed78195a554 | -1.51444 | -52.09207 | 2024-11-19 04:46:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| af3f43a8-4ca7-385e-ad0a-c365830163fe | -0.80799 | -51.488 | 2024-11-19 04:46:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fefa73c4-b568-3f85-ad94-92aec7cdf24c | 0.34029 | -50.40727 | 2024-11-19 04:46:00 | NOAA-21 | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d3b334a9-6c2d-3c59-a78f-11da9aa076d6 | -6.05229 | -46.60532 | 2024-11-19 04:46:00 | NOAA-21 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a918d890-ac73-3a54-a929-f1bb1e400045 | -3.74722 | -54.71945 | 2024-11-19 04:46:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 10ddffe1-992d-326e-89c0-8d35bd46f008 | -1.76677 | -50.85658 | 2024-11-19 04:46:00 | NOAA-21 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8a3036d3-0db5-3540-8010-9897f5cbca5f | -1.13843 | -51.69416 | 2024-11-19 04:46:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b4eda271-192f-3d23-b0bd-c6412b114e91 | -2.22168 | -50.5151 | 2024-11-19 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e070cf85-e5c8-39d6-8463-dcfba0c87fdf | -1.30501 | -51.74558 | 2024-11-19 04:46:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 29bff74f-12d0-332d-9a8e-e4f991fa49f6 | -3.30734 | -53.36375 | 2024-11-19 04:46:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4f612e43-6b32-31d4-a7e8-6ce0cc085f83 | -1.33288 | -51.41242 | 2024-11-19 04:46:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d5a3eb23-8ae9-3c03-8a91-3a595e322d45 | -3.29084 | -53.8468 | 2024-11-19 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 60bac6e4-e5af-3ba5-8d02-53a1b88855a6 | -8.2674 | -44.04073 | 2024-11-19 04:46:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d8be805d-6fa9-3570-bba5-a2dcda57fadc | -2.69149 | -51.88218 | 2024-11-19 04:46:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cef4281a-3e72-3cf9-ba13-9649c3c8b664 | -3.58911 | -43.62368 | 2024-11-19 04:46:00 | NOAA-21 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5380dc02-64a9-341e-a811-bdcee7b12c6d | -2.08263 | -48.54054 | 2024-11-19 04:46:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ec3d09f3-0c91-3833-9436-beed50595fa2 | -2.67957 | -46.17843 | 2024-11-19 04:46:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8db3e09f-c782-37c5-a462-94b50090048d | -2.28252 | -48.81193 | 2024-11-19 04:46:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3bea0475-914b-36d8-965b-caee4946f564 | -2.61634 | -54.53517 | 2024-11-19 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 6a1601bb-d84b-3560-ab80-9cd124d183b3 | -4.57799 | -48.02388 | 2024-11-19 04:46:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| f9f72478-070d-31c3-b65a-7027a3686125 | -3.92733 | -50.98395 | 2024-11-19 04:46:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a46d1cf5-3550-375a-8464-99604b33467c | -2.19824 | -53.66394 | 2024-11-19 04:46:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2b2b59a3-def6-327d-9d17-3ac9ae091cb6 | -4.28477 | -48.21621 | 2024-11-19 04:46:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3b66e0ba-0f78-3cec-811e-670b947f2dfb | -3.33343 | -52.66772 | 2024-11-19 04:46:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 21de4289-69ec-3739-9b36-83e3d756dbc2 | -0.26727 | -48.43099 | 2024-11-19 04:46:00 | NOAA-21 | SOURE | PARÁ | Brasil | 1507904 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9e0023cf-4d37-3a5d-b02a-40b847b2edd2 | -1.41817 | -52.43866 | 2024-11-19 04:46:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 22.5 |
| 11bbde63-cd18-3e0e-a999-86c8987fa760 | -7.40323 | -42.76368 | 2024-11-19 04:46:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 8d6b5313-7ef6-36e2-8aa8-7267d74a9fac | -4.11085 | -51.05125 | 2024-11-19 04:46:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 0a6262b7-8b4b-34ee-8a30-99a6cf723dd6 | -2.2514 | -50.51968 | 2024-11-19 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bf39acd1-3578-3890-95b5-db4cccef552c | -3.28721 | -50.61934 | 2024-11-19 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| df3d8992-4731-3c01-8542-1e19d79b7ce1 | -7.57045 | -46.45658 | 2024-11-19 04:46:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b2212beb-222a-3e01-836e-272eb2865dde | -5.05461 | -48.3668 | 2024-11-19 04:46:00 | NOAA-21 | SÃO PEDRO DA ÁGUA BRANCA | MARANHÃO | Brasil | 2111532 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2add601c-80c5-3100-8be5-3613adeef16b | -1.78901 | -53.59646 | 2024-11-19 04:46:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 00c8bd27-2b3f-3f10-814b-887bc6124324 | -2.58064 | -51.71895 | 2024-11-19 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8b65e22f-760d-327b-8ae1-9f2370a4968d | -1.41217 | -52.05021 | 2024-11-19 04:46:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f74df241-21d5-3df0-9693-f8021bf557ab | -1.3982 | -47.45265 | 2024-11-19 04:46:00 | NOAA-21 | SANTA MARIA DO PARÁ | PARÁ | Brasil | 1506609 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 43fff2f8-ef1f-3883-a0f6-6db10f63e7b9 | -2.21545 | -48.40663 | 2024-11-19 04:46:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 161706fa-75c5-37b9-8e66-3e87c53e4590 | -5.98398 | -45.36296 | 2024-11-19 04:46:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 494a2e73-02d1-3419-a29f-e2711bd43682 | -3.26374 | -51.61563 | 2024-11-19 04:46:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| acd17830-7500-34cf-89c3-51871122218e | -3.75214 | -44.56891 | 2024-11-19 04:46:00 | NOAA-21 | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 72fbfb8a-9ccb-3685-bb64-341b4a7ab92b | -3.60066 | -53.996 | 2024-11-19 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a8bcd4a7-746a-3b12-8a61-bd898ef560be | -2.3858 | -53.66442 | 2024-11-19 04:46:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 3d66d445-d193-3de8-9dbc-3b1559372fc0 | -1.67341 | -46.9573 | 2024-11-19 04:46:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6efda137-aa76-31dc-ba87-e3fb9d1a2e6e | -2.27657 | -50.81656 | 2024-11-19 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 91dba2a1-6bbb-3f48-bbae-f9bd57af657b | -2.60307 | -51.79538 | 2024-11-19 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 24e85f67-92a8-37c8-8d82-0b3a77b498e2 | -2.64635 | -46.21685 | 2024-11-19 04:46:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5700e3ed-506d-3db5-b782-b9b5f108f39d | -2.60363 | -51.79182 | 2024-11-19 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b1ab3d81-7298-3b22-8fd8-43c04843d0fb | -2.5868 | -51.72354 | 2024-11-19 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7043b2b7-7e24-3d09-b56f-79ac40970893 | -2.14194 | -53.64248 | 2024-11-19 04:46:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 0e0c2e71-bb70-3597-9635-5fee69c442f1 | -4.49244 | -46.71531 | 2024-11-19 04:46:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 3.3 |
| ea93bed3-c069-307e-9ff6-4a638d6b38ea | -2.24293 | -50.46566 | 2024-11-19 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b6f2c3b7-1cd4-37ba-9ef9-a8dc12cf10be | -2.02657 | -51.17476 | 2024-11-19 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| baf17dff-7b71-396f-8cc1-224407cebff3 | -2.38161 | -48.91869 | 2024-11-19 04:46:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ef65d494-3460-3151-ae3f-0683c6b7da2e | -2.65903 | -51.71641 | 2024-11-19 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 76c33cda-ce28-3abf-8a21-943bda684a8f | -8.00434 | -44.39477 | 2024-11-19 04:46:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f183bc17-2c3c-3889-ba4e-8fc1ce934d6c | 0.0863 | -50.58905 | 2024-11-19 04:46:00 | NOAA-21 | AFUÁ | PARÁ | Brasil | 1500305 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1c4001f0-f5b8-3c87-bbe2-301eb2a5ddaf | 0.29096 | -51.11404 | 2024-11-19 04:46:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7fc568cf-91bf-3352-a53a-0267ecdee2e1 | -1.62702 | -47.23657 | 2024-11-19 04:46:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 225ae009-4d5e-32b6-86b6-21797b1a4a1b | -3.77619 | -51.03752 | 2024-11-19 04:46:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 45c19271-bd54-3a8b-80a2-dd6199d795ab | -3.50813 | -54.70924 | 2024-11-19 04:46:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 67e18831-610a-3a36-8ec1-579461bfc688 | -1.64932 | -52.77305 | 2024-11-19 04:46:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2f630bbc-14c7-3708-947a-27c257774c35 | -2.64323 | -46.21159 | 2024-11-19 04:46:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 27394ff2-599c-3f56-8318-8a6401fb68e0 | -2.7385 | -54.13402 | 2024-11-19 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8ad78e76-c3bd-3b1b-822a-e17d3f3b5c01 | -2.33395 | -45.67774 | 2024-11-19 04:46:00 | NOAA-21 | PRESIDENTE MÉDICI | MARANHÃO | Brasil | 2109239 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9c66fdac-330a-30c8-bbe7-da8cec15e181 | -1.58065 | -53.79927 | 2024-11-19 04:46:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 3ca58cdd-0c24-3c1a-be9e-6448a551deae | -1.24954 | -54.0492 | 2024-11-19 04:46:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 15294cb8-20e8-39ca-a999-39cda6b0c80c | -2.0764 | -48.53585 | 2024-11-19 04:46:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 24eade4a-8b98-3c26-ab1a-a166c19b1fc7 | -4.06425 | -54.05125 | 2024-11-19 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cfc5072b-22f1-3799-9739-ab1517a054fc | -0.85777 | -51.86762 | 2024-11-19 04:46:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 5.1 |
| b851dea7-0dab-3178-800d-2c3fb03c67f0 | -2.96595 | -51.41096 | 2024-11-19 04:46:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 4339bc0f-8863-3f2a-94ab-6c44ec0c0452 | -6.2716 | -47.22536 | 2024-11-19 04:46:00 | NOAA-21 | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| aa3ac3a5-9333-35da-9ee6-8ac1fb989623 | 0.61551 | -51.77289 | 2024-11-19 04:46:00 | NOAA-21 | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 16.0 |
| adf90e3e-e46f-34e7-a598-4ec8cc293339 | -3.62714 | -54.2295 | 2024-11-19 04:46:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 417976f9-f3a8-3659-a9df-8dd9d6a4c3bf | -2.79842 | -45.95186 | 2024-11-19 04:46:00 | NOAA-21 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ca43a05f-fa4a-33f1-a8f3-635dc1a7b6d2 | -2.86818 | -51.79286 | 2024-11-19 04:46:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| afdc5bd7-4b54-3437-8a07-8d4773becb09 | -3.96955 | -49.9489 | 2024-11-19 04:46:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b1028e5d-f66d-3da3-a7ad-5289e813678c | -6.41533 | -46.18796 | 2024-11-19 04:46:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 12e20f06-3b3a-3c13-b604-b3fbb6f76487 | -1.07596 | -53.36697 | 2024-11-19 04:46:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 066e0cda-bad0-3ecb-9517-219788b7c824 | -2.70431 | -51.69071 | 2024-11-19 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6aac5669-013e-36ba-a19d-56e87dff5b81 | -2.20188 | -53.66453 | 2024-11-19 04:46:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d7a0ce1c-3570-3dee-9615-59687387abd0 | -6.25599 | -43.56395 | 2024-11-19 04:46:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 7e423d5b-e045-3c44-9620-3b3744de4dfd | -2.1429 | -50.64717 | 2024-11-19 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4d93c1e7-fe31-3128-a451-105046304e63 | -3.51495 | -50.22528 | 2024-11-19 04:46:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 13.8 |
| e64b2bbe-70d4-3f09-bc3d-292847307cdd | -1.07233 | -53.36639 | 2024-11-19 04:46:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| bffbba8e-b21e-3a07-877c-2c801193db34 | -3.79451 | -51.39861 | 2024-11-19 04:46:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 58f7f188-fc1b-3023-aadc-2ec0cd3b2ab7 | -6.87984 | -44.77101 | 2024-11-19 04:46:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 11b4cae5-4a39-3a34-8be7-59f010f4a2f9 | -1.45071 | -52.67537 | 2024-11-19 04:46:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 962902bb-5322-31bc-b69a-7fb884360969 | -4.11964 | -43.58518 | 2024-11-19 04:46:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 10.3 |
| e389920f-3342-3c35-8640-e55065e072de | -2.35587 | -53.71185 | 2024-11-19 04:46:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bcfc9332-d03c-3c00-b398-ef73b6b27854 | -1.38499 | -51.55515 | 2024-11-19 04:46:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d56021f5-0c4c-3e9a-a0df-9d132f103bf4 | -2.70375 | -51.69426 | 2024-11-19 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| dc84bc49-59e4-3984-967e-a5398d423756 | -1.3691 | -47.2664 | 2024-11-19 04:46:00 | NOAA-21 | BONITO | PARÁ | Brasil | 1501600 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a75cb4c9-e2c3-39f1-8250-e12c1718f23c | -1.14238 | -51.69107 | 2024-11-19 04:46:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9b546b6c-04e9-393b-94bd-3bc1c1623ba0 | -2.74202 | -54.11197 | 2024-11-19 04:46:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3c33532b-2e31-3225-900d-742dea57a87a | -5.97916 | -45.36627 | 2024-11-19 04:46:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 80370207-7005-3ce7-91d0-c522b33f0dc5 | -4.20465 | -46.5933 | 2024-11-19 04:46:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| f7b68184-a9a2-33a0-a93b-325ffe486988 | -2.32559 | -51.28581 | 2024-11-19 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 310c3917-6c05-3e7c-ad8d-1f1566b5b8e9 | -4.56039 | -45.64223 | 2024-11-19 04:46:00 | NOAA-21 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 9b2b6b38-a5dd-30d8-a3f0-26a2e0b9da5f | -1.2503 | -52.05191 | 2024-11-19 04:46:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| a8c960ef-74ed-3a2f-be21-3be94ccfd563 | -5.12818 | -46.20334 | 2024-11-19 04:46:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |


[Clique aqui para ver as próximas entradas](README27.md)
