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

## Dados Diários - Página 64

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f71b001f-3b63-3cbb-ace2-036fbbb6870c | -9.41919 | -60.42698 | 2026-08-20 05:42:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 2dcd5071-249e-3826-b5d6-4c7ad83760c0 | -11.21238 | -55.05831 | 2026-08-20 05:42:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 13.8 |
| 932fe3da-7f5b-3d15-8eb2-31773b9d7085 | -8.56383 | -54.76717 | 2026-08-20 05:42:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9cf5d3ad-4803-388b-9616-f6bba7f39656 | -8.56255 | -54.66289 | 2026-08-20 05:42:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b47932e4-0ca5-3416-84e7-ee17252463c7 | -11.83605 | -58.8464 | 2026-08-20 05:42:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6a3514c4-6131-3551-bfe2-8fd83c80a350 | -6.74357 | -59.03842 | 2026-08-20 05:42:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 952f7224-14c3-33d7-badc-d5da4892e586 | -8.40417 | -62.69896 | 2026-08-20 05:42:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ac3ac5b6-af16-37a9-b0d2-a9fbfa6a7277 | -13.40541 | -54.37409 | 2026-08-20 05:42:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c9ae30d4-97b5-33b8-abfc-b8dd1187b7b4 | -6.95785 | -59.05008 | 2026-08-20 05:42:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| babdfbb7-373e-385f-b76b-f26b133f5724 | -8.04865 | -54.03053 | 2026-08-20 05:42:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 21ef8505-4113-3d55-9fd3-67bee1a41fc3 | -8.58287 | -54.77548 | 2026-08-20 05:42:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 81dc0a3a-1e8b-3a95-9919-716e7516f405 | -6.97602 | -59.5859 | 2026-08-20 05:42:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ddcc25d5-8cfc-34f4-8a0d-9a712136cfe2 | -9.11686 | -61.60564 | 2026-08-20 05:42:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 58e2af57-e87d-3bd6-9341-a10a37366539 | -8.28886 | -62.89441 | 2026-08-20 05:42:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ed664371-5ae3-357a-9d20-60639f03641d | -13.44622 | -51.42567 | 2026-08-20 05:42:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5e9e9ef2-6d1b-32fa-836b-8d43479d4ce0 | -10.3301 | -57.56679 | 2026-08-20 05:42:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5a26b085-137d-3000-b56c-424f4e36d5ee | -7.60909 | -60.95114 | 2026-08-20 05:42:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6e487e76-f94f-34f1-a896-afca2825d639 | -10.92356 | -57.17803 | 2026-08-20 05:42:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f0286838-9dbc-33c7-84a7-ecfde6c8baa8 | -9.15976 | -59.55405 | 2026-08-20 05:42:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d633e1a6-e8dd-39fa-a1b6-874b60ef10ff | -6.70294 | -58.93641 | 2026-08-20 05:42:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 124de3fb-b8f7-3343-b129-cf1a2556625c | -7.87136 | -63.76165 | 2026-08-20 05:42:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 316387d9-5717-3f21-822f-02470d719684 | -8.55403 | -54.79159 | 2026-08-20 05:42:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 94279728-2472-3482-bc3f-62041ad73c29 | -8.66693 | -54.64306 | 2026-08-20 05:42:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| d3fd4cf6-5c2a-3ac2-a0fa-8d5bb569842c | -13.40411 | -54.38448 | 2026-08-20 05:42:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 91f1fa2b-85ad-3078-9ea7-34d742011c2a | -9.21564 | -59.77717 | 2026-08-20 05:42:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 8a712064-ab11-3df9-9568-ac112a13f4a0 | -6.85675 | -59.02764 | 2026-08-20 05:42:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 404ea461-2461-3d8b-9f52-3dc939bb250e | -10.38374 | -61.21432 | 2026-08-20 05:42:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 51c70ce4-c531-3a53-a10a-628a353e6e2b | -8.6806 | -54.65152 | 2026-08-20 05:42:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b67ccc18-439e-3c70-96f1-096869d3f1c8 | -9.37037 | -58.95185 | 2026-08-20 05:42:00 | NPP-375D | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3ec19b3e-6975-34e0-a015-b6b2c4ed716f | -6.8035 | -59.58067 | 2026-08-20 05:42:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ae74847c-6e47-3103-8c48-95e44dbcdc87 | -10.38833 | -61.20729 | 2026-08-20 05:42:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 008920a1-46c4-3414-af41-8ad9ee70d873 | -9.22086 | -60.8129 | 2026-08-20 05:42:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7bac08ca-03eb-3870-aa9d-6c9135240764 | -11.21742 | -55.05899 | 2026-08-20 05:42:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 8.6 |
| e88f5b4e-efff-30fd-bcb5-ad58332357ea | -9.11742 | -61.60205 | 2026-08-20 05:42:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 9.3 |
| c26386d2-e03a-3810-b935-e66c79f457ce | -6.91933 | -59.34895 | 2026-08-20 05:42:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| f02dade5-4da5-3d46-82c3-f95c8575539d | -9.11405 | -61.60152 | 2026-08-20 05:42:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 9.3 |
| c85abed3-97dc-3b76-8e1c-5531d7960364 | -7.86475 | -63.74976 | 2026-08-20 05:42:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ba90b381-3551-3121-ba78-97bb68ad5873 | -10.78654 | -50.31087 | 2026-08-20 05:42:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| e3ac173e-7445-33ec-9786-3ef265fffb67 | -8.56014 | -54.79475 | 2026-08-20 05:42:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9d76f1d6-157a-3b05-b63a-e2e51ce96696 | -6.84772 | -59.01332 | 2026-08-20 05:42:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 508011e3-53e4-32f8-8c7e-2f824c77b4dc | -6.59782 | -58.96582 | 2026-08-20 05:42:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bfaa525f-12a0-3ccc-a3cd-7846d0eb335f | -7.86638 | -63.74985 | 2026-08-20 05:42:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6d0463ab-2cb3-37fa-acdc-1ac485f37385 | -8.95282 | -60.5819 | 2026-08-20 05:42:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 4d3d0976-3011-3d9f-9880-dd56e266a58d | -6.88539 | -59.03461 | 2026-08-20 05:42:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| db9f1da8-3758-31e5-acff-825a436893f3 | -9.42038 | -60.41911 | 2026-08-20 05:42:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 21781791-6ab0-3cbd-9e83-60b270db10ad | -7.37763 | -59.95155 | 2026-08-20 05:42:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0ad3f9df-8a56-358f-afcb-edb6ebbcfa0b | -8.56316 | -54.65494 | 2026-08-20 05:42:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ed25c780-34cc-3b99-a0a3-74d5d5d1ab9d | -8.53246 | -54.87333 | 2026-08-20 05:42:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 18ae5b13-f49e-3754-8530-4b574ab50e87 | -8.0339 | -54.02291 | 2026-08-20 05:42:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 4052fda9-a623-3656-998d-044176f34797 | -6.58429 | -58.98117 | 2026-08-20 05:42:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 896013dd-4cf4-3b45-8023-01117aa4a4f7 | -8.57793 | -54.77477 | 2026-08-20 05:42:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 28492db5-41c8-3f77-8c7b-2b9bd1443db5 | -8.52758 | -54.87246 | 2026-08-20 05:42:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9ebe9f0e-9426-3be3-a9a2-82a524e5b3ac | -8.5552 | -54.79407 | 2026-08-20 05:42:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6f0c03bc-85b2-3b3c-a103-bbe46789a01b | -7.05517 | -59.84535 | 2026-08-20 05:42:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 88cb9a2d-987f-364e-98e8-ee2e6f5d8f84 | -6.84406 | -59.01277 | 2026-08-20 05:42:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 51939e5b-574d-328a-b33b-94b104312365 | -11.20734 | -55.05764 | 2026-08-20 05:42:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 13.8 |
| 4c3395f0-b651-387e-83d1-f4a6ec2356c1 | -9.12416 | -61.60312 | 2026-08-20 05:42:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| eca27ed7-24af-39d7-8732-7ea0c9d286ee | -7.5497 | -55.59098 | 2026-08-20 05:42:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| cd348f8b-85e5-36ab-b8e8-9766691f4243 | -9.10182 | -60.92993 | 2026-08-20 05:42:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 86b0219f-86b3-3d40-8b28-a3d6249a2692 | -9.20778 | -59.78023 | 2026-08-20 05:42:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 4816bfd7-c404-3547-908a-153685785e14 | -9.08083 | -65.38764 | 2026-08-20 05:42:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| bb18b8a0-aa6f-381c-a2a3-992a420e0f9d | -11.1912 | -54.02186 | 2026-08-20 05:42:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a1b76a38-ea38-3503-94c6-7a46f221dcd5 | -6.58366 | -58.9854 | 2026-08-20 05:42:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.7 |
| cf26a5d0-6da1-3947-9485-541922883842 | -6.74956 | -59.04801 | 2026-08-20 05:42:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5ca07e62-e80f-3849-9ed7-2e4897e5f9bc | -8.57987 | -54.68045 | 2026-08-20 05:42:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f95a011a-d430-3709-8cec-59fcb9afc488 | -6.80558 | -59.01985 | 2026-08-20 05:42:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 659e560d-2088-33ea-838a-118f433eb534 | -9.00896 | -60.44786 | 2026-08-20 05:42:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 20c70540-2637-3cd0-a6bf-2144042b4e8b | -8.71759 | -49.61967 | 2026-08-20 05:42:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 10.6 |
| cdb126c5-eef5-3e1f-8905-52e81c000ce3 | -8.6695 | -54.66107 | 2026-08-20 05:42:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 5ed1d787-630f-3e06-ba87-10e5cccc8521 | -6.79283 | -59.57906 | 2026-08-20 05:42:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 38170440-f7e0-3993-98ca-4c6d3f318f8b | -13.44468 | -51.43147 | 2026-08-20 05:42:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 516a43f5-6ddb-33e7-8405-1d8856c0c6eb | -10.3803 | -61.2138 | 2026-08-20 05:42:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3fea2e97-9b3e-38e8-b101-7004a64ea6e1 | -7.00244 | -59.59692 | 2026-08-20 05:42:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 430b6897-7b17-3202-9eee-b2cab5c636d7 | -9.13079 | -51.15301 | 2026-08-20 05:42:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8f3f6ffb-3611-3dc5-97b2-41e55045db30 | -6.70967 | -59.08953 | 2026-08-20 05:42:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 1b9c6d99-46c8-3c1d-99c7-2fc180418762 | -7.60286 | -60.94641 | 2026-08-20 05:42:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e3ed3017-8d55-3095-8a9e-8fac5d5debdd | -6.80622 | -59.01559 | 2026-08-20 05:42:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 26748c30-416d-37d2-9967-43835e6f1170 | -9.41972 | -60.44716 | 2026-08-20 05:42:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 3559cde1-9982-3bc0-89aa-ccc78bb575bc | -6.71565 | -59.09908 | 2026-08-20 05:42:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 18301cfe-186a-3a10-8dcc-1e4e80716d05 | -8.04907 | -54.02745 | 2026-08-20 05:42:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 333f3487-a580-3494-bd2e-984e39a52b6d | -10.55839 | -56.33051 | 2026-08-20 05:42:00 | NPP-375D | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9437f331-4d0d-36b2-a04c-bf513a5bda22 | -7.83066 | -61.61447 | 2026-08-20 05:42:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6fff73c6-a8a6-3779-9a35-aaf3e36eefd4 | -6.58859 | -58.97747 | 2026-08-20 05:42:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8d950f12-2a42-3263-af93-4d1c0110b954 | -13.4426 | -51.81051 | 2026-08-20 05:42:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b9038570-5d04-373a-9432-08623866fd26 | -6.73992 | -59.03788 | 2026-08-20 05:42:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 060f75b2-3811-3ca2-a243-f0da9fd450bf | -6.71266 | -59.09432 | 2026-08-20 05:42:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 1ef23d17-f493-3908-a5d9-7918a5ac514b | -6.68656 | -59.09473 | 2026-08-20 05:42:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c3832b1d-7aae-3c91-878b-f84c5ecd6120 | -6.70046 | -59.10115 | 2026-08-20 05:42:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 396600b3-c0dc-34e6-8be4-9fae4ec0a955 | -10.33063 | -57.5629 | 2026-08-20 05:42:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e5b949dd-bb94-3d3d-be3e-60498a093288 | -6.59288 | -58.97375 | 2026-08-20 05:42:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a152ba8a-1e42-3b40-82bf-3f6543368ba8 | -9.2169 | -59.7688 | 2026-08-20 05:42:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 137bdb29-b855-3a75-baf5-854bbdc4da02 | -6.58191 | -58.97214 | 2026-08-20 05:42:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.2 |
| aff55e46-a9fc-324b-828f-755627b76db4 | -7.61136 | -60.95896 | 2026-08-20 05:42:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2a1cf39a-ceca-38b7-84b5-e3319ef33f6c | -13.63093 | -51.772 | 2026-08-20 05:42:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7e9dec5f-36f0-33da-b998-60f2c6ebb5fb | -7.82731 | -61.61394 | 2026-08-20 05:42:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 501a122f-f8c0-3a25-b6bf-4cd1ec2ea5f9 | -8.28775 | -62.90137 | 2026-08-20 05:42:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 1d6633ce-1146-3637-b247-a464bf3ded11 | -8.6769 | -54.64456 | 2026-08-20 05:42:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 47cea59c-8781-360e-84fe-becc03573562 | -11.82888 | -58.84026 | 2026-08-20 05:42:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7884003f-12e4-30c5-99df-cb8f95d11c3e | -6.84707 | -59.01754 | 2026-08-20 05:42:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5ea02f81-9a81-38fb-af41-fbd3f1b4f6b2 | -11.22401 | -55.04762 | 2026-08-20 05:42:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |


[Clique aqui para ver as próximas entradas](README65.md)
