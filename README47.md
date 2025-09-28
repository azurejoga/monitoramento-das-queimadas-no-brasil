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

## Dados Diários - Página 47

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2e361901-a81f-3b85-8cd3-93e63018f181 | -11.14725 | -54.3098 | 2025-09-28 04:06:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| e92036c7-f1ac-31d0-b254-fc7ea4f883c5 | -11.85726 | -48.24042 | 2025-09-28 04:06:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f0adf72e-18c5-3ff4-86b2-db265c7870d7 | -13.61246 | -48.0993 | 2025-09-28 04:06:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f952077a-5894-3b05-8ad1-edb12a5c3de0 | -11.95805 | -47.89302 | 2025-09-28 04:06:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7bfd793b-9c19-368c-a372-15f6c6a922a6 | -15.27361 | -46.45281 | 2025-09-28 04:06:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 9bf6f514-a972-392d-b6ad-a7a3effcf2a4 | -11.35434 | -45.00227 | 2025-09-28 04:06:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a42e5de2-0166-3046-8fd4-cba1178d4b26 | -11.44995 | -44.9865 | 2025-09-28 04:06:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 4c2af0eb-0f1f-33f1-b7d1-3778eec4865d | -14.54381 | -48.40542 | 2025-09-28 04:06:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 30c42d1d-850a-3c02-a9d3-3e5f565b1563 | -11.38909 | -46.97555 | 2025-09-28 04:06:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b01c68aa-7fb4-3f18-bed3-5b1875c30574 | -12.90294 | -45.15499 | 2025-09-28 04:06:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 8.3 |
| f712cf0d-9e13-3ddd-a5ef-b89101e25bd7 | -13.59744 | -47.28992 | 2025-09-28 04:06:00 | NPP-375D | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 17315618-3ad8-3781-8a5e-f95421de0bd5 | -10.51454 | -51.94582 | 2025-09-28 04:06:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 58da25b9-de8b-38d6-9376-3e3c519292ec | -15.08586 | -48.32893 | 2025-09-28 04:06:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 613d7c11-3eba-394e-9e09-60bde0961655 | -15.46681 | -50.22561 | 2025-09-28 04:06:00 | NPP-375D | FAINA | GOIÁS | Brasil | 5207535 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0db36ab2-f550-33f7-a042-fe96ca691f07 | -11.62412 | -52.85015 | 2025-09-28 04:06:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 53356d44-4525-3ee6-912d-0d601c9eee04 | -13.61132 | -48.08042 | 2025-09-28 04:06:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 04836f4f-1221-3d74-be6d-80112bcabbe8 | -12.00768 | -47.97686 | 2025-09-28 04:06:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 55d556c4-a804-39b2-8163-3992e227e661 | -14.81675 | -45.45791 | 2025-09-28 04:06:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 29d8b688-9932-3424-870a-7eeec9b1fc99 | -11.94696 | -47.92818 | 2025-09-28 04:06:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 107f7039-9612-3b13-bb71-86a250ce3251 | -11.42181 | -45.0383 | 2025-09-28 04:06:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 09d65587-2eee-346a-9cb8-79ed5d858ae5 | -13.62242 | -48.06933 | 2025-09-28 04:06:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| f518843d-bf92-3d9a-854b-8fd01d16d473 | -12.0042 | -47.09394 | 2025-09-28 04:06:00 | NPP-375D | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| b4ca4e21-afc7-3277-8c30-5da8348a5c77 | -11.96252 | -47.89384 | 2025-09-28 04:06:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f319accc-dda3-3d40-b983-683a1f9a0fd6 | -13.2566 | -48.45451 | 2025-09-28 04:06:00 | NPP-375D | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 90af71d5-44df-3e52-b25b-bf9849a9715e | -10.05061 | -49.20034 | 2025-09-28 04:06:00 | NPP-375D | MONTE SANTO DO TOCANTINS | TOCANTINS | Brasil | 1713700 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| a7740aed-3c6f-3494-b3cb-edc8521f6280 | -11.64876 | -48.26826 | 2025-09-28 04:06:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6a8296c1-c246-3cf0-b2ce-9764b47409c1 | -13.39546 | -48.1536 | 2025-09-28 04:06:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6cbff9b9-33f7-3f85-a0b6-25f2d0579735 | -15.24185 | -46.45187 | 2025-09-28 04:06:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 2bdb0705-6ff6-3e1b-ac98-c0ee29d64387 | -14.77221 | -45.64911 | 2025-09-28 04:06:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 58a972e9-7b3e-3cd8-9798-3007a07f5941 | -15.28123 | -46.4548 | 2025-09-28 04:06:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f9a70758-a42e-33d5-915f-e62c0d06d94f | -12.2935 | -45.64009 | 2025-09-28 04:06:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 46b08110-bd26-3629-92ba-cc95aa7ec608 | -13.40456 | -48.16719 | 2025-09-28 04:06:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| a6fb4d0f-34cb-32f6-961d-352e28eeacf9 | -12.95553 | -46.3803 | 2025-09-28 04:06:00 | NPP-375D | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 4e556ffd-112f-3630-a19f-5e66601638ba | -14.50154 | -48.56114 | 2025-09-28 04:06:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1547e001-3e78-3244-a505-299bf0be591f | -12.97706 | -49.43768 | 2025-09-28 04:06:00 | NPP-375D | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b0f30730-5ef5-34be-a44e-7e645ceb6875 | -11.36138 | -44.96185 | 2025-09-28 04:06:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 38af8229-7dd1-3dda-a60c-9b427aaaef0e | -13.62689 | -47.3182 | 2025-09-28 04:06:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b0707f0e-7830-386e-8016-c5fa410bc233 | -14.89555 | -45.56364 | 2025-09-28 04:06:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 27916b6a-4e9f-359c-860b-eaa00d40e881 | -15.88789 | -46.24562 | 2025-09-28 04:06:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3fb16ead-4869-3789-877e-8efbda40f3a8 | -13.76669 | -47.86781 | 2025-09-28 04:06:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8aba8d04-1dad-36ce-847a-bf66c61f08a5 | -13.77588 | -47.89685 | 2025-09-28 04:06:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1cf7c4bb-958e-3ada-abc1-9409419173b9 | -11.60032 | -44.33745 | 2025-09-28 04:06:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| faceab40-1094-37c1-b3a2-55c8886a7d5b | -13.78904 | -47.92253 | 2025-09-28 04:06:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 973b78f4-871d-31e2-89d3-7d763872be20 | -12.91612 | -45.1899 | 2025-09-28 04:06:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4c36821d-c040-3db3-9ffe-2d6bdd1e87dc | -11.35457 | -45.04549 | 2025-09-28 04:06:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| bbfa00fa-d628-361c-aee7-a9f4676a328f | -14.20924 | -41.79793 | 2025-09-28 04:06:00 | NPP-375D | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | 0.3 |
| 3377e5ef-3771-31b3-9b44-0c6f96bc7668 | -15.69838 | -49.13811 | 2025-09-28 04:06:00 | NPP-375D | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f98a43cb-e8d7-3004-9640-0baa24686c37 | -15.33277 | -47.89985 | 2025-09-28 04:06:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d3082d65-cf00-3e97-ba9c-beca656ba986 | -12.01552 | -47.90728 | 2025-09-28 04:06:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 7377e396-5ff2-363d-9200-dc2ea1d7cd76 | -11.52292 | -54.31757 | 2025-09-28 04:06:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9780f369-b4c7-3e38-aa8a-6ec7ec20dbba | -12.99776 | -49.43481 | 2025-09-28 04:06:00 | NPP-375D | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ad13c118-5d08-39f7-9c7f-d027c75c0bfd | -15.29642 | -49.47962 | 2025-09-28 04:06:00 | NPP-375D | SANTA ISABEL | GOIÁS | Brasil | 5219357 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1b6d65ed-705b-3322-8e8e-00beff424517 | -11.62675 | -52.85586 | 2025-09-28 04:06:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 718d39ba-192f-3da6-bb9f-2497d7f3dce5 | -11.73274 | -43.11405 | 2025-09-28 04:06:00 | NPP-375D | MORPARÁ | BAHIA | Brasil | 2921609 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| bb74c00f-7676-30e7-802f-b637ebe5b12f | -13.51336 | -47.3975 | 2025-09-28 04:06:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 83ee448b-55e3-3391-ae9d-e54e8c121268 | -11.78073 | -43.76429 | 2025-09-28 04:06:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 687132b9-93d3-38d6-9071-2407385acd70 | -15.44022 | -48.23931 | 2025-09-28 04:06:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 44de477e-6d1e-3bbd-b924-adfa94378c56 | -15.67667 | -46.2598 | 2025-09-28 04:06:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7fcfba21-3f9c-32cf-82bb-567261d8079e | -15.44714 | -48.23458 | 2025-09-28 04:06:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a18e87d7-66fd-37e4-a41a-1c7e05e51dfc | -11.9951 | -47.07167 | 2025-09-28 04:06:00 | NPP-375D | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 18b62938-689c-3db1-b85a-d49a08123553 | -12.00069 | -47.08914 | 2025-09-28 04:06:00 | NPP-375D | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| ab5b541b-4b6e-3d21-9bad-1410dbc91dee | -11.38696 | -46.98751 | 2025-09-28 04:06:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a07aae15-62bc-328a-871c-220487531434 | -15.32933 | -47.89484 | 2025-09-28 04:06:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| b0ab593e-2dc9-332f-aa8e-bb34c91dbfd8 | -12.98467 | -49.45072 | 2025-09-28 04:06:00 | NPP-375D | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 097a7a09-bf05-3e81-95c4-318040199264 | -15.33497 | -47.88793 | 2025-09-28 04:06:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5f570b9d-98bc-384e-8d8f-2f6d96549556 | -11.97946 | -48.00453 | 2025-09-28 04:06:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 275048c3-c2c3-3f86-b3cb-8948ed8867ce | -13.34828 | -47.30172 | 2025-09-28 04:06:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a6b5eb5c-9eb6-3282-90d4-30e658375222 | -11.70842 | -44.46928 | 2025-09-28 04:06:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| bea4473d-f0d5-3d46-aaca-dcc05f4edeb3 | -10.94185 | -44.31993 | 2025-09-28 04:06:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 32425445-b219-3e55-8f8a-620e00101ccc | -12.89005 | -47.10532 | 2025-09-28 04:06:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5a862a83-26d1-3025-85c8-c66c258cf515 | -11.40533 | -46.95812 | 2025-09-28 04:06:00 | NPP-375D | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8f0ff45e-4dca-39dd-a9b5-7abaa57884b0 | -13.60286 | -48.102 | 2025-09-28 04:06:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 0ab98b5a-1dd0-35a0-974b-53be52d94c7f | -14.49795 | -48.55552 | 2025-09-28 04:06:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8d6bc491-2f77-33f4-b409-21d752dd50fd | -12.94027 | -45.11554 | 2025-09-28 04:06:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 02ff6843-f63d-3c3d-b3f5-1c9e9c38a12b | -15.43744 | -48.21534 | 2025-09-28 04:06:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d36dab41-e6c1-3c5a-a5c7-9546d4781eed | -12.97798 | -46.85015 | 2025-09-28 04:06:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5008d809-db11-3d1e-aebe-99c4da94d9c7 | -12.01411 | -47.08752 | 2025-09-28 04:06:00 | NPP-375D | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ff88fd85-9874-351e-a3aa-bcd1d2b7e0a7 | -11.58383 | -45.49677 | 2025-09-28 04:06:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ad977d29-6937-3acf-b09b-b390ceed67fe | -15.48759 | -41.92444 | 2025-09-28 04:06:00 | NPP-375D | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 73fe808d-212c-3f05-b81b-3f1d07d41a6a | -13.78024 | -47.89752 | 2025-09-28 04:06:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1130a8f5-4045-3197-b82b-2a06cf63b705 | -15.81671 | -41.89367 | 2025-09-28 04:06:00 | NPP-375D | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 11fbaca7-2655-33d0-bdd0-4fc12dbe99f6 | -14.82607 | -45.67633 | 2025-09-28 04:06:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0188ef44-137e-38d5-a835-db52a97d8d35 | -12.02042 | -47.91729 | 2025-09-28 04:06:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 7.8 |
| a9d4fda7-e7e9-3daa-a2b9-926932e44c39 | -15.40373 | -45.30578 | 2025-09-28 04:06:00 | NPP-375D | CHAPADA GAÚCHA | MINAS GERAIS | Brasil | 3116159 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 5167b5b7-0d55-3b5a-a5d2-e03945ba69d7 | -12.01021 | -47.96272 | 2025-09-28 04:06:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| cf509938-74cb-3d20-87b0-e553f58e85f1 | -12.29491 | -44.57918 | 2025-09-28 04:06:00 | NPP-375D | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 520ea59f-c6cd-346a-86cb-3aaf14642203 | -14.54062 | -48.42291 | 2025-09-28 04:06:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| fc93d367-93fc-3574-a688-86ccbfa5a57e | -13.29246 | -50.68765 | 2025-09-28 04:06:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9a59a753-9053-302b-9293-b49509ba1708 | -12.25343 | -44.06812 | 2025-09-28 04:06:00 | NPP-375D | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| af2bd7f6-7486-36a4-b636-0ca3e3bf69c0 | -12.02232 | -47.93195 | 2025-09-28 04:06:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| fe308419-f20e-3c30-8d25-c7554d5ea07a | -13.62105 | -47.30264 | 2025-09-28 04:06:00 | NPP-375D | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b79975a9-f25b-3530-90fa-41d49512b13b | -15.03675 | -46.96371 | 2025-09-28 04:06:00 | NPP-375D | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8b437e49-3dcd-359b-b9e5-62a7c89ff039 | -10.82605 | -47.62844 | 2025-09-28 04:06:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| b3032ec5-2a4f-3843-8fef-d3e802b97e53 | -10.90489 | -45.7576 | 2025-09-28 04:06:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 43bb93d0-9dc4-35bd-8d55-5d72554926b0 | -12.95155 | -46.37954 | 2025-09-28 04:06:00 | NPP-375D | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| baa4a8ed-18b4-31de-a9b0-bf7053b87624 | -11.98942 | -47.89834 | 2025-09-28 04:06:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 547eb763-b334-366f-afd9-8939a27b375d | -11.95557 | -47.90651 | 2025-09-28 04:06:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| aa1298d7-c94b-36a1-b4d7-db20b4759067 | -12.94474 | -45.11171 | 2025-09-28 04:06:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 607a0414-0d08-39f6-a82a-b9493cf2d4d2 | -11.38979 | -46.97159 | 2025-09-28 04:06:00 | NPP-375D | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c1f0dab8-2ebf-32e0-be3d-0d3a572a67ba | -13.62176 | -48.06738 | 2025-09-28 04:06:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |


[Clique aqui para ver as próximas entradas](README48.md)
