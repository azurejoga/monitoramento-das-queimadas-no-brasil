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

## Dados Diários - Página 11

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c20af2b2-fad6-35b3-9f8d-b16076ca63c5 | -9.62294 | -49.49115 | 2025-05-20 04:59:00 | NPP-375D | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b5e26b47-3232-328e-8950-571698bf1616 | -11.23626 | -49.49568 | 2025-05-20 04:59:00 | NPP-375D | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b645cd98-0d9f-3f69-9ec0-54f16b92e3ff | -13.03072 | -45.07001 | 2025-05-20 04:59:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 6af9f7f1-3f81-33d4-9536-d94029722258 | -11.0075 | -50.75858 | 2025-05-20 04:59:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| fdd303e4-6f56-32e4-9db9-2eca3ec8868b | -10.55213 | -55.62264 | 2025-05-20 04:59:00 | NPP-375D | COLÍDER | MATO GROSSO | Brasil | 5103205 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9ea1ef18-3a3a-341b-9b7f-5fec2abd7938 | -8.69678 | -49.02541 | 2025-05-20 04:59:00 | NPP-375D | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7742e748-6f8f-3854-85f1-152ee6316853 | -11.41237 | -44.70403 | 2025-05-20 04:59:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d112b9b4-c00b-335d-aebc-ec85ba522703 | -8.74756 | -49.74712 | 2025-05-20 04:59:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 617eefb5-405a-3db3-8e81-826958f31215 | -10.76096 | -57.23143 | 2025-05-20 04:59:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 588c1ec0-af39-30b2-8c7e-c52655e00313 | -12.42727 | -43.73014 | 2025-05-20 04:59:00 | NPP-375D | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d9eb2828-22a1-33d6-9e3a-66c05da65983 | -9.4152 | -58.33284 | 2025-05-20 04:59:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 08e9d498-a7a2-3579-b033-2d3457373ade | -9.9311 | -59.93046 | 2025-05-20 04:59:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 09a4756b-13e3-3d00-9fef-94e56374f9af | -13.31748 | -45.37516 | 2025-05-20 04:59:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7fd6a59e-7b99-39e7-a9f7-89dc9a3f4c25 | -9.03446 | -48.94122 | 2025-05-20 04:59:00 | NPP-375D | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 3f184092-6cbd-309d-82dd-a863ce64fd49 | -9.95216 | -54.17329 | 2025-05-20 04:59:00 | NPP-375D | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 142c2f59-aaff-3188-98d1-04a7a611d99f | -12.1307 | -54.65734 | 2025-05-20 04:59:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ed6aa1fa-e3f4-313e-960a-ea37992e7a3f | -9.03989 | -47.75942 | 2025-05-20 04:59:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6c1d2c30-5dda-3389-aa7e-0999ca8010a3 | -13.02304 | -45.07091 | 2025-05-20 04:59:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 8e8c0fa7-84f6-3095-8e50-881f6c6b4bd5 | -9.04454 | -47.76006 | 2025-05-20 04:59:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 32d93db9-2371-3497-b7e0-704afa7bd349 | -7.31014 | -55.30724 | 2025-05-20 04:59:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ae312288-1cd7-33f3-8e36-857521affb31 | -8.63606 | -51.28889 | 2025-05-20 04:59:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d8fb09fa-663c-3340-9c98-5e05203a7e38 | -9.76946 | -57.79832 | 2025-05-20 04:59:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d599f56b-f6f6-3de6-8443-a276ef2529fa | -13.31703 | -45.37457 | 2025-05-20 04:59:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 29a640fe-bdd0-3fa6-9916-ddee9c841dc9 | -11.36092 | -55.1245 | 2025-05-20 04:59:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| abad00e9-6acd-3504-8d70-63a36732f56d | -8.7511 | -49.75126 | 2025-05-20 04:59:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 489cff35-151e-35e1-be63-53bceecd3bbf | -12.12903 | -54.66812 | 2025-05-20 04:59:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 468b2948-2e64-3b33-8bef-85f3eeb6cc5e | -11.41828 | -44.70482 | 2025-05-20 04:59:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| aabb7c93-0715-3d17-87c9-0c249fdd5b6e | -10.60238 | -46.97211 | 2025-05-20 04:59:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7a33f242-c3a5-3f7d-87c9-2e9eed715413 | -8.07359 | -47.1256 | 2025-05-20 04:59:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 92153cf0-de95-370a-b8f5-a881dd94964d | -11.08408 | -54.77676 | 2025-05-20 04:59:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b4852d3c-d3bd-368c-bd93-f703651289ca | -12.12735 | -54.6568 | 2025-05-20 04:59:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0edb9594-5e6b-307d-8214-13045089dd1d | -13.02431 | -45.07357 | 2025-05-20 04:59:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 1fb2f752-edb7-371b-9e5c-8ff8993f5f69 | -12.12679 | -54.6604 | 2025-05-20 04:59:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7795cbf6-255f-33df-985f-26330fbe8d4f | -12.08419 | -54.57994 | 2025-05-20 04:59:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 53a2a360-fe6e-3dc8-883a-bbb04b1af386 | -11.51826 | -48.58451 | 2025-05-20 04:59:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 574c049b-3b69-35c7-b4d5-ebdc83d19fa4 | -12.4357 | -43.72585 | 2025-05-20 04:59:00 | NPP-375D | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 44b49e10-179e-37dd-8789-4963a7423ebe | -10.55157 | -55.62617 | 2025-05-20 04:59:00 | NPP-375D | COLÍDER | MATO GROSSO | Brasil | 5103205 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f9528644-426d-3283-8316-86401f2c5023 | -11.69873 | -47.78942 | 2025-05-20 04:59:00 | NPP-375D | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7b89afd6-502c-3b5c-b15c-59f2a25cbdf7 | -11.66675 | -54.94553 | 2025-05-20 04:59:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7850767d-de8c-31db-a1bf-cd233c91e17b | -12.27747 | -57.27137 | 2025-05-20 05:01:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| d091d2f2-a386-33a2-bc25-bd7e870dcf48 | -14.01697 | -55.13275 | 2025-05-20 05:01:00 | NPP-375D | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| df8c3f5b-ce82-36ed-beca-f3d2ea421a75 | -14.03443 | -55.12035 | 2025-05-20 05:01:00 | NPP-375D | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 46425c3b-c4fa-3d89-a5d6-c29ded49bca8 | -19.05431 | -53.45873 | 2025-05-20 05:01:00 | NPP-375D | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 90bc3816-151c-3d4f-81d9-34aa603e4f8c | -15.25579 | -60.06046 | 2025-05-20 05:01:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ff97c173-92f5-3308-9681-26b7ee20a446 | -14.02775 | -55.14154 | 2025-05-20 05:01:00 | NPP-375D | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9e347826-51bd-318c-85ca-c46461fece97 | -17.62059 | -50.91481 | 2025-05-20 05:01:00 | NPP-375D | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7a3cb0fd-0f57-334d-b2db-4feb21fce51f | -14.02814 | -55.12715 | 2025-05-20 05:01:00 | NPP-375D | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5e589afe-1639-3b93-8a36-041155e0dcc5 | -13.48747 | -60.37659 | 2025-05-20 05:01:00 | NPP-375D | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| de20ed0c-c131-3c9c-984c-e9ba822cd5f6 | -20.3604 | -49.30741 | 2025-05-20 05:01:00 | NPP-375D | NOVA GRANADA | SÃO PAULO | Brasil | 3533007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| c35fd266-0713-3fae-befe-a4847059b6e8 | -13.04832 | -53.71935 | 2025-05-20 05:01:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 7a4586ad-670a-34f4-a30c-2a243b3e2817 | -13.66392 | -53.93327 | 2025-05-20 05:01:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 4c0bf8fd-1b2c-3b95-8956-149a35dc1194 | -19.06174 | -53.45988 | 2025-05-20 05:01:00 | NPP-375D | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8aafa7e3-99c6-3ebd-ae0d-2770d0d6225f | -17.42029 | -51.33973 | 2025-05-20 05:01:00 | NPP-375D | MONTIVIDIU | GOIÁS | Brasil | 5213756 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f7137276-09ba-38c1-8731-c7cef1565d45 | -16.228 | -59.64713 | 2025-05-20 05:01:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 327050f0-c307-3552-973b-667730b285a5 | -13.61206 | -55.45388 | 2025-05-20 05:01:00 | NPP-375D | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 58070e32-25d4-3f94-a8a8-3c2d09b0cfef | -14.01585 | -55.13998 | 2025-05-20 05:01:00 | NPP-375D | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 88343811-e3ad-3da1-a6b5-fab4c0fcc1a8 | -19.15717 | -47.8173 | 2025-05-20 05:01:00 | NPP-375D | NOVA PONTE | MINAS GERAIS | Brasil | 3145000 | 31 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 0851b9d0-cd21-38bb-8669-e78f594b43dc | -14.03277 | -55.13123 | 2025-05-20 05:01:00 | NPP-375D | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| eb42d974-ed10-396f-85a4-c552f1b36794 | -14.02423 | -55.13022 | 2025-05-20 05:01:00 | NPP-375D | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d6def88d-c960-37ab-86a5-d9c64a2067f2 | -17.50285 | -46.74231 | 2025-05-20 05:01:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 8169d5a0-68d1-38c2-8da3-dfe5d09ce380 | -15.28013 | -43.07503 | 2025-05-20 05:01:00 | NPP-375D | MONTE AZUL | MINAS GERAIS | Brasil | 3142908 | 31 | 33 | nan | nan | nan | Caatinga | 2.6 |
| cfc3fec4-1feb-36bc-a7fd-4d0d323d29ad | -20.22371 | -50.7548 | 2025-05-20 05:01:00 | NPP-375D | ASPÁSIA | SÃO PAULO | Brasil | 3503950 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 1f96481a-acaa-32e3-b526-9e4387d8e1ea | -12.6123 | -56.02297 | 2025-05-20 05:01:00 | NPP-375D | SORRISO | MATO GROSSO | Brasil | 5107925 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| cdf5a225-4fc1-3725-bed8-4ebcf67cd11d | -12.27466 | -57.26706 | 2025-05-20 05:01:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| b17404be-28fa-3503-bb18-61e6b48de7aa | -14.03723 | -55.12452 | 2025-05-20 05:01:00 | NPP-375D | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6ee0c0fd-c103-3ae0-b90e-a9252b449112 | -14.02927 | -55.1199 | 2025-05-20 05:01:00 | NPP-375D | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0083a4d3-9387-3f6d-960a-26c6600c09f0 | -14.02479 | -55.1266 | 2025-05-20 05:01:00 | NPP-375D | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5091bb2e-471b-3433-82fe-01f10a286958 | -16.92899 | -53.01741 | 2025-05-20 05:01:00 | NPP-375D | SANTA RITA DO ARAGUAIA | GOIÁS | Brasil | 5219407 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| dc773d45-d60d-3de3-b168-394960ed8307 | -14.04633 | -45.51479 | 2025-05-20 05:01:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 38839e0d-0bb9-378b-a2fd-63cc04f9abbf | -16.93106 | -53.01554 | 2025-05-20 05:01:00 | NPP-375D | SANTA RITA DO ARAGUAIA | GOIÁS | Brasil | 5219407 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 94249f2a-37be-3aae-8a02-0856ef4f1fe9 | -19.11327 | -52.69252 | 2025-05-20 05:01:00 | NPP-375D | CHAPADÃO DO SUL | MATO GROSSO DO SUL | Brasil | 5002951 | 50 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 66c83a2f-8d85-371d-a274-bd5b4e5d3d4b | -17.11089 | -49.14357 | 2025-05-20 05:01:00 | NPP-375D | HIDROLÂNDIA | GOIÁS | Brasil | 5209705 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 69f1993b-3d08-3ba1-b224-cf81dc06810e | -14.0259 | -55.14162 | 2025-05-20 05:01:00 | NPP-375D | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f6974124-c793-3785-b7b2-9d010a979a99 | -17.31267 | -51.1113 | 2025-05-20 05:01:00 | NPP-375D | MONTIVIDIU | GOIÁS | Brasil | 5213756 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 799f844a-1f0e-380b-8457-2202553bec7d | -12.64432 | -54.08341 | 2025-05-20 05:01:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| d6c82c79-d548-3a6b-bb7b-c3d96f8e7429 | -17.50326 | -46.73845 | 2025-05-20 05:01:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 0515a691-46f8-3434-b643-9ce08b2507cd | -13.04428 | -53.72267 | 2025-05-20 05:01:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| db593966-0b1c-36f9-9cc8-858789636461 | -13.04082 | -53.72214 | 2025-05-20 05:01:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3125e92c-2f56-388e-82ea-e585f7080dea | -20.21926 | -50.75415 | 2025-05-20 05:01:00 | NPP-375D | ASPÁSIA | SÃO PAULO | Brasil | 3503950 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 8b18f22d-0b4c-33aa-845d-cc7ed406ddb4 | -18.13646 | -52.35538 | 2025-05-20 05:01:00 | NPP-375D | SERRANÓPOLIS | GOIÁS | Brasil | 5220504 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 41e9675f-6a2e-3e30-a7d0-783d726f77e8 | -15.2635 | -54.26624 | 2025-05-20 05:01:00 | NPP-375D | PRIMAVERA DO LESTE | MATO GROSSO | Brasil | 5107040 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 2ccdbc8c-678c-3d45-be85-5f8f72e022ec | -14.0192 | -55.14053 | 2025-05-20 05:01:00 | NPP-375D | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 324441e3-265e-367f-9608-852b2f76c8c8 | -13.04486 | -53.71883 | 2025-05-20 05:01:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| d523c3ec-a3da-3151-90d1-d952020d1d74 | -19.34118 | -54.17044 | 2025-05-20 05:01:00 | NPP-375D | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 9afbe72c-1203-30dd-a82d-c36d1a168075 | -14.01976 | -55.13691 | 2025-05-20 05:01:00 | NPP-375D | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 80fd028b-6876-353d-8eed-019c1fd0482c | -14.02997 | -55.12706 | 2025-05-20 05:01:00 | NPP-375D | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 411bd2c0-ce26-30a8-ae5c-6a00c43270a2 | -14.03108 | -55.11981 | 2025-05-20 05:01:00 | NPP-375D | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 272e4154-b558-34b5-bd48-4b9606387302 | -14.04869 | -56.07272 | 2025-05-20 05:01:00 | NPP-375D | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| fd792bc8-66b9-3616-9e01-f34fe62f489a | -14.03332 | -55.1276 | 2025-05-20 05:01:00 | NPP-375D | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 709477b3-0ce8-3528-9c5d-321cacd5291c | -17.49912 | -46.73959 | 2025-05-20 05:01:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d7b3d0f8-ca07-33d3-aa86-b30567cc0acf | -13.71084 | -57.47866 | 2025-05-20 05:01:00 | NPP-375D | CAMPO NOVO DO PARECIS | MATO GROSSO | Brasil | 5102637 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5364fdc5-9f45-3d86-904e-ecd73656a1c1 | -12.65057 | -54.08821 | 2025-05-20 05:01:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 428821a8-55c7-37cf-af1b-4df815e54a68 | -14.03778 | -55.1209 | 2025-05-20 05:01:00 | NPP-375D | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 57ac0ae0-addf-3820-98bc-28f59444cdfd | -14.03556 | -55.13539 | 2025-05-20 05:01:00 | NPP-375D | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 694a728a-e1f2-3502-a3e1-22c9a369ac98 | -14.03221 | -55.13485 | 2025-05-20 05:01:00 | NPP-375D | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 7b82f90c-c238-3d65-a12f-18aea44faf3a | -20.22256 | -50.75142 | 2025-05-20 05:01:00 | NPP-375D | ASPÁSIA | SÃO PAULO | Brasil | 3503950 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| a1adaf48-2b14-3d35-bbd6-3bd43a057d8e | -14.02592 | -55.11936 | 2025-05-20 05:01:00 | NPP-375D | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 06ce7a50-455d-3930-8fe4-6bb50c6bf55a | -16.22727 | -59.65136 | 2025-05-20 05:01:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| ce6465a5-8b9a-3f98-8bcb-31d8ec88df1b | -16.39687 | -58.16687 | 2025-05-20 05:01:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.3 |
| d7a68fb7-c1d8-30a3-b930-9331201c1d6b | -12.83495 | -62.01771 | 2025-05-20 05:01:00 | NPP-375D | ALTO ALEGRE DOS PARECIS | RONDÔNIA | Brasil | 1100379 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |


[Clique aqui para ver as próximas entradas](README12.md)
