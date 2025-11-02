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

## Dados Diários - Página 19

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 56598d0c-c025-39f9-926f-0306d1d05bf3 | -2.83115 | -49.41224 | 2025-11-02 04:48:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f0291723-daa3-3e26-861e-1608896def71 | -3.32111 | -51.57298 | 2025-11-02 04:48:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 24f9634f-1bcc-30ed-878d-6de936911280 | -3.57276 | -50.2678 | 2025-11-02 04:48:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 61075d20-20ba-313a-8283-fc45e5e4d2d1 | -3.50298 | -50.47258 | 2025-11-02 04:48:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 27647497-061d-3d91-9a49-2d62aa17c443 | -3.02557 | -51.22621 | 2025-11-02 04:48:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 3c5ef1a5-c1bf-31a0-b594-2b9b32bdda49 | -4.64296 | -38.56995 | 2025-11-02 04:48:00 | NPP-375D | OCARA | CEARÁ | Brasil | 2309458 | 23 | 33 | nan | nan | nan | Caatinga | 2.8 |
| a8e63901-6470-30fe-abbf-d39ad226b03a | -3.58144 | -51.55891 | 2025-11-02 04:48:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f2e6c11b-2e3f-3a61-ace0-2a8b00094fdf | -3.08564 | -52.9229 | 2025-11-02 04:48:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 31263c6c-9ff3-3bbf-a258-6c80c5ad2784 | -4.14637 | -51.15166 | 2025-11-02 04:48:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 33055789-2710-3dde-830d-cb684ac05e78 | -3.01827 | -53.96546 | 2025-11-02 04:48:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ca70a302-da3b-3f91-96ce-1acd5e99b5d5 | -3.61951 | -50.14416 | 2025-11-02 04:48:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e101121e-1b98-3e5d-9293-b39d803c32e1 | -3.55853 | -54.57255 | 2025-11-02 04:48:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| d03141f3-8a87-3a3b-8fab-277c92a53c69 | -3.31932 | -52.56677 | 2025-11-02 04:48:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3a7a5e64-6972-3d16-83fe-6d2c5c9a479c | -3.45424 | -50.22381 | 2025-11-02 04:48:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 948b806e-d20e-3468-98d3-2290a19b1fdc | -3.07812 | -51.25223 | 2025-11-02 04:48:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d4651b09-2aab-3e31-a30e-4a34b2b5c355 | -3.47728 | -49.92626 | 2025-11-02 04:48:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 77d9d405-203e-338d-ad5c-91c2f0bdf5d5 | -3.82343 | -52.36391 | 2025-11-02 04:48:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1c8a718c-64b1-3c19-90ff-7191134f09b3 | -3.07923 | -51.2452 | 2025-11-02 04:48:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3cb24e90-fb10-31d5-bf84-3791d2070ea2 | -2.90369 | -53.95719 | 2025-11-02 04:48:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| bb141951-7336-3e19-af88-c7e8aae6ce4d | -4.37513 | -49.74506 | 2025-11-02 04:48:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 0ca60199-b412-3552-a96d-5ccb158c5593 | -4.13978 | -47.33157 | 2025-11-02 04:48:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 42ec4d29-d911-384b-a00d-f3ae37e47ba0 | -3.38638 | -49.96914 | 2025-11-02 04:48:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 38ce0889-3795-32c2-a0d5-4bc057374816 | -7.50911 | -42.45126 | 2025-11-02 04:48:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 26e4f759-25d5-3517-8804-4e27c827db5b | -2.79458 | -50.28655 | 2025-11-02 04:48:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 69e14542-079e-3ca1-9f2c-4d36581940fa | -4.13693 | -51.14661 | 2025-11-02 04:48:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| a9004a34-3bdb-3f34-8682-0a9f5b9aca68 | -5.78266 | -53.45065 | 2025-11-02 04:48:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| eb735a73-b74c-3d52-8eff-547e49f0ce82 | -3.01196 | -49.44364 | 2025-11-02 04:48:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| e08fe037-0f9b-3be7-8149-4e5290982b91 | -3.72488 | -45.55075 | 2025-11-02 04:48:00 | NPP-375D | TUFILÂNDIA | MARANHÃO | Brasil | 2112274 | 21 | 33 | nan | nan | nan | Amazônia | 23.7 |
| 5e833dd3-2403-3ac2-acbc-682a03a9e016 | -3.7091 | -53.37669 | 2025-11-02 04:48:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| de178f42-6e56-3e1a-9e82-36b6a19da57c | -2.66005 | -51.72992 | 2025-11-02 04:48:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| da5324f9-ae96-395e-85dc-7579adcea6cb | -1.49889 | -47.80569 | 2025-11-02 04:48:00 | NPP-375D | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3f85b731-59f0-3968-a5bd-796fed492b41 | -3.25461 | -52.9043 | 2025-11-02 04:48:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a22a8b99-1d21-3e86-a5a6-7e5e204c8fa0 | -3.56944 | -50.26728 | 2025-11-02 04:48:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b151313c-e2a9-3cf3-aedd-48b4216eae2c | -3.58381 | -50.26246 | 2025-11-02 04:48:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 735b0fb7-c8fe-3d48-87f5-f4cc25a5d32e | -0.40258 | -52.05397 | 2025-11-02 04:48:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ee5a26a3-bf88-36fc-959f-685c4d7dcfdd | -3.38142 | -49.97898 | 2025-11-02 04:48:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ddba7130-341e-3f5c-8f7b-188f89589967 | -3.87089 | -49.90274 | 2025-11-02 04:48:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 254d0843-6da9-3c02-8e30-a3bb0f45b02b | -4.57925 | -44.78712 | 2025-11-02 04:48:00 | NPP-375D | BERNARDO DO MEARIM | MARANHÃO | Brasil | 2101939 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| be795323-3cdb-38e0-8aad-07a3a846a67f | -4.70286 | -45.87849 | 2025-11-02 04:48:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c56f8a44-5bf7-36f4-b7a0-01bd1f166bff | -3.15561 | -50.82848 | 2025-11-02 04:48:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a263b074-7f01-30d1-91c6-5cccad30a2ca | -3.56451 | -51.64359 | 2025-11-02 04:48:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2546981e-02dc-3505-b9fc-fbfaf20738c1 | -3.56788 | -51.64413 | 2025-11-02 04:48:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 019960ca-e12f-3154-8dc3-0c8461cd0764 | -2.63725 | -51.9163 | 2025-11-02 04:48:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6f892f1f-f558-3151-ba30-f4cea0979adf | -3.54729 | -54.6923 | 2025-11-02 04:48:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b1439364-a1b6-3291-bcdd-e35d98d35f0d | -3.42772 | -50.24088 | 2025-11-02 04:48:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 57fc33b7-db31-3f62-8eea-caeb93ed837d | -3.4581 | -50.22087 | 2025-11-02 04:48:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| f6276407-3ce6-3dca-8d5f-13e93a532684 | -4.80892 | -45.69798 | 2025-11-02 04:48:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 1868846b-1783-3d7c-98ce-ae88bc67c357 | -3.70048 | -51.23142 | 2025-11-02 04:48:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| dc444948-241a-3fab-a55a-f17b0c6c3c38 | -2.49123 | -48.15045 | 2025-11-02 04:48:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e65ebb52-0ba0-3255-971e-b781a68118a8 | -3.06461 | -45.45121 | 2025-11-02 04:48:00 | NPP-375D | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 371f35b5-cf36-3f92-bf28-3459261e240d | -3.32278 | -52.56734 | 2025-11-02 04:48:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ad37b7ba-e5bb-3a19-86c0-ff1384e4684f | -4.1362 | -48.8145 | 2025-11-02 04:48:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 95bd0d52-fa5d-35be-8b1a-3bcbc57ec615 | -3.37841 | -51.06971 | 2025-11-02 04:48:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9338b1c6-53b7-30c2-9e1e-9d5a97c3d2e5 | -3.9499 | -50.00032 | 2025-11-02 04:48:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4798396b-21f1-30c5-bed4-5975f53dadfc | -3.81389 | -51.69767 | 2025-11-02 04:48:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3e7049f4-6532-3788-bd25-26217923f2ae | -3.56998 | -50.26383 | 2025-11-02 04:48:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8e85973a-ebde-3af6-8aef-17b0e0dd28d8 | -3.63558 | -49.89118 | 2025-11-02 04:48:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 70b6a0ca-dfe4-3512-b904-f13cfa9a4e7c | -2.37512 | -47.71665 | 2025-11-02 04:48:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 52d70567-128b-33b7-9366-99fbb7a53e11 | -5.03042 | -43.61921 | 2025-11-02 04:48:00 | NPP-375D | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 28500da1-192b-3af9-ae3a-e8017fe5823c | -2.3115 | -48.58585 | 2025-11-02 04:48:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 577f5e16-b5d9-38c2-8059-e55234152c0d | -3.03643 | -50.34199 | 2025-11-02 04:48:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6c4fa2bb-9ff8-35e3-9f7b-18b75cc77833 | -3.73582 | -51.71091 | 2025-11-02 04:48:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3ec1078a-4b55-3986-b247-4cb2af518382 | -4.05598 | -46.75246 | 2025-11-02 04:48:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 7ffb48c6-1121-3085-bb67-623ec3834a19 | -3.63225 | -49.89066 | 2025-11-02 04:48:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fbf288b8-a495-3364-9fab-177d10c836ff | -6.79643 | -42.20504 | 2025-11-02 04:48:00 | NPP-375D | SANTA ROSA DO PIAUÍ | PIAUÍ | Brasil | 2209377 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| cd642a12-9559-3aea-aefa-1838937fe6ba | -3.35181 | -51.68368 | 2025-11-02 04:48:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 21f4f345-2304-30cd-8e50-e61422052c62 | -3.41526 | -50.00201 | 2025-11-02 04:48:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b3f9fcb0-4072-3e04-a8d6-f3fc6fdd6682 | -3.91395 | -50.03375 | 2025-11-02 04:48:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d80e9f75-d5cc-327f-8d54-1d4b7478ffd9 | -3.08202 | -51.24924 | 2025-11-02 04:48:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f0245ce5-632e-3ead-b756-dc4b125a3cb9 | -3.06421 | -49.37275 | 2025-11-02 04:48:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 98497fca-93dc-3b2a-ba67-52943580bfe2 | -5.78459 | -40.81016 | 2025-11-02 04:48:00 | NPP-375D | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| d3e4f050-815a-302b-898a-7b04d69c049b | -3.08629 | -52.91896 | 2025-11-02 04:48:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2d4f953f-469b-3ab4-b195-f0d2f02326e5 | -3.50355 | -52.94973 | 2025-11-02 04:48:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b85817e6-e68d-302b-88a7-7332157cd4c2 | -0.84747 | -48.61758 | 2025-11-02 04:48:00 | NPP-375D | SALVATERRA | PARÁ | Brasil | 1506302 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 8ed7e936-1f91-3833-aa8f-e9a39cd10c85 | -3.89347 | -52.20865 | 2025-11-02 04:48:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| e56de7bb-a760-38a7-8058-94bfa31ef199 | -3.57237 | -54.58434 | 2025-11-02 04:48:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ad94bb99-d12b-398a-872d-ff71624935e6 | -5.31372 | -44.41738 | 2025-11-02 04:48:00 | NPP-375D | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| c40665d1-0a22-3237-b344-fa53c8c58497 | -2.31489 | -48.58638 | 2025-11-02 04:48:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 169fe9cd-905d-3132-9bf6-4658ee9864a9 | -3.14467 | -49.4174 | 2025-11-02 04:48:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 08a31d75-ff31-34b6-8fb4-53f9595a62b9 | -5.12696 | -45.81567 | 2025-11-02 04:48:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4da73507-ec22-3a4b-bd86-f091828497f1 | -4.27019 | -48.71847 | 2025-11-02 04:48:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 138640df-1327-34aa-89c8-74cd742e668f | -3.82288 | -51.69139 | 2025-11-02 04:48:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0d6f4e79-ea78-3e2c-a61a-995a6b08c9e3 | -3.28493 | -51.61778 | 2025-11-02 04:48:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6fce7c2a-1887-398e-8341-b70a7a998230 | -3.66822 | -51.71436 | 2025-11-02 04:48:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c85d191d-d93d-39f0-9df1-d09121c29e3e | -6.80168 | -42.20608 | 2025-11-02 04:48:00 | NPP-375D | SANTA ROSA DO PIAUÍ | PIAUÍ | Brasil | 2209377 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| b07c0f82-ce5d-39b1-a2d9-9d930bc7d999 | -5.52187 | -41.10471 | 2025-11-02 04:48:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 67b3725e-ae33-3ea0-88a7-04579a052209 | -3.02222 | -51.22568 | 2025-11-02 04:48:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 17350778-ae71-3189-a5e7-26094296bd40 | -3.54985 | -50.17576 | 2025-11-02 04:48:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 04d60ccb-b302-30cd-9e74-2072a12954da | -14.0356 | -43.4666 | 2025-11-02 04:50:00 | GOES-19 | PALMAS DE MONTE ALTO | BAHIA | Brasil | 2923407 | 29 | 33 | nan | nan | nan | Cerrado | 83.9 |
| dcf1bd64-a978-338c-8f6a-2bdd245c9313 | -4.1361 | -51.152 | 2025-11-02 04:50:00 | GOES-19 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 58.8 |
| 4b461109-3189-3af1-9835-8acaf0f1446d | -13.98407 | -51.50534 | 2025-11-02 04:50:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 4.8 |
| ab56942b-9cc2-3c53-95b1-221bc1b0c739 | -8.15841 | -44.48566 | 2025-11-02 04:50:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 765557a3-a355-34c7-b253-6ea36ba5849a | -13.61197 | -48.26918 | 2025-11-02 04:50:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 69537e46-87e3-3964-a289-4e2846eea8d8 | -10.6292 | -52.18316 | 2025-11-02 04:50:00 | NPP-375D | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 984f0d94-5897-3896-b4ef-57aef4a2c675 | -10.61923 | -52.18154 | 2025-11-02 04:50:00 | NPP-375D | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9e1a24ed-2f88-3554-aac0-79791a7e995b | -12.87805 | -50.89097 | 2025-11-02 04:50:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 16f6f4f3-e54e-34be-b72e-f3a08b40ae03 | -10.80271 | -54.91068 | 2025-11-02 04:50:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 7bc7a6a7-a363-39db-a5ff-9e21f906f0dd | -13.58605 | -51.02965 | 2025-11-02 04:50:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 166bec1d-3ba1-3c43-ab83-e288987f6599 | -11.56817 | -47.07492 | 2025-11-02 04:50:00 | NPP-375D | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 305f464b-16ed-357c-8b05-cb4eacce0525 | -11.56716 | -47.08226 | 2025-11-02 04:50:00 | NPP-375D | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |


[Clique aqui para ver as próximas entradas](README20.md)
