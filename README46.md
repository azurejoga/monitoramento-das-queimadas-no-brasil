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

## Dados Diários - Página 46

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| aab1ff29-2cd2-32e6-b35c-86f40cd34531 | -4.79918 | -42.74771 | 2026-10-07 04:19:00 | NOAA-20 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8d384ac9-f670-3efb-b9d5-7ce93d8b8a54 | -4.3624 | -43.91185 | 2026-10-07 04:19:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 42d1c14c-08c7-3092-884a-e3bd0fbe4fa6 | -6.03078 | -42.2798 | 2026-10-07 04:19:00 | NOAA-20 | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| aca55805-afda-345b-bffb-746bb5d03032 | -3.03477 | -53.92802 | 2026-10-07 04:19:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b514918b-ccb9-3063-b626-2c2239c9c551 | -2.77275 | -54.11295 | 2026-10-07 04:19:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 10.7 |
| bb8f7a20-144b-34fc-a492-d19524d508f3 | -3.50693 | -54.67124 | 2026-10-07 04:19:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 8e88840f-368f-3e74-931b-6b3f6cfee09f | -3.53788 | -54.64436 | 2026-10-07 04:19:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 3f3888f4-315c-301c-bff6-b0ba9e20af7f | -2.77066 | -54.08659 | 2026-10-07 04:19:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 12.6 |
| 0dce4c0a-c362-337f-b8cc-ce58b697135d | -5.37667 | -44.15993 | 2026-10-07 04:19:00 | NOAA-20 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6830fa7d-3939-32c0-88e5-e4a95f87a43f | -3.05116 | -54.1554 | 2026-10-07 04:19:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| db652afb-b3a9-33aa-9757-1d468fa3656f | -3.08506 | -54.29555 | 2026-10-07 04:19:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| dc6d160a-d319-32cf-ad6d-54400061d867 | -3.29307 | -54.03351 | 2026-10-07 04:19:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 10.5 |
| a71ab98f-5e6e-3127-b52f-2a0d9e9c393a | -2.79983 | -54.0881 | 2026-10-07 04:19:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 20ef0796-b2a1-3433-b350-367fcd9f2288 | -7.86393 | -44.15873 | 2026-10-07 04:19:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 48b35b2e-240b-3cb7-859f-79271f1267e8 | -5.29066 | -42.7546 | 2026-10-07 04:19:00 | NOAA-20 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 7e8c04c4-ae8e-3e48-ad02-9b479b9327e9 | -2.76731 | -54.10682 | 2026-10-07 04:19:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 32.8 |
| f62e6170-6a39-3a76-b7c6-8e497b547b97 | -5.97819 | -40.94894 | 2026-10-07 04:19:00 | NOAA-20 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 10.3 |
| a87abf95-a919-3336-9dc2-58fb2b6a2994 | -5.67851 | -47.93481 | 2026-10-07 04:19:00 | NOAA-20 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 07f2e22d-643a-31ce-83b4-9797f7d04d7a | -4.82448 | -38.68691 | 2026-10-07 04:19:00 | NOAA-20 | IBARETAMA | CEARÁ | Brasil | 2305266 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| edced874-af95-3b31-b3de-0c565818296f | -4.04474 | -50.9863 | 2026-10-07 04:19:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 0fbfcef7-7c4b-3df8-b823-0ea8ec608ca8 | -3.28046 | -54.07805 | 2026-10-07 04:19:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 10dc7c73-e4da-3289-a6d1-ccc72ca09301 | -3.06749 | -54.15006 | 2026-10-07 04:19:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 87409574-ca46-315d-a259-f6c439b80d00 | -4.13319 | -54.90908 | 2026-10-07 04:19:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 2a940d44-7ae5-373c-ac4f-332b4f66ca24 | -3.05667 | -54.21466 | 2026-10-07 04:19:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 825ae394-a4e5-324e-8743-e35d64516569 | -5.4447 | -44.55455 | 2026-10-07 04:19:00 | NOAA-20 | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9831fff1-4d28-30fc-8515-7aeabb5cd32b | -3.11284 | -53.76631 | 2026-10-07 04:19:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| bf3486b1-5cf9-36d5-b114-f1ef27585bd9 | -3.0529 | -54.14552 | 2026-10-07 04:19:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ef3992f6-6f47-3509-838b-b14006c11ad0 | -6.91572 | -47.65765 | 2026-10-07 04:19:00 | NOAA-20 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7c902855-fae1-3b14-97d7-9d5517a3a74a | -7.09333 | -45.5729 | 2026-10-07 04:19:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 459d284d-6c83-355f-a5d0-1cb255115668 | -3.53336 | -54.63898 | 2026-10-07 04:19:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 2c95060b-4e82-333d-9a39-e8e03998bc0c | -5.75906 | -45.29618 | 2026-10-07 04:19:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 62113709-3d03-3b67-91ee-be6190dd3175 | -3.73795 | -51.22355 | 2026-10-07 04:19:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 18eb48af-ab28-30ab-987b-64e3828373c7 | -1.25436 | -49.05677 | 2026-10-07 04:19:00 | NOAA-20 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 54de800f-6f08-3a67-b74e-1d4fe7f1361d | -3.53153 | -54.64939 | 2026-10-07 04:19:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| d57add7d-c7ef-302b-8f25-abee28a58217 | -3.52605 | -54.63634 | 2026-10-07 04:19:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 9438c45f-22f7-33c6-bb50-4e1db13e9a64 | -6.94743 | -41.49535 | 2026-10-07 04:19:00 | NOAA-20 | SANTANA DO PIAUÍ | PIAUÍ | Brasil | 2209351 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 79c9b8c4-6ade-3661-adaa-def9df5e8649 | -5.72417 | -41.67998 | 2026-10-07 04:19:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 2acbb330-924a-3ad1-ab08-f0a9867ee63a | -7.60527 | -42.37607 | 2026-10-07 04:19:00 | NOAA-20 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| e1ac83de-5b87-38ff-8bd8-7ea3dc516095 | -5.6745 | -53.49005 | 2026-10-07 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 7c714f25-d6ae-313b-a394-ab8204658fe2 | -6.21164 | -52.83281 | 2026-10-07 04:19:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9280c7ce-a7b2-3118-95b5-7e3fc3afec10 | -3.50849 | -51.6893 | 2026-10-07 04:19:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5155a1e1-57b7-3fb9-a775-8095dd1e61c2 | -4.03977 | -50.98524 | 2026-10-07 04:19:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3b1bd5a7-a8b4-3ffe-b9ec-255052e735a8 | -3.67791 | -55.95121 | 2026-10-07 04:19:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| fb953328-55b7-3016-a235-a051996790be | -4.75474 | -43.26348 | 2026-10-07 04:19:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5c1eb9f1-4d0d-32c2-a736-0727e2569e11 | -2.77675 | -54.10991 | 2026-10-07 04:19:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e49aac4f-a732-3fa8-92a8-fe81fd8806e4 | -3.10141 | -53.75956 | 2026-10-07 04:19:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 9f8ed31c-7dc8-3b73-a198-093d2497e95b | -3.50962 | -51.6827 | 2026-10-07 04:19:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| df416bd2-c9f8-3d79-88c6-3a630afcd5f4 | -4.45306 | -47.92505 | 2026-10-07 04:19:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 18.8 |
| 81c4a964-986d-37ac-b42c-13d446f0141a | -4.1842 | -51.1347 | 2026-10-07 04:19:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e7d2c4c9-263e-3523-9112-eb4505346427 | -3.8019 | -51.99095 | 2026-10-07 04:19:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2173f21b-0831-3855-8ed5-709b27bab405 | -3.05048 | -54.27017 | 2026-10-07 04:19:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 46fd45e2-6394-3e49-ad1f-91af7da5bddc | -5.74882 | -43.27308 | 2026-10-07 04:19:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 2bb934bb-d39d-367c-bcfc-1d593291d11a | -3.0805 | -54.28429 | 2026-10-07 04:19:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| cbb27ddc-7927-32fc-b297-b222b2a7ffe7 | -7.87284 | -49.05622 | 2026-10-07 04:19:00 | NOAA-20 | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 2.8 |
| cff56eba-727b-3d8b-8511-ad640c37c4ee | -3.07275 | -54.17952 | 2026-10-07 04:19:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 9f902c56-5705-3838-97b5-3ea0c0ac3ecd | -5.96459 | -41.35113 | 2026-10-07 04:19:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 089c9485-7ec2-32e4-95ad-1a6000959c2f | -3.16097 | -50.44032 | 2026-10-07 04:19:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 9e831491-f4d8-30b5-802c-081992690245 | -3.35814 | -50.47954 | 2026-10-07 04:19:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7a252e65-616f-332a-9b50-b82734bfe524 | -3.05952 | -54.21836 | 2026-10-07 04:19:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 9b21bbcd-db7f-37c6-b9fa-37f86b21b417 | -4.35676 | -47.77904 | 2026-10-07 04:19:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 7416940b-539f-3d95-91f1-f1fc9c266e3d | -3.527 | -54.63762 | 2026-10-07 04:19:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 08763728-7e8b-31c1-ad93-06610a1a86cd | -6.2076 | -52.69429 | 2026-10-07 04:19:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f2a50db7-78ea-31ca-8c3f-7c8238c189a0 | -4.91891 | -55.87268 | 2026-10-07 04:19:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 7d21e418-b10c-32c4-b73a-8195b5de85a7 | -5.2368 | -50.90851 | 2026-10-07 04:19:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2b3113a8-6fe1-3699-bc9d-940e8615ee5d | -3.5216 | -54.66262 | 2026-10-07 04:19:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 1a4e86a5-bbd4-3e69-8300-0e82216b5593 | -5.69219 | -40.89095 | 2026-10-07 04:19:00 | NOAA-20 | NOVO ORIENTE | CEARÁ | Brasil | 2309409 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 07954e78-b8dd-3096-8c42-e2ec666b6f59 | -7.87218 | -44.2137 | 2026-10-07 04:19:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 5.8 |
| a8680f26-be90-34a6-a7ee-a7dcc90517e6 | -5.83038 | -47.40222 | 2026-10-07 04:19:00 | NOAA-20 | RIBAMAR FIQUENE | MARANHÃO | Brasil | 2109551 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 38286e79-a57d-364e-b535-ee7cbf2fbf87 | -6.33269 | -43.83105 | 2026-10-07 04:19:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| f8c72555-62ab-3c19-99bc-d0461170f3e5 | -3.07415 | -54.28346 | 2026-10-07 04:19:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| af7beba2-761f-37a8-b835-302a3f99a53c | -3.13146 | -54.36713 | 2026-10-07 04:19:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 34ddbc94-bc94-3d6a-8fe9-54021f0f954a | -3.29536 | -54.06544 | 2026-10-07 04:19:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| d9e52cad-e29d-382e-8270-dd5204254af3 | -3.23037 | -53.89179 | 2026-10-07 04:19:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 92dbcd37-6b13-31cd-b2b5-447da190103d | -5.83336 | -45.01271 | 2026-10-07 04:19:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| e299b928-de74-3086-998e-1d3c70a68ab4 | -1.20078 | -49.04115 | 2026-10-07 04:19:00 | NOAA-20 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d489c55e-ab8e-3fe6-93f8-070d6e333ae9 | -2.49973 | -48.13862 | 2026-10-07 04:19:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| f2e6bac4-a5cc-366a-a563-0a566ab56fa1 | -3.50036 | -54.63237 | 2026-10-07 04:19:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| e6f78885-286f-3045-842e-226babc3144c | -2.99047 | -54.1109 | 2026-10-07 04:19:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 3276c08d-1207-3034-9f17-474483ea3797 | -2.76648 | -54.11182 | 2026-10-07 04:19:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 33.1 |
| 7fe9de70-606c-3a0c-9f80-8c762e7ce396 | -3.02039 | -53.90088 | 2026-10-07 04:19:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 3f0b23e6-6199-3bda-9d31-f8f119d6fdcc | -2.98668 | -51.04737 | 2026-10-07 04:19:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| cf17e94f-0643-32c8-a7e6-138a9472042a | -3.10035 | -54.16914 | 2026-10-07 04:19:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| b8436e44-b48f-319c-a5c2-0e8ae9e63167 | -2.95492 | -51.04827 | 2026-10-07 04:19:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 852f65e8-5c0d-3a64-a9e4-1aa5fab7da2b | -3.58381 | -54.31513 | 2026-10-07 04:19:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 4f159dbf-90e0-3e93-823f-67812ed9a1b7 | -3.29223 | -54.0383 | 2026-10-07 04:19:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 10.5 |
| de30c6e3-03c7-3156-b828-93db814b35bc | -2.95528 | -54.14453 | 2026-10-07 04:19:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9c6e148a-0acb-3422-ab73-996d0fa205c0 | -7.74675 | -49.20709 | 2026-10-07 04:19:00 | NOAA-20 | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 3.3 |
| d3a4a514-eece-3011-b0d0-4777bca9aac7 | -3.21268 | -53.88424 | 2026-10-07 04:19:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6a8b4c2f-c626-397b-a925-a0202df9b877 | -3.26552 | -50.40243 | 2026-10-07 04:19:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 80a728c5-3572-3a46-9e0b-fdbce740d692 | -4.32039 | -43.81523 | 2026-10-07 04:19:00 | NOAA-20 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ea573b00-4319-3d79-983b-3a41de448a93 | -3.5447 | -50.09137 | 2026-10-07 04:19:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 1a7d584f-da45-33eb-b233-52c3b68c4f58 | -3.28916 | -54.06435 | 2026-10-07 04:19:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| a71f5f7e-6d1a-3d17-8ce0-13ef55144ae7 | -3.51595 | -54.6628 | 2026-10-07 04:19:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| dd2c6c91-25fd-3069-9fde-725be959135a | -6.79817 | -42.27975 | 2026-10-07 04:19:00 | NOAA-20 | SANTA ROSA DO PIAUÍ | PIAUÍ | Brasil | 2209377 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| d5aa3c8c-6425-3dc1-a258-99fb93d91cb2 | -2.77358 | -54.10793 | 2026-10-07 04:19:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 16.8 |
| 51cca568-77e4-35a9-9310-1b232e5c9e0a | -6.21064 | -42.51925 | 2026-10-07 04:19:00 | NOAA-20 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 420a4c00-87e4-3fd4-9e91-707e7e10c6a6 | -3.10429 | -53.77977 | 2026-10-07 04:19:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| f870c178-d3b2-3087-90ce-7bd7bf8c9798 | -5.6916 | -40.89483 | 2026-10-07 04:19:00 | NOAA-20 | NOVO ORIENTE | CEARÁ | Brasil | 2309409 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 1582fa54-3ceb-300c-ba3c-4f8b461e1cb3 | -5.7236 | -41.66151 | 2026-10-07 04:19:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 97b08406-021f-35dd-bf38-dba6f7d2786f | -3.26369 | -50.41314 | 2026-10-07 04:19:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |


[Clique aqui para ver as próximas entradas](README47.md)
