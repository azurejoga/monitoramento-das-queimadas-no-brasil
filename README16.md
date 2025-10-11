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

## Dados Diários - Página 16

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| cb462a0b-fac2-30d6-8f00-1b3ebe0dcc9e | -13.2257 | -42.317 | 2025-10-11 04:00:00 | GOES-19 | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 182.7 |
| fc514de1-e506-3437-b355-562665879e9e | -17.2722 | -46.8932 | 2025-10-11 04:00:00 | GOES-19 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 97.2 |
| d7867b8b-19b1-3066-93d3-a4612670e34d | -10.5084 | -47.3624 | 2025-10-11 04:00:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 68.6 |
| 6a8fef80-e521-337c-9c22-93c6946ecca5 | -10.5277 | -47.3379 | 2025-10-11 04:00:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 50.9 |
| b7bb5f63-0864-34d0-aacb-dac382ea80ae | -13.2057 | -42.345 | 2025-10-11 04:00:00 | GOES-19 | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 264.3 |
| 994a1419-766f-3eb8-b930-583906fc91ec | -13.2252 | -42.3414 | 2025-10-11 04:00:00 | GOES-19 | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 330.1 |
| b818fae5-d412-3384-a93a-2e0096ec4a06 | -13.2062 | -42.3206 | 2025-10-11 04:00:00 | GOES-19 | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 140.4 |
| 427c4b49-b5e1-3fd8-9269-7bc0a28ee379 | -8.1996 | -43.3189 | 2025-10-11 04:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 69.3 |
| 6a1815bc-1998-3e3d-b7a5-816f9607eb3c | -13.2257 | -42.317 | 2025-10-11 04:10:00 | GOES-19 | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 171.6 |
| 98702eee-8b2e-3065-acb7-0249f1cb4fa9 | -13.2252 | -42.3414 | 2025-10-11 04:10:00 | GOES-19 | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 352.1 |
| dca28421-90d6-3a0e-bcbe-de641d42858a | -13.2057 | -42.345 | 2025-10-11 04:10:00 | GOES-19 | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 274.9 |
| 048990d0-5c29-3d4b-928e-f153084ba95e | -13.2062 | -42.3206 | 2025-10-11 04:10:00 | GOES-19 | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 133.0 |
| 6473b34d-9abe-3173-a7ef-a8bd962f34e5 | -17.2722 | -46.8932 | 2025-10-11 04:10:00 | GOES-19 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 109.4 |
| fff88afd-0698-3129-a5f1-a3c1924fc2ea | -8.1996 | -43.3189 | 2025-10-11 04:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 83.2 |
| cb25c6a4-3ea1-399c-aaf6-c3c37f48f716 | -13.2057 | -42.345 | 2025-10-11 04:20:00 | GOES-19 | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 170.4 |
| ab8e4516-24af-3471-94c5-7dec12947f83 | -17.2722 | -46.8932 | 2025-10-11 04:20:00 | GOES-19 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 107.1 |
| 7504091b-c41d-3b11-b602-6f00357f6f2c | -13.2252 | -42.3414 | 2025-10-11 04:20:00 | GOES-19 | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 291.6 |
| 11a5706c-d5c8-3290-8525-0bc0d0f45df9 | -8.1996 | -43.3189 | 2025-10-11 04:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 70.9 |
| f6b0f53e-298d-3722-a0ca-f17ab494435a | -13.2257 | -42.317 | 2025-10-11 04:20:00 | GOES-19 | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 201.8 |
| be5df2a2-3040-3094-8261-722ab247f842 | -13.2062 | -42.3206 | 2025-10-11 04:20:00 | GOES-19 | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 123.9 |
| 38c5e713-4eb2-3fbb-8482-a85b6d068f99 | 1.21345 | -50.86532 | 2025-10-11 04:29:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 3cf42e08-6743-3cc7-b2d7-dad490446643 | 1.18826 | -50.88164 | 2025-10-11 04:29:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 3.7 |
| a4df3aab-0e87-3228-b5fc-7dc9fa6920a4 | 1.2095 | -50.86591 | 2025-10-11 04:29:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 047a11ef-9654-3132-bcaa-51d5126fee3a | 1.20632 | -50.87155 | 2025-10-11 04:29:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 089084c5-171a-3306-adab-9faae224e2ea | 1.21428 | -50.86747 | 2025-10-11 04:29:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7a2b8abc-7e3e-3f2e-a766-2f043b40f554 | 1.20484 | -50.88434 | 2025-10-11 04:29:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c54021fd-766b-3992-8192-3fdb3a2f8b36 | 1.20954 | -50.86302 | 2025-10-11 04:29:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 4.5 |
| c0cddcd5-3223-3d30-a0d1-c0bd079b19d8 | 1.19854 | -50.89563 | 2025-10-11 04:29:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0d39f7c2-fd92-31d5-baae-1b431420f87d | 1.20085 | -50.86204 | 2025-10-11 04:29:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 63749b3a-17d1-360d-a811-19c6335d9a07 | 1.2072 | -50.87369 | 2025-10-11 04:29:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 2.6 |
| be8a866a-5b08-3cf2-8bda-dd043dad1bc7 | 1.20556 | -50.8665 | 2025-10-11 04:29:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f9a7f224-a546-384f-bf63-598929c8d060 | 1.19535 | -50.87541 | 2025-10-11 04:29:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ad516810-1746-3c4d-b9e7-a3dc7ffa3847 | 1.20709 | -50.8766 | 2025-10-11 04:29:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d08a753f-4c81-31f0-a7b6-00e6d3d6c354 | 1.20314 | -50.87719 | 2025-10-11 04:29:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c9285673-e1d3-3955-b798-661057ecc4d5 | 1.20405 | -50.87931 | 2025-10-11 04:29:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c84f0f64-bf45-3444-9c36-c868e023d164 | 1.19771 | -50.86477 | 2025-10-11 04:29:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 6ace3087-e136-38c3-aa80-b91631764d5f | 1.21034 | -50.86806 | 2025-10-11 04:29:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.7 |
| baf1d2b3-17ce-392b-aa24-c1550f0a789a | 1.2064 | -50.86864 | 2025-10-11 04:29:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 7899ffb7-84c1-3b49-b259-626e0dc4e933 | 1.20086 | -50.85916 | 2025-10-11 04:29:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 72302df5-834c-3037-aadb-a21c88951e58 | 1.2039 | -50.88223 | 2025-10-11 04:29:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 1441256d-fa36-32e6-bd29-50f7d8001829 | 1.2048 | -50.86145 | 2025-10-11 04:29:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f0e9d1fa-b828-34b8-a415-f3d29c41574e | 1.1922 | -50.88103 | 2025-10-11 04:29:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 22dadd76-90a0-319f-83c1-8d1ced6d342a | 1.2056 | -50.8636 | 2025-10-11 04:29:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0a17365a-1c6e-3194-ba78-878ec212dbda | 1.20874 | -50.86086 | 2025-10-11 04:29:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 2.2 |
| aa719f74-f067-399d-a873-a9484dd1ddc5 | 1.20165 | -50.86418 | 2025-10-11 04:29:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0f5a2ef1-f0fb-3b4c-9f80-a6d41e6c4b66 | 1.19691 | -50.86264 | 2025-10-11 04:29:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 87f80e68-f526-3ecc-a239-00b0cf2633ca | -13.2062 | -42.3206 | 2025-10-11 04:30:00 | GOES-19 | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 115.3 |
| fdaddb4a-a78b-3b3e-a414-9de57553c0fa | -13.2057 | -42.345 | 2025-10-11 04:30:00 | GOES-19 | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 154.4 |
| f759e1e0-3f69-38b1-9823-cb383a43ca11 | -17.2722 | -46.8932 | 2025-10-11 04:30:00 | GOES-19 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 74.0 |
| 864efa97-1427-3262-9663-b37c58799df6 | -13.2252 | -42.3414 | 2025-10-11 04:30:00 | GOES-19 | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 216.8 |
| 6233841b-6b5c-3f62-976b-5d63ba2beabf | -8.1996 | -43.3189 | 2025-10-11 04:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 71.2 |
| f682e585-7cb6-38f5-9a34-794ea3535460 | -13.2257 | -42.317 | 2025-10-11 04:30:00 | GOES-19 | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 153.3 |
| 0b50fc09-204c-3112-acd1-da7f5cc83554 | -7.74793 | -46.67136 | 2025-10-11 04:32:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.3 |
| b181e7d5-a78d-3de9-ae30-6f23071fb5bf | -7.67797 | -42.5774 | 2025-10-11 04:32:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| cbe4fbb6-0a15-3d33-83b4-41638a41d15a | -7.79804 | -42.42527 | 2025-10-11 04:32:00 | NOAA-21 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 393f6c56-18af-30af-8834-ad38dc8b93c9 | -4.13564 | -47.65514 | 2025-10-11 04:32:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| aba19532-159d-37be-bc00-d8b4578ecf3e | -6.4306 | -45.82748 | 2025-10-11 04:32:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1ecbf02a-6243-3414-b3a5-5411be6303bc | -4.91344 | -48.55257 | 2025-10-11 04:32:00 | NOAA-21 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5ddfd292-3bba-3819-ab8b-5109de57c920 | -3.40555 | -46.90445 | 2025-10-11 04:32:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 01a2ac80-c39c-3bb4-9de0-3cb80c52e339 | -4.42544 | -43.47266 | 2025-10-11 04:32:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 7f86fe7b-e6d3-3067-a34f-a631d5c48eb6 | -6.24911 | -47.22021 | 2025-10-11 04:32:00 | NOAA-21 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 80812652-cb9d-373e-b25b-cc4c3e1ea973 | -8.02046 | -44.46367 | 2025-10-11 04:32:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 6d58016e-60d1-337b-95a5-fb01125c04fc | -8.04835 | -44.11721 | 2025-10-11 04:32:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9d4ee3ce-dcd2-3743-b6e2-b469a60f5f34 | -6.03829 | -42.50311 | 2025-10-11 04:32:00 | NOAA-21 | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 6594d46e-7701-39b2-aeb9-5d11f04105aa | -3.39726 | -42.39207 | 2025-10-11 04:32:00 | NOAA-21 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 47b44399-6ed7-3eb0-83ac-c2d65feed192 | -5.58937 | -42.98462 | 2025-10-11 04:32:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| a1e8b1bb-1623-33ea-981d-b6d8e05b569a | -3.9811 | -47.88136 | 2025-10-11 04:32:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 8710ebdf-9ab9-34f1-87ed-d6b4becd0b44 | -8.17686 | -43.31355 | 2025-10-11 04:32:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 1af8393f-e12a-3562-96f1-525fd2f1fbab | -5.97318 | -42.26927 | 2025-10-11 04:32:00 | NOAA-21 | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 5c7ff876-a55a-3375-a0f9-8989bdc28448 | -3.69942 | -43.19609 | 2025-10-11 04:32:00 | NOAA-21 | MATA ROMA | MARANHÃO | Brasil | 2106409 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ff8ac652-f078-341b-96a8-34f250fb9112 | -2.73263 | -42.5397 | 2025-10-11 04:32:00 | NOAA-21 | PAULINO NEVES | MARANHÃO | Brasil | 2108058 | 21 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 8bab8f18-f8a6-39fa-a136-ae3fdc1cc3a6 | -9.15976 | -41.06137 | 2025-10-11 04:32:00 | NOAA-21 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| f07ce98b-7418-3300-86d1-3ce185d46f01 | -6.65228 | -43.92018 | 2025-10-11 04:32:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| d57ff745-1dc1-3a19-95cd-8ce8fea8403d | -8.38626 | -42.26481 | 2025-10-11 04:32:00 | NOAA-21 | SÃO JOÃO DO PIAUÍ | PIAUÍ | Brasil | 2210003 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| b409cd44-734f-36c4-acad-109fd8f243c3 | -5.86863 | -42.83429 | 2025-10-11 04:32:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| eff759f3-65ec-3028-b83f-135082cc5f23 | -2.55315 | -48.39169 | 2025-10-11 04:32:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 4b9bee9f-44cb-367d-afd7-308abe75b5cc | -7.80296 | -42.42432 | 2025-10-11 04:32:00 | NOAA-21 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 804c5f6a-1635-3a21-b6ca-66cbb2ad5920 | -6.2568 | -46.1145 | 2025-10-11 04:32:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| b542aeb1-024c-305a-a5c4-9bf0600556e3 | -6.43744 | -45.82856 | 2025-10-11 04:32:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| eec71c62-fa33-3ea5-b4e1-f5a18cc60815 | -7.98428 | -47.65627 | 2025-10-11 04:32:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9da5c7bf-4150-3088-9810-f040901bc351 | -5.86107 | -42.85788 | 2025-10-11 04:32:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 9.9 |
| a6d4aca4-9098-3e0b-8435-9aa252c5f5c0 | -7.80169 | -42.42984 | 2025-10-11 04:32:00 | NOAA-21 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| fff558e0-bd06-3b31-bcae-c9832b4b83ce | -6.75641 | -39.67419 | 2025-10-11 04:32:00 | NOAA-21 | TARRAFAS | CEARÁ | Brasil | 2313252 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| db70c2eb-f405-3d14-a0e6-d54dd7d74d8a | -6.81873 | -42.8036 | 2025-10-11 04:32:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 9e886dc1-2553-3c26-9d6f-571a04ce977f | -6.66342 | -41.37448 | 2025-10-11 04:32:00 | NOAA-21 | SÃO JOÃO DA CANABRAVA | PIAUÍ | Brasil | 2209856 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 79e90cd1-a42f-39dd-9233-244e0d742413 | -3.97962 | -40.9191 | 2025-10-11 04:32:00 | NOAA-21 | IBIAPINA | CEARÁ | Brasil | 2305308 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| ba553532-7f95-3413-bc3e-2a7d0f1ca2f6 | -6.04536 | -42.51176 | 2025-10-11 04:32:00 | NOAA-21 | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 230a5442-0db9-3b5e-8d97-4f269eb732e4 | -2.14697 | -47.50716 | 2025-10-11 04:32:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 627328e6-1a91-330f-984e-d881c5c2244e | -7.85776 | -44.12283 | 2025-10-11 04:32:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b7607a76-85e4-3a56-818b-2d085b0086b1 | -6.94896 | -45.60051 | 2025-10-11 04:32:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| be8f18da-ac3c-3431-bf7e-03ce396d76aa | -7.5251 | -47.78648 | 2025-10-11 04:32:00 | NOAA-21 | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 234ace96-eda3-3d80-9683-7896eff34402 | -8.19931 | -43.32758 | 2025-10-11 04:32:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 11.7 |
| e83026ed-fe2c-33c1-96ee-de6f44123596 | -7.87182 | -44.45239 | 2025-10-11 04:32:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 59d0de61-ee80-39ec-b18c-1c2a48a1df90 | -6.50506 | -44.4367 | 2025-10-11 04:32:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 389d5050-8373-3f76-a64b-63c624fb2708 | -5.7053 | -42.79181 | 2025-10-11 04:32:00 | NOAA-21 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 6f010d6c-c4df-3ef8-ba2c-117d599679de | -7.25165 | -43.49885 | 2025-10-11 04:32:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| c7440e00-749c-3519-b9aa-0d5b991046e5 | -7.30231 | -45.56061 | 2025-10-11 04:32:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| af359178-817c-31fc-a1ce-9b1c231d5160 | -6.45783 | -44.57804 | 2025-10-11 04:32:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| a3952d9a-7de1-3c65-89d1-1487be41fa5c | -6.43576 | -45.81676 | 2025-10-11 04:32:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| cd5a5595-3e09-3f87-a474-27c9e15a328d | -4.9427 | -38.00124 | 2025-10-11 04:32:00 | NOAA-21 | RUSSAS | CEARÁ | Brasil | 2311801 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |


[Clique aqui para ver as próximas entradas](README17.md)
