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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b0a7d4a9-1f15-3a58-8bae-c7c28d53eae0 | -8.07 | -43.1216 | 2025-05-25 00:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 107.2 |
| 5e319810-962d-3242-894e-d71e3de56bd9 | -7.6577 | -46.0788 | 2025-05-25 00:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 70.7 |
| 146d86c0-0211-3148-85c4-498308d27376 | -8.0696 | -43.1452 | 2025-05-25 00:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 125.8 |
| 88cf1fba-c9ea-3cfa-860d-3b1831dffd15 | -7.2214 | -43.1153 | 2025-05-25 00:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 120.0 |
| c8838d49-1803-327c-9f9b-e91577bf2579 | -8.051 | -43.1237 | 2025-05-25 00:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 79.3 |
| f4118cfd-11c6-3402-8b1f-461be3716864 | -7.2025 | -43.1171 | 2025-05-25 00:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 85.4 |
| c7a2108d-57c7-323b-9983-6f8d92c33bd1 | -7.6574 | -46.1013 | 2025-05-25 00:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 176.4 |
| ba51be38-4360-3a5b-8d5d-2b3756953cb6 | -8.0507 | -43.1472 | 2025-05-25 00:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 106.5 |
| 3493615c-aae3-36db-b588-593efdd72e70 | -7.6386 | -46.103 | 2025-05-25 00:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 48.1 |
| 855c96fc-9020-3ce0-b689-bddc72c0921b | -7.2211 | -43.1388 | 2025-05-25 00:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 80.1 |
| 0e7e73e5-e851-3908-857d-0512a1d6018d | -20.9398 | -56.5998 | 2025-05-25 00:00:00 | GOES-19 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 60.0 |
| 294ef59d-46db-3d86-ba4d-178eafd8c317 | -20.9398 | -56.5998 | 2025-05-25 00:10:00 | GOES-19 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 66.0 |
| 070e6c6b-ec86-3706-a322-371f55e615c7 | -8.0507 | -43.1472 | 2025-05-25 00:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 90.3 |
| ba772247-66eb-3e9c-8f52-1bfc89930c13 | -20.9402 | -56.5786 | 2025-05-25 00:10:00 | GOES-19 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 44.7 |
| cd44e329-2a04-3c87-8caf-caa1d0f28494 | -7.2025 | -43.1171 | 2025-05-25 00:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 105.9 |
| 47d8aaf2-0c44-3afe-ae34-9c17eee57d68 | -8.051 | -43.1237 | 2025-05-25 00:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 77.1 |
| 891b9aed-19ef-3619-85e0-1f5baa4aa12e | -7.6574 | -46.1013 | 2025-05-25 00:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 116.2 |
| c485306b-ef41-3ea1-8a24-b36d5ce03c95 | -7.6577 | -46.0788 | 2025-05-25 00:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 59.9 |
| 46b717ec-1746-3e7e-bb82-35619d47aa42 | -7.6762 | -46.0995 | 2025-05-25 00:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 54.1 |
| 60dc7324-04f2-3e08-85a9-25702cb8fc99 | -8.0696 | -43.1452 | 2025-05-25 00:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 79.6 |
| 360fb3a9-75ad-3159-9da2-f9743f908c39 | -8.07 | -43.1216 | 2025-05-25 00:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 99.1 |
| 6229bbb4-d725-3b3a-aa75-fbc6ca0dccc5 | -7.2214 | -43.1153 | 2025-05-25 00:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 91.1 |
| a5997fdc-5c40-35a1-8d6d-d4f4b0ca6963 | -7.6386 | -46.103 | 2025-05-25 00:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 49.9 |
| bb46dfa5-450c-3209-9da8-39814f7c7404 | -7.6644 | -46.104801 | 2025-05-25 00:13:00 | METOP-C | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 65c6b92c-3e31-3014-9dcb-2d341d5b23f8 | -6.5539 | -44.480598 | 2025-05-25 00:13:00 | METOP-C | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 9690efb0-19a5-3c43-b156-ece3f30f703e | -12.2775 | -44.5937 | 2025-05-25 00:13:00 | METOP-C | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 07f6848a-3b76-3673-9428-e3048a280b5f | -5.581 | -43.592499 | 2025-05-25 00:13:00 | METOP-C | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 00b0989c-6a3f-3f4f-bf65-731ab70bce1c | -8.0627 | -43.134499 | 2025-05-25 00:13:00 | METOP-C | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| dbee1ff8-9f27-3f90-a4f0-88437325ef08 | -7.2045 | -43.120098 | 2025-05-25 00:13:00 | METOP-C | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 57ffbb0a-44a3-383c-ac01-c4bbd655df40 | -7.4041 | -43.730099 | 2025-05-25 00:13:00 | METOP-C | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 810f4eef-3ce7-3741-ac51-27c7091cdfd9 | -8.0545 | -43.143799 | 2025-05-25 00:13:00 | METOP-C | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 3fe30948-25bc-356f-8e6f-7fe706fd564a | -6.843 | -44.623001 | 2025-05-25 00:13:00 | METOP-C | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 5bdf3e35-f93b-3da3-8463-389d5d7ac893 | -7.2061 | -43.127102 | 2025-05-25 00:13:00 | METOP-C | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 22f602ed-6d95-3090-b6b1-c8e04fa1cf03 | -5.5803 | -43.453602 | 2025-05-25 00:13:00 | METOP-C | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 27f0cd33-3aa2-3ce6-98ea-5c2b018f94b6 | -9.9309 | -44.1791 | 2025-05-25 00:13:00 | METOP-C | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 55d712c8-4386-3c88-b50a-812bdddb0639 | -4.2872 | -48.2645 | 2025-05-25 00:13:00 | METOP-C | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2166482f-ca2b-329a-a330-fff79d6bdf33 | -7.6506 | -46.0886 | 2025-05-25 00:13:00 | METOP-C | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 9689f49c-4610-3d2d-bc18-7ed0d796d170 | -6.2272 | -43.3531 | 2025-05-25 00:13:00 | METOP-C | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 71a7a9d0-4b91-3709-aeca-b1e3a1831c38 | -8.7267 | -47.991402 | 2025-05-25 00:13:00 | METOP-C | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| e1691198-d54a-36dc-ba3d-6d83d5e2c724 | -8.0791 | -43.1161 | 2025-05-25 00:13:00 | METOP-C | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| a42552a9-0388-3038-8f24-c18f61fcee20 | -5.5837 | -45.199501 | 2025-05-25 00:13:00 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| df4116bb-eb47-3d03-9cce-9a9d82c46e14 | -7.234 | -43.113499 | 2025-05-25 00:13:00 | METOP-C | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| db14973f-252a-33e2-825b-f29546d623a9 | -8.0611 | -43.127499 | 2025-05-25 00:13:00 | METOP-C | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 2db36c5c-baae-3470-b061-c68a073ce123 | -8.0561 | -43.150799 | 2025-05-25 00:13:00 | METOP-C | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| d11f361e-9daa-3133-a16d-699650565f5e | -12.2794 | -44.602402 | 2025-05-25 00:13:00 | METOP-C | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| f0847184-dfec-3116-a5b9-545846a8e98e | -11.7532 | -47.257 | 2025-05-25 00:13:00 | METOP-C | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 7d7f9a11-b72f-36f4-88a6-4e1ee7046965 | -7.2356 | -43.120499 | 2025-05-25 00:13:00 | METOP-C | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| cb36ba45-625d-38ac-84e5-85bf283f5600 | -8.0693 | -43.118301 | 2025-05-25 00:13:00 | METOP-C | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| e97f85f0-f2c5-37fd-bab3-9d43e154806e | -8.0643 | -43.141602 | 2025-05-25 00:13:00 | METOP-C | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 16253f10-4b9f-3459-8b40-69831afaf67b | -12.8263 | -47.3806 | 2025-05-25 00:13:00 | METOP-C | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 15bdfee6-40fc-3ff6-b9c0-6ad9ba98f7d1 | -8.0741 | -43.1394 | 2025-05-25 00:13:00 | METOP-C | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| d75fe41b-3da0-302f-8a9a-b14fed82dd98 | -8.6478 | -45.4436 | 2025-05-25 00:13:00 | METOP-C | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 4849d076-ad0e-3774-a43a-191da1cb58cb | -6.8598 | -43.189899 | 2025-05-25 00:13:00 | METOP-C | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| b5b36ebc-2d52-3063-8a6f-c1e6b7bec38b | -6.9576 | -42.803799 | 2025-05-25 00:13:00 | METOP-C | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 35af00db-8332-3917-908c-b416cf380525 | -11.968 | -44.154598 | 2025-05-25 00:13:00 | METOP-C | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 3d7b7aa0-7c99-3347-b579-3fbbbab46c11 | -5.5819 | -43.460602 | 2025-05-25 00:13:00 | METOP-C | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 0de150ff-7169-3c09-8e32-886994f4f24c | -6.8614 | -43.1968 | 2025-05-25 00:13:00 | METOP-C | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| cb0d0da5-6142-314b-bff2-887a781633c3 | -5.5787 | -43.446701 | 2025-05-25 00:13:00 | METOP-C | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 6765ffc6-8649-3ccd-a513-63559a6ab7a3 | -5.604 | -45.3354 | 2025-05-25 00:13:00 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 6f3a1bcd-cbce-3fb3-9e5c-06c370735b21 | -7.2226 | -43.1087 | 2025-05-25 00:13:00 | METOP-C | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| a2599af7-39f8-372a-94d1-b95d95a238fd | -7.2324 | -43.106499 | 2025-05-25 00:13:00 | METOP-C | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 2c81154e-e33e-3da0-8b57-9930a4fff560 | -8.0709 | -43.125301 | 2025-05-25 00:13:00 | METOP-C | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| c2d03011-de7f-37ba-8166-5c63e2d28f1c | -5.5794 | -43.585499 | 2025-05-25 00:13:00 | METOP-C | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 1c59bf5a-ef81-3b01-a907-5df909218cc5 | -7.2242 | -43.1157 | 2025-05-25 00:13:00 | METOP-C | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 1d6a2168-c059-3801-8565-26cc3faa53ee | -11.1338 | -48.105 | 2025-05-25 00:13:00 | METOP-C | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 3a1f251f-072c-39a3-bd00-9c5a0f048d96 | -7.6604 | -46.086498 | 2025-05-25 00:13:00 | METOP-C | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 726eb35d-51cb-3ec1-aaca-7374e8aeba71 | -8.6459 | -45.434898 | 2025-05-25 00:13:00 | METOP-C | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 4eacaba5-784f-3dd3-98b9-e04a3a3286d2 | -8.0595 | -43.120399 | 2025-05-25 00:13:00 | METOP-C | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 0dc85ec9-0dec-35f7-aa10-22f982293542 | -6.5556 | -44.488098 | 2025-05-25 00:13:00 | METOP-C | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 2129c6a4-a406-3d30-9497-353c84ce164d | -7.6429 | -46.0998 | 2025-05-25 00:13:00 | METOP-C | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| aa6e9d12-dd7e-3648-8562-27f9df421221 | -6.9478 | -42.806 | 2025-05-25 00:13:00 | METOP-C | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| ed10f64f-0782-362f-b24e-63a73ff33fde | -6.5573 | -44.495602 | 2025-05-25 00:13:00 | METOP-C | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 6a043019-6fe9-3fa6-b46b-bbd1292d2b13 | -8.7241 | -47.979 | 2025-05-25 00:13:00 | METOP-C | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 02a9ad91-30ce-3992-a67e-986737ff4954 | -11.9778 | -44.152401 | 2025-05-25 00:13:00 | METOP-C | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 3b28b9ab-d0e2-31b3-989e-1b7778c06ed2 | -6.2288 | -43.3601 | 2025-05-25 00:13:00 | METOP-C | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 9fa5cb02-26af-32a1-b3f9-12f2e0e74556 | -5.5655 | -43.478901 | 2025-05-25 00:13:00 | METOP-C | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| cd541bd6-f60f-37ad-8475-f47c1f6e2d6e | -5.6022 | -45.327499 | 2025-05-25 00:13:00 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 789a5deb-a81a-3bb9-bf37-ca35b1bb54bc | -7.6624 | -46.0956 | 2025-05-25 00:13:00 | METOP-C | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 45f21d90-4a17-3ecc-b32a-fc16694ab8a3 | -7.2077 | -43.133999 | 2025-05-25 00:13:00 | METOP-C | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 24b649e4-d555-328e-a90d-44f8ebf9c83c | -7.6526 | -46.097698 | 2025-05-25 00:13:00 | METOP-C | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 047c0761-8fae-33da-bd2b-7b36190b36be | -5.582 | -45.1917 | 2025-05-25 00:13:00 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 9ec9abde-2467-328b-817f-3d980d3c4f2e | -8.0725 | -43.132401 | 2025-05-25 00:13:00 | METOP-C | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| f2b4b25e-55a8-3aff-aacd-67a1ffc02501 | -7.2175 | -43.131802 | 2025-05-25 00:13:00 | METOP-C | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 891dc3f6-6c72-327e-b28c-860382f0b4d1 | -8.0529 | -43.1367 | 2025-05-25 00:13:00 | METOP-C | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 63a7216e-a555-3d8d-b859-670ded69f498 | -7.2258 | -43.1227 | 2025-05-25 00:13:00 | METOP-C | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| f15ea9f6-b485-31f8-a72f-4133d2e45727 | -11.1435 | -48.103001 | 2025-05-25 00:13:00 | METOP-C | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 23fe28b0-4c9f-322e-a5b3-446aac322f0b | -7.2159 | -43.124901 | 2025-05-25 00:13:00 | METOP-C | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| ccba3d23-2482-3755-8397-a2956426b485 | -11.7506 | -47.244701 | 2025-05-25 00:13:00 | METOP-C | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 185480db-2edd-33f9-9461-90322f218375 | -7.2143 | -43.117901 | 2025-05-25 00:13:00 | METOP-C | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 5e833d2f-1395-3142-ac69-98a9f324ac38 | -4.2896 | -48.275501 | 2025-05-25 00:13:00 | METOP-C | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 443d8d35-59b9-3424-8b62-7231591799ff | -11.9697 | -44.1628 | 2025-05-25 00:13:00 | METOP-C | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 81aed83f-e9c0-333b-81ec-07bd75eba38d | -7.6546 | -46.106899 | 2025-05-25 00:13:00 | METOP-C | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| dd18c47a-182b-38a2-81c0-a688e1dcb978 | -6.9494 | -42.812901 | 2025-05-25 00:13:00 | METOP-C | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| d388dcbf-0fe9-3449-bda2-66866f03400b | -7.6577 | -46.0788 | 2025-05-25 00:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 50.0 |
| 8de02a6d-9ff1-33c2-ab99-095688a68a4f | -7.6762 | -46.0995 | 2025-05-25 00:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 51.4 |
| cf23b694-f058-3c6f-8de9-7b65b8f1de64 | -8.0696 | -43.1452 | 2025-05-25 00:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 78.7 |
| ef75f189-fd40-331a-9f2a-81618b33e062 | -8.07 | -43.1216 | 2025-05-25 00:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 94.4 |
| a40c858e-0c43-30a5-87cc-b4cae0d2ac4a | -8.0507 | -43.1472 | 2025-05-25 00:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 82.9 |
| 9f4ca53f-50cd-33b9-9e5f-119c0cd33b1f | -7.6574 | -46.1013 | 2025-05-25 00:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 133.1 |
| 3fcad1fe-a219-3c0e-a10d-fc8e3fc677f9 | -7.2214 | -43.1153 | 2025-05-25 00:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 94.7 |


[Clique aqui para ver as próximas entradas](README2.md)
