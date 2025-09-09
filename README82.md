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

## Dados Diários - Página 82

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 692d0ae5-312b-3edb-b601-d7377352abf3 | -6.527 | -44.7974 | 2025-09-09 14:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 80.3 |
| 28133590-0cf5-30cc-9573-31902d849752 | -15.8205 | -52.2444 | 2025-09-09 14:00:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 154.9 |
| ff06dc56-2605-325b-a16c-f56108cb4957 | -5.453 | -43.4525 | 2025-09-09 14:00:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 168.7 |
| 1df6febf-e24b-3957-a7d4-c8920fdd0b1a | -10.2982 | -48.8148 | 2025-09-09 14:00:00 | GOES-19 | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 61.1 |
| e99679a7-bee5-3a37-84fc-ad1387c4bee9 | -5.5504 | -45.1891 | 2025-09-09 14:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 86.7 |
| f62af1c9-2220-3c21-8b0e-4d9a089adde8 | -5.3669 | -44.793 | 2025-09-09 14:00:00 | GOES-19 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 69.1 |
| a6d9114a-43ca-31d4-bd43-aa8327c5f53f | -9.0934 | -45.7088 | 2025-09-09 14:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 88.8 |
| 23ce65ff-994c-3b78-bae9-3783e2669684 | -5.4343 | -43.4538 | 2025-09-09 14:00:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 346.2 |
| 522095eb-ad05-3057-856c-4e4b6f23af70 | -17.2757 | -46.7538 | 2025-09-09 14:00:00 | GOES-19 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 102.4 |
| b8d2750f-c267-3e45-8c1c-d4da2505760e | -5.8395 | -44.2103 | 2025-09-09 14:00:00 | GOES-19 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 186.2 |
| edab0f70-d1f7-3b75-945b-c251e9c89499 | -11.4469 | -43.5988 | 2025-09-09 14:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 101.8 |
| 266a57bd-5b78-300a-9f2a-deea06cfe389 | -7.881 | -46.2598 | 2025-09-09 14:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 98.3 |
| e28dd2a0-c1f2-3705-bd00-624544195a53 | -6.2226 | -43.3459 | 2025-09-09 14:00:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 127.1 |
| 88e5c5c9-dab5-3c85-9690-cf4e3c786f07 | -11.2196 | -54.9975 | 2025-09-09 14:00:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 70.9 |
| 7fb9a5f0-2bac-3057-a874-0968922bc24a | -6.2595 | -43.4129 | 2025-09-09 14:10:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 67.7 |
| 8bb3fb2b-e85a-38fe-b395-3799dff7b247 | -16.3602 | -43.0349 | 2025-09-09 14:10:00 | GOES-19 | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 121.3 |
| 249c4f79-f1fe-38b4-bb9e-25f175f551df | -17.2967 | -46.7032 | 2025-09-09 14:10:00 | GOES-19 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 126.8 |
| 570e57a9-01bd-3433-bd9a-3ec31f340e32 | -8.0604 | -48.664 | 2025-09-09 14:10:00 | GOES-19 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 87.8 |
| 60d2c689-b8ec-306f-baab-f29aecc8b4a9 | -12.5098 | -45.2786 | 2025-09-09 14:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 76.7 |
| 455a0891-e002-315d-8076-45e033475c29 | -6.4096 | -45.3067 | 2025-09-09 14:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 119.5 |
| a4c191d7-0947-3c76-ad0f-214583495815 | -13.1367 | -54.9171 | 2025-09-09 14:10:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 106.7 |
| 14703372-6255-3cf7-8053-25c9d784470a | -11.3014 | -46.5018 | 2025-09-09 14:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 162.9 |
| 074db829-8654-3a1e-8393-644a61ad2663 | -8.4612 | -51.4595 | 2025-09-09 14:10:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 84.0 |
| 4c8e4158-4a48-3e31-be76-77538bd8ad8a | -9.2181 | -60.8305 | 2025-09-09 14:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 59.8 |
| 9b645cfc-9cac-3da7-8bcd-33a72e7b38c0 | -5.8582 | -44.2088 | 2025-09-09 14:10:00 | GOES-19 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 80.5 |
| 7c6a5c4f-78ac-344e-9c04-adddd9f2471d | -15.2062 | -41.1215 | 2025-09-09 14:10:00 | GOES-19 | VITÓRIA DA CONQUISTA | BAHIA | Brasil | 2933307 | 29 | 33 | nan | nan | nan | Mata Atlântica | 89.5 |
| 39fac1f4-5400-33d7-8dc7-c770a64314c3 | -7.789 | -46.0891 | 2025-09-09 14:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 98.7 |
| 7ed78fc4-bbaf-373a-88fa-22b45aac7b0c | -8.0606 | -48.6423 | 2025-09-09 14:10:00 | GOES-19 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 119.8 |
| 4388df77-756e-3935-ad20-f7ecbdba1430 | -14.5601 | -52.2262 | 2025-09-09 14:10:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 90.6 |
| a8092b3f-02ec-33ba-ba90-9a2f6fbe138e | -12.529 | -45.2756 | 2025-09-09 14:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 169.3 |
| c7184e4b-cff6-329d-b726-e566f61a5011 | -14.2932 | -45.0261 | 2025-09-09 14:10:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 87.8 |
| 66e16a4c-5a7c-3ae1-a67e-f65cd62fa796 | -5.8218 | -44.0965 | 2025-09-09 14:10:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 94.6 |
| 35aea319-bc8d-3011-84f1-1103bb31ecb4 | -5.8791 | -43.9769 | 2025-09-09 14:10:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 84.1 |
| c1e2900c-d643-3506-926f-eeb4cc2e7465 | -17.7328 | -44.4637 | 2025-09-09 14:10:00 | GOES-19 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 423.5 |
| 53d1a73e-2dc7-35d3-8575-1422e0cfb620 | -6.2087 | -41.0137 | 2025-09-09 14:10:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 90.9 |
| 79c725f7-5316-39ea-b8ed-cf32e0f28f53 | -15.8397 | -52.2631 | 2025-09-09 14:10:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 99.0 |
| ce2b8d6b-da3d-36d7-b974-b58fd0e27546 | -5.8406 | -44.0951 | 2025-09-09 14:10:00 | GOES-19 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 83.7 |
| 80d5d90e-8db3-3138-af55-fc0311365c58 | -5.6418 | -45.4312 | 2025-09-09 14:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 106.9 |
| 4f9f9fbf-f26f-3823-b3a4-e31d90c96c7e | -5.898 | -43.9523 | 2025-09-09 14:10:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 105.9 |
| 8681ac2f-f3e2-3b10-b72b-e555e4a6aa7b | -6.2226 | -43.3459 | 2025-09-09 14:10:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 119.4 |
| 7f749407-3b74-3263-8742-c251e6b5d2be | -9.1914 | -59.3843 | 2025-09-09 14:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 54.2 |
| e7151a64-bc53-370b-8ba4-3c2f834d6d9e | -15.8205 | -52.2444 | 2025-09-09 14:10:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 167.1 |
| cddec375-863c-321c-95b4-8b121f36929b | -12.0295 | -51.0935 | 2025-09-09 14:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 113.0 |
| 9a82ee2d-4975-3d19-89dc-5180814db60a | -15.8201 | -52.2659 | 2025-09-09 14:10:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 106.3 |
| 5f12a8c6-95a7-34b9-a05f-9bed4e091998 | -5.4585 | -42.8206 | 2025-09-09 14:10:00 | GOES-19 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 89.5 |
| e81f7085-925d-312a-8ba9-622370d795c8 | -5.8395 | -44.2103 | 2025-09-09 14:10:00 | GOES-19 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 161.0 |
| 9aea5bb6-9dac-3bcc-af29-d725897a1140 | -4.7345 | -44.4685 | 2025-09-09 14:10:00 | GOES-19 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 222.8 |
| 1888f317-bf50-3fc6-96ba-231b9f63ca22 | -5.9191 | -45.7717 | 2025-09-09 14:10:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 83.4 |
| 67054179-98de-3b15-ab90-8f029d34c9d6 | -6.2407 | -43.4144 | 2025-09-09 14:10:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 81.7 |
| 1e76b2a7-6bc7-3229-ab02-892c14bf0f1b | -18.6904 | -52.594 | 2025-09-09 14:10:00 | GOES-19 | CHAPADÃO DO SUL | MATO GROSSO DO SUL | Brasil | 5002951 | 50 | 33 | nan | nan | nan | Cerrado | 158.5 |
| cd2caacb-01cd-3144-b9bc-aa0b8c625199 | -17.7127 | -44.4684 | 2025-09-09 14:10:00 | GOES-19 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 258.3 |
| 7959fb96-62dd-3045-af65-cf2109d27a34 | -5.5506 | -45.1664 | 2025-09-09 14:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 91.7 |
| fc7ee255-a57e-3160-ac03-1eefead1ced1 | -6.9134 | -45.5142 | 2025-09-09 14:10:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 84.4 |
| eff11c32-957f-34f9-8597-9a3281052794 | -12.2178 | -53.9005 | 2025-09-09 14:10:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 75.1 |
| 91b52ffc-76b1-3bb3-abad-5252d682722f | -5.6738 | -43.9 | 2025-09-09 14:10:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 103.9 |
| b182eb6c-3696-3401-b272-fffa38438810 | -5.7168 | -45.4035 | 2025-09-09 14:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 95.1 |
| e53802a7-af1e-39d6-8ceb-9470861bfad7 | -12.1988 | -53.9024 | 2025-09-09 14:10:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 226.2 |
| 9447f2c2-4a28-37d4-8c2c-5d2efa4a11d6 | -12.1993 | -53.8611 | 2025-09-09 14:10:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 76.4 |
| 524795ba-2f1d-327a-ac40-237f09cd1920 | -11.3172 | -50.4275 | 2025-09-09 14:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 182.3 |
| 32719789-f983-38b3-9202-a9350e0db95a | -4.7346 | -44.4457 | 2025-09-09 14:10:00 | GOES-19 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 241.8 |
| 80871265-5e81-3c7b-8bfd-fc55900ffdaa | -11.4465 | -43.6224 | 2025-09-09 14:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 93.8 |
| ea44e11f-38bf-3fdd-8d57-63434e02d377 | -6.1803 | -45.82 | 2025-09-09 14:10:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 123.4 |
| 53c03dcc-7f30-36d8-a795-8afbd9602ce2 | -11.3549 | -50.4447 | 2025-09-09 14:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 167.8 |
| fa2ee4b7-11c0-309a-856c-75a7eb595d16 | -12.6343 | -56.9725 | 2025-09-09 14:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 79.2 |
| 41849926-4290-3396-81fb-65eac678a58c | -12.0291 | -51.1149 | 2025-09-09 14:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 226.9 |
| 8b86d391-1c94-3412-a471-9d4e76805d4d | -13.9564 | -48.2493 | 2025-09-09 14:10:00 | GOES-19 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 45.4 |
| df19a736-09ee-39d9-a2b1-2ebec553e15f | -13.9726 | -54.0211 | 2025-09-09 14:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 99.5 |
| ab1e6bb5-ffdf-392a-8366-3b4883804a47 | -12.2181 | -53.8798 | 2025-09-09 14:10:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 109.4 |
| b9a8401d-5c9b-3b6b-8cac-0a9b9032e484 | -13.8412 | -46.2369 | 2025-09-09 14:10:00 | GOES-19 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 87.4 |
| 23fbf185-bdc4-322f-a8e7-84c9e1559394 | -5.3482 | -44.7943 | 2025-09-09 14:10:00 | GOES-19 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 96.9 |
| 699ac30d-1c6d-327d-880d-8f392885a2b7 | -5.6607 | -45.4074 | 2025-09-09 14:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 81.0 |
| 0a903664-1413-3c7b-9535-e511c413d2a0 | -17.2973 | -46.6799 | 2025-09-09 14:10:00 | GOES-19 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 67.1 |
| f1e68cad-3353-341e-9e10-72af2b47a498 | -11.3011 | -46.5244 | 2025-09-09 14:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 303.8 |
| 7526eab5-be64-3df4-9148-201f6b30c374 | -12.5286 | -45.2987 | 2025-09-09 14:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 133.2 |
| 93adee37-8eb8-3168-adce-94166f1371ba | -19.9545 | -49.2928 | 2025-09-09 14:10:00 | GOES-19 | ITAPAGIPE | MINAS GERAIS | Brasil | 3133402 | 31 | 33 | nan | nan | nan | Mata Atlântica | 220.0 |
| e6f3e71a-b4d1-31ce-9edb-1007dd04abce | -9.7206 | -46.8302 | 2025-09-09 14:10:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 138.6 |
| 3e05bdd0-e40d-3a18-9f8e-d4f2b86ae52a | -5.7553 | -45.2652 | 2025-09-09 14:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 78.5 |
| c1220bb8-b1df-3fd5-9495-2c5a76178991 | -11.4469 | -43.5988 | 2025-09-09 14:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 165.5 |
| 55da6cc6-0ef7-3370-9c28-92b7c1446a3f | -5.5504 | -45.1891 | 2025-09-09 14:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 92.8 |
| 5593d4da-2497-3163-8b0b-92665f378125 | -11.3552 | -50.4233 | 2025-09-09 14:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 141.0 |
| 22f59dd7-97ca-31dc-9ef5-137cbbc18aa7 | -15.758 | -53.548 | 2025-09-09 14:10:00 | GOES-19 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 125.2 |
| 0886e901-0654-3669-adaa-26bbcec2b305 | -5.9899 | -46.2141 | 2025-09-09 14:10:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 87.6 |
| 8a7cc514-d9f3-3cc9-875c-68d573f173e9 | -9.7203 | -46.8526 | 2025-09-09 14:10:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 154.4 |
| b898d17d-0ac4-3ded-b4eb-627ab7734812 | -17.7322 | -44.4879 | 2025-09-09 14:10:00 | GOES-19 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 171.0 |
| 8326eda3-62cd-3a31-b5e5-fd00d5ea9b16 | -5.975 | -45.7901 | 2025-09-09 14:10:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 143.1 |
| 0eaaf93e-f67e-3a6e-820d-2ad4873e1d43 | -5.9563 | -45.7915 | 2025-09-09 14:10:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 78.5 |
| 6b23d0e9-3da3-37cd-a415-521d05f56c6d | -9.7014 | -46.8547 | 2025-09-09 14:10:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 174.8 |
| e3f6ea3e-9575-3795-bf16-e019f41b6e12 | -12.6153 | -56.9742 | 2025-09-09 14:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 80.9 |
| 0e333967-0549-3565-9bb7-c1a5a6550d62 | -13.9723 | -54.0419 | 2025-09-09 14:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 86.8 |
| 0a2a2aaa-ce34-3308-9833-6d1d02628351 | -8.4119 | -49.0869 | 2025-09-09 14:10:00 | GOES-19 | COUTO MAGALHÃES | TOCANTINS | Brasil | 1706001 | 17 | 33 | nan | nan | nan | Cerrado | 173.1 |
| bc8cea05-f1f9-3858-be8a-20dd5be9f7fd | -11.2196 | -54.9975 | 2025-09-09 14:10:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 76.3 |
| a0cd9448-d8c8-3d85-a5a9-9c3d77632bc5 | -5.2263 | -43.7006 | 2025-09-09 14:10:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 85.9 |
| b30e652b-ea37-38b6-af2f-4317b7b17ec8 | -15.7583 | -53.5268 | 2025-09-09 14:10:00 | GOES-19 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 282.1 |
| 1e3ac138-82b7-3541-98ca-30953424f2bf | -9.7857 | -46.24 | 2025-09-09 14:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 76.8 |
| 25ee5059-934c-3504-98c7-9f245e31c99b | -11.4272 | -43.6254 | 2025-09-09 14:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 85.5 |
| 813d96db-6f29-3517-8fd5-4ee78056d535 | -6.199 | -45.8186 | 2025-09-09 14:10:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 361.9 |
| 6e7fec6a-acf0-3296-8533-ce7b74cead69 | -5.453 | -43.4525 | 2025-09-09 14:10:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 137.4 |
| 6e94ad36-b876-347f-a9b2-2ec1b51dee88 | -6.2224 | -43.3693 | 2025-09-09 14:10:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 131.0 |
| 3ce2940c-a370-3f5c-80d1-acf12c384949 | -12.9482 | -54.7519 | 2025-09-09 14:10:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 82.2 |
| 766112a5-082a-38bc-9d53-c1e850fb3bae | -7.881 | -46.2598 | 2025-09-09 14:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 120.8 |


[Clique aqui para ver as próximas entradas](README83.md)
