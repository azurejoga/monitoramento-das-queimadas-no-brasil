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
| 11950b66-f9be-3e9f-8e13-2845d8e02fe6 | -14.47834 | -43.36233 | 2024-11-20 04:29:00 | NOAA-21 | PALMAS DE MONTE ALTO | BAHIA | Brasil | 2923407 | 29 | 33 | nan | nan | nan | Caatinga | 2.2 |
| fb4f649c-d2b5-3f05-b180-b58e65fd0619 | -11.10222 | -54.6376 | 2024-11-20 04:29:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 346a4354-3e26-3b8e-bc4a-9ac24abd40de | -12.53017 | -44.53141 | 2024-11-20 04:29:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 95837211-4556-3e4c-af93-1b73d27278b7 | -11.10871 | -54.62796 | 2024-11-20 04:29:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 08d2a569-7c77-3b0a-a2ed-deb4d3f99b66 | -11.1109 | -54.6204 | 2024-11-20 04:30:00 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 85.1 |
| e891084c-83e5-30bd-bf46-3a1a8263ee30 | -1.2017 | -53.6769 | 2024-11-20 04:30:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 56.7 |
| ae002481-ac08-3ccf-b353-0475a42b4e89 | -2.9116 | -53.0606 | 2024-11-20 04:30:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 81.7 |
| 17c4e9d4-ce6d-30d6-9ce8-c5baf4277319 | -2.7317 | -51.8176 | 2024-11-20 04:30:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 42.9 |
| 734b0d4b-7714-3c4c-ab99-58a418e93505 | -3.2014 | -54.3243 | 2024-11-20 04:30:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 47.6 |
| 5441493f-a8f0-3b0c-90c2-d12eb02cfe84 | -2.7501 | -51.8171 | 2024-11-20 04:30:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 60.3 |
| a3551249-89b0-31b1-921d-e953bb33956c | -2.9299 | -53.0805 | 2024-11-20 04:30:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 72.6 |
| 280630c8-078f-34eb-b8e3-c8c9d9c92b69 | -11.092 | -54.6221 | 2024-11-20 04:30:00 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 71.3 |
| 86ae1ed3-098c-39e8-8949-da62e394bc4a | -2.75 | -51.8377 | 2024-11-20 04:30:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 56.9 |
| c9d71215-365e-3184-9077-dda1fae48800 | -11.1106 | -54.6408 | 2024-11-20 04:30:00 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 62.7 |
| c02f66c1-2ab8-3fd5-a1bd-5ae05eaece1c | -11.0917 | -54.6425 | 2024-11-20 04:30:00 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 54.7 |
| 8d3693e5-8a98-36bb-8fda-e3162cba5979 | -2.93 | -53.0601 | 2024-11-20 04:30:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 97.3 |
| 62366eaf-d3a0-3c72-ad3d-02f1345fb42b | -2.9115 | -53.0809 | 2024-11-20 04:30:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 51.7 |
| 21eeb1f7-8d9a-35ef-9b59-60592d1743a7 | -18.39743 | -50.90394 | 2024-11-20 04:31:00 | NOAA-21 | CACHOEIRA ALTA | GOIÁS | Brasil | 5204102 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 07d119ce-6c0c-3acd-bf51-a279e69521b5 | -23.33749 | -46.77393 | 2024-11-20 04:31:00 | NOAA-21 | CAIEIRAS | SÃO PAULO | Brasil | 3509007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 046f7245-54bd-3315-b6e9-195caaececfd | -17.62697 | -57.59806 | 2024-11-20 04:31:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.0 |
| f5254328-f06d-3d85-847d-c31b7bccc186 | -20.20956 | -56.6251 | 2024-11-20 04:31:00 | NOAA-21 | MIRANDA | MATO GROSSO DO SUL | Brasil | 5005608 | 50 | 33 | nan | nan | nan | Pantanal | 3.1 |
| ff806615-0e33-3623-97ba-b61f7fb19642 | -16.44135 | -55.97873 | 2024-11-20 04:31:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 926addc2-e648-3f30-b59b-f8d6ac2d2f72 | -20.90201 | -43.82074 | 2024-11-20 04:31:00 | NOAA-21 | CARANDAÍ | MINAS GERAIS | Brasil | 3113206 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| ebe6606b-e995-3a62-987e-c05ae73f5706 | -17.00948 | -49.78167 | 2024-11-20 04:31:00 | NOAA-21 | CEZARINA | GOIÁS | Brasil | 5205455 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7f63b0ff-ac3d-3f37-9f83-7672904ab610 | -22.5418 | -48.81207 | 2024-11-20 04:31:00 | NOAA-21 | MACATUBA | SÃO PAULO | Brasil | 3528007 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 431f581f-7882-3367-9557-f9b17d6a7699 | -17.65639 | -56.46111 | 2024-11-20 04:31:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 95ac263b-9516-3029-b5f5-89521885daae | -17.62607 | -57.59654 | 2024-11-20 04:31:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.7 |
| 9e265ed3-25f2-3f0b-b5ed-1e75c54cca2e | -17.86102 | -44.70927 | 2024-11-20 04:31:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f4bed183-ce5b-3633-8826-e6d764db0470 | -20.053 | -57.20718 | 2024-11-20 04:31:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e70f0ebb-38f8-3a64-befd-31e4e29e711c | -17.62204 | -57.59699 | 2024-11-20 04:31:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.2 |
| c454ce0c-2268-31c9-8bd1-948a739d752b | -21.31556 | -56.01089 | 2024-11-20 04:31:00 | NOAA-21 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 540510fa-21b9-38a6-96db-2c6839d65f39 | -17.62816 | -57.59224 | 2024-11-20 04:31:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| d5c97519-8697-359f-aaf0-a19d2084b64f | -16.43682 | -55.97782 | 2024-11-20 04:31:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 3e74f91c-db63-39c3-a3bf-c3b51323ee53 | -16.0318 | -57.58245 | 2024-11-20 04:31:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d00e7bea-81ab-3478-97f6-0e8c0ba8b422 | -23.40608 | -46.55552 | 2024-11-20 04:31:00 | NOAA-21 | GUARULHOS | SÃO PAULO | Brasil | 3518800 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| e3772569-b8aa-373c-ab02-78a34d6bfcda | -24.23311 | -50.97229 | 2024-11-20 04:31:00 | NOAA-21 | ORTIGUEIRA | PARANÁ | Brasil | 4117305 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| c925997f-8d39-30b4-bb5f-0d783bb74ab9 | -20.49843 | -42.15335 | 2024-11-20 04:31:00 | NOAA-21 | DIVINO | MINAS GERAIS | Brasil | 3122009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| bfb35140-3030-3dd5-bab7-73ffa239ee8d | -21.00973 | -47.4485 | 2024-11-20 04:31:00 | NOAA-21 | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 82c865e7-d116-3941-ad8c-d5261373354c | -20.0484 | -57.20623 | 2024-11-20 04:31:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 20dc88a9-11bf-3c45-8597-17c108847db3 | -16.44265 | -52.5635 | 2024-11-20 04:31:00 | NOAA-21 | BALIZA | GOIÁS | Brasil | 5203104 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e86489c7-a3f5-3a3b-8798-71d33fed40f2 | -17.61101 | -57.38941 | 2024-11-20 04:31:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 958aad3d-b6c8-3438-bbdf-2e5bd8404f67 | -21.19442 | -44.93642 | 2024-11-20 04:31:00 | NOAA-21 | IJACI | MINAS GERAIS | Brasil | 3130408 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| cb6d056e-28e2-31b0-baee-17b0cb56679e | -21.00625 | -47.44797 | 2024-11-20 04:31:00 | NOAA-21 | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 0beb2663-8631-35d8-89d7-7751404b329a | -22.30936 | -49.76745 | 2024-11-20 04:31:00 | NOAA-21 | GARÇA | SÃO PAULO | Brasil | 3516705 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| a6b578a0-faf1-355e-bee6-3325b3be96d4 | -19.30958 | -55.20784 | 2024-11-20 04:31:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 722f569d-ffea-3925-a844-37a549b82ff9 | -21.00917 | -47.45256 | 2024-11-20 04:31:00 | NOAA-21 | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 4e02deea-4309-3ec7-ad3d-dc535b138bf2 | -17.62115 | -57.59547 | 2024-11-20 04:31:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.7 |
| d7085b6f-96ca-3dcb-a332-1b805ac819d6 | -22.5131 | -47.71763 | 2024-11-20 04:31:00 | NOAA-21 | CHARQUEADA | SÃO PAULO | Brasil | 3511706 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 7b831ea5-b261-3b3b-b1ad-4886387f3ad1 | -19.50992 | -48.40831 | 2024-11-20 04:31:00 | NOAA-21 | VERÍSSIMO | MINAS GERAIS | Brasil | 3171105 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1533f6e6-4539-303f-9461-0a60fed99fe4 | -20.07915 | -50.73085 | 2024-11-20 04:31:00 | NOAA-21 | SANTA ALBERTINA | SÃO PAULO | Brasil | 3545704 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 2b4030b9-626d-3c91-a4ba-73f3155a8976 | -23.63376 | -46.42483 | 2024-11-20 04:31:00 | NOAA-21 | SÃO PAULO | SÃO PAULO | Brasil | 3550308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| f3172012-9c01-3067-818f-558900520c58 | -18.18513 | -42.82961 | 2024-11-20 04:31:00 | NOAA-21 | COLUNA | MINAS GERAIS | Brasil | 3116803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| b387f857-0fbd-3917-8257-d9fee1dfdef1 | -20.32787 | -48.81685 | 2024-11-20 04:31:00 | NOAA-21 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b3b6f7b1-9935-30b7-9d52-438ecb93db2c | -20.41878 | -43.55494 | 2024-11-20 04:31:00 | NOAA-21 | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 4a3e63d8-00e6-31eb-9160-846d05773fe7 | -16.43897 | -52.56273 | 2024-11-20 04:31:00 | NOAA-21 | BALIZA | GOIÁS | Brasil | 5203104 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f5117eb3-8a8b-30e6-8531-45ef7bc0abc6 | -22.30604 | -49.76686 | 2024-11-20 04:31:00 | NOAA-21 | GARÇA | SÃO PAULO | Brasil | 3516705 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 63d5cd6a-beb9-3afb-b7bf-0a757f003ba2 | -17.60232 | -57.561 | 2024-11-20 04:31:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 4b969f8b-748f-393c-ad57-a0834fd48536 | -20.21256 | -56.62844 | 2024-11-20 04:31:00 | NOAA-21 | MIRANDA | MATO GROSSO DO SUL | Brasil | 5005608 | 50 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 0da06dab-af0b-3f47-a294-548f06c0cbba | -16.02681 | -57.58099 | 2024-11-20 04:31:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b3788317-f0c1-31bf-921e-753e9b4d6510 | -17.60117 | -57.56681 | 2024-11-20 04:31:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 2b6dffe5-9043-3a54-a925-cbe9f7c7a617 | -20.20867 | -56.62971 | 2024-11-20 04:31:00 | NOAA-21 | MIRANDA | MATO GROSSO DO SUL | Brasil | 5005608 | 50 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 80a52092-4b34-3e4e-8b54-c3d8f2c170e0 | -17.55483 | -57.4664 | 2024-11-20 04:31:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 8cb9019f-de06-3929-b389-0b406296abaa | -20.20816 | -56.62746 | 2024-11-20 04:31:00 | NOAA-21 | MIRANDA | MATO GROSSO DO SUL | Brasil | 5005608 | 50 | 33 | nan | nan | nan | Pantanal | 3.0 |
| da0d87a7-2a79-3377-9b10-6eabfcef75a0 | -16.43774 | -55.97301 | 2024-11-20 04:31:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| c6b899d4-dad7-39ea-b2aa-b66ee3e519be | -20.0774 | -57.18071 | 2024-11-20 04:31:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 340970bd-584c-3360-bb09-9b2e31bcd257 | -19.02206 | -57.62376 | 2024-11-20 04:31:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 25144344-7cf8-34b6-a27d-64d2f998c092 | -20.33121 | -48.81741 | 2024-11-20 04:31:00 | NOAA-21 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d85ea4ab-11ed-33e5-ac75-d6c1b6576d0e | -23.63058 | -46.42581 | 2024-11-20 04:31:00 | NOAA-21 | SÃO PAULO | SÃO PAULO | Brasil | 3550308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| c2645b57-9261-3a6c-8aaf-d01c49c48061 | -17.85718 | -44.70867 | 2024-11-20 04:31:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3801b203-9911-3bd1-85e5-83bc6900a370 | -27.7748 | -54.43726 | 2024-11-20 04:33:00 | NOAA-21 | SANTA ROSA | RIO GRANDE DO SUL | Brasil | 4317202 | 43 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 7b4ad0f7-033f-3a38-88b9-86334d56f1e9 | -2.75 | -51.8377 | 2024-11-20 04:40:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 80.2 |
| a9438378-2032-3cb5-b3e3-a1034ce86b64 | -2.9115 | -53.0809 | 2024-11-20 04:40:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 61.2 |
| b3f126d1-9145-3d5b-bc9b-d243bd8fc5d6 | -11.1106 | -54.6408 | 2024-11-20 04:40:00 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 61.7 |
| c9165827-f12b-3ad9-8a62-ceea6b379308 | -11.092 | -54.6221 | 2024-11-20 04:40:00 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 67.0 |
| 200c012b-816e-36e7-a8b5-5115420e9277 | -11.1109 | -54.6204 | 2024-11-20 04:40:00 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 80.2 |
| 536a962b-c4c2-37ff-bf4f-dd955cc9fbd8 | -2.9116 | -53.0606 | 2024-11-20 04:40:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 98.6 |
| 1404133a-a948-3548-b2e5-bcad8f78e958 | -2.9299 | -53.0805 | 2024-11-20 04:40:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 68.8 |
| 904a295c-15a5-39c3-a1c5-514d5636fa28 | -1.2017 | -53.6769 | 2024-11-20 04:40:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 68.3 |
| c1eb6f88-194d-3411-938c-ea2b02223b76 | -2.93 | -53.0601 | 2024-11-20 04:40:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 76.5 |
| eb406130-3b35-3b9a-b3fe-4cebe3a84213 | -4.4404 | -46.5975 | 2024-11-20 04:40:00 | GOES-16 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 61.2 |
| 6bb201fe-4927-3c29-b440-2b653d7d0372 | -2.7501 | -51.8171 | 2024-11-20 04:40:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 87.1 |
| 0514069f-ec3a-364f-9eef-d2a1cab95e9a | -4.4405 | -46.5754 | 2024-11-20 04:40:00 | GOES-16 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 60.5 |
| a8a63dfb-c068-36a2-80f7-3da29bca9320 | -11.0917 | -54.6425 | 2024-11-20 04:40:00 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 53.2 |
| 114ba667-fe1b-3bdf-a893-944bfc76a83d | -6.01045 | -38.65509 | 2024-11-20 04:40:00 | AQUA_M-M | JAGUARIBE | CEARÁ | Brasil | 2306900 | 23 | 33 | nan | nan | nan | Caatinga | 21.1 |
| e540d93a-a305-32a1-b174-dfc6aece1af8 | -6.01043 | -38.65003 | 2024-11-20 04:40:00 | AQUA_M-M | JAGUARIBE | CEARÁ | Brasil | 2306900 | 23 | 33 | nan | nan | nan | Caatinga | 12.3 |
| 1d122268-83c0-3a16-b488-1ee5ed5d6527 | -6.00858 | -38.66166 | 2024-11-20 04:40:00 | AQUA_M-M | JAGUARIBE | CEARÁ | Brasil | 2306900 | 23 | 33 | nan | nan | nan | Caatinga | 9.6 |
| c5b1ac7e-e81e-3274-9865-c42442a6b9d1 | -11.06536 | -41.61051 | 2024-11-20 04:42:00 | AQUA_M-M | SÃO GABRIEL | BAHIA | Brasil | 2929255 | 29 | 33 | nan | nan | nan | Caatinga | 14.8 |
| 6d75b39b-4276-3e80-967d-27d8f6de4881 | -11.03345 | -44.5713 | 2024-11-20 04:42:00 | AQUA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 44.8 |
| 9068bd26-ba9a-3196-a57d-32031683e249 | -11.03071 | -44.56597 | 2024-11-20 04:42:00 | AQUA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 51.8 |
| ac48b0d2-918a-350e-87cb-c0f2cbc9dbaa | -6.92616 | -41.19065 | 2024-11-20 04:42:00 | AQUA_M-M | SANTO ANTÔNIO DE LISBOA | PIAUÍ | Brasil | 2209401 | 22 | 33 | nan | nan | nan | Caatinga | 50.2 |
| 7cd9acf4-65f7-3f72-8824-8a8123f75e59 | -11.05514 | -41.61764 | 2024-11-20 04:42:00 | AQUA_M-M | SÃO GABRIEL | BAHIA | Brasil | 2929255 | 29 | 33 | nan | nan | nan | Caatinga | 15.4 |
| 8593781c-1745-372c-aa88-7f5bacbcb3d0 | -11.06274 | -41.62584 | 2024-11-20 04:42:00 | AQUA_M-M | SÃO GABRIEL | BAHIA | Brasil | 2929255 | 29 | 33 | nan | nan | nan | Caatinga | 9.5 |
| c46572b0-df91-395e-8b9a-a7127ed097f7 | -18.16566 | -39.63387 | 2024-11-20 04:44:00 | AQUA_M-M | MUCURI | BAHIA | Brasil | 2922003 | 29 | 33 | nan | nan | nan | Mata Atlântica | 8.4 |
| f606cdeb-5eab-3d8f-8683-be34272e7b2a | -1.16045 | -46.74937 | 2024-11-20 04:48:00 | NPP-375D | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f159d2e8-0afe-39c5-9074-14f535e6eeb3 | -0.07972 | -51.46642 | 2024-11-20 04:48:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 425a29d4-bf9e-3532-8d11-37ce4c423915 | -0.30079 | -51.49762 | 2024-11-20 04:48:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 222c90a1-1bee-34a2-880f-1ab5e9707f2e | -0.39943 | -51.54124 | 2024-11-20 04:48:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bbfc8186-0679-32d7-98d0-3270c5afa63d | -0.35811 | -51.60917 | 2024-11-20 04:48:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0592e9f6-716a-321b-8c34-81345dc544e9 | -0.91179 | -47.38945 | 2024-11-20 04:48:00 | NPP-375D | SANTARÉM NOVO | PARÁ | Brasil | 1506906 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 494b239b-7a96-3b04-aa37-8ff35fc2c880 | -0.08783 | -51.47462 | 2024-11-20 04:48:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |


[Clique aqui para ver as próximas entradas](README41.md)
