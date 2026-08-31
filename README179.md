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

## Dados Diários - Página 179

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2b182ff2-e204-3f41-b463-46d35b8cabea | -9.4153 | -45.6726 | 2026-08-31 17:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 149.8 |
| 8ece9a6b-8a9a-3eaa-9b5f-76025820ab1d | -13.471 | -57.0373 | 2026-08-31 17:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 178.1 |
| ef545947-5fe0-3997-9501-03ba3f4f130d | -10.7271 | -50.6405 | 2026-08-31 17:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 240.0 |
| cc7bd74b-923d-323d-8847-8f28cc784df6 | -11.2295 | -51.2667 | 2026-08-31 17:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 34.9 |
| 5c70c0b3-8a5b-3004-b940-1ad4efa8079f | -9.4345 | -45.6477 | 2026-08-31 17:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 152.3 |
| acc2b6de-0fd1-36d1-92d9-7efa3bf5dff4 | -3.3322 | -59.4086 | 2026-08-31 17:40:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 60.0 |
| 1229f3ab-4189-3bec-b6e6-a05ca019a4ad | -9.1544 | -59.3669 | 2026-08-31 17:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 48.2 |
| b7de7841-72a4-3c43-aa79-72102d93b7d7 | -9.12 | -61.6011 | 2026-08-31 17:40:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 57.3 |
| c5452a60-ad37-3ee7-a815-b87c8eca0134 | -9.6679 | -46.5455 | 2026-08-31 17:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 77.9 |
| cf5d9ccb-c0d2-332b-ab74-6198ad616e07 | -9.7126 | -65.0951 | 2026-08-31 17:40:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 60.1 |
| dd1cdd05-1a36-3510-b417-323f3b7b2cd0 | -8.7628 | -46.4642 | 2026-08-31 17:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 139.4 |
| 6c9bba90-c655-355f-9804-843130d4f5c8 | -3.9363 | -59.3381 | 2026-08-31 17:40:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 46.0 |
| e9ba5960-2b22-3690-884f-d374d5d25e5f | -7.7034 | -63.3249 | 2026-08-31 17:40:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 62.8 |
| fba02adb-7da4-3190-9dc0-6c4d465b83c3 | -10.844 | -45.3356 | 2026-08-31 17:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 114.7 |
| 10577c53-aee2-31df-bed5-baa11cf52207 | -3.1266 | -61.2 | 2026-08-31 17:40:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 51.6 |
| 3ee6ed76-0127-31ae-b157-c74344a9feb9 | -3.6399 | -60.5466 | 2026-08-31 17:40:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 107.5 |
| fa47c1ec-716e-3c37-9e79-ed3dcd04249d | -10.3202 | -49.9782 | 2026-08-31 17:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 72.8 |
| c4a200f1-94c0-315e-aac6-0c4f9a61379c | -3.1083 | -61.238 | 2026-08-31 17:40:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 43.3 |
| 6d8cbaa4-7390-314a-80ca-dde8c5b54600 | -9.6939 | -65.1145 | 2026-08-31 17:40:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 125.5 |
| efc055d4-9550-33eb-9ec6-8a0993797339 | -13.4764 | -51.43 | 2026-08-31 17:40:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 79.9 |
| 1e6a33d5-6015-3150-87e5-eb6f2cb3200a | -8.8031 | -70.785 | 2026-08-31 17:40:00 | GOES-19 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 50.7 |
| c9605f79-d568-3869-93cc-3296d351ca93 | -13.967 | -54.395 | 2026-08-31 17:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 171.4 |
| 58f8a30b-0db1-388e-934c-20de0b01c264 | -13.9667 | -54.4157 | 2026-08-31 17:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 121.2 |
| 3948de32-2b8f-39a9-83de-45385eef633c | -6.861 | -41.6772 | 2026-08-31 17:40:00 | GOES-19 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 77.7 |
| eed8d18a-e772-3c18-b3c5-97616696aa3e | -13.4137 | -57.0426 | 2026-08-31 17:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 65.8 |
| a32c9277-2574-37d1-b264-c37004c1b6f4 | -7.4952 | -55.3062 | 2026-08-31 17:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 61.4 |
| f71c338b-2ab2-344f-a9b8-708bf22d11b0 | -8.2414 | -54.9601 | 2026-08-31 17:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 92.5 |
| 9f23c2b1-0423-359f-a982-74be8ea3636a | -10.8444 | -45.3126 | 2026-08-31 17:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 94.2 |
| e8128d7b-6e2b-3199-b501-15d5caad2901 | -8.7093 | -71.6289 | 2026-08-31 17:40:00 | GOES-19 | JORDÃO | ACRE | Brasil | 1200328 | 12 | 33 | nan | nan | nan | Amazônia | 46.8 |
| f814c218-b617-3d5e-bb47-d1ef585c02db | -7.5661 | -61.3239 | 2026-08-31 17:40:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 54.7 |
| f3f0323c-4a3a-309f-8281-cf93d16fc341 | -8.6674 | -62.8179 | 2026-08-31 17:40:00 | GOES-19 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 61.6 |
| 3638d696-48dc-3f63-b06f-4ac41c070b56 | -8.877 | -70.8023 | 2026-08-31 17:40:00 | GOES-19 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 39.0 |
| 8dfee08b-0a3c-3866-9894-715f14119474 | -8.6908 | -71.6474 | 2026-08-31 17:40:00 | GOES-19 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 45.8 |
| 2ab60559-1764-3fa8-bf7b-e8c70f2e8d08 | -9.173 | -59.3659 | 2026-08-31 17:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 55.3 |
| 48372a1c-88c7-3d27-a4bb-cd11cabaa930 | -3.1267 | -61.1811 | 2026-08-31 17:40:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 115.8 |
| 471b5885-b1fd-38d1-828e-9bd2070e5abc | -6.8019 | -59.4008 | 2026-08-31 17:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 108.5 |
| 3f0c91cf-2aa5-3c01-93c3-f382750bcf6a | -19.074 | -57.4084 | 2026-08-31 17:40:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 79.8 |
| b18e9e91-3bd5-3730-900a-79205ccb49b5 | -10.7827 | -50.7198 | 2026-08-31 17:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 71.3 |
| 97313f11-479c-3440-a668-62642ca4a471 | -12.0925 | -47.1587 | 2026-08-31 17:40:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 102.5 |
| b52115de-b177-333d-8035-f33e744cce6e | -10.4794 | -64.5012 | 2026-08-31 17:40:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 50.3 |
| b36b98b5-9e9e-3e89-9432-e6fe089a6e69 | -14.4641 | -52.1964 | 2026-08-31 17:40:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 74.9 |
| 20e355b7-71d4-3678-a832-e7a8711617fd | -10.3205 | -49.9567 | 2026-08-31 17:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 85.8 |
| 45b02faf-0cbc-37ce-a6fd-fe85e8cbb967 | -8.9002 | -68.8899 | 2026-08-31 17:40:00 | GOES-19 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 72.3 |
| 90e47f51-d4b2-346a-aa90-dba173411994 | -6.8384 | -59.4571 | 2026-08-31 17:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 41.5 |
| 098d7bd3-e074-3179-8d11-855f4cb03d0d | -13.4519 | -57.039 | 2026-08-31 17:50:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 81.9 |
| 6adc8971-d3ab-3b36-ad92-6a78efd04058 | -9.0057 | -65.456 | 2026-08-31 17:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 74.9 |
| 07a4372f-795c-342e-bb0d-d70bdb0f2fdc | -6.8569 | -59.4564 | 2026-08-31 17:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 60.8 |
| 57bc6e8b-c615-37d8-8099-2375530ce42f | -8.9428 | -63.2797 | 2026-08-31 17:50:00 | GOES-19 | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 64.9 |
| da30751d-a9d6-3237-a32e-cb5ea01afb5f | -8.6674 | -62.8179 | 2026-08-31 17:50:00 | GOES-19 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 93.7 |
| c095b993-850c-3ec9-9af6-8656bc0b926a | -14.2373 | -51.9284 | 2026-08-31 17:50:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 97.2 |
| 55abbad1-d678-3487-a06e-c79f3f336283 | -10.7272 | -47.9559 | 2026-08-31 17:50:00 | GOES-19 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 73.1 |
| 709549aa-58ef-31f2-a262-8decc79bdc8b | -9.694 | -65.0958 | 2026-08-31 17:50:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 75.7 |
| 1c3b9613-29c2-3c45-8dfc-48b00c80d8b8 | -3.6076 | -59.0769 | 2026-08-31 17:50:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 93.9 |
| f3926df3-9de3-3832-b3a6-922345512e11 | -8.948 | -62.3894 | 2026-08-31 17:50:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 66.8 |
| f38add7c-a5be-3eaf-b25d-4509f514eb64 | -10.802 | -50.6965 | 2026-08-31 17:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 91.3 |
| a967f235-1d72-3140-910f-278abf369140 | -6.1108 | -57.7035 | 2026-08-31 17:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 38.1 |
| a837b49a-f323-3104-a565-6d4690f9cd72 | -9.173 | -59.3659 | 2026-08-31 17:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 70.2 |
| 5ca61f50-fea1-3b82-8e5c-b8f9384443c5 | -10.3205 | -49.9567 | 2026-08-31 17:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 83.5 |
| e2b24f10-773c-39f1-8378-8c652fb41aad | -7.9425 | -44.2538 | 2026-08-31 17:50:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 65.0 |
| 605fb580-36fa-3ef7-bbdb-82d8d13fada5 | -9.12 | -61.6011 | 2026-08-31 17:50:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 59.7 |
| 8cfbda7a-9163-38f4-a452-431938b972ec | -12.1905 | -50.5194 | 2026-08-31 17:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 72.3 |
| b131cccb-1810-3fa1-b496-f6231fe18cae | -7.2932 | -60.6096 | 2026-08-31 17:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 53.4 |
| d2fb0ba9-937b-3a5b-8c50-f516edaf2877 | -13.967 | -54.395 | 2026-08-31 17:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 157.7 |
| fdfe509e-39f1-3376-bce7-8fd83f39cc0e | -10.4961 | -59.6195 | 2026-08-31 17:50:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 46.7 |
| 60d90a08-5ea0-383d-85ce-295567f29ea0 | -7.2191 | -60.6699 | 2026-08-31 17:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 52.3 |
| 48b7a013-fc58-3e1f-887f-419ec02f6fc1 | -9.2256 | -59.7894 | 2026-08-31 17:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 73.9 |
| 02e6c928-8b1c-37ce-a657-fdba2f4f9089 | -7.5662 | -61.3049 | 2026-08-31 17:50:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 67.3 |
| 51f85bcc-225a-3d18-bad9-e37088ed6590 | -8.9664 | -62.4076 | 2026-08-31 17:50:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 64.7 |
| a11d700e-e207-3e57-9c61-97ebe6c25747 | -7.0457 | -45.4124 | 2026-08-31 17:50:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 84.3 |
| d1b649a0-5a18-311c-a3ec-5e3aca94434b | -8.9481 | -62.3704 | 2026-08-31 17:50:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 93.8 |
| 35a8316b-8551-386f-878f-3f99125f94f4 | -8.6012 | -70.2192 | 2026-08-31 17:50:00 | GOES-19 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 40.9 |
| e982a811-e020-3895-aa76-a68704775bfb | -9.1709 | -59.6374 | 2026-08-31 17:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 66.7 |
| 2e176e39-a61c-38e5-8648-fbb9f24ca096 | -14.2369 | -51.9498 | 2026-08-31 17:50:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 168.7 |
| 3719a8f5-38ee-3e62-b227-c0efb3bb61a1 | -9.0431 | -65.3988 | 2026-08-31 17:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 73.8 |
| 797792ac-7b29-364d-8670-a091a86c2320 | -7.917 | -61.3481 | 2026-08-31 17:50:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 103.4 |
| af7c7ea6-ff1d-34ab-97b2-9d2b1e41b3e4 | -10.7827 | -50.7198 | 2026-08-31 17:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 119.7 |
| 245418a9-df8b-3ced-b74c-2b48397d3d53 | -10.7407 | -54.0401 | 2026-08-31 17:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 252.2 |
| 998ca072-d383-37d0-8088-3dfb08ccae9d | -11.6786 | -54.5484 | 2026-08-31 17:50:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 64.6 |
| 5dda1bbb-6f99-3325-a678-ae90608121fc | -8.9499 | -62.0662 | 2026-08-31 17:50:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 48.1 |
| c8258365-bfeb-3ef7-b54b-8b2100d07111 | -9.2258 | -59.77 | 2026-08-31 17:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 52.9 |
| 5f6991b1-35d7-36b4-a228-e77c019aeb01 | -10.3391 | -49.9762 | 2026-08-31 17:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 65.8 |
| c26c5690-1581-34ef-b10e-22adfea6efda | -6.82 | -59.4579 | 2026-08-31 17:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 44.6 |
| 23f1bc6a-ebbc-3e15-9ad1-f6f7a110b9c5 | -8.6673 | -62.8369 | 2026-08-31 17:50:00 | GOES-19 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 88.9 |
| 5eda9708-cab2-3f53-8c1a-884320a7e47d | -8.9295 | -62.3712 | 2026-08-31 17:50:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 46.5 |
| fc509621-7bb3-32a2-86da-606c9cfd3e18 | -11.175 | -54.001 | 2026-08-31 17:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 63.7 |
| 3abdf561-4d42-3687-912f-b33f99158b0e | -8.6852 | -62.9496 | 2026-08-31 17:50:00 | GOES-19 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 73.8 |
| e6249539-8380-3424-8c00-c4c44d02e321 | -3.1266 | -61.2 | 2026-08-31 17:50:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 63.4 |
| 1839eaa3-188e-3e9e-bee2-e3dc757c00e4 | -10.107 | -68.4008 | 2026-08-31 17:50:00 | GOES-19 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 216.4 |
| 997aa6f1-c738-36a0-ba73-9e3983e7de8d | -15.2475 | -53.8876 | 2026-08-31 17:50:00 | GOES-19 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 125.2 |
| c3ba9f99-b184-3230-8fc3-869db072099f | -6.7833 | -59.4208 | 2026-08-31 17:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 63.7 |
| 9860233a-5fce-3e2c-814e-bc2c2115b2c6 | -3.4002 | -61.3276 | 2026-08-31 17:50:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 71.4 |
| 250825e2-ed7c-3ef7-b96f-6fd83106c095 | -7.2933 | -60.5905 | 2026-08-31 17:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 108.1 |
| edfdc2b7-6c8f-3b18-af59-27d3b7de811c | -14.4835 | -52.1938 | 2026-08-31 17:50:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 93.3 |
| b44b2c5f-76a2-3ade-b31f-a83516b11daa | -6.8419 | -41.7032 | 2026-08-31 17:50:00 | GOES-19 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 128.8 |
| e003c493-529d-37ee-a8f0-a0c5c1de8faa | -8.5739 | -66.9754 | 2026-08-31 17:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 117.7 |
| d7e213a5-9ff0-3092-badb-59764fb3d73e | -12.0925 | -44.996 | 2026-08-31 17:50:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 188.8 |
| d469e3f8-531f-358b-84be-59f08f37a91e | -6.7514 | -55.6654 | 2026-08-31 17:50:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 70.7 |
| 62de31fa-427e-3deb-b284-0efa326e3a56 | -7.529 | -61.3635 | 2026-08-31 17:50:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 89.3 |
| aeef62b0-34c2-3266-b312-5ab24d07e967 | -3.6399 | -60.5466 | 2026-08-31 17:50:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 112.0 |
| 2ea8d071-2ea4-39be-9f80-c01cb6d4d63c | -13.9667 | -54.4157 | 2026-08-31 17:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 133.4 |


[Clique aqui para ver as próximas entradas](README180.md)
