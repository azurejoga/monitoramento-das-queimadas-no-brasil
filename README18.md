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

## Dados Diários - Página 18

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6660b259-1e14-35b8-b7c7-f013a9381328 | -0.2646 | -51.53812 | 2024-11-22 04:12:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7b849a3e-17d4-38f7-b5e1-069744cd955b | -1.25671 | -53.36381 | 2024-11-22 04:12:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 71d5ab04-9f05-346d-b07c-02bcce1f4362 | -6.71397 | -38.97076 | 2024-11-22 04:12:00 | NPP-375D | LAVRAS DA MANGABEIRA | CEARÁ | Brasil | 2307502 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 1613f620-f73c-3073-9ba7-bd7293b8a2c4 | -3.71354 | -52.09256 | 2024-11-22 04:12:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4e295c90-3d50-3cad-8792-bfad8a76c537 | -2.69657 | -46.07314 | 2024-11-22 04:12:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5011f583-7a0a-30d4-be58-21dae060698f | -5.96472 | -48.0568 | 2024-11-22 04:12:00 | NPP-375D | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b05f28b8-b617-3dc8-a89c-61c8884e4ebd | -6.50365 | -42.19154 | 2024-11-22 04:12:00 | NPP-375D | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 8c99da4c-bab7-3f39-af58-82c6cbb2043e | -3.33439 | -53.33813 | 2024-11-22 04:12:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 96c4d835-8d6f-3320-a4b4-b5a33bda711a | -1.19901 | -51.96303 | 2024-11-22 04:12:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 7f8bf35a-1ec7-3b61-a007-8def0a6ebca4 | -1.78289 | -47.10722 | 2024-11-22 04:12:00 | NPP-375D | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 8b9838b4-730f-3843-bfad-664b13bc48f1 | -0.27857 | -51.56027 | 2024-11-22 04:12:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 67f09cf6-83bb-308d-ac65-9c2581b6b09e | -5.24677 | -42.63615 | 2024-11-22 04:12:00 | NPP-375D | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 7.3 |
| e4a0b326-3b33-3020-9d5d-84cde97a6e8d | -4.82173 | -43.69345 | 2024-11-22 04:12:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e40457fc-e472-3cf5-861a-d6f9934935fa | -4.21711 | -48.65483 | 2024-11-22 04:12:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 7cbccae2-585b-33be-840f-e77be34a6b4a | -1.20027 | -51.9551 | 2024-11-22 04:12:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 14172977-2e1b-3d1e-946b-8c4222753bc1 | -3.11164 | -45.19323 | 2024-11-22 04:12:00 | NPP-375D | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f31024f0-43c5-34af-b16a-70ff486bc4b4 | -3.83888 | -41.56288 | 2024-11-22 04:12:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| bb18f458-347b-3ac9-8834-ba45d345b7d4 | -5.09199 | -45.94094 | 2024-11-22 04:12:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 16d68025-636b-3d76-a8d8-07b33515762e | -2.08472 | -46.28259 | 2024-11-22 04:12:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 81348aaa-3da9-3a48-b629-54bc49fe7276 | -1.73152 | -52.71309 | 2024-11-22 04:12:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c58084b9-70d5-30f6-98a9-90980ceaacb1 | -5.68385 | -46.33593 | 2024-11-22 04:12:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 454d120d-32f5-3ff3-b71a-d64b22c29d99 | -4.66488 | -46.53794 | 2024-11-22 04:12:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| fef0b0ac-9f26-30a6-8011-9e9f714b8e82 | -3.65219 | -51.14585 | 2024-11-22 04:12:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 873dd4f6-cf03-37c5-9475-aebf9e48e29d | -1.71947 | -52.48522 | 2024-11-22 04:12:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 66e769ef-3f65-33ba-a7a1-f1e702e95e2f | -5.47428 | -42.07075 | 2024-11-22 04:12:00 | NPP-375D | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| bc5cec3c-1fdf-32f5-8a93-54d108ee87b5 | -7.7419 | -38.61454 | 2024-11-22 04:12:00 | NPP-375D | SÃO JOSÉ DO BELMONTE | PERNAMBUCO | Brasil | 2613503 | 26 | 33 | nan | nan | nan | Caatinga | 5.0 |
| 604038d4-4399-32fe-a76a-52702114359e | -2.55838 | -46.5486 | 2024-11-22 04:12:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1bd29a93-9db0-3e64-ab56-416d7590b549 | -1.74037 | -52.39388 | 2024-11-22 04:12:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 7c7609ef-5793-3f5d-8ce0-898066dc500c | -1.29905 | -52.22329 | 2024-11-22 04:12:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f1f2f4c8-52fb-35df-8998-2e60121eb6ba | -3.00905 | -51.30954 | 2024-11-22 04:12:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c61c34fd-9c1d-38ee-9114-9029fa145957 | -5.50942 | -45.4898 | 2024-11-22 04:12:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 07e7b68c-db96-3586-9bfe-9ec3eed6ce10 | -2.83414 | -51.82145 | 2024-11-22 04:12:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 19ef248b-5ff1-353d-b150-be8ea0f563ae | -1.74308 | -52.3772 | 2024-11-22 04:12:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 100c331a-ddfd-3109-b064-765fe91f0cb2 | -2.73528 | -47.54048 | 2024-11-22 04:12:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bfeaf73d-9866-3e6b-8d4d-3ebadfa605dc | -3.26611 | -45.37209 | 2024-11-22 04:12:00 | NPP-375D | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c57cd496-f3c5-3084-8566-bbc2d3a76d25 | -3.2293 | -54.25024 | 2024-11-22 04:12:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 13.8 |
| d5e90f87-f418-3059-846a-195e7235ff93 | -3.5179 | -54.69103 | 2024-11-22 04:12:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 54375029-3b5e-355e-bbaa-7b99ebb287ec | -4.70091 | -48.29707 | 2024-11-22 04:12:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| efd666ab-76c2-33da-b3bf-252645018643 | -5.44449 | -45.58383 | 2024-11-22 04:12:00 | NPP-375D | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7362e29f-f57a-3f66-a95d-d11fa63155bb | -3.82324 | -52.26618 | 2024-11-22 04:12:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 903ae7ed-fbe0-3f8b-b094-4e6d68ae0f97 | -0.05237 | -51.23996 | 2024-11-22 04:12:00 | NPP-375D | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 12.4 |
| a3f2f766-66a1-392f-9380-104bc15c2283 | -3.64159 | -54.32668 | 2024-11-22 04:12:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3a2a1f38-c049-3b92-ae87-399163dde622 | -3.23121 | -54.23901 | 2024-11-22 04:12:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| de7d4208-e534-3d8f-9db0-ac8b301b9408 | -2.44425 | -46.53786 | 2024-11-22 04:12:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 96e9e8d5-74fd-3850-9bc3-c5e127deab1f | -5.9352 | -43.78268 | 2024-11-22 04:12:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| aa63331a-1d89-3a9a-9a06-2acb032cf343 | -2.73943 | -47.54114 | 2024-11-22 04:12:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4edaed45-2545-3632-a6fc-d776c63e3178 | -1.13049 | -53.40831 | 2024-11-22 04:12:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| bd4e2761-faaa-3e6f-8b9e-a72940216d78 | -2.64732 | -47.13131 | 2024-11-22 04:12:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ceb58c3d-e11e-321b-bfee-abdb94ead2fa | -4.40419 | -44.11685 | 2024-11-22 04:12:00 | NPP-375D | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f513e388-1fe8-3699-b254-8502d3434a97 | -3.07207 | -53.29454 | 2024-11-22 04:12:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b8d305e3-0c17-38d2-a906-ba4fe562107f | -3.75887 | -46.11786 | 2024-11-22 04:12:00 | NPP-375D | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 373fd89c-750f-314c-930a-e9ccdf438501 | -3.22381 | -54.24358 | 2024-11-22 04:12:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 13.8 |
| a3c1d49f-7148-3e57-9d6b-e14057dfa77b | -2.08784 | -46.28798 | 2024-11-22 04:12:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 85c7ec5e-4c87-3855-b517-48174edfa123 | -4.19813 | -53.49839 | 2024-11-22 04:12:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 18799a9b-c5d1-34a7-94cc-efb3dfd052be | -3.20795 | -46.54163 | 2024-11-22 04:12:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2985a0bb-7f21-3c57-bea8-2341729c4664 | -3.00576 | -45.1316 | 2024-11-22 04:12:00 | NPP-375D | MATINHA | MARANHÃO | Brasil | 2106508 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bc35c5f6-92ba-371d-a461-51f8befeb100 | -1.96157 | -52.99571 | 2024-11-22 04:12:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2ad5c2ab-8323-3fc8-8c95-20b6de9de55b | -1.12499 | -53.40232 | 2024-11-22 04:12:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| bbcf0962-304c-3672-9087-b672db1faa5a | -1.22974 | -51.74412 | 2024-11-22 04:12:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ef4461ae-b005-3485-aa1d-6df84b20c9aa | -2.69583 | -46.07766 | 2024-11-22 04:12:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6236ec52-e86b-3908-9684-b29dc13e2bd5 | -5.57722 | -42.59901 | 2024-11-22 04:12:00 | NPP-375D | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| f5ad2cfa-6418-3d17-820e-c7de77db1cfa | -3.24868 | -54.25308 | 2024-11-22 04:12:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 3d1839a8-ae27-334a-969e-b221c6f3b419 | -4.00686 | -43.24762 | 2024-11-22 04:12:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3acfe4d8-8aa2-3915-b9ba-07abcc1f3d42 | -2.55447 | -46.54799 | 2024-11-22 04:12:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 325bfe69-187f-384e-a107-90cc704ce0fd | -3.52995 | -51.10454 | 2024-11-22 04:12:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c4f899ae-6654-32e1-8878-66258bd25a14 | -4.05568 | -46.21891 | 2024-11-22 04:12:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9e36e2db-c585-3ac8-90bd-68b1d3e730b6 | -1.72179 | -52.70858 | 2024-11-22 04:12:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7395488d-214d-3f46-9eaa-b6b808bb86bd | -4.34486 | -45.53133 | 2024-11-22 04:12:00 | NPP-375D | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a1b5a76f-b5e2-35bb-9747-d6224de5fb31 | -4.067 | -50.00279 | 2024-11-22 04:12:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c28ef449-d2c8-3cc2-bd79-a6f2e3cc9e3b | -3.24777 | -54.2585 | 2024-11-22 04:12:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| c5c4bd71-65d1-3fcc-b373-de2e2bebcb36 | -4.43752 | -42.59362 | 2024-11-22 04:12:00 | NPP-375D | LAGOA ALEGRE | PIAUÍ | Brasil | 2205557 | 22 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 40b37939-d696-36a5-8590-aac4b9890389 | -5.95205 | -44.4641 | 2024-11-22 04:12:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 79d17f79-e9f0-32fa-8974-81ee738f42ab | -3.33565 | -53.33038 | 2024-11-22 04:12:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2e111f31-e3ec-31c2-9ba8-5450de87f919 | -3.29049 | -53.8529 | 2024-11-22 04:12:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| bfaada0e-d9a9-3df7-a2db-697fba86241e | -3.83257 | -52.26081 | 2024-11-22 04:12:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 8d09a5c9-6896-30fa-bb0e-5b231b519457 | -2.65437 | -46.24446 | 2024-11-22 04:12:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 84c34fdd-f9b2-354f-a395-0ae734b586ee | -4.13448 | -46.70697 | 2024-11-22 04:12:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d74befc2-1c8a-3815-8584-9cce55e8dd66 | -3.07926 | -45.97434 | 2024-11-22 04:12:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 07d01ba0-3001-3ba4-b265-1c234f4ab454 | -4.1488 | -43.88061 | 2024-11-22 04:12:00 | NPP-375D | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d6ffc4f2-0b92-3013-9680-41df9b629b41 | -4.06399 | -46.84096 | 2024-11-22 04:12:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 19d44018-0e41-34f5-88b4-edb1d207ea8e | -1.09687 | -47.50439 | 2024-11-22 04:12:00 | NPP-375D | IGARAPÉ-AÇU | PARÁ | Brasil | 1503200 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5f8591b0-1bea-3a4b-8472-787fcf6c2166 | -3.2404 | -54.26289 | 2024-11-22 04:12:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 7572ee21-19ce-3700-ba5b-93529ef7b3dd | -5.25983 | -43.19516 | 2024-11-22 04:12:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 20180600-7823-3282-b080-1be1d6008ae4 | -3.34019 | -53.34072 | 2024-11-22 04:12:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 5c221d37-f5c3-31a7-a236-19df7f0c6abe | -3.65071 | -42.26153 | 2024-11-22 04:12:00 | NPP-375D | MORRO DO CHAPÉU DO PIAUÍ | PIAUÍ | Brasil | 2206670 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 704ac55d-0681-35b8-93ba-4ee008b6eff0 | -2.16929 | -47.9525 | 2024-11-22 04:12:00 | NPP-375D | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 26b9e751-4176-3339-a3e7-1f0993f47938 | -0.80612 | -51.78514 | 2024-11-22 04:12:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 292488dc-96a8-3f08-ab1c-cd2abc3e9954 | -3.20273 | -54.25066 | 2024-11-22 04:12:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| f8e88698-be05-38a4-bd3f-e489676cb7a2 | -4.06219 | -50.002 | 2024-11-22 04:12:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 877c50bf-7fed-3cfe-beab-994eeaf3b7ee | -0.3025 | -51.48164 | 2024-11-22 04:12:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9d34aaa0-981d-331b-9959-0299423c267c | -3.79132 | -44.01758 | 2024-11-22 04:12:00 | NPP-375D | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 338f98e5-8b8a-37e5-954a-e25c759f526e | -1.82896 | -46.28219 | 2024-11-22 04:12:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d35d7759-0548-37f1-8aed-22f6f92720c9 | -3.10982 | -54.29092 | 2024-11-22 04:12:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 58e6f176-805b-316d-b8a2-30e98750c8fd | -3.75441 | -46.12175 | 2024-11-22 04:12:00 | NPP-375D | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 3.3 |
| d5be93a4-2174-35a7-a66b-d9011322b391 | -2.44737 | -46.54339 | 2024-11-22 04:12:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6fff515f-7223-3be6-881e-8be3296b1fc0 | -2.74423 | -54.13295 | 2024-11-22 04:12:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b83e2c46-d37c-3ea0-99ca-4b9ae1e0e0b2 | -2.01743 | -51.17353 | 2024-11-22 04:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 89e1f88f-6eee-3be9-8f1b-fac3e0db9583 | -2.92337 | -46.83913 | 2024-11-22 04:12:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 630df933-f381-38b0-a1e6-005686e3a52d | -1.19979 | -51.77419 | 2024-11-22 04:12:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 1b6c5ef7-d391-334d-b5f5-7f714acdc9bc | -4.24251 | -48.63728 | 2024-11-22 04:12:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |


[Clique aqui para ver as próximas entradas](README19.md)
