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
| 01593860-613e-3c53-bcaa-6d0e966c99f3 | -3.10601 | -53.76262 | 2026-10-06 00:18:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 95.6 |
| 7e73d886-db20-39d6-88ae-5be2796e2516 | -4.56969 | -54.95677 | 2026-10-06 00:18:00 | TERRA_M-M | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 9.9 |
| d85b4c0b-e95e-39da-acb1-2f83798b10bc | -4.04819 | -54.05512 | 2026-10-06 00:18:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 8146fa40-3272-37a3-921a-af8ba329fccb | -3.66617 | -54.54497 | 2026-10-06 00:18:00 | TERRA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 16.1 |
| 17ce4945-0579-3a1d-862a-7d0908f82800 | -3.72897 | -55.48079 | 2026-10-06 00:18:00 | TERRA_M-M | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 8008634e-42a0-3eef-90b6-1dbff5d3bf70 | -4.23397 | -49.98057 | 2026-10-06 00:18:00 | TERRA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 12.9 |
| 2f515c77-dd79-3818-823d-2e65c19c1fc2 | -2.99573 | -54.03571 | 2026-10-06 00:18:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 013a4929-6be3-369e-8eea-6898637f35d7 | -3.13666 | -53.72171 | 2026-10-06 00:18:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 35fdcfa3-0f31-34ab-9ec0-530e62a35951 | -3.45904 | -54.59247 | 2026-10-06 00:18:00 | TERRA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| ec610d0f-737d-3aa5-8d15-4721d25462a0 | -2.94405 | -54.06696 | 2026-10-06 00:18:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 2e2991d2-d1ed-3125-8aa0-b8def5ed8e10 | -2.78673 | -57.67209 | 2026-10-06 00:18:00 | TERRA_M-M | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 219.2 |
| 7e9a6087-636b-3196-b038-493001ef56ef | -3.06192 | -54.17342 | 2026-10-06 00:18:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 42.9 |
| 13d93d46-b8d3-3b09-a239-4c5f1a8a1a8d | -3.06153 | -54.25169 | 2026-10-06 00:18:00 | TERRA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 19.7 |
| 0216ab17-7f12-3187-b9f1-c1d474e2f629 | -5.61937 | -44.85964 | 2026-10-06 00:18:00 | TERRA_M-M | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 34.4 |
| ad13531b-88d1-3ca2-a393-26d9153d2ec0 | -2.92482 | -54.12383 | 2026-10-06 00:18:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 66.7 |
| df9ab21d-e160-33f6-bea8-c1b27bb91e48 | -3.37875 | -58.18868 | 2026-10-06 00:18:00 | TERRA_M-M | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 19.1 |
| 548b79f8-a9a1-3904-a2b6-30e633652160 | -2.99711 | -57.78981 | 2026-10-06 00:18:00 | TERRA_M-M | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 8.7 |
| ef74bff3-2b0d-3e67-b4d5-b77147e00422 | -3.09851 | -53.70873 | 2026-10-06 00:18:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 34.0 |
| fef663fe-df73-32c8-9df0-c1baac2bf5e7 | -2.98782 | -54.10906 | 2026-10-06 00:18:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 11.1 |
| a7223eff-46a4-3897-a195-476d2be597b9 | -4.45378 | -47.92783 | 2026-10-06 00:18:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 38.1 |
| c6b976e2-2037-311f-b00a-4e048ca1008b | -2.87297 | -54.14011 | 2026-10-06 00:18:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 124.5 |
| 9877fffb-b434-39f1-8530-a28981b1d5ea | -2.87419 | -54.14893 | 2026-10-06 00:18:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 196.3 |
| 2f82f9f2-2d1d-3f89-9065-928872a54e97 | -3.6915 | -55.942 | 2026-10-06 00:20:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 130.0 |
| bc522b72-3357-3d6c-be09-3c3c6304c1bd | -3.3723 | -58.1957 | 2026-10-06 00:20:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 107.2 |
| 6d6045ad-ebfb-3e35-8f03-877b4b374803 | -2.7796 | -54.0937 | 2026-10-06 00:20:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 98.9 |
| af61b4ce-40e7-331c-bc70-f97652a874bc | -2.9816 | -54.1291 | 2026-10-06 00:20:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 72.1 |
| 7bf2d8cc-a833-3e0a-972f-56061b563306 | -2.7696 | -57.6847 | 2026-10-06 00:20:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 103.6 |
| 8ab61844-7ed9-31e3-908d-339e21f11866 | -3.6731 | -55.9622 | 2026-10-06 00:20:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 101.3 |
| eb4ffa83-c748-3330-aeb3-f392fc53ba2e | -3.1608 | -50.4347 | 2026-10-06 00:20:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 74.4 |
| ecaa36d3-38b8-36b6-b45c-7d230c00992e | 0.4465 | -60.5442 | 2026-10-06 00:20:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 63.4 |
| 936d3727-8c72-3908-b347-a8d135b4250a | -3.6732 | -55.9425 | 2026-10-06 00:20:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 132.0 |
| fda6a292-f40c-3480-9b69-e25ca0ea2a76 | -9.7313 | -65.0757 | 2026-10-06 00:20:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 112.4 |
| 5ef39115-beff-386f-aa31-98ef6c3ca9ce | -11.6378 | -43.6403 | 2026-10-06 00:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 125.9 |
| f86b7835-d4ac-3fa8-90d7-dc0019e74fa1 | -3.3906 | -58.1953 | 2026-10-06 00:20:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 135.8 |
| 828b7b34-0e8c-37fa-83a5-64c27122daaa | -2.7879 | -57.6843 | 2026-10-06 00:20:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 177.0 |
| 0c91b7de-c109-367c-9359-298fa38ec00a | -3.0 | -54.1287 | 2026-10-06 00:20:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 88.4 |
| 903ab595-0100-3ec2-bbaf-143f5a1c21e1 | -2.7879 | -57.6649 | 2026-10-06 00:20:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 166.4 |
| 267c4873-c9ae-33f7-baec-b859b849a51a | -3.3905 | -58.2146 | 2026-10-06 00:20:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 95.7 |
| 2cf841ae-1f9d-3c1f-8ffd-e470693c32f2 | -11.6374 | -43.664 | 2026-10-06 00:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 105.8 |
| 852b2134-d0e7-3257-be93-a414fe1cebc6 | -2.7696 | -57.6653 | 2026-10-06 00:20:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 98.6 |
| 6cfd46ad-6500-3401-9089-4dbc676f6f36 | -9.7126 | -65.0951 | 2026-10-06 00:20:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 61.9 |
| 91008e84-ed04-3a91-9760-092307d45488 | -3.0191 | -53.9071 | 2026-10-06 00:20:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 80.1 |
| 50d8853e-13fb-3473-81e2-23453d42c41d | -2.7796 | -54.1138 | 2026-10-06 00:20:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 67.1 |
| 3fb07724-2ad4-3239-8af6-a03f14da5ea5 | -3.0192 | -53.887 | 2026-10-06 00:20:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 106.7 |
| cff535c3-f010-372b-8c85-1475549da38a | -3.6915 | -55.9618 | 2026-10-06 00:20:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 149.2 |
| 598377cd-8109-3b73-835a-d486c6e7d86c | -11.6946 | -43.6787 | 2026-10-06 00:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 125.2 |
| e7042e8a-c193-3a34-882e-98d0407462f6 | -2.9817 | -54.1091 | 2026-10-06 00:20:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 66.3 |
| 0b1cbd0c-f036-3781-9a10-32ccc2940d8c | -3.1607 | -50.4556 | 2026-10-06 00:20:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 49.6 |
| cd23db3e-92d0-37e6-b83d-47c7f380394e | -4.8075 | -47.3261 | 2026-10-06 00:20:00 | GOES-19 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 42.4 |
| d5ea5b81-ff0b-3a98-96d3-d1e5ab65e680 | -11.6566 | -43.661 | 2026-10-06 00:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 137.3 |
| 68bd414a-fe7f-36e2-a578-1c55abf9185d | -4.3587 | -47.7853 | 2026-10-06 00:20:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 65.7 |
| 9ec099ad-d839-38a4-802c-4c96bf862c66 | -3.4955 | -49.8979 | 2026-10-06 00:20:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 44.8 |
| 5a378d89-4a36-3b8e-b60e-f8c284e7412b | -8.7033 | -45.2289 | 2026-10-06 00:20:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 75.0 |
| 3e5a3ae7-4f0f-360c-a737-776abd4d9060 | 0.4465 | -60.5252 | 2026-10-06 00:20:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 43.3 |
| 8de82d90-b1d1-3968-9999-14d4df916746 | -3.0001 | -54.1086 | 2026-10-06 00:20:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 77.3 |
| f0c50a91-1555-34b3-82b8-547314a53363 | -8.7036 | -45.2061 | 2026-10-06 00:20:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 101.6 |
| 310a4012-0c64-3588-89d1-8526b015a3e5 | -3.0375 | -53.8865 | 2026-10-06 00:20:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 73.2 |
| 10590d4d-47d4-39c4-a3f8-5e0ca4dedb44 | -4.1084 | -49.4084 | 2026-10-06 00:20:00 | GOES-19 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 38.1 |
| 119757fa-8fa0-3d39-a42a-6cc40332aa7e | -8.5847 | -45.6502 | 2026-10-06 00:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 58.5 |
| 0fe49e33-d570-343c-90db-0878bda19c2d | -11.657 | -43.6373 | 2026-10-06 00:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 173.8 |
| ee72821e-de69-3626-85bc-98aa80e6767b | -9.7312 | -65.0944 | 2026-10-06 00:20:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 157.5 |
| a537dd05-e2d2-3d00-862c-0f6762ca7ef3 | -11.6951 | -43.655 | 2026-10-06 00:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 91.1 |
| 571261eb-7901-3ff0-931d-73d69c2fa96a | 1.8496 | -55.78962 | 2026-10-06 00:20:00 | TERRA_M-M | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| a59e6a92-0bf3-39e8-a150-4039ee2b8d54 | -2.48629 | -56.09616 | 2026-10-06 00:20:00 | TERRA_M-M | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 15cc6bab-c9bb-3a5d-b785-ad7255473457 | 3.58349 | -61.31675 | 2026-10-06 00:20:00 | TERRA_M-M | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 98afbffd-144e-38ff-a045-af8748ab7ace | 0.44336 | -60.55299 | 2026-10-06 00:20:00 | TERRA_M-M | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 14.1 |
| af471b15-2013-3405-b0ea-1e30dd714ec7 | 3.57363 | -61.32619 | 2026-10-06 00:20:00 | TERRA_M-M | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 68.1 |
| c3cfcb66-ba34-37a5-b423-62e60a73f77e | 1.72964 | -55.73135 | 2026-10-06 00:20:00 | TERRA_M-M | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 73a725f0-983d-3888-a82e-10b7517d18e6 | -2.05048 | -56.89187 | 2026-10-06 00:20:00 | TERRA_M-M | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 7.3 |
| f7cd81ec-e0d4-31a8-ab5f-b4934226c508 | 1.56346 | -55.99076 | 2026-10-06 00:20:00 | TERRA_M-M | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 483cfb35-4ccf-3149-9758-c81542f61433 | -2.07437 | -56.85881 | 2026-10-06 00:20:00 | TERRA_M-M | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 10.9 |
| c280c7e3-0c68-3afa-b9bd-542105a81581 | 1.88322 | -55.74079 | 2026-10-06 00:20:00 | TERRA_M-M | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 7638e18f-94c2-3387-83d0-1a5c512e3f4e | 1.87081 | -55.76581 | 2026-10-06 00:20:00 | TERRA_M-M | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| dbb863af-93ba-37a5-a366-696efd73814f | -2.37238 | -55.27061 | 2026-10-06 00:20:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| ced3c934-e762-3712-9e04-b216057417ac | 0.44556 | -60.53719 | 2026-10-06 00:20:00 | TERRA_M-M | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 63.4 |
| 6c7bb195-d3bc-3200-8246-0b1627299fa5 | 2.47226 | -50.83403 | 2026-10-06 00:20:00 | TERRA_M-M | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 28.5 |
| de45bbd7-ac37-35fa-9f88-f57f90e4357f | -2.13498 | -56.6959 | 2026-10-06 00:20:00 | TERRA_M-M | FARO | PARÁ | Brasil | 1503002 | 15 | 33 | nan | nan | nan | Amazônia | 12.6 |
| 93e1afdb-0be2-3405-a392-2b6e5936268f | -1.47942 | -54.53155 | 2026-10-06 00:20:00 | TERRA_M-M | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 16990f23-28e8-3e42-af0a-207ffe7e74ca | 1.85081 | -55.78086 | 2026-10-06 00:20:00 | TERRA_M-M | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| d0f1d51b-b302-349b-a417-8a8ba61b97ab | 2.7401 | -60.24991 | 2026-10-06 00:20:00 | TERRA_M-M | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 11.3 |
| d9e92fb3-4b58-3ebb-af27-f35a21f9afc7 | -2.49971 | -56.12593 | 2026-10-06 00:20:00 | TERRA_M-M | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 5dc4187d-48d1-3f5e-aff2-ab0c09371cee | -2.46448 | -56.07112 | 2026-10-06 00:20:00 | TERRA_M-M | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| a03df1fa-1c1f-39b6-ab85-fc4806cf99e4 | 2.15082 | -55.95417 | 2026-10-06 00:20:00 | TERRA_M-M | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| cb52dded-6c6e-359f-8098-d9d584930a43 | 2.46085 | -50.83246 | 2026-10-06 00:20:00 | TERRA_M-M | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 15.7 |
| 93d65fad-ac31-30c2-bbf2-d9ae75b5afdd | -1.2815 | -56.98315 | 2026-10-06 00:20:00 | TERRA_M-M | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 46.0 |
| d58617d4-0b50-397c-81cb-28a47b9affa9 | -2.13629 | -56.70553 | 2026-10-06 00:20:00 | TERRA_M-M | FARO | PARÁ | Brasil | 1503002 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 6e936c67-1ef2-3b38-bd76-d8af2a0dd07b | -2.83409 | -59.24864 | 2026-10-06 00:20:00 | TERRA_M-M | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 8c46dc2e-a42e-3a71-bac6-e22354f28116 | -2.33078 | -56.17091 | 2026-10-06 00:20:00 | TERRA_M-M | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 5f1957df-3e94-34c0-bc9f-46e21ed783ce | 1.8584 | -55.79084 | 2026-10-06 00:20:00 | TERRA_M-M | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 14.4 |
| e9f23ca3-0935-3375-a667-e692b175a209 | -2.3889 | -56.12535 | 2026-10-06 00:20:00 | TERRA_M-M | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 46345bba-3de4-38b4-ad76-18b3961a12e6 | 1.8596 | -55.78209 | 2026-10-06 00:20:00 | TERRA_M-M | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 18.8 |
| e6b4b0eb-e243-343a-b45c-792f746c7f37 | 3.32037 | -51.34304 | 2026-10-06 00:20:00 | TERRA_M-M | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 77a92808-df3d-3983-8bb2-1719bb319772 | -1.11887 | -54.12064 | 2026-10-06 00:20:00 | TERRA_M-M | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 893e8b02-d1bc-3a8d-ab3a-368b5e7ed4e7 | -2.33015 | -57.99207 | 2026-10-06 00:20:00 | TERRA_M-M | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 5b9c523e-a348-34f6-8582-9b41f8139f09 | 3.57134 | -61.34226 | 2026-10-06 00:20:00 | TERRA_M-M | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 24.7 |
| a8049ea7-838e-319d-979e-342b402e1274 | -2.43586 | -58.0184 | 2026-10-06 00:20:00 | TERRA_M-M | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 437823ad-da99-36c4-9d4a-53e6f6999122 | 1.86201 | -55.76459 | 2026-10-06 00:20:00 | TERRA_M-M | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 80036ce7-f337-3707-85c6-debc129f8c5e | 2.73573 | -60.25698 | 2026-10-06 00:20:00 | TERRA_M-M | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 14.5 |
| 5a65d91c-76e7-314a-83d8-78759d6149bc | -1.80524 | -53.75409 | 2026-10-06 00:20:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 77edabb7-ad8c-38e2-910a-2db8d95b0b60 | 1.87201 | -55.75706 | 2026-10-06 00:20:00 | TERRA_M-M | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 16.1 |


[Clique aqui para ver as próximas entradas](README7.md)
