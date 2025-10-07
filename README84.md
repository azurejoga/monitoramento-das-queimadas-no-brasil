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

## Dados Diários - Página 84

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1444d66c-bfe4-3d7b-9119-a3f77584042b | -5.57174 | -43.57239 | 2025-10-07 04:55:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 02665fb0-c26a-3de8-96f7-d398861f9291 | -3.92321 | -53.47474 | 2025-10-07 04:55:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3e2125c7-243d-3362-b658-c7e321a41ed1 | -3.13789 | -44.42311 | 2025-10-07 04:55:00 | NOAA-20 | SANTA RITA | MARANHÃO | Brasil | 2110203 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 924397b2-6c98-3d9d-9e6f-82a017e798cd | -2.98649 | -52.62865 | 2025-10-07 04:55:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9f371008-6215-3d4f-8537-348fbdc57b45 | -5.70881 | -44.83662 | 2025-10-07 04:55:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2b878c62-c0ed-3441-baf8-bfe2dd5e8a01 | -6.52897 | -55.0399 | 2025-10-07 04:55:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0cf6ca9a-6c91-30e6-99fa-95b80f94bd5a | -7.6838 | -42.40838 | 2025-10-07 04:55:00 | NOAA-20 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 5.7 |
| e2c0a718-6e1b-3aa7-8455-fb7a4c812b98 | -5.77424 | -45.74237 | 2025-10-07 04:55:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| df57172d-8662-3586-8a5d-fefe110fbd16 | -7.52054 | -49.91222 | 2025-10-07 04:55:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f3ead79a-f874-301d-b99b-d0386cec4068 | -8.18054 | -43.35207 | 2025-10-07 04:55:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 14170fd1-f177-3650-b56d-17fd101e7738 | -3.53087 | -52.99001 | 2025-10-07 04:55:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| dc3a3c79-ce1a-3654-a64d-61bc3abc3e28 | -3.08949 | -47.0284 | 2025-10-07 04:55:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d8727e59-bc50-3655-9e63-2227d27f0ad6 | -5.48757 | -43.08499 | 2025-10-07 04:55:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 01006a74-8647-3a38-a6d5-3020036ccf6a | -5.49179 | -43.08015 | 2025-10-07 04:55:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 8.5 |
| ef077f61-ebae-3abd-a2db-bb9690c923f3 | -7.69654 | -42.41045 | 2025-10-07 04:55:00 | NOAA-20 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| af905524-3908-32ac-a557-48acf6ac37ad | -5.74632 | -44.98572 | 2025-10-07 04:55:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f57d6113-376e-39db-be61-eeb868d15f41 | -7.69145 | -42.3993 | 2025-10-07 04:55:00 | NOAA-20 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 8b4564a8-6b80-3737-8ac4-fc3c141dad33 | -3.09012 | -47.02413 | 2025-10-07 04:55:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f20b98f0-7f3e-34e2-aeff-042b52f8a6d2 | -5.76219 | -45.7555 | 2025-10-07 04:55:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 8e6fd948-fe04-3265-96f6-23cc50f3de3e | -8.58786 | -44.33799 | 2025-10-07 04:55:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 292ca4d3-5a64-300d-8929-cb30557c8ac5 | -7.69626 | -42.39749 | 2025-10-07 04:55:00 | NOAA-20 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| b1e61ab0-7aa5-3089-a2b3-0b5d84c1d85a | -4.11223 | -50.05032 | 2025-10-07 04:55:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 66f6b4e9-e135-3553-9b72-5252068d34f6 | -8.20147 | -44.22441 | 2025-10-07 04:55:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 95ce908e-199b-3f4e-961f-3d2b25949bcb | -3.10456 | -47.01763 | 2025-10-07 04:55:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 816aac77-7401-3374-aa77-46772440124e | -6.17509 | -51.16205 | 2025-10-07 04:55:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f19867ef-3b78-3e76-acee-89bf2927b6fc | -3.09577 | -47.01628 | 2025-10-07 04:55:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 23.2 |
| b9411b59-4754-3e51-bc90-407f2d3b3716 | -3.09638 | -50.58199 | 2025-10-07 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 701ae24d-8cb5-3c64-bf21-1c13f6814938 | -7.67878 | -50.21097 | 2025-10-07 04:55:00 | NOAA-20 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 99e5a52e-8291-3f85-8581-49f3d3b4423d | -7.72405 | -42.3989 | 2025-10-07 04:55:00 | NOAA-20 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 408484f0-2992-3908-bd52-cf8d4a6783b3 | -8.20562 | -44.19207 | 2025-10-07 04:55:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 2e0a8163-5862-332b-9757-b7b1413b8734 | -2.89908 | -50.73419 | 2025-10-07 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b41af56b-56e7-3679-8a87-2e7a655f643b | -8.20611 | -44.18108 | 2025-10-07 04:55:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ee7e161e-e30f-3360-9ddc-12c6c757bf68 | -6.72654 | -42.82457 | 2025-10-07 04:55:00 | NOAA-20 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 058b45e6-5ba1-338d-973a-2d25e7bca186 | -7.68852 | -42.40672 | 2025-10-07 04:55:00 | NOAA-20 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 7b2f8b3a-1746-3478-8d15-b90a800fa8a3 | -6.75292 | -42.23734 | 2025-10-07 04:55:00 | NOAA-20 | TANQUE DO PIAUÍ | PIAUÍ | Brasil | 2210979 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| c9eba181-a572-3c60-84cb-b8f519fec782 | -5.71416 | -44.83717 | 2025-10-07 04:55:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 90a8ef46-db05-32da-a599-43230be77723 | -8.20199 | -44.22038 | 2025-10-07 04:55:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a5641b28-ec50-3d81-9452-a25614446659 | -7.02344 | -42.75852 | 2025-10-07 04:55:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| d5fe4cf6-d1a7-32e2-9bb0-8151236602ba | -2.90259 | -50.73472 | 2025-10-07 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 847674c8-c3d3-36f7-8453-f336bf45c14c | -7.69351 | -42.41807 | 2025-10-07 04:55:00 | NOAA-20 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 4.3 |
| e4e02628-650f-340c-b809-f31eb565a82f | -6.74021 | -50.83554 | 2025-10-07 04:55:00 | NOAA-20 | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ce774f15-505a-343c-87ea-b425f94373f2 | -2.80002 | -54.86152 | 2025-10-07 04:55:00 | NOAA-20 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 149fc224-6f9c-326b-b340-6c0b3c0c4b05 | -6.70242 | -42.86462 | 2025-10-07 04:55:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 9e917226-bbd7-3202-894d-e12e882a993c | -4.55546 | -46.67991 | 2025-10-07 04:55:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a78d8bd2-eedc-30db-84b3-66fc33a321a4 | -5.67129 | -42.77041 | 2025-10-07 04:55:00 | NOAA-20 | MIGUEL LEÃO | PIAUÍ | Brasil | 2206308 | 22 | 33 | nan | nan | nan | Caatinga | 5.2 |
| a5043b30-05ed-39ce-8672-d247396db3ea | -7.52512 | -49.90788 | 2025-10-07 04:55:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| dd9fab2c-331f-3f32-9fa0-962e15bf7662 | -4.44629 | -43.23468 | 2025-10-07 04:55:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 20.9 |
| 666b376c-68c3-385e-8ed8-e081f166bf52 | -5.74064 | -49.1329 | 2025-10-07 04:55:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 812cda2d-a5d4-3eec-bdcd-889579f4117b | -8.20596 | -46.98896 | 2025-10-07 04:55:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 85b59069-d298-3d1f-b392-f635d3e561b5 | -7.02235 | -42.7591 | 2025-10-07 04:55:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| d5b5a031-011e-3d42-b389-89fb34e3c711 | -3.19594 | -51.0333 | 2025-10-07 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fc8a72c1-42fa-39fc-b50b-739a6103753e | -4.8708 | -50.89829 | 2025-10-07 04:55:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1b2035ab-dab5-377c-ab33-08b28df65b26 | -4.06848 | -44.51316 | 2025-10-07 04:55:00 | NOAA-20 | SÃO MATEUS DO MARANHÃO | MARANHÃO | Brasil | 2111508 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 61cf566b-382b-3ed1-b9f9-2e31342649e5 | -7.8842 | -47.81435 | 2025-10-07 04:55:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 41f9e514-f63b-37f9-97f6-40d266c9d984 | -8.20043 | -44.23246 | 2025-10-07 04:55:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 4c8d4319-0347-32b1-863e-8979cbbf3b50 | -4.68153 | -45.84084 | 2025-10-07 04:55:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 8014c915-d6d4-3c97-84c8-65b9c91e0464 | -2.20178 | -56.91761 | 2025-10-07 04:55:00 | NOAA-20 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5a171f3d-2642-3ab0-8f1d-26882920011d | -3.09129 | -54.61314 | 2025-10-07 04:55:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| e72714a4-eb3d-3f9c-a6fe-6a0708ca5b29 | -4.06318 | -44.51239 | 2025-10-07 04:55:00 | NOAA-20 | SÃO MATEUS DO MARANHÃO | MARANHÃO | Brasil | 2111508 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| dead02e3-e7ca-39b3-bcad-d9e0dc01bcc1 | -5.21792 | -47.37363 | 2025-10-07 04:55:00 | NOAA-20 | SÃO FRANCISCO DO BREJÃO | MARANHÃO | Brasil | 2110856 | 21 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 2c72261f-c8b4-38a6-bbf1-66fd52f8a8a5 | -7.68217 | -42.40556 | 2025-10-07 04:55:00 | NOAA-20 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 014539b9-7a22-326c-9a04-7640786f51c1 | -3.66224 | -51.95403 | 2025-10-07 04:55:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 261d714e-9589-3202-bbee-498d9f84d24d | -6.69628 | -42.86382 | 2025-10-07 04:55:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 18533ded-ba39-3a89-9554-98fe94ab85b4 | -5.33101 | -49.32471 | 2025-10-07 04:55:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cb856def-a35b-37ad-a607-f48f3562ad48 | -3.89078 | -52.14709 | 2025-10-07 04:55:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| e2d45aad-5d51-3c93-8efe-5c528e49cfb8 | -5.48881 | -43.07638 | 2025-10-07 04:55:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 10.6 |
| a601027f-099f-34ab-a339-b603dda0e288 | -3.08608 | -47.02078 | 2025-10-07 04:55:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 47eca374-7359-3c67-81ab-070d245363d3 | -5.88953 | -49.37051 | 2025-10-07 04:55:00 | NOAA-20 | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f46b4524-8b0d-32ec-9849-b872c05caff0 | -6.58821 | -44.62691 | 2025-10-07 04:55:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 159ec37c-1d5c-3eba-a792-3eeea9e85677 | -4.44688 | -43.23057 | 2025-10-07 04:55:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 36.6 |
| 0d82220a-92ac-3ab6-bfe6-a05dc66876a4 | -2.51881 | -51.93207 | 2025-10-07 04:55:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 207b87ee-fa60-3c5d-86e6-2bb06bd57988 | -3.46815 | -53.45255 | 2025-10-07 04:55:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 703a3d7c-3f3d-3c63-a720-91e003298852 | -6.56368 | -44.15253 | 2025-10-07 04:55:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a492f1c0-ffe4-3310-8b11-98571aec1208 | -7.01951 | -42.78695 | 2025-10-07 04:55:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 9ef26836-f823-305b-90b5-f2910493dd4a | -4.55147 | -46.6766 | 2025-10-07 04:55:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1da2ea0b-1a4d-3a3f-8870-20057b8439a9 | -5.6495 | -43.18949 | 2025-10-07 04:55:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 66263ff1-6f9b-3581-b11f-7d8cc69edc8b | -3.66674 | -51.94734 | 2025-10-07 04:55:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c5a03886-eaeb-374b-b0e2-2f4b0f88a50d | -5.49417 | -43.08136 | 2025-10-07 04:55:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 10.6 |
| c5ae9bbe-c055-31dc-a74a-63e6e07375ea | -3.0989 | -47.02548 | 2025-10-07 04:55:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| b4aeddb9-99a4-39a4-8ee0-2413b5e8ba84 | -2.14576 | -47.50713 | 2025-10-07 04:55:00 | NOAA-20 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 52677b8c-fa89-3bcb-a166-f91c05c82f73 | -3.08637 | -50.57641 | 2025-10-07 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| abab45d4-0678-3c40-8101-8adff219717d | -8.58213 | -44.3373 | 2025-10-07 04:55:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6779e69b-9df9-35ad-8d1c-35b899ab26d3 | -3.95007 | -55.78492 | 2025-10-07 04:55:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2e749f36-59dd-3623-a774-8954cabe23c2 | -2.89969 | -50.73029 | 2025-10-07 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d44439c4-1714-3e0d-84d0-993f4dccf236 | -3.86958 | -54.35229 | 2025-10-07 04:55:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a1a7ef32-017b-387d-aeed-f1d7cbdf5f79 | -6.17215 | -51.15742 | 2025-10-07 04:55:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1a1d3406-96f9-3c64-bbf0-8cae24329f7b | -7.69588 | -42.4157 | 2025-10-07 04:55:00 | NOAA-20 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 52fdf053-5e67-34e3-bfee-dd246b88c675 | -6.21847 | -44.33261 | 2025-10-07 04:55:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 5135b2b3-0c40-332f-bd81-e98e06da9b72 | -6.98169 | -42.87931 | 2025-10-07 04:55:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 15.7 |
| 19a1fb50-a2af-376a-bb5d-cfffccba5d82 | -6.72716 | -42.8199 | 2025-10-07 04:55:00 | NOAA-20 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| af45a9f7-3fb8-34a7-851e-090dbdc74e48 | -6.69681 | -42.85984 | 2025-10-07 04:55:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 66f1a091-9963-3352-9bdb-78b7a90ae6a0 | -2.24567 | -47.86945 | 2025-10-07 04:55:00 | NOAA-20 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ec749765-9473-30dd-b6a5-f1738c2459a1 | -4.06366 | -44.5091 | 2025-10-07 04:55:00 | NOAA-20 | SÃO MATEUS DO MARANHÃO | MARANHÃO | Brasil | 2111508 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| f2ef3235-a1f6-3211-902b-829b0485f13b | -7.89314 | -47.81567 | 2025-10-07 04:55:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 0a0cbdf5-f826-3dcf-a932-987018684c23 | -8.18116 | -43.34735 | 2025-10-07 04:55:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| e6454359-3e74-3bb3-b582-1464a824bf8c | -5.50014 | -43.08201 | 2025-10-07 04:55:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 7a653d4b-153d-32b4-b588-0ec70476a22d | -3.21858 | -50.7963 | 2025-10-07 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a2786494-e895-306f-8180-e68dc2f52ad2 | -7.69637 | -48.06105 | 2025-10-07 04:55:00 | NOAA-20 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b6b38917-f4b4-3e6e-98b5-af3e890bf4b7 | -5.55192 | -42.68574 | 2025-10-07 04:55:00 | NOAA-20 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 6.4 |
| c2fc639a-82b0-30f8-8d4d-a880d6e59de1 | -5.03357 | -45.55948 | 2025-10-07 04:55:00 | NOAA-20 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |


[Clique aqui para ver as próximas entradas](README85.md)
