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

## Dados Diários - Página 57

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1a4e5929-213d-3224-a9ac-47997ff58cdc | -9.66047 | -54.33554 | 2026-09-22 04:46:00 | NOAA-21 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 004faaa3-edd0-36e8-9f06-6b62357e2bc7 | -3.05894 | -54.39679 | 2026-09-22 04:46:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 3d3080bf-fc9d-3582-bc95-ee3e02f4824a | -7.2377 | -55.59159 | 2026-09-22 04:46:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3d7b1af9-afba-3424-85a1-d892dff381d8 | -7.42155 | -49.83944 | 2026-09-22 04:46:00 | NOAA-21 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 7130e3b9-6f0d-3016-9cb0-58fae58dada0 | -5.13592 | -49.93881 | 2026-09-22 04:46:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 1689a1c5-61e3-3d67-8104-3d935ecc2d9f | -6.58768 | -44.14912 | 2026-09-22 04:46:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 83eb4cd8-804f-305c-84a2-376e71671f95 | -8.82705 | -50.49256 | 2026-09-22 04:46:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 56cc5fec-5dfd-3934-9728-240869a0fb1a | -8.44769 | -45.82084 | 2026-09-22 04:46:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 15395177-aa72-3d85-9d1c-5442f368aa02 | -9.66804 | -54.33281 | 2026-09-22 04:46:00 | NOAA-21 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| bb45c7e0-7a9f-38bb-9e81-74bc81196949 | -7.5741 | -57.68217 | 2026-09-22 04:46:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| e0c39f27-4322-3f67-9e32-596333c9e7d6 | -4.55849 | -54.92164 | 2026-09-22 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 8383acf6-4028-393c-85eb-5e66b6fefa01 | -6.80604 | -55.83179 | 2026-09-22 04:46:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| da40a8c1-33bf-372d-acce-4e3407440402 | -6.16135 | -59.94353 | 2026-09-22 04:46:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fa6ae618-e128-38c5-82d5-6af17f13bffb | -9.38471 | -47.76152 | 2026-09-22 04:46:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| df51a459-b2ca-3b74-b6ce-c882f50a1f5d | -5.87297 | -52.03801 | 2026-09-22 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3074f14f-d7cb-3083-8f77-095978cbf95e | -5.75889 | -45.07765 | 2026-09-22 04:46:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 696c9c2c-a831-38a1-8272-89707187c222 | -8.6031 | -54.62856 | 2026-09-22 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a0dc026d-2b6d-3ea9-9419-984da2cf80ee | -7.8299 | -45.25515 | 2026-09-22 04:46:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| afe5e673-7ac4-3992-88e8-ed170a7271cc | -4.10157 | -56.34557 | 2026-09-22 04:46:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 88b94bb9-fcc5-3208-8331-a72cdd725fa0 | -2.93428 | -57.79607 | 2026-09-22 04:46:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 195162eb-1851-3a5e-929e-83051b48c2bb | -10.49011 | -51.26445 | 2026-09-22 04:46:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c01665f5-6a32-35cb-a102-2bd875cb3443 | -5.65651 | -43.41413 | 2026-09-22 04:46:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d8b932c8-0692-3a64-8c73-082ba0a00114 | -10.45823 | -51.33908 | 2026-09-22 04:46:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ac292001-f4cd-33ec-bc54-743a1d4eca26 | -6.12183 | -59.94814 | 2026-09-22 04:46:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 4afe6a00-0205-3049-87aa-4fd3b50f2827 | -8.08707 | -44.36853 | 2026-09-22 04:46:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| d115f2fe-4197-3afa-a4bd-a6e68c4a482f | -3.58557 | -59.07012 | 2026-09-22 04:46:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| fa97ea03-1a5c-3df2-afcf-f560bdcc0431 | -9.60784 | -43.92653 | 2026-09-22 04:46:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 3618931b-346b-3d87-8413-e233a143111d | -3.03689 | -54.40918 | 2026-09-22 04:46:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ea5997ce-92d2-36a0-a41f-0b160a8d3d76 | -5.8066 | -52.09258 | 2026-09-22 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f888a0fb-d8fe-34d3-9928-ed63e45e0c8d | -6.45484 | -54.99405 | 2026-09-22 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 62193505-047e-3ff2-9a1c-b1fc0268dd25 | -6.83076 | -55.53874 | 2026-09-22 04:46:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 212c1cef-5938-3ba2-9ea2-eaea0be264c1 | -9.49983 | -48.50746 | 2026-09-22 04:46:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 4bc070cc-521f-3a06-8340-7b49be450e45 | -3.17003 | -58.59425 | 2026-09-22 04:46:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| f80fb84d-e1a9-3e12-b86a-f25d5d34a82d | -9.24393 | -57.15745 | 2026-09-22 04:46:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1cafcc94-2e0b-3999-90d9-5712f1e86510 | -9.68067 | -54.34283 | 2026-09-22 04:46:00 | NOAA-21 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7c91cdec-64dd-3f7d-b6bd-1d6cb93291fc | -6.16187 | -57.79758 | 2026-09-22 04:46:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ec3711ef-7fca-354c-8840-366c990cd8f7 | -3.11168 | -60.71928 | 2026-09-22 04:46:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6921b572-3c12-36e0-a5e8-3c4501643c59 | -7.45405 | -44.74188 | 2026-09-22 04:46:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 86b155d5-8e2f-3fde-86bd-8d6fb109c564 | -6.78363 | -58.61005 | 2026-09-22 04:46:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ee893087-a6c8-320c-8103-face6e3b26b2 | -6.4439 | -55.63974 | 2026-09-22 04:46:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9a2faff2-e06c-3dd9-ad51-c4cfaba1290b | -5.99464 | -49.94797 | 2026-09-22 04:46:00 | NOAA-21 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ec785bca-0ca9-33eb-a7c4-61ab34583af9 | -5.21569 | -56.07265 | 2026-09-22 04:46:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 2fd1276f-e131-3406-b925-18bd4baba1fd | -6.46255 | -59.97543 | 2026-09-22 04:46:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 21e28c03-1797-32ac-ac34-ffbcd3a4a181 | -9.66394 | -54.33613 | 2026-09-22 04:46:00 | NOAA-21 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| a77dcbd9-0bf1-3926-9579-9bd23bb40984 | -6.30314 | -57.73816 | 2026-09-22 04:46:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| f08a1ff5-8f20-37b8-be0b-cdc29113487a | -8.48927 | -57.61768 | 2026-09-22 04:46:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 43d4b746-2437-378a-81fd-3c598d8bc0e0 | -8.24851 | -55.25392 | 2026-09-22 04:46:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| e2e3445a-b8df-30ed-834f-b7a4f451bf31 | -7.41933 | -49.85398 | 2026-09-22 04:46:00 | NOAA-21 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| fb211aff-bca7-3d68-8d45-7a7ab7e3f362 | -9.24328 | -46.15447 | 2026-09-22 04:46:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 203ff922-d91c-3de7-94a3-477198594951 | -2.92815 | -57.79298 | 2026-09-22 04:46:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 4.6 |
| c9aa5c10-a173-33fb-ba66-ee207bfb26bc | -6.72756 | -48.12747 | 2026-09-22 04:46:00 | NOAA-21 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4a0b41ee-0923-3a0c-b977-b4073d97d2a3 | -6.0916 | -57.62384 | 2026-09-22 04:46:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 21dadcd0-2836-358a-b0ef-3dadc757e92d | -6.65938 | -50.90317 | 2026-09-22 04:46:00 | NOAA-21 | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 09ff14d7-2763-306d-b362-985f70ff7334 | -3.37779 | -50.44085 | 2026-09-22 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7596d759-ea06-3f0a-867d-41cf9c9112a2 | -3.78195 | -51.68308 | 2026-09-22 04:46:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5db66169-a6bd-395a-b35c-597dfbf6d724 | -4.52249 | -55.76288 | 2026-09-22 04:46:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ce0c6f37-21ff-3f26-89c5-5572c7300578 | -3.54925 | -51.53927 | 2026-09-22 04:46:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c6df4894-a55b-3877-81e5-bc5439ed1207 | -9.56358 | -46.54503 | 2026-09-22 04:46:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6afff37d-e98c-37ff-a00e-1a5fdf02f9bf | -5.93692 | -59.98534 | 2026-09-22 04:46:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 9868db80-68b7-3ccc-bafc-230c3f66eb55 | -2.78287 | -59.95957 | 2026-09-22 04:46:00 | NOAA-21 | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| be7aab16-50ee-390e-8b66-46c23d527269 | -6.47038 | -59.97137 | 2026-09-22 04:46:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9c9626ef-13c9-3489-a4f7-e6d6f7db8e07 | -6.13695 | -55.66631 | 2026-09-22 04:46:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a75d9707-5d77-307a-828c-cc7a17ef786c | -4.45995 | -47.91905 | 2026-09-22 04:46:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 48172e05-6535-3d4c-bff3-7d8efa4acda7 | -6.1471 | -43.85141 | 2026-09-22 04:46:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 5dece342-47ea-3128-acb8-c9adf746521b | -11.14473 | -42.84464 | 2026-09-22 04:46:00 | NOAA-21 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| c18bbdc4-3531-3d58-9f1a-49102286a6b2 | -7.61462 | -55.35905 | 2026-09-22 04:46:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c36c5326-eba0-393e-ad0d-81eb03d8755d | -7.58569 | -57.69271 | 2026-09-22 04:46:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| f4287b04-d95e-3ed4-8704-9902a16bb97d | -8.23417 | -54.6842 | 2026-09-22 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 89e130de-a452-3c92-93c4-df0f85c346a0 | -8.37817 | -47.28893 | 2026-09-22 04:46:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4c35c77d-1883-3059-ad6d-581ce02ba3ce | -7.56014 | -42.66145 | 2026-09-22 04:46:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 6ca15157-9c5d-3ce8-b816-c31ee97926dd | -4.50143 | -54.96027 | 2026-09-22 04:46:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 1bdc6891-70e7-328a-82d8-b3a3c449d432 | -4.50461 | -59.55579 | 2026-09-22 04:46:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3d13ed6d-646f-3679-b69d-8558bae216d3 | -6.55056 | -56.0373 | 2026-09-22 04:46:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 06a0b6b2-4c76-348e-86e2-776ea3495aae | -6.86482 | -59.90426 | 2026-09-22 04:46:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 21c3fe94-a295-3506-80d9-ffaf9f517dfc | -8.31503 | -44.75311 | 2026-09-22 04:46:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 0f5e6969-cd12-3b89-95e1-d1b644b2092f | -10.68362 | -50.75515 | 2026-09-22 04:46:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b075a567-09f9-3981-844c-850c665b08fb | -7.13787 | -48.43258 | 2026-09-22 04:46:00 | NOAA-21 | CARMOLÂNDIA | TOCANTINS | Brasil | 1703883 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b4497902-a1c3-33e8-b95e-2350bb6d74d6 | -6.79579 | -59.14251 | 2026-09-22 04:46:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| dfb0ff41-2c4a-35b3-b03a-938cb97e8abd | -5.81788 | -57.74454 | 2026-09-22 04:46:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 1975542e-285e-35d5-b514-ddd3437704a5 | -6.64846 | -50.92981 | 2026-09-22 04:46:00 | NOAA-21 | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ce98fa05-b870-32cf-830d-46a0bef35c93 | -3.12762 | -51.60286 | 2026-09-22 04:46:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4c60168a-3680-3c4c-81f6-a8cb5056d328 | -6.19312 | -57.7755 | 2026-09-22 04:46:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 0136a093-34d0-33cc-97cc-1df55b6910dc | -9.6548 | -54.32661 | 2026-09-22 04:46:00 | NOAA-21 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 73c06961-3bd0-3c1f-b895-a239bf689745 | -8.48501 | -57.61697 | 2026-09-22 04:46:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 54ddd0af-cc46-3811-99f5-06564b6b3309 | -3.4814 | -59.57415 | 2026-09-22 04:46:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f3309f28-e0fa-3e94-87b2-c065826a1f90 | -3.60915 | -60.57519 | 2026-09-22 04:46:00 | NOAA-21 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a7a69742-bdfa-3e12-8fd6-73c2bb4565cd | -6.47638 | -42.78558 | 2026-09-22 04:46:00 | NOAA-21 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 2d4cb964-52cc-359d-938f-57f3735a2293 | -5.87851 | -52.04612 | 2026-09-22 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 05fb2e3a-ac09-3345-b677-63c3d5b38c3b | -6.75457 | -59.06408 | 2026-09-22 04:46:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 25f3ae8a-3f1d-3b86-a454-15ed5098b100 | -7.58923 | -57.67184 | 2026-09-22 04:46:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| da646eb7-722b-3d1b-afbf-b1d5474a7d21 | -5.83301 | -52.05341 | 2026-09-22 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 245688af-7fbe-3edb-b85f-8c7e92b9cdd2 | -5.89167 | -53.64457 | 2026-09-22 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2b4826bf-33fc-3b13-be31-ca2cb4f3557a | -5.62803 | -43.37202 | 2026-09-22 04:46:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 085dbd18-d393-331b-a9d9-a55d90311b16 | -9.13116 | -58.88728 | 2026-09-22 04:46:00 | NOAA-21 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 08535a10-d8e3-3c6e-94c8-32469c93cb5c | -8.32651 | -46.00596 | 2026-09-22 04:46:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 21a0a2ad-1469-315c-b82a-37a7a676cd41 | -7.88291 | -54.73213 | 2026-09-22 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ce4d921b-a178-314a-9784-415e16b99350 | -3.12324 | -60.68448 | 2026-09-22 04:46:00 | NOAA-21 | IRANDUBA | AMAZONAS | Brasil | 1301852 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cc85987e-034b-32ce-b15d-1878fcc2a4a9 | -7.39066 | -44.80085 | 2026-09-22 04:46:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 5c9969d5-7ca2-342f-9644-b302e78e96ff | -10.42311 | -50.22965 | 2026-09-22 04:46:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0c294eed-8c8b-3af4-b679-d2da88bd2dfe | -6.46415 | -59.9661 | 2026-09-22 04:46:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |


[Clique aqui para ver as próximas entradas](README58.md)
