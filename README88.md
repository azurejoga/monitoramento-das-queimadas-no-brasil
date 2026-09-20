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

## Dados Diários - Página 88

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 82b63eaf-ded9-3bde-a0e4-11e0fccfb203 | -8.77635 | -48.73512 | 2026-09-20 05:23:00 | NOAA-21 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 4.1 |
| c1e89d30-a4a9-32b0-8ef5-84d75757054b | -10.31135 | -50.23469 | 2026-09-20 05:23:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| f7ff83b7-8115-3e86-85a8-06ab273f59e3 | 1.21716 | -50.98408 | 2026-09-20 05:23:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b921e192-a905-3e40-96a3-fd3ebce89450 | -8.1808 | -54.76778 | 2026-09-20 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| d508e1b6-d26e-3fa0-9621-5adecc6439aa | -3.44945 | -57.94632 | 2026-09-20 05:23:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 09dbd3c3-f27a-3720-86db-47a6155d4da4 | -10.31844 | -50.22605 | 2026-09-20 05:23:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 7e9477f0-f30f-3fbe-b8e4-fad294a6da04 | -8.4685 | -57.62835 | 2026-09-20 05:23:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1c8e0460-aa8c-3ad4-9bf1-3331d97f6937 | -6.44567 | -58.15634 | 2026-09-20 05:23:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b18771a9-7eee-392c-b30b-f893aedf316a | -3.44848 | -50.59861 | 2026-09-20 05:23:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 84409b3c-cfaf-3170-8219-5d023c373a35 | -2.81831 | -50.4698 | 2026-09-20 05:23:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 04b9d302-ffae-3cdb-8db3-bbf2daa853a4 | -3.77999 | -49.76797 | 2026-09-20 05:23:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 54cff6ec-4607-3faf-aba4-47fe7c559f4f | -2.12382 | -59.5964 | 2026-09-20 05:23:00 | NOAA-21 | PRESIDENTE FIGUEIREDO | AMAZONAS | Brasil | 1303536 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 7db677ec-164d-353f-9886-8ba9186926e1 | -10.30381 | -50.24345 | 2026-09-20 05:23:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| d7dba1b5-f3d4-3480-81a7-2eb9d7bee63e | -3.50216 | -53.43874 | 2026-09-20 05:23:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 435fec77-9450-3e63-b134-3b8e54ea1adf | -3.44442 | -58.23037 | 2026-09-20 05:23:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 3785905e-39bc-3a4d-ace6-358e4105a2ce | -3.07765 | -61.17427 | 2026-09-20 05:23:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d880c4f7-2689-3c49-b687-e59c932ed79e | -6.49431 | -58.37854 | 2026-09-20 05:23:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4926f74d-0900-3432-9913-e59277a973f9 | -3.36151 | -50.45627 | 2026-09-20 05:23:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a3fd698f-13e4-3d1d-948c-0dc87d0fbdac | -3.59118 | -47.36018 | 2026-09-20 05:23:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 8b7c39eb-20ed-3d81-86c0-c8e7e4817354 | -9.47538 | -54.45125 | 2026-09-20 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 0b2b4a47-2da0-37c5-90a5-4b049f3445b9 | -3.0049 | -54.16581 | 2026-09-20 05:23:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 0ee9a3e2-be06-3e6b-aa2a-e0864a3656f6 | -10.41422 | -48.3359 | 2026-09-20 05:23:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 6e1a0fae-0bba-37b3-83aa-5cac62ae2015 | -2.88513 | -57.78593 | 2026-09-20 05:23:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 4.3 |
| f18e836a-7095-3c73-bf9b-534fc7e3f1a4 | -7.55487 | -61.32733 | 2026-09-20 05:23:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2e7ffb32-02c5-34aa-a949-6db0c138a0cc | -10.66673 | -48.70212 | 2026-09-20 05:23:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 15fdeeb4-28c1-3554-ad7b-41765d4d8098 | -10.32081 | -50.20694 | 2026-09-20 05:23:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| c475ca64-bac7-3784-b2c9-c82f1f7b85ab | -3.08546 | -61.18996 | 2026-09-20 05:23:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 245d8a94-2ad2-310f-9faf-99b9b088850f | -7.76424 | -49.19836 | 2026-09-20 05:23:00 | NOAA-21 | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 4.6 |
| a38f9806-563e-3a1b-8554-d5148122e060 | -10.49966 | -51.28945 | 2026-09-20 05:23:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| c54fab19-0f93-3cb6-9554-57492198fa59 | -3.35929 | -59.87782 | 2026-09-20 05:23:00 | NOAA-21 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fce294f4-4417-3d1f-952b-0170928746e4 | -8.8546 | -62.3617 | 2026-09-20 05:23:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 270c00f2-2787-323d-a273-566e66b51589 | -6.36423 | -58.30841 | 2026-09-20 05:23:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 38deeec0-1b80-35b9-81c8-8ba10b1b2ac3 | -6.36078 | -58.28415 | 2026-09-20 05:23:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9643eedf-6cd4-3e1f-9bc3-aa9a5eb98042 | 2.84604 | -60.72991 | 2026-09-20 05:23:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a353c0dd-385c-3656-b6ea-aeff80a80cbe | -9.7004 | -54.82307 | 2026-09-20 05:23:00 | NOAA-21 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| a252f018-2996-3665-92db-e1b4ca87df8f | -9.68326 | -54.33554 | 2026-09-20 05:23:00 | NOAA-21 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 30488398-c90a-3f10-a3fd-00d5e8919252 | -10.20971 | -53.91663 | 2026-09-20 05:23:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ba718f25-7bf4-3ae9-a7f9-3c2cbe15369f | -3.89677 | -49.06651 | 2026-09-20 05:23:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 12.3 |
| 3c8c54f6-e6de-3894-9de9-b49b05496e74 | -2.82857 | -50.46604 | 2026-09-20 05:23:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 7d000b16-d1d3-3f25-9e91-4eb1d9c09a5a | -3.44902 | -59.25552 | 2026-09-20 05:23:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e5dcd829-585c-3960-9888-8292729429e9 | -7.31788 | -55.60926 | 2026-09-20 05:23:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 8c1be2a0-3e45-3c8b-a70e-641e93f20b1d | -8.63867 | -47.6193 | 2026-09-20 05:23:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 03a90620-9f1b-3461-a2b2-6e8033213e71 | -6.44813 | -59.98174 | 2026-09-20 05:23:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cba1ade2-f869-389d-b615-22344e0b8f35 | -2.91025 | -54.18924 | 2026-09-20 05:23:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7c8c0777-be49-37a5-bb42-8f62a62b43d4 | -2.91037 | -57.82439 | 2026-09-20 05:23:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f03583be-546e-36c9-b1af-0ad0d2918055 | -8.61421 | -54.58793 | 2026-09-20 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6c726c2f-ff45-3761-b457-350a712da059 | 0.69263 | -59.54848 | 2026-09-20 05:23:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 6c37fd3f-e4be-3b70-8056-3c625235bfd1 | -4.07526 | -52.12184 | 2026-09-20 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 9a8f0cca-35b4-3789-a110-5abf1fcf108f | -3.45285 | -50.59717 | 2026-09-20 05:23:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| e919d63a-7074-325b-8864-042ccb895008 | -9.17882 | -59.4235 | 2026-09-20 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 361f9078-52c7-3826-bc77-cec9932b5d20 | -8.17623 | -54.7362 | 2026-09-20 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 9c7e4a60-6c84-3865-abdd-b5789dbc0e68 | -8.42896 | -54.72907 | 2026-09-20 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9be266dd-ff12-34b0-8ad2-2f4661464ddf | -8.75822 | -48.66417 | 2026-09-20 05:23:00 | NOAA-21 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 076ef30a-f613-35d0-8c4a-a31a879e2167 | -6.13432 | -59.94361 | 2026-09-20 05:23:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 17a5fc5c-722b-3b9d-af0c-420d72b81b2c | -3.31027 | -57.87257 | 2026-09-20 05:23:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| da7032e7-f4f1-39e9-bb0b-d224162434a5 | -9.05501 | -48.71969 | 2026-09-20 05:23:00 | NOAA-21 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 3.6 |
| d479c569-6852-39a2-8df3-4b73af5dd3d4 | -9.18888 | -60.77211 | 2026-09-20 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d3ad83c4-3977-3316-8498-c96f1b062d97 | -2.82102 | -50.47904 | 2026-09-20 05:23:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 27c29f43-36b4-30b0-a93f-b6cc98fb9342 | -8.17382 | -54.75351 | 2026-09-20 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a276da17-11a3-3c17-a796-9940848f32d3 | -3.33408 | -59.81775 | 2026-09-20 05:23:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d7002104-5175-37c2-940c-83f90200476e | -3.07219 | -51.20068 | 2026-09-20 05:23:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 4f966a77-28bd-34b8-bb79-4045f088c9c8 | -7.0441 | -62.95794 | 2026-09-20 05:23:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| efe17ab1-f4e5-337c-8cd3-9d5094934bdd | -3.04316 | -51.105 | 2026-09-20 05:23:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9e9605cd-1bd3-3da8-9851-879257686956 | -8.25527 | -62.94028 | 2026-09-20 05:23:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1260f7a9-ab84-35ea-b953-a97163620396 | -1.9244 | -59.93779 | 2026-09-20 05:23:00 | NOAA-21 | PRESIDENTE FIGUEIREDO | AMAZONAS | Brasil | 1303536 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f824cc7e-bddd-3f68-98e1-95dc76beaac8 | -3.24866 | -60.88797 | 2026-09-20 05:23:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8dde98b9-107c-3f09-bc93-d96059d3e82d | -10.39053 | -51.87518 | 2026-09-20 05:23:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 1a31c7ad-c235-39d5-9552-077781de6923 | -2.97918 | -54.76936 | 2026-09-20 05:23:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0f287415-3c16-3c29-a794-fc7b71e505df | -8.19828 | -62.85582 | 2026-09-20 05:23:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 762ebc7c-ecf6-372a-8992-64d4f364b977 | -9.15515 | -49.99081 | 2026-09-20 05:23:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 6afdc571-e4ed-35e4-903a-12e049b01b3f | -3.07319 | -61.1808 | 2026-09-20 05:23:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d6f625ef-20e2-336b-84da-31686186adf1 | -3.29018 | -57.86566 | 2026-09-20 05:23:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| d309f38c-fc61-39f8-baab-06fdb665d2fe | -8.23034 | -50.65278 | 2026-09-20 05:23:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ff057911-57c1-3cb3-9b4a-3b790a5f5330 | -10.28134 | -50.27417 | 2026-09-20 05:23:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| dbbcf459-f1e7-33a8-8195-3eb09c773517 | -6.45093 | -58.1451 | 2026-09-20 05:23:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b11ddf80-59a4-35c7-b783-d47de70c3665 | -2.58934 | -59.99282 | 2026-09-20 05:23:00 | NOAA-21 | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| f86cdeed-8b74-32eb-bc90-d56f1b084172 | -8.17322 | -54.75782 | 2026-09-20 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 0929b32e-2a02-34ab-a183-f3509587c25f | -8.2366 | -50.64867 | 2026-09-20 05:23:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f09cea01-3cb0-39ae-b848-f6d3552ce9d8 | -3.11399 | -61.41633 | 2026-09-20 05:23:00 | NOAA-21 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f8b18bf2-7265-39b8-8c46-fccbc637b0a5 | -3.50692 | -59.05706 | 2026-09-20 05:23:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 824154ae-ff87-3a43-9842-34b81d97b158 | -3.2672 | -54.26308 | 2026-09-20 05:23:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f9962eba-cfc0-3d52-82e4-d03826eb4ae5 | -2.45251 | -49.21039 | 2026-09-20 05:23:00 | NOAA-21 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| c9217106-9563-338b-b535-312e67ca3b4c | -3.42963 | -58.19046 | 2026-09-20 05:23:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b46ca573-e5e5-312e-9c19-20250261bb65 | -6.3509 | -58.30241 | 2026-09-20 05:23:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b819308d-468f-3519-b319-4c712fc3d0cd | -2.7958 | -59.88769 | 2026-09-20 05:23:00 | NOAA-21 | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 27d48e36-1994-3e93-9f1f-408ef322666b | -5.22502 | -47.57999 | 2026-09-20 05:23:00 | NOAA-21 | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 4a58afaf-df14-3243-9802-b9e4eb646736 | -9.70036 | -48.32239 | 2026-09-20 05:23:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| ba8bad7a-7749-3522-be98-56e5dc5d39c4 | -6.13656 | -59.95108 | 2026-09-20 05:23:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5c0a4555-16bf-3302-8ff9-8601668b04fd | -6.2971 | -59.99068 | 2026-09-20 05:23:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4ba91621-d280-3e84-ab5a-24ac17921ca1 | 1.10557 | -59.64272 | 2026-09-20 05:23:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0821c259-7fe8-3463-8abc-1e38a9614b50 | -3.16038 | -58.68252 | 2026-09-20 05:23:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a56803a7-43e7-37be-bbf0-24efa982ed92 | -2.91393 | -59.3498 | 2026-09-20 05:23:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 27f60119-c564-31ad-ad75-676370a0429e | -2.25959 | -52.02729 | 2026-09-20 05:23:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 11f6280f-9658-3084-b6e8-131782285f2d | -8.23612 | -62.84283 | 2026-09-20 05:23:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ad07aea4-13d7-3df2-86cf-89f207e18a5c | -8.19886 | -62.85215 | 2026-09-20 05:23:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 56fcccdc-4036-3a8e-9f30-f759e2bc1101 | -2.86038 | -58.28801 | 2026-09-20 05:23:00 | NOAA-21 | SILVES | AMAZONAS | Brasil | 1304005 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7f0fbaa6-c93c-3341-aee9-370e09686581 | -8.17183 | -54.73557 | 2026-09-20 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 40c0c6d8-384d-3a4b-b054-90a0cdd6abd8 | -3.14766 | -61.39957 | 2026-09-20 05:23:00 | NOAA-21 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a7c88528-b9c7-3f4a-a40e-288899ecb9db | -3.15247 | -58.64489 | 2026-09-20 05:23:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 06f71893-d338-3e1e-ad73-384edc9e2107 | -2.71337 | -59.76613 | 2026-09-20 05:23:00 | NOAA-21 | RIO PRETO DA EVA | AMAZONAS | Brasil | 1303569 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |


[Clique aqui para ver as próximas entradas](README89.md)
