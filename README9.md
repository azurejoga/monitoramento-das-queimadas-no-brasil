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

## Dados Diários - Página 9

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ecc311f2-a170-30e5-9abd-245450cbef84 | -4.78576 | -45.32684 | 2025-08-18 03:32:00 | NPP-375D | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 29bd2232-79a9-3f2f-8bb0-dc3b9ff954e8 | -11.80525 | -44.93797 | 2025-08-18 03:32:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 46400e09-c851-33dc-9f8b-2693233af16c | -10.99714 | -45.65011 | 2025-08-18 03:32:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 876ef5ba-78fc-3e9a-a129-1ad01a77d02a | -6.56665 | -44.47698 | 2025-08-18 03:32:00 | NPP-375D | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 10.0 |
| dd776950-8594-333a-be35-0e7e84be7b6a | -8.49653 | -44.73802 | 2025-08-18 03:32:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6597ced8-adec-3f76-a219-9da5d346ac5d | -5.67201 | -43.38593 | 2025-08-18 03:32:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| eb3c5650-8989-3594-a1cb-f79eae4f7afe | -7.20158 | -43.96886 | 2025-08-18 03:32:00 | NPP-375D | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e898caa4-b1b1-3e68-93f7-66a8291b6bb0 | -6.56297 | -44.47456 | 2025-08-18 03:32:00 | NPP-375D | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 86f1d58f-0b96-3037-82c2-eeab98f97bed | -4.77665 | -45.32327 | 2025-08-18 03:32:00 | NPP-375D | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 428778da-a46b-351e-bab9-0495b5f31b05 | -9.86946 | -44.69236 | 2025-08-18 03:32:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 84d66681-312f-32c3-bb04-738b6fd296b5 | -10.99599 | -45.65586 | 2025-08-18 03:32:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| eda1176f-feb9-3802-897e-90ea8697a835 | -6.55257 | -44.47904 | 2025-08-18 03:32:00 | NPP-375D | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 1ee9980d-2916-35cd-901c-a6c181f817af | -7.50779 | -44.98795 | 2025-08-18 03:32:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 945a0783-dc8d-3cd2-8503-f766cfc21def | -6.5488 | -44.4773 | 2025-08-18 03:32:00 | NPP-375D | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 52a9184d-4798-3b0b-8cc0-70007bee9378 | -10.99999 | -45.65769 | 2025-08-18 03:32:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8dfa5fb4-49a6-344c-a3de-f393669e9e0c | -17.39222 | -42.61723 | 2025-08-18 03:34:00 | NPP-375D | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 23.0 |
| 333d6d11-6ff8-3d36-8cd6-ebcb9c553c9a | -12.63628 | -46.90139 | 2025-08-18 03:34:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1cf4021e-c302-38db-890a-b34f45dfb7cb | -18.54244 | -43.99494 | 2025-08-18 03:34:00 | NPP-375D | GOUVEIA | MINAS GERAIS | Brasil | 3127602 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b4b32128-aed1-39c3-9e8c-8115a7978728 | -19.43917 | -43.72823 | 2025-08-18 03:34:00 | NPP-375D | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 9d1501a5-feca-3c94-9c84-a209746b986d | -13.86687 | -45.54947 | 2025-08-18 03:34:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 0b115509-392f-37e2-a8b7-4a0f4022506f | -18.54749 | -43.99679 | 2025-08-18 03:34:00 | NPP-375D | GOUVEIA | MINAS GERAIS | Brasil | 3127602 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 965faaf3-7204-360f-a118-f5c3c99de6e6 | -13.43645 | -45.90294 | 2025-08-18 03:34:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 119511c4-c5b1-3228-b0ed-b8b0cbfc2b08 | -19.43851 | -43.73141 | 2025-08-18 03:34:00 | NPP-375D | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| b5badd31-64a6-3240-afba-935d04491b59 | -16.21858 | -43.14654 | 2025-08-18 03:34:00 | NPP-375D | RIACHO DOS MACHADOS | MINAS GERAIS | Brasil | 3154507 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0fcb5738-924b-3456-8e81-f9a995a0be86 | -15.91098 | -47.71176 | 2025-08-18 03:34:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 9fc535cb-6c0d-382e-87a4-3a9d95d65a42 | -16.70932 | -40.45497 | 2025-08-18 03:34:00 | NPP-375D | RIO DO PRADO | MINAS GERAIS | Brasil | 3155108 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 403d6a00-15fe-380a-9136-40ba1021308a | -16.73821 | -45.0021 | 2025-08-18 03:34:00 | NPP-375D | PONTO CHIQUE | MINAS GERAIS | Brasil | 3152131 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 238d0d4e-c9b4-3ae5-8e52-30c8573265d6 | -19.9216 | -43.86622 | 2025-08-18 03:34:00 | NPP-375D | SABARÁ | MINAS GERAIS | Brasil | 3156700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 2d46f7b0-7eac-3c55-b56a-8d91a6523ad9 | -16.73909 | -44.99792 | 2025-08-18 03:34:00 | NPP-375D | PONTO CHIQUE | MINAS GERAIS | Brasil | 3152131 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cfc39f64-9f8c-31d6-a008-797d4d6dafb0 | -13.86791 | -45.54449 | 2025-08-18 03:34:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 6d750e33-a3b2-32df-90cc-f14a041b87ff | -13.8751 | -45.54124 | 2025-08-18 03:34:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3f81269d-4b8d-36ee-bce1-42d3350684b2 | -18.9048 | -45.0391 | 2025-08-18 03:34:00 | NPP-375D | POMPÉU | MINAS GERAIS | Brasil | 3152006 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e8078310-9b3f-3b43-8e81-8a090c696594 | -17.39597 | -42.62387 | 2025-08-18 03:34:00 | NPP-375D | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 23.0 |
| 840a89d8-dc5f-36f6-9548-2efe04fde475 | -12.63069 | -46.89388 | 2025-08-18 03:34:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2178f85f-74fb-3086-ab27-bc71ecd2a7b4 | -18.54317 | -43.99141 | 2025-08-18 03:34:00 | NPP-375D | MONJOLOS | MINAS GERAIS | Brasil | 3142502 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5011ce31-4879-3c4d-a696-ee602c33ab56 | -12.62206 | -46.90066 | 2025-08-18 03:34:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7a4c873b-5877-3e2f-a0c6-e7912fb0d856 | -12.42503 | -43.76837 | 2025-08-18 03:34:00 | NPP-375D | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9661a971-59bd-3480-a06e-761406c2e8c1 | -14.19263 | -42.81387 | 2025-08-18 03:34:00 | NPP-375D | GUANAMBI | BAHIA | Brasil | 2911709 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 0e052e34-2327-364f-b095-3f4307c23a32 | -17.39109 | -42.62287 | 2025-08-18 03:34:00 | NPP-375D | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 23.0 |
| b381690b-dd76-3782-8b22-2588315bad34 | -13.43116 | -45.89614 | 2025-08-18 03:34:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fef0e4fe-14a0-356e-932b-a9fecd867025 | -18.61552 | -49.20127 | 2025-08-18 03:34:00 | NPP-375D | CENTRALINA | MINAS GERAIS | Brasil | 3115805 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 275b8ff6-d770-3435-a6a8-445bf2f7444d | -18.61731 | -49.19368 | 2025-08-18 03:34:00 | NPP-375D | CENTRALINA | MINAS GERAIS | Brasil | 3115805 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 7970d483-ac3b-31ac-aec4-96406145499b | -13.58741 | -47.76122 | 2025-08-18 03:34:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| f6d58f2b-adf2-36ab-ba1e-77569b8cf411 | -17.92831 | -44.36873 | 2025-08-18 03:34:00 | NPP-375D | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 02a3c6e5-14b1-3a2d-999e-e964e6bdd39e | -13.59402 | -47.74553 | 2025-08-18 03:34:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 922f6e21-b346-3f47-abd5-9884a215cfb7 | -13.43108 | -45.89621 | 2025-08-18 03:34:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 70e37338-d074-3648-812e-4895794989fc | -12.42009 | -43.76312 | 2025-08-18 03:34:00 | NPP-375D | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c64071de-c4d3-34a9-a680-5ff6cbcc14f7 | -18.04794 | -43.81671 | 2025-08-18 03:34:00 | NPP-375D | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 0.3 |
| b3bcdca7-8ef5-3052-8684-745105974c1d | -13.43534 | -45.90832 | 2025-08-18 03:34:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d2281cb7-f58c-3236-acad-a0e0e4e1527f | -18.54825 | -43.99313 | 2025-08-18 03:34:00 | NPP-375D | GOUVEIA | MINAS GERAIS | Brasil | 3127602 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 438ed813-6eaa-3655-8c18-b6806ab7126d | -17.32911 | -41.60245 | 2025-08-18 03:34:00 | NPP-375D | ITAIPÉ | MINAS GERAIS | Brasil | 3132305 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 86f9eeac-1c45-37e5-9a05-44924982664d | -12.42582 | -43.76435 | 2025-08-18 03:34:00 | NPP-375D | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 353f62a0-b065-36ea-8045-2d882aaceb36 | -20.25217 | -41.95714 | 2025-08-18 03:34:00 | NPP-375D | REDUTO | MINAS GERAIS | Brasil | 3154150 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 67aecd70-d338-38f2-a8b9-2229370650c8 | -12.62937 | -46.90007 | 2025-08-18 03:34:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7e684bfe-07bf-3631-a003-4ba4b55d52a0 | -17.92293 | -44.36755 | 2025-08-18 03:34:00 | NPP-375D | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 06ac4a76-5d8f-304e-b045-d8d979442b8e | -17.38996 | -42.62854 | 2025-08-18 03:34:00 | NPP-375D | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 38.3 |
| c23563e9-9b13-382b-842a-041efd737a1a | -16.67748 | -41.36124 | 2025-08-18 03:34:00 | NPP-375D | PONTO DOS VOLANTES | MINAS GERAIS | Brasil | 3152170 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 066fe824-0efd-3639-9950-64afcf36a758 | -14.19328 | -42.81058 | 2025-08-18 03:34:00 | NPP-375D | GUANAMBI | BAHIA | Brasil | 2911709 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| c7f32d5b-8340-3648-bcdf-1d988c6fc5f9 | -13.43634 | -45.90297 | 2025-08-18 03:34:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 81cc1e0f-3cb3-388c-91f9-e7e173550a90 | -13.58331 | -47.76033 | 2025-08-18 03:34:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 9ada020b-90e0-394f-b3ff-42e4bc38d7b1 | -15.96323 | -43.90332 | 2025-08-18 03:34:00 | NPP-375D | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Caatinga | 1.3 |
| c827fc53-7764-3e5a-83a4-b83fd103a333 | -19.43349 | -43.73026 | 2025-08-18 03:34:00 | NPP-375D | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 0069a7bf-389a-3cc5-a9e5-555e8ffd7d70 | -13.58024 | -47.76002 | 2025-08-18 03:34:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| fe0a6156-378a-3cf8-9208-e144c64cd8f2 | -20.08843 | -41.56747 | 2025-08-18 03:34:00 | NPP-375D | LAJINHA | MINAS GERAIS | Brasil | 3137700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 2db8b20d-4812-39f2-a605-c9b519834291 | -19.5414 | -45.61748 | 2025-08-18 03:34:00 | NPP-375D | DORES DO INDAIÁ | MINAS GERAIS | Brasil | 3123205 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0884ff59-f963-3d45-a22b-81d43ffbba7c | -16.21924 | -43.14325 | 2025-08-18 03:34:00 | NPP-375D | RIACHO DOS MACHADOS | MINAS GERAIS | Brasil | 3154507 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b456a444-e769-3dfe-b70e-9837d1e5d377 | -18.90401 | -45.03818 | 2025-08-18 03:34:00 | NPP-375D | POMPÉU | MINAS GERAIS | Brasil | 3152006 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7d15d25f-cf6a-3aa1-945f-c3f908a3f5b8 | -17.85019 | -42.52153 | 2025-08-18 03:34:00 | NPP-375D | CAPELINHA | MINAS GERAIS | Brasil | 3112307 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| f201ffbd-33fa-3826-84da-885b36ed2749 | -19.54028 | -45.61538 | 2025-08-18 03:34:00 | NPP-375D | DORES DO INDAIÁ | MINAS GERAIS | Brasil | 3123205 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a267879b-c279-391a-a19f-e523c4e14895 | -18.54391 | -43.98782 | 2025-08-18 03:34:00 | NPP-375D | MONJOLOS | MINAS GERAIS | Brasil | 3142502 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| adf34a8b-cbdd-36e5-b916-c57dee3ad514 | -17.6278 | -39.92945 | 2025-08-18 03:34:00 | NPP-375D | CARAVELAS | BAHIA | Brasil | 2906907 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| c6824f6a-5c06-3021-94e8-c1aea3115b7c | -13.58894 | -47.75407 | 2025-08-18 03:34:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 1fc80d71-efe8-38b9-974c-9c536210246f | -19.53669 | -45.61205 | 2025-08-18 03:34:00 | NPP-375D | DORES DO INDAIÁ | MINAS GERAIS | Brasil | 3123205 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 520fe483-a130-34f2-934b-efbe4fbe2e69 | -14.16824 | -41.58778 | 2025-08-18 03:34:00 | NPP-375D | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 008cdb8b-ef3e-322c-8027-6cc6744fe1d9 | -19.53466 | -45.61405 | 2025-08-18 03:34:00 | NPP-375D | DORES DO INDAIÁ | MINAS GERAIS | Brasil | 3123205 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| aead8f08-f5a5-317a-81ca-1682da7e47b2 | -19.53579 | -45.61609 | 2025-08-18 03:34:00 | NPP-375D | DORES DO INDAIÁ | MINAS GERAIS | Brasil | 3123205 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9fb91d6f-1f9e-31e8-a4fb-919a119f9d58 | -12.4193 | -43.76711 | 2025-08-18 03:34:00 | NPP-375D | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 07187067-c655-3e1c-bd44-ab8b9279a71a | -15.91158 | -47.71233 | 2025-08-18 03:34:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 24ec0084-2b7d-3010-ac4c-06095fe6eb9f | -13.59223 | -47.75364 | 2025-08-18 03:34:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 9ce6e14e-a28c-33f7-9263-bcc90d21d883 | -13.86893 | -45.53967 | 2025-08-18 03:34:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 888faa81-8cc6-3a77-b3e1-bc00caab61fd | -18.04343 | -43.81224 | 2025-08-18 03:34:00 | NPP-375D | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 816c348c-eba1-33e5-bc49-4395833847f8 | -13.58492 | -47.75307 | 2025-08-18 03:34:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d35ad55a-a38f-3d59-920f-ace81074893d | -13.4352 | -45.90833 | 2025-08-18 03:34:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| aaced49f-4f1e-3db6-b33d-f69bb9ae9ca4 | -15.49749 | -48.52794 | 2025-08-18 03:34:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2caff64a-d995-36ab-9a0e-97696d6ff4dc | -23.13648 | -49.99503 | 2025-08-18 03:36:00 | NPP-375D | JACAREZINHO | PARANÁ | Brasil | 4111803 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 42b96401-902f-3eba-9101-49b6caebb84f | -23.07274 | -45.61254 | 2025-08-18 03:36:00 | NPP-375D | TAUBATÉ | SÃO PAULO | Brasil | 3554102 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| fd3807dd-914d-3c2d-bf4f-70f4876aee34 | -23.67771 | -51.6423 | 2025-08-18 03:36:00 | NPP-375D | MARUMBI | PARANÁ | Brasil | 4115507 | 41 | 33 | nan | nan | nan | Mata Atlântica | 5.4 |
| 7f8bb1f1-ff85-3cb0-b716-fc696a712231 | -23.134 | -49.99712 | 2025-08-18 03:36:00 | NPP-375D | JACAREZINHO | PARANÁ | Brasil | 4111803 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| bc8dd0a8-11e0-3614-97ee-f07dcaaa6ad5 | -23.06752 | -45.61112 | 2025-08-18 03:36:00 | NPP-375D | TAUBATÉ | SÃO PAULO | Brasil | 3554102 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 04d0dafe-68bf-36cb-8324-02a79c1dc93f | -22.82133 | -45.05137 | 2025-08-18 03:36:00 | NPP-375D | LORENA | SÃO PAULO | Brasil | 3527207 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 06c23b6d-5b83-37f6-85e0-7baf3ef385df | -23.68492 | -51.64311 | 2025-08-18 03:36:00 | NPP-375D | MARUMBI | PARANÁ | Brasil | 4115507 | 41 | 33 | nan | nan | nan | Mata Atlântica | 40.9 |
| cce39547-ae74-34b3-b265-d26bbe4631f0 | -22.136 | -50.02546 | 2025-08-18 03:36:00 | NPP-375D | MARÍLIA | SÃO PAULO | Brasil | 3529005 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 6d7a1f91-0aca-3ee2-b1a3-9a97c1cdf0f3 | -23.67794 | -51.64034 | 2025-08-18 03:36:00 | NPP-375D | MARUMBI | PARANÁ | Brasil | 4115507 | 41 | 33 | nan | nan | nan | Mata Atlântica | 4.9 |
| 681172e9-eeb0-339f-bbfa-8ec64c0ba042 | -23.68471 | -51.645 | 2025-08-18 03:36:00 | NPP-375D | MARUMBI | PARANÁ | Brasil | 4115507 | 41 | 33 | nan | nan | nan | Mata Atlântica | 38.6 |
| b03ce5f6-f534-396e-9d4d-e569ebff8d44 | -23.68246 | -51.65324 | 2025-08-18 03:36:00 | NPP-375D | MARUMBI | PARANÁ | Brasil | 4115507 | 41 | 33 | nan | nan | nan | Mata Atlântica | 38.6 |
| 4af5e0b9-bae5-361d-b55f-eb7ef9388219 | -21.79124 | -47.55537 | 2025-08-18 03:36:00 | NPP-375D | DESCALVADO | SÃO PAULO | Brasil | 3513702 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 09bdde8e-a1de-34a3-b51f-d6b32d7f1bf2 | -22.33267 | -47.7281 | 2025-08-18 03:36:00 | NPP-375D | RIO CLARO | SÃO PAULO | Brasil | 3543907 | 35 | 33 | nan | nan | nan | Cerrado | 4.5 |
| c9eee94c-edb1-37e1-80d3-8000d50967a6 | -23.07352 | -45.60899 | 2025-08-18 03:36:00 | NPP-375D | TAUBATÉ | SÃO PAULO | Brasil | 3554102 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 872da39f-bc58-367c-9691-2c352c1cdaf8 | -21.7853 | -47.55349 | 2025-08-18 03:36:00 | NPP-375D | SANTA RITA DO PASSA QUATRO | SÃO PAULO | Brasil | 3547502 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 942dc864-63d5-3f9c-aff6-2f1834b98a77 | -23.50365 | -48.31527 | 2025-08-18 03:36:00 | NPP-375D | ANGATUBA | SÃO PAULO | Brasil | 3502200 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.2 |


[Clique aqui para ver as próximas entradas](README10.md)
