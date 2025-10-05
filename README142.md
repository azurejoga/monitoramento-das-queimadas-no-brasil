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

## Dados Diários - Página 142

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1dea7c02-97c4-36f5-8fcb-a14794cd5a35 | -13.73565 | -51.27512 | 2025-10-05 05:36:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 8f27723a-dee8-350a-9bb3-440af3afd660 | -10.46974 | -57.50258 | 2025-10-05 05:36:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4c1b14a0-1568-31aa-90f1-f7b3490740f5 | -11.39861 | -55.17909 | 2025-10-05 05:36:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5d895255-98ec-3e83-8058-f6855114a23f | -10.07153 | -62.50122 | 2025-10-05 05:36:00 | NOAA-20 | THEOBROMA | RONDÔNIA | Brasil | 1101609 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cde0ce00-42c0-3d72-8f44-678afca04020 | -12.40767 | -51.10416 | 2025-10-05 05:36:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 13f67cab-a955-3fe0-90a9-dbafcceca3f3 | -9.16459 | -62.22702 | 2025-10-05 05:36:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2b5debb2-d226-3a23-8df5-a5f6f255988c | -12.31623 | -55.14919 | 2025-10-05 05:36:00 | NOAA-20 | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e1f4b4c2-d121-31fe-8edf-6588a18978e3 | -9.81881 | -67.56978 | 2025-10-05 05:36:00 | NOAA-20 | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| eaa26174-947a-3976-8bcd-e401d837cffc | -9.32947 | -62.1786 | 2025-10-05 05:36:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7498b747-7e93-3c88-ab7c-53c12931e12f | -8.42819 | -70.12931 | 2025-10-05 05:36:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 2106ecdf-f2b2-3034-88f0-f95c019f99fe | -12.3158 | -55.15277 | 2025-10-05 05:36:00 | NOAA-20 | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b0626ba8-4326-3647-8452-745fa47e0974 | -10.64825 | -58.75511 | 2025-10-05 05:36:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1becd3e4-bd98-38fc-b619-9024d7d74cbe | -9.03735 | -61.64385 | 2025-10-05 05:36:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2667c852-503f-35d9-85c7-6d85ecafda72 | -8.42794 | -70.11897 | 2025-10-05 05:36:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 8f65fffe-8a58-3962-a0d4-e4adc7852fb9 | -12.23661 | -60.33585 | 2025-10-05 05:36:00 | NOAA-20 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e20d8441-e022-3272-a3c8-eda370e14cff | -8.59278 | -63.17605 | 2025-10-05 05:36:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bad682f3-6044-3b65-bedf-0ba145d1a796 | -8.82304 | -64.24332 | 2025-10-05 05:36:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 630c9010-7cb4-31d5-b0c6-fb26b938b85f | -8.42654 | -70.12721 | 2025-10-05 05:36:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 7da00a7a-4d4a-3e9e-ab75-f18ec0127d9d | -9.85185 | -59.83649 | 2025-10-05 05:36:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9077a9e5-3cd6-3f59-b3df-6dc4e482cc2f | -12.30559 | -55.14423 | 2025-10-05 05:36:00 | NOAA-20 | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bb58d612-f7ae-3011-8e34-2c90e851bc73 | -11.84846 | -63.72108 | 2025-10-05 05:36:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4e84a911-a4f7-381d-aaf2-0ccbe7ba1417 | -8.6685 | -64.10463 | 2025-10-05 05:36:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 04d94dda-934e-35d3-86fe-a8e2f8d395d1 | -9.71599 | -67.46735 | 2025-10-05 05:36:00 | NOAA-20 | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f8e1a5cb-7ccb-3ba8-99c7-d80534c1b1cd | -11.87534 | -56.88631 | 2025-10-05 05:36:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 9.4 |
| d6bc8c29-9901-3b99-9789-7bd08217ba5e | -12.31112 | -55.14497 | 2025-10-05 05:36:00 | NOAA-20 | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e2f9ed0d-da79-3734-8c51-5d5620648e89 | -10.05974 | -59.35823 | 2025-10-05 05:36:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 0bab7ade-bc44-3b07-80d7-9b3c63f71fc1 | -9.85171 | -59.83453 | 2025-10-05 05:36:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8c77667d-18eb-3cf6-a37c-13bfd8763dbd | -11.82802 | -60.48687 | 2025-10-05 05:36:00 | NOAA-20 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 106f1929-450f-3f8b-a513-825858b6ee84 | -9.20131 | -59.40695 | 2025-10-05 05:36:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 88e7c9f1-d90d-3b35-9ecc-6cf5f7635f03 | -9.31515 | -54.53711 | 2025-10-05 05:36:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| aaf9bb20-d322-302a-999f-ea3b706b761e | -10.07837 | -62.50228 | 2025-10-05 05:36:00 | NOAA-20 | THEOBROMA | RONDÔNIA | Brasil | 1101609 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| be8c1e92-e159-38ae-963b-89343d96fee0 | -8.82953 | -62.35989 | 2025-10-05 05:36:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 7d9d6622-b40a-3b2f-8ef9-2f5c55e6eaca | -9.21828 | -62.47174 | 2025-10-05 05:36:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c2df030f-0170-3885-a580-711767740352 | -9.13334 | -61.87645 | 2025-10-05 05:36:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f655725d-9b22-3739-bb55-9f7cde440447 | -9.18826 | -62.53121 | 2025-10-05 05:36:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b7fd57ed-299c-387f-80c5-005375a09a88 | -9.63655 | -54.31879 | 2025-10-05 05:36:00 | NOAA-20 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fe1282be-5e78-3866-bce2-7efd0748f4b7 | -12.97773 | -51.03621 | 2025-10-05 05:36:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 82eef3bd-0c1c-3431-b140-feb46e067856 | -9.54858 | -54.59798 | 2025-10-05 05:36:00 | NOAA-20 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bfe7b0f9-58bc-3fd7-a856-e49934e6ff32 | -8.32097 | -70.19801 | 2025-10-05 05:36:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b0ef99fa-bc80-32c1-a5a4-d18a6560bdd6 | -8.42535 | -70.12032 | 2025-10-05 05:36:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 59e03352-653e-33b9-96c0-8b00c5f5995a | -10.38667 | -67.96577 | 2025-10-05 05:36:00 | NOAA-20 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a720b726-b44c-306c-9ce0-424b2fde4771 | -9.14552 | -60.29693 | 2025-10-05 05:36:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f20d969b-7dd5-3fcb-8418-733dd3ba763c | -12.97056 | -51.0354 | 2025-10-05 05:36:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 8f8c5a24-6b3c-3aa2-84e4-61c40ac61fcc | -12.41151 | -51.10406 | 2025-10-05 05:36:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f79a7481-4f2e-3fb4-b8bb-6290a4407229 | -10.06701 | -63.51895 | 2025-10-05 05:36:00 | NOAA-20 | MONTE NEGRO | RONDÔNIA | Brasil | 1101401 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6788b19a-6a67-34cd-b5a3-957f05be3bcb | -12.41079 | -51.11106 | 2025-10-05 05:36:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 20f2dd2d-f44e-3318-94d1-606f8fe7eb25 | -9.64562 | -54.31965 | 2025-10-05 05:36:00 | NOAA-20 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0f774e14-60f1-37c3-b6dc-9bfc4eaa5857 | -9.21885 | -62.46806 | 2025-10-05 05:36:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6b937d08-f4fe-34a9-990a-f64adff4b25f | -9.34482 | -54.52553 | 2025-10-05 05:36:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 43cef072-a4f4-3420-bcab-a24bf2844519 | -9.9259 | -67.42394 | 2025-10-05 05:36:00 | NOAA-20 | SENADOR GUIOMARD | ACRE | Brasil | 1200450 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f3fc3cd1-b26a-3900-b455-efe9580df293 | -12.31537 | -55.15636 | 2025-10-05 05:36:00 | NOAA-20 | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cb52f1ee-7e6b-3e31-ae76-f24de1946695 | -9.85868 | -60.28032 | 2025-10-05 05:36:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.3 |
| f22c8718-8543-3aea-ac5a-911ef8c359f7 | -9.85177 | -60.27449 | 2025-10-05 05:36:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 64fb4636-98a4-38be-8e70-c8b0d40bf80c | -10.83633 | -57.17897 | 2025-10-05 05:36:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 940876a8-1281-3412-a98f-0631bc2427d3 | -11.20956 | -54.85399 | 2025-10-05 05:36:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0fab40bf-55c3-3a4f-87b8-6ee505e237fd | -9.62152 | -64.67137 | 2025-10-05 05:36:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1054588e-4037-32be-8b27-836c1a9cf8f3 | -8.43176 | -70.1342 | 2025-10-05 05:36:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| fbe9dd95-d8d7-36ba-a02d-bf2a8b3dd3f1 | -9.18882 | -62.52753 | 2025-10-05 05:36:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5a5dd95c-faed-3a98-a823-7187104a6325 | -13.73492 | -51.28226 | 2025-10-05 05:36:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 8.1 |
| e2e65ba2-ca90-3008-a4f1-5505010d002e | -11.86863 | -56.88195 | 2025-10-05 05:36:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 7.5 |
| f0f73118-a7e1-3376-bae0-edefda368d20 | -12.31494 | -55.15996 | 2025-10-05 05:36:00 | NOAA-20 | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1b12ab5b-80f9-314b-a060-1463dbc5a7a2 | -12.30645 | -55.13694 | 2025-10-05 05:36:00 | NOAA-20 | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f5a3cdb1-ec50-358c-b0d9-501ddd06eee6 | -9.8435 | -60.27804 | 2025-10-05 05:36:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 20d04fab-fe9c-3574-a30f-b05ab524b205 | -9.60646 | -58.98397 | 2025-10-05 05:36:00 | NOAA-20 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f7dcfa83-f495-398e-b8f5-f879c9797155 | -9.65461 | -63.79324 | 2025-10-05 05:36:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| bad501b2-e28f-30a2-a756-7a812fed7449 | -11.98847 | -64.10922 | 2025-10-05 05:36:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 94fb277a-22a7-3533-b73f-1d3cac7d7c04 | -12.3069 | -55.13323 | 2025-10-05 05:36:00 | NOAA-20 | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2df2e0af-0133-3c37-afd2-092f35c7d7d2 | -14.58486 | -52.4545 | 2025-10-05 05:36:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e10b4566-1633-38bc-b576-def38cab28cd | -10.65566 | -58.76411 | 2025-10-05 05:36:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a61df8aa-f4b1-3275-9d7c-616f05c76bb7 | -13.73273 | -51.30355 | 2025-10-05 05:36:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7fd8ed1d-21ab-35e5-a0e8-a5a367a8795c | -12.22494 | -56.63793 | 2025-10-05 05:36:00 | NOAA-20 | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 060e2995-9ec9-33db-a96a-dbfec01d8c28 | -9.1592 | -58.3101 | 2025-10-05 05:36:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 189166f3-8c5b-33d2-9335-d74ffed7791a | -12.31027 | -55.15207 | 2025-10-05 05:36:00 | NOAA-20 | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5bc4aba8-619a-3831-b08d-890f7a760962 | -11.86969 | -56.89127 | 2025-10-05 05:36:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 3e607b10-14ae-3077-b7ed-8f1ea483a8ec | -9.85489 | -60.27975 | 2025-10-05 05:36:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0f1a0772-23b2-3e52-91b8-89255d973ad7 | -9.24062 | -65.69373 | 2025-10-05 05:36:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| adaf609f-1dd5-30f6-9be4-87ec793f5b21 | -7.73623 | -63.3152 | 2025-10-05 05:36:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 40382df4-1d9b-328e-b599-fbdf6a7d0bcf | -12.84247 | -58.76475 | 2025-10-05 05:36:00 | NOAA-20 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 143962b0-6309-3289-ae03-2c0814532512 | -10.84037 | -57.18465 | 2025-10-05 05:36:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| cfa5f69c-3cef-333e-b4e0-1f3968742796 | -9.19645 | -59.55215 | 2025-10-05 05:36:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 295b3afa-998f-334e-86e3-b37d256a4610 | -10.83968 | -57.18972 | 2025-10-05 05:36:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f79515f3-4d1f-34ee-a151-4c5e14fe7649 | -11.7677 | -64.86813 | 2025-10-05 05:36:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bd571770-b6f8-30cb-97da-0fab20a15198 | -9.19222 | -62.52806 | 2025-10-05 05:36:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 993acc2b-25f4-3a43-b718-292fd1e32486 | -9.90647 | -66.73085 | 2025-10-05 05:36:00 | NOAA-20 | ACRELÂNDIA | ACRE | Brasil | 1200013 | 12 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4b07b87a-0751-3301-8eec-899c0f36938f | -10.67339 | -65.21283 | 2025-10-05 05:36:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fa21c130-eaed-3ef0-ae39-7b74d4418e1f | -9.14663 | -62.36962 | 2025-10-05 05:36:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b3094f57-75aa-3b91-a137-3b41c2cbbbe2 | -9.16059 | -67.85139 | 2025-10-05 05:36:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9842599e-b49b-3759-a10c-93739ce761f8 | -9.21059 | -60.42714 | 2025-10-05 05:36:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 69fad3b2-d6d6-3e24-ae88-53d328dba4c5 | -10.99587 | -57.04633 | 2025-10-05 05:36:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 109c9117-86d2-3dbb-85d6-eed52b875058 | -9.04187 | -61.64402 | 2025-10-05 05:36:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ff6c88a7-28cd-388f-a00c-21e8de285750 | -11.76433 | -64.93242 | 2025-10-05 05:36:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f0d13327-89e4-3641-bd77-b498d9b23b00 | -9.10175 | -68.17522 | 2025-10-05 05:36:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.4 |
| b826ef9e-2328-3130-9998-708801138eae | -14.74925 | -54.65784 | 2025-10-05 05:36:00 | NOAA-20 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 4e1bd458-130a-35ba-9223-81950885565b | -11.40451 | -55.17628 | 2025-10-05 05:36:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 760937c6-a7be-3d7e-a85c-8cc626ac8dcc | -14.58682 | -52.46241 | 2025-10-05 05:36:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 695f3660-3c6c-36cb-8253-4c4f04fa58bd | -11.867 | -56.87411 | 2025-10-05 05:36:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d252e67b-f6ed-3233-82da-67e3454dcdf1 | -12.22505 | -56.63694 | 2025-10-05 05:36:00 | NOAA-20 | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| b6634f66-5a7b-3371-8542-bcccd4169990 | -12.32265 | -55.1426 | 2025-10-05 05:36:00 | NOAA-20 | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0022f55d-2963-3471-92bc-ba1cae69fc64 | -10.80129 | -69.043 | 2025-10-05 05:36:00 | NOAA-20 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 5fbddc47-f618-337c-9e55-d778c63f2a05 | -9.19251 | -59.55162 | 2025-10-05 05:36:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |


[Clique aqui para ver as próximas entradas](README143.md)
