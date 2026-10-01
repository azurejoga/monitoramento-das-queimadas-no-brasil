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

## Dados Diários - Página 109

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b688275a-6b3a-3a87-8ba3-6607666bf178 | -18.59838 | -43.49725 | 2026-10-01 16:09:00 | NOAA-21 | SERRO | MINAS GERAIS | Brasil | 3167103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 17.7 |
| a7917d0c-ce09-3021-91c7-a365d38382aa | -19.60123 | -44.65467 | 2026-10-01 16:09:00 | NOAA-21 | PEQUI | MINAS GERAIS | Brasil | 3149606 | 31 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 55d95812-a6fe-31d9-8f2b-1b449c72f414 | -21.15999 | -44.34155 | 2026-10-01 16:09:00 | NOAA-21 | SÃO JOÃO DEL REI | MINAS GERAIS | Brasil | 3162500 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.2 |
| d0af2301-4d60-3775-a7c2-a123599375e8 | -18.2963 | -42.2314 | 2026-10-01 16:09:00 | NOAA-21 | SANTA MARIA DO SUAÇUÍ | MINAS GERAIS | Brasil | 3158201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.2 |
| 39cf1dc1-01ed-331e-8315-1510a3f4d06d | -16.9113 | -42.11074 | 2026-10-01 16:09:00 | NOAA-21 | ARAÇUAÍ | MINAS GERAIS | Brasil | 3103405 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.1 |
| 9c74b74f-d200-38fa-a286-82f3ae548626 | -18.30002 | -42.23097 | 2026-10-01 16:09:00 | NOAA-21 | SANTA MARIA DO SUAÇUÍ | MINAS GERAIS | Brasil | 3158201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.2 |
| 4e51d176-4214-388d-851a-0347fd0d0391 | -19.66454 | -40.08992 | 2026-10-01 16:09:00 | NOAA-21 | ARACRUZ | ESPÍRITO SANTO | Brasil | 3200607 | 32 | 33 | nan | nan | nan | Mata Atlântica | 17.9 |
| a9727d1f-1f8e-31f4-9ad8-de0ee0715356 | -18.11124 | -44.54791 | 2026-10-01 16:09:00 | NOAA-21 | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 1f1abd55-804d-3f23-813d-239d2566f1aa | -17.0275 | -45.43148 | 2026-10-01 16:09:00 | NOAA-21 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 4.7 |
| e731dbc6-f026-3163-809a-c93e1bb7e90d | -16.86744 | -39.25871 | 2026-10-01 16:09:00 | NOAA-21 | PORTO SEGURO | BAHIA | Brasil | 2925303 | 29 | 33 | nan | nan | nan | Mata Atlântica | 22.1 |
| b7238b79-72eb-358c-9c65-0025bbfe365a | -18.33023 | -42.24222 | 2026-10-01 16:09:00 | NOAA-21 | SANTA MARIA DO SUAÇUÍ | MINAS GERAIS | Brasil | 3158201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| ccc75808-2751-3c1e-bdb7-b23f2ef24e7b | -19.17988 | -43.95748 | 2026-10-01 16:09:00 | NOAA-21 | JEQUITIBÁ | MINAS GERAIS | Brasil | 3135704 | 31 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 38024b9d-29e9-38f6-821c-e1b24e7c5a8b | -19.77157 | -43.81147 | 2026-10-01 16:09:00 | NOAA-21 | SANTA LUZIA | MINAS GERAIS | Brasil | 3157807 | 31 | 33 | nan | nan | nan | Cerrado | 27.1 |
| 5213ebe8-f2d8-3465-9d8a-536459ae965a | -18.68504 | -40.0641 | 2026-10-01 16:09:00 | NOAA-21 | SÃO MATEUS | ESPÍRITO SANTO | Brasil | 3204906 | 32 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| f0f2c884-450a-3996-ac4a-2087dda5f930 | -19.65178 | -44.89893 | 2026-10-01 16:09:00 | NOAA-21 | PITANGUI | MINAS GERAIS | Brasil | 3151404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 23.1 |
| 5678a446-67a4-350c-8d26-7d7cb8d5b7eb | -21.43945 | -47.03797 | 2026-10-01 16:09:00 | NOAA-21 | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | 7.6 |
| f464dca6-3632-3211-8264-8e2e3da34c67 | -18.81912 | -43.54081 | 2026-10-01 16:09:00 | NOAA-21 | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.6 |
| e8c6f8df-79d1-3490-8afe-3ba9fef35bf8 | -17.90598 | -44.31755 | 2026-10-01 16:09:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 5edc51fa-b419-3871-bcf6-0528db2209d6 | -17.32494 | -41.54557 | 2026-10-01 16:09:00 | NOAA-21 | CATUJI | MINAS GERAIS | Brasil | 3115458 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| 56b7a5a0-0fb0-318f-9693-deed9c33bfe4 | -18.35199 | -40.0343 | 2026-10-01 16:09:00 | NOAA-21 | PINHEIROS | ESPÍRITO SANTO | Brasil | 3204104 | 32 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| 4c2b008b-f37d-3b31-aab4-9c89e6976a83 | -19.66509 | -40.09383 | 2026-10-01 16:09:00 | NOAA-21 | ARACRUZ | ESPÍRITO SANTO | Brasil | 3200607 | 32 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| 4c82b7bf-2d61-3ad4-ab76-5807a46faf02 | -16.76944 | -43.95242 | 2026-10-01 16:09:00 | NOAA-21 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 26.0 |
| 4a8cc8c0-e2bd-39ea-a55f-8ce35116fad8 | -17.42748 | -45.03933 | 2026-10-01 16:09:00 | NOAA-21 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 10.0 |
| e3badbf5-18e5-3faa-b2fc-6984b58e9763 | -20.10894 | -42.16427 | 2026-10-01 16:09:00 | NOAA-21 | MANHUAÇU | MINAS GERAIS | Brasil | 3139409 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.1 |
| cca7f873-a223-3282-acdf-40951d4a353e | -19.34209 | -40.50457 | 2026-10-01 16:09:00 | NOAA-21 | LINHARES | ESPÍRITO SANTO | Brasil | 3203205 | 32 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| fc169870-3ca7-3e76-9a42-1b0ba4acbec2 | -16.08762 | -40.57191 | 2026-10-01 16:09:00 | NOAA-21 | ALMENARA | MINAS GERAIS | Brasil | 3101706 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 70b09850-7511-3d81-b73f-e57bc4eb77c5 | -19.52792 | -40.18662 | 2026-10-01 16:09:00 | NOAA-21 | LINHARES | ESPÍRITO SANTO | Brasil | 3203205 | 32 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| f81dbf18-2d4f-373a-bd48-5af74683fadd | -18.88424 | -41.07813 | 2026-10-01 16:09:00 | NOAA-21 | MANTENÓPOLIS | ESPÍRITO SANTO | Brasil | 3203304 | 32 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| 34e8bdba-59db-304b-9d8e-bbcc54e20050 | -18.76942 | -47.61483 | 2026-10-01 16:09:00 | NOAA-21 | MONTE CARMELO | MINAS GERAIS | Brasil | 3143104 | 31 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 7f4669ba-82b8-3a1f-8d08-65fbab93963d | -18.26341 | -42.23945 | 2026-10-01 16:09:00 | NOAA-21 | SANTA MARIA DO SUAÇUÍ | MINAS GERAIS | Brasil | 3158201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 31.0 |
| 9c0b2bb1-9fbc-34ff-83a2-84352a6d7eab | -19.66222 | -40.09828 | 2026-10-01 16:09:00 | NOAA-21 | ARACRUZ | ESPÍRITO SANTO | Brasil | 3200607 | 32 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| 0fc04adb-cc7b-358b-bf8d-bfce56528779 | -17.65493 | -48.20124 | 2026-10-01 16:09:00 | NOAA-21 | IPAMERI | GOIÁS | Brasil | 5210109 | 52 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 1afab9a7-cf8d-3ff7-bc68-849c5822af83 | -18.05971 | -42.38935 | 2026-10-01 16:09:00 | NOAA-21 | ÁGUA BOA | MINAS GERAIS | Brasil | 3100609 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.0 |
| b1c5af20-2a1a-3e57-9b06-41a5165ed5ec | -18.71423 | -43.17863 | 2026-10-01 16:09:00 | NOAA-21 | SABINÓPOLIS | MINAS GERAIS | Brasil | 3156809 | 31 | 33 | nan | nan | nan | Mata Atlântica | 19.0 |
| 409f1f2d-a0bd-39ed-b4ef-941a62841773 | -20.06831 | -44.59926 | 2026-10-01 16:09:00 | NOAA-21 | ITAÚNA | MINAS GERAIS | Brasil | 3133808 | 31 | 33 | nan | nan | nan | Cerrado | 5.6 |
| fbd240fe-271e-347d-9113-9b497ec29e5b | -20.80145 | -42.23965 | 2026-10-01 16:09:00 | NOAA-21 | SÃO FRANCISCO DO GLÓRIA | MINAS GERAIS | Brasil | 3161403 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| a888b37e-ef30-3b64-916f-2ef730cf30f2 | -16.34788 | -41.31825 | 2026-10-01 16:09:00 | NOAA-21 | JEQUITINHONHA | MINAS GERAIS | Brasil | 3135803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.9 |
| 03534138-9274-395a-bb52-e4d6eb9e0ace | -17.69053 | -41.26711 | 2026-10-01 16:09:00 | NOAA-21 | TEÓFILO OTONI | MINAS GERAIS | Brasil | 3168606 | 31 | 33 | nan | nan | nan | Mata Atlântica | 15.0 |
| 061fc8ef-9eca-3bc6-b984-757aeba41669 | -19.77741 | -42.84353 | 2026-10-01 16:09:00 | NOAA-21 | SÃO DOMINGOS DO PRATA | MINAS GERAIS | Brasil | 3161007 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.9 |
| 0249b662-41ac-3149-a29e-c19e6f0b57ec | -19.61425 | -45.55211 | 2026-10-01 16:09:00 | NOAA-21 | DORES DO INDAIÁ | MINAS GERAIS | Brasil | 3123205 | 31 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 83bd2f4f-8749-3fc5-94b1-123c6e031c4a | -18.49444 | -41.10131 | 2026-10-01 16:09:00 | NOAA-21 | NOVA BELÉM | MINAS GERAIS | Brasil | 3144672 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.5 |
| fb1c7484-43b6-33ac-a98a-ed39f59d4ba4 | -17.87115 | -44.31004 | 2026-10-01 16:09:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e1f076bf-3628-3f2a-bf83-30f59c204bb2 | -18.97039 | -41.28481 | 2026-10-01 16:09:00 | NOAA-21 | CONSELHEIRO PENA | MINAS GERAIS | Brasil | 3118403 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| d0a41304-63cc-3015-9b11-f8d5815beec4 | -19.65566 | -44.8936 | 2026-10-01 16:09:00 | NOAA-21 | PITANGUI | MINAS GERAIS | Brasil | 3151404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 23.1 |
| f9dfb180-3dcf-3f9c-b095-2032ab836175 | -19.87049 | -42.63742 | 2026-10-01 16:09:00 | NOAA-21 | DIONÍSIO | MINAS GERAIS | Brasil | 3121803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.3 |
| 97c3bb57-4f67-38d3-8d0e-9d571a87b8dd | -17.88 | -44.31305 | 2026-10-01 16:09:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| d4f7f9a0-af30-3167-ba3f-b6f3c64d3b3c | -17.5464 | -41.47684 | 2026-10-01 16:09:00 | NOAA-21 | TEÓFILO OTONI | MINAS GERAIS | Brasil | 3168606 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.2 |
| 930e28ff-85e0-3f3e-8df8-da8c2cc6ab70 | -20.40484 | -42.42981 | 2026-10-01 16:09:00 | NOAA-21 | ABRE CAMPO | MINAS GERAIS | Brasil | 3100302 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.1 |
| d576681c-cc11-3c1a-9a07-ae52621b1be6 | -17.01404 | -41.17954 | 2026-10-01 16:09:00 | NOAA-21 | JOAÍMA | MINAS GERAIS | Brasil | 3136009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.3 |
| 7e42fcfa-5c55-33df-8d83-7e0c64f811af | -18.42665 | -42.25661 | 2026-10-01 16:09:00 | NOAA-21 | VIRGOLÂNDIA | MINAS GERAIS | Brasil | 3171907 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| e5a5db7c-79d0-320f-bbc9-ea444445921e | -19.66796 | -40.08939 | 2026-10-01 16:09:00 | NOAA-21 | ARACRUZ | ESPÍRITO SANTO | Brasil | 3200607 | 32 | 33 | nan | nan | nan | Mata Atlântica | 27.6 |
| e506cdb3-2e62-3e6c-9caa-e7acbff5c208 | -17.41374 | -39.36937 | 2026-10-01 16:09:00 | NOAA-21 | ALCOBAÇA | BAHIA | Brasil | 2900801 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 273c9720-062f-35e3-a14a-bc62eb40a8e9 | -18.11214 | -44.55534 | 2026-10-01 16:09:00 | NOAA-21 | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 53d60fa4-7c88-3908-8a6c-6ab695ed0a5e | -16.99524 | -45.46352 | 2026-10-01 16:09:00 | NOAA-21 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 17.1 |
| 35968da7-12b1-310f-b995-e8896b81721e | -18.61532 | -45.13157 | 2026-10-01 16:09:00 | NOAA-21 | FELIXLÂNDIA | MINAS GERAIS | Brasil | 3125705 | 31 | 33 | nan | nan | nan | Cerrado | 7.7 |
| b27e6a48-d94d-3002-9e67-c6a68a95d5c2 | -18.54036 | -42.16846 | 2026-10-01 16:09:00 | NOAA-21 | NACIP RAYDAN | MINAS GERAIS | Brasil | 3144201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.8 |
| 2c62e017-6036-3d09-bcbf-09fdffcf96b9 | -17.00157 | -45.46953 | 2026-10-01 16:09:00 | NOAA-21 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 15.7 |
| 95dae32d-6edc-365b-a1ac-f88ff3c6ea9b | -16.5121 | -41.28715 | 2026-10-01 16:09:00 | NOAA-21 | JEQUITINHONHA | MINAS GERAIS | Brasil | 3135803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.6 |
| d8569c02-d6af-3dd7-b2c7-96b67c502fd2 | -18.13417 | -46.57683 | 2026-10-01 16:09:00 | NOAA-21 | LAGAMAR | MINAS GERAIS | Brasil | 3137106 | 31 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 5431107e-9a02-3b38-ad9e-f86e1f9f7661 | -17.428 | -45.04355 | 2026-10-01 16:09:00 | NOAA-21 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 14.6 |
| 3483d836-6988-30db-9766-67041dffd94d | -17.80831 | -44.36362 | 2026-10-01 16:09:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 5.2 |
| e020acd9-e202-3e97-9263-c0c6accb3075 | -18.59794 | -43.4937 | 2026-10-01 16:09:00 | NOAA-21 | SERRO | MINAS GERAIS | Brasil | 3167103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 15.9 |
| 37b4d527-d8d5-35f2-9345-e55d00c3fa9b | -17.91014 | -44.31692 | 2026-10-01 16:09:00 | NOAA-21 | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 5f634ebd-3b7a-3a55-9c11-000f988ea674 | -20.07323 | -44.60326 | 2026-10-01 16:09:00 | NOAA-21 | ITAÚNA | MINAS GERAIS | Brasil | 3133808 | 31 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 5d087068-8d41-3900-95ce-99bb961fa77e | -17.61242 | -44.33383 | 2026-10-01 16:09:00 | NOAA-21 | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| dce53d15-c233-37dd-992e-c8f603e2db0b | -16.59875 | -39.57277 | 2026-10-01 16:09:00 | NOAA-21 | ITABELA | BAHIA | Brasil | 2914653 | 29 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| 8c8f857f-1dce-3ba1-a2d7-6203c1280cf2 | -16.66426 | -43.15305 | 2026-10-01 16:09:00 | NOAA-21 | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 7.6 |
| f375e54c-a4e6-3267-a2de-eacbb48894c6 | -18.10788 | -44.55582 | 2026-10-01 16:09:00 | NOAA-21 | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 000d0fe5-bdc7-3c71-ab1b-81da17aeef70 | -18.72487 | -44.39629 | 2026-10-01 16:09:00 | NOAA-21 | CURVELO | MINAS GERAIS | Brasil | 3120904 | 31 | 33 | nan | nan | nan | Cerrado | 21.4 |
| 8171a14d-fcf9-3951-a441-b6ad2bd808c7 | -17.00022 | -45.46749 | 2026-10-01 16:09:00 | NOAA-21 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 19.3 |
| 3023bfdc-b5fc-32cc-aff7-0200f31ac66c | -17.55999 | -40.41751 | 2026-10-01 16:09:00 | NOAA-21 | LAJEDÃO | BAHIA | Brasil | 2918902 | 29 | 33 | nan | nan | nan | Mata Atlântica | 7.2 |
| 47dbdfcf-5943-3af7-8fa6-7d9c5d6f20a6 | -16.78965 | -40.82864 | 2026-10-01 16:09:00 | NOAA-21 | JOAÍMA | MINAS GERAIS | Brasil | 3136009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| 7b1349e5-3c29-3da9-b867-ebdc2e0c195f | -16.97579 | -41.93801 | 2026-10-01 16:09:00 | NOAA-21 | ARAÇUAÍ | MINAS GERAIS | Brasil | 3103405 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.5 |
| 2951307e-2dae-32eb-8a9b-2d642193940a | -18.51424 | -45.14693 | 2026-10-01 16:09:00 | NOAA-21 | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 6.6 |
| d89300b5-74e8-3e53-8e99-e44824f613dc | -16.85391 | -45.43695 | 2026-10-01 16:09:00 | NOAA-21 | SANTA FÉ DE MINAS | MINAS GERAIS | Brasil | 3157609 | 31 | 33 | nan | nan | nan | Cerrado | 56.2 |
| 4f9bf855-1ee9-30de-8ac3-56162c1da513 | -16.64179 | -42.32565 | 2026-10-01 16:09:00 | NOAA-21 | VIRGEM DA LAPA | MINAS GERAIS | Brasil | 3171600 | 31 | 33 | nan | nan | nan | Cerrado | 17.1 |
| f7823f36-e978-323c-88d6-ce0040c88a90 | -17.32436 | -41.54142 | 2026-10-01 16:09:00 | NOAA-21 | CATUJI | MINAS GERAIS | Brasil | 3115458 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 1a820682-40ba-3903-ba39-a083c8d59b1f | -20.80083 | -42.24185 | 2026-10-01 16:09:00 | NOAA-21 | SÃO FRANCISCO DO GLÓRIA | MINAS GERAIS | Brasil | 3161403 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 0e18d31c-c573-3d05-af16-012fc2dfa053 | -17.87948 | -44.30895 | 2026-10-01 16:09:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| bdcb3734-9455-336e-bded-1c221b26d345 | -17.62213 | -44.34418 | 2026-10-01 16:09:00 | NOAA-21 | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 19.1 |
| 7343084c-0cb9-36e3-a261-673ddfae1bd7 | -18.19986 | -42.31834 | 2026-10-01 16:09:00 | NOAA-21 | SANTA MARIA DO SUAÇUÍ | MINAS GERAIS | Brasil | 3158201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.1 |
| 350b9fe3-e90f-3727-be14-9ef676782804 | -18.29259 | -42.23186 | 2026-10-01 16:09:00 | NOAA-21 | SANTA MARIA DO SUAÇUÍ | MINAS GERAIS | Brasil | 3158201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.1 |
| ff0e37c2-0bf4-31c4-be28-24fba8eba7b9 | -17.61956 | -39.22408 | 2026-10-01 16:09:00 | NOAA-21 | ALCOBAÇA | BAHIA | Brasil | 2900801 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 7cdf1e7f-cfe0-3982-a29f-0f1c39011340 | -17.62629 | -44.34356 | 2026-10-01 16:09:00 | NOAA-21 | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 19.8 |
| fb301812-6bb5-35eb-b474-b06171bd2ff7 | -1.3193 | -49.0397 | 2026-10-01 16:10:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 59.4 |
| 8e2372d7-5dd4-3f02-ba4b-c9b6354d7087 | -1.2818 | -49.3803 | 2026-10-01 16:10:00 | GOES-19 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 61.4 |
| b6601b0c-f1a8-35c1-9009-4029ea177160 | -1.4303 | -48.9316 | 2026-10-01 16:10:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 73.9 |
| 513fb40e-8601-3f0e-9592-f44842d66638 | 2.1514 | -55.8172 | 2026-10-01 16:10:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 72.3 |
| 8539b957-757f-3475-92a0-92c91dfdeba4 | -1.4672 | -48.931 | 2026-10-01 16:10:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 70.5 |
| 4754206b-7546-3579-88e9-44d08e3c3d32 | -16.17625 | -42.88042 | 2026-10-01 16:11:00 | NOAA-21 | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 13.2 |
| 0cededf2-5a1f-3daa-ada1-8f95d1b144f0 | -14.2492 | -39.4881 | 2026-10-01 16:11:00 | NOAA-21 | UBAITABA | BAHIA | Brasil | 2932200 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| b301cd63-6081-36f8-9ead-1f4f14a72716 | -15.95737 | -45.9664 | 2026-10-01 16:11:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 72.7 |
| 3c233343-a8cf-3a93-a5a0-f8407a88ed3c | -15.62525 | -49.27066 | 2026-10-01 16:11:00 | NOAA-21 | JARAGUÁ | GOIÁS | Brasil | 5211800 | 52 | 33 | nan | nan | nan | Cerrado | 33.9 |
| 45c46506-2912-3b40-b2a3-1a97fcd6b2ad | -15.46257 | -41.45568 | 2026-10-01 16:11:00 | NOAA-21 | NINHEIRA | MINAS GERAIS | Brasil | 3144656 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.9 |
| 0511d82e-6f7c-3add-b887-6ab5cdab62a3 | -16.15512 | -42.86473 | 2026-10-01 16:11:00 | NOAA-21 | RIACHO DOS MACHADOS | MINAS GERAIS | Brasil | 3154507 | 31 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 90e50edf-ce74-37db-b567-e2e980d8502a | -14.36074 | -41.1932 | 2026-10-01 16:11:00 | NOAA-21 | ARACATU | BAHIA | Brasil | 2902005 | 29 | 33 | nan | nan | nan | Caatinga | 10.7 |
| 9fe360b5-2064-31c3-a431-a63bb567acde | -14.38069 | -44.74731 | 2026-10-01 16:11:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 23.4 |
| 6bfdb67c-594b-3436-b373-7998ede749a2 | -14.37202 | -44.74464 | 2026-10-01 16:11:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 25.9 |
| 77151fdd-35e8-3619-b11c-a4e9b4f14056 | -15.9084 | -42.52753 | 2026-10-01 16:11:00 | NOAA-21 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| ff6d5f54-788e-3055-836d-ab58f111ef3c | -15.21963 | -47.96586 | 2026-10-01 16:11:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |


[Clique aqui para ver as próximas entradas](README110.md)
