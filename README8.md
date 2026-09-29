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

## Dados Diários - Página 8

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d6169a55-94e8-301a-8afb-ca07dfa7c1f0 | -3.8202 | -55.899 | 2026-09-29 02:40:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 75.8 |
| 440e0266-26ff-301a-97d7-ef31d83a2000 | -5.6083 | -44.9811 | 2026-09-29 02:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 73.0 |
| f44543ea-c118-3ac4-9d2d-52caa7362480 | -3.8202 | -55.9187 | 2026-09-29 02:40:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 57.1 |
| 4a46e3f6-b2cd-3a62-914e-d92b11be3f86 | -7.8483 | -45.8363 | 2026-09-29 02:40:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 62.2 |
| cba11331-6108-34bd-8727-f1ffed2cb052 | -11.4012 | -54.0417 | 2026-09-29 02:40:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 93.9 |
| 639095de-ef46-3ec1-985e-39a9992bfa87 | -12.9456 | -46.652 | 2026-09-29 02:40:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 72.8 |
| 3a21aeff-f9b0-324c-acfb-ca73e9085894 | -11.3823 | -54.0434 | 2026-09-29 02:40:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 141.3 |
| 5492b796-b418-363b-8ca8-88e3a7d102f7 | 1.675 | -55.9028 | 2026-09-29 02:40:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 55.0 |
| eafb5552-86e8-3f12-a3a8-2973037aa212 | -5.6081 | -45.0038 | 2026-09-29 02:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 149.4 |
| 26b4bfd8-bb11-3201-a411-92729f2f2837 | -15.2314 | -43.2784 | 2026-09-29 02:40:00 | GOES-19 | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 84.8 |
| d09c3416-5ef8-3d3e-97ea-abe7bbcde1a7 | -15.2511 | -43.2743 | 2026-09-29 02:40:00 | GOES-19 | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 98.2 |
| 7a4d2923-abd4-3bde-b519-fc56a6fa0f75 | -7.8486 | -45.8138 | 2026-09-29 02:40:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 159.4 |
| db6230be-e914-3d89-a13e-ddb1bc7c88e2 | -3.8386 | -55.8985 | 2026-09-29 02:40:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 55.7 |
| fc4bfe81-d930-3003-95d1-a21c7b1310c8 | -9.177 | -61.4073 | 2026-09-29 02:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 72.1 |
| 2c21defc-9d22-3cee-8d57-ed8736065edd | -7.8297 | -45.8156 | 2026-09-29 02:40:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 120.3 |
| 331fc0da-4937-31e3-b34c-94194757724f | -7.7025 | -48.8667 | 2026-09-29 02:40:00 | GOES-19 | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 94.0 |
| 2405be77-e8da-3f4d-9890-4741aaac4c52 | -15.4585 | -46.1367 | 2026-09-29 02:40:00 | GOES-19 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 70.7 |
| 433c4353-ef13-3dcd-8ff9-135ab304e9bb | -9.9595 | -50.1431 | 2026-09-29 02:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 57.0 |
| 3ca39a47-855d-3c86-b11b-8a232472af40 | -12.946 | -46.6293 | 2026-09-29 02:40:00 | GOES-19 | NOVO ALEGRE | TOCANTINS | Brasil | 1715150 | 17 | 33 | nan | nan | nan | Cerrado | 63.7 |
| 4537b497-f6db-3c58-8793-aa039fc3a296 | -9.1584 | -61.4082 | 2026-09-29 02:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 67.8 |
| b009da89-515e-3a82-953b-0a4f5c896500 | -12.0314 | -50.9656 | 2026-09-29 02:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 298.0 |
| 15233a19-ece5-3f96-8749-3e69d69db9a8 | -10.8424 | -60.7622 | 2026-09-29 02:50:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 47.8 |
| de35db31-f5cc-31a1-8abd-9b1794d8aeaf | -5.6081 | -45.0038 | 2026-09-29 02:50:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 122.6 |
| 0d9cf67d-b03c-3e5c-893a-04060a99dcbc | -12.0126 | -50.9464 | 2026-09-29 02:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 116.2 |
| 9c53a8a6-a656-3426-b9ca-ce552fdf7130 | -11.1775 | -44.7832 | 2026-09-29 02:50:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 56.5 |
| c8df95d2-6826-34f0-aad0-fd7f54fd1ae5 | -9.177 | -61.4073 | 2026-09-29 02:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 83.5 |
| bc22fa90-c7f1-3b19-a9aa-5b6fc26c3e98 | -12.9456 | -46.652 | 2026-09-29 02:50:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 85.6 |
| d4908996-1156-3419-80ef-9d12e740a066 | -12.0508 | -50.942 | 2026-09-29 02:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 100.9 |
| 60b0aed6-7d2c-32eb-ba49-c22baa566ab0 | -3.8202 | -55.9187 | 2026-09-29 02:50:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 70.8 |
| c626d044-579e-35c2-bbed-7e4d938e4b96 | -7.8486 | -45.8138 | 2026-09-29 02:50:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 156.9 |
| 0ebf1b68-5033-362a-823d-c98c2f94b001 | -12.946 | -46.6293 | 2026-09-29 02:50:00 | GOES-19 | NOVO ALEGRE | TOCANTINS | Brasil | 1715150 | 17 | 33 | nan | nan | nan | Cerrado | 57.2 |
| d769c350-6150-3785-85b0-060993af1017 | 1.6566 | -55.903 | 2026-09-29 02:50:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 62.2 |
| c8cf945c-6d5f-3bde-8bb2-2176c65b6e2c | 1.675 | -55.8831 | 2026-09-29 02:50:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 93.8 |
| 9e12530c-2413-3caa-bb41-ea66ae7a7e36 | -12.0123 | -50.9678 | 2026-09-29 02:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 115.4 |
| 130ccaa0-8b03-3a33-92af-e5afb3d0b24f | -12.0317 | -50.9442 | 2026-09-29 02:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 258.4 |
| ede31bc3-692e-381b-b4ae-e5557adbcde9 | -11.3823 | -54.0434 | 2026-09-29 02:50:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 74.2 |
| 8fd0453f-388a-3a03-8fa7-c0eff9f15adb | -7.4074 | -40.2299 | 2026-09-29 02:50:00 | GOES-19 | IPUBI | PERNAMBUCO | Brasil | 2607307 | 26 | 33 | nan | nan | nan | Caatinga | 58.4 |
| 30d6c997-53a5-385f-b623-ebb10c5f4862 | -15.2517 | -43.2501 | 2026-09-29 02:50:00 | GOES-19 | MONTE AZUL | MINAS GERAIS | Brasil | 3142908 | 31 | 33 | nan | nan | nan | Caatinga | 63.1 |
| 710e0d16-7d0e-3c31-8d9f-d2b6d87d1c53 | -15.2511 | -43.2743 | 2026-09-29 02:50:00 | GOES-19 | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 171.9 |
| fafeabd1-3709-3079-89c9-97916d9c964d | -9.4819 | -66.7836 | 2026-09-29 02:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 58.6 |
| 50401421-8b82-3adf-b730-26ad30f9e3de | 1.6567 | -55.8833 | 2026-09-29 02:50:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 100.5 |
| e9ec0d21-c8ab-3325-8c41-41d7a136d868 | -5.6268 | -45.0025 | 2026-09-29 02:50:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 68.1 |
| 0be86774-04ae-3862-9bfe-97fa7d9da5f2 | -12.0504 | -50.9634 | 2026-09-29 02:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 100.5 |
| c2cc1a8f-7f87-3eca-8c24-1d4770825cee | -9.9595 | -50.1431 | 2026-09-29 02:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 56.7 |
| ad73ac56-adb0-3730-a1a7-64f00bec102b | -7.8297 | -45.8156 | 2026-09-29 02:50:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 142.6 |
| 1022d63d-38c9-33eb-9f65-323ff635a783 | -12.7606 | -50.6857 | 2026-09-29 02:50:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 76.8 |
| 429b5dbc-acd4-3211-86c3-c7c8fa311423 | -3.8202 | -55.899 | 2026-09-29 02:50:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 76.9 |
| 882d2658-2485-341a-9464-0b1481501975 | 1.675 | -55.9028 | 2026-09-29 02:50:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 81.7 |
| 0a462a40-bac4-39c1-8353-b62e43a4f3e7 | -7.7025 | -48.8667 | 2026-09-29 02:50:00 | GOES-19 | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 55.7 |
| f258464a-54c1-3c3f-9566-48014af65d16 | -15.2314 | -43.2784 | 2026-09-29 02:50:00 | GOES-19 | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 61.4 |
| 53f0347a-a5be-36c2-afff-6f62b56329a2 | -10.8424 | -60.7622 | 2026-09-29 03:00:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 48.9 |
| 183535d8-1082-3ad7-9312-972f000eee97 | -12.9456 | -46.652 | 2026-09-29 03:00:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 66.2 |
| 6304db3c-3c0f-3e85-a2de-7ffa70786af5 | -12.0508 | -50.942 | 2026-09-29 03:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 76.8 |
| 2700e2b6-d32c-3579-9f24-aa06c64523e3 | -9.4819 | -66.7836 | 2026-09-29 03:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 49.1 |
| 31676865-c282-33f1-b5aa-d7c8ef7732aa | -12.0126 | -50.9464 | 2026-09-29 03:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 116.5 |
| 0c0540c8-312b-30a7-b1b4-9f466a8cf6d0 | -12.0123 | -50.9678 | 2026-09-29 03:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 95.3 |
| df0b1598-52a4-3edf-aae9-752a39a921c1 | 1.6567 | -55.8833 | 2026-09-29 03:00:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 115.1 |
| 68cf09ea-edf8-3408-9bc7-00e5ce491810 | -3.8202 | -55.899 | 2026-09-29 03:00:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 79.2 |
| e754b286-64a3-3b91-9b04-94810ae1a942 | -5.6081 | -45.0038 | 2026-09-29 03:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 93.1 |
| d81c0f9c-d412-3d94-83b6-7bf1e1f3a3f4 | -12.0314 | -50.9656 | 2026-09-29 03:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 142.7 |
| 60bb2a1f-c857-3458-b840-14e51c6a6c8d | -7.8297 | -45.8156 | 2026-09-29 03:00:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 113.2 |
| 3afe3320-bb48-3cc1-b96b-20ea6d9212c5 | -15.2517 | -43.2501 | 2026-09-29 03:00:00 | GOES-19 | MONTE AZUL | MINAS GERAIS | Brasil | 3142908 | 31 | 33 | nan | nan | nan | Caatinga | 72.8 |
| 139d2f23-2815-3249-9408-f102a86843df | -15.2314 | -43.2784 | 2026-09-29 03:00:00 | GOES-19 | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 66.4 |
| 7227f2f3-9041-3fbb-8573-da5c0fe71d3c | 1.675 | -55.8831 | 2026-09-29 03:00:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 76.5 |
| 978bbde1-56f5-3230-a16d-ebb7f70d22a4 | -12.0317 | -50.9442 | 2026-09-29 03:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 182.4 |
| ef78fafa-9172-3862-bce0-2d177b3fd664 | -12.761 | -50.6643 | 2026-09-29 03:00:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 73.0 |
| 71539b35-791c-350a-9131-4295dfa4d0cf | -12.0618 | -50.2127 | 2026-09-29 03:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 74.2 |
| 577ec6f6-9b04-3214-93a0-19ab313ef411 | -10.8426 | -60.7429 | 2026-09-29 03:00:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 47.0 |
| cd93f2ec-a617-3099-854d-45eec13cfc9a | -12.7606 | -50.6857 | 2026-09-29 03:00:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 75.3 |
| 039ba358-bcbc-3724-8108-cc57984faef1 | -3.8202 | -55.9187 | 2026-09-29 03:00:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 61.6 |
| 196b2c73-5765-3ca7-9bfc-d9265cb4e5e1 | -11.1775 | -44.7832 | 2026-09-29 03:00:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 53.6 |
| 3fb143d0-dd26-3d56-bc97-008c01ced57d | -7.8486 | -45.8138 | 2026-09-29 03:00:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 122.4 |
| 5cbb1ef0-b213-3a34-8ad8-0faae676060b | -9.177 | -61.4073 | 2026-09-29 03:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 87.1 |
| 671b814c-2790-34e3-80ae-dda21a21ea65 | -15.2511 | -43.2743 | 2026-09-29 03:00:00 | GOES-19 | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 201.8 |
| 3b20881d-2bc8-3a29-b785-0df688182114 | -9.9595 | -50.1431 | 2026-09-29 03:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 52.3 |
| 3a2ba1e2-b0d1-3bed-a567-811d78b01287 | -5.6083 | -44.9811 | 2026-09-29 03:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 58.1 |
| a1012306-2060-31c9-bffb-d2bcb2439144 | -12.012 | -50.9891 | 2026-09-29 03:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 167.3 |
| a088db2f-3648-3bba-91a6-42c555712b68 | -11.9929 | -50.9913 | 2026-09-29 03:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 73.0 |
| 249b8830-55ba-3cc1-b4ae-a16c200bbef0 | -3.8202 | -55.9187 | 2026-09-29 03:10:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 54.5 |
| 69836a20-b2a7-380a-a370-155cf7bbc95d | -7.8297 | -45.8156 | 2026-09-29 03:10:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 126.5 |
| bd59d623-de10-39ee-a364-49189fecfb5e | -12.0123 | -50.9678 | 2026-09-29 03:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 89.9 |
| e87b3205-5843-31c9-834c-15261659397c | -9.9595 | -50.1431 | 2026-09-29 03:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 53.7 |
| 297b6c23-f5c8-326f-b220-17111ccb38a8 | -7.8486 | -45.8138 | 2026-09-29 03:10:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 131.3 |
| 210753bd-b406-3c38-a53a-8781ae696d0b | -11.4307 | -43.4358 | 2026-09-29 03:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 106.9 |
| b0345f6f-db68-3f29-863c-8b11f8a776be | -5.6081 | -45.0038 | 2026-09-29 03:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 98.8 |
| 859cb896-25f4-3ebf-91f7-cbe51761e23b | -10.8426 | -60.7429 | 2026-09-29 03:10:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 45.7 |
| 3327c118-dfbe-32bf-aa63-2446e1f7a2c3 | -12.9456 | -46.652 | 2026-09-29 03:10:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 60.4 |
| 73a4dca8-fd29-3c09-bcfd-34a5820f97fa | -7.4074 | -40.2299 | 2026-09-29 03:10:00 | GOES-19 | IPUBI | PERNAMBUCO | Brasil | 2607307 | 26 | 33 | nan | nan | nan | Caatinga | 57.7 |
| f423780f-0a60-32f8-bae9-0414ee82b4cd | -6.2947 | -43.6427 | 2026-09-29 03:10:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 108.8 |
| 8791261b-3424-3483-9e71-0b526c4618b9 | -12.761 | -50.6643 | 2026-09-29 03:10:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 89.0 |
| bad402d6-89bb-31f6-80ca-0c8f2bc5133f | -15.2314 | -43.2784 | 2026-09-29 03:10:00 | GOES-19 | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 63.9 |
| 66b00394-61f6-3f71-9e15-e7f89cf0d36c | -11.4115 | -43.4388 | 2026-09-29 03:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 91.7 |
| e7fa21f6-2751-33ed-9dfe-ebc3e9c10c83 | -12.0314 | -50.9656 | 2026-09-29 03:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 61.1 |
| 73d14057-a54d-3bdf-9352-aa5a9465a553 | 1.6567 | -55.8833 | 2026-09-29 03:10:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 71.3 |
| 8e475458-74be-375e-95f4-d12a9a3880c9 | -11.4495 | -43.4566 | 2026-09-29 03:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 82.6 |
| cdbc5bc4-7976-3a7e-98a0-9a01d5aa1672 | -15.2511 | -43.2743 | 2026-09-29 03:10:00 | GOES-19 | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 200.5 |
| 99c0b59e-047c-330e-aa58-9a55ebc278ad | -15.2517 | -43.2501 | 2026-09-29 03:10:00 | GOES-19 | MONTE AZUL | MINAS GERAIS | Brasil | 3142908 | 31 | 33 | nan | nan | nan | Caatinga | 78.9 |
| 867e3da5-b28b-3cc3-bf25-c37700b4ad16 | -11.4298 | -43.4833 | 2026-09-29 03:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 73.6 |
| 9ed80b48-612e-3717-bc5b-5aac2eef8767 | -11.411 | -43.4625 | 2026-09-29 03:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 80.6 |
| fd281252-7af9-374d-b944-6984e3b275db | -7.4077 | -40.2051 | 2026-09-29 03:10:00 | GOES-19 | IPUBI | PERNAMBUCO | Brasil | 2607307 | 26 | 33 | nan | nan | nan | Caatinga | 55.3 |


[Clique aqui para ver as próximas entradas](README9.md)
