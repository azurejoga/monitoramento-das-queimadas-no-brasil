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

## Dados Diários - Página 39

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 56caf18e-96eb-3efb-8ace-70969ee0d1f3 | -15.23095 | -50.11772 | 2025-10-02 04:04:00 | NOAA-21 | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 21.6 |
| fb8f0cf9-5d29-30b4-802d-47288d3c2726 | -12.94228 | -48.43274 | 2025-10-02 04:04:00 | NOAA-21 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 10.1 |
| e2034757-4a6b-3b32-b1cc-554ac46d84f2 | -13.29847 | -50.67838 | 2025-10-02 04:04:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 6269af14-8245-3882-966a-8f03af46feea | -12.91658 | -47.16219 | 2025-10-02 04:04:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9c5c7888-5064-355d-990c-2f657454f8ba | -13.80977 | -47.53035 | 2025-10-02 04:04:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| a99fd0e5-f930-39eb-a7d5-45b80ba3c286 | -15.14623 | -48.02056 | 2025-10-02 04:04:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 40272b89-f57f-36e5-921f-aa4e08a973a5 | -15.40905 | -47.06308 | 2025-10-02 04:04:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| dc721162-5bee-3573-8dae-38104b5c995f | -15.31094 | -46.39301 | 2025-10-02 04:04:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a2d72666-7297-31a3-8442-7043ec181948 | -14.28695 | -45.96859 | 2025-10-02 04:04:00 | NOAA-21 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 61a1bbfe-0021-3c5d-b90a-b936b903711f | -14.22208 | -46.11845 | 2025-10-02 04:04:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| caf1e966-5895-3601-9c03-1f17fb5251e3 | -13.40471 | -47.78849 | 2025-10-02 04:04:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 624da7ae-27fa-39f1-a8dc-e036725f85b4 | -15.34861 | -47.08821 | 2025-10-02 04:04:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 20.4 |
| d3192468-2dd7-3a2a-bf89-8a0cb6d70bbe | -15.51011 | -45.904 | 2025-10-02 04:04:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 4b89cb24-0243-3fbf-b018-bc119d2c1e1f | -14.22589 | -46.11916 | 2025-10-02 04:04:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 67ab7f9c-7c40-3ae2-98e3-fecca66f8b74 | -13.76863 | -48.00019 | 2025-10-02 04:04:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 4de2a1b9-b927-3008-936d-07353e03696b | -15.39592 | -47.04527 | 2025-10-02 04:04:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| dbe6ee91-7674-3a77-ba6b-50a67d0dea73 | -15.27773 | -46.40268 | 2025-10-02 04:04:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 3.9 |
| a8c951ee-3ea7-3f9f-ae83-12d9a6153966 | -15.64404 | -46.25115 | 2025-10-02 04:04:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0f6e2adc-c4f7-30fd-a2f6-c05b012446a2 | -14.41473 | -46.08401 | 2025-10-02 04:04:00 | NOAA-21 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 6a715d5b-8569-3975-a6f7-aaafa277f433 | -13.20738 | -47.34024 | 2025-10-02 04:04:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e3067937-1d00-3926-808b-9aebdb2d595b | -15.93364 | -46.24197 | 2025-10-02 04:04:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 4.0 |
| b3381764-2a0f-3cb9-bef6-aa142c96d740 | -13.34426 | -47.32848 | 2025-10-02 04:04:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 8f1746e0-8738-3c60-8f7d-9b0c7798d87c | -13.06795 | -47.01936 | 2025-10-02 04:04:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2c3f2495-a178-301d-b30e-270b6b51756e | -19.89966 | -44.49814 | 2025-10-02 04:04:00 | NOAA-21 | FLORESTAL | MINAS GERAIS | Brasil | 3126000 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 70d47ed0-29f9-3e8a-98c1-358079647037 | -13.95933 | -48.12538 | 2025-10-02 04:04:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 14.1 |
| ca4e2b4f-5938-3796-8463-4fc79e76a6b1 | -19.96902 | -43.71347 | 2025-10-02 04:04:00 | NOAA-21 | CAETÉ | MINAS GERAIS | Brasil | 3110004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.9 |
| 80a64a9e-5f65-31b5-a874-da61c0838070 | -14.80448 | -46.96691 | 2025-10-02 04:04:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d65250ea-46ee-3e52-808b-f35585998a45 | -16.01777 | -50.87289 | 2025-10-02 04:04:00 | NOAA-21 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 23ae879e-184a-3ac1-b446-af63baecb70c | -13.94879 | -48.13398 | 2025-10-02 04:04:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 7.2 |
| ea34aab0-6cd7-364b-be0a-524482c8dca0 | -14.8959 | -47.18161 | 2025-10-02 04:04:00 | NOAA-21 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| aed1af49-197d-3aa1-9e03-dfa164239ff0 | -13.19037 | -47.841 | 2025-10-02 04:04:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a7568960-a41e-3c78-928a-f93385068255 | -18.58811 | -43.04301 | 2025-10-02 04:04:00 | NOAA-21 | SABINÓPOLIS | MINAS GERAIS | Brasil | 3156809 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 2ff95f10-b336-3b59-8aa1-d0ca1997c455 | -14.32246 | -45.96575 | 2025-10-02 04:04:00 | NOAA-21 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0db52396-0a49-316e-97f2-6ac30aead34f | -15.39753 | -44.97807 | 2025-10-02 04:04:00 | NOAA-21 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 3df2d355-d578-39d0-a32e-15780bb8c005 | -13.76677 | -47.98577 | 2025-10-02 04:04:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 05bb1101-f01e-3666-96a3-5bcde61bf14c | -16.36386 | -47.08194 | 2025-10-02 04:04:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1bd47f78-8a59-3a9d-92ca-1ac434aefaea | -18.50682 | -44.03968 | 2025-10-02 04:04:00 | NOAA-21 | MONJOLOS | MINAS GERAIS | Brasil | 3142502 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ce4f7a89-5f9e-3778-abb6-52a189bf208f | -17.11332 | -47.11415 | 2025-10-02 04:04:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 251b9c19-9f2a-3a43-805f-370e09ee98e0 | -14.43836 | -46.36822 | 2025-10-02 04:04:00 | NOAA-21 | BURITINÓPOLIS | GOIÁS | Brasil | 5203962 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 453935ad-e0e2-36bf-9fad-61221123ee40 | -13.3401 | -47.32769 | 2025-10-02 04:04:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| ac148cca-0ff5-330f-92c3-8bc08bb595f1 | -20.48557 | -42.24615 | 2025-10-02 04:04:00 | NOAA-21 | SANTA MARGARIDA | MINAS GERAIS | Brasil | 3157906 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| f873e785-3c25-3ab5-b467-ce7928f83413 | -13.78731 | -47.99558 | 2025-10-02 04:04:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 3199b5c6-adb4-3636-b273-8664c17ba225 | -13.55621 | -47.28942 | 2025-10-02 04:04:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 6.4 |
| bea8eaaf-625f-37e7-ab3e-8ab9ef93f07f | -19.77395 | -46.5785 | 2025-10-02 04:04:00 | NOAA-21 | IBIÁ | MINAS GERAIS | Brasil | 3129509 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 62f30959-f7a6-3d01-bba2-cd566c167c96 | -13.96019 | -48.12066 | 2025-10-02 04:04:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 0a7d4b59-a37d-374e-9b4f-6b376d986c98 | -18.49683 | -43.40296 | 2025-10-02 04:04:00 | NOAA-21 | SERRO | MINAS GERAIS | Brasil | 3167103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| ddcb76fe-39eb-3ca8-a97a-e3c86bf08446 | -14.92116 | -47.23152 | 2025-10-02 04:04:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 502446ed-d0d6-326e-b40e-df60d738724a | -14.29905 | -45.96616 | 2025-10-02 04:04:00 | NOAA-21 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 92fabb78-2128-3c26-899b-f07e4d4c294f | -20.87761 | -44.62417 | 2025-10-02 04:04:00 | NOAA-21 | SÃO TIAGO | MINAS GERAIS | Brasil | 3165008 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 55745304-6791-3cbc-a3bd-bb5c37f4a8bb | -17.98052 | -45.01343 | 2025-10-02 04:04:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 22314b5c-b687-3c40-a816-023618f22b7f | -16.29067 | -45.24183 | 2025-10-02 04:04:00 | NOAA-21 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8fdbfe58-0f30-3020-9a01-6f28499895f9 | -20.18884 | -46.01682 | 2025-10-02 04:04:00 | NOAA-21 | BAMBUÍ | MINAS GERAIS | Brasil | 3105103 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| f077b66f-110a-32a4-9d84-425a49fea9f1 | -18.50532 | -44.02776 | 2025-10-02 04:04:00 | NOAA-21 | MONJOLOS | MINAS GERAIS | Brasil | 3142502 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1309c19c-e406-36a5-9336-71335636697d | -12.76653 | -50.5927 | 2025-10-02 04:04:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 848fad86-fc31-3827-9d1d-a2241efe8343 | -16.04063 | -50.86256 | 2025-10-02 04:04:00 | NOAA-21 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 6.4 |
| d885f954-796f-3ebe-9016-ee778808ada6 | -12.70456 | -48.57172 | 2025-10-02 04:04:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 9.9 |
| baf97afd-6d25-3629-b3ed-000c9ef0699c | -12.41737 | -54.35205 | 2025-10-02 04:04:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 241e5090-b860-36ba-b19a-53a7fd39887a | -12.70083 | -48.56639 | 2025-10-02 04:04:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 65f4469e-90bc-3a5c-8bef-25f8902ad7a7 | -13.66241 | -48.08463 | 2025-10-02 04:04:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| bb12cbbb-e8aa-3776-ba41-cfb9ffa7997e | -13.15812 | -47.8364 | 2025-10-02 04:04:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 999be3a7-3a60-3e14-9697-6b09cf31072d | -19.85173 | -44.0827 | 2025-10-02 04:04:00 | NOAA-21 | CONTAGEM | MINAS GERAIS | Brasil | 3118601 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ec5cab10-c43d-3123-a716-0f31aa694746 | -13.80438 | -47.51246 | 2025-10-02 04:04:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 28b383d6-e2b4-3e71-ad4c-1855adede2a7 | -14.21609 | -44.93725 | 2025-10-02 04:04:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| df7c07a4-8e16-39cd-b27d-9cee51dab609 | -21.0864 | -44.49217 | 2025-10-02 04:04:00 | NOAA-21 | CONCEIÇÃO DA BARRA DE MINAS | MINAS GERAIS | Brasil | 3115201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| d3832b04-0419-3c14-b1a8-3c2d8ac681e2 | -13.40396 | -47.79253 | 2025-10-02 04:04:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| b341f218-44b5-3adf-877b-01f2b0ec4c51 | -14.30386 | -45.89444 | 2025-10-02 04:04:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 11878bbc-e083-3527-82ce-54a75ed8e15e | -13.24434 | -47.32635 | 2025-10-02 04:04:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 9b53715b-ba09-3e09-b7b6-c9805db59642 | -13.15229 | -47.84402 | 2025-10-02 04:04:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 1d681157-c982-33d7-9d97-6fcdb90d6196 | -13.76104 | -47.94365 | 2025-10-02 04:04:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| ae3e6b73-c2fc-3cd2-a2a7-2fc99f2f875e | -13.37488 | -47.28727 | 2025-10-02 04:04:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 5467b5b7-7770-3b66-9a65-5d97e8835af0 | -16.36872 | -47.07744 | 2025-10-02 04:04:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| fc7ece35-98e4-3da0-b229-dfa5f240f68f | -15.99858 | -50.91683 | 2025-10-02 04:04:00 | NOAA-21 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9c17df3b-86eb-3b77-82d5-7f6e75e5ae15 | -19.18353 | -41.93563 | 2025-10-02 04:04:00 | NOAA-21 | TARUMIRIM | MINAS GERAIS | Brasil | 3168408 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| c5047cb5-5c68-37ab-80c7-dc13b9147afc | -17.55159 | -44.48396 | 2025-10-02 04:04:00 | NOAA-21 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6ca42e35-293d-3951-8b55-64aea27dd022 | -13.21861 | -47.34985 | 2025-10-02 04:04:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 366eca79-34e4-3c46-a247-2e7700c4990c | -15.63593 | -46.25098 | 2025-10-02 04:04:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7da02fa1-4007-3a49-b4b5-7db19f5f6eb1 | -15.70164 | -49.93785 | 2025-10-02 04:04:00 | NOAA-21 | ITAPURANGA | GOIÁS | Brasil | 5211206 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 69abd55e-05d2-3cb9-8d2e-363624fea7d0 | -15.94857 | -43.30393 | 2025-10-02 04:04:00 | NOAA-21 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 2aff5781-208d-3d44-a2dc-65665482aac2 | -17.87359 | -42.25823 | 2025-10-02 04:04:00 | NOAA-21 | MALACACHETA | MINAS GERAIS | Brasil | 3139201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 7feff8cb-86cb-3290-9996-7e68da779bd0 | -15.78995 | -43.7356 | 2025-10-02 04:04:00 | NOAA-21 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8080a951-507a-3e36-bc11-44f5bc489ec6 | -19.78531 | -44.30055 | 2025-10-02 04:04:00 | NOAA-21 | ESMERALDAS | MINAS GERAIS | Brasil | 3124104 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e8c6d722-a2e7-3f57-adb7-eea2ed6be451 | -15.18742 | -46.40701 | 2025-10-02 04:04:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 240eeff6-ed29-34f1-bc4d-a2d59ee842ae | -15.60075 | -46.919 | 2025-10-02 04:04:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| adb785eb-8f75-322f-83ae-e4f7160ea207 | -14.59131 | -46.71127 | 2025-10-02 04:04:00 | NOAA-21 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| a7eef2a2-3daa-32b6-b624-2a6c4d454ba2 | -13.74882 | -48.01089 | 2025-10-02 04:04:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 37cfac29-d359-3ed9-a8f5-e3ba9fba83f3 | -15.26421 | -49.31629 | 2025-10-02 04:04:00 | NOAA-21 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 5.9 |
| eb6e6e33-c77f-3143-bb89-1068b60c84fc | -18.34704 | -44.50662 | 2025-10-02 04:04:00 | NOAA-21 | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 18.2 |
| 90481080-e2c0-3914-acb1-d40102ee6e6c | -16.55226 | -42.48587 | 2025-10-02 04:04:00 | NOAA-21 | JOSENÓPOLIS | MINAS GERAIS | Brasil | 3136579 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 979b3278-94dd-3ba3-ba83-6b65fe314dca | -21.11803 | -43.76586 | 2025-10-02 04:04:00 | NOAA-21 | ALFREDO VASCONCELOS | MINAS GERAIS | Brasil | 3101631 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 6f5b732e-8955-37d2-8250-45b502a6c48e | -13.75516 | -47.95149 | 2025-10-02 04:04:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c714ee26-517e-35e0-a20f-b731dc5b3ef7 | -14.31202 | -46.00334 | 2025-10-02 04:04:00 | NOAA-21 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 6.5 |
| da42cccb-55b1-37a8-92a2-3d3bb543a667 | -14.18388 | -46.66292 | 2025-10-02 04:04:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| a24ad8bb-de15-3b1c-be32-6940155ea147 | -13.29676 | -47.2112 | 2025-10-02 04:04:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 86165c7d-97d2-30ff-b403-145cbd4cd164 | -18.4419 | -42.40921 | 2025-10-02 04:04:00 | NOAA-21 | PEÇANHA | MINAS GERAIS | Brasil | 3148608 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 4826bbec-addd-3899-b44d-3d77a170c4dd | -13.78174 | -48.05896 | 2025-10-02 04:04:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 944c779f-1722-3c8c-a63d-1193ec292473 | -15.99824 | -50.86639 | 2025-10-02 04:04:00 | NOAA-21 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 6.1 |
| c63b20c3-063f-30ef-8f10-095d7150dcdb | -19.85951 | -42.58746 | 2025-10-02 04:04:00 | NOAA-21 | DIONÍSIO | MINAS GERAIS | Brasil | 3121803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 329e4e39-4bc6-31f6-b66f-697380903b08 | -19.88757 | -42.62612 | 2025-10-02 04:04:00 | NOAA-21 | DIONÍSIO | MINAS GERAIS | Brasil | 3121803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| c3039dee-2573-3dc6-84f6-e519f7bb3e08 | -13.34221 | -47.34001 | 2025-10-02 04:04:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 1b97cf32-5dde-3b52-82e4-f49fc77df25b | -13.31414 | -46.99902 | 2025-10-02 04:04:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |


[Clique aqui para ver as próximas entradas](README40.md)
