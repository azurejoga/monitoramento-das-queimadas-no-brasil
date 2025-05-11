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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2fc15ca0-033c-373d-af32-da1c6f06a999 | -10.50148 | -42.40094 | 2025-05-11 04:02:00 | NOAA-21 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 6a2946d1-1624-302d-85cc-45e703327fc3 | -14.65191 | -45.13884 | 2025-05-11 04:02:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7b50c77c-3034-307c-b873-a23a7c1f9374 | -11.40211 | -52.95052 | 2025-05-11 04:02:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 023e258e-9238-3efd-af2f-056290c4502d | -14.28308 | -42.69616 | 2025-05-11 04:02:00 | NOAA-21 | GUANAMBI | BAHIA | Brasil | 2911709 | 29 | 33 | nan | nan | nan | Caatinga | 2.1 |
| a865a300-da23-3557-9da2-6958fbb7c06e | -12.1771 | -54.23587 | 2025-05-11 04:02:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 487dca3b-e73c-3e21-a1fb-c8260d4c0fef | -14.65265 | -45.13454 | 2025-05-11 04:02:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4e701c74-0602-3ee5-a7f6-49e60eb97956 | -12.11078 | -47.98426 | 2025-05-11 04:02:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 9054bbfb-b305-385e-9499-f8fc7098b353 | -13.31357 | -47.16578 | 2025-05-11 04:02:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 267b107a-b961-3509-b67a-f071d5c9cde9 | -14.65053 | -45.1253 | 2025-05-11 04:02:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 608798ff-c7c0-31b7-bb02-e9052a7578ec | -9.03179 | -36.66711 | 2025-05-11 04:02:00 | NOAA-21 | TEREZINHA | PERNAMBUCO | Brasil | 2615102 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 0fb50d09-b263-3cdf-90a8-6f74d3b5f73f | -13.31705 | -47.17019 | 2025-05-11 04:02:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a256cf9b-2289-34d8-a046-3a7acd52e933 | -10.49837 | -46.17707 | 2025-05-11 04:02:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 90fcd647-4505-3740-a5a9-336c1ef6d3f8 | -12.32624 | -45.70247 | 2025-05-11 04:02:00 | NOAA-21 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| db813f3f-8ae5-3199-b7f3-67d88f71bd40 | -10.49022 | -46.1756 | 2025-05-11 04:02:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8a9757ea-1d91-3748-a41f-39787bde5d52 | -9.35 | -40.38685 | 2025-05-11 04:02:00 | NOAA-21 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 0.9 |
| f436f63d-7b2d-3897-b847-63b2ea577868 | -10.49869 | -42.39673 | 2025-05-11 04:02:00 | NOAA-21 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| ddbd6d7f-19c7-3b70-b8f9-42aed249ae3b | -13.02447 | -43.59725 | 2025-05-11 04:02:00 | NOAA-21 | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c033c569-d539-39f5-bed0-9b13ce7a0248 | -12.64999 | -54.07066 | 2025-05-11 04:02:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| eb23f1ea-30e8-3a72-bfac-6f43e09e7e22 | -12.52355 | -40.01818 | 2025-05-11 04:02:00 | NOAA-21 | ITABERABA | BAHIA | Brasil | 2914703 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 8f076d45-fbf1-3192-bb79-e730a505fb73 | -14.65127 | -45.12099 | 2025-05-11 04:02:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9c3e8214-e2f8-39fd-897f-8d1ecabd57a8 | -12.11158 | -47.9799 | 2025-05-11 04:02:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a26ae8fa-f692-3341-a34e-3b086aa50b1c | -12.59459 | -48.33931 | 2025-05-11 04:02:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 71f89a5f-fe76-3f63-bc8a-2470dfaebc20 | -8.9002 | -44.78465 | 2025-05-11 04:02:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f8a619f6-9170-3cfa-9f13-d458789a1484 | -11.12039 | -43.33555 | 2025-05-11 04:02:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 8aa49b53-322e-3351-b096-0f8a1c834724 | -14.64904 | -45.1339 | 2025-05-11 04:02:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b4d278ac-7dc9-3f64-8884-2adfb9542da1 | -9.0274 | -36.67112 | 2025-05-11 04:02:00 | NOAA-21 | TEREZINHA | PERNAMBUCO | Brasil | 2615102 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 0563e844-c3f3-3634-9494-57c66422389b | -11.11976 | -43.33942 | 2025-05-11 04:02:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 5.4 |
| 0c56f9e9-9582-3001-ab36-7fabae2c3a77 | -12.74334 | -47.99576 | 2025-05-11 04:02:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 633bef13-ecf4-3ad6-b026-eac830b4c15d | -11.56387 | -47.87267 | 2025-05-11 04:02:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| df4f145b-0ea4-3ffe-81ac-dfca2603a876 | -12.76719 | -47.99043 | 2025-05-11 04:02:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| f931140e-c4c3-3ad0-b8ff-d6accd27fef0 | -10.4943 | -46.1763 | 2025-05-11 04:02:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 56da6549-aaaa-3762-bbf7-b86bbae453e3 | -12.17047 | -54.23452 | 2025-05-11 04:02:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5b80bffa-c738-3e49-9c2e-95bcd5249789 | -11.39607 | -48.70304 | 2025-05-11 04:02:00 | NOAA-21 | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4ec1c86d-5358-30b9-b7a7-3f1b433c48c1 | -10.62669 | -46.3746 | 2025-05-11 04:02:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 88d4c1d8-853d-327f-af5e-db12baba8c62 | -9.60972 | -42.13964 | 2025-05-11 04:02:00 | NOAA-21 | REMANSO | BAHIA | Brasil | 2926004 | 29 | 33 | nan | nan | nan | Caatinga | 2.9 |
| b517bfa7-9f88-3420-aadb-bf4c592947d9 | -13.02103 | -43.59666 | 2025-05-11 04:02:00 | NOAA-21 | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| caf83f38-e1d9-3b47-b73e-b27190d5faf4 | -14.65414 | -45.12594 | 2025-05-11 04:02:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c5f145d5-76bd-3b2d-9bfb-c25e9d74fe69 | -14.28367 | -42.69255 | 2025-05-11 04:02:00 | NOAA-21 | GUANAMBI | BAHIA | Brasil | 2911709 | 29 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 2ad27ba2-fbba-3d9d-9204-02a29dcb8e5f | -11.3969 | -52.94417 | 2025-05-11 04:02:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f98c6b2b-990f-3a77-a658-91908e61c882 | -12.58549 | -48.33775 | 2025-05-11 04:02:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 66500479-dbb2-3958-9674-72cfb0daee64 | -12.17298 | -54.23659 | 2025-05-11 04:02:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| bfc194d7-89fa-301a-988b-40697e6bf038 | -10.63082 | -46.37527 | 2025-05-11 04:02:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 55481f97-ae85-3095-bd43-5606e4df303e | -11.39577 | -48.70119 | 2025-05-11 04:02:00 | NOAA-21 | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8ac2dba8-8a87-3fdd-a38c-e73fe62b5f7a | -14.13623 | -41.69288 | 2025-05-11 04:02:00 | NOAA-21 | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| a64d2991-d83a-3be4-977a-e52a06fbefeb | -9.56434 | -35.69116 | 2025-05-11 04:02:00 | NOAA-21 | MACEIÓ | ALAGOAS | Brasil | 2704302 | 27 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 2aeb1624-3a1e-38a9-9dd1-9cdd1c122895 | -12.32708 | -45.69757 | 2025-05-11 04:02:00 | NOAA-21 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 480859c5-4239-3f93-97b7-bb59be628399 | -13.80007 | -44.33686 | 2025-05-11 04:02:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 24c384b9-f898-35bd-a369-e5c5ad003d7c | -9.03113 | -36.67165 | 2025-05-11 04:02:00 | NOAA-21 | TEREZINHA | PERNAMBUCO | Brasil | 2615102 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| cb90bed7-bcac-3a3c-a280-e61d53c59d30 | -13.4864 | -52.97969 | 2025-05-11 04:04:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 5.1 |
| b8c61a1c-51b3-30a7-9247-363c70d261ca | -16.44067 | -43.46669 | 2025-05-11 04:04:00 | NOAA-21 | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7ad81955-9f7b-3208-b804-affca2fde6fe | -16.4965 | -43.13832 | 2025-05-11 04:04:00 | NOAA-21 | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 7e572a1f-c964-3f78-898d-b7f9d42327c3 | -21.39246 | -44.57185 | 2025-05-11 04:04:00 | NOAA-21 | CARRANCAS | MINAS GERAIS | Brasil | 3114600 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| fad261ed-e4cf-3d91-bd52-d3dfefacf184 | -22.14916 | -41.53131 | 2025-05-11 04:04:00 | NOAA-21 | QUISSAMÃ | RIO DE JANEIRO | Brasil | 3304151 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 603b4086-fd60-3a3a-83da-0195a306d09f | -14.65987 | -45.13583 | 2025-05-11 04:04:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| d74d5613-7f0a-3edd-88ca-24aff8fab6ce | -13.48418 | -52.96786 | 2025-05-11 04:04:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 5a97f8cb-fb7f-3d59-a6cd-49ed299a0ed1 | -20.16128 | -46.8405 | 2025-05-11 04:04:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 3.9 |
| e12c59bf-8789-3a5a-ad88-950af4c9acaa | -20.37762 | -45.60485 | 2025-05-11 04:04:00 | NOAA-21 | PAINS | MINAS GERAIS | Brasil | 3146503 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e2aef2a2-ba45-3243-a038-4deb00e98baa | -13.05332 | -53.72334 | 2025-05-11 04:04:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 09141b48-5b76-328a-89a2-cc843b6c407b | -20.19547 | -46.71213 | 2025-05-11 04:04:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 34ca7621-880c-3d77-990a-e00c2ca1a40c | -20.16653 | -46.83232 | 2025-05-11 04:04:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 04ac620d-abf3-3413-8c77-1fffd9c00ae2 | -20.16212 | -46.83584 | 2025-05-11 04:04:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 3.9 |
| d27997f4-82d7-34ca-a956-fb56271af91b | -16.68286 | -43.88284 | 2025-05-11 04:04:00 | NOAA-21 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 69102689-6fac-3e3a-b771-62fbc356cada | -17.921 | -45.54686 | 2025-05-11 04:04:00 | NOAA-21 | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a27f0ddf-a8e1-3b9e-9eca-dc245d1d6387 | -13.03964 | -53.72554 | 2025-05-11 04:04:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 0dec2b15-3b69-35b0-976e-d24fe859a17f | -13.48833 | -52.97801 | 2025-05-11 04:04:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 5.3 |
| cd4ae2e4-a58d-3a24-ba70-8a88c8ec7aad | -14.65626 | -45.13519 | 2025-05-11 04:04:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 6cfa519b-37a2-3476-994d-c2d895c0b4d1 | -14.67144 | -45.1335 | 2025-05-11 04:04:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2e3a05fc-c78b-3256-895a-39d726066bee | -17.46292 | -44.7145 | 2025-05-11 04:04:00 | NOAA-21 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3c640d9c-de97-35f5-a654-29d4bf1cd123 | -14.66858 | -45.12853 | 2025-05-11 04:04:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 7512149c-20b1-3afe-af74-e99588381f7f | -16.4971 | -43.13467 | 2025-05-11 04:04:00 | NOAA-21 | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5b67c882-28d4-3920-8ed3-e010130bd1a6 | -13.47437 | -52.9772 | 2025-05-11 04:04:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 3f9ce289-38b9-3ae5-aa1c-ef68a26ac718 | -20.19468 | -46.71661 | 2025-05-11 04:04:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 6dd7c7d1-0b79-3875-9422-bacac47c664e | -20.19027 | -46.72025 | 2025-05-11 04:04:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| f508bb9d-fd75-3c1b-ba74-c8db98ef6a1d | -14.22067 | -54.55646 | 2025-05-11 04:04:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ec8719a9-baa0-3189-88be-295ed398667c | -20.17778 | -46.81164 | 2025-05-11 04:04:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 8f4bef98-c4be-3cd3-9f06-1d66f0d4db3a | -14.87246 | -51.98214 | 2025-05-11 04:04:00 | NOAA-21 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 4.7 |
| d3721846-be48-3923-beaa-7f8525f5364f | -20.17258 | -46.8196 | 2025-05-11 04:04:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f2381631-28ac-3c8c-924c-9b44a40eb78d | -20.34983 | -40.36343 | 2025-05-11 04:04:00 | NOAA-21 | CARIACICA | ESPÍRITO SANTO | Brasil | 3201308 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| aed6f8b6-1b5c-392e-84f2-e9daef8a873b | -20.37597 | -48.08072 | 2025-05-11 04:04:00 | NOAA-21 | IPUÃ | SÃO PAULO | Brasil | 3521309 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5389f028-5d36-398e-b4bd-2b8d385f4b1b | -13.48138 | -52.98124 | 2025-05-11 04:04:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 8ee27d63-77a7-3ef5-808d-1d86f3fd6486 | -20.19108 | -46.71569 | 2025-05-11 04:04:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 197d4bc3-59d4-3792-a07c-b3d1248ac1ba | -17.78129 | -42.80856 | 2025-05-11 04:04:00 | NOAA-21 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 65ec74ba-fea7-31a7-a0be-361e0cb009ed | -20.16736 | -46.82769 | 2025-05-11 04:04:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 744efe92-e535-3d2f-8aa7-f86e619d7eba | -14.87156 | -51.98348 | 2025-05-11 04:04:00 | NOAA-21 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 2a38f520-ea9e-377b-94af-533866851312 | -13.48925 | -52.97361 | 2025-05-11 04:04:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 5.3 |
| db5e0bf4-39a8-3dfd-9ef4-7f815fc01456 | -13.47527 | -52.97274 | 2025-05-11 04:04:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 8d7ec4a7-7e2d-346b-b0fa-5fa9702e8f51 | -20.31122 | -45.58504 | 2025-05-11 04:04:00 | NOAA-21 | ARCOS | MINAS GERAIS | Brasil | 3104205 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4aa9ab43-f773-35b9-8d88-71b2393ee072 | -13.48039 | -52.97844 | 2025-05-11 04:04:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 8.6 |
| eb7f5a88-9823-370a-94a5-de12a7348d31 | -13.48128 | -52.97401 | 2025-05-11 04:04:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 4f63ad44-9322-3e05-a516-9b9941602dff | -21.65292 | -44.22945 | 2025-05-11 04:04:00 | NOAA-21 | ANDRELÂNDIA | MINAS GERAIS | Brasil | 3102803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 3f30ce88-7821-334c-8b13-23381bd6dd0c | -13.48219 | -52.96954 | 2025-05-11 04:04:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 1d1ed60e-d944-3a85-a999-033b4350a1b4 | -14.66423 | -45.13218 | 2025-05-11 04:04:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 29dbbd84-8651-3b70-868b-7a97e9b98614 | -16.86611 | -41.62886 | 2025-05-11 04:04:00 | NOAA-21 | PONTO DOS VOLANTES | MINAS GERAIS | Brasil | 3152170 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 94b0df68-8350-3bb1-b044-da3a42e53086 | -13.47618 | -52.96825 | 2025-05-11 04:04:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 4c7e380e-3b05-33ff-a097-49c340574489 | -14.2194 | -54.56241 | 2025-05-11 04:04:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c5565a54-3dfa-36ed-932c-711fc613a1c0 | -16.49591 | -43.14197 | 2025-05-11 04:04:00 | NOAA-21 | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| ee8d99a1-e480-3bd0-86c8-e74f39684b89 | -15.56824 | -47.85478 | 2025-05-11 04:04:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 92d0a254-f574-3160-8ccc-f428ddcc3256 | -20.5981 | -47.61921 | 2025-05-11 04:04:00 | NOAA-21 | SÃO JOSÉ DA BELA VISTA | SÃO PAULO | Brasil | 3549508 | 35 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 25161dff-4f97-396e-95ae-5918ce7c9920 | -17.77799 | -42.80799 | 2025-05-11 04:04:00 | NOAA-21 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ed6b1138-6350-326c-ba9c-997703a48f1a | -13.4763 | -52.97554 | 2025-05-11 04:04:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 5.9 |


[Clique aqui para ver as próximas entradas](README3.md)
