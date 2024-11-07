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
| 5476a4fa-e16c-34df-b627-915e8fd53687 | -5.4409 | -45.088402 | 2024-11-07 00:31:00 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 3e5cda39-0fbc-3797-8698-f17680ed7320 | -4.0467 | -49.266701 | 2024-11-07 00:31:00 | METOP-C | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7af002d4-5bfb-354b-a26e-e5f4e9e48079 | -5.9491 | -39.6814 | 2024-11-07 00:31:00 | METOP-C | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 42e7dc39-562f-3b1a-aeec-b98ed961e791 | -3.7042 | -48.983299 | 2024-11-07 00:31:00 | METOP-C | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 08a5b03c-9da4-3670-87c7-d9e6e3cd90a6 | -2.6171 | -51.726299 | 2024-11-07 00:31:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a0df6f25-6ca7-31a5-9ebf-6e2ca23f1121 | -3.9482 | -48.1534 | 2024-11-07 00:31:00 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ade2d15b-093a-38c7-acd5-4c60075f0f0e | -3.9494 | -49.428299 | 2024-11-07 00:31:00 | METOP-C | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 44e9b4e0-ff16-313d-aeeb-bffcd31e14a8 | -4.4212 | -44.476299 | 2024-11-07 00:31:00 | METOP-C | SÃO LUÍS GONZAGA DO MARANHÃO | MARANHÃO | Brasil | 2111409 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 0bafc380-d984-3c36-966e-45e1b7bb6c89 | -6.183 | -46.335499 | 2024-11-07 00:31:00 | METOP-C | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 17d83c52-a4c0-378b-8fb8-3237da9feac2 | -10.7336 | -49.527599 | 2024-11-07 00:31:00 | METOP-C | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| e3f88e8e-3428-39ba-a7a7-5395d1ad8bf0 | -3.2474 | -53.384499 | 2024-11-07 00:31:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 26b18491-d1d4-3714-9d8d-2ecdf07fa3b5 | -9.7365 | -43.586399 | 2024-11-07 00:31:00 | METOP-C | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 65d53b6c-5bef-356d-93c3-5d0b47191c8d | -2.6618 | -48.570499 | 2024-11-07 00:31:00 | METOP-C | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4a60090d-56ff-3edd-9b13-5a9328fdad10 | -5.9842 | -45.562 | 2024-11-07 00:31:00 | METOP-C | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c7ce4ae8-1d9b-3a43-a0ae-4df7a4af4b7d | -2.4155 | -48.5308 | 2024-11-07 00:31:00 | METOP-C | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 03a449e0-776d-31c7-a13e-a73af207198c | -10.7073 | -48.788898 | 2024-11-07 00:31:00 | METOP-C | FÁTIMA | TOCANTINS | Brasil | 1707553 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 40bd8427-d806-3786-b7be-927e5da19667 | -6.6934 | -43.952999 | 2024-11-07 00:31:00 | METOP-C | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b40cb402-4b9b-3224-8990-2f06adfa1f31 | -5.2344 | -44.910198 | 2024-11-07 00:31:00 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 3440329a-0f6e-3d3c-8bd8-94663c6be8cd | -2.8572 | -48.6586 | 2024-11-07 00:31:00 | METOP-C | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f3d63982-31cf-35bb-b930-66eaa3b77595 | -5.0526 | -46.849201 | 2024-11-07 00:31:00 | METOP-C | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 4ee354b4-8e58-358e-8561-b09a70c209f0 | -2.8227 | -52.909302 | 2024-11-07 00:31:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7bfdc075-a144-3d9d-ba22-20f4645e7e94 | -5.0216 | -46.848999 | 2024-11-07 00:31:00 | METOP-C | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| d558c605-cf89-3cc2-8f2b-fd55b852bc32 | -3.0337 | -48.032001 | 2024-11-07 00:31:00 | METOP-C | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| dd8a14d6-38c5-35fb-b261-5be4a0ead54d | -6.2522 | -43.569099 | 2024-11-07 00:31:00 | METOP-C | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 4ff1cedd-4145-35b0-8793-245f6c1dc317 | -3.204 | -49.230499 | 2024-11-07 00:31:00 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a3eb6523-8d4c-3eaa-b84a-c43056bf65d9 | -4.2785 | -48.6535 | 2024-11-07 00:31:00 | METOP-C | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e6b4dc89-3dd2-31da-9db2-974688a780e6 | -3.9742 | -48.403 | 2024-11-07 00:31:00 | METOP-C | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 95f5ee09-a658-3292-97ed-fb20bc01eeb6 | -2.6796 | -51.8204 | 2024-11-07 00:31:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d9ae80ec-8ede-3c02-a606-2d21903bfeca | -3.2431 | -50.446602 | 2024-11-07 00:31:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e8c8eade-a05c-3ac6-a481-ca5877073bd9 | -4.4599 | -46.514599 | 2024-11-07 00:31:00 | METOP-C | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| cff0f208-4581-3391-8a02-791a94976463 | -5.5201 | -43.659901 | 2024-11-07 00:31:00 | METOP-C | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 81c33dd5-646b-36d6-a170-7d1259e2f680 | -9.5897 | -43.138901 | 2024-11-07 00:31:00 | METOP-C | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 8d9921cd-3d86-3b0e-8708-28f40afa6261 | -2.4292 | -46.298901 | 2024-11-07 00:31:00 | METOP-C | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 05f39a10-eaf8-3bbc-8bc7-6fb37677eedb | -5.0011 | -49.891602 | 2024-11-07 00:31:00 | METOP-C | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 161e7ad7-d9f7-3ac6-b9ce-ae7c3145564b | -13.7173 | -42.893101 | 2024-11-07 00:31:00 | METOP-C | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 9c89d6fb-90fc-3a32-b34a-d60d2b1ec8cd | -3.2415 | -49.577 | 2024-11-07 00:31:00 | METOP-C | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0d299bad-1af5-3917-adf9-efc471099e72 | -6.0869 | -44.714901 | 2024-11-07 00:31:00 | METOP-C | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 894c9c64-374e-38db-bd3e-4e73ec62b392 | -1.7207 | -45.776501 | 2024-11-07 00:31:00 | METOP-C | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| d0de4747-a022-3554-ba34-d2ce4e79934e | -3.0931 | -53.701801 | 2024-11-07 00:31:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f62567ad-a305-3a57-997e-01082deea068 | -2.8153 | -52.922501 | 2024-11-07 00:31:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6523cc0f-4fec-33fe-aaef-c676fae730c8 | -2.3162 | -49.089001 | 2024-11-07 00:31:00 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a9a736cf-459a-38cf-92c7-e1d2f26a0c58 | -8.0844 | -44.426102 | 2024-11-07 00:31:00 | METOP-C | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 1004fdfe-de4b-34ae-8c96-a6fed0eaf9c4 | -5.2782 | -44.876598 | 2024-11-07 00:31:00 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 3673c469-a413-378d-9cd6-40b9f28bd73c | -5.836 | -46.2621 | 2024-11-07 00:31:00 | METOP-C | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 671d08a3-a690-31b1-8381-b2645e0d9e8c | -5.5906 | -45.200001 | 2024-11-07 00:31:00 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b60d81fd-1ca7-34a7-9576-0329bf1b32e8 | -2.83 | -52.896099 | 2024-11-07 00:31:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ab6be95d-5b66-3c94-b9e2-4e4d921a59e4 | -2.8251 | -52.9203 | 2024-11-07 00:31:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a2f40350-e6e9-3cc1-9483-fbb5cedc62ae | -4.1097 | -48.8633 | 2024-11-07 00:31:00 | METOP-C | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c1f91808-1424-3ee9-a298-c86f969f49e7 | -5.1115 | -43.1516 | 2024-11-07 00:31:00 | METOP-C | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 0178718b-8cc3-3daf-8f78-72e0f0470df5 | -4.765 | -45.7346 | 2024-11-07 00:31:00 | METOP-C | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 2e446e12-8395-3b46-aba1-465a9eaa64ad | -2.8081 | -52.935699 | 2024-11-07 00:31:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 998e09f6-69b5-3824-bfc4-bde89f0cb84c | -4.5093 | -42.872799 | 2024-11-07 00:31:00 | METOP-C | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 98fc6725-a5a4-3da0-b74f-4b8b8d69b2a5 | -2.0015 | -46.950901 | 2024-11-07 00:31:00 | METOP-C | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7a9ece1d-8094-36ae-8f4a-7ee4aaf97cc7 | -4.3537 | -48.621799 | 2024-11-07 00:31:00 | METOP-C | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4b0590db-d59b-35a0-ba2f-1058b8cdc0c8 | -3.9615 | -48.1213 | 2024-11-07 00:31:00 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f2f13048-48fe-3dda-91e0-bf0f50eb2e0c | -4.716 | -47.2258 | 2024-11-07 00:31:00 | METOP-C | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 74ebf1f7-b2c6-3660-9968-045ce4de8094 | -2.3043 | -48.541 | 2024-11-07 00:31:00 | METOP-C | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6bbb902b-1552-3c11-a7bd-d296c5f9c0d7 | -3.9694 | -48.155899 | 2024-11-07 00:31:00 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 29a0695f-79ac-34bb-9c93-8b0b728a1468 | -8.9343 | -42.597301 | 2024-11-07 00:31:00 | METOP-C | SÃO RAIMUNDO NONATO | PIAUÍ | Brasil | 2210607 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| f00a973e-7ebd-3c68-a0fc-bfb382dc899e | -2.8391 | -48.669998 | 2024-11-07 00:31:00 | METOP-C | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 29b6595c-97cd-3668-8624-82b42058a9ad | -3.9466 | -48.1465 | 2024-11-07 00:31:00 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e7023324-1b63-3ef6-83b7-9b8f28a4b281 | -2.1522 | -48.822701 | 2024-11-07 00:31:00 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 49ee61a9-e5eb-3da9-bcb2-dafdbaeb8d56 | -5.3807 | -46.256302 | 2024-11-07 00:31:00 | METOP-C | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 95b7b24f-afd6-344f-9f52-cd4bd07a76ce | -2.8097 | -48.676498 | 2024-11-07 00:31:00 | METOP-C | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ce32b838-89b9-3576-9c8e-f02a1a8dfedd | -2.8049 | -48.655499 | 2024-11-07 00:31:00 | METOP-C | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f9faf66d-0320-39b9-a467-4d6a36027b2b | -4.2413 | -48.535301 | 2024-11-07 00:31:00 | METOP-C | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| da9bbdce-e061-3a97-a1fc-77b76e4bdea6 | -2.8081 | -48.669498 | 2024-11-07 00:31:00 | METOP-C | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| eaccabdd-522c-30ad-84af-b702198a7bf3 | -3.0342 | -53.256599 | 2024-11-07 00:31:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| df86c185-c202-3369-8277-d7b85c5da761 | -2.5422 | -47.283001 | 2024-11-07 00:31:00 | METOP-C | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 389c5a38-ea50-3c7c-b94d-2335ecdebf73 | -4.4996 | -42.875099 | 2024-11-07 00:31:00 | METOP-C | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 5c869adf-0ef4-3bf5-8404-f190b0dd6b72 | -8.186 | -42.8391 | 2024-11-07 00:31:00 | METOP-C | BREJO DO PIAUÍ | PIAUÍ | Brasil | 2201988 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 4770a188-60d6-3660-bc7c-8286fdd52a1b | -4.3553 | -48.628899 | 2024-11-07 00:31:00 | METOP-C | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f98a625f-b91c-3c83-9a4b-a82594cee708 | -2.2096 | -48.352402 | 2024-11-07 00:31:00 | METOP-C | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 070ea979-e65f-3cc7-a05b-51b8e24673d7 | -5.4396 | -43.580898 | 2024-11-07 00:31:00 | METOP-C | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c24bfc8b-e706-3770-bc3d-7e7c67fe254f | -3.7791 | -47.729301 | 2024-11-07 00:31:00 | METOP-C | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 479cb7a8-2671-3695-a927-458e757ba519 | -3.2468 | -50.462799 | 2024-11-07 00:31:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8b54ef8e-9020-3f5e-af85-12d1b0750351 | -5.9387 | -43.772301 | 2024-11-07 00:31:00 | METOP-C | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| bc39e80a-7773-3f9f-ab11-3169c5ad7e93 | -5.1592 | -49.633598 | 2024-11-07 00:31:00 | METOP-C | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bd2c5023-a8cb-3ee6-ae22-beb99a21d525 | -2.2244 | -46.529301 | 2024-11-07 00:31:00 | METOP-C | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 70c39d72-e161-3aca-bed1-ed4d7d9332ea | -5.2684 | -44.878799 | 2024-11-07 00:31:00 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 8c14bfc2-df78-3055-97c5-d4134ed92e11 | -2.4281 | -48.586102 | 2024-11-07 00:31:00 | METOP-C | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 186ffc8c-d107-384b-b2c0-2240f067c697 | -8.5033 | -42.0909 | 2024-11-07 00:31:00 | METOP-C | CAPITÃO GERVÁSIO OLIVEIRA | PIAUÍ | Brasil | 2202455 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| d3dc3b6a-3385-35df-92f7-4710836c881b | -5.4376 | -43.572498 | 2024-11-07 00:31:00 | METOP-C | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| cb5a3b5c-4b92-3edf-b1fb-ac5323e38df1 | -3.1029 | -53.699699 | 2024-11-07 00:31:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8556ebe3-a29b-3b39-8240-3f80b7c41a5b | -6.6955 | -46.997501 | 2024-11-07 00:31:00 | METOP-C | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 585f8af5-5e5d-3eba-bf52-ec583c58e31c | -1.026 | -47.060501 | 2024-11-07 00:31:00 | METOP-C | PRIMAVERA | PARÁ | Brasil | 1506104 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ed1059da-e978-3c32-b1e8-d48bc4181a75 | -3.6624 | -50.252899 | 2024-11-07 00:31:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fd8dc651-cced-3114-8148-395b0e485321 | -3.7157 | -48.9883 | 2024-11-07 00:31:00 | METOP-C | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e1f5c253-84d4-331b-b843-0fb53605d1fe | -4.6668 | -46.337502 | 2024-11-07 00:31:00 | METOP-C | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 40499e4e-b414-3701-8f1d-71c2e9bd0e5a | -4.7175 | -47.2327 | 2024-11-07 00:31:00 | METOP-C | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 9c29e909-fdfb-3fcb-aed3-cc6cd6b0ad9d | -2.6004 | -49.250599 | 2024-11-07 00:31:00 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 09c2a0b9-9a98-3daa-8f61-b4a0b870d76b | -5.083 | -46.039299 | 2024-11-07 00:31:00 | METOP-C | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| a77e69c8-05a9-3ab9-ab8f-0f0de03e1fc9 | -5.0736 | -45.507198 | 2024-11-07 00:31:00 | METOP-C | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ce30d720-4032-30ed-a458-dc593d7c8afc | -4.6877 | -46.383598 | 2024-11-07 00:31:00 | METOP-C | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| bed6469c-bfa1-38c0-8dc0-f213d293201f | -9.7445 | -43.576401 | 2024-11-07 00:31:00 | METOP-C | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 80010cc2-d457-38c0-84ed-938886e4e4a3 | -2.1932 | -48.370499 | 2024-11-07 00:31:00 | METOP-C | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ba8e1160-5f5c-3a3f-96cb-8453ae30b4b9 | -6.5446 | -39.673901 | 2024-11-07 00:31:00 | METOP-C | JUCÁS | CEARÁ | Brasil | 2307403 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 2e58fd53-2cbf-332c-8d0e-1086771e87de | -5.4413 | -45.134499 | 2024-11-07 00:31:00 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| cab98b93-25c1-3d70-ada8-77d015b700ab | -2.895 | -48.5989 | 2024-11-07 00:31:00 | METOP-C | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 75cd690b-b067-3e06-a130-c631747bb4fd | -4.0776 | -48.313999 | 2024-11-07 00:31:00 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README7.md)
