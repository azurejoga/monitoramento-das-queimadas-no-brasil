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

## Dados Diários - Página 117

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0a3c3c9d-1f02-3e55-bdad-c51090faf4e7 | -4.0073 | -41.5154 | 2025-09-10 14:40:00 | GOES-19 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 92.5 |
| 3c50a3b9-011d-361e-a751-5dc1c6432137 | -11.4699 | -50.3676 | 2025-09-10 14:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 141.1 |
| a4ebc6ea-a2a7-3f10-85b7-d7facff99221 | -10.0155 | -51.7031 | 2025-09-10 14:40:00 | GOES-19 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 146.6 |
| e1ab7831-5c19-3e5a-9688-54c711993993 | -12.8405 | -52.9413 | 2025-09-10 14:40:00 | GOES-19 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 57.2 |
| e34e90f5-7502-34c6-99f9-eae53eb20c7b | -15.2881 | -53.7777 | 2025-09-10 14:40:00 | GOES-19 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 70.7 |
| 6d3c2b68-fd5c-30f9-8f12-7676ddec4ed6 | -10.6609 | -48.5999 | 2025-09-10 14:40:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 126.1 |
| 7bc92101-8e0e-3516-b7d6-52fea1f48911 | -14.5122 | -53.9576 | 2025-09-10 14:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 97.1 |
| 627bac27-b562-32d4-9e22-07fabba30d4d | -5.679 | -45.4512 | 2025-09-10 14:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 93.1 |
| 5717a04f-e1f9-3016-8048-eaf458c3e4b4 | -7.7439 | -50.316 | 2025-09-10 14:40:00 | GOES-19 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 76.5 |
| 3ce906dc-cd60-3bdf-b1c4-4d73c24675ba | -12.1885 | -50.6482 | 2025-09-10 14:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 88.8 |
| d749c818-c05d-35fa-88ea-8d4e79dd8352 | -9.8646 | -50.1951 | 2025-09-10 14:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 93.9 |
| fa6646b5-cdab-3d2f-ac18-301b927c1cbe | -16.5099 | -55.1459 | 2025-09-10 14:40:00 | GOES-19 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 49.1 |
| 7054d658-f7ad-3711-a572-84459988ddb9 | -9.0768 | -46.9668 | 2025-09-10 14:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 176.5 |
| 307361f8-8ac8-3a4c-b745-79fa5c076038 | -8.49 | -45.6826 | 2025-09-10 14:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 236.1 |
| e3cf4667-1279-3022-8972-de205f7befa4 | -13.1364 | -54.9376 | 2025-09-10 14:40:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 89.6 |
| 6a48a941-b4f0-3f4f-8010-68c7d21961ac | -9.7011 | -46.877 | 2025-09-10 14:40:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 86.1 |
| 62cf55b2-6480-3912-aee7-df39c822ca44 | -15.1569 | -52.4013 | 2025-09-10 14:40:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 125.2 |
| 98b4d6ea-b538-34a5-882e-80d335819f8d | -5.8582 | -44.2088 | 2025-09-10 14:40:00 | GOES-19 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 121.9 |
| 25dadfc3-e058-38fa-9120-59fed488e35c | -5.5702 | -42.9062 | 2025-09-10 14:40:00 | GOES-19 | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | 103.5 |
| 0571b056-2957-313e-8181-cf48bfa44afc | -6.3806 | -44.4434 | 2025-09-10 14:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 102.1 |
| 94ec6e6d-cd07-34b2-9624-14ee9ce7486e | -14.5609 | -52.1836 | 2025-09-10 14:40:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 157.0 |
| 47f557b4-c251-349b-8753-b39ea0817e4e | -7.8812 | -46.2374 | 2025-09-10 14:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 98.2 |
| 816b3b8d-1b66-3334-87c2-d31161173e1e | -9.6821 | -46.8791 | 2025-09-10 14:40:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 170.3 |
| ac53cd01-57de-34b3-af31-2c659aa218be | -6.8521 | -47.9143 | 2025-09-10 14:40:00 | GOES-19 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 212.7 |
| 9257058c-1589-3903-9d23-335c46b5dbbb | -16.5117 | -55.0415 | 2025-09-10 14:40:00 | GOES-19 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 198.6 |
| 4ced6fbd-823e-364b-978d-5a5fcda104c5 | -7.8998 | -46.2581 | 2025-09-10 14:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 81.8 |
| 7e6a7eb4-8107-332e-93dc-d0877a6fcc55 | -9.5912 | -48.0169 | 2025-09-10 14:40:00 | GOES-19 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 150.4 |
| 4ef898c5-ccd3-3002-9e64-91ebe7ec9985 | -14.4654 | -53.2731 | 2025-09-10 14:40:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 84.4 |
| ce6b3599-1f00-3564-bd72-efc0383a13ea | -11.2834 | -46.4365 | 2025-09-10 14:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 117.1 |
| 35518cc9-9f2c-3f78-a3bd-d58147179626 | -9.6098 | -48.0368 | 2025-09-10 14:40:00 | GOES-19 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 103.9 |
| f6043d80-2f8f-39f0-9485-ce4c52636411 | -16.5298 | -55.1225 | 2025-09-10 14:40:00 | GOES-19 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 126.4 |
| cfda3090-8707-386c-8719-ba14f928b64c | -11.4657 | -43.6195 | 2025-09-10 14:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 617.6 |
| ca96b3ce-aa19-3ec2-80b4-0c26b8439c8a | -7.445 | -44.945 | 2025-09-10 14:40:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 152.5 |
| c2283d9e-bfed-386b-bb4e-b127b66057f1 | -12.5479 | -45.2957 | 2025-09-10 14:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 104.1 |
| d184ba7b-dd7a-3024-be05-e746ae555392 | -6.8261 | -44.8863 | 2025-09-10 14:40:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 151.1 |
| bbbf6b33-0ba9-36bf-a120-ad11b0860345 | -16.5309 | -55.0599 | 2025-09-10 14:40:00 | GOES-19 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 109.4 |
| b05986e2-e611-37ab-a947-d9a8f5d081ca | -14.8877 | -55.8567 | 2025-09-10 14:40:00 | GOES-19 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 69.6 |
| 5e3b7236-5dfc-30e9-9bc7-36730deb4c75 | -15.2877 | -53.7987 | 2025-09-10 14:40:00 | GOES-19 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 71.8 |
| 452feeda-a29f-3d50-95f5-3c83c0c2f818 | -9.3437 | -46.7603 | 2025-09-10 14:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 178.0 |
| e70e3850-82a8-3550-bab0-57d44066d759 | -11.9535 | -51.081 | 2025-09-10 14:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 139.8 |
| c72c516b-a345-36ae-97d7-760b43789ffb | -13.1176 | -54.9191 | 2025-09-10 14:40:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 96.3 |
| 60301fd8-0f6b-38d5-9567-07f1b646a2d6 | -14.5285 | -40.7451 | 2025-09-10 14:40:00 | GOES-19 | ANAGÉ | BAHIA | Brasil | 2901205 | 29 | 33 | nan | nan | nan | Caatinga | 198.7 |
| ae545c0c-6c9b-3bd5-a563-7b382f6066c8 | -12.1993 | -53.8611 | 2025-09-10 14:40:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 78.5 |
| 96c04d6c-5cdf-3991-904a-46d731ab0a71 | -11.7602 | -46.4621 | 2025-09-10 14:40:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 245.8 |
| 4041f01b-ed3c-3e25-b328-f904bffe7e62 | -12.5286 | -45.2987 | 2025-09-10 14:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 126.2 |
| 0b928404-097c-3adf-8523-e3ccea5689d9 | -9.8838 | -50.1719 | 2025-09-10 14:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 550.3 |
| 079950ab-381a-3f03-8b9e-cee87cc277e7 | -15.8201 | -52.2659 | 2025-09-10 14:40:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 67.6 |
| 756ce30d-3807-3eab-ab58-83887c19b63f | -11.2007 | -54.9992 | 2025-09-10 14:40:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 96.1 |
| 49305b47-9f38-37db-aebc-0ab89a700bf0 | -5.3761 | -45.9653 | 2025-09-10 14:40:00 | GOES-19 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 67.9 |
| e6a98ac6-39dd-31bd-8fe9-cd5bd5cb6018 | -6.7299 | -45.122 | 2025-09-10 14:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 82.5 |
| d2b9ccfe-d840-38e1-9102-0f14a1b3ab22 | -4.1193 | -41.5808 | 2025-09-10 14:40:00 | GOES-19 | BRASILEIRA | PIAUÍ | Brasil | 2201960 | 22 | 33 | nan | nan | nan | Caatinga | 112.5 |
| e6d5756e-3cf8-3313-9058-ccb92d7e6415 | -14.5125 | -53.9367 | 2025-09-10 14:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 147.7 |
| a9aae396-bde3-3452-a3cf-fe3d7e2eb067 | -9.0714 | -50.4818 | 2025-09-10 14:40:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 73.1 |
| 9412f5f7-e7cf-3f57-81cd-a7d8c48dc587 | -11.4705 | -50.3247 | 2025-09-10 14:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 176.5 |
| 0c272cb6-50f7-3ebb-950a-abd61ca23748 | -9.0756 | -47.0558 | 2025-09-10 14:40:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 80.4 |
| b2bd1b18-714a-38e3-9c0b-194278083466 | -6.7503 | -44.9611 | 2025-09-10 14:40:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 106.2 |
| 8ad9e881-78bf-30aa-b17f-a2efc43d0d27 | -4.7345 | -44.4685 | 2025-09-10 14:40:00 | GOES-19 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 65.9 |
| 2616054c-7aa7-364e-b2dc-b2773628fa61 | -6.204 | -43.3241 | 2025-09-10 14:40:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 110.5 |
| 155abbe7-1c24-38fe-83cd-f0863466a31a | -14.5612 | -52.1623 | 2025-09-10 14:40:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 87.1 |
| f6b4e179-5916-387f-a040-9ac1db6b2fd3 | -6.8895 | -47.9115 | 2025-09-10 14:40:00 | GOES-19 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 228.0 |
| 2be2af30-6d2f-3923-af38-b191f78c5aeb | -10.6606 | -48.6218 | 2025-09-10 14:40:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 81.8 |
| 83710539-3a8a-3eb8-8a88-b5a46267db63 | -11.4702 | -50.3461 | 2025-09-10 14:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 386.8 |
| 402423d3-762b-3a3e-8fb1-48d138628595 | -9.7777 | -51.1366 | 2025-09-10 14:40:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 207.0 |
| eb1558ec-6864-3e36-99a3-17f17bafa90c | -13.8015 | -46.2892 | 2025-09-10 14:40:00 | GOES-19 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 103.4 |
| 6541eb31-28f0-394f-b909-708d6440d8f0 | -14.3882 | -53.2826 | 2025-09-10 14:40:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 67.4 |
| 291da8e9-c560-3f29-9a9e-506cf5368435 | -12.1803 | -53.863 | 2025-09-10 14:40:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 107.0 |
| 3e0bbed8-3ac7-3351-bfb0-43f2b3acd4d3 | -6.1896 | -41.0398 | 2025-09-10 14:40:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 168.1 |
| fc645154-34e1-3583-b584-1db67d12f2fb | -5.6788 | -43.3425 | 2025-09-10 14:40:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 82.3 |
| 89cd8314-9f58-3e34-be9f-3e40c6ea81c0 | -5.5888 | -42.9282 | 2025-09-10 14:40:00 | GOES-19 | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | 125.8 |
| 717ceb96-292b-3b06-99d2-69de38dc7672 | -10.016 | -51.6611 | 2025-09-10 14:40:00 | GOES-19 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 109.6 |


