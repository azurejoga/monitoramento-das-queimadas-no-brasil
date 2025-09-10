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

## Dados Diários - Página 17

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| bc56f81d-a0fd-3344-9328-b2fff0dade7b | -20.98898 | -48.0017 | 2025-09-10 03:25:00 | NOAA-20 | PONTAL | SÃO PAULO | Brasil | 3540200 | 35 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 5b9e84b9-81fe-3762-8903-1b942dd7c104 | -20.0094 | -47.62469 | 2025-09-10 03:25:00 | NOAA-20 | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 7.2 |
| b8a9a218-ec56-3c61-aaf1-587ac7b8e620 | -18.46266 | -46.47833 | 2025-09-10 03:25:00 | NOAA-20 | PRESIDENTE OLEGÁRIO | MINAS GERAIS | Brasil | 3153400 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 18294a22-cdb1-3106-8380-d10eaed2e077 | -17.7416 | -44.49439 | 2025-09-10 03:25:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 68d12a00-1338-3bfc-a178-b245de3b905b | -17.71311 | -44.43934 | 2025-09-10 03:25:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 24480a7e-cdaa-32a4-a999-5aeb297c17c1 | -20.22179 | -40.36174 | 2025-09-10 03:25:00 | NOAA-20 | SERRA | ESPÍRITO SANTO | Brasil | 3205002 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 270454b9-b220-3b2f-bafb-39f770d08955 | -18.53303 | -43.28101 | 2025-09-10 03:25:00 | NOAA-20 | SERRO | MINAS GERAIS | Brasil | 3167103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 778789f1-2615-3fea-a793-e176a4d808e1 | -17.23431 | -46.08735 | 2025-09-10 03:25:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 3.9 |
| bd05dc85-62c8-3c58-9bfd-d8c4eed25cfc | -17.12468 | -39.53736 | 2025-09-10 03:25:00 | NOAA-20 | PRADO | BAHIA | Brasil | 2925501 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 113426aa-253b-3482-8f79-cc0da799c715 | -20.55132 | -47.62837 | 2025-09-10 03:25:00 | NOAA-20 | SÃO JOSÉ DA BELA VISTA | SÃO PAULO | Brasil | 3549508 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 05e3a134-ed84-3aa2-bb87-077a922a22e4 | -20.37591 | -46.63134 | 2025-09-10 03:25:00 | NOAA-20 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| cc9b8b44-fa68-37ce-b63e-16e88a34817a | -18.52137 | -43.28243 | 2025-09-10 03:25:00 | NOAA-20 | SERRO | MINAS GERAIS | Brasil | 3167103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| fe4d2b71-42b3-34c1-a835-bd5c8cfd7b1e | -15.21776 | -44.0405 | 2025-09-10 03:25:00 | NOAA-20 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d41b2fe2-4daa-3fea-b08d-1d170c49ab9e | -21.58263 | -43.97728 | 2025-09-10 03:25:00 | NOAA-20 | SANTA RITA DE IBITIPOCA | MINAS GERAIS | Brasil | 3159407 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 2fe0f0fd-65d3-3fd8-8a0b-93bb924166d8 | -19.99875 | -47.60962 | 2025-09-10 03:25:00 | NOAA-20 | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 5.0 |
| e487a017-ddef-35d7-83a1-346f0f92e2d8 | -19.92158 | -46.15732 | 2025-09-10 03:25:00 | NOAA-20 | TAPIRAÍ | MINAS GERAIS | Brasil | 3168200 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7ea8efec-c893-373c-8dec-41eda63d91d5 | -21.11741 | -47.73708 | 2025-09-10 03:25:00 | NOAA-20 | RIBEIRÃO PRETO | SÃO PAULO | Brasil | 3543402 | 35 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 17a29ed6-72ad-3bd2-8ce7-73e982e2e179 | -15.79797 | -41.42323 | 2025-09-10 03:25:00 | NOAA-20 | ÁGUAS VERMELHAS | MINAS GERAIS | Brasil | 3101003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| aa7ab588-7485-384e-9867-45737e9cc2e9 | -19.30349 | -43.25802 | 2025-09-10 03:25:00 | NOAA-20 | SÃO SEBASTIÃO DO RIO PRETO | MINAS GERAIS | Brasil | 3164803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| e5b04e60-b095-35bc-9544-b2353bbf229a | -14.75358 | -45.3371 | 2025-09-10 03:25:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 633d6f9f-82af-3717-91aa-bbdaf0f4ca65 | -15.14356 | -44.03325 | 2025-09-10 03:25:00 | NOAA-20 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f974f99b-b3fb-3c00-96e0-16c77a39f2e0 | -17.29801 | -46.73111 | 2025-09-10 03:25:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 4.5 |
| fbd0249c-f227-35b5-b493-ce025e1e5e63 | -17.74534 | -44.47746 | 2025-09-10 03:25:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 961378f8-5a81-37b3-8e52-305ae4cd7a02 | -21.02173 | -48.42091 | 2025-09-10 03:25:00 | NOAA-20 | BEBEDOURO | SÃO PAULO | Brasil | 3506102 | 35 | 33 | nan | nan | nan | Cerrado | 3.9 |
| c07cc149-0809-31b8-aed6-e9b1266852f0 | -17.30446 | -46.72937 | 2025-09-10 03:25:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 92fd3973-e9de-3169-ba2d-fdcbc662dd5e | -20.11657 | -47.69003 | 2025-09-10 03:25:00 | NOAA-20 | IGARAPAVA | SÃO PAULO | Brasil | 3520103 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3423fbc1-06a6-3417-ac94-235cb012e086 | -20.0087 | -47.6334 | 2025-09-10 03:25:00 | NOAA-20 | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 19.9 |
| 06fedd58-79c6-3998-b83a-4153fe31b25f | -20.54096 | -47.67938 | 2025-09-10 03:25:00 | NOAA-20 | SÃO JOSÉ DA BELA VISTA | SÃO PAULO | Brasil | 3549508 | 35 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 104b9ec4-6e54-32cc-8dde-69271f517642 | -20.22148 | -40.364 | 2025-09-10 03:25:00 | NOAA-20 | SERRA | ESPÍRITO SANTO | Brasil | 3205002 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 1004ed80-cae0-35dd-984a-56afc3343dca | -19.17442 | -43.06467 | 2025-09-10 03:25:00 | NOAA-20 | FERROS | MINAS GERAIS | Brasil | 3125903 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| b6aecce6-0e0f-3132-ad55-c737c276c1da | -20.28327 | -46.24577 | 2025-09-10 03:25:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 7.4 |
| ac3e7374-fba6-371d-a032-3fd091004019 | -17.31625 | -46.74016 | 2025-09-10 03:25:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1ac77327-427f-3255-af05-48d92d407396 | -17.33573 | -46.72229 | 2025-09-10 03:25:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 60d556c2-83e4-3180-982d-de7323f66da4 | -20.07232 | -47.5405 | 2025-09-10 03:25:00 | NOAA-20 | IGARAPAVA | SÃO PAULO | Brasil | 3520103 | 35 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 527d8d01-c3fa-3d1f-897e-8acd640f4bf0 | -15.22509 | -44.04074 | 2025-09-10 03:25:00 | NOAA-20 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b410a957-2912-35c4-8bf0-297d6930d2ca | -20.11072 | -47.80396 | 2025-09-10 03:25:00 | NOAA-20 | ARAMINA | SÃO PAULO | Brasil | 3503000 | 35 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 90cf15da-c725-374a-89b3-63d6363ee2cb | -17.73599 | -44.4917 | 2025-09-10 03:25:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 459c3c7b-4bee-381f-a032-fadecd22015f | -20.46165 | -43.95766 | 2025-09-10 03:25:00 | NOAA-20 | BELO VALE | MINAS GERAIS | Brasil | 3106408 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.7 |
| 03762da5-df76-3113-b2dc-68f246ff34e3 | -19.29164 | -47.98631 | 2025-09-10 03:25:00 | NOAA-20 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 9d3270d7-5283-3a28-ac91-cb0fff032f4f | -20.12332 | -47.69171 | 2025-09-10 03:25:00 | NOAA-20 | IGARAPAVA | SÃO PAULO | Brasil | 3520103 | 35 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9162873b-bf34-3e84-8515-a5c3111534cc | -19.64359 | -45.04485 | 2025-09-10 03:25:00 | NOAA-20 | LEANDRO FERREIRA | MINAS GERAIS | Brasil | 3138302 | 31 | 33 | nan | nan | nan | Cerrado | 6.8 |
| ff891524-27f7-30bd-9ae8-cf27c2e75389 | -18.46531 | -46.4752 | 2025-09-10 03:25:00 | NOAA-20 | PRESIDENTE OLEGÁRIO | MINAS GERAIS | Brasil | 3153400 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 737f9d50-df1f-3ba1-8307-3c4cd75341d3 | -16.28383 | -45.68762 | 2025-09-10 03:25:00 | NOAA-20 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 1ad15490-cb3e-309f-96bd-170d0390f81b | -19.99614 | -47.6204 | 2025-09-10 03:25:00 | NOAA-20 | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 7d478cd5-d89f-32d3-bc2b-4b11ffec41fe | -18.52656 | -43.28031 | 2025-09-10 03:25:00 | NOAA-20 | SERRO | MINAS GERAIS | Brasil | 3167103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| b8aa0dfc-e382-3876-a6ce-bca66faffffb | -17.30812 | -46.74453 | 2025-09-10 03:25:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 7592cd54-e903-326d-9ad4-c2216a2391ee | -16.84717 | -41.14778 | 2025-09-10 03:25:00 | NOAA-20 | JOAÍMA | MINAS GERAIS | Brasil | 3136009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 2e2d6d8c-f582-3e09-abdf-68efffdbd704 | -18.46393 | -46.47292 | 2025-09-10 03:25:00 | NOAA-20 | PRESIDENTE OLEGÁRIO | MINAS GERAIS | Brasil | 3153400 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| c0febec7-5131-3969-9d48-e4b322ae8209 | -20.13004 | -47.69355 | 2025-09-10 03:25:00 | NOAA-20 | IGARAPAVA | SÃO PAULO | Brasil | 3520103 | 35 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ed78b275-348a-3248-ab34-7a74cb13cdd5 | -18.95737 | -42.3901 | 2025-09-10 03:25:00 | NOAA-20 | AÇUCENA | MINAS GERAIS | Brasil | 3100500 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.3 |
| 6f132d54-2ddb-33fb-bd58-784549ac1b1b | -16.28378 | -45.68167 | 2025-09-10 03:25:00 | NOAA-20 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 984b9bd8-8387-3fa5-a754-cec4397f7c4e | -20.93331 | -45.79681 | 2025-09-10 03:25:00 | NOAA-20 | ILICÍNEA | MINAS GERAIS | Brasil | 3130507 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d88d8357-a783-3b92-afae-089365260b9f | -20.12431 | -47.69178 | 2025-09-10 03:25:00 | NOAA-20 | IGARAPAVA | SÃO PAULO | Brasil | 3520103 | 35 | 33 | nan | nan | nan | Cerrado | 2.1 |
| dc2a2f0f-0d98-34a9-be65-7351a89b7608 | -16.27735 | -45.68602 | 2025-09-10 03:25:00 | NOAA-20 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 00ff4279-7d6c-3a09-889e-2e870729503c | -19.35011 | -47.45203 | 2025-09-10 03:25:00 | NOAA-20 | SANTA JULIANA | MINAS GERAIS | Brasil | 3157708 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| bf568dcc-2277-3476-aef1-43c3989d94c7 | -20.06035 | -47.53973 | 2025-09-10 03:25:00 | NOAA-20 | IGARAPAVA | SÃO PAULO | Brasil | 3520103 | 35 | 33 | nan | nan | nan | Cerrado | 3.6 |
| b3b5c26d-8d91-341f-b5a3-d4e373c87c20 | -20.10452 | -47.83018 | 2025-09-10 03:25:00 | NOAA-20 | ARAMINA | SÃO PAULO | Brasil | 3503000 | 35 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 4b3dedc9-b086-3b3a-9a2a-632653ea8fa4 | -20.07361 | -47.54366 | 2025-09-10 03:25:00 | NOAA-20 | IGARAPAVA | SÃO PAULO | Brasil | 3520103 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c4b1ae69-6717-304b-b695-0639d1090d9b | -19.91533 | -46.15587 | 2025-09-10 03:25:00 | NOAA-20 | TAPIRAÍ | MINAS GERAIS | Brasil | 3168200 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 80490c6a-c296-3433-af1b-8ae17b1c6288 | -19.91414 | -46.161 | 2025-09-10 03:25:00 | NOAA-20 | TAPIRAÍ | MINAS GERAIS | Brasil | 3168200 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 460617d0-032a-341e-82ce-01e7d073e054 | -21.31891 | -43.89044 | 2025-09-10 03:25:00 | NOAA-20 | BARBACENA | MINAS GERAIS | Brasil | 3105608 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 67f6e99c-0c61-322a-90d3-42ad37c32462 | -19.20884 | -43.05861 | 2025-09-10 03:25:00 | NOAA-20 | FERROS | MINAS GERAIS | Brasil | 3125903 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 08677763-65a4-38c5-acfb-1f16b501bf14 | -18.52577 | -43.28408 | 2025-09-10 03:25:00 | NOAA-20 | SERRO | MINAS GERAIS | Brasil | 3167103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| dcf82c13-4c10-3a90-b0b1-723d022b6d7b | -17.30964 | -46.73789 | 2025-09-10 03:25:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 977baabc-8787-38f5-b583-1b824bd7800e | -18.45719 | -46.47231 | 2025-09-10 03:25:00 | NOAA-20 | PRESIDENTE OLEGÁRIO | MINAS GERAIS | Brasil | 3153400 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 31829914-f997-38cf-a6de-1e36ef298802 | -20.18665 | -44.45066 | 2025-09-10 03:25:00 | NOAA-20 | ITATIAIUÇU | MINAS GERAIS | Brasil | 3133709 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.0 |
| 68297614-8911-3187-a309-c2a61ed95f7d | -20.1875 | -44.44681 | 2025-09-10 03:25:00 | NOAA-20 | ITATIAIUÇU | MINAS GERAIS | Brasil | 3133709 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.7 |
| 40a41b3f-e49d-3186-b0b7-cb68522e9602 | -20.54447 | -47.62743 | 2025-09-10 03:25:00 | NOAA-20 | SÃO JOSÉ DA BELA VISTA | SÃO PAULO | Brasil | 3549508 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 23ed9300-3b55-30b9-92b9-d0709a9f98f7 | -18.00875 | -47.11004 | 2025-09-10 03:25:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| cfeac2f3-5f16-3cb2-a3bc-b37ad444c2e1 | -20.10593 | -47.82387 | 2025-09-10 03:25:00 | NOAA-20 | ARAMINA | SÃO PAULO | Brasil | 3503000 | 35 | 33 | nan | nan | nan | Cerrado | 2.5 |
| cd08d902-7d77-3a09-9a20-89845174dbb0 | -15.21806 | -44.04408 | 2025-09-10 03:25:00 | NOAA-20 | ITACARAMBI | MINAS GERAIS | Brasil | 3132107 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 17709ed5-b631-3a3a-a491-a314724e5807 | -20.55923 | -41.65054 | 2025-09-10 03:25:00 | NOAA-20 | IBITIRAMA | ESPÍRITO SANTO | Brasil | 3202553 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 4c899b0d-9fad-3b78-b575-8af5e7a48707 | -17.32546 | -46.70536 | 2025-09-10 03:25:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6f0457b5-76b4-3027-bb61-aef0f1d4c317 | -20.52027 | -47.63953 | 2025-09-10 03:25:00 | NOAA-20 | SÃO JOSÉ DA BELA VISTA | SÃO PAULO | Brasil | 3549508 | 35 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 8a77adfe-a805-3366-be89-a445f13ab118 | -20.86623 | -43.70938 | 2025-09-10 03:25:00 | NOAA-20 | CARANAÍBA | MINAS GERAIS | Brasil | 3113107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| d3bf86d0-ab02-3caf-ab1f-711878232329 | -19.51572 | -45.0191 | 2025-09-10 03:25:00 | NOAA-20 | MARTINHO CAMPOS | MINAS GERAIS | Brasil | 3140506 | 31 | 33 | nan | nan | nan | Cerrado | 6.3 |
| d19448c4-efc8-3927-939e-0d70de27bcc1 | -17.73281 | -44.49171 | 2025-09-10 03:25:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 32c42a38-9cf6-3a37-801d-ab58a723a860 | -21.39832 | -43.87339 | 2025-09-10 03:25:00 | NOAA-20 | ANTÔNIO CARLOS | MINAS GERAIS | Brasil | 3102902 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| fe9e7955-99be-3817-957c-9645e9b6a7eb | -17.24267 | -46.08073 | 2025-09-10 03:25:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 0c5278ea-b9e5-334c-9817-6d8dcce82dbf | -20.13097 | -47.69387 | 2025-09-10 03:25:00 | NOAA-20 | IGARAPAVA | SÃO PAULO | Brasil | 3520103 | 35 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 78ad7fb1-b7c3-3b24-add3-1d97790e1e00 | -20.99731 | -47.99702 | 2025-09-10 03:25:00 | NOAA-20 | PONTAL | SÃO PAULO | Brasil | 3540200 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4d53d1fb-2ac9-3ffd-b7bd-79fcd2801746 | -20.20194 | -41.5517 | 2025-09-10 03:25:00 | NOAA-20 | LAJINHA | MINAS GERAIS | Brasil | 3137700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| d931e7e1-714d-3578-8d89-642dc0775484 | -18.53197 | -43.28154 | 2025-09-10 03:25:00 | NOAA-20 | SERRO | MINAS GERAIS | Brasil | 3167103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 8b89b900-96fd-3d2b-a714-8b52f1068f61 | -20.93923 | -45.79857 | 2025-09-10 03:25:00 | NOAA-20 | ILICÍNEA | MINAS GERAIS | Brasil | 3130507 | 31 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 8fa4c352-5be2-33cb-9489-ac75d341098e | -17.7462 | -44.47361 | 2025-09-10 03:25:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| cb52d92e-06dc-3e39-b9ab-95bc1c8bacea | -19.8489 | -48.10433 | 2025-09-10 03:25:00 | NOAA-20 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5f30e7d4-ec0a-37ce-a994-6bee3a8d9da7 | -20.46605 | -43.96354 | 2025-09-10 03:25:00 | NOAA-20 | BELO VALE | MINAS GERAIS | Brasil | 3106408 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.7 |
| bf9f877c-4e8d-3ee2-8fb5-62deaacd8822 | -17.77672 | -46.13659 | 2025-09-10 03:25:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 23d68d7a-9782-3b3d-af14-5228486e00ef | -19.29414 | -47.98544 | 2025-09-10 03:25:00 | NOAA-20 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 9e4d798f-8aa2-3b7b-8b9c-5f8fab223412 | -17.30825 | -46.7482 | 2025-09-10 03:25:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 4.2 |
| e396b090-6cf4-392b-9a73-e7e181113abf | -20.15916 | -43.65777 | 2025-09-10 03:25:00 | NOAA-20 | ITABIRITO | MINAS GERAIS | Brasil | 3131901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 746441c3-9588-3ac3-b16a-72492d286822 | -21.5034 | -44.79368 | 2025-09-10 03:25:00 | NOAA-20 | LUMINÁRIAS | MINAS GERAIS | Brasil | 3138708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 17.4 |
| a4feb027-e979-3f5c-bc6c-29e612dc548f | -17.5562 | -44.5484 | 2025-09-10 03:25:00 | NOAA-20 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| eb2539a3-b6a9-3746-9068-6065f00a8050 | -19.29247 | -47.9924 | 2025-09-10 03:25:00 | NOAA-20 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 0e5689cf-4bc5-3e3b-979b-e854cf091e8d | -20.10912 | -47.8106 | 2025-09-10 03:25:00 | NOAA-20 | ARAMINA | SÃO PAULO | Brasil | 3503000 | 35 | 33 | nan | nan | nan | Cerrado | 8.4 |
| c506d1e0-5393-3836-9244-80db14a4105b | -20.01808 | -47.62444 | 2025-09-10 03:25:00 | NOAA-20 | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 4e59a4e9-1bf7-346c-8abe-c240996cec55 | -17.5573 | -44.54337 | 2025-09-10 03:25:00 | NOAA-20 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5d708f61-e62b-3910-8cd8-1609a7bf390e | -21.21754 | -44.14704 | 2025-09-10 03:25:00 | NOAA-20 | SÃO JOÃO DEL REI | MINAS GERAIS | Brasil | 3162500 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| cba0a9a7-c9a1-3cdb-b194-810932cb1aaf | -18.02301 | -47.14271 | 2025-09-10 03:25:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 20.4 |
| a9bc294f-a28f-3661-8f2e-98f578808e56 | -17.50376 | -43.73109 | 2025-09-10 03:25:00 | NOAA-20 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |


[Clique aqui para ver as próximas entradas](README18.md)
