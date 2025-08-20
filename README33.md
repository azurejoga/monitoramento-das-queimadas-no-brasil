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

## Dados Diários - Página 33

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b3624b66-410f-37d2-bbca-62cfe9c5050e | -12.52049 | -45.60627 | 2025-08-20 04:36:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 05f109c8-d3b2-33bb-9c4d-a7e1cac6566e | -9.18593 | -59.63694 | 2025-08-20 04:36:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 5b96bafe-c16a-3c73-ac4c-9d96c24016b1 | -9.18416 | -59.64598 | 2025-08-20 04:36:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 79bb19a3-8fe0-3d36-b25f-01609b2b2a87 | -14.61691 | -54.89215 | 2025-08-20 04:36:00 | NPP-375D | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 04296f89-481c-344c-a9d5-4e47f8269488 | -12.10827 | -47.89806 | 2025-08-20 04:36:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4eea7827-3a29-32c8-a586-83751de941cf | -13.57492 | -47.01892 | 2025-08-20 04:36:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8eb11fb9-9f8a-3121-9fc8-da41457c2212 | -15.09607 | -47.33455 | 2025-08-20 04:36:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 0.3 |
| d7ac0481-a462-336e-a5b6-96582b31b291 | -11.19638 | -55.91732 | 2025-08-20 04:36:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 50bb2ee9-88d3-37d3-aa89-4202a3d0f2d5 | -11.97134 | -46.77193 | 2025-08-20 04:36:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9f8c3972-6578-38fe-af29-160e4079cf81 | -13.02941 | -46.81222 | 2025-08-20 04:36:00 | NPP-375D | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 832b3483-db3a-39d2-b728-51e5d35701a0 | -13.15064 | -54.92966 | 2025-08-20 04:36:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6b95b5b4-e937-3ed3-9bcf-ade32900a83d | -13.58596 | -47.01667 | 2025-08-20 04:36:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ec9b60d6-bc9f-3a8b-be4a-b6df192d3a08 | -13.40515 | -46.36996 | 2025-08-20 04:36:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 2001ac42-06ce-30b5-bd2d-a78d4de734b0 | -12.97535 | -56.8658 | 2025-08-20 04:36:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 9287d0b8-461f-340a-b08f-c722d39adbcd | -12.9706 | -56.86482 | 2025-08-20 04:36:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 3a153e7e-2130-3d4e-823c-398914da7eb2 | -11.5951 | -50.53367 | 2025-08-20 04:36:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 7e95ecec-4a79-3683-b753-2157ffa34242 | -12.50639 | -47.43381 | 2025-08-20 04:36:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 09e7ce31-6dc4-3db5-89b3-aa9bf4bbeddf | -11.0272 | -44.60154 | 2025-08-20 04:36:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7f7dbdae-1b82-32a2-8904-08b44e7fd28e | -13.033 | -46.78844 | 2025-08-20 04:36:00 | NPP-375D | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| c30c2ec0-6e37-3f90-b6ab-976b4822ea6f | -9.18048 | -59.60099 | 2025-08-20 04:36:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| fc8959c7-4cd2-3067-9c9e-462fa50481a1 | -9.20728 | -59.6932 | 2025-08-20 04:36:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 134324d9-75ed-31fa-8478-6e7629e72834 | -11.02338 | -44.60094 | 2025-08-20 04:36:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 658e391e-ea24-3028-911e-251bb96ffbd2 | -15.74721 | -46.62519 | 2025-08-20 04:36:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3bcf11a3-b850-3c07-8577-bc8cb6161869 | -14.45576 | -48.48233 | 2025-08-20 04:36:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 479fdc60-de1f-365e-9d22-be5f73ae056a | -9.89294 | -60.28596 | 2025-08-20 04:36:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f2e533f4-6f04-351b-bd15-4d646e16d8ed | -11.31746 | -55.21626 | 2025-08-20 04:36:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 90883fbe-49f9-3cb4-9101-ef1ca2fef620 | -11.21874 | -49.16109 | 2025-08-20 04:36:00 | NPP-375D | CRIXÁS DO TOCANTINS | TOCANTINS | Brasil | 1706258 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2bde5680-066f-3739-9af7-3a698a869a05 | -14.62474 | -54.8897 | 2025-08-20 04:36:00 | NPP-375D | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6d1ed96d-19a0-3280-ab25-1d1b6739e269 | -11.747 | -55.84268 | 2025-08-20 04:36:00 | NPP-375D | IPIRANGA DO NORTE | MATO GROSSO | Brasil | 5104526 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 77eba182-11e3-3dcc-a727-9706a9a98ced | -15.5767 | -50.30825 | 2025-08-20 04:36:00 | NPP-375D | FAINA | GOIÁS | Brasil | 5207535 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 056ccb38-6bf9-3b22-a4d8-8ec0fe008c58 | -15.12592 | -48.71184 | 2025-08-20 04:36:00 | NPP-375D | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6d510693-f80e-39f6-8f47-348a95cf635e | -10.91277 | -57.50632 | 2025-08-20 04:36:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d886e9e8-70da-3581-8925-ae6984b5ea04 | -13.17542 | -46.87367 | 2025-08-20 04:36:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3a2c5ca2-4dfe-33c1-a690-f31113cb6648 | -15.54093 | -48.56715 | 2025-08-20 04:36:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 12d58cb6-187c-3fe9-a135-397306befd5e | -13.41118 | -46.35396 | 2025-08-20 04:36:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 71aefda9-f0fb-3017-baa8-b768a1e36ca0 | -13.15411 | -54.93435 | 2025-08-20 04:36:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| fb0e0735-e96f-33a6-84a0-037ee9639bf8 | -13.3932 | -47.49245 | 2025-08-20 04:36:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 69759630-e1be-359d-8ca3-8cf7307893d8 | -13.14852 | -54.94139 | 2025-08-20 04:36:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 26b1520b-a549-375a-b02c-b9a73a9514b7 | -13.17953 | -46.87003 | 2025-08-20 04:36:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| cb03914d-43a1-355d-a1c1-f1b9d4812c3f | -13.17947 | -46.89449 | 2025-08-20 04:36:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| bebd8c16-7355-36ec-9124-8755fd8fd551 | -15.54511 | -42.28509 | 2025-08-20 04:36:00 | NPP-375D | INDAIABIRA | MINAS GERAIS | Brasil | 3130655 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| ad2f2c05-6a8a-38be-8295-60512284901d | -13.08166 | -46.82744 | 2025-08-20 04:36:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ea26c851-3f95-3fd1-ada4-7058cbd987dc | -13.33149 | -54.41121 | 2025-08-20 04:36:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 9786f391-a032-3b6c-b426-248a6efcddf5 | -12.10375 | -47.9199 | 2025-08-20 04:36:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 299e9695-6057-3528-b3de-ceefae3f06c0 | -13.15758 | -54.93905 | 2025-08-20 04:36:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| aafa1db6-0a14-3fac-b141-b25503b314f3 | -15.74747 | -46.62295 | 2025-08-20 04:36:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 51365d83-d11b-322d-b790-ebefe993eef1 | -12.94969 | -46.15804 | 2025-08-20 04:36:00 | NPP-375D | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d1a5f186-ae9a-349a-a828-b1a97e962e42 | -11.67102 | -60.19429 | 2025-08-20 04:36:00 | NPP-375D | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| cac26750-1d7b-3007-b6b1-633a417e9f47 | -9.19475 | -59.62411 | 2025-08-20 04:36:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 30d3cc49-c6b3-36e8-9002-2cf115d5b986 | -15.75107 | -46.62368 | 2025-08-20 04:36:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8ed9f9dc-1cab-3370-89c6-7a3b4c9ab2bd | -13.02891 | -46.79178 | 2025-08-20 04:36:00 | NPP-375D | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| bf8b864d-c611-3f57-8e54-745847dcf5bb | -9.23648 | -59.60386 | 2025-08-20 04:36:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e60e74d6-ed04-3dd2-9ac7-003854af1a7e | -9.18505 | -59.64146 | 2025-08-20 04:36:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 0771f5e5-0026-3e85-be62-857dcda68acb | -10.12433 | -47.43051 | 2025-08-20 04:36:00 | NPP-375D | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4200b241-92c2-31d8-8931-a9bd4a6c4fcf | -15.54824 | -48.56457 | 2025-08-20 04:36:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ddf2c25d-1af0-3db9-b152-28b798f631cc | -10.27482 | -46.77328 | 2025-08-20 04:36:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f6bccbfe-b8d6-3c7d-9cea-2330df7f16b1 | -13.14157 | -54.93204 | 2025-08-20 04:36:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 12.6 |
| 92cb7fa9-5e54-312d-bc3e-ef6e357ed212 | -13.17664 | -46.86541 | 2025-08-20 04:36:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 35d3848b-0d44-3fe0-a85a-f9e2ce35c703 | -9.23379 | -59.61778 | 2025-08-20 04:36:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 539d5c2f-92ac-3b3b-8260-e746c8254e4d | -13.35017 | -54.39986 | 2025-08-20 04:36:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 643de2f8-7c2f-3ef5-8a72-11132e70a700 | -13.40759 | -46.35348 | 2025-08-20 04:36:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 88a341ca-5558-3869-8bd6-a2cc35367573 | -13.03619 | -56.85685 | 2025-08-20 04:36:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 4b2ca84e-8da0-3753-b04c-3dcd3d6ed1ff | -12.90578 | -46.09734 | 2025-08-20 04:36:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 58c43140-1d08-3220-b802-541bbb910ca8 | -14.30813 | -52.00553 | 2025-08-20 04:36:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 04606e02-fc5b-3ba4-8c61-caf0f3e65a4f | -14.50143 | -45.96052 | 2025-08-20 04:36:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 974b6877-5f6c-3181-bcc3-4c8a93b3caa5 | -14.61834 | -54.90778 | 2025-08-20 04:36:00 | NPP-375D | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 7119aa40-d8a9-3a8e-b7d1-1c6626b0a700 | -13.33617 | -54.40836 | 2025-08-20 04:36:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 61cd0c24-efb1-3efa-958b-cee799f94f2e | -14.54982 | -53.95026 | 2025-08-20 04:36:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 31f89e80-65e6-3d7c-b054-6dfb5e423ff1 | -13.18891 | -54.95707 | 2025-08-20 04:36:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d41a896e-35ad-34bd-b74d-5ca170f319dc | -12.23039 | -44.62991 | 2025-08-20 04:36:00 | NPP-375D | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3cecacfa-739e-30e2-92e8-ab6c6c0ed775 | -11.67189 | -60.18985 | 2025-08-20 04:36:00 | NPP-375D | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 4f14f0a4-78ae-3d3a-9e9d-656ff385ceb3 | -12.09087 | -47.91418 | 2025-08-20 04:36:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 21f9f8ae-56b6-3b5b-8231-9948d631eb3e | -13.03845 | -46.805 | 2025-08-20 04:36:00 | NPP-375D | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3bbdf243-0e0d-337b-b7de-0e5b64e7c46a | -13.14575 | -54.93282 | 2025-08-20 04:36:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 12.6 |
| 2f968eaa-2932-368e-89ae-00df0b7e8bb3 | -9.23559 | -59.60846 | 2025-08-20 04:36:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f4cab221-45f3-3517-a027-9261d2fb2e6f | -13.14922 | -54.93751 | 2025-08-20 04:36:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 710e21d8-8782-31a0-8ac3-1b0c2d4c5daa | -14.89192 | -48.09047 | 2025-08-20 04:36:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 50a31c89-1135-3256-9b28-792940a1178b | -13.1063 | -51.91163 | 2025-08-20 04:36:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 81e47d4e-d0f0-3549-9c6e-2c018a0e171c | -9.17618 | -59.59046 | 2025-08-20 04:36:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| edeac7c9-5e16-3136-b343-cf62d3838973 | -12.52417 | -45.60683 | 2025-08-20 04:36:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 63fe5838-a48e-326e-bce5-b589a2a01bb4 | -14.16173 | -45.29013 | 2025-08-20 04:36:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7ca2b672-f7a9-3d6e-b03a-5ebf6a17cccc | -12.97635 | -56.86057 | 2025-08-20 04:36:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 7805bb26-2f56-3490-9340-18927204ff8c | -13.21853 | -50.82138 | 2025-08-20 04:36:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b3e71d89-19c1-35d2-bd41-66096f1483be | -15.07884 | -48.39955 | 2025-08-20 04:36:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| bd1fde92-bbba-3e50-8217-076351c3e3ed | -9.2347 | -59.61308 | 2025-08-20 04:36:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2439ebe3-b490-37e8-b82b-db72416c80a3 | -12.14151 | -48.01768 | 2025-08-20 04:36:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| d49f6e79-06e6-3a58-9d06-d593829845a6 | -13.86718 | -45.55452 | 2025-08-20 04:36:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e6871d59-0638-331a-b0ab-e1cc2a28e6dc | -9.23983 | -59.6191 | 2025-08-20 04:36:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0758fd0a-dcbf-3fdf-bc71-844fd4511f6b | -12.36568 | -54.17029 | 2025-08-20 04:36:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 33d4ba60-d506-3633-9883-ea649b9f31dc | -9.20634 | -59.69429 | 2025-08-20 04:36:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 897898ef-f02a-3ac3-adaf-c15a76a22331 | -10.46963 | -48.35639 | 2025-08-20 04:36:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 62644111-0131-3fd3-8ef9-f0b826e95143 | -14.88908 | -48.08622 | 2025-08-20 04:36:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c2389503-2c50-35b5-ac26-ce78055bb817 | -13.03494 | -46.80457 | 2025-08-20 04:36:00 | NPP-375D | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 05c919e1-8d67-3f90-ab4f-dab5f2b80f63 | -12.94192 | -46.16086 | 2025-08-20 04:36:00 | NPP-375D | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 24b3fe21-1d44-396a-b41a-2b8e53f8a339 | -13.49389 | -47.07898 | 2025-08-20 04:36:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7a26efb9-f381-37a6-b5df-bdad8ae634b6 | -8.96949 | -60.49723 | 2025-08-20 04:36:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f4106e62-61ac-3fc3-b46a-4cc13d402624 | -12.9173 | -46.10182 | 2025-08-20 04:36:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e2143808-66d4-3b73-9c88-aec22c8424de | -13.33214 | -54.40763 | 2025-08-20 04:36:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 8451dcd6-5b70-38ff-94e8-054098c7945c | -15.5488 | -48.56089 | 2025-08-20 04:36:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a6cee569-50c7-3115-969c-5268eac67c6e | -11.74362 | -58.32262 | 2025-08-20 04:36:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |


[Clique aqui para ver as próximas entradas](README34.md)
