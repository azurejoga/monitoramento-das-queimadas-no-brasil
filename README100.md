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

## Dados Diários - Página 100

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7a7fadb2-e603-35d4-884b-24b89a3b9908 | -3.1679 | -60.65401 | 2026-09-23 05:23:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 35e6a28a-a6d2-3a1a-9507-1b7447af93a6 | -11.66903 | -50.98016 | 2026-09-23 05:23:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 25631a52-cbc2-3ac6-ad31-de95d6a39a64 | -3.86218 | -58.8236 | 2026-09-23 05:23:00 | NOAA-20 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 4ad769ef-61dd-3e63-bacf-9da6ca1a7986 | -10.30554 | -50.49351 | 2026-09-23 05:23:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0574116a-1936-36e8-9022-4633aa9260ac | -10.38669 | -54.41248 | 2026-09-23 05:23:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 90921581-d737-3a13-9c3c-c8ce4dbe540b | -11.65825 | -50.97874 | 2026-09-23 05:23:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 410641cb-4539-371c-9757-a2cde398dedc | -2.46409 | -57.91197 | 2026-09-23 05:23:00 | NOAA-20 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 4.9 |
| dd60a6bc-22a3-3d46-a15c-d22fb22d939e | -3.54376 | -62.08144 | 2026-09-23 05:23:00 | NOAA-20 | CODAJÁS | AMAZONAS | Brasil | 1301308 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e53abbcd-1170-3e3b-a00b-881c198e5303 | -4.2773 | -55.43592 | 2026-09-23 05:23:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e2b1afe0-c989-3ac8-b0f4-145cd514b37b | -9.25375 | -65.44201 | 2026-09-23 05:23:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 132bb7ec-f660-3b27-9775-06683dde1939 | -6.88513 | -46.56612 | 2026-09-23 05:23:00 | NOAA-20 | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b32f302d-010c-3767-acf0-d67f85aefe51 | -9.7151 | -48.3383 | 2026-09-23 05:23:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| ddbd9851-c1c6-39ad-8f1e-1979eb45976e | -10.30197 | -50.522 | 2026-09-23 05:23:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2cecdcd4-2270-339f-a662-eb6c0b29dfc5 | -7.88094 | -61.17588 | 2026-09-23 05:23:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.3 |
| bed6825f-a3be-37e4-b00d-ab5f21f61f44 | -9.32999 | -65.72482 | 2026-09-23 05:23:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ee43375c-feb8-39a9-b36d-9598a6ae5ce7 | -4.83699 | -55.76427 | 2026-09-23 05:23:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2e702205-809b-3624-898e-408a0f3e3c40 | -6.2349 | -51.01178 | 2026-09-23 05:23:00 | NOAA-20 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 52055c68-122b-310e-84f8-782e45a5e364 | -3.25137 | -53.96587 | 2026-09-23 05:23:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7700093e-7a22-39a5-a591-33adbd123870 | -2.45373 | -49.21677 | 2026-09-23 05:23:00 | NOAA-20 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 14c0261a-f6fa-3472-a297-f563314774a4 | -10.30922 | -50.50169 | 2026-09-23 05:23:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 1c448868-84a5-3a9d-84ac-f0ab73234e81 | -3.19294 | -59.70055 | 2026-09-23 05:23:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 5.0 |
| fbc9dff7-612e-3a70-b300-02678abcfd88 | -2.46355 | -57.91541 | 2026-09-23 05:23:00 | NOAA-20 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| f48d0fe9-fb69-33b4-81da-904990b31dd7 | -4.42066 | -55.47476 | 2026-09-23 05:23:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d0decf47-de57-36ef-abf6-ad81369eb146 | -3.18351 | -61.10371 | 2026-09-23 05:23:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 72f77764-5c45-3f52-99b7-92c663d5a6f1 | -10.25297 | -49.96967 | 2026-09-23 05:23:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 3d4a9971-6b09-31e2-870e-743311ebefa5 | -3.33208 | -61.3056 | 2026-09-23 05:23:00 | NOAA-20 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 65e77542-378e-3258-a293-e1fd1d47979d | -4.15489 | -60.79056 | 2026-09-23 05:23:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 884819eb-4cc1-3d6a-acd6-310151647de4 | -3.95424 | -59.35572 | 2026-09-23 05:23:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f0f326e6-7bb6-3f3b-bc28-64ef6a4528ad | -11.70083 | -50.76934 | 2026-09-23 05:23:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 644a8531-3d3c-39b6-8039-cc0d56677437 | -3.68269 | -60.63261 | 2026-09-23 05:23:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d34e4137-d229-3fd3-a087-7d26f82105a4 | -10.28884 | -50.5383 | 2026-09-23 05:23:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 7cf8104a-f043-3103-8832-55225a706659 | -4.15733 | -60.77551 | 2026-09-23 05:23:00 | NOAA-20 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0fb989ec-381b-34a2-ae4d-6a0408d79d1c | -3.77698 | -59.59711 | 2026-09-23 05:23:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 321af8aa-32f8-3590-b11c-ace1ddb2c8a9 | -10.30874 | -50.50525 | 2026-09-23 05:23:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 2067651e-f852-3839-a46a-6dbd0ee72618 | -10.84758 | -56.22152 | 2026-09-23 05:23:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0577ecf2-315b-3943-b1fe-95e9cb2ffd30 | -3.69182 | -60.5535 | 2026-09-23 05:23:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| aa814ad9-1f75-3258-99a5-c235b1ccd8d7 | -9.58452 | -46.54044 | 2026-09-23 05:23:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 00cd4c12-a4d0-3396-a5d6-cd32c04d4ec6 | -9.15017 | -61.19808 | 2026-09-23 05:23:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 07d67caa-7f5e-3dc2-a886-401cdc2974e3 | -9.5414 | -65.68337 | 2026-09-23 05:23:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0e1ec40f-4c6c-3384-86ac-e0f5b0ac2653 | -10.03701 | -50.22239 | 2026-09-23 05:23:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f2f65676-8876-3421-91e3-16a907d8f351 | -3.68077 | -60.57854 | 2026-09-23 05:23:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5d556fbb-3887-34ba-b2b4-b6b5e28612e8 | -10.30007 | -50.49278 | 2026-09-23 05:23:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4b8255ac-52e5-390b-b0b9-8ffadda7ce48 | -8.92186 | -61.4833 | 2026-09-23 05:23:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| c6641543-55ec-3b7b-b3de-5718fd7cf82c | -3.31554 | -54.9347 | 2026-09-23 05:23:00 | NOAA-20 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6b13208a-aeec-30e1-9438-bdac0a57840f | -5.89441 | -52.10001 | 2026-09-23 05:23:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 97feba71-54ac-3c7d-a159-56005e6822e0 | -4.44522 | -55.07521 | 2026-09-23 05:23:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 264e650e-94e1-359f-8c00-df48e2973c5b | -9.10106 | -61.43716 | 2026-09-23 05:23:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 99533cbc-c807-36d7-8a22-32a5afbdbbfa | -2.74353 | -51.54682 | 2026-09-23 05:23:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 1d18ae29-c406-3140-aa49-816074b33181 | -3.66794 | -57.08044 | 2026-09-23 05:23:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 6277ae1b-3503-366f-af7d-587f979344c5 | -2.85916 | -60.91379 | 2026-09-23 05:23:00 | NOAA-20 | IRANDUBA | AMAZONAS | Brasil | 1301852 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 0d78212d-aa87-3c2a-85bb-61736a9c103b | -10.29385 | -50.54258 | 2026-09-23 05:23:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 39869086-d2d8-3170-8621-f2fff7f83f5b | -6.17789 | -52.78979 | 2026-09-23 05:23:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 62b2eac7-059c-3412-a6a2-77c2b4494563 | -7.69482 | -61.54375 | 2026-09-23 05:23:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 983f8d06-8698-35e8-af18-bb122744c05b | -8.49585 | -57.61123 | 2026-09-23 05:23:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 5dfe6080-29aa-3e79-abb4-b84b922195e0 | -3.24622 | -53.95236 | 2026-09-23 05:23:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 23f62dd2-437c-3774-95df-cb41152e19ed | -2.65196 | -59.68514 | 2026-09-23 05:23:00 | NOAA-20 | RIO PRETO DA EVA | AMAZONAS | Brasil | 1303569 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| e9f30443-94e4-3aeb-9fd9-171cda40efdf | -4.34129 | -55.65307 | 2026-09-23 05:23:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2a624f33-527e-31b6-b578-9c052a63e70a | -9.04432 | -65.42183 | 2026-09-23 05:23:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b319792d-1987-39e4-9ac0-e42dd15a9f39 | -1.72073 | -49.98529 | 2026-09-23 05:23:00 | NOAA-20 | CURRALINHO | PARÁ | Brasil | 1502806 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5c3f903e-42e9-3564-8a92-82cf0ce672dc | -5.89567 | -52.09105 | 2026-09-23 05:23:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| bb7a31b1-9fb9-3d60-96e0-ae13b1036f19 | -4.30635 | -55.59298 | 2026-09-23 05:23:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 08e7d5b3-5f67-330d-aeb3-3b1918c1a009 | -4.26003 | -60.01127 | 2026-09-23 05:23:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 04f4329f-e8ae-3b71-8b34-a33edbdcc01b | -3.27314 | -57.86507 | 2026-09-23 05:23:00 | NOAA-20 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 84f03ec1-def0-3e39-8603-51b3d36ee0a2 | -3.88018 | -59.5665 | 2026-09-23 05:23:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 173f0665-ff7b-3d3a-b5f8-4814a2b7e62b | -4.06206 | -59.83363 | 2026-09-23 05:23:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2bc9a78f-1ec9-33ae-a5fb-1fdc8488baf6 | -3.72049 | -55.97248 | 2026-09-23 05:23:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 343ac0b7-fbf1-3e1b-9bbf-4359e3d5535f | -3.33273 | -61.30159 | 2026-09-23 05:23:00 | NOAA-20 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 79a3350a-f8f3-3068-8b85-01e4a5cfab1b | -11.78764 | -50.97068 | 2026-09-23 05:23:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| fe92a130-2fcb-33a7-b473-8ff4e869712b | -4.45586 | -47.92344 | 2026-09-23 05:23:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 6d41a8e6-825a-30b5-9284-3de72dc7a70e | -10.04209 | -50.22683 | 2026-09-23 05:23:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| bf45c877-b20a-3dfe-91e7-00334b634df2 | -3.06592 | -54.4058 | 2026-09-23 05:23:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2fb816e4-155f-3b66-a8df-9fd48e93ef97 | -3.77666 | -60.74723 | 2026-09-23 05:23:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 104a4f4a-bd92-3c55-9bab-230797221097 | -11.66949 | -50.88794 | 2026-09-23 05:23:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 08f62daa-6cee-378e-8151-729b0024df16 | -3.50026 | -59.92812 | 2026-09-23 05:23:00 | NOAA-20 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d733b27f-1a56-35ef-a297-5f52403cd507 | -3.06347 | -61.17576 | 2026-09-23 05:23:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 27debd55-3d18-30b9-a42e-325afbbe46cd | -3.11681 | -60.68483 | 2026-09-23 05:23:00 | NOAA-20 | IRANDUBA | AMAZONAS | Brasil | 1301852 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 22b9de9b-cd89-3912-aec6-cebea5378309 | -3.78917 | -55.87827 | 2026-09-23 05:23:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8325d15b-44f0-3a11-884e-c2ac2b27fb5c | -6.88157 | -46.56631 | 2026-09-23 05:23:00 | NOAA-20 | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 202b621a-be94-3cfb-97e3-343b3d73ca64 | -9.16492 | -51.53203 | 2026-09-23 05:23:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1cc675fe-5848-3eed-a11a-863d0ab7f49e | -4.871 | -55.85324 | 2026-09-23 05:23:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 4be660c4-420f-3873-b540-b883c54e2ec1 | -3.48524 | -59.56878 | 2026-09-23 05:23:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 152be4a4-bd95-3b88-b695-16d368e0bcf4 | -3.59033 | -54.51871 | 2026-09-23 05:23:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 748425e4-c1ec-3f15-ae3a-079296fb934a | -12.37192 | -50.15443 | 2026-09-23 05:23:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| eb54a1ce-6b59-3a81-9cc3-7fb064add364 | -9.58797 | -60.52406 | 2026-09-23 05:23:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 11c351b1-99f8-3621-9ee7-ab135ab23e6e | -7.04087 | -62.9326 | 2026-09-23 05:23:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0776376d-0cb1-3ccd-a3df-28b174b16956 | -3.47074 | -59.5737 | 2026-09-23 05:23:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0757eae9-68c3-342f-b743-280ab471268a | -3.76532 | -59.47652 | 2026-09-23 05:23:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ebaa1f5b-e322-3567-a4d4-b214a8d41dd1 | -10.30019 | -50.53621 | 2026-09-23 05:23:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 0062a2fa-10b8-3700-ac4e-3ed12f6c3786 | -9.16131 | -59.55347 | 2026-09-23 05:23:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9a241118-2d72-3007-a44e-cf69f8143b53 | -3.69003 | -60.56469 | 2026-09-23 05:23:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 9.9 |
| e29a863d-00ed-3ea3-b498-a95507d0f604 | -3.80274 | -58.92023 | 2026-09-23 05:23:00 | NOAA-20 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ad764255-8988-3374-ae37-7257f765f28f | -8.18701 | -61.18809 | 2026-09-23 05:23:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7e76e25b-287b-3af4-896a-d623f29ae0c8 | -11.70406 | -50.78796 | 2026-09-23 05:23:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0a8893bb-75df-3e37-8404-515deb52fb62 | -7.45431 | -62.31298 | 2026-09-23 05:23:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 627e457d-8498-3dcb-bfd0-1e50a60b91dd | -4.15772 | -60.7949 | 2026-09-23 05:23:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cc28e6bc-1bdb-3ab0-ba68-60cce849e675 | -10.53122 | -54.49318 | 2026-09-23 05:23:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 4066113c-cfaf-3d34-bdb6-93c895098d00 | -3.44399 | -50.61615 | 2026-09-23 05:23:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 68988fbd-4853-3f83-aed9-15c63de39b35 | -7.87221 | -61.18301 | 2026-09-23 05:23:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.4 |
| de96923d-c3f3-3895-a343-c8e86e68b96c | -5.2427 | -48.19136 | 2026-09-23 05:23:00 | NOAA-20 | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ee1d376c-73d3-33d3-930b-5c85ff313a5a | -3.10722 | -60.72242 | 2026-09-23 05:23:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |


[Clique aqui para ver as próximas entradas](README101.md)
