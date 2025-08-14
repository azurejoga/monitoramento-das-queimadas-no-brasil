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

## Dados Diários - Página 29

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5d23cef3-48d6-39a6-be2f-14bae44aea83 | -6.90695 | -59.12843 | 2025-08-14 05:10:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b7f36e46-d38a-3d76-904c-7b74bdb17e89 | -5.75343 | -59.89186 | 2025-08-14 05:10:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e1037cda-c3ae-35a5-b26d-4696220c3b5d | -7.32984 | -60.62673 | 2025-08-14 05:10:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 7f190176-09a0-3cfa-8a32-20d0ab957d23 | -6.88212 | -59.13189 | 2025-08-14 05:10:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c9345ee9-9183-353b-86d3-4467a6e86199 | -7.6321 | -63.51749 | 2025-08-14 05:10:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b81e069d-faac-371d-b510-e4ac6427ee53 | -9.20837 | -59.64974 | 2025-08-14 05:10:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bea354d9-3bbd-385d-9df7-b12726d1332b | -6.87477 | -59.13441 | 2025-08-14 05:10:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 04ed4cde-b21d-380b-8c05-0ef48200a9a9 | -6.8855 | -59.13242 | 2025-08-14 05:10:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c45d5bfd-fdee-3947-9667-6821ba159890 | -9.16075 | -59.65753 | 2025-08-14 05:10:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 40ac1f9a-e52d-30c6-bb3d-2c3ce1b4f9b6 | -7.56013 | -63.48171 | 2025-08-14 05:10:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1684d07f-0794-32b6-92b0-109cd1ce1e62 | -7.09212 | -60.01921 | 2025-08-14 05:10:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ef8c3ff2-7e1c-3416-b02b-8eaeff2af469 | -10.36227 | -50.80869 | 2025-08-14 05:10:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 7342ee89-1e0b-35d1-87fd-8ea945238557 | -9.12795 | -59.66714 | 2025-08-14 05:10:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 8671f916-afa8-3c2f-9f48-1785a71338e8 | -6.10183 | -59.93692 | 2025-08-14 05:10:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 03d01d05-5dc5-3485-9fcc-03f96035bf57 | -9.20718 | -59.65704 | 2025-08-14 05:10:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| cc5e56b7-001e-3955-8520-3f1eefa3c6c2 | -9.06086 | -60.65851 | 2025-08-14 05:10:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b39785f6-23ee-396e-b9a8-74da4339b06a | -5.75881 | -59.88071 | 2025-08-14 05:10:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a95d1bdb-29cd-3553-a70b-bcff5a3a5412 | -6.85815 | -59.96692 | 2025-08-14 05:10:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| d368ea33-5a29-30d1-8185-1d87e70e4517 | -7.08452 | -60.02197 | 2025-08-14 05:10:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| eac1b504-2429-38c2-b29c-6b550ce07b07 | -9.05515 | -60.64942 | 2025-08-14 05:10:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2b1453d7-caec-3d4f-aaf0-3bd26cb22ce5 | -8.1148 | -61.20887 | 2025-08-14 05:10:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2b5c87b4-497f-3d37-aa46-28593da9d9bc | -9.13708 | -59.65363 | 2025-08-14 05:10:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c4a22e36-d2b0-3957-ad1d-69588e1c0d3a | -6.48288 | -55.89732 | 2025-08-14 05:10:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 19d26d16-37e1-3608-9a12-43a9d67b750e | -7.89095 | -61.47797 | 2025-08-14 05:10:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4402836a-10e9-3511-8edd-0db193995066 | -7.87572 | -61.80764 | 2025-08-14 05:10:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 5.4 |
| e91ef2ba-46f2-3f91-b725-80024697c903 | -7.4566 | -60.40568 | 2025-08-14 05:10:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 655994cf-1fc8-3991-9641-4047f9023da5 | -7.17395 | -59.64625 | 2025-08-14 05:10:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4b20f185-25cb-31ea-88b0-af40a2da8480 | -7.55542 | -63.48392 | 2025-08-14 05:10:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ba1dc3df-8e19-3aba-af35-56d84a8b6979 | -5.73174 | -59.89244 | 2025-08-14 05:10:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1a771680-79c2-34a8-89f7-20f2701d2794 | -6.91079 | -59.14769 | 2025-08-14 05:10:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.9 |
| eea9919c-d6ab-3458-b905-b93397f362fe | -7.8674 | -61.81097 | 2025-08-14 05:10:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| bb26f4e1-58a5-37fe-b5f2-128256afff45 | -9.15093 | -59.4178 | 2025-08-14 05:10:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 938dc1e4-9d15-329f-aed8-3fa272c2531e | -6.87124 | -59.15618 | 2025-08-14 05:10:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.1 |
| e9c53740-ac24-3f7c-9bb1-ef27d28005f6 | -6.09769 | -59.94028 | 2025-08-14 05:10:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b96301b6-7948-368c-8805-69576ea5b0d4 | -6.88197 | -59.15419 | 2025-08-14 05:10:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 1271c95b-4634-3fe4-9838-0e3c4da50de2 | -9.15281 | -59.66372 | 2025-08-14 05:10:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 12.1 |
| dc6f444b-5835-3d38-bfc6-000b2d70b0f1 | -9.16458 | -59.67691 | 2025-08-14 05:10:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b246e940-1988-36c4-8964-59d868739854 | -9.13767 | -59.64998 | 2025-08-14 05:10:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 4c080e4f-f65a-3f00-87f8-61df63c29952 | -7.27529 | -57.64857 | 2025-08-14 05:10:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 11d49e1b-9cad-3b36-9126-b15bf4c38561 | -7.24045 | -59.99563 | 2025-08-14 05:10:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9392d6cf-81cf-3e80-865e-48e66d031392 | -9.82622 | -60.76457 | 2025-08-14 05:10:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 688b0a57-acd9-3e54-92e6-ebdab7b7f13d | -9.71704 | -56.18182 | 2025-08-14 05:10:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bc9aa6fb-f98a-3104-add3-9b00b1f8ae6d | -7.07766 | -59.20337 | 2025-08-14 05:10:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d75ad3e2-471c-3939-a2d9-600f5715124b | -7.59837 | -63.51161 | 2025-08-14 05:10:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| faea0e16-526d-302e-9de2-6ba0a2094699 | -8.11186 | -61.20402 | 2025-08-14 05:10:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| bd0dad25-e1aa-31ec-b81b-3c58523d5aa8 | -5.75756 | -59.88851 | 2025-08-14 05:10:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2bf4b830-7b18-379b-8a19-4477f75bc4f0 | -7.45683 | -59.89257 | 2025-08-14 05:10:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| eb00a39f-2c28-3fc4-81c6-816e8b4aa285 | -9.38519 | -61.52808 | 2025-08-14 05:10:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 734a4ac7-13bc-3780-b4ae-5d94a3f2a0dd | -5.88733 | -57.74684 | 2025-08-14 05:10:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f7f95f07-384a-3088-a1f4-15c48a133487 | -6.09354 | -59.94365 | 2025-08-14 05:10:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 988d74e0-5c30-3dd5-9b18-783f2c7dda52 | -5.75919 | -59.90085 | 2025-08-14 05:10:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 16d55481-b02d-3fb7-88f1-4f3e46deca79 | -7.2613 | -59.99898 | 2025-08-14 05:10:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ce14962b-bf5e-3fda-af2a-2215ea28fba1 | -6.90357 | -59.12788 | 2025-08-14 05:10:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 20e0c7a4-581c-3b44-8c7b-763044a2b76b | -6.09003 | -59.94311 | 2025-08-14 05:10:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 5.3 |
| db7c6317-94cd-3370-b2c4-f4447c15ca6c | -7.10355 | -56.7735 | 2025-08-14 05:10:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 741c7723-933f-3038-9810-e1ad4e6ecce1 | -7.07428 | -59.20281 | 2025-08-14 05:10:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 463726b2-addb-3fd1-a8e9-96c9769259a8 | -6.61094 | -43.88494 | 2025-08-14 05:10:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 568a99fc-365f-3ad9-a530-4ff7f54e0423 | -9.19526 | -59.66631 | 2025-08-14 05:10:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c0a1956f-07cd-3115-bae8-c4003ebbf2c4 | -6.09418 | -59.93975 | 2025-08-14 05:10:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 6b9a95bd-47fb-331c-91a3-c907e2804825 | -7.52376 | -61.38118 | 2025-08-14 05:10:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 762064d9-7f57-374d-841f-75032d16d3b7 | -8.10893 | -61.19915 | 2025-08-14 05:10:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 04dbd105-4811-33e1-85c6-2f54885bba6f | -5.89119 | -57.74392 | 2025-08-14 05:10:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 6f4d0459-c1dc-3e69-a020-f8f957bd798e | -6.88131 | -56.47578 | 2025-08-14 05:10:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| d508695f-64c2-3bb8-8e3e-97029402f081 | -6.9376 | -59.63227 | 2025-08-14 05:10:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 48764747-aa75-3ec4-bb68-64f25afac3b7 | -7.0696 | -59.20267 | 2025-08-14 05:10:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fb2ddd5a-228f-330e-99d8-1ad2c3f46acf | -6.87918 | -59.15001 | 2025-08-14 05:10:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.6 |
| f7fef031-7e78-3775-aa86-e25967fc4360 | -9.20321 | -59.66014 | 2025-08-14 05:10:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9c757e4f-c001-3b49-8d22-636bf37335e0 | -5.75406 | -59.88795 | 2025-08-14 05:10:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 824c64b3-e9a1-3c42-a968-ba86059c4e1d | -7.33697 | -60.62791 | 2025-08-14 05:10:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b5961780-bb37-39eb-b374-d0ad395c1921 | -6.91295 | -59.63209 | 2025-08-14 05:10:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9b8f64e7-73ce-37c9-a70b-8549421a97dc | -7.60613 | -63.51701 | 2025-08-14 05:10:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 39a05b21-563c-326e-84e3-86485d564dcd | -9.94098 | -60.46878 | 2025-08-14 05:10:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8704b2e9-5585-301f-bbbe-dcf1a2fe50d5 | -7.07356 | -59.19958 | 2025-08-14 05:10:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| dcba6889-1e5a-3b5d-a4d4-e2cb153b8eed | -7.82132 | -61.32646 | 2025-08-14 05:10:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8a5815db-fa8b-35ce-b3cc-00678bf59945 | -6.08781 | -59.93474 | 2025-08-14 05:10:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 8aea5f61-5976-30e9-a84c-ca10ec17b671 | -8.1141 | -61.21311 | 2025-08-14 05:10:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3c9299ba-12cf-39ed-8376-d337702d3114 | -7.2597 | -60.63703 | 2025-08-14 05:10:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7fc1cb32-6505-33ca-a6d2-205edf60e2d8 | -6.89889 | -59.15694 | 2025-08-14 05:10:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 61f0acd9-b248-380c-8cf2-13a917123bac | -8.90087 | -60.59341 | 2025-08-14 05:10:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1bf29229-ffd9-31fd-b0e2-1d89651bb3fe | -6.11012 | -59.93021 | 2025-08-14 05:10:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e506b5af-2f81-3cc2-82ba-a0558c760143 | -7.60259 | -63.51234 | 2025-08-14 05:10:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 5ecc60fe-c6d9-3f38-9db0-b835230e8848 | -5.75055 | -59.8874 | 2025-08-14 05:10:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2181456f-bad6-3d0f-8aa5-875578ef3974 | -6.77411 | -55.48738 | 2025-08-14 05:10:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 58969ba8-bfc6-3233-9632-3e2855f567fe | -7.32694 | -60.62203 | 2025-08-14 05:10:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| f695986b-136d-314a-aa9a-40b2bc55659b | -6.88815 | -59.15891 | 2025-08-14 05:10:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 10.1 |
| d5b2d5c1-a348-3d06-aea4-9a76afaa91c2 | -6.07506 | -59.94107 | 2025-08-14 05:10:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5fbf296f-5994-3469-9c4b-757d417c710f | -6.0929 | -59.94757 | 2025-08-14 05:10:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 78f602d8-09ee-3c25-8503-66f282677b39 | -6.91196 | -59.14042 | 2025-08-14 05:10:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.7 |
| d9b0a783-3135-3d61-a15c-b9fe37467f4f | -9.60645 | -55.14647 | 2025-08-14 05:10:00 | NOAA-20 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| dd1b1756-e19f-324c-9c5b-20d192418873 | -6.94658 | -44.55039 | 2025-08-14 05:10:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 11.1 |
| f49a60e3-ecfe-3a3b-9f2a-305b27b7ed51 | -6.91092 | -59.12534 | 2025-08-14 05:10:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e6b87568-510a-3473-b15b-75261f9cb4bd | -6.10534 | -59.93747 | 2025-08-14 05:10:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 74321477-dd31-387f-a1d1-d249f1b44e25 | -8.10741 | -61.18576 | 2025-08-14 05:10:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 0731e337-ce1e-3dd9-a322-0cc092c4e5e8 | -6.88491 | -59.13607 | 2025-08-14 05:10:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a2c05281-c6f7-34c0-8ef8-ad48fa3b6b42 | -7.12519 | -60.12434 | 2025-08-14 05:10:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 87610f0b-3a51-33cf-a7da-8e9d8a3995d1 | -7.31556 | -60.62437 | 2025-08-14 05:10:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5aff8d3c-066f-33b4-9aa2-191e31e05543 | -6.90402 | -59.1466 | 2025-08-14 05:10:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 63458f7a-ae8c-3dad-93e4-a08a398a1ada | -6.90483 | -60.09829 | 2025-08-14 05:10:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| dbe32da5-5725-38c2-9ddf-698ba37267c8 | -6.90019 | -59.12733 | 2025-08-14 05:10:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fe80345f-911c-375b-892c-7ce6c51ea2b3 | -5.7617 | -59.88517 | 2025-08-14 05:10:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |


[Clique aqui para ver as próximas entradas](README30.md)
