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

## Dados Diários - Página 79

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| acde7d19-732b-344f-a3ba-ff245b722842 | -12.4901 | -41.4012 | 2026-09-14 15:20:00 | GOES-19 | LENÇÓIS | BAHIA | Brasil | 2919306 | 29 | 33 | nan | nan | nan | Caatinga | 152.9 |
| c58323f9-386c-3766-be3a-99c008d75296 | -11.5095 | -50.2559 | 2026-09-14 15:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 122.8 |
| a8085649-0d59-3584-8c1b-595dcb135b62 | -12.1265 | -44.199 | 2026-09-14 15:20:00 | GOES-19 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 90.6 |
| 95ae7337-5721-3beb-92f5-df9d2f6cf4bf | -10.2922 | -45.339 | 2026-09-14 15:20:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 97.5 |
| def12774-3d44-3420-8fc6-9669bff463ec | -10.2929 | -45.2932 | 2026-09-14 15:20:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 166.5 |
| 45672fa5-df1d-3920-830f-10c74ba494c0 | -6.67 | -43.657 | 2026-09-14 15:20:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 163.3 |
| 61e3ebd5-8bbb-31b3-8a7e-45ed382c64d6 | -2.6602 | -57.5119 | 2026-09-14 15:20:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 70.8 |
| b37c5b24-c162-3ecd-9c23-e2888083474a | -9.6854 | -48.0288 | 2026-09-14 15:20:00 | GOES-19 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 24.7 |
| 8f37cc8e-3353-3204-a998-d18f6c519c37 | -6.1111 | -57.6645 | 2026-09-14 15:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 221.7 |
| fc648679-fd99-3d5b-8ca1-02f529cbdd82 | -13.5526 | -51.4629 | 2026-09-14 15:20:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 215.2 |
| c00d81b1-dcb9-319b-a79b-d858356ab0dc | -3.1697 | -58.6437 | 2026-09-14 15:20:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 151.7 |
| d37debac-c856-38e4-8e97-14164080f07f | -8.5415 | -54.7187 | 2026-09-14 15:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 72.8 |
| 69faa6d8-c4a9-39c3-a33a-917982eae4ca | -9.2676 | -48.2472 | 2026-09-14 15:20:00 | GOES-19 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 24.2 |
| 79c8fcf9-ed4c-3f6c-b24c-87a785c9f0f5 | -8.5604 | -54.6973 | 2026-09-14 15:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 49.3 |
| 275ac431-6dbf-34e8-84cb-843d2aeb17ca | -15.5768 | -48.792 | 2026-09-14 15:20:00 | GOES-19 | COCALZINHO DE GOIÁS | GOIÁS | Brasil | 5205513 | 52 | 33 | nan | nan | nan | Cerrado | 149.5 |
| e67939d4-7b55-304f-9a4e-7c0d9b271cf5 | -3.332 | -59.466 | 2026-09-14 15:20:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 91.0 |
| 90c97cd7-a6e7-3cbb-8050-f5c50e6e1820 | -2.6601 | -57.5507 | 2026-09-14 15:20:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 119.2 |
| 9a308d2c-ce3b-3648-91be-d7075688a24e | -6.5593 | -45.3173 | 2026-09-14 15:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 97.6 |
| 95450e76-a049-3dd1-ab61-62b001e38c64 | -10.5667 | -51.3349 | 2026-09-14 15:20:00 | GOES-19 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 75.7 |
| fc842f34-fd66-3663-948c-1c971a022392 | -14.1856 | -47.407 | 2026-09-14 15:20:00 | GOES-19 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 136.9 |
| f510e589-fad7-3136-88a9-42d8f8cc90a2 | -3.4279 | -57.9816 | 2026-09-14 15:20:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 58.0 |
| 9b7c2805-eecc-3ffd-844f-ae36d56b0eea | -10.7715 | -46.3001 | 2026-09-14 15:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 112.9 |
| 9979a073-4110-3b37-9699-ad42115e513c | -3.1816 | -61.1235 | 2026-09-14 15:20:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 86.9 |
| 8a39674a-61a2-34b6-9012-eedd068cb9ac | -3.6457 | -58.6143 | 2026-09-14 15:20:00 | GOES-19 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 50.2 |
| 08028f28-ca2d-329d-9db6-08669f03cc36 | -3.3871 | -59.4075 | 2026-09-14 15:20:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 110.0 |
| 64e6d79a-37f4-33e5-adec-2a9d8faa20c7 | -8.7772 | -49.955 | 2026-09-14 15:20:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 65.9 |
| 7de25132-773a-33b0-bbc1-5c3765ad1cca | -10.7909 | -46.2751 | 2026-09-14 15:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 121.0 |
| 1875c7c2-510c-3fee-a918-e6dd86704e5c | -2.6601 | -57.5702 | 2026-09-14 15:20:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 75.6 |
| e0d1595d-5eb3-3dc9-9f17-7f7c3117e0e1 | -3.3305 | -54.2005 | 2026-09-14 15:20:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 56.8 |
| 84979ce5-1d6d-349c-9968-045626c2477e | -6.1608 | -52.7701 | 2026-09-14 15:20:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 51.9 |
| 3b40a1f3-1856-370e-9a97-0143332590ff | -3.3141 | -59.3515 | 2026-09-14 15:20:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 55.5 |
| 4bff56eb-3d4e-3373-80ae-5143d5985182 | -2.6602 | -57.5313 | 2026-09-14 15:20:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 91.7 |
| 68f1f0ec-30c9-3f2a-a58b-6421bda165c6 | -6.5781 | -45.3158 | 2026-09-14 15:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 100.6 |
| 6943f2f2-e3d6-3396-9f91-8cd54a4fe394 | -3.3137 | -59.4664 | 2026-09-14 15:20:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 52.1 |
| 857dddb8-9370-3de9-877c-a4c8967c444c | -3.3321 | -59.4469 | 2026-09-14 15:20:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 77.6 |
| 341ab18b-3883-395a-90a1-5adcb90fbe99 | -10.5484 | -51.2945 | 2026-09-14 15:20:00 | GOES-19 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 56.2 |
| ffc0de66-add7-3012-8c88-f0b132500c53 | -8.8081 | -45.8753 | 2026-09-14 15:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 143.5 |
| 8b44478f-7b8a-3962-863b-703301e24bdc | -10.9506 | -57.1895 | 2026-09-14 15:20:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 71.5 |
| 6f6ebc02-02f1-3961-9203-812dd11f30c1 | -11.8365 | -50.0028 | 2026-09-14 15:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 133.0 |
| cf115802-a281-3535-b021-fca350be1cd8 | -3.1696 | -58.6629 | 2026-09-14 15:20:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 66.3 |
| 9a5c78ce-0641-31f0-82af-7b1778941597 | -7.207 | -46.1187 | 2026-09-14 15:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 104.7 |
| 543ec3f6-a607-3f36-93b3-3b6f6b73b0fc | -6.0925 | -57.6847 | 2026-09-14 15:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 81.6 |
| 90499515-bb2c-33c9-9b43-b555fd7b1112 | -5.2023 | -49.3348 | 2026-09-14 15:20:00 | GOES-19 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 62.0 |
| 5f3ab938-4e50-3cf3-a621-5b794e911128 | -7.8713 | -54.7217 | 2026-09-14 15:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 55.1 |
| 5cfdad01-cd57-39ab-9606-be2e0c2841ca | -3.3138 | -59.4472 | 2026-09-14 15:20:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 56.9 |
| 49990e57-8de1-3678-9719-a153e1b9c2f9 | -6.3436 | -55.8243 | 2026-09-14 15:20:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 85.4 |
| 52380d22-2db9-32de-8bcd-0e25d9474655 | -7.1578 | -42.1032 | 2026-09-14 15:20:00 | GOES-19 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 149.8 |
| 9b907ee1-fced-3025-9200-6844f3f0841b | -9.7036 | -54.371 | 2026-09-14 15:20:00 | GOES-19 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 84.0 |
| 21399561-6961-3a22-b6f5-10607aacae1b | -10.7722 | -46.2549 | 2026-09-14 15:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 201.6 |
| 046f499b-efef-3921-81d6-83e9619c38ad | -3.3677 | -59.8094 | 2026-09-14 15:20:00 | GOES-19 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 47.7 |
| 8efec6c3-6068-3a27-b1d8-a5c05c7a73ac | -6.1422 | -52.7711 | 2026-09-14 15:20:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 61.2 |
| 0ce774c2-1ac7-3b72-b11e-645c7cb973f6 | -9.1339 | -51.5927 | 2026-09-14 15:20:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 65.6 |
| 717d4c8f-167e-3cc3-9cc6-934cfb7fcf38 | -12.23029 | -39.30804 | 2026-09-14 15:26:00 | NPP-375 | IPECAETÁ | BAHIA | Brasil | 2913804 | 29 | 33 | nan | nan | nan | Mata Atlântica | 17.2 |
| 53a8b5e2-c54d-348f-bc89-98734fa9aaa6 | -12.22659 | -39.30885 | 2026-09-14 15:26:00 | NPP-375 | IPECAETÁ | BAHIA | Brasil | 2913804 | 29 | 33 | nan | nan | nan | Mata Atlântica | 10.3 |
| 34c7c6a0-45b8-3127-b0ef-c148435149fb | -12.22584 | -39.3018 | 2026-09-14 15:26:00 | NPP-375 | IPECAETÁ | BAHIA | Brasil | 2913804 | 29 | 33 | nan | nan | nan | Mata Atlântica | 11.5 |
| 51a7cece-17d4-3bc9-9102-41e616b8c261 | -4.45681 | -39.36264 | 2026-09-14 15:29:00 | NPP-375 | CANINDÉ | CEARÁ | Brasil | 2302800 | 23 | 33 | nan | nan | nan | Caatinga | 85.5 |
| bccf42a6-57f7-38c9-b183-30d72832aa81 | -7.49985 | -37.63486 | 2026-09-14 15:29:00 | NPP-375 | ÁGUA BRANCA | PARAÍBA | Brasil | 2500106 | 25 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 3e93209c-d39c-3c93-ad08-78ee33434aaa | -7.08339 | -37.73135 | 2026-09-14 15:29:00 | NPP-375 | EMAS | PARAÍBA | Brasil | 2505907 | 25 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 2d28d737-4011-33ff-ad77-909062440622 | -6.42905 | -38.40902 | 2026-09-14 15:29:00 | NPP-375 | UIRAÚNA | PARAÍBA | Brasil | 2516904 | 25 | 33 | nan | nan | nan | Caatinga | 19.2 |
| 782df818-17eb-3c41-895c-c970efc0a8fe | -8.24138 | -37.40432 | 2026-09-14 15:29:00 | NPP-375 | SERTÂNIA | PERNAMBUCO | Brasil | 2614105 | 26 | 33 | nan | nan | nan | Caatinga | 5.6 |
| 4c29d8df-392f-331d-8dc6-9e8360dc8dcb | -4.45604 | -39.35736 | 2026-09-14 15:29:00 | NPP-375 | CANINDÉ | CEARÁ | Brasil | 2302800 | 23 | 33 | nan | nan | nan | Caatinga | 85.5 |
| 54903e92-6226-3d10-8dd5-adea952300e1 | -6.52431 | -38.42444 | 2026-09-14 15:29:00 | NPP-375 | UIRAÚNA | PARAÍBA | Brasil | 2516904 | 25 | 33 | nan | nan | nan | Caatinga | 7.0 |
| 316c1bb4-612b-3744-911e-3410f683b12a | -4.98249 | -37.38981 | 2026-09-14 15:29:00 | NPP-375 | MOSSORÓ | RIO GRANDE DO NORTE | Brasil | 2408003 | 24 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 33abff37-96c4-3eae-a3bb-0618179d1308 | -8.31607 | -36.57225 | 2026-09-14 15:29:00 | NPP-375 | SANHARÓ | PERNAMBUCO | Brasil | 2612406 | 26 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 31baf1d7-6135-3f0d-9a61-2ddd8bf60b96 | -6.01806 | -35.45987 | 2026-09-14 15:29:00 | NPP-375 | MACAÍBA | RIO GRANDE DO NORTE | Brasil | 2407104 | 24 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 90648deb-1444-3dd5-90c7-5f850fbd649e | -7.67682 | -35.11022 | 2026-09-14 15:29:00 | NPP-375 | ITAQUITINGA | PERNAMBUCO | Brasil | 2607802 | 26 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| 89019c1d-2860-3dd5-aac3-d4b0d35442d0 | -4.9761 | -37.38654 | 2026-09-14 15:29:00 | NPP-375 | MOSSORÓ | RIO GRANDE DO NORTE | Brasil | 2408003 | 24 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 9fca922c-2280-3899-9a53-660067dd73b5 | -10.04199 | -39.66379 | 2026-09-14 15:29:00 | NPP-375 | UAUÁ | BAHIA | Brasil | 2932002 | 29 | 33 | nan | nan | nan | Caatinga | 19.8 |
| 72c05cf1-19f6-3836-85ba-0e6dd1b1c1d0 | -6.43985 | -39.34773 | 2026-09-14 15:29:00 | NPP-375 | IGUATU | CEARÁ | Brasil | 2305506 | 23 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 68d68477-ac68-3bad-a29d-adb3ce08ac35 | -6.78106 | -35.83669 | 2026-09-14 15:29:00 | NPP-375 | CASSERENGUE | PARAÍBA | Brasil | 2504157 | 25 | 33 | nan | nan | nan | Caatinga | 2.1 |
| e4408e32-1610-34fa-baf4-55ae0ecff169 | -8.03043 | -39.0004 | 2026-09-14 15:29:00 | NPP-375 | VERDEJANTE | PERNAMBUCO | Brasil | 2616100 | 26 | 33 | nan | nan | nan | Caatinga | 10.0 |
| a993fc31-b3cb-35d1-94c7-c499d153ce06 | -10.42617 | -39.31533 | 2026-09-14 15:29:00 | NPP-375 | MONTE SANTO | BAHIA | Brasil | 2921500 | 29 | 33 | nan | nan | nan | Caatinga | 10.0 |
| 6ac5f8e7-086c-3c29-816e-4ca2b0d3f380 | -6.43232 | -38.41077 | 2026-09-14 15:29:00 | NPP-375 | UIRAÚNA | PARAÍBA | Brasil | 2516904 | 25 | 33 | nan | nan | nan | Caatinga | 6.6 |
| 1f2b0379-636b-30b4-8328-a7a366301bcc | -6.43167 | -38.40585 | 2026-09-14 15:29:00 | NPP-375 | UIRAÚNA | PARAÍBA | Brasil | 2516904 | 25 | 33 | nan | nan | nan | Caatinga | 6.6 |
| 7ec197ae-e1d6-3385-9428-79bfcd2a6c08 | -5.11628 | -40.61008 | 2026-09-14 15:29:00 | NPP-375 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 7.2 |
| 8ec67f5a-98d4-3664-8a0c-ef186547f1b0 | -5.56164 | -39.25875 | 2026-09-14 15:29:00 | NPP-375 | SENADOR POMPEU | CEARÁ | Brasil | 2312700 | 23 | 33 | nan | nan | nan | Caatinga | 10.8 |
| ad4a2e0c-5b93-3a64-840c-de28da115ec6 | -9.11993 | -40.00423 | 2026-09-14 15:29:00 | NPP-375 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 123f4241-cb0d-3492-85e1-1725f35f74a2 | -9.74084 | -37.16848 | 2026-09-14 15:29:00 | NPP-375 | BATALHA | ALAGOAS | Brasil | 2700706 | 27 | 33 | nan | nan | nan | Caatinga | 8.8 |
| 93381dcd-384a-3e4e-85b7-b0cad9b871ea | -6.22124 | -35.3881 | 2026-09-14 15:29:00 | NPP-375 | BREJINHO | RIO GRANDE DO NORTE | Brasil | 2401800 | 24 | 33 | nan | nan | nan | Caatinga | 2.4 |
| ac21afa5-e294-344d-8747-eecab95c8f44 | -4.45563 | -39.35743 | 2026-09-14 15:29:00 | NPP-375 | CANINDÉ | CEARÁ | Brasil | 2302800 | 23 | 33 | nan | nan | nan | Caatinga | 87.3 |
| 7b40b28a-450b-3463-ace0-ac6bbac4b508 | -6.44203 | -39.34473 | 2026-09-14 15:29:00 | NPP-375 | IGUATU | CEARÁ | Brasil | 2305506 | 23 | 33 | nan | nan | nan | Caatinga | 2.9 |
| f21a9489-f68b-3866-bffe-6b783157e298 | -8.69655 | -35.16149 | 2026-09-14 15:29:00 | NPP-375 | RIO FORMOSO | PERNAMBUCO | Brasil | 2611903 | 26 | 33 | nan | nan | nan | Mata Atlântica | 5.6 |
| 11c6da85-fd62-31a3-a8e9-5df381d63db0 | -4.45528 | -39.35213 | 2026-09-14 15:29:00 | NPP-375 | CANINDÉ | CEARÁ | Brasil | 2302800 | 23 | 33 | nan | nan | nan | Caatinga | 51.9 |
| 1983c432-0294-3c7d-915e-93d1eadde713 | -5.56352 | -39.25558 | 2026-09-14 15:29:00 | NPP-375 | SENADOR POMPEU | CEARÁ | Brasil | 2312700 | 23 | 33 | nan | nan | nan | Caatinga | 8.9 |
| b61c6926-2be2-3d1b-889e-2e0bd68c3844 | -4.97668 | -37.3906 | 2026-09-14 15:29:00 | NPP-375 | MOSSORÓ | RIO GRANDE DO NORTE | Brasil | 2408003 | 24 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 93e79742-a240-35be-8797-870875458f22 | -7.28977 | -37.10825 | 2026-09-14 15:29:00 | NPP-375 | DESTERRO | PARAÍBA | Brasil | 2505402 | 25 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 454f4064-f6a8-3066-8504-8f970dfe4f0d | -6.87073 | -38.73711 | 2026-09-14 15:29:00 | NPP-375 | IPAUMIRIM | CEARÁ | Brasil | 2305704 | 23 | 33 | nan | nan | nan | Caatinga | 11.2 |
| 62b23690-64eb-306d-97af-8ddf2c6ff16c | -7.49938 | -37.63352 | 2026-09-14 15:29:00 | NPP-375 | ÁGUA BRANCA | PARAÍBA | Brasil | 2500106 | 25 | 33 | nan | nan | nan | Caatinga | 2.8 |
| dd88e2bf-c8f6-377e-a2a1-84309d27366e | -7.67298 | -35.11087 | 2026-09-14 15:29:00 | NPP-375 | ITAQUITINGA | PERNAMBUCO | Brasil | 2607802 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 5f836aa4-8a61-3744-ab49-d4e305ae42ff | -6.52596 | -38.42152 | 2026-09-14 15:29:00 | NPP-375 | UIRAÚNA | PARAÍBA | Brasil | 2516904 | 25 | 33 | nan | nan | nan | Caatinga | 6.7 |
| 71bbb743-220f-3246-a7fc-de83e30d8924 | -7.67815 | -35.11009 | 2026-09-14 15:29:00 | NPP-375 | ITAQUITINGA | PERNAMBUCO | Brasil | 2607802 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 447a163b-abac-3d75-a692-e5f72d92334a | -11.20176 | -39.69889 | 2026-09-14 15:29:00 | NPP-375 | QUEIMADAS | BAHIA | Brasil | 2925808 | 29 | 33 | nan | nan | nan | Caatinga | 4.9 |
| c771693b-95ef-367c-85aa-05588afb221e | -8.36453 | -35.26643 | 2026-09-14 15:29:00 | NPP-375 | ESCADA | PERNAMBUCO | Brasil | 2605202 | 26 | 33 | nan | nan | nan | Mata Atlântica | 6.4 |
| 0e23a22b-4ea5-3f5d-b2ba-667e9a7e2de7 | -7.85022 | -38.07199 | 2026-09-14 15:29:00 | NPP-375 | TRIUNFO | PERNAMBUCO | Brasil | 2615706 | 26 | 33 | nan | nan | nan | Caatinga | 12.5 |
| 648b9dfd-8cb3-3a54-af9b-1067fcab5774 | -5.93352 | -38.11561 | 2026-09-14 15:29:00 | NPP-375 | RODOLFO FERNANDES | RIO GRANDE DO NORTE | Brasil | 2411007 | 24 | 33 | nan | nan | nan | Caatinga | 4.2 |
| ef9ceee1-0232-3cc4-bccd-8c4822abfb9d | -6.42531 | -38.40634 | 2026-09-14 15:29:00 | NPP-375 | UIRAÚNA | PARAÍBA | Brasil | 2516904 | 25 | 33 | nan | nan | nan | Caatinga | 6.6 |
| 434e7658-f1d0-35b3-a2fe-a52e2ad1688f | -7.71576 | -37.02266 | 2026-09-14 15:29:00 | NPP-375 | PRATA | PARAÍBA | Brasil | 2512200 | 25 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 174f6460-2365-3578-bfde-056596c4ff52 | -7.57006 | -35.45569 | 2026-09-14 15:29:00 | NPP-375 | SÃO VICENTE FÉRRER | PERNAMBUCO | Brasil | 2613800 | 26 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| fc11361a-e91f-351d-8a3c-8ead83df6133 | -5.93287 | -38.11089 | 2026-09-14 15:29:00 | NPP-375 | RODOLFO FERNANDES | RIO GRANDE DO NORTE | Brasil | 2411007 | 24 | 33 | nan | nan | nan | Caatinga | 4.2 |
| d0f2fac6-3929-3193-bf04-43004318ec41 | -4.37978 | -39.24187 | 2026-09-14 15:29:00 | NPP-375 | CANINDÉ | CEARÁ | Brasil | 2302800 | 23 | 33 | nan | nan | nan | Caatinga | 5.0 |


[Clique aqui para ver as próximas entradas](README80.md)
