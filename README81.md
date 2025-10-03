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

## Dados Diários - Página 81

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 25e7a739-503e-3725-b6e2-2494f52c4f18 | -18.66574 | -46.5821 | 2025-10-03 04:14:00 | NPP-375D | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 71e00155-d99d-3ec6-9a72-31e490f49a2a | -19.81925 | -46.91872 | 2025-10-03 04:14:00 | NPP-375D | TAPIRA | MINAS GERAIS | Brasil | 3168101 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 868e6d87-5aa5-3a25-8972-0d4fcc79882c | -21.59432 | -45.27799 | 2025-10-03 04:14:00 | NPP-375D | VARGINHA | MINAS GERAIS | Brasil | 3170701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 2cfc9aac-fca1-3ce3-8411-dace847f2b55 | -15.35517 | -46.26566 | 2025-10-03 04:14:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f6f4e651-105b-348a-97c9-5ea88b224bec | -14.9057 | -48.29259 | 2025-10-03 04:14:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 3a5138f5-0d05-31ea-bc87-846f9f20cad3 | -19.51109 | -41.96524 | 2025-10-03 04:14:00 | NPP-375D | SÃO SEBASTIÃO DO ANTA | MINAS GERAIS | Brasil | 3164472 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 6e098f8f-5632-338b-b7fd-430d5cb65788 | -15.76532 | -43.66734 | 2025-10-03 04:14:00 | NPP-375D | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 87eb104b-76bd-31f6-b748-599351bd78e1 | -15.75827 | -47.77329 | 2025-10-03 04:14:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 908ceb30-0504-3e8c-a5da-137eb2c88e4f | -19.45853 | -43.64961 | 2025-10-03 04:14:00 | NPP-375D | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c5046039-8389-384f-96a9-85fd275a3470 | -20.42044 | -48.86272 | 2025-10-03 04:14:00 | NPP-375D | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5f1a0f90-73cd-3556-89ed-5e1c43d69565 | -17.91417 | -43.93642 | 2025-10-03 04:14:00 | NPP-375D | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ef3593fb-27a6-3010-86cd-c4a175314417 | -16.26805 | -47.09694 | 2025-10-03 04:14:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bf941bf0-bce4-3924-b8e2-5d9bc8e8f9bc | -14.74514 | -48.10716 | 2025-10-03 04:14:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.3 |
| b669f5af-fbe9-3f48-8de4-e172bf4e3708 | -15.58599 | -46.91024 | 2025-10-03 04:14:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5a9c9b71-2a06-303e-9124-5b06d5784ed6 | -15.31314 | -46.38505 | 2025-10-03 04:14:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| ade2c006-2a93-342f-b3e4-cbcf0d1f5b30 | -19.45733 | -44.29051 | 2025-10-03 04:14:00 | NPP-375D | SETE LAGOAS | MINAS GERAIS | Brasil | 3167202 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ca47c168-eb41-342f-be27-1125a06681ca | -16.68452 | -53.02209 | 2025-10-03 04:14:00 | NPP-375D | PONTE BRANCA | MATO GROSSO | Brasil | 5106703 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| a0c31423-be75-3c3b-82c0-5a624cf49eba | -14.7296 | -48.10867 | 2025-10-03 04:14:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0214d365-e0ae-3b9b-a0f8-f4cef16ae599 | -17.48858 | -43.47321 | 2025-10-03 04:14:00 | NPP-375D | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 1dbcf086-02c0-3ed4-bdab-46de2b1adad2 | -16.06884 | -51.00463 | 2025-10-03 04:14:00 | NPP-375D | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| abb05fe0-e131-3f2d-acc2-f2435a5a7a96 | -21.58648 | -45.28423 | 2025-10-03 04:14:00 | NPP-375D | VARGINHA | MINAS GERAIS | Brasil | 3170701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| a1c2cf7f-aeef-3032-a77e-47de8abc073f | -15.51908 | -46.80149 | 2025-10-03 04:14:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| fdb68119-5d86-31ca-bbf5-879a18d484bf | -14.73575 | -48.11961 | 2025-10-03 04:14:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4d42f24e-a0ac-3c12-a706-b1878affb61a | -15.34446 | -47.83455 | 2025-10-03 04:14:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a22f4594-2a78-3654-a5ca-d58e436348b0 | -21.33897 | -44.33131 | 2025-10-03 04:14:00 | NPP-375D | SÃO JOÃO DEL REI | MINAS GERAIS | Brasil | 3162500 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 868e23bc-5171-37fa-b5c0-3029be8997e4 | -14.7037 | -48.20152 | 2025-10-03 04:14:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 40dde4ec-a443-3948-9374-84f6b3295e38 | -15.33679 | -47.33036 | 2025-10-03 04:14:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 36fed4de-5e98-3e9f-ad5f-c9314c95fffc | -20.99638 | -49.21553 | 2025-10-03 04:14:00 | NPP-375D | IBIRÁ | SÃO PAULO | Brasil | 3519402 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| 4abb3c41-fb91-38d5-9e17-4dd74cdfa163 | -16.04316 | -50.91919 | 2025-10-03 04:14:00 | NPP-375D | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 140c48ee-b4cc-345f-8557-8e680b0498c1 | -19.60079 | -45.90218 | 2025-10-03 04:14:00 | NPP-375D | ESTRELA DO INDAIÁ | MINAS GERAIS | Brasil | 3124708 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a30c27a1-acd7-3dad-84dd-b1cbacfe74e6 | -19.63552 | -43.92683 | 2025-10-03 04:14:00 | NPP-375D | LAGOA SANTA | MINAS GERAIS | Brasil | 3137601 | 31 | 33 | nan | nan | nan | Cerrado | 0.3 |
| d60a8d70-9fcc-33d6-accd-e4439c87a267 | -15.91786 | -43.34214 | 2025-10-03 04:14:00 | NPP-375D | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 22.4 |
| 4177c6f6-ca37-3add-980e-f62862e2207d | -15.23804 | -50.08331 | 2025-10-03 04:14:00 | NPP-375D | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| d7d9189f-64c2-3083-a6c2-d30edc8151b5 | -14.95077 | -47.52218 | 2025-10-03 04:14:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 91959d81-f2e3-34db-9883-9443dbd84920 | -15.48771 | -45.93045 | 2025-10-03 04:14:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 680bbf23-d7fc-32bb-a9ff-b4a8912ac92b | -15.29953 | -46.29369 | 2025-10-03 04:14:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e0f45a52-3bd0-3045-966e-a7a3617f58b5 | -19.28985 | -43.73232 | 2025-10-03 04:14:00 | NPP-375D | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a29dd41d-21f8-37a9-95d3-6b3026545d7a | -14.7363 | -48.09325 | 2025-10-03 04:14:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| a75ea65b-413c-30c4-a5a5-8713f72eaec0 | -16.08788 | -51.05431 | 2025-10-03 04:14:00 | NPP-375D | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3f4db98f-a007-3118-ad6f-a44556b0934b | -16.03592 | -50.93238 | 2025-10-03 04:14:00 | NPP-375D | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 8.9 |
| a70ed417-1e6c-3c66-be6c-b82490a9914f | -15.25158 | -50.12679 | 2025-10-03 04:14:00 | NPP-375D | FAINA | GOIÁS | Brasil | 5207535 | 52 | 33 | nan | nan | nan | Cerrado | 5.4 |
| f6a0fe6d-b974-39ac-9b5d-b3460ca599f2 | -21.34299 | -45.00103 | 2025-10-03 04:14:00 | NPP-375D | INGAÍ | MINAS GERAIS | Brasil | 3130804 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| da37ab9b-7ed5-339a-a8ec-889ac4ff252d | -18.15648 | -53.34529 | 2025-10-03 04:14:00 | NPP-375D | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8d689875-fcb9-3516-8b7d-a00ed277c231 | -14.93716 | -46.90446 | 2025-10-03 04:14:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 11.1 |
| c6edeceb-f942-3789-ac24-a5530fc7fddf | -16.93166 | -54.14595 | 2025-10-03 04:14:00 | NPP-375D | PEDRA PRETA | MATO GROSSO | Brasil | 5106372 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ab258b3d-c574-3719-a738-295fa406a63d | -14.73617 | -48.08988 | 2025-10-03 04:14:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6a706eb8-5298-3c61-bb79-1ab274e6f605 | -15.66547 | -43.26701 | 2025-10-03 04:14:00 | NPP-375D | NOVA PORTEIRINHA | MINAS GERAIS | Brasil | 3145059 | 31 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 9cee314c-0c3a-37a9-91ef-0a95bd7c58fa | -19.823 | -46.83306 | 2025-10-03 04:14:00 | NPP-375D | TAPIRA | MINAS GERAIS | Brasil | 3168101 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| bc950492-2633-3732-ae6c-aa181d4f4db8 | -16.27095 | -47.1018 | 2025-10-03 04:14:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 052bee10-e476-3f01-baf9-1a829e2b88ad | -21.83447 | -45.85091 | 2025-10-03 04:14:00 | NPP-375D | TURVOLÂNDIA | MINAS GERAIS | Brasil | 3169802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 9642ea85-5996-3882-b0ed-1c49b39233dc | -20.004 | -44.18613 | 2025-10-03 04:14:00 | NPP-375D | BETIM | MINAS GERAIS | Brasil | 3106705 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.1 |
| 67e220ea-b2ac-3657-9758-961eb490d80f | -18.16097 | -53.34956 | 2025-10-03 04:14:00 | NPP-375D | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 3.7 |
| a83c81b0-820c-3926-b226-5ab87a263d4f | -14.93199 | -46.89077 | 2025-10-03 04:14:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 785358a3-d6e3-32b9-ba7e-ac5b5a0adc9a | -16.35061 | -47.09659 | 2025-10-03 04:14:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4d45bfb8-c017-3e0c-b623-cb8fcd1e8d65 | -20.11479 | -44.39074 | 2025-10-03 04:14:00 | NPP-375D | MATEUS LEME | MINAS GERAIS | Brasil | 3140704 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 95c2c822-24b1-3461-be5a-6ee5e968a96f | -19.97529 | -43.71563 | 2025-10-03 04:14:00 | NPP-375D | CAETÉ | MINAS GERAIS | Brasil | 3110004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| f3d784e3-87b3-3804-9330-06d98d4845ee | -19.45962 | -44.27582 | 2025-10-03 04:14:00 | NPP-375D | SETE LAGOAS | MINAS GERAIS | Brasil | 3167202 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 8858a60d-8e2f-3c5d-a55b-a737bb2b6d12 | -15.34687 | -47.06424 | 2025-10-03 04:14:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 88293503-d168-35d6-96d5-f6873a1c6e17 | -17.07815 | -44.91438 | 2025-10-03 04:14:00 | NPP-375D | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 37bfdb41-0910-3aa4-abd1-33b949342d3e | -15.52195 | -46.80633 | 2025-10-03 04:14:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c5a7b2aa-63e1-3e5a-98f9-0bdd24eadb91 | -14.9373 | -46.89828 | 2025-10-03 04:14:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 1168e8a0-f226-3a9a-ab5b-f8c1c4a2bd87 | -14.72743 | -48.09357 | 2025-10-03 04:14:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e2696563-3aef-3b9a-bd43-a939b3ab71dc | -15.9451 | -43.34299 | 2025-10-03 04:14:00 | NPP-375D | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c245638a-cbd2-35cd-a5d4-f8e8578f04b8 | -15.21355 | -47.18704 | 2025-10-03 04:14:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9ff14a83-28f8-3cdf-acbf-179ed76f0c83 | -15.94917 | -46.21387 | 2025-10-03 04:14:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| b4cdd9d4-a079-3cdd-b699-24a40395d925 | -17.78762 | -45.00272 | 2025-10-03 04:14:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 897d2f47-077b-3f11-a650-a5412a7777b0 | -14.93792 | -46.91618 | 2025-10-03 04:14:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 74aa653f-77c8-35a5-9c42-1d837f25fa05 | -14.74216 | -48.10134 | 2025-10-03 04:14:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1310a8a8-74d0-3b64-b87c-3a10f45bbae5 | -15.30181 | -46.3872 | 2025-10-03 04:14:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fd3aea9e-6171-376c-a94c-14d7ee2afe1a | -15.29016 | -47.96051 | 2025-10-03 04:14:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 337b050d-6d24-3b8c-8f36-3604196e67e7 | -16.63083 | -49.41169 | 2025-10-03 04:14:00 | NPP-375D | TRINDADE | GOIÁS | Brasil | 5221403 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4a2d8733-f01f-32ab-98bb-f867209b42c7 | -15.76203 | -47.77402 | 2025-10-03 04:14:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e2884347-0332-32ed-9e5d-c835e20a5e56 | -15.91341 | -43.34878 | 2025-10-03 04:14:00 | NPP-375D | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 4.0 |
| fb1b1fd3-6bdc-3d7c-be5e-ec6423730bff | -14.89861 | -46.84458 | 2025-10-03 04:14:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 7eb93861-c1d7-37e1-8d6d-4c72cf80eb02 | -21.17004 | -45.24519 | 2025-10-03 04:14:00 | NPP-375D | NEPOMUCENO | MINAS GERAIS | Brasil | 3144607 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 3ea8e285-c62f-3a2c-9566-73aa8c5819d2 | -14.74723 | -48.11793 | 2025-10-03 04:14:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 5e7acaf6-4bb4-370d-9649-b0cdb17c7ee1 | -19.8921 | -44.18966 | 2025-10-03 04:14:00 | NPP-375D | BETIM | MINAS GERAIS | Brasil | 3106705 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 1b9d47e3-d663-3334-95c9-8f30e1affcfc | -14.93345 | -46.90423 | 2025-10-03 04:14:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 2e1c297f-b0b6-34a4-b48b-19bb1dc96526 | -19.45905 | -44.27951 | 2025-10-03 04:14:00 | NPP-375D | SETE LAGOAS | MINAS GERAIS | Brasil | 3167202 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| aff88f69-3420-33dc-a7b2-846e704ed885 | -19.842 | -44.07911 | 2025-10-03 04:14:00 | NPP-375D | RIBEIRÃO DAS NEVES | MINAS GERAIS | Brasil | 3154606 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a52a669c-f856-35a0-9f57-585fd828670b | -20.1293 | -44.00929 | 2025-10-03 04:14:00 | NPP-375D | BRUMADINHO | MINAS GERAIS | Brasil | 3109006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| e1f3bb12-d6c6-3dd3-81cf-a0e2941936b6 | -19.14416 | -41.49918 | 2025-10-03 04:14:00 | NPP-375D | CONSELHEIRO PENA | MINAS GERAIS | Brasil | 3118403 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 21ea6873-0893-310b-b70f-34b33366b739 | -15.58473 | -46.91724 | 2025-10-03 04:14:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0a22c014-44a3-3050-b831-02b565a5e20f | -15.22168 | -47.63459 | 2025-10-03 04:14:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 37b8e3cc-8684-3b3e-9da8-1023869641b6 | -15.24893 | -50.11673 | 2025-10-03 04:14:00 | NPP-375D | FAINA | GOIÁS | Brasil | 5207535 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| cfbbcc23-5181-3fc9-a3ce-ea525238944c | -17.96356 | -45.04079 | 2025-10-03 04:14:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9af81933-527a-3fdf-9f81-ec206939b4ba | -14.87466 | -48.32993 | 2025-10-03 04:14:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b423f6ab-09cb-314e-82ac-8125d2ce3978 | -16.07339 | -51.00576 | 2025-10-03 04:14:00 | NPP-375D | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 594edf96-0554-394f-9ca1-223a7929e3fa | -21.34574 | -45.00534 | 2025-10-03 04:14:00 | NPP-375D | INGAÍ | MINAS GERAIS | Brasil | 3130804 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| aa286286-56ad-3857-99eb-8370ca5e975b | -15.74853 | -43.70876 | 2025-10-03 04:14:00 | NPP-375D | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 224735e1-8d54-3b3a-a966-dc1eda7c5555 | -15.71354 | -46.25991 | 2025-10-03 04:14:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4e8f7dbe-f033-3042-865e-cafef6d0b47a | -14.68286 | -48.09908 | 2025-10-03 04:14:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 0cd37ef1-f40a-3679-a64d-750bcbd49245 | -14.68559 | -48.08371 | 2025-10-03 04:14:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a30a27ac-5416-3645-9921-ca6acb70d644 | -20.38354 | -44.12785 | 2025-10-03 04:14:00 | NPP-375D | BELO VALE | MINAS GERAIS | Brasil | 3106408 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.9 |
| c2d06f5b-c909-33e0-9c20-9d67af40e333 | -19.64823 | -46.80569 | 2025-10-03 04:14:00 | NPP-375D | ARAXÁ | MINAS GERAIS | Brasil | 3104007 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8fd18e47-fc5d-3280-9082-9b293dfd01db | -14.66538 | -48.26603 | 2025-10-03 04:14:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 46288340-b6d9-3b68-ab1c-eeaf7af3feb7 | -14.68772 | -48.09443 | 2025-10-03 04:14:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1158fe7a-27e7-3e90-8de3-8df56aca35c9 | -14.63773 | -48.26097 | 2025-10-03 04:14:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a74e6e23-1273-3a8f-9885-e1346475dfd5 | -15.57508 | -46.95235 | 2025-10-03 04:14:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0df263ef-8012-3f3e-80f9-df5626831adf | -14.73451 | -48.12127 | 2025-10-03 04:14:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |


[Clique aqui para ver as próximas entradas](README82.md)
