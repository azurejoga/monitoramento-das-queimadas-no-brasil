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

## Dados Diários - Página 82

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 55d1424a-ea9f-3913-9c7c-682c1a6fb3f2 | -15.35594 | -46.28265 | 2025-10-03 04:14:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e284e79c-02b5-3e9e-956a-01203aa7f82f | -15.5889 | -46.93605 | 2025-10-03 04:14:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 40efabf4-8ea6-31c8-a6be-caab4a46e0ab | -14.87282 | -48.34028 | 2025-10-03 04:14:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 18805916-c2d6-3ed0-85e9-bbf4a35584a3 | -20.38631 | -44.13217 | 2025-10-03 04:14:00 | NPP-375D | BELO VALE | MINAS GERAIS | Brasil | 3106408 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 45095aaf-128e-32d1-9a7e-b2b72a2cd1ae | -15.11678 | -46.6848 | 2025-10-03 04:14:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e6849442-6afc-3cab-8dd0-6eabd1b5560b | -14.88179 | -46.85504 | 2025-10-03 04:14:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 590266f8-6221-32b5-8d72-1f1b7bf1263a | -14.93421 | -46.91583 | 2025-10-03 04:14:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 15bc1b2e-408e-34cc-9f60-5110f1e04e78 | -15.27683 | -47.91496 | 2025-10-03 04:14:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bdcfb302-0ed8-303a-983d-0638b2b2319f | -17.87872 | -57.61433 | 2025-10-03 04:14:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 4595d72f-bc2a-313c-ad51-3aa63e414d39 | -17.85415 | -57.61625 | 2025-10-03 04:14:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 00437520-cabb-3144-98a0-c685a2c52636 | -15.92176 | -43.3391 | 2025-10-03 04:14:00 | NPP-375D | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4441531d-5e23-3c3b-8e1a-e975d33ebce7 | -16.40804 | -52.16225 | 2025-10-03 04:14:00 | NPP-375D | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 4ee5436c-cd17-33a9-9f54-a2db3ffe134e | -16.8755 | -52.79688 | 2025-10-03 04:14:00 | NPP-375D | DOVERLÂNDIA | GOIÁS | Brasil | 5207253 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| dc3feac8-a9a6-3ee3-80e2-50fe5e386bae | -14.93566 | -46.89125 | 2025-10-03 04:14:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 8.0 |
| ffc880d8-7a81-3087-8db7-d760d82a4cfb | -17.4053 | -45.0501 | 2025-10-03 04:14:00 | NPP-375D | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 9febcf2e-d513-3ff8-bc09-7c732e7931f4 | -19.23228 | -43.71541 | 2025-10-03 04:14:00 | NPP-375D | SANTANA DO RIACHO | MINAS GERAIS | Brasil | 3159001 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a05b2e64-1a59-3501-9e3a-c52fe3473ff2 | -15.5743 | -46.95691 | 2025-10-03 04:14:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3e1a4418-a721-36f2-afa3-561644e31203 | -15.58376 | -46.94403 | 2025-10-03 04:14:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1a6c361d-3cd0-3c91-8820-6d673aad33e3 | -14.90698 | -48.34299 | 2025-10-03 04:14:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 6.1 |
| dc9d0eab-f223-3fc1-924f-3314b9e0f559 | -14.94231 | -46.8963 | 2025-10-03 04:14:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 99dfbc26-e82d-3f82-9c51-8b03b03a43f3 | -19.59458 | -43.81316 | 2025-10-03 04:14:00 | NPP-375D | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 43aa056b-0232-3535-82e0-298a64f970ec | -14.86953 | -48.31292 | 2025-10-03 04:14:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 84db9c51-d001-39c3-833c-e529d8fb82e1 | -16.0743 | -51.00107 | 2025-10-03 04:14:00 | NPP-375D | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 55f098f4-50af-3cc5-b5ed-a84f86c8cc9f | -17.49584 | -43.47064 | 2025-10-03 04:14:00 | NPP-375D | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| aeb5a7bd-5505-3390-9fdc-b54fc82d61a3 | -15.59046 | -46.90582 | 2025-10-03 04:14:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 99b8ca9c-a8f1-355c-be74-6edb4965cf5a | -20.38688 | -44.12843 | 2025-10-03 04:14:00 | NPP-375D | BELO VALE | MINAS GERAIS | Brasil | 3106408 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 48091796-1c02-3f6f-80b5-3d52316d57b0 | -21.34454 | -45.01268 | 2025-10-03 04:14:00 | NPP-375D | INGAÍ | MINAS GERAIS | Brasil | 3130804 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| cbdef004-2f4d-3e06-a5f6-19cf81ca36f5 | -21.59099 | -45.27739 | 2025-10-03 04:14:00 | NPP-375D | VARGINHA | MINAS GERAIS | Brasil | 3170701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 2712aa4c-86d0-330d-a316-343f9dac1f37 | -16.17272 | -57.59724 | 2025-10-03 04:14:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| acd05f99-758f-31f5-857a-7680966ab1c1 | -15.93213 | -43.07405 | 2025-10-03 04:14:00 | NPP-375D | RIACHO DOS MACHADOS | MINAS GERAIS | Brasil | 3154507 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 518a88d9-8ab8-37aa-b5fa-8c205fa101ef | -19.89564 | -44.50819 | 2025-10-03 04:14:00 | NPP-375D | FLORESTAL | MINAS GERAIS | Brasil | 3126000 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 54868a62-f97f-36b3-966a-cef595d6a1dd | -15.24602 | -49.3232 | 2025-10-03 04:14:00 | NPP-375D | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 653a3d6e-fe19-3e86-8d6f-b05d55eff84a | -15.35342 | -47.06294 | 2025-10-03 04:14:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 309834c5-7ea7-3382-af2a-c29ab45116ac | -14.71732 | -48.20218 | 2025-10-03 04:14:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 5f743cc0-5b5a-327c-9dfe-71e20db5afc6 | -16.3623 | -47.0723 | 2025-10-03 04:14:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 4.6 |
| b139fc1d-bc20-30bc-957c-a323b3cfe73f | -14.66236 | -48.26007 | 2025-10-03 04:14:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0facdeb7-81e0-3abb-b471-ce7f28af568d | -17.84626 | -57.62012 | 2025-10-03 04:14:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 56add2ed-6d41-3efd-9935-162b2802447a | -16.76718 | -43.95959 | 2025-10-03 04:14:00 | NPP-375D | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ef22ab2d-5b30-3466-bece-6322f1dd06e8 | -17.98541 | -45.03335 | 2025-10-03 04:14:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 172d2191-8b1a-3185-9524-434880a1ed14 | -14.89951 | -46.97054 | 2025-10-03 04:14:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 98ea7cfe-2192-33c0-9744-26ea22ad3b28 | -14.93727 | -46.88175 | 2025-10-03 04:14:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 0a7e47de-9528-3bd1-97cc-92686276b442 | -18.16452 | -53.33216 | 2025-10-03 04:14:00 | NPP-375D | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 4dac4b2c-f4f9-343b-8780-d1bc5774caf8 | -15.30445 | -46.28618 | 2025-10-03 04:14:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 15243645-47c7-333f-a72d-56def11a094d | -14.8914 | -46.97375 | 2025-10-03 04:14:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| cfb71eb4-c4db-3676-8fe9-f45ec93fd049 | -14.73849 | -48.10379 | 2025-10-03 04:14:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8bd3fe6b-bc91-3bfa-9498-4eb3acc7fca1 | -14.8734 | -49.71426 | 2025-10-03 04:14:00 | NPP-375D | GUARINOS | GOIÁS | Brasil | 5209457 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 554f50fb-fa8b-3447-a1d9-46e563bfa8b3 | -16.68573 | -53.01609 | 2025-10-03 04:14:00 | NPP-375D | PONTE BRANCA | MATO GROSSO | Brasil | 5106703 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 28246014-0cd5-30bf-8671-8235c37a8acf | -15.70716 | -46.25488 | 2025-10-03 04:14:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e26e1678-81c3-3bbb-ad88-d9ed92e7cb4f | -19.59067 | -45.90034 | 2025-10-03 04:14:00 | NPP-375D | ESTRELA DO INDAIÁ | MINAS GERAIS | Brasil | 3124708 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f87d702a-b44f-36e5-a98f-cee9d4d2ef5c | -15.57072 | -46.95599 | 2025-10-03 04:14:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 3d7d0c84-033e-34df-948c-dadb3055cfa0 | -19.87313 | -43.65273 | 2025-10-03 04:14:00 | NPP-375D | CAETÉ | MINAS GERAIS | Brasil | 3110004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| c893f3b4-535a-3a2e-9828-7c9e2d333633 | -20.14964 | -42.0191 | 2025-10-03 04:14:00 | NPP-375D | SIMONÉSIA | MINAS GERAIS | Brasil | 3167608 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 211debfe-41c9-31a1-b49f-0bffbcd6ee1b | -16.18169 | -57.58992 | 2025-10-03 04:14:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| f61180bf-0f9e-324a-8130-6f497cbd137e | -14.90038 | -47.82592 | 2025-10-03 04:14:00 | NPP-375D | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| ceb31891-d2f6-3ab1-ae46-3282680a5eb0 | -19.96478 | -43.64879 | 2025-10-03 04:14:00 | NPP-375D | CAETÉ | MINAS GERAIS | Brasil | 3110004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 1de2c25c-bc1f-3ed1-93cf-7dd9e371a4ae | -15.49184 | -45.92721 | 2025-10-03 04:14:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3bdc8043-1d03-31de-ba75-5e994b1879a0 | -15.27091 | -47.90363 | 2025-10-03 04:14:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bd89b5cb-a435-36c6-8edd-62460617598c | -15.52554 | -46.80704 | 2025-10-03 04:14:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8b6f2a0d-5b65-3f4f-aaa4-7bda32022015 | -15.37606 | -48.60093 | 2025-10-03 04:14:00 | NPP-375D | COCALZINHO DE GOIÁS | GOIÁS | Brasil | 5205513 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c3b5995f-f93c-3d69-8d56-2b284ed9b734 | -15.22123 | -47.96025 | 2025-10-03 04:14:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| e597a29f-27e9-3739-a5f3-6f587598b6fe | -15.25077 | -50.13107 | 2025-10-03 04:14:00 | NPP-375D | FAINA | GOIÁS | Brasil | 5207535 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d6112872-53dc-3059-914f-10a9f3269b8b | -19.72396 | -45.87435 | 2025-10-03 04:14:00 | NPP-375D | LUZ | MINAS GERAIS | Brasil | 3138807 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d4451469-7721-3051-8daf-118d1a80e6c5 | -20.11811 | -44.39134 | 2025-10-03 04:14:00 | NPP-375D | MATEUS LEME | MINAS GERAIS | Brasil | 3140704 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 5affa012-f250-3a90-8577-fe2915b1c031 | -14.73416 | -50.04679 | 2025-10-03 04:14:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f5caaa05-f9df-35c6-b2fa-e5ee7b33eed9 | -19.71776 | -45.91193 | 2025-10-03 04:14:00 | NPP-375D | LUZ | MINAS GERAIS | Brasil | 3138807 | 31 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 4a07ab0b-001e-3985-ac1b-e931f200e6b1 | -14.8951 | -46.97423 | 2025-10-03 04:14:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ece5181c-a7a0-31b2-8398-1942b9721555 | -20.8761 | -44.74878 | 2025-10-03 04:14:00 | NPP-375D | OLIVEIRA | MINAS GERAIS | Brasil | 3145604 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 45443c92-0989-3f09-8fda-b0992948a815 | -14.97492 | -49.96705 | 2025-10-03 04:14:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| feb4c238-a1fa-3c91-8537-286a0d3977ce | -15.27978 | -47.9207 | 2025-10-03 04:14:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e04c36aa-ccd3-35cb-b03c-37e1130fcd92 | -19.72051 | -45.91629 | 2025-10-03 04:14:00 | NPP-375D | LUZ | MINAS GERAIS | Brasil | 3138807 | 31 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 7325e45d-706c-304d-a675-9e5a6a948ec2 | -15.30868 | -46.28272 | 2025-10-03 04:14:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ed6b8ca7-1519-38c5-8ac2-b1f030800b3e | -15.64921 | -46.25743 | 2025-10-03 04:14:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ada07b3b-cbe2-3dd7-b80f-913cf0c614ea | -15.25175 | -49.31544 | 2025-10-03 04:14:00 | NPP-375D | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 8e2a963e-a7a0-398f-b6e7-5fdd7abd04a2 | -15.52268 | -46.80213 | 2025-10-03 04:14:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 68b50f05-d5de-3cd1-8a75-2eeaa70521ff | -15.32423 | -46.29824 | 2025-10-03 04:14:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 6.6 |
| bd9d7f82-b61b-3cb1-b5f7-07d84f8ceaed | -14.88694 | -46.84698 | 2025-10-03 04:14:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 59b519d5-05d2-30b5-9d36-bb26ce0100b4 | -21.52243 | -46.0772 | 2025-10-03 04:14:00 | NPP-375D | SERRANIA | MINAS GERAIS | Brasil | 3166907 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| b72b5dc7-5af0-3e95-941d-4dd69b4219df | -19.04541 | -42.15471 | 2025-10-03 04:14:00 | NPP-375D | PERIQUITO | MINAS GERAIS | Brasil | 3149952 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 787427b0-019c-35d8-bdf1-c6560fd133a2 | -15.25125 | -49.29434 | 2025-10-03 04:14:00 | NPP-375D | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9bd4b077-8227-31fe-9767-6de86bf5ac13 | -20.01186 | -45.54414 | 2025-10-03 04:14:00 | NPP-375D | LAGOA DA PRATA | MINAS GERAIS | Brasil | 3137205 | 31 | 33 | nan | nan | nan | Cerrado | 0.3 |
| bef17ae4-53c7-374d-b2b8-cbf730ee72a3 | -15.25217 | -47.9201 | 2025-10-03 04:14:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 134a44ae-1aa0-3316-9b45-ccd3cada7327 | -14.62822 | -48.13326 | 2025-10-03 04:14:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b13d4426-aeb3-32c3-b019-467808581799 | -14.72383 | -48.11861 | 2025-10-03 04:14:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 06006db6-c823-3e70-8f21-95a00519534e | -14.93276 | -46.88621 | 2025-10-03 04:14:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d896a48e-a8ff-3301-a5bf-f86e4eba6c3e | -15.34973 | -47.06243 | 2025-10-03 04:14:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| bdb4b766-a415-38b9-8003-a40ea7f2b2f2 | -17.98174 | -45.01368 | 2025-10-03 04:14:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| be0a6abf-41e2-36dc-9e19-78d5210cfe68 | -19.72159 | -47.2183 | 2025-10-03 04:14:00 | NPP-375D | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f312fe18-1b78-3757-825d-c5d1eb37261f | -19.73556 | -45.88813 | 2025-10-03 04:14:00 | NPP-375D | LUZ | MINAS GERAIS | Brasil | 3138807 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 356fc914-9d4d-3837-a450-8e02167d78a0 | -14.9115 | -48.35241 | 2025-10-03 04:14:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 86346bd8-c598-3e37-819a-f9b78f69fd78 | -14.94323 | -46.90741 | 2025-10-03 04:14:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 4da14084-a360-3a08-a13a-d0f3d5e68110 | -21.00016 | -49.21636 | 2025-10-03 04:14:00 | NPP-375D | IBIRÁ | SÃO PAULO | Brasil | 3519402 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| 5248cc99-6527-3e8f-9ccc-5d8c43b7f097 | -17.27478 | -49.01005 | 2025-10-03 04:14:00 | NPP-375D | PIRACANJUBA | GOIÁS | Brasil | 5217104 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 60c4741e-1d09-39a0-bcd9-ff7aac286a44 | -17.19018 | -47.0154 | 2025-10-03 04:14:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a4b9c209-f162-3916-8339-b0915e3f023c | -16.29011 | -45.24659 | 2025-10-03 04:14:00 | NPP-375D | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 842f16ba-a4ac-3f2a-bcb7-ca09bb42219a | -15.58885 | -46.93735 | 2025-10-03 04:14:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 777c28ea-71b8-3332-87bd-10fb1a6c30d9 | -18.38972 | -45.46527 | 2025-10-03 04:14:00 | NPP-375D | MORADA NOVA DE MINAS | MINAS GERAIS | Brasil | 3143500 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 884ae587-b099-378d-a454-9ef4dade2f4d | -17.98602 | -45.02966 | 2025-10-03 04:14:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0126bd67-4784-36ea-9e30-d198712637c7 | -14.65058 | -48.12146 | 2025-10-03 04:14:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| bcb19a7e-cec3-3d3f-b591-ea772670ad86 | -15.23667 | -50.08551 | 2025-10-03 04:14:00 | NPP-375D | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 73a40af2-e19f-3e0b-a875-528f5b6c0846 | -17.17807 | -47.0216 | 2025-10-03 04:14:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |


[Clique aqui para ver as próximas entradas](README83.md)
