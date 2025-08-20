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

## Dados Diários - Página 61

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e4575922-2081-30e5-9ef3-15c83d722dc8 | -21.27176 | -45.48042 | 2025-08-20 12:17:00 | TERRA_M-T | SANTANA DA VARGEM | MINAS GERAIS | Brasil | 3158300 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.9 |
| a7707f8d-d43a-3ef4-87f4-250c893e46fb | -17.57602 | -42.27702 | 2025-08-20 12:17:00 | TERRA_M-T | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Mata Atlântica | 108.5 |
| 6b9f3e3f-87e2-3703-987c-88202a36be0c | -20.22678 | -44.12964 | 2025-08-20 12:17:00 | TERRA_M-T | BRUMADINHO | MINAS GERAIS | Brasil | 3109006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 59.3 |
| 34217d1a-67c9-30ce-8af8-fb744d3a1cd9 | -15.5422 | -42.28646 | 2025-08-20 12:17:00 | TERRA_M-T | INDAIABIRA | MINAS GERAIS | Brasil | 3130655 | 31 | 33 | nan | nan | nan | Cerrado | 10.0 |
| ac93f461-9c09-3e16-a2b5-092619c4f1ff | -15.43103 | -46.71635 | 2025-08-20 12:17:00 | TERRA_M-T | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 6b22dffc-507a-3d37-89a6-07842b9b8af6 | -18.68323 | -46.9691 | 2025-08-20 12:17:00 | TERRA_M-T | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 19.5 |
| d426990a-51c6-3dde-bf59-19aa34b67cd8 | -13.86829 | -45.56896 | 2025-08-20 12:17:00 | TERRA_M-T | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 7859517f-1620-3548-a2c1-611dc926aa0c | -18.15023 | -49.66493 | 2025-08-20 12:17:00 | TERRA_M-T | BOM JESUS DE GOIÁS | GOIÁS | Brasil | 5203500 | 52 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 3d7c80fc-36d5-3664-85d2-4d366cc2f8c0 | -14.69898 | -46.99503 | 2025-08-20 12:17:00 | TERRA_M-T | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 90419290-d348-3ff9-90e3-23dcff8d07a2 | -13.15366 | -54.91914 | 2025-08-20 12:17:00 | TERRA_M-T | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 63.9 |
| d635f765-0d62-33b4-a717-aeeaaf6cde4f | -15.54654 | -40.73812 | 2025-08-20 12:17:00 | TERRA_M-T | ENCRUZILHADA | BAHIA | Brasil | 2910404 | 29 | 33 | nan | nan | nan | Mata Atlântica | 14.9 |
| f85aa19f-c999-3e95-9a53-e7b2a5b897bd | -15.54906 | -48.55738 | 2025-08-20 12:17:00 | TERRA_M-T | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 767cd5ea-8bd0-3b0a-a61d-92088df86b3c | -15.71592 | -46.5169 | 2025-08-20 12:17:00 | TERRA_M-T | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 5.1 |
| a48002e3-594a-3f75-bea6-f0cd8482033b | -21.03272 | -45.83734 | 2025-08-20 12:17:00 | TERRA_M-T | BOA ESPERANÇA | MINAS GERAIS | Brasil | 3107109 | 31 | 33 | nan | nan | nan | Cerrado | 11.5 |
| b278940b-7c2f-32da-ab1a-c79dbb238998 | -17.6845 | -44.4361 | 2025-08-20 12:17:00 | TERRA_M-T | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 17.7 |
| 7b7befa6-9c9f-3272-bd82-d4aab49c8afd | -17.01602 | -49.5418 | 2025-08-20 12:17:00 | TERRA_M-T | GUAPÓ | GOIÁS | Brasil | 5209200 | 52 | 33 | nan | nan | nan | Cerrado | 6.0 |
| b939512b-0e18-3d5a-adbf-d085b90d7b76 | -15.14607 | -41.2862 | 2025-08-20 12:17:00 | TERRA_M-T | BELO CAMPO | BAHIA | Brasil | 2903508 | 29 | 33 | nan | nan | nan | Mata Atlântica | 31.9 |
| 3acca4e9-7a2d-3d04-919f-ed622ffc6dbd | -21.38084 | -45.26199 | 2025-08-20 12:17:00 | TERRA_M-T | CARMO DA CACHOEIRA | MINAS GERAIS | Brasil | 3113909 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.0 |
| aecc7fdd-729b-3883-b23e-f9404706b448 | -13.48968 | -47.06733 | 2025-08-20 12:17:00 | TERRA_M-T | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 2d992615-a95e-3d5e-8622-34bcddfc2f87 | -19.0044 | -47.177 | 2025-08-20 12:17:00 | TERRA_M-T | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 9.5 |
| f4c34eb9-1a7b-32ac-8c55-de4d8e72f78d | -13.49099 | -47.05829 | 2025-08-20 12:17:00 | TERRA_M-T | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 9fbefc18-c5b0-3f88-9f31-59cc5a8fcf94 | -21.19356 | -45.45162 | 2025-08-20 12:17:00 | TERRA_M-T | COQUEIRAL | MINAS GERAIS | Brasil | 3118700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.6 |
| fbc6b408-200a-342d-a09c-75b8ffd39723 | -21.19505 | -45.43995 | 2025-08-20 12:17:00 | TERRA_M-T | COQUEIRAL | MINAS GERAIS | Brasil | 3118700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 27.6 |
| 0d27cd7a-0b7a-3701-be1c-6e942d80b7fe | -19.66971 | -48.65166 | 2025-08-20 12:17:00 | TERRA_M-T | CAMPO FLORIDO | MINAS GERAIS | Brasil | 3111408 | 31 | 33 | nan | nan | nan | Cerrado | 17.4 |
| ba05c463-a8f1-3a48-bba5-d3689d6cbe7e | -17.57792 | -42.2603 | 2025-08-20 12:17:00 | TERRA_M-T | SETUBINHA | MINAS GERAIS | Brasil | 3165552 | 31 | 33 | nan | nan | nan | Mata Atlântica | 33.9 |
| d8edcd04-7ea9-392a-b153-ebe075128dc1 | -18.15943 | -49.66644 | 2025-08-20 12:17:00 | TERRA_M-T | BOM JESUS DE GOIÁS | GOIÁS | Brasil | 5203500 | 52 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 98e07ceb-27f7-3b7b-ae5a-5db0d4372381 | -17.27156 | -46.92426 | 2025-08-20 12:17:00 | TERRA_M-T | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 15.8 |
| 8d023986-856f-36ee-95f9-ca28b7b23613 | -17.48614 | -44.71134 | 2025-08-20 12:17:00 | TERRA_M-T | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 23.8 |
| aadc4cfe-3e25-33a0-ac0f-c5ab981e8655 | -21.66901 | -41.43639 | 2025-08-20 12:17:00 | TERRA_M-T | CAMPOS DOS GOYTACAZES | RIO DE JANEIRO | Brasil | 3301009 | 33 | 33 | nan | nan | nan | Mata Atlântica | 14.4 |
| 8eebf617-41a7-3efe-bf06-b064d1e259ff | -19.73457 | -45.71155 | 2025-08-20 12:17:00 | TERRA_M-T | LUZ | MINAS GERAIS | Brasil | 3138807 | 31 | 33 | nan | nan | nan | Cerrado | 6.3 |
| ce66f178-a4c8-335b-b1a2-2abaaa2e99c7 | -14.16431 | -45.28846 | 2025-08-20 12:17:00 | TERRA_M-T | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 7.0 |
| c1dffedd-8c60-3356-a8d1-89ab4ccdc126 | -16.21533 | -47.92332 | 2025-08-20 12:17:00 | TERRA_M-T | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 505b1777-3039-3a0e-a40d-6fa6abf61007 | -13.8773 | -45.57024 | 2025-08-20 12:17:00 | TERRA_M-T | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 00adebf7-209a-3463-b0b4-5e9580e71c0e | -13.19607 | -50.74522 | 2025-08-20 12:17:00 | TERRA_M-T | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 10.2 |
| b9a4ae16-0602-3657-994b-4f1614016df2 | -13.86959 | -45.55952 | 2025-08-20 12:17:00 | TERRA_M-T | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 57.0 |
| 7508844c-6053-3edf-a8d5-ad0b8ef216d4 | -19.03464 | -48.0716 | 2025-08-20 12:17:00 | TERRA_M-T | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 811b2bff-580c-3193-a01f-3031f1934817 | -14.73663 | -41.6627 | 2025-08-20 12:17:00 | TERRA_M-T | PRESIDENTE JÂNIO QUADROS | BAHIA | Brasil | 2925709 | 29 | 33 | nan | nan | nan | Caatinga | 26.8 |
| 5de78743-56ff-39d8-ace8-52e2e36954ed | -15.002 | -54.8032 | 2025-08-20 12:17:00 | TERRA_M-T | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 32.4 |
| 527cfdf2-1d0f-3d7f-844d-f50bf88225c5 | -14.51036 | -46.63326 | 2025-08-20 12:17:00 | TERRA_M-T | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 20.2 |
| 01b95ccd-d992-3674-89fa-c3dcff30ddde | -20.21627 | -44.12815 | 2025-08-20 12:17:00 | TERRA_M-T | BRUMADINHO | MINAS GERAIS | Brasil | 3109006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.6 |
| d26f1eb6-56bc-37bc-b28e-f75305735def | -18.88399 | -51.56579 | 2025-08-20 12:17:00 | TERRA_M-T | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | 12.2 |
| cf3c9425-b5f0-3151-b130-bf1b4eb22ecc | -13.57934 | -47.02241 | 2025-08-20 12:17:00 | TERRA_M-T | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 93832bf8-7e32-3b2e-b79d-5e708623834d | -19.67581 | -48.67189 | 2025-08-20 12:17:00 | TERRA_M-T | CAMPO FLORIDO | MINAS GERAIS | Brasil | 3111408 | 31 | 33 | nan | nan | nan | Cerrado | 116.0 |
| 5dacd1eb-3232-3ada-bbc9-baec222b7b70 | -18.86196 | -48.92939 | 2025-08-20 12:17:00 | TERRA_M-T | MONTE ALEGRE DE MINAS | MINAS GERAIS | Brasil | 3142809 | 31 | 33 | nan | nan | nan | Cerrado | 6.5 |
| c68e7b32-73ac-3ba8-9739-c22f86347ae3 | -15.54891 | -40.72379 | 2025-08-20 12:17:00 | TERRA_M-T | ENCRUZILHADA | BAHIA | Brasil | 2910404 | 29 | 33 | nan | nan | nan | Mata Atlântica | 33.5 |
| 33341545-74be-3be0-ae1d-1301c29f0302 | -14.38894 | -39.80575 | 2025-08-20 12:17:00 | TERRA_M-T | IBICUÍ | BAHIA | Brasil | 2912301 | 29 | 33 | nan | nan | nan | Mata Atlântica | 24.3 |
| 977b8d09-c973-34d7-ba5a-c8a1e14caa8f | -16.54753 | -43.84081 | 2025-08-20 12:17:00 | TERRA_M-T | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 9e2c1315-4fa1-36d0-86aa-e0be085cbf59 | -15.76686 | -47.89829 | 2025-08-20 12:17:00 | TERRA_M-T | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 5.4 |
| db468065-8683-3d19-97bb-f39d37372764 | -17.65346 | -43.36897 | 2025-08-20 12:17:00 | TERRA_M-T | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 20.0 |
| 931fd6c1-97c6-3f2f-94c8-28288991db8a | -13.3363 | -54.4013 | 2025-08-20 12:17:00 | TERRA_M-T | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 57.9 |
| dcbbf1c6-2bad-33de-9c01-bcb9cd1b1cf0 | -20.79271 | -45.63812 | 2025-08-20 12:17:00 | TERRA_M-T | CRISTAIS | MINAS GERAIS | Brasil | 3120201 | 31 | 33 | nan | nan | nan | Cerrado | 22.4 |
| 428ab3c0-fc61-382a-9097-41080232ccb3 | -14.88282 | -48.07547 | 2025-08-20 12:17:00 | TERRA_M-T | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 2089972b-b503-303f-84bd-ea72d9a5ad3c | -15.27082 | -47.6914 | 2025-08-20 12:17:00 | TERRA_M-T | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 6.6 |
| a57a872c-1065-308d-a3a2-06cdcf9057de | -13.8709 | -45.55005 | 2025-08-20 12:17:00 | TERRA_M-T | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 46.5 |
| d2e12f68-6dc3-3717-b49f-5faacbda32eb | -19.67719 | -48.66248 | 2025-08-20 12:17:00 | TERRA_M-T | CAMPO FLORIDO | MINAS GERAIS | Brasil | 3111408 | 31 | 33 | nan | nan | nan | Cerrado | 255.3 |
| 38ce0a62-cce3-3ce3-b58c-d33c890027e0 | -18.9776 | -50.34419 | 2025-08-20 12:17:00 | TERRA_M-T | SANTA VITÓRIA | MINAS GERAIS | Brasil | 3159803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 71.2 |
| 5381c60c-94d1-3ad1-8537-c50480fa2e34 | -13.86318 | -45.53933 | 2025-08-20 12:17:00 | TERRA_M-T | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 53.9 |
| 0265b989-27f4-3fca-9957-b2db649beb23 | -18.27729 | -51.94691 | 2025-08-20 12:17:00 | TERRA_M-T | SERRANÓPOLIS | GOIÁS | Brasil | 5220504 | 52 | 33 | nan | nan | nan | Cerrado | 99.6 |
| cb0e2b22-31e5-314e-a777-521f70e66714 | -15.73384 | -41.15156 | 2025-08-20 12:17:00 | TERRA_M-T | ENCRUZILHADA | BAHIA | Brasil | 2910404 | 29 | 33 | nan | nan | nan | Mata Atlântica | 18.9 |
| 929c636f-5e53-355c-9f06-0fdc5f592830 | -15.55268 | -43.14844 | 2025-08-20 12:17:00 | TERRA_M-T | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 10.5 |
| 388ba83f-ca3c-39df-baf9-904adca1e8fb | -20.79414 | -45.62696 | 2025-08-20 12:17:00 | TERRA_M-T | CRISTAIS | MINAS GERAIS | Brasil | 3120201 | 31 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 4c600837-fb52-3fb8-a736-02b0ea1ba074 | -20.02196 | -45.6934 | 2025-08-20 12:17:00 | TERRA_M-T | LUZ | MINAS GERAIS | Brasil | 3138807 | 31 | 33 | nan | nan | nan | Cerrado | 5.0 |
| ca84874e-a13f-3348-8751-fd4eae149f33 | -18.51967 | -46.2864 | 2025-08-20 12:17:00 | TERRA_M-T | PRESIDENTE OLEGÁRIO | MINAS GERAIS | Brasil | 3153400 | 31 | 33 | nan | nan | nan | Cerrado | 5.2 |
| f3e3fe94-8354-3337-afcb-881446958339 | -13.62673 | -46.88181 | 2025-08-20 12:17:00 | TERRA_M-T | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| adf03098-ade3-3214-aecf-34769f88c7d8 | -15.54762 | -48.56695 | 2025-08-20 12:17:00 | TERRA_M-T | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 6c711e4e-124e-358f-8f61-d607d8be9986 | -20.22516 | -44.14314 | 2025-08-20 12:17:00 | TERRA_M-T | BRUMADINHO | MINAS GERAIS | Brasil | 3109006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 14.1 |
| d5020191-c806-3336-8be8-9ed88dbcc0eb | -19.66833 | -48.66106 | 2025-08-20 12:17:00 | TERRA_M-T | CAMPO FLORIDO | MINAS GERAIS | Brasil | 3111408 | 31 | 33 | nan | nan | nan | Cerrado | 194.0 |
| 559957fd-de37-3add-8074-e6f5ac045440 | -19.03598 | -48.06231 | 2025-08-20 12:17:00 | TERRA_M-T | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 1e16e87b-918a-3ec3-bc2b-2dd2fcc21cf3 | -18.673 | -46.97713 | 2025-08-20 12:17:00 | TERRA_M-T | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 14.5 |
| c0a5c830-bd07-3dbe-8833-761cc6897416 | -20.7532 | -47.90639 | 2025-08-20 12:17:00 | TERRA_M-T | ORLÂNDIA | SÃO PAULO | Brasil | 3534302 | 35 | 33 | nan | nan | nan | Cerrado | 6.1 |
| b5961366-d084-341a-9da8-c7bb9bf66d5a | -18.68192 | -46.97854 | 2025-08-20 12:17:00 | TERRA_M-T | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 17.9 |
| cc3c4308-59da-331f-9ba7-763efde5accc | -16.17523 | -43.6396 | 2025-08-20 12:17:00 | TERRA_M-T | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 6.9 |
| cd48febb-8c37-341e-b689-527b32311380 | -17.58762 | -42.27864 | 2025-08-20 12:17:00 | TERRA_M-T | SETUBINHA | MINAS GERAIS | Brasil | 3165552 | 31 | 33 | nan | nan | nan | Mata Atlântica | 27.6 |
| 3b615d55-59c4-391d-b4b4-90bd5f2db705 | -20.89988 | -45.20139 | 2025-08-20 12:17:00 | TERRA_M-T | CAMPO BELO | MINAS GERAIS | Brasil | 3111200 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.5 |
| b71b84e6-4c76-394e-bfe3-9c84e309fce9 | -14.39401 | -39.80089 | 2025-08-20 12:17:00 | TERRA_M-T | IBICUÍ | BAHIA | Brasil | 2912301 | 29 | 33 | nan | nan | nan | Mata Atlântica | 20.0 |
| b44e80bf-831a-31ba-96c4-0791588bdaeb | -18.52103 | -46.27653 | 2025-08-20 12:17:00 | TERRA_M-T | PRESIDENTE OLEGÁRIO | MINAS GERAIS | Brasil | 3153400 | 31 | 33 | nan | nan | nan | Cerrado | 4.0 |
| cc051289-1676-3db0-9d1f-1da221208d01 | -23.34312 | -46.11853 | 2025-08-20 12:19:00 | TERRA_M-T | GUARAREMA | SÃO PAULO | Brasil | 3518305 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.4 |
| 5ac79470-50b1-3cda-89da-1db24528a547 | -22.0902 | -45.1219 | 2025-08-20 12:19:00 | TERRA_M-T | CARMO DE MINAS | MINAS GERAIS | Brasil | 3114105 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.5 |
| ddd6d578-4e09-3449-8138-1236048e1b69 | -21.97585 | -42.89279 | 2025-08-20 12:19:00 | TERRA_M-T | SAPUCAIA | RIO DE JANEIRO | Brasil | 3305406 | 33 | 33 | nan | nan | nan | Mata Atlântica | 11.8 |
| c73006dd-3db8-3e70-913c-a4d3bf70a213 | -22.63429 | -44.56627 | 2025-08-20 12:19:00 | TERRA_M-T | SÃO JOSÉ DO BARREIRO | SÃO PAULO | Brasil | 3549607 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.6 |
| 64a2f816-3a1f-39a1-a696-3ad849aa5454 | -23.1355 | -49.34994 | 2025-08-20 12:19:00 | TERRA_M-T | PIRAJU | SÃO PAULO | Brasil | 3538808 | 35 | 33 | nan | nan | nan | Mata Atlântica | 9.9 |
| 7072daf1-fff9-3461-9c3f-bcd928dfe181 | -23.04057 | -47.40495 | 2025-08-20 12:19:00 | TERRA_M-T | ELIAS FAUSTO | SÃO PAULO | Brasil | 3514908 | 35 | 33 | nan | nan | nan | Mata Atlântica | 8.1 |
| ac8d40a7-caae-30cd-bad9-a2a4d88d335a | -22.30337 | -47.14052 | 2025-08-20 12:19:00 | TERRA_M-T | CONCHAL | SÃO PAULO | Brasil | 3512209 | 35 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 4a10fe1a-655e-33bb-ba7d-7d1626e7eb7c | -22.99833 | -46.5962 | 2025-08-20 12:19:00 | TERRA_M-T | BRAGANÇA PAULISTA | SÃO PAULO | Brasil | 3507605 | 35 | 33 | nan | nan | nan | Mata Atlântica | 39.1 |
| 88e94887-535e-3716-838e-413b3ff0395f | -21.91155 | -47.25104 | 2025-08-20 12:19:00 | TERRA_M-T | SANTA CRUZ DAS PALMEIRAS | SÃO PAULO | Brasil | 3546306 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.0 |
| 952dc889-5503-3fb9-95a1-e55860ae61c3 | -21.97756 | -42.8766 | 2025-08-20 12:19:00 | TERRA_M-T | SAPUCAIA | RIO DE JANEIRO | Brasil | 3305406 | 33 | 33 | nan | nan | nan | Mata Atlântica | 17.2 |
| 7549b26a-8932-3f1e-bd53-964af5d6a99e | -23.39106 | -47.25459 | 2025-08-20 12:19:00 | TERRA_M-T | ITU | SÃO PAULO | Brasil | 3523909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 27.3 |
| d82c8364-4027-31f3-a599-27c82a611540 | -22.8465 | -52.7044 | 2025-08-20 12:19:00 | TERRA_M-T | TERRA RICA | PARANÁ | Brasil | 4127304 | 41 | 33 | nan | nan | nan | Mata Atlântica | 11.9 |
| 65f91fea-4ede-382f-a174-e444c8e554e8 | -22.27282 | -48.50113 | 2025-08-20 12:19:00 | TERRA_M-T | JAÚ | SÃO PAULO | Brasil | 3525300 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.8 |
| be3d9b26-3f2d-3c98-862f-4e793fd807ad | -23.34171 | -46.13001 | 2025-08-20 12:19:00 | TERRA_M-T | GUARAREMA | SÃO PAULO | Brasil | 3518305 | 35 | 33 | nan | nan | nan | Mata Atlântica | 17.1 |
| f33f8f99-05ee-36f3-bd14-8fb0746803c9 | -22.52603 | -46.62666 | 2025-08-20 12:19:00 | TERRA_M-T | LINDÓIA | SÃO PAULO | Brasil | 3527009 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.0 |
| 55f17d6e-a8a5-388a-883b-ddf8ad99724a | -22.9997 | -46.58543 | 2025-08-20 12:19:00 | TERRA_M-T | BRAGANÇA PAULISTA | SÃO PAULO | Brasil | 3507605 | 35 | 33 | nan | nan | nan | Mata Atlântica | 19.2 |
| e918c436-3aef-3706-8ccf-25ab387d22e9 | -21.79028 | -46.58316 | 2025-08-20 12:19:00 | TERRA_M-T | POÇOS DE CALDAS | MINAS GERAIS | Brasil | 3151800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.6 |
| 6c18a1bc-9224-384a-9758-e72b9a7deec2 | -21.60258 | -48.28594 | 2025-08-20 12:19:00 | TERRA_M-T | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 22.9 |
| 17363c38-3eeb-3177-ae55-6c2dc3e7e75a | -21.60393 | -48.27647 | 2025-08-20 12:19:00 | TERRA_M-T | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | 8.8 |
| d365db48-e247-3845-a0fe-a1f17d51feaf | -22.95024 | -43.69174 | 2025-08-20 12:19:00 | TERRA_M-T | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 15.3 |
| 55581659-88eb-3592-ad55-9d5c28c52ff5 | -21.79166 | -46.57277 | 2025-08-20 12:19:00 | TERRA_M-T | POÇOS DE CALDAS | MINAS GERAIS | Brasil | 3151800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.9 |
| 9dfbc974-afa3-376a-8b87-ace5a0fe4951 | -21.54089 | -49.52867 | 2025-08-20 12:19:00 | TERRA_M-T | SABINO | SÃO PAULO | Brasil | 3544608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.2 |
| 852fd19b-3fee-33f6-bd7b-296abe51b4c7 | -13.3346 | -54.4233 | 2025-08-20 12:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 79.6 |
| f59cb404-75a1-35b7-b24a-befdeec55343 | -12.9921 | -45.2252 | 2025-08-20 12:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 169.6 |


[Clique aqui para ver as próximas entradas](README62.md)
