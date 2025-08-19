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

## Dados Diários - Página 54

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7f429834-ca0f-3297-ba70-2ee638809f5e | -7.59357 | -67.37009 | 2025-08-19 06:08:00 | NOAA-21 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 2cad78fb-82be-3094-b126-31e655ad7247 | -7.7853 | -66.96394 | 2025-08-19 06:08:00 | NOAA-21 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 271b2954-7ce4-3bda-8646-a6f71deeb26f | -8.97129 | -69.38484 | 2025-08-19 06:08:00 | NOAA-21 | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c04bdea4-f062-35d4-9bf1-44273b5bdad2 | -9.48334 | -63.51131 | 2025-08-19 06:08:00 | NOAA-21 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d4ca21a4-ff67-3f71-b74f-2984cf0cd84c | -8.63693 | -67.26501 | 2025-08-19 06:08:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1ddf5731-9517-3b03-8345-116a27c0ec51 | -9.18645 | -59.64991 | 2025-08-19 06:08:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 96cac4b0-279f-3780-96f5-b1ff3c40cba3 | -7.79094 | -66.95374 | 2025-08-19 06:08:00 | NOAA-21 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d0f8d4c1-90d0-3d2a-9d2e-3c0131b46b29 | -9.17981 | -59.64838 | 2025-08-19 06:08:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 9933f9fd-2c50-388f-bc1e-9f81330483d3 | -8.76144 | -64.20184 | 2025-08-19 06:08:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 21b3cbeb-9419-34ac-8b44-e030ddb5b96b | -9.18399 | -59.64228 | 2025-08-19 06:08:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 1c62e71f-c861-363a-8f58-be3b29b18d39 | -7.78635 | -66.95676 | 2025-08-19 06:08:00 | NOAA-21 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| a7982320-aa63-3939-acf8-b80c951fda19 | -8.97417 | -60.49685 | 2025-08-19 06:08:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 28a5d897-567a-382f-a3ea-1936c3606d33 | -9.19886 | -59.63241 | 2025-08-19 06:08:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 7c1ee7c7-36ab-322c-a622-019cbd987f96 | -7.55687 | -63.84955 | 2025-08-19 06:08:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.2 |
| b3f65048-990a-3f0d-9a4b-76bb8c42dd9b | -9.19455 | -59.6389 | 2025-08-19 06:08:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 1e8b0694-aae5-3cd5-ba0c-93bb60202112 | -9.07435 | -60.4198 | 2025-08-19 06:08:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a19e0247-76a5-3695-9290-43536441951a | -8.36613 | -70.13873 | 2025-08-19 06:08:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| dce991b0-a9be-3578-a0d4-bfc3e48da1e2 | -9.19599 | -59.62656 | 2025-08-19 06:08:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 6b8747fa-ddd2-33d6-a928-93b23857fe84 | -9.11133 | -60.33291 | 2025-08-19 06:08:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 16865d1d-d7b9-3e11-a61b-0805915e8e87 | -9.19292 | -59.62524 | 2025-08-19 06:08:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 7b7d6950-084a-30ab-9568-b356fade6159 | -9.17357 | -59.61588 | 2025-08-19 06:08:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8f47fb04-ad3b-34a4-a4e7-167b737e1cba | -7.59637 | -63.44706 | 2025-08-19 06:08:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a7011d67-d1cb-30c0-a66f-0308737b0627 | -9.19217 | -59.63129 | 2025-08-19 06:08:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| e6286906-189e-3663-9abd-e8e66fe6ebc2 | -7.79448 | -66.95795 | 2025-08-19 06:08:00 | NOAA-21 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 66f3cb95-1251-3427-9610-ee848b9db541 | -8.97355 | -60.50205 | 2025-08-19 06:08:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.9 |
| c985108e-4cf3-3fcc-9bb6-c53418676fd9 | -7.50333 | -63.82997 | 2025-08-19 06:08:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 982dff9d-346a-3957-822a-f0662f294058 | -7.55186 | -63.84884 | 2025-08-19 06:08:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 89b3f8e5-d968-39cb-8f07-58f43e1ef255 | -8.37015 | -70.13547 | 2025-08-19 06:08:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| af1c7dac-4a31-37c6-a155-464d1cc0e881 | -8.52611 | -72.78402 | 2025-08-19 06:08:00 | NOAA-21 | PORTO WALTER | ACRE | Brasil | 1200393 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1d0fcf04-56a1-3e1c-9a73-17e813a2ba7a | -7.78989 | -66.96096 | 2025-08-19 06:08:00 | NOAA-21 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 1f49a568-aa19-36e2-860b-eafe3d886515 | -8.97193 | -60.49636 | 2025-08-19 06:08:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 8946cbda-e337-35cf-a915-187f6e6d201c | -7.78583 | -66.96035 | 2025-08-19 06:08:00 | NOAA-21 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 44637e6e-ff39-3892-bd42-08c32ac3b94d | -9.18051 | -59.64232 | 2025-08-19 06:08:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 59b8e7f3-f06a-37bb-8362-6d927047b96c | -9.18324 | -59.6484 | 2025-08-19 06:08:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| d5726eba-4f66-32af-b04e-0844f3bad596 | -9.17284 | -59.62188 | 2025-08-19 06:08:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 3af33043-8db9-302f-a37d-048b391333a0 | -9.07369 | -60.42509 | 2025-08-19 06:08:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 65c30da9-90be-3171-aa32-808d3a9e38c6 | -9.19062 | -59.64388 | 2025-08-19 06:08:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| f919abd5-5df5-3c45-a047-2ed7a74aebed | -7.93337 | -63.29329 | 2025-08-19 06:08:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 211ef56c-b7ef-3be8-9bd7-14ed3452454e | -7.79041 | -66.95735 | 2025-08-19 06:08:00 | NOAA-21 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 7578f56d-f205-3f94-8b79-438cfa228017 | -9.64814 | -64.36879 | 2025-08-19 06:08:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| bfae5523-e657-3d31-9694-dc08ca58f481 | -9.17089 | -70.93089 | 2025-08-19 06:08:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9a7463c6-ad04-3b34-93ab-279d0fbb8adb | -9.18027 | -59.61699 | 2025-08-19 06:08:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f0e27749-bf88-3de4-b7f6-13da7f0e6443 | -9.06969 | -71.25459 | 2025-08-19 06:08:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ad92cf2e-a5cb-398b-8eee-a96d065fc589 | -10.0341 | -59.3554 | 2025-08-19 06:08:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 7f700aae-5367-33c1-827c-37320cb9d449 | -11.09534 | -58.94453 | 2025-08-19 06:08:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7166949b-18b4-327a-82cc-7a7b77499335 | -8.36901 | -70.14304 | 2025-08-19 06:08:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6fc0bfd8-1dc3-32f1-bc00-8417d9e93de3 | -7.79501 | -66.95435 | 2025-08-19 06:08:00 | NOAA-21 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ee9327e9-d7f2-3cbf-bcc0-41c7fe19de92 | -9.43128 | -68.59222 | 2025-08-19 06:08:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2aee5260-6e17-3b66-80b4-75046658b443 | -9.18717 | -59.64373 | 2025-08-19 06:08:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| cfb3d6d9-917a-31cc-af3c-2658134cd2df | -7.78936 | -66.96456 | 2025-08-19 06:08:00 | NOAA-21 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0d610e88-6184-3718-8bdf-3146fd9e726e | -9.17657 | -59.64711 | 2025-08-19 06:08:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 88a6bb77-c477-3d09-8284-1e739a855973 | -7.60152 | -63.44779 | 2025-08-19 06:08:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0a1ccac5-c19a-37ab-8ea1-3cdee6ed281b | -9.89247 | -64.26044 | 2025-08-19 06:08:00 | NOAA-21 | BURITIS | RONDÔNIA | Brasil | 1100452 | 11 | 33 | nan | nan | nan | Amazônia | 0.3 |
| ee208d88-734a-3a2f-aa70-04c9216c7a5e | -7.91709 | -70.92671 | 2025-08-19 06:08:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a3c8c8ff-39f3-3353-9ff1-0502830a8f23 | -8.30068 | -70.75354 | 2025-08-19 06:08:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 845a2091-d03a-3054-bb13-b5bf53daa970 | -8.37245 | -70.14356 | 2025-08-19 06:08:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0f8d3ce7-4689-380d-9944-58e29f2fbc79 | -8.97128 | -60.50153 | 2025-08-19 06:08:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 8ec3470e-d8a2-396f-9270-c50d6da9ecd9 | -6.9336 | -43.6101 | 2025-08-19 06:10:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 74.4 |
| c3c9e285-9593-38b9-90da-a9513736fffa | -6.9715 | -43.5833 | 2025-08-19 06:10:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 105.6 |
| 78492b11-0876-3bf6-8d42-5333f0c3658e | -6.9524 | -43.6083 | 2025-08-19 06:10:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 63.4 |
| a045b4b5-9bda-3554-adc6-26404b5fbfbb | -6.9339 | -43.5868 | 2025-08-19 06:10:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 129.2 |
| 6321af28-3aba-3f5b-85a7-476b3ff9f077 | -6.9527 | -43.585 | 2025-08-19 06:10:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 78.8 |
| 901deaae-064a-3cac-b038-4bbba23f5620 | -13.1555 | -54.9357 | 2025-08-19 06:10:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 67.9 |
| 57637321-4b9f-3173-b481-c536913025a8 | -6.9712 | -43.6066 | 2025-08-19 06:10:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 68.6 |
| 9bede269-4dc8-3271-a0e8-51e0c98a719f | -10.92367 | -68.43127 | 2025-08-19 06:10:00 | NOAA-21 | EPITACIOLÂNDIA | ACRE | Brasil | 1200252 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 614fe9c4-15ae-3fe6-a498-5f949b6066bf | -10.09524 | -68.46155 | 2025-08-19 06:10:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 01631e96-2f3e-375d-9cc5-57dec59fc000 | -6.9339 | -43.5868 | 2025-08-19 06:20:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 141.0 |
| cc4edfbf-3f70-3d32-9f68-ccc8449c2a93 | -6.1932 | -42.5259 | 2025-08-19 06:20:00 | GOES-19 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 59.3 |
| 2ac58261-27b5-3a91-8832-16d7d4ce7999 | -5.7887 | -43.6134 | 2025-08-19 06:20:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 47.6 |
| cbb07fab-ef32-3aec-b2a0-2f9521fb5b13 | -13.1555 | -54.9357 | 2025-08-19 06:20:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 72.8 |
| 0bc718f3-0306-3cd9-b8cd-2880f6bfd524 | -6.9715 | -43.5833 | 2025-08-19 06:20:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 114.0 |
| 475da332-9832-3102-a76f-43f79018dc5b | -6.9527 | -43.585 | 2025-08-19 06:20:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 81.4 |
| 9f9998df-1f7d-3c9e-bb33-45710feef12c | -6.9527 | -43.585 | 2025-08-19 06:30:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 80.7 |
| 1d78f112-ed3e-30cd-9a45-7636fd4b9f9d | -6.9715 | -43.5833 | 2025-08-19 06:30:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 103.7 |
| f52fd03a-4e21-3d48-bfed-e4c3cfe9283b | -6.1932 | -42.5259 | 2025-08-19 06:30:00 | GOES-19 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 82.4 |
| 8aa26325-887c-3da5-af35-9854ca276f19 | -6.9339 | -43.5868 | 2025-08-19 06:30:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 109.5 |
| 9cd94b64-72d9-353b-9a85-d1b061c4adc5 | -13.1555 | -54.9357 | 2025-08-19 06:30:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 74.1 |
| 3f66cfc8-ba7a-3434-9813-d924ef7d101b | -13.3537 | -54.4213 | 2025-08-19 06:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 45.0 |
| d057409b-b1bd-3773-9ebd-45ecc8d743da | -7.59462 | -67.37367 | 2025-08-19 06:33:00 | NPP-375D | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 382c39c0-610f-33f9-85cd-ac6781c706ca | -7.78526 | -66.96131 | 2025-08-19 06:33:00 | NPP-375D | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 85c6635e-a4d1-3a3c-9fb8-234f22bbb26d | -7.792 | -66.9575 | 2025-08-19 06:33:00 | NPP-375D | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5aa60d80-b1b0-3e38-9a02-268e421ae54f | -7.59517 | -67.36947 | 2025-08-19 06:33:00 | NPP-375D | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7cf253ce-1e96-3043-9f20-1d191dc7e114 | -7.79262 | -66.95281 | 2025-08-19 06:33:00 | NPP-375D | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2dbec230-c8db-30e1-9432-b5354789679b | -8.63557 | -67.26774 | 2025-08-19 06:33:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b8a9bd71-0553-3037-b415-75661e62860e | -7.79138 | -66.96217 | 2025-08-19 06:33:00 | NPP-375D | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 9d29fe2f-51e2-37b8-926b-6c6fdb684fae | -7.78587 | -66.95667 | 2025-08-19 06:33:00 | NPP-375D | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a8bd9364-27b5-3109-9374-3f631a702d23 | -8.52588 | -72.78495 | 2025-08-19 06:35:00 | NPP-375D | PORTO WALTER | ACRE | Brasil | 1200393 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 615e9d07-489a-3973-b36c-8fe4a8b70627 | -10.17296 | -69.01768 | 2025-08-19 06:35:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a3e55371-fea2-3a0b-af58-1c9d011b487d | -6.9715 | -43.5833 | 2025-08-19 06:40:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 92.3 |
| f60c8945-5d04-36d2-b4c5-b89be0fe44df | -6.9336 | -43.6101 | 2025-08-19 06:40:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 64.6 |
| bfe5b835-8ce5-300b-a8fc-54376db9920e | -6.9527 | -43.585 | 2025-08-19 06:40:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 72.6 |
| d15fb7c9-3aca-355f-a74c-8b794ae324dd | -6.9339 | -43.5868 | 2025-08-19 06:40:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 130.0 |
| 449e2998-561e-37f7-baed-1d309095f926 | -13.1555 | -54.9357 | 2025-08-19 06:40:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 52.6 |
| 17123d64-3ae0-3ed3-bf94-dc178d7bf44e | -6.1932 | -42.5259 | 2025-08-19 06:40:00 | GOES-19 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 140.7 |
| 149ec31b-0711-319b-b279-e43d0b072769 | -6.9339 | -43.5868 | 2025-08-19 06:50:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 142.1 |
| 0b09cb64-b5ce-35a8-aa24-d75292bba592 | -6.1932 | -42.5259 | 2025-08-19 06:50:00 | GOES-19 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 173.5 |
| 888469ca-59b1-34fe-96da-553d640cc6ec | -6.9715 | -43.5833 | 2025-08-19 06:50:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 97.8 |
| 3ec4a54b-87a7-3981-b53e-92de620137d8 | -6.9527 | -43.585 | 2025-08-19 06:50:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 75.4 |
| cc441302-d6a1-3797-89b6-172cb217b57a | -13.1555 | -54.9357 | 2025-08-19 06:50:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 51.4 |
| 401ad025-46ca-3742-a4d2-f54a0b41e400 | -9.19396 | -59.61821 | 2025-08-19 06:59:00 | AQUA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 7.5 |


[Clique aqui para ver as próximas entradas](README55.md)
