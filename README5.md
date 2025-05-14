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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 10009cf8-d729-350e-a86a-207cd3e8c24b | -10.65946 | -44.49458 | 2025-05-14 03:53:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 3da0b053-c915-3d6b-a2ec-d96ed0cf1c8a | -9.76328 | -44.00301 | 2025-05-14 03:53:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 94e29852-f733-3d88-bce0-6cc237783092 | -9.46307 | -40.30928 | 2025-05-14 03:53:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 1c7bdade-ea6a-3f9c-8244-150c13dafa96 | -9.99707 | -47.84026 | 2025-05-14 03:53:00 | NOAA-20 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| eb54b35c-0a74-3e2c-8bd9-f6961f6eb099 | -10.55177 | -42.42867 | 2025-05-14 03:53:00 | NOAA-20 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| a06dacc7-7921-3c98-af85-dc097ff761a4 | -8.0613 | -47.12848 | 2025-05-14 03:53:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| dfc7d454-d651-30b9-9e0c-e0a1e8d96501 | -9.26603 | -50.21865 | 2025-05-14 03:53:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 17a9973e-2cad-34e5-adef-31d98a60b122 | -11.56836 | -47.87421 | 2025-05-14 03:53:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5cd18ba6-347c-384e-a986-f3a3a3d0e860 | -8.9157 | -37.97067 | 2025-05-14 03:53:00 | NOAA-20 | INAJÁ | PERNAMBUCO | Brasil | 2607000 | 26 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 62a31889-8e4e-39d4-be7e-ddb196521b23 | -11.80532 | -46.64013 | 2025-05-14 03:53:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 81c8b1d8-69e5-3ed1-a796-6342eb7244b0 | -11.62869 | -48.12551 | 2025-05-14 03:53:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 2ce18766-6b5e-3548-bfee-e5c44a5fc6b9 | -11.78702 | -47.37161 | 2025-05-14 03:53:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 00261656-d420-396d-8060-4dddad8a7117 | -11.79529 | -46.6431 | 2025-05-14 03:53:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4d8c5b7a-33f3-37d3-b3f1-dc073998431f | -12.15689 | -48.01105 | 2025-05-14 03:53:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6411ea35-87c1-3e06-9799-771e3bc9e4be | -6.95739 | -47.92827 | 2025-05-14 03:53:00 | NOAA-20 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 16aa3399-cb91-313c-b159-63034203b245 | -14.63593 | -45.11551 | 2025-05-14 03:55:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 304f6f5d-0ce2-3514-a49e-5010890bbbc0 | -14.62687 | -45.09755 | 2025-05-14 03:55:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1806e2dc-ecf9-3b5f-8b2b-e903af4794c3 | -13.67635 | -53.9449 | 2025-05-14 03:55:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| e4446906-8931-37ce-9ed7-70ac55cfc8b6 | -14.63477 | -45.09906 | 2025-05-14 03:55:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| dd634639-4f06-3f95-8128-c903cb3ff7b1 | -14.87394 | -45.11542 | 2025-05-14 03:55:00 | NOAA-20 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4daebaa3-3ccb-3ad3-8380-97ef1309db24 | -12.99441 | -48.88195 | 2025-05-14 03:55:00 | NOAA-20 | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 13906762-7d51-3923-9942-d05a67fdbdf5 | -13.56729 | -52.87513 | 2025-05-14 03:55:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b451fdf5-545f-3745-ac84-a0068aeb0b06 | -13.56977 | -52.87319 | 2025-05-14 03:55:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f7cfc603-9e7d-3d64-8195-5d2c22ad639b | -14.62594 | -45.10278 | 2025-05-14 03:55:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f5e33e37-88f7-3b5c-a267-bf242d2588d2 | -15.82054 | -48.12519 | 2025-05-14 03:55:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 76bdb260-076e-30d7-a109-796f89514e83 | -13.60185 | -47.38461 | 2025-05-14 03:55:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| dbdd3dfb-bd1d-36d8-b1c1-9c653c43b6df | -13.61663 | -47.79777 | 2025-05-14 03:55:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a9e48d9a-2e41-32ec-8e6f-f08b3f028b42 | -14.62896 | -45.10876 | 2025-05-14 03:55:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 71826a60-ce81-3959-bc4f-22004e890090 | -13.67668 | -53.95259 | 2025-05-14 03:55:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0eedeee5-95e6-3dc6-a2a2-be0bfea1b218 | -13.68531 | -47.77198 | 2025-05-14 03:55:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 00e5547d-667f-3a47-b174-5a0398ee654b | -13.05137 | -53.72171 | 2025-05-14 03:55:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 2a6035f7-4774-31b9-b30c-1eaffc7bdaa0 | -18.32509 | -45.34166 | 2025-05-14 03:55:00 | NOAA-20 | MORADA NOVA DE MINAS | MINAS GERAIS | Brasil | 3143500 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6b0eb5ba-9561-3449-aabc-c7a599c3d9ba | -15.26228 | -51.46094 | 2025-05-14 03:55:00 | NOAA-20 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c7b8860d-efe6-38a0-b627-869cfc7a189c | -14.63082 | -45.0983 | 2025-05-14 03:55:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 705c32d9-81e2-35d0-805d-383016e0890f | -17.49853 | -45.17829 | 2025-05-14 03:55:00 | NOAA-20 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c88bbd3f-dc2c-39fe-ad66-72b8730380a5 | -13.06745 | -52.02377 | 2025-05-14 03:55:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 5.8 |
| a940df07-54a1-31f6-8ab0-b72901b02f36 | -15.27264 | -43.07576 | 2025-05-14 03:55:00 | NOAA-20 | MONTE AZUL | MINAS GERAIS | Brasil | 3142908 | 31 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 7940c343-5393-396b-862a-983da3e2976a | -13.55827 | -52.88496 | 2025-05-14 03:55:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| cf470b62-b094-3330-aba9-515a3afeb5ac | -13.56204 | -52.87728 | 2025-05-14 03:55:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2660d8c3-b03b-3192-88bc-7f88786f00d0 | -13.66975 | -53.95093 | 2025-05-14 03:55:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c96324b2-b54f-35b8-8f82-b1dfc07f4b4b | -13.56074 | -52.87365 | 2025-05-14 03:55:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a1576ef3-98aa-3cb3-abcd-6a094aaaefb9 | -14.63779 | -45.10504 | 2025-05-14 03:55:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 23473aeb-5af8-302b-9733-9d657be18535 | -12.99457 | -48.88218 | 2025-05-14 03:55:00 | NOAA-20 | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 68292e9f-2824-3fc9-ad28-fba01a07cd57 | -14.63291 | -45.10952 | 2025-05-14 03:55:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5ff2571a-2dbd-3124-8415-ab9b07c46da3 | -13.56322 | -52.87169 | 2025-05-14 03:55:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1636c0b6-e06c-371d-bca7-68ff43bebf67 | -14.63686 | -45.11028 | 2025-05-14 03:55:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9cc9a933-a66a-3944-9268-0c5242f669ca | -13.6025 | -47.39423 | 2025-05-14 03:55:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d44b520f-0bf0-344c-93d9-33478f113c13 | -20.22067 | -46.74853 | 2025-05-14 03:55:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| af483742-8eea-3360-81a1-d143217a966a | -19.97001 | -44.21679 | 2025-05-14 03:55:00 | NOAA-20 | BETIM | MINAS GERAIS | Brasil | 3106705 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 0ff84a61-7b7a-34f7-bd38-4fd04c12151a | -14.63198 | -45.11475 | 2025-05-14 03:55:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 17458ef6-a507-34b9-b067-e8da4de48417 | -17.50312 | -48.92861 | 2025-05-14 03:55:00 | NOAA-20 | PIRACANJUBA | GOIÁS | Brasil | 5217104 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9de003fb-ffc9-3537-bfb0-819e2ea13af1 | -14.62989 | -45.10353 | 2025-05-14 03:55:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9210c63e-a833-30a9-a9a4-8709432ff4c0 | -13.04613 | -53.72049 | 2025-05-14 03:55:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fe809046-e1ed-3075-9030-ae767734c801 | -13.60464 | -47.3825 | 2025-05-14 03:55:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| cc6275bf-aabf-3a5b-92a2-5dc2175fa991 | -14.87788 | -45.11618 | 2025-05-14 03:55:00 | NOAA-20 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 418766a2-37e3-3505-9151-7cd7ee3a3170 | -13.60418 | -47.39769 | 2025-05-14 03:55:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5101f95c-a6dc-32b4-811b-5651dfd67295 | -13.61764 | -47.79236 | 2025-05-14 03:55:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 78095910-64e4-3cff-8f21-6aee6c457158 | -13.55952 | -52.87924 | 2025-05-14 03:55:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 2a89b72c-f872-3b9f-9c2a-549d61b8fac8 | -17.49799 | -45.17572 | 2025-05-14 03:55:00 | NOAA-20 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8479a5c5-5f21-3167-9a7f-eebfed4f92cb | -13.67483 | -53.95175 | 2025-05-14 03:55:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 381ef6d2-dad4-3605-b6dd-61b489ce6cee | -13.69111 | -47.76756 | 2025-05-14 03:55:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d84d6ac4-900e-3586-8692-f16d440cd198 | -13.60742 | -47.38078 | 2025-05-14 03:55:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 20ecff23-ae19-33c2-9d2c-779b4fd126d5 | -13.56084 | -52.88295 | 2025-05-14 03:55:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f0e67d8e-5185-3b74-9b93-06f9db1b64a0 | -19.43695 | -44.33773 | 2025-05-14 03:55:00 | NOAA-20 | SETE LAGOAS | MINAS GERAIS | Brasil | 3167202 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 58e769ca-d543-39c8-b32e-37130418a4be | -13.39405 | -47.51281 | 2025-05-14 03:55:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| bb862de1-0999-32c6-a40c-26c1a881775a | -13.61009 | -47.37918 | 2025-05-14 03:55:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4aecf5d5-fe87-3769-b5e6-01898bd499b9 | -13.05299 | -53.72241 | 2025-05-14 03:55:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9580c53a-6879-3f98-b829-5cf097b1a498 | -15.26842 | -43.0792 | 2025-05-14 03:55:00 | NOAA-20 | MONTE AZUL | MINAS GERAIS | Brasil | 3142908 | 31 | 33 | nan | nan | nan | Caatinga | 14.7 |
| bc8b4240-f1f8-34bd-a431-75287ea6e35c | -15.26561 | -43.07444 | 2025-05-14 03:55:00 | NOAA-20 | MONTE AZUL | MINAS GERAIS | Brasil | 3142908 | 31 | 33 | nan | nan | nan | Caatinga | 28.0 |
| 4fae006c-c1c9-36c1-a621-530ce113022c | -13.38902 | -47.51353 | 2025-05-14 03:55:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 0357c0cf-4068-377a-b827-5a559b38eb25 | -13.0447 | -53.72716 | 2025-05-14 03:55:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 5c629db5-73c0-3bf9-ab2e-ba1e0df89e23 | -13.67128 | -53.94383 | 2025-05-14 03:55:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 47cb91a6-a03c-3fbe-897f-0a2abcd85019 | -12.99519 | -48.87901 | 2025-05-14 03:55:00 | NOAA-20 | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d17fcb5e-0de1-324e-8ad0-d8008c88ed0f | -13.61197 | -47.38225 | 2025-05-14 03:55:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 07f0b3f2-e99b-305b-b2fa-99dfb9effc1a | -13.52917 | -44.0475 | 2025-05-14 03:55:00 | NOAA-20 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8f71bfb3-6493-38fb-ba2b-fb46a8d68673 | -13.59898 | -47.38704 | 2025-05-14 03:55:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 95da2611-b115-358e-b927-95a39987f8e1 | -14.63384 | -45.10429 | 2025-05-14 03:55:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 83683cee-b508-3c2f-936c-113358f61f27 | -19.304 | -44.43231 | 2025-05-14 03:55:00 | NOAA-20 | CAETANÓPOLIS | MINAS GERAIS | Brasil | 3109907 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1098a29d-0b3f-3004-88cc-778b050b7d23 | -17.09243 | -43.80516 | 2025-05-14 03:55:00 | NOAA-20 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 038f9252-6f6f-3c65-9c70-f8c3b4d0c785 | -14.87302 | -45.12062 | 2025-05-14 03:55:00 | NOAA-20 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 95ca9011-f87b-3beb-b8f1-3042e15f465c | -19.849 | -43.84396 | 2025-05-14 03:55:00 | NOAA-20 | SABARÁ | MINAS GERAIS | Brasil | 3156700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 66722e27-49a1-3234-b0d4-d1ea1e2e2b47 | -13.55304 | -52.88735 | 2025-05-14 03:55:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3ada04ea-2cd5-3c62-a81a-3d5376f78252 | -13.55427 | -52.88152 | 2025-05-14 03:55:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 294a7a8a-08cb-382a-a17a-f4ccb596a0ff | -23.33776 | -46.77057 | 2025-05-14 03:57:00 | NOAA-20 | CAIEIRAS | SÃO PAULO | Brasil | 3509007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 4e9770dc-c8d6-39bd-b5ab-53e5b5cd924e | -20.81657 | -49.78881 | 2025-05-14 03:57:00 | NOAA-20 | MONTE APRAZÍVEL | SÃO PAULO | Brasil | 3531407 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| d0480028-ff13-3115-afa7-25cf98ba718f | -20.82132 | -49.78992 | 2025-05-14 03:57:00 | NOAA-20 | MONTE APRAZÍVEL | SÃO PAULO | Brasil | 3531407 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 182bfc1d-a6e6-3f3b-8cbe-0b199901f489 | -21.59079 | -49.81029 | 2025-05-14 03:57:00 | NOAA-20 | GUAIÇARA | SÃO PAULO | Brasil | 3517208 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| c5bdc2e6-6397-3d82-b3a3-d97f438a3f1a | -23.78844 | -54.86628 | 2025-05-14 03:57:00 | NOAA-20 | TACURU | MATO GROSSO DO SUL | Brasil | 5007950 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 360c2a96-a605-31d0-95ed-440325aa1183 | -21.71878 | -55.37355 | 2025-05-14 03:57:00 | NOAA-20 | MARACAJU | MATO GROSSO DO SUL | Brasil | 5005400 | 50 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c2f1f671-b7dd-39b8-9d9e-68392fcf1bf7 | -26.60019 | -53.14907 | 2025-05-14 03:57:00 | NOAA-20 | SANTA TEREZINHA DO PROGRESSO | SANTA CATARINA | Brasil | 4215687 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| bf2a44f0-25f1-3019-a30c-3ba61a99351b | -21.60382 | -56.04606 | 2025-05-14 03:57:00 | NOAA-20 | GUIA LOPES DA LAGUNA | MATO GROSSO DO SUL | Brasil | 5004106 | 50 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 7ae3be50-127d-30aa-a500-32745a1afc73 | -21.45824 | -57.15463 | 2025-05-14 03:57:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 457cd06f-a907-3a94-9a83-26380eac962e | -21.71734 | -55.37943 | 2025-05-14 03:57:00 | NOAA-20 | MARACAJU | MATO GROSSO DO SUL | Brasil | 5005400 | 50 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 1cd2338f-5395-33ec-8031-59456972513c | -21.46358 | -57.15551 | 2025-05-14 03:57:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 3.3 |
| be99e02e-39b6-3bae-bd5a-8921edf4be20 | -23.78962 | -54.86148 | 2025-05-14 03:57:00 | NOAA-20 | TACURU | MATO GROSSO DO SUL | Brasil | 5007950 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 374d5845-1e46-3467-884c-7b51c2170c1a | -22.7871 | -43.75569 | 2025-05-14 03:57:00 | NOAA-20 | SEROPÉDICA | RIO DE JANEIRO | Brasil | 3305554 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 66524446-353d-3c53-8a9d-522903cea6d7 | -21.46021 | -57.14706 | 2025-05-14 03:57:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4a84b350-7312-3fe8-b5b7-a2629900e70d | -21.1297 | -47.80012 | 2025-05-14 03:57:00 | NOAA-20 | RIBEIRÃO PRETO | SÃO PAULO | Brasil | 3543402 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 08df7399-6c0d-3734-9ac1-a681cbf771f6 | -22.16656 | -42.94448 | 2025-05-14 03:57:00 | NOAA-20 | SÃO JOSÉ DO VALE DO RIO PRETO | RIO DE JANEIRO | Brasil | 3305158 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| 43b2fc3a-cfac-32bd-97d5-60575c793c0e | -21.60258 | -56.04602 | 2025-05-14 03:57:00 | NOAA-20 | GUIA LOPES DA LAGUNA | MATO GROSSO DO SUL | Brasil | 5004106 | 50 | 33 | nan | nan | nan | Cerrado | 10.5 |


[Clique aqui para ver as próximas entradas](README6.md)
