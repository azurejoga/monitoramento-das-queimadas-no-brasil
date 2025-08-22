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

## Dados Diários - Página 17

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d97e490f-af4f-36c4-9313-840f7c4a0e10 | -12.95948 | -46.27536 | 2025-08-22 03:57:00 | NPP-375D | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 4a3907a7-5525-3dbb-9dc2-7056374ae48f | -13.37969 | -47.50386 | 2025-08-22 03:57:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 0171f846-0dc8-32b9-98df-936095917b9d | -12.95586 | -46.27003 | 2025-08-22 03:57:00 | NPP-375D | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 1e564ca2-4809-3917-b0ff-5190242890aa | -15.15751 | -47.95606 | 2025-08-22 03:57:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 453ddf4a-9a5e-346d-adff-e3bf3cecdfbe | -12.09363 | -43.33883 | 2025-08-22 03:57:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e984d9b7-2f71-3fa1-aa69-59cfc6d2cb90 | -10.98371 | -45.60476 | 2025-08-22 03:57:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5b003282-6b02-3be5-be62-cd0f364e64ca | -12.95795 | -46.28388 | 2025-08-22 03:57:00 | NPP-375D | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3c179073-1491-3e07-9d97-ad29f362623d | -12.94013 | -46.17992 | 2025-08-22 03:57:00 | NPP-375D | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 6e0646ae-3875-332a-9925-895200163a88 | -15.7333 | -43.24154 | 2025-08-22 03:57:00 | NPP-375D | NOVA PORTEIRINHA | MINAS GERAIS | Brasil | 3145059 | 31 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 1b3e3176-1926-3c41-ad0e-1347c5b1a6a7 | -10.27191 | -46.75698 | 2025-08-22 03:57:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 354ef1b9-d288-38a7-a975-4e14fd18563e | -12.92795 | -46.17171 | 2025-08-22 03:57:00 | NPP-375D | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 597b2899-342e-32e9-a7b2-5ba2025335b4 | -13.0282 | -45.18154 | 2025-08-22 03:57:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1d0eb2e1-232d-362c-9d26-b016ecb062ef | -9.71891 | -45.63356 | 2025-08-22 03:57:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 495e39b8-10f5-35ad-84f3-686695adb07e | -13.38294 | -42.05232 | 2025-08-22 03:57:00 | NPP-375D | ÉRICO CARDOSO | BAHIA | Brasil | 2900504 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 57e1813c-f4cb-368f-aa54-87f47a5f29ac | -7.84685 | -46.98205 | 2025-08-22 03:57:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b1f62dd5-eaf2-3e60-ac00-7e2ddb7b8a58 | -15.58439 | -43.80169 | 2025-08-22 03:57:00 | NPP-375D | VERDELÂNDIA | MINAS GERAIS | Brasil | 3171030 | 31 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 51ea506c-6f77-3bc3-9b4b-8cb8012066a7 | -12.94424 | -46.28359 | 2025-08-22 03:57:00 | NPP-375D | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| e95f1f8b-adc8-36da-9d8c-b860f82bfedc | -12.99614 | -45.24213 | 2025-08-22 03:57:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| a0bd63e0-7354-39ea-86f2-5fa393cfc433 | -13.49787 | -47.06188 | 2025-08-22 03:57:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e9e55840-f2cd-39a5-a36b-052fa34e6366 | -7.85618 | -47.00512 | 2025-08-22 03:57:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7c994672-d49e-38ec-bc6a-7c12fe408092 | -10.73369 | -48.25681 | 2025-08-22 03:57:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| b8f0d4dd-d2ea-3dbc-8936-fc017eeacce6 | -14.76288 | -45.42553 | 2025-08-22 03:57:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c8bd523c-ea1a-3148-b7f5-f7b9fa8b0d69 | -13.38107 | -47.49672 | 2025-08-22 03:57:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 8face710-e449-38c9-9cf6-b7ae2af94eca | -13.63066 | -46.87982 | 2025-08-22 03:57:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| d9d4f890-53b7-3e85-aeed-627f0172fb03 | -11.12887 | -44.708 | 2025-08-22 03:57:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4e716af9-4767-3889-a352-6ee16ee9eb1f | -13.03033 | -45.19364 | 2025-08-22 03:57:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ffebfb7b-364d-315a-b8eb-7888261f7921 | -14.7676 | -45.39964 | 2025-08-22 03:57:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| d7a3f81b-5bf2-3825-ae04-64c8151ca643 | -14.86975 | -47.94435 | 2025-08-22 03:57:00 | NPP-375D | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b6ad2040-4c0b-37e4-9ecf-18ec754498f7 | -10.27689 | -46.75682 | 2025-08-22 03:57:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e8d5c094-603b-308a-b4d9-43e8f8430612 | -11.29287 | -44.93291 | 2025-08-22 03:57:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 02d86df2-88e6-3b5e-b2e0-d4d95d5e33bc | -7.86746 | -47.00089 | 2025-08-22 03:57:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 59df1dc1-63b5-3006-a230-7120b0a86291 | -13.37119 | -47.49666 | 2025-08-22 03:57:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| a8040814-a61e-35ac-b3e9-d38f97d2c27c | -14.75746 | -45.40918 | 2025-08-22 03:57:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a3d73312-e706-3487-beed-a89ed340f9dc | -14.76625 | -45.40703 | 2025-08-22 03:57:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 37fb677a-b206-3e77-83e6-fd4182ee7218 | -8.5159 | -48.82654 | 2025-08-22 03:57:00 | NPP-375D | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 580a484d-01ec-3416-94be-ac4139a23b4b | -13.00021 | -45.21927 | 2025-08-22 03:57:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d6b70979-56ff-3659-80f8-3c9a14d2df2e | -10.73744 | -48.23655 | 2025-08-22 03:57:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 022dbe95-541d-38cf-b972-e3bab7f1ba71 | -14.88911 | -47.94686 | 2025-08-22 03:57:00 | NPP-375D | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| dca6299e-223a-3622-b0bd-f6ec614733ed | -11.00563 | -45.63454 | 2025-08-22 03:57:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7956b100-54c0-34de-a9e5-b32e25886053 | -12.94499 | -46.27944 | 2025-08-22 03:57:00 | NPP-375D | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 378097e4-5b33-316d-a2ff-f6c40af9cc88 | -13.00164 | -45.23527 | 2025-08-22 03:57:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 13.2 |
| ad497623-cca6-398f-b8e1-5821abdbeae0 | -14.76221 | -45.4292 | 2025-08-22 03:57:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 430f1ab4-c675-35cb-9d94-8693f0bc1ebc | -13.03175 | -46.32336 | 2025-08-22 03:57:00 | NPP-375D | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 6c29aad0-f26e-3abe-838e-8c10b1806f96 | -8.79469 | -45.42146 | 2025-08-22 03:57:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| d4d3de20-3f9a-3288-b60c-8b7c61e590b6 | -13.14786 | -46.89867 | 2025-08-22 03:57:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| e3f77d09-4aa4-3743-96a4-5d70ac032799 | -13.38362 | -42.04827 | 2025-08-22 03:57:00 | NPP-375D | ÉRICO CARDOSO | BAHIA | Brasil | 2900504 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 3641282f-3e38-3940-91df-3b0b1c3ef641 | -12.99743 | -45.2109 | 2025-08-22 03:57:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c603fe22-fb5a-3b76-bf48-1b33f9c58719 | -8.90056 | -47.33248 | 2025-08-22 03:57:00 | NPP-375D | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 68b8e9f6-5a4c-3049-a2e1-bad44a4269d3 | -13.65269 | -45.71099 | 2025-08-22 03:57:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 078b12b3-935e-3503-944c-46bfe39c0d7a | -14.75881 | -45.40178 | 2025-08-22 03:57:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e0312ba4-39fd-3631-b631-6334dce72e08 | -12.95074 | -46.27301 | 2025-08-22 03:57:00 | NPP-375D | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 49565286-899c-3c1b-9467-8b64dadb350a | -12.10412 | -41.07885 | 2025-08-22 03:57:00 | NPP-375D | UTINGA | BAHIA | Brasil | 2932804 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| be68014b-5c84-3afa-ac5b-19f7d8379448 | -13.03365 | -45.17477 | 2025-08-22 03:57:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 69ab69af-fd3a-32b4-b260-270f72dac906 | -13.00366 | -45.22386 | 2025-08-22 03:57:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 05987c49-cd5e-3f0b-ac1c-0e6df0938a0a | -13.03257 | -46.31883 | 2025-08-22 03:57:00 | NPP-375D | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 64c16e05-a3d6-3440-8d5d-8515a7a64be3 | -13.36325 | -46.25931 | 2025-08-22 03:57:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 36043772-031d-3968-87ed-d169d082074e | -12.09737 | -43.33946 | 2025-08-22 03:57:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 360a1083-a913-3201-a9cc-94fc260c11d0 | -12.92927 | -46.18952 | 2025-08-22 03:57:00 | NPP-375D | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a6defa42-0880-30f0-8dcc-a4ea59481d5e | -8.12479 | -47.1487 | 2025-08-22 03:57:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 64b31bd8-41c0-35cf-911a-303d94cd60ad | -13.40099 | -49.13375 | 2025-08-22 03:57:00 | NPP-375D | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| cfe11fe7-f449-31b9-b50e-01f91272968f | -11.27632 | -44.95327 | 2025-08-22 03:57:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 49cde75f-81c4-38bb-b376-70f302e8750f | -12.99269 | -45.23754 | 2025-08-22 03:57:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 4fd53bb4-a851-32e5-bbde-13866b55bfd7 | -12.0057 | -44.67147 | 2025-08-22 03:57:00 | NPP-375D | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 20.1 |
| 63ec1b0d-77e5-391d-8225-b260491d6ea9 | -14.83279 | -47.9302 | 2025-08-22 03:57:00 | NPP-375D | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 27f88574-a385-3dbc-ae3e-7bea3013b704 | -13.42062 | -43.68127 | 2025-08-22 03:57:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| df4db6b4-7d92-32c3-bfd2-cb1b95fd31f8 | -13.42051 | -43.67876 | 2025-08-22 03:57:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6b1b5fb7-f537-3e84-8b04-44f1bc6e45e8 | -13.02561 | -46.33187 | 2025-08-22 03:57:00 | NPP-375D | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 63181753-7d5c-3884-b402-8ccef04b6beb | -7.81959 | -46.87032 | 2025-08-22 03:57:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 477e275f-2704-39b4-9ae3-6d747dc2ccb8 | -14.88809 | -47.95222 | 2025-08-22 03:57:00 | NPP-375D | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 7c692393-55e2-362f-99c5-1fa13f724bce | -7.85438 | -46.99897 | 2025-08-22 03:57:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e2b12bd3-5ba2-3a2f-96a9-342a422f3e63 | -12.9502 | -46.2925 | 2025-08-22 03:57:00 | NPP-375D | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f858a0d5-6dd3-340e-a21f-8ceaa8f03f61 | -13.02476 | -45.17695 | 2025-08-22 03:57:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 539d1c01-1110-38e0-bc72-153024b8f3bb | -13.03087 | -45.1664 | 2025-08-22 03:57:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 580a8b16-8012-3aa6-a3b9-e93b54504d46 | -12.9394 | -46.18394 | 2025-08-22 03:57:00 | NPP-375D | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c74d7885-1373-36a7-aa0f-6646ad79d86e | -11.31664 | -44.9447 | 2025-08-22 03:57:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c6abca63-8b18-317e-9b0b-6aa9396e1878 | -14.91515 | -49.45623 | 2025-08-22 03:57:00 | NPP-375D | ITAPACI | GOIÁS | Brasil | 5210901 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0607865b-cc71-3220-97cb-989fe4f68fa9 | -7.81084 | -46.89014 | 2025-08-22 03:57:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b7a1f88e-2864-3ba8-a536-77484d70203e | -8.47673 | -48.24839 | 2025-08-22 03:57:00 | NPP-375D | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 00f28cd1-2402-3a32-836e-e9e1ae74dbe6 | -14.75949 | -45.39808 | 2025-08-22 03:57:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 68df80c2-5d66-3c1e-af7a-17a3f4445208 | -10.72693 | -48.23455 | 2025-08-22 03:57:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 7771599d-517a-3438-8bb4-18619b5ead8d | -10.18266 | -47.56567 | 2025-08-22 03:57:00 | NPP-375D | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6a62cb43-5e8b-3a4e-a0fc-46b8f5567e69 | -14.89293 | -47.9724 | 2025-08-22 03:57:00 | NPP-375D | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| ae55c1dd-c68d-3c77-b493-1137b0456504 | -10.28623 | -46.75502 | 2025-08-22 03:57:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3ab09a43-8c28-3278-a64a-b6e1fbbfb9c9 | -7.85946 | -46.99994 | 2025-08-22 03:57:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a35fe9c4-4f58-3906-bdfd-ba6f284486bf | -11.28736 | -44.93968 | 2025-08-22 03:57:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| c62c26d1-6558-364a-9f34-a80159ed0a50 | -13.02342 | -45.18451 | 2025-08-22 03:57:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c2684c5b-b341-373f-8cf8-da0cc3261532 | -13.58495 | -47.04626 | 2025-08-22 03:57:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 23d3f21b-6afe-3e61-b348-d43b65f06c84 | -12.96085 | -46.26007 | 2025-08-22 03:57:00 | NPP-375D | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 8.6 |
| e112bf62-48b4-3fbb-be3f-aca7cfd10557 | -11.31731 | -44.94086 | 2025-08-22 03:57:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 28b59d34-8cf8-35ef-9995-eb3fe205791c | -7.85653 | -46.98664 | 2025-08-22 03:57:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6303c3df-3ea8-3459-9718-60e2327507ff | -12.71095 | -40.89614 | 2025-08-22 03:57:00 | NPP-375D | IBIQUERA | BAHIA | Brasil | 2912608 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| b724f85f-7ffe-3801-9193-3435c9201049 | -13.65342 | -45.70699 | 2025-08-22 03:57:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 60d75b05-2669-368a-9390-79c38a08685b | -14.76355 | -45.42186 | 2025-08-22 03:57:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 74fb35d8-419f-31de-9835-f555f3dc4c5c | -10.72223 | -48.23063 | 2025-08-22 03:57:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 858079fa-c822-3abc-9735-1c5c09ab7527 | -10.9741 | -45.60787 | 2025-08-22 03:57:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| be117d63-0309-34f4-94ef-db0713ab268e | -13.63527 | -46.88039 | 2025-08-22 03:57:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3d27c430-972a-30c9-a97f-6f6a8f48aee5 | -7.85839 | -47.00605 | 2025-08-22 03:57:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 2ec8855f-7471-36f4-980e-0048dd08486f | -10.7281 | -48.22827 | 2025-08-22 03:57:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 51d320ab-4f95-3896-843a-876f4777f53d | -14.32015 | -52.01175 | 2025-08-22 03:57:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e71f07dd-f22a-3158-aa7f-d905b8837f3c | -13.38831 | -46.24633 | 2025-08-22 03:57:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |


[Clique aqui para ver as próximas entradas](README18.md)
