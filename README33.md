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

## Dados Diários - Página 33

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6d4bf024-fb70-39e0-a4ad-e7e6e876474e | -21.81135 | -46.50709 | 2025-08-23 04:04:00 | NOAA-20 | POÇOS DE CALDAS | MINAS GERAIS | Brasil | 3151800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 8a1f87c2-f1fc-3b8b-8a2b-08198ba0acf4 | -19.38625 | -41.44134 | 2025-08-23 04:04:00 | NOAA-20 | SANTA RITA DO ITUETO | MINAS GERAIS | Brasil | 3159506 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.9 |
| a01ccd11-cdee-3f63-828b-7454d4670097 | -18.75653 | -46.6863 | 2025-08-23 04:04:00 | NOAA-20 | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4c79ccfd-dbce-39f4-bd79-5d96149e555e | -22.31011 | -43.17962 | 2025-08-23 04:04:00 | NOAA-20 | PETRÓPOLIS | RIO DE JANEIRO | Brasil | 3303906 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 3e537597-b990-339c-9740-6cae85a9940d | -17.59229 | -46.55702 | 2025-08-23 04:04:00 | NOAA-20 | LAGOA GRANDE | MINAS GERAIS | Brasil | 3137536 | 31 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 25f79b42-3dd0-3dfd-87bd-7283800a45ff | -15.54673 | -51.70012 | 2025-08-23 04:04:00 | NOAA-20 | MONTES CLAROS DE GOIÁS | GOIÁS | Brasil | 5213707 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f9b67b02-fc35-35c2-8fa8-61b9f4c3ee23 | -21.96551 | -45.59742 | 2025-08-23 04:04:00 | NOAA-20 | SÃO GONÇALO DO SAPUCAÍ | MINAS GERAIS | Brasil | 3162005 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.5 |
| c9f97282-4bcb-3c2b-9257-29bcfa40c0cf | -17.58401 | -46.56023 | 2025-08-23 04:04:00 | NOAA-20 | LAGOA GRANDE | MINAS GERAIS | Brasil | 3137536 | 31 | 33 | nan | nan | nan | Cerrado | 16.5 |
| 32d0a74f-407d-3d24-939f-b228d3c84b1f | -19.94456 | -47.48542 | 2025-08-23 04:04:00 | NOAA-20 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 39a3193c-87b7-3e5f-9711-8f842edafcc1 | -14.75705 | -55.99483 | 2025-08-23 04:04:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 4b84bda4-381d-3a41-95c8-045d110718a1 | -17.27133 | -46.76729 | 2025-08-23 04:04:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 21b44c52-eef5-3837-8945-2b0d6a9ee25e | -21.89621 | -48.16777 | 2025-08-23 04:04:00 | NOAA-20 | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 2820873e-16cb-3333-b892-a09dd24a6f32 | -15.22959 | -53.86243 | 2025-08-23 04:04:00 | NOAA-20 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 16fdbc5f-2245-329f-a977-694d81775466 | -17.58691 | -46.56564 | 2025-08-23 04:04:00 | NOAA-20 | LAGOA GRANDE | MINAS GERAIS | Brasil | 3137536 | 31 | 33 | nan | nan | nan | Cerrado | 6.6 |
| b18cae31-07f3-31b0-b1bf-925ce6cb2d5d | -21.85123 | -41.40159 | 2025-08-23 04:04:00 | NOAA-20 | CAMPOS DOS GOYTACAZES | RIO DE JANEIRO | Brasil | 3301009 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| d9d5f68f-1050-32ee-9a90-ff9c03b44e47 | -14.61671 | -54.81451 | 2025-08-23 04:04:00 | NOAA-20 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 1a351789-b574-3e84-a19e-5d29c009cffe | -19.97586 | -47.50786 | 2025-08-23 04:04:00 | NOAA-20 | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f6fbba0c-2578-3120-a745-8ef6b8585329 | -17.83166 | -44.40581 | 2025-08-23 04:04:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| d559b10a-ef45-38fc-9d46-88ddc8ec30ad | -22.49162 | -43.8213 | 2025-08-23 04:04:00 | NOAA-20 | BARRA DO PIRAÍ | RIO DE JANEIRO | Brasil | 3300308 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| f088523d-3f05-3f47-b9a7-c944b5f772d9 | -20.16532 | -45.3347 | 2025-08-23 04:04:00 | NOAA-20 | SANTO ANTÔNIO DO MONTE | MINAS GERAIS | Brasil | 3160405 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| b001bd16-510a-32f6-a91a-8ac62c60e4a1 | -15.22968 | -53.86575 | 2025-08-23 04:04:00 | NOAA-20 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 86f2445b-8de1-3885-a857-caed90433ade | -15.22359 | -53.86427 | 2025-08-23 04:04:00 | NOAA-20 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 9f343d4e-9f0f-3f45-a828-0e39be93fff1 | -15.2174 | -53.85955 | 2025-08-23 04:04:00 | NOAA-20 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 7707fcd4-805c-3727-a1ce-908444381b61 | -15.7199 | -48.21167 | 2025-08-23 04:04:00 | NOAA-20 | ÁGUAS LINDAS DE GOIÁS | GOIÁS | Brasil | 5200258 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 46c28c17-35f7-3f14-9625-f3e0f5ea21f0 | -14.66021 | -54.9208 | 2025-08-23 04:04:00 | NOAA-20 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 36847b53-7ac5-36d9-9d4b-420242ec134c | -22.42457 | -44.49745 | 2025-08-23 04:04:00 | NOAA-20 | RESENDE | RIO DE JANEIRO | Brasil | 3304201 | 33 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| 0a4fe888-5332-37e8-99a6-64c71e7b002d | -14.72815 | -55.41709 | 2025-08-23 04:04:00 | NOAA-20 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 424d315c-429d-300a-a55a-ca353454a26c | -17.6975 | -48.51709 | 2025-08-23 04:04:00 | NOAA-20 | CALDAS NOVAS | GOIÁS | Brasil | 5204508 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e671ac2e-1dec-3922-9434-66dd1b38e320 | -20.28149 | -46.65079 | 2025-08-23 04:04:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| cd5854db-037e-35e3-9458-ad30a2988ba1 | -14.62332 | -54.84704 | 2025-08-23 04:04:00 | NOAA-20 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| b18659ee-8c34-369e-8d96-3dfe7954f8ff | -18.30219 | -45.54718 | 2025-08-23 04:04:00 | NOAA-20 | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 2a52deba-bef2-3fc9-8b0e-a8ebddf4a8a4 | -18.29939 | -45.54237 | 2025-08-23 04:04:00 | NOAA-20 | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 352068ed-e09f-3968-a4d0-886b7170a4c7 | -19.67849 | -43.86633 | 2025-08-23 04:04:00 | NOAA-20 | LAGOA SANTA | MINAS GERAIS | Brasil | 3137601 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a4b66ef8-0fac-3670-a192-e3cac3295a98 | -20.43852 | -42.12726 | 2025-08-23 04:04:00 | NOAA-20 | LUISBURGO | MINAS GERAIS | Brasil | 3138674 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 222a64bc-1e02-3643-a0e1-e1bbcb4ab495 | -22.83566 | -45.18277 | 2025-08-23 04:04:00 | NOAA-20 | GUARATINGUETÁ | SÃO PAULO | Brasil | 3518404 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 8242d6c8-42db-3c02-8ff8-30bd549ecf4b | -21.95189 | -45.59474 | 2025-08-23 04:04:00 | NOAA-20 | SÃO GONÇALO DO SAPUCAÍ | MINAS GERAIS | Brasil | 3162005 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| dff51260-3b4d-3e79-a525-1cc6ee50d358 | -17.69779 | -48.49215 | 2025-08-23 04:04:00 | NOAA-20 | CALDAS NOVAS | GOIÁS | Brasil | 5204508 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3c76020d-3d87-3b25-923c-8dc9277e453e | -15.00602 | -54.8904 | 2025-08-23 04:04:00 | NOAA-20 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 6b5ea571-7844-32c5-a23c-80f0c184a14a | -15.54746 | -51.69647 | 2025-08-23 04:04:00 | NOAA-20 | MONTES CLAROS DE GOIÁS | GOIÁS | Brasil | 5213707 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8ffe7416-f8dc-3154-8a2f-56654b2b0920 | -21.42903 | -52.69118 | 2025-08-23 04:04:00 | NOAA-20 | SANTA RITA DO PARDO | MATO GROSSO DO SUL | Brasil | 5007554 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| fadf8f02-a469-30bd-aa5b-7935a2e1c070 | -20.48529 | -41.95243 | 2025-08-23 04:04:00 | NOAA-20 | ALTO JEQUITIBÁ | MINAS GERAIS | Brasil | 3153509 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 11de88b1-81bd-3b8c-b67b-23589389f757 | -17.58939 | -46.55162 | 2025-08-23 04:04:00 | NOAA-20 | LAGOA GRANDE | MINAS GERAIS | Brasil | 3137536 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d55b74ab-ed33-3246-a721-a3f45023bdda | -23.49586 | -46.00164 | 2025-08-23 04:04:00 | NOAA-20 | GUARAREMA | SÃO PAULO | Brasil | 3518305 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 83f7d632-589a-3763-9ecc-942a90844c07 | -21.96211 | -45.59671 | 2025-08-23 04:04:00 | NOAA-20 | SÃO GONÇALO DO SAPUCAÍ | MINAS GERAIS | Brasil | 3162005 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.5 |
| be5c5abd-d19a-3481-8d9b-af18f4d990fb | -20.22214 | -43.80276 | 2025-08-23 04:04:00 | NOAA-20 | ITABIRITO | MINAS GERAIS | Brasil | 3131901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.0 |
| 5891a98b-7a45-3408-b333-1837198708c3 | -22.17545 | -43.28281 | 2025-08-23 04:04:00 | NOAA-20 | PARAÍBA DO SUL | RIO DE JANEIRO | Brasil | 3303708 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 036f658d-bb34-3bfe-b99f-2f7d0b151807 | -17.26584 | -46.7762 | 2025-08-23 04:04:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 1f20b900-1160-382a-a80c-b920c3fd1e58 | -17.69707 | -48.49606 | 2025-08-23 04:04:00 | NOAA-20 | CALDAS NOVAS | GOIÁS | Brasil | 5204508 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 21584402-1edf-3c8e-9e61-950ede5e2941 | -22.18878 | -45.06197 | 2025-08-23 04:04:00 | NOAA-20 | SÃO SEBASTIÃO DO RIO VERDE | MINAS GERAIS | Brasil | 3164902 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 5f5333e0-2331-3b70-a7d8-cf9a9f679736 | -19.68182 | -43.86694 | 2025-08-23 04:04:00 | NOAA-20 | LAGOA SANTA | MINAS GERAIS | Brasil | 3137601 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f08516b3-6459-3746-9d74-8e92f5724519 | -14.4247 | -53.33724 | 2025-08-23 04:04:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d30484a7-312f-34b1-9f31-e42efbde8ab6 | -20.0076 | -46.43362 | 2025-08-23 04:04:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 43b28719-3300-3578-b1be-88d2d596982d | -18.96955 | -52.46898 | 2025-08-23 04:04:00 | NOAA-20 | CASSILÂNDIA | MATO GROSSO DO SUL | Brasil | 5002902 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bb0558d8-b60f-3d0a-812a-0f886853d068 | -20.87099 | -42.5444 | 2025-08-23 04:04:00 | NOAA-20 | ERVÁLIA | MINAS GERAIS | Brasil | 3124005 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.5 |
| 7bbb38d3-1aab-34ef-8104-6e492549a6c4 | -15.01093 | -54.8675 | 2025-08-23 04:04:00 | NOAA-20 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 9d4a0bc6-38cb-3480-a123-6ebb9b0a9531 | -19.79366 | -43.40334 | 2025-08-23 04:04:00 | NOAA-20 | BARÃO DE COCAIS | MINAS GERAIS | Brasil | 3105400 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| fe0ee1b6-f781-3303-b47a-9037c942aec1 | -18.84939 | -49.49039 | 2025-08-23 04:04:00 | NOAA-20 | ITUIUTABA | MINAS GERAIS | Brasil | 3134202 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 70712119-ebb8-3ea5-be48-12ca647e18fc | -22.27379 | -43.54512 | 2025-08-23 04:04:00 | NOAA-20 | VASSOURAS | RIO DE JANEIRO | Brasil | 3306206 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 628e2c6c-b15b-3494-a33d-e4b52d1effd0 | -20.35727 | -46.53724 | 2025-08-23 04:04:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e4c17cc2-7646-35b4-adc5-ef958023b9a4 | -22.82831 | -45.18535 | 2025-08-23 04:04:00 | NOAA-20 | GUARATINGUETÁ | SÃO PAULO | Brasil | 3518404 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 3cbd292a-6809-3b7b-9cfa-21656a1795ca | -20.0392 | -44.19731 | 2025-08-23 04:04:00 | NOAA-20 | BETIM | MINAS GERAIS | Brasil | 3106705 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| fc5022aa-4366-3567-86d6-2027c3fe846a | -22.53066 | -43.72486 | 2025-08-23 04:04:00 | NOAA-20 | MENDES | RIO DE JANEIRO | Brasil | 3302809 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| d74c8d42-5084-30b3-a537-3c5bc4f6f390 | -21.88872 | -48.18692 | 2025-08-23 04:04:00 | NOAA-20 | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8aff5ac6-cb1d-38fe-b7b4-423ce91e70e0 | -19.97832 | -47.51041 | 2025-08-23 04:04:00 | NOAA-20 | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b2a105be-f4bd-32bd-9635-b834ce4accb8 | -20.09815 | -47.77499 | 2025-08-23 04:04:00 | NOAA-20 | ARAMINA | SÃO PAULO | Brasil | 3503000 | 35 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 52814115-2215-3067-bc14-d3d501c203b9 | -22.55225 | -49.76334 | 2025-08-23 04:04:00 | NOAA-20 | SÃO PEDRO DO TURVO | SÃO PAULO | Brasil | 3550506 | 35 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 625f71c5-dcd3-3200-b4ca-db6325ffba89 | -17.60628 | -46.69889 | 2025-08-23 04:04:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fece5668-7f1c-36d2-af43-e2fedf31ea03 | -22.1904 | -44.55753 | 2025-08-23 04:04:00 | NOAA-20 | BOCAINA DE MINAS | MINAS GERAIS | Brasil | 3107208 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| b931859c-db48-38b4-a23a-b6c1c40e5e3f | -22.47525 | -44.2676 | 2025-08-23 04:04:00 | NOAA-20 | BARRA MANSA | RIO DE JANEIRO | Brasil | 3300407 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 69a984c7-81fc-3f41-beb2-03026a69e752 | -17.61103 | -46.69212 | 2025-08-23 04:04:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 979923ee-2100-3e14-a5c1-41b2103b89eb | -14.66145 | -54.92487 | 2025-08-23 04:04:00 | NOAA-20 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 9951b088-46b9-3a5b-9f93-242995221263 | -20.30025 | -42.24236 | 2025-08-23 04:04:00 | NOAA-20 | MATIPÓ | MINAS GERAIS | Brasil | 3140902 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 24fe70fd-0e71-3c74-ae94-0097d41eb73d | -17.26944 | -46.77319 | 2025-08-23 04:04:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ed2e4e6c-c3cd-3501-9ee1-b5b5a83453c3 | -16.32799 | -46.7735 | 2025-08-23 04:04:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2cb52dc9-0290-38e6-825a-15e5a25b8e47 | -15.01822 | -54.89713 | 2025-08-23 04:04:00 | NOAA-20 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 5.2 |
| eaf56178-b501-334b-92b4-cfaffd88f969 | -19.77997 | -45.65512 | 2025-08-23 04:04:00 | NOAA-20 | LUZ | MINAS GERAIS | Brasil | 3138807 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 100fe59f-9ba6-3002-b5e4-4a50fba822ff | -14.61269 | -54.86437 | 2025-08-23 04:04:00 | NOAA-20 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| bb2d7470-10c7-30cf-b584-ea21309fe3cb | -15.01108 | -54.89167 | 2025-08-23 04:04:00 | NOAA-20 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 79cdac53-f5b2-3c60-9a99-2c413edd3a32 | -15.71108 | -48.23518 | 2025-08-23 04:04:00 | NOAA-20 | ÁGUAS LINDAS DE GOIÁS | GOIÁS | Brasil | 5200258 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c1c78c98-ed40-3508-ab1c-5562dc8cb064 | -19.4267 | -47.22575 | 2025-08-23 04:04:00 | NOAA-20 | PERDIZES | MINAS GERAIS | Brasil | 3149804 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2b60818b-eee4-3824-8697-423b82e25024 | -20.2734 | -42.83449 | 2025-08-23 04:04:00 | NOAA-20 | SANTA CRUZ DO ESCALVADO | MINAS GERAIS | Brasil | 3157401 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| cd127086-c2fc-3b10-a4ed-df2b1f473a0b | -18.28743 | -45.5485 | 2025-08-23 04:04:00 | NOAA-20 | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 0176a2c8-fd54-37b5-8f06-86c92a80a4a1 | -15.02341 | -54.89768 | 2025-08-23 04:04:00 | NOAA-20 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 5311257e-231f-393e-8fe5-6966048a583c | -21.95529 | -45.59542 | 2025-08-23 04:04:00 | NOAA-20 | SÃO GONÇALO DO SAPUCAÍ | MINAS GERAIS | Brasil | 3162005 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 8a9a5cb9-46df-31b5-be31-a94e0d6351e4 | -14.75892 | -55.99573 | 2025-08-23 04:04:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| fa94313d-61b7-321d-8c52-dfd82e3c6530 | -19.3823 | -41.44459 | 2025-08-23 04:04:00 | NOAA-20 | SANTA RITA DO ITUETO | MINAS GERAIS | Brasil | 3159506 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.9 |
| 1ebb3411-f1e4-3016-98da-cd3e6325f04f | -15.55592 | -50.31838 | 2025-08-23 04:04:00 | NOAA-20 | FAINA | GOIÁS | Brasil | 5207535 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| ae71f1e6-8b21-33ea-ae1d-12c776e2615d | -17.58856 | -46.55629 | 2025-08-23 04:04:00 | NOAA-20 | LAGOA GRANDE | MINAS GERAIS | Brasil | 3137536 | 31 | 33 | nan | nan | nan | Cerrado | 5.3 |
| db18ca34-643c-38dc-8c4a-7f423f5af843 | -16.38898 | -49.15258 | 2025-08-23 04:04:00 | NOAA-20 | ANÁPOLIS | GOIÁS | Brasil | 5201108 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0b9c79af-056d-362e-ba91-b2b833a16ca8 | -17.04843 | -47.1403 | 2025-08-23 04:04:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 573d2a46-13df-349b-b55c-03078b40f511 | -19.96905 | -47.51807 | 2025-08-23 04:04:00 | NOAA-20 | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a2494444-2c0d-339b-9015-64ca5f560cf1 | -19.43581 | -42.5457 | 2025-08-23 04:04:00 | NOAA-20 | SANTANA DO PARAÍSO | MINAS GERAIS | Brasil | 3158953 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| a2bcb087-793a-3b33-bea6-2d4f693ee857 | -14.66021 | -54.93066 | 2025-08-23 04:04:00 | NOAA-20 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 01176782-8939-30cf-a089-fbc82ef78281 | -15.02506 | -54.89705 | 2025-08-23 04:04:00 | NOAA-20 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 5.2 |
| b5800ccb-ef15-3d19-b170-8fa6171404b6 | -22.16996 | -43.27417 | 2025-08-23 04:04:00 | NOAA-20 | PARAÍBA DO SUL | RIO DE JANEIRO | Brasil | 3303708 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| b4cfea61-50e4-34bc-bf26-26454095a667 | -20.0932 | -47.73692 | 2025-08-23 04:04:00 | NOAA-20 | IGARAPAVA | SÃO PAULO | Brasil | 3520103 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 19ac9d51-d33e-3081-aa20-27d8d89bda69 | -19.95521 | -47.51349 | 2025-08-23 04:04:00 | NOAA-20 | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 51b2028f-2562-3146-a0f8-f03b022b9384 | -20.28312 | -46.64164 | 2025-08-23 04:04:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ffc64b0b-765d-322b-b05c-07e37884ff55 | -18.31204 | -45.51105 | 2025-08-23 04:04:00 | NOAA-20 | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d805fe13-8c30-30a5-959a-cffbda6c19aa | -22.91809 | -43.50459 | 2025-08-23 04:04:00 | NOAA-20 | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |


[Clique aqui para ver as próximas entradas](README34.md)
