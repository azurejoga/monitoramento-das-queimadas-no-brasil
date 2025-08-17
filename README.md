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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 06f44c7c-939b-3a4e-a44a-e3b24c48b708 | -4.912 | -43.2337 | 2025-08-17 00:00:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 68.5 |
| 88a73842-f846-38bb-ab0f-5cddc00e994f | -18.7582 | -45.0625 | 2025-08-17 00:00:00 | GOES-19 | FELIXLÂNDIA | MINAS GERAIS | Brasil | 3125705 | 31 | 33 | nan | nan | nan | Cerrado | 111.5 |
| 198ca693-42fa-3fc4-890f-113ef732f3e4 | -9.518 | -60.5268 | 2025-08-17 00:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 121.3 |
| a3f57100-45d6-32aa-9579-8e587fe0a4bc | -9.4994 | -60.5278 | 2025-08-17 00:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 78.5 |
| 21199b11-3922-30d8-b995-d3fe17003a8c | -9.1709 | -59.6374 | 2025-08-17 00:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 50.9 |
| fbe32f52-8a11-3a0e-9c65-ffdd207afef8 | -18.7575 | -45.0866 | 2025-08-17 00:00:00 | GOES-19 | FELIXLÂNDIA | MINAS GERAIS | Brasil | 3125705 | 31 | 33 | nan | nan | nan | Cerrado | 156.9 |
| cf5c9d6c-33ba-38f4-8848-d194a870a67a | -9.5179 | -60.5461 | 2025-08-17 00:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 116.3 |
| 06117fc1-7709-3329-89e2-5528b8f18b6a | -9.1895 | -59.6364 | 2025-08-17 00:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 77.0 |
| a0ea8d91-bb9b-36da-bf23-e4af53698910 | -9.4991 | -60.5663 | 2025-08-17 00:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 54.7 |
| c2358fd4-bea2-36f7-823d-fd4b3259e7c8 | -9.1894 | -59.6558 | 2025-08-17 00:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 61.3 |
| c3a42b8f-112d-38d0-9658-eed2a2d3f075 | -9.5177 | -60.5653 | 2025-08-17 00:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 53.5 |
| b37140cc-1905-37fb-9594-fada1e84ad2e | -8.034 | -47.6639 | 2025-08-17 00:00:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 42.8 |
| 00500432-9613-3cb4-a0c1-26041aa84b30 | -8.9974 | -60.4955 | 2025-08-17 00:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 50.9 |
| 62cc7c89-95f6-3078-84b0-98949e2e6b74 | -10.3064 | -52.5528 | 2025-08-17 00:00:00 | GOES-19 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 64.2 |
| 9579856c-edb3-3bf5-8075-1647f92b9c25 | -4.9307 | -43.2324 | 2025-08-17 00:00:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 69.5 |
| d20bb8e0-9639-3006-a07d-850ce67a1186 | -9.4992 | -60.547 | 2025-08-17 00:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 86.6 |
| 55b465eb-f238-3a4b-88d0-83cbb73e764c | -9.1708 | -59.6568 | 2025-08-17 00:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 47.5 |
| 676b78e9-d9cb-3a3a-9c82-c7f845125fd9 | -6.1859 | -47.2845 | 2025-08-17 00:00:00 | GOES-19 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 39.2 |
| 44252477-efbf-324f-84c3-743fd7dd1197 | -6.1838 | -45.4371 | 2025-08-17 00:00:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 61.4 |
| be7c24c5-6252-3a68-87f6-da4bfd55d094 | -6.545 | -43.0373 | 2025-08-17 00:00:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 82.7 |
| 67c0560d-7013-3c36-bce1-ccce60c17a72 | -9.2082 | -59.6354 | 2025-08-17 00:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 52.5 |
| 02bcef81-e5af-3cd3-871c-6f179e595c6d | -8.9788 | -60.4964 | 2025-08-17 00:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 100.9 |
| 86b35e61-8bf1-3010-8f74-ecdbf34bc2fd | -4.9118 | -43.257 | 2025-08-17 00:00:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 153.6 |
| 381f1546-d33c-3a4d-a371-b7291ba0de01 | -6.1672 | -47.2858 | 2025-08-17 00:00:00 | GOES-19 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 39.6 |
| 89ae8ac0-2ea4-368c-88af-65cf8849384e | -6.128 | -57.9367 | 2025-08-17 00:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 47.6 |
| e11dc6a0-b52a-3568-824e-8504a9aa0839 | -4.9305 | -43.2558 | 2025-08-17 00:00:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 151.6 |
| ce2ac985-130e-377f-b4ef-e3900a689323 | -8.9787 | -60.5156 | 2025-08-17 00:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 52.7 |
| 5de0b81f-3dd6-385a-8e13-383e15906efe | -15.1869 | -48.7894 | 2025-08-17 00:10:00 | GOES-19 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 60.2 |
| 26f73f5b-50b3-3b3a-bd5d-201cdd78a0ad | -9.1708 | -59.6568 | 2025-08-17 00:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 47.6 |
| b2bdda02-f65b-393b-888f-ff4f56d338e1 | -6.1838 | -45.4371 | 2025-08-17 00:10:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 64.3 |
| 46756f2c-2c73-3797-a62a-3cc7c01bb2ed | -9.4994 | -60.5278 | 2025-08-17 00:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 73.7 |
| b6e27a5b-eb75-3065-bcc3-b6da724fcd7e | -15.1674 | -48.7926 | 2025-08-17 00:10:00 | GOES-19 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 58.4 |
| a3ced8ae-8768-379f-98d9-a3afc69a99cb | -9.1709 | -59.6374 | 2025-08-17 00:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 47.7 |
| bee77029-d9e1-3343-b8cc-455dd79c09cd | -6.545 | -43.0373 | 2025-08-17 00:10:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 76.2 |
| f985f64f-5b56-33e9-b116-38b75260be48 | -15.1873 | -48.7671 | 2025-08-17 00:10:00 | GOES-19 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 79.9 |
| 19aa76c8-f0ba-3434-885c-28b9122014a4 | -20.3643 | -47.6596 | 2025-08-17 00:10:00 | GOES-19 | ITUVERAVA | SÃO PAULO | Brasil | 3524105 | 35 | 33 | nan | nan | nan | Cerrado | 55.8 |
| f971014d-28ca-3aa5-946f-5edd0296e611 | -14.9251 | -54.6774 | 2025-08-17 00:10:00 | GOES-19 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 73.5 |
| 936d1c1e-1f72-3cc0-98e9-3a10a8fb6887 | -9.2082 | -59.6354 | 2025-08-17 00:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 48.1 |
| 12e71490-245c-3ccb-a8dd-804ec0bfb450 | -9.5179 | -60.5461 | 2025-08-17 00:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 73.5 |
| d8bace02-206c-3860-85f7-a071b637cef7 | -14.9445 | -54.6751 | 2025-08-17 00:10:00 | GOES-19 | PRIMAVERA DO LESTE | MATO GROSSO | Brasil | 5107040 | 51 | 33 | nan | nan | nan | Cerrado | 83.7 |
| 4aa386ad-41c6-3922-bad7-768fc5e521f8 | -9.518 | -60.5268 | 2025-08-17 00:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 100.2 |
| 507975c0-0f73-3592-bc0a-b0a49eff1a04 | -9.4991 | -60.5663 | 2025-08-17 00:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 45.6 |
| 8dcdb101-1dee-3a4a-be7d-3c0fe9aaa603 | -11.366 | -55.3904 | 2025-08-17 00:10:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 64.7 |
| ed9ef786-de3d-38fa-817e-18202875ee73 | -4.9118 | -43.257 | 2025-08-17 00:10:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 154.8 |
| 876c3e1b-a101-3898-91f7-fb0a2b48a460 | -3.8209 | -47.7444 | 2025-08-17 00:10:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 62.2 |
| a0571493-75f1-3d1c-afbd-b970d905f44e | -9.4992 | -60.547 | 2025-08-17 00:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 61.9 |
| 91cb6bec-aeba-330c-abf7-72fdcbb5c591 | -9.1895 | -59.6364 | 2025-08-17 00:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 62.9 |
| 486c5101-b8ae-37e3-832e-9a4054d3fdda | -9.1894 | -59.6558 | 2025-08-17 00:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 50.4 |
| f1dadff4-0417-3907-8293-6e24a1adb9eb | -15.1678 | -48.7703 | 2025-08-17 00:10:00 | GOES-19 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 72.1 |
| beda2b8d-2dc2-372f-87f6-2eb8101eb388 | -4.9305 | -43.2558 | 2025-08-17 00:10:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 152.1 |
| 4ebfef4d-17fb-3ec0-b46a-8d29126e6244 | -8.034 | -47.6639 | 2025-08-17 00:10:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 64.7 |
| ebc97412-ce91-3a10-8385-f05e02feba34 | -9.5179 | -60.5461 | 2025-08-17 00:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 66.4 |
| 8d4dd2d1-fbab-3b57-bdcf-c26a60845c7d | -9.1895 | -59.6364 | 2025-08-17 00:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 57.1 |
| dbc81f41-50da-3002-b9a5-efecd0534612 | -9.4991 | -60.5663 | 2025-08-17 00:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 53.7 |
| 826dc01b-ca13-310c-becf-d3bfa2cc141e | -4.9118 | -43.257 | 2025-08-17 00:20:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 114.7 |
| 610c49b6-84d7-3333-878a-78e4c58c52e2 | -8.034 | -47.6639 | 2025-08-17 00:20:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 55.2 |
| 323aef93-97d8-384f-8d82-a9e2695b52aa | -10.4617 | -55.4251 | 2025-08-17 00:20:00 | GOES-19 | COLÍDER | MATO GROSSO | Brasil | 5103205 | 51 | 33 | nan | nan | nan | Amazônia | 158.4 |
| e109af9b-27ed-397a-8c04-bd31d5e70949 | -9.1894 | -59.6558 | 2025-08-17 00:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 48.6 |
| 87d663e5-55db-3f43-b154-24b415aa4208 | -10.4427 | -55.4468 | 2025-08-17 00:20:00 | GOES-19 | COLÍDER | MATO GROSSO | Brasil | 5103205 | 51 | 33 | nan | nan | nan | Amazônia | 77.1 |
| 6bb9b8b3-56d9-3cc2-bf07-76e858aa4cd3 | -4.9307 | -43.2324 | 2025-08-17 00:20:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 70.9 |
| 75a41fc9-94f4-356b-a19f-ba795c8e2225 | -9.518 | -60.5268 | 2025-08-17 00:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 69.0 |
| 0367f00e-42ce-3d7d-896b-f779695d5ccd | -9.4992 | -60.547 | 2025-08-17 00:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 51.6 |
| 7eefe809-f6c9-38ee-8707-a89a724c6582 | -8.9788 | -60.4964 | 2025-08-17 00:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 61.6 |
| 9d9246ee-f667-3d75-8345-0d283ab62f75 | -10.4429 | -55.4266 | 2025-08-17 00:20:00 | GOES-19 | COLÍDER | MATO GROSSO | Brasil | 5103205 | 51 | 33 | nan | nan | nan | Amazônia | 292.3 |
| 76814b32-09cc-3f11-af49-8100206ba17d | -4.9305 | -43.2558 | 2025-08-17 00:20:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 162.1 |
| 66bc7c6a-c995-3c38-8454-b13349e49025 | -14.9251 | -54.6774 | 2025-08-17 00:20:00 | GOES-19 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 83.4 |
| ee6ce7ba-2ed7-381d-832b-3f56a08ea70e | -14.9445 | -54.6751 | 2025-08-17 00:20:00 | GOES-19 | PRIMAVERA DO LESTE | MATO GROSSO | Brasil | 5107040 | 51 | 33 | nan | nan | nan | Cerrado | 82.2 |
| 3c63c542-b4cf-3131-90ca-780971e4061d | -10.8444 | -45.3126 | 2025-08-17 00:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 54.9 |
| 03febd80-4ead-3184-8da3-223d6b0ecf0a | -6.0671 | -44.628201 | 2025-08-17 00:26:00 | METOP-B | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 64df2859-b07f-3eac-910b-3d6e54fdae86 | -11.4302 | -52.213001 | 2025-08-17 00:26:00 | METOP-B | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 12e88672-6869-353a-8ad3-a333c9963a3c | -16.6336 | -51.371399 | 2025-08-17 00:26:00 | METOP-B | PALESTINA DE GOIÁS | GOIÁS | Brasil | 5215652 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 363c850e-ebad-3af0-8632-97ddc8d82536 | -6.6116 | -43.872002 | 2025-08-17 00:26:00 | METOP-B | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| acffc6ba-eb5d-3a70-992a-aab13bfe4dc7 | -16.8419 | -48.904701 | 2025-08-17 00:26:00 | METOP-B | BELA VISTA DE GOIÁS | GOIÁS | Brasil | 5203302 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| caed43dc-40ca-324e-ac1a-91140e332249 | -6.1723 | -47.2626 | 2025-08-17 00:26:00 | METOP-B | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 81727c5a-9193-3abc-9748-bd1cc0bcfc49 | -14.9384 | -54.687599 | 2025-08-17 00:26:00 | METOP-B | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 75323c76-1b04-34f8-a58b-c09238c7b027 | -10.8438 | -45.300499 | 2025-08-17 00:26:00 | METOP-B | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 2e09a999-cc62-3c3e-96bd-5c1e9e441fc8 | -8.5073 | -44.727501 | 2025-08-17 00:26:00 | METOP-B | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 8bf79187-a166-36e6-8ef0-1b7e1cd787cf | -4.0773 | -48.028702 | 2025-08-17 00:26:00 | METOP-B | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c695204d-bad0-38f8-9c09-b72df82103df | -17.414301 | -48.110199 | 2025-08-17 00:26:00 | METOP-B | URUTAÍ | GOIÁS | Brasil | 5221809 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 10d95317-14d9-3088-b09e-bc25be610dc9 | -3.8246 | -47.738201 | 2025-08-17 00:26:00 | METOP-B | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d26d46fb-a909-3ca0-8002-5563578ff80e | -16.4911 | -45.099998 | 2025-08-17 00:26:00 | METOP-B | PONTO CHIQUE | MINAS GERAIS | Brasil | 3152131 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 0800081d-a724-3eec-badf-c7394f6ee70a | -3.4499 | -48.963799 | 2025-08-17 00:26:00 | METOP-B | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 18b48391-e355-3812-ba61-ca4f825dcfc3 | -10.8338 | -45.343899 | 2025-08-17 00:26:00 | METOP-B | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 504389e7-591e-3f30-b81f-70a42fedba9a | -8.5193 | -47.209099 | 2025-08-17 00:26:00 | METOP-B | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| c284b94c-eac0-3f6b-b4e5-7866dde92d66 | -20.4853 | -49.351398 | 2025-08-17 00:26:00 | METOP-B | NOVA GRANADA | SÃO PAULO | Brasil | 3533007 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 41ddf42c-47d3-3daf-9cc4-48a0f98ae616 | -8.804 | -52.0662 | 2025-08-17 00:26:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4bdd2d6b-0394-351f-a98b-20bbdfa0c7f7 | -6.1315 | -57.9249 | 2025-08-17 00:26:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ab34b49f-3754-356c-b23e-ac6c1ce0356a | -11.3139 | -55.2043 | 2025-08-17 00:26:00 | METOP-B | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 47ae6eed-e1ac-3fba-8803-9aceafcab4b0 | -4.0798 | -48.039398 | 2025-08-17 00:26:00 | METOP-B | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8f5f5f56-284b-32b1-9f66-96cd1a92c2ae | -14.9346 | -54.669102 | 2025-08-17 00:26:00 | METOP-B | PRIMAVERA DO LESTE | MATO GROSSO | Brasil | 5107040 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 13589883-796b-3c97-9998-800d939529b0 | -4.9236 | -43.252899 | 2025-08-17 00:26:00 | METOP-B | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f51ce641-4939-371e-bf28-35fd4d2de240 | -6.1291 | -57.914101 | 2025-08-17 00:26:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3e92e825-479a-3ccc-a5c5-95a603ea87f5 | -14.5992 | -47.949902 | 2025-08-17 00:26:00 | METOP-B | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 93c3f53e-3bd0-31c8-9222-396e0d04e03a | -15.185 | -48.785999 | 2025-08-17 00:26:00 | METOP-B | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 7c65bbd0-a829-3fd9-a4b9-b9686f4c1494 | -14.981 | -54.746399 | 2025-08-17 00:26:00 | METOP-B | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 1d258b06-0048-3f1f-aa22-85494e8bcb4b | -14.9365 | -54.678299 | 2025-08-17 00:26:00 | METOP-B | PRIMAVERA DO LESTE | MATO GROSSO | Brasil | 5107040 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 0bcf3de7-8a66-30f2-ae57-acf6f0e2ea5f | -7.1401 | -44.647701 | 2025-08-17 00:26:00 | METOP-B | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| fe4f6af1-c96d-3cf8-8881-ee9174b34e09 | -13.5664 | -46.9883 | 2025-08-17 00:26:00 | METOP-B | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 9e403040-665d-3a7a-bd87-52341086f613 | -6.1776 | -47.285099 | 2025-08-17 00:26:00 | METOP-B | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 17a37f5c-bc1b-3561-afc0-afe77430ec26 | -10.8306 | -45.3311 | 2025-08-17 00:26:00 | METOP-B | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README2.md)
