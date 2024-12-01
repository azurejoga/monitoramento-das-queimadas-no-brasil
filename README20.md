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

## Dados Diários - Página 20

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6e587758-2cfd-3cd9-9dd0-09fb0cf35470 | -3.4974 | -53.8339 | 2024-12-01 03:20:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 80.5 |
| f7b610fe-d580-37a7-91a5-56747e596057 | -3.2591 | -53.6186 | 2024-12-01 03:20:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 69.9 |
| 99938306-6b40-3195-bdd8-c542f11aad5b | 1.1439 | -55.9871 | 2024-12-01 03:20:00 | GOES-16 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 66.4 |
| 6502fbea-9fb5-37dc-bc95-679abfe20342 | -3.5158 | -53.8333 | 2024-12-01 03:20:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 64.7 |
| 8dabe0c8-e291-3b22-a6a3-7df7997d9ed8 | -6.9344 | -43.5401 | 2024-12-01 03:20:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 104.0 |
| 37e84514-9998-34b2-aeb0-5f7836c2807c | -3.1273 | -54.5264 | 2024-12-01 03:20:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 67.8 |
| 8fbcaffc-2dc0-3c84-b33e-fdcde9894952 | -4.558 | -45.7008 | 2024-12-01 03:20:00 | GOES-16 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 58.9 |
| 31cacd36-79cb-31e5-8539-8fe1f041f37c | 1.1622 | -55.9869 | 2024-12-01 03:20:00 | GOES-16 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 48.1 |
| 9f9b74fc-b9e7-3a08-8cdf-2dd70dd609c1 | -2.6578 | -51.8811 | 2024-12-01 03:20:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 56.5 |
| db459ebd-a1ce-36be-836e-043f1adcf483 | -2.8196 | -53.0629 | 2024-12-01 03:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 61.1 |
| 6b71914d-f024-3076-814b-81f7a6d3fb18 | -3.2774 | -53.6383 | 2024-12-01 03:20:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 69.6 |
| 97807f93-f857-3a7a-beb4-c85aad28e4c3 | -3.259 | -53.6388 | 2024-12-01 03:20:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 100.4 |
| f4e595f5-f435-3fc3-8aa6-8d4ccc1c2e67 | -4.5562 | -43.3028 | 2024-12-01 03:20:00 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 158.4 |
| 8426992d-fea3-335b-ad00-c581745d8d5f | -2.8197 | -53.0425 | 2024-12-01 03:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 77.1 |
| 1aac8b6b-7e44-3db7-b118-906b2becda8f | -3.90508 | -42.42107 | 2024-12-01 03:25:00 | NOAA-20 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 91d52966-2140-3278-a87b-703e37f6c0d7 | -4.54737 | -43.31862 | 2024-12-01 03:25:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| f5ffce72-a6fa-35f0-b2b8-977787a8d3cf | -4.69037 | -42.40284 | 2024-12-01 03:25:00 | NOAA-20 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 3a86274d-ae56-3a26-86d8-657aad54b7e2 | -4.89789 | -41.32115 | 2024-12-01 03:25:00 | NOAA-20 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 5.9 |
| 6709ee40-9000-32ba-b405-8eb4d08c9459 | -4.55099 | -43.29815 | 2024-12-01 03:25:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 24.3 |
| 91b3a2f8-c485-38b3-a556-fa7d72863296 | -4.55011 | -43.30317 | 2024-12-01 03:25:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 24.3 |
| 126a4896-bbbf-316d-abe0-a28727c1fe0b | -4.89238 | -41.32 | 2024-12-01 03:25:00 | NOAA-20 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 17e3d231-a2e7-3699-a7eb-b04f853c4424 | -4.55551 | -43.30948 | 2024-12-01 03:25:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 30.6 |
| c54a3ef8-eaeb-331e-b30f-dd9472bac05a | -4.00043 | -44.75858 | 2024-12-01 03:25:00 | NOAA-20 | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 6af5b621-8b4a-35fa-a9de-7a56d658015f | -4.55641 | -43.30433 | 2024-12-01 03:25:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 24.3 |
| f92858ec-b762-36bd-99da-24e8facc790f | -4.54829 | -43.31342 | 2024-12-01 03:25:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 30.6 |
| 0dbe711a-dc3b-3396-8e26-53cc5631971a | -4.50459 | -42.07375 | 2024-12-01 03:25:00 | NOAA-20 | BOQUEIRÃO DO PIAUÍ | PIAUÍ | Brasil | 2201945 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| c88f6f1a-4d37-3314-8639-023057fef6ab | -4.69631 | -42.40393 | 2024-12-01 03:25:00 | NOAA-20 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| f57728c8-e73c-3667-be4f-8d3dc5fa0057 | -3.90945 | -42.4244 | 2024-12-01 03:25:00 | NOAA-20 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 2df55b39-4644-321d-96f9-a808e42927df | -4.5492 | -43.30828 | 2024-12-01 03:25:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 30.6 |
| fe70a02d-96e7-3e8e-ac54-1c97b3224372 | -3.90417 | -42.41883 | 2024-12-01 03:25:00 | NOAA-20 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 52dbd72c-7ed5-3f69-a29f-d2006ec41de9 | -4.89663 | -41.3284 | 2024-12-01 03:25:00 | NOAA-20 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 5.1 |
| 868a1a27-a93a-3c12-a432-752f6dd934e3 | -4.69369 | -42.4021 | 2024-12-01 03:25:00 | NOAA-20 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 6228e0d8-a307-33fd-9de1-d99b65db1c4c | -4.54289 | -43.30711 | 2024-12-01 03:25:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d9b7154a-c86f-3916-8f81-db7b68952190 | -4.89301 | -41.31638 | 2024-12-01 03:25:00 | NOAA-20 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 0ce3347b-d512-3806-845e-f5b25cdfc01e | -4.89175 | -41.32364 | 2024-12-01 03:25:00 | NOAA-20 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 03abc462-bbab-33c6-9f99-6bc59375f5c7 | -4.50361 | -42.07311 | 2024-12-01 03:25:00 | NOAA-20 | BOQUEIRÃO DO PIAUÍ | PIAUÍ | Brasil | 2201945 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 2bfcfd57-7941-383c-a64f-01485fc3513d | -4.69709 | -42.39954 | 2024-12-01 03:25:00 | NOAA-20 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 4d3b1e1c-9a14-3b0b-a6af-91ce73d033a1 | -4.50945 | -42.0742 | 2024-12-01 03:25:00 | NOAA-20 | BOQUEIRÃO DO PIAUÍ | PIAUÍ | Brasil | 2201945 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| dba5d5c6-57a7-3a92-b45e-5ba127809315 | -3.99927 | -44.76516 | 2024-12-01 03:25:00 | NOAA-20 | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Amazônia | 6.1 |
| d7f3d9e6-52bf-35fd-8dc7-e7c0e45c41fd | -4.5438 | -43.30201 | 2024-12-01 03:25:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 284d4a3c-b950-340b-9d29-9dda54d94662 | -3.90587 | -42.41656 | 2024-12-01 03:25:00 | NOAA-20 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 4fb3dee9-e4e1-3938-a1f3-b505c34263ac | -4.89726 | -41.32479 | 2024-12-01 03:25:00 | NOAA-20 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 5.1 |
| d74a14e5-46f9-3f84-ba0c-d62977c1c09f | -6.92672 | -43.54354 | 2024-12-01 03:27:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 20.2 |
| 6ea19632-c1ca-3a8b-8e5a-200d909d3b3d | -5.91583 | -43.84975 | 2024-12-01 03:27:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 551827d2-265c-36db-831d-1e6e1ee37829 | -7.33335 | -34.81692 | 2024-12-01 03:27:00 | NOAA-20 | CONDE | PARAÍBA | Brasil | 2504603 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 079448de-c776-3793-b8ad-0b4c4220f3a9 | -9.83072 | -36.15775 | 2024-12-01 03:27:00 | NOAA-20 | SÃO MIGUEL DOS CAMPOS | ALAGOAS | Brasil | 2708600 | 27 | 33 | nan | nan | nan | Mata Atlântica | 16.0 |
| 52fdeac8-c0d0-350e-9c87-9e39ef458ed5 | -9.31218 | -40.24058 | 2024-12-01 03:27:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| addea4f7-2514-3a1a-bbb2-43a806132db7 | -4.74394 | -43.71636 | 2024-12-01 03:27:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 2f98b945-4828-3a9e-80c4-bce240774b02 | -6.92124 | -43.54566 | 2024-12-01 03:27:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 13.6 |
| a60fa44a-add4-352a-9116-a0e349663c7f | -5.57922 | -45.21827 | 2024-12-01 03:27:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 2d7aada8-fa9c-3244-ad71-092f321a43fb | -10.52998 | -42.53028 | 2024-12-01 03:27:00 | NOAA-20 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 5644d85e-89f9-3ec6-850b-e54eeab3d45d | -8.12992 | -44.47753 | 2024-12-01 03:27:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 9478e135-d5f8-34f3-9f0c-94b68229f8e1 | -8.93525 | -44.25903 | 2024-12-01 03:27:00 | NOAA-20 | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9af60360-8e17-369a-81a1-e9f9e24d75b8 | -9.31124 | -40.24581 | 2024-12-01 03:27:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| eda8c8c5-b175-363e-8808-d3c182f6c0fb | -10.51624 | -42.42457 | 2024-12-01 03:27:00 | NOAA-20 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 5c51d4d2-3c7f-347f-9ffb-a070e79c64c3 | -8.93 | -44.25261 | 2024-12-01 03:27:00 | NOAA-20 | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ca7c5060-af6b-315e-88ce-71f469a8a763 | -7.25062 | -39.85173 | 2024-12-01 03:27:00 | NOAA-20 | SANTANA DO CARIRI | CEARÁ | Brasil | 2312106 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 6af9cc76-acc7-3d33-b1ef-698d805e23b8 | -6.92211 | -43.54087 | 2024-12-01 03:27:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 16.1 |
| 832cf8e2-4b73-307b-861d-d467a61be8ce | -4.74392 | -43.71756 | 2024-12-01 03:27:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 1c417c0a-2e02-356f-81bc-363d52a0ec0d | -6.15412 | -39.79617 | 2024-12-01 03:27:00 | NOAA-20 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 4be0113e-cb1e-3dcc-b3fc-c63c23ca5bbc | -9.83438 | -36.15839 | 2024-12-01 03:27:00 | NOAA-20 | SÃO MIGUEL DOS CAMPOS | ALAGOAS | Brasil | 2708600 | 27 | 33 | nan | nan | nan | Mata Atlântica | 20.8 |
| e51c37d7-f640-3f2e-9d9c-00ba8512110b | -7.78992 | -38.47056 | 2024-12-01 03:27:00 | NOAA-20 | SERRA TALHADA | PERNAMBUCO | Brasil | 2613909 | 26 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 6d9a37a7-b719-3335-be62-d0a8aef7364a | -4.43895 | -45.3662 | 2024-12-01 03:27:00 | NOAA-20 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| be99f30c-8b71-3896-ad81-467b334c6069 | -7.6524 | -35.25626 | 2024-12-01 03:27:00 | NOAA-20 | ALIANÇA | PERNAMBUCO | Brasil | 2600708 | 26 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 4973b62c-5fa6-3aef-846d-7f061a66e762 | -7.1987 | -35.15761 | 2024-12-01 03:27:00 | NOAA-20 | CRUZ DO ESPÍRITO SANTO | PARAÍBA | Brasil | 2504900 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 57d1a738-a796-3dd4-a280-f58c234cb125 | -7.3404 | -34.81809 | 2024-12-01 03:27:00 | NOAA-20 | CONDE | PARAÍBA | Brasil | 2504603 | 25 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| cff2303d-b84f-368b-aa5f-682280036701 | -9.5242 | -37.03155 | 2024-12-01 03:27:00 | NOAA-20 | MAJOR ISIDORO | ALAGOAS | Brasil | 2704401 | 27 | 33 | nan | nan | nan | Caatinga | 6.1 |
| 26acd5ee-56ae-3554-9ce1-a5a80dd47937 | -5.18131 | -43.96018 | 2024-12-01 03:27:00 | NOAA-20 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 1939f310-8f2b-3b14-a869-740c0faacbfc | -12.78132 | -38.49783 | 2024-12-01 03:27:00 | NOAA-20 | CANDEIAS | BAHIA | Brasil | 2906501 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| ce83acaf-631a-338b-9bbd-1d34304aa7a7 | -6.92145 | -43.53761 | 2024-12-01 03:27:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 16.5 |
| 19288bc6-3a6a-3fbf-8611-6c0d20101370 | -9.83731 | -36.1634 | 2024-12-01 03:27:00 | NOAA-20 | SÃO MIGUEL DOS CAMPOS | ALAGOAS | Brasil | 2708600 | 27 | 33 | nan | nan | nan | Mata Atlântica | 6.0 |
| 7a6aaa5e-f4a0-3015-907b-108d16a68573 | -5.9114 | -43.84632 | 2024-12-01 03:27:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c0a88778-646a-3d86-85bb-2b6670fce2f1 | -5.57777 | -45.21783 | 2024-12-01 03:27:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 1cd6a9a0-be8f-3e94-bb1a-2318bbc980df | -8.7247 | -35.7745 | 2024-12-01 03:27:00 | NOAA-20 | JAQUEIRA | PERNAMBUCO | Brasil | 2607950 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 478c4942-bf04-3b5f-9c2c-a6b2651c6e9c | -6.92035 | -43.55058 | 2024-12-01 03:27:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 13.6 |
| b57416b2-79e7-3e2b-801f-81bfd777ee37 | -9.83803 | -36.15903 | 2024-12-01 03:27:00 | NOAA-20 | SÃO MIGUEL DOS CAMPOS | ALAGOAS | Brasil | 2708600 | 27 | 33 | nan | nan | nan | Mata Atlântica | 20.8 |
| b296b647-a9a6-322e-85a4-70867eff4cea | -8.13086 | -44.47254 | 2024-12-01 03:27:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f5f9b28d-4fac-31d8-829d-44496870c359 | -5.58471 | -45.21923 | 2024-12-01 03:27:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 4fee53bb-e6d8-3b59-b4d0-0dc3bf60c20b | -6.91872 | -43.55211 | 2024-12-01 03:27:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 10.1 |
| b4a2ac84-794e-3c50-83ac-f79489dc84ab | -5.73146 | -43.98619 | 2024-12-01 03:27:00 | NOAA-20 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| b95b58dd-570e-377e-ba46-52e7adccbf09 | -5.41887 | -45.11851 | 2024-12-01 03:27:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 67b6b143-a9c1-3d24-8d54-1e9c801e074f | -5.90947 | -43.84839 | 2024-12-01 03:27:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 28040408-6c85-3739-88de-6d9b35835917 | -8.63791 | -35.70855 | 2024-12-01 03:27:00 | NOAA-20 | CATENDE | PERNAMBUCO | Brasil | 2604205 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 947cb035-4ce6-3e7c-9135-31a39b21a6cc | -6.91508 | -43.54447 | 2024-12-01 03:27:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 13.6 |
| 74d3dd60-e1c6-33e5-b143-085be598785e | -6.92055 | -43.54238 | 2024-12-01 03:27:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 20.2 |
| 86c8f3c7-0977-3322-b864-68a0a6027db5 | -8.93624 | -44.25378 | 2024-12-01 03:27:00 | NOAA-20 | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 715ddfa3-6bf0-32a9-8c9f-72b56cfd4b13 | -6.92581 | -43.54838 | 2024-12-01 03:27:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 20.2 |
| e7b860c8-364b-3acf-ad5f-a1c5549e9a50 | -7.33688 | -34.81748 | 2024-12-01 03:27:00 | NOAA-20 | CONDE | PARAÍBA | Brasil | 2504603 | 25 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 1535ee28-ec46-30c5-b96b-34fdc603579f | -6.91419 | -43.54938 | 2024-12-01 03:27:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 13.6 |
| 41298bf9-1f13-376c-8264-d8bb90038183 | -7.78921 | -38.47472 | 2024-12-01 03:27:00 | NOAA-20 | SERRA TALHADA | PERNAMBUCO | Brasil | 2613909 | 26 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 045a7091-3d0c-3619-a039-e66b34aa6916 | -6.91595 | -43.53967 | 2024-12-01 03:27:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 16.1 |
| 03155cc4-5989-301d-8e80-b8080a6c3443 | -6.92652 | -43.55178 | 2024-12-01 03:27:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 12.0 |
| b165b354-d8fc-3bcb-8571-79173711c958 | -5.42019 | -45.11125 | 2024-12-01 03:27:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| acd34e68-68b6-37fb-a54f-742cdf24664c | -6.91965 | -43.54719 | 2024-12-01 03:27:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 20.2 |
| 7907a72f-aa10-3707-a732-0ba75a1f7fda | -7.75022 | -38.80775 | 2024-12-01 03:27:00 | NOAA-20 | SÃO JOSÉ DO BELMONTE | PERNAMBUCO | Brasil | 2613503 | 26 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 1a02f2bb-7508-3845-9479-1428c6c0aca8 | -10.95551 | -38.13117 | 2024-12-01 03:27:00 | NOAA-20 | TOBIAS BARRETO | SERGIPE | Brasil | 2807402 | 28 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 06167025-05bc-39b4-a336-a3a6164ebfbc | -9.38974 | -39.94274 | 2024-12-01 03:27:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 2e0b135b-8566-3eba-905e-96b3ee46589b | -6.92489 | -43.55328 | 2024-12-01 03:27:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 10.1 |
| e9cf039b-ac0f-357c-9e3f-653bfe56a349 | -8.8597 | -36.51077 | 2024-12-01 03:27:00 | NOAA-20 | GARANHUNS | PERNAMBUCO | Brasil | 2606002 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 1acd9317-2a25-3da6-bdf7-1218fec92641 | -9.44748 | -39.35245 | 2024-12-01 03:27:00 | NOAA-20 | CHORROCHÓ | BAHIA | Brasil | 2907707 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |


[Clique aqui para ver as próximas entradas](README21.md)
