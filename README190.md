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

## Dados Diários - Página 190

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f8b845d6-7e87-39cd-81c3-60ce96c8fe4d | -21.9583 | -48.5638 | 2024-09-26 13:57:07 | GOES-16 | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 134.9 |
| f0f5bde5-d0a0-30f5-9612-acf38c953d5a | -21.9374 | -48.5688 | 2024-09-26 13:57:07 | GOES-16 | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 163.6 |
| eb1e9734-9960-30b8-8945-bc746e4a3c89 | -21.9381 | -48.5453 | 2024-09-26 13:57:07 | GOES-16 | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 139.9 |
| 309729ab-68c6-332a-b264-dd6fccd56520 | -22.679 | -47.3927 | 2024-09-26 13:57:11 | GOES-16 | LIMEIRA | SÃO PAULO | Brasil | 3526902 | 35 | 33 | nan | nan | nan | Cerrado | 194.9 |
| b7f1394c-25b3-3524-927c-b5cfe118f488 | -22.27 | -48.67 | 2024-09-26 14:03:18 | MSG-03 | ITAPUÍ | SÃO PAULO | Brasil | 3522901 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| bc6d0d5d-4a74-3f29-800f-e31c4de28b06 | -13.16 | -45.49 | 2024-09-26 14:04:08 | MSG-03 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| a7936e98-2ca7-3585-9db6-d9a37e031fb7 | -12.83 | -54.07 | 2024-09-26 14:04:14 | MSG-03 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 8b8d6eec-6c75-3b70-9cd1-7d3635775ea4 | -12.83 | -54.01 | 2024-09-26 14:04:14 | MSG-03 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c38d5c5b-98af-3dfb-9bf9-55bc3c735b90 | -11.94 | -47.33 | 2024-09-26 14:04:16 | MSG-03 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 2bdf5915-aa13-3b87-8e60-5b3ff0574df2 | -10.83 | -45.95 | 2024-09-26 14:04:21 | MSG-03 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 5c582da3-4aae-3a5c-a774-3d05c6468117 | -11.18 | -45.56 | 2024-09-26 14:04:21 | MSG-03 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 9468a7e2-2465-3de0-be2b-902a699841b4 | -11.22 | -54.77 | 2024-09-26 14:04:21 | MSG-03 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| fe7d25c3-5e3c-39f7-92ef-69ef817b0ad9 | -10.65 | -45.96 | 2024-09-26 14:04:24 | MSG-03 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| c6e73991-51c4-328d-b29d-ce408796f5c5 | -10.65 | -45.91 | 2024-09-26 14:04:24 | MSG-03 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| ec0847bb-c593-3a25-b1f9-419d2e630be2 | -10.8 | -45.94 | 2024-09-26 14:04:24 | MSG-03 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 55be2ada-6bcb-30b8-a821-711721e62949 | -10.01 | -53.48 | 2024-09-26 14:04:29 | MSG-03 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| aa48e724-464d-3486-9821-75fedf9ff7fe | -10.04 | -53.48 | 2024-09-26 14:04:29 | MSG-03 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a5429ebf-ae7b-35b2-8375-50228bd7627f | -10.04 | -53.42 | 2024-09-26 14:04:29 | MSG-03 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 261eb726-17bc-3cf1-a898-3869e6d8dd56 | -21.34 | -51.0 | 2024-09-26 15:03:23 | MSG-03 | VALPARAÍSO | SÃO PAULO | Brasil | 3556305 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 79f4be08-10b0-3965-a2d3-b289c157b909 | -20.85 | -48.95 | 2024-09-26 15:03:25 | MSG-03 | OLÍMPIA | SÃO PAULO | Brasil | 3533908 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 407d3978-eb48-3b1b-853a-0a286dcd0acb | -15.71 | -41.1 | 2024-09-26 15:03:52 | MSG-03 | ENCRUZILHADA | BAHIA | Brasil | 2910404 | 29 | 33 | nan | nan | nan | Mata Atlântica | nan |
| fec763e6-916c-3b8d-b512-d33c6166a7bf | -15.68 | -41.09 | 2024-09-26 15:03:54 | MSG-03 | ENCRUZILHADA | BAHIA | Brasil | 2910404 | 29 | 33 | nan | nan | nan | Mata Atlântica | nan |
| bb814915-79d0-3b17-8244-42a7de3b52bd | -12.83 | -54.01 | 2024-09-26 15:04:13 | MSG-03 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c8c947b0-c002-3154-850c-ef618c4c6016 | -11.22 | -54.77 | 2024-09-26 15:04:21 | MSG-03 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 0aa6f531-8749-3bf0-b5c2-a2ec842e2c25 | -11.21 | -45.57 | 2024-09-26 15:04:21 | MSG-03 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 81087265-9c2f-3ec4-96b6-83085d335a2e | -10.04 | -53.42 | 2024-09-26 15:04:28 | MSG-03 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 87ee65e3-77e6-3354-9981-177b7aa9ea90 | -10.04 | -53.48 | 2024-09-26 15:04:28 | MSG-03 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| edc1a757-f47a-36c0-bb7f-0b5686fa745f | -10.01 | -53.48 | 2024-09-26 15:04:28 | MSG-03 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ad598c5f-2d80-3c10-8fd4-477766805c86 | -2.8611 | -51.6699 | 2024-09-26 15:05:23 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 294.7 |
| 4ff8492f-54a5-3092-8710-2fde10430b69 | -3.5488 | -50.38 | 2024-09-26 15:05:27 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 71.0 |
| 93124189-71a0-305a-b8ec-cea549827664 | -4.3719 | -48.6704 | 2024-09-26 15:05:31 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 67.8 |
| d5e8a0e3-fbf4-30ab-902a-cf8e3d9f2e73 | -5.26 | -49.0541 | 2024-09-26 15:05:36 | GOES-16 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 70.9 |
| bb40c162-5b64-33fc-b316-71fe5369f1a1 | -5.2029 | -49.2495 | 2024-09-26 15:05:36 | GOES-16 | NOVA IPIXUNA | PARÁ | Brasil | 1504976 | 15 | 33 | nan | nan | nan | Amazônia | 89.7 |
| 1664638c-c4f6-3e40-8768-21b3482d592b | -5.1843 | -49.2505 | 2024-09-26 15:05:36 | GOES-16 | NOVA IPIXUNA | PARÁ | Brasil | 1504976 | 15 | 33 | nan | nan | nan | Amazônia | 69.3 |
| c7e03993-f7fd-3d52-ab82-44aa12b29c41 | -5.1842 | -49.2718 | 2024-09-26 15:05:36 | GOES-16 | NOVA IPIXUNA | PARÁ | Brasil | 1504976 | 15 | 33 | nan | nan | nan | Amazônia | 90.4 |
| 0b341017-06b7-3b00-96c6-7e34c1cb1a01 | -5.8351 | -49.1706 | 2024-09-26 15:05:40 | GOES-16 | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 66.5 |
| e76b4e8a-b71f-3684-ae01-d902cf6e8a95 | -6.841 | -59.0132 | 2024-09-26 15:05:46 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 56.7 |
| 7532cce3-0d7b-3dd5-b078-269c285edcc0 | -6.8224 | -59.0333 | 2024-09-26 15:05:46 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 53.1 |
| 0dbba7db-b2a8-3996-986a-02f5ce778ba7 | -7.0612 | -59.2358 | 2024-09-26 15:05:47 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 50.8 |
| eaae5d5b-0468-366f-8022-458878104ada | -7.3157 | -44.7515 | 2024-09-26 15:05:48 | GOES-16 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 69.8 |
| 916cdf6e-db88-3644-a05a-c32e43def29e | -7.5869 | -49.1986 | 2024-09-26 15:05:49 | GOES-16 | PAU D'ARCO | TOCANTINS | Brasil | 1716307 | 17 | 33 | nan | nan | nan | Amazônia | 48.1 |
| 93d773dd-529b-3361-9b2d-ae0e59afb707 | -7.3854 | -64.3662 | 2024-09-26 15:05:49 | GOES-16 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 58.0 |
| 42f972f0-95d1-3306-a965-cf02323b7c4e | -7.5256 | -44.4795 | 2024-09-26 15:05:49 | GOES-16 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 83.5 |
| 8439d47c-a2f7-33fc-99c9-9584325eb925 | -7.8406 | -61.7887 | 2024-09-26 15:05:51 | GOES-16 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 56.1 |
| 9258ee85-b941-376f-8fe6-d4bd1e3a0157 | -8.5862 | -44.0924 | 2024-09-26 15:05:55 | GOES-16 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 34.2 |
| ca05fbea-3105-3acf-816d-8cec06255686 | -10.4246 | -53.6987 | 2024-09-26 15:06:06 | GOES-16 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 61.6 |
| 0ede0b12-72aa-32eb-a4a7-9cc7e7234315 | -10.5698 | -51.1022 | 2024-09-26 15:06:06 | GOES-16 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 63.6 |
| 1ef45df9-edf5-345f-a32e-63e3a6bae47f | -10.9601 | -50.2101 | 2024-09-26 15:06:08 | GOES-16 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 103.1 |
| 8419f272-9dbb-3f84-a71a-e919f66138af | -10.942 | -50.1478 | 2024-09-26 15:06:08 | GOES-16 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 86.0 |
| e05dd269-2db2-345f-85ea-b08584e2cebe | -10.9038 | -50.1733 | 2024-09-26 15:06:08 | GOES-16 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 74.2 |
| 13270c89-3f7c-3079-b973-15e4c27b9f92 | -10.8851 | -50.1539 | 2024-09-26 15:06:08 | GOES-16 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 77.4 |
| d54ae671-9f4e-30f6-989b-f2509a36c375 | -10.8662 | -50.156 | 2024-09-26 15:06:08 | GOES-16 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 92.7 |
| c3210638-4e15-319f-9efd-75cb1c47e0fb | -10.8602 | -50.5839 | 2024-09-26 15:06:08 | GOES-16 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 81.9 |
| dadd5549-1259-3ecb-9ed6-60cbcccd2364 | -11.0953 | -51.3866 | 2024-09-26 15:06:09 | GOES-16 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 88.7 |
| cefb7dad-3a76-38c1-8394-1f7bef5a4644 | -11.0059 | -53.9344 | 2024-09-26 15:06:09 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 67.6 |
| 99d9fddb-c449-3ed3-a968-9d47387fbd22 | -11.0057 | -53.9549 | 2024-09-26 15:06:09 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 100.4 |
| 0602e3ce-8d3d-3dcc-aac0-a92ad0f0a763 | -11.0173 | -50.1824 | 2024-09-26 15:06:09 | GOES-16 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 52.0 |
| 6d57bee4-1bfb-3fd1-82bd-fd998f64e43c | -10.9791 | -50.208 | 2024-09-26 15:06:09 | GOES-16 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 71.1 |
| 5c391dcd-f83f-30ee-b2f6-5d0ff2ab6000 | -11.3028 | -50.1077 | 2024-09-26 15:06:10 | GOES-16 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 83.0 |
| b5f988f9-a83b-3253-8b07-e43816568331 | -11.2633 | -50.2194 | 2024-09-26 15:06:10 | GOES-16 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 99.3 |
| 38a15955-fe86-391a-bd61-46845dbb323f | -11.2629 | -50.2409 | 2024-09-26 15:06:10 | GOES-16 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 109.5 |
| 9ab4cece-c431-3ad3-b9a6-ccc6bbf6bc5f | -11.1714 | -50.0151 | 2024-09-26 15:06:10 | GOES-16 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 91.3 |
| 8a2f40c9-6a42-39b1-a21e-a3cc6b89acf2 | -11.1522 | -51.3806 | 2024-09-26 15:06:10 | GOES-16 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 91.9 |
| aaf22e96-a5f6-32ee-b488-7acf51eb0c29 | -11.1335 | -51.3615 | 2024-09-26 15:06:10 | GOES-16 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 98.0 |
| d7e725df-0783-37ed-8774-7db84f8cdd5f | -11.1332 | -51.3826 | 2024-09-26 15:06:10 | GOES-16 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 119.4 |
| d376ee8e-c4d1-3d2e-8f91-a982fc5a409a | -11.4677 | -50.5176 | 2024-09-26 15:06:11 | GOES-16 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 83.8 |
| be44e3d4-8aa3-3558-8349-918c9756b0f3 | -11.4487 | -50.5197 | 2024-09-26 15:06:11 | GOES-16 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 93.1 |
| 93ea9c48-7c19-38ee-a40d-f0038dfc63c5 | -11.4297 | -50.5219 | 2024-09-26 15:06:11 | GOES-16 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 96.0 |
| aaa9411d-14ec-3c32-bd73-4fd2ab8c2d2e | -12.3618 | -50.5417 | 2024-09-26 15:06:16 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 106.8 |
| 40c1b041-91d6-3a5b-af0b-8a67cab00f4e | -12.3239 | -50.5248 | 2024-09-26 15:06:16 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 93.0 |
| ae81c991-4074-3af1-a453-cf992808daed | -12.3236 | -50.5463 | 2024-09-26 15:06:16 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 89.8 |
| 2ba5c78c-d148-3173-892a-286d1e31f951 | -12.3048 | -50.5271 | 2024-09-26 15:06:16 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 98.7 |
| 8f114b71-a74c-3f09-b821-e9741a0d467a | -12.3045 | -50.5486 | 2024-09-26 15:06:16 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 81.8 |
| ac7b50a6-fb8f-3e9b-8b0c-d4fe079e9f2f | -12.286 | -50.5079 | 2024-09-26 15:06:16 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 75.1 |
| 4d80c95d-559d-3c92-b672-18f75e7db3be | -12.2472 | -50.5555 | 2024-09-26 15:06:16 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 91.8 |
| 8591ddfe-496c-34eb-bd0f-4c383ac85f06 | -12.2468 | -50.577 | 2024-09-26 15:06:16 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 89.7 |
| b6dedb14-6c5a-3c46-89b0-b544c83dcbcf | -12.2248 | -50.7722 | 2024-09-26 15:06:16 | GOES-16 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 93.6 |
| ac01c844-fea5-33ce-a3af-a4242df77022 | -12.2241 | -50.815 | 2024-09-26 15:06:16 | GOES-16 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 73.3 |
| a5745b60-bbcc-3780-b834-477ce9039609 | -12.4977 | -50.3962 | 2024-09-26 15:06:17 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 79.0 |
| 31830321-04f3-364e-aa0a-8a393af97924 | -12.4974 | -50.4177 | 2024-09-26 15:06:17 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 89.5 |
| fe23f0c1-f386-3059-8165-94e786f43d64 | -12.5464 | -53.5147 | 2024-09-26 15:06:18 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 77.2 |
| 0e6d6029-4d6c-3fab-9157-b3ac632b82e7 | -12.8469 | -51.2737 | 2024-09-26 15:06:19 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 87.4 |
| abd7499e-3edb-3302-bdec-c7fb0c82f898 | -12.8462 | -51.3164 | 2024-09-26 15:06:19 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 81.1 |
| b19f87cf-bd97-3055-8f76-a7059c3e7e66 | -12.8435 | -51.4869 | 2024-09-26 15:06:19 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 97.0 |
| 66078f94-9640-3900-b569-aecca62bd3b2 | -12.828 | -51.2547 | 2024-09-26 15:06:19 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 84.1 |
| 12ffd7dc-c941-3181-bce8-202d9c536d6d | -12.8082 | -51.2997 | 2024-09-26 15:06:19 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 84.6 |
| 0d358e77-9f99-3961-8725-eaf57b853040 | -13.1796 | -45.4952 | 2024-09-26 15:06:20 | GOES-16 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 90.4 |
| fd61ce6c-fb20-3406-9300-520acf49f5eb | -13.7142 | -50.9927 | 2024-09-26 15:06:24 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 68.2 |
| decbd4b7-1760-3758-b98b-9c317dbcf36e | -14.0191 | -51.1668 | 2024-09-26 15:06:25 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 88.4 |
| cdeb5eb6-5796-3c0f-9bee-29c89505ac2b | -14.0195 | -51.1453 | 2024-09-26 15:06:25 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 88.1 |
| 2750bcdd-a3ee-3acb-9ead-c2e6b9499078 | -14.6131 | -45.5273 | 2024-09-26 15:06:28 | GOES-16 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 133.9 |
| 17a7c736-474a-384a-ac4a-ab0751fd4f4e | -18.5223 | -47.0952 | 2024-09-26 15:06:49 | GOES-16 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 99.7 |
| 72d34099-6d79-321b-8105-066779d70aa1 | -2.4018 | -51.2883 | 2024-09-26 15:15:20 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 63.4 |
| 9c0976f8-08f5-3ddf-9bdd-baf9c1fd84fe | -2.8611 | -51.6699 | 2024-09-26 15:15:23 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 255.4 |
| bd9bbc47-f1cc-30c3-9443-d9ed0e481aa9 | -3.5488 | -50.38 | 2024-09-26 15:15:27 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 77.6 |
| a1251f26-d3e4-326a-8071-b93b2f6d250e | -5.1843 | -49.2505 | 2024-09-26 15:15:36 | GOES-16 | NOVA IPIXUNA | PARÁ | Brasil | 1504976 | 15 | 33 | nan | nan | nan | Amazônia | 65.7 |
| 1b2bb8d2-c6c2-30ef-b733-2350b569cee6 | -5.1842 | -49.2718 | 2024-09-26 15:15:36 | GOES-16 | NOVA IPIXUNA | PARÁ | Brasil | 1504976 | 15 | 33 | nan | nan | nan | Amazônia | 86.7 |
| a3fe4aab-384b-3d9b-a494-9633d64b4280 | -6.7839 | -59.3245 | 2024-09-26 15:15:45 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 53.4 |
| 2889b934-4922-35d8-8d3f-e8f41755e544 | -6.7902 | -44.7296 | 2024-09-26 15:15:45 | GOES-16 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 78.1 |
| 0de47578-9454-372d-8c7e-08b6c4d2a2ee | -6.8224 | -59.0333 | 2024-09-26 15:15:46 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 64.1 |


[Clique aqui para ver as próximas entradas](README191.md)
