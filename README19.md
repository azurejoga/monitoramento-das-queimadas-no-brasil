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

## Dados Diários - Página 19

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4421a966-dd2c-3e52-bc15-39013429ca9c | -5.13071 | -46.15873 | 2024-10-20 04:08:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 55f5ac4c-87ab-3b8b-af41-545312a6018e | -5.12733 | -46.1544 | 2024-10-20 04:08:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5e1733ea-0f04-3ac2-b4cb-b85efdb85612 | -5.12215 | -46.16084 | 2024-10-20 04:08:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6fa9ff56-28f5-3cb6-bd31-15b04dd4bcc5 | -5.12156 | -46.16438 | 2024-10-20 04:08:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 4749a174-531c-3e92-b53d-11de13695012 | -5.11816 | -46.16015 | 2024-10-20 04:08:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1d22ab49-c772-3662-9855-cd037a5b496c | -5.09623 | -46.13165 | 2024-10-20 04:08:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 6.0 |
| c442c9e4-3715-3cfd-bfb8-ab06d2de7c28 | -5.09568 | -46.13507 | 2024-10-20 04:08:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 0eb9ed8e-f39f-3a64-9fdf-88a129f0cfd5 | -6.28645 | -45.99089 | 2024-10-20 04:08:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9661c7cb-8ccc-3526-bcc5-fba7ed6401a7 | -5.98434 | -45.36689 | 2024-10-20 04:08:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 21ac6e34-2edb-314e-95cb-1b7282ca1bc3 | -5.9836 | -45.37146 | 2024-10-20 04:08:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 29f81549-7937-33e6-97fe-830357219bc7 | -5.98093 | -45.36888 | 2024-10-20 04:08:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 28.9 |
| c85dcce1-b1ea-3bd5-964a-bc2ce23fa7cc | -5.98058 | -45.36629 | 2024-10-20 04:08:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 7.8 |
| e138def2-f61a-3e5e-b6fa-44297eb3b970 | -5.98017 | -45.37344 | 2024-10-20 04:08:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 2fce8ae3-2d7e-31d1-b9a9-e65c9550c466 | -5.97984 | -45.37086 | 2024-10-20 04:08:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 0c6a8d30-3374-3ca6-9ad4-7e7958f8fdd9 | -5.92406 | -45.49943 | 2024-10-20 04:08:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| aeb6aaa4-cca5-3bc9-8683-020d89049336 | -5.05459 | -45.86514 | 2024-10-20 04:08:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8282457e-ecc3-3be6-b0ac-f6ca996155c2 | -7.17813 | -46.79705 | 2024-10-20 04:08:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 12df429e-91d6-31b0-84cd-6c25eb68c351 | -7.17348 | -46.79997 | 2024-10-20 04:08:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 1123349c-c992-35db-8156-b7a035299252 | -7.16944 | -46.7993 | 2024-10-20 04:08:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 3f85f9a3-e21d-39bd-a7b4-5c70507ec88d | -6.82113 | -46.04685 | 2024-10-20 04:08:00 | NOAA-21 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9d68c86d-50ca-3be4-87c6-2aecdd326a16 | -3.09253 | -45.94519 | 2024-10-20 04:08:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a2be2c48-4ae7-324c-a8a9-1954cdeddee8 | -3.09194 | -45.9488 | 2024-10-20 04:08:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9a4db339-3084-3cb7-beca-d70f4c9aad33 | -3.08796 | -46.55379 | 2024-10-20 04:08:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d49e8d3c-c52e-3507-99c4-de8783ab7135 | -3.08728 | -45.95173 | 2024-10-20 04:08:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8b1959ab-ca71-32fa-a543-9430f1054a64 | -3.08261 | -45.95472 | 2024-10-20 04:08:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 79b6b907-8f44-3024-b9ef-5526df47568e | -3.07188 | -46.62441 | 2024-10-20 04:08:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fe1cb228-619f-375c-8989-266f50ba1f3d | -2.65343 | -46.05094 | 2024-10-20 04:08:00 | NOAA-21 | MARANHÃOZINHO | MARANHÃO | Brasil | 2106375 | 21 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 7474bd3b-b15e-3ead-ad26-f36a0d0b93b4 | -2.63076 | -46.91023 | 2024-10-20 04:08:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ae23be1e-9f2b-3c73-ad50-7735cb09ff58 | -2.6264 | -46.90949 | 2024-10-20 04:08:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 2fd858e1-43bf-37eb-b6dd-9ae0114783a9 | -3.50997 | -46.22923 | 2024-10-20 04:08:00 | NOAA-21 | SÃO JOÃO DO CARÚ | MARANHÃO | Brasil | 2111029 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0f1bb124-a55a-3658-8b28-1a71c62a13cc | -2.19561 | -46.49448 | 2024-10-20 04:08:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 53a2f93e-5736-316f-b107-6b49caa73241 | -2.19133 | -46.49381 | 2024-10-20 04:08:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ed08a7e4-eff6-3171-84d9-c4cf4143193a | -2.18705 | -46.49313 | 2024-10-20 04:08:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b482a32f-3bda-35c3-ae23-d726c942ddb9 | -2.56882 | -47.06764 | 2024-10-20 04:08:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a2f408fb-7a25-3f04-a298-811c23cbf288 | -2.56543 | -47.06421 | 2024-10-20 04:08:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5b2f0b2a-517c-3374-841a-f53bceeb58dc | -2.56475 | -47.06852 | 2024-10-20 04:08:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b6f8033c-3de1-3488-ab34-d26f9383bb30 | -2.56439 | -47.06699 | 2024-10-20 04:08:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| a664fadc-0ef9-350b-b5eb-763666793a5d | -2.55398 | -47.29647 | 2024-10-20 04:08:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4a3deb95-a20d-3d3a-af77-9efc233c07e8 | -2.5469 | -47.12384 | 2024-10-20 04:08:00 | NOAA-21 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7942db4a-3d9f-378b-89e8-0c01c771b00f | -2.54612 | -47.12215 | 2024-10-20 04:08:00 | NOAA-21 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2f62d3d2-378b-30b3-b6ce-188f5ad0fa66 | -2.51651 | -45.99131 | 2024-10-20 04:08:00 | NOAA-21 | MARANHÃOZINHO | MARANHÃO | Brasil | 2106375 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fd74d952-01cf-3508-b1e5-d0c9dfe7a370 | -2.51361 | -45.99099 | 2024-10-20 04:08:00 | NOAA-21 | MARANHÃOZINHO | MARANHÃO | Brasil | 2106375 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5bc07987-80e5-3101-aa8f-92b9ec68be94 | -2.51303 | -45.99469 | 2024-10-20 04:08:00 | NOAA-21 | MARANHÃOZINHO | MARANHÃO | Brasil | 2106375 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1a879245-aebd-31f6-9da9-51f3e5f60efe | -2.5124 | -45.99066 | 2024-10-20 04:08:00 | NOAA-21 | MARANHÃOZINHO | MARANHÃO | Brasil | 2106375 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| dd9ac569-c632-36b6-85b7-7e7268e5d876 | -2.51178 | -45.99436 | 2024-10-20 04:08:00 | NOAA-21 | MARANHÃOZINHO | MARANHÃO | Brasil | 2106375 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b4803c1c-0986-3a3c-ac8f-d4cd3a6694fb | -2.33676 | -46.04744 | 2024-10-20 04:08:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 78186e37-24dd-3f10-9db6-d57cbd56ccc3 | -2.3262 | -46.59316 | 2024-10-20 04:08:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| aac831da-7418-39d7-8691-ad8a411b6f9c | -2.32189 | -46.5925 | 2024-10-20 04:08:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ba3005ad-eb81-34b6-b044-e874adb545e7 | -2.26477 | -46.74066 | 2024-10-20 04:08:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3d73ed2c-29f3-382f-a675-993b95d753fa | -4.99264 | -46.48704 | 2024-10-20 04:08:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 27a46646-51a1-3fd4-96f4-1502dd297ce8 | -4.98918 | -46.48257 | 2024-10-20 04:08:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 72e41dd7-dbc8-333b-b112-f861890d5725 | -4.98856 | -46.48631 | 2024-10-20 04:08:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 952e8287-35b5-31f9-a616-17d70bde8066 | -4.83285 | -46.9016 | 2024-10-20 04:08:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 16b7d36a-f727-3668-8db6-5a3a33cf5ddc | -4.8322 | -46.90557 | 2024-10-20 04:08:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 0b3ab193-e635-3579-a699-ab6ce93f2e9f | -4.82799 | -46.90482 | 2024-10-20 04:08:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 32698210-3256-38ae-9137-d8397a2b5f45 | -4.65943 | -46.90068 | 2024-10-20 04:08:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4423e362-b9fe-3bd3-8a26-496be0ef864c | -3.89236 | -46.44294 | 2024-10-20 04:08:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a240f0b5-c356-3209-87c1-a533f0f04e5b | -4.65519 | -46.90007 | 2024-10-20 04:08:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a4028a72-8f5c-3c6a-bb70-ec8b990fdc1a | -4.65454 | -46.90393 | 2024-10-20 04:08:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| cbb07a1c-ed93-311a-a963-41ccb8a7b515 | -4.63722 | -46.41068 | 2024-10-20 04:08:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5c9c46a3-51e4-3d78-a8ac-8d655b4fa54c | -4.61151 | -47.53349 | 2024-10-20 04:08:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3503b2c3-214e-315b-847e-b3c2d3fee54b | -4.61081 | -47.53775 | 2024-10-20 04:08:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| b5f8ce50-e403-3f0a-bc76-7d6ebd07af13 | -4.6064 | -47.53694 | 2024-10-20 04:08:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 9bae3324-bb5e-342c-a00b-ed886d2daa8b | -4.46983 | -47.73433 | 2024-10-20 04:08:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 9dccdf4b-eb27-3136-857a-f78ae72bed22 | -4.31794 | -47.53429 | 2024-10-20 04:08:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6d23c495-1f46-3f1c-962d-d31efc0429b7 | -4.24095 | -46.61666 | 2024-10-20 04:08:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ac4964f6-114f-306b-b1d3-6b5a485f876b | -4.24033 | -46.62044 | 2024-10-20 04:08:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 68e548d2-f730-35ea-b0be-ad3d102d9922 | -4.23676 | -46.61601 | 2024-10-20 04:08:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 27e35b9e-c743-3e05-9a3c-cd6a73fa67ce | -4.19956 | -46.63359 | 2024-10-20 04:08:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 022901a8-62e3-3032-9f63-675ecea73881 | -4.19892 | -46.63748 | 2024-10-20 04:08:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 30.9 |
| fe99bad3-596c-3d46-832e-641dd867c247 | -4.19605 | -46.62887 | 2024-10-20 04:08:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 5ee7b1f4-ac3e-3346-906b-4165d81f5cad | -4.1954 | -46.6328 | 2024-10-20 04:08:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 0021b704-548c-321a-af00-1c66d9531086 | -4.19475 | -46.63673 | 2024-10-20 04:08:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 30.9 |
| fc9d5367-ccd6-346c-b6fe-a9f689e53f0e | -4.19187 | -46.62816 | 2024-10-20 04:08:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 475c6775-3300-3f67-bcfa-2ec1b4961e7b | -4.1666 | -46.86013 | 2024-10-20 04:08:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e354b7ef-c5d8-3d11-b290-44d66bc683c1 | -4.13744 | -46.85174 | 2024-10-20 04:08:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.6 |
| ea2a1d37-3d07-37cf-a776-d7dc275dac01 | -4.12635 | -46.86586 | 2024-10-20 04:08:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 5.3 |
| b4d43adb-5f7a-339e-be86-fd00848b8d06 | -4.09629 | -46.91449 | 2024-10-20 04:08:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| aafeef99-d98f-3bb2-98eb-c369537043dd | -4.09317 | -46.91362 | 2024-10-20 04:08:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 797a04fd-bdde-357f-8757-26e9448dfb63 | -4.09253 | -46.91762 | 2024-10-20 04:08:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 111b0192-5386-3e2a-a463-710e61a370ae | -4.04021 | -46.94225 | 2024-10-20 04:08:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 269ab01d-d9b1-330a-bece-709332015830 | -4.03592 | -46.94161 | 2024-10-20 04:08:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 7452f1e7-5e13-344e-94eb-fde84f7d2a5d | -4.03526 | -46.94563 | 2024-10-20 04:08:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 6.6 |
| a45dc8bb-4d16-3b17-b5c5-9f45dc725b44 | -3.91253 | -46.44987 | 2024-10-20 04:08:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 499849d6-149c-36c7-b787-6bd203d4642c | -3.61636 | -47.51086 | 2024-10-20 04:08:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 96d95308-13fb-3955-8983-081607a5b90c | -3.61113 | -47.51464 | 2024-10-20 04:08:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5bb9fed5-4be3-3e7c-8088-b349dbc9a7b6 | -3.61039 | -47.51911 | 2024-10-20 04:08:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a75d7fc7-fb1f-3689-ade5-48ff19797caf | -3.60965 | -47.52359 | 2024-10-20 04:08:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f1abb1f7-190e-3d9b-b5e2-baef1ada7719 | -3.60664 | -47.51394 | 2024-10-20 04:08:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7747bf8b-33c9-322a-949d-cb1aabcf244a | -4.27315 | -46.28801 | 2024-10-20 04:08:00 | NOAA-21 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d47b8c55-c6ed-34a8-bcf9-8041611cef78 | -5.40456 | -46.9093 | 2024-10-20 04:08:00 | NOAA-21 | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| dd39a9e4-31f9-3626-addf-c46225e76de3 | -5.40228 | -46.90477 | 2024-10-20 04:08:00 | NOAA-21 | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| c850100c-7be6-3539-a6bd-7b9b8181413e | -5.40164 | -46.90853 | 2024-10-20 04:08:00 | NOAA-21 | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| b022b035-f677-364b-8ad4-94d3dcdbaaaa | -5.401 | -46.90483 | 2024-10-20 04:08:00 | NOAA-21 | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7e2c80dc-ff41-3cd9-af75-fdf761a29f28 | -5.40038 | -46.90858 | 2024-10-20 04:08:00 | NOAA-21 | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 4b58d199-ff58-31c1-a88c-9c7946afc24b | -5.39682 | -46.90413 | 2024-10-20 04:08:00 | NOAA-21 | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 99adb871-5cd6-318e-9c20-ae2639a93913 | -5.39621 | -46.90788 | 2024-10-20 04:08:00 | NOAA-21 | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 1e8d7134-5321-3802-9f1f-5746dfd63749 | -5.2229 | -46.68072 | 2024-10-20 04:08:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e7cc1f3f-d95c-346e-935a-96837edad348 | -7.67016 | -47.32312 | 2024-10-20 04:08:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7975bc76-2122-315e-adaa-17142e49515c | -7.21213 | -47.33267 | 2024-10-20 04:08:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |


[Clique aqui para ver as próximas entradas](README20.md)
