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

## Dados Diários - Página 138

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f87e3e60-2756-3bed-8847-58a7dc48ce59 | -3.86273 | -61.34108 | 2026-10-05 17:34:00 | NOAA-20 | BERURI | AMAZONAS | Brasil | 1300631 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 19e68b91-ab53-38ef-8a11-8ca571aa2e50 | -11.09128 | -60.72253 | 2026-10-05 17:34:00 | NOAA-20 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 15.6 |
| d7714519-1e1d-3f7b-8060-9a8fe171501a | -3.32286 | -59.4751 | 2026-10-05 17:34:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 32ba663b-6ce8-386b-a001-d48787238993 | -4.30721 | -54.79674 | 2026-10-05 17:34:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 17.8 |
| bf686d7e-b8bc-315d-bc27-fd4414e92172 | -8.34303 | -70.1022 | 2026-10-05 17:34:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 54.6 |
| fc10f61c-f325-3153-a736-f53e77d36897 | -3.47228 | -59.53964 | 2026-10-05 17:34:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| a4e44808-a729-3f19-822d-db12d46ed3e1 | -7.85333 | -69.93606 | 2026-10-05 17:34:00 | NOAA-20 | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 06cec853-74a2-3379-978f-bd43368bf96d | -3.51076 | -58.44268 | 2026-10-05 17:34:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 7e999a4a-db99-380d-930b-11c003ec4be6 | -3.84992 | -55.84211 | 2026-10-05 17:34:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 11f439d9-a173-3148-9375-62c23e891167 | -10.96032 | -60.90069 | 2026-10-05 17:34:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 05acf0c5-595c-3095-8ae1-9f44dfe3aa8c | -3.62435 | -58.61311 | 2026-10-05 17:34:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 5.2 |
| d9701909-a4ae-3168-b787-ca805f237482 | -7.76312 | -70.72788 | 2026-10-05 17:34:00 | NOAA-20 | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 1d67288d-821a-3b09-814a-5a9d7f9d62fa | -3.41245 | -58.01734 | 2026-10-05 17:34:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 6efe6f88-185e-3a30-b717-465f69da10f3 | -7.13268 | -71.53231 | 2026-10-05 17:34:00 | NOAA-20 | IPIXUNA | AMAZONAS | Brasil | 1301803 | 13 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 0f90f42e-69d5-3759-ad76-2c6b9ce7a027 | -3.56705 | -59.4261 | 2026-10-05 17:34:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 7.7 |
| a3677c48-5fab-392c-87e0-2f51e444e39d | -3.84937 | -55.8386 | 2026-10-05 17:34:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 90ec9630-b422-3495-b036-8c92e418d84e | -3.39482 | -59.5952 | 2026-10-05 17:34:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 96a15eb0-9d34-37bb-b951-cd161af84d04 | -4.15838 | -60.78605 | 2026-10-05 17:34:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 14.8 |
| 311394d9-b79f-3ad2-a869-e97106e54fb0 | -8.0633 | -71.15629 | 2026-10-05 17:34:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 71787eb6-da69-3b18-a580-ccf17b0d3378 | -3.49354 | -59.37477 | 2026-10-05 17:34:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 10.3 |
| a01db253-8942-339b-b27c-1d4e0ebf6885 | -3.77186 | -61.18932 | 2026-10-05 17:34:00 | NOAA-20 | BERURI | AMAZONAS | Brasil | 1300631 | 13 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 4be79770-2bdd-34ce-aded-b1f1db01a39b | -3.24411 | -58.75719 | 2026-10-05 17:34:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 0a8f3d2b-858f-33fc-9e4d-cdaa14d63509 | -10.87692 | -61.40712 | 2026-10-05 17:34:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 41f092e3-9f79-36db-b46a-b0e4f6e4fa08 | -3.72847 | -55.47429 | 2026-10-05 17:34:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 20.4 |
| fb681c70-78af-3999-a88e-200114c747f4 | -3.84507 | -59.60785 | 2026-10-05 17:34:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 2924c58b-a921-3733-8c99-593eb25edac3 | -2.93439 | -54.13065 | 2026-10-05 17:34:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 17.9 |
| ac28e6c4-4c58-3018-b483-b3ddc694b5fb | -2.95533 | -54.14266 | 2026-10-05 17:34:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 13.4 |
| 134f7b0a-6148-3961-9434-b099cd57106a | -3.86322 | -55.82209 | 2026-10-05 17:34:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 8d170d66-64d1-3315-871f-a6869f055135 | -7.94189 | -72.84553 | 2026-10-05 17:34:00 | NOAA-20 | CRUZEIRO DO SUL | ACRE | Brasil | 1200203 | 12 | 33 | nan | nan | nan | Amazônia | 14.3 |
| f8d6815a-ee48-3229-a668-64f142030f71 | -3.28243 | -54.18563 | 2026-10-05 17:34:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 28.1 |
| abe24f12-b38f-306d-a0a5-1baaa9627c70 | -3.03492 | -57.41739 | 2026-10-05 17:34:00 | NOAA-20 | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 3e9f4a0e-e829-3d02-a751-0de4e5a50ace | -3.08549 | -54.16219 | 2026-10-05 17:34:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 19.0 |
| 9316d6fd-b08a-33eb-8d5d-8423c2004b42 | -2.95763 | -54.15659 | 2026-10-05 17:34:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 16.5 |
| 02b90d8d-d8ed-32c7-bdbf-d474745dfd5e | -6.1819 | -55.42193 | 2026-10-05 17:34:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 797093cc-357e-3b17-b824-401fedfeba87 | -3.73018 | -59.41087 | 2026-10-05 17:34:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| fbd7e4e8-0402-3933-b775-f6b833fd87a4 | -2.48384 | -49.40953 | 2026-10-05 17:34:00 | NOAA-20 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 16.4 |
| 8d26671e-326f-3723-a5f1-7e55419325ce | -2.80149 | -54.09282 | 2026-10-05 17:34:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 97bee521-5c43-3a9d-9fcf-17c72c0c2b9c | -3.53725 | -58.59182 | 2026-10-05 17:34:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 427ebcfd-7ab9-3b18-af75-723dbc4d4f5c | -11.11335 | -46.09131 | 2026-10-05 17:34:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 48cf98d4-1963-3c00-8b4b-7588cd0179ea | -3.47912 | -55.43085 | 2026-10-05 17:34:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 1c780209-3374-36b4-8944-8e0e98b5c265 | -2.95322 | -54.161 | 2026-10-05 17:34:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 15.0 |
| 7b16ed9a-5ccb-30c0-af79-113e9e9e1428 | -7.39302 | -70.11696 | 2026-10-05 17:34:00 | NOAA-20 | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 2396cc3e-e532-37e5-89de-a7d9a032612c | -2.86505 | -54.13662 | 2026-10-05 17:34:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 547a2c37-4ade-3c37-9b83-76267887b521 | -3.58383 | -54.31074 | 2026-10-05 17:34:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 24.4 |
| 80961b9a-f96d-3d15-a067-a5a709a87cfc | -8.88695 | -72.77571 | 2026-10-05 17:34:00 | NOAA-20 | MARECHAL THAUMATURGO | ACRE | Brasil | 1200351 | 12 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 2a292e86-c240-377a-9bb4-ae090fef5ac1 | -3.49436 | -57.77501 | 2026-10-05 17:34:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 0da3cdad-3407-32aa-bfcd-14ddb76abd79 | -4.19232 | -59.41189 | 2026-10-05 17:34:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 11.6 |
| 60ba9aa6-3135-3499-a887-1cc325360143 | -3.07035 | -54.15527 | 2026-10-05 17:34:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 27.0 |
| ecf08a52-d853-3bb6-894e-213681ee8ded | -10.51651 | -46.0656 | 2026-10-05 17:34:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 23.5 |
| 6ce0fe54-7dba-3555-ad66-f6a8f1386dc4 | -3.2372 | -58.75824 | 2026-10-05 17:34:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 55a0e7de-9b1f-35d8-8e1d-d67facaa505e | -3.589 | -54.31441 | 2026-10-05 17:34:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 18.4 |
| 99570e89-6994-3763-9dcf-5fa29ace6207 | -3.66936 | -58.22659 | 2026-10-05 17:34:00 | NOAA-20 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 9505c184-b896-3d1a-9f8e-8dc3843e269c | -6.18761 | -55.35815 | 2026-10-05 17:34:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| c7618727-8c82-3261-88ca-b3b96fa7c674 | -8.0689 | -70.49281 | 2026-10-05 17:34:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 6.3 |
| ed61d90b-ea19-3835-a490-f98393e4899f | -3.11896 | -57.64684 | 2026-10-05 17:34:00 | NOAA-20 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 7.5 |
| b98d1ac2-6926-3047-b8b5-263e243fbdab | -4.10292 | -59.10143 | 2026-10-05 17:34:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 14bfad97-fe9a-317a-b544-6f814f8cd5df | -3.59998 | -58.15237 | 2026-10-05 17:34:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 0c567975-25c0-3415-9d6a-294073f294c9 | -2.95249 | -54.15633 | 2026-10-05 17:34:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 15.0 |
| 5a83e098-6895-3d8e-8113-ddc99656aab5 | -3.86834 | -55.82845 | 2026-10-05 17:34:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| ab667c03-de00-3ad3-ac4c-0e5671b0a917 | -10.51411 | -46.05366 | 2026-10-05 17:34:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 19.0 |
| cc64a4f8-22d7-3c51-ac2e-1053b3861dc3 | -6.38634 | -60.04007 | 2026-10-05 17:34:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 9.6 |
| f5de5b9d-6d1d-3bc2-a34a-48ffaf1d1f86 | -3.48344 | -54.72661 | 2026-10-05 17:34:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 9e3bf932-47f4-33c6-9673-daf5f3cbce23 | -3.91903 | -59.66535 | 2026-10-05 17:34:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 8.2 |
| d162ab55-b887-3b2b-b9ec-00a7286f7488 | -8.61972 | -47.15162 | 2026-10-05 17:34:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| d7c605d9-68bf-3f97-b447-06462f81935f | -4.08257 | -59.12679 | 2026-10-05 17:34:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 4c0512fa-ba0d-3b6e-8e37-8c859d3bf853 | -6.89777 | -71.50497 | 2026-10-05 17:34:00 | NOAA-20 | IPIXUNA | AMAZONAS | Brasil | 1301803 | 13 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 096f8c12-3903-3427-9320-885670e41f6b | -3.37918 | -58.19846 | 2026-10-05 17:34:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 100.0 |
| dfc459ba-ff04-31ff-baf2-b7d100905da0 | -10.51516 | -46.0505 | 2026-10-05 17:34:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 14.4 |
| 1d8d7392-529d-3a41-a858-87c32e2ebc53 | -3.78059 | -59.32542 | 2026-10-05 17:34:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 3c8061d8-63c5-3d5f-b261-9b191d30c364 | -3.06504 | -54.15141 | 2026-10-05 17:34:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 81.4 |
| 62fdaa74-5e63-34ef-8620-de32b630ae33 | -13.5193 | -61.12931 | 2026-10-05 17:34:00 | NOAA-20 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 39519951-ea59-31cb-9f53-6f952eb116af | -10.48228 | -47.24059 | 2026-10-05 17:34:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| ae9ab7df-4d91-3001-8673-db98101d9ca5 | -3.52031 | -54.61641 | 2026-10-05 17:34:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 4a0e5d9d-7f40-3571-a655-0fb7e56d5877 | -3.34737 | -58.20322 | 2026-10-05 17:34:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 0d0b3e19-4aa5-3ce5-ade4-67303b3466dd | -3.09087 | -58.2985 | 2026-10-05 17:34:00 | NOAA-20 | SILVES | AMAZONAS | Brasil | 1304005 | 13 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 81dfe2ea-caee-3443-97a1-0bb78acdcb49 | -3.4252 | -59.72495 | 2026-10-05 17:34:00 | NOAA-20 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 10.2 |
| efec1a2c-9a2c-3831-9436-d4485bd1bc23 | -3.21661 | -56.84052 | 2026-10-05 17:34:00 | NOAA-20 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 10.8 |
| ee6b27f2-1768-3450-b9b7-0f0cac0e055a | -11.34996 | -46.67508 | 2026-10-05 17:34:00 | NOAA-20 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| a9a808dc-3648-37ae-aec4-68cf43aefb51 | -3.09312 | -54.18032 | 2026-10-05 17:34:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 20.6 |
| a9ec0083-5740-319b-a2c2-594ab0823f76 | -3.16962 | -58.86872 | 2026-10-05 17:34:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a0be1ea1-b800-381e-b429-724d8e5500ec | -3.48114 | -55.43045 | 2026-10-05 17:34:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 18.2 |
| 9917de50-594e-39a7-ab31-844c2beeaa6d | -12.13684 | -63.16991 | 2026-10-05 17:34:00 | NOAA-20 | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 185c3077-f8ff-3767-b6e8-b6d71f4159dc | -3.69391 | -55.95541 | 2026-10-05 17:34:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 26.9 |
| d44c6d79-0d3d-3218-a5a2-89a2dd182e58 | -5.89766 | -55.52343 | 2026-10-05 17:34:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 15.5 |
| 4cb668e0-e2c7-3888-b1b9-70a8b5389eb1 | -10.86283 | -68.68732 | 2026-10-05 17:34:00 | NOAA-20 | EPITACIOLÂNDIA | ACRE | Brasil | 1200252 | 12 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 1fbdad35-0516-3584-981a-7ac072f4cc9c | -3.54496 | -59.48447 | 2026-10-05 17:34:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 11.7 |
| 865f7824-04fa-3f9c-99e5-61f1895e9115 | -2.98972 | -54.03681 | 2026-10-05 17:34:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 3e35eb8f-d668-30a3-b2f0-16f03b2b428a | -2.93292 | -54.12134 | 2026-10-05 17:34:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 16.2 |
| 53f3dd99-1f4f-3a1a-8174-f885e56ead3d | -5.22671 | -60.20325 | 2026-10-05 17:34:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 47.7 |
| 670d8c5e-4698-37df-9506-340983fb5edd | -2.78235 | -54.0909 | 2026-10-05 17:34:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 20.3 |
| 5f15f5bd-acfc-3762-a0c4-12bb88b2ec22 | -3.28768 | -53.84494 | 2026-10-05 17:34:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 8b1b998d-531b-3ed1-9a79-c4dc2fbf4802 | -11.10948 | -46.0906 | 2026-10-05 17:34:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 18.7 |
| 109225a6-3248-3516-8e9f-5c24e5d0d3b1 | -3.08018 | -54.15831 | 2026-10-05 17:34:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 19.0 |
| cd290d20-f0e2-323c-a7f9-8ea46b828ee7 | -3.58509 | -55.40251 | 2026-10-05 17:34:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| cfc42ffa-69ba-3efb-875f-bd06c4e1755d | -3.37439 | -58.19107 | 2026-10-05 17:34:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 23.2 |
| b0e2e7c6-34ef-3e40-98db-0dd1eeff0c99 | -3.37566 | -60.68393 | 2026-10-05 17:34:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 5.2 |
| c1f98772-18fb-3399-bde5-6211845bb5d5 | -6.59066 | -69.89838 | 2026-10-05 17:34:00 | NOAA-20 | EIRUNEPÉ | AMAZONAS | Brasil | 1301407 | 13 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 83e62352-774b-3fd7-aac8-36aeae01cd34 | -3.83063 | -55.79832 | 2026-10-05 17:34:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| c0f48cd7-1c09-34ce-a734-ded3a1c39566 | -4.05665 | -54.03538 | 2026-10-05 17:34:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| f9cf7c9e-b58b-3ae6-a641-9e59a1676291 | -8.27662 | -71.11964 | 2026-10-05 17:34:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 9.2 |


[Clique aqui para ver as próximas entradas](README139.md)
