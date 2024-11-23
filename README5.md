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
| 364e5ae5-2a78-3538-a187-eea0d36b9c49 | -7.97187 | -35.07724 | 2024-11-23 00:07:00 | TERRA_M-M | SÃO LOURENÇO DA MATA | PERNAMBUCO | Brasil | 2613701 | 26 | 33 | nan | nan | nan | Mata Atlântica | 40.6 |
| 52c5ad0c-db41-3f90-895a-9f5a6fbbc22e | -7.04857 | -40.41986 | 2024-11-23 00:07:00 | TERRA_M-M | CAMPOS SALES | CEARÁ | Brasil | 2302701 | 23 | 33 | nan | nan | nan | Caatinga | 6.6 |
| 376d1dae-19af-32df-a665-48cf74db2075 | -7.13271 | -39.06171 | 2024-11-23 00:07:00 | TERRA_M-M | AURORA | CEARÁ | Brasil | 2301703 | 23 | 33 | nan | nan | nan | Caatinga | 5.9 |
| dc60a959-6ad4-340e-a27a-a28115cfcc98 | -6.21909 | -39.42377 | 2024-11-23 00:07:00 | TERRA_M-M | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 4.9 |
| 2538e90f-448a-392e-8c7f-80df93c49183 | -6.56428 | -39.77028 | 2024-11-23 00:07:00 | TERRA_M-M | SABOEIRO | CEARÁ | Brasil | 2311900 | 23 | 33 | nan | nan | nan | Caatinga | 10.9 |
| 7b8aa94b-e24d-303d-9a9e-816da8965189 | -9.81813 | -39.14331 | 2024-11-23 00:07:00 | TERRA_M-M | CANUDOS | BAHIA | Brasil | 2906824 | 29 | 33 | nan | nan | nan | Caatinga | 12.5 |
| 6d2d4377-cd87-3be4-bdf4-63fea5ac499f | -10.67842 | -37.05092 | 2024-11-23 00:07:00 | TERRA_M-M | ROSÁRIO DO CATETE | SERGIPE | Brasil | 2806107 | 28 | 33 | nan | nan | nan | Mata Atlântica | 8.3 |
| 3d4f2a13-c606-3d56-9180-e900bab849e4 | -9.38093 | -35.79184 | 2024-11-23 00:07:00 | TERRA_M-M | MESSIAS | ALAGOAS | Brasil | 2705200 | 27 | 33 | nan | nan | nan | Mata Atlântica | 5.0 |
| 5a60e391-771d-3f01-93c8-806b317ec817 | -5.57726 | -38.98011 | 2024-11-23 00:07:00 | TERRA_M-M | SOLONÓPOLE | CEARÁ | Brasil | 2313005 | 23 | 33 | nan | nan | nan | Caatinga | 6.9 |
| 0cf8a4fa-232f-3a6f-be35-c58477ee5b8b | -10.50145 | -36.69837 | 2024-11-23 00:07:00 | TERRA_M-M | PACATUBA | SERGIPE | Brasil | 2804904 | 28 | 33 | nan | nan | nan | Mata Atlântica | 11.8 |
| dab21272-b313-34bb-95e2-6845b1b349c8 | -9.81961 | -39.15459 | 2024-11-23 00:07:00 | TERRA_M-M | CANUDOS | BAHIA | Brasil | 2906824 | 29 | 33 | nan | nan | nan | Caatinga | 22.8 |
| 06370831-da6b-3292-8391-2a5145d42982 | -8.15466 | -38.24666 | 2024-11-23 00:07:00 | TERRA_M-M | SERRA TALHADA | PERNAMBUCO | Brasil | 2613909 | 26 | 33 | nan | nan | nan | Caatinga | 10.1 |
| e59c720a-fae2-34bb-ac1b-286858ae5141 | -5.94785 | -39.67423 | 2024-11-23 00:07:00 | TERRA_M-M | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 22.9 |
| e6076266-bc47-30a2-b4a2-6f6c80f98188 | -5.8638 | -39.65896 | 2024-11-23 00:07:00 | TERRA_M-M | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 9.0 |
| 4b94e7f0-0103-396a-964a-6330e7c4b05b | -10.04282 | -36.10955 | 2024-11-23 00:07:00 | TERRA_M-M | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 7.0 |
| 74cbaf84-18f8-3b8c-afd7-27c2b28d8b0f | -11.87835 | -38.34769 | 2024-11-23 00:07:00 | TERRA_M-M | INHAMBUPE | BAHIA | Brasil | 2913705 | 29 | 33 | nan | nan | nan | Caatinga | 6.3 |
| fdc51452-b696-3d30-b346-89ce9a404a09 | -9.73678 | -37.02929 | 2024-11-23 00:07:00 | TERRA_M-M | BATALHA | ALAGOAS | Brasil | 2700706 | 27 | 33 | nan | nan | nan | Caatinga | 21.2 |
| 65b7e206-a7b8-3a40-9155-002aaf849a4d | -6.84487 | -34.92739 | 2024-11-23 00:07:00 | TERRA_M-M | RIO TINTO | PARAÍBA | Brasil | 2512903 | 25 | 33 | nan | nan | nan | Mata Atlântica | 5.8 |
| b7bf1245-6f90-3431-9816-e25fcd43f385 | -9.93562 | -36.33812 | 2024-11-23 00:07:00 | TERRA_M-M | TEOTÔNIO VILELA | ALAGOAS | Brasil | 2709152 | 27 | 33 | nan | nan | nan | Mata Atlântica | 67.7 |
| 3da097e3-c7c1-3865-8f25-e281c7ddcd52 | -7.13134 | -39.05146 | 2024-11-23 00:07:00 | TERRA_M-M | AURORA | CEARÁ | Brasil | 2301703 | 23 | 33 | nan | nan | nan | Caatinga | 6.4 |
| b954eca6-110f-381f-8eee-728a731b5e84 | -7.31748 | -34.94584 | 2024-11-23 00:07:00 | TERRA_M-M | ALHANDRA | PARAÍBA | Brasil | 2500601 | 25 | 33 | nan | nan | nan | Mata Atlântica | 8.8 |
| bd6cea8e-33f3-32f3-bf4d-af2f07a25eb9 | -8.66294 | -36.98072 | 2024-11-23 00:07:00 | TERRA_M-M | BUÍQUE | PERNAMBUCO | Brasil | 2602803 | 26 | 33 | nan | nan | nan | Caatinga | 8.5 |
| 237fe6cf-9b74-3741-9e41-94fd64ae6d1c | -7.6099 | -38.97544 | 2024-11-23 00:07:00 | TERRA_M-M | BREJO SANTO | CEARÁ | Brasil | 2302503 | 23 | 33 | nan | nan | nan | Caatinga | 23.0 |
| 44afbfd4-2269-3ed6-9476-2b2542f6aa13 | -8.87673 | -35.9328 | 2024-11-23 00:07:00 | TERRA_M-M | SÃO BENEDITO DO SUL | PERNAMBUCO | Brasil | 2612901 | 26 | 33 | nan | nan | nan | Mata Atlântica | 5.7 |
| b13686b3-67bd-3d5a-a182-d71007fe375d | -5.86527 | -39.66967 | 2024-11-23 00:07:00 | TERRA_M-M | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 19.3 |
| 5e806d88-458b-356a-946b-17a9a9074acd | -6.47516 | -39.10092 | 2024-11-23 00:07:00 | TERRA_M-M | CEDRO | CEARÁ | Brasil | 2303808 | 23 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 27a1d985-cf44-3ec7-a1d4-3c6d299d1acd | -9.44872 | -35.81263 | 2024-11-23 00:07:00 | TERRA_M-M | RIO LARGO | ALAGOAS | Brasil | 2707701 | 27 | 33 | nan | nan | nan | Mata Atlântica | 4.7 |
| 373ab289-0be0-391b-97e0-b1fadef5253a | -9.928 | -36.34835 | 2024-11-23 00:07:00 | TERRA_M-M | TEOTÔNIO VILELA | ALAGOAS | Brasil | 2709152 | 27 | 33 | nan | nan | nan | Mata Atlântica | 94.0 |
| d6cde94a-74b5-3614-a77d-fcf690ea6b22 | -10.47102 | -37.14905 | 2024-11-23 00:07:00 | TERRA_M-M | NOSSA SENHORA DAS DORES | SERGIPE | Brasil | 2804607 | 28 | 33 | nan | nan | nan | Mata Atlântica | 22.2 |
| 6be7bf9d-a7a3-3637-ad31-640dab30f7a3 | -5.59727 | -37.98648 | 2024-11-23 00:07:00 | TERRA_M-M | APODI | RIO GRANDE DO NORTE | Brasil | 2401008 | 24 | 33 | nan | nan | nan | Caatinga | 7.8 |
| 3fd1180b-17e5-3afa-b294-829cbb753762 | -10.46976 | -37.13975 | 2024-11-23 00:07:00 | TERRA_M-M | NOSSA SENHORA DAS DORES | SERGIPE | Brasil | 2804607 | 28 | 33 | nan | nan | nan | Mata Atlântica | 120.2 |
| 804933e2-7c6a-3031-8228-73a2c16e2f50 | -6.86384 | -39.57595 | 2024-11-23 00:07:00 | TERRA_M-M | FARIAS BRITO | CEARÁ | Brasil | 2304301 | 23 | 33 | nan | nan | nan | Caatinga | 5.7 |
| d48f4b3f-4172-3545-98c1-bb64189575ce | -9.72782 | -37.03056 | 2024-11-23 00:07:00 | TERRA_M-M | BATALHA | ALAGOAS | Brasil | 2700706 | 27 | 33 | nan | nan | nan | Caatinga | 9.6 |
| fd2b7ac9-7286-3e7f-8315-7d4170b9ce16 | -8.17149 | -35.05486 | 2024-11-23 00:07:00 | TERRA_M-M | JABOATÃO DOS GUARARAPES | PERNAMBUCO | Brasil | 2607901 | 26 | 33 | nan | nan | nan | Mata Atlântica | 8.3 |
| d8987421-8cf5-3a78-8065-eafb2a736fca | -8.16241 | -35.05619 | 2024-11-23 00:07:00 | TERRA_M-M | JABOATÃO DOS GUARARAPES | PERNAMBUCO | Brasil | 2607901 | 26 | 33 | nan | nan | nan | Mata Atlântica | 12.2 |
| 73862884-f6b7-3b4b-8f29-e9a49a706b3f | -10.51038 | -36.69709 | 2024-11-23 00:07:00 | TERRA_M-M | PACATUBA | SERGIPE | Brasil | 2804904 | 28 | 33 | nan | nan | nan | Mata Atlântica | 18.1 |
| 4a00714e-0620-3ec5-97e0-c2cc50725913 | -6.25518 | -43.55491 | 2024-11-23 00:07:00 | TERRA_M-M | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 21.9 |
| b78c51dc-44cb-31ae-bcbe-5cca491ad32d | -7.48667 | -41.75195 | 2024-11-23 00:07:00 | TERRA_M-M | FLORESTA DO PIAUÍ | PIAUÍ | Brasil | 2203859 | 22 | 33 | nan | nan | nan | Caatinga | 12.3 |
| 924e64c5-f5d3-3b27-8e89-99148ef81ac3 | -6.35192 | -39.7945 | 2024-11-23 00:07:00 | TERRA_M-M | SABOEIRO | CEARÁ | Brasil | 2311900 | 23 | 33 | nan | nan | nan | Caatinga | 20.9 |
| 95d7980c-17d1-3683-9abc-e840787ab379 | -10.04406 | -36.1185 | 2024-11-23 00:07:00 | TERRA_M-M | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 40.2 |
| 518fb90e-5aed-312e-9bb1-4a93d7674ae4 | -7.6113 | -38.98577 | 2024-11-23 00:07:00 | TERRA_M-M | BREJO SANTO | CEARÁ | Brasil | 2302503 | 23 | 33 | nan | nan | nan | Caatinga | 9.8 |
| f640f520-0529-3eb7-b729-31ec8f475d35 | -7.97321 | -35.08661 | 2024-11-23 00:07:00 | TERRA_M-M | SÃO LOURENÇO DA MATA | PERNAMBUCO | Brasil | 2613701 | 26 | 33 | nan | nan | nan | Mata Atlântica | 56.4 |
| d3664fe0-b936-368e-81f7-4d0cebd7c328 | -9.79738 | -36.13577 | 2024-11-23 00:07:00 | TERRA_M-M | SÃO MIGUEL DOS CAMPOS | ALAGOAS | Brasil | 2708600 | 27 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| 9ae7b0e9-7b86-3291-83fc-56858897c4e4 | -6.74925 | -35.48511 | 2024-11-23 00:07:00 | TERRA_M-M | BELÉM | PARAÍBA | Brasil | 2501906 | 25 | 33 | nan | nan | nan | Caatinga | 5.0 |
| 2b90ee64-b19f-3ca2-b6bf-9642a9d78fb1 | -3.16429 | -45.72707 | 2024-11-23 00:09:00 | TERRA_M-M | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 43.0 |
| d8f40a59-760d-360a-a43b-d24694ad599f | -6.15495 | -46.67851 | 2024-11-23 00:09:00 | TERRA_M-M | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 59.2 |
| 853d28da-e678-35d9-8773-a0765d44ddb9 | -3.53225 | -43.32916 | 2024-11-23 00:09:00 | TERRA_M-M | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 23.8 |
| c89148dd-d20e-3b45-a24b-7103f935040a | -2.70985 | -46.29535 | 2024-11-23 00:09:00 | TERRA_M-M | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 41.0 |
| fa99cb01-8d10-3ade-bc52-fae7dcda99b5 | -4.72861 | -45.50242 | 2024-11-23 00:09:00 | TERRA_M-M | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Cerrado | 38.4 |
| 71dad0ea-e204-302c-ac54-05a0b4da1e18 | -4.02846 | -46.1869 | 2024-11-23 00:09:00 | TERRA_M-M | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 32.7 |
| b39739e3-5d27-3f08-adaa-dd423e1e5986 | -5.22539 | -45.11574 | 2024-11-23 00:09:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 18.4 |
| c8874ee6-2634-3f09-972d-0651d3531b46 | -2.71313 | -46.10758 | 2024-11-23 00:09:00 | TERRA_M-M | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 25.9 |
| 2c086480-2358-3eb9-903d-1e07af62544d | -4.53636 | -45.87191 | 2024-11-23 00:09:00 | TERRA_M-M | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 19.8 |
| 6c6d515e-006e-3890-8a62-a93cbeb2698d | -4.50313 | -44.71459 | 2024-11-23 00:09:00 | TERRA_M-M | TRIZIDELA DO VALE | MARANHÃO | Brasil | 2112233 | 21 | 33 | nan | nan | nan | Cerrado | 39.6 |
| 096c4720-1071-381d-8dee-ffe0f7d47b27 | -4.66017 | -45.68598 | 2024-11-23 00:09:00 | TERRA_M-M | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 67.2 |
| ae5fa46f-bb04-378d-ad10-a6f58d91088f | -3.63421 | -45.72078 | 2024-11-23 00:09:00 | TERRA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 24.8 |
| fb1565b6-5cf0-3fb2-93e5-9ff0d5bbd2fe | -2.70575 | -46.26518 | 2024-11-23 00:09:00 | TERRA_M-M | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 84.4 |
| 80e070d3-eba5-3646-a4d1-114895fece99 | -2.93883 | -45.62993 | 2024-11-23 00:09:00 | TERRA_M-M | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 21.4 |
| be557247-faba-3d5d-a8fe-8b84ba9673e2 | -6.13813 | -46.68039 | 2024-11-23 00:09:00 | TERRA_M-M | LAJEADO NOVO | MARANHÃO | Brasil | 2105989 | 21 | 33 | nan | nan | nan | Cerrado | 23.7 |
| 63acb87d-0ecd-3431-9692-630da1184e25 | -3.7347 | -46.02591 | 2024-11-23 00:09:00 | TERRA_M-M | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 25.2 |
| 972eaa4b-1064-36ec-a4bd-9cb8c239b13f | -4.42408 | -44.11897 | 2024-11-23 00:09:00 | TERRA_M-M | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 74.5 |
| 8ea16ff7-d84f-329f-a4d8-078ddbe441f9 | -4.7273 | -45.49586 | 2024-11-23 00:09:00 | TERRA_M-M | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Cerrado | 43.0 |
| 38bf0274-0798-35d0-8a45-5074d32c659c | -2.68327 | -45.6609 | 2024-11-23 00:09:00 | TERRA_M-M | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 109.7 |
| ed74aeb0-73ab-3767-83cd-669617fc29bd | -3.72313 | -46.03401 | 2024-11-23 00:09:00 | TERRA_M-M | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 32.8 |
| a0712359-741b-34f4-a144-9398af5db507 | -5.10677 | -43.1585 | 2024-11-23 00:09:00 | TERRA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 65.3 |
| e967fbe6-21bb-3184-acce-998e77c4bee3 | -5.5389 | -45.79343 | 2024-11-23 00:09:00 | TERRA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 31.7 |
| 25c78b7e-d7a2-3c6c-a92a-df9a36b1d884 | -3.73863 | -46.05595 | 2024-11-23 00:09:00 | TERRA_M-M | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 47.5 |
| 50a6726f-1134-3e2b-bb71-fe9c6644bd8c | -4.10113 | -42.48105 | 2024-11-23 00:09:00 | TERRA_M-M | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 21.8 |
| 8745993b-dbea-3daa-8f7d-97c3804564b4 | -3.61918 | -45.72265 | 2024-11-23 00:09:00 | TERRA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 17.6 |
| bcb8c0c5-8760-3edf-a7ad-59c009d2cec1 | -5.75338 | -46.25102 | 2024-11-23 00:09:00 | TERRA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 44.8 |
| 58b3b548-681d-3fcf-8eaa-da17ea8aa4f5 | -1.52412 | -47.30019 | 2024-11-23 00:09:00 | TERRA_M-M | BONITO | PARÁ | Brasil | 1501600 | 15 | 33 | nan | nan | nan | Amazônia | 33.1 |
| 1fed0dbe-7008-3529-9625-dfa2540e2dd1 | -2.88957 | -45.36823 | 2024-11-23 00:09:00 | TERRA_M-M | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 20.1 |
| 337be777-c30d-3b0d-90b2-92563b089c47 | -4.67791 | -45.6885 | 2024-11-23 00:09:00 | TERRA_M-M | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 21.8 |
| 8bd066c7-549e-336c-a498-4e8ff0d7970a | -2.96591 | -45.1778 | 2024-11-23 00:09:00 | TERRA_M-M | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 26.4 |
| 45e42ba9-34d9-3364-a9bf-61971bd3bfe2 | -4.52668 | -42.9239 | 2024-11-23 00:09:00 | TERRA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 103.5 |
| 94842804-7287-356f-a24b-dc793196bab8 | -4.6067 | -46.50988 | 2024-11-23 00:09:00 | TERRA_M-M | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 249.6 |
| 9d5b850e-073c-3046-be17-6a492b6cc60c | -2.86599 | -45.32563 | 2024-11-23 00:09:00 | TERRA_M-M | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 25.6 |
| ffea7f7c-f5b0-3c92-be06-0f9b4d4975d1 | -2.68374 | -45.65553 | 2024-11-23 00:09:00 | TERRA_M-M | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 106.3 |
| 5e438d14-a9e7-3f70-acbd-42deaf4e3f02 | -2.95849 | -45.19877 | 2024-11-23 00:09:00 | TERRA_M-M | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 39.7 |
| a50423f9-bb13-30bc-933b-fa23b364acd7 | -4.69426 | -44.40672 | 2024-11-23 00:09:00 | TERRA_M-M | CAPINZAL DO NORTE | MARANHÃO | Brasil | 2102754 | 21 | 33 | nan | nan | nan | Cerrado | 62.2 |
| 3ab016c3-a619-3ef8-a6de-a711e5d1738b | -6.05766 | -44.04198 | 2024-11-23 00:09:00 | TERRA_M-M | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 19.0 |
| 68a85e3e-6084-3ebf-aea3-497a924e3976 | -2.13188 | -46.40969 | 2024-11-23 00:09:00 | TERRA_M-M | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 29.8 |
| 186da9c7-9e86-3760-9c86-b151f7a9e8b9 | -2.7326 | -47.54552 | 2024-11-23 00:09:00 | TERRA_M-M | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 27.5 |
| aa649de4-9b95-3cd8-ba3d-0fdb4acfa2b5 | -4.52438 | -42.9066 | 2024-11-23 00:09:00 | TERRA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 80.8 |
| bb72e5ff-b1dd-3d8b-835b-f29a948f3343 | -4.67158 | -45.65406 | 2024-11-23 00:09:00 | TERRA_M-M | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 26.7 |
| b6749ca8-f77f-3ab0-8526-b92d7632180c | -4.59882 | -45.43991 | 2024-11-23 00:09:00 | TERRA_M-M | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Cerrado | 21.3 |
| a91dfe97-a7ab-3a28-b589-026ff30e6a22 | -4.35842 | -44.99871 | 2024-11-23 00:09:00 | TERRA_M-M | BOM LUGAR | MARANHÃO | Brasil | 2102077 | 21 | 33 | nan | nan | nan | Amazônia | 34.1 |
| 5ced4761-42a1-3c61-b4f4-2ab33137f975 | -5.11823 | -45.84005 | 2024-11-23 00:09:00 | TERRA_M-M | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 45.9 |
| 55a30b4e-1ea4-3f95-978e-747d1fc9a86e | -4.69788 | -45.83663 | 2024-11-23 00:09:00 | TERRA_M-M | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 58.7 |
| a5745744-bd8c-32f0-b850-d0e8216ab95a | -4.69813 | -45.86287 | 2024-11-23 00:09:00 | TERRA_M-M | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 93.7 |
| e67f3f52-8886-3e62-b1a6-4c7f28123c12 | -4.69419 | -45.83186 | 2024-11-23 00:09:00 | TERRA_M-M | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 30.7 |
| 51f3db81-6c54-3cf0-9e9a-257196833db4 | -4.67535 | -45.68363 | 2024-11-23 00:09:00 | TERRA_M-M | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 42.0 |
| 61689aa6-d290-3576-a12b-06b178793aea | -2.7359 | -47.53984 | 2024-11-23 00:09:00 | TERRA_M-M | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 35.9 |
| 8662d89e-18ca-3644-a818-88a3010b51fb | -3.46489 | -42.09573 | 2024-11-23 00:09:00 | TERRA_M-M | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 8.7 |
| 16a2cd3a-b4ee-3877-8663-7f25b6a2e5a9 | -3.78117 | -45.21542 | 2024-11-23 00:09:00 | TERRA_M-M | SATUBINHA | MARANHÃO | Brasil | 2111722 | 21 | 33 | nan | nan | nan | Amazônia | 18.1 |
| a5147d74-2856-3d0d-9e4d-d88d2951809b | -2.68705 | -45.68769 | 2024-11-23 00:09:00 | TERRA_M-M | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 23.8 |
| 542c3302-d19c-378c-8319-a1c3146ac4b6 | -2.68733 | -45.68237 | 2024-11-23 00:09:00 | TERRA_M-M | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 63.1 |
| de71f61e-d59f-35f5-a3b6-2e4a4f4cff30 | -6.49121 | -47.04781 | 2024-11-23 00:09:00 | TERRA_M-M | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 77.6 |
| 0f47012b-15f7-3531-866f-fd1a8aa62a2f | -4.26698 | -46.29683 | 2024-11-23 00:09:00 | TERRA_M-M | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 32.4 |
| cb2c7f36-a2bf-3698-85e6-d6374f9b899c | -4.38693 | -38.95725 | 2024-11-23 00:09:00 | TERRA_M-M | CAPISTRANO | CEARÁ | Brasil | 2302909 | 23 | 33 | nan | nan | nan | Caatinga | 5.2 |


[Clique aqui para ver as próximas entradas](README6.md)
