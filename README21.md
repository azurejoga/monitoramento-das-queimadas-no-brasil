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

## Dados Diários - Página 21

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 95cbb4cd-6e81-3f1c-b9f2-690381589824 | -5.9788 | -45.3621 | 2024-10-01 00:55:40 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 67.4 |
| 874212a4-448d-377f-8cae-a9a35a9d5f3b | -5.9786 | -45.3847 | 2024-10-01 00:55:40 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 55.2 |
| 5328736d-f74b-30c0-bb6c-6ae411d88320 | -6.2524 | -44.132 | 2024-10-01 00:55:41 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 82.6 |
| 9c29fff0-1797-39ca-9c83-7e3f9048aad6 | -6.6953 | -43.0474 | 2024-10-01 00:55:43 | GOES-16 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 62.6 |
| 4118179d-a7fd-387e-81b1-0ea3c5de5523 | -6.9671 | -47.6215 | 2024-10-01 00:55:45 | GOES-16 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 49.3 |
| cb9087a7-b342-359e-82a1-85f6d4c8080f | -8.6706 | -49.4296 | 2024-10-01 00:55:55 | GOES-16 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 73.2 |
| 0f16dbdd-215a-353a-9a75-d6258a5b96e3 | -10.9429 | -50.0833 | 2024-10-01 00:56:08 | GOES-16 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 85.4 |
| 3bc55c47-5bde-365b-b93c-57dbc3cf561b | -11.1253 | -45.6178 | 2024-10-01 00:56:08 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 73.7 |
| c62b25b7-12ae-3a43-9152-7070462cdae5 | -11.1249 | -45.6407 | 2024-10-01 00:56:08 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 88.9 |
| 2151b957-2bd5-358f-a0de-65219c34b57e | -11.1054 | -45.6662 | 2024-10-01 00:56:08 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 34.2 |
| 8904c9a7-2d02-330c-b94a-59b3e255fd3d | -11.1051 | -45.689 | 2024-10-01 00:56:08 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 32.3 |
| ea5748a5-f5d7-3317-98de-3c8698cd9a81 | -11.9842 | -50.3079 | 2024-10-01 00:56:13 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 81.9 |
| f45cd87d-26cd-37ad-8914-9a4338212679 | -12.0224 | -50.3034 | 2024-10-01 00:56:14 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 64.5 |
| 001315eb-2713-3fbd-880a-42449dc1c604 | -12.0033 | -50.3057 | 2024-10-01 00:56:14 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 163.1 |
| 2e23488a-68e5-3c9f-a292-3321b60d8b06 | -12.0029 | -50.3272 | 2024-10-01 00:56:14 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 96.6 |
| 21c7439a-f9ea-36e1-a9a3-6586fef7ad9c | -12.5848 | -53.4899 | 2024-10-01 00:56:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 85.6 |
| a05bd160-70de-3966-a88c-45bc91f6410a | -12.5135 | -53.1441 | 2024-10-01 00:56:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 86.8 |
| 142b92ce-3b93-37f6-a3eb-bc7bc045a9de | -12.6039 | -53.4879 | 2024-10-01 00:56:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 129.1 |
| e2d1bfdf-f5ad-31ea-9596-ed34d3f506e0 | -12.5132 | -53.165 | 2024-10-01 00:56:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 90.7 |
| 67ea0aa5-001e-3cc9-9141-d33a05509d77 | -12.4945 | -53.1462 | 2024-10-01 00:56:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 80.3 |
| ccc6d370-f0bb-3c65-8dd3-3c6ad3ce95cd | -12.4942 | -53.167 | 2024-10-01 00:56:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 94.2 |
| 3c42c7ac-d1f4-3fa3-8fa1-153bec835f14 | -12.9796 | -51.3427 | 2024-10-01 00:56:19 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 253.5 |
| a65a7bb0-5dd6-3a8c-b6a4-942c3fafd335 | -12.9793 | -51.364 | 2024-10-01 00:56:19 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 275.7 |
| 7a7f1f6f-8a07-3dd5-ad18-a41863d71f5d | -12.9605 | -51.345 | 2024-10-01 00:56:19 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 171.3 |
| 656c8e68-66f8-304f-be52-ada0674a9285 | -12.9601 | -51.3664 | 2024-10-01 00:56:19 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 159.6 |
| a278a5af-f096-3f59-a348-27ec48aac24e | -12.9228 | -51.307 | 2024-10-01 00:56:19 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 130.6 |
| 023bbd90-5b73-35d9-87dd-ad7f7fc879df | -12.904 | -51.288 | 2024-10-01 00:56:19 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 78.2 |
| 36ad42ce-7a1e-3bc6-af38-07947e2b6361 | -12.9037 | -51.3094 | 2024-10-01 00:56:19 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 189.5 |
| c047d26b-3f89-30f1-9000-381a62ab3e54 | -13.2493 | -51.2452 | 2024-10-01 00:56:21 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 74.0 |
| 43f09354-6dfc-3999-a2fe-45ec40cb4cf1 | -13.5961 | -51.1582 | 2024-10-01 00:56:22 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 66.6 |
| 6bff9b88-cb3b-301b-9882-7d81ca7f663b | -13.5768 | -51.1607 | 2024-10-01 00:56:22 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 95.2 |
| c6bc11fa-f57a-3579-830f-4ae2a5f1b6a3 | -14.7406 | -48.7498 | 2024-10-01 00:56:28 | GOES-16 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 88.5 |
| ce41a8e1-b324-3cd7-8c4d-4313911486d8 | -14.7211 | -48.7529 | 2024-10-01 00:56:28 | GOES-16 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 63.7 |
| f0f5733a-9db5-373d-93e6-29c5f62ad2ad | -15.6179 | -57.4491 | 2024-10-01 00:56:34 | GOES-16 | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 70.6 |
| f334ad7b-712d-31f9-bfe8-a23ae761972d | -16.6263 | -55.1934 | 2024-10-01 00:56:39 | GOES-16 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 167.1 |
| d0683ea7-261e-3d2b-bb27-3e06ff15a575 | -16.6259 | -55.2142 | 2024-10-01 00:56:39 | GOES-16 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 87.9 |
| 3b33117c-25f9-3314-a54e-b62086c4c09d | -16.5134 | -57.3305 | 2024-10-01 00:56:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 92.2 |
| 418530f2-373b-324b-8128-b6856af2127b | -16.6459 | -55.1908 | 2024-10-01 00:56:39 | GOES-16 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 111.8 |
| c29b57ad-a84a-33bf-9ffe-e94a5ff654df | -16.6455 | -55.2117 | 2024-10-01 00:56:39 | GOES-16 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 99.1 |
| c1553787-d8c7-3f8d-9255-2c2ad231697b | -16.5131 | -57.3509 | 2024-10-01 00:56:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 82.4 |
| c39b1bb2-4443-3646-a3fb-5a31b34bd527 | -16.4939 | -57.3327 | 2024-10-01 00:56:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 134.6 |
| ebe06a59-1017-37d0-8c46-fbe29d7bb299 | -16.4935 | -57.3531 | 2024-10-01 00:56:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 116.1 |
| 61caa744-52cc-3935-957d-52bcd4ea920d | -16.4743 | -57.3349 | 2024-10-01 00:56:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 118.6 |
| c6bd935a-6037-32c0-abdc-9f3a9beaea7f | -16.474 | -57.3553 | 2024-10-01 00:56:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 111.8 |
| e38a122f-8753-3c25-b607-49b2aca08bc7 | -16.8103 | -55.8762 | 2024-10-01 00:56:40 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 69.7 |
| 6818b191-48c0-3f90-9ed1-d0f6e2e97636 | -16.9919 | -57.9696 | 2024-10-01 00:56:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 48.9 |
| 0c8a237a-9ff5-3565-868b-41cff389ecd6 | -18.5423 | -43.4683 | 2024-10-01 00:56:48 | GOES-16 | SERRO | MINAS GERAIS | Brasil | 3167103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 78.0 |
| b37293ea-e6fa-3212-a86d-8d77089f26fc | -18.6011 | -53.0412 | 2024-10-01 00:56:50 | GOES-16 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 71.8 |
| 035503a5-dd9e-3892-90e4-ca8a6f3baed1 | -18.6006 | -53.0628 | 2024-10-01 00:56:50 | GOES-16 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 69.1 |
| 18226bc7-fd19-359e-8fd1-382b82a5b127 | -18.9253 | -47.0305 | 2024-10-01 00:56:51 | GOES-16 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 50.8 |
| 17ab0869-8682-3745-b3d3-aaff82f704d6 | -19.1329 | -57.4628 | 2024-10-01 00:56:53 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 169.4 |
| cd65bd4f-284e-35ef-a9b0-8cf794243dd8 | -19.1325 | -57.4836 | 2024-10-01 00:56:53 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 118.2 |
| abd9de31-efdd-317c-8f08-5efce1f602d7 | -19.1129 | -57.4655 | 2024-10-01 00:56:53 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 108.4 |
| b1b0df20-09d8-3afa-ba6a-fee0ce9ff61e | -19.1125 | -57.4862 | 2024-10-01 00:56:53 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 90.2 |
| 93374526-8725-3587-9e60-e85a48cd07dc | -21.7122 | -54.8253 | 2024-10-01 00:57:06 | GOES-16 | RIO BRILHANTE | MATO GROSSO DO SUL | Brasil | 5007208 | 50 | 33 | nan | nan | nan | Cerrado | 75.2 |
| 8bd20d11-e23b-30cf-af22-7cfbd5ba92b1 | -21.7117 | -54.847 | 2024-10-01 00:57:06 | GOES-16 | RIO BRILHANTE | MATO GROSSO DO SUL | Brasil | 5007208 | 50 | 33 | nan | nan | nan | Cerrado | 81.9 |
| 80b86f8c-2edb-3651-a453-c5ef65fdf0a0 | -21.6917 | -54.8288 | 2024-10-01 00:57:06 | GOES-16 | RIO BRILHANTE | MATO GROSSO DO SUL | Brasil | 5007208 | 50 | 33 | nan | nan | nan | Cerrado | 109.8 |
| 7157d1ad-be06-34ee-b51f-6f9e38f55f21 | -21.6912 | -54.8506 | 2024-10-01 00:57:06 | GOES-16 | RIO BRILHANTE | MATO GROSSO DO SUL | Brasil | 5007208 | 50 | 33 | nan | nan | nan | Cerrado | 129.1 |
| 9fcdb5da-324b-39ea-b6f1-7ef216dbe660 | -22.1242 | -48.5469 | 2024-10-01 00:57:07 | GOES-16 | BOCAINA | SÃO PAULO | Brasil | 3506805 | 35 | 33 | nan | nan | nan | Cerrado | 110.6 |
| 74ad8ada-13d8-3a40-a610-20ca3686a4be | -22.3922 | -49.2961 | 2024-10-01 00:57:09 | GOES-16 | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 87.3 |
| e9889643-02b4-3fe1-aabc-a99f48a39e5d | -22.3916 | -49.3194 | 2024-10-01 00:57:09 | GOES-16 | CABRÁLIA PAULISTA | SÃO PAULO | Brasil | 3508306 | 35 | 33 | nan | nan | nan | Mata Atlântica | 73.2 |
| 901c794d-90e5-3969-a59d-76d7675cf3d0 | -22.3713 | -49.3011 | 2024-10-01 00:57:09 | GOES-16 | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 148.9 |
| 26786a47-7f37-32b0-8bf9-7ec2758bad7b | -22.3707 | -49.3244 | 2024-10-01 00:57:09 | GOES-16 | DUARTINA | SÃO PAULO | Brasil | 3514502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 188.0 |
| 172dbb96-3b27-352d-b012-bebbea11b578 | -23.0793 | -45.3951 | 2024-10-01 00:57:12 | GOES-16 | TAUBATÉ | SÃO PAULO | Brasil | 3554102 | 35 | 33 | nan | nan | nan | Mata Atlântica | 87.9 |
| 9a4428c2-2649-332d-a155-78502bafbc9c | -22.34 | -49.32 | 2024-10-01 01:03:16 | MSG-03 | DUARTINA | SÃO PAULO | Brasil | 3514502 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 02964039-2782-3882-920f-f0eab175bcaf | -21.56 | -47.88 | 2024-10-01 01:03:22 | MSG-03 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 89fb6823-bf3d-3e72-b7cf-fdcebb92aa13 | -21.56 | -47.83 | 2024-10-01 01:03:22 | MSG-03 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 1b75bb6c-8b0a-3631-b2fe-03971e958755 | -21.56 | -47.77 | 2024-10-01 01:03:22 | MSG-03 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 4a1751de-16c6-310b-9501-ca675067b366 | -21.59 | -47.84 | 2024-10-01 01:03:22 | MSG-03 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| a55078b1-e675-304b-9bec-6a86c2de7472 | -17.13 | -56.21 | 2024-10-01 01:03:48 | MSG-03 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 559b3b13-4a56-3073-9f36-1e444a2247b6 | -17.13 | -56.14 | 2024-10-01 01:03:48 | MSG-03 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| ca100c18-aa33-37b6-b462-c2825d0cbae9 | -17.16 | -56.23 | 2024-10-01 01:03:48 | MSG-03 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| a70f5813-c4ef-3ce4-9efe-86c8ce82c6f2 | -17.16 | -56.16 | 2024-10-01 01:03:48 | MSG-03 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 50abda35-4e1a-3a65-91a5-7dbe3c164985 | -16.64 | -57.26 | 2024-10-01 01:03:51 | MSG-03 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 64627d3a-d1ec-35df-b458-5c37d37dd91d | -12.96 | -51.37 | 2024-10-01 01:04:12 | MSG-03 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 06714ba4-5724-3436-84f2-315e88fbe42c | -12.95 | -51.31 | 2024-10-01 01:04:12 | MSG-03 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 7e4f5570-c87f-3068-b5a1-b12de869f3a2 | -12.95 | -51.25 | 2024-10-01 01:04:12 | MSG-03 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 57412693-8b3b-3e11-bd58-fdcbfff165a8 | -12.98 | -51.32 | 2024-10-01 01:04:12 | MSG-03 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 318999ae-dbb6-3c9b-bc63-7a8112ef9d3b | -2.82 | -50.78 | 2024-10-01 01:05:12 | MSG-03 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 56dd7999-7a6a-3c23-8abd-d354fdc7bf92 | -2.82 | -50.72 | 2024-10-01 01:05:12 | MSG-03 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fffe855b-5fc2-3f1a-a273-2497cb37d498 | -2.85 | -50.78 | 2024-10-01 01:05:12 | MSG-03 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b457be5a-73dc-3f34-8588-9cb1a68f9125 | -2.85 | -50.72 | 2024-10-01 01:05:12 | MSG-03 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f7a7e5da-ac7a-3bce-b062-bfc10f257b2e | -2.85 | -50.67 | 2024-10-01 01:05:12 | MSG-03 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 10bcc105-63b6-370f-ae2c-4b89c55add4f | -2.88 | -50.78 | 2024-10-01 01:05:12 | MSG-03 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8a4c427a-e6d3-39a2-91b6-0ffb27ff1c78 | -2.88 | -50.73 | 2024-10-01 01:05:12 | MSG-03 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bce0e369-bd36-3098-a962-94db74616e6e | -2.88 | -50.67 | 2024-10-01 01:05:12 | MSG-03 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9decfd1d-ce51-355b-8266-673dda7ee8a0 | -2.91 | -50.73 | 2024-10-01 01:05:12 | MSG-03 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 69db3598-7814-3d13-8ce5-c937abecb95e | -3.0282 | -51.3345 | 2024-10-01 01:05:23 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 47.7 |
| bd1fbcab-bd18-3e32-a584-ae4f1e60f036 | -4.6987 | -49.8062 | 2024-10-01 01:05:32 | GOES-16 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 61.3 |
| 2cae9279-7ad6-3670-b516-f507b836d74a | -5.7715 | -45.5574 | 2024-10-01 01:05:38 | GOES-16 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 53.5 |
| 9b90e3b5-bbaf-3c17-8403-712f4e9047c6 | -5.9788 | -45.3621 | 2024-10-01 01:05:40 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 64.2 |
| 4af94ebd-2f8e-3932-8752-2259d7ece7ac | -5.9786 | -45.3847 | 2024-10-01 01:05:40 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 61.6 |
| 0b5d9647-5631-3936-bf00-6d9615ad5d99 | -6.2524 | -44.132 | 2024-10-01 01:05:41 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 73.3 |
| 9c014b4b-8718-38da-befa-ff6b68268fd7 | -6.9858 | -47.6201 | 2024-10-01 01:05:45 | GOES-16 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 52.1 |
| b4232a5c-90fc-3085-a80f-629485f0c2ba | -6.9671 | -47.6215 | 2024-10-01 01:05:45 | GOES-16 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 43.7 |
| 03d14ce3-6e71-3b7d-9bd6-7d2f67b8bc84 | -10.5743 | -48.0399 | 2024-10-01 01:06:05 | GOES-16 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 65.1 |
| 3bdf911a-169e-35cc-99f7-14f50107db7f | -11.6744 | -64.9793 | 2024-10-01 01:06:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 66.4 |
| 99c7cb08-0b76-3ae4-be4d-9e042b33b700 | -11.6743 | -64.9983 | 2024-10-01 01:06:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 103.3 |
| ebbde42e-0c4a-3134-9df8-be30ff102d64 | -11.6556 | -64.9802 | 2024-10-01 01:06:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 136.4 |
| 750125ed-c49f-3114-b633-5de93a454982 | -11.6555 | -64.9991 | 2024-10-01 01:06:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 240.3 |


[Clique aqui para ver as próximas entradas](README22.md)
