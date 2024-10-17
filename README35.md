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

## Dados Diários - Página 35

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6195299d-30d9-3f85-8809-95748f4d31b2 | -17.74577 | -43.91166 | 2024-10-17 04:17:00 | NOAA-20 | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 91a0295f-d75d-3355-95c6-b88e9b3fdee8 | -17.7452 | -43.91549 | 2024-10-17 04:17:00 | NOAA-20 | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cd54e8e0-1428-3ba7-9b5b-58f25b8f9863 | -17.74237 | -43.9111 | 2024-10-17 04:17:00 | NOAA-20 | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f8fa071b-6b46-3866-9e18-2afe305a7527 | -17.6492 | -44.4671 | 2024-10-17 04:17:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c14cf86c-fbd5-3cbd-980c-6721afc88a29 | -18.52098 | -43.9886 | 2024-10-17 04:17:00 | NOAA-20 | MONJOLOS | MINAS GERAIS | Brasil | 3142502 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| ad136c68-9ecc-3864-b0a7-f2b1bc328c0b | -19.48927 | -44.13283 | 2024-10-17 04:17:00 | NOAA-20 | PRUDENTE DE MORAIS | MINAS GERAIS | Brasil | 3153608 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 4d460834-164f-38eb-a781-577964e7e618 | -19.96268 | -44.68901 | 2024-10-17 04:17:00 | NOAA-20 | IGARATINGA | MINAS GERAIS | Brasil | 3130200 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 21e41ea9-3035-32c4-8b84-b9951ab5a80c | -19.63772 | -43.48497 | 2024-10-17 04:17:00 | NOAA-20 | ITABIRA | MINAS GERAIS | Brasil | 3131703 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0437897f-9b21-3e8d-8c28-6fb61b5b9819 | -19.51366 | -44.27583 | 2024-10-17 04:17:00 | NOAA-20 | SETE LAGOAS | MINAS GERAIS | Brasil | 3167202 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f5a2998e-6954-3e33-a750-08b32f1ff36d | -20.89967 | -43.81806 | 2024-10-17 04:17:00 | NOAA-20 | CARANAÍBA | MINAS GERAIS | Brasil | 3113107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 906eab1a-1384-3e17-a050-6f9fc600f01e | -20.25366 | -43.56676 | 2024-10-17 04:17:00 | NOAA-20 | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| d760cf86-1979-357b-b96c-c57627330305 | -20.24189 | -43.57383 | 2024-10-17 04:17:00 | NOAA-20 | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 9914f464-9919-384d-8448-28eee7da492d | -19.84894 | -43.84611 | 2024-10-17 04:17:00 | NOAA-20 | SABARÁ | MINAS GERAIS | Brasil | 3156700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| b889caa1-265f-3d4b-ab8c-ff9a1df62996 | -21.61313 | -45.36091 | 2024-10-17 04:17:00 | NOAA-20 | VARGINHA | MINAS GERAIS | Brasil | 3170701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 72fb9752-f4cf-30be-b92b-3bacbb9bb857 | -21.61256 | -45.3647 | 2024-10-17 04:17:00 | NOAA-20 | VARGINHA | MINAS GERAIS | Brasil | 3170701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| cb63e4a0-e8ba-3b4e-9255-5faf4e9d683d | -21.60977 | -45.36034 | 2024-10-17 04:17:00 | NOAA-20 | VARGINHA | MINAS GERAIS | Brasil | 3170701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 385ae5a7-76bf-3c04-b46c-80afa3eb5b3b | -21.60921 | -45.36414 | 2024-10-17 04:17:00 | NOAA-20 | VARGINHA | MINAS GERAIS | Brasil | 3170701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 8a6f283c-5623-3f21-8b58-2e0fda30494a | -21.19594 | -44.93642 | 2024-10-17 04:17:00 | NOAA-20 | IJACI | MINAS GERAIS | Brasil | 3130408 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| bcffdd41-8247-3533-abc2-fec432b27940 | -21.18082 | -44.27425 | 2024-10-17 04:17:00 | NOAA-20 | SÃO JOÃO DEL REI | MINAS GERAIS | Brasil | 3162500 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| c180c153-8f42-304d-bcde-1351a42790fd | -21.00933 | -44.18227 | 2024-10-17 04:17:00 | NOAA-20 | CORONEL XAVIER CHAVES | MINAS GERAIS | Brasil | 3119708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 960bb804-01cc-3285-8e2e-fe2b8f695fe8 | -21.00588 | -44.18171 | 2024-10-17 04:17:00 | NOAA-20 | CORONEL XAVIER CHAVES | MINAS GERAIS | Brasil | 3119708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 7c3300f5-db0c-3baf-9019-d7e16e26c5cb | -23.98525 | -55.18424 | 2024-10-17 04:19:00 | NOAA-20 | SETE QUEDAS | MATO GROSSO DO SUL | Brasil | 5007703 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| bc5c50f0-9a5c-3b1f-b2eb-e8f734a14083 | -3.3526 | -53.2112 | 2024-10-17 04:25:25 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 60.4 |
| 861f80f4-307a-3264-8e63-742d178074bb | -3.7007 | -45.9223 | 2024-10-17 04:25:27 | GOES-16 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 64.8 |
| c693869a-ae57-3eab-b277-296eb3a44268 | -3.7009 | -45.9 | 2024-10-17 04:25:27 | GOES-16 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 62.9 |
| 50c6f789-93ff-3253-a309-d575f3690623 | -3.9078 | -42.4256 | 2024-10-17 04:25:28 | GOES-16 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 59.1 |
| 60814fb4-f346-30a2-8ed4-8b3c0df60b40 | -3.908 | -42.402 | 2024-10-17 04:25:28 | GOES-16 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 108.4 |
| 2af5666c-2952-3093-843d-58b4ac6a586b | -3.9265 | -42.4246 | 2024-10-17 04:25:28 | GOES-16 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 88.7 |
| 9cfa571c-3ada-364d-b454-edce864ebf08 | -3.9267 | -42.401 | 2024-10-17 04:25:28 | GOES-16 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 162.2 |
| c4358f71-e36c-3b69-8b6e-3a864aed6b47 | -5.5716 | -44.8927 | 2024-10-17 04:25:37 | GOES-16 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 69.9 |
| 90c2d2aa-860c-3110-b4d3-deacc569c7f7 | -9.1552 | -61.9047 | 2024-10-17 04:25:58 | GOES-16 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 59.2 |
| f91b1bc8-f742-3a18-8259-2663c41437b9 | -10.129 | -56.7722 | 2024-10-17 04:26:04 | GOES-16 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 53.1 |
| 39868e3c-a69a-3e4b-88ed-867b45a86c08 | -11.4859 | -65.1198 | 2024-10-17 04:26:12 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 52.0 |
| 7d5197de-5f76-3938-9693-be05264b250c | -17.8049 | -57.4655 | 2024-10-17 04:26:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 80.7 |
| 38121621-6a8b-3db4-81f1-8cdfd1e15a73 | -17.8052 | -57.4449 | 2024-10-17 04:26:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 87.6 |
| 24f9f97c-1f8c-3e7c-b3db-a56f28bf8270 | -17.8641 | -57.4583 | 2024-10-17 04:26:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 54.8 |
| c4cbe562-a750-3584-8505-1f0edbc54043 | -18.254 | -56.6029 | 2024-10-17 04:26:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 75.7 |
| 740c227b-0919-381b-9492-466bb1b2af9c | -18.9491 | -54.5281 | 2024-10-17 04:26:52 | GOES-16 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 53.5 |
| 30de31ac-c77a-3e60-926d-69199fd6f9f5 | -3.3526 | -53.2112 | 2024-10-17 04:35:25 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 64.7 |
| e7828edc-878f-3d8c-8974-3a3311ac4cbf | -3.5086 | -51.1122 | 2024-10-17 04:35:26 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 62.0 |
| 93ae4adb-dad3-3595-945d-d097f355eb43 | -3.7007 | -45.9223 | 2024-10-17 04:35:27 | GOES-16 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 57.6 |
| 9ef1bf34-dfee-346e-8971-7087f4300181 | -3.9078 | -42.4256 | 2024-10-17 04:35:28 | GOES-16 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 60.8 |
| 499f3706-0f29-3d3b-b59b-ba2ead69b940 | -3.908 | -42.402 | 2024-10-17 04:35:28 | GOES-16 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 200.1 |
| 42f8f8da-866b-321c-a38c-298dc500d06b | -3.9081 | -42.3784 | 2024-10-17 04:35:28 | GOES-16 | ESPERANTINA | PIAUÍ | Brasil | 2203701 | 22 | 33 | nan | nan | nan | Caatinga | 68.3 |
| 171862fc-2298-3876-a40b-22ab5a9e419f | -3.9265 | -42.4246 | 2024-10-17 04:35:28 | GOES-16 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 81.1 |
| 2f971f57-b333-39f7-a00a-cff881680f27 | -3.9267 | -42.401 | 2024-10-17 04:35:28 | GOES-16 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 240.4 |
| 2463a8b9-734d-309c-bcf3-ccc93532d777 | -3.9268 | -42.3773 | 2024-10-17 04:35:28 | GOES-16 | ESPERANTINA | PIAUÍ | Brasil | 2203701 | 22 | 33 | nan | nan | nan | Caatinga | 51.6 |
| 03edb37e-417d-32e3-bac5-d8d60b3a0cc4 | -9.1552 | -61.9047 | 2024-10-17 04:35:58 | GOES-16 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 57.5 |
| 87e2b230-140d-32fa-a2a6-edad0c205b97 | -10.129 | -56.7722 | 2024-10-17 04:36:04 | GOES-16 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 85.6 |
| e226e5ec-9022-3753-af65-9811bcf38f22 | -11.4859 | -65.1198 | 2024-10-17 04:36:12 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 52.5 |
| b76a6bee-8d65-3831-b69f-e034edfcc37a | -11.6566 | -64.8288 | 2024-10-17 04:36:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 52.0 |
| 4bee0d62-6cca-3fd6-af80-7da5fb64a03b | -17.8049 | -57.4655 | 2024-10-17 04:36:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 82.3 |
| eab4c774-ee60-3ed4-b190-a48c7c26ae1f | -17.8052 | -57.4449 | 2024-10-17 04:36:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 101.4 |
| 4978cf03-9056-3b3e-8b6b-665c6a43057a | -17.8246 | -57.4631 | 2024-10-17 04:36:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 70.2 |
| b2ebc220-ca82-33d6-a972-e26c8eecc5a7 | -17.8444 | -57.4607 | 2024-10-17 04:36:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 63.5 |
| 55798b51-8f45-33a5-ba56-ff223f28b43a | -17.8641 | -57.4583 | 2024-10-17 04:36:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 68.1 |
| 58dd8dc3-405c-3724-8b7c-7a20f63833ac | -18.254 | -56.6029 | 2024-10-17 04:36:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 99.6 |
| a36a10d6-e13b-336b-b561-d01d027ba963 | -18.2739 | -56.6003 | 2024-10-17 04:36:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 49.7 |
| f0d130ca-6a26-314a-8fe5-b728d345c746 | -18.9491 | -54.5281 | 2024-10-17 04:36:52 | GOES-16 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 60.3 |
| 09436345-ae28-38dc-8b2a-8285571a3e7c | -2.9674 | -47.9931 | 2024-10-17 04:45:20 | GOES-16 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 58.4 |
| 9d092956-6dd7-300b-8a38-8b025c957521 | -3.3526 | -53.2112 | 2024-10-17 04:45:22 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 51.4 |
| dac4490a-fb8b-361c-8e50-23d53f7e7ab8 | -3.5086 | -51.1122 | 2024-10-17 04:45:23 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 63.7 |
| 91eb6254-8662-3363-a702-0082ef3e2500 | -3.908 | -42.402 | 2024-10-17 04:45:25 | GOES-16 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 100.8 |
| ab0b3bfc-d01a-3fb2-9be9-9328817d1507 | -3.9081 | -42.3784 | 2024-10-17 04:45:25 | GOES-16 | ESPERANTINA | PIAUÍ | Brasil | 2203701 | 22 | 33 | nan | nan | nan | Caatinga | 51.4 |
| 37f96ea5-19ff-3f43-881c-0e2d8a9caa65 | -3.9265 | -42.4246 | 2024-10-17 04:45:25 | GOES-16 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 64.0 |
| c0c562d2-9797-38bc-9aaa-bf31fb4a5e7f | -3.9267 | -42.401 | 2024-10-17 04:45:25 | GOES-16 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 133.8 |
| 85715be9-f33c-316f-a675-3716d43e6040 | -3.9268 | -42.3773 | 2024-10-17 04:45:25 | GOES-16 | ESPERANTINA | PIAUÍ | Brasil | 2203701 | 22 | 33 | nan | nan | nan | Caatinga | 42.6 |
| 34f7fdfb-73a3-37ea-a0aa-836ab11c2944 | -5.9788 | -45.3621 | 2024-10-17 04:45:37 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 73.1 |
| 8cd00c43-99a0-3855-8056-7d568fc667bb | -9.1552 | -61.9047 | 2024-10-17 04:45:55 | GOES-16 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 64.6 |
| 2a3162f5-11e8-336b-b00e-ae48c097c866 | -11.6566 | -64.8288 | 2024-10-17 04:46:10 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 59.6 |
| 244878a8-56f5-3ccf-ad28-addbeb0d7fd4 | -17.8049 | -57.4655 | 2024-10-17 04:46:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 76.2 |
| 19b264ab-6f5f-38d3-837b-5b599dbc65d9 | -17.8052 | -57.4449 | 2024-10-17 04:46:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 91.7 |
| 5bbca9f6-2b16-3cc8-b2f5-8998359eafc2 | -17.8444 | -57.4607 | 2024-10-17 04:46:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 74.1 |
| 1e207bf7-3333-35d7-9aec-188e325ee735 | -17.8641 | -57.4583 | 2024-10-17 04:46:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 100.3 |
| dd53eaf2-5361-3e12-9095-174d7df11175 | -18.2342 | -56.6055 | 2024-10-17 04:46:45 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 56.4 |
| fc48ebab-3441-30d5-b63b-22716b4a8e5e | -18.254 | -56.6029 | 2024-10-17 04:46:45 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 116.6 |
| fbd50e05-f033-3361-aba1-c1079a67222e | -18.2544 | -56.5821 | 2024-10-17 04:46:45 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 56.1 |
| 1f8bcfd2-755d-370f-bf4d-71b5d5247a3a | -2.9674 | -47.9931 | 2024-10-17 04:55:21 | GOES-16 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 60.6 |
| d17ad29c-02b4-314a-88f8-3f1933baf8df | -3.3526 | -53.2112 | 2024-10-17 04:55:24 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 66.0 |
| 3956ba08-ac5c-33fb-bc4c-fb951a79f33b | -3.7009 | -45.9 | 2024-10-17 04:55:25 | GOES-16 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 62.5 |
| b5c335b2-3fd3-3233-9cd2-a2aa2d281ada | -3.908 | -42.402 | 2024-10-17 04:55:26 | GOES-16 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 88.4 |
| 15bd6513-179e-31f7-b1e7-93156c28a686 | -3.9081 | -42.3784 | 2024-10-17 04:55:26 | GOES-16 | ESPERANTINA | PIAUÍ | Brasil | 2203701 | 22 | 33 | nan | nan | nan | Caatinga | 45.9 |
| de0a1914-c94b-342e-8feb-dfacde33ffc7 | -3.7575 | -45.741 | 2024-10-17 04:55:26 | GOES-16 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 62.8 |
| 6a08838f-b794-36ed-8784-3ebd190896b5 | -3.9267 | -42.401 | 2024-10-17 04:55:27 | GOES-16 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 90.3 |
| a18f4dde-cd70-3532-b262-06ce6baf38cc | -3.9268 | -42.3773 | 2024-10-17 04:55:27 | GOES-16 | ESPERANTINA | PIAUÍ | Brasil | 2203701 | 22 | 33 | nan | nan | nan | Caatinga | 46.4 |
| ddb8bef1-7bd7-34f8-9025-319f4cc1a80b | -5.9788 | -45.3621 | 2024-10-17 04:55:38 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 85.2 |
| 03deb4d2-12c5-3207-905c-6fabe7a8c962 | 1.2462 | -50.83278 | 2024-10-17 05:01:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 85c88081-3f08-3a8f-a0ab-d30f8d9b59cd | 0.29461 | -51.1592 | 2024-10-17 05:01:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2efe2e1c-8acb-3ef4-b8c1-0f34ce5d7116 | 0.29102 | -51.15976 | 2024-10-17 05:01:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fd3742d9-7c2a-3cc8-9003-ef0284db51a7 | 3.39881 | -51.31037 | 2024-10-17 05:01:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 95a3b442-cf04-3257-8b92-0c36b053d587 | 3.8668 | -51.80259 | 2024-10-17 05:01:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5b49554a-1a5a-3b07-8f88-58f0e087834b | 3.83964 | -51.76229 | 2024-10-17 05:01:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 3.8 |
| a4bd14a0-242f-3cb0-b13a-dd3c066ae31a | 3.54976 | -51.41853 | 2024-10-17 05:01:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 0.7 |
| badc39cf-debf-31fc-92d2-7d316430bd99 | 3.54633 | -51.41908 | 2024-10-17 05:01:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7cf1a8a2-7fc9-3f12-8bfe-1ac801c28490 | 2.2688 | -51.62653 | 2024-10-17 05:01:00 | NOAA-21 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 1.7 |
| af87d7ce-055d-3897-8f65-7f7799e81bcd | 1.0103 | -52.21817 | 2024-10-17 05:01:00 | NOAA-21 | PEDRA BRANCA DO AMAPARI | AMAPÁ | Brasil | 1600154 | 16 | 33 | nan | nan | nan | Amazônia | 17.0 |
| 439cb1ad-193f-3294-b3e3-5c862a91cf01 | 1.00953 | -52.21835 | 2024-10-17 05:01:00 | NOAA-21 | PEDRA BRANCA DO AMAPARI | AMAPÁ | Brasil | 1600154 | 16 | 33 | nan | nan | nan | Amazônia | 21.6 |
| bb8f4976-c052-3aeb-8c32-0c0736fff342 | 0.58194 | -51.58172 | 2024-10-17 05:01:00 | NOAA-21 | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 52c99a3a-fec8-36dd-a85d-c9a334e551fc | 0.58094 | -51.58157 | 2024-10-17 05:01:00 | NOAA-21 | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1df1107c-6f1a-36dd-ae22-20c855c38cda | 0.53981 | -51.88832 | 2024-10-17 05:01:00 | NOAA-21 | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 0.6 |


[Clique aqui para ver as próximas entradas](README36.md)
