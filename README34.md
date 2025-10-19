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

## Dados Diários - Página 34

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5e30038b-b6a8-333e-bda0-cf6f8a59e188 | -16.03694 | -42.37299 | 2025-10-19 04:14:00 | NPP-375D | NOVORIZONTE | MINAS GERAIS | Brasil | 3145372 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 272c198b-aab5-38d8-9133-d019430fe29c | -15.79175 | -43.64569 | 2025-10-19 04:14:00 | NPP-375D | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4489ad2e-b39e-3558-811e-18b4c32130db | -16.8051 | -42.82184 | 2025-10-19 04:14:00 | NPP-375D | CRISTÁLIA | MINAS GERAIS | Brasil | 3120300 | 31 | 33 | nan | nan | nan | Cerrado | 11.5 |
| b6aee346-b104-3f0e-ad68-10f8f13da7dc | -16.82092 | -40.16891 | 2025-10-19 04:14:00 | NPP-375D | JUCURUÇU | BAHIA | Brasil | 2918456 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 52bc5333-1e56-39bb-81cc-a60a8a03d988 | -15.69114 | -45.3462 | 2025-10-19 04:14:00 | NPP-375D | CHAPADA GAÚCHA | MINAS GERAIS | Brasil | 3116159 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0c517b83-9c66-3900-b019-aa75bfd75bdd | -16.82283 | -41.79625 | 2025-10-19 04:14:00 | NPP-375D | ARAÇUAÍ | MINAS GERAIS | Brasil | 3103405 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 584fba15-1f50-3dc2-aef7-4e6edb0c498a | -15.27157 | -43.21957 | 2025-10-19 04:14:00 | NPP-375D | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 19581c9c-5a80-3408-84f2-0ea507433f33 | -16.81171 | -41.00409 | 2025-10-19 04:14:00 | NPP-375D | JOAÍMA | MINAS GERAIS | Brasil | 3136009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 2bc1f0c9-b7ae-3f71-9f99-5d00a2a38f50 | -16.7445 | -42.76623 | 2025-10-19 04:14:00 | NPP-375D | CRISTÁLIA | MINAS GERAIS | Brasil | 3120300 | 31 | 33 | nan | nan | nan | Cerrado | 0.2 |
| 464b93c8-dea7-37f2-b07a-c3342b6b453c | -14.46884 | -43.34415 | 2025-10-19 04:14:00 | NPP-375D | PALMAS DE MONTE ALTO | BAHIA | Brasil | 2923407 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| bac7a884-9e1c-3fc1-9bfc-fad0bb09af3c | -14.55444 | -43.51161 | 2025-10-19 04:14:00 | NPP-375D | IUIU | BAHIA | Brasil | 2917334 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c3e605f8-0d27-3d36-b0ba-5bf9812a24c4 | -16.75405 | -42.77165 | 2025-10-19 04:14:00 | NPP-375D | CRISTÁLIA | MINAS GERAIS | Brasil | 3120300 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 598d5722-b7b6-3b60-a9c5-0d007d86d574 | -16.98037 | -41.15333 | 2025-10-19 04:14:00 | NPP-375D | JOAÍMA | MINAS GERAIS | Brasil | 3136009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.4 |
| 5446fa92-de09-3552-bd77-a201110f9574 | -15.2754 | -46.01278 | 2025-10-19 04:14:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d9ae0bab-2315-33a0-a0b5-6b8d0528fe8f | -16.75629 | -42.77966 | 2025-10-19 04:14:00 | NPP-375D | CRISTÁLIA | MINAS GERAIS | Brasil | 3120300 | 31 | 33 | nan | nan | nan | Cerrado | 64.8 |
| 3d1bed9b-03e6-3a78-9307-615cc6366bd4 | -15.51597 | -41.67767 | 2025-10-19 04:14:00 | NPP-375D | ÁGUAS VERMELHAS | MINAS GERAIS | Brasil | 3101003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 2d6e9dd7-8d9e-3f59-83c9-4745e33171d3 | -14.1386 | -44.68956 | 2025-10-19 04:14:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 71c5dcc3-5d72-3b0d-9030-72bb66cb9e4c | -15.25528 | -43.58444 | 2025-10-19 04:14:00 | NPP-375D | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d53baa78-b3ee-3673-abd8-f60ef8754e1c | -14.18716 | -44.79646 | 2025-10-19 04:14:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 1a741caa-0fe8-3f8d-a40c-e4380a798e1f | -15.01676 | -41.99395 | 2025-10-19 04:14:00 | NPP-375D | CONDEÚBA | BAHIA | Brasil | 2908705 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| f4ff8d5b-006a-3a6a-87d8-044dd213b798 | -16.78659 | -42.80745 | 2025-10-19 04:14:00 | NPP-375D | CRISTÁLIA | MINAS GERAIS | Brasil | 3120300 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| bf578a28-ffbf-37fb-9f94-75a55768749b | -16.98336 | -41.15794 | 2025-10-19 04:14:00 | NPP-375D | JOAÍMA | MINAS GERAIS | Brasil | 3136009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.4 |
| 28660986-a656-3c48-b906-2c44c9a1137b | -15.97794 | -41.20809 | 2025-10-19 04:14:00 | NPP-375D | PEDRA AZUL | MINAS GERAIS | Brasil | 3148707 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| e95f39bc-05b0-3005-9035-e4adf0df835c | -15.79897 | -43.64322 | 2025-10-19 04:14:00 | NPP-375D | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a687e7a4-30b3-3799-931f-d07987a77cfb | -15.09125 | -40.16917 | 2025-10-19 04:14:00 | NPP-375D | ITAMBÉ | BAHIA | Brasil | 2915809 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 903cfa04-7fc6-3836-96a3-7e709ccb2e72 | -14.91485 | -46.71782 | 2025-10-19 04:14:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 040818cf-6544-3761-acbd-317d83d56ffb | -16.78826 | -42.81908 | 2025-10-19 04:14:00 | NPP-375D | CRISTÁLIA | MINAS GERAIS | Brasil | 3120300 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ff9010cf-8180-30c3-a342-ea00d3ad8a1e | -16.78043 | -42.75706 | 2025-10-19 04:14:00 | NPP-375D | CRISTÁLIA | MINAS GERAIS | Brasil | 3120300 | 31 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 37208094-71b6-3d6e-9c37-cb3c1b7476c7 | -14.13523 | -44.68898 | 2025-10-19 04:14:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ac6614d8-e360-3b3a-a4c8-0a5d6694a43f | -15.52759 | -45.34526 | 2025-10-19 04:14:00 | NPP-375D | CHAPADA GAÚCHA | MINAS GERAIS | Brasil | 3116159 | 31 | 33 | nan | nan | nan | Cerrado | 10.9 |
| ef511e8b-686b-368f-a7c5-811a4390eabf | -15.78241 | -43.25364 | 2025-10-19 04:14:00 | NPP-375D | NOVA PORTEIRINHA | MINAS GERAIS | Brasil | 3145059 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 3ad31ed1-3500-30f5-9711-40228eaa92fe | -15.79231 | -43.6421 | 2025-10-19 04:14:00 | NPP-375D | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f2316b6e-54c4-3800-9f1f-65d504a90867 | -14.1848 | -44.49027 | 2025-10-19 04:14:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4d590035-9963-3790-92f1-9b070d16f4f6 | -16.50831 | -40.78527 | 2025-10-19 04:14:00 | NPP-375D | JEQUITINHONHA | MINAS GERAIS | Brasil | 3135803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| c2e17aeb-cd5e-356b-9340-b18c87f3fd17 | -15.26639 | -43.57895 | 2025-10-19 04:14:00 | NPP-375D | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| b3d02d58-a923-3d1f-867d-32343c60b02f | -16.97979 | -41.15742 | 2025-10-19 04:14:00 | NPP-375D | JOAÍMA | MINAS GERAIS | Brasil | 3136009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.4 |
| 74aeae2f-3d10-376d-92b9-ea1ac8730af2 | -16.14357 | -41.15634 | 2025-10-19 04:14:00 | NPP-375D | JEQUITINHONHA | MINAS GERAIS | Brasil | 3135803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 35c728e5-a547-379d-9784-1649e5cc4905 | -16.78325 | -42.7613 | 2025-10-19 04:14:00 | NPP-375D | CRISTÁLIA | MINAS GERAIS | Brasil | 3120300 | 31 | 33 | nan | nan | nan | Cerrado | 8.1 |
| d9365d31-626c-35a6-b965-b979eb0eb537 | -16.82967 | -41.18388 | 2025-10-19 04:14:00 | NPP-375D | MONTE FORMOSO | MINAS GERAIS | Brasil | 3143153 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| bd1d69bc-1eea-3195-8e34-43ec92a67d77 | -14.45009 | -45.56724 | 2025-10-19 04:14:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 78629116-5fd6-37c0-94e0-796eb1944f5f | -16.76695 | -42.77765 | 2025-10-19 04:14:00 | NPP-375D | CRISTÁLIA | MINAS GERAIS | Brasil | 3120300 | 31 | 33 | nan | nan | nan | Cerrado | 58.7 |
| 1e2d0b19-e28d-3eeb-a6a8-5fabb74951fd | -14.0274 | -47.09162 | 2025-10-19 04:14:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3ad807cb-6e06-3423-9df0-1360dec767e4 | -14.91411 | -46.72206 | 2025-10-19 04:14:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| ff4ecc94-6d89-3f34-ad8b-ebce0be24a09 | -14.74711 | -42.46392 | 2025-10-19 04:14:00 | NPP-375D | JACARACI | BAHIA | Brasil | 2917409 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 2ac4e8b5-4d9a-3f31-8223-c63e23b40caf | -17.08044 | -43.26937 | 2025-10-19 04:14:00 | NPP-375D | ITACAMBIRA | MINAS GERAIS | Brasil | 3132008 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1f4b2df1-a24a-3eae-b5df-7117b9e15008 | -15.01252 | -40.45954 | 2025-10-19 04:14:00 | NPP-375D | CAATIBA | BAHIA | Brasil | 2904803 | 29 | 33 | nan | nan | nan | Mata Atlântica | 9.9 |
| 2196237b-7294-372e-a73e-f406a088c351 | -15.79727 | -43.65399 | 2025-10-19 04:14:00 | NPP-375D | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a66a50ac-757c-3ab0-b2db-35667b4d68f1 | -14.55501 | -43.50804 | 2025-10-19 04:14:00 | NPP-375D | IUIU | BAHIA | Brasil | 2917334 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b72f607e-da11-3179-b65f-e2b41eb0ab87 | -15.52357 | -45.34843 | 2025-10-19 04:14:00 | NPP-375D | CHAPADA GAÚCHA | MINAS GERAIS | Brasil | 3116159 | 31 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 07d41201-b081-3e2f-b0d1-e600a9679a0d | -16.75292 | -42.77909 | 2025-10-19 04:14:00 | NPP-375D | CRISTÁLIA | MINAS GERAIS | Brasil | 3120300 | 31 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 77057830-9c96-38fe-b906-d3a92d208766 | -14.47794 | -45.59208 | 2025-10-19 04:14:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 3117c986-41f7-3897-9924-0347687a4042 | -16.14295 | -41.13554 | 2025-10-19 04:14:00 | NPP-375D | JEQUITINHONHA | MINAS GERAIS | Brasil | 3135803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| e931e536-cae0-3a6f-acf6-785c77a72e93 | -16.34616 | -41.75343 | 2025-10-19 04:14:00 | NPP-375D | COMERCINHO | MINAS GERAIS | Brasil | 3117009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| e11ce880-527b-3492-8833-9ec3157157e8 | -16.78606 | -42.76552 | 2025-10-19 04:14:00 | NPP-375D | CRISTÁLIA | MINAS GERAIS | Brasil | 3120300 | 31 | 33 | nan | nan | nan | Cerrado | 15.6 |
| 464d8ac7-29d3-3c0f-bfb4-7ccd32552ddd | -16.14237 | -41.1396 | 2025-10-19 04:14:00 | NPP-375D | JEQUITINHONHA | MINAS GERAIS | Brasil | 3135803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 26d78ab6-5704-3d7f-af71-8f23d0a66721 | -15.48699 | -41.3381 | 2025-10-19 04:14:00 | NPP-375D | CÂNDIDO SALES | BAHIA | Brasil | 2906709 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| faa906b1-b2c3-3c53-b93c-42521da6084b | -15.81629 | -42.52047 | 2025-10-19 04:14:00 | NPP-375D | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 79ca2518-b083-3944-afc6-936f2af68ce1 | -15.47196 | -45.94048 | 2025-10-19 04:14:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| bb3fb491-8ef6-3be1-8e73-347dedd938fb | -15.79507 | -43.64625 | 2025-10-19 04:14:00 | NPP-375D | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 30878e7c-f093-3cb6-ac3d-0a2e8d90bd66 | -15.78898 | -43.64154 | 2025-10-19 04:14:00 | NPP-375D | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b4a77fe0-788c-3174-a0c4-74b6587aefae | -15.51052 | -41.53865 | 2025-10-19 04:14:00 | NPP-375D | NINHEIRA | MINAS GERAIS | Brasil | 3144656 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| f81cf1e7-2990-3366-9bb9-3ee7538433c5 | -15.01671 | -41.99311 | 2025-10-19 04:14:00 | NPP-375D | CONDEÚBA | BAHIA | Brasil | 2908705 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| f9e7a375-67e0-3694-afda-90a8ce89346d | -16.81127 | -42.8266 | 2025-10-19 04:14:00 | NPP-375D | CRISTÁLIA | MINAS GERAIS | Brasil | 3120300 | 31 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 4638d14b-bc76-3554-959f-fcff103f746e | -15.78297 | -43.25007 | 2025-10-19 04:14:00 | NPP-375D | NOVA PORTEIRINHA | MINAS GERAIS | Brasil | 3145059 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f6af552f-ec8f-3f91-b381-9d213592f432 | -15.18805 | -43.56596 | 2025-10-19 04:14:00 | NPP-375D | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 1.7 |
| c69d1a0e-b09f-386e-872c-80643ae260c6 | -15.79451 | -43.64984 | 2025-10-19 04:14:00 | NPP-375D | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7b93f7a1-35e0-30bc-85fc-10b51722c6ba | -14.90536 | -46.7295 | 2025-10-19 04:14:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 86dbee35-7266-3d7c-b088-a7047d2f3c4b | -15.69126 | -42.5874 | 2025-10-19 04:14:00 | NPP-375D | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 097a491c-38e8-342d-8205-087f850b597e | -15.44678 | -45.91638 | 2025-10-19 04:14:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 746748a3-7142-3cbc-b751-e8735b2a9634 | -15.2438 | -43.85072 | 2025-10-19 04:14:00 | NPP-375D | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5dd582bc-1c2e-3434-a4a2-be2fa902b666 | -15.53075 | -45.69848 | 2025-10-19 04:14:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 1e3049d5-353c-3e74-9f4f-10beb5b47f4d | -14.48702 | -45.60167 | 2025-10-19 04:14:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 31c98443-893c-3713-a0c5-32d00acc818d | -16.66871 | -42.10957 | 2025-10-19 04:14:00 | NPP-375D | CORONEL MURTA | MINAS GERAIS | Brasil | 3119500 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 030ccf6d-e868-3ced-89e4-347fd64965d3 | -16.78719 | -42.75809 | 2025-10-19 04:14:00 | NPP-375D | CRISTÁLIA | MINAS GERAIS | Brasil | 3120300 | 31 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 7ffe1d07-ca0e-3975-8a72-38fc54f2240e | -14.54835 | -43.50693 | 2025-10-19 04:14:00 | NPP-375D | IUIU | BAHIA | Brasil | 2917334 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1a04aeeb-c91a-3886-8e9f-51b1d8885980 | -16.77875 | -42.7682 | 2025-10-19 04:14:00 | NPP-375D | CRISTÁLIA | MINAS GERAIS | Brasil | 3120300 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 62a01cc1-086d-348d-9b25-89871d0b176f | -15.78575 | -43.2542 | 2025-10-19 04:14:00 | NPP-375D | NOVA PORTEIRINHA | MINAS GERAIS | Brasil | 3145059 | 31 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 0482b904-223e-3a53-b912-0a29457a2d3e | -15.25861 | -43.585 | 2025-10-19 04:14:00 | NPP-375D | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0dece63d-6c45-3827-b666-0a64ad05e889 | -16.81184 | -42.82288 | 2025-10-19 04:14:00 | NPP-375D | CRISTÁLIA | MINAS GERAIS | Brasil | 3120300 | 31 | 33 | nan | nan | nan | Cerrado | 4.0 |
| f14f3685-f78a-3efd-9346-6eaca07c388c | -14.21156 | -44.39393 | 2025-10-19 04:14:00 | NPP-375D | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| b890a51b-3507-3ab0-b525-24d35f0aa89c | -16.77931 | -42.7645 | 2025-10-19 04:14:00 | NPP-375D | CRISTÁLIA | MINAS GERAIS | Brasil | 3120300 | 31 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 8178b25a-7da7-3008-ae1e-1fe3195c887f | -15.702 | -43.48368 | 2025-10-19 04:14:00 | NPP-375D | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5827fa83-3ad8-3179-ad02-3eb05adbd531 | -16.75965 | -42.78023 | 2025-10-19 04:14:00 | NPP-375D | CRISTÁLIA | MINAS GERAIS | Brasil | 3120300 | 31 | 33 | nan | nan | nan | Cerrado | 64.8 |
| 8ef987df-8991-3ae7-8878-e4b665ac169b | -15.463 | -45.94778 | 2025-10-19 04:14:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c2fc20f4-ae60-3df7-add1-024e2c8f5a88 | -13.93025 | -45.60798 | 2025-10-19 04:14:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7024171a-725e-3eb7-8d5e-558002afc086 | -15.46715 | -45.94771 | 2025-10-19 04:14:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 0.2 |
| c827dd13-7df4-3838-9281-d093ba2a439f | -15.81967 | -42.52102 | 2025-10-19 04:14:00 | NPP-375D | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| e831aa5c-ff13-35bf-8909-f275c4e2e84b | -14.4786 | -45.58819 | 2025-10-19 04:14:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| c1ddd273-deed-363d-b046-2686687e1dd3 | -15.38111 | -44.35215 | 2025-10-19 04:14:00 | NPP-375D | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 653247f3-a1a8-3c0e-9f7a-7d454c271d29 | -16.74394 | -42.76998 | 2025-10-19 04:14:00 | NPP-375D | CRISTÁLIA | MINAS GERAIS | Brasil | 3120300 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 54cf5905-2ab2-3a08-a8e2-bff28afe3593 | -14.46064 | -45.58908 | 2025-10-19 04:14:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 0feb0915-41be-347f-ab30-0c3fa5541e64 | -14.47217 | -43.34471 | 2025-10-19 04:14:00 | NPP-375D | PALMAS DE MONTE ALTO | BAHIA | Brasil | 2923407 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 3e76dc01-b451-37be-864c-54ff1cb70e7f | -13.93853 | -45.60131 | 2025-10-19 04:14:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 5.8 |
| ab45a80a-5752-33cf-8a6a-40ed053753d0 | -14.91793 | -41.4198 | 2025-10-19 04:14:00 | NPP-375D | TREMEDAL | BAHIA | Brasil | 2931806 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 22ba6c23-010e-36d0-925a-cca5f894ca84 | -16.74057 | -42.7694 | 2025-10-19 04:14:00 | NPP-375D | CRISTÁLIA | MINAS GERAIS | Brasil | 3120300 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c9d09048-5c8a-35af-805d-7df1e487d4d1 | -15.78509 | -43.64457 | 2025-10-19 04:14:00 | NPP-375D | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e0415b95-e3e8-3d85-8906-7cd99fa12806 | -16.75798 | -42.76848 | 2025-10-19 04:14:00 | NPP-375D | CRISTÁLIA | MINAS GERAIS | Brasil | 3120300 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1b40ece2-4cd5-3aa5-915a-5f97767df7c4 | -17.08868 | -41.69507 | 2025-10-19 04:14:00 | NPP-375D | CARAÍ | MINAS GERAIS | Brasil | 3113008 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| fbe74bbe-ba6e-3a7e-9d06-ca24cd19b65b | -14.55112 | -43.51105 | 2025-10-19 04:14:00 | NPP-375D | IUIU | BAHIA | Brasil | 2917334 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ad7dfce4-a17f-3316-a18b-c9781c190129 | -15.98688 | -41.80289 | 2025-10-19 04:14:00 | NPP-375D | SANTA CRUZ DE SALINAS | MINAS GERAIS | Brasil | 3157377 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |


[Clique aqui para ver as próximas entradas](README35.md)
