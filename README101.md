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

## Dados Diários - Página 101

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0bbb98bd-379f-3997-a839-0be88c960f67 | -17.81736 | -57.51046 | 2024-10-26 05:40:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 2a6c5781-6550-369e-a140-93a3909a4cc6 | -17.81529 | -57.52932 | 2024-10-26 05:40:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 9f938eed-361b-3abb-b595-867688dce4b3 | -17.8119 | -57.51294 | 2024-10-26 05:40:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.4 |
| e6d9de6b-2784-38c4-9c25-32af8fe7da32 | -17.81156 | -57.51608 | 2024-10-26 05:40:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 7.7 |
| 068f0d67-6707-371e-bc07-90aa9019e3cd | -17.81019 | -57.52867 | 2024-10-26 05:40:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| c286f36a-6ee8-37d5-abb6-19431ecf2140 | -17.79793 | -57.59345 | 2024-10-26 05:40:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| ad56070c-a72c-37ee-881f-50e4274a5acf | -17.79251 | -57.5959 | 2024-10-26 05:40:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 8.6 |
| 9ae9f875-202e-3e78-80b1-3194e034bf5c | -16.09599 | -60.12368 | 2024-10-26 05:40:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| cc0bba4e-f3b9-31a0-a181-cfcfe099d359 | -16.09548 | -60.12765 | 2024-10-26 05:40:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 11674c22-0352-3056-acde-156c670029bc | -16.0923 | -60.11909 | 2024-10-26 05:40:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6933076f-014f-3416-bc91-1f8c5b0f456d | -16.09179 | -60.12307 | 2024-10-26 05:40:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a5cd0701-3359-34d0-a35c-2867d728c33e | -16.0881 | -60.11847 | 2024-10-26 05:40:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7830edfc-2a41-3c88-9d62-e72d0edc0a91 | -15.69162 | -59.74481 | 2024-10-26 05:40:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 903a7b62-25e4-3167-8770-edf98efeab11 | -15.68735 | -59.74421 | 2024-10-26 05:40:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| dbdce773-39a7-3814-b564-0792228c86e8 | -15.67175 | -59.73987 | 2024-10-26 05:40:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b804436f-3c69-3bb5-ae21-b4b7d0a076ee | -15.67121 | -59.74401 | 2024-10-26 05:40:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8557f845-f890-3281-980c-67213d2f5cbd | -15.66851 | -59.76466 | 2024-10-26 05:40:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3334561d-3de7-3453-806a-f1c1dba2c609 | -2.9945 | -50.4816 | 2024-10-26 05:45:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 52.7 |
| 9c286ab3-becc-3014-9f33-50ba1c53213e | -2.9501 | -52.5708 | 2024-10-26 05:45:22 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 48.7 |
| 9ef3762b-441f-3008-9d3e-6889045876cf | -3.013 | -50.481 | 2024-10-26 05:45:23 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 76.0 |
| 640373bd-13d3-3577-8b17-e0212d4700d2 | -3.473 | -43.3144 | 2024-10-26 05:45:25 | GOES-16 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 72.2 |
| 3c231878-037d-3e83-ab98-5ab79c75c2ef | -3.4729 | -43.3377 | 2024-10-26 05:45:25 | GOES-16 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 94.2 |
| 93335610-7133-32a5-9d20-b2095e1dfeed | -4.5614 | -48.0141 | 2024-10-26 05:45:31 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 74.9 |
| fc743a5a-a444-37f0-8a85-0b55cd7ee378 | -4.5613 | -48.0358 | 2024-10-26 05:45:31 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 68.8 |
| 40f0cb99-8130-3883-9f45-5371f4dd0549 | -4.58 | -48.0132 | 2024-10-26 05:45:31 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 154.7 |
| d7e9ea8d-9f1e-3df0-976a-f00618d63ef5 | -4.5799 | -48.0349 | 2024-10-26 05:45:31 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 140.8 |
| 86c82fc9-aa16-3c0a-bed0-492c7d54c2cb | -3.013 | -50.481 | 2024-10-26 05:55:23 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 65.4 |
| 8059043d-80c0-3767-ad2f-25d69500cddb | 4.33874 | -60.21317 | 2024-10-26 05:57:00 | NPP-375D | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 97a0905b-41f8-33e3-9418-5239478244eb | 4.33547 | -60.22253 | 2024-10-26 05:57:00 | NPP-375D | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a2ffd4be-2611-3dbd-af4c-c141207b3cfe | 1.56762 | -55.63875 | 2024-10-26 05:57:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6c25e232-7b08-32b6-a232-a3be6249c103 | 1.56097 | -55.63987 | 2024-10-26 05:57:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c2eacf2f-2827-3a83-91e5-a5283a19dbcc | -3.63145 | -55.50879 | 2024-10-26 05:57:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| f362b116-e5b9-3edc-8d1a-2190bc1b46ec | -3.63042 | -55.51592 | 2024-10-26 05:57:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 3e546d33-09c8-32c6-8f4f-acf02d92b957 | -1.38411 | -55.83942 | 2024-10-26 05:57:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7fd9ac03-0c47-3fb8-af7a-c08b96fae920 | -1.38314 | -55.84566 | 2024-10-26 05:57:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5bb6b021-f041-3165-a246-f92abf227128 | -7.39185 | -72.6541 | 2024-10-26 05:59:00 | NPP-375D | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 19b4c729-edd1-39fb-93c2-16fc2a3bdab7 | -7.38834 | -72.65353 | 2024-10-26 05:59:00 | NPP-375D | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 29798983-eee0-365e-8b48-4c4853fb2f26 | -7.36326 | -72.85189 | 2024-10-26 05:59:00 | NPP-375D | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 274b00fb-0e7e-3bda-8639-173f8a749286 | -7.33926 | -72.79901 | 2024-10-26 05:59:00 | NPP-375D | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3e2c1447-5708-3e77-8fb3-5ee235195a2f | -7.33861 | -72.80296 | 2024-10-26 05:59:00 | NPP-375D | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3589cb39-6538-343b-8aa9-2354f82bd0b0 | -7.03911 | -63.11296 | 2024-10-26 05:59:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cd8f768f-84a6-3d10-af55-7b404d8a5e5a | -7.03842 | -63.11774 | 2024-10-26 05:59:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 77a07615-bf94-361e-8589-5d045ca68392 | -7.03449 | -63.11229 | 2024-10-26 05:59:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1c608831-2bf0-346c-b38e-4ef184746546 | -6.92122 | -71.50046 | 2024-10-26 05:59:00 | NPP-375D | IPIXUNA | AMAZONAS | Brasil | 1301803 | 13 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 18613336-1c55-3dfc-bbea-29b1b5143f1b | -5.6005 | -60.24567 | 2024-10-26 05:59:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.4 |
| c58d53cb-a813-3e58-9e86-9f9553ed7e41 | -5.6 | -60.24925 | 2024-10-26 05:59:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.4 |
| fdeaa92c-16be-3133-b443-605932be93de | -5.24659 | -55.96265 | 2024-10-26 05:59:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0fdedd37-de56-3dbc-a9d9-427c4c00bc8b | -5.24564 | -55.96954 | 2024-10-26 05:59:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 3a1c9c2e-f15a-3fdb-bc74-9ab0422fc38c | -3.46155 | -64.97198 | 2024-10-26 05:59:00 | NPP-375D | ALVARÃES | AMAZONAS | Brasil | 1300029 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c1f9a136-b7e4-315c-8e6c-14d01554e24c | -3.46001 | -64.97468 | 2024-10-26 05:59:00 | NPP-375D | ALVARÃES | AMAZONAS | Brasil | 1300029 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 59e564aa-2545-334b-9c88-da09cbcf0f37 | -3.38155 | -59.54023 | 2024-10-26 05:59:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 02e5bfcf-9ed0-3a1d-a348-54fe3215809d | -3.37705 | -68.23597 | 2024-10-26 05:59:00 | NPP-375D | AMATURÁ | AMAZONAS | Brasil | 1300060 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5a2d7589-ce34-37f0-9d9d-92b92564d521 | -3.2373 | -65.18557 | 2024-10-26 05:59:00 | NPP-375D | UARINI | AMAZONAS | Brasil | 1304260 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b3a5bf8b-e080-3b6a-8c0c-86238fbfd2e4 | -3.16175 | -68.14107 | 2024-10-26 05:59:00 | NPP-375D | AMATURÁ | AMAZONAS | Brasil | 1300060 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e8aa7d6f-768a-371a-b8ee-2bcf35879e18 | -3.16119 | -68.1446 | 2024-10-26 05:59:00 | NPP-375D | AMATURÁ | AMAZONAS | Brasil | 1300060 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 647f49d4-2ac5-3be3-b863-fde2e1c1d0da | -3.15784 | -68.14407 | 2024-10-26 05:59:00 | NPP-375D | AMATURÁ | AMAZONAS | Brasil | 1300060 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 19be823f-2a16-340d-ac24-97d0028355fb | 3.63962 | -51.27942 | 2024-10-26 06:01:00 | AQUA_M-M | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 71751655-ddea-389d-9168-d4308c650a12 | 2.79383 | -50.92743 | 2024-10-26 06:01:00 | AQUA_M-M | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 48a1ad9f-1ec4-3586-9068-417ada44494c | 1.78809 | -50.46219 | 2024-10-26 06:01:00 | AQUA_M-M | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 16.4 |
| 84f0cef0-3a71-3838-9ea3-516a2a9d557a | -9.44993 | -70.6023 | 2024-10-26 06:01:00 | NPP-375D | SANTA ROSA DO PURUS | ACRE | Brasil | 1200435 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9e5d2aa8-263d-30cf-beea-bdc2f4f2a792 | -8.47164 | -69.69462 | 2024-10-26 06:01:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 729c78b3-5b0f-3b6d-83c1-6539383accbb | -8.4683 | -69.69409 | 2024-10-26 06:01:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.4 |
| dc72e311-1606-34da-bfe7-9a3d024d551e | -7.94556 | -70.72382 | 2024-10-26 06:01:00 | NPP-375D | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3cc43dd9-a4ea-3f68-93a9-0483245ba24e | -7.82564 | -72.78221 | 2024-10-26 06:01:00 | NPP-375D | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 1faf729c-e062-3b50-9e9a-c4f25b54b974 | -7.82213 | -72.78162 | 2024-10-26 06:01:00 | NPP-375D | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 12.8 |
| dc566997-f98f-3093-8bd1-c754755026d8 | -16.09457 | -60.12819 | 2024-10-26 06:01:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 5501b698-ad7f-3733-b4aa-c648b88952f5 | -16.08875 | -60.1222 | 2024-10-26 06:01:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 942c8ba8-bdd8-3182-8ec6-60c04f241a51 | -11.80187 | -65.01078 | 2024-10-26 06:01:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 95bf955c-f3d6-3284-9d23-9784c2c3c1af | -11.02172 | -68.52942 | 2024-10-26 06:01:00 | NPP-375D | EPITACIOLÂNDIA | ACRE | Brasil | 1200252 | 12 | 33 | nan | nan | nan | Amazônia | 0.5 |
| d78500be-9ad7-3864-a6de-a0425a42afff | -10.9136 | -69.23389 | 2024-10-26 06:01:00 | NPP-375D | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 63a93b0b-72d3-36c0-8e12-559a5f0c219b | -10.54924 | -67.83891 | 2024-10-26 06:01:00 | NPP-375D | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d6c27a72-f763-3c60-b5f3-f7226f1f481a | -10.51006 | -67.87971 | 2024-10-26 06:01:00 | NPP-375D | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6094758f-c568-33df-8f71-74fa25ad9439 | -10.12402 | -67.59599 | 2024-10-26 06:01:00 | NPP-375D | SENADOR GUIOMARD | ACRE | Brasil | 1200450 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4225d04c-895a-3360-af90-a3815e28d262 | -10.09893 | -68.37279 | 2024-10-26 06:01:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0b62bb4f-adb4-32a3-9e7e-bdd596c19f6d | -1.34087 | -54.60755 | 2024-10-26 06:03:00 | AQUA_M-M | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 9f9b4869-67a9-360d-9ccc-26ced2bb219f | -5.59931 | -60.24556 | 2024-10-26 06:03:00 | AQUA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 8b180e7e-135f-387e-9d72-6d9d25e8a0ce | -4.57957 | -47.99757 | 2024-10-26 06:03:00 | AQUA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 109.2 |
| c05b409c-7ab7-3b82-806a-0b00491480d4 | -4.57547 | -48.02705 | 2024-10-26 06:03:00 | AQUA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 342.2 |
| 380a9c03-1213-3bcb-b574-42900d8f9eff | -4.57524 | -48.00457 | 2024-10-26 06:03:00 | AQUA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 155.9 |
| 90468761-550e-3d21-b894-4e282131a6a8 | -4.57141 | -48.03378 | 2024-10-26 06:03:00 | AQUA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 170.5 |
| 91ce66cd-1572-3a8a-86ea-2acd0d9d1ca6 | -4.34006 | -55.35355 | 2024-10-26 06:03:00 | AQUA_M-M | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| b46c7189-5509-307c-ae45-c4890afe8a83 | -4.29726 | -55.08554 | 2024-10-26 06:03:00 | AQUA_M-M | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 713bd058-047a-3d3b-a99e-6ab24212a888 | -3.9852 | -53.80323 | 2024-10-26 06:03:00 | AQUA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 82bb2951-08b8-331b-9e7a-d7e39c7a408f | -3.74658 | -53.40479 | 2024-10-26 06:03:00 | AQUA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 11.5 |
| 73ad051f-0c83-3692-a66d-946b6cdd441b | -3.74404 | -53.41016 | 2024-10-26 06:03:00 | AQUA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 12.5 |
| 99ffae64-7795-372e-8374-a85f5d15929a | -3.66033 | -53.8405 | 2024-10-26 06:03:00 | AQUA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 11.5 |
| f365ba5a-b88b-3ed4-89d2-b4c7103b695d | -3.63567 | -55.50522 | 2024-10-26 06:03:00 | AQUA_M-M | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| cc327069-bfd3-3d79-8f32-a8451960e1c2 | -3.63434 | -55.51423 | 2024-10-26 06:03:00 | AQUA_M-M | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 15ac6364-8ea7-3bfd-ae83-0e658f02a808 | -3.62673 | -55.50395 | 2024-10-26 06:03:00 | AQUA_M-M | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| e38f2623-d601-3630-9678-e0cd434bfa77 | -3.61216 | -54.035 | 2024-10-26 06:03:00 | AQUA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| cca1af36-8d4a-33db-8414-2ce48a4834bd | -3.57931 | -54.63221 | 2024-10-26 06:03:00 | AQUA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 882fb64a-b9cb-33d2-974d-db61bdbcc2f0 | -3.48953 | -54.43873 | 2024-10-26 06:03:00 | AQUA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 01c13b32-2146-346f-aea6-edb01be4bc43 | -3.43094 | -54.57901 | 2024-10-26 06:03:00 | AQUA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 13.7 |
| 2db4a4cd-cb8c-3f48-9d80-30fb81f36d4d | -3.42171 | -54.57776 | 2024-10-26 06:03:00 | AQUA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 31.2 |
| c2f89288-b421-3452-8c9c-c69161e73792 | -3.13553 | -54.27338 | 2024-10-26 06:03:00 | AQUA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 205b3646-a2e9-3950-8164-850199cb7876 | -3.12825 | -50.60305 | 2024-10-26 06:03:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 12.0 |
| 0e870c0f-baa9-3ea2-b863-7c289273c62e | -3.12619 | -54.27208 | 2024-10-26 06:03:00 | AQUA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 99d79416-9fd8-3d06-89c3-1f6f22a92933 | -3.12483 | -50.59573 | 2024-10-26 06:03:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 14.3 |
| 8b2fbf10-302e-3471-b1e0-23f39eba8409 | -3.10467 | -53.72401 | 2024-10-26 06:03:00 | AQUA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 19.1 |
| ad860bad-ae86-3b46-8837-be2989d023fc | -3.10312 | -53.73451 | 2024-10-26 06:03:00 | AQUA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |


[Clique aqui para ver as próximas entradas](README102.md)
