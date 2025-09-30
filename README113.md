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

## Dados Diários - Página 113

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8607bcc2-9d01-37a9-ae3c-f18143aa810f | -10.9586 | -46.5016 | 2025-09-30 13:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 109.2 |
| 834427ed-0d3c-3e1e-9e71-141580c591f0 | -18.2176 | -53.3177 | 2025-09-30 13:00:00 | GOES-19 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 202.3 |
| 43b8eef4-699a-308c-a9a0-264ae4163bde | -12.877 | -45.1974 | 2025-09-30 13:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 264.7 |
| f95c035d-188b-320d-b7cb-d03f402c47d4 | -8.2474 | -45.5037 | 2025-09-30 13:00:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 86.5 |
| bd25b4e8-23a3-37dd-9ec9-be2972d55369 | -13.8354 | -47.5076 | 2025-09-30 13:00:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 87.8 |
| 53e463e8-4bd9-36a1-92d4-0fb286d4391b | -6.523 | -45.207 | 2025-09-30 13:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 110.5 |
| 92c3ac83-7e35-34ea-b1ea-12347ef61d81 | -10.1045 | -47.7851 | 2025-09-30 13:00:00 | GOES-19 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 75.5 |
| 052eeb82-2117-310e-ab32-7d3c9119ccfb | -17.921 | -57.5952 | 2025-09-30 13:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 62.7 |
| 85f6b999-d412-322d-b298-440135d57fef | -9.0494 | -47.6332 | 2025-09-30 13:00:00 | GOES-19 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 75.6 |
| 8940837e-329c-3091-bbf3-3023f6f97d85 | -10.1847 | -44.917 | 2025-09-30 13:00:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 53.4 |
| e3eb45a3-17f1-3fac-bb8a-977214e42bb7 | -9.1246 | -47.6476 | 2025-09-30 13:00:00 | GOES-19 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 65.2 |
| 3eb875be-7d42-3514-85b0-6bc310367b0b | -6.4319 | -43.0707 | 2025-09-30 13:00:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 96.8 |
| c7a82eeb-dd3e-3ecd-abd4-6a3273190d0a | -8.6668 | -46.608 | 2025-09-30 13:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 171.1 |
| 25063383-845d-34ab-adb6-739de35951b7 | -14.5141 | -48.4299 | 2025-09-30 13:00:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 107.3 |
| b59e6564-7f4e-341f-8ec2-60594e5bf433 | -12.8967 | -45.1711 | 2025-09-30 13:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 179.1 |
| ce82d43c-871c-3be7-91d5-db074a7ce69f | -7.8353 | -46.9764 | 2025-09-30 13:00:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 68.2 |
| 1b60f67b-01d1-38f9-a3f2-d01d2de6ef8c | -7.835 | -46.9986 | 2025-09-30 13:00:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 180.8 |
| adda544f-f2b9-3d54-91b5-d6e3175fd334 | -6.504 | -45.2312 | 2025-09-30 13:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 112.1 |
| 3459900b-5d64-3ff0-b6fc-58629475c173 | -7.8188 | -46.7783 | 2025-09-30 13:00:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 257.3 |
| 4948639a-fb29-3a95-b4a2-909a029f0486 | -12.2153 | -47.8112 | 2025-09-30 13:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 70.4 |
| 322b83f9-7959-3cd8-9c41-a6d95289837a | -7.9191 | -44.6245 | 2025-09-30 13:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 122.3 |
| 389ac588-d8f1-3cf1-bf3e-9e35060280a8 | -10.0531 | -50.1978 | 2025-09-30 13:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 72.1 |
| de4bffdb-bc1d-3607-ba80-83e91bd8d91a | -9.0236 | -46.7052 | 2025-09-30 13:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 95.0 |
| 43c613b4-404f-36a2-8f0a-b4123aec8c7f | -7.8188 | -46.7783 | 2025-09-30 13:10:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 80.4 |
| a75d94b2-508e-34c0-af05-a6fa3acfbc70 | -12.2344 | -47.8086 | 2025-09-30 13:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 150.5 |
| bd3ff18f-e2c3-340d-a045-9f09b0e08816 | -12.9712 | -48.4158 | 2025-09-30 13:10:00 | GOES-19 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 110.9 |
| 696ff9ca-34bf-361e-8efe-a2def0817dfd | -6.0792 | -42.6537 | 2025-09-30 13:10:00 | GOES-19 | SÃO GONÇALO DO PIAUÍ | PIAUÍ | Brasil | 2209807 | 22 | 33 | nan | nan | nan | Caatinga | 71.1 |
| adcc3924-b619-36df-8c8c-008500da9735 | -10.8055 | -45.3637 | 2025-09-30 13:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 80.9 |
| b4a3a1b5-6846-3462-95bc-91b4ddebf59b | -10.1855 | -44.8709 | 2025-09-30 13:10:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 64.2 |
| e2895976-a266-3a92-a8b0-b2b4d1943327 | -13.8359 | -47.4851 | 2025-09-30 13:10:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 106.9 |
| 16d0ded4-9242-3349-b814-5b7a9d992adb | -8.2474 | -45.5037 | 2025-09-30 13:10:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 96.3 |
| 5e65a093-74e5-3dd1-9c98-45910190100f | -16.7575 | -51.3482 | 2025-09-30 13:10:00 | GOES-19 | PALESTINA DE GOIÁS | GOIÁS | Brasil | 5215652 | 52 | 33 | nan | nan | nan | Cerrado | 185.9 |
| f42e2a6f-1fb0-317b-9893-c4c71f4ff459 | -11.1546 | -54.126 | 2025-09-30 13:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 147.9 |
| d6a8f44a-0345-3568-ad3f-2bc014d7f46f | -14.697 | -45.2561 | 2025-09-30 13:10:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 149.5 |
| aa14e451-cf54-30c7-8753-871b7dd3ba8f | -17.921 | -57.5952 | 2025-09-30 13:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 89.3 |
| 22676980-3195-3d77-adc9-ee74110e1a29 | -6.4319 | -43.0707 | 2025-09-30 13:10:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 91.8 |
| 707f38a1-8b2d-328d-bd56-72d6ddc0dea1 | -8.8417 | -46.187 | 2025-09-30 13:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 72.1 |
| 24de1136-13ca-370f-b1a5-cf141a25d76e | -10.0342 | -50.1997 | 2025-09-30 13:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 87.1 |
| fc077969-ed37-3264-b627-949ee6a2adbb | -6.4131 | -43.0724 | 2025-09-30 13:10:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 84.4 |
| 31eaf763-84cb-30a7-be0e-5d2a1a212a76 | -15.2746 | -49.263 | 2025-09-30 13:10:00 | GOES-19 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 101.1 |
| cef9f8c5-4007-3864-b3ba-7eb0103d8d01 | -20.6818 | -50.2054 | 2025-09-30 13:10:00 | GOES-19 | FLOREAL | SÃO PAULO | Brasil | 3515905 | 35 | 33 | nan | nan | nan | Mata Atlântica | 305.4 |
| 216e4a97-bfb7-3065-b78e-fb20be0b75c1 | -17.9016 | -57.577 | 2025-09-30 13:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 62.1 |
| 2e2d7e07-174c-390d-90b9-c433340e71a2 | -10.6419 | -48.6021 | 2025-09-30 13:10:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 66.0 |
| a23df2f5-da03-3051-a679-679f0cdf3d88 | -7.9194 | -44.6016 | 2025-09-30 13:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 87.8 |
| 9e79f13c-f976-33f9-b3b7-796f3dd8a02d | -15.9273 | -46.2101 | 2025-09-30 13:10:00 | GOES-19 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 100.9 |
| 106221df-c087-3d7d-b00f-8c611f36c219 | -11.1735 | -54.1242 | 2025-09-30 13:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 112.0 |
| c42a3332-794d-373b-ae7c-a58289b4f22e | -14.5712 | -48.4877 | 2025-09-30 13:10:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 111.8 |
| 42a16032-891e-3bb3-9983-930b68f51900 | -10.0717 | -50.2173 | 2025-09-30 13:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 74.1 |
| 0f0871fe-3823-3e4a-a1b9-783eae44f65d | -10.9586 | -46.5016 | 2025-09-30 13:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 146.5 |
| 8f1fd313-7730-3bf4-8074-2a8bd53e01ae | -10.9395 | -46.504 | 2025-09-30 13:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 182.8 |
| 5dc93156-12a6-3189-8a08-54c62ff1fde4 | -13.8548 | -47.5046 | 2025-09-30 13:10:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 62.8 |
| d00a4260-68fb-3c15-98d9-cd7b73aa969b | -10.1847 | -44.917 | 2025-09-30 13:10:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 59.4 |
| 74bee780-040f-3337-95c9-10eee4d252ee | -7.0481 | -45.1856 | 2025-09-30 13:10:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 78.2 |
| d88b2c16-475a-3b80-a990-689f9842b626 | -7.835 | -46.9986 | 2025-09-30 13:10:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 213.5 |
| 5db15683-0437-35fa-9054-a7f75b942b1c | -11.1753 | -47.2358 | 2025-09-30 13:10:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 69.5 |
| 015fd864-d6a5-35f2-bc24-7dfb7b7721e2 | -15.9268 | -46.2334 | 2025-09-30 13:10:00 | GOES-19 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 92.9 |
| 6c2496e7-9182-3024-b690-30c28d42f13f | -11.1548 | -54.1054 | 2025-09-30 13:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 87.1 |
| 0332c8ee-97ac-3cfc-bdfd-8b4006c11637 | -7.8348 | -47.0207 | 2025-09-30 13:10:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 129.5 |
| 0c5d2256-8a32-3a06-a908-31879907067b | -8.2471 | -45.5263 | 2025-09-30 13:10:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 68.6 |
| 25456a64-db39-33f1-b8e6-68ed7c271dd1 | -12.7018 | -45.2947 | 2025-09-30 13:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 100.1 |
| 08303404-4005-37d3-9ccc-a6948f4026a6 | -11.1944 | -47.2334 | 2025-09-30 13:10:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 65.5 |
| 887235fe-b5d0-335b-a8d5-acd4ca373606 | -14.5141 | -48.4299 | 2025-09-30 13:10:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 93.5 |
| af6e7c90-21bf-33d6-b047-ef6d187e975a | -10.1851 | -44.8939 | 2025-09-30 13:10:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 172.0 |
| 18d9da92-c650-3b31-867f-2c239c7a5fc5 | -15.0725 | -45.0457 | 2025-09-30 13:10:00 | GOES-19 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 116.1 |
| f1a7a78e-bf6a-3933-bcd0-246fd80927c5 | -13.8354 | -47.5076 | 2025-09-30 13:10:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 222.5 |
| 81639c96-5ccc-3e7e-abcc-66181cb1d801 | -10.3058 | -48.2681 | 2025-09-30 13:10:00 | GOES-19 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 61.6 |
| fbeae635-95d4-3731-8629-08344a515b12 | -6.098 | -42.6521 | 2025-09-30 13:10:00 | GOES-19 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 89.0 |
| d550df8e-3d05-38c4-a275-284dc7e17dd2 | -7.8375 | -46.7766 | 2025-09-30 13:10:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 96.2 |
| 6526bfad-f251-3e46-a099-9c85d51076c6 | -8.8516 | -51.6998 | 2025-09-30 13:10:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 69.3 |
| e7916c79-031b-318e-9a41-0994065dc9c8 | -9.4007 | -54.6984 | 2025-09-30 13:10:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 78.7 |
| 373f09c5-303f-3089-9935-8ec3cec13280 | -7.8378 | -46.7544 | 2025-09-30 13:10:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 98.4 |
| d44c2794-9135-31b1-a287-510d3617eef4 | -14.5517 | -48.4907 | 2025-09-30 13:10:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 126.4 |
| 9349f6e2-fb8e-372f-9688-b7ba45044ead | -6.504 | -45.2312 | 2025-09-30 13:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 108.2 |
| 5c0aea3f-eb9e-3d01-8d1c-1a89c242282c | -7.8353 | -46.9764 | 2025-09-30 13:10:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 65.0 |
| b9d73aab-aa5d-3737-b6a4-2c2942926233 | -7.8696 | -47.2606 | 2025-09-30 13:10:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 105.1 |
| d3d6fb35-63e8-3456-bced-e68aa252621a | -15.2654 | -49.7273 | 2025-09-30 13:10:00 | GOES-19 | CERES | GOIÁS | Brasil | 5205406 | 52 | 33 | nan | nan | nan | Cerrado | 80.1 |
| 5d15ead3-66ff-37b9-825f-bd08e6941b05 | -12.952 | -48.4185 | 2025-09-30 13:10:00 | GOES-19 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 130.5 |
| 8ff4e1de-7615-3995-93af-8b94d969e4a9 | -14.7166 | -45.2525 | 2025-09-30 13:10:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 336.9 |
| fa08f316-afec-3ba6-8848-39c3af7fda38 | -10.1045 | -47.7851 | 2025-09-30 13:10:00 | GOES-19 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 76.0 |
| 8ee41c2f-46da-3120-a35a-3a039a3306e0 | -8.8229 | -46.189 | 2025-09-30 13:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 158.7 |
| 90efb3a8-7358-313c-b083-cde688a7c640 | -9.1248 | -47.6256 | 2025-09-30 13:10:00 | GOES-19 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 84.0 |
| a0b114e9-516b-3489-b749-d12681c05b7f | -18.2176 | -53.3177 | 2025-09-30 13:10:00 | GOES-19 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 152.0 |
| e8a2e41e-0fdc-33e7-a77e-ded758c17258 | -6.523 | -45.207 | 2025-09-30 13:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 363.0 |
| 25e4d633-523b-33ad-a3b0-7f3e8f6d4c05 | -6.2451 | -44.8884 | 2025-09-30 13:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 82.4 |
| 8cbea2bf-83ee-3958-a92f-4f13f786adeb | -14.5716 | -48.4653 | 2025-09-30 13:10:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 84.4 |
| 9352c9db-7fb6-398f-addc-d7da03c18c4e | -6.5227 | -45.2297 | 2025-09-30 13:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 463.7 |
| 3bcbeb5c-b95e-3b93-8ba9-fe2a6c807e8b | -18.218 | -53.2962 | 2025-09-30 13:10:00 | GOES-19 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 85.8 |
| 146df10a-8d49-3727-8695-975a45b6cd45 | -12.2348 | -47.7863 | 2025-09-30 13:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 65.0 |
| 73d4f116-6dd2-35b4-ad36-44b359078b9e | -10.6423 | -48.5802 | 2025-09-30 13:10:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 55.8 |
| 8630629f-a08a-3412-9fde-ff192fa959a3 | -14.6603 | -46.9663 | 2025-09-30 13:10:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 152.7 |
| 8dab66e7-d1f1-3553-9db2-cc9779b1bde8 | -9.0425 | -46.7032 | 2025-09-30 13:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 135.8 |
| 24537b1d-ba77-39d0-a900-3c4ec528df3b | -14.7367 | -45.2255 | 2025-09-30 13:10:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 127.1 |
| 4ac5df82-fd5e-3f5e-aec9-a9535a0e8fef | -12.9524 | -48.3963 | 2025-09-30 13:10:00 | GOES-19 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 84.8 |
| 51e78216-223b-368d-8a95-70c1658732bb | -12.7022 | -45.2715 | 2025-09-30 13:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 108.1 |
| 4be254a4-3587-3209-9f37-c73ac63e1d06 | -14.5323 | -48.4938 | 2025-09-30 13:10:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 90.7 |
| 368b059a-4b22-33a4-9fcf-830e99421243 | -14.5128 | -48.4968 | 2025-09-30 13:20:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 77.0 |
| bb18151f-cea9-30aa-a3d7-5425a10af731 | -9.7681 | -46.1519 | 2025-09-30 13:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 119.0 |
| 745e019c-b45d-3e90-b56a-e7d457afbeb7 | -10.1045 | -47.7851 | 2025-09-30 13:20:00 | GOES-19 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 115.9 |
| ddb628f5-74ef-3fe4-93e7-ed8195147405 | -12.7022 | -45.2715 | 2025-09-30 13:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 121.6 |
| af5edf82-a53f-310e-89b0-8fda3d9959c6 | -13.162 | -47.4309 | 2025-09-30 13:20:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 117.3 |


[Clique aqui para ver as próximas entradas](README114.md)
