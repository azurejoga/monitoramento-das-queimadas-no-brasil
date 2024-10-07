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

## Dados Diários - Página 32

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ecf6b836-88e7-349f-8a97-4cab0794a3d7 | -18.4722 | -53.4919 | 2024-10-07 01:56:49 | GOES-16 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 54.1 |
| 3e07b87d-b3f9-3eb4-8dc9-fa60e585c487 | -18.659 | -57.2552 | 2024-10-07 01:56:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 78.5 |
| cd505795-c790-3b8e-bf98-2e5f924041a7 | -19.8112 | -42.36 | 2024-10-07 01:56:55 | GOES-16 | CÓRREGO NOVO | MINAS GERAIS | Brasil | 3120003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 77.4 |
| e61659c2-1e16-32a1-ade7-225a5b84e5eb | -19.831 | -42.3796 | 2024-10-07 01:56:55 | GOES-16 | CÓRREGO NOVO | MINAS GERAIS | Brasil | 3120003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 79.5 |
| a3f3718f-1def-330a-846f-755dad9d71a3 | -19.8318 | -42.3542 | 2024-10-07 01:56:55 | GOES-16 | BOM JESUS DO GALHO | MINAS GERAIS | Brasil | 3107802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 124.3 |
| 26f59ffa-9e91-3f23-be65-e231ea14d58c | -20.1019 | -49.0791 | 2024-10-07 01:56:57 | GOES-16 | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | 97.0 |
| 54a6016b-db5b-30ad-ba7e-5d8cfbf67135 | -20.1026 | -49.0562 | 2024-10-07 01:56:57 | GOES-16 | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | 182.0 |
| 78aa7e08-4229-3ad5-85c6-ae6cec05f90e | -20.1223 | -49.0748 | 2024-10-07 01:56:57 | GOES-16 | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | 179.4 |
| 1d1b277f-5f75-3039-8645-4becde3fb475 | -20.1229 | -49.0518 | 2024-10-07 01:56:57 | GOES-16 | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | 308.6 |
| d69f57e3-3d3d-3262-bcbd-08aeb56156dc | -20.1433 | -49.0474 | 2024-10-07 01:56:58 | GOES-16 | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | 83.7 |
| 39c5b305-ea55-3327-8a03-e4c57408d786 | -20.4449 | -47.6875 | 2024-10-07 01:56:59 | GOES-16 | ITUVERAVA | SÃO PAULO | Brasil | 3524105 | 35 | 33 | nan | nan | nan | Cerrado | 79.6 |
| 0821aded-ee9b-389c-b4ed-29cd8c8153b5 | -20.4456 | -47.664 | 2024-10-07 01:56:59 | GOES-16 | ITUVERAVA | SÃO PAULO | Brasil | 3524105 | 35 | 33 | nan | nan | nan | Cerrado | 123.9 |
| 2076fe24-ca9a-3642-a890-fe832a100c44 | -20.4655 | -47.6827 | 2024-10-07 01:56:59 | GOES-16 | GUARÁ | SÃO PAULO | Brasil | 3517703 | 35 | 33 | nan | nan | nan | Cerrado | 174.9 |
| a85f703d-2fca-3fb1-900e-fc6862f82c8c | -20.4661 | -47.6592 | 2024-10-07 01:56:59 | GOES-16 | GUARÁ | SÃO PAULO | Brasil | 3517703 | 35 | 33 | nan | nan | nan | Cerrado | 356.4 |
| 98387c68-6f57-3421-a4c9-e797863f7790 | -20.4866 | -47.6544 | 2024-10-07 01:56:59 | GOES-16 | GUARÁ | SÃO PAULO | Brasil | 3517703 | 35 | 33 | nan | nan | nan | Cerrado | 125.4 |
| faa503b3-b74e-3cb6-b4cc-26507042dc22 | -20.5848 | -48.5137 | 2024-10-07 01:57:00 | GOES-16 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 295.1 |
| 1004918a-39a2-3d51-9a00-0453cce098b9 | -20.5855 | -48.4904 | 2024-10-07 01:57:00 | GOES-16 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 580.0 |
| e3bad92d-dbd6-316e-9f9e-b5e737161a3d | -20.6053 | -48.509 | 2024-10-07 01:57:00 | GOES-16 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 258.9 |
| d8607626-010b-353f-9137-598d0033e31c | -20.606 | -48.4858 | 2024-10-07 01:57:00 | GOES-16 | JABORANDI | SÃO PAULO | Brasil | 3524204 | 35 | 33 | nan | nan | nan | Cerrado | 571.3 |
| b0ab90ef-36da-35fd-b8d1-1f518f97c095 | -21.0712 | -47.2331 | 2024-10-07 01:57:02 | GOES-16 | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | 122.5 |
| 313e8443-1fb3-36ef-9690-58da7ca3e49f | -21.0919 | -47.228 | 2024-10-07 01:57:02 | GOES-16 | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | 85.9 |
| d2ff2b4e-c7f3-3ac3-b4a7-97baf2fe82b7 | -21.5843 | -47.9536 | 2024-10-07 01:57:05 | GOES-16 | GUATAPARÁ | SÃO PAULO | Brasil | 3518859 | 35 | 33 | nan | nan | nan | Cerrado | 109.1 |
| c02ce2e1-4975-3c16-9cdd-1b0b049b8459 | -21.605 | -47.9485 | 2024-10-07 01:57:05 | GOES-16 | RINCÃO | SÃO PAULO | Brasil | 3543709 | 35 | 33 | nan | nan | nan | Cerrado | 78.8 |
| 46def8f5-563a-3600-8f2d-bf1de54a5c54 | -21.6529 | -47.7255 | 2024-10-07 01:57:05 | GOES-16 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 78.2 |
| 0573bf3a-97d4-3bef-b8c0-9fd50522b5c3 | -21.56 | -47.77 | 2024-10-07 02:03:21 | MSG-03 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 045bf584-275a-300f-96ae-b2b91e07ee43 | -21.55 | -47.72 | 2024-10-07 02:03:21 | MSG-03 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 92f351df-ef1d-3d14-8bf6-908cdcf4736a | -21.59 | -47.73 | 2024-10-07 02:03:21 | MSG-03 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 3933423f-28a8-348b-bfb4-0066614cb036 | -20.57 | -48.48 | 2024-10-07 02:03:26 | MSG-03 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 24538d8b-42d1-3c5c-bb67-8ae91f2089db | -20.61 | -48.55 | 2024-10-07 02:03:26 | MSG-03 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 247fa166-3c0f-3db9-a01a-f3842687c281 | -20.61 | -48.49 | 2024-10-07 02:03:26 | MSG-03 | JABORANDI | SÃO PAULO | Brasil | 3524204 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| a755699c-8a63-3e19-921a-19777a9fb04c | -20.44 | -47.66 | 2024-10-07 02:03:26 | MSG-03 | ITUVERAVA | SÃO PAULO | Brasil | 3524105 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| f51d228d-2090-34f2-bb00-102604318f60 | -20.47 | -47.67 | 2024-10-07 02:03:26 | MSG-03 | GUARÁ | SÃO PAULO | Brasil | 3517703 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 7a03647e-8b1c-3865-870c-ac116448c1bb | -20.58 | -48.53 | 2024-10-07 02:03:26 | MSG-03 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 0917149c-8f42-3daf-b330-802ae6b8cd05 | -20.1 | -49.09 | 2024-10-07 02:03:29 | MSG-03 | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| f63b7bab-e44a-328c-ad8d-41f888d8a6d7 | -20.1 | -49.04 | 2024-10-07 02:03:29 | MSG-03 | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 5c1de5fa-efa4-3229-8ccb-5a22e3e90feb | -20.13 | -49.11 | 2024-10-07 02:03:29 | MSG-03 | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 0917b396-897e-36d5-9cba-765d8be22b49 | -20.13 | -49.06 | 2024-10-07 02:03:29 | MSG-03 | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| defcc255-77b7-3af8-9b78-8726e588ed32 | -17.77 | -53.81 | 2024-10-07 02:03:45 | MSG-03 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| cccd7d13-7324-3ada-8cc0-3b4b4c111c56 | -4.27 | -43.74 | 2024-10-07 02:05:04 | MSG-03 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| dd0c69fc-59db-31c4-bce6-3973f3e971e8 | -1.0365 | -53.7389 | 2024-10-07 02:05:12 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 90.9 |
| 85774bcc-6608-3c14-b420-0e974203a265 | -1.0365 | -53.7187 | 2024-10-07 02:05:12 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 80.9 |
| 0ecca780-8aa4-3091-9751-19a4d1a3be20 | -2.2297 | -53.7026 | 2024-10-07 02:05:19 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 78.7 |
| 3afdc492-50de-3477-b943-8469066a5a14 | -2.8569 | -52.9197 | 2024-10-07 02:05:22 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 81.5 |
| cfa6e12f-cf84-3db4-a166-2524b9d914e0 | -2.857 | -52.8993 | 2024-10-07 02:05:22 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 91.9 |
| 2d544670-69b2-3aa7-b51f-0968b60007f2 | -2.8753 | -52.9192 | 2024-10-07 02:05:22 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 160.9 |
| ecd631e5-d98a-303f-8af1-37a5daae4b9f | -2.8754 | -52.8989 | 2024-10-07 02:05:22 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 194.9 |
| 18d8edcf-f6a2-37ee-a28a-ebd0271ecda9 | -2.8937 | -52.8984 | 2024-10-07 02:05:23 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 74.9 |
| 5bd935b9-292e-30ec-9269-647a0165cf82 | -3.538 | -65.0414 | 2024-10-07 02:05:26 | GOES-16 | ALVARÃES | AMAZONAS | Brasil | 1300029 | 13 | 33 | nan | nan | nan | Amazônia | 47.6 |
| 8d02a63d-fa1b-3744-9af9-d7cdc3d899c4 | -3.5381 | -65.0229 | 2024-10-07 02:05:26 | GOES-16 | ALVARÃES | AMAZONAS | Brasil | 1300029 | 13 | 33 | nan | nan | nan | Amazônia | 70.0 |
| da98c96c-0004-3cd2-88de-d97eee2e122d | -18.8836 | -57.760101 | 2024-10-07 02:05:26 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 951030e2-ae75-3f31-b121-9901bbbdf2ac | -18.8932 | -57.757099 | 2024-10-07 02:05:26 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 56dec595-20f1-33a9-bb70-6e08fc2a8b4c | -18.894899 | -57.727001 | 2024-10-07 02:05:26 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| f5b996ee-7de3-3cf5-975d-bcab2adf1a52 | -18.662201 | -57.2808 | 2024-10-07 02:05:27 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| f4f53754-70d7-3645-90c6-863179a73afa | -18.680099 | -57.306702 | 2024-10-07 02:05:27 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| d83f85cb-e3b0-3cc5-81a9-416199e28745 | -18.6717 | -57.277699 | 2024-10-07 02:05:27 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 98aa7be3-d16c-35c6-9cd1-3eb0938667b7 | -3.9103 | -48.3466 | 2024-10-07 02:05:28 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 37.7 |
| b06f0978-1236-3e2c-9b63-9e426bf9ec17 | -4.2542 | -43.7381 | 2024-10-07 02:05:30 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 56.5 |
| 2c503433-dcbe-37a4-909c-349899679b52 | -4.2728 | -43.7601 | 2024-10-07 02:05:30 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 76.5 |
| f1fb57e5-e1a9-3216-9758-f62e6e9390f1 | -4.2729 | -43.737 | 2024-10-07 02:05:30 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 197.2 |
| a9404005-6e44-3010-8d3c-cb8b9eee68aa | -4.2731 | -43.7139 | 2024-10-07 02:05:30 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 45.9 |
| 5a6f1bac-b5b7-38dc-b40a-905cdf7d1f09 | -4.2916 | -43.736 | 2024-10-07 02:05:30 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 65.0 |
| 790e707b-2615-353a-bfe6-8dd6abe8c9c6 | -18.690599 | -57.2715 | 2024-10-07 02:05:40 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 3a2859b1-1015-3d29-9018-327012acb2d1 | -18.698999 | -57.300598 | 2024-10-07 02:05:40 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| b841d262-e357-3f29-bf63-1bca39da06ea | -18.681101 | -57.274601 | 2024-10-07 02:05:40 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| df8300e4-91c2-3002-9954-630e0bdacd88 | -18.626101 | -57.228401 | 2024-10-07 02:05:40 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| e7331ae5-892c-37ad-941d-b1141db5a3c8 | -6.1116 | -47.2457 | 2024-10-07 02:05:41 | GOES-16 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 38.7 |
| c55f23cf-dddf-3e87-bdac-3b5c99aa9085 | -6.1118 | -47.2237 | 2024-10-07 02:05:41 | GOES-16 | LAJEADO NOVO | MARANHÃO | Brasil | 2105989 | 21 | 33 | nan | nan | nan | Cerrado | 79.1 |
| 8cc41662-5a24-365e-b899-26ae076cbda3 | -6.1304 | -47.2224 | 2024-10-07 02:05:41 | GOES-16 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 47.8 |
| a6575b9b-e7fe-348c-8c9f-a66c4c19e815 | -18.6166 | -57.231499 | 2024-10-07 02:05:41 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 4fcf3385-fb68-365f-90da-13b10c7c1f0e | -9.5152 | -40.331 | 2024-10-07 02:05:59 | GOES-16 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 102.9 |
| f7be7a9d-9676-328b-82bb-9aac06dec73e | -9.5343 | -40.3282 | 2024-10-07 02:05:59 | GOES-16 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 167.9 |
| 79e0aae9-b59c-3cea-842c-4ffff298bc3c | -17.089399 | -56.761799 | 2024-10-07 02:06:03 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 1ad9e18b-6cac-31b4-bc52-b850331ffddf | -17.0991 | -56.7953 | 2024-10-07 02:06:03 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| d4db7b51-f1c0-383d-882f-48faa236af46 | -17.08 | -56.7649 | 2024-10-07 02:06:03 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 21463295-6289-3c04-80b2-d003b2b57824 | -17.089701 | -56.798401 | 2024-10-07 02:06:03 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| abac93f2-4294-3617-9b48-775cc5a815f8 | -17.0802 | -56.801399 | 2024-10-07 02:06:03 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| b9c69bf5-a97e-3205-b8a1-e1c2c14e34e5 | -17.089899 | -56.834801 | 2024-10-07 02:06:03 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 4858ada9-63c8-374e-b1f7-9642b0d05cb7 | -17.0707 | -56.804501 | 2024-10-07 02:06:03 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| eb85b442-05a0-328d-ba20-60b4a5ed5fdf | -17.0804 | -56.837799 | 2024-10-07 02:06:03 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 12000b91-a3c6-3907-b012-b31ec90bedf5 | -17.0613 | -56.807499 | 2024-10-07 02:06:04 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 2d9fa671-082f-3b92-8f57-8e11ddac9103 | -17.070999 | -56.840801 | 2024-10-07 02:06:04 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 37f7979c-d9fc-342e-9144-cf27089ddfdf | -17.0518 | -56.8106 | 2024-10-07 02:06:04 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| aac0cb2a-bc6a-3f68-a732-04e99a0c87f2 | -17.042299 | -56.813599 | 2024-10-07 02:06:04 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 62064ba3-1f4a-3fea-81cb-d5479c36d709 | -17.0329 | -56.816601 | 2024-10-07 02:06:04 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 3f8d792b-e8a0-3c9a-ae6b-331cfbb426d7 | -17.023399 | -56.819599 | 2024-10-07 02:06:04 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 4e5a33cb-2f44-3cda-9e71-7134eaeecf5c | -16.9744 | -56.687599 | 2024-10-07 02:06:04 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| d604ccf9-af39-3412-ae76-e12d97574340 | -16.965 | -56.690701 | 2024-10-07 02:06:05 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| dded5b20-61b3-341f-9761-7aed9a26cf99 | -16.975 | -56.724701 | 2024-10-07 02:06:05 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 03705b4a-b838-36ec-bd7b-9e51bba1cefb | -16.9555 | -56.693699 | 2024-10-07 02:06:05 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 88df27bc-e69c-3e1c-9c62-7d1d3b6d57eb | -17.125099 | -57.313599 | 2024-10-07 02:06:05 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| a19d9584-d0d9-354c-8ca1-cd01ca60c58c | -17.134001 | -57.344501 | 2024-10-07 02:06:05 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| d4a8f008-59f8-37ff-b8d6-69bcef36f895 | -17.1157 | -57.3167 | 2024-10-07 02:06:05 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| d3cdcaf5-36d1-3fc9-9ad2-3057ce6d3467 | -17.124599 | -57.3475 | 2024-10-07 02:06:05 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 3fa2a21a-50c1-37b8-9b90-406872183070 | -16.927601 | -56.739899 | 2024-10-07 02:06:05 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| a4971580-4470-3177-bb10-c3fb4e2e8fc8 | -16.9375 | -56.773701 | 2024-10-07 02:06:05 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 495d294d-e727-3105-9177-82d55d610467 | -16.927999 | -56.776699 | 2024-10-07 02:06:06 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 0f03c47b-968d-356d-96fa-b95e46d96ad3 | -10.8754 | -63.9169 | 2024-10-07 02:06:08 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 56.9 |
| fffc9ad2-cdff-3cb4-bad4-aa613baebbd9 | -10.8755 | -63.8979 | 2024-10-07 02:06:08 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 65.3 |
| ba0d2345-f1a3-3761-8a54-27712faa7855 | -16.7843 | -57.3535 | 2024-10-07 02:06:11 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| e594fdaa-45e3-36ab-8102-9164f2e7cb10 | -16.793301 | -57.384602 | 2024-10-07 02:06:11 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |


[Clique aqui para ver as próximas entradas](README33.md)
