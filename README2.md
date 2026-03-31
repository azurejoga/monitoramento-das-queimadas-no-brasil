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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a66bb026-c372-3252-90cb-593d645c42bb | -16.31502 | -58.49177 | 2026-03-31 05:01:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.6 |
| 3d9a4cff-3ced-387f-a08c-d2072b091a7e | -22.06015 | -56.22054 | 2026-03-31 05:01:00 | NPP-375D | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7b7158be-24c4-39a8-95a7-918649474969 | -15.24449 | -50.82861 | 2026-03-31 05:01:00 | NPP-375D | MATRINCHÃ | GOIÁS | Brasil | 5212956 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 32063c16-58de-327e-8514-682dd02e17fd | -22.03333 | -56.3038 | 2026-03-31 05:01:00 | NPP-375D | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d47aa5fd-4a07-35c2-8393-8622c9e4fbaa | -19.18223 | -49.12978 | 2026-03-31 05:01:00 | NPP-375D | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2f5fca15-2250-3532-a0d5-a196bad7ce1d | -21.5266 | -53.3926 | 2026-03-31 05:01:00 | NPP-375D | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3d1db863-fe17-3abb-b8dd-0272fa0088a3 | -20.91883 | -49.52516 | 2026-03-31 05:01:00 | NPP-375D | MIRASSOL | SÃO PAULO | Brasil | 3530300 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 7c4abc71-0308-301a-bb21-052472133035 | -15.24008 | -50.83271 | 2026-03-31 05:01:00 | NPP-375D | MATRINCHÃ | GOIÁS | Brasil | 5212956 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0f940ba3-ccf2-35f0-8f33-a5a75267f0c3 | -21.71533 | -56.32381 | 2026-03-31 05:01:00 | NPP-375D | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 99cde616-2125-3093-a793-00b321eaeabc | -20.20168 | -46.44123 | 2026-03-31 05:01:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 60f96a3b-1c93-3352-b7e7-dc0b9ec95c59 | -20.7959 | -55.37178 | 2026-03-31 05:01:00 | NPP-375D | DOIS IRMÃOS DO BURITI | MATO GROSSO DO SUL | Brasil | 5003488 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b6025e5f-feb7-337a-bd0b-5529b794d1d9 | -14.32526 | -57.73045 | 2026-03-31 05:01:00 | NPP-375D | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4cd000c9-01a9-370b-922b-b961ae33bba9 | -20.19966 | -46.44165 | 2026-03-31 05:01:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 89694a93-6c6c-3e31-8bd1-813a19fff3e1 | -28.57084 | -51.0269 | 2026-03-31 05:04:00 | NPP-375D | VACARIA | RIO GRANDE DO SUL | Brasil | 4322509 | 43 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| c02fe8f3-11ad-3302-83b4-a6607e13f192 | -12.44701 | -60.5201 | 2026-03-31 05:21:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4f066e23-0df0-3cd4-b304-6a7f5b9fcd8a | -12.28708 | -57.3923 | 2026-03-31 05:21:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| aae08ebb-ef0a-3fba-8da5-2f6ed8cbdf50 | -13.1551 | -53.25987 | 2026-03-31 05:21:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b8d9b09d-e069-35e7-b34e-334f718ebb41 | -13.15042 | -53.25927 | 2026-03-31 05:21:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ce1b3019-eb4a-307a-a560-e6d5b929793d | -12.29006 | -57.39699 | 2026-03-31 05:21:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7078384d-0a5c-3aa7-8ca8-7a4f658f3093 | -13.15108 | -53.25422 | 2026-03-31 05:21:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5a9e18e7-cfab-3c76-a953-337e75cd50e9 | -14.82911 | -59.83492 | 2026-03-31 05:23:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 62d91808-fafd-316c-865e-02f24de67c12 | -14.33173 | -57.727 | 2026-03-31 05:23:00 | NOAA-20 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f6d07c2d-3b53-387c-b3f4-ac782b9b25dd | -20.91602 | -49.5217 | 2026-03-31 05:23:00 | NOAA-20 | MIRASSOL | SÃO PAULO | Brasil | 3530300 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 46b3bc9b-215f-333d-ba57-aab7f5b819c4 | -21.70754 | -48.43399 | 2026-03-31 05:23:00 | NOAA-20 | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 74330f81-9999-3b3b-a8ed-752cc2858cf3 | -19.29313 | -55.16091 | 2026-03-31 05:23:00 | NOAA-20 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f68ccb5f-ad6b-3f20-8c58-b591363df6cb | -14.32453 | -57.72594 | 2026-03-31 05:23:00 | NOAA-20 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d66dcc9a-8279-3314-9386-6e81dc1fa523 | -20.04346 | -54.51103 | 2026-03-31 05:23:00 | NOAA-20 | JARAGUARI | MATO GROSSO DO SUL | Brasil | 5004908 | 50 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f6351224-b2fc-314d-95fd-bdb8b7646392 | -14.32813 | -57.72648 | 2026-03-31 05:23:00 | NOAA-20 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5d34a52b-9190-3a75-9557-c1276d77561d | -21.71585 | -48.44193 | 2026-03-31 05:23:00 | NOAA-20 | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6b4b999f-849c-3004-84a9-aeb9cb603598 | -18.84021 | -53.42656 | 2026-03-31 05:23:00 | NOAA-20 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 83018d9b-e696-3b68-aeab-6a3d9eb1effa | -21.70934 | -48.43476 | 2026-03-31 05:23:00 | NOAA-20 | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 39e451e6-d409-3689-9179-2d739470a2d8 | -20.91549 | -49.52775 | 2026-03-31 05:23:00 | NOAA-20 | MIRASSOL | SÃO PAULO | Brasil | 3530300 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| f15e745c-135f-3598-bc0c-5ee0b1f31bcd | -21.7141 | -48.44113 | 2026-03-31 05:23:00 | NOAA-20 | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 2.6 |
| dacc905e-254c-35e3-a40a-3ad7801c7b46 | -16.31816 | -58.48959 | 2026-03-31 05:23:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 42526179-2455-3915-8375-325acc1b6818 | -21.71459 | -48.4341 | 2026-03-31 05:23:00 | NOAA-20 | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 647dc769-bcd6-3ef0-8c86-a7532e2ad020 | -21.71389 | -52.9924 | 2026-03-31 05:25:00 | NOAA-20 | BATAGUASSU | MATO GROSSO DO SUL | Brasil | 5001904 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2288c6ff-0f41-39ca-8a69-ba4277a73040 | -21.71352 | -52.99601 | 2026-03-31 05:25:00 | NOAA-20 | BATAGUASSU | MATO GROSSO DO SUL | Brasil | 5001904 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fd7762af-60d4-3273-84a5-5074e5ba2688 | -22.07419 | -55.48857 | 2026-03-31 05:25:00 | NOAA-20 | DOURADOS | MATO GROSSO DO SUL | Brasil | 5003702 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| cd01bcdd-cf12-314f-ab45-6d3f9390fc3e | -21.71418 | -56.32296 | 2026-03-31 05:25:00 | NOAA-20 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1d1a4eb6-fc7c-398e-940f-29aeb0bf8f7a | -22.07365 | -55.49335 | 2026-03-31 05:25:00 | NOAA-20 | DOURADOS | MATO GROSSO DO SUL | Brasil | 5003702 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8505cd70-e686-301e-95bc-4c55e94f6bd8 | -12.7878 | -45.8333 | 2026-03-31 11:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 123.5 |
| 21a0b11e-e69a-3ec3-9f9d-53227dc214e7 | -12.7878 | -45.8333 | 2026-03-31 11:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 123.4 |
| e6218bdb-05f4-3f59-85d8-88815ef1e15f | -12.7878 | -45.8333 | 2026-03-31 11:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 120.1 |
| 1991ccf8-ed7f-3a0b-9000-77f00f997008 | -12.7878 | -45.8333 | 2026-03-31 12:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 136.7 |
| d467570c-fec2-368e-976b-ce19c263b206 | -12.7878 | -45.8333 | 2026-03-31 12:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 148.1 |
| 83346018-24f5-3548-af99-32df312749b5 | -12.7878 | -45.8333 | 2026-03-31 12:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 145.0 |
| e71c2aca-d98e-367e-8491-c14974931452 | -16.19291 | -45.1227 | 2026-03-31 12:27:00 | TERRA_M-T | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 49.9 |
| df38a590-0d3c-3836-9a2d-301f7fc9ffdb | -16.86156 | -48.38475 | 2026-03-31 12:27:00 | TERRA_M-T | VIANÓPOLIS | GOIÁS | Brasil | 5222005 | 52 | 33 | nan | nan | nan | Cerrado | 21.4 |
| 0a70debe-2792-39b2-bdf2-2c4746449392 | -13.50787 | -56.86644 | 2026-03-31 12:27:00 | TERRA_M-T | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 14.5 |
| 60ab57d5-95b9-3f9c-b7ea-52dfa8131630 | -12.78894 | -45.84982 | 2026-03-31 12:27:00 | TERRA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 60.9 |
| b8985336-1d2b-307a-85f2-a9bfd37c5e70 | -15.32166 | -46.47081 | 2026-03-31 12:27:00 | TERRA_M-T | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 15.9 |
| 658354d0-eaef-3623-8dee-e9c09ebebaa5 | -16.1836 | -45.15421 | 2026-03-31 12:27:00 | TERRA_M-T | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 61.6 |
| 1a554ec8-e957-3b3c-847e-24ccee5448e1 | -11.32322 | -55.6641 | 2026-03-31 12:27:00 | TERRA_M-T | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 6b3b347e-bcfc-3799-9b73-098ca5fbe665 | -15.52905 | -45.8974 | 2026-03-31 12:27:00 | TERRA_M-T | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 15.7 |
| 77c4d551-145b-34c3-a428-0db80c254c5b | -13.50943 | -56.85609 | 2026-03-31 12:27:00 | TERRA_M-T | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 131.8 |
| 74c6b1f1-7595-3ba2-96ea-396aa6e572bb | -15.12288 | -47.31722 | 2026-03-31 12:27:00 | TERRA_M-T | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 22.2 |
| 70d0158e-5783-399c-872c-538e3c8767b8 | -16.18939 | -45.1601 | 2026-03-31 12:27:00 | TERRA_M-T | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 42.8 |
| 05856fb0-52bd-3045-a579-b4e99cb1a419 | -16.02511 | -50.04301 | 2026-03-31 12:27:00 | TERRA_M-T | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 29.5 |
| 917c41ed-a02f-33ff-b8b4-b5dd90921b78 | -16.18735 | -45.11684 | 2026-03-31 12:27:00 | TERRA_M-T | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 43.5 |
| f94d81cb-3813-367d-8836-ea4bddb6a27d | -25.08066 | -53.2668 | 2026-03-31 12:29:00 | TERRA_M-T | CASCAVEL | PARANÁ | Brasil | 4104808 | 41 | 33 | nan | nan | nan | Mata Atlântica | 6.3 |
| 62a45d29-8e53-33e0-b58f-dd135faf8890 | -26.91901 | -53.07189 | 2026-03-31 12:29:00 | TERRA_M-T | SAUDADES | SANTA CATARINA | Brasil | 4217303 | 42 | 33 | nan | nan | nan | Mata Atlântica | 7.6 |
| 2c1d6c5b-fd07-3384-bf0e-77d48434b9de | -19.01403 | -49.87221 | 2026-03-31 12:29:00 | TERRA_M-T | GURINHATÃ | MINAS GERAIS | Brasil | 3129103 | 31 | 33 | nan | nan | nan | Cerrado | 19.9 |
| 57b47a36-96a2-3003-a4fd-a70040d04495 | -21.72544 | -57.03559 | 2026-03-31 12:29:00 | TERRA_M-T | CARACOL | MATO GROSSO DO SUL | Brasil | 5002803 | 50 | 33 | nan | nan | nan | Cerrado | 6.4 |
| d444cb0b-70d0-3b76-a9c3-8b5e4e75cf3b | -23.03538 | -52.67321 | 2026-03-31 12:29:00 | TERRA_M-T | PARANAVAÍ | PARANÁ | Brasil | 4118402 | 41 | 33 | nan | nan | nan | Mata Atlântica | 16.7 |
| a41dc304-d863-3028-8594-cf6cad244b50 | -26.92064 | -53.05678 | 2026-03-31 12:29:00 | TERRA_M-T | SAUDADES | SANTA CATARINA | Brasil | 4217303 | 42 | 33 | nan | nan | nan | Mata Atlântica | 11.3 |
| eabab2b4-7474-30c7-8fa4-cd3f6ac52c7b | -12.7878 | -45.8333 | 2026-03-31 12:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 144.3 |
| 966a8aed-7a01-3759-8c1f-9cea7ddc47a0 | -12.7878 | -45.8333 | 2026-03-31 12:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 129.7 |
| aefd8577-18da-30f3-a1c3-c32ad3872996 | -12.7878 | -45.8333 | 2026-03-31 13:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 142.8 |
| e9d4fb72-a60b-329b-b08a-8ce3b404ee43 | -13.5113 | -56.8723 | 2026-03-31 14:30:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 109.3 |
| 461a6aca-3b16-395f-9657-3d1bbfa3d124 | -13.5113 | -56.8723 | 2026-03-31 14:40:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 94.7 |


