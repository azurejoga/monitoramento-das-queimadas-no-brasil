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
| 92f461cb-ce58-31ae-9ad4-d1d70d50c7ca | -22.99139 | -49.93487 | 2025-09-16 04:06:00 | NOAA-21 | JACAREZINHO | PARANÁ | Brasil | 4111803 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 2bf4419e-ae34-37fe-84db-43917abc14d6 | -22.99602 | -49.94398 | 2025-09-16 04:06:00 | NOAA-21 | JACAREZINHO | PARANÁ | Brasil | 4111803 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| d92cc6e0-eca2-3e03-8780-a7a268527bc9 | -21.60677 | -46.87869 | 2025-09-16 04:06:00 | NOAA-21 | SÃO JOSÉ DO RIO PARDO | SÃO PAULO | Brasil | 3549706 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| f83fdaf8-195e-3eaf-8878-331ddd45760a | -23.13132 | -49.70891 | 2025-09-16 04:06:00 | NOAA-21 | CHAVANTES | SÃO PAULO | Brasil | 3557204 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| d25b8734-0a4d-3004-8657-38fdf58de86f | -21.19799 | -44.37066 | 2025-09-16 04:06:00 | NOAA-21 | SÃO JOÃO DEL REI | MINAS GERAIS | Brasil | 3162500 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.5 |
| ff829b61-d0f6-3327-8f44-d722fac838f2 | -22.99186 | -49.94326 | 2025-09-16 04:06:00 | NOAA-21 | JACAREZINHO | PARANÁ | Brasil | 4111803 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| b40a3c83-6064-38f7-9220-c400284dacf8 | -20.86055 | -46.21547 | 2025-09-16 04:06:00 | NOAA-21 | CARMO DO RIO CLARO | MINAS GERAIS | Brasil | 3114402 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1e50b596-3636-3383-ac03-8b8f6906498a | -21.26982 | -47.01268 | 2025-09-16 04:06:00 | NOAA-21 | MONTE SANTO DE MINAS | MINAS GERAIS | Brasil | 3143203 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5f240fc4-0e98-379b-aaa1-c1f392ad2c59 | -21.22494 | -46.94429 | 2025-09-16 04:06:00 | NOAA-21 | MONTE SANTO DE MINAS | MINAS GERAIS | Brasil | 3143203 | 31 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 00a7465b-14fe-34cd-a152-2d7c635c99e7 | -22.55546 | -46.60144 | 2025-09-16 04:06:00 | NOAA-21 | SOCORRO | SÃO PAULO | Brasil | 3552106 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 4759756f-43ef-34ca-9e25-007c79536821 | -20.43962 | -47.1265 | 2025-09-16 04:06:00 | NOAA-21 | IBIRACI | MINAS GERAIS | Brasil | 3129707 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1833b77d-83d5-358f-9b8f-b57b88e76008 | -22.99347 | -49.93514 | 2025-09-16 04:06:00 | NOAA-21 | JACAREZINHO | PARANÁ | Brasil | 4111803 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 688f6065-2f26-348d-933c-de4b23651e64 | -22.34625 | -47.33535 | 2025-09-16 04:06:00 | NOAA-21 | ARARAS | SÃO PAULO | Brasil | 3503307 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| ce6c3479-5dd1-390b-8b64-c390469b8254 | -21.93814 | -46.57021 | 2025-09-16 04:06:00 | NOAA-21 | ANDRADAS | MINAS GERAIS | Brasil | 3102605 | 31 | 33 | nan | nan | nan | Mata Atlântica | 11.4 |
| 289da706-1b99-3a9a-86f1-5ddfc8e6cd9f | -20.09327 | -47.73387 | 2025-09-16 04:06:00 | NOAA-21 | IGARAPAVA | SÃO PAULO | Brasil | 3520103 | 35 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c8aba27f-8781-34c8-bbda-b90ef8b8af81 | -20.20723 | -45.36589 | 2025-09-16 04:06:00 | NOAA-21 | SANTO ANTÔNIO DO MONTE | MINAS GERAIS | Brasil | 3160405 | 31 | 33 | nan | nan | nan | Mata Atlântica | 12.2 |
| 4c76f4f4-12d3-38ce-9ba0-bdafb6d62002 | -21.9374 | -46.5745 | 2025-09-16 04:06:00 | NOAA-21 | ANDRADAS | MINAS GERAIS | Brasil | 3102605 | 31 | 33 | nan | nan | nan | Mata Atlântica | 11.4 |
| 766d3357-78a9-35cb-997e-43386442c684 | -21.26622 | -47.01194 | 2025-09-16 04:06:00 | NOAA-21 | MONTE SANTO DE MINAS | MINAS GERAIS | Brasil | 3143203 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 56571c03-921d-3a16-865e-1c4714a116cb | -22.98688 | -49.94661 | 2025-09-16 04:06:00 | NOAA-21 | JACAREZINHO | PARANÁ | Brasil | 4111803 | 41 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| ba23d7f2-a1ee-3953-8bc1-f8a37d403032 | -23.71951 | -47.45703 | 2025-09-16 04:06:00 | NOAA-21 | PIEDADE | SÃO PAULO | Brasil | 3537800 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 0d9414d9-3e94-33c9-a5c7-b83cc9e28b1d | -20.92845 | -44.26876 | 2025-09-16 04:06:00 | NOAA-21 | RESENDE COSTA | MINAS GERAIS | Brasil | 3154200 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 5f7547ff-d9a9-3a8a-966f-5ef44509bb0d | -22.57142 | -44.74411 | 2025-09-16 04:06:00 | NOAA-21 | QUELUZ | SÃO PAULO | Brasil | 3541901 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| a09868b8-b707-361f-ab89-3ff4dfa00833 | -23.20026 | -49.63427 | 2025-09-16 04:06:00 | NOAA-21 | TIMBURI | SÃO PAULO | Brasil | 3554607 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 2d22f384-1394-3c2a-ae91-af10a1fc67a1 | -22.98334 | -49.95443 | 2025-09-16 04:06:00 | NOAA-21 | JACAREZINHO | PARANÁ | Brasil | 4111803 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| adbb764a-0eca-3aa0-84a6-e3d4bf0a25cf | -20.41426 | -45.51326 | 2025-09-16 04:06:00 | NOAA-21 | CÓRREGO FUNDO | MINAS GERAIS | Brasil | 3119955 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ab3ca091-20b3-3ef9-a8e4-f4eaf18e517d | -23.23348 | -51.00596 | 2025-09-16 04:06:00 | NOAA-21 | IBIPORÃ | PARANÁ | Brasil | 4109807 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| e13839db-ef43-34cf-b3a6-bd597c9b0766 | -21.92661 | -48.25068 | 2025-09-16 04:06:00 | NOAA-21 | RIBEIRÃO BONITO | SÃO PAULO | Brasil | 3542909 | 35 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 5968df7d-d467-3bc0-8154-a875a5271d90 | -23.20099 | -49.63046 | 2025-09-16 04:06:00 | NOAA-21 | TIMBURI | SÃO PAULO | Brasil | 3554607 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 97449ee4-a41d-3cc1-abcb-f8846f1f9994 | -23.05064 | -47.30132 | 2025-09-16 04:06:00 | NOAA-21 | ELIAS FAUSTO | SÃO PAULO | Brasil | 3514908 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 2ad7b772-14c2-3770-8bd1-629c3f135a07 | -20.43879 | -47.13119 | 2025-09-16 04:06:00 | NOAA-21 | IBIRACI | MINAS GERAIS | Brasil | 3129707 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3ecc8b63-4bb4-3042-a077-ed09a662d07b | -21.2309 | -46.69995 | 2025-09-16 04:06:00 | NOAA-21 | GUAXUPÉ | MINAS GERAIS | Brasil | 3128709 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| a4bded1e-7426-35ce-bc97-08c9213d18b3 | -22.21644 | -48.3508 | 2025-09-16 04:06:00 | NOAA-21 | DOIS CÓRREGOS | SÃO PAULO | Brasil | 3514106 | 35 | 33 | nan | nan | nan | Cerrado | 5.0 |
| ff0dd33a-5130-35d6-89c0-dfde2b0d22f9 | -22.94448 | -47.0419 | 2025-09-16 04:06:00 | NOAA-21 | CAMPINAS | SÃO PAULO | Brasil | 3509502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 90ff2aae-6424-3619-adc6-b5c5e8190a7e | -19.85726 | -49.07968 | 2025-09-16 04:06:00 | NOAA-21 | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 423ba7ab-e9c3-3073-a5ac-f39570e822f0 | -20.38346 | -46.02606 | 2025-09-16 04:06:00 | NOAA-21 | PIUMHI | MINAS GERAIS | Brasil | 3151503 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5f9c6a53-9511-30d0-8e68-ed8b52344dcb | -23.19256 | -49.78285 | 2025-09-16 04:06:00 | NOAA-21 | RIBEIRÃO CLARO | PARANÁ | Brasil | 4121802 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| d4080a2c-78b5-3da1-8a20-50843f6df7d4 | -22.98527 | -49.95472 | 2025-09-16 04:06:00 | NOAA-21 | JACAREZINHO | PARANÁ | Brasil | 4111803 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 2db2b36c-7a7a-39b5-8e6b-e44a6ee9887b | -23.14888 | -49.63892 | 2025-09-16 04:06:00 | NOAA-21 | TIMBURI | SÃO PAULO | Brasil | 3554607 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 294a9354-b7bb-3c0f-8517-f7a4bb4f38d8 | -22.98412 | -49.95037 | 2025-09-16 04:06:00 | NOAA-21 | JACAREZINHO | PARANÁ | Brasil | 4111803 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| c1ee973c-5073-386d-b23d-d22b660e91de | -21.21778 | -46.94266 | 2025-09-16 04:06:00 | NOAA-21 | MONTE SANTO DE MINAS | MINAS GERAIS | Brasil | 3143203 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ff706903-eeae-3fbe-b2a2-e1dcc47e18a1 | -20.8648 | -46.21183 | 2025-09-16 04:06:00 | NOAA-21 | CARMO DO RIO CLARO | MINAS GERAIS | Brasil | 3114402 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9505160c-e8dc-3fff-aae1-0d6ce5a81c1b | -21.82477 | -46.06281 | 2025-09-16 04:06:00 | NOAA-21 | POÇO FUNDO | MINAS GERAIS | Brasil | 3151701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 437d4bb2-68e9-3540-beba-c169254a136b | -23.25948 | -48.2896 | 2025-09-16 04:06:00 | NOAA-21 | BOFETE | SÃO PAULO | Brasil | 3506904 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| f0697b80-6540-3e53-b258-e47af9f6a6a3 | -23.16309 | -47.63658 | 2025-09-16 04:06:00 | NOAA-21 | TIETÊ | SÃO PAULO | Brasil | 3554508 | 35 | 33 | nan | nan | nan | Mata Atlântica | 7.1 |
| 67be3fc5-17c4-3bb4-9860-98337e57e5a2 | -21.15818 | -44.32119 | 2025-09-16 04:06:00 | NOAA-21 | SÃO JOÃO DEL REI | MINAS GERAIS | Brasil | 3162500 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| b87c616a-4b4f-3509-9ab6-440c812b5d37 | -20.4128 | -45.18892 | 2025-09-16 04:06:00 | NOAA-21 | ITAPECERICA | MINAS GERAIS | Brasil | 3133501 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 4a193a15-24a1-3d75-9dd0-c120c364249b | -23.03854 | -45.32759 | 2025-09-16 04:06:00 | NOAA-21 | TAUBATÉ | SÃO PAULO | Brasil | 3554102 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| e52abfd4-2188-391e-822b-8f77002f4cf3 | -22.46746 | -45.21196 | 2025-09-16 04:06:00 | NOAA-21 | MARMELÓPOLIS | MINAS GERAIS | Brasil | 3140407 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.2 |
| cf51d52f-8dbf-3cb3-831d-6b2d47105989 | -20.86127 | -46.21129 | 2025-09-16 04:06:00 | NOAA-21 | CARMO DO RIO CLARO | MINAS GERAIS | Brasil | 3114402 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 904d0924-c1e2-374c-8245-f198d512e388 | -21.22057 | -46.94798 | 2025-09-16 04:06:00 | NOAA-21 | MONTE SANTO DE MINAS | MINAS GERAIS | Brasil | 3143203 | 31 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 2b4b846d-25c1-3726-94fa-b73c58a8af57 | -21.15837 | -46.28273 | 2025-09-16 04:06:00 | NOAA-21 | CONCEIÇÃO DA APARECIDA | MINAS GERAIS | Brasil | 3117108 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| a8183dfd-3481-395c-a370-10878dfc4271 | -23.03916 | -45.32383 | 2025-09-16 04:06:00 | NOAA-21 | TAUBATÉ | SÃO PAULO | Brasil | 3554102 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| f8e1c7a1-32fb-3334-a57c-19988c37cab2 | -20.53814 | -45.6141 | 2025-09-16 04:06:00 | NOAA-21 | FORMIGA | MINAS GERAIS | Brasil | 3126109 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 07e6e562-cd1b-382d-869c-b4e503440d4c | -21.20192 | -44.36752 | 2025-09-16 04:06:00 | NOAA-21 | SÃO JOÃO DEL REI | MINAS GERAIS | Brasil | 3162500 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| c53b7a39-3fe2-3780-9f58-1dbbef142c83 | -23.44657 | -47.67572 | 2025-09-16 04:06:00 | NOAA-21 | CAPELA DO ALTO | SÃO PAULO | Brasil | 3510302 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.6 |
| 574821f3-46c7-3f8a-a827-8ea92d243d68 | -5.98462 | -45.8391 | 2025-09-16 04:27:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e1bacdf2-c016-3e38-8c85-50fad9fc64f8 | -6.29391 | -42.39322 | 2025-09-16 04:27:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 35fa655f-cc28-3900-a362-205ad2ba966a | -6.18609 | -41.18371 | 2025-09-16 04:27:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 55c65412-5da6-3291-b72f-a0334b8ea6a1 | -3.89293 | -42.51707 | 2025-09-16 04:27:00 | NPP-375D | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| a4c9355f-ee32-39b5-999c-b844e5c61530 | -3.81643 | -41.56029 | 2025-09-16 04:27:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| ca4acf1d-4de9-3dea-9a94-699b4674e404 | -5.6034 | -42.89577 | 2025-09-16 04:27:00 | NPP-375D | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| f2ebea0a-67f6-3e34-a587-76bdfadc1e01 | -5.56882 | -41.18547 | 2025-09-16 04:27:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| ef153ce2-b289-3ca4-8d14-4932bc259ba8 | -6.21913 | -43.8996 | 2025-09-16 04:27:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 5fd4c523-70cb-3188-8382-39ae1de512bf | -6.46466 | -43.68036 | 2025-09-16 04:27:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 05b6551c-bf01-3a94-a94d-2fd57783a898 | -2.57469 | -48.39431 | 2025-09-16 04:27:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 016f7946-a149-31a9-9d25-52157b34762e | -5.66939 | -43.32278 | 2025-09-16 04:27:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 400e094e-eeb6-3164-a8b4-61840551762d | -3.81357 | -41.57895 | 2025-09-16 04:27:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 75c11990-a2e7-3079-93cd-bd8614b99da6 | -5.79737 | -45.93092 | 2025-09-16 04:27:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 595964b7-1f6f-3cab-8dcc-64ef91d7f15c | -4.04344 | -49.07587 | 2025-09-16 04:27:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 293a0feb-7f50-3264-9326-7a5c3077aa20 | -4.13245 | -51.07951 | 2025-09-16 04:27:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b0270d0b-0b6e-3514-b1c3-d03c6f4d49ce | -6.40529 | -42.65596 | 2025-09-16 04:27:00 | NPP-375D | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 6078d935-c3b7-3379-bdee-c6a5a502bf1d | -6.81368 | -45.615 | 2025-09-16 04:27:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 66b2b4fd-2082-3ba5-b2c5-12fc394e5ccb | -5.26542 | -43.77925 | 2025-09-16 04:27:00 | NPP-375D | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e308d132-df8d-34e5-8da4-d02f8aa6276b | -6.52343 | -51.19407 | 2025-09-16 04:27:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9b4f10ca-af1a-3ef5-923a-75f1e4b210ea | -5.79627 | -45.93781 | 2025-09-16 04:27:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9bd529bf-a168-3802-9461-20917cb9dc86 | -6.52729 | -41.82442 | 2025-09-16 04:27:00 | NPP-375D | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| ea6806d6-8817-365c-a040-cd69339dd711 | -5.90383 | -45.89759 | 2025-09-16 04:27:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ccdbc795-061a-38ad-b491-ace78bd3b4c0 | -6.17564 | -41.22536 | 2025-09-16 04:27:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| b045bafa-8c76-3590-8b3c-4b5fedee6be9 | -4.60836 | -48.78838 | 2025-09-16 04:27:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2c8967f1-1ae2-310b-8e19-41c1666a597b | -3.46238 | -52.90145 | 2025-09-16 04:27:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2431c038-0e66-31fd-87e7-e188cda2240b | -6.82393 | -47.83449 | 2025-09-16 04:27:00 | NPP-375D | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0316b280-4ca3-381f-83b3-64c8b8597f91 | -5.98731 | -45.80033 | 2025-09-16 04:27:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3a357125-2bbe-3483-8b2c-9e111b011e11 | -5.28823 | -45.25559 | 2025-09-16 04:27:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1f1060e7-2445-314c-a023-c90491787fb8 | -6.92198 | -44.80141 | 2025-09-16 04:27:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 72aec118-baf5-3b9d-86df-79ae63fb76ca | -7.26334 | -46.61092 | 2025-09-16 04:27:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 5fe43a97-ad59-3e86-aa5c-9450717871d2 | -6.21855 | -43.90344 | 2025-09-16 04:27:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 5ab86481-8cef-30b7-a696-cdf90cbeaa2d | -7.37235 | -44.29631 | 2025-09-16 04:27:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1ef845f1-450a-37a5-b6ad-91d380ec6e70 | -6.25719 | -43.46427 | 2025-09-16 04:27:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 724f3a66-cff8-3b34-b9a1-3288cb94f8ba | -6.12603 | -43.37535 | 2025-09-16 04:27:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3088d574-7804-3b8c-8566-b52276abbaab | -5.88896 | -45.73885 | 2025-09-16 04:27:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| e1dc1778-5a11-3889-b45b-c5b3fbd29e59 | -5.67253 | -51.13839 | 2025-09-16 04:27:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 46ef1b66-5714-30fd-a694-84796d3e8aef | -3.85408 | -48.97892 | 2025-09-16 04:27:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ae4daded-f915-3b47-82e0-cb2ff3d2648a | -6.18636 | -41.17967 | 2025-09-16 04:27:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 710f7850-eae5-311c-b526-426c5425426b | -3.82484 | -44.10048 | 2025-09-16 04:27:00 | NPP-375D | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9eda13bf-07c3-3a7d-96b0-4837d78cb2d4 | -7.52055 | -44.35733 | 2025-09-16 04:27:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f1326297-0784-3004-a277-dda2104e292c | -6.25558 | -46.11688 | 2025-09-16 04:27:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 24c109d2-2373-3db6-bcef-99bbb35fb541 | -6.24651 | -43.46267 | 2025-09-16 04:27:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 019adf86-2654-3821-8081-863f2bd24368 | -7.00699 | -45.64131 | 2025-09-16 04:27:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 54ddc6d5-d2fc-3e07-bba1-a8f5e0124224 | -6.12539 | -42.94136 | 2025-09-16 04:27:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| f0cad566-ef97-323f-ac4e-48c0919c701b | -7.14833 | -44.32494 | 2025-09-16 04:27:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |


[Clique aqui para ver as próximas entradas](README30.md)
