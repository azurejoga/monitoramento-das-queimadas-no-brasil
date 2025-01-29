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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| af82d771-d05d-3afc-a05f-e0d87e0dbcd5 | -6.9466 | -43.53492 | 2025-01-29 04:14:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 4b387d4d-b60a-3cd9-adde-53f705b9e65d | -8.71712 | -44.00621 | 2025-01-29 04:14:00 | NOAA-21 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 83da877e-f637-3a9b-bf54-d84e4db018d2 | -6.32708 | -43.36193 | 2025-01-29 04:14:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f4a092fd-19b6-309e-a0de-090ce6c6779a | -6.93723 | -43.52991 | 2025-01-29 04:14:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 8.5 |
| a7d35f60-baf4-34f4-92eb-7edcd0a59bf3 | -6.93669 | -43.53337 | 2025-01-29 04:14:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 8.5 |
| b3b0fe9c-71b6-3102-b98e-ec7f5db4e8fd | -6.94714 | -43.53146 | 2025-01-29 04:14:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 0dd79744-8ef4-3e4d-949d-714927f30d84 | -6.93063 | -43.52887 | 2025-01-29 04:14:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 567c6f31-34aa-3d03-ad6f-276cc652270c | -11.79957 | -49.32394 | 2025-01-29 04:16:00 | NOAA-21 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 53d7f37e-b503-3be4-95fc-aa9687ed2ce4 | -11.13789 | -54.22391 | 2025-01-29 04:16:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| cb7d048e-4429-31fa-be03-dac61cc910c1 | -13.41277 | -41.34452 | 2025-01-29 04:16:00 | NOAA-21 | IBICOARA | BAHIA | Brasil | 2912202 | 29 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 6f22d9a7-c979-3b6d-bf07-63f768815832 | -14.7001 | -47.31128 | 2025-01-29 04:16:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 6560283b-1169-3811-8896-9065d74319c8 | -18.03928 | -39.9245 | 2025-01-29 04:16:00 | NOAA-21 | MUCURI | BAHIA | Brasil | 2922003 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 468b2fee-2b0a-32a9-93bc-47ec2077163e | -15.29827 | -47.90366 | 2025-01-29 04:16:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8b650d98-6478-308e-b8b5-50ea3188f55b | -15.29544 | -47.8989 | 2025-01-29 04:16:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 5e177191-f58f-3b56-8a17-9bc11527040e | -11.80418 | -49.3211 | 2025-01-29 04:16:00 | NOAA-21 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c87f096f-b428-30aa-bc87-9a46b2fcddd1 | -14.12096 | -41.67594 | 2025-01-29 04:16:00 | NOAA-21 | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 18af7595-bde8-3e81-80fd-c6bf148502cd | -16.08828 | -39.40826 | 2025-01-29 04:16:00 | NOAA-21 | EUNÁPOLIS | BAHIA | Brasil | 2910727 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 565e2da8-a050-3119-819a-848b7ae91798 | -17.00924 | -49.77971 | 2025-01-29 04:16:00 | NOAA-21 | CEZARINA | GOIÁS | Brasil | 5205455 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| aa53345e-0daa-31bc-be50-9013dd9ac8e9 | -12.90093 | -45.05724 | 2025-01-29 04:16:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| de0518b8-2f26-3e73-9c0e-ffc98f0c60ad | -13.15866 | -42.29026 | 2025-01-29 04:16:00 | NOAA-21 | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 41e64ea1-060d-3016-bdbd-69d43ef06d5e | -15.713 | -39.04084 | 2025-01-29 04:16:00 | NOAA-21 | CANAVIEIRAS | BAHIA | Brasil | 2906303 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| a4151b1d-d516-36ac-8275-6c2941dfbe7c | -13.15921 | -42.29145 | 2025-01-29 04:16:00 | NOAA-21 | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| aa7d0fa6-ecdb-3ac6-b623-8166bf069672 | -15.07887 | -48.94591 | 2025-01-29 04:16:00 | NOAA-21 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| bca06345-d153-3405-acb1-c0937e075b66 | -12.90423 | -45.05778 | 2025-01-29 04:16:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e9cd8d4b-756e-3954-86c7-ebb667c2ee25 | -12.89868 | -45.07139 | 2025-01-29 04:16:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| fcfb54b3-a006-3905-8693-67bb4c769612 | -12.89925 | -45.06785 | 2025-01-29 04:16:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 51218aed-0af8-3c8b-a1d1-3a12d5748b86 | -13.98488 | -41.82344 | 2025-01-29 04:16:00 | NOAA-21 | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 8166b92b-3406-3c6c-9ca3-1049b14f95c4 | -11.80357 | -49.32467 | 2025-01-29 04:16:00 | NOAA-21 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 34aafdd6-67f3-36f1-99f0-b9ef0a97065e | -13.66623 | -50.62991 | 2025-01-29 04:16:00 | NOAA-21 | NOVA CRIXÁS | GOIÁS | Brasil | 5214838 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3f66a952-1d5d-3d74-a509-55076127dac2 | -15.5595 | -43.13929 | 2025-01-29 04:16:00 | NOAA-21 | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 9029a177-349c-31d3-9f35-643d592a7755 | -19.30391 | -48.39028 | 2025-01-29 04:16:00 | NOAA-21 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9adf08ce-e2aa-3794-8baa-8d89e84586b2 | -12.86342 | -45.67416 | 2025-01-29 04:16:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 19cf5683-2870-3dc3-b206-2b5ea0e67ca6 | -12.90255 | -45.06839 | 2025-01-29 04:16:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c0824b48-dd14-3e2e-ba1c-4b037e4fc4ef | -13.98411 | -41.82599 | 2025-01-29 04:16:00 | NOAA-21 | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 99b1cf96-3b8d-3aa3-869e-9c3a602b63a1 | -15.56823 | -47.85655 | 2025-01-29 04:16:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cee7caec-7f49-3bd8-a57e-4181929b4db5 | -18.19586 | -47.97179 | 2025-01-29 04:16:00 | NOAA-21 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2fae22b1-75ee-392d-8685-bfa3b012de1e | -11.1323 | -54.22276 | 2025-01-29 04:16:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f8abb01c-d9c9-3d88-84f5-dcdea426dedf | -14.32102 | -57.61036 | 2025-01-29 04:16:00 | NOAA-21 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 8930cd45-96bc-3b46-8f4a-15514b11d016 | -14.32033 | -57.61155 | 2025-01-29 04:16:00 | NOAA-21 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| e2b699e9-ae4a-3a62-ade2-f79fc6ec57ee | -13.98428 | -41.82754 | 2025-01-29 04:16:00 | NOAA-21 | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 312b16ba-d5f1-3376-b2f5-94ee03ffd457 | -12.9053 | -45.07247 | 2025-01-29 04:16:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 57cc50a7-796b-3af1-bc00-72c5d8bb963e | -11.4562 | -52.92129 | 2025-01-29 04:16:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4f4e251d-db8c-3e77-8ee8-2e59fb48aa35 | -13.41335 | -41.34037 | 2025-01-29 04:16:00 | NOAA-21 | IBICOARA | BAHIA | Brasil | 2912202 | 29 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 5c473a8c-0e79-347d-a688-773b630f43d9 | -20.54794 | -55.84339 | 2025-01-29 04:18:00 | NOAA-21 | ANASTÁCIO | MATO GROSSO DO SUL | Brasil | 5000708 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| eabac6ad-2d96-3a62-b711-6c922fc9a1ae | -20.70331 | -55.42569 | 2025-01-29 04:18:00 | NOAA-21 | DOIS IRMÃOS DO BURITI | MATO GROSSO DO SUL | Brasil | 5003488 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f875e2f8-ae63-343b-852d-89a4c6247b9f | -20.70264 | -55.42885 | 2025-01-29 04:18:00 | NOAA-21 | DOIS IRMÃOS DO BURITI | MATO GROSSO DO SUL | Brasil | 5003488 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 51a37823-f740-3063-949c-3c11ea107af3 | -20.90529 | -56.53758 | 2025-01-29 04:18:00 | NOAA-21 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 11a22692-1535-3c30-9b4f-046c452c31f2 | -20.69759 | -55.42772 | 2025-01-29 04:18:00 | NOAA-21 | DOIS IRMÃOS DO BURITI | MATO GROSSO DO SUL | Brasil | 5003488 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d3b430a9-257b-38f9-878b-721a50ac1a5b | -29.51357 | -51.72915 | 2025-01-29 04:21:00 | NOAA-21 | PAVERAMA | RIO GRANDE DO SUL | Brasil | 4314159 | 43 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| 73eb2f62-fd9d-3e0d-a513-3bd770172c56 | -27.08518 | -50.50954 | 2025-01-29 04:21:00 | NOAA-21 | SANTA CECÍLIA | SANTA CATARINA | Brasil | 4215505 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| a3620cee-a831-33fc-b63d-af6f883cb9e9 | -29.51369 | -51.72698 | 2025-01-29 04:21:00 | NOAA-21 | PAVERAMA | RIO GRANDE DO SUL | Brasil | 4314159 | 43 | 33 | nan | nan | nan | Mata Atlântica | 4.6 |
| 3ee2e1ce-5fc7-38d5-86ba-62ae6fd9c20c | -3.09959 | -41.86777 | 2025-01-29 04:38:00 | NPP-375D | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| fce51932-b1e1-34b8-ada2-68b7787bb4a4 | -2.80873 | -54.73121 | 2025-01-29 04:38:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d97d411a-0913-3b46-b5c9-b58c174c9950 | -3.30627 | -53.8613 | 2025-01-29 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 779be13a-5228-3b8d-9b0d-7df9c804eca2 | -3.10031 | -41.86302 | 2025-01-29 04:38:00 | NPP-375D | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 1287f5dc-6b86-35fb-b99e-fe3263ec38b7 | -2.93484 | -54.80835 | 2025-01-29 04:38:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5a09c22f-3614-31b4-a9a8-92e91aee7a95 | -3.44427 | -42.9024 | 2025-01-29 04:38:00 | NPP-375D | MILAGRES DO MARANHÃO | MARANHÃO | Brasil | 2106672 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 85fe6115-c763-3501-9390-7d948b4ce346 | -3.71988 | -53.69549 | 2025-01-29 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 68beb491-08fa-3473-9b30-7d05b453f400 | -3.3103 | -53.86195 | 2025-01-29 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3a4288dc-0581-3210-a26a-ac33890fba19 | -0.82609 | -47.58651 | 2025-01-29 04:38:00 | NPP-375D | MAGALHÃES BARATA | PARÁ | Brasil | 1504109 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d226d519-73b4-35d3-b33d-849dcc56060e | -2.8094 | -54.72707 | 2025-01-29 04:38:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d47447f2-4d95-3150-984b-a142b7919198 | -0.82697 | -47.45054 | 2025-01-29 04:38:00 | NPP-375D | MARACANÃ | PARÁ | Brasil | 1504307 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d94ef9de-425e-3bfd-9e95-9b041e8088ed | -3.41853 | -43.16263 | 2025-01-29 04:38:00 | NPP-375D | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5286b201-0664-3486-96ce-6fb4d3687b8f | -3.31834 | -54.91174 | 2025-01-29 04:38:00 | NPP-375D | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 2d01a290-10f8-31e6-979f-59df8408488e | -6.51306 | -47.59623 | 2025-01-29 04:40:00 | NPP-375D | PALMEIRAS DO TOCANTINS | TOCANTINS | Brasil | 1713809 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| ff1fa687-ec3f-3454-8e43-c441e792c37e | -7.94647 | -49.75799 | 2025-01-29 04:40:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 77605e2f-2d8e-38ce-ae35-3b35c0dede53 | -9.19762 | -49.47649 | 2025-01-29 04:40:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f6759241-a0af-3df1-ad80-9fff515dda47 | -7.9498 | -49.75852 | 2025-01-29 04:40:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 12b11c3e-b2bb-36f9-b966-7fc1e6385992 | -12.49043 | -43.78624 | 2025-01-29 04:40:00 | NPP-375D | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8a738fd1-6869-3358-8372-8d6bf589a74a | -11.45578 | -52.92133 | 2025-01-29 04:40:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| dfcff026-b815-3577-9e82-c86962e8d819 | -9.16367 | -49.4965 | 2025-01-29 04:40:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| df788ff0-0df7-3ea3-bbd0-2e330f4007eb | -11.79943 | -49.32191 | 2025-01-29 04:40:00 | NPP-375D | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 900556d9-e960-3fe7-95c4-4c20e1ca222c | -9.25609 | -60.31892 | 2025-01-29 04:40:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ee3518bb-2fcb-3c22-bbb7-9c6ee2559565 | -9.16702 | -49.49703 | 2025-01-29 04:40:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8d7bd55d-205b-30f9-b7bc-4561ea8d2c9c | -5.46526 | -42.92455 | 2025-01-29 04:40:00 | NPP-375D | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| dff85af6-2bf1-3c94-b3c4-dc22fc5f5d59 | -9.98168 | -48.08471 | 2025-01-29 04:40:00 | NPP-375D | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e0896ecb-57f1-39ed-b6b0-470d8db4d06e | -5.46592 | -42.92015 | 2025-01-29 04:40:00 | NPP-375D | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| bd6c287d-bfc9-3ea1-9d4a-d7a39416d279 | -6.51364 | -47.59246 | 2025-01-29 04:40:00 | NPP-375D | PALMEIRAS DO TOCANTINS | TOCANTINS | Brasil | 1713809 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| fa322d2e-812f-31a8-a6f7-9fe88f6ae5a0 | -10.21088 | -52.85472 | 2025-01-29 04:40:00 | NPP-375D | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| b5cde11a-bbc5-3b9e-9c46-cd2644d41677 | -7.79613 | -55.02906 | 2025-01-29 04:40:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b08b7ba3-b49e-3b16-bc2b-c8ea46852f4a | -6.51019 | -47.5919 | 2025-01-29 04:40:00 | NPP-375D | PALMEIRAS DO TOCANTINS | TOCANTINS | Brasil | 1713809 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 76a0d66c-a021-364f-a2ec-784d10feb5f3 | -4.13098 | -54.89726 | 2025-01-29 04:40:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 74f5e92b-fa1e-3508-af03-d375a123dd9a | -6.51594 | -47.60057 | 2025-01-29 04:40:00 | NPP-375D | PALMEIRAS DO TOCANTINS | TOCANTINS | Brasil | 1713809 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| c4cebf58-83ea-3591-9d92-b4e5de941e1f | -6.72155 | -47.62332 | 2025-01-29 04:40:00 | NPP-375D | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 17649957-8b59-36eb-9817-1650dd2fae12 | -12.48575 | -43.78563 | 2025-01-29 04:40:00 | NPP-375D | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1d408f8e-4280-39a9-9eb7-02bca7044829 | -11.79887 | -49.3256 | 2025-01-29 04:40:00 | NPP-375D | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 516f4066-0afe-3bb1-b26f-da7767f5edfb | -10.21684 | -59.41154 | 2025-01-29 04:40:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c2593670-2865-3743-8f53-31b5cec62096 | -11.86384 | -46.94547 | 2025-01-29 04:40:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f8c40f8c-4b43-3741-83a1-e23c8b3639e0 | -11.78032 | -44.71644 | 2025-01-29 04:40:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f8f5b957-9c17-30aa-8fae-f87e25dbdda3 | -5.459 | -42.92245 | 2025-01-29 04:40:00 | NPP-375D | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 3b3f8c73-9291-337e-8781-05a53b3e52ad | -6.49844 | -47.49396 | 2025-01-29 04:40:00 | NPP-375D | AGUIARNÓPOLIS | TOCANTINS | Brasil | 1700301 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| de1c2d0b-6c04-31b1-9d7a-94359d48f86d | -5.75104 | -43.40889 | 2025-01-29 04:40:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bccfb0a8-8401-32d7-b0ba-8079788023e8 | -9.19707 | -49.48003 | 2025-01-29 04:40:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 03dfcb27-1ae2-3fd0-a4ea-fd1dd7b3cf5f | -8.85885 | -49.88792 | 2025-01-29 04:40:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 17af9f62-3431-3bcc-87ee-08889a306f46 | -6.50149 | -47.48586 | 2025-01-29 04:40:00 | NPP-375D | AGUIARNÓPOLIS | TOCANTINS | Brasil | 1700301 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 85342d01-4181-3a41-96d4-0a19c41f9311 | -5.46856 | -42.91949 | 2025-01-29 04:40:00 | NPP-375D | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 74d2cd25-32cf-355e-ad92-a88d31f279ef | -5.45838 | -42.92682 | 2025-01-29 04:40:00 | NPP-375D | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 81a1ce2b-073d-3c24-994c-0c96533f2fd9 | -8.72009 | -44.00481 | 2025-01-29 04:40:00 | NPP-375D | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| a7cd8610-6b7f-32cf-8a07-e705bc2b25c8 | -6.50961 | -47.59568 | 2025-01-29 04:40:00 | NPP-375D | PALMEIRAS DO TOCANTINS | TOCANTINS | Brasil | 1713809 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 534200a9-e225-3c5c-914d-be4aeaec7af5 | -6.49903 | -47.49015 | 2025-01-29 04:40:00 | NPP-375D | AGUIARNÓPOLIS | TOCANTINS | Brasil | 1700301 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |


[Clique aqui para ver as próximas entradas](README4.md)
