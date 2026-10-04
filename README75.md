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

## Dados Diários - Página 75

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a7b5cebb-7406-3428-8673-9a91eef74e8f | 3.6753 | -60.9632 | 2026-10-04 14:30:00 | GOES-19 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 77.3 |
| 144ace78-4404-3db5-9fa0-c798fecd2334 | -10.8377 | -57.1979 | 2026-10-04 14:30:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 55.2 |
| 3002048a-8cdb-37cb-ab2b-c5a756523087 | 3.6966 | -59.9173 | 2026-10-04 14:30:00 | GOES-19 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 68.8 |
| 42150b35-4562-3310-9f73-2e9abae9615c | 4.1697 | -60.7443 | 2026-10-04 14:30:00 | GOES-19 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 77.8 |
| 00a9dd37-a250-31c1-a177-a91e60860257 | -10.5318 | -57.7549 | 2026-10-04 14:30:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 58.6 |
| f9957a9c-157a-312e-a6ea-f2854e7958a6 | 4.0432 | -60.2528 | 2026-10-04 14:30:00 | GOES-19 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 62.9 |
| 018f8feb-92ea-3dc8-bd69-e9fb5fb4c8db | -1.3927 | -49.2727 | 2026-10-04 14:30:00 | GOES-19 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 72.8 |
| 3cad071b-1551-3290-8b8a-a8e8871b9d8d | 3.7701 | -59.8011 | 2026-10-04 14:30:00 | GOES-19 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 64.1 |
| 54221c62-56b0-3340-ad6e-c4208d5a5004 | -9.4751 | -64.3336 | 2026-10-04 14:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 56.5 |
| c9b34225-251a-3b41-a4be-4dd242b03bb0 | 3.8215 | -60.9792 | 2026-10-04 14:30:00 | GOES-19 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 81.6 |
| 5961e833-6afa-3a92-baaf-f329ba6d2c2d | -8.3397 | -44.1658 | 2026-10-04 14:30:00 | GOES-19 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 95.9 |
| 6e196682-14a1-3463-8739-241c6a8129e7 | 3.8801 | -59.7223 | 2026-10-04 14:30:00 | GOES-19 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 62.6 |
| 7f0576a4-4c14-32fe-adfb-422dd2864c78 | -14.4221 | -51.2839 | 2026-10-04 14:30:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 66.8 |
| 2c7dc63c-c0c1-32f3-aced-1b39917a3e76 | 3.8061 | -59.9912 | 2026-10-04 14:30:00 | GOES-19 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 65.7 |
| 041e53d5-712b-340f-a95e-a7ef5dc1f617 | -12.1964 | -57.1303 | 2026-10-04 14:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 54.8 |
| 9aac0ecf-f131-3de5-a7a2-39712709fc9c | 3.6755 | -60.8874 | 2026-10-04 14:40:00 | GOES-19 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 78.1 |
| 8c61cf9c-bfe3-3385-b601-d748c296b314 | 3.9699 | -60.2735 | 2026-10-04 14:40:00 | GOES-19 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 75.9 |
| 25082f81-7a12-3831-882d-ddfb5eff94dd | 1.7583 | -50.8232 | 2026-10-04 14:40:00 | GOES-19 | PRACUÚBA | AMAPÁ | Brasil | 1600550 | 16 | 33 | nan | nan | nan | Amazônia | 63.1 |
| b0c61754-64f9-393d-9697-97096f0e6410 | 3.6393 | -60.7554 | 2026-10-04 14:40:00 | GOES-19 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 86.8 |
| cefc6f21-2be4-3246-b633-4c7773e46d32 | -10.8377 | -57.1979 | 2026-10-04 14:40:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 55.6 |
| 69e2ffdb-898a-303f-890a-5171e08ad31c | 3.6393 | -60.7365 | 2026-10-04 14:40:00 | GOES-19 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 76.7 |
| b6d9e7c5-3ba3-3212-9466-1517cb52b42d | -10.8187 | -57.2192 | 2026-10-04 14:40:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 67.8 |
| 528f53e4-9066-326b-89e7-0046eecaaee9 | 3.843 | -59.895 | 2026-10-04 14:40:00 | GOES-19 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 72.1 |
| 7595f3ed-b556-36b0-8129-c51469e9d6d7 | -10.8189 | -57.1993 | 2026-10-04 14:40:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 72.6 |
| ece4b7f0-a738-36b9-82dc-7be9347eba52 | 3.8965 | -60.3512 | 2026-10-04 14:40:00 | GOES-19 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 68.0 |
| 8144e15d-0f41-397f-9cf3-1b491c4397d6 | -10.5316 | -57.7747 | 2026-10-04 14:40:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 56.4 |
| 7d00cf4a-720f-399f-bfe4-72395fc967c8 | -10.5318 | -57.7549 | 2026-10-04 14:40:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 59.5 |
| 1be217d6-8e15-3bc0-a618-73b1ee430069 | 3.6755 | -60.8685 | 2026-10-04 14:40:00 | GOES-19 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 85.3 |
| f772b32b-483f-3fdf-9fec-e1eb17eed411 | 3.6211 | -60.7368 | 2026-10-04 14:40:00 | GOES-19 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 85.4 |
| 8056bab5-3599-3d01-bcdb-bd831ce30bf0 | 3.8953 | -60.7313 | 2026-10-04 14:40:00 | GOES-19 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 87.0 |
| ea69cbb1-52d1-33bd-824e-d30e08114691 | 3.8214 | -61.0171 | 2026-10-04 14:40:00 | GOES-19 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 68.5 |
| 80dcd6ab-8341-3b9e-a794-8051d4efa67a | -6.2355 | -52.6841 | 2026-10-04 14:40:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 57.3 |
| 4726b475-9bca-379a-b5c6-62d63bac33e4 | -12.1967 | -57.1103 | 2026-10-04 14:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 83.5 |
| 6e67ea97-3bf1-3efa-a400-b0e3d58f001b | -10.7999 | -57.2206 | 2026-10-04 14:40:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 58.7 |
| 87cfceb0-7abf-3cc2-970c-3455b1ff703a | -1.2455 | -49.0194 | 2026-10-04 14:40:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 65.8 |
| 15311881-1364-366a-b667-dff83928c08c | 3.6753 | -60.9632 | 2026-10-04 14:40:00 | GOES-19 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 78.9 |
| af4bdfc9-1fc1-3ae1-af8d-0964ebe864d0 | -1.0911 | -54.1001 | 2026-10-04 14:40:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 53.9 |
| 238dfd72-497a-3124-a604-b692315bc967 | -9.0046 | -65.6988 | 2026-10-04 14:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 52.1 |
| 272286ca-d06f-388d-aaeb-1d3104bb576e | 3.8965 | -60.3322 | 2026-10-04 14:40:00 | GOES-19 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 71.6 |
| 8a60bba4-70a5-3133-8898-26da8faee411 | -14.4031 | -51.265 | 2026-10-04 14:40:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 77.1 |
| 3a11e804-845c-3653-875c-3d3edeb42617 | 3.9136 | -60.7309 | 2026-10-04 14:40:00 | GOES-19 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 80.0 |
| fc1e56d9-5fb8-3394-8c64-ae9a7071dcee | 3.7483 | -60.9807 | 2026-10-04 14:40:00 | GOES-19 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 90.3 |
| c337f737-d624-3aed-804f-aa9c78eaad58 | -14.4221 | -51.2839 | 2026-10-04 14:40:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 73.7 |
| a8acbdbb-6e30-3748-a8c2-8ca25f02f1a5 | -6.2162 | -52.7876 | 2026-10-04 14:40:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 73.8 |
| 632e1050-4ff7-326e-9a04-58667547b045 | 3.7504 | -60.2592 | 2026-10-04 14:40:00 | GOES-19 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 70.3 |
| 7d0b6cca-561c-347b-95e0-79983af32ce6 | 1.9608 | -50.8612 | 2026-10-04 14:40:00 | GOES-19 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 65.0 |
| 05324437-32e7-3922-bcb0-b8c97c50ef21 | -12.1777 | -57.1119 | 2026-10-04 14:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 58.7 |
| 720d36d1-4125-38aa-9ded-41c19cb02929 | -13.5007 | -61.1333 | 2026-10-04 14:40:00 | GOES-19 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 65.1 |
| c686feea-30c7-34b6-981f-7bd697f151de | 3.6963 | -60.0126 | 2026-10-04 14:40:00 | GOES-19 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 67.3 |
| 3188d93e-f7cc-34d4-a256-e5e539f02106 | -9.7051 | -58.1247 | 2026-10-04 14:40:00 | GOES-19 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 54.9 |
| 41058ced-1462-3df2-81c7-1b3422a47afc | 3.8215 | -60.9792 | 2026-10-04 14:40:00 | GOES-19 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 79.4 |
| 689004e4-ce31-30d0-9a63-9b355bb83178 | 3.8214 | -60.9982 | 2026-10-04 14:40:00 | GOES-19 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 79.9 |
| 83390184-f078-389a-a016-df485438012c | 4.1134 | -61.2193 | 2026-10-04 14:40:00 | GOES-19 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 63.0 |
| 302fe63d-56cb-3395-b3ea-d8843418f039 | 3.6966 | -59.9173 | 2026-10-04 14:40:00 | GOES-19 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 70.3 |
| de1c2948-a78a-3fdc-ba7f-cd83de1d62b4 | 3.7504 | -60.2592 | 2026-10-04 14:50:00 | GOES-19 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 72.0 |
| 0483c714-2fbb-333e-af6c-03c7461d37a4 | 3.5481 | -60.6813 | 2026-10-04 14:50:00 | GOES-19 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 67.1 |
| fec27c04-d742-31eb-97ff-9a116c0c22ff | 3.6393 | -60.7554 | 2026-10-04 14:50:00 | GOES-19 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 83.2 |
| 0071adce-b62b-3c2c-894e-1fd567a67b23 | -10.8377 | -57.1979 | 2026-10-04 14:50:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 63.2 |
| 11f5746d-add3-3f38-9ccc-44156a2dc878 | 3.9136 | -60.7309 | 2026-10-04 14:50:00 | GOES-19 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 81.9 |
| 09303a65-a746-3e9b-a706-7cb558a4b1cb | -1.4487 | -48.9313 | 2026-10-04 14:50:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 71.6 |
| 0db1850e-ec2f-34fd-86d4-0bc5ad73a921 | 3.8965 | -60.3512 | 2026-10-04 14:50:00 | GOES-19 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 70.7 |
| 4129237f-0934-3f27-83f5-491e40c7f8b9 | 3.9314 | -60.9202 | 2026-10-04 14:50:00 | GOES-19 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 64.8 |
| 456b03f4-46ab-3064-abff-aecf78d284fa | 3.676 | -60.7168 | 2026-10-04 14:50:00 | GOES-19 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 78.2 |
| 1da618b3-1172-3a4e-b08b-8711a1691098 | -12.1967 | -57.1103 | 2026-10-04 14:50:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 89.2 |
| f4b24591-765a-38c3-aaba-8b87c6a6047f | 3.6966 | -59.9173 | 2026-10-04 14:50:00 | GOES-19 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 73.2 |
| ae1ee0c7-ea81-3e3e-ab04-8e13c5ca5c2f | 3.9132 | -60.8826 | 2026-10-04 14:50:00 | GOES-19 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 82.1 |
| da26c26c-6e02-3f2b-af21-eaae077dc87f | 3.434 | -51.3015 | 2026-10-04 14:50:00 | GOES-19 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 78.8 |
| 31c5360a-23a9-3931-b4ef-c90b86cf0531 | -1.3192 | -49.1249 | 2026-10-04 14:50:00 | GOES-19 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 65.5 |
| 3a7c01d6-d625-36d7-86d4-5cc9c4938615 | -10.8187 | -57.2192 | 2026-10-04 14:50:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 74.0 |
| 1b083163-2c87-3b02-ad0a-e003635f78be | 3.8783 | -60.3326 | 2026-10-04 14:50:00 | GOES-19 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 69.4 |
| 4e58ab3c-b2eb-30f4-afbc-5898071e3d2c | 3.7483 | -60.9807 | 2026-10-04 14:50:00 | GOES-19 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 92.0 |
| 40d891ad-67be-3b42-b889-6ff8ec54466a | -10.8189 | -57.1993 | 2026-10-04 14:50:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 77.2 |
| 2cb5bdce-4e96-33f0-886d-d6f001b2f1c8 | 4.1709 | -60.3832 | 2026-10-04 14:50:00 | GOES-19 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 61.7 |
| 49b727ac-346f-3509-b5e3-faf62f409232 | 3.6573 | -60.8688 | 2026-10-04 14:50:00 | GOES-19 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 82.5 |
| 15be0199-6c2b-3e2a-b49d-cacdec79d960 | -1.3927 | -49.2727 | 2026-10-04 14:50:00 | GOES-19 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 75.7 |
| d3eae7ed-f5cb-369d-bee7-cabe69f02c11 | 4.1134 | -61.2193 | 2026-10-04 14:50:00 | GOES-19 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 63.4 |
| 46389d19-4cc2-3159-bc7f-177aef159fc5 | -5.9887 | -53.5538 | 2026-10-04 14:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 70.6 |
| 74132fb9-5d59-3615-b9d7-84eedd9235d7 | -1.0911 | -54.1202 | 2026-10-04 14:50:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 62.4 |
| 8ea3601d-3714-3ac5-8c16-ab3d908bd847 | -12.1777 | -57.1119 | 2026-10-04 14:50:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 54.3 |
| b228a4e7-77f5-31b3-9ea1-af8f9e943c8f | -1.4672 | -48.9097 | 2026-10-04 14:50:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 61.0 |
| 93682fe6-5f56-3d3a-be61-5730f03de71d | 3.8953 | -60.7313 | 2026-10-04 14:50:00 | GOES-19 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 88.5 |
| d3ba360c-a658-3e5d-bdbc-7fc0e38c58d2 | 3.9699 | -60.2735 | 2026-10-04 14:50:00 | GOES-19 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 78.2 |
| b43aa428-a506-3553-98b4-675c2da17454 | 3.8965 | -60.3322 | 2026-10-04 14:50:00 | GOES-19 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 76.7 |
| f67bfb19-4ff2-3673-bcf4-117ecea5a192 | 3.6211 | -60.7368 | 2026-10-04 14:50:00 | GOES-19 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 87.4 |
| 3ae3b04a-179d-311f-a8c1-f18cfde94c96 | -1.2455 | -49.0194 | 2026-10-04 14:50:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 63.6 |
| a3c40d4d-cd17-3f78-b8c8-e83cac0a243b | 3.8965 | -60.3512 | 2026-10-04 15:00:00 | GOES-19 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 71.0 |
| 7bd1017d-dd4b-3de5-8956-a40e212cc2fb | 4.2249 | -60.6671 | 2026-10-04 15:00:00 | GOES-19 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 87.2 |
| 43dd3b6e-6a66-3cc8-b492-81689b180563 | -12.1964 | -57.1303 | 2026-10-04 15:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 85.1 |
| b623f767-b316-365c-b13a-ae3e1c56fc4a | -0.84 | -48.618 | 2026-10-04 15:00:00 | GOES-19 | SALVATERRA | PARÁ | Brasil | 1506302 | 15 | 33 | nan | nan | nan | Amazônia | 59.4 |
| 8f2e2576-64de-36cd-a2fb-9c95c24efb93 | 3.8783 | -60.3326 | 2026-10-04 15:00:00 | GOES-19 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 71.7 |
| 8bd40d00-2c82-3190-8ee0-2670400bb2e4 | 3.9351 | -59.7019 | 2026-10-04 15:00:00 | GOES-19 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 78.2 |
| b1e1850b-8cbc-3489-810e-1018ccd72f9c | 3.6573 | -60.8499 | 2026-10-04 15:00:00 | GOES-19 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 81.8 |
| 1f097cc6-8b67-3ac2-86d6-fed230ec7c6c | -1.0911 | -54.1001 | 2026-10-04 15:00:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 55.5 |
| 66ff5e3a-4e7b-31ea-b3f2-add9090a0097 | -1.1989 | -55.8684 | 2026-10-04 15:00:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 91.5 |
| f40b16c2-6afd-345a-81ac-a5f9c0d49988 | -9.7051 | -58.1247 | 2026-10-04 15:00:00 | GOES-19 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 63.2 |
| 5efa9c71-9f92-3c14-9ca7-0f795170c022 | 3.8426 | -60.0286 | 2026-10-04 15:00:00 | GOES-19 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 61.4 |
| 5d797f18-f046-39ae-a074-7d8b659e77eb | 3.6211 | -60.7368 | 2026-10-04 15:00:00 | GOES-19 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 86.3 |
| bc93672d-d667-3755-b6ac-c51ccbbf7b0b | -12.2154 | -57.1287 | 2026-10-04 15:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 63.3 |
| 659dfba6-9b4e-3478-8da6-89be5a36ade3 | 4.1697 | -60.7443 | 2026-10-04 15:00:00 | GOES-19 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 87.7 |
| 656e05c7-3d5f-3c4e-a9bc-e5b35f46892c | 0.4508 | -51.0656 | 2026-10-04 15:00:00 | GOES-19 | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 59.4 |


[Clique aqui para ver as próximas entradas](README76.md)
