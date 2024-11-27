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

## Dados Diários - Página 21

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 949b594b-b9e8-3ad1-acc4-138edf7b9e0d | -2.1744 | -53.7842 | 2024-11-27 02:30:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 52.4 |
| e654a986-f035-36a9-b6a0-584ddbe47b61 | -2.8347 | -54.1125 | 2024-11-27 02:30:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 68.4 |
| 4d98e67c-bd4c-351a-a4fd-3b5b22aabdbd | -3.5226 | -52.1448 | 2024-11-27 02:30:00 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 70.6 |
| 4e8a3d26-34f7-37cc-b1de-a65af7aa1737 | -3.1876 | -48.4387 | 2024-11-27 02:30:00 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 108.8 |
| af790e0c-1303-3893-ae70-d17de4dfa36e | -2.8346 | -54.1326 | 2024-11-27 02:30:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 62.8 |
| a2252748-8a9b-334b-9656-380d907f725d | -1.6813 | -52.4333 | 2024-11-27 02:30:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 44.1 |
| 65dd5493-e959-34ad-9973-5348d688ae90 | -3.5226 | -52.1653 | 2024-11-27 02:30:00 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 49.8 |
| 5e5226dc-3a31-3e82-ba79-b363b5cc2038 | -3.1132 | -53.2786 | 2024-11-27 02:30:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 65.0 |
| ce6d14cc-7a39-3442-a7d4-b6f1b2a7d357 | -3.0949 | -53.2385 | 2024-11-27 02:30:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 112.9 |
| 7743e03c-6fe7-3bc4-92d9-f94375313398 | -3.0393 | -48.5082 | 2024-11-27 02:30:00 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 60.5 |
| 53ebb849-4f35-3089-8dea-83816ee4c14c | -5.9975 | -45.3607 | 2024-11-27 02:30:00 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 50.5 |
| 6e94979d-479c-33bc-8be6-5da07d7fe5e3 | -3.1692 | -48.4179 | 2024-11-27 02:40:00 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 56.7 |
| 8a337f83-c8df-36c7-a314-9e62f4b8c6a7 | -3.0949 | -53.2588 | 2024-11-27 02:40:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 159.6 |
| 2dec2002-eb4a-37b7-ac8d-1d22054d6f39 | -4.23 | -50.8774 | 2024-11-27 02:40:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 50.2 |
| bc278772-9621-3136-9805-d3bd80c144b7 | -3.1133 | -53.2381 | 2024-11-27 02:40:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 58.0 |
| a621d4dd-51ed-35e4-97bc-ea73c2129771 | -4.1419 | -43.7905 | 2024-11-27 02:40:00 | GOES-16 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 52.8 |
| 03ff1f9e-e09a-3b78-9035-7ebf3120e53c | -2.8346 | -54.1326 | 2024-11-27 02:40:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 63.7 |
| 934257da-7287-3e30-9b0b-3f532b792877 | -4.2299 | -50.8983 | 2024-11-27 02:40:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 58.1 |
| 89cd1530-6f72-354d-a8db-55e6d4fb2707 | -3.9674 | -48.0851 | 2024-11-27 02:40:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 43.4 |
| f7c1debf-1032-320c-948a-66f5e25b1213 | -2.8347 | -54.1125 | 2024-11-27 02:40:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 79.9 |
| e173d047-fc87-3102-a67a-abf008f95af7 | -5.9788 | -45.3621 | 2024-11-27 02:40:00 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 53.4 |
| ded03d4b-0d1e-3aef-8845-c61ff46d3161 | -3.0578 | -48.5076 | 2024-11-27 02:40:00 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 42.3 |
| d2aef179-0407-32e1-8a0f-8fb67f04e372 | -3.5411 | -52.1442 | 2024-11-27 02:40:00 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 47.1 |
| 8acea1c0-8bc6-3d9e-9cef-8008d10fbaeb | -3.0949 | -53.2385 | 2024-11-27 02:40:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 70.3 |
| 76a8351e-9fab-3476-85b9-259ea0d27e1a | -3.1133 | -53.2583 | 2024-11-27 02:40:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 140.7 |
| 20b46878-bf31-32af-8f27-0d31dc40628e | -5.9975 | -45.3607 | 2024-11-27 02:40:00 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 55.7 |
| 44e8c99d-3dce-3fa6-aa5e-07502d20294f | -4.1417 | -43.8135 | 2024-11-27 02:40:00 | GOES-16 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 73.2 |
| 450c05fb-918b-3103-a80c-e6d376e9b5eb | -3.1691 | -48.4394 | 2024-11-27 02:40:00 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 188.8 |
| af2492ba-597a-3e0e-93d1-2a951fd987fd | -3.0393 | -48.5082 | 2024-11-27 02:40:00 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 62.6 |
| 4df71ac7-057c-3f54-add5-04088212ea49 | -4.2114 | -50.899 | 2024-11-27 02:40:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 67.3 |
| 2177f684-55fc-3564-a443-1d1babd7f436 | -3.1876 | -48.4387 | 2024-11-27 02:40:00 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 91.0 |
| 8c9a7e17-82a7-3f53-8a2b-20c0a3409430 | -2.1928 | -53.7839 | 2024-11-27 02:40:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 53.8 |
| 8c6f14e2-41c2-3e83-87e0-ff2efef9cb90 | -2.9428 | -54.7904 | 2024-11-27 02:40:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 69.8 |
| 113e5722-3fcb-3016-998c-4396a1c5c124 | -5.9788 | -45.3621 | 2024-11-27 02:50:00 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 74.4 |
| 36415e5e-d7e6-34e3-8f00-b43bded9e796 | -4.2115 | -50.8782 | 2024-11-27 02:50:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 53.6 |
| c744a2b6-6059-3149-8d1a-917b6279fd93 | -3.1876 | -48.4387 | 2024-11-27 02:50:00 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 108.4 |
| 7138cd6a-cdf4-3ff6-a227-a75a0ea7ecad | -3.0578 | -48.5076 | 2024-11-27 02:50:00 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 51.1 |
| 935bc856-4842-3e51-91e6-a12ec0059f06 | -3.5226 | -52.1653 | 2024-11-27 02:50:00 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 49.5 |
| 690f75f1-7b62-39ae-a5e8-c4372342c44c | -3.5226 | -52.1448 | 2024-11-27 02:50:00 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 55.5 |
| 077242f5-54c9-301d-9f23-cd3ff6aab048 | -3.9674 | -48.0851 | 2024-11-27 02:50:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 31.3 |
| 59d4b6b5-d8c3-3110-8ebb-eea86dc7e1c8 | -5.9975 | -45.3607 | 2024-11-27 02:50:00 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 53.9 |
| b8dfd199-6d9f-35b0-8e27-866814cc6051 | -4.2114 | -50.899 | 2024-11-27 02:50:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 86.4 |
| c54b2763-422f-301c-ab2f-a46c0b3f85e3 | -3.1132 | -53.2786 | 2024-11-27 02:50:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 57.6 |
| 730c9cce-de48-3219-81c3-aa2c94d24e51 | -3.0949 | -53.2385 | 2024-11-27 02:50:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 101.3 |
| 47098619-a63e-3271-ae33-c34a08e122a9 | -2.9428 | -54.7904 | 2024-11-27 02:50:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 57.8 |
| 8531f133-0071-351e-91a9-573d7195120c | -3.0949 | -53.2588 | 2024-11-27 02:50:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 241.7 |
| b00fe73d-e2c3-3cd6-b54c-569b21237cf9 | -2.1744 | -53.7842 | 2024-11-27 02:50:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 53.6 |
| 90789089-da0c-3229-8168-72fc20392125 | -3.1691 | -48.4394 | 2024-11-27 02:50:00 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 162.6 |
| 12e952df-24c3-3f8c-b51d-9d2a3c9a1b18 | -1.9546 | -46.2479 | 2024-11-27 02:50:00 | GOES-16 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 55.8 |
| ea33579d-8764-3b18-9be0-1321115dd078 | -3.0948 | -53.2791 | 2024-11-27 02:50:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 67.1 |
| 798afe69-316e-36c3-af9f-ec66c2279783 | -1.9546 | -46.2701 | 2024-11-27 02:50:00 | GOES-16 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 77.2 |
| 489a1ecf-2b3f-3a5f-ae0a-98633148fc67 | -1.791 | -52.7376 | 2024-11-27 02:50:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 20.9 |
| dddf1593-20c8-325b-82c7-8751f3ff4e16 | -3.1133 | -53.2381 | 2024-11-27 02:50:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 66.7 |
| 92e4381f-93ae-37d2-ad8a-20ee9882fda1 | -3.1692 | -48.4179 | 2024-11-27 02:50:00 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 52.3 |
| 171fb9df-c620-3871-8abe-b857a4ede552 | -3.0393 | -48.5082 | 2024-11-27 02:50:00 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 46.0 |
| a51b7cd1-0993-36ae-863d-ee6bda326723 | -3.1133 | -53.2583 | 2024-11-27 02:50:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 207.6 |
| 210c2295-bfb9-3871-86d2-6a60ce10c799 | -3.1133 | -53.2583 | 2024-11-27 03:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 151.1 |
| 0d8135f3-f151-3693-9c36-4913dfffdb82 | -3.0393 | -48.5082 | 2024-11-27 03:00:00 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 58.7 |
| a3a5696c-abfe-3eef-aaab-1994a83015bd | -2.1928 | -53.7839 | 2024-11-27 03:00:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 58.7 |
| 6d45651e-6ca3-3b0c-8f34-8018c4ba5d17 | -4.23 | -50.8774 | 2024-11-27 03:00:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 54.4 |
| 41a14480-1c51-31d3-b7c3-385f02c8e311 | -3.0949 | -53.2588 | 2024-11-27 03:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 143.0 |
| b5f1cd27-18aa-36ad-8210-bdea8554fbb1 | -4.2299 | -50.8983 | 2024-11-27 03:00:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 62.4 |
| bb141e10-c484-3ced-8d12-0dd5e6d7ed2b | -3.9674 | -48.0851 | 2024-11-27 03:00:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 26.0 |
| 62c8ce34-6d42-3585-a13b-759787b6429c | -3.1876 | -48.4387 | 2024-11-27 03:00:00 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 82.1 |
| 1654e68b-0ce1-33b4-9eca-ed41e63328c6 | -2.8346 | -54.1326 | 2024-11-27 03:00:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 64.5 |
| 5d6c6d12-0bfe-38d1-872d-e72bb6f8da99 | -3.1692 | -48.4179 | 2024-11-27 03:00:00 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 59.2 |
| 82bb0131-0be7-31f4-83f4-3e82800cd9a2 | -4.1417 | -43.8135 | 2024-11-27 03:00:00 | GOES-16 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 60.9 |
| 69856fac-dadc-3008-b9a0-89c408e845cf | -3.1691 | -48.4394 | 2024-11-27 03:00:00 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 178.1 |
| de87fc3c-2534-3579-ade0-638106112513 | -3.0949 | -53.2385 | 2024-11-27 03:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 57.8 |
| 250b1f2c-fa5a-30d8-b66c-efe2777f3292 | -5.9788 | -45.3621 | 2024-11-27 03:00:00 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 65.0 |
| e32a07c2-501b-3f8b-b11b-5319413c66ef | -5.9975 | -45.3607 | 2024-11-27 03:00:00 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 69.9 |
| a5d29994-1efd-317b-8157-849dff8801e0 | -3.1133 | -53.2381 | 2024-11-27 03:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 52.7 |
| c5addac0-8c9b-3bf7-8057-5e5da48f3a1f | -2.9428 | -54.7904 | 2024-11-27 03:00:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 68.6 |
| 472dfdbf-15bf-3953-b201-420b06abd661 | -4.2114 | -50.899 | 2024-11-27 03:00:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 75.0 |
| 5f6b4a49-4434-3cf7-8d81-78f3244ba071 | -2.8347 | -54.1125 | 2024-11-27 03:00:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 78.2 |
| e955c1de-a93b-31af-a543-8f24bd244be4 | -6.84553 | -35.32454 | 2024-11-27 03:02:00 | NOAA-20 | ARAÇAGI | PARAÍBA | Brasil | 2500809 | 25 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 751a1bdf-5452-3f4a-bb32-0ed47e949c68 | -7.07139 | -35.26855 | 2024-11-27 03:02:00 | NOAA-20 | MARI | PARAÍBA | Brasil | 2509107 | 25 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 0e616e22-5d66-3db1-bbac-2785a90d57b2 | -5.36788 | -35.61802 | 2024-11-27 03:02:00 | NOAA-20 | PUREZA | RIO GRANDE DO NORTE | Brasil | 2410405 | 24 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 87e14773-8453-3fa5-8600-d63a7b514a81 | -7.73029 | -35.15979 | 2024-11-27 03:02:00 | NOAA-20 | TRACUNHAÉM | PERNAMBUCO | Brasil | 2615508 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| e459fa1e-46ce-3920-b1a5-d1acbe6fb279 | -6.86951 | -36.81522 | 2024-11-27 03:02:00 | NOAA-20 | SÃO JOSÉ DO SABUGI | PARAÍBA | Brasil | 2514701 | 25 | 33 | nan | nan | nan | Caatinga | 0.3 |
| 8579264c-0f04-3768-833a-5c9fec3e8c22 | -8.54107 | -35.1772 | 2024-11-27 03:02:00 | NOAA-20 | SIRINHAÉM | PERNAMBUCO | Brasil | 2614204 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 53246cea-fe8c-3ac2-8aeb-88983bb1fe1c | -5.14375 | -37.75056 | 2024-11-27 03:02:00 | NOAA-20 | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 1.2 |
| efdb69e6-a9c6-3a94-8202-124ec9ce540a | -8.95485 | -36.77457 | 2024-11-27 03:02:00 | NOAA-20 | SALOÁ | PERNAMBUCO | Brasil | 2612307 | 26 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 6ff9b17a-ef76-3e45-ab8e-07df09546047 | -8.95401 | -36.77898 | 2024-11-27 03:02:00 | NOAA-20 | SALOÁ | PERNAMBUCO | Brasil | 2612307 | 26 | 33 | nan | nan | nan | Caatinga | 1.0 |
| faf2fd3b-7051-3deb-b5b5-79d5aa5a30a0 | -8.54048 | -35.18048 | 2024-11-27 03:02:00 | NOAA-20 | SIRINHAÉM | PERNAMBUCO | Brasil | 2614204 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 294462c8-94cd-3d32-bc9b-6ca1b2ffe0fc | -5.36318 | -35.6192 | 2024-11-27 03:02:00 | NOAA-20 | PUREZA | RIO GRANDE DO NORTE | Brasil | 2410405 | 24 | 33 | nan | nan | nan | Caatinga | 2.9 |
| aca4ce7a-0184-3147-914a-ee078f437df8 | -6.84616 | -35.32104 | 2024-11-27 03:02:00 | NOAA-20 | ARAÇAGI | PARAÍBA | Brasil | 2500809 | 25 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 39d8997d-fa2c-3f6f-b80e-3bd02029ee47 | -7.72494 | -35.15887 | 2024-11-27 03:02:00 | NOAA-20 | TRACUNHAÉM | PERNAMBUCO | Brasil | 2615508 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 91504d50-09c8-32a9-9316-f8b189a2cff2 | -5.36148 | -35.62096 | 2024-11-27 03:02:00 | NOAA-20 | PUREZA | RIO GRANDE DO NORTE | Brasil | 2410405 | 24 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 5b7ab810-b595-30cf-bfda-4785fa202633 | -8.99813 | -36.00345 | 2024-11-27 03:02:00 | NOAA-20 | SÃO JOSÉ DA LAJE | ALAGOAS | Brasil | 2708303 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| fb206389-fc4f-3b61-a08c-82b58f401464 | -5.36961 | -35.61628 | 2024-11-27 03:02:00 | NOAA-20 | PUREZA | RIO GRANDE DO NORTE | Brasil | 2410405 | 24 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 1c9d2288-c23a-3586-8591-d663e88d95a8 | -5.36216 | -35.61702 | 2024-11-27 03:02:00 | NOAA-20 | PUREZA | RIO GRANDE DO NORTE | Brasil | 2410405 | 24 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 7ab27c8f-09e9-3e56-b06e-2571f07b5d3f | -5.14476 | -37.745 | 2024-11-27 03:02:00 | NOAA-20 | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 352da916-3b1b-32e0-b370-dccc770dcb24 | -6.87553 | -36.81636 | 2024-11-27 03:02:00 | NOAA-20 | SÃO JOSÉ DO SABUGI | PARAÍBA | Brasil | 2514701 | 25 | 33 | nan | nan | nan | Caatinga | 0.3 |
| a73b9249-5d0f-38c7-93c5-9d2abc2f2245 | -9.85838 | -36.23565 | 2024-11-27 03:04:00 | NOAA-20 | CAMPO ALEGRE | ALAGOAS | Brasil | 2701407 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| f33990f4-5514-3b2e-bbc9-ccb225916dad | -10.02134 | -36.18427 | 2024-11-27 03:04:00 | NOAA-20 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 86269195-a591-365f-85d7-408bfc4b05f4 | -9.85123 | -36.00204 | 2024-11-27 03:04:00 | NOAA-20 | ROTEIRO | ALAGOAS | Brasil | 2707800 | 27 | 33 | nan | nan | nan | Mata Atlântica | 8.5 |
| 89a309e2-2c95-3d57-a314-ee7628f6504d | -9.85056 | -36.00558 | 2024-11-27 03:04:00 | NOAA-20 | ROTEIRO | ALAGOAS | Brasil | 2707800 | 27 | 33 | nan | nan | nan | Mata Atlântica | 8.5 |
| 69f55e16-a36b-3e22-b47b-3c807b27bb70 | -9.8639 | -36.23674 | 2024-11-27 03:04:00 | NOAA-20 | CAMPO ALEGRE | ALAGOAS | Brasil | 2701407 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| cb647d3c-db0d-3cc8-bea8-9c9b9f13e538 | -9.86458 | -36.23307 | 2024-11-27 03:04:00 | NOAA-20 | JEQUIÁ DA PRAIA | ALAGOAS | Brasil | 2703759 | 27 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |


[Clique aqui para ver as próximas entradas](README22.md)
