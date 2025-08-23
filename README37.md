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

## Dados Diários - Página 37

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e838e4cd-af75-31ea-a4c3-ac924b871c54 | -7.07083 | -44.61696 | 2025-08-23 04:51:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ba884b88-d739-30c6-84f1-02b7c16ea2c4 | -9.19098 | -59.64507 | 2025-08-23 04:51:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 609c4d5b-cb99-3e20-a590-7cf31e8640d4 | -6.70945 | -43.1979 | 2025-08-23 04:51:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 4.2 |
| e23fe880-0699-3a84-9e53-49d6659448bd | -10.63632 | -50.13752 | 2025-08-23 04:51:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 307a2ac1-2ad4-3cda-8125-19a05bf9b65a | -5.75133 | -57.59314 | 2025-08-23 04:51:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| ca558b91-b13c-3ca8-a14e-34db2534473e | -7.05562 | -59.83071 | 2025-08-23 04:51:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b80a895c-847a-3739-b0f4-b77661cec630 | -6.55054 | -45.45274 | 2025-08-23 04:51:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 044d17dd-453f-3d72-8706-46df39ee0295 | -9.19369 | -59.59447 | 2025-08-23 04:51:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 0dd91721-f974-345b-a88e-429734bc4226 | -6.59719 | -44.56768 | 2025-08-23 04:51:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 2959635e-6c4f-3fbc-beb3-f6a3d550208e | -6.31078 | -59.883 | 2025-08-23 04:51:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 7c749bdd-3314-31e2-a5bb-0ce3a657c5ad | -9.17929 | -59.66054 | 2025-08-23 04:51:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| a8caf686-d016-3b35-b6e6-0addfcf153db | -4.31272 | -48.0983 | 2025-08-23 04:51:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 361cab12-8793-3f35-a877-02ce8dc6dcc4 | -5.11297 | -43.21946 | 2025-08-23 04:51:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 38b01e59-1d5b-3d04-8aef-f4789c918521 | -7.63098 | -45.23745 | 2025-08-23 04:51:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 7.2 |
| af68e3c7-0fea-3d42-bfcd-b31bc4d1e39e | -7.1813 | -48.42755 | 2025-08-23 04:51:00 | NOAA-21 | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| dd7a9169-67e8-3a92-bc1e-86234abeef34 | -5.88382 | -53.62719 | 2025-08-23 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 24f41deb-2159-3758-a199-4efd9fa61564 | -6.59677 | -44.57066 | 2025-08-23 04:51:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 3cdbb395-60c9-3ced-8d4c-ad8f61e6493f | -6.60221 | -44.56842 | 2025-08-23 04:51:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 10.3 |
| d0528a84-e565-349d-a519-d987b2c9fad9 | -9.18324 | -59.58828 | 2025-08-23 04:51:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 08d18f39-cad1-3444-8589-cc01c938cd3a | -6.93399 | -62.8935 | 2025-08-23 04:51:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fe96b9c9-6162-3133-b023-913744fbd9dc | -6.60765 | -44.56619 | 2025-08-23 04:51:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 13.8 |
| 266d689a-5e5e-3308-b3b5-44f46518170e | -7.43633 | -60.62937 | 2025-08-23 04:51:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 55a1b1b3-b9a7-393e-adb4-5aa3122f9d09 | -9.59641 | -55.34425 | 2025-08-23 04:51:00 | NOAA-21 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 88d1c373-6f2b-373a-aa48-22d68b7c076c | -3.70319 | -49.54886 | 2025-08-23 04:51:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 24b6e323-f3a6-338f-9e5a-a6a332c5e036 | -9.24941 | -59.61705 | 2025-08-23 04:51:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| dd4be6c0-4975-3bdb-9b9b-91af99296841 | -7.08377 | -44.59743 | 2025-08-23 04:51:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7c5f9c04-4470-3796-a81c-89fafa65797d | -9.18182 | -43.04672 | 2025-08-23 04:51:00 | NOAA-21 | ANÍSIO DE ABREU | PIAUÍ | Brasil | 2200707 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 5b1e159c-81a5-3743-aa7b-0984f24fcbb0 | -8.61108 | -62.60551 | 2025-08-23 04:51:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b38eb3bb-05fa-32ff-8c11-33c36b5749b4 | -5.7404 | -57.60931 | 2025-08-23 04:51:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 28729728-6ebe-3a94-91fc-fb7defda4f0c | -9.2017 | -59.44331 | 2025-08-23 04:51:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 100bbe70-52dc-300d-b30c-6debabb53491 | -9.1867 | -59.61886 | 2025-08-23 04:51:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 12.2 |
| 6287ece1-1e79-3e1b-92a3-5559a7ad2c42 | -9.20474 | -59.61772 | 2025-08-23 04:51:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 52ec7c0d-e0ce-38a4-88f6-4aea781c1bf8 | -8.59855 | -62.61377 | 2025-08-23 04:51:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| bd791bb9-7095-3bc0-b534-fa7b0214fb6b | -9.20809 | -59.44871 | 2025-08-23 04:51:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f927cb7a-5698-3f43-b314-e95a5af3ed37 | -9.18446 | -59.63147 | 2025-08-23 04:51:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 03fefaa6-1056-38c7-8e8c-049934f39e05 | -8.65897 | -51.27815 | 2025-08-23 04:51:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 43c6055d-0f62-30cf-af74-b5bb0342d0fa | -8.66583 | -51.2792 | 2025-08-23 04:51:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b09e4eb5-a58f-3433-bab6-f267ccfa908c | -8.66011 | -51.27062 | 2025-08-23 04:51:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 84641c1e-2672-38d1-ad98-bc1dd575e561 | -6.57679 | -59.87402 | 2025-08-23 04:51:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 7.9 |
| be732efb-60ff-3183-908f-f9e70db8417f | -2.93001 | -53.69674 | 2025-08-23 04:51:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 37f15dc8-1ee9-3011-be75-3d8120b017c4 | -7.8099 | -51.0059 | 2025-08-23 04:51:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4aed7d9a-d1bf-3b70-a9c4-19e4473dc85b | -6.37692 | -45.54696 | 2025-08-23 04:51:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 31.0 |
| e253fbe2-aa2b-3fd2-8ebf-213e8a1ddcf0 | -7.54731 | -48.86523 | 2025-08-23 04:51:00 | NOAA-21 | PAU D'ARCO | TOCANTINS | Brasil | 1716307 | 17 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 50de04a6-0df9-306b-a845-305e6feef2b5 | -6.68587 | -58.85875 | 2025-08-23 04:51:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 8024294b-3098-3fcd-af02-b97bbf4922c4 | -5.79876 | -59.21458 | 2025-08-23 04:51:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a1201e73-7382-3e97-a6a2-294c89b56c0e | -7.67598 | -45.41246 | 2025-08-23 04:51:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| f89359e6-d9b8-3e64-acba-91af5e819aaa | -5.23071 | -56.0212 | 2025-08-23 04:51:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 617e2104-ce6b-34e4-aaf7-4c6684f45579 | -9.18801 | -59.62792 | 2025-08-23 04:51:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 1fadd4db-bbb0-3eb5-a017-1a7c9023d17d | -9.20829 | -59.48233 | 2025-08-23 04:51:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3d3f07e4-18cb-3c16-99f4-ed9fa29d1adf | -7.44758 | -46.13246 | 2025-08-23 04:51:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e44a83a4-a74d-3ea2-8ac4-22b928a5f516 | -4.54627 | -46.69074 | 2025-08-23 04:51:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 29277388-d76b-3d50-a61a-fc92c268867f | -4.12406 | -48.11826 | 2025-08-23 04:51:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 8a59b3c1-84da-3409-8d5b-e1d15d5abd92 | -4.31655 | -48.09888 | 2025-08-23 04:51:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| acbc6c36-6707-3fd3-8724-78b40f542382 | -7.61683 | -44.37253 | 2025-08-23 04:51:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 474d91f9-fd83-30dd-af72-0f2196e259b4 | -6.06445 | -53.88351 | 2025-08-23 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 250d316c-978a-33ce-94c8-4e4f5c16a309 | -11.13873 | -44.74313 | 2025-08-23 04:51:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b1c42c12-603c-3cfb-921a-dd11c2267d3e | -2.96694 | -54.65685 | 2025-08-23 04:51:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 9870683d-3c1a-39cb-baa5-47a9c9947a6a | -5.79353 | -59.21838 | 2025-08-23 04:51:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5dda8e46-3497-34b3-9386-502cad6a7e32 | -6.16355 | -53.77271 | 2025-08-23 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 618c545b-95be-35c3-9974-b869fbe69b0c | -7.78543 | -61.57562 | 2025-08-23 04:51:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1c9992ed-7cfb-3f58-95e6-b8427267d7d6 | -9.2024 | -59.43925 | 2025-08-23 04:51:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 39d28e38-78b7-3819-9f03-5e6605738c53 | -6.44522 | -53.39034 | 2025-08-23 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1d58c1b7-f105-3fa1-9112-56610fc4ecf6 | -7.54897 | -63.85693 | 2025-08-23 04:51:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| fcf0eb3b-f544-3df9-be00-c23008e4cdb3 | -9.17104 | -59.70691 | 2025-08-23 04:51:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| dc09aa60-3717-39ae-9c93-78c207ed8a5f | -8.30412 | -47.26971 | 2025-08-23 04:51:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4b94df2e-fbdf-3ffb-a94d-72d0ee939003 | -6.60179 | -44.57138 | 2025-08-23 04:51:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 10.3 |
| d77c449e-4869-34b2-a51d-e53e0c689f3f | -5.11344 | -43.21605 | 2025-08-23 04:51:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 61f85976-6da7-3c83-9c56-faad0ec469b9 | -8.04395 | -47.31303 | 2025-08-23 04:51:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ac326d3a-90b1-3783-90bc-e6c7d06cc4ad | -6.27535 | -53.71096 | 2025-08-23 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e65c0b17-7bd2-3565-bf5d-1bae941184e5 | -4.22773 | -47.21015 | 2025-08-23 04:51:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| f86e64f9-e07f-3297-87cf-78dee96d3d44 | -4.14379 | -46.45812 | 2025-08-23 04:51:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bdf451ff-fd56-397c-8f00-77d541603392 | -7.73206 | -67.06719 | 2025-08-23 04:51:00 | NOAA-21 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 4.3 |
| aca7037c-0ada-3aff-9076-644abda89992 | -5.79325 | -50.18722 | 2025-08-23 04:51:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 832019c3-31ec-3bb9-bb6a-df858b4a8318 | -7.04699 | -51.41598 | 2025-08-23 04:51:00 | NOAA-21 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| a0fc55f2-6e25-3ce8-adce-d7a92ae8ddfc | -7.81963 | -63.56104 | 2025-08-23 04:51:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| a9415562-b68e-3ef5-bc42-98c59a743e3d | -6.06389 | -53.88705 | 2025-08-23 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 43f1ce89-4e5a-381a-a90f-4a665abc8502 | -9.20898 | -59.47824 | 2025-08-23 04:51:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8bea3b65-5a1e-3446-a603-6d858b22bed0 | -9.05897 | -49.53379 | 2025-08-23 04:51:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 7c114f17-0d21-389c-a14b-a94f0fc60a3b | -8.59133 | -62.62303 | 2025-08-23 04:51:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 5.3 |
| f3642cc3-bf09-3be3-99cb-4e1fa034295e | -5.8766 | -53.62967 | 2025-08-23 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 15a08ed6-3d07-3bf1-b4ab-ac3943cb014a | -3.36933 | -50.82497 | 2025-08-23 04:51:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 62fc88be-9a2e-30a5-92c5-f23ec384f470 | -9.81251 | -46.39815 | 2025-08-23 04:51:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 1e7a5dc1-7ea6-3463-9888-cd6769d163c8 | -6.37624 | -45.5519 | 2025-08-23 04:51:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 15.5 |
| aa375923-8757-3238-9977-984872c8fddf | -9.20731 | -59.47792 | 2025-08-23 04:51:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 935bd374-f20c-3363-bdc8-ae5dc611057b | -5.74098 | -57.60582 | 2025-08-23 04:51:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3473350c-c1ed-36d4-80f5-1677458280e9 | -6.05888 | -53.87536 | 2025-08-23 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5f334163-9820-3e74-98a2-fdb80888490a | -7.17812 | -48.42191 | 2025-08-23 04:51:00 | NOAA-21 | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 1a0c1707-d533-32f6-a5ac-fb6b27ca464d | -7.77982 | -61.57777 | 2025-08-23 04:51:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9cf9c9d3-fc52-32c0-ae72-d34a386a2f53 | -4.38106 | -55.75576 | 2025-08-23 04:51:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9c1f95ec-2d7f-3db3-b433-2fc3807b8460 | -8.85321 | -49.8585 | 2025-08-23 04:51:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5b1160d7-51af-31d4-8a9c-20170e7f9452 | -8.66926 | -51.27973 | 2025-08-23 04:51:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3b6e21f3-de4d-3046-b43a-d1b05ae53391 | -9.47775 | -57.82959 | 2025-08-23 04:51:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| eb7cf2be-0057-3a6e-b6f5-7276273f4a82 | -10.64867 | -50.13033 | 2025-08-23 04:51:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| b6ec9b6a-093e-315a-8bff-f60203ee961e | -7.29511 | -59.64336 | 2025-08-23 04:51:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 20737af3-8e1b-3a2f-9b62-1d966ea74ab2 | -9.1851 | -59.61877 | 2025-08-23 04:51:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 77f1d407-aaa1-307f-900e-ebaff86f53d1 | -9.20043 | -59.61692 | 2025-08-23 04:51:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 1f33eeff-7c60-3ca7-b062-69583d492811 | -9.44235 | -47.65371 | 2025-08-23 04:51:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| e5323b57-c232-3e97-a9b5-551ffc1562af | -5.81061 | -59.22575 | 2025-08-23 04:51:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2b13a307-1e38-33cc-9abd-a5065cdb72d0 | -5.61504 | -60.22699 | 2025-08-23 04:51:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9013ae24-1be4-3098-baf3-34fe943bd296 | -6.43637 | -53.38184 | 2025-08-23 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |


[Clique aqui para ver as próximas entradas](README38.md)
