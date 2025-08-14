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

## Dados Diários - Página 31

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a59e9485-b0d9-3d97-b3f7-f1d250626d8b | -5.73939 | -59.88965 | 2025-08-14 05:10:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 010d8490-733a-3539-b383-a7e581566913 | -6.94572 | -44.5498 | 2025-08-14 05:10:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 63160aff-a793-3c2f-b2ed-d0a0a60bcc4a | -6.90952 | -59.63154 | 2025-08-14 05:10:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ce8860aa-cd26-3a88-ada6-ec0801461d50 | -5.76107 | -59.88908 | 2025-08-14 05:10:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| abc980a0-d4a6-339f-a283-d0928a0c0ed8 | -6.08939 | -59.94703 | 2025-08-14 05:10:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 74c75476-1f61-32fd-936f-cca81934183d | -5.97973 | -44.14965 | 2025-08-14 05:10:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| d1ab6909-89f0-39d5-a16f-f8a0ae30a24c | -7.623 | -63.51994 | 2025-08-14 05:10:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 04a0362e-a1da-3567-ad2e-6908d33453a9 | -5.79654 | -59.22719 | 2025-08-14 05:10:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c5536e49-b631-36e4-b878-faece3fb4e11 | -6.91534 | -59.14096 | 2025-08-14 05:10:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 4f18ec1f-9b88-3cad-9004-fba8dbec3e57 | -8.30775 | -55.11029 | 2025-08-14 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d3bad616-5384-3a28-a848-91f35e0606b1 | -6.53258 | -56.21048 | 2025-08-14 05:10:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bcfa3f06-2015-3835-9517-c03a3150616e | -8.80366 | -52.04097 | 2025-08-14 05:10:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4fcb9d7a-8b6b-357e-a143-a58a3318eebe | -7.46481 | -57.65344 | 2025-08-14 05:10:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3052be8a-e781-3c33-b23f-2d0342f92085 | -7.11981 | -59.41666 | 2025-08-14 05:10:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 92a6d114-148b-350b-ae31-62aab1ed5f70 | -7.31624 | -60.62026 | 2025-08-14 05:10:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| a7785aa2-db11-3249-b5cb-f4ca72496755 | -7.23506 | -57.64576 | 2025-08-14 05:10:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0da6f994-bb5b-3d99-a3c7-84d3abb10e35 | -9.15222 | -59.66738 | 2025-08-14 05:10:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 12.1 |
| eb7010a9-894c-301f-bd69-4d31fa2a36a8 | -8.11046 | -61.21252 | 2025-08-14 05:10:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 29104150-5a7a-3c54-88d4-65d45d545308 | -7.14105 | -60.12241 | 2025-08-14 05:10:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c3721e7c-b41a-3cb2-ab4f-af0e8247d3fc | -8.92979 | -60.72746 | 2025-08-14 05:10:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f2e11d5c-3451-35a5-ae5f-f6a09a2559fb | -5.79688 | -43.61835 | 2025-08-14 05:10:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2fb4f3b4-450c-3cf7-8f7f-64ab892d7968 | -9.34352 | -58.83245 | 2025-08-14 05:10:00 | NOAA-20 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8a1cebcc-bf33-304e-858d-8b82b71e392c | -8.10448 | -61.1809 | 2025-08-14 05:10:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 26be17fe-f180-326c-9613-d3e177516b60 | -9.20558 | -59.64553 | 2025-08-14 05:10:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fea30fe8-b0ac-300f-bdfd-347adc124191 | -9.49861 | -60.51223 | 2025-08-14 05:10:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d0fb7c0c-59e8-37e7-a22f-c1d1d9f4a660 | -9.16575 | -59.66961 | 2025-08-14 05:10:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7a5cc4da-009b-3772-9ba2-be81114ba40d | -6.64412 | -59.07887 | 2025-08-14 05:10:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3929e533-1e45-354d-9488-21243d999b67 | -7.12375 | -59.6303 | 2025-08-14 05:10:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 1f1c2985-cc60-377c-a0ac-66ca90187e0a | -10.34678 | -57.59473 | 2025-08-14 05:10:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0524b47d-e9dd-337b-b799-9b638e58ecd7 | -7.14454 | -60.12299 | 2025-08-14 05:10:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 290eebcc-c5bd-3541-8515-e8d806b961bd | -7.12457 | -60.12825 | 2025-08-14 05:10:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6b5b2859-503a-3cb0-b845-57cd77af1680 | -5.74892 | -59.87511 | 2025-08-14 05:10:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4adcfb2e-6f41-345e-883e-aac34b87d630 | -5.74002 | -59.88575 | 2025-08-14 05:10:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f972198a-aa92-34ec-acdd-1e35296bdebc | -7.28799 | -55.30598 | 2025-08-14 05:10:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 739c2945-d79b-33d9-81a9-5c6fac7f7742 | -7.8734 | -61.82143 | 2025-08-14 05:10:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 206e64da-6ee0-3d66-93e6-778ab7eba072 | -5.74164 | -59.89802 | 2025-08-14 05:10:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f0466097-c5e0-3f38-a9fd-994e5534cf76 | -6.87977 | -59.14638 | 2025-08-14 05:10:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 85edf106-170d-3598-8fea-5faaac913017 | -6.65467 | -58.81814 | 2025-08-14 05:10:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 21a4793b-5781-37c1-bf39-2d031fa48f2e | -8.6874 | -63.00476 | 2025-08-14 05:10:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4815896d-bc60-31be-9385-5a67ea22a8a6 | -7.87117 | -61.8116 | 2025-08-14 05:10:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d086096b-7f43-355d-95db-76d2a933bd50 | -7.89992 | -63.52631 | 2025-08-14 05:10:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5f2cae14-4fa8-3666-aae0-a4bc1e3ee92b | -6.90858 | -59.13988 | 2025-08-14 05:10:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.7 |
| d2087d19-b286-33fb-881b-5e588c0c8ed1 | -9.50364 | -60.525 | 2025-08-14 05:10:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 6.0 |
| cd5dd6f4-301f-3298-8355-415c3f0e4b79 | -6.87462 | -59.15673 | 2025-08-14 05:10:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.1 |
| d75c8a7d-c95c-3d1d-9c74-9555e3bcf0f3 | -9.63949 | -63.15408 | 2025-08-14 05:10:00 | NOAA-20 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0c93d5a1-21b1-32bb-b781-7bc7bc2dfcb5 | -5.75468 | -59.88404 | 2025-08-14 05:10:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 73022b2b-ba78-311f-8822-64328c51e555 | -8.10378 | -61.18515 | 2025-08-14 05:10:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b7124b90-352e-388f-adfa-32b4af458389 | -7.49713 | -61.31345 | 2025-08-14 05:10:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e1a171d0-9ab4-3fa7-a85e-9abe2dfd9c6a | -6.69469 | -59.13908 | 2025-08-14 05:10:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b71c6c3a-5e12-3245-b8a2-419f81fc9fe3 | -6.89623 | -59.13043 | 2025-08-14 05:10:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a42da4da-9550-34fb-9a7b-97a2a7a471a3 | -9.38812 | -61.53299 | 2025-08-14 05:10:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4c1fb978-f91f-3c27-b12b-91e228d19c62 | -6.10726 | -59.92575 | 2025-08-14 05:10:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 73d0140e-31f0-3e2c-9f96-5d1019820a7f | -5.89174 | -57.74047 | 2025-08-14 05:10:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| d63545b8-d5ab-3b7a-94e2-8b2e90eadcc2 | -9.21115 | -59.65396 | 2025-08-14 05:10:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 041bcd89-93ce-312e-bddc-00afaa46f9ce | -6.10025 | -59.92466 | 2025-08-14 05:10:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ce0286a1-c6f6-39e5-a35f-daae5b31a155 | -7.76209 | -61.57781 | 2025-08-14 05:10:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 70713fc1-dc5a-3563-8a7c-be527aa700fc | -8.10822 | -61.20341 | 2025-08-14 05:10:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| d13a6aab-62aa-362f-aa76-311a15cd1b21 | -6.93699 | -59.63602 | 2025-08-14 05:10:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 80f7eee3-3fd7-3201-ac14-e3d1d42d35e3 | -6.95247 | -44.55133 | 2025-08-14 05:10:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 908bb7dc-1931-35ec-b82d-e8a8677ebbfe | -5.7429 | -59.89021 | 2025-08-14 05:10:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3226e6a4-534f-37c6-aebc-32ee20010623 | -7.60192 | -63.51627 | 2025-08-14 05:10:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 5fa7838a-2e5f-39d5-b151-fa267a541d94 | -7.13506 | -60.12992 | 2025-08-14 05:10:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| aab11abf-b8fc-3e8d-9da5-7fbe1a06434d | -7.32338 | -60.62144 | 2025-08-14 05:10:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c667525c-c042-3fb8-9d7f-edb73442e241 | -7.07298 | -59.20323 | 2025-08-14 05:10:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 828b3241-2328-32dd-b301-ce08744e63bd | -9.19069 | -59.67304 | 2025-08-14 05:10:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d3176ae0-e773-3601-a53a-d3031e516dc6 | -6.88874 | -59.15528 | 2025-08-14 05:10:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 14.2 |
| 0bcc1fcb-0d7a-3332-9b65-abdd54b00fea | -9.18791 | -59.66882 | 2025-08-14 05:10:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| aba0e87e-6054-33f8-90f4-531fc444aadb | -7.56032 | -63.48075 | 2025-08-14 05:10:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 087a6bff-1a7f-3aaa-86dc-9f4a5907818a | -7.13844 | -59.64814 | 2025-08-14 05:10:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 72fe6df1-eb87-35aa-a18e-fa57a140e31f | -9.46042 | -63.14738 | 2025-08-14 05:10:00 | NOAA-20 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 444d80a1-f244-3ce8-80d9-58532d0702eb | -7.62367 | -63.51601 | 2025-08-14 05:10:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 00e180de-3f4c-3b38-baad-bf75bfa601ec | -7.23921 | -60.0033 | 2025-08-14 05:10:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 52b20b5d-4ef2-3e37-a4a3-f545e63c44d4 | -6.91417 | -59.14823 | 2025-08-14 05:10:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 8269d68d-aa44-390a-8c70-c62612400983 | -5.88843 | -57.73995 | 2025-08-14 05:10:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 2a3e5c01-81ae-3332-bb24-cd3bc28a8481 | -6.08368 | -59.95464 | 2025-08-14 05:10:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 5.8 |
| f0eb0aa0-5159-3c9b-842c-4bf7c12feae8 | -9.20896 | -59.6461 | 2025-08-14 05:10:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f88adb8e-8276-30e2-88c7-d507db7f38ad | -6.87139 | -59.13385 | 2025-08-14 05:10:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 20bd1a20-93cf-3db3-8b7b-d8f2b26f1ae6 | -7.12869 | -60.12489 | 2025-08-14 05:10:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| c1f7cac9-e46f-32a1-9b85-ab2cc74bd0cc | -9.13133 | -59.6677 | 2025-08-14 05:10:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| ebc788a2-e0bd-39c1-a5cc-b689e23e4829 | -6.08846 | -59.93081 | 2025-08-14 05:10:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6cb0ddb7-1587-3b93-806a-5efb85721718 | -8.10529 | -61.19854 | 2025-08-14 05:10:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 7f6e7cc1-ef40-34c4-b15e-d46a3010d7b7 | -6.93821 | -59.62853 | 2025-08-14 05:10:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f2376c33-39dd-34a6-96a2-375a73a0d8d2 | -7.26394 | -60.63349 | 2025-08-14 05:10:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6cb6f3bc-4b45-3f0a-bb6f-0b6d6b6a4dd1 | -7.13219 | -60.12545 | 2025-08-14 05:10:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d9564f53-695d-3618-a40a-b4f9207fbef8 | -7.1041 | -56.76999 | 2025-08-14 05:10:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 75c5a37d-6c84-308d-a699-b14750feb0db | -9.15781 | -59.67581 | 2025-08-14 05:10:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5c06652f-8519-36ea-ac87-0638df47aaa8 | -7.87949 | -61.80827 | 2025-08-14 05:10:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 309d4c61-ca93-387f-92ff-0bd9ea4f486f | -5.74704 | -59.88684 | 2025-08-14 05:10:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2768af56-b9b4-327d-8a2f-83c98b3f850c | -6.89446 | -59.14133 | 2025-08-14 05:10:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ba687f9b-6f27-3418-ad7a-fcaca918e354 | -8.93331 | -60.72807 | 2025-08-14 05:10:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| cc719f7a-b86b-3b47-8dd4-f9d9ba8a3d7d | -5.75819 | -59.8846 | 2025-08-14 05:10:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 511a3e79-a9bc-3918-8a39-b67e6db39c0c | -7.28852 | -57.65065 | 2025-08-14 05:10:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bd5bb277-3a93-3146-8b72-534f25c4828c | -6.09067 | -59.9392 | 2025-08-14 05:10:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 9ae8fd34-8881-3fe8-be6a-1c3ca3edbf48 | -6.87874 | -59.13134 | 2025-08-14 05:10:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 10100a40-19ae-30d3-b63a-e5f9f4308b28 | -7.23561 | -57.6423 | 2025-08-14 05:10:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8b8ab3d7-9caa-33f9-bda4-402461615828 | -7.14803 | -60.12359 | 2025-08-14 05:10:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c776c9da-9f92-3d74-89aa-92308df7fa18 | -9.50802 | -60.54168 | 2025-08-14 05:10:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1e28925e-df94-38d0-b025-36dffd571b1d | -7.13156 | -60.12936 | 2025-08-14 05:10:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 90c9e2fb-af58-38a7-bf4b-98685e73aea9 | -6.88432 | -59.13969 | 2025-08-14 05:10:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bb3e8d4c-1380-3912-bbbf-c4d2e662346e | -6.08653 | -59.94255 | 2025-08-14 05:10:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 8.4 |


[Clique aqui para ver as próximas entradas](README32.md)
