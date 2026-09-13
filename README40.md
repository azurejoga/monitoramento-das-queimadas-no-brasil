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

## Dados Diários - Página 40

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 594b9640-9fe4-367e-854e-0794ff1b8f55 | -10.96026 | -58.95761 | 2026-09-13 04:51:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b1e94918-31e5-38dd-adfe-6a25bc98c664 | -10.68889 | -54.15538 | 2026-09-13 04:51:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 12.3 |
| a87e59df-1196-3c40-a893-363ee5b429a2 | -8.05752 | -54.84534 | 2026-09-13 04:51:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 31a9844e-5cb4-3dae-8351-b48e399b9ff2 | -7.87123 | -54.7229 | 2026-09-13 04:51:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9c8ce501-ee85-32b8-82f1-8e8307462894 | -9.94587 | -48.50547 | 2026-09-13 04:51:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5145b27f-004a-317d-b6c0-3a92b0a2fac4 | -12.17934 | -44.01844 | 2026-09-13 04:51:00 | NPP-375D | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 11a0f1fa-d775-39cd-a9da-deaf69765af5 | -9.37156 | -50.10026 | 2026-09-13 04:51:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 3e6bde6b-fdd1-3dd5-bc4c-cc4aeafc892f | -13.30802 | -51.72047 | 2026-09-13 04:51:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0dde755f-4c47-3344-870d-09b299585080 | -10.58484 | -51.35904 | 2026-09-13 04:51:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 444c02dc-be54-34a0-8afb-a34231a8d78a | -10.2573 | -57.70388 | 2026-09-13 04:51:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5fa10156-6b0b-3085-b9b4-9e7f47b110fb | -10.68658 | -54.1688 | 2026-09-13 04:51:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| eed0de42-4844-3456-8f23-53cb5fd5d13d | -11.82721 | -46.39848 | 2026-09-13 04:51:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 43193e1f-59a3-367d-8ca7-41f5de81b0cb | -13.60899 | -47.87304 | 2026-09-13 04:51:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| bf7301bb-a707-3c7a-bbcb-30c2b6b28467 | -13.46242 | -48.49239 | 2026-09-13 04:51:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 79d02ae3-ee9a-39c9-a162-e5fc877b5099 | -13.60835 | -47.87732 | 2026-09-13 04:51:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| d3ea0dd9-5e99-3f00-a1bd-d8ba5efee1f1 | -10.90123 | -47.81747 | 2026-09-13 04:51:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 71fcea29-a792-3d7d-995a-903273730407 | -10.93823 | -48.35589 | 2026-09-13 04:51:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| cb95e62e-aafc-34bb-af6e-715df711ab97 | -9.17578 | -59.62646 | 2026-09-13 04:51:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8aec1d36-ff90-385e-bf3c-cb4b7cca204c | -10.51564 | -57.45667 | 2026-09-13 04:51:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 6a7a31c2-ec96-33f0-9f77-55013766f185 | -13.38484 | -48.00897 | 2026-09-13 04:51:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| cf750825-11de-305e-bb0a-0b8fa9d7ae0c | -10.6926 | -54.15604 | 2026-09-13 04:51:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 12.3 |
| dd17d0fa-d725-3f80-8279-dae0f5e57285 | -11.57623 | -46.98838 | 2026-09-13 04:51:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 10.6 |
| f666b82e-19f3-3453-bf7d-5f49e2fd3ebe | -6.38016 | -58.29567 | 2026-09-13 04:51:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 40f73a0f-1dfd-361c-a77f-5adf6cdba067 | -6.96296 | -59.74857 | 2026-09-13 04:51:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 2bd9f0d0-7878-341e-9414-a87f894e864e | -8.04947 | -54.84389 | 2026-09-13 04:51:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 24cfb0b3-ec81-350d-9dec-a21bace12e2f | -10.96093 | -48.35481 | 2026-09-13 04:51:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 5744626a-d78d-37a3-881d-a09c60385cbc | -7.60168 | -46.11296 | 2026-09-13 04:51:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e0e90d16-b6d3-34ed-ae23-f7537ba3e6a6 | -7.86889 | -54.71259 | 2026-09-13 04:51:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d67c1c70-fe63-3ce7-b096-f98826ceb292 | -11.24964 | -54.13498 | 2026-09-13 04:51:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2a3bb5b5-7174-310d-aacb-90844b00604b | -7.86489 | -54.71193 | 2026-09-13 04:51:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 743bf3a0-d7de-3fc2-b07f-437db91bb6c1 | -6.60639 | -58.85863 | 2026-09-13 04:51:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 652bc41b-fe4c-3c58-af2e-88f0efb40ce9 | -10.69324 | -54.17464 | 2026-09-13 04:51:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 6.1 |
| adf7ac1d-a3dd-3c98-be1c-d78f4c398db0 | -10.58541 | -51.35545 | 2026-09-13 04:51:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b950e80b-188d-3cfc-95cc-232acabaeeb8 | -6.74205 | -55.64263 | 2026-09-13 04:51:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 6b5f9a2e-3a53-3d01-9da5-7dfb2e0a804c | -8.03098 | -54.85528 | 2026-09-13 04:51:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5c9c8cbb-ad7e-324e-af68-4d7a1284fd52 | -12.1552 | -48.96134 | 2026-09-13 04:51:00 | NPP-375D | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 432f9462-95a2-3c88-a442-67fa5544cb90 | -11.23858 | -54.13299 | 2026-09-13 04:51:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 267f9e9c-1453-3e32-a27c-dc29e9e1728c | -7.24751 | -46.70396 | 2026-09-13 04:51:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4edfa2e0-9cdc-3a62-9545-34e4582a4878 | -10.52227 | -47.89664 | 2026-09-13 04:51:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2218aa54-8ee1-3b74-a9a4-75a48ae69bff | -6.28583 | -59.9332 | 2026-09-13 04:51:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 404044ee-e021-343d-8c22-bf59025368c1 | -11.72456 | -46.73843 | 2026-09-13 04:51:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3ee74149-5d29-368b-b4a2-67670bee4bad | -10.09375 | -48.85723 | 2026-09-13 04:51:00 | NPP-375D | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 32ccf8da-823b-3f0a-b1b6-ccf1b9f88722 | -10.28771 | -55.06326 | 2026-09-13 04:51:00 | NPP-375D | TERRA NOVA DO NORTE | MATO GROSSO | Brasil | 5108055 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 69828ecc-5eac-3d9a-9ccb-6e03227078ea | -6.59811 | -58.84289 | 2026-09-13 04:51:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c87e3f78-11f2-3461-bafa-48710f90434e | -12.85556 | -44.38856 | 2026-09-13 04:51:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 24f8654a-81d8-3bbe-90db-fcb55c8c3797 | -8.28382 | -39.96839 | 2026-09-13 04:51:00 | NPP-375D | PARNAMIRIM | PERNAMBUCO | Brasil | 2610400 | 26 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 5b068790-fbd2-33d4-bd53-3ca5b3655722 | -11.31329 | -48.54449 | 2026-09-13 04:51:00 | NPP-375D | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 0310ea0d-5c7c-35a9-950d-c12b20dff193 | -12.66726 | -54.71403 | 2026-09-13 04:51:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 461225f0-dae4-3729-8e2c-56086724ffe2 | -6.61718 | -58.86063 | 2026-09-13 04:51:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7a9388d9-b812-336e-b3f6-8e53702df7d0 | -7.42368 | -55.52882 | 2026-09-13 04:51:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7beaea2d-ae70-3b91-937b-f0ca1ce27d46 | -10.06206 | -48.76953 | 2026-09-13 04:51:00 | NPP-375D | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 40676cb0-480e-3f2b-a336-f7352bdc9daf | -12.66646 | -54.71859 | 2026-09-13 04:51:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 15af024b-7909-32ba-944b-2e79305b177a | -6.29962 | -59.9572 | 2026-09-13 04:51:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e9658348-8ac8-31de-b14c-c58a05861829 | -11.23499 | -54.10976 | 2026-09-13 04:51:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c0504e66-cb5b-3eba-b8a8-6c2d523bb047 | -13.29743 | -51.72236 | 2026-09-13 04:51:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2bba6014-43af-3cae-9cd8-5fedc87c1630 | -13.3426 | -51.79588 | 2026-09-13 04:51:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1aab4f22-c67a-3abe-be29-fa1af36a6d90 | -6.60565 | -58.85534 | 2026-09-13 04:51:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0ba7f971-b0ae-35cd-93ee-1f1b1d6e2d07 | -10.50469 | -51.30174 | 2026-09-13 04:51:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a282cd98-0f26-310f-ae92-d44264100f44 | -8.04366 | -54.85384 | 2026-09-13 04:51:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c9afe9e6-4131-3b98-ad98-5b0437c26f33 | -10.94198 | -47.90448 | 2026-09-13 04:51:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0c34dbb6-a867-32fe-a487-90710b0816c7 | -7.76684 | -46.69037 | 2026-09-13 04:51:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 9a1ccf76-f507-3b04-b6cf-8791e11c0203 | -6.73845 | -55.63766 | 2026-09-13 04:51:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 29e4850c-4e43-3ef1-90e7-42f74cc16e36 | -6.37962 | -58.29883 | 2026-09-13 04:51:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b7537654-55a2-39e7-8fc3-b158c29ad191 | -13.38426 | -48.01296 | 2026-09-13 04:51:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9814f3ce-5f4f-3b58-a621-509f8adfe230 | -8.97846 | -44.393 | 2026-09-13 04:51:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 803db404-83d1-3b86-a9c6-ed872b4e0970 | -10.63577 | -46.00842 | 2026-09-13 04:51:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a31416e3-86a8-3fc4-8c2b-bec363d1c706 | -6.19206 | -57.71629 | 2026-09-13 04:51:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 64374c93-65c4-37ea-b5b5-90bd01dc7902 | -13.45596 | -48.48724 | 2026-09-13 04:51:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 58ec3205-447f-3708-8ea5-a11787037a4f | -13.6126 | -47.87373 | 2026-09-13 04:51:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| ad148370-83c5-3bca-9dfe-3a0fd5943795 | -10.54475 | -45.20419 | 2026-09-13 04:51:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9fed1473-2277-345d-b8c3-960e091bdbe2 | -11.24519 | -54.13874 | 2026-09-13 04:51:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d334906a-cdef-3f27-9969-7a6b870086ca | -7.86397 | -54.71722 | 2026-09-13 04:51:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f874ea26-df3a-3737-b463-ca6aef773872 | -9.75035 | -48.18814 | 2026-09-13 04:51:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 73b6ee7a-b85d-38d6-9371-b086ea3fd331 | -8.63557 | -47.35348 | 2026-09-13 04:51:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 7905fb59-91fd-3997-aa70-c0a39c20a3b2 | -11.43186 | -45.1488 | 2026-09-13 04:51:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6bd15293-ebb0-32b2-a9f4-7a114f2693eb | -6.59783 | -58.86829 | 2026-09-13 04:51:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a7277446-4397-3e70-87d7-cb116fa1128b | -13.60348 | -47.88317 | 2026-09-13 04:51:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 5710fc6f-8f11-37c8-9d4c-e1d26462c4f8 | -13.48483 | -48.48736 | 2026-09-13 04:51:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 365f54b7-40d0-3761-933f-0e5bad219c86 | -5.96702 | -57.77192 | 2026-09-13 04:51:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 2e1542c3-f29a-3275-932a-0b5af964181b | -9.71482 | -54.35473 | 2026-09-13 04:51:00 | NPP-375D | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b92fca7a-9c79-3169-a27e-1388de3d3fcf | -7.86799 | -54.71064 | 2026-09-13 04:51:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3d0607a4-1f0c-35e4-a97b-595a812527f3 | -7.86267 | -54.71789 | 2026-09-13 04:51:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7cd020d0-298f-3ced-989b-69bbebf5c6a7 | -6.6455 | -58.8269 | 2026-09-13 04:51:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5ecbef9f-e75b-3bf2-8135-7a50639bba76 | -8.97902 | -44.38908 | 2026-09-13 04:51:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 9f169a96-b3c2-38dc-a375-9c7fabef5995 | -6.07464 | -57.86282 | 2026-09-13 04:51:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9c823019-c2e6-36be-a093-1b92215a4f51 | -10.45353 | -48.65123 | 2026-09-13 04:51:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 258c351c-0dfa-36bc-b4b9-5ba54f4d7ecf | -13.31747 | -51.72572 | 2026-09-13 04:51:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 9c6b003b-720a-3b18-8ee1-50892bcc374b | -7.86662 | -54.72572 | 2026-09-13 04:51:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d88eb9ea-de40-3f1a-9122-f2f5b5ccc212 | -9.18122 | -59.62742 | 2026-09-13 04:51:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 4183224b-d59b-3bcb-a9da-d13ce8085fa0 | -6.30443 | -59.95863 | 2026-09-13 04:51:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 806f1f59-f154-3f01-be3d-649b6a9e27cd | -7.86756 | -54.69652 | 2026-09-13 04:51:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fde9c8bf-11b1-3fee-8745-1a67db20f4be | -6.30469 | -59.96254 | 2026-09-13 04:51:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b548560f-c9c4-3210-8011-05cc09baab94 | -13.60957 | -47.89258 | 2026-09-13 04:51:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b300e332-5ca9-3047-ba06-fcc9435c752f | -6.38124 | -58.28939 | 2026-09-13 04:51:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e7e6d98f-7ed4-357a-8bf8-8ae6066d75ef | -6.08027 | -57.86066 | 2026-09-13 04:51:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| e134f5eb-9c52-36a1-b1a3-cd29baf4afb3 | -10.62599 | -46.10184 | 2026-09-13 04:51:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f2b14dd8-5dab-33c4-9920-6b727bcaa04f | -13.56244 | -51.46295 | 2026-09-13 04:51:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2c2eec6b-56f6-3135-9966-574672ecce9b | -9.71022 | -54.35875 | 2026-09-13 04:51:00 | NPP-375D | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| df803f29-6c18-3e29-8e1c-2410e7a79d44 | -13.59922 | -47.8888 | 2026-09-13 04:51:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c9064b46-721a-32dc-9918-e4b4b59f1634 | -6.60025 | -58.85437 | 2026-09-13 04:51:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |


[Clique aqui para ver as próximas entradas](README41.md)
