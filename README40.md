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

## Dados Diários - Página 40

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2eb97c72-8899-3500-b67d-8841328d11c2 | -11.70441 | -43.63131 | 2026-10-03 05:18:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| df1ff5ea-26a3-3b29-b296-27df3ed0f47c | -10.08832 | -55.1612 | 2026-10-03 05:18:00 | NPP-375D | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| d83c94a6-a68f-3b63-980b-b27bd4456932 | -10.97106 | -54.09148 | 2026-10-03 05:18:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2ae7ddd7-ce7c-3cb8-95e3-a8104053b896 | -9.16514 | -61.40763 | 2026-10-03 05:18:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 3d93ab35-0e7e-3ad0-8f9e-da57e5ba584d | -8.7044 | -66.73136 | 2026-10-03 05:18:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9e86b5c4-f042-3da9-967c-cf1e0dc8d418 | -9.69898 | -57.45127 | 2026-10-03 05:18:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 90f55dbf-3c29-3d8a-8bbf-250b197dfbc7 | -10.96811 | -54.08693 | 2026-10-03 05:18:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fe2d75ff-f6e2-3991-95d9-6e897fe94e1d | -8.69908 | -66.73272 | 2026-10-03 05:18:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f53ad2f6-c967-3aa0-9914-fb83c1192baa | -9.9543 | -55.33012 | 2026-10-03 05:18:00 | NPP-375D | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0ad40fc7-df94-3d48-a62c-62898dd723a3 | -9.72376 | -56.79559 | 2026-10-03 05:18:00 | NPP-375D | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9ef51002-1dd5-3a87-81ee-81d14d8fdaee | -8.85577 | -66.78492 | 2026-10-03 05:18:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f5508f04-e185-38fc-9e49-68ca5078b8bd | -8.3464 | -62.8369 | 2026-10-03 05:18:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4dd450ae-d595-37ae-8b45-8eba74a9ccd9 | -8.34721 | -62.83239 | 2026-10-03 05:18:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 455b2f2b-4623-3fcd-bdd2-91cbb74965ba | -9.0829 | -59.48096 | 2026-10-03 05:18:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 42ec462a-8aed-3783-b8ac-b663128717b6 | -9.16978 | -61.4049 | 2026-10-03 05:18:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8bd9cf1a-5fba-31c9-89cf-0a0602811d56 | -9.16575 | -61.40413 | 2026-10-03 05:18:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| fa4533db-eacb-3e8a-93fb-52258120358e | -9.89417 | -60.29255 | 2026-10-03 05:18:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7a905eeb-d5d6-3e4c-8d3e-7d65d00a6b97 | -8.89565 | -66.88455 | 2026-10-03 05:18:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 445544dd-9b16-3bcc-af8a-6f09ed7aec44 | -9.95823 | -55.32705 | 2026-10-03 05:18:00 | NPP-375D | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5a8139e3-64f9-3894-a7f7-cb038fc8ac25 | -9.16918 | -61.40837 | 2026-10-03 05:18:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 65f1815b-64bc-3a5d-a9c9-8db004e61772 | -9.70176 | -57.45539 | 2026-10-03 05:18:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| bf1d77a7-eb83-3d6b-9cf5-d26c9167adc4 | -9.75225 | -59.31904 | 2026-10-03 05:18:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 68a7edeb-701d-365d-8ee9-26fd6bb8bd19 | -9.89043 | -60.29192 | 2026-10-03 05:18:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7c7ca231-20f0-314d-9713-322e9b139644 | -11.20299 | -54.12873 | 2026-10-03 05:18:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 34f2345f-cc4e-3484-82c8-173b0cadcc6c | -9.95767 | -55.33066 | 2026-10-03 05:18:00 | NPP-375D | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| e1981ca8-1aa8-312e-b5e6-65030ea070b0 | -10.52707 | -57.75152 | 2026-10-03 05:18:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2aa692eb-b45a-3e0c-9629-d81e4781cf4d | -9.70234 | -57.45183 | 2026-10-03 05:18:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f9056aec-77d1-365e-bb8b-a7474bb8b620 | -8.86078 | -66.79015 | 2026-10-03 05:18:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 57f34ec0-5fb8-3cb3-a3d0-a03783b67170 | -9.37565 | -65.47171 | 2026-10-03 05:18:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 723eb1f7-bef9-37b6-a2ce-de141dee6049 | -9.17398 | -59.69505 | 2026-10-03 05:18:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5bda3536-fb14-3ef6-b039-bf68cbf6719e | -8.85499 | -66.78902 | 2026-10-03 05:18:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6eaaeb99-921a-337c-86f3-0a8c929e1ea5 | -11.7922 | -43.54026 | 2026-10-03 05:18:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 42e03a2f-5b98-3e83-987b-edea788952a2 | -11.71138 | -43.63182 | 2026-10-03 05:18:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8ea153b6-1aa1-3da9-8692-bbbe3246398d | -9.6984 | -57.45484 | 2026-10-03 05:18:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 7b1f2a2a-57c0-3fe4-845b-6d479b614b35 | -9.15613 | -65.54211 | 2026-10-03 05:18:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f40f765a-e081-3368-bf47-d09c49ec01b0 | -9.37625 | -65.46841 | 2026-10-03 05:18:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 584ce976-57e3-3706-998d-10afb3523d32 | -9.7006 | -57.46254 | 2026-10-03 05:18:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bd966fb3-ff04-3b01-a036-c385f346081d | -11.79917 | -43.54106 | 2026-10-03 05:18:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| f07f248e-e515-343f-9241-e508f69b77ca | -9.15551 | -65.54543 | 2026-10-03 05:18:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b5a2bdfa-825b-3a99-a32d-c0196c8f1f0d | -8.85421 | -66.79318 | 2026-10-03 05:18:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 34e16879-5366-3504-9d5d-27f65194c638 | -9.75158 | -59.3231 | 2026-10-03 05:18:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2f6d016e-6712-309f-867a-538459d0aa8e | -8.70362 | -66.73543 | 2026-10-03 05:18:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a9e5728e-b6f6-366a-8d3c-8aa334c1eb9f | -16.18067 | -59.43774 | 2026-10-03 05:21:00 | NPP-375D | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| eadea07f-862e-3fe3-a3b0-e4ab41ad4976 | 2.36018 | -50.75475 | 2026-10-03 05:33:00 | NOAA-20 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 19f81775-e144-3136-9540-eaf93c416965 | -2.8869 | -54.14735 | 2026-10-03 05:33:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 63f44e4c-08f0-36ba-8c22-22e97a3c1997 | -1.22172 | -54.53476 | 2026-10-03 05:33:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b2c62564-276f-3856-91ec-d6e16dc9ee53 | -3.29162 | -53.84085 | 2026-10-03 05:33:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fbad0768-d0ec-303a-ac60-e68a6219299d | -1.27483 | -54.56346 | 2026-10-03 05:33:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5ab9484f-6acd-37a7-b06a-ef5a7e686e9c | -3.88011 | -49.68776 | 2026-10-03 05:33:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 77048ea7-561f-3e7d-aab9-d6bb06fa94b6 | -2.96724 | -54.10317 | 2026-10-03 05:33:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 2a1d3a24-b43e-308a-826b-100096b46c34 | -0.35199 | -52.01367 | 2026-10-03 05:33:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 4.7 |
| dafc9dc3-4e67-3f26-9706-86644413782e | -3.24265 | -54.51551 | 2026-10-03 05:33:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 36ccd37b-ad52-361c-b407-94e1b7cd6bf7 | -1.64328 | -55.14771 | 2026-10-03 05:33:00 | NOAA-20 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fdbfa6e4-e431-32eb-a2f8-441106052d10 | 0.40116 | -60.00084 | 2026-10-03 05:33:00 | NOAA-20 | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2dba260c-238d-37aa-8788-9416fe35d0a8 | 0.39119 | -60.00238 | 2026-10-03 05:33:00 | NOAA-20 | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5d90e9b6-4e12-331b-834a-6e6816e865e2 | -2.40841 | -56.82312 | 2026-10-03 05:33:00 | NOAA-20 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ef3512bf-67fb-3cf6-95d3-c61ef3fbebcf | -3.11564 | -50.28003 | 2026-10-03 05:33:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b324e61b-c436-3dd6-83b2-8c4b12a781a8 | -2.91968 | -54.09598 | 2026-10-03 05:33:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| accafcff-9a66-327b-ab96-bbac26a1e031 | 4.80432 | -60.27279 | 2026-10-03 05:33:00 | NOAA-20 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 80067913-a9b9-39c8-9eb9-b21b50a6967f | -2.92369 | -54.1018 | 2026-10-03 05:33:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| ffb6dcfa-2601-35e4-ac80-d74998bb45bf | -3.13981 | -53.73899 | 2026-10-03 05:33:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| f1ae47db-6f6b-34c0-b921-faa13960c6e3 | -2.85981 | -49.63486 | 2026-10-03 05:33:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 358081b7-bdd9-3f21-a9d9-964d2d0a0e53 | -3.22752 | -54.3161 | 2026-10-03 05:33:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e3dd531a-c4e9-363f-978c-c60af8b30e9c | -2.8892 | -54.13241 | 2026-10-03 05:33:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 7b0b09b9-f681-30e2-90b0-d1b248e704b3 | -3.22045 | -54.31244 | 2026-10-03 05:33:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 88fb731d-6373-3b09-8a29-9138bedf3146 | 0.49964 | -60.59998 | 2026-10-03 05:33:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 613fd620-59e6-38e9-b58a-cc7ba17fa301 | -3.22282 | -54.31536 | 2026-10-03 05:33:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a514942d-3949-3e70-90f4-16a73dcdf10c | -3.09487 | -51.09902 | 2026-10-03 05:33:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3c96ee94-adf7-3ca8-82d2-508adebd14d6 | -2.88953 | -56.82527 | 2026-10-03 05:33:00 | NOAA-20 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8f3df070-3c7b-3f46-a660-fbf126f0392b | -3.18818 | -54.09845 | 2026-10-03 05:33:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 18bdc523-4f4d-33f8-8e3e-df3e8dd0426c | -3.28472 | -53.84199 | 2026-10-03 05:33:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 23902cba-95f7-3d6d-8a38-aa387a0c77f7 | -3.28594 | -53.84544 | 2026-10-03 05:33:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fc77ddb4-c82d-3443-bc35-a6920f31e685 | 2.01082 | -61.08813 | 2026-10-03 05:33:00 | NOAA-20 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 0.4 |
| e98571b8-9833-3440-8e1d-4f5433016664 | -0.59777 | -58.11734 | 2026-10-03 05:33:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 50134078-4b57-3735-8a11-dac25419c128 | -1.22102 | -54.53922 | 2026-10-03 05:33:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 678b4e3c-8978-38c3-a5bd-55a94b6c08ad | -2.33916 | -57.98708 | 2026-10-03 05:33:00 | NOAA-20 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1a6324b6-352c-3d4e-9c17-34cf2fcb9c50 | -3.70459 | -50.97702 | 2026-10-03 05:33:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e535b722-6a40-362b-bd11-c3f460465969 | -2.97065 | -53.2637 | 2026-10-03 05:33:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5aab52d9-52aa-37e6-b773-8cc9ad7968ad | 1.13464 | -59.52496 | 2026-10-03 05:33:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 08a2b8b8-1e14-3105-824a-d989e2175305 | -0.35672 | -52.01559 | 2026-10-03 05:33:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 27a956c6-442f-3266-9223-49185685e206 | -1.63895 | -55.14702 | 2026-10-03 05:33:00 | NOAA-20 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e6a764de-7f53-3fa9-b2af-a31919a06b9c | -3.17212 | -54.07523 | 2026-10-03 05:33:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 519f856f-e7f2-327f-9b6e-99a5ad4d795a | -2.96878 | -54.09299 | 2026-10-03 05:33:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b84caa0d-0838-3a91-80e3-1df7e0dd2337 | -1.25756 | -54.55635 | 2026-10-03 05:33:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9c83707d-1eb6-3fde-88bc-c6489c737b3b | -3.01776 | -53.89893 | 2026-10-03 05:33:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a52ddf1d-0ab5-3c3d-aaca-2156fb7effba | -3.28958 | -53.84276 | 2026-10-03 05:33:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 57a7826c-8a47-3aab-854d-c780243cb878 | -1.76558 | -55.027 | 2026-10-03 05:33:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7d2769da-8417-3e5b-a7f3-837ffd0501f6 | -2.88842 | -54.13745 | 2026-10-03 05:33:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 89e41097-8634-3bce-afce-6f0f01783c73 | -1.26205 | -54.55697 | 2026-10-03 05:33:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 44682f07-2292-34c1-b76a-30ff2fc85a41 | -3.29657 | -50.32684 | 2026-10-03 05:33:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3f8c863b-1c88-385d-a47b-66437be56b63 | -1.27931 | -54.56415 | 2026-10-03 05:33:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8c15ab24-0039-3768-b30f-ce5318c01a4c | -1.49806 | -55.83353 | 2026-10-03 05:33:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8da9559c-763f-3e2f-b394-e8d10ecbc076 | -3.07393 | -51.27975 | 2026-10-03 05:33:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 5ba6d759-f6f3-31c0-8800-bc16dac7756d | -3.2855 | -53.83663 | 2026-10-03 05:33:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c1c958b4-a238-372d-a808-32d6f9f269db | 1.92835 | -55.73793 | 2026-10-03 05:33:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 50567bb3-9b3d-3771-81b5-d77be5962a43 | -3.1826 | -54.10308 | 2026-10-03 05:33:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d3be608e-dbb2-3e37-bb9e-b25a6c1eed37 | -3.69802 | -50.9806 | 2026-10-03 05:33:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 77e4c415-af3b-3c40-9ab9-39701616d62e | -3.28273 | -53.83393 | 2026-10-03 05:33:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 8ee8ae6e-287b-3433-94c2-33e6b2555c55 | -3.16579 | -54.08489 | 2026-10-03 05:33:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f49de7f5-890f-3f00-8da8-c09c20f8089f | -2.92791 | -54.10192 | 2026-10-03 05:33:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |


[Clique aqui para ver as próximas entradas](README41.md)
