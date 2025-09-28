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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 67b3b4c9-2713-318a-8870-67ad8764fa04 | -14.93182 | -49.37041 | 2025-09-28 00:50:00 | TERRA_M-M | SÃO LUIZ DO NORTE | GOIÁS | Brasil | 5220157 | 52 | 33 | nan | nan | nan | Cerrado | 16.8 |
| 6b9e20ee-a286-3363-bae4-92685bc802f4 | -22.61701 | -49.03086 | 2025-09-28 00:50:00 | TERRA_M-M | AGUDOS | SÃO PAULO | Brasil | 3500709 | 35 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 5747b0b5-6c85-3cff-9ebd-ead21f684db7 | -14.48203 | -48.58163 | 2025-09-28 00:50:00 | TERRA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 27.7 |
| 6a67ec47-2a45-36a2-8380-22d4491e24cc | -14.53951 | -48.42399 | 2025-09-28 00:50:00 | TERRA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 9.9 |
| e3371f59-1107-3b1b-a457-60bcbdda8834 | -16.96643 | -51.28051 | 2025-09-28 00:50:00 | TERRA_M-M | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 6.2 |
| eb51bf0f-3e7b-3a91-abf3-631ddfc9aba6 | -15.08959 | -48.33227 | 2025-09-28 00:50:00 | TERRA_M-M | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 16.1 |
| c372b8cf-fed9-3ed8-82c1-b2acbb6c1d7d | -15.21024 | -48.06079 | 2025-09-28 00:50:00 | TERRA_M-M | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 8.5 |
| fdbf0af4-3f7c-3d76-b55e-1242dfeec17b | -15.55359 | -47.89659 | 2025-09-28 00:50:00 | TERRA_M-M | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 9355a478-eb4b-3e80-8a25-0668977cd0d9 | -13.63532 | -44.43344 | 2025-09-28 00:50:00 | TERRA_M-M | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 33.0 |
| 02a54c8c-6e53-317a-aafa-5c0c629332d5 | -16.96245 | -53.70507 | 2025-09-28 00:50:00 | TERRA_M-M | ALTO GARÇAS | MATO GROSSO | Brasil | 5100409 | 51 | 33 | nan | nan | nan | Cerrado | 77.6 |
| 325f95b0-5403-3c75-aaef-726e81213e80 | -14.78517 | -45.63363 | 2025-09-28 00:50:00 | TERRA_M-M | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 45.6 |
| 17174fca-5330-3f4f-ac08-7f2efe7c13f1 | -22.87222 | -47.18635 | 2025-09-28 00:50:00 | TERRA_M-M | HORTOLÂNDIA | SÃO PAULO | Brasil | 3519071 | 35 | 33 | nan | nan | nan | Mata Atlântica | 11.4 |
| 816c234d-ec48-3930-ab99-1bdcdce2764e | -14.20267 | -44.60761 | 2025-09-28 00:50:00 | TERRA_M-M | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 22.9 |
| d5ac4437-bd7c-3edc-a2c8-63eaa150d505 | -17.72764 | -46.70481 | 2025-09-28 00:50:00 | TERRA_M-M | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 88.7 |
| 25af136d-414b-368e-a82d-b2d90de2ec3d | -15.53461 | -47.91335 | 2025-09-28 00:50:00 | TERRA_M-M | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 45.9 |
| cc912939-3778-357a-af0c-761a356f69b6 | -13.63769 | -44.42657 | 2025-09-28 00:50:00 | TERRA_M-M | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 58.6 |
| da9c5378-42dc-3536-8abd-1b91c3b971e5 | -15.33523 | -47.89048 | 2025-09-28 00:50:00 | TERRA_M-M | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 7.7 |
| ea872cbe-421f-3fc4-a60e-9c98506ba6b1 | -14.77571 | -45.65577 | 2025-09-28 00:50:00 | TERRA_M-M | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 83.8 |
| 5786cb61-96be-3fe2-b44c-aa24545e91fd | -15.4457 | -48.24876 | 2025-09-28 00:50:00 | TERRA_M-M | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 39815006-9d9a-3a0b-a67a-325564a881ab | -15.92728 | -57.5061 | 2025-09-28 00:50:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 12.7 |
| efb0e9c9-7768-3693-84e1-de03332c8b28 | -17.71911 | -46.72184 | 2025-09-28 00:50:00 | TERRA_M-M | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 26.8 |
| 9a5577da-3785-32fd-8d8a-7650db457691 | -18.20059 | -53.33018 | 2025-09-28 00:50:00 | TERRA_M-M | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 27.6 |
| 70e11d28-2b2a-313c-9c4b-ff15b9e7ec0c | -15.31839 | -47.88596 | 2025-09-28 00:50:00 | TERRA_M-M | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 76148f61-2c62-3e66-958e-253d463246fc | -11.00193 | -57.05865 | 2025-09-28 00:52:00 | TERRA_M-M | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 42.9 |
| 929a4b8d-e6b9-3307-919a-ca2cd2228b81 | -10.53377 | -43.61798 | 2025-09-28 00:52:00 | TERRA_M-M | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 40.3 |
| 5e1c5d17-e749-3b0b-903a-4793dda9d940 | -10.96014 | -54.09994 | 2025-09-28 00:52:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 11.9 |
| c3be08aa-9772-301e-bd4e-4231c84ecb8d | -12.64465 | -51.69181 | 2025-09-28 00:52:00 | TERRA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 6.5 |
| b5246c75-1aa5-3806-9a15-33f1ed131384 | -10.17461 | -49.36917 | 2025-09-28 00:52:00 | TERRA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 14.9 |
| 8d2e4a5b-effb-321b-929b-31342e058068 | -10.99141 | -57.0601 | 2025-09-28 00:52:00 | TERRA_M-M | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 40.6 |
| 1ebb0e46-6328-34fc-9ac3-c893e3fedbf8 | -13.5881 | -47.29819 | 2025-09-28 00:52:00 | TERRA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 12.7 |
| ec5ae558-a63e-3d0d-90c5-eaa9a64c3355 | -6.44036 | -43.94026 | 2025-09-28 00:52:00 | TERRA_M-M | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 79.9 |
| 18804b1d-9d46-3f60-ba39-ff1d2fdbcbec | -11.99839 | -47.88324 | 2025-09-28 00:52:00 | TERRA_M-M | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 19.3 |
| 5750a523-350e-39a0-8528-1ce910bbc505 | -10.99494 | -57.05214 | 2025-09-28 00:52:00 | TERRA_M-M | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 53b559ab-302d-31f6-90a6-9682344b1b9f | -6.76078 | -44.60493 | 2025-09-28 00:52:00 | TERRA_M-M | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 27.9 |
| 198ea6cd-2a20-3b44-b74f-174a53f58cdf | -8.48344 | -47.82178 | 2025-09-28 00:52:00 | TERRA_M-M | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 32.3 |
| fa2c1c01-6ec3-31cf-962a-b7bb4c363b53 | -7.78954 | -47.01715 | 2025-09-28 00:52:00 | TERRA_M-M | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 75.4 |
| ab486883-6ace-3213-88ea-719882d21fa9 | -10.97953 | -44.31239 | 2025-09-28 00:52:00 | TERRA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 50.4 |
| 8db41825-8806-331c-815a-2e8bf7bf9019 | -7.77971 | -47.04001 | 2025-09-28 00:52:00 | TERRA_M-M | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 40.3 |
| 4e60cec6-f0e3-3bc3-ab82-dd799980ae60 | -7.73982 | -47.03054 | 2025-09-28 00:52:00 | TERRA_M-M | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 22.3 |
| 4a833fec-20c1-3900-a9ec-cc7caf2d89e3 | -8.49676 | -44.73373 | 2025-09-28 00:52:00 | TERRA_M-M | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 29.2 |
| 62849bd6-0a43-3756-848b-57f6d1f4d681 | -7.8587 | -44.55588 | 2025-09-28 00:52:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 23.2 |
| 41c5f132-b794-3ca2-b8c8-7243ae71638d | -12.94023 | -45.13617 | 2025-09-28 00:52:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 16.8 |
| 1e69d451-8772-3660-a838-025242b28bd9 | -10.9091 | -45.73444 | 2025-09-28 00:52:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 20.2 |
| da96f062-5e5d-3c83-8b37-4a2c211177fa | -8.48841 | -47.80947 | 2025-09-28 00:52:00 | TERRA_M-M | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 60.9 |
| 21aeb2ac-146f-3709-8276-28ce892349a4 | -12.98336 | -46.83861 | 2025-09-28 00:52:00 | TERRA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 39.8 |
| 0a9055fe-205d-3a21-942e-e4f625ff4e81 | -9.65412 | -62.86231 | 2025-09-28 00:52:00 | TERRA_M-M | RIO CRESPO | RONDÔNIA | Brasil | 1100262 | 11 | 33 | nan | nan | nan | Amazônia | 134.4 |
| 44c1b9a3-a8a4-3c7c-88f9-852011a441dc | -10.83087 | -47.6362 | 2025-09-28 00:52:00 | TERRA_M-M | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 83a0cdfb-9887-3b11-9149-681d2f479105 | -9.06624 | -45.51481 | 2025-09-28 00:52:00 | TERRA_M-M | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 78.9 |
| 8b8bd0d2-7114-39aa-839a-4604e9705a37 | -12.68766 | -46.87368 | 2025-09-28 00:52:00 | TERRA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 46.4 |
| 9fa6184c-ccd9-3a30-ab5e-7d7df9600a89 | -13.60447 | -47.32666 | 2025-09-28 00:52:00 | TERRA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 22.7 |
| 5bd5a81d-7104-33a0-ab38-d57f526a7e55 | -11.98575 | -47.87582 | 2025-09-28 00:52:00 | TERRA_M-M | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 8452d757-47fc-3186-b560-c96bf1776ce4 | -7.80262 | -47.01515 | 2025-09-28 00:52:00 | TERRA_M-M | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 46.3 |
| e1219ccb-89d2-3344-8d34-327e338ecbd7 | -8.71781 | -47.98354 | 2025-09-28 00:52:00 | TERRA_M-M | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 48.2 |
| 88704102-8535-3308-b79a-8f451632e0b5 | -10.20549 | -58.21814 | 2025-09-28 00:52:00 | TERRA_M-M | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 10.7 |
| be74c6b9-4bb0-36b1-b1ed-f19333d3ea77 | -10.04595 | -49.1977 | 2025-09-28 00:52:00 | TERRA_M-M | MONTE SANTO DO TOCANTINS | TOCANTINS | Brasil | 1713700 | 17 | 33 | nan | nan | nan | Cerrado | 33.9 |
| d0629aee-4513-34cf-b536-5778327db970 | -11.00355 | -57.07178 | 2025-09-28 00:52:00 | TERRA_M-M | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 24.1 |
| 92fe6da9-8495-3e15-a321-531b13cbc962 | -12.64965 | -51.66273 | 2025-09-28 00:52:00 | TERRA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 13.2 |
| a0a67e79-653b-3688-8420-b3654f964345 | -12.0009 | -47.89869 | 2025-09-28 00:52:00 | TERRA_M-M | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 24.1 |
| 4201e3f3-2f05-3cba-a128-5210fd93b0f7 | -11.36491 | -44.95015 | 2025-09-28 00:52:00 | TERRA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 43.5 |
| a0165926-fc68-3303-9c36-aa915fd2c7b3 | -11.57209 | -46.92075 | 2025-09-28 00:52:00 | TERRA_M-M | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 18.0 |
| 053f4fc1-8ecc-354b-aaac-2db16a9fa394 | -13.39267 | -48.17141 | 2025-09-28 00:52:00 | TERRA_M-M | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 123ebb91-4219-38e1-865a-83060515dbdf | -11.97998 | -46.58985 | 2025-09-28 00:52:00 | TERRA_M-M | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 11.5 |
| c51a6d38-b0b6-37de-953f-c6c2a99e6155 | -9.07029 | -45.54056 | 2025-09-28 00:52:00 | TERRA_M-M | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 196.7 |
| 68326d97-5a70-3702-8949-3de7808869de | -12.64334 | -51.68259 | 2025-09-28 00:52:00 | TERRA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 84d65ca4-5929-343f-b97c-db79d589084a | -9.64292 | -62.83309 | 2025-09-28 00:52:00 | TERRA_M-M | RIO CRESPO | RONDÔNIA | Brasil | 1100262 | 11 | 33 | nan | nan | nan | Amazônia | 117.4 |
| e61311b9-8e12-3866-8abe-c598a838a23b | -10.7899 | -49.58239 | 2025-09-28 00:52:00 | TERRA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 1079c085-f108-3ff0-bc38-46627110b67a | -7.87454 | -44.55332 | 2025-09-28 00:52:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 25.0 |
| 612fed63-8731-3ded-8809-49bcda939abd | -7.80914 | -46.8992 | 2025-09-28 00:52:00 | TERRA_M-M | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 32.9 |
| 68d561bb-c859-3e51-8ba7-7586fee59833 | -11.65593 | -48.27312 | 2025-09-28 00:52:00 | TERRA_M-M | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 9764ad98-7a3b-3ec9-ad6c-7fdc0e56c6f2 | -9.44905 | -50.89927 | 2025-09-28 00:52:00 | TERRA_M-M | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 44aa979a-5e33-3992-992c-deeee4dcf863 | -12.65858 | -51.66138 | 2025-09-28 00:52:00 | TERRA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 12.7 |
| cbe4f64a-1e88-3bd6-94a9-c6625159549a | -9.41074 | -54.69412 | 2025-09-28 00:52:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| d0ddc30d-4c3b-3dc2-9e30-7c4c5f4dca07 | -9.5081 | -54.66478 | 2025-09-28 00:52:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| d6d31fe9-2422-37ca-940f-b7a94011fe2c | -12.01104 | -47.96488 | 2025-09-28 00:52:00 | TERRA_M-M | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 18.9 |
| ae02e1b5-5def-3473-929b-33323a4f0747 | -7.76014 | -47.00055 | 2025-09-28 00:52:00 | TERRA_M-M | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 44.9 |
| 51c69d4d-9d73-39bf-954c-fbf2fd827220 | -9.73515 | -49.11641 | 2025-09-28 00:52:00 | TERRA_M-M | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 15.7 |
| 08115441-7f3b-3949-bbbc-6ab3570c9630 | -12.95037 | -46.38782 | 2025-09-28 00:52:00 | TERRA_M-M | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 13.9 |
| 77d55179-44d2-3d4c-8603-2d46a4a106e7 | -7.74704 | -47.00262 | 2025-09-28 00:52:00 | TERRA_M-M | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 65.5 |
| 0904665d-26a8-3d45-bb8a-a2756640ee05 | -12.32404 | -51.5121 | 2025-09-28 00:52:00 | TERRA_M-M | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 57653deb-f6d3-39a7-88bf-c9cdf8667dcd | -13.59292 | -47.32776 | 2025-09-28 00:52:00 | TERRA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 27.5 |
| cd5c636f-92d2-31ed-9369-d023c3db04cd | -7.77646 | -47.01917 | 2025-09-28 00:52:00 | TERRA_M-M | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 171.1 |
| 718bc723-2b3d-3707-98b3-655fd7ee8bb5 | -13.40343 | -48.16975 | 2025-09-28 00:52:00 | TERRA_M-M | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 36.0 |
| 4c33107a-5ce4-3cc0-a8aa-3b9cc1c37e7a | -7.80964 | -46.98638 | 2025-09-28 00:52:00 | TERRA_M-M | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 22.3 |
| 86ae2971-bcd3-3ac6-9c6e-a4c47354679c | -7.87324 | -44.58179 | 2025-09-28 00:52:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 40.3 |
| cdbd0c0b-f85e-3e89-b183-f8b9bb5f1cc0 | -7.38522 | -47.04213 | 2025-09-28 00:52:00 | TERRA_M-M | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 11.4 |
| ecacb1ce-efcd-3e5e-a27b-11ee81871b7e | -5.86992 | -47.25483 | 2025-09-28 00:52:00 | TERRA_M-M | RIBAMAR FIQUENE | MARANHÃO | Brasil | 2109551 | 21 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 3ace4c9f-7940-3649-a54d-838e9ffbbfc0 | -11.98813 | -47.89116 | 2025-09-28 00:52:00 | TERRA_M-M | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 63.0 |
| 5e2263df-43ef-31c4-b884-84df4370558d | -12.63077 | -48.16156 | 2025-09-28 00:52:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 19.8 |
| 69b0c932-93d1-30cc-9d0f-c08438c0357f | -11.62735 | -52.85578 | 2025-09-28 00:52:00 | TERRA_M-M | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 14.9 |
| 84b5e9a8-b049-399a-99a1-daaa3a65d6d3 | -12.88943 | -47.09696 | 2025-09-28 00:52:00 | TERRA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 16.3 |
| 2ba4de02-e661-3179-ad93-1f8f0157ef4b | -7.79944 | -46.99446 | 2025-09-28 00:52:00 | TERRA_M-M | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 68.7 |
| cfb92dc9-1c39-3434-83ce-420e7800f221 | -11.3855 | -46.98492 | 2025-09-28 00:52:00 | TERRA_M-M | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 24.8 |
| 8895e66a-8e23-31fd-b457-ca645bcde31d | -11.99947 | -47.8899 | 2025-09-28 00:52:00 | TERRA_M-M | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 28.0 |
| e228e287-edef-342a-98a2-d4ba3039693d | -10.45638 | -50.84731 | 2025-09-28 00:52:00 | TERRA_M-M | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 5.0 |
| ffeec223-169e-3074-ba4e-a4c96103d98e | -11.62143 | -48.5022 | 2025-09-28 00:52:00 | TERRA_M-M | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 54e9af4e-fa74-3fff-a566-855e7b70ce61 | -9.07265 | -45.53365 | 2025-09-28 00:52:00 | TERRA_M-M | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 321.3 |
| 769db09b-ad74-3893-97bb-ed783e76b9d0 | -11.095 | -54.27608 | 2025-09-28 00:52:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 5.7 |
| c0d93b14-1416-3278-be2e-e052ee5c3737 | -7.86033 | -43.79453 | 2025-09-28 00:52:00 | TERRA_M-M | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Caatinga | 56.0 |
| 2ecd117b-2b4d-37af-873d-ee3febdcd5e6 | -13.62755 | -47.32438 | 2025-09-28 00:52:00 | TERRA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 139b7df9-a7d8-349c-a01c-0f23e7e93120 | -10.97364 | -49.57189 | 2025-09-28 00:52:00 | TERRA_M-M | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 8.9 |


[Clique aqui para ver as próximas entradas](README5.md)
