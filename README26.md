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

## Dados Diários - Página 26

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a98b2462-d66a-31fb-8fb0-d2744f5dfa7e | -7.62287 | -41.84863 | 2025-10-24 04:19:00 | NPP-375D | CAMPINAS DO PIAUÍ | PIAUÍ | Brasil | 2202109 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| a4b1cfd1-e084-394c-8a7f-3dbe29a1754c | -6.80747 | -45.4493 | 2025-10-24 04:19:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c9ddfc7d-6166-3c29-9066-f3b8493e59a6 | -7.62231 | -41.85228 | 2025-10-24 04:19:00 | NPP-375D | CAMPINAS DO PIAUÍ | PIAUÍ | Brasil | 2202109 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 22432877-90dc-36f4-a575-a4845860f6e5 | -12.67508 | -48.62771 | 2025-10-24 04:19:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c6bf77f2-70d5-3639-a6bd-5e698e2c9154 | -8.17379 | -47.76545 | 2025-10-24 04:19:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 76a87c13-1e44-3d26-b3e0-83ec2980c526 | -13.20956 | -47.73396 | 2025-10-24 04:19:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 069073f3-e503-3964-858f-d19e00a3eb66 | -17.4038 | -52.02018 | 2025-10-24 04:19:00 | NPP-375D | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4e803c23-2989-3be7-b79a-6edc3f2de3a5 | -16.64285 | -43.71305 | 2025-10-24 04:19:00 | NPP-375D | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b94a1092-e52a-3e22-a93d-a9e52c4b8a95 | -8.50998 | -44.20605 | 2025-10-24 04:19:00 | NPP-375D | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 61d36652-9132-387a-93b6-b52617b65c05 | -20.45984 | -44.92691 | 2025-10-24 04:19:00 | NPP-375D | ITAPECERICA | MINAS GERAIS | Brasil | 3133501 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1a8a083c-2f53-355f-8ad4-ff406daf3516 | -13.89716 | -48.38892 | 2025-10-24 04:19:00 | NPP-375D | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| abccabc4-4683-398e-8635-7fc39e39058a | -16.48023 | -46.47614 | 2025-10-24 04:19:00 | NPP-375D | NATALÂNDIA | MINAS GERAIS | Brasil | 3144375 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d556db75-e9ee-3251-b3ef-5783eacb4980 | -7.68387 | -42.23901 | 2025-10-24 04:19:00 | NPP-375D | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 3ce39858-6560-3d5b-b24a-77767f864ceb | -7.97591 | -47.23792 | 2025-10-24 04:19:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6df1ac2b-6294-3d3d-be78-9a7b07d1507f | -17.65214 | -46.66301 | 2025-10-24 04:19:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| c6ef727e-4a1b-35c4-aa51-a1fc0cbf007b | -13.64146 | -49.46216 | 2025-10-24 04:19:00 | NPP-375D | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a04c420a-4732-3fb6-9a4e-ef3be7e22c51 | -7.85151 | -49.64981 | 2025-10-24 04:19:00 | NPP-375D | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 74966c4f-a48f-33ca-bd58-7335f92faa20 | -14.46912 | -47.91239 | 2025-10-24 04:19:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 773877b0-ab34-3d24-8378-ab26ec607f66 | -7.64278 | -42.17023 | 2025-10-24 04:19:00 | NPP-375D | SIMPLÍCIO MENDES | PIAUÍ | Brasil | 2210805 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 2bc264b8-b98b-34ea-b826-a715f4e882d3 | -12.80294 | -48.62857 | 2025-10-24 04:19:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c3560640-d5f0-3d3c-b1e3-4fa41265a2c2 | -15.56415 | -45.92416 | 2025-10-24 04:19:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 0.3 |
| cb69d3d9-fab2-3293-942d-bd9d50c9869c | -7.6291 | -41.85336 | 2025-10-24 04:19:00 | NPP-375D | CAMPINAS DO PIAUÍ | PIAUÍ | Brasil | 2202109 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 2db373ba-aa77-38c6-b188-fd0fe850997d | -12.81365 | -50.96452 | 2025-10-24 04:19:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 211ff6df-82ea-3c9a-952f-d539f10ba96d | -13.02835 | -48.57853 | 2025-10-24 04:19:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 68e681ca-23a2-3787-b9e8-b7ff5475e6dd | -5.86954 | -51.12471 | 2025-10-24 04:19:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 93eca1ac-0913-3c3f-aa84-2c96063f8f7e | -19.79899 | -44.12431 | 2025-10-24 04:19:00 | NPP-375D | RIBEIRÃO DAS NEVES | MINAS GERAIS | Brasil | 3154606 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5df89cbd-0d36-34b4-9e8f-207f3e8c8c24 | -13.92227 | -50.26199 | 2025-10-24 04:19:00 | NPP-375D | MUNDO NOVO | GOIÁS | Brasil | 5214051 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 487f66f6-f414-3554-836f-e1dec441da7f | -12.81905 | -50.93455 | 2025-10-24 04:19:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f33aed4c-fa4b-317e-bba5-64499f5dd0fa | -16.53524 | -54.17774 | 2025-10-24 04:19:00 | NPP-375D | PEDRA PRETA | MATO GROSSO | Brasil | 5106372 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 44f1180e-d54c-346e-8290-b96864a0e509 | -13.26469 | -47.88927 | 2025-10-24 04:19:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 99f1c654-6340-395e-91ae-1296648bf4db | -13.3413 | -47.96807 | 2025-10-24 04:19:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| eee06867-e4c8-34df-ae61-416c2f72beeb | -7.55658 | -47.36238 | 2025-10-24 04:19:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 9.1 |
| fb90a7dc-a8c9-35d8-b0ec-d027098b53df | -8.34898 | -46.17796 | 2025-10-24 04:19:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3ee95fcf-3f15-3b61-a231-93cae0f230c2 | -7.55127 | -47.37088 | 2025-10-24 04:19:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 16.7 |
| 832847d4-1267-35d4-ae3e-8f47b856a4f3 | -14.2689 | -48.07339 | 2025-10-24 04:19:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 519145f1-7fe0-35c2-9eb2-f7678c4508c3 | -8.21958 | -45.48682 | 2025-10-24 04:19:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fcd47343-f022-3f3e-b873-003166bff3ce | -6.77594 | -45.46782 | 2025-10-24 04:19:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4971b219-2e95-39e9-bdbd-c34196269aea | -14.5377 | -48.028 | 2025-10-24 04:19:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ebb6ca66-30b7-3aad-abf5-68bfa37b6c7e | -13.36175 | -50.46714 | 2025-10-24 04:19:00 | NPP-375D | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7cbd974b-3294-3160-ab4c-aac662b46ad3 | -13.33766 | -47.96753 | 2025-10-24 04:19:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ce308671-d75a-304c-97a0-530d208fb84c | -7.69148 | -42.24346 | 2025-10-24 04:19:00 | NPP-375D | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| abd8c7f2-fe20-3c3e-baf0-38fbbe50dd23 | -8.17762 | -47.7661 | 2025-10-24 04:19:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 84835a05-5f8b-360d-a3c8-6f6f6027dedc | -13.27522 | -47.98349 | 2025-10-24 04:19:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4c1a5203-cd9d-36cb-96f5-0b0c62fc0f7d | -16.99234 | -51.47837 | 2025-10-24 04:19:00 | NPP-375D | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ec1f655a-9d97-37f9-9ecd-c0c1634bd305 | -8.15059 | -46.86619 | 2025-10-24 04:19:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9594698e-4f6a-36ba-90d8-8cadcd04143a | -8.3448 | -46.18139 | 2025-10-24 04:19:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| eca04b57-e206-3d4d-ac71-7cd78ce0b8f5 | -16.54825 | -46.43913 | 2025-10-24 04:19:00 | NPP-375D | NATALÂNDIA | MINAS GERAIS | Brasil | 3144375 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 05d82aa3-7049-3fd4-aa0b-59d60da5f663 | -6.77568 | -45.49128 | 2025-10-24 04:19:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 45.8 |
| 8eaace01-ef61-3687-b73d-ea3bf7228385 | -19.46697 | -44.38943 | 2025-10-24 04:19:00 | NPP-375D | INHAÚMA | MINAS GERAIS | Brasil | 3131000 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e24a19ab-30db-3e98-a27b-de0444652367 | -16.61282 | -44.57279 | 2025-10-24 04:19:00 | NPP-375D | SÃO JOÃO DO PACUÍ | MINAS GERAIS | Brasil | 3162658 | 31 | 33 | nan | nan | nan | Cerrado | 0.3 |
| d04bee74-2570-3033-b663-8b7da2eaf40e | -7.77575 | -45.40063 | 2025-10-24 04:19:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 736cef7c-8b06-3539-965b-73dd213b20af | -18.24024 | -44.16338 | 2025-10-24 04:19:00 | NPP-375D | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 00200b60-e7d8-3c1e-a419-0557fc6cc3d7 | -8.34219 | -46.19749 | 2025-10-24 04:19:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4457c7c5-f3be-38eb-9343-d24f5cf12de6 | -17.6549 | -46.66727 | 2025-10-24 04:19:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 80fabb8b-ea5e-3257-99c6-d957f7215152 | -13.90015 | -48.34961 | 2025-10-24 04:19:00 | NPP-375D | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 21a4f52f-1da7-319f-ad9a-7949cd93809b | -14.51658 | -48.35152 | 2025-10-24 04:19:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4d4d1cf4-7f54-31ca-82b1-075bb2ecb158 | -15.94709 | -51.05258 | 2025-10-24 04:19:00 | NPP-375D | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1d33bdc8-04b3-3569-b27b-cb924fc4576e | -12.80856 | -48.66415 | 2025-10-24 04:19:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 173b0696-adc4-3e7c-919a-24d6899d0bd6 | -16.916 | -45.52987 | 2025-10-24 04:19:00 | NPP-375D | SANTA FÉ DE MINAS | MINAS GERAIS | Brasil | 3157609 | 31 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 5c25facb-76ce-34a0-82fe-b301afcf4c9b | -19.49718 | -44.23046 | 2025-10-24 04:19:00 | NPP-375D | SETE LAGOAS | MINAS GERAIS | Brasil | 3167202 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9b859335-6126-3ef9-a116-c63d9699f09d | -7.47376 | -48.39523 | 2025-10-24 04:19:00 | NPP-375D | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Amazônia | 0.7 |
| de2e7071-c95f-37c8-9fa5-ec87ed1df5e6 | -12.81161 | -50.95081 | 2025-10-24 04:19:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 5.2 |
| ab7a325e-a10b-36d2-9ccc-2be5524d9fd1 | -14.52473 | -47.95237 | 2025-10-24 04:19:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0f06195b-34fd-3072-96e2-9cf39d4bfb5e | -12.94303 | -46.54152 | 2025-10-24 04:19:00 | NPP-375D | NOVO ALEGRE | TOCANTINS | Brasil | 1715150 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| efb89966-f0b6-34cc-a3d4-dfeb01df841d | -7.07638 | -44.49497 | 2025-10-24 04:19:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 033cc82b-dea6-3cbb-9047-310eb1c99764 | -8.32535 | -46.25641 | 2025-10-24 04:19:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| d1ce0049-f59d-38e4-aa35-c630463daabe | -13.30545 | -47.44996 | 2025-10-24 04:19:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 64d9b7ce-a8d0-3b98-8ee3-45a17ae79da9 | -7.83215 | -45.37895 | 2025-10-24 04:19:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 32e07588-89ea-3edc-b1d7-1b4a2f3a0f1d | -13.61633 | -47.05729 | 2025-10-24 04:19:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2a4d507c-a1e8-395d-a9c4-a40995d32d25 | -8.34127 | -46.18087 | 2025-10-24 04:19:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| e73c2caa-e4bf-3ad6-a35a-8bbc00e25cf9 | -19.99268 | -44.22656 | 2025-10-24 04:19:00 | NPP-375D | BETIM | MINAS GERAIS | Brasil | 3106705 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 1be6d7c8-f01a-30b0-b3e0-f8229f56008e | -8.326 | -46.25241 | 2025-10-24 04:19:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 9d9d8fd6-4d4a-36a8-ba6d-1a9948d36458 | -17.65155 | -46.66668 | 2025-10-24 04:19:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 1c7cd276-e854-390b-b253-3325d4ee9ba1 | -6.7763 | -45.48745 | 2025-10-24 04:19:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 45.8 |
| 565f99ab-a34d-3450-b5eb-94c2b3e68285 | -13.89723 | -48.34462 | 2025-10-24 04:19:00 | NPP-375D | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 747271da-8f25-320a-a870-0c069b6459e5 | -13.33189 | -47.95761 | 2025-10-24 04:19:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2f32c2ef-8140-3b68-b8d1-efd0807322f6 | -8.3273 | -46.24442 | 2025-10-24 04:19:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 82830f81-8575-315f-9a64-5ae0c1c12397 | -17.00621 | -49.15633 | 2025-10-24 04:19:00 | NPP-375D | HIDROLÂNDIA | GOIÁS | Brasil | 5209705 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3f8a1910-e9a3-36ad-ac30-72954acb1e62 | -6.91913 | -44.01635 | 2025-10-24 04:19:00 | NPP-375D | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| c84896a8-b9c9-3596-9029-6c006772f709 | -19.79554 | -44.12373 | 2025-10-24 04:19:00 | NPP-375D | RIBEIRÃO DAS NEVES | MINAS GERAIS | Brasil | 3154606 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 01fa31f5-a1f6-3c6b-8b8b-1bcb0135e0e5 | -16.13141 | -54.00388 | 2025-10-24 04:19:00 | NPP-375D | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 548a5c83-b6f0-34c4-ba23-ab08c56688f9 | -7.07592 | -41.66118 | 2025-10-24 04:19:00 | NPP-375D | PAQUETÁ | PIAUÍ | Brasil | 2207553 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 78407cbe-a9f6-325c-a504-37a538d14785 | -18.35576 | -51.70963 | 2025-10-24 04:19:00 | NPP-375D | SERRANÓPOLIS | GOIÁS | Brasil | 5220504 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 69db510f-28ef-3aa2-b19e-ffa321db459d | -7.98335 | -47.23932 | 2025-10-24 04:19:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2a7dbb10-fa6b-37e8-b737-0e462596544c | -15.13439 | -47.93544 | 2025-10-24 04:19:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| fb8ffa58-a9d0-3d6c-8d95-57fde7c53cd3 | -7.47648 | -42.5671 | 2025-10-24 04:19:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 52eb01ab-dc14-389e-b157-aae6b77d232d | -13.21613 | -47.73877 | 2025-10-24 04:19:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e9b3dc5c-ec7d-30c5-9c58-f8a562d3310e | -14.34391 | -46.88259 | 2025-10-24 04:19:00 | NPP-375D | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5f78bea7-6a14-3e11-8895-d5de0c7a6c70 | -17.09887 | -46.19265 | 2025-10-24 04:19:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e768f2d6-12b3-3f6f-8475-c97a79ec6e17 | -13.91186 | -48.39144 | 2025-10-24 04:19:00 | NPP-375D | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c8e261ae-1712-308b-90b1-1da86a4da0ed | -6.77282 | -45.4869 | 2025-10-24 04:19:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 45.8 |
| 68bf505c-bc02-320d-91f8-c68c4cd25852 | -8.61909 | -44.81213 | 2025-10-24 04:19:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 0d31e452-0d96-3fcf-80d2-71102af999e4 | -8.24071 | -47.17905 | 2025-10-24 04:19:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| e9ba4c58-a13a-3f90-b166-74b45d43fad9 | -14.73883 | -46.60751 | 2025-10-24 04:19:00 | NPP-375D | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 510be204-10fe-3951-a497-0808d2f9c8a7 | -6.77345 | -45.48309 | 2025-10-24 04:19:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 43.0 |
| 78d3d889-510e-3eb7-a158-bcf95fdda103 | -7.62801 | -48.39283 | 2025-10-24 04:19:00 | NPP-375D | NOVA OLINDA | TOCANTINS | Brasil | 1714880 | 17 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5b6189e7-5f66-383a-96cd-89b6234de061 | -13.63891 | -46.83463 | 2025-10-24 04:19:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c259ac24-0d3a-3514-94f6-3430187d784e | -12.81443 | -50.96022 | 2025-10-24 04:19:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| f63e00f8-7d00-31de-a182-41ae23625c0c | -14.46361 | -47.91312 | 2025-10-24 04:19:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9d3fa23c-0d2a-3a7d-aeb2-9d89b80c6f0a | -14.52401 | -47.95664 | 2025-10-24 04:19:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |


[Clique aqui para ver as próximas entradas](README27.md)
