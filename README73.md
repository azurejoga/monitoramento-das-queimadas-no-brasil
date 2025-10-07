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

## Dados Diários - Página 73

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 426e771a-76dd-3c22-bdd9-b0f5b38a1469 | -13.24791 | -47.1723 | 2025-10-07 04:38:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 814430ab-99a6-3bb3-91bf-aa4a11cc7ac9 | -13.78632 | -50.78733 | 2025-10-07 04:38:00 | NPP-375D | NOVA CRIXÁS | GOIÁS | Brasil | 5214838 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a1582181-edc9-3de2-9ad6-e39801559e9b | -14.31643 | -49.46164 | 2025-10-07 04:38:00 | NPP-375D | PILAR DE GOIÁS | GOIÁS | Brasil | 5216908 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 06dbc36d-ddd8-338c-9c9d-54cbb6919dd5 | -15.17521 | -45.731 | 2025-10-07 04:38:00 | NPP-375D | CHAPADA GAÚCHA | MINAS GERAIS | Brasil | 3116159 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0875a7f2-98db-35a6-b7c4-90ca5c304741 | -13.33755 | -48.02825 | 2025-10-07 04:38:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| afff7a60-07d8-39f0-92bb-253d730334cb | -15.38228 | -47.98549 | 2025-10-07 04:38:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 77bfcfaa-6657-34fa-8201-2bcd37161705 | -14.96673 | -49.95307 | 2025-10-07 04:38:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 992ed217-f839-3434-b6b8-f9ff20046214 | -18.51803 | -43.91101 | 2025-10-07 04:38:00 | NPP-375D | GOUVEIA | MINAS GERAIS | Brasil | 3127602 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8cb394cb-c1dc-3429-a1a1-4409408bfba7 | -9.60721 | -57.14227 | 2025-10-07 04:38:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 633ef62d-f6a4-3077-a019-8c02fe3a816c | -16.00742 | -50.82946 | 2025-10-07 04:38:00 | NPP-375D | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f428bfd9-83dc-3f66-921f-09821da0d654 | -15.60514 | -42.37443 | 2025-10-07 04:38:00 | NPP-375D | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 534b7619-4b9f-3aad-96d8-15ba109b7d62 | -16.02211 | -51.04471 | 2025-10-07 04:38:00 | NPP-375D | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 17460bab-4f69-3f4b-8035-3f728769c23b | -13.34398 | -47.18166 | 2025-10-07 04:38:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 7610d54b-c579-3a97-8b5b-0eca15463150 | -15.57977 | -52.54897 | 2025-10-07 04:38:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| e7864f01-e91b-3ed1-b620-56a82e751fc0 | -11.86881 | -56.88865 | 2025-10-07 04:38:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 69ae5246-3adf-3ccc-a06d-d8ad1f704d21 | -14.97062 | -49.95005 | 2025-10-07 04:38:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a8ce28c3-c5e7-3866-a780-c60aa35a8b9d | -11.67364 | -46.34314 | 2025-10-07 04:38:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 318e7f8a-3e2b-3ccb-b4c4-e1cf8ea1b23f | -14.91056 | -46.85403 | 2025-10-07 04:38:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 0ba9929d-bbaf-3222-bbc0-2ef8fd0198d0 | -15.20516 | -46.37675 | 2025-10-07 04:38:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| bd9f2214-c3ed-3301-8d58-b7951a6a917b | -15.4998 | -47.92006 | 2025-10-07 04:38:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 8f4aa13e-c791-398e-99b6-1e673f97e6bf | -12.94442 | -54.72596 | 2025-10-07 04:38:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 51722fd0-b41a-368a-b850-2e2e6de6904b | -12.06485 | -51.20539 | 2025-10-07 04:38:00 | NPP-375D | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bf33b58c-2e06-37f0-ba24-21bb98fa3a8f | -15.36159 | -47.30212 | 2025-10-07 04:38:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 2a17e425-6d9a-373d-b400-251234aaf276 | -11.15544 | -47.75071 | 2025-10-07 04:38:00 | NPP-375D | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 56f83889-c7f9-3da2-9d21-4b673b01e5dc | -13.058 | -48.71321 | 2025-10-07 04:38:00 | NPP-375D | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9f94facb-48a8-32c8-ac1f-5da8b73ea301 | -11.15432 | -54.88097 | 2025-10-07 04:38:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 1a532594-2774-3f70-af72-e738f42b92da | -13.02536 | -51.03556 | 2025-10-07 04:38:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9ead3de8-c2b2-3577-8806-be54bb69b1c7 | -14.74217 | -46.03237 | 2025-10-07 04:38:00 | NPP-375D | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 39.8 |
| 618d74c1-b323-3668-a406-da06e4284f75 | -16.0148 | -51.04724 | 2025-10-07 04:38:00 | NPP-375D | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 2c7311a3-5f3e-3717-8b3e-98ae214c8398 | -12.8996 | -54.74034 | 2025-10-07 04:38:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 13.3 |
| eb68b2f3-68fb-3eea-b00a-2b6ed7757e5f | -11.02537 | -50.91827 | 2025-10-07 04:38:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 9.5 |
| ad71eedd-7fda-35c6-bfcc-8cfd98b5be9f | -11.85713 | -44.93376 | 2025-10-07 04:38:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a5f63a92-481c-33a9-80fb-69af910ee8ea | -10.42871 | -50.33448 | 2025-10-07 04:38:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0791a3b1-b504-3f91-9dd1-8ac3751676f3 | -14.70352 | -46.00817 | 2025-10-07 04:38:00 | NPP-375D | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 009caaee-adc6-3c63-ab20-c88316912842 | -11.26006 | -47.77433 | 2025-10-07 04:38:00 | NPP-375D | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f24d6b1c-d60d-38d9-a5ac-dcecfbbed4c4 | -16.04694 | -50.9554 | 2025-10-07 04:38:00 | NPP-375D | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2896497b-5573-3d16-aad4-9339f59a76b6 | -11.23363 | -47.76633 | 2025-10-07 04:38:00 | NPP-375D | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6950f593-22b6-32fa-aa3b-40fbecb945ae | -12.9819 | -46.78387 | 2025-10-07 04:38:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| bcf06300-ec46-339f-b258-4d3b9963b682 | -14.73785 | -46.00866 | 2025-10-07 04:38:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b400d427-3315-3f9d-a936-008110fbc820 | -12.15757 | -50.89132 | 2025-10-07 04:38:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 85726b92-614f-3d42-b6a6-b2d3654c9edc | -11.77195 | -45.13052 | 2025-10-07 04:38:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8ff2b4ff-c10a-3522-b66f-e56f1870fac0 | -11.7802 | -45.12706 | 2025-10-07 04:38:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6cd308dc-2c0d-3976-9100-f50691f583d6 | -11.15961 | -47.94715 | 2025-10-07 04:38:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4d050b59-6cfe-33ef-88b2-75e49d9e13b4 | -16.35394 | -47.04896 | 2025-10-07 04:38:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0c41056f-1501-3f5e-b4d9-b1bebad97e18 | -12.93283 | -54.71994 | 2025-10-07 04:38:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| de50d7a0-dcaf-3e41-aeb5-3e78b2e0bde8 | -10.67749 | -54.69116 | 2025-10-07 04:38:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 156aa616-195c-3ce8-bb7b-a4c3e136a1b1 | -11.86484 | -44.93472 | 2025-10-07 04:38:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6ac12808-6ebd-37a7-a864-3d7f474cb69a | -13.37253 | -47.234 | 2025-10-07 04:38:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 5ce0df4d-2613-3749-8aea-785bf12e15d1 | -16.29453 | -50.99799 | 2025-10-07 04:38:00 | NPP-375D | ISRAELÂNDIA | GOIÁS | Brasil | 5210307 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 066cb2d1-4d9e-39ad-86e2-1ce6aa7843e2 | -13.217 | -47.81177 | 2025-10-07 04:38:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f92822c0-64ee-39cb-83c5-4abef85f9adf | -12.90435 | -54.73745 | 2025-10-07 04:38:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| a93c88fc-72b0-37d7-8a96-b0ef3e481497 | -14.69733 | -48.39046 | 2025-10-07 04:38:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0cdb3f67-15db-32cb-9bda-d3e76dbe23e9 | -15.50193 | -46.8273 | 2025-10-07 04:38:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7d6df146-2964-308a-835a-84c573d424d8 | -11.04809 | -50.9213 | 2025-10-07 04:38:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| aac0c4d9-7c72-3e64-a6ba-b4d1102a8e76 | -11.79872 | -45.05268 | 2025-10-07 04:38:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3db50368-a28c-3246-ace7-c60b26a4e0da | -13.10324 | -47.9849 | 2025-10-07 04:38:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5b667a72-20db-3820-afdb-4cc97134dbfd | -13.86095 | -44.41661 | 2025-10-07 04:38:00 | NPP-375D | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 6253e1cf-157a-333b-8d3a-eafbba1cc773 | -14.77076 | -46.04625 | 2025-10-07 04:38:00 | NPP-375D | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 44c54029-2370-3375-ac8d-adcf1b5287f9 | -13.02999 | -51.0287 | 2025-10-07 04:38:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 8576aa6e-3e58-30cb-b112-d75dff12a880 | -15.60346 | -47.29609 | 2025-10-07 04:38:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bd946e71-63c6-3861-a883-b7816a35d6b2 | -13.09481 | -47.99457 | 2025-10-07 04:38:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e764e5e6-2380-37ca-a069-0624e6e25553 | -10.38598 | -50.29725 | 2025-10-07 04:38:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e59d85ae-ddcf-31c1-9f03-b3bbdee007f3 | -13.071 | -47.87682 | 2025-10-07 04:38:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 352eff85-a4b9-31b3-8fdd-96c8c1b2e636 | -10.99207 | -51.21474 | 2025-10-07 04:38:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f2c2b5f4-8d51-33c4-9810-b341792283bb | -14.76264 | -46.04966 | 2025-10-07 04:38:00 | NPP-375D | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 7.3 |
| e54bae64-d371-315f-b643-3704a0c52b89 | -10.61597 | -48.70027 | 2025-10-07 04:38:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c4e84760-8d55-368d-b744-079c6a401c06 | -13.58053 | -48.14837 | 2025-10-07 04:38:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 923c6ce6-419d-3424-98f0-4bb67c46a5c9 | -14.96949 | -49.9572 | 2025-10-07 04:38:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7c29ee70-cba5-38fe-b6f7-9215d8155f3c | -14.56214 | -48.95319 | 2025-10-07 04:38:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 78aea32d-b2fd-373d-8ffa-3cba0f80398b | -10.52588 | -58.03367 | 2025-10-07 04:38:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| a915321b-d50d-3002-9569-eeecca56893a | -10.81114 | -48.8141 | 2025-10-07 04:38:00 | NPP-375D | FÁTIMA | TOCANTINS | Brasil | 1707553 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e37b1ced-9459-364f-b76a-9db94b45918f | -13.39538 | -47.57761 | 2025-10-07 04:38:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4748deaf-95c7-34a4-af6b-033440cd86e9 | -11.72254 | -44.44294 | 2025-10-07 04:38:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c32d2d25-1dfd-38bc-b359-feac86a610d9 | -13.23979 | -51.6842 | 2025-10-07 04:38:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 17b3f77f-c65f-355c-b844-bb811dea9003 | -11.06323 | -47.93977 | 2025-10-07 04:38:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2047af48-55dd-38c1-bdd3-2e0f26e03974 | -12.36463 | -54.16643 | 2025-10-07 04:38:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 0c2dfa31-48f8-3200-8bb6-9aec3981f313 | -15.88238 | -46.25518 | 2025-10-07 04:38:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 42c87be1-ee27-39a5-b51f-ae8ac4f22191 | -11.1557 | -47.95021 | 2025-10-07 04:38:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 28d7ec96-de41-35f1-90e2-bbcd3d3e5524 | -14.73722 | -46.01317 | 2025-10-07 04:38:00 | NPP-375D | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 3e42eb34-cf4a-3b6b-85fb-d10c152e9e1b | -14.9093 | -46.86979 | 2025-10-07 04:38:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 7156ff62-4917-35e6-848e-26e2388a61f2 | -14.9272 | -46.79559 | 2025-10-07 04:38:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 0d75e7e3-87ab-327c-9840-f6edbb01e191 | -9.39556 | -61.43858 | 2025-10-07 04:38:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c61517db-0556-30a4-b5fb-07dbc681a86f | -14.93322 | -51.44068 | 2025-10-07 04:38:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 33d54674-36c8-39ff-8208-7351b04f691d | -10.45357 | -50.41798 | 2025-10-07 04:38:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 6712321c-d287-3149-be99-136dbbb029ff | -14.93668 | -46.80664 | 2025-10-07 04:38:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| fed148bd-967f-3e25-a63a-26b38a5f04b0 | -13.27932 | -48.47946 | 2025-10-07 04:38:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5294a405-da93-3e4f-949d-9983707b5989 | -10.40574 | -50.30429 | 2025-10-07 04:38:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 20.7 |
| df43a77c-b980-3ecd-971a-0830d439fb67 | -13.32794 | -47.5578 | 2025-10-07 04:38:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a2645bac-24c1-32f7-9396-070b577977fc | -15.58329 | -52.54952 | 2025-10-07 04:38:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| cb9a6ec4-be14-30f2-a445-20f1b4b2343c | -14.73221 | -46.02167 | 2025-10-07 04:38:00 | NPP-375D | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 67dd8391-9de5-3f35-9705-0650d94d9d37 | -10.80827 | -48.59374 | 2025-10-07 04:38:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e8fe8279-810e-358f-84c3-f9e511b0ea55 | -17.08822 | -43.37797 | 2025-10-07 04:38:00 | NPP-375D | ITACAMBIRA | MINAS GERAIS | Brasil | 3132008 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9184343c-67f1-3929-8f44-758d65bee4b4 | -10.88007 | -47.22754 | 2025-10-07 04:38:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4533ec75-b331-3647-8029-b523b58013cf | -15.37156 | -47.30811 | 2025-10-07 04:38:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 08c224f5-cd52-3913-97b1-d37579b76b87 | -15.19357 | -56.82076 | 2025-10-07 04:38:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6765367c-5a00-3b11-a916-3679bde9867f | -13.28397 | -48.05729 | 2025-10-07 04:38:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 43e39093-c376-3224-846d-1f12c6f4792d | -15.58266 | -52.57457 | 2025-10-07 04:38:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 8441e1ce-2005-3e52-af8e-a34ee407bd4a | -12.41667 | -50.26542 | 2025-10-07 04:38:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2ca00f79-bb4c-307c-81cb-67a54bbb117f | -16.11224 | -48.94231 | 2025-10-07 04:38:00 | NPP-375D | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 48ca4ef8-cd32-3675-b5de-cc9200a077a6 | -13.72204 | -48.06399 | 2025-10-07 04:38:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |


[Clique aqui para ver as próximas entradas](README74.md)
