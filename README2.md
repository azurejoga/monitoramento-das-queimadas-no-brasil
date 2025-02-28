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
| c89a2286-181d-399a-8abc-f0322f8077ec | -9.80569 | -38.09586 | 2025-02-28 03:59:00 | NOAA-20 | SANTA BRÍGIDA | BAHIA | Brasil | 2927606 | 29 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 624b4b78-d063-301b-a967-2e899f81a41b | -6.63648 | -44.57949 | 2025-02-28 03:59:00 | NOAA-20 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 55186169-1563-3b0c-a0d7-39d6b310686a | -19.01 | -42.16418 | 2025-02-28 04:01:00 | NOAA-20 | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 411f790a-144d-321e-8e60-4ecb8ac8cf68 | -15.56661 | -47.85548 | 2025-02-28 04:01:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3b64445b-ce68-3dd4-a78c-8455b8167dc6 | -19.37468 | -46.04758 | 2025-02-28 04:01:00 | NOAA-20 | SÃO GOTARDO | MINAS GERAIS | Brasil | 3162104 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| faad6a6d-f758-3d7e-b333-003159b38afd | -17.112 | -48.42637 | 2025-02-28 04:01:00 | NOAA-20 | PIRES DO RIO | GOIÁS | Brasil | 5217401 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d7dd35db-1b41-3867-8256-361e067b2250 | -16.40716 | -45.08333 | 2025-02-28 04:01:00 | NOAA-20 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 305ccbda-07d1-3777-bbcf-ce00cfc72c88 | -17.38488 | -42.65765 | 2025-02-28 04:01:00 | NOAA-20 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 7ca40126-d44c-3e2e-a91c-dbb41f722101 | -14.41298 | -43.48586 | 2025-02-28 04:01:00 | NOAA-20 | IUIU | BAHIA | Brasil | 2917334 | 29 | 33 | nan | nan | nan | Cerrado | 0.3 |
| b6458261-6126-36bf-a7d6-abdbdff8f940 | -15.55802 | -46.27608 | 2025-02-28 04:01:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 601b7704-d24a-317c-9c3f-8fe8818e5129 | -15.07767 | -48.94382 | 2025-02-28 04:01:00 | NOAA-20 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 9106d427-1f85-3d3d-affc-c7736a6e684c | -14.85649 | -46.79418 | 2025-02-28 04:01:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5e04aa1c-8974-35b0-bb0d-5d5ec4d66d88 | -17.11126 | -48.43031 | 2025-02-28 04:01:00 | NOAA-20 | PIRES DO RIO | GOIÁS | Brasil | 5217401 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| df66f604-57d3-3db4-bd74-742d20276b40 | -17.45071 | -47.02696 | 2025-02-28 04:01:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d6615cf9-b085-3b59-815d-3bf5a513b907 | -13.49719 | -43.61106 | 2025-02-28 04:01:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 5570c281-d232-3dc1-b80a-801df523198b | -15.55339 | -46.28014 | 2025-02-28 04:01:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3b112d9c-fd90-3d0a-bdc3-e3db9dcf022f | -15.3751 | -43.71897 | 2025-02-28 04:01:00 | NOAA-20 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 1.1 |
| f10de949-3782-3e8b-b884-cec84e6346df | -19.27291 | -47.33259 | 2025-02-28 04:01:00 | NOAA-20 | PERDIZES | MINAS GERAIS | Brasil | 3149804 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 56414365-1f54-31a0-aa79-64f4d70adce1 | -19.43746 | -44.34169 | 2025-02-28 04:01:00 | NOAA-20 | SETE LAGOAS | MINAS GERAIS | Brasil | 3167202 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0c5d5b11-2584-3b48-a799-a7d11bc0ab71 | -19.00724 | -42.15992 | 2025-02-28 04:01:00 | NOAA-20 | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| cf93dcd1-67de-38b4-a3ec-fe9fb737f84e | -19.2738 | -47.32773 | 2025-02-28 04:01:00 | NOAA-20 | PERDIZES | MINAS GERAIS | Brasil | 3149804 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4def90ce-e1bd-36f5-b42a-fe62be60874a | -19.9794 | -44.85952 | 2025-02-28 04:01:00 | NOAA-20 | SÃO GONÇALO DO PARÁ | MINAS GERAIS | Brasil | 3161809 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 02c615ac-1280-3e54-84be-546e7dd18003 | -19.71616 | -40.35249 | 2025-02-28 04:01:00 | NOAA-20 | JOÃO NEIVA | ESPÍRITO SANTO | Brasil | 3203130 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 0b9821fe-ed2e-308e-86c7-2793aa1e9fa4 | -19.00668 | -42.16359 | 2025-02-28 04:01:00 | NOAA-20 | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| c477880d-a49a-3a12-a6b6-5998e97a09c3 | -19.96921 | -44.21677 | 2025-02-28 04:01:00 | NOAA-20 | BETIM | MINAS GERAIS | Brasil | 3106705 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 91177da3-e0c9-3d95-9dda-d69e3581e269 | -22.9603 | -42.86514 | 2025-02-28 04:04:00 | NOAA-20 | MARICÁ | RIO DE JANEIRO | Brasil | 3302700 | 33 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| ee486a34-a38d-33e2-9239-75e7ef4e9b80 | -22.5711 | -42.07105 | 2025-02-28 04:04:00 | NOAA-20 | CABO FRIO | RIO DE JANEIRO | Brasil | 3300704 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| f248639f-ca42-3291-9853-d1a94253c96d | -22.85503 | -42.97971 | 2025-02-28 04:04:00 | NOAA-20 | SÃO GONÇALO | RIO DE JANEIRO | Brasil | 3304904 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 445df36a-94fb-3696-a15c-e96e6043b17b | -20.99646 | -51.79494 | 2025-02-28 04:04:00 | NOAA-20 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 72794d9d-6834-3b58-b9f4-21cb29503fbc | -21.91285 | -42.2612 | 2025-02-28 04:04:00 | NOAA-20 | CANTAGALO | RIO DE JANEIRO | Brasil | 3301108 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 8322cbb8-bd8c-3cdd-a070-715de39ad055 | -23.20636 | -50.80853 | 2025-02-28 04:04:00 | NOAA-20 | URAÍ | PARANÁ | Brasil | 4128401 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 1cf25f82-594f-331e-8b3d-5bf7b1fcc86a | -23.33746 | -46.77232 | 2025-02-28 04:04:00 | NOAA-20 | CAIEIRAS | SÃO PAULO | Brasil | 3509007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| c27e8c11-69c8-33ec-9b10-cefa99935ccf | -20.85281 | -41.08004 | 2025-02-28 04:04:00 | NOAA-20 | CACHOEIRO DE ITAPEMIRIM | ESPÍRITO SANTO | Brasil | 3201209 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 517ffcbe-81df-3efc-9fd9-d3b422bd1a73 | -23.20544 | -50.81308 | 2025-02-28 04:04:00 | NOAA-20 | URAÍ | PARANÁ | Brasil | 4128401 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| fe41d64a-31c6-36b2-97b9-535e247e1f70 | -22.67396 | -42.85543 | 2025-02-28 04:04:00 | NOAA-20 | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| d01169f7-e0b8-3329-a752-a8f624625b49 | -22.10658 | -48.27087 | 2025-02-28 04:04:00 | NOAA-20 | DOURADO | SÃO PAULO | Brasil | 3514304 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 46857872-06a6-3c05-90d9-b094373183a6 | -20.70092 | -41.71556 | 2025-02-28 04:04:00 | NOAA-20 | GUAÇUÍ | ESPÍRITO SANTO | Brasil | 3202306 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 4555d51a-be88-3364-acd9-069adc2bc7c6 | -22.10884 | -48.26833 | 2025-02-28 04:04:00 | NOAA-20 | DOURADO | SÃO PAULO | Brasil | 3514304 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 89e036e4-577d-36f9-b65e-5d0555446720 | -21.18027 | -44.2723 | 2025-02-28 04:04:00 | NOAA-20 | SÃO JOÃO DEL REI | MINAS GERAIS | Brasil | 3162500 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| eb3f24ab-2fd4-3011-bbd9-60bf4140acd5 | -22.87285 | -42.97506 | 2025-02-28 04:04:00 | NOAA-20 | SÃO GONÇALO | RIO DE JANEIRO | Brasil | 3304904 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 37581e2d-88d0-3271-b7bd-beedb95baa89 | -22.77814 | -43.32542 | 2025-02-28 04:04:00 | NOAA-20 | DUQUE DE CAXIAS | RIO DE JANEIRO | Brasil | 3301702 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| d467ccb9-5beb-319b-9523-186717d7aad8 | -22.53997 | -48.81353 | 2025-02-28 04:04:00 | NOAA-20 | MACATUBA | SÃO PAULO | Brasil | 3528007 | 35 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4f79efc2-7d0c-372c-adda-9a70abcc2560 | -21.19662 | -44.93684 | 2025-02-28 04:04:00 | NOAA-20 | IJACI | MINAS GERAIS | Brasil | 3130408 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 2556f8a8-a1dc-360f-a019-07b13f2af61a | -20.94163 | -45.71206 | 2025-02-28 04:04:00 | NOAA-20 | ILICÍNEA | MINAS GERAIS | Brasil | 3130507 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| ec97f352-f879-33e7-bf15-e8b76c1d0aad | -21.04895 | -47.78499 | 2025-02-28 04:04:00 | NOAA-20 | JARDINÓPOLIS | SÃO PAULO | Brasil | 3525102 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9481e5c2-8eca-32d7-a69b-1df332dc437f | -21.07026 | -43.88194 | 2025-02-28 04:04:00 | NOAA-20 | CARANDAÍ | MINAS GERAIS | Brasil | 3113206 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| a30ad528-70c3-35cb-a933-2ef797b1d6f5 | -22.95697 | -42.86454 | 2025-02-28 04:04:00 | NOAA-20 | MARICÁ | RIO DE JANEIRO | Brasil | 3302700 | 33 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| 3447a53f-77f1-3dbc-94c6-593d141b8104 | -21.6138 | -48.4672 | 2025-02-28 04:04:00 | NOAA-20 | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 582bab46-f512-3eff-9705-128105ecb98e | -22.6773 | -42.85602 | 2025-02-28 04:04:00 | NOAA-20 | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| b228b1ec-790a-31d4-bb9e-088ed80b526e | -21.6128 | -48.4726 | 2025-02-28 04:04:00 | NOAA-20 | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 2.9 |
| fadd176b-ed99-3d25-8278-8436ecb52c1f | -23.40462 | -46.5574 | 2025-02-28 04:04:00 | NOAA-20 | SÃO PAULO | SÃO PAULO | Brasil | 3550308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 7b86eb0b-e195-3fad-b51f-9e4b07ef1b22 | -22.22361 | -42.82652 | 2025-02-28 04:04:00 | NOAA-20 | TERESÓPOLIS | RIO DE JANEIRO | Brasil | 3305802 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 4aa0f039-2b76-315e-82a4-76846628378b | -22.74705 | -42.37013 | 2025-02-28 04:04:00 | NOAA-20 | ARARUAMA | RIO DE JANEIRO | Brasil | 3300209 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 5b736f8f-c337-34c1-937c-0efe0780eb25 | -1.5652 | -54.3592 | 2025-02-28 04:50:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 21b1d7bb-05fb-3c6a-a4b5-8332d34742a7 | 2.10525 | -61.8239 | 2025-02-28 04:50:00 | NOAA-21 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 053928ae-25e9-3550-8bec-066f3c5ae47b | 3.21051 | -60.23947 | 2025-02-28 04:50:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| da299e61-9eb9-337a-a2f1-eec05f8104b6 | 1.2753 | -60.0772 | 2025-02-28 04:50:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 766e7914-86b5-3bfc-8db2-f6809175100d | 2.1062 | -61.82144 | 2025-02-28 04:50:00 | NOAA-21 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6694f8eb-d4d6-3440-a9ce-569b1bf118a4 | 2.1055 | -61.81672 | 2025-02-28 04:50:00 | NOAA-21 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e9b6d784-4f79-30b8-acde-eb294c899f13 | -1.66511 | -55.58452 | 2025-02-28 04:50:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| bd575305-bf17-323b-b671-4e7c1f220537 | 2.29589 | -61.05358 | 2025-02-28 04:50:00 | NOAA-21 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ea125463-8cbb-346c-96aa-756ab2df9991 | 2.11059 | -61.81831 | 2025-02-28 04:50:00 | NOAA-21 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0b7151dc-9d65-3451-a073-fcb86764246c | 0.83025 | -59.94863 | 2025-02-28 04:50:00 | NOAA-21 | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 95d14562-375a-3218-a724-da2459b77c00 | 2.11224 | -61.82037 | 2025-02-28 04:50:00 | NOAA-21 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a267bd6d-e6bb-34ba-b645-863d871f2d60 | 1.31221 | -60.06817 | 2025-02-28 04:50:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| acd83269-2eb2-384c-a698-d65843c92131 | -2.53521 | -53.9577 | 2025-02-28 04:50:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a812d3f0-0e7f-3300-9de6-3f509606c3f7 | -1.56456 | -54.36317 | 2025-02-28 04:50:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e4a894c5-4c71-3f02-8a18-17e3f0c1b87c | -1.5681 | -54.36376 | 2025-02-28 04:50:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 844f5a3a-272f-312a-8527-352ef66a591a | 2.10454 | -61.81931 | 2025-02-28 04:50:00 | NOAA-21 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9419f942-9b09-3a49-aac0-36c6b259b0ae | 2.1113 | -61.82285 | 2025-02-28 04:50:00 | NOAA-21 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 23c329fe-50d5-3898-820a-0020fa22c22e | 2.29522 | -61.04918 | 2025-02-28 04:50:00 | NOAA-21 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0eac1280-e343-3617-ad7e-3bc0c18da690 | 2.51102 | -60.98101 | 2025-02-28 04:50:00 | NOAA-21 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 29b0788f-fddb-315d-a672-2833fe817d01 | 2.10686 | -61.82597 | 2025-02-28 04:50:00 | NOAA-21 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d7b8bf8b-6611-371c-95f3-d479333237ad | 2.51166 | -60.98179 | 2025-02-28 04:50:00 | NOAA-21 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 57cff173-db47-3115-a93e-8dd53ed5c667 | 1.28486 | -60.10346 | 2025-02-28 04:50:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5b4ff5df-16e3-3f06-b4e0-f140c0a4f84f | 2.11291 | -61.82489 | 2025-02-28 04:50:00 | NOAA-21 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7ba9fdb3-09b1-3222-b4d9-83a34e9b1353 | -15.5564 | -46.2802 | 2025-02-28 04:53:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 10c283d1-712a-3f67-bee0-b7d263dc172f | -17.11124 | -48.42659 | 2025-02-28 04:53:00 | NOAA-21 | PIRES DO RIO | GOIÁS | Brasil | 5217401 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6c9ebaf1-1313-325d-b607-d8924f562891 | -15.55676 | -46.27716 | 2025-02-28 04:53:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7795c70c-eb39-3b6d-9f33-80c2dcea82b7 | -15.07947 | -48.94533 | 2025-02-28 04:53:00 | NOAA-21 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 87837bd2-ce2f-3849-b6db-a847a10cf44c | -6.60149 | -44.18401 | 2025-02-28 04:53:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 139fe3ed-f2b5-3fe9-bf74-e21cab2da109 | -6.54465 | -44.48265 | 2025-02-28 04:53:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ff890617-9404-35fe-b994-9d742359c9aa | -11.02819 | -45.17886 | 2025-02-28 04:53:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 72213e75-6d50-3c48-9b21-44e6c0128b00 | -11.02398 | -45.18198 | 2025-02-28 04:53:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| b0a0bd12-5081-322c-9332-754d3faa71c3 | -6.97083 | -43.01156 | 2025-02-28 04:53:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 5881c2d1-cbee-33c0-ad88-684df5aa983b | -6.54924 | -44.48633 | 2025-02-28 04:53:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 268f3d26-c329-3109-b7cf-a0efad5d6ca4 | -6.96528 | -43.01073 | 2025-02-28 04:53:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 695eb5e6-4b90-33c6-ab1f-7cf91304e618 | -11.02947 | -45.17953 | 2025-02-28 04:53:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3be01ba3-178d-3a2c-a9ab-f943f3471df8 | -6.96578 | -43.00704 | 2025-02-28 04:53:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 6bf97d4b-2695-3c18-97bf-228a49536cf4 | -10.50087 | -42.40838 | 2025-02-28 04:53:00 | NOAA-21 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 2.5 |
| f0036846-f6ec-3220-b845-165e53bb8fe5 | -11.87795 | -44.38209 | 2025-02-28 04:53:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2c89e86e-18ff-3523-a377-89be026d8c87 | -11.02438 | -45.17892 | 2025-02-28 04:53:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1663699d-8f1c-3969-aefc-04d45c0bd4bf | -11.02782 | -45.18191 | 2025-02-28 04:53:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 174db45c-3d77-3bae-9068-2a6ad8f6ec9f | -11.88136 | -44.38379 | 2025-02-28 04:53:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8d076836-78ce-3073-ae9e-53328e8b14cd | -6.54964 | -44.48343 | 2025-02-28 04:53:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c80ba422-02e1-3b4b-a133-0d8ffa4c04bc | -11.02907 | -45.18258 | 2025-02-28 04:53:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| e1f4bb3e-8ef0-3079-b0d7-9b26d3c5fb12 | -6.60193 | -44.18082 | 2025-02-28 04:53:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 37d7ab4a-4b83-3534-b00a-6f7dcdab7a02 | -23.11737 | -55.28844 | 2025-02-28 04:55:00 | NOAA-21 | AMAMBAI | MATO GROSSO DO SUL | Brasil | 5000609 | 50 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 44a79ca0-dd5a-3337-bb2b-14710856a1d4 | -25.10832 | -52.73055 | 2025-02-28 04:55:00 | NOAA-21 | GUARANIAÇU | PARANÁ | Brasil | 4109302 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 90687b99-7b56-34a7-8a99-6a6a863e4719 | -23.2056 | -50.80685 | 2025-02-28 04:55:00 | NOAA-21 | URAÍ | PARANÁ | Brasil | 4128401 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |


[Clique aqui para ver as próximas entradas](README3.md)
