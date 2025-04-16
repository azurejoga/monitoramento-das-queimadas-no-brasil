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
| a99393ad-a1c8-3f54-90df-4dac561a9bfd | -6.5631 | -51.1126 | 2025-04-16 00:10:00 | GOES-19 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 64.3 |
| d5903ad2-75a1-3e21-9024-d1113bb458aa | -6.66403 | -47.59982 | 2025-04-16 00:28:00 | TERRA_M-M | PALMEIRAS DO TOCANTINS | TOCANTINS | Brasil | 1713809 | 17 | 33 | nan | nan | nan | Cerrado | 16.5 |
| 486d7d7f-f298-3016-8f89-c8871c7d7d62 | -5.64284 | -43.71178 | 2025-04-16 00:28:00 | TERRA_M-M | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 18.1 |
| 82ca3a1d-c9f9-3907-b4c2-a9cde175213b | -5.16531 | -45.10908 | 2025-04-16 00:28:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 24.0 |
| ef2465f0-70a5-32b2-854b-45dff86b7d4d | -5.94188 | -44.45935 | 2025-04-16 00:28:00 | TERRA_M-M | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 7d5d3f69-5179-352d-963f-623aa954eb25 | -5.94312 | -44.46825 | 2025-04-16 00:28:00 | TERRA_M-M | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 12.3 |
| ca6a07b7-235f-3039-89c9-0218dd1e2cef | -7.24614 | -44.77283 | 2025-04-16 00:28:00 | TERRA_M-M | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 2fb38376-9283-3970-864d-c840bfd67579 | -7.56884 | -45.84398 | 2025-04-16 00:28:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 2b1f8b84-3a54-3aac-822e-ddaa05e9f8ab | -8.94019 | -44.227 | 2025-04-16 00:28:00 | TERRA_M-M | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 10.0 |
| fd91047b-4c6f-32aa-8a49-873129366660 | -6.66258 | -47.58891 | 2025-04-16 00:28:00 | TERRA_M-M | PALMEIRAS DO TOCANTINS | TOCANTINS | Brasil | 1713809 | 17 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 964c6313-71d1-3142-916c-559e4f0df4c7 | -5.64152 | -43.70252 | 2025-04-16 00:28:00 | TERRA_M-M | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 57d59844-5f5c-3ca5-9928-f96ba4752caf | -6.5631 | -51.1126 | 2025-04-16 02:40:00 | GOES-19 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 52.4 |
| 94aaecc7-2f4a-3080-bbbf-22ee4494c096 | -5.16626 | -45.1131 | 2025-04-16 03:28:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8f6770e2-d3b1-364d-b24c-7206a5d5a485 | -5.16747 | -45.10637 | 2025-04-16 03:28:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b5d92fa0-e3fd-3c75-bc3c-308803afbdbe | -5.15851 | -45.11153 | 2025-04-16 03:28:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 2e242c49-08a9-3047-a256-76add56e97f1 | -5.15937 | -45.11152 | 2025-04-16 03:28:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| c1b66145-0247-3a5d-997f-377b10e7cc0b | -7.11644 | -37.25766 | 2025-04-16 03:28:00 | NOAA-21 | SÃO JOSÉ DO BONFIM | PARAÍBA | Brasil | 2514602 | 25 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 86847fb4-82e5-332d-86be-7762e8751be4 | -5.16665 | -45.10637 | 2025-04-16 03:28:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 754af4a4-0b2a-3a54-9c68-6ee764aeb02e | -5.94128 | -44.46825 | 2025-04-16 03:28:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| a7493389-b8c3-356d-ad35-87d7957f6b65 | -5.94891 | -44.46394 | 2025-04-16 03:28:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 86c80341-8ed8-33f8-87b8-17e4d9373fd4 | -5.94461 | -44.46192 | 2025-04-16 03:28:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 4e7e0454-2ca0-3115-9dee-8cdba19d296c | -5.1654 | -45.11305 | 2025-04-16 03:28:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 8cbe5780-22db-34d8-a871-aa7fffc6ef6e | -5.94361 | -44.46749 | 2025-04-16 03:28:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 93eb43b3-b63b-30ac-8c4b-d24b66b1f61c | -5.46879 | -39.52121 | 2025-04-16 03:28:00 | NOAA-21 | SENADOR POMPEU | CEARÁ | Brasil | 2312700 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| e4a139c8-f480-3b4b-a858-3ab7ca33eb83 | -5.94231 | -44.46271 | 2025-04-16 03:28:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| dd7b3ab9-5b75-3c57-a8ea-950560e15725 | -5.07181 | -37.71565 | 2025-04-16 03:28:00 | NOAA-21 | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 607742ac-bec8-3296-acb3-22014d76a047 | -9.56201 | -35.69341 | 2025-04-16 03:30:00 | NOAA-21 | MACEIÓ | ALAGOAS | Brasil | 2704302 | 27 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| fa74528a-73da-3365-8307-64fa91fb21a4 | -8.11045 | -43.12385 | 2025-04-16 03:30:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 39476043-ec46-33ab-85de-5adf8db6213d | -8.52926 | -36.37534 | 2025-04-16 03:30:00 | NOAA-21 | SÃO BENTO DO UNA | PERNAMBUCO | Brasil | 2613008 | 26 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 6b027401-dfef-3189-b46b-2d5ce8e0c8aa | -8.1118 | -43.12557 | 2025-04-16 03:30:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| faef9a6e-8ad3-3c5f-80eb-7b95845414b6 | -11.53934 | -37.81804 | 2025-04-16 03:30:00 | NOAA-21 | JANDAÍRA | BAHIA | Brasil | 2917904 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 97b98497-a57f-357e-937b-b3407ac81ced | -9.67488 | -37.07516 | 2025-04-16 03:30:00 | NOAA-21 | BATALHA | ALAGOAS | Brasil | 2700706 | 27 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 15b4afe3-797f-3707-bfb1-dea3a6d5a2e4 | -8.39115 | -35.02362 | 2025-04-16 03:30:00 | NOAA-21 | IPOJUCA | PERNAMBUCO | Brasil | 2607208 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 3e30a044-3b3e-369d-9e78-24ef90da69c8 | -11.97369 | -40.29058 | 2025-04-16 03:30:00 | NOAA-21 | BAIXA GRANDE | BAHIA | Brasil | 2902609 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 09e90b2f-3837-3599-9243-33091a035c45 | -9.81807 | -36.98883 | 2025-04-16 03:30:00 | NOAA-21 | TRAIPU | ALAGOAS | Brasil | 2709202 | 27 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 0412415f-a37a-3ad2-840b-1d182410f519 | -8.11259 | -43.12128 | 2025-04-16 03:30:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 778abf83-744b-33fc-94a4-fd00361a267e | -8.39408 | -37.06908 | 2025-04-16 03:30:00 | NOAA-21 | ARCOVERDE | PERNAMBUCO | Brasil | 2601201 | 26 | 33 | nan | nan | nan | Caatinga | 1.2 |
| e8eb5532-f6d2-3d07-ae07-a2a4e5db30a6 | -10.69439 | -37.04881 | 2025-04-16 03:30:00 | NOAA-21 | ROSÁRIO DO CATETE | SERGIPE | Brasil | 2806107 | 28 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 1fb1e549-3817-341f-9db9-e4188fd0aae7 | -9.6159 | -37.03782 | 2025-04-16 03:30:00 | NOAA-21 | MAJOR ISIDORO | ALAGOAS | Brasil | 2704401 | 27 | 33 | nan | nan | nan | Caatinga | 2.0 |
| fec1b47e-0da0-343f-b2e5-48652f704d94 | -29.77902 | -51.17816 | 2025-04-16 03:36:00 | NOAA-21 | SÃO LEOPOLDO | RIO GRANDE DO SUL | Brasil | 4318705 | 43 | 33 | nan | nan | nan | Pampa | 1.6 |
| fe0b90ef-a88c-39b3-91c2-6d551b5b0d45 | -28.58434 | -49.44041 | 2025-04-16 03:36:00 | NOAA-21 | SIDERÓPOLIS | SANTA CATARINA | Brasil | 4217600 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 4eddaf03-edd8-388c-b8cd-2612e40359df | -5.53081 | -36.8129 | 2025-04-16 03:53:00 | NPP-375D | IPANGUAÇU | RIO GRANDE DO NORTE | Brasil | 2404705 | 24 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 832a8eb4-2eb3-383a-ae92-c4faf3da9efe | -3.12926 | -40.99023 | 2025-04-16 03:53:00 | NPP-375D | GRANJA | CEARÁ | Brasil | 2304707 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 12202a8f-bcb3-30e8-9a61-7ab73802cfbf | -5.06871 | -37.71612 | 2025-04-16 03:53:00 | NPP-375D | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 1.2 |
| ef7c2dd2-fe8f-387f-96a6-55c60f71686b | -5.47002 | -39.52177 | 2025-04-16 03:53:00 | NPP-375D | SENADOR POMPEU | CEARÁ | Brasil | 2312700 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| b32e6791-ecd6-3dd8-9dce-ec66de2d3a9c | -5.47059 | -39.51816 | 2025-04-16 03:53:00 | NPP-375D | SENADOR POMPEU | CEARÁ | Brasil | 2312700 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 209614f2-14cd-38b0-9c4c-e027d3b25d04 | -11.36882 | -37.56528 | 2025-04-16 03:55:00 | NPP-375D | SANTA LUZIA DO ITANHY | SERGIPE | Brasil | 2806305 | 28 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 8ea79550-b276-3509-b82a-5654ef92abed | -6.34766 | -43.65509 | 2025-04-16 03:55:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 69d683f8-3af2-3b7f-9816-f092b5479aa3 | -12.06685 | -40.01821 | 2025-04-16 03:55:00 | NPP-375D | IPIRÁ | BAHIA | Brasil | 2914000 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 374f1f02-f5a7-3241-b27d-70cccd67f278 | -6.3524 | -43.65217 | 2025-04-16 03:55:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3281f91a-33c6-317b-aaa8-4c55cbe54b51 | -7.97475 | -35.61802 | 2025-04-16 03:55:00 | NPP-375D | PASSIRA | PERNAMBUCO | Brasil | 2610509 | 26 | 33 | nan | nan | nan | Caatinga | 0.5 |
| e98ee1c2-321c-3a39-b97b-9c70d73b32f2 | -7.94878 | -37.17498 | 2025-04-16 03:55:00 | NPP-375D | MONTEIRO | PARAÍBA | Brasil | 2509701 | 25 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 681a6911-c9f1-307d-91af-2b372d7f2afa | -6.34513 | -43.65923 | 2025-04-16 03:55:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 95cfbd0c-b8c6-32bd-84af-ca7cefca3fda | -5.16422 | -45.10489 | 2025-04-16 03:55:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| c18885c8-502b-3a44-b1aa-b357d3d5b656 | -9.67574 | -37.07372 | 2025-04-16 03:55:00 | NPP-375D | BATALHA | ALAGOAS | Brasil | 2700706 | 27 | 33 | nan | nan | nan | Caatinga | 1.6 |
| c17d4afb-a41e-3a65-a61a-4182d1696a0b | -6.66236 | -47.59307 | 2025-04-16 03:55:00 | NPP-375D | PALMEIRAS DO TOCANTINS | TOCANTINS | Brasil | 1713809 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| dcba5743-9ffb-3456-af96-c75088fc9ccf | -6.66174 | -47.59649 | 2025-04-16 03:55:00 | NPP-375D | PALMEIRAS DO TOCANTINS | TOCANTINS | Brasil | 1713809 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 3e9faf58-ca21-394d-98a2-b32408f78be7 | -7.5689 | -45.84581 | 2025-04-16 03:55:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2522c6bf-dbbb-3c4d-b8f5-8d0d18bbf16c | -6.34631 | -43.65203 | 2025-04-16 03:55:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 95585165-32d0-3cb2-b48f-a31beeed5793 | -6.34352 | -43.65445 | 2025-04-16 03:55:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8ebc5d2b-149b-3eac-ae1a-d92c0227ca09 | -11.53992 | -37.81654 | 2025-04-16 03:55:00 | NPP-375D | JANDAÍRA | BAHIA | Brasil | 2917904 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| f3fb1576-dcdf-3ac9-97f0-55ba2cf9f21d | -13.01615 | -39.05617 | 2025-04-16 03:55:00 | NPP-375D | MUNIZ FERREIRA | BAHIA | Brasil | 2922201 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| a86e7694-7ffa-3e07-84eb-63255dd69245 | -5.1634 | -45.10972 | 2025-04-16 03:55:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| fb269387-d43b-3335-8cf7-46bfceebb0e8 | -7.11558 | -37.25827 | 2025-04-16 03:55:00 | NPP-375D | SÃO JOSÉ DO BONFIM | PARAÍBA | Brasil | 2514602 | 25 | 33 | nan | nan | nan | Caatinga | 1.4 |
| b65970a4-2262-39f0-9042-31bc8e390776 | -6.3404 | -43.66216 | 2025-04-16 03:55:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 07d4ee29-9cd9-3aab-b0b3-e69f96bfcb13 | -6.43744 | -36.21072 | 2025-04-16 03:55:00 | NPP-375D | NOVA FLORESTA | PARAÍBA | Brasil | 2510105 | 25 | 33 | nan | nan | nan | Caatinga | 0.8 |
| aa39d315-5535-306b-9627-ac5c3ca4693a | -11.97298 | -40.29044 | 2025-04-16 03:55:00 | NPP-375D | BAIXA GRANDE | BAHIA | Brasil | 2902609 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 489f2a11-89a8-3376-a9bf-6c5cebe9d628 | -5.6423 | -43.70862 | 2025-04-16 03:55:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 2f63040f-a4bf-3899-9e90-a1d99e584bef | -6.34228 | -43.66167 | 2025-04-16 03:55:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 37eeb618-b996-3f20-a9ce-efcce2b8d096 | -6.34573 | -43.6556 | 2025-04-16 03:55:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 2ee3001f-1ec9-3a9e-9ed8-43ceaba1edd7 | -6.66112 | -47.59996 | 2025-04-16 03:55:00 | NPP-375D | PALMEIRAS DO TOCANTINS | TOCANTINS | Brasil | 1713809 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 3036bec4-baf3-3b4a-a986-2f2da08975c0 | -6.71638 | -47.6001 | 2025-04-16 03:55:00 | NPP-375D | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9c07e123-fcbd-35c6-b4c1-05fe5bbad625 | -9.6157 | -37.03428 | 2025-04-16 03:55:00 | NPP-375D | MAJOR ISIDORO | ALAGOAS | Brasil | 2704401 | 27 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 571dfa71-be69-30d0-9af0-7a6223685c91 | -6.66296 | -47.58967 | 2025-04-16 03:55:00 | NPP-375D | PALMEIRAS DO TOCANTINS | TOCANTINS | Brasil | 1713809 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 7b6b43c5-2ff8-31f1-a533-d1cacc2f44ea | -6.35116 | -43.6594 | 2025-04-16 03:55:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 086aaca1-1e7a-384f-82a4-02bd5ef17948 | -5.64167 | -43.71245 | 2025-04-16 03:55:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 0b034914-8c4a-35c9-9be2-20d1bb93d078 | -5.94785 | -44.46098 | 2025-04-16 03:55:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a6d6ef32-ba67-36fb-bb25-059d13799f56 | -9.56323 | -35.69299 | 2025-04-16 03:55:00 | NPP-375D | MACEIÓ | ALAGOAS | Brasil | 2704302 | 27 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 5b51ef29-777b-3b86-99a5-176768c84b8c | -5.93767 | -44.46782 | 2025-04-16 03:55:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| b220b57a-bbf9-3efe-b66c-79cdc6c951c9 | -6.34641 | -43.66236 | 2025-04-16 03:55:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 94b2ed80-2a47-3abf-afb4-2dd8a172cd3a | -6.3429 | -43.65806 | 2025-04-16 03:55:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 47323a1f-852d-3fda-ba5b-f697b147f5e8 | -11.72619 | -37.62227 | 2025-04-16 03:55:00 | NPP-375D | CONDE | BAHIA | Brasil | 2908606 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 078629ae-d720-3c29-9965-e17a75e99161 | -5.94714 | -44.46519 | 2025-04-16 03:55:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| bdccf8aa-3f6b-30a0-ae69-be7cc83516c2 | -6.35179 | -43.65574 | 2025-04-16 03:55:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 2e345e33-950c-381f-b7a0-68abe050ab10 | -6.36004 | -43.65714 | 2025-04-16 03:55:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 53689217-4b99-3d67-933a-385b3bc36742 | -5.64294 | -43.7048 | 2025-04-16 03:55:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 7109c6cf-6647-3dd3-bf8d-0472b8746190 | -9.81725 | -36.98985 | 2025-04-16 03:55:00 | NPP-375D | TRAIPU | ALAGOAS | Brasil | 2709202 | 27 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 16c6604a-797a-3c80-a545-1313257fe4fc | -8.53743 | -37.72235 | 2025-04-16 03:55:00 | NPP-375D | IBIMIRIM | PERNAMBUCO | Brasil | 2606606 | 26 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 73d2921d-3648-35fb-be42-acad48008178 | -6.36066 | -43.6535 | 2025-04-16 03:55:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8695db5a-cea4-3926-af4e-d908c2bfecb0 | -6.71158 | -47.59599 | 2025-04-16 03:55:00 | NPP-375D | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| de9139a4-d6c5-315f-bcbc-63d8e3779f19 | -5.93838 | -44.46365 | 2025-04-16 03:55:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f30ceb90-e109-37b3-a73c-bb791e7fc680 | -6.33877 | -43.6574 | 2025-04-16 03:55:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 48c12035-a273-3939-bc03-2f3a34f551d2 | -6.71697 | -47.59677 | 2025-04-16 03:55:00 | NPP-375D | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| de05a167-5415-357d-93a4-ec080136d5e3 | -8.99094 | -37.35978 | 2025-04-16 03:55:00 | NPP-375D | ITAÍBA | PERNAMBUCO | Brasil | 2607505 | 26 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 8bfd1f31-b727-3601-8447-2abbf8e37f9a | -9.67656 | -37.0746 | 2025-04-16 03:55:00 | NPP-375D | BATALHA | ALAGOAS | Brasil | 2700706 | 27 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 68d4c637-ccac-3b81-ba17-825ba7d806c6 | -5.94205 | -44.46859 | 2025-04-16 03:55:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| fa5f1f44-5c73-3e2a-b00c-6995537e1c1b | -8.53407 | -37.72181 | 2025-04-16 03:55:00 | NPP-375D | IBIMIRIM | PERNAMBUCO | Brasil | 2606606 | 26 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 9539a6b6-3ec1-33dd-8987-b4c0e6ad70de | -9.85978 | -37.19768 | 2025-04-16 03:55:00 | NPP-375D | BELO MONTE | ALAGOAS | Brasil | 2700904 | 27 | 33 | nan | nan | nan | Caatinga | 0.8 |
| ec3a669d-58cd-35ba-bbf5-5849c69a1b3d | -8.11035 | -43.12166 | 2025-04-16 03:55:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| f48d8c71-6ac0-305d-b325-8006c9ef9916 | -5.94276 | -44.46442 | 2025-04-16 03:55:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |


[Clique aqui para ver as próximas entradas](README2.md)
