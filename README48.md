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

## Dados Diários - Página 48

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 36f09cab-7777-3b53-aaa8-8e96b545b6f1 | -20.75544 | -45.39294 | 2025-10-08 04:19:00 | NPP-375D | CANDEIAS | MINAS GERAIS | Brasil | 3112000 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3cedbc62-a7de-3868-983c-353593c62cb1 | -7.80827 | -44.24008 | 2025-10-08 04:19:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0b720625-3259-34a3-bc72-00e952b38301 | -14.53154 | -46.64503 | 2025-10-08 04:19:00 | NPP-375D | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| fdbe5a80-e4d8-3107-9c3e-9a020a3b2e54 | -17.37773 | -45.05727 | 2025-10-08 04:19:00 | NPP-375D | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 70910ead-ec6c-32bb-8528-380a92d9ea17 | -17.13756 | -43.45904 | 2025-10-08 04:19:00 | NPP-375D | ITACAMBIRA | MINAS GERAIS | Brasil | 3132008 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bb26ffa0-45aa-3ad2-810b-af074741b689 | -17.55317 | -46.06989 | 2025-10-08 04:19:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b183b5b6-70fe-3372-9b06-f1190df58f3e | -8.55237 | -44.62829 | 2025-10-08 04:19:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c320d7e1-68fb-382b-80e1-b2cbcc545eb0 | -14.74554 | -47.86023 | 2025-10-08 04:19:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7797f06b-2055-393a-a864-92f5aac536ae | -15.77727 | -46.2524 | 2025-10-08 04:19:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 50c74930-017b-350e-835e-d69ad228d88b | -14.75262 | -47.86158 | 2025-10-08 04:19:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.3 |
| dc9c85bf-cc00-36b3-aedf-d0cdadea289c | -7.03203 | -47.90853 | 2025-10-08 04:19:00 | NPP-375D | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6ec1e2de-4df8-3c5e-aceb-372a67eed22d | -19.72218 | -43.9063 | 2025-10-08 04:19:00 | NPP-375D | VESPASIANO | MINAS GERAIS | Brasil | 3171204 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 814f1509-8d42-3850-bde9-11c5c2b5d120 | -8.56911 | -46.22851 | 2025-10-08 04:19:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c620db79-64be-30c6-b7fc-db38e15b3617 | -19.42756 | -49.58508 | 2025-10-08 04:19:00 | NPP-375D | CAMPINA VERDE | MINAS GERAIS | Brasil | 3111101 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c50b1bd0-186c-3682-91f7-3b22223cd8eb | -20.501 | -45.94496 | 2025-10-08 04:19:00 | NPP-375D | PIUMHI | MINAS GERAIS | Brasil | 3151503 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 8f90c452-0221-3872-82bd-3ed7e40ec78c | -8.8677 | -46.77434 | 2025-10-08 04:19:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| f7f0e081-c3b2-3f6d-8e7e-c8d66c47f2c5 | -14.69726 | -46.01387 | 2025-10-08 04:19:00 | NPP-375D | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 96617eb9-1c23-301b-9352-b7c08af6d7a5 | -18.02675 | -44.94191 | 2025-10-08 04:19:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 10335d33-d96f-3fca-9b57-678aa861d9ae | -15.31825 | -46.17109 | 2025-10-08 04:19:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 775ab42f-816a-30a0-b7fb-8b4a0a08b3cf | -21.30076 | -45.45524 | 2025-10-08 04:19:00 | NPP-375D | SANTANA DA VARGEM | MINAS GERAIS | Brasil | 3158300 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 60ee4f9e-073c-3714-82af-5b0efa167634 | -15.95037 | -42.6076 | 2025-10-08 04:19:00 | NPP-375D | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 11.6 |
| b3294a17-2cca-3d4f-8880-d0459b970708 | -14.95777 | -46.8365 | 2025-10-08 04:19:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 968b2a66-6b81-37c9-9b41-0d7583386a27 | -16.29462 | -45.24278 | 2025-10-08 04:19:00 | NPP-375D | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e6fca910-cbdb-32e0-a7a4-78db1a2cb374 | -8.26765 | -47.00774 | 2025-10-08 04:19:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2ec57ae3-824f-33e8-833c-996cf545eb0f | -17.1445 | -45.78846 | 2025-10-08 04:19:00 | NPP-375D | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 526fb3e7-e27e-34c6-a750-30f15a3fba0a | -8.39267 | -49.70722 | 2025-10-08 04:19:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 84e46eea-f5e8-3d49-9650-3919e0dcadc2 | -17.82714 | -57.63852 | 2025-10-08 04:19:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 12.4 |
| 5bd3d204-8346-316e-a0eb-c8ff0d3e2ced | -13.3186 | -48.02197 | 2025-10-08 04:19:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 16112a3f-ce6b-3dde-b761-c8552059ecf8 | -18.00998 | -44.97313 | 2025-10-08 04:19:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 95b12546-7b45-32ab-a111-c227ca7ddca3 | -13.75432 | -45.75172 | 2025-10-08 04:19:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9666d5ba-d3b1-32b1-a4ad-7922b1701556 | -19.26384 | -44.11815 | 2025-10-08 04:19:00 | NPP-375D | JEQUITIBÁ | MINAS GERAIS | Brasil | 3135704 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 528b33b5-7da8-35cd-8da2-3c06b5001036 | -8.58192 | -44.33524 | 2025-10-08 04:19:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 0.4 |
| d00b1def-d7da-3615-ac98-5faf6b2c4f3c | -17.82448 | -57.622 | 2025-10-08 04:19:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 6af1e627-9c6b-3bc6-9d0b-41a38a3616f8 | -17.28594 | -42.65355 | 2025-10-08 04:19:00 | NPP-375D | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 4.7 |
| c630a339-c252-3c33-8ccf-fe0236c65506 | -19.30427 | -43.76516 | 2025-10-08 04:19:00 | NPP-375D | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 35dcce2a-39f6-374f-bd87-9a6b153e6e8e | -13.80398 | -45.79699 | 2025-10-08 04:19:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d4591b44-b38d-363a-a04c-19dcd04fe14d | -15.79185 | -46.24748 | 2025-10-08 04:19:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1902dac8-5901-38f5-bc0e-62d83f45f625 | -9.98724 | -43.59729 | 2025-10-08 04:19:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9e0d631c-dae9-38f3-84a9-c3b285c8aa7a | -8.89898 | -47.66299 | 2025-10-08 04:19:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 11ee5305-d4a3-38bd-9374-1eec5a0fef88 | -17.28781 | -42.65552 | 2025-10-08 04:19:00 | NPP-375D | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 261681cf-3fb1-3d2c-9f89-029cc695484a | -13.75766 | -45.7523 | 2025-10-08 04:19:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| aa2f02c7-705b-36f7-b53c-3dd162a004a4 | -20.17196 | -42.20646 | 2025-10-08 04:19:00 | NPP-375D | CAPUTIRA | MINAS GERAIS | Brasil | 3112901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 854a8290-8277-36ad-81bd-47839e824ec6 | -14.24651 | -45.86722 | 2025-10-08 04:19:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4a9057b5-5d50-335f-9b85-1676acbbc979 | -15.06079 | -49.4855 | 2025-10-08 04:19:00 | NPP-375D | NOVA GLÓRIA | GOIÁS | Brasil | 5214861 | 52 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 00120a0a-2614-3aa1-984a-10053edd9b09 | -19.84928 | -46.15967 | 2025-10-08 04:19:00 | NPP-375D | TAPIRAÍ | MINAS GERAIS | Brasil | 3168200 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9231c59a-db90-3705-abf3-6579d0dba565 | -7.09664 | -48.29774 | 2025-10-08 04:19:00 | NPP-375D | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7a2a6cfa-83a4-38a7-aa72-c65914f5b843 | -9.32085 | -45.779 | 2025-10-08 04:19:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 904d1e25-1827-3895-85eb-04bacd82cdcc | -8.94943 | -46.59361 | 2025-10-08 04:19:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e46c295f-e058-3bd7-9a6b-cb3cb0da5cee | -20.29881 | -48.5163 | 2025-10-08 04:19:00 | NPP-375D | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 82526110-bebd-3553-8fbf-d027ec8cb10b | -15.38514 | -46.27584 | 2025-10-08 04:19:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 19ef9fad-ee5b-3795-9771-f1add2690ffd | -8.99609 | -40.41871 | 2025-10-08 04:19:00 | NPP-375D | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 1cebe54f-1593-3b41-91dd-0ea7b00ac6b6 | -8.41038 | -46.80584 | 2025-10-08 04:19:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4c9e5d22-cd57-310a-8d5c-62cc6d880d3d | -8.11682 | -47.25337 | 2025-10-08 04:19:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7f65df6a-d552-305f-bc30-725875806b99 | -15.60456 | -52.58148 | 2025-10-08 04:19:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3cf824a2-ff25-39e8-89f5-0366af1a460c | -15.70462 | -47.51275 | 2025-10-08 04:19:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 34c1d6fd-a31f-371f-8b8c-bb1d5080ba1b | -18.07047 | -44.46404 | 2025-10-08 04:19:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a32312e4-d4ff-35ce-9f0d-f56b0202f746 | -17.99488 | -44.98192 | 2025-10-08 04:19:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 35dd8062-73ac-3519-b30b-e6970a4277d6 | -14.24592 | -45.87083 | 2025-10-08 04:19:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 04919a5f-b06f-3be0-a4bb-4177b1ec494b | -7.80106 | -44.22086 | 2025-10-08 04:19:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d1c4fd1d-17b9-35a7-a35c-caae723f34aa | -9.0892 | -47.96114 | 2025-10-08 04:19:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 093ba0e4-ff80-38d8-8de5-06ea047ff4e3 | -20.19399 | -43.94587 | 2025-10-08 04:19:00 | NPP-375D | NOVA LIMA | MINAS GERAIS | Brasil | 3144805 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| e58d1a7e-4ec7-3226-be4f-bc03fcac1137 | -14.92987 | -46.7933 | 2025-10-08 04:19:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6e30172d-9e8a-373b-8b24-ad239ac38029 | -17.92484 | -57.51375 | 2025-10-08 04:19:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.2 |
| c20e8fb7-0806-396d-a8fd-d82da8749a39 | -17.56824 | -46.06129 | 2025-10-08 04:19:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5296f88c-a079-3ffc-8c5b-241a6064e830 | -14.71561 | -46.02831 | 2025-10-08 04:19:00 | NPP-375D | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f70a7114-29ad-3e6c-9e3e-cf1382db245a | -8.68146 | -44.72186 | 2025-10-08 04:19:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 70b88c36-5dc8-3526-966d-e27d665e63d9 | -14.742 | -47.8596 | 2025-10-08 04:19:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| bfed3e4d-6cd8-3067-a4d7-c9afdbacf532 | -17.55709 | -46.06681 | 2025-10-08 04:19:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 155688ca-5fdb-330f-9725-7bccf05269f3 | -16.14076 | -48.24231 | 2025-10-08 04:19:00 | NPP-375D | SANTO ANTÔNIO DO DESCOBERTO | GOIÁS | Brasil | 5219753 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 76e037d2-1938-3d88-89cb-647ac0c59dd9 | -8.23647 | -44.18589 | 2025-10-08 04:19:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 7db7636d-30db-3e63-91fb-97689b0995e9 | -8.9684 | -47.48163 | 2025-10-08 04:19:00 | NPP-375D | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6a888be9-6d49-359e-b9e6-ab2d7a9211f0 | -9.39466 | -45.94597 | 2025-10-08 04:19:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 23d21530-3564-3a75-81c4-69e00ed76cb8 | -8.55721 | -46.23476 | 2025-10-08 04:19:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e5cccff6-ea99-3506-a40e-5300c2a2fba3 | -8.19027 | -43.34769 | 2025-10-08 04:19:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 8.8 |
| 427d941d-4adf-3f50-9240-1fbef61ae3ab | -16.00457 | -50.82421 | 2025-10-08 04:19:00 | NPP-375D | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 52c7d37b-e211-3d9b-9f7d-28d07db51de5 | -8.2259 | -44.18778 | 2025-10-08 04:19:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7a0d74c2-7aa3-3f71-a10a-63f462bddf3e | -8.89049 | -46.03058 | 2025-10-08 04:19:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 71d8c661-8d56-3454-941e-7c30b7902075 | -15.38367 | -47.31786 | 2025-10-08 04:19:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 607a48a4-ddb5-37d2-b68a-4af4d0a2afce | -20.26362 | -43.63837 | 2025-10-08 04:19:00 | NPP-375D | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 52c14eb1-5df8-34dd-bc84-abfbd66218b0 | -20.50167 | -46.99268 | 2025-10-08 04:19:00 | NPP-375D | CÁSSIA | MINAS GERAIS | Brasil | 3115102 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| fc41db5e-8382-30f5-b91b-22454c976df5 | -15.30637 | -46.37241 | 2025-10-08 04:19:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d9df09c2-b35c-3c1f-aecb-a71cefb4f80b | -9.20927 | -47.84342 | 2025-10-08 04:19:00 | NPP-375D | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 3e751c14-0941-3b28-a1ef-c8836ed8edc0 | -17.96471 | -44.97691 | 2025-10-08 04:19:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ccf267c7-3193-3040-9ed5-ee2543a2b76c | -14.29105 | -44.75857 | 2025-10-08 04:19:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2ddef768-23d7-3c45-a6ab-009c7bbf4f38 | -16.59523 | -46.55056 | 2025-10-08 04:19:00 | NPP-375D | NATALÂNDIA | MINAS GERAIS | Brasil | 3144375 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| cb81c8d8-318c-35db-97e8-13106c94d920 | -20.42138 | -42.88757 | 2025-10-08 04:19:00 | NPP-375D | PONTE NOVA | MINAS GERAIS | Brasil | 3152105 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| e9a519ab-4189-3918-8c76-501bebd0d764 | -13.29822 | -48.03147 | 2025-10-08 04:19:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 123faa34-d317-37da-bcf7-dc8c02fafa0e | -20.12451 | -44.42127 | 2025-10-08 04:19:00 | NPP-375D | MATEUS LEME | MINAS GERAIS | Brasil | 3140704 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 50b94f24-96fb-3a58-9237-74f7a85ac2d2 | -18.02619 | -44.94559 | 2025-10-08 04:19:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9334ab12-b7c3-33f4-b27c-eaba5b01559b | -8.97214 | -47.48228 | 2025-10-08 04:19:00 | NPP-375D | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8a59f437-0bb2-3715-9952-66b5a8fc57b7 | -8.5199 | -46.24107 | 2025-10-08 04:19:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 4c1aa8bf-b824-3b7f-baef-2180f18fdaf6 | -18.62333 | -46.61777 | 2025-10-08 04:19:00 | NPP-375D | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0ff16fa5-abfb-3f09-b0a5-b0b907c37a85 | -19.71522 | -43.90506 | 2025-10-08 04:19:00 | NPP-375D | VESPASIANO | MINAS GERAIS | Brasil | 3171204 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| aaacd936-e2a1-334e-9be6-440c23266757 | -8.66805 | -44.71956 | 2025-10-08 04:19:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 62b59289-b9bf-3beb-bcff-6b16e373f588 | -16.33679 | -47.05719 | 2025-10-08 04:19:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 94ca5693-e1ff-3f7b-b7c8-533bb3c5cb54 | -14.72247 | -46.03649 | 2025-10-08 04:19:00 | NPP-375D | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 01019243-693c-3500-bfe0-ee63723b7343 | -17.26009 | -46.79823 | 2025-10-08 04:19:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 563d4ddc-a9d5-38e7-9f84-cc703cb90a6d | -16.13247 | -47.91013 | 2025-10-08 04:19:00 | NPP-375D | CIDADE OCIDENTAL | GOIÁS | Brasil | 5205497 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| eca30ed4-c189-3bb0-b7d8-b7b6df7ce29c | -15.06549 | -49.48135 | 2025-10-08 04:19:00 | NPP-375D | NOVA GLÓRIA | GOIÁS | Brasil | 5214861 | 52 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 01125284-bd59-39d5-870f-94271daaa99a | -17.97533 | -44.97488 | 2025-10-08 04:19:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 4.7 |


[Clique aqui para ver as próximas entradas](README49.md)
