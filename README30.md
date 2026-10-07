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

## Dados Diários - Página 30

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c033a530-493f-3e8c-8cf8-3bccf8bab1b5 | -3.531 | -54.6557 | 2026-10-07 03:00:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 93.3 |
| f495d0a0-7c01-3a06-b557-202c3486c86e | -3.1114 | -53.7839 | 2026-10-07 03:00:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 83.3 |
| 4bed4905-82fe-3522-a435-0e2f9438299c | -3.6205 | -55.2907 | 2026-10-07 03:00:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 62.8 |
| de4fd76a-2012-3968-ac36-6953194a8937 | -3.1115 | -53.7637 | 2026-10-07 03:00:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 67.4 |
| c69b1692-92f9-3632-8426-a5aecdb69f43 | -3.8567 | -55.9769 | 2026-10-07 03:00:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 74.9 |
| 0ac8c2b5-1a01-3080-947c-bbadd386979d | -2.7613 | -54.0941 | 2026-10-07 03:00:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 352.2 |
| 24243473-eae0-392c-a9ce-664be2822604 | -2.7796 | -54.0937 | 2026-10-07 03:00:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 299.7 |
| da90beb8-291d-3573-ae61-dd35f9871f80 | -3.4762 | -50.0883 | 2026-10-07 03:00:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 58.9 |
| f35ce9dc-9f8b-3bd7-9ddf-278859243f25 | -8.7225 | -45.204 | 2026-10-07 03:00:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 126.9 |
| d6db4b29-024c-3717-833f-bcbaa7396357 | -3.658 | -60.6222 | 2026-10-07 03:00:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 83.3 |
| edf3e0f7-c9b8-3960-b123-024430055751 | -3.0913 | -54.287 | 2026-10-07 03:00:00 | GOES-19 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 120.2 |
| eb17bfed-970e-3149-87b9-7a50af33b6a5 | -1.801 | -57.1161 | 2026-10-07 03:00:00 | GOES-19 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 56.6 |
| 08e1dc8b-9ef9-39e0-b5a8-4d356e29bc13 | -3.0913 | -54.307 | 2026-10-07 03:00:00 | GOES-19 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 56.4 |
| 4f35ddfb-fe78-3c8e-a84e-f37dedc27477 | -9.1517 | -65.9554 | 2026-10-07 03:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 54.1 |
| 732a45ce-839e-3968-9d5b-15080b920553 | -3.5127 | -54.6562 | 2026-10-07 03:00:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 90.1 |
| 0a776683-af56-3062-a9a6-b9bccf152998 | -3.0184 | -54.1282 | 2026-10-07 03:00:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 53.5 |
| 7e19f9ab-c3c4-38ec-a5c8-e65792d57a18 | -3.0 | -54.1287 | 2026-10-07 03:00:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 85.7 |
| c948d06c-1256-3fcf-8be4-70bd3e805478 | -8.7228 | -45.1812 | 2026-10-07 03:10:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 87.2 |
| 472f2055-1d2c-33b4-816d-74ff7221d23c | -15.2511 | -43.2743 | 2026-10-07 03:10:00 | GOES-19 | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 68.1 |
| 3820575f-9035-30ee-bc86-4b5b008d0ad9 | -5.7189 | -45.1547 | 2026-10-07 03:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 140.8 |
| fc32aba8-f219-3719-898a-63d973faf7fd | -6.2362 | -41.9991 | 2026-10-07 03:10:00 | GOES-19 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 65.0 |
| b809b743-769d-3eb9-8774-9ac1acf2df64 | -3.1114 | -53.7839 | 2026-10-07 03:10:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 77.3 |
| 9c2a21b5-c6ca-3563-b6dd-aefbe203d0fb | -3.531 | -54.6557 | 2026-10-07 03:10:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 96.4 |
| 9b5f0cb3-fcf9-3a62-9af6-2b952c7a0505 | -2.7613 | -54.0941 | 2026-10-07 03:10:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 329.2 |
| a798082c-194b-3cbc-aa81-c05263187648 | -3.5127 | -54.6562 | 2026-10-07 03:10:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 88.9 |
| af9693d2-d8c3-398e-9a21-f405a0142eb4 | -3.073 | -54.2674 | 2026-10-07 03:10:00 | GOES-19 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 65.5 |
| 810f5f54-a433-3bfe-b8e0-b9375c79c634 | -3.8567 | -55.9769 | 2026-10-07 03:10:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 74.9 |
| bad22306-a7e8-3744-9dc2-f2dfc392d59c | -2.7797 | -54.0736 | 2026-10-07 03:10:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 80.3 |
| a740d221-f7d0-33c0-8593-f44d160e2c4c | -8.2865 | -50.2731 | 2026-10-07 03:10:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 96.8 |
| 1bfa1ad5-eb1e-37ca-addf-ab0643d91c05 | -3.6205 | -55.2907 | 2026-10-07 03:10:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 61.8 |
| 37ec6010-0fe5-3b67-ba37-b635a610a1b6 | -3.1115 | -53.7637 | 2026-10-07 03:10:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 68.3 |
| 11de3259-688b-3d8e-9426-ab66ca3e7a8d | -3.0913 | -54.287 | 2026-10-07 03:10:00 | GOES-19 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 123.8 |
| 9704268b-b73b-31ff-850f-6758e11ac900 | -3.5311 | -54.6357 | 2026-10-07 03:10:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 58.3 |
| e575eaba-299b-3a62-9719-19ddd0afd006 | -6.2364 | -41.9752 | 2026-10-07 03:10:00 | GOES-19 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 76.1 |
| e9d7e5fb-bc6e-3fcd-bc96-bd8adb2e1a8b | -2.7796 | -54.1138 | 2026-10-07 03:10:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 202.9 |
| 0021517e-3aa5-3885-bf57-db6000cb7a28 | -3.0731 | -54.2473 | 2026-10-07 03:10:00 | GOES-19 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 57.0 |
| 13394aba-0c3f-36ea-a83c-43179bea3a4d | -3.0184 | -54.1282 | 2026-10-07 03:10:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 56.4 |
| 64ea9d8d-31f7-352e-a17d-c95588621d56 | -1.801 | -57.1161 | 2026-10-07 03:10:00 | GOES-19 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 42.5 |
| dba04815-3a52-3447-ba93-d759eef5bb7d | -3.1787 | -50.5597 | 2026-10-07 03:10:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 75.5 |
| b6809a4b-5ffb-3eb2-8141-3cfafb9c1140 | -2.7612 | -54.1142 | 2026-10-07 03:10:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 253.0 |
| 5bb7a270-6a5d-3068-92fa-c06ac8559c7a | -8.7039 | -45.1832 | 2026-10-07 03:10:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 72.4 |
| e69bc3c4-2379-36c5-baf8-3bae46a1e3f6 | -11.7335 | -43.649 | 2026-10-07 03:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 71.3 |
| 034b3955-057b-3d78-822e-9624543b9305 | -8.7036 | -45.2061 | 2026-10-07 03:10:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 179.0 |
| 7e814ba8-eba4-36e6-a3ae-3df40955f154 | -5.7187 | -45.1773 | 2026-10-07 03:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 88.2 |
| a80e011c-1272-3e96-9f4e-8ec1462fa702 | -5.7376 | -45.1533 | 2026-10-07 03:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 94.0 |
| bfe29370-072b-3ace-82f6-7be1d1151a64 | -3.0374 | -53.9268 | 2026-10-07 03:10:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 49.9 |
| ccadeaf3-5073-32d5-bfff-fbe4778d2d15 | -3.0 | -54.1287 | 2026-10-07 03:10:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 67.6 |
| 6dd05d15-c3f4-3598-9dda-5419a4af2df4 | -5.7374 | -45.176 | 2026-10-07 03:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 67.9 |
| 06d116c1-b197-39d1-a923-197e4d4cf967 | -3.0914 | -54.2669 | 2026-10-07 03:10:00 | GOES-19 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 59.4 |
| b65edae4-f072-3346-a7ef-681f4295584a | -2.9448 | -54.1501 | 2026-10-07 03:10:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 59.2 |
| 4d8308ba-9928-3dc5-a93f-3641c597c937 | -3.8566 | -55.9967 | 2026-10-07 03:10:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 70.5 |
| f9f89a31-c267-31f2-abfe-1987ba6eac2f | -3.4762 | -50.0883 | 2026-10-07 03:10:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 55.3 |
| 1294e848-8d92-31c6-9545-e93a1d08f5c6 | -2.7796 | -54.0937 | 2026-10-07 03:10:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 231.5 |
| b0cb9ba0-0e23-3544-a269-8e80b74c2c36 | -3.0375 | -53.9066 | 2026-10-07 03:10:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 62.0 |
| 396a610d-dc6e-326d-89f1-1d596b0ef13e | -2.7613 | -54.074 | 2026-10-07 03:10:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 98.0 |
| f83d05dc-d867-3b51-89ea-4c4a3e09e06b | -3.658 | -60.6222 | 2026-10-07 03:10:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 85.5 |
| fd64ff6e-d022-3577-bbcf-170abe9a47d2 | -8.7225 | -45.204 | 2026-10-07 03:10:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 129.7 |
| feb67204-02e3-3290-9646-05c3710ef7a2 | -3.0913 | -54.307 | 2026-10-07 03:10:00 | GOES-19 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 52.8 |
| 61f3b6a0-a46e-3c80-8cc2-14c72f11bdf8 | -3.6579 | -60.6412 | 2026-10-07 03:10:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 60.1 |
| 593efcfa-4a6f-3c6a-a407-31277ea547ab | -2.76 | -54.08 | 2026-10-07 03:15:00 | MSG-03 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 27c0fa05-2061-3c5c-b7e7-760f821a76b8 | -2.7797 | -54.0736 | 2026-10-07 03:20:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 69.5 |
| 13e30917-3f40-3e80-af3d-0037a1dd47ca | -3.1115 | -53.7637 | 2026-10-07 03:20:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 68.4 |
| f1255cb5-0927-3746-8b66-67ef5aa3cfce | -1.801 | -57.1161 | 2026-10-07 03:20:00 | GOES-19 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 42.5 |
| 93452445-45ee-3e01-9a5b-9a79e400d6ad | -3.5311 | -54.6357 | 2026-10-07 03:20:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 56.7 |
| 7585cea4-c7e9-394c-bbad-239bad0a24b4 | -8.7036 | -45.2061 | 2026-10-07 03:20:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 184.9 |
| af02ba9c-dd3e-3bc9-a2d6-9f72e2378c80 | -2.7613 | -54.074 | 2026-10-07 03:20:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 99.5 |
| 8bcd786c-18da-3b47-b1be-8460604f04fb | -3.1787 | -50.5597 | 2026-10-07 03:20:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 69.7 |
| 8b4ad61d-c54d-3cad-8f26-05cfa8bd89fc | -9.1517 | -65.9554 | 2026-10-07 03:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 40.6 |
| 8de7f24f-c90c-3a2a-8cef-ea0a26421d45 | -3.0913 | -54.307 | 2026-10-07 03:20:00 | GOES-19 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 54.0 |
| 6aab4f84-f856-364a-9bfe-1cb1dddcff1f | -3.1114 | -53.7839 | 2026-10-07 03:20:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 74.2 |
| c6506190-f50a-3076-a639-9f2bf0839dbd | -5.7376 | -45.1533 | 2026-10-07 03:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 91.2 |
| bccab250-2137-385c-82fd-b4d4d878a894 | -3.658 | -60.6222 | 2026-10-07 03:20:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 66.7 |
| 831bc7c9-e8c3-3884-b54d-cb0ac7c9bbcd | -2.9448 | -54.1501 | 2026-10-07 03:20:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 60.4 |
| e43bb34e-1560-3fda-a235-96062a556a57 | -5.7374 | -45.176 | 2026-10-07 03:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 89.6 |
| f3dec5c8-c412-38f2-a64e-a44d06f00c1d | -5.7189 | -45.1547 | 2026-10-07 03:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 114.5 |
| affe6c89-74f4-3326-bd07-db50d8e31649 | -8.7228 | -45.1812 | 2026-10-07 03:20:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 69.5 |
| 4f959889-326e-366a-bb1e-4d41183783cd | -2.7612 | -54.1142 | 2026-10-07 03:20:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 248.3 |
| 1b081f06-926c-3118-8a3f-834bd17bd71c | -3.8567 | -55.9769 | 2026-10-07 03:20:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 73.8 |
| 4b43a734-195d-3349-9fac-d3d283c8533b | -3.0375 | -53.9066 | 2026-10-07 03:20:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 51.7 |
| f5354bcd-f429-3968-9c42-6f77decb6d77 | -3.0 | -54.1287 | 2026-10-07 03:20:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 74.3 |
| c812ab64-e6af-3aa0-8f5e-350c10b19640 | -3.4762 | -50.0883 | 2026-10-07 03:20:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 51.5 |
| c2c847b6-5405-3aa0-b928-b60878a19e7c | -8.7039 | -45.1832 | 2026-10-07 03:20:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 78.3 |
| f72c3d78-68f1-38ad-9dad-0c4106dc7767 | -11.7335 | -43.649 | 2026-10-07 03:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 88.0 |
| 8a2c0f6f-0aa2-3643-bb22-a94286824922 | -3.6206 | -55.2708 | 2026-10-07 03:20:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 50.2 |
| c24ecd9d-a35b-35b8-a1b4-9882cc869279 | -3.0731 | -54.2473 | 2026-10-07 03:20:00 | GOES-19 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 57.5 |
| 11db0228-bb3e-378a-a88f-a7300434fb3c | -3.8566 | -55.9967 | 2026-10-07 03:20:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 68.8 |
| 61c3adef-59f5-346e-9bec-f3aba98f416b | -2.7613 | -54.0941 | 2026-10-07 03:20:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 291.3 |
| 95196d9a-04f3-37cd-b2e8-e083718c9fea | -8.2865 | -50.2731 | 2026-10-07 03:20:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 83.6 |
| 38ef634d-bd0b-3c9e-9f0c-c67a1c1e2606 | -3.0913 | -54.287 | 2026-10-07 03:20:00 | GOES-19 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 112.3 |
| c4b10a32-0019-325f-bfa4-786fce99f8b9 | -3.0914 | -54.2669 | 2026-10-07 03:20:00 | GOES-19 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 57.7 |
| 01f4bf7e-609e-3276-b0cd-d650894f3435 | -3.531 | -54.6557 | 2026-10-07 03:20:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 86.3 |
| 10277568-3da6-38e0-b8eb-27e1efdc0927 | -6.2362 | -41.9991 | 2026-10-07 03:20:00 | GOES-19 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 67.5 |
| 1474b1a2-d53c-3197-9907-ec589500c9d3 | -3.6579 | -60.6412 | 2026-10-07 03:20:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 58.2 |
| 65edbd38-12aa-3ff8-98d7-a28be664d9a6 | -3.5127 | -54.6562 | 2026-10-07 03:20:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 87.2 |
| 5582b6e7-8824-3599-a261-7b42f6cc077d | -2.7796 | -54.0937 | 2026-10-07 03:20:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 174.5 |
| 716dfd8d-5104-3b82-bac7-ee34bcc18620 | -5.7187 | -45.1773 | 2026-10-07 03:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 106.4 |
| c091c674-bf52-3cd7-b7ae-7119776aaa6a | -2.7796 | -54.1138 | 2026-10-07 03:20:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 159.5 |
| 1d013a98-9495-3612-a6b5-6944d13cb6f9 | -8.7225 | -45.204 | 2026-10-07 03:20:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 98.7 |
| c21baa93-8c7b-34b1-85ad-a58222f7c3db | -3.073 | -54.2674 | 2026-10-07 03:20:00 | GOES-19 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 68.4 |
| 4beba637-a7be-3cc0-a4f5-00c7d988567c | -3.6205 | -55.2907 | 2026-10-07 03:20:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 72.7 |


[Clique aqui para ver as próximas entradas](README31.md)
