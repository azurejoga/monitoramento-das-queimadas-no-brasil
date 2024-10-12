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

## Dados Diários - Página 10

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 84eedae3-a1b1-36b0-b8f1-804ef3eacf12 | -17.9837 | -57.3819 | 2024-10-12 00:36:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 58.4 |
| 5c1bed7a-bd32-3666-8206-8a29ed8d646b | -17.9841 | -57.3612 | 2024-10-12 00:36:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 58.9 |
| c44566cb-3505-39e2-abf2-5d5c382834bd | -2.77 | -51.3829 | 2024-10-12 00:45:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 75.7 |
| 14ecb5ac-176c-3784-a2be-97f110262ab6 | -2.7701 | -51.3622 | 2024-10-12 00:45:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 99.7 |
| 658142ca-5145-3fef-a05f-cb19695b6146 | -2.7884 | -51.3825 | 2024-10-12 00:45:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 101.6 |
| f20bdf2b-d40d-3e3a-83de-652b9ba908bb | -2.7885 | -51.3618 | 2024-10-12 00:45:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 157.1 |
| a866427b-176d-3451-8a15-fcd8d46e4c3a | -2.7983 | -54.0129 | 2024-10-12 00:45:22 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 84.5 |
| d3987975-e6fe-3203-936a-6bdf0a868b15 | -2.8611 | -51.6699 | 2024-10-12 00:45:23 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 82.9 |
| 937f30ff-fef9-32c5-8f92-4e5ab82e0958 | -3.1426 | -50.3724 | 2024-10-12 00:45:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 74.8 |
| c0a200d2-c912-3e33-a609-aa1e81d2232c | -3.1427 | -50.3514 | 2024-10-12 00:45:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 72.1 |
| 2b18bb78-76f6-34af-b84e-a1b298cfb373 | -3.161 | -50.3718 | 2024-10-12 00:45:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 87.0 |
| 9390ef84-d6e2-30ec-b4b2-e7b9ff33ea4a | -3.1611 | -50.3508 | 2024-10-12 00:45:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 110.3 |
| 31312429-b64d-3030-947a-05e9439b267a | -3.2136 | -46.7843 | 2024-10-12 00:45:24 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 50.7 |
| f1e43709-fef8-3dc7-8b56-19c242a8035b | -3.6978 | -50.1225 | 2024-10-12 00:45:27 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 130.0 |
| f82248a8-8c07-391a-8d69-253ba722aef9 | -3.6979 | -50.1015 | 2024-10-12 00:45:27 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 80.8 |
| dd4c3eec-83d1-3f7f-be50-55ea0ba4e3d1 | -3.7163 | -50.1219 | 2024-10-12 00:45:27 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 81.6 |
| df6db41a-3e31-3cec-99e8-90b6bff7a4ef | -3.7844 | -51.3312 | 2024-10-12 00:45:28 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 71.8 |
| d2da841b-f478-3a32-b8ca-307983d6ca09 | -3.7845 | -51.3104 | 2024-10-12 00:45:28 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 73.5 |
| 5d720569-3181-35b9-9221-a18647c7e432 | -3.8167 | -52.3403 | 2024-10-12 00:45:28 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 58.5 |
| cdec9db2-d669-30f6-9570-2e7069358bbc | -3.9394 | -46.445 | 2024-10-12 00:45:29 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 127.2 |
| 2b2f1bdc-0b94-3c3c-adb7-de9d5808bf74 | -3.9396 | -46.4229 | 2024-10-12 00:45:29 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 126.5 |
| 5df2fa3d-8b89-35ad-a204-bdb40a183329 | -4.1148 | -48.2515 | 2024-10-12 00:45:30 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 79.2 |
| 6c1031f3-87e9-3629-af2b-1add019c3297 | -4.2665 | -50.9594 | 2024-10-12 00:45:31 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 96.6 |
| fed09267-93ac-34e2-b571-25b371393bee | -4.285 | -50.9586 | 2024-10-12 00:45:31 | GOES-16 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 76.2 |
| 5de3256e-539a-393c-a1c4-2c548fbd56ff | -4.3782 | -50.8087 | 2024-10-12 00:45:31 | GOES-16 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 90.5 |
| eb5c3a75-fca4-37e5-8175-c9849944e74a | -4.7004 | -60.8266 | 2024-10-12 00:45:33 | GOES-16 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 48.7 |
| 7725ddfb-b2c5-3036-ab27-f71142893e12 | -4.7004 | -60.8077 | 2024-10-12 00:45:33 | GOES-16 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 108.0 |
| 6f0777f8-c3e9-3fb1-b18b-ca3b80bdc804 | -4.7188 | -60.8072 | 2024-10-12 00:45:33 | GOES-16 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 61.9 |
| 2f0dbac4-092a-3f5c-b629-6475b6f79e75 | -4.7188 | -60.7882 | 2024-10-12 00:45:33 | GOES-16 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 94.4 |
| ce386aa4-82d9-3658-a50b-dbbd56f66c12 | -4.7371 | -60.7877 | 2024-10-12 00:45:33 | GOES-16 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 72.8 |
| 1600797b-2d32-3760-99b6-1a731a7faf39 | -5.5547 | -44.689 | 2024-10-12 00:45:38 | GOES-16 | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 60.3 |
| 4fd4f6a8-7625-3560-9a8d-ce02e80baa8f | -6.0791 | -44.6276 | 2024-10-12 00:45:41 | GOES-16 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 55.6 |
| 25f73557-3636-3d96-a8a2-bbf493c89233 | -6.7284 | -59.346 | 2024-10-12 00:45:45 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 90.6 |
| b6ccb06e-5e38-3445-a177-17b447496316 | -6.7285 | -59.3267 | 2024-10-12 00:45:45 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 147.8 |
| 51a1aba1-98df-3ba9-bca9-8d3bcbdb8e9a | -6.7469 | -59.3452 | 2024-10-12 00:45:45 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 225.1 |
| 463a23c8-4ab5-3ab8-925b-fd9d1152a932 | -6.747 | -59.3259 | 2024-10-12 00:45:45 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 432.0 |
| 0c6e5bf1-7ce6-3573-9b46-1931f3202134 | -6.7471 | -59.3067 | 2024-10-12 00:45:45 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 65.9 |
| 0cad006d-acac-31ea-8056-134528064dce | -6.7654 | -59.3252 | 2024-10-12 00:45:45 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 81.7 |
| 6fd274b3-3a9e-3d66-88a8-ddb5ab23ffd5 | -6.8776 | -59.0697 | 2024-10-12 00:45:46 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 61.4 |
| b488ca4d-f505-34c8-8495-b9d5cbedf09c | -7.8715 | -54.7016 | 2024-10-12 00:45:51 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 73.9 |
| 9a1db603-6741-3782-bd54-897bb61bc5f5 | -8.2325 | -61.1823 | 2024-10-12 00:45:54 | GOES-16 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 52.2 |
| d66ab3a8-1fc0-31ca-9db3-d6b612b6af15 | -8.4231 | -55.4704 | 2024-10-12 00:45:54 | GOES-16 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 54.1 |
| 3b276d9d-95bd-3e41-ba3d-e284367367f8 | -8.4631 | -66.9783 | 2024-10-12 00:45:55 | GOES-16 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 45.2 |
| 8d01baa0-0105-3165-a72b-74e9fb2743a7 | -9.5878 | -64.1034 | 2024-10-12 00:46:01 | GOES-16 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 63.8 |
| 66f16852-d328-3a36-b26b-aa24aa4d43ac | -9.6594 | -56.9635 | 2024-10-12 00:46:01 | GOES-16 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 57.3 |
| 3a7e5489-5429-3f76-8a26-e05a1039bc77 | -10.3708 | -61.232 | 2024-10-12 00:46:06 | GOES-16 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 72.5 |
| 9f74d0f4-c45f-3415-a28c-36bd616131cd | -10.3892 | -61.2695 | 2024-10-12 00:46:06 | GOES-16 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 60.0 |
| 58ff2617-4eb8-3304-82e3-61bba543d930 | -10.3897 | -61.2118 | 2024-10-12 00:46:06 | GOES-16 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 60.2 |
| be96974f-61e0-3d0e-a358-08317bb10f62 | -10.4079 | -61.2685 | 2024-10-12 00:46:06 | GOES-16 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 60.5 |
| fdac6b92-ed58-3dc2-b0a8-24c4258054e4 | -10.9506 | -44.653 | 2024-10-12 00:46:08 | GOES-16 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 83.2 |
| a238dda6-5c2d-36b0-9824-19173d391238 | -10.8362 | -64.2027 | 2024-10-12 00:46:08 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 37.3 |
| 373171ca-586d-3b19-be8a-1b0e3314ece0 | -11.2912 | -50.9208 | 2024-10-12 00:46:10 | GOES-16 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 61.9 |
| 23f57b63-39fc-3b63-a211-0af86972b185 | -11.2915 | -50.8995 | 2024-10-12 00:46:10 | GOES-16 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 60.5 |
| c090f8f3-181a-38f5-b8e6-d64eb4950c9e | -11.3102 | -50.9187 | 2024-10-12 00:46:10 | GOES-16 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 146.1 |
| d9974de2-481e-38f2-8db7-53b2f262a1c5 | -11.3105 | -50.8974 | 2024-10-12 00:46:10 | GOES-16 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 161.3 |
| e22250ee-2b23-3d34-9893-622df775a200 | -11.3292 | -50.9167 | 2024-10-12 00:46:10 | GOES-16 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 78.2 |
| 36a6c2ee-88bc-32b1-9353-da555a771266 | -11.3295 | -50.8954 | 2024-10-12 00:46:10 | GOES-16 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 77.6 |
| 7612a3d7-ef15-3ea9-88ff-4ea358933322 | -11.2761 | -60.5038 | 2024-10-12 00:46:11 | GOES-16 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 74.5 |
| 0d3b1537-9e97-3d1e-97c1-3fa8ca3c63ac | -11.2763 | -60.4844 | 2024-10-12 00:46:11 | GOES-16 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 71.9 |
| 33f96f9b-cb0e-3316-8e5a-d6e29be13038 | -11.8188 | -58.8459 | 2024-10-12 00:46:14 | GOES-16 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 56.7 |
| 2c9e6759-996c-3dae-b27f-61e225175b1b | -11.8375 | -58.8642 | 2024-10-12 00:46:14 | GOES-16 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 55.1 |
| 38dd0839-a831-3fb6-a97c-b77059cb1bbe | -11.8377 | -58.8445 | 2024-10-12 00:46:14 | GOES-16 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 142.7 |
| 170fbf03-1c04-374a-98ff-c7bf98c11286 | -12.6034 | -48.6209 | 2024-10-12 00:46:17 | GOES-16 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 58.6 |
| c761cf0b-1e5f-3a9e-ba6b-4cfd77154640 | -12.6038 | -48.5988 | 2024-10-12 00:46:17 | GOES-16 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 62.9 |
| ea161c3f-3304-3a1e-8eb8-1deaace1fe4c | -12.7678 | -44.8671 | 2024-10-12 00:46:18 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 83.4 |
| 00992d20-1e37-3b70-8346-606e01c612fe | -12.7866 | -44.8873 | 2024-10-12 00:46:18 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 124.2 |
| 5ad9d730-0525-3f28-8fa2-b1656d4f62d3 | -12.7871 | -44.8639 | 2024-10-12 00:46:18 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 510.1 |
| ad40011f-afea-3fca-83fa-edc10908dd5f | -12.7875 | -44.8406 | 2024-10-12 00:46:18 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 330.3 |
| 1f33504a-4744-34cf-b64d-65828249f459 | -12.8064 | -44.8608 | 2024-10-12 00:46:18 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 179.8 |
| 49d24248-d990-37b5-b874-3b0cf93d69aa | -12.8069 | -44.8375 | 2024-10-12 00:46:18 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 117.4 |
| 49fe3ae9-4b1e-3301-963b-3bf07c8b9ac3 | -13.213 | -51.1216 | 2024-10-12 00:46:21 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 65.4 |
| 475e915d-118f-39e8-8464-3ee017dfc7a3 | -13.2322 | -51.1192 | 2024-10-12 00:46:21 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 82.6 |
| ff1d94b3-177a-3d87-8b7f-6712cb190ca7 | -13.2325 | -51.0978 | 2024-10-12 00:46:21 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 64.4 |
| d32f9609-2555-3212-9887-4e3d11449596 | -15.6228 | -59.9585 | 2024-10-12 00:46:35 | GOES-16 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 62.0 |
| 8ea63396-7278-3ccc-a652-46bdc2d610a0 | -16.9802 | -57.4609 | 2024-10-12 00:46:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 76.0 |
| 9af98c9a-d50b-3ade-b185-c4c61b3c63e3 | -16.9805 | -57.4404 | 2024-10-12 00:46:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 112.4 |
| 7d0a16a4-9f01-3d5f-b12e-1058cb905136 | -16.9998 | -57.4586 | 2024-10-12 00:46:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 84.3 |
| 6659918c-c44a-3947-9f6c-928669ee8fe5 | -17.0001 | -57.4381 | 2024-10-12 00:46:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 71.3 |
| bbd16920-56a3-3838-92fe-36dc6c8de769 | -17.1758 | -57.479 | 2024-10-12 00:46:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 75.9 |
| 69068970-6fa9-391c-b3fa-addda1ebd32e | -17.1761 | -57.4585 | 2024-10-12 00:46:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 118.4 |
| c665342c-c4a9-370c-9a67-c61a5b08861c | -17.627 | -56.3318 | 2024-10-12 00:46:45 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 127.6 |
| 280999a2-8999-3d9a-9d03-6e7e3d5df87b | -17.6273 | -56.311 | 2024-10-12 00:46:45 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 77.2 |
| d3ec2f72-5b3d-3f8d-ac60-fab40869c3bc | -17.6467 | -56.3292 | 2024-10-12 00:46:45 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 149.3 |
| d15b922a-a568-3dd4-ab2d-bb2d987a4b18 | -17.6471 | -56.3084 | 2024-10-12 00:46:45 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 93.9 |
| c6687518-78e8-3d67-b40a-9ba555eb2783 | -17.964 | -57.3843 | 2024-10-12 00:46:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 93.5 |
| 7a5b3fda-1e54-310c-ac05-83d2e57e271a | -17.9643 | -57.3637 | 2024-10-12 00:46:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 89.4 |
| 863e6baf-34c3-3534-8a62-d9ec84373ac8 | -17.9837 | -57.3819 | 2024-10-12 00:46:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 81.2 |
| 7da1e5f6-8a42-3e8c-b2ae-a65f6efab802 | -17.9841 | -57.3612 | 2024-10-12 00:46:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 85.9 |
| bd3948d3-9647-3ac0-9e3b-5147c6b9ad9e | -1.6061 | -53.3492 | 2024-10-12 00:55:15 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 50.9 |
| 7c5d06a4-787c-39d8-8865-ae95fa401880 | -2.77 | -51.3829 | 2024-10-12 00:55:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 82.3 |
| 3ffe644c-4ffc-3d45-85cf-a461287afcae | -2.7701 | -51.3622 | 2024-10-12 00:55:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 106.2 |
| 1fdb3e55-f9b9-3d39-b74d-fd0dec5fec22 | -2.7884 | -51.3825 | 2024-10-12 00:55:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 99.3 |
| 6ecd39d3-d390-3c5b-bc4c-367febc20101 | -2.7885 | -51.3618 | 2024-10-12 00:55:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 149.5 |
| 798eb53f-abe9-36c9-9efa-0cd3bf460a61 | -2.7983 | -54.0129 | 2024-10-12 00:55:22 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 85.9 |
| 473ba079-1506-36fd-aaad-fa49bb7bc11a | -2.8611 | -51.6699 | 2024-10-12 00:55:23 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 85.4 |
| 650ba221-c640-37f2-ac9b-b0ea925a64cb | -3.1426 | -50.3724 | 2024-10-12 00:55:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 69.3 |
| c766c56e-d2db-32de-b618-9d76bab0c8e5 | -3.1427 | -50.3514 | 2024-10-12 00:55:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 69.9 |
| 93c16121-5029-38c0-9436-d0bf5f5485e5 | -3.161 | -50.3718 | 2024-10-12 00:55:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 104.1 |
| fd191e45-56c3-3b2f-879b-df5733d21208 | -3.1611 | -50.3508 | 2024-10-12 00:55:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 113.7 |
| eaf4fcea-dffb-3733-aa3d-0ba68fb358f0 | -3.2136 | -46.7843 | 2024-10-12 00:55:24 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 58.4 |


[Clique aqui para ver as próximas entradas](README11.md)
