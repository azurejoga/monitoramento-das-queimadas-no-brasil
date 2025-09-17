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

## Dados Diários - Página 28

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2b39d8d6-6f54-30d8-95a6-3281d4a2fb37 | -16.61566 | -43.37037 | 2025-09-17 04:12:00 | NPP-375D | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5e5bbb0f-e4c8-3526-8300-e55ba6cc79f1 | -12.98919 | -47.943 | 2025-09-17 04:12:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3acb335b-ef29-39ae-bef3-f3d90aac6f1e | -12.84868 | -47.19619 | 2025-09-17 04:12:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 90ad643b-8362-30e6-943a-7f58d1ea50ff | -15.39775 | -46.14524 | 2025-09-17 04:12:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b00bd46c-d9e2-3417-93a9-be07a3f1e60c | -15.01694 | -49.45982 | 2025-09-17 04:12:00 | NPP-375D | NOVA GLÓRIA | GOIÁS | Brasil | 5214861 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 93fc71bf-3afc-38bb-a7d1-5a380d5522fe | -13.85881 | -44.88785 | 2025-09-17 04:12:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a9c6dc3e-cf97-3f9e-b4fb-4120b93d2d4e | -14.61552 | -46.37175 | 2025-09-17 04:12:00 | NPP-375D | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 933784fe-10d6-3172-9c88-a48e3432f80f | -13.20854 | -46.77763 | 2025-09-17 04:12:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9ddae652-77f9-3ce3-a746-9efbbfd904cd | -15.43638 | -47.32426 | 2025-09-17 04:12:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 25b0bca9-35cd-3091-a4cf-aaeb12bb4141 | -14.60479 | -46.39164 | 2025-09-17 04:12:00 | NPP-375D | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 49cab55a-1b7f-32b0-b376-4c79997a8566 | -10.89965 | -45.4395 | 2025-09-17 04:12:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 249d9b4e-0825-3e88-9c20-7a7a3bb87c7b | -16.42385 | -45.67107 | 2025-09-17 04:12:00 | NPP-375D | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4800d374-e128-3981-aca1-228d0ba2d247 | -11.04109 | -42.24809 | 2025-09-17 04:12:00 | NPP-375D | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| e06461fd-2c20-3196-8114-cbdbf080cbab | -12.71544 | -47.98314 | 2025-09-17 04:12:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b787b3d1-8b00-37ec-b5ad-5399f0453377 | -14.98827 | -42.23782 | 2025-09-17 04:12:00 | NPP-375D | MORTUGABA | BAHIA | Brasil | 2921807 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 64da76c9-2d59-3299-8eea-5155c3629bd1 | -14.90558 | -51.69571 | 2025-09-17 04:12:00 | NPP-375D | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a793fa5c-73f2-311b-a764-0329bba4125d | -11.1776 | -50.65397 | 2025-09-17 04:12:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| dc5c692a-5de1-3d8a-9f0a-03d07768c922 | -11.59743 | -49.8167 | 2025-09-17 04:12:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a84c77ca-190a-30ba-a9f9-7e4d0cdde548 | -12.86723 | -47.14697 | 2025-09-17 04:12:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 84057ba9-bc39-3295-8b8a-f03ae933eb11 | -12.84755 | -47.1932 | 2025-09-17 04:12:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e98f4743-7e05-328c-b5e3-2fd154c74a88 | -14.15524 | -46.13962 | 2025-09-17 04:12:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f103464d-b422-3a45-b43a-65f3f22e6516 | -12.86282 | -47.13872 | 2025-09-17 04:12:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| b57e98e1-ebd6-3502-b817-ec4071ab1142 | -11.47062 | -43.56805 | 2025-09-17 04:12:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 69be4af7-d324-3b5e-a390-ef67982b06c5 | -12.69526 | -45.80167 | 2025-09-17 04:12:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 82c69855-0f26-38ab-b9cb-dbe10eb4e4ff | -15.54915 | -46.71028 | 2025-09-17 04:12:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 62507a39-d452-324d-8700-b77a317b3ea1 | -14.8582 | -45.12163 | 2025-09-17 04:12:00 | NPP-375D | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 932d54bf-75b5-3609-99cb-d2368d506285 | -14.87268 | -50.24052 | 2025-09-17 04:12:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 449bb7d2-884b-380b-9e15-6677b0f32a96 | -12.66217 | -48.00303 | 2025-09-17 04:12:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ea8ffa89-c8b5-37fb-b79c-7debca77aeaf | -13.0323 | -47.95517 | 2025-09-17 04:12:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6576557a-5457-3262-8249-0c33341d68c0 | -13.95418 | -44.92302 | 2025-09-17 04:12:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2ba14dfd-2334-311f-953e-f954591eb2cc | -15.18911 | -47.36782 | 2025-09-17 04:12:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 187491a5-3ce7-3675-b196-d2045e5ad60c | -12.71142 | -47.98242 | 2025-09-17 04:12:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 58d9bdb1-8fce-3f72-a30c-d6b9c51f06b8 | -14.20669 | -47.00858 | 2025-09-17 04:12:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d580acc4-7d94-3895-bbc0-49a61c3ce347 | -10.3041 | -46.63977 | 2025-09-17 04:12:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| fbac69af-81af-3e92-b566-22f23dbf2664 | -12.70748 | -47.76944 | 2025-09-17 04:12:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 35ef8596-1878-37f9-a8f1-57050ab79f98 | -14.56121 | -47.37013 | 2025-09-17 04:12:00 | NPP-375D | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| e662a5c7-4157-3f4f-86aa-583c3f3bea61 | -12.72799 | -48.03018 | 2025-09-17 04:12:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f6240986-3058-397c-9560-f445593bb5c8 | -16.58876 | -42.91435 | 2025-09-17 04:12:00 | NPP-375D | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 42e0bc2a-2b89-3340-a8b1-d7b937360aef | -13.36923 | -43.77443 | 2025-09-17 04:12:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c044c0aa-2698-3b54-97f9-3cfb874f5774 | -15.42002 | -46.13998 | 2025-09-17 04:12:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 6c342f60-6d17-34f0-9a06-d93ef4ac6494 | -10.80173 | -50.71238 | 2025-09-17 04:12:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 1f0f7604-c427-3a45-bccb-7e007bf3cd0d | -12.94365 | -47.96718 | 2025-09-17 04:12:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 315fa463-9539-31b3-b5da-2cdb1473a154 | -15.93132 | -42.63594 | 2025-09-17 04:12:00 | NPP-375D | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.5 |
| 65de6067-4049-39d1-984e-37e40053e627 | -12.96231 | -47.95515 | 2025-09-17 04:12:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 22db4f08-8562-3189-96eb-4be0983103a4 | -13.18052 | -44.48386 | 2025-09-17 04:12:00 | NPP-375D | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2bc479d1-1a51-3bd3-899f-6658a3cc21da | -12.69789 | -47.96501 | 2025-09-17 04:12:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 0d3d3665-5e77-3aed-862a-c3b0968d7ee5 | -13.22655 | -47.30119 | 2025-09-17 04:12:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b189b43f-f1d9-3a77-a9fa-4861afd81f8a | -13.83658 | -42.44366 | 2025-09-17 04:12:00 | NPP-375D | CAETITÉ | BAHIA | Brasil | 2905206 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| a3f1aef1-cb36-345a-9add-d65de7be525b | -12.09957 | -44.83175 | 2025-09-17 04:12:00 | NPP-375D | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 663bf4ff-4a29-33cb-8646-398a8b528ef7 | -12.94304 | -47.96594 | 2025-09-17 04:12:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 50101afb-c41c-3e57-a8e0-c3795014fdb1 | -12.11029 | -44.8098 | 2025-09-17 04:12:00 | NPP-375D | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 12eca6c0-340e-3a30-9af4-4477118c5a7b | -12.72106 | -47.99938 | 2025-09-17 04:12:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a0294fcd-6b02-301e-afc5-171cc84706c8 | -14.83867 | -48.3507 | 2025-09-17 04:12:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6f65e950-ea21-3b74-9512-a7d5c691319c | -14.70341 | -50.24233 | 2025-09-17 04:12:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 91cc1ed1-e214-31ff-bfa9-8f6c826d0156 | -13.22073 | -47.28933 | 2025-09-17 04:12:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 783fdb17-7701-361c-9605-0322c15c9d35 | -12.7259 | -48.01865 | 2025-09-17 04:12:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6df09830-5e1a-31d0-a7dc-f680c321f18e | -14.60336 | -46.37826 | 2025-09-17 04:12:00 | NPP-375D | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 27dacd64-44d9-31a9-80d2-259caed64030 | -11.77465 | -44.74384 | 2025-09-17 04:12:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1a0ec824-b4f1-39e7-8473-9c34a68c0d38 | -12.70125 | -47.96949 | 2025-09-17 04:12:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c42c6649-edd8-3bca-9895-ed5375ca2cc4 | -11.45894 | -43.55511 | 2025-09-17 04:12:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 59bd0144-fb63-321e-8746-38b4eee89acd | -10.80273 | -50.70572 | 2025-09-17 04:12:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3c4ad14b-a33f-3243-9c82-1b0114c4d9ac | -15.42498 | -46.15324 | 2025-09-17 04:12:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 4.9 |
| b0f12c81-372a-312c-a79f-38e37a54ac08 | -15.41751 | -46.15685 | 2025-09-17 04:12:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 78c03415-1a6f-3a01-8ee6-5003806434f1 | -10.80711 | -50.65361 | 2025-09-17 04:12:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 7.5 |
| eb6f1c1f-7db0-3a93-a859-43f583201284 | -13.32738 | -43.09914 | 2025-09-17 04:12:00 | NPP-375D | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| cdc863a2-e6a6-381b-9f78-52935eaadbba | -15.55274 | -46.71098 | 2025-09-17 04:12:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 45113669-5f21-3675-ab82-3a276cc5fb9d | -12.10583 | -44.83671 | 2025-09-17 04:12:00 | NPP-375D | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5e7b8ccd-786b-33f1-9ec0-424ce1e9720f | -14.86143 | -50.05477 | 2025-09-17 04:12:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9e2b4731-8e4b-3e0f-bb9c-c04f8d617886 | -14.68533 | -42.21334 | 2025-09-17 04:12:00 | NPP-375D | JACARACI | BAHIA | Brasil | 2917409 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 0f6a49d4-229a-34fe-93e9-606b30d58c6d | -16.94187 | -42.86898 | 2025-09-17 04:12:00 | NPP-375D | BOTUMIRIM | MINAS GERAIS | Brasil | 3108503 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6ceb2915-c1fe-3e85-bd46-e89ed54ccd9f | -14.62093 | -46.39281 | 2025-09-17 04:12:00 | NPP-375D | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| fed68a3f-defc-33a3-b3b3-70efbdee5d11 | -12.97134 | -47.95074 | 2025-09-17 04:12:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 024f7c55-597f-3bb4-a89e-1fe286be43bb | -12.42666 | -40.92894 | 2025-09-17 04:12:00 | NPP-375D | LAJEDINHO | BAHIA | Brasil | 2919009 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 79ff291c-108e-3db4-b67f-d57a993f269f | -10.77583 | -50.71231 | 2025-09-17 04:12:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 19cb349e-8c25-30cf-b36a-6d65e95d2de1 | -12.99724 | -47.944 | 2025-09-17 04:12:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| cfcdde3a-87af-3bc1-ab30-40b61dd3600b | -16.6151 | -43.37399 | 2025-09-17 04:12:00 | NPP-375D | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| fd24d6a6-919b-3820-877f-806de926f172 | -10.90253 | -45.44418 | 2025-09-17 04:12:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0115f8c8-e4a4-340e-bfff-58707630fc1e | -12.24905 | -46.75714 | 2025-09-17 04:12:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 171445ff-9749-3e40-9d5c-4d40e0de4eef | -11.49388 | -43.61605 | 2025-09-17 04:12:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ba790787-0e47-3af8-84e3-1e1e099f0973 | -12.6917 | -47.95311 | 2025-09-17 04:12:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 268beca4-c55b-3ea1-b1b6-e87838d2382c | -15.42306 | -46.14535 | 2025-09-17 04:12:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 924c3ffe-32f5-3121-954c-1a56086e42aa | -15.77045 | -43.86543 | 2025-09-17 04:12:00 | NPP-375D | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 675d7b6a-440b-3c31-a46f-4b9678167504 | -14.63107 | -42.92082 | 2025-09-17 04:12:00 | NPP-375D | SEBASTIÃO LARANJEIRAS | BAHIA | Brasil | 2930006 | 29 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 70a738bc-9f2f-3463-8b8a-add2def051ba | -12.94873 | -47.95693 | 2025-09-17 04:12:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5faec1e7-296f-3d69-9755-f0c01fdf947b | -15.98987 | -46.44683 | 2025-09-17 04:12:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 25525881-1522-37d9-b3c1-ca8b7d145051 | -12.10149 | -44.82019 | 2025-09-17 04:12:00 | NPP-375D | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7926101c-10d2-31a4-87f1-8e50aaea5ce6 | -11.45952 | -43.55154 | 2025-09-17 04:12:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8bb0dc49-221e-3262-a2a7-b1a6bb9cbf11 | -12.09675 | -44.82735 | 2025-09-17 04:12:00 | NPP-375D | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d9409ab8-c08b-3265-ab19-011756e3ceb4 | -12.71497 | -47.98718 | 2025-09-17 04:12:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1d5ac143-3d2a-3c85-acfe-0dc1a24106cd | -15.41725 | -46.15609 | 2025-09-17 04:12:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| a9a0ea2a-9344-31d8-abab-0fb4c26b054f | -14.90448 | -51.70138 | 2025-09-17 04:12:00 | NPP-375D | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| da7c04f7-a1cd-37b8-ac2a-1338dd17812a | -14.83227 | -51.7019 | 2025-09-17 04:12:00 | NPP-375D | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| c80a7288-adf5-3042-b505-fa8bf3bffbe9 | -14.62453 | -46.39334 | 2025-09-17 04:12:00 | NPP-375D | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| aa09ee1e-6351-3f32-b53c-d614a754305e | -12.71432 | -47.99075 | 2025-09-17 04:12:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| dd1b7aa3-e344-36f0-bca7-bf608550508f | -12.69743 | -45.81052 | 2025-09-17 04:12:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 2d14fbf5-ad82-3629-af2a-f3b23d6d3154 | -14.83062 | -46.71386 | 2025-09-17 04:12:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 20274891-95be-39eb-ad1c-da7fa0621d42 | -12.70963 | -44.67237 | 2025-09-17 04:12:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a5bba188-dadd-332e-8b5e-cf3e1c1be3a5 | -12.70896 | -47.94902 | 2025-09-17 04:12:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 5c95cf44-4620-3c8c-83f4-138ae06a02ec | -12.86363 | -47.13418 | 2025-09-17 04:12:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d414d7ef-9795-3661-8907-997ebfd33d7f | -12.06109 | -46.54425 | 2025-09-17 04:12:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |


[Clique aqui para ver as próximas entradas](README29.md)
