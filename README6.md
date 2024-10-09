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
| 070cfe89-6aa8-36f4-8dd1-5bedbf201236 | -7.0231 | -59.4303 | 2024-10-09 00:35:46 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 35.2 |
| 9429dc3a-c899-37f9-8284-34a71f11ce49 | -7.0232 | -59.4111 | 2024-10-09 00:35:46 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 44.0 |
| b683e29b-da55-3588-9d8c-d469c36c900f | -7.0417 | -59.4103 | 2024-10-09 00:35:47 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 32.2 |
| 65a68d55-3b51-37d7-b4c3-a9e383bb3104 | -7.1871 | -59.7893 | 2024-10-09 00:35:47 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 40.0 |
| 2c631cf7-7dc8-3197-9a35-2e1ab6a59e19 | -7.1873 | -59.7701 | 2024-10-09 00:35:47 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 51.8 |
| d6699500-4d68-31ac-affc-f02292c71ece | -7.2435 | -59.633 | 2024-10-09 00:35:48 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 46.2 |
| dff0f68e-e953-37eb-8597-35f6026d6749 | -7.2619 | -59.6323 | 2024-10-09 00:35:48 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 39.1 |
| 4211ab30-4236-3703-a7d1-181987aaff68 | -7.3473 | -64.6661 | 2024-10-09 00:35:48 | GOES-16 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 38.7 |
| a1698c83-909e-3ac6-80e0-adaf4ede934a | -7.7312 | -43.0402 | 2024-10-09 00:35:50 | GOES-16 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 69.5 |
| cdcebc3e-1b0a-3f7f-887d-e86ae9f9ccb0 | -8.4919 | -48.6476 | 2024-10-09 00:35:54 | GOES-16 | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Amazônia | 188.0 |
| 2a3a32ba-a7e9-3176-92d9-2e51780b674d | -8.4921 | -48.6259 | 2024-10-09 00:35:54 | GOES-16 | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Amazônia | 138.3 |
| 2a124560-3413-3067-8878-1af6e096a9c8 | -8.5107 | -48.6459 | 2024-10-09 00:35:54 | GOES-16 | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Amazônia | 130.4 |
| 8e514a11-98ac-357a-81fd-6f5ba717cf00 | -8.5109 | -48.6242 | 2024-10-09 00:35:54 | GOES-16 | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Amazônia | 97.7 |
| c86bf2e8-bf1c-3e54-b30e-f4b89c2995ea | -9.0543 | -63.2375 | 2024-10-09 00:35:58 | GOES-16 | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 66.9 |
| 99246e3d-8dae-304a-8051-f69ab7138c6a | -9.2689 | -46.7014 | 2024-10-09 00:35:58 | GOES-16 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 80.3 |
| 72afd944-5328-35bc-942c-08d8a64f3140 | -9.1573 | -61.5803 | 2024-10-09 00:35:59 | GOES-16 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 77.0 |
| 8316c64d-bb79-3ad7-889f-2b5bfcca5e6c | -10.3656 | -64.8262 | 2024-10-09 00:36:06 | GOES-16 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 53.2 |
| 2fc06127-80e9-349b-b539-e93fd0339882 | -10.3894 | -61.2502 | 2024-10-09 00:36:06 | GOES-16 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 91.1 |
| b82db25f-b64f-3d31-9709-95770abc7401 | -10.3895 | -61.231 | 2024-10-09 00:36:06 | GOES-16 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 89.0 |
| 52ede00a-a826-3d26-a773-18312a0067ae | -10.3842 | -64.8443 | 2024-10-09 00:36:06 | GOES-16 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 55.5 |
| 5610fddb-9bb9-3aa5-83a7-60b0c17ad67d | -10.3843 | -64.8255 | 2024-10-09 00:36:06 | GOES-16 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 79.6 |
| c5f859e4-56c6-38f3-b710-d1e4a46356c3 | -10.4287 | -60.9979 | 2024-10-09 00:36:06 | GOES-16 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 59.8 |
| 50837fe5-9df4-33b7-9138-c5a3cba439f7 | -10.5943 | -64.024 | 2024-10-09 00:36:07 | GOES-16 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 89.9 |
| 45b4d773-4824-3714-b92f-f7c1c435ca8e | -10.8567 | -63.9177 | 2024-10-09 00:36:08 | GOES-16 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 82.1 |
| 12db4d41-d31a-3e91-a5a9-6f099ff3bc35 | -10.8568 | -63.8988 | 2024-10-09 00:36:08 | GOES-16 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 81.1 |
| 8a9633d8-78c3-3a97-97c0-402b5acfc602 | -10.8754 | -63.9169 | 2024-10-09 00:36:08 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 123.1 |
| fed0a6cc-7204-382c-b34a-d51641544eda | -10.8755 | -63.8979 | 2024-10-09 00:36:08 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 97.9 |
| 5f526614-4bae-325a-9748-b8d07494ecfb | -10.8925 | -64.1623 | 2024-10-09 00:36:09 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 75.9 |
| 1a405b5f-1e2d-365d-83f1-2925ac679042 | -10.8941 | -63.916 | 2024-10-09 00:36:09 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 85.3 |
| d110a6d7-f119-3dc7-9717-c96591b8a221 | -10.9112 | -64.1615 | 2024-10-09 00:36:09 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 167.2 |
| 21a412c3-f4aa-3e35-ba0f-a9e022d482f8 | -10.9113 | -64.1426 | 2024-10-09 00:36:09 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 203.3 |
| d8bcbf13-ffb8-3cff-a76c-c989ccc0e10e | -11.5726 | -58.9619 | 2024-10-09 00:36:12 | GOES-16 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 83.2 |
| c09ea0a9-94b9-3acc-9f38-0fd47ed7ce07 | -11.5728 | -58.9423 | 2024-10-09 00:36:12 | GOES-16 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 75.0 |
| 2c10b776-ddaa-3266-acde-ed337eaf20a2 | -11.6806 | -64.0312 | 2024-10-09 00:36:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 82.9 |
| a43b13db-39bf-3e0a-a13a-d25d2cb6137c | -11.6808 | -64.0121 | 2024-10-09 00:36:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 78.5 |
| 1b7fcbad-c82f-38e2-bf96-b96656a8acbd | -11.9917 | -51.0766 | 2024-10-09 00:36:14 | GOES-16 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 68.2 |
| 6354fa97-7850-32e5-be53-89023ae73d9e | -11.992 | -51.0553 | 2024-10-09 00:36:14 | GOES-16 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 103.6 |
| 2045b622-1596-352d-9b69-b55d129a524f | -12.0107 | -51.0744 | 2024-10-09 00:36:14 | GOES-16 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 113.3 |
| 4d4243d7-a915-3da8-8296-883290f7ef42 | -12.011 | -51.0531 | 2024-10-09 00:36:14 | GOES-16 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 150.3 |
| 1c8dcb5d-5030-3bba-a604-4d4b16189f13 | -12.0298 | -51.0722 | 2024-10-09 00:36:14 | GOES-16 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 57.7 |
| c0283d26-fa2d-337e-9530-f82120758312 | -12.7673 | -44.8904 | 2024-10-09 00:36:18 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 79.1 |
| f0fa4475-f087-3b47-9dff-b524ee985c0d | -12.6676 | -63.0819 | 2024-10-09 00:36:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 121.3 |
| 94236b6e-7716-3648-abba-88a2a310020d | -12.6876 | -62.9464 | 2024-10-09 00:36:19 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 73.5 |
| 74f9ce12-c282-37bc-ab09-46d93ca6fa94 | -12.7501 | -62.269 | 2024-10-09 00:36:19 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 96.9 |
| 91dd7dc3-68ab-36e7-8434-1ea95074c2a1 | -12.7502 | -62.2497 | 2024-10-09 00:36:19 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 55.2 |
| 9f1b9bc6-07f7-3501-8672-790b49766e99 | -12.769 | -62.2678 | 2024-10-09 00:36:19 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 69.4 |
| 8724dc72-2cb1-3dcb-899a-2cd6a9fc76a5 | -12.9166 | -62.7214 | 2024-10-09 00:36:20 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 69.0 |
| 0ba66505-0fc3-31b2-bc65-f4b56d276891 | -13.8958 | -44.5351 | 2024-10-09 00:36:24 | GOES-16 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 93.7 |
| 601e2dd8-7afa-366b-b8cf-b68a9811cc53 | -13.8963 | -44.5116 | 2024-10-09 00:36:24 | GOES-16 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 77.3 |
| e4e1fb07-72fd-31bc-98e5-dda74927ee2a | -13.9153 | -44.5317 | 2024-10-09 00:36:24 | GOES-16 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 94.4 |
| 7af05fec-7fcb-3f4a-a4a9-249b9040232d | -13.9158 | -44.5081 | 2024-10-09 00:36:24 | GOES-16 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 88.2 |
| 77bad5fb-83b2-328e-8108-fb6b46a5cfcc | -14.0985 | -44.1447 | 2024-10-09 00:36:25 | GOES-16 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 74.7 |
| 57b0f8c4-8238-3756-9444-c6b95488625b | -14.1002 | -44.9672 | 2024-10-09 00:36:25 | GOES-16 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 85.8 |
| 358dc2a9-7f66-3b5a-9a0a-7e380555d088 | -14.1192 | -44.9872 | 2024-10-09 00:36:25 | GOES-16 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 165.1 |
| 82052211-2eef-3aca-b72f-b493457208e5 | -14.1197 | -44.9637 | 2024-10-09 00:36:25 | GOES-16 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 240.1 |
| a5b149c2-f87e-33e7-a6ab-53b995a4d158 | -14.1387 | -44.9837 | 2024-10-09 00:36:25 | GOES-16 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 86.1 |
| 69e8aefd-5161-3413-83d7-6357f460fc60 | -14.1392 | -44.9603 | 2024-10-09 00:36:25 | GOES-16 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 154.3 |
| 66247fd4-ab44-359b-8746-cafd7f764800 | -14.1397 | -44.9368 | 2024-10-09 00:36:25 | GOES-16 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 80.2 |
| 86343d76-0b6b-3cdd-944d-b29779beba31 | -15.688 | -59.3945 | 2024-10-09 00:36:35 | GOES-16 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 75.5 |
| 7379f656-f43f-37c2-9390-799a29ad2a50 | -15.7073 | -59.3926 | 2024-10-09 00:36:35 | GOES-16 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 72.7 |
| 210364c4-f99b-39b4-883f-2f215e20c184 | -15.7076 | -59.3726 | 2024-10-09 00:36:35 | GOES-16 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 92.0 |
| 0aca6952-72a2-3cce-a177-0362a34dc658 | -16.3988 | -55.9479 | 2024-10-09 00:36:39 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 55.5 |
| f24cee8a-2419-3988-b00c-7b144526a372 | -16.3992 | -55.9272 | 2024-10-09 00:36:39 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 46.8 |
| 5d75a049-22cc-371c-a97c-3b4e3ad0f3dc | -16.4184 | -55.9455 | 2024-10-09 00:36:39 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 121.9 |
| 84d84a4a-9534-3097-93b8-7cedcafd8d38 | -16.4187 | -55.9248 | 2024-10-09 00:36:39 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 96.6 |
| b6cd0afe-3bc4-3db4-85fc-e19ae4bb1ea7 | -16.4379 | -55.9431 | 2024-10-09 00:36:39 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 61.2 |
| 2da4f01e-b4fa-3998-a61a-a4a02a7f11b3 | -16.4383 | -55.9224 | 2024-10-09 00:36:39 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 59.5 |
| 7900026f-d88f-347e-8fb0-df2e09ec59d6 | -16.6723 | -57.1488 | 2024-10-09 00:36:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 50.7 |
| d5f4dab5-cad8-3107-b4ec-2907fecf76f5 | -16.7575 | -56.7081 | 2024-10-09 00:36:41 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 89.2 |
| 4138a545-fc2a-3736-8d72-2ecb2eea7f87 | -16.8743 | -56.7352 | 2024-10-09 00:36:41 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 93.2 |
| 2f5633a0-140e-3e24-b9d8-15bd5041f442 | -16.9094 | -55.8014 | 2024-10-09 00:36:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 70.6 |
| 44d3a32f-2c32-3edc-86cb-a4a879e3391b | -16.9518 | -56.7875 | 2024-10-09 00:36:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 97.7 |
| 3921b71a-5309-3f87-b845-b8bf9cd1049d | -16.9521 | -56.7669 | 2024-10-09 00:36:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 84.5 |
| 987acaaf-f324-30db-b5a2-3ffa63f7ceae | -16.9805 | -57.4404 | 2024-10-09 00:36:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 44.8 |
| 44d2a322-da1e-3eb1-8de5-1edf36e361f5 | -17.0878 | -56.8534 | 2024-10-09 00:36:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 105.5 |
| c88b8690-3eea-33f1-a44b-b5f2e08adc1e | -17.1074 | -56.851 | 2024-10-09 00:36:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 91.8 |
| 461f8b02-047d-35ea-9ae0-18b8b1e2cdf1 | -17.1271 | -56.8486 | 2024-10-09 00:36:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 87.6 |
| b8952601-ba30-3c4d-814d-03b37079a44f | -17.1467 | -56.8463 | 2024-10-09 00:36:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 98.5 |
| 2ca8869f-b8f5-3186-8cf8-d9b0285dfbf7 | -17.1471 | -56.8256 | 2024-10-09 00:36:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 92.4 |
| 2ffcefc4-965e-3807-8a0c-0ea6004b9745 | -17.1588 | -56.1222 | 2024-10-09 00:36:43 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 80.6 |
| a80736de-e9ea-3ae0-a4bd-d7d82788167f | -17.1587 | -57.3172 | 2024-10-09 00:36:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 53.8 |
| 40582601-1445-323d-8132-89301ebeec10 | -17.1977 | -57.333 | 2024-10-09 00:36:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 77.1 |
| 3b893f8e-96e4-3f1d-adb2-581b15f26046 | -17.2173 | -57.3307 | 2024-10-09 00:36:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 90.5 |
| 172e8f9e-39cc-35c9-8c47-bd3c1005da4d | -17.316 | -54.9973 | 2024-10-09 00:36:43 | GOES-16 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | 53.8 |
| f5f45108-6e45-31bf-88bb-f3ec47ff7bf7 | -17.3353 | -55.0156 | 2024-10-09 00:36:43 | GOES-16 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | 57.4 |
| 57705c25-632b-3393-ad57-131506c56683 | -17.3357 | -54.9946 | 2024-10-09 00:36:43 | GOES-16 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | 54.5 |
| 3399c730-6898-36b7-b4a2-b8539473bcaa | -22.658001 | -42.093498 | 2024-10-09 00:36:45 | METOP-C | CABO FRIO | RIO DE JANEIRO | Brasil | 3300704 | 33 | 33 | nan | nan | nan | Mata Atlântica | nan |
| b22d4dba-a8b2-3653-9265-a3ea9aa9660f | -22.6597 | -42.101002 | 2024-10-09 00:36:45 | METOP-C | CABO FRIO | RIO DE JANEIRO | Brasil | 3300704 | 33 | 33 | nan | nan | nan | Mata Atlântica | nan |
| cd47050e-ef91-303f-89d4-24aa8f5b973c | -22.6614 | -42.108501 | 2024-10-09 00:36:45 | METOP-C | CABO FRIO | RIO DE JANEIRO | Brasil | 3300704 | 33 | 33 | nan | nan | nan | Mata Atlântica | nan |
| c63a0244-6b2c-3e9e-abb9-9c7d9a8f7065 | -18.5993 | -57.2629 | 2024-10-09 00:36:50 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 98.8 |
| ee37ce53-e79e-3275-8574-4e1468ca9747 | -18.5996 | -57.2422 | 2024-10-09 00:36:50 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 96.8 |
| f67a9c2b-a6cd-3ead-9d44-09b13c2a9f07 | -19.9924 | -42.4346 | 2024-10-09 00:36:56 | GOES-16 | RAUL SOARES | MINAS GERAIS | Brasil | 3154002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 125.7 |
| c7f10d88-205d-34c3-ace5-5f6c76f3d791 | -20.0122 | -42.4541 | 2024-10-09 00:36:56 | GOES-16 | RAUL SOARES | MINAS GERAIS | Brasil | 3154002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 96.2 |
| cf94973a-c0c6-3cf9-92d3-d6c7ada97b62 | -20.013 | -42.4287 | 2024-10-09 00:36:56 | GOES-16 | RAUL SOARES | MINAS GERAIS | Brasil | 3154002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 170.4 |
| b4f2c082-57a1-383d-b0d6-f04b87ddd538 | -20.1087 | -48.8261 | 2024-10-09 00:36:57 | GOES-16 | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | 183.4 |
| 05955714-2045-34a7-aad5-c978533ca7cd | -20.1291 | -48.8217 | 2024-10-09 00:36:58 | GOES-16 | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | 146.0 |
| 08349396-08cd-3bfd-a5de-508fe3984766 | -20.208 | -52.9616 | 2024-10-09 00:36:58 | GOES-16 | ÁGUA CLARA | MATO GROSSO DO SUL | Brasil | 5000203 | 50 | 33 | nan | nan | nan | Cerrado | 105.7 |
| f6a3fdfd-b590-3791-83ac-a310a7f5cf25 | -23.2351 | -48.971802 | 2024-10-09 00:36:58 | METOP-C | AVARÉ | SÃO PAULO | Brasil | 3504503 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 01e4cc6b-b9d3-3de5-927e-6c7fc2d55b84 | -23.2374 | -48.9846 | 2024-10-09 00:36:58 | METOP-C | AVARÉ | SÃO PAULO | Brasil | 3504503 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 63ab7f19-b5be-3d0b-9eb6-5ab8d64b6369 | -23.677601 | -51.827 | 2024-10-09 00:36:58 | METOP-C | BOM SUCESSO | PARANÁ | Brasil | 4103206 | 41 | 33 | nan | nan | nan | Mata Atlântica | nan |


[Clique aqui para ver as próximas entradas](README7.md)
