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
| 26c5111b-840c-3488-b7b9-f3a5bbad650d | -17.0888 | -56.7915 | 2024-10-05 00:06:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 108.0 |
| 2ce8958b-c63d-3504-80af-f63dc6a95116 | -17.0892 | -56.7709 | 2024-10-05 00:06:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 122.7 |
| 85fd7000-bf86-33fc-beb0-5fbb0496bef0 | -17.1085 | -56.7892 | 2024-10-05 00:06:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 113.5 |
| dd80ecb3-aac3-3a6c-8439-92d5f8288f8e | -17.1288 | -56.7455 | 2024-10-05 00:06:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 103.5 |
| d778604f-67de-32ca-975e-2c499e7c420f | -17.684 | -42.624 | 2024-10-05 00:06:44 | GOES-16 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Mata Atlântica | 88.6 |
| ca513e15-10a3-330f-9c46-01316579dc31 | -17.6268 | -47.0057 | 2024-10-05 00:06:44 | GOES-16 | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 90.1 |
| 42c883a7-80d5-3df8-a980-9e3b8666c8c7 | -17.6273 | -46.9825 | 2024-10-05 00:06:44 | GOES-16 | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 119.2 |
| 146022a6-04c7-335c-afcc-fee4978eaed6 | -17.6473 | -46.9784 | 2024-10-05 00:06:44 | GOES-16 | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 62.0 |
| b343c081-be19-3199-b228-a990e8df1b6f | -18.4862 | -52.8226 | 2024-10-05 00:06:49 | GOES-16 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 85.0 |
| 3f628ab6-a9e9-3110-a3c3-cae121b91ec4 | -18.4867 | -52.8009 | 2024-10-05 00:06:49 | GOES-16 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 124.3 |
| d7e18e0f-ea10-3879-b718-93bbfa8fbc62 | -18.4872 | -52.7792 | 2024-10-05 00:06:49 | GOES-16 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 106.5 |
| 5694defd-2bdf-3198-8e52-4bbd3118bd89 | -18.8613 | -43.5837 | 2024-10-05 00:06:50 | GOES-16 | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 55.5 |
| 1c6306ce-77fc-3a18-922a-d2608af7696c | -18.8809 | -43.6032 | 2024-10-05 00:06:50 | GOES-16 | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 66.1 |
| 1b9f1bf3-53f9-3d6c-bb91-0412ce7d43a5 | -18.8816 | -43.5785 | 2024-10-05 00:06:50 | GOES-16 | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 69.5 |
| 0d4139c7-5063-311a-b49a-63b7c446cb00 | -18.6782 | -57.2941 | 2024-10-05 00:06:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 113.4 |
| 96cd7e85-6df4-3414-b59b-825af3a058ef | -18.6785 | -57.2734 | 2024-10-05 00:06:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 116.9 |
| fa1314e2-3d68-3e80-9f3f-f6be10e9b1d7 | -18.6981 | -57.2915 | 2024-10-05 00:06:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 70.1 |
| 8fb9187a-1283-3eb4-8ac7-99f030301fdf | -19.5096 | -42.8942 | 2024-10-05 00:06:53 | GOES-16 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 80.1 |
| 73fea516-8b6a-3d96-8739-9a2d73d5b1b0 | -20.7901 | -47.7465 | 2024-10-05 00:07:01 | GOES-16 | NUPORANGA | SÃO PAULO | Brasil | 3533601 | 35 | 33 | nan | nan | nan | Cerrado | 96.5 |
| e6618ae7-6dfd-3131-8b75-e1dd03b7f336 | -20.8107 | -47.7417 | 2024-10-05 00:07:01 | GOES-16 | SALES OLIVEIRA | SÃO PAULO | Brasil | 3544905 | 35 | 33 | nan | nan | nan | Cerrado | 77.5 |
| 99421e00-9cf1-37f6-8f9f-b52ec9114554 | -20.9378 | -49.033 | 2024-10-05 00:07:02 | GOES-16 | TABAPUÃ | SÃO PAULO | Brasil | 3552601 | 35 | 33 | nan | nan | nan | Mata Atlântica | 98.3 |
| c79b4e4b-3d0d-368b-b620-5d1294df9dbc | -20.9385 | -49.0098 | 2024-10-05 00:07:02 | GOES-16 | TABAPUÃ | SÃO PAULO | Brasil | 3552601 | 35 | 33 | nan | nan | nan | Mata Atlântica | 124.6 |
| 2125841e-a0e2-3b96-91a5-287abbf10d35 | -19.49956 | -42.91774 | 2024-10-05 00:09:00 | TERRA_M-M | SANTA MARIA DE ITABIRA | MINAS GERAIS | Brasil | 3158003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 49.8 |
| 90d1062f-d42b-3944-bc47-c868de56959d | -19.49913 | -42.92275 | 2024-10-05 00:09:00 | TERRA_M-M | SANTA MARIA DE ITABIRA | MINAS GERAIS | Brasil | 3158003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 24.1 |
| 28ef75bd-1b1f-3154-9525-012529fc38c5 | -19.49689 | -42.88858 | 2024-10-05 00:09:00 | TERRA_M-M | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 88.2 |
| f1f546bd-d08a-3aba-bd18-a163c8c84fab | -19.4963 | -42.89405 | 2024-10-05 00:09:00 | TERRA_M-M | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 116.0 |
| 3a18950e-a844-31c9-99c8-aba90c20b095 | -19.31719 | -42.58735 | 2024-10-05 00:09:00 | TERRA_M-M | SANTANA DO PARAÍSO | MINAS GERAIS | Brasil | 3158953 | 31 | 33 | nan | nan | nan | Mata Atlântica | 24.4 |
| f111f74a-f704-34c5-909e-2cce815bb249 | -19.23962 | -43.35994 | 2024-10-05 00:09:00 | TERRA_M-M | MORRO DO PILAR | MINAS GERAIS | Brasil | 3143708 | 31 | 33 | nan | nan | nan | Cerrado | 33.3 |
| 0dc971cd-faec-3b7a-af50-3a2642e4318f | -18.50739 | -39.92789 | 2024-10-05 00:09:00 | TERRA_M-M | CONCEIÇÃO DA BARRA | ESPÍRITO SANTO | Brasil | 3201605 | 32 | 33 | nan | nan | nan | Mata Atlântica | 7.9 |
| c377f7f1-17c7-341c-a615-fac3cb964b23 | -18.28275 | -42.63457 | 2024-10-05 00:09:00 | TERRA_M-M | SÃO PEDRO DO SUAÇUÍ | MINAS GERAIS | Brasil | 3164100 | 31 | 33 | nan | nan | nan | Mata Atlântica | 39.7 |
| 048bcbf2-7d60-35f0-9455-9003ccb19b46 | -18.27876 | -42.6413 | 2024-10-05 00:09:00 | TERRA_M-M | SÃO JOSÉ DO JACURI | MINAS GERAIS | Brasil | 3163508 | 31 | 33 | nan | nan | nan | Mata Atlântica | 26.8 |
| 6d4f2794-5f4b-35a3-a5f5-9866cc7bcb5a | -18.27608 | -42.6151 | 2024-10-05 00:09:00 | TERRA_M-M | SÃO PEDRO DO SUAÇUÍ | MINAS GERAIS | Brasil | 3164100 | 31 | 33 | nan | nan | nan | Mata Atlântica | 27.5 |
| e5fb0659-3876-3934-89d6-472bd083b85a | -18.2253 | -42.83192 | 2024-10-05 00:09:00 | TERRA_M-M | COLUNA | MINAS GERAIS | Brasil | 3116803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 16.0 |
| 483c8e39-8c8b-3207-8684-62766d8a8923 | -18.22263 | -42.80406 | 2024-10-05 00:09:00 | TERRA_M-M | COLUNA | MINAS GERAIS | Brasil | 3116803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 25.3 |
| 5a3ee4b6-0396-3654-b385-5d26678ee8c0 | -18.21999 | -42.80947 | 2024-10-05 00:09:00 | TERRA_M-M | COLUNA | MINAS GERAIS | Brasil | 3116803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 33.8 |
| 8efc308a-06ed-3fd4-9f74-6c19f8978424 | -18.18853 | -42.59859 | 2024-10-05 00:09:00 | TERRA_M-M | SÃO JOSÉ DO JACURI | MINAS GERAIS | Brasil | 3163508 | 31 | 33 | nan | nan | nan | Mata Atlântica | 22.4 |
| 0a410e12-bdb9-3644-a4f5-d3fc6860acf1 | -18.18448 | -42.60416 | 2024-10-05 00:09:00 | TERRA_M-M | SÃO JOSÉ DO JACURI | MINAS GERAIS | Brasil | 3163508 | 31 | 33 | nan | nan | nan | Mata Atlântica | 16.1 |
| 8cd67a8d-1085-3ddf-94c2-5f6adab9f788 | -18.18188 | -42.57893 | 2024-10-05 00:09:00 | TERRA_M-M | SÃO SEBASTIÃO DO MARANHÃO | MINAS GERAIS | Brasil | 3164506 | 31 | 33 | nan | nan | nan | Mata Atlântica | 15.4 |
| 9295c846-bde1-333c-890c-a38f2b00d905 | -18.09285 | -45.60361 | 2024-10-05 00:09:00 | TERRA_M-M | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 53.2 |
| aa92abd6-eb25-3c86-998d-2c1c13aa2570 | -18.0925 | -45.59858 | 2024-10-05 00:09:00 | TERRA_M-M | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 50.3 |
| d095f074-9226-3960-9e1d-1e7a746fb580 | -17.94764 | -41.47132 | 2024-10-05 00:09:00 | TERRA_M-M | TEÓFILO OTONI | MINAS GERAIS | Brasil | 3168606 | 31 | 33 | nan | nan | nan | Mata Atlântica | 15.4 |
| 3417ed5d-92d1-3604-b832-52b84e037917 | -17.92398 | -43.46027 | 2024-10-05 00:09:00 | TERRA_M-M | COUTO DE MAGALHÃES DE MINAS | MINAS GERAIS | Brasil | 3120102 | 31 | 33 | nan | nan | nan | Cerrado | 55.8 |
| 8caada3b-f009-3581-87dc-27cb3da792b7 | -17.92197 | -43.45498 | 2024-10-05 00:09:00 | TERRA_M-M | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 52.4 |
| 6ef85415-c704-30f1-bb0c-b15860dfed0f | -17.87918 | -42.7057 | 2024-10-05 00:09:00 | TERRA_M-M | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Mata Atlântica | 16.6 |
| e36521e0-662f-3bb9-ba60-620aaf39adbf | -17.87656 | -42.67949 | 2024-10-05 00:09:00 | TERRA_M-M | ARICANDUVA | MINAS GERAIS | Brasil | 3104452 | 31 | 33 | nan | nan | nan | Mata Atlântica | 47.4 |
| 0adabbc5-876f-3896-99f4-477f6225e2ed | -17.87317 | -42.68584 | 2024-10-05 00:09:00 | TERRA_M-M | ARICANDUVA | MINAS GERAIS | Brasil | 3104452 | 31 | 33 | nan | nan | nan | Mata Atlântica | 59.6 |
| b0ffd476-99da-30ab-849e-a502e76fa2ff | -17.8648 | -41.42458 | 2024-10-05 00:09:00 | TERRA_M-M | TEÓFILO OTONI | MINAS GERAIS | Brasil | 3168606 | 31 | 33 | nan | nan | nan | Mata Atlântica | 12.4 |
| 74e0e819-24b3-3c9a-95df-6526b2169a7e | -17.85188 | -41.42543 | 2024-10-05 00:09:00 | TERRA_M-M | TEÓFILO OTONI | MINAS GERAIS | Brasil | 3168606 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.9 |
| 3cf9cc3d-9d9f-3bb2-8ae1-882ab38beed4 | -17.70263 | -43.80452 | 2024-10-05 00:09:00 | TERRA_M-M | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 20.6 |
| 3cb34c2f-c04c-3e56-a6d2-5ba26d6b1e6f | -17.6991 | -43.79776 | 2024-10-05 00:09:00 | TERRA_M-M | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 24.2 |
| e31c97e3-d5d1-338b-85cc-fec2ea8c9e56 | -17.68684 | -42.64102 | 2024-10-05 00:09:00 | TERRA_M-M | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Mata Atlântica | 22.4 |
| d29770d0-8a9b-3f70-af03-d1e05efbdae8 | -17.6842 | -42.61647 | 2024-10-05 00:09:00 | TERRA_M-M | CAPELINHA | MINAS GERAIS | Brasil | 3112307 | 31 | 33 | nan | nan | nan | Mata Atlântica | 23.4 |
| f4737969-77b6-3a91-b73c-30fbd542e647 | -17.67738 | -42.63694 | 2024-10-05 00:09:00 | TERRA_M-M | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Mata Atlântica | 72.7 |
| ef1fe444-6868-349c-a7fb-ad80cef0ad98 | -17.67489 | -42.61197 | 2024-10-05 00:09:00 | TERRA_M-M | CAPELINHA | MINAS GERAIS | Brasil | 3112307 | 31 | 33 | nan | nan | nan | Mata Atlântica | 28.3 |
| 66d45436-5959-357e-b089-27bb5c163868 | -17.67284 | -42.64334 | 2024-10-05 00:09:00 | TERRA_M-M | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Mata Atlântica | 22.3 |
| 32a87658-7212-31e5-9c55-113ace827d8c | -17.67013 | -42.61792 | 2024-10-05 00:09:00 | TERRA_M-M | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Mata Atlântica | 24.3 |
| 8ae61091-df7f-38a9-80b1-e7ec33fab42a | -17.63008 | -42.0345 | 2024-10-05 00:09:00 | TERRA_M-M | SETUBINHA | MINAS GERAIS | Brasil | 3165552 | 31 | 33 | nan | nan | nan | Mata Atlântica | 20.6 |
| d91c5a2a-bcec-34ea-99ca-eb7a85ae77bb | -17.62774 | -42.01193 | 2024-10-05 00:09:00 | TERRA_M-M | SETUBINHA | MINAS GERAIS | Brasil | 3165552 | 31 | 33 | nan | nan | nan | Mata Atlântica | 84.6 |
| c54dfd4d-5525-3c95-87c0-b5a21a373a7c | -17.61909 | -43.27074 | 2024-10-05 00:09:00 | TERRA_M-M | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 18.9 |
| 912b6e8c-4e7c-302d-965d-18349fe4fe9c | -17.61898 | -42.01847 | 2024-10-05 00:09:00 | TERRA_M-M | SETUBINHA | MINAS GERAIS | Brasil | 3165552 | 31 | 33 | nan | nan | nan | Mata Atlântica | 97.2 |
| 9ada5100-4359-3d73-874d-2fa18a8ff42a | -17.4625 | -40.06421 | 2024-10-05 00:09:00 | TERRA_M-M | CARAVELAS | BAHIA | Brasil | 2906907 | 29 | 33 | nan | nan | nan | Mata Atlântica | 69.5 |
| 0708c844-ed18-3577-a7a2-c8bf47d4e61d | -15.2612 | -40.3889 | 2024-10-05 00:09:00 | TERRA_M-M | ITAMBÉ | BAHIA | Brasil | 2915809 | 29 | 33 | nan | nan | nan | Mata Atlântica | 8.9 |
| 7902e8ee-5343-326a-90d6-3227d8911cf0 | -13.94062 | -42.39751 | 2024-10-05 00:09:00 | TERRA_M-M | CAETITÉ | BAHIA | Brasil | 2905206 | 29 | 33 | nan | nan | nan | Caatinga | 59.4 |
| 1e53036d-002b-3acb-aecc-d7938290f2d5 | -12.72279 | -40.2184 | 2024-10-05 00:11:00 | TERRA_M-M | ITABERABA | BAHIA | Brasil | 2914703 | 29 | 33 | nan | nan | nan | Caatinga | 7.4 |
| b0c03a80-23eb-309f-9be8-9f7eb59d554d | -12.25844 | -45.96468 | 2024-10-05 00:11:00 | TERRA_M-M | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 74.1 |
| d4047337-13ec-306f-bd24-7fa61cb4549b | -8.33039 | -41.17287 | 2024-10-05 00:11:00 | TERRA_M-M | PAULISTANA | PIAUÍ | Brasil | 2207801 | 22 | 33 | nan | nan | nan | Caatinga | 9.3 |
| 53036cfd-1198-3a85-afb2-555cdf1d0324 | -11.68555 | -40.60094 | 2024-10-05 00:11:00 | TERRA_M-M | PIRITIBA | BAHIA | Brasil | 2924801 | 29 | 33 | nan | nan | nan | Caatinga | 27.9 |
| 37a26d5c-555c-3203-b485-f0f15e93c529 | -11.68385 | -40.58694 | 2024-10-05 00:11:00 | TERRA_M-M | PIRITIBA | BAHIA | Brasil | 2924801 | 29 | 33 | nan | nan | nan | Caatinga | 23.9 |
| 4b048b2c-0124-3adb-b1f4-fa816c7f46b2 | -11.68164 | -40.59357 | 2024-10-05 00:11:00 | TERRA_M-M | PIRITIBA | BAHIA | Brasil | 2924801 | 29 | 33 | nan | nan | nan | Caatinga | 38.7 |
| f8b9a3e3-a85c-365f-bee7-21f5bae1de1b | -11.20639 | -39.91922 | 2024-10-05 00:11:00 | TERRA_M-M | QUEIMADAS | BAHIA | Brasil | 2925808 | 29 | 33 | nan | nan | nan | Caatinga | 9.5 |
| bafcde88-8925-34a6-8d7b-89cbd2257e9c | -11.20479 | -39.90683 | 2024-10-05 00:11:00 | TERRA_M-M | QUEIMADAS | BAHIA | Brasil | 2925808 | 29 | 33 | nan | nan | nan | Caatinga | 14.7 |
| 1b49005c-390e-316e-b0cb-c9f613d2758e | -10.84174 | -42.84417 | 2024-10-05 00:11:00 | TERRA_M-M | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Cerrado | 15.1 |
| d3213a4e-c474-3d29-842a-f509cfff21ea | -8.32859 | -41.15911 | 2024-10-05 00:11:00 | TERRA_M-M | PAULISTANA | PIAUÍ | Brasil | 2207801 | 22 | 33 | nan | nan | nan | Caatinga | 18.2 |
| 0bdd3e78-4cca-346d-acb5-d7f9486dfeaa | -9.48034 | -36.06776 | 2024-10-05 00:11:00 | TERRA_M-M | ATALAIA | ALAGOAS | Brasil | 2700409 | 27 | 33 | nan | nan | nan | Mata Atlântica | 5.2 |
| f8a333d8-42cc-3941-917f-5d67248c21c6 | -9.54472 | -36.93002 | 2024-10-05 00:11:00 | TERRA_M-M | MAJOR ISIDORO | ALAGOAS | Brasil | 2704401 | 27 | 33 | nan | nan | nan | Caatinga | 4.8 |
| fc257368-0255-3fe0-90fd-39191f1db89f | -9.60268 | -36.08975 | 2024-10-05 00:11:00 | TERRA_M-M | PILAR | ALAGOAS | Brasil | 2706901 | 27 | 33 | nan | nan | nan | Mata Atlântica | 8.9 |
| 492aa95a-fd1a-3744-bc12-d2e7db4e6150 | -8.37324 | -43.65784 | 2024-10-05 00:11:00 | TERRA_M-M | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 50.7 |
| f22d136a-f9dc-3f30-b824-79a0e001f089 | -10.91118 | -46.67957 | 2024-10-05 00:11:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 53.0 |
| e5452e45-d351-38af-a025-820ace489348 | -13.17075 | -44.06345 | 2024-10-05 00:11:00 | TERRA_M-M | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 22.6 |
| c13861f2-ae9b-324d-980a-1438e117be6c | -9.92624 | -36.15507 | 2024-10-05 00:11:00 | TERRA_M-M | JEQUIÁ DA PRAIA | ALAGOAS | Brasil | 2703759 | 27 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| bb086a4a-2ecf-3f89-9c9f-b023ea8db16f | -9.92498 | -36.14611 | 2024-10-05 00:11:00 | TERRA_M-M | JEQUIÁ DA PRAIA | ALAGOAS | Brasil | 2703759 | 27 | 33 | nan | nan | nan | Mata Atlântica | 53.4 |
| 2c24900a-2302-3c1a-a126-41a1f8096aff | -9.92372 | -36.13715 | 2024-10-05 00:11:00 | TERRA_M-M | JEQUIÁ DA PRAIA | ALAGOAS | Brasil | 2703759 | 27 | 33 | nan | nan | nan | Mata Atlântica | 10.1 |
| ec1cbd38-00d2-35c2-999a-267c39e07332 | -9.91613 | -36.14741 | 2024-10-05 00:11:00 | TERRA_M-M | JEQUIÁ DA PRAIA | ALAGOAS | Brasil | 2703759 | 27 | 33 | nan | nan | nan | Mata Atlântica | 36.2 |
| 0d062204-5511-3f57-be3b-c48c63fb7f7c | -9.91487 | -36.13846 | 2024-10-05 00:11:00 | TERRA_M-M | JEQUIÁ DA PRAIA | ALAGOAS | Brasil | 2703759 | 27 | 33 | nan | nan | nan | Mata Atlântica | 6.8 |
| 84107468-0537-34db-87ca-8fb4adcb2a3e | -9.78251 | -36.37982 | 2024-10-05 00:11:00 | TERRA_M-M | CAMPO ALEGRE | ALAGOAS | Brasil | 2701407 | 27 | 33 | nan | nan | nan | Mata Atlântica | 125.1 |
| d17a2805-e44e-3b21-9582-2fddf25907f9 | -9.78127 | -36.3709 | 2024-10-05 00:11:00 | TERRA_M-M | CAMPO ALEGRE | ALAGOAS | Brasil | 2701407 | 27 | 33 | nan | nan | nan | Mata Atlântica | 88.2 |
| 4b539f8b-1f46-3389-99d4-31d9320de59c | -9.77492 | -36.39003 | 2024-10-05 00:11:00 | TERRA_M-M | CAMPO ALEGRE | ALAGOAS | Brasil | 2701407 | 27 | 33 | nan | nan | nan | Mata Atlântica | 5.3 |
| 119c139c-6c2d-34e3-94c0-7bfb58ca561c | -9.77367 | -36.38111 | 2024-10-05 00:11:00 | TERRA_M-M | CAMPO ALEGRE | ALAGOAS | Brasil | 2701407 | 27 | 33 | nan | nan | nan | Mata Atlântica | 68.7 |
| a01c5fe3-bc49-321b-b793-edc12686d0dd | -7.74974 | -43.06301 | 2024-10-05 00:11:00 | TERRA_M-M | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 16.0 |
| ed05c285-e3e4-39bc-95d5-028e8b410ae1 | -7.70077 | -42.97541 | 2024-10-05 00:11:00 | TERRA_M-M | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 13.8 |
| 6fd710b3-4eda-300e-a966-cf2ec56b0214 | -7.69817 | -42.98103 | 2024-10-05 00:11:00 | TERRA_M-M | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 18.7 |
| 3821f9c6-ce94-3ab1-a06e-387aa613da44 | -7.50481 | -34.83517 | 2024-10-05 00:11:00 | TERRA_M-M | PITIMBU | PARAÍBA | Brasil | 2511905 | 25 | 33 | nan | nan | nan | Mata Atlântica | 25.3 |
| 2e62f402-4f8a-3914-b620-d6a3b2cc1449 | -7.49851 | -34.83163 | 2024-10-05 00:11:00 | TERRA_M-M | PITIMBU | PARAÍBA | Brasil | 2511905 | 25 | 33 | nan | nan | nan | Mata Atlântica | 6.7 |
| dad2fb68-f010-3da9-9c9c-f02e37c0c7b5 | -13.17017 | -44.06994 | 2024-10-05 00:11:00 | TERRA_M-M | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 41.7 |
| e6b81ada-071b-35c8-a311-8cd459cbe31b | -7.45761 | -35.14175 | 2024-10-05 00:11:00 | TERRA_M-M | ITAMBÉ | PERNAMBUCO | Brasil | 2607653 | 26 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| ae678cec-2250-3351-bd41-bd9874e57ffa | -6.88479 | -35.11911 | 2024-10-05 00:11:00 | TERRA_M-M | MAMANGUAPE | PARAÍBA | Brasil | 2508901 | 25 | 33 | nan | nan | nan | Mata Atlântica | 22.5 |
| 0b471655-6e74-366d-9e91-85c414abb30f | -6.88338 | -35.1092 | 2024-10-05 00:11:00 | TERRA_M-M | MAMANGUAPE | PARAÍBA | Brasil | 2508901 | 25 | 33 | nan | nan | nan | Mata Atlântica | 27.9 |
| 235eec74-e557-3f45-bb77-747b8210eb88 | -8.15874 | -41.34888 | 2024-10-05 00:11:00 | TERRA_M-M | PAULISTANA | PIAUÍ | Brasil | 2207801 | 22 | 33 | nan | nan | nan | Caatinga | 10.2 |
| bf74d911-8763-32fd-a6e2-c0b051207f1e | -6.84733 | -42.83294 | 2024-10-05 00:11:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 17.7 |
| 8b8482ae-a8a6-31de-9642-c076a61c6b73 | -6.84518 | -42.81586 | 2024-10-05 00:11:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 12.9 |


[Clique aqui para ver as próximas entradas](README3.md)
