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

## Dados Diários - Página 14

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| df54a335-d736-31f4-bb45-541d0368919c | -10.97497 | -45.11239 | 2025-06-29 04:10:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 15.3 |
| 9f906459-4f8c-3f40-81a2-f4c687d8400c | -13.27542 | -48.42676 | 2025-06-29 04:10:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8c0c4d34-52c7-380b-83e6-c77dbdaed768 | -11.55881 | -52.79391 | 2025-06-29 04:10:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6d7eb76c-282b-3764-b754-fd26acead04e | -11.55471 | -52.78509 | 2025-06-29 04:10:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 14.1 |
| ac481079-6249-31d7-b62e-5a5caf34130f | -10.57037 | -52.03706 | 2025-06-29 04:10:00 | NPP-375D | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1abfa66f-cb92-37f2-9911-8e80eea51841 | -11.55545 | -52.78127 | 2025-06-29 04:10:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 13.7 |
| 665befea-81d4-3983-8436-7766e962db82 | -13.4825 | -47.72735 | 2025-06-29 04:10:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 620398fd-1310-3d04-845c-8ea27a62a2c6 | -9.4254 | -47.95295 | 2025-06-29 04:10:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 5ac34841-93cd-329f-be39-6b7c0bfc175c | -12.06064 | -48.47369 | 2025-06-29 04:10:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| e708d4ae-49b4-3415-8bd4-26aed0d67e70 | -11.01513 | -56.23898 | 2025-06-29 04:10:00 | NPP-375D | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 5ce43600-1584-3ecd-88b3-1e50107ba98c | -10.54254 | -42.53941 | 2025-06-29 04:10:00 | NPP-375D | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 71b8c156-90a0-3256-9665-34d3bbe28d83 | -7.09369 | -43.65675 | 2025-06-29 04:10:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4fc23794-8311-37cb-8da6-9dd576e1682c | -10.55611 | -52.05262 | 2025-06-29 04:10:00 | NPP-375D | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| f42d3673-6c54-322f-932a-fd9b54c400ad | -11.55587 | -52.80914 | 2025-06-29 04:10:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 6.5 |
| e2a8707b-8e8e-342d-981f-71c5a7f32b40 | -11.57696 | -44.83477 | 2025-06-29 04:10:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d335c3c8-dff6-3736-be75-dbf91944b854 | -10.56223 | -52.05011 | 2025-06-29 04:10:00 | NPP-375D | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 9062c752-c032-3e04-99ac-b87ce21832f6 | -6.67136 | -44.25325 | 2025-06-29 04:10:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 239ffd52-3d74-3f46-bb01-8d8d3680a47e | -6.51586 | -44.43088 | 2025-06-29 04:10:00 | NPP-375D | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6e723a27-2aeb-360a-a3c6-11169129012e | -10.55294 | -52.03405 | 2025-06-29 04:10:00 | NPP-375D | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 4ef7178c-2eb1-3dab-842c-ae58e5f66c09 | -10.56378 | -52.03619 | 2025-06-29 04:10:00 | NPP-375D | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e58c4407-ffa0-34af-bbac-7375bee58d19 | -7.56011 | -45.84688 | 2025-06-29 04:10:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 98c3d4e5-8f7f-3efb-b2a8-c94ba3103c40 | -12.11511 | -54.58187 | 2025-06-29 04:10:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 78278046-802b-34c2-9a12-eefbf33a0c4c | -7.19016 | -43.42855 | 2025-06-29 04:10:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 91cfa6d4-52e1-3a73-b6da-51b7a6315c7d | -12.10896 | -54.58045 | 2025-06-29 04:10:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| b8e48cfe-64ed-3c9b-9525-735d18fd1716 | -11.55955 | -52.79009 | 2025-06-29 04:10:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| bc705ab4-1749-348b-9480-fc516fbdb26d | -11.54427 | -52.77903 | 2025-06-29 04:10:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 26.3 |
| 37445010-636e-3ea5-ac00-1239dad6ab06 | -7.5563 | -45.84627 | 2025-06-29 04:10:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e1922412-b91e-3653-abcb-85a89bfb850e | -10.86563 | -53.75497 | 2025-06-29 04:10:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6fa58012-717c-3d49-bbdd-bd7ebb214cc4 | -10.55901 | -52.0316 | 2025-06-29 04:10:00 | NPP-375D | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| aa2659a7-fd7f-333f-b2b1-2f00805a32d1 | -10.97848 | -45.11297 | 2025-06-29 04:10:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 13.6 |
| 6c13a208-95ff-38e7-b16c-05ba9e41927a | -11.5394 | -52.77419 | 2025-06-29 04:10:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 26.3 |
| 2da2eade-9023-315b-a9a4-1cc21363c8d7 | -11.26121 | -52.75179 | 2025-06-29 04:10:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 5749f746-f84c-3457-943a-701f8d623ad1 | -11.02836 | -56.27289 | 2025-06-29 04:10:00 | NPP-375D | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 14df429d-8594-3655-9b7d-2569320806c3 | -11.03189 | -56.26329 | 2025-06-29 04:10:00 | NPP-375D | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 3bab5d46-b65f-3e45-8eab-178c92150c46 | -10.55817 | -52.04196 | 2025-06-29 04:10:00 | NPP-375D | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 14272436-fc2b-3ae4-b1a7-567a48c719d7 | -10.55411 | -52.03386 | 2025-06-29 04:10:00 | NPP-375D | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 07b2b1f8-1dc0-3f99-9af2-6fe15b3ec438 | -14.53193 | -53.76815 | 2025-06-29 04:12:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5f87b8c7-1a7a-331b-9c82-276d5a0fa839 | -14.21732 | -45.51038 | 2025-06-29 04:12:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5c442092-5026-33fc-b74b-31d61c156ac8 | -13.94888 | -54.49412 | 2025-06-29 04:12:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6659a249-e5d9-3385-823d-973d4f670d4e | -15.73038 | -49.5597 | 2025-06-29 04:12:00 | NPP-375D | ITAGUARU | GOIÁS | Brasil | 5210604 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| f39cb9a5-4a77-3092-876a-1e6c6d95abf9 | -17.39978 | -42.6258 | 2025-06-29 04:12:00 | NPP-375D | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 13.3 |
| 28c37de7-c8d7-3b61-8f0e-a4d199279e32 | -19.51264 | -44.27554 | 2025-06-29 04:12:00 | NPP-375D | SETE LAGOAS | MINAS GERAIS | Brasil | 3167202 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 521178c0-408f-3b75-a25e-983647c27244 | -19.31968 | -43.73319 | 2025-06-29 04:12:00 | NPP-375D | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e490b48a-4675-3526-840c-1c694f1ed331 | -17.38796 | -42.6585 | 2025-06-29 04:12:00 | NPP-375D | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0a52543f-f301-30b7-9a08-f545c673c0a0 | -12.62198 | -54.20819 | 2025-06-29 04:12:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| d170b442-47c4-3bfc-8f18-0f69dba335ba | -16.68273 | -43.88463 | 2025-06-29 04:12:00 | NPP-375D | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 44156f41-8683-39f2-97bf-5c7b03c802c5 | -16.28802 | -49.94135 | 2025-06-29 04:12:00 | NPP-375D | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a350e9dc-4081-39ff-824b-7cb783a914d4 | -15.56952 | -47.85411 | 2025-06-29 04:12:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9f16d4e2-bda6-39ca-9ada-f880dba9e975 | -19.93406 | -44.2001 | 2025-06-29 04:12:00 | NPP-375D | BETIM | MINAS GERAIS | Brasil | 3106705 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 240106db-a7f6-32e3-a7d9-9819b9e0a28e | -19.02952 | -46.58908 | 2025-06-29 04:12:00 | NPP-375D | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b39a83a9-b026-38cc-bfde-1a4b507fb56f | -13.01481 | -53.42505 | 2025-06-29 04:12:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| fcb70c71-58cc-3fc8-abd8-74bb7ed157fc | -15.34133 | -49.13005 | 2025-06-29 04:12:00 | NPP-375D | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 12f6a06c-5b6f-3ae6-a676-c10a16dd759f | -20.34191 | -45.7226 | 2025-06-29 04:12:00 | NPP-375D | PAINS | MINAS GERAIS | Brasil | 3146503 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 56eadb52-693e-378c-955a-df33640271f6 | -17.76079 | -52.45131 | 2025-06-29 04:12:00 | NPP-375D | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 78c1d479-4433-384b-843f-66ded2461724 | -12.97961 | -54.68578 | 2025-06-29 04:12:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4f77da11-b6e0-3e64-abf8-05f2c67ed7df | -17.92263 | -45.55617 | 2025-06-29 04:12:00 | NPP-375D | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 27931006-d493-3c1c-917b-16e236dfe962 | -13.10022 | -52.29432 | 2025-06-29 04:12:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fe2bc99e-7770-303b-9fbd-c61cc831643a | -14.53252 | -48.25937 | 2025-06-29 04:12:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 21db5409-16fa-31f1-a310-08df271f0927 | -14.21796 | -45.50651 | 2025-06-29 04:12:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| cf311c29-b3cf-3949-8810-e39605e22f52 | -14.21549 | -45.50891 | 2025-06-29 04:12:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0edc8367-e44a-37e0-bb9f-8c8b72a417f8 | -14.84255 | -48.34356 | 2025-06-29 04:12:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a25b0992-e44a-304f-aef2-25e92e576836 | -15.73111 | -49.55575 | 2025-06-29 04:12:00 | NPP-375D | ITAGUARU | GOIÁS | Brasil | 5210604 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 935f761f-d392-3b5e-ab81-0505650be0a2 | -17.39696 | -42.62148 | 2025-06-29 04:12:00 | NPP-375D | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 5cb7cf2a-7831-3b90-8db6-fc44d59dbfb7 | -13.95574 | -54.49094 | 2025-06-29 04:12:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7ef4f91f-637c-3722-92db-7433ec535b38 | -13.95248 | -54.48782 | 2025-06-29 04:12:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 992211ba-f1e2-34ed-aff3-7ac493c335ea | -15.08015 | -48.94361 | 2025-06-29 04:12:00 | NPP-375D | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 0e887aff-6b96-3d43-a622-56780fd03a8c | -18.95772 | -44.08758 | 2025-06-29 04:12:00 | NPP-375D | SANTANA DE PIRAPAMA | MINAS GERAIS | Brasil | 3158508 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 361e6a12-4e5e-3df7-aa06-0f0700dab797 | -14.66629 | -47.98298 | 2025-06-29 04:12:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bfcdb22f-9f21-3762-9126-ac4bc007e004 | -14.30324 | -46.93167 | 2025-06-29 04:12:00 | NPP-375D | IACIARA | GOIÁS | Brasil | 5209903 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d501eeba-61f7-39a8-8263-1d46fcd84636 | -17.3964 | -42.62524 | 2025-06-29 04:12:00 | NPP-375D | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 13.3 |
| 8a2f6640-faad-3686-95f1-35f58fa50d09 | -14.2224 | -45.51014 | 2025-06-29 04:12:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 619fd83d-b7e3-3cb6-9713-b45e2c449832 | -17.39922 | -42.62956 | 2025-06-29 04:12:00 | NPP-375D | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 13.3 |
| cb0b33d4-7f74-3eda-82e4-1d3907b1e3b5 | -13.9584 | -54.48927 | 2025-06-29 04:12:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e9ea2139-9adf-337e-a498-b7d9489b0c96 | -12.62104 | -54.21279 | 2025-06-29 04:12:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 2086cb12-f416-3c6d-9f65-8325eb74aa75 | -18.37852 | -44.5019 | 2025-06-29 04:12:00 | NPP-375D | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| aa8b9562-3bbb-3d5d-9a7b-90143f04daec | -12.62703 | -54.21404 | 2025-06-29 04:12:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ca8323c5-2f4f-3ac5-8a78-709c9e91e57b | -14.02748 | -54.48552 | 2025-06-29 04:12:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 2e850375-6055-3898-931e-404ec923a071 | -17.92201 | -45.55991 | 2025-06-29 04:12:00 | NPP-375D | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b3ce3853-89b9-3a36-97fc-9e649bfef4ea | -19.63559 | -45.18929 | 2025-06-29 04:12:00 | NPP-375D | BOM DESPACHO | MINAS GERAIS | Brasil | 3107406 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 8fc75efa-786e-376e-b757-4567ddd1fe2f | -14.21894 | -45.50952 | 2025-06-29 04:12:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 97fca819-36ba-34f3-99ca-d5effdf9a33f | -18.67132 | -44.59721 | 2025-06-29 04:12:00 | NPP-375D | MORRO DA GARÇA | MINAS GERAIS | Brasil | 3143609 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 1c52d937-4f94-3bcc-93c4-ba5dcfb95a45 | -15.64782 | -49.73058 | 2025-06-29 04:12:00 | NPP-375D | ITAPURANGA | GOIÁS | Brasil | 5211206 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 51ab5cc9-0f64-36f2-ae07-39053e1428e1 | -16.58251 | -49.33301 | 2025-06-29 04:12:00 | NPP-375D | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 70196149-aa91-3b76-b3de-a10ff19d15e0 | -16.28724 | -49.94548 | 2025-06-29 04:12:00 | NPP-375D | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b7671991-ba57-3388-8d57-025aa09edd14 | -18.78941 | -52.58271 | 2025-06-29 04:12:00 | NPP-375D | CHAPADÃO DO SUL | MATO GROSSO DO SUL | Brasil | 5002951 | 50 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 45a1040b-b2ce-38a2-85a6-7070e9e53dc7 | -15.93142 | -52.28103 | 2025-06-29 04:12:00 | NPP-375D | PONTAL DO ARAGUAIA | MATO GROSSO | Brasil | 5106653 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 13265161-e7c0-3bfa-ac31-58d29c2ae74d | -17.40034 | -42.62204 | 2025-06-29 04:12:00 | NPP-375D | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 21273ff5-5101-3987-ada1-0f2b8e33c0f2 | -16.57841 | -49.3323 | 2025-06-29 04:12:00 | NPP-375D | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 23e4eced-6a68-3166-a9b7-f5b060d186f5 | -19.63226 | -45.18869 | 2025-06-29 04:12:00 | NPP-375D | BOM DESPACHO | MINAS GERAIS | Brasil | 3107406 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| b6e7be95-ee8f-328b-bdd9-4ac753116212 | -14.52879 | -53.76644 | 2025-06-29 04:12:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d9ec3d87-a34e-305a-8ea8-38107f4d09c7 | -18.78705 | -52.58151 | 2025-06-29 04:12:00 | NPP-375D | CHAPADÃO DO SUL | MATO GROSSO DO SUL | Brasil | 5002951 | 50 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 7e6f1cb6-4427-3d9a-8005-1b95047a2d3e | -13.13849 | -56.8086 | 2025-06-29 04:12:00 | NPP-375D | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 1821c40a-d075-34ae-a76c-f1e04dcec20e | -13.09958 | -52.29765 | 2025-06-29 04:12:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 69a6d8df-a9f6-3580-a5d9-76fbf778fb3a | -18.79188 | -52.58253 | 2025-06-29 04:12:00 | NPP-375D | CHAPADÃO DO SUL | MATO GROSSO DO SUL | Brasil | 5002951 | 50 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 46539d9c-54f3-3623-b522-06996bc3a6a9 | -14.69196 | -53.39324 | 2025-06-29 04:12:00 | NPP-375D | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ea034bc0-91be-386d-b527-a013eeeb4b6e | -16.21195 | -43.41515 | 2025-06-29 04:12:00 | NPP-375D | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ede4bf3d-c327-38fa-a5db-15c0511077be | -16.58088 | -49.3328 | 2025-06-29 04:12:00 | NPP-375D | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 63d59b06-2156-3d5f-9170-78a8e1f722c6 | -16.58158 | -49.32911 | 2025-06-29 04:12:00 | NPP-375D | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 3ebcc9d6-1c02-3b72-a91c-e89109b9e2c2 | -14.24033 | -45.50929 | 2025-06-29 04:12:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 58f3fb20-fc91-38ee-8595-816830efdb1b | -16.12688 | -46.45137 | 2025-06-29 04:12:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |


[Clique aqui para ver as próximas entradas](README15.md)
