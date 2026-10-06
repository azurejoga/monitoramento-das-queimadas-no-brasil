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
| 7ea0758e-6865-3a37-90e6-03990637660c | -3.6915 | -55.942 | 2026-10-06 02:20:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 69.1 |
| 7347a23e-3f23-3a09-9c94-2bb9efc69303 | -11.2794 | -45.5281 | 2026-10-06 02:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 58.4 |
| 073dd54a-b0b7-3a16-8f9e-f23d0ccaa74d | -9.0232 | -65.6982 | 2026-10-06 02:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 56.3 |
| a55270f5-1c9b-375e-bba8-94a1e97c5802 | -11.2611 | -45.4849 | 2026-10-06 02:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 104.8 |
| 73042768-7c1a-3716-a88e-f047c756f0d7 | -3.6731 | -55.9622 | 2026-10-06 02:20:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 74.8 |
| aacb207e-7ecc-317a-b9f9-8d14e7a87904 | -3.0917 | -54.1867 | 2026-10-06 02:20:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 68.3 |
| 3af830b7-ee3f-397d-b42f-8ecd2e0f14b0 | -3.0 | -54.1287 | 2026-10-06 02:20:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 75.0 |
| 24e32639-5138-39dd-b301-43b935f7755d | -3.0375 | -53.9066 | 2026-10-06 02:20:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 57.8 |
| a93f4996-cc92-39ce-a1b8-2881fedc9901 | -3.1101 | -54.1661 | 2026-10-06 02:20:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 53.6 |
| 70a109a5-3148-3b02-8356-5c407d08edde | -3.0192 | -53.887 | 2026-10-06 02:20:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 85.0 |
| 3587ca99-8a8f-3639-ac19-bb8b3bcc0cd9 | -2.9449 | -54.13 | 2026-10-06 02:20:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 67.3 |
| 00a9e012-44bb-36d3-8f5d-118d4d8b0904 | -5.8511 | -45.0091 | 2026-10-06 02:20:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 76.0 |
| 3c3e8b8f-e316-3686-834f-1fd099f55c82 | -2.8714 | -54.1318 | 2026-10-06 02:20:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 87.6 |
| 517809cf-68ec-3b38-9901-2fab6fd179f7 | -2.8712 | -54.1719 | 2026-10-06 02:20:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 62.3 |
| 3f1e654e-e160-3930-946c-3393d5723927 | -11.2798 | -45.5052 | 2026-10-06 02:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 256.6 |
| bf985fc5-5724-3304-9ff8-0edba4bd72d3 | -2.9816 | -54.1291 | 2026-10-06 02:20:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 75.6 |
| ad35a19e-e370-3e07-94f1-5a0ed1013343 | 0.4465 | -60.5442 | 2026-10-06 02:20:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 63.9 |
| 357d18c7-e546-37cf-8737-5c13b4d83d98 | -2.7879 | -57.6843 | 2026-10-06 02:20:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 101.2 |
| e97cb80b-8e67-34e5-845f-037bb3813728 | -2.7796 | -54.0937 | 2026-10-06 02:20:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 71.6 |
| 5d24323e-1657-3cc6-86f2-0961a615aa79 | -2.9265 | -54.1305 | 2026-10-06 02:20:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 74.9 |
| 3476acac-34aa-34c8-b0ba-7d9bfa7b2db3 | -2.9448 | -54.1501 | 2026-10-06 02:20:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 76.9 |
| 21e3eeed-ed3a-3543-a91d-16ede928938b | -3.0734 | -54.147 | 2026-10-06 02:20:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 62.5 |
| 228aaeaf-ab71-3464-832c-7b4a856d55dc | -2.7879 | -57.6649 | 2026-10-06 02:20:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 71.2 |
| 63f8fa56-078c-33f0-b686-cfed070b015d | -11.2802 | -45.4823 | 2026-10-06 02:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 109.6 |
| 464c7ff2-9409-3435-8dbb-f7e82ae5d7be | -2.8897 | -54.1514 | 2026-10-06 02:20:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 66.5 |
| f539368b-bdd9-3f72-b8e2-06481bfecd18 | -9.7126 | -65.0951 | 2026-10-06 02:20:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 60.1 |
| 2a57aa07-c349-31ae-a58d-faaf5416d647 | -2.8897 | -54.1514 | 2026-10-06 02:30:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 64.7 |
| 0ec2f2b3-79c3-3be4-ab6b-6210da9b9498 | -11.2607 | -45.5078 | 2026-10-06 02:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 143.7 |
| 1045b1e1-1149-3634-bda0-7dd57390fce0 | -2.7796 | -54.0937 | 2026-10-06 02:30:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 68.8 |
| 79d3957d-e9bc-3bf6-aca4-5e842bc28f4f | -3.0191 | -53.9071 | 2026-10-06 02:30:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 72.3 |
| 8a91e6bc-c4bf-31ca-a8bf-b810e3b6cee4 | -9.0232 | -65.6982 | 2026-10-06 02:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 60.5 |
| e933fd4a-203a-3d5f-bb85-48ddc20c2527 | -3.0192 | -53.887 | 2026-10-06 02:30:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 89.4 |
| 204ba9c1-0fc7-3b20-8879-b67076a4ec40 | -3.0375 | -53.9066 | 2026-10-06 02:30:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 68.0 |
| 25a94c0c-3919-3883-9c17-1ed695616f9d | -2.9449 | -54.13 | 2026-10-06 02:30:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 62.9 |
| d63d8b61-d9e1-3af2-8530-e5573d6d93b9 | -2.9448 | -54.1501 | 2026-10-06 02:30:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 77.5 |
| 070ed69d-1c59-3460-8138-ceca31842276 | -11.2798 | -45.5052 | 2026-10-06 02:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 268.4 |
| 9f80184e-9a74-3460-ad28-6b232dcf2dbb | -3.1116 | -53.7436 | 2026-10-06 02:30:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 58.8 |
| 515ea48e-4b21-3193-b160-176e52a6500f | -2.8713 | -54.1518 | 2026-10-06 02:30:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 115.2 |
| 8df5f9d3-ffe1-3239-8590-b8ff5a592d8f | -3.6915 | -55.9618 | 2026-10-06 02:30:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 74.2 |
| 7f2367d4-6000-3cc4-9046-a9f076db473e | -11.2802 | -45.4823 | 2026-10-06 02:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 100.5 |
| f5db75b0-1a24-3f20-8a2c-ce143512ed0f | -8.7033 | -45.2289 | 2026-10-06 02:30:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 45.7 |
| b500ccc4-cca3-3ca8-9e42-ecd94f5dd80c | -2.7879 | -57.6843 | 2026-10-06 02:30:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 101.2 |
| bf732f28-5399-3deb-8924-bcd9a839b685 | -3.6731 | -55.9622 | 2026-10-06 02:30:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 75.2 |
| df68bc54-7cfc-31ff-9787-c68c36783970 | -5.8323 | -45.0105 | 2026-10-06 02:30:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 90.2 |
| bf411785-3344-33e5-a2f8-3944dac2df95 | -3.0375 | -53.8865 | 2026-10-06 02:30:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 83.1 |
| 6a953a36-d601-3711-9f42-ed4ba0403d4d | -11.2611 | -45.4849 | 2026-10-06 02:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 80.9 |
| 66c11063-9bbd-3fe4-925e-8b1298965191 | -3.6915 | -55.942 | 2026-10-06 02:30:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 65.8 |
| 7b6e183a-c89a-3b83-9ebe-c5fcc694f69c | -9.0231 | -65.7169 | 2026-10-06 02:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 159.2 |
| 7aefbc50-9f11-3e96-b34e-cd21c09bbc90 | -2.9265 | -54.1305 | 2026-10-06 02:30:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 69.0 |
| 6b63b716-ce3c-3a0a-af81-f44fd2dafe5a | -2.8712 | -54.1719 | 2026-10-06 02:30:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 61.5 |
| 274c7870-26d5-357d-bf72-10126471d877 | -2.8714 | -54.1318 | 2026-10-06 02:30:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 79.2 |
| f7eb1abd-68c8-3d98-8929-836f2a2067ac | -2.7796 | -54.1138 | 2026-10-06 02:30:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 58.1 |
| 4cdd67a2-2710-33be-96e3-5378a323fc61 | -3.0932 | -53.7239 | 2026-10-06 02:30:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 96.2 |
| cb98c182-e68f-36ad-8771-de894584c5b8 | -3.0932 | -53.7441 | 2026-10-06 02:30:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 64.9 |
| 0fc41923-5652-3f3b-a3b6-1f0c36082b53 | -5.8511 | -45.0091 | 2026-10-06 02:30:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 65.0 |
| 425ba5ce-41aa-3bf3-b8b0-f876ac807ccc | -3.1115 | -53.7637 | 2026-10-06 02:30:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 76.1 |
| aebef8c6-355c-39df-b9df-e209163a7924 | -3.0 | -54.1287 | 2026-10-06 02:30:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 73.1 |
| 0ac3e762-64c1-3280-9285-4423bdfca5d7 | -8.7036 | -45.2061 | 2026-10-06 02:30:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 47.1 |
| 4b17a859-d286-3285-960e-568c0ce63db1 | -3.1116 | -53.7234 | 2026-10-06 02:30:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 52.4 |
| b827fe22-a93b-318b-9789-cc9f813fc013 | -3.6732 | -55.9425 | 2026-10-06 02:30:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 83.7 |
| eea48005-efcc-35dd-b1ea-a1b91504e453 | -2.9816 | -54.1291 | 2026-10-06 02:30:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 77.8 |
| d3b21697-db7f-3413-bd29-42492b0d198e | -9.7312 | -65.0944 | 2026-10-06 02:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 76.0 |
| 61063023-7f6f-334b-b72d-1e68f9b58651 | -11.2794 | -45.5281 | 2026-10-06 02:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 64.6 |
| ab75986b-40f1-3bb5-96e2-6d64fb0f59dc | -5.8323 | -45.0105 | 2026-10-06 02:40:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 87.2 |
| 4ab02866-739c-3922-a5c0-8908593240e8 | -2.8713 | -54.1518 | 2026-10-06 02:40:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 102.6 |
| db0e7d18-9606-3e4b-beda-377cec1aeddb | -3.1115 | -53.7637 | 2026-10-06 02:40:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 78.3 |
| c76755bc-d55b-3e14-846a-d9601ed0d231 | -3.0191 | -53.9071 | 2026-10-06 02:40:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 95.1 |
| f0ce1646-99a2-3e43-83b9-ae81524e0fec | -2.8897 | -54.1514 | 2026-10-06 02:40:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 58.5 |
| f951cbc5-b9c1-302a-a315-1a892978742d | -3.0192 | -53.887 | 2026-10-06 02:40:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 91.4 |
| 3e9001f2-f1d8-3056-91f8-f54f51b84909 | -8.7033 | -45.2289 | 2026-10-06 02:40:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 47.3 |
| e43eca13-435c-3207-afea-aa6c217353fb | -3.0375 | -53.8865 | 2026-10-06 02:40:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 75.1 |
| 53790df9-37fe-340b-ba49-2ad5a17dfb66 | -3.0375 | -53.9066 | 2026-10-06 02:40:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 76.0 |
| 38092a8f-0825-30be-81d1-1c964cc45835 | -3.6732 | -55.9425 | 2026-10-06 02:40:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 73.0 |
| bc117216-3fd3-38eb-b04c-c7522138f787 | -2.7796 | -54.0937 | 2026-10-06 02:40:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 65.8 |
| f79c8f67-35b4-3fc4-af24-78c1e3a6801d | -2.9265 | -54.1305 | 2026-10-06 02:40:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 68.6 |
| 9bc989fd-0218-34bb-9163-3e07e54d9ea9 | -3.0 | -54.1287 | 2026-10-06 02:40:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 69.7 |
| a122a1e4-0234-374d-93e8-317ed5556822 | -3.1116 | -53.7436 | 2026-10-06 02:40:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 68.2 |
| 0acec781-d2c4-3fea-abf4-4d36218895e4 | -2.8712 | -54.1719 | 2026-10-06 02:40:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 54.8 |
| 714a47e2-1798-3e83-a0e0-b53aaf01038f | -8.7036 | -45.2061 | 2026-10-06 02:40:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 46.0 |
| a7776b7a-3f40-3b93-bdd7-e6e1bc5545c5 | -2.8714 | -54.1318 | 2026-10-06 02:40:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 73.2 |
| 4887e384-474c-3bc4-a334-d6ee70ad3388 | -3.0932 | -53.7441 | 2026-10-06 02:40:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 68.2 |
| b8742650-10f0-3a6d-824a-596b1fb3e47f | -2.9449 | -54.13 | 2026-10-06 02:40:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 60.2 |
| 7523a55f-52a8-30ac-bc9f-8b12cf404a22 | -3.0932 | -53.7239 | 2026-10-06 02:40:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 93.8 |
| 3e59fe1d-2a85-3c74-b1e5-4d4314fbc986 | -2.9448 | -54.1501 | 2026-10-06 02:40:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 76.0 |
| 90180a01-555a-3ba4-ac67-b59e6e8fa30f | -3.6731 | -55.9622 | 2026-10-06 02:40:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 70.3 |
| e2575056-b572-3515-9d37-b306fe41af2d | -2.7879 | -57.6843 | 2026-10-06 02:40:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 79.0 |
| 9475b43e-de93-36e8-a584-4574e5d8c70a | -3.6915 | -55.9618 | 2026-10-06 02:40:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 84.6 |
| 914d2846-6f8f-3d00-a1e5-102106bfac59 | -2.9816 | -54.1291 | 2026-10-06 02:40:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 93.1 |
| 52e30c9e-be35-396c-85e1-08912a2f2716 | -3.1116 | -53.7234 | 2026-10-06 02:40:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 57.7 |
| 9a3c1139-026d-3768-8d2d-23d719560d77 | -9.0231 | -65.7169 | 2026-10-06 02:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 54.1 |
| b22ed465-a2e4-3aba-af32-53fe319eba14 | -5.8511 | -45.0091 | 2026-10-06 02:40:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 62.1 |
| c0adcedb-60f7-3735-8291-6edd5dac2eda | 0.4465 | -60.5442 | 2026-10-06 02:40:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 39.9 |
| 3557265a-0926-3f12-a224-42ae66007ac9 | -2.7796 | -54.1138 | 2026-10-06 02:40:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 55.5 |
| 02a543d5-9926-3664-a9a8-faee90a5db18 | -3.6915 | -55.942 | 2026-10-06 02:40:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 63.7 |
| 9d120a4a-f331-35e6-927b-d153f1f9e633 | -9.7312 | -65.0944 | 2026-10-06 02:40:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 62.7 |
| 890a63eb-a4d9-3f34-909d-3a4b5dbb1627 | -3.0932 | -53.7441 | 2026-10-06 02:50:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 65.0 |
| 9283328c-e892-33a7-8f49-1228ea6e84ff | -3.6915 | -55.942 | 2026-10-06 02:50:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 65.0 |
| b595af1e-1dfa-35a9-93bf-7288c89d46fd | -11.2802 | -45.4823 | 2026-10-06 02:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 67.9 |
| e5150f5b-70ca-3de4-b8fb-5ea199531610 | -3.0915 | -54.2469 | 2026-10-06 02:50:00 | GOES-19 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 107.6 |
| 42ae0da1-cb2b-3b79-bd33-44f6bac37f4c | -3.1116 | -53.7234 | 2026-10-06 02:50:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 52.0 |


[Clique aqui para ver as próximas entradas](README17.md)
