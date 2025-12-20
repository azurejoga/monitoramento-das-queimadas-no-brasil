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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5202fcc3-8be7-36cb-bef6-4999a98061a7 | -3.86154 | -40.64814 | 2025-12-20 04:50:00 | NPP-375D | CARIRÉ | CEARÁ | Brasil | 2303105 | 23 | 33 | nan | nan | nan | Caatinga | 5.0 |
| 1b700272-7627-3f2b-9120-4e7e22df9cab | -9.57871 | -44.59948 | 2025-12-20 04:50:00 | NPP-375D | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 7.4 |
| b0e1e3cb-505c-38ff-900c-8a4d6f845f13 | -4.3371 | -39.36372 | 2025-12-20 04:50:00 | NPP-375D | CANINDÉ | CEARÁ | Brasil | 2302800 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 0a3ba9cc-a7ff-3564-91f1-7d2e1c64d45e | -3.86209 | -40.6443 | 2025-12-20 04:50:00 | NPP-375D | CARIRÉ | CEARÁ | Brasil | 2303105 | 23 | 33 | nan | nan | nan | Caatinga | 5.0 |
| 7ae100c3-5bf6-3209-b427-f919a431e48f | -2.45851 | -48.2289 | 2025-12-20 04:50:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 0bed2837-27a4-32a1-8454-9ad9467036be | -3.89924 | -41.69725 | 2025-12-20 04:50:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 4.9 |
| 06287510-844b-364e-bd02-10cd73cb7e15 | -3.86052 | -40.64191 | 2025-12-20 04:50:00 | NPP-375D | CARIRÉ | CEARÁ | Brasil | 2303105 | 23 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 51bf62a5-1df2-331b-9e92-ebb987d8ce48 | -3.86561 | -40.64652 | 2025-12-20 04:50:00 | NPP-375D | CARIRÉ | CEARÁ | Brasil | 2303105 | 23 | 33 | nan | nan | nan | Caatinga | 4.2 |
| c5e34fd0-bf43-3b1c-b247-570179a74d4a | -9.57335 | -44.60363 | 2025-12-20 04:50:00 | NPP-375D | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 6d8dfe7c-7dbc-3f66-976b-f64af12e6873 | -3.90452 | -41.698 | 2025-12-20 04:50:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 7.5 |
| e413417b-ecaf-3cea-bd7a-94f3b22f68a7 | -9.57804 | -44.60434 | 2025-12-20 04:50:00 | NPP-375D | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 11.6 |
| b3b83925-61c9-3dc6-9651-b7fc7f7bc315 | -2.82406 | -48.6132 | 2025-12-20 04:50:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7cc1c1ae-f31c-3b0d-ade0-24572286a2f6 | -3.86619 | -40.64268 | 2025-12-20 04:50:00 | NPP-375D | CARIRÉ | CEARÁ | Brasil | 2303105 | 23 | 33 | nan | nan | nan | Caatinga | 2.5 |
| fc27dc74-4574-384b-93f0-cc720548659d | -9.57268 | -44.60846 | 2025-12-20 04:50:00 | NPP-375D | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 7d8638b9-7d40-3558-a98e-537679ba9cea | -9.58342 | -44.6001 | 2025-12-20 04:50:00 | NPP-375D | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9638c419-1617-3141-be05-6ba735ea1c47 | -5.45962 | -40.49991 | 2025-12-20 04:50:00 | NPP-375D | INDEPENDÊNCIA | CEARÁ | Brasil | 2305605 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 1e2501d3-8b55-3830-8746-e28fee053104 | -3.90405 | -41.70117 | 2025-12-20 04:50:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 6.4 |
| 05016e8f-f064-35c2-8705-5e1c69bc76af | -9.56397 | -44.60217 | 2025-12-20 04:50:00 | NPP-375D | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 4.4 |
| de089207-0134-3c78-aa7b-c7d1d75b19a3 | -20.30986 | -57.27885 | 2025-12-20 04:53:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.9 |
| c4dd732b-e9e9-33ce-85c8-4e1a56df873f | -11.15512 | -43.31173 | 2025-12-20 04:53:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 3ba05d16-f628-36e6-9c9f-35e1770d0989 | -9.72112 | -60.20425 | 2025-12-20 04:53:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 6.1 |
| f7f853cf-e872-301f-8e91-fd9b2c3d137d | -11.16079 | -43.30921 | 2025-12-20 04:53:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 3.8 |
| f3d8ba3b-0bbd-33fc-bf93-b5c9862830bb | -11.16486 | -43.31257 | 2025-12-20 04:53:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 6358ef9d-a5a5-3ffe-be91-49ab6135817e | -20.45356 | -56.55211 | 2025-12-20 04:53:00 | NPP-375D | BODOQUENA | MATO GROSSO DO SUL | Brasil | 5002159 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 38b9d4fb-b160-3b9e-a255-93dcdd33b8ff | -13.94527 | -44.35332 | 2025-12-20 04:53:00 | NPP-375D | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b86837ca-3d4d-37d7-975b-f77c284b0c56 | -11.16527 | -43.30932 | 2025-12-20 04:53:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 10943827-e70b-3e22-a9b0-b80052933a63 | -20.45701 | -56.55277 | 2025-12-20 04:53:00 | NPP-375D | BODOQUENA | MATO GROSSO DO SUL | Brasil | 5002159 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ba0715ef-6dad-350b-903e-5a99b27742fc | -9.7222 | -60.20189 | 2025-12-20 04:53:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 32e36b29-d5b6-3dfa-82e4-567d87723ce4 | -13.38938 | -44.37848 | 2025-12-20 04:53:00 | NPP-375D | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 602edfe3-ac64-33fb-ac4c-230559e4df4c | -13.39158 | -44.37246 | 2025-12-20 04:53:00 | NPP-375D | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 62b5186c-2acf-3787-9673-4db3e91ee8a5 | -20.81213 | -56.04956 | 2025-12-20 04:53:00 | NPP-375D | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d6c7ec4d-6840-39cc-b978-af9904f6c201 | -20.30045 | -56.55325 | 2025-12-20 04:53:00 | NPP-375D | MIRANDA | MATO GROSSO DO SUL | Brasil | 5005608 | 50 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 0d0b0ae8-2690-3882-a286-69697f2b54ac | -13.41975 | -42.17017 | 2025-12-20 04:53:00 | NPP-375D | ÉRICO CARDOSO | BAHIA | Brasil | 2900504 | 29 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 028eacad-6bbf-3751-8170-3d54f10a6dd3 | -21.20565 | -56.9302 | 2025-12-20 04:53:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b8baead4-a806-3558-837f-c6482d5be11e | -13.94564 | -44.35032 | 2025-12-20 04:53:00 | NPP-375D | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| fc7db6ac-634b-375f-841d-649b4ebb07d8 | -11.16604 | -43.30994 | 2025-12-20 04:53:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| a77b6a97-416f-31c4-9f7e-fc0dbc48ad98 | -11.16037 | -43.31245 | 2025-12-20 04:53:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 1f0d4c27-360f-3a37-acae-5008aa0d1b75 | -13.61335 | -44.32868 | 2025-12-20 04:53:00 | NPP-375D | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 0.3 |
| e92ad712-bc06-3d64-9d61-82e759746ca1 | -13.3901 | -44.37251 | 2025-12-20 04:53:00 | NPP-375D | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ec0b8138-f2da-3d57-bc60-0f8527a6f41f | -20.32302 | -55.92164 | 2025-12-20 04:53:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.7 |
| d6329f0a-5b2a-3674-ac09-93e25794f633 | -20.31059 | -57.27463 | 2025-12-20 04:53:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 54492b36-b99e-3822-b30b-f353d0292b3e | -21.20147 | -56.93367 | 2025-12-20 04:53:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a061bbda-10d8-3f13-a2a0-748a63063bc6 | -11.15994 | -43.31569 | 2025-12-20 04:53:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 5.4 |
| 20db995b-d5de-3dcb-a2fd-4b395aa35010 | -23.4758 | -47.2959 | 2025-12-20 04:53:00 | NPP-375D | MAIRINQUE | SÃO PAULO | Brasil | 3528403 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 7792a77f-e6aa-3b0e-985c-06867c370670 | -12.51484 | -48.37844 | 2025-12-20 04:53:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 36657726-98fa-364f-8d13-0e78d4bb4327 | -23.476 | -47.29531 | 2025-12-20 04:53:00 | NPP-375D | MAIRINQUE | SÃO PAULO | Brasil | 3528403 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 5ca84b89-d812-32a7-bde7-8c5154f8a3cb | -20.30631 | -57.27815 | 2025-12-20 04:53:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 1f8c3b9d-5839-3c6d-bd1b-2ddeeda9f78c | -12.51764 | -48.37599 | 2025-12-20 04:53:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d01923e6-891d-3d17-907e-858473721b48 | -20.81552 | -56.05021 | 2025-12-20 04:53:00 | NPP-375D | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d521784c-be04-3489-8d2d-0d48e28b66fa | -13.38576 | -44.37782 | 2025-12-20 04:53:00 | NPP-375D | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a22a2140-5934-3538-8328-60fa2d78e446 | -13.60828 | -44.32791 | 2025-12-20 04:53:00 | NPP-375D | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 8a40504b-529e-3d18-9d87-2ea6ab694f87 | -11.15469 | -43.31496 | 2025-12-20 04:53:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 5.4 |
| eb400a4a-c8a8-371f-98d0-eb4ec7ae385d | -13.41924 | -42.17448 | 2025-12-20 04:53:00 | NPP-375D | ÉRICO CARDOSO | BAHIA | Brasil | 2900504 | 29 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 4c8f7d49-3b89-3115-b825-352312a1cab7 | -20.31963 | -55.92101 | 2025-12-20 04:53:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| d3494a7e-f838-39cb-92e0-02ad7cbb0836 | -26.74188 | -52.08619 | 2025-12-20 04:55:00 | NPP-375D | VARGEÃO | SANTA CATARINA | Brasil | 4219101 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| e7c69dc7-6372-3ceb-be1f-56bf2a2e4ada | -26.74244 | -52.08784 | 2025-12-20 04:55:00 | NPP-375D | VARGEÃO | SANTA CATARINA | Brasil | 4219101 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 1fe3441e-4592-3905-bd47-d7c3f5617b7f | 3.96885 | -59.91478 | 2025-12-20 05:08:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1e2cfdc4-7639-3886-bc95-cf6499834a7b | 4.18567 | -59.96911 | 2025-12-20 05:08:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| dd8f9a8b-82c4-3144-971d-2a4e7a27e10f | 3.96495 | -59.91569 | 2025-12-20 05:08:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 867328ca-8b87-3234-ba8c-7b7945f1c683 | 2.89049 | -60.26163 | 2025-12-20 05:08:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c1448994-5c5b-3283-a6d9-68b8ecf53f18 | 3.21312 | -60.19391 | 2025-12-20 05:08:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d209a756-2bdc-3f5e-bebb-d8fd03dcc66b | 3.23227 | -60.21234 | 2025-12-20 05:08:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| eeec674d-d49d-3539-98e9-1c2f9ce86b4c | 3.22881 | -60.21642 | 2025-12-20 05:08:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fd2f76c6-c69c-3778-909c-d8c583dc78ed | 2.89448 | -60.26102 | 2025-12-20 05:08:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| bf682d96-82ee-31ee-8ee9-22667fef4f15 | 3.22827 | -60.21292 | 2025-12-20 05:08:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| af6aff1c-6bfe-3a49-802c-831913b1bc75 | 0.73212 | -60.11055 | 2025-12-20 05:10:00 | NOAA-20 | SÃO LUIZ | RORAIMA | Brasil | 1400605 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 439fed93-de7a-3860-b6db-780a7fe95b1d | -9.57646 | -44.60487 | 2025-12-20 05:12:00 | NOAA-20 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 7e675555-ce75-33b0-9614-dd3ec482e1b9 | -9.57725 | -44.59842 | 2025-12-20 05:12:00 | NOAA-20 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 5.1 |
| dcc68fec-1fd5-32cb-97d7-c3384a230dec | -9.56943 | -44.60382 | 2025-12-20 05:12:00 | NOAA-20 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 73d2564e-fe06-3860-965b-3dbbc685eed6 | -9.57401 | -44.60422 | 2025-12-20 05:12:00 | NOAA-20 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 6.7 |
| b2decbf1-7de4-3a9a-b618-f4088fe51981 | -9.56865 | -44.61024 | 2025-12-20 05:12:00 | NOAA-20 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 71392767-0c93-38dc-8529-9a45b770a906 | -9.57022 | -44.59735 | 2025-12-20 05:12:00 | NOAA-20 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 6effc239-21a8-31cf-9a7c-ba679df79a3b | -9.58181 | -44.59867 | 2025-12-20 05:12:00 | NOAA-20 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 55d78ddb-5ab3-39e1-ab6c-c1391ed2c23f | -9.57327 | -44.61058 | 2025-12-20 05:12:00 | NOAA-20 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 705c3054-54a3-32a6-ab40-9668f82789b0 | -9.58105 | -44.60518 | 2025-12-20 05:12:00 | NOAA-20 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 6.7 |
| b1b5d261-6225-3b41-9fd8-c9b0d1e6c794 | -9.57568 | -44.61121 | 2025-12-20 05:12:00 | NOAA-20 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 4a206205-54fb-355d-a5f7-465f60610ae6 | -9.56623 | -44.6096 | 2025-12-20 05:12:00 | NOAA-20 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 5.6 |
| cdb8690f-cf94-3a42-b6fa-023fe6f6d6c9 | -15.55675 | -45.50126 | 2025-12-20 05:14:00 | NOAA-20 | CHAPADA GAÚCHA | MINAS GERAIS | Brasil | 3116159 | 31 | 33 | nan | nan | nan | Cerrado | 0.1 |
| 1f0cc9e7-dc10-36bf-9122-2e435d0e1bd9 | -21.9598 | -57.3115 | 2025-12-20 05:16:00 | NOAA-20 | CARACOL | MATO GROSSO DO SUL | Brasil | 5002803 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f4e0a0c6-6f0c-3ef8-8c31-f12a083f3d30 | -20.30809 | -57.28007 | 2025-12-20 05:16:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| afa86628-1cad-399e-be37-60de37d024c5 | -20.3087 | -57.27557 | 2025-12-20 05:16:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 760dca5b-f8e9-3872-9fcf-8cf00d2b80bb | -21.72833 | -56.58583 | 2025-12-20 05:16:00 | NOAA-20 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6f4e60dc-a395-3e0c-ba7b-1ae4165455a8 | -21.20189 | -56.93335 | 2025-12-20 05:16:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 2.0 |
| cff46b0a-a32b-35d2-8c1c-f4746f762626 | -20.31235 | -57.27613 | 2025-12-20 05:16:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.6 |
| 2742ee5c-1614-311a-a57d-44d848fd8d0c | -21.20526 | -56.93151 | 2025-12-20 05:16:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 0a9f47a2-b747-3f8a-a7f2-559169d54e83 | -21.20625 | -56.92931 | 2025-12-20 05:16:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 0b3f2a4f-a497-37d1-8a34-04d4bf2dccf8 | -5.07568 | -37.64069 | 2025-12-20 05:48:00 | AQUA_M-M | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 8.0 |
| efbfed58-14d9-38aa-ada5-5551b2a3662d | -3.86146 | -40.64227 | 2025-12-20 05:48:00 | AQUA_M-M | CARIRÉ | CEARÁ | Brasil | 2303105 | 23 | 33 | nan | nan | nan | Caatinga | 11.2 |
| 87caafe9-db10-3747-af55-43d88648fb22 | -3.89751 | -41.69111 | 2025-12-20 05:48:00 | AQUA_M-M | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 11.4 |
| 4f7a2942-51c4-3e05-9998-c144d850f8d2 | -3.8962 | -41.69983 | 2025-12-20 05:48:00 | AQUA_M-M | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 9.9 |
| 6460c934-8047-3902-a3aa-47c4223ed3a0 | -3.90627 | -41.6924 | 2025-12-20 05:48:00 | AQUA_M-M | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 4841e3bf-85d5-31ef-87a0-a9b38f38f28a | -7.38705 | -35.24319 | 2025-12-20 05:48:00 | AQUA_M-M | ITAMBÉ | PERNAMBUCO | Brasil | 2607653 | 26 | 33 | nan | nan | nan | Mata Atlântica | 28.2 |
| 4a9d122c-5658-378f-9ebf-b17f5f14caac | -9.56601 | -44.60543 | 2025-12-20 05:50:00 | AQUA_M-M | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 14.0 |
| a3bdd113-9d8a-3c13-bf2b-a533d5f09690 | -11.16027 | -43.31515 | 2025-12-20 05:50:00 | AQUA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 14.4 |
| 4163f7bf-2ff9-355b-8077-a82b0d5b10e3 | -9.57515 | -44.60683 | 2025-12-20 05:50:00 | AQUA_M-M | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 82d66fd9-7246-3dfe-a057-03ff08516a53 | -11.16161 | -43.30627 | 2025-12-20 05:50:00 | AQUA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 15.4 |
| f78b9f26-ac85-38cd-8234-e01c0a8accae | -9.56751 | -44.59571 | 2025-12-20 05:50:00 | AQUA_M-M | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 837f5112-ebf0-3333-8c24-de43b112a5a7 | -9.57665 | -44.59712 | 2025-12-20 05:50:00 | AQUA_M-M | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 25.3 |
| cd60284e-9afa-39a8-807c-49d3af436bff | 2.89297 | -60.2573 | 2025-12-20 05:59:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b2c30fcc-63fd-3930-b682-6b242fbf0da5 | 2.88901 | -60.26352 | 2025-12-20 05:59:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |


[Clique aqui para ver as próximas entradas](README6.md)
