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

## Dados Diários - Página 74

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d374030d-63ff-3492-9610-957bcc6e9336 | -12.95753 | -54.78238 | 2025-09-06 04:40:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 8d7635b7-53d0-3192-83b2-57368a499794 | -15.71201 | -53.58731 | 2025-09-06 04:40:00 | NOAA-20 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 40f39791-19e7-3073-883d-39156c9ad7de | -9.20479 | -57.09409 | 2025-09-06 04:40:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 30a1adfd-e723-3f1d-96e7-87d15a5ba503 | -12.98266 | -54.82223 | 2025-09-06 04:40:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b03026ac-a742-3b46-9670-dc4bf1b4a313 | -13.84125 | -46.27172 | 2025-09-06 04:40:00 | NOAA-20 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| f71256bf-a701-366b-90ed-bee89fad734e | -15.58323 | -52.90433 | 2025-09-06 04:40:00 | NOAA-20 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| eb476dce-2cf5-399c-aa8c-a5c5b9382e20 | -13.27578 | -46.81393 | 2025-09-06 04:40:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| ad7eff34-cd9e-3d26-8d22-9f0c47a4a31d | -11.36287 | -50.3009 | 2025-09-06 04:40:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| fe17e386-bfb4-3aaf-bdbb-cb38bf9018d2 | -11.63615 | -52.23175 | 2025-09-06 04:40:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1bac1a66-6bb5-3d5b-b224-5b56466c3147 | -12.85136 | -48.01743 | 2025-09-06 04:40:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 06ef772a-9aa2-3bf6-805c-087bac1d0fd3 | -13.32459 | -51.7248 | 2025-09-06 04:40:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6fff2b01-ce0d-3eac-a432-ba03e46d337a | -15.0232 | -49.25368 | 2025-09-06 04:40:00 | NOAA-20 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ba99f9de-abfe-3f8c-9c7d-83d228ba78ab | -15.84193 | -52.29753 | 2025-09-06 04:40:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e80004e9-e2ff-356c-8347-71655544aecc | -11.13442 | -46.3491 | 2025-09-06 04:40:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 387c8e8f-c2d6-32dc-bbf1-540da234a0ce | -15.22731 | -52.35645 | 2025-09-06 04:40:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 684126b8-fd2e-3400-97cd-a3e0fcef647c | -12.96432 | -54.79536 | 2025-09-06 04:40:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0ae104d9-bec4-381a-8de3-8ef0b34e46aa | -10.23693 | -50.5504 | 2025-09-06 04:40:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ef3fc517-678d-3157-8e18-54547a94f804 | -12.69123 | -44.97433 | 2025-09-06 04:40:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 65857eaa-6ebc-3d36-b2e4-621c2600d648 | -12.95927 | -54.78046 | 2025-09-06 04:40:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 033072a1-a7f2-3d5c-9020-3db7bc135178 | -15.72377 | -53.60128 | 2025-09-06 04:40:00 | NOAA-20 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 08a5014d-c31d-34bc-ac1e-b27650f40dd3 | -10.74631 | -48.18409 | 2025-09-06 04:40:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 440694bd-d4bc-397d-a8dd-7545cdf3b47a | -15.60216 | -52.91536 | 2025-09-06 04:40:00 | NOAA-20 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 50435246-1a12-3298-bd77-1cd0186f9220 | -15.23164 | -52.37199 | 2025-09-06 04:40:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5f414571-9104-30fd-a892-f61ecae00f7c | -15.23439 | -52.37616 | 2025-09-06 04:40:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b99bcb86-51a7-3beb-aa1d-4927faf8c3ec | -14.90268 | -49.45293 | 2025-09-06 04:40:00 | NOAA-20 | ITAPACI | GOIÁS | Brasil | 5210901 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c90f0836-a3ef-3bff-b2d7-740d8f13e045 | -11.21563 | -55.01651 | 2025-09-06 04:40:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9dec0b3f-8c85-3acf-9fea-a83f6db0f0dc | -12.85424 | -47.99746 | 2025-09-06 04:40:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c87f092d-6106-3914-ae25-3c62d9bb64a7 | -11.01621 | -45.93318 | 2025-09-06 04:40:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 35763ad2-98d0-3ce7-8931-a72f7c7314fc | -12.78725 | -48.16225 | 2025-09-06 04:40:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c5152952-c261-33bf-82f9-cc5bcfd79749 | -14.56628 | -48.01669 | 2025-09-06 04:40:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 747d4f19-5c5b-37a9-8fe6-8f0c0789e108 | -10.46832 | -53.6209 | 2025-09-06 04:40:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fd4b96ec-c568-32cb-b5f0-f511391eb328 | -11.09773 | -52.04878 | 2025-09-06 04:40:00 | NOAA-20 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bb17a11e-7e6c-3fd6-972a-7543bf65a654 | -12.94707 | -46.56563 | 2025-09-06 04:40:00 | NOAA-20 | NOVO ALEGRE | TOCANTINS | Brasil | 1715150 | 17 | 33 | nan | nan | nan | Cerrado | 19.1 |
| 111e3528-db81-3f35-939c-deb004e1fd8b | -11.01049 | -45.91707 | 2025-09-06 04:40:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| db8759ea-0e04-3ba8-8488-e411dc5e56a4 | -14.57822 | -48.03658 | 2025-09-06 04:40:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 52769b2b-8989-30dc-9d46-af77390efddf | -12.09014 | -45.69456 | 2025-09-06 04:40:00 | NOAA-20 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 9f0948e7-b335-3934-9031-a2f1c79dfd5d | -15.17438 | -52.39191 | 2025-09-06 04:40:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3103e929-8c68-3a98-b6ca-6bb2d8631b5a | -14.109 | -51.72776 | 2025-09-06 04:40:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ac1fad2b-c3ef-3500-b86b-aa104f325e43 | -11.60732 | -52.17402 | 2025-09-06 04:40:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 9875a80b-d3e6-37e1-b125-7172682d3352 | -12.9464 | -46.57051 | 2025-09-06 04:40:00 | NOAA-20 | NOVO ALEGRE | TOCANTINS | Brasil | 1715150 | 17 | 33 | nan | nan | nan | Cerrado | 19.1 |
| 4e964eec-1773-3031-9f8d-0e2ad2cebde2 | -9.97558 | -51.65603 | 2025-09-06 04:40:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 1706996a-a86d-3248-9098-f9745d96d9ba | -16.92045 | -45.74843 | 2025-09-06 04:40:00 | NOAA-20 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2da0ece0-3daa-31f6-804e-1092fb3ea025 | -13.26814 | -46.81277 | 2025-09-06 04:40:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 860540e6-f52d-38f1-8b3b-433fe7f71d0e | -12.98955 | -54.80465 | 2025-09-06 04:40:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 46ec5d71-cdbf-3888-a998-c2d544a251c0 | -11.17729 | -55.04831 | 2025-09-06 04:40:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f272f145-9ddb-3a31-b3ee-82487a5f5880 | -13.84195 | -46.26646 | 2025-09-06 04:40:00 | NOAA-20 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 0cc91a16-f886-39b1-a4d7-2bfe3e0512ca | -12.97147 | -54.82029 | 2025-09-06 04:40:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| c549ffa3-8f46-3b2d-88d4-6d0dacc71d7f | -14.17992 | -53.06874 | 2025-09-06 04:40:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 5.4 |
| be15e0d6-7e37-3d18-bc3c-89f1454684d0 | -14.18673 | -53.0699 | 2025-09-06 04:40:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 86d96361-0e91-3be2-85b9-505bfad1a2f6 | -12.5308 | -48.0637 | 2025-09-06 04:40:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| b5b8a4e8-3fde-30ae-ab41-3534368c5ff9 | -12.51075 | -53.85477 | 2025-09-06 04:40:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| b7955f6b-20af-338c-a205-be20c7edd8e3 | -11.81592 | -51.42839 | 2025-09-06 04:40:00 | NOAA-20 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f4193d5a-80a0-3d6f-852a-c364900fc0c5 | -16.30126 | -50.48256 | 2025-09-06 04:40:00 | NOAA-20 | SANCLERLÂNDIA | GOIÁS | Brasil | 5219001 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bfe63367-4923-3a2a-972c-2ce11b8d1c91 | -12.95905 | -54.77337 | 2025-09-06 04:40:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 6967874a-4f2d-3589-af10-e55595c4c62c | -12.47262 | -48.09323 | 2025-09-06 04:40:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d190368e-0cf8-3add-a23a-4e60cf75000f | -14.34357 | -60.3264 | 2025-09-06 04:40:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c28a428c-8034-3bcd-838e-a65d63331704 | -11.6393 | -54.54386 | 2025-09-06 04:40:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 05f60231-fcc7-380d-9213-c5b5d7a3595c | -11.68239 | -52.16742 | 2025-09-06 04:40:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f39e790f-254b-3a58-bc60-562234669c7f | -12.90604 | -48.01733 | 2025-09-06 04:40:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b5dc28c5-d1f8-30ea-87d3-3fe83300e78f | -11.40427 | -43.59774 | 2025-09-06 04:40:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 68b62bab-221d-30b7-8632-84095e50bc46 | -16.33266 | -52.95678 | 2025-09-06 04:40:00 | NOAA-20 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| b4964255-3869-31ea-8d4a-cc0c68a8cccc | -12.64074 | -56.98493 | 2025-09-06 04:40:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 497b9d1f-55f5-3b1e-a2bd-b27f46c9aec2 | -9.46365 | -60.51744 | 2025-09-06 04:40:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bfb08d08-36b5-366e-bb5d-629fbd77138d | -9.23724 | -57.07075 | 2025-09-06 04:40:00 | NOAA-20 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0d190337-cd33-38eb-a95f-67638187fb5f | -14.11904 | -51.7075 | 2025-09-06 04:40:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 159eb278-54de-322b-af80-5bc4520c8f3c | -15.03011 | -49.25476 | 2025-09-06 04:40:00 | NOAA-20 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| be6511c8-4c5b-33f7-a2c9-ff11ce96ad48 | -10.76627 | -48.277 | 2025-09-06 04:40:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0294b8e7-ac26-3b21-97d9-50d6acd5c0c9 | -9.68126 | -51.09452 | 2025-09-06 04:40:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c0682238-fe32-3787-8235-ce32f015ef43 | -11.02668 | -52.0524 | 2025-09-06 04:40:00 | NOAA-20 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 17f8fd1f-cbaa-3dd2-849a-7aac99fa3f0f | -9.231 | -57.07932 | 2025-09-06 04:40:00 | NOAA-20 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| bb0e08bc-94fa-315e-bde3-e1340e36e307 | -17.26108 | -49.0024 | 2025-09-06 04:40:00 | NOAA-20 | PIRACANJUBA | GOIÁS | Brasil | 5217104 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 51ea7b2f-9a9f-3a1f-9369-94a9d8d55b03 | -13.0052 | -54.8029 | 2025-09-06 04:40:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fffbca72-0833-38d2-8791-2468cfed3187 | -16.32166 | -52.93984 | 2025-09-06 04:40:00 | NOAA-20 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| cf54204c-118e-34eb-add8-f0d72c499a5a | -11.30393 | -50.28789 | 2025-09-06 04:40:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f0185ecf-ceb8-346e-8306-a6b0f70a1dd2 | -11.20405 | -55.06013 | 2025-09-06 04:40:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 4e1fa521-daee-3919-bd04-e03953b3cd43 | -9.70619 | -49.01402 | 2025-09-06 04:40:00 | NOAA-20 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3915bfaf-a9fd-362e-964f-8e1b6e3bf820 | -10.06875 | -48.05721 | 2025-09-06 04:40:00 | NOAA-20 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 9b62022a-adf7-30d5-91d0-67ddbb95f4e2 | -11.16436 | -59.15106 | 2025-09-06 04:40:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5033c4b4-3055-3253-85c3-e6f3c18accf4 | -15.72609 | -53.56623 | 2025-09-06 04:40:00 | NOAA-20 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 21276a0f-6114-3ac3-a3c5-fedd099f5c3e | -15.57988 | -52.90368 | 2025-09-06 04:40:00 | NOAA-20 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 668468a0-8997-3bf9-98e9-e4eac589b4db | -13.92798 | -53.99119 | 2025-09-06 04:40:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 2887c7a2-d78a-3677-a40a-df480c48ef34 | -9.69419 | -51.05663 | 2025-09-06 04:40:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bca9a2b0-13ff-35fd-acf0-46710242079f | -12.94593 | -46.56339 | 2025-09-06 04:40:00 | NOAA-20 | NOVO ALEGRE | TOCANTINS | Brasil | 1715150 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 0d1c9c63-fd69-3134-a663-4c75ddde889c | -15.22391 | -53.77453 | 2025-09-06 04:40:00 | NOAA-20 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 59556fe5-94e1-3d52-96e8-a43b3bdc6de5 | -9.74804 | -51.06174 | 2025-09-06 04:40:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 714d26cf-d6c6-38de-93e7-23cc77a22d31 | -15.18006 | -52.37791 | 2025-09-06 04:40:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 05053cca-7fb7-3497-aa2d-cd140d02d292 | -12.96034 | -54.81108 | 2025-09-06 04:40:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 7cf89c7c-e114-33c0-97e1-baf651759a07 | -13.84525 | -46.27215 | 2025-09-06 04:40:00 | NOAA-20 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 7655d76d-8d54-348c-827c-3a54a1f94b6d | -13.7325 | -46.91512 | 2025-09-06 04:40:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0f78e6c0-44f3-3185-a41a-37355cbbedfa | -9.69085 | -51.0561 | 2025-09-06 04:40:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 85ab4285-e558-3c83-bb05-35f83041c47d | -11.02776 | -52.05219 | 2025-09-06 04:40:00 | NOAA-20 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 18ac0e21-ab2b-3a83-829c-22e43d6ad976 | -15.73405 | -53.60301 | 2025-09-06 04:40:00 | NOAA-20 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c6dabc62-9324-36d1-acd6-645a4d8dffeb | -11.62441 | -52.21844 | 2025-09-06 04:40:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 6b395096-a7c1-3221-a8a6-32ffb0b1a4b8 | -16.32441 | -52.94409 | 2025-09-06 04:40:00 | NOAA-20 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2a690c34-d7d1-397b-bbdc-7dfdce3d1e9c | -14.96375 | -47.58998 | 2025-09-06 04:40:00 | NOAA-20 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 004e6c00-a9be-3956-8a1e-3e58edf35bf0 | -12.95381 | -54.78169 | 2025-09-06 04:40:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0e5c8c6a-44bb-3455-a19b-65b5bfa89a87 | -12.976 | -54.81635 | 2025-09-06 04:40:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7fca1e29-fa8f-3290-a9c8-25350021c664 | -11.93391 | -46.67291 | 2025-09-06 04:40:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d9fef5ad-9874-3328-bb81-3eb48c175dc3 | -11.54161 | -47.31554 | 2025-09-06 04:40:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 891d084c-a8f1-3003-b51b-5ab31be49494 | -11.53796 | -47.31502 | 2025-09-06 04:40:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |


[Clique aqui para ver as próximas entradas](README75.md)
