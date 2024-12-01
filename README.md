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
| 45f12c5e-b762-3f56-856b-51414e0a1860 | -2.7687 | -51.7548 | 2024-12-01 00:00:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 60.1 |
| 2fb6f6e3-3f64-3092-bd9c-1b49b61c3e19 | -3.2775 | -53.6181 | 2024-12-01 00:00:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 83.0 |
| 63d7ae3e-18b2-3662-a748-3683c9421f24 | -4.8897 | -41.3385 | 2024-12-01 00:00:00 | GOES-16 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 70.5 |
| 1f8785d9-6fac-3f12-8017-349eeff162c6 | -4.5562 | -43.3028 | 2024-12-01 00:00:00 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 268.5 |
| a254fa3d-dde5-31dc-8b89-3c65b965e400 | -3.457 | -50.2572 | 2024-12-01 00:00:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 73.6 |
| fc36f03d-7628-34b2-a389-ea74134705a8 | 1.1622 | -55.9672 | 2024-12-01 00:00:00 | GOES-16 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 56.6 |
| 20866c28-4d09-3feb-a690-ed66bd4a620e | 1.1439 | -55.9871 | 2024-12-01 00:00:00 | GOES-16 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 86.9 |
| 4d33301f-d89d-3f9e-a695-35b2afefaa1c | -4.5578 | -45.7232 | 2024-12-01 00:00:00 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 218.6 |
| c06c08d0-18c3-30f3-86f9-4ef03ece52bb | -3.0081 | -51.7897 | 2024-12-01 00:00:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 69.7 |
| e1a81f71-daf9-34e7-8c3c-a2b93b7a7a77 | -6.9158 | -43.5185 | 2024-12-01 00:00:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 69.2 |
| f4062381-e870-3beb-8d6d-0b3531746d0a | -3.0896 | -45.4999 | 2024-12-01 00:00:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 51.3 |
| 1c4c70fe-76a2-3078-bd17-b123373272c7 | -3.2058 | -53.1138 | 2024-12-01 00:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 82.5 |
| f292a5bf-7295-32f3-9b6e-e71bd316142b | -2.8013 | -53.043 | 2024-12-01 00:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 64.7 |
| a21e69a8-500f-3afa-ba28-849d7d4b7bb9 | -4.556 | -43.3261 | 2024-12-01 00:00:00 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 77.4 |
| 33b6d325-5ced-306a-aef2-c53832531561 | -2.1535 | -54.8659 | 2024-12-01 00:00:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 174.4 |
| 6f975c49-1086-3889-99f1-a5120211207d | 1.1621 | -56.0066 | 2024-12-01 00:00:00 | GOES-16 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 53.6 |
| 85c57dcd-c588-3afd-ad42-99b57b49c93d | -6.9346 | -43.5168 | 2024-12-01 00:00:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 63.0 |
| fee09234-34e2-35b0-aa01-259f9661a15d | -2.1351 | -54.8861 | 2024-12-01 00:00:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 110.7 |
| 6eaf74f3-272a-35e9-b60d-1e5a27f1e8ae | -3.69 | -51.8101 | 2024-12-01 00:00:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 106.3 |
| 0cac0053-12a9-392d-96db-a26204aaab88 | -4.5395 | -45.6794 | 2024-12-01 00:00:00 | GOES-16 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 79.6 |
| 4916a39d-584e-3b26-a25e-73cb61b7e435 | -4.9087 | -41.313 | 2024-12-01 00:00:00 | GOES-16 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 129.7 |
| 718346db-2e5e-38a6-bfc9-56893981abf6 | -3.259 | -53.6388 | 2024-12-01 00:00:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 197.6 |
| e942dc26-dde6-3807-b496-fa86d03f59a4 | -4.8899 | -41.3143 | 2024-12-01 00:00:00 | GOES-16 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 140.9 |
| b292e3b5-9b14-3d91-9899-f67ca85a294d | -3.1273 | -54.5264 | 2024-12-01 00:00:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 87.6 |
| d78e514d-56ef-3cf5-8b63-241c0b9c0589 | -3.4754 | -50.2776 | 2024-12-01 00:00:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 191.9 |
| 52601a5c-d90e-342a-9ba7-770e52073e1c | -3.2774 | -53.6383 | 2024-12-01 00:00:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 156.7 |
| c2271c1d-a0d0-3bcc-8c11-489ec87456a4 | -3.3134 | -53.8592 | 2024-12-01 00:00:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 74.3 |
| c86071a2-29dd-30cb-844d-3fd2246eb4aa | -3.2057 | -53.1341 | 2024-12-01 00:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 94.1 |
| 5b032b85-c2f3-386c-a457-238b84a72d60 | -4.558 | -45.7008 | 2024-12-01 00:00:00 | GOES-16 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 108.0 |
| 52593359-752f-321a-b8a9-4cfe3aeae775 | -6.9344 | -43.5401 | 2024-12-01 00:00:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 292.7 |
| aee324f6-bc3d-30bd-babe-08f34271aa38 | -2.8196 | -53.0629 | 2024-12-01 00:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 79.2 |
| cbbab945-0f94-3e11-b699-b8d00bc2bf78 | -3.4974 | -53.8339 | 2024-12-01 00:00:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 106.0 |
| 99919ef7-f37f-3da9-92f0-c2fb1a05b654 | -10.6674 | -44.4835 | 2024-12-01 00:00:00 | GOES-16 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 78.9 |
| 8c4df83e-f2d8-3010-9cc2-6a78c8962609 | -3.4755 | -50.2566 | 2024-12-01 00:00:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 143.6 |
| 7982c762-f1be-3ba8-ab40-ac0a014888a5 | -2.849 | -49.8974 | 2024-12-01 00:00:00 | GOES-16 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 73.3 |
| 0542324e-baf8-31f7-bb02-978f57cf3a83 | -3.0895 | -45.5223 | 2024-12-01 00:00:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 78.0 |
| 7bb89665-50ba-34c9-8296-422e47d6545c | -4.5765 | -45.7222 | 2024-12-01 00:00:00 | GOES-16 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 44.2 |
| 62a0aa01-d8a0-320a-94cc-8eab2a0e71b3 | -4.5392 | -45.7243 | 2024-12-01 00:00:00 | GOES-16 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 83.0 |
| 96432d68-8773-3a59-ac4a-97d4e590478f | -4.5563 | -43.2795 | 2024-12-01 00:00:00 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 102.5 |
| 8f42c066-bcd6-364e-9f4f-76116d81b547 | -3.2591 | -53.6186 | 2024-12-01 00:00:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 128.7 |
| 873a64e0-86d5-32ca-8c52-d7228f7d2665 | -2.8197 | -53.0425 | 2024-12-01 00:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 87.0 |
| d5134020-21e2-3c98-8c30-3d9955e66942 | -2.6578 | -51.8811 | 2024-12-01 00:00:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 94.0 |
| ee3236f9-cc6d-36bd-8f5c-e2d3466cf5dd | -3.6899 | -51.8307 | 2024-12-01 00:00:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 70.8 |
| 26f50fa7-dc09-38c4-a650-36cc1a4918a5 | -6.9156 | -43.5418 | 2024-12-01 00:00:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 277.4 |
| ababdf1b-8a46-3dd6-8f5a-022dd5651484 | -4.5394 | -45.7019 | 2024-12-01 00:00:00 | GOES-16 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 189.4 |
| 6cdad6f5-ba68-3c4d-bb15-7988b25093e9 | -2.6579 | -51.8606 | 2024-12-01 00:00:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 71.0 |
| 8e6e2be0-18c7-3c9b-bdc9-a26dc1b17915 | -6.9341 | -43.5634 | 2024-12-01 00:00:00 | GOES-16 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 136.9 |
| 3d491898-d443-396c-b386-12a970068a5c | -10.6483 | -44.4861 | 2024-12-01 00:00:00 | GOES-16 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 64.0 |
| 22301166-1488-3180-9f45-93c5eff880f5 | -2.7503 | -51.7553 | 2024-12-01 00:00:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 124.6 |
| 1836a8aa-1008-357a-afad-4ec27215fe80 | -3.4569 | -50.2782 | 2024-12-01 00:00:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 91.6 |
| f4dd5c66-03a7-3fe8-b9da-2663166d0b48 | -3.5158 | -53.8333 | 2024-12-01 00:00:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 78.2 |
| 78176c18-6aff-31c7-827d-d97f548b8098 | -2.1535 | -54.8858 | 2024-12-01 00:00:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 238.1 |
| a26d4181-3329-3e12-be36-117fe044d2bc | 1.1622 | -55.9869 | 2024-12-01 00:00:00 | GOES-16 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 107.2 |
| 35604d18-be41-3326-95b3-fc7b6e27f925 | -2.1352 | -54.8662 | 2024-12-01 00:00:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 91.3 |
| a52be41f-0a74-35ba-a134-c5febd5e323a | -2.8491 | -49.8763 | 2024-12-01 00:00:00 | GOES-16 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 97.5 |
| 98367398-045b-33ac-b641-e1b3f4fbfac3 | -3.1456 | -54.5259 | 2024-12-01 00:00:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 82.7 |
| 0cab44af-36cc-35a5-8872-c7d67f341f70 | -6.9153 | -43.5652 | 2024-12-01 00:00:00 | GOES-16 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 88.5 |
| a2b31671-5f9b-36fe-8dcf-f9b6f5ed79ea | -6.9 | -43.56 | 2024-12-01 00:00:00 | MSG-03 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 495dcb59-bb2b-35ed-a060-8ccae8d7c29d | -3.2 | -45.77 | 2024-12-01 00:00:00 | MSG-03 | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 491f570e-827f-31c2-a557-e500846a2d34 | -4.52 | -45.7 | 2024-12-01 00:00:00 | MSG-03 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 8faef1a5-0cf0-342e-9d1e-0c3e75e6b638 | -4.55 | -45.7 | 2024-12-01 00:00:00 | MSG-03 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 3e2dc3fc-84ba-313c-b1ec-3fb0ba68ad5e | -3.22 | -45.78 | 2024-12-01 00:00:00 | MSG-03 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| fab4cb58-d010-38a5-b250-dca6dceac620 | -6.9 | -43.51 | 2024-12-01 00:00:00 | MSG-03 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| b73718c9-8960-35f4-81ec-1c475ee50dd8 | -3.22 | -45.73 | 2024-12-01 00:00:00 | MSG-03 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| e6925a2c-5460-31ad-9ac0-5ba8181cec90 | -6.92 | -43.52 | 2024-12-01 00:00:00 | MSG-03 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 27699166-d714-3aea-bd99-525260572b42 | -4.88 | -41.32 | 2024-12-01 00:00:00 | MSG-03 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 7ff00471-54db-33fd-9ed2-3e605c5fb08a | -6.93 | -43.56 | 2024-12-01 00:00:00 | MSG-03 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 16f03377-4d09-3e5d-950b-7a80bae07fea | -3.4754 | -50.2776 | 2024-12-01 00:10:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 177.2 |
| 39aff89b-7b68-32ae-a4fe-38d768a8a147 | -4.556 | -43.3261 | 2024-12-01 00:10:00 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 66.8 |
| 12a9dd14-203e-37ef-b1c5-b1bfcabbaab3 | -3.259 | -53.6388 | 2024-12-01 00:10:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 182.3 |
| ac541ddc-a218-3e76-b61c-917f6316dc67 | -2.1535 | -54.8858 | 2024-12-01 00:10:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 303.7 |
| 35361eb1-7dea-308e-90b2-24b915889bac | -3.0081 | -51.7897 | 2024-12-01 00:10:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 72.5 |
| 28eaadff-b8b8-323e-b46b-deb2be640212 | -10.6674 | -44.4835 | 2024-12-01 00:10:00 | GOES-16 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 81.5 |
| 41906027-682c-362f-ba13-0a4c3ccb02ad | -3.3134 | -53.8592 | 2024-12-01 00:10:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 71.6 |
| 115aefce-6a59-371e-a6dc-9852faafaaa4 | -2.6579 | -51.8606 | 2024-12-01 00:10:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 74.9 |
| d729d097-3e0c-3ba9-91e6-002d246effd5 | -4.5392 | -45.7243 | 2024-12-01 00:10:00 | GOES-16 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 84.2 |
| 4ac4ab9b-895e-3aa6-bab4-20406246280a | -2.1535 | -54.8659 | 2024-12-01 00:10:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 314.5 |
| 2bb2208e-ec0e-3841-ba27-0493976a735c | -3.2591 | -53.6186 | 2024-12-01 00:10:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 125.9 |
| ca676e13-2672-343b-98a5-b8c2e5d85b22 | -4.5563 | -43.2795 | 2024-12-01 00:10:00 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 89.2 |
| fceb24ae-4f48-3b17-97ae-946c243dde19 | -3.1273 | -54.5264 | 2024-12-01 00:10:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 103.9 |
| e8466abe-3b9d-3537-b765-409e120b9c45 | -2.7503 | -51.7553 | 2024-12-01 00:10:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 108.1 |
| bc286f3e-1f91-3f6d-b7b5-871ad0c6060a | -3.457 | -50.2572 | 2024-12-01 00:10:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 82.8 |
| 8daaefb8-0dd7-3a42-ae1d-b589adf37f8d | -4.5395 | -45.6794 | 2024-12-01 00:10:00 | GOES-16 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 67.2 |
| b7c864dc-d471-37ab-8f61-56a305c75ce0 | -3.5158 | -53.8333 | 2024-12-01 00:10:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 74.5 |
| 9e2a47b9-296d-3181-9004-453190d781fa | -3.2774 | -53.6383 | 2024-12-01 00:10:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 140.7 |
| 7c4662c7-0807-39e7-9680-8231db262063 | -4.5394 | -45.7019 | 2024-12-01 00:10:00 | GOES-16 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 198.0 |
| 8e552608-6f58-3745-8439-521b06cc2977 | -3.1114 | -53.8041 | 2024-12-01 00:10:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 69.8 |
| d99bc39e-39bd-3ea8-a230-b9c80e48bd6e | -6.9153 | -43.5652 | 2024-12-01 00:10:00 | GOES-16 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 89.7 |
| 849ec015-7809-3386-b3e5-e1daee56413e | -4.558 | -45.7008 | 2024-12-01 00:10:00 | GOES-16 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 96.9 |
| 641ca4ec-b662-379c-8b39-3beaa1821156 | -2.6578 | -51.8811 | 2024-12-01 00:10:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 101.1 |
| 252fb9ea-e0aa-3df2-a029-2569ebeab59a | -4.5578 | -45.7232 | 2024-12-01 00:10:00 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 226.8 |
| ba61a1c5-4b41-38bc-bfb9-96b32df138ce | -2.8196 | -53.0629 | 2024-12-01 00:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 67.6 |
| 3f0e60ae-b099-379f-ac2e-5e61b6a64356 | -3.2369 | -45.7853 | 2024-12-01 00:10:00 | GOES-16 | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 68.6 |
| 8576a4d8-4d35-349a-b562-5e954febc00c | -3.4755 | -50.2566 | 2024-12-01 00:10:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 129.1 |
| bc51020d-38c8-3cd1-af43-d2a6c79dc8a5 | -2.8491 | -49.8763 | 2024-12-01 00:10:00 | GOES-16 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 78.0 |
| 78fa575c-7268-3be8-9c41-a089386ef727 | -4.5577 | -45.7457 | 2024-12-01 00:10:00 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 42.9 |
| 9c373cf0-219e-39a3-970c-7f3f4d539c1d | -2.8013 | -53.043 | 2024-12-01 00:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 63.4 |
| 7a631368-c2f1-31d8-86bf-2c5c50adef6f | -6.9158 | -43.5185 | 2024-12-01 00:10:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 68.8 |
| 3025edf7-1090-3a1c-a03a-11aeb0ed7c79 | -6.9156 | -43.5418 | 2024-12-01 00:10:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 266.7 |
| 16c646ab-301f-3885-aa14-0e1f617b9d8e | -2.1351 | -54.8861 | 2024-12-01 00:10:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 134.9 |


[Clique aqui para ver as próximas entradas](README2.md)
