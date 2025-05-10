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

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9f59d3a9-7f68-369e-808c-ba97a689b50c | -13.09445 | -52.29047 | 2025-05-10 04:49:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| f58ec91b-cfcf-3c7a-af2b-1c3582680269 | -11.40271 | -52.94918 | 2025-05-10 04:49:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 354b8cbe-c5de-3ecf-bea8-c9b1a0f2fa57 | -12.6852 | -58.13723 | 2025-05-10 04:49:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| d66d3246-f0aa-3114-9fda-803d8a0458d8 | -11.38557 | -52.93872 | 2025-05-10 04:49:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 2234196c-5cbd-339e-88e0-b0ef3389ab3b | -11.38835 | -52.94283 | 2025-05-10 04:49:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 71de3a95-7f66-3c47-bb75-b8ade3d17d20 | -12.63296 | -54.06385 | 2025-05-10 04:49:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 644902ce-0543-39e7-947a-5e801b4e1930 | -11.14531 | -54.2282 | 2025-05-10 04:49:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 76623803-f9f6-36b5-b501-b4fdd41ba9bd | -10.99315 | -44.43753 | 2025-05-10 04:49:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 8af535f4-9964-39ad-8ac7-9862e9d584ee | -13.97954 | -56.80605 | 2025-05-10 04:49:00 | NPP-375D | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 19.7 |
| 60cdf0bf-f4b5-33fb-bca8-65f4363462aa | -8.69364 | -64.1459 | 2025-05-10 04:49:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f8424cad-e1fe-3cf1-a3f7-3240e1fe3627 | -11.38892 | -52.93928 | 2025-05-10 04:49:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 49013315-3729-3c4d-8957-b15254d028ad | -11.77453 | -48.70389 | 2025-05-10 04:49:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0ad2b465-9deb-31ef-86d6-ccfd567c4934 | -11.14185 | -54.22762 | 2025-05-10 04:49:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b35ded04-7b34-3992-b208-5944d49f3877 | -13.04809 | -53.72501 | 2025-05-10 04:49:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 45a06bbe-0723-39f9-b958-45a0749e74a4 | -12.36821 | -63.91968 | 2025-05-10 04:49:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a49825c0-72ac-368d-b5c7-cc1422b05ccd | -12.69111 | -58.12942 | 2025-05-10 04:49:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| da0b1bb9-b602-3aaa-b757-c0bcd6a6208f | -13.62233 | -54.8857 | 2025-05-10 04:49:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3d0700d5-3d38-3974-8dfa-2ba58f91823f | -13.05263 | -53.71832 | 2025-05-10 04:49:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ba322354-f1a8-312b-bb2a-b2943dddcee4 | -13.04413 | -53.72806 | 2025-05-10 04:49:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| dd7b65af-55fe-3168-8e10-39deeca26172 | -11.37512 | -55.12251 | 2025-05-10 04:49:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 66204d91-8ca7-36e0-9114-399ceaf25638 | -12.37428 | -63.92102 | 2025-05-10 04:49:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 40c7aff8-85f5-3ffb-b843-18a9a1a87d4e | -13.04868 | -53.72137 | 2025-05-10 04:49:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 234fb82f-c80b-3137-84e1-2ba2f638af4a | -11.30553 | -54.01772 | 2025-05-10 04:49:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4fda26b2-b3f1-37fe-b1a0-5f0610e8c625 | -11.97213 | -63.52904 | 2025-05-10 04:49:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| da315bb7-9499-3ca7-a2e7-ab08b8c1dd43 | -10.67142 | -44.37521 | 2025-05-10 04:49:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e6fe3121-1984-3ae8-b288-75a82b202ba4 | -8.7002 | -64.14722 | 2025-05-10 04:49:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a6cdbf12-8234-35b7-b189-3ff455a47cc8 | -12.63575 | -54.06815 | 2025-05-10 04:49:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ceb8b9a8-640e-3e24-80a9-f1e34d376a85 | -13.05145 | -53.72558 | 2025-05-10 04:49:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4eaddf0d-68b8-3407-b57c-ac7bd10b0188 | -12.64595 | -54.06987 | 2025-05-10 04:49:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ee302bc4-283a-376a-adf6-3e943a68c52c | -12.69072 | -58.13028 | 2025-05-10 04:49:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2485f87c-b9b7-3a58-99b4-3b633e33ef8e | -14.64634 | -45.13448 | 2025-05-10 04:49:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2ec3146f-acd2-3741-a2ea-9e80df253fea | -13.37888 | -54.2638 | 2025-05-10 04:49:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4fec201e-cdb9-39af-b90e-50da964f9246 | -9.77884 | -50.88337 | 2025-05-10 04:49:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3d240be9-4509-3b6b-9908-a3b0c51ae849 | -13.04472 | -53.72443 | 2025-05-10 04:49:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 3212dfc9-7dc7-3422-9ad8-2cd9a216ab84 | -11.15151 | -48.67231 | 2025-05-10 04:49:00 | NPP-375D | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5a98efca-71d9-3843-82e5-1465fb3d5892 | -13.09389 | -52.29403 | 2025-05-10 04:49:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 481c6436-80ee-3990-a2f1-8fce9366e41a | -14.65051 | -45.14056 | 2025-05-10 04:49:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e6580fbb-3ae1-36e7-b5ec-4cd48402504c | -12.35787 | -54.5214 | 2025-05-10 04:49:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 377c0540-d539-39e6-bccf-009ed23c4f67 | -12.64996 | -54.06673 | 2025-05-10 04:49:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bc621808-a0e8-31bc-80b7-cc13be328ad0 | -11.37939 | -55.11902 | 2025-05-10 04:49:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 03f4bdb3-628f-3694-9cf8-9d320a0574e7 | -13.05204 | -53.72195 | 2025-05-10 04:49:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ea3203fe-9575-3750-9332-d3a1fa6d2d3b | -12.64935 | -54.07045 | 2025-05-10 04:49:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8709194c-3306-35ab-b885-4f6e9536d11d | -13.0554 | -53.72253 | 2025-05-10 04:49:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9487d6c7-856a-35a1-ab89-2164b84ebfcf | -11.83298 | -51.34029 | 2025-05-10 04:49:00 | NPP-375D | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8e0df026-605a-3520-ac5a-9b7cb7323fb2 | -12.64656 | -54.06615 | 2025-05-10 04:49:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 32d3ea9c-e4c6-3589-9c2b-8623854ce17e | -12.68553 | -58.13636 | 2025-05-10 04:49:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 74cff511-6740-3d38-9ef5-c7fd25108a9f | -12.69041 | -58.13325 | 2025-05-10 04:49:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ef1a2c25-0831-3862-aed1-11fedce95fc7 | -13.04531 | -53.7208 | 2025-05-10 04:49:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 02353a55-c57d-34c2-8474-f65ed4ea9c26 | -14.31185 | -54.64799 | 2025-05-10 04:49:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| dd999e1a-dce6-3359-ba5e-50841f08c74e | -13.61887 | -54.88509 | 2025-05-10 04:49:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b365d479-00fc-3fa3-bedd-300156d541ee | -14.64285 | -45.12296 | 2025-05-10 04:49:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f4626cca-8fed-323a-8bfb-bb89ac8e5b2c | -11.40115 | -52.9486 | 2025-05-10 04:49:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 53a65b22-62b9-3150-b174-6304f8333d53 | -13.23322 | -56.80407 | 2025-05-10 04:49:00 | NPP-375D | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 63a1f49a-a48a-331d-b9c1-d763396ba6ae | -10.98831 | -44.43694 | 2025-05-10 04:49:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c67f5b3f-6a0c-3687-812a-ca6ebbbccd5a | -12.68238 | -58.12878 | 2025-05-10 04:49:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7f657ad3-bad1-3a2b-bc6a-4d251398fbd3 | -11.07179 | -46.12456 | 2025-05-10 04:49:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fc014c0a-8cf5-3f11-9df1-fb6bbf084e7b | -12.68694 | -58.12867 | 2025-05-10 04:49:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ffed4027-a2f1-3a9d-b97c-06313a68eeaa | -19.0624 | -53.44338 | 2025-05-10 04:51:00 | NPP-375D | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6a3de067-2654-3c03-b1f0-acd651477133 | -21.19763 | -41.30228 | 2025-05-10 04:51:00 | NPP-375D | MIMOSO DO SUL | ESPÍRITO SANTO | Brasil | 3203403 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 5592f933-be63-3167-b8e6-e44062e5d3d0 | -18.95764 | -52.24886 | 2025-05-10 04:51:00 | NPP-375D | CASSILÂNDIA | MATO GROSSO DO SUL | Brasil | 5002902 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6d8ca801-e7a1-32ad-bc45-d9f104bf7298 | -18.59497 | -46.55201 | 2025-05-10 04:51:00 | NPP-375D | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c25dd4e7-530e-33ce-914d-129fbc3cadee | -21.19711 | -41.30849 | 2025-05-10 04:51:00 | NPP-375D | MIMOSO DO SUL | ESPÍRITO SANTO | Brasil | 3203403 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| d9aaffb8-8990-35e7-8375-679faaa80074 | -17.53173 | -52.12037 | 2025-05-10 04:51:00 | NPP-375D | PEROLÂNDIA | GOIÁS | Brasil | 5216452 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d6610a8c-9fd7-353d-944d-70058f04f51a | -19.87476 | -46.61454 | 2025-05-10 04:51:00 | NPP-375D | IBIÁ | MINAS GERAIS | Brasil | 3129509 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| beddc8e2-dfcc-3d55-9b50-3336f403f3ce | -19.551 | -45.28873 | 2025-05-10 04:51:00 | NPP-375D | BOM DESPACHO | MINAS GERAIS | Brasil | 3107406 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ec7543e6-e719-3f65-bab0-7002b4a906f6 | -19.54911 | -45.29053 | 2025-05-10 04:51:00 | NPP-375D | BOM DESPACHO | MINAS GERAIS | Brasil | 3107406 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2eca1d44-bb0e-3ec7-883a-1c9f0f75ecdc | -16.30277 | -53.8331 | 2025-05-10 04:51:00 | NPP-375D | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 17cb76db-1000-3b83-980d-14d162cac5e6 | -18.49917 | -47.60204 | 2025-05-10 04:51:00 | NPP-375D | MONTE CARMELO | MINAS GERAIS | Brasil | 3143104 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2b331e79-d513-3f10-8f76-a774d254e533 | -21.96678 | -47.17892 | 2025-05-10 04:51:00 | NPP-375D | CASA BRANCA | SÃO PAULO | Brasil | 3510807 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1b9f78d4-69ec-3581-8d84-bc1f203981c7 | -21.78414 | -52.74186 | 2025-05-10 04:51:00 | NPP-375D | BATAGUASSU | MATO GROSSO DO SUL | Brasil | 5001904 | 50 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 8dc93cd4-e4f2-3031-8f22-827cb4f44088 | -21.77954 | -52.7492 | 2025-05-10 04:51:00 | NPP-375D | BATAGUASSU | MATO GROSSO DO SUL | Brasil | 5001904 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1ec386bb-6c79-3a45-b93b-8e6f7365b92b | -17.77527 | -42.80796 | 2025-05-10 04:51:00 | NPP-375D | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3d9adda0-1743-30bc-a1a9-d2b1fa39fa4c | -17.30005 | -47.01078 | 2025-05-10 04:51:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 95b2e33b-6425-3b48-b9fa-c9040901af8a | -17.30449 | -47.01139 | 2025-05-10 04:51:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| eb126e4f-e4f7-35b3-b384-938d4f5ce3f3 | -19.05402 | -53.45326 | 2025-05-10 04:51:00 | NPP-375D | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 45a11f4a-366d-38a5-af1b-bfdb61c6cf34 | -16.30611 | -53.83367 | 2025-05-10 04:51:00 | NPP-375D | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| dbb64bbe-fe60-30f5-9d96-1b596580a74f | -19.06404 | -53.45498 | 2025-05-10 04:51:00 | NPP-375D | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f811217e-5fd1-3e78-b367-fea42e877bd4 | -19.05736 | -53.45383 | 2025-05-10 04:51:00 | NPP-375D | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 450c9971-a1bd-3f3d-9880-c41606f7c511 | -16.68102 | -43.88234 | 2025-05-10 04:51:00 | NPP-375D | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0b6fb26a-17c1-3861-9ee2-613ebe0bb595 | -18.95933 | -52.26098 | 2025-05-10 04:51:00 | NPP-375D | CASSILÂNDIA | MATO GROSSO DO SUL | Brasil | 5002902 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 95337f18-8f21-3a75-b3bd-135cc95d1b1e | -17.78115 | -42.80873 | 2025-05-10 04:51:00 | NPP-375D | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3be9c1be-1455-3b88-adc0-974a65f87977 | -21.78356 | -52.74582 | 2025-05-10 04:51:00 | NPP-375D | BATAGUASSU | MATO GROSSO DO SUL | Brasil | 5001904 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 58e2c4dd-ee67-3924-b228-28568cd30a06 | -18.95875 | -52.26483 | 2025-05-10 04:51:00 | NPP-375D | CASSILÂNDIA | MATO GROSSO DO SUL | Brasil | 5002902 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 98f5027a-6872-363b-8562-949dc256e51b | -19.0607 | -53.45441 | 2025-05-10 04:51:00 | NPP-375D | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1f394b55-439a-3577-b239-326c242b170a | -16.68058 | -43.8863 | 2025-05-10 04:51:00 | NPP-375D | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8ba1b778-43ab-353a-9827-3242a6db5c6c | -18.95991 | -52.25713 | 2025-05-10 04:51:00 | NPP-375D | CASSILÂNDIA | MATO GROSSO DO SUL | Brasil | 5002902 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c44e2752-3eff-3352-8fa9-33f578fbcf7e | -6.9589 | -43.023 | 2025-05-10 05:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 62.7 |
| ae55961b-c390-3636-99b0-4cfc050e7d76 | -13.9902 | -56.8058 | 2025-05-10 05:10:00 | GOES-19 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 46.2 |
| 88216980-f3b5-3e25-911b-383a7eb89b23 | -10.65093 | -44.48051 | 2025-05-10 05:10:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 1b3a4377-6b8f-3f3f-ad47-4cd732b85158 | -11.14827 | -48.67938 | 2025-05-10 05:10:00 | NOAA-20 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 0d3b8cd9-3608-395a-a312-598bfec4662a | -12.68637 | -58.134 | 2025-05-10 05:10:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 36e0a961-47a7-3efd-83d5-a208c3d265a7 | -11.14296 | -54.22476 | 2025-05-10 05:10:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a7f08b2e-7dea-3180-b158-d8bdf38425bd | -12.68969 | -58.13453 | 2025-05-10 05:10:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| eeac2f27-0f1f-393e-98e5-6678cc085c73 | -9.93169 | -59.93879 | 2025-05-10 05:10:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7d5c7f03-eee0-3d49-8bb1-04f9aebbe580 | -13.05103 | -53.72252 | 2025-05-10 05:10:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 8b26e01d-c5a5-3807-bfc3-b825c1e50883 | -13.98078 | -56.81208 | 2025-05-10 05:10:00 | NOAA-20 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 15.7 |
| c336cd6a-07d2-3293-bf2c-e2e0250cdacd | -13.04649 | -53.72562 | 2025-05-10 05:10:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 9906eec4-ebb1-3d4a-9b6b-44c9b2c90b76 | -13.05153 | -53.71891 | 2025-05-10 05:10:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 51bfd18e-3387-32ad-9a9a-846b03521e59 | -11.97147 | -63.53136 | 2025-05-10 05:10:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c923ce1b-5921-3c61-ad74-0cec0a1b0beb | -12.17217 | -54.23717 | 2025-05-10 05:10:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |


[Clique aqui para ver as próximas entradas](README7.md)
