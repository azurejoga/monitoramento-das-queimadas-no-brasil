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

## Dados Diários - Página 78

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0639d2db-bceb-3e19-b70e-976b3d1aedf9 | -8.61663 | -54.85478 | 2026-09-01 05:36:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 9b6956e4-1dbc-3c96-92a7-729d19ac8353 | -9.00732 | -67.79732 | 2026-09-01 05:36:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 00f8f472-d261-3e03-8869-a193539d6ab3 | -10.21362 | -50.32254 | 2026-09-01 05:36:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| d58f2f51-56e9-379e-8d08-cca8cc656871 | -9.03018 | -65.44863 | 2026-09-01 05:36:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 1ba6b5bb-5770-3127-b0da-e09c654f1b30 | -7.56612 | -60.46037 | 2026-09-01 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3f419cc3-78af-30b6-a636-45ff33bbb5ce | -9.03242 | -65.4298 | 2026-09-01 05:36:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| e1c7385b-b52f-3b14-81a3-1c213864c137 | -7.56726 | -60.47602 | 2026-09-01 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a6f871b2-bd3a-3445-98e5-a959e3f5e7ef | -8.45882 | -62.71278 | 2026-09-01 05:36:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7ba8aeea-b170-3c22-8905-afa47727cb0c | -6.81201 | -59.08994 | 2026-09-01 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3f3a3f24-be8f-3721-a3c2-194f28f80df9 | -7.57128 | -60.47282 | 2026-09-01 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 014b5f28-2201-3c3e-b571-18dccf5193a6 | -6.86097 | -59.48436 | 2026-09-01 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ccca1d38-20c2-3fe1-b768-cdea654f978b | -6.05392 | -57.64445 | 2026-09-01 05:36:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| e870440b-f063-36ed-ae4e-3a9e2d1a4b35 | -6.75912 | -59.44041 | 2026-09-01 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d58cd2a2-edab-329c-9c0f-124087e8aa92 | -11.10323 | -51.54837 | 2026-09-01 05:36:00 | NOAA-20 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 967d6cf9-aa99-3ef1-b512-e3c45eac2194 | -8.80455 | -62.32914 | 2026-09-01 05:36:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 110436a1-0bc3-3373-9996-3d0e8c7016fc | -7.57818 | -60.47387 | 2026-09-01 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 4c05cc5e-f183-3355-babc-d4713a7faae5 | -7.35729 | -60.59074 | 2026-09-01 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d68c9d23-08e6-3ac7-a08d-e0a720945df2 | -10.50172 | -59.61048 | 2026-09-01 05:36:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 74f951b4-1e95-3072-b528-e42763d9d541 | -6.60572 | -58.60535 | 2026-09-01 05:36:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 06551a9f-ad5f-31a0-9be9-946378194b96 | -6.12348 | -53.55162 | 2026-09-01 05:36:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 745035f8-d677-3c18-bb3f-d62b6340aba7 | -6.80774 | -59.57148 | 2026-09-01 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 99c9dabc-52a0-36e4-a62e-e75b0e094187 | -6.6003 | -58.59074 | 2026-09-01 05:36:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 677b0c49-437c-326f-b4ee-921d98f8dc01 | -7.25607 | -61.11168 | 2026-09-01 05:36:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4eb20288-4019-3878-a7b7-ae4e9ebd015d | -7.5753 | -60.46958 | 2026-09-01 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c6dbeb78-97c0-3130-89a4-1cf15e0c3d10 | -10.94691 | -61.65631 | 2026-09-01 05:36:00 | NOAA-20 | JI-PARANÁ | RONDÔNIA | Brasil | 1100122 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a6736767-e058-3fe4-af14-5a0646ca9255 | -7.50572 | -61.3809 | 2026-09-01 05:36:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e79bdbc0-dcc2-3930-af83-d84e7dc6bcde | -7.62 | -57.62051 | 2026-09-01 05:36:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 14f2e52e-38ab-3d72-823e-3aefc85923db | -7.30203 | -60.56326 | 2026-09-01 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4b4fc87e-4de3-3d56-bf32-746cd69c1b7d | -10.41911 | -64.45483 | 2026-09-01 05:36:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 4.4 |
| faad0353-ea27-3c24-8de2-961f5f925a9d | -9.02923 | -65.44942 | 2026-09-01 05:36:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 16f7d7c1-50f9-36d5-a7e3-fb3f79655079 | -6.13077 | -55.64787 | 2026-09-01 05:36:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 25fd08a9-1102-38c8-b69e-dd9633f4d498 | -6.20941 | -53.59034 | 2026-09-01 05:36:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6f0b0421-0502-3207-bef6-e3aa74e78dab | -7.58905 | -57.69102 | 2026-09-01 05:36:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ebe7efc6-7050-3a66-bbdd-2c75456697a0 | -7.02337 | -59.65189 | 2026-09-01 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3cfd9140-5944-3c33-a58f-81526ad08a9c | -8.69528 | -62.93648 | 2026-09-01 05:36:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ba01481e-9e43-3aec-bc96-feb7cab8f111 | -6.11884 | -57.69201 | 2026-09-01 05:36:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b339ae31-631b-3cdb-aa4e-06abf9d0dd56 | -7.25663 | -61.10807 | 2026-09-01 05:36:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e1e8ad8c-c8a3-3c72-8335-f9cfed62ff6d | -8.67581 | -62.84394 | 2026-09-01 05:36:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 074d3a05-db51-33f4-887c-19bb3924d80b | -6.12075 | -57.68007 | 2026-09-01 05:36:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| cf5bba83-a933-3a88-bc2b-00220aba6900 | -9.45455 | -67.46178 | 2026-09-01 05:36:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| c69ce480-a440-33fc-ac35-0a22f52139db | -7.19243 | -60.68339 | 2026-09-01 05:36:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 537be704-26e0-36e7-9b78-855defb9afe6 | -11.06587 | -51.53838 | 2026-09-01 05:36:00 | NOAA-20 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 06c7cc3e-f897-3ed2-8238-3462646b7857 | -7.56832 | -61.37603 | 2026-09-01 05:36:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6cc314f7-162c-3502-b62f-bf9af9f08cd9 | -6.16289 | -52.63623 | 2026-09-01 05:36:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fd0b3648-a188-3d9e-97fd-c9712fbb2a18 | -6.8924 | -59.05273 | 2026-09-01 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a6d1a9dd-9460-393d-aca2-75948d5d3011 | -7.36243 | -60.60292 | 2026-09-01 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1ec6e0ba-2245-32a6-aeff-9b21cd379790 | -6.94101 | -55.64119 | 2026-09-01 05:36:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a695a85e-dbf9-3f50-b376-78b8f5d86121 | -6.11682 | -57.67953 | 2026-09-01 05:36:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| dc584e33-0f49-3ad6-aabf-0dc1bb43b8be | -8.03879 | -61.73304 | 2026-09-01 05:36:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2ca1e719-e8fc-3fb9-b3b6-518eec0b4c3d | -8.26445 | -62.76033 | 2026-09-01 05:36:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d6060e7b-abcf-3780-8e60-63e2654ed5d5 | -7.10118 | -63.04764 | 2026-09-01 05:36:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 312c18b2-ab35-3a30-9736-9ffb4b278ec8 | -6.11638 | -57.68147 | 2026-09-01 05:36:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| b663ceb7-f5b4-3045-bb47-0875f7c784c5 | -10.50414 | -59.6199 | 2026-09-01 05:36:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 03d75cfd-2b6e-3c6b-9b77-1767ab9f53b1 | -7.03199 | -59.2162 | 2026-09-01 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d8f9895b-a18c-3516-b76d-905b0663d220 | -9.1354 | -61.09393 | 2026-09-01 05:36:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7ff1089a-c057-3b83-97d8-f3b963c55571 | -10.36184 | -50.00687 | 2026-09-01 05:36:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 4d87eaa2-d430-36dd-9864-0cc9f337635c | -7.52024 | -61.37585 | 2026-09-01 05:36:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b0c79d0a-c591-3c1b-ad6f-bc17ba2306ea | -10.35496 | -50.00604 | 2026-09-01 05:36:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 17858f0d-5237-3c2a-81ee-77b0a57e2fd0 | -9.47663 | -57.02236 | 2026-09-01 05:36:00 | NOAA-20 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8f10c19c-4d67-347a-a208-7626e6501d96 | -7.33786 | -60.58012 | 2026-09-01 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.7 |
| e949ab5b-cb7a-35e3-8d7c-45bd01744e83 | -6.75458 | -56.33632 | 2026-09-01 05:36:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ec0e7005-0953-3566-afa9-660bcfa918ae | -6.86282 | -59.47211 | 2026-09-01 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e4710a67-4c9c-3a34-b6a2-fe1282a1265a | -9.01951 | -57.53823 | 2026-09-01 05:36:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 938db5b6-9ccd-3d6a-8bd0-5f226a51e6f8 | -6.82908 | -59.57473 | 2026-09-01 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 66c8a374-801f-3715-9501-c3cb30b1d7fa | -7.59026 | -60.46415 | 2026-09-01 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9b81b3a0-567a-3f48-b3b6-7a8f1c6c6754 | -7.85218 | -61.14737 | 2026-09-01 05:36:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a34410b1-5e28-3e0f-9337-97c1443ef3a2 | -6.82223 | -58.87121 | 2026-09-01 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ad13397b-65c9-3fe7-a56c-f8e08efbf9f5 | -7.58104 | -60.47821 | 2026-09-01 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| f568e0a2-5f95-3389-be12-9c24ef84aa24 | -9.14849 | -61.09978 | 2026-09-01 05:36:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 94d32188-3399-3c83-b1a3-b3b2b65c8250 | -7.0416 | -59.22622 | 2026-09-01 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 59f48adf-5dc5-3952-bf53-93555588493e | -6.11957 | -57.68703 | 2026-09-01 05:36:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6fc0d922-55fc-3328-9f8b-ae6480692f47 | -6.59589 | -58.59463 | 2026-09-01 05:36:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| fae3e545-0e90-3d89-9488-9fd7bbbb4dbf | -10.41575 | -64.45427 | 2026-09-01 05:36:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 170141aa-c76c-30b7-ba58-f74acf40146a | -10.45525 | -63.16916 | 2026-09-01 05:36:00 | NOAA-20 | CACAULÂNDIA | RONDÔNIA | Brasil | 1100601 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c86ee68a-84a3-3801-bc1f-b9d4d75e70b2 | -5.95659 | -57.67845 | 2026-09-01 05:36:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 0b3e4143-b8c8-3a0a-aabc-2639e5a01c58 | -10.82109 | -50.72417 | 2026-09-01 05:36:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 3e9a8aa2-b798-3d2a-a1d6-8004723776aa | -6.9326 | -55.6352 | 2026-09-01 05:36:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a17a88b4-dbf5-3f70-b48d-692b16316fa3 | -9.14805 | -60.94257 | 2026-09-01 05:36:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 8.1 |
| ea605206-07c2-3859-b01d-eaa36c74079b | -8.78102 | -62.50079 | 2026-09-01 05:36:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 92e2de02-2cc6-356a-acd3-d4c339e1224d | -8.60707 | -70.22252 | 2026-09-01 05:36:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e8c54809-2711-3654-94bf-189ab15469ee | -5.94802 | -57.68231 | 2026-09-01 05:36:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 3d3b0a5a-da16-37f1-94c7-659b622de416 | -5.88824 | -57.75809 | 2026-09-01 05:36:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7ddbee05-adc7-3e1a-95bc-a14baa07305e | -8.93374 | -62.3711 | 2026-09-01 05:36:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ca54d8fe-da47-3cf4-9633-e631c6a1f685 | -6.13592 | -55.64398 | 2026-09-01 05:36:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 97df6203-7154-3f10-a55a-b13c80f987f4 | -8.89002 | -62.34625 | 2026-09-01 05:36:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 250e7051-0fec-3db3-a794-e5a126ff445e | -8.45827 | -62.71626 | 2026-09-01 05:36:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5fbcd7f0-ba1c-3a2e-9098-9a0bb71d89c4 | -8.95106 | -60.60144 | 2026-09-01 05:36:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 49892a2d-9edb-3eb8-9c3e-89e3ec7f22b4 | -8.80422 | -62.50448 | 2026-09-01 05:36:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 31c492dd-16a6-30cd-b5e8-accf84525ac1 | -11.2458 | -50.58752 | 2026-09-01 05:36:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| d945baf5-2a43-39ce-8e09-7483a12e9d28 | -9.48093 | -57.02296 | 2026-09-01 05:36:00 | NOAA-20 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2712558a-8e7d-31e5-9d6b-bbeff86d7028 | -7.58449 | -60.47878 | 2026-09-01 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e0103e47-4461-30ea-a46b-ebd5c0333c91 | -8.12784 | -54.96491 | 2026-09-01 05:36:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 18ebbc82-06a0-3bc4-9a0f-d6448dd9d67d | -9.15465 | -59.53476 | 2026-09-01 05:36:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 521b9fc0-aeae-3d96-95d3-439c9bed39d8 | -7.19186 | -60.68711 | 2026-09-01 05:36:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 6a278f81-c0d3-329a-8c45-8876bc875a5e | -8.59121 | -70.22999 | 2026-09-01 05:36:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ad9f7c1a-6af1-35dc-b721-8723e708f337 | -11.06137 | -51.5222 | 2026-09-01 05:36:00 | NOAA-20 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 63f715d1-7e3b-319c-ad52-f2bfe0645c0b | -8.93152 | -63.28823 | 2026-09-01 05:36:00 | NOAA-20 | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 9b092a29-d2ac-315e-bf3e-9e83a4b72ae3 | -6.02838 | -57.68163 | 2026-09-01 05:36:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 937a2a8a-1dd2-3c3b-a511-64e9fb45313a | -6.95455 | -55.6508 | 2026-09-01 05:36:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 30.2 |
| bfc65e2e-f1d2-3c16-9689-7a553d5f08a5 | -11.48198 | -58.51607 | 2026-09-01 05:36:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |


[Clique aqui para ver as próximas entradas](README79.md)
