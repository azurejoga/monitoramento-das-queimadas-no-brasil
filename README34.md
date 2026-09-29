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

## Dados Diários - Página 34

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2ed66a17-7218-30d0-9262-2e7e9d26314c | -19.46733 | -40.89067 | 2026-09-29 04:19:00 | NOAA-21 | BAIXO GUANDU | ESPÍRITO SANTO | Brasil | 3200805 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 35beddab-7ccb-35a5-82fb-470f077e65b3 | -18.68393 | -48.62938 | 2026-09-29 04:19:00 | NOAA-21 | TUPACIGUARA | MINAS GERAIS | Brasil | 3169604 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e6432998-4ec3-3d60-a5b6-821d50ced46a | -18.13023 | -44.35747 | 2026-09-29 04:19:00 | NOAA-21 | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 98cb3fd0-a236-3909-b041-3e40a4cba86a | -17.10499 | -46.47161 | 2026-09-29 04:19:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9fc62f02-c91f-3bb2-bc29-abb12e503231 | -18.40563 | -42.31424 | 2026-09-29 04:19:00 | NOAA-21 | VIRGOLÂNDIA | MINAS GERAIS | Brasil | 3171907 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 0d8f8503-e209-3b0a-a5fc-2579de4e987d | -18.08572 | -44.40136 | 2026-09-29 04:19:00 | NOAA-21 | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f80de43b-cf2e-39b9-a429-66e76c0a2519 | -18.9093 | -46.85406 | 2026-09-29 04:19:00 | NOAA-21 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 74c448ad-3a1d-3f51-9adf-e699349bfd96 | -18.09411 | -44.36772 | 2026-09-29 04:19:00 | NOAA-21 | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3ed70519-0730-38f2-a74c-defc06df1207 | -17.51155 | -44.42634 | 2026-09-29 04:19:00 | NOAA-21 | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8ea90ba6-3b62-3e03-bf94-a4c4091e0f51 | -17.90888 | -45.04267 | 2026-09-29 04:19:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 82616dea-6c62-39e7-99bf-26883619c1bc | -18.81967 | -47.34546 | 2026-09-29 04:19:00 | NOAA-21 | MONTE CARMELO | MINAS GERAIS | Brasil | 3143104 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9c4b2018-7e48-3a47-9f3b-9092196fb107 | -17.60195 | -43.70984 | 2026-09-29 04:19:00 | NOAA-21 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c74a269c-e242-337c-b82b-8b3bae63cb20 | -17.79071 | -47.16137 | 2026-09-29 04:19:00 | NOAA-21 | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 345e8929-3dbc-31e1-8577-f57f1fe2ca41 | -16.82145 | -48.99717 | 2026-09-29 04:19:00 | NOAA-21 | BELA VISTA DE GOIÁS | GOIÁS | Brasil | 5203302 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ac88b339-a2c4-31bb-8a8c-f40c376d08a2 | -17.97758 | -44.49225 | 2026-09-29 04:19:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 59f11e4e-6cf5-308c-a67a-d6a7642b2917 | -9.9595 | -50.1431 | 2026-09-29 04:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 41.6 |
| f52d82a1-225f-35a8-841a-2c3d667d7092 | -9.177 | -61.4073 | 2026-09-29 04:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 64.4 |
| c6af7e3a-d27d-31b3-8bff-389aadc7ae87 | -10.3894 | -61.2502 | 2026-09-29 04:20:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 92.1 |
| a685397d-467d-35df-bf52-e6a6e80b3c07 | -10.4081 | -61.2492 | 2026-09-29 04:30:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 56.8 |
| bc5951b7-98e2-328d-999e-96e254a7c17f | -10.3894 | -61.2502 | 2026-09-29 04:30:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 210.3 |
| b291a532-936b-3865-a3f4-a637e92db46e | -9.177 | -61.4073 | 2026-09-29 04:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 61.9 |
| b0955d12-29bf-35b1-9b5e-5358662d17cc | -10.3892 | -61.2695 | 2026-09-29 04:30:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 82.1 |
| d30eb47c-e255-3f0d-9072-e5abf110675e | -10.3895 | -61.231 | 2026-09-29 04:30:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 55.5 |
| 3aec0e1f-bfb3-358c-858f-5a1a202f8a37 | -9.1584 | -61.4082 | 2026-09-29 04:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 66.4 |
| c471d634-3147-3dff-9494-32acc490f9dc | 2.70353 | -50.88628 | 2026-09-29 04:46:00 | NPP-375D | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 59d5191a-e1db-3a39-aeea-9dcc6cec2c82 | 3.38112 | -51.29369 | 2026-09-29 04:46:00 | NPP-375D | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bc812413-12f4-3060-a0ef-1ccd2a57a5f3 | 2.56552 | -50.83911 | 2026-09-29 04:46:00 | NPP-375D | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d6ce89e4-c7fd-3957-9d99-c6d8ce33a404 | 3.38495 | -51.2931 | 2026-09-29 04:46:00 | NPP-375D | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 47257624-19e2-3806-b241-a0da2b83df2c | 4.00006 | -51.67318 | 2026-09-29 04:46:00 | NPP-375D | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ac02266b-35c7-3903-9277-00c946eb5358 | 2.56183 | -50.83968 | 2026-09-29 04:46:00 | NPP-375D | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d7973943-171e-3b4f-909d-c22ff8345ea9 | 2.0854 | -50.74994 | 2026-09-29 04:46:00 | NPP-375D | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f5dc630c-8546-3bed-a522-af39fc6f3533 | 2.08109 | -50.74631 | 2026-09-29 04:46:00 | NPP-375D | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fe342413-7e16-3221-96da-610da4ca912c | 3.83037 | -51.77324 | 2026-09-29 04:46:00 | NPP-375D | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d8028fc5-c530-3ad8-a56d-54010d4df7c5 | -5.57868 | -42.73498 | 2026-09-29 04:49:00 | NPP-375D | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 1e41337a-fd07-3c0c-a2ea-5f09c11c9104 | -7.06133 | -42.0697 | 2026-09-29 04:49:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 6.7 |
| 41380fdf-0da4-37e9-8efb-d82bf69274ba | 0.9075 | -50.02125 | 2026-09-29 04:49:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9bd6c99c-823d-3e65-bf58-c82a250bb08a | -3.70605 | -54.22008 | 2026-09-29 04:49:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 70de50ee-ca68-38a0-b458-95ef9f6ed15b | -3.7102 | -54.22081 | 2026-09-29 04:49:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9ad997e1-998a-3627-9336-80ca5f5bed28 | -3.01982 | -53.87453 | 2026-09-29 04:49:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9900c345-1630-3738-af1d-8df241a0682a | -6.13543 | -44.13842 | 2026-09-29 04:49:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 92131b69-e875-3eb6-bbd7-576fc9480c14 | -5.73638 | -45.05977 | 2026-09-29 04:49:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 55671bdc-3ed3-3a8c-88be-d9b78e23fe52 | -4.7169 | -50.63793 | 2026-09-29 04:49:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2a3443df-a12c-35ec-8aef-591bbfe0f763 | -6.32221 | -46.34431 | 2026-09-29 04:49:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 49d54f19-8729-30a2-8f90-3c119af67a1c | -5.43255 | -43.44404 | 2026-09-29 04:49:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| dd6e562e-b4e7-3436-905e-71651c5d566c | -2.86931 | -49.63419 | 2026-09-29 04:49:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d02ebe79-ed40-3420-abbf-2ef1aa4a686f | -5.73495 | -43.27962 | 2026-09-29 04:49:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| be158649-1293-3927-af56-ba91a2fe7514 | 1.86965 | -55.57322 | 2026-09-29 04:49:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b1d66091-66fb-3aa3-8579-eecfdd87c62f | -6.14044 | -44.13982 | 2026-09-29 04:49:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 25272a2f-0ca0-326a-93bd-daabe410cfdd | -3.14712 | -54.09625 | 2026-09-29 04:49:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 13e30dcc-e613-3402-ad1a-97620347f816 | 1.67018 | -55.90538 | 2026-09-29 04:49:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 083db257-d8c6-3da7-b038-c295109a35f7 | -6.37424 | -45.80843 | 2026-09-29 04:49:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 99c38542-5fb8-3ccc-8c0f-4441ec75731f | -5.02602 | -43.57169 | 2026-09-29 04:49:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a14eefe3-3a90-3d36-8e05-2e5053ab0705 | -6.14004 | -44.13549 | 2026-09-29 04:49:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e6a6281d-35a0-310f-a7b6-0fbd294329bb | -5.32861 | -46.19565 | 2026-09-29 04:49:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 10051304-123c-305d-9f1a-26f46f90b043 | -3.50637 | -50.47867 | 2026-09-29 04:49:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 425e3ae1-50e6-3cf1-b5b1-a43668cd5672 | -5.73529 | -45.1701 | 2026-09-29 04:49:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 632bb358-027f-3442-b1fe-11cd58568b2b | -4.31758 | -48.63022 | 2026-09-29 04:49:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d28a5a69-c4fd-37c5-81cc-70e5b95151d7 | -3.71082 | -54.21705 | 2026-09-29 04:49:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7df0d880-640d-37de-b77f-4441ef837d6b | 1.67437 | -55.89873 | 2026-09-29 04:49:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ed462621-2c27-32e2-90e8-e50543546a44 | -1.79972 | -47.95097 | 2026-09-29 04:49:00 | NPP-375D | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| ba15a2d6-f478-3864-b65c-e2fc369bd7e0 | 1.68171 | -55.91269 | 2026-09-29 04:49:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f0075774-e204-33e7-a18e-e136d7fadfc3 | -3.79484 | -50.04903 | 2026-09-29 04:49:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 90f7fe78-3ef9-3d7a-9829-177591323e55 | -5.36433 | -46.22636 | 2026-09-29 04:49:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6e5fb102-7953-3ce0-bf68-2d935e821887 | -3.15544 | -54.09766 | 2026-09-29 04:49:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8bc2f73e-de28-3d54-9aa5-e17081553894 | -4.26856 | -48.55865 | 2026-09-29 04:49:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d6c9d8e8-b9bf-369b-b700-ee465af52629 | -4.06759 | -50.76638 | 2026-09-29 04:49:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 56445594-9e95-3d44-a023-1e2ac8d10721 | -3.99633 | -38.98374 | 2026-09-29 04:49:00 | NPP-375D | MARANGUAPE | CEARÁ | Brasil | 2307700 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| f249ac08-3e87-3002-b22a-f2eff78e7519 | -7.06264 | -42.30379 | 2026-09-29 04:49:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| ecb7a8fe-e1ca-36e5-969f-49c7ac90e08b | -5.87566 | -43.58973 | 2026-09-29 04:49:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 44170064-cc4e-346e-8c08-4905ca370c66 | -4.05029 | -54.92894 | 2026-09-29 04:49:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 13.3 |
| 3bbc0cbe-5496-373b-8988-2335c7442d4c | -0.48763 | -49.12744 | 2026-09-29 04:49:00 | NPP-375D | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0ed3cfe3-a6ef-30fe-a88a-d3408f8a4d65 | -4.04598 | -54.92807 | 2026-09-29 04:49:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| f152ffe2-58e8-383d-b495-a17cd5ca6dda | -2.38843 | -45.17107 | 2026-09-29 04:49:00 | NPP-375D | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 1c91d15a-bd58-3efe-b766-a1fab81e2545 | -5.01411 | -48.04775 | 2026-09-29 04:49:00 | NPP-375D | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a771a9b2-b11d-3107-b854-6bb42812d7f0 | -4.42229 | -46.28082 | 2026-09-29 04:49:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 569db7b1-cc99-3f72-9834-761bf0e79906 | -3.70728 | -54.21267 | 2026-09-29 04:49:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7b8f216a-6ab6-37ff-88ab-9462728551fb | -2.57121 | -54.74498 | 2026-09-29 04:49:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 45545bd0-9115-388c-aa7a-9246c4f24836 | -5.60645 | -44.99915 | 2026-09-29 04:49:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| eb45a6c3-4e27-3d96-8873-8dcbda2653a1 | -4.89709 | -45.99981 | 2026-09-29 04:49:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f4fb5264-bd12-301a-96a3-d09b29c9f5be | 0.53379 | -50.81146 | 2026-09-29 04:49:00 | NPP-375D | ITAUBAL | AMAPÁ | Brasil | 1600253 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 39d00ec0-7eef-3b6e-8f3e-3c47312d2634 | 0.07441 | -51.14051 | 2026-09-29 04:49:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f231f172-9e69-33f7-b144-762bee5e4cc0 | -3.70893 | -54.22843 | 2026-09-29 04:49:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 764aa6d7-18ae-3c68-b50b-88d7a571d5d4 | -5.08714 | -44.84052 | 2026-09-29 04:49:00 | NPP-375D | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 46725de3-7079-3c04-8648-e288f02dd69c | -1.32871 | -47.78802 | 2026-09-29 04:49:00 | NPP-375D | CASTANHAL | PARÁ | Brasil | 1502400 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c020ea82-ea6e-3a20-8d3d-2abd1d2f1565 | 1.69182 | -55.94461 | 2026-09-29 04:49:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 47b30ab1-41f8-3af2-a3c3-b7df4f7c2f8d | -4.05097 | -54.92485 | 2026-09-29 04:49:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 940b6b97-d664-3839-804f-50839778b3f3 | -5.42829 | -43.44344 | 2026-09-29 04:49:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 6265bd31-3ba6-305d-97d2-a7b8fe84393e | -6.37795 | -45.80898 | 2026-09-29 04:49:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 43ac2965-01bf-3ef9-bd25-8e0d08b053fb | -3.14951 | -54.08138 | 2026-09-29 04:49:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d1a0c7e0-718d-318e-9ec4-8dc0e4ba43de | -3.15366 | -54.08213 | 2026-09-29 04:49:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d756c7e9-bd36-3096-8830-971abdf5d8a4 | -3.51159 | -50.31464 | 2026-09-29 04:49:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| bf94329e-0f6d-3ac0-9feb-03ce52a3f7e6 | -3.15689 | -54.09392 | 2026-09-29 04:49:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| d712af1b-24e6-30d8-b9e9-c23972c07235 | -3.14891 | -54.0851 | 2026-09-29 04:49:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 58231dad-ca88-3564-9a7c-9ed8e6f64ffa | -3.60426 | -49.45554 | 2026-09-29 04:49:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 55ed10c7-2909-3c3d-ade7-9d3bbd4a6e1d | -3.49494 | -48.57147 | 2026-09-29 04:49:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b5d4e7d3-e4eb-36e4-9d5a-510e8cd7c1de | -5.42713 | -43.45124 | 2026-09-29 04:49:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 177b8cb9-3b70-3af8-8a8d-acfa27d017c8 | -5.48707 | -45.30629 | 2026-09-29 04:49:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 6b939734-43a0-390d-bbec-d86791873c77 | -5.73064 | -43.27895 | 2026-09-29 04:49:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 28b63a45-dc9b-34b6-8de5-410c0a764455 | -4.49586 | -49.63991 | 2026-09-29 04:49:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c74ae2d0-a0ac-381c-b1e8-4ee2e7effe6a | -4.50198 | -49.64446 | 2026-09-29 04:49:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |


[Clique aqui para ver as próximas entradas](README35.md)
