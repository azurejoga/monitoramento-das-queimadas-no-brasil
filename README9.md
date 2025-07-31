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

## Dados Diários - Página 9

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| aa1d0f7e-684b-3a69-81ee-5d97fa792d12 | -6.526 | -56.1923 | 2025-07-31 04:00:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 45.6 |
| 04b74d5c-807f-31e8-87c3-9d449b03e7d3 | -8.0513 | -43.1001 | 2025-07-31 04:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 83.7 |
| 45025918-afe4-3fcb-8aed-e6487c07858a | -6.6725 | -56.4029 | 2025-07-31 04:00:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 63.3 |
| e442db14-4c58-3093-b9a8-6b1d8026d8f8 | -5.00442 | -47.80905 | 2025-07-31 04:08:00 | NPP-375D | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a22ed899-6efd-33cb-bdbf-0b628668a273 | -5.00365 | -47.81355 | 2025-07-31 04:08:00 | NPP-375D | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ef03be3c-7167-3d02-8c52-212c96a858c4 | -4.19453 | -38.36353 | 2025-07-31 04:08:00 | NPP-375D | CASCAVEL | CEARÁ | Brasil | 2303501 | 23 | 33 | nan | nan | nan | Caatinga | 5.3 |
| 61562cf2-3870-3bcb-a1b3-916fd8da5e50 | -3.55549 | -39.97592 | 2025-07-31 04:08:00 | NPP-375D | MIRAÍMA | CEARÁ | Brasil | 2308377 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 0a98db87-b501-367b-88e9-8ca0a11219d2 | -3.99539 | -38.98947 | 2025-07-31 04:08:00 | NPP-375D | MARANGUAPE | CEARÁ | Brasil | 2307700 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 33c05a0c-ef3f-3d5d-9367-52b23047519e | -6.23301 | -37.42792 | 2025-07-31 04:08:00 | NPP-375D | SÃO JOSÉ DO BREJO DO CRUZ | PARAÍBA | Brasil | 2514651 | 25 | 33 | nan | nan | nan | Caatinga | 2.5 |
| fbbce94e-8c15-3b74-a7f4-ae9e81b4de8d | -6.5258 | -56.2121 | 2025-07-31 04:10:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 44.4 |
| 25f46da9-e3b8-34df-843d-ccea0fca0124 | -6.6725 | -56.4029 | 2025-07-31 04:10:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 58.0 |
| acf0d971-90af-3d96-bd6b-6253d529c23a | -6.526 | -56.1923 | 2025-07-31 04:10:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 47.7 |
| 5921eca5-7227-3e17-88e8-83575658160a | -10.5203 | -42.55019 | 2025-07-31 04:10:00 | NPP-375D | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 2.6 |
| f350fdfb-fa42-3b6d-8589-24f212b9a7c0 | -11.53129 | -44.25632 | 2025-07-31 04:10:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b4ff8200-2721-3952-b7f0-675d5d71cda8 | -6.37659 | -53.32804 | 2025-07-31 04:10:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| fb884703-6e54-3e84-a928-335bdb430205 | -8.37683 | -44.03112 | 2025-07-31 04:10:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e11efcb6-18e0-3f54-a4b9-1c99525cacfd | -9.64007 | -43.84906 | 2025-07-31 04:10:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| cc19cfd6-2c68-3eb9-8f0c-a57c04695436 | -9.56765 | -43.88706 | 2025-07-31 04:10:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| ebf233b8-b18c-3aa3-892b-de2b3806159f | -11.99123 | -46.68165 | 2025-07-31 04:10:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ad420a9e-bd6c-3e86-a4b9-8397b18b6130 | -10.95918 | -48.153 | 2025-07-31 04:10:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 42b1928c-f5c3-3534-992b-d1ee2778c37d | -8.4448 | -45.14727 | 2025-07-31 04:10:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 94f2ef26-4544-3812-9045-41c7969ce357 | -12.61215 | -48.09544 | 2025-07-31 04:10:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c95c0b4b-1c06-3d19-97b7-ffe8cce63e3a | -12.81707 | -43.08923 | 2025-07-31 04:10:00 | NPP-375D | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 2d0d0094-4bc5-34c6-909e-12c92c658d6c | -11.92049 | -44.54634 | 2025-07-31 04:10:00 | NPP-375D | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1d1298a1-081f-32a1-b756-e3224dc93725 | -11.02413 | -43.23901 | 2025-07-31 04:10:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| eb15deea-2787-32af-ae53-a8ce298ff41b | -7.31581 | -44.67619 | 2025-07-31 04:10:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2358bd48-cf5c-3e2e-b333-4823929d8818 | -12.58562 | -48.08417 | 2025-07-31 04:10:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1eea8977-ee17-3379-b969-14766b83826c | -10.21336 | -47.98645 | 2025-07-31 04:10:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1cfea19c-a42f-3e9d-a801-5dcc1d27baf5 | -8.59918 | -45.5158 | 2025-07-31 04:10:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| cfcf719b-95c4-3a5a-9c7b-0d854d4bf37a | -12.58499 | -48.08779 | 2025-07-31 04:10:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| eaa340a2-0f9e-353f-a78d-d197b7c3b439 | -8.17501 | -45.01583 | 2025-07-31 04:10:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 088382a0-d650-3451-b0df-b8040dcd6906 | -7.88062 | -45.54955 | 2025-07-31 04:10:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 70289cf4-7a7f-39cb-9eb3-41878297de17 | -10.08524 | -53.86825 | 2025-07-31 04:10:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 3c71b5d3-7f75-3a7e-a8a5-9e81d17f3b17 | -10.93522 | -44.50565 | 2025-07-31 04:10:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8bbaf004-d59a-33a9-82e0-7cc87b65c66a | -13.5151 | -45.64113 | 2025-07-31 04:10:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 6f67d41f-4cf9-3d51-ac59-f805302962db | -12.58435 | -48.09148 | 2025-07-31 04:10:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f1983f41-9d57-3502-8083-65f816602b16 | -8.88068 | -44.79263 | 2025-07-31 04:10:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 2601c506-d074-3339-b8ac-dd55ba71de7c | -7.87837 | -45.54007 | 2025-07-31 04:10:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c6e787e0-68e4-38ef-b740-4b1962d23fd0 | -11.54464 | -44.2814 | 2025-07-31 04:10:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| f773fd6d-096e-3296-b1af-34b0bbfeefd5 | -10.63883 | -45.23403 | 2025-07-31 04:10:00 | NPP-375D | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| a24ef7a0-50d8-3a00-9de7-cfbbd57750cd | -12.76384 | -44.41457 | 2025-07-31 04:10:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 23.1 |
| 4dfb3ad4-4fb6-39fe-8efd-0a483a58cc25 | -12.58971 | -48.08476 | 2025-07-31 04:10:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ef0d7d12-fdfd-3253-ac52-c03bd2af842a | -7.54263 | -44.41077 | 2025-07-31 04:10:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f62c8870-347e-363c-801c-2c90a7c5f020 | -10.95875 | -48.15267 | 2025-07-31 04:10:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f9ea0b84-9ef1-325d-a7c5-c08a7b40de7f | -9.22821 | -48.59874 | 2025-07-31 04:10:00 | NPP-375D | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1fe30739-1301-3b24-b31f-c32cb931facd | -9.56886 | -43.87963 | 2025-07-31 04:10:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 3c299fb1-e103-3c02-b6c8-08dcd1331952 | -13.5454 | -44.1431 | 2025-07-31 04:10:00 | NPP-375D | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4750213b-f22a-3a6a-9ebf-508c01f9c432 | -11.92329 | -44.55067 | 2025-07-31 04:10:00 | NPP-375D | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a96dc03f-0270-391e-9ccf-d4cac896ddf6 | -7.58396 | -44.81789 | 2025-07-31 04:10:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| c567f1ae-b683-33e5-aed1-a0baef4377ad | -10.53025 | -42.5518 | 2025-07-31 04:10:00 | NPP-375D | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 5.0 |
| 0d72007c-0979-38a1-874b-ee9f3cc9aba3 | -7.57967 | -44.82145 | 2025-07-31 04:10:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 4345267d-46c4-38da-ace2-5e62d7aa1355 | -11.92111 | -44.54258 | 2025-07-31 04:10:00 | NPP-375D | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 31102be5-02b2-30dc-8ff8-a7f2736290e0 | -12.55202 | -44.72392 | 2025-07-31 04:10:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ad4b06ed-0cc9-3c17-876a-693bd47cbb22 | -7.64106 | -49.79993 | 2025-07-31 04:10:00 | NPP-375D | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 14373688-3301-3c6a-9b0d-d380f774aec5 | -8.29226 | -47.3543 | 2025-07-31 04:10:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 3fdf0aab-ddcd-325d-bf69-8995055b2fe3 | -12.76106 | -44.4103 | 2025-07-31 04:10:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 13.8 |
| cf09e970-eb6f-3b40-bdac-cb6c4496ad03 | -8.59473 | -45.51963 | 2025-07-31 04:10:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| af2eaa4d-bffd-3992-bfbe-5cbbfc9c8e9f | -13.50742 | -45.64383 | 2025-07-31 04:10:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f8b04de7-11ff-3399-a5e6-4651d39841e5 | -7.12636 | -44.89857 | 2025-07-31 04:10:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 8edf8e5a-1c48-3194-8a1b-23bcdce29377 | -10.52362 | -42.55072 | 2025-07-31 04:10:00 | NPP-375D | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 2f9a148e-52ea-3136-8bd6-5e9c019b28d0 | -9.63946 | -43.85277 | 2025-07-31 04:10:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| e643d8e5-321e-3df7-b4d8-ee90c32351f8 | -11.54124 | -44.28083 | 2025-07-31 04:10:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 340381bc-3af8-38fb-a39f-3bf2470b18f1 | -10.31198 | -54.15601 | 2025-07-31 04:10:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 00fe9d7f-57bc-392d-a413-a138e41904b2 | -8.17069 | -45.01945 | 2025-07-31 04:10:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| dccbdeeb-4e3d-3d91-b516-b5706d25846a | -9.39574 | -45.49089 | 2025-07-31 04:10:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 412ece4b-da20-3995-8768-c17eb63aaee8 | -12.63379 | -48.09159 | 2025-07-31 04:10:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bf594c77-ded6-35e2-a794-1be5018d81a6 | -12.74063 | -47.00669 | 2025-07-31 04:10:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 29b32dc8-98bd-32b8-a16b-fd80ddf980c8 | -8.58785 | -45.52493 | 2025-07-31 04:10:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| eadf8b80-3806-349e-a402-5632620b6402 | -9.59532 | -43.84586 | 2025-07-31 04:10:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| e9c0b079-8388-32f9-b3e0-53ff55b78722 | -8.95878 | -46.73742 | 2025-07-31 04:10:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 658e50c8-269a-3544-81ad-aa2a7685fc42 | -9.57106 | -43.88762 | 2025-07-31 04:10:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| b509c560-12a1-3fdb-8ed2-8ac592f3bf01 | -12.48726 | -44.75972 | 2025-07-31 04:10:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a57c6776-932b-3280-ae75-a1e722679ca1 | -7.74312 | -51.09378 | 2025-07-31 04:10:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| ecf749e4-257e-38ff-9e9e-b1a07b0649e2 | -9.63391 | -43.84479 | 2025-07-31 04:10:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| e47fd1b5-83b3-35cc-987c-de6893fc3365 | -8.16415 | -45.01407 | 2025-07-31 04:10:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 806a165e-0417-39a6-8210-bb008a47bb61 | -10.61983 | -45.26009 | 2025-07-31 04:10:00 | NPP-375D | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1e0be07f-ab81-3b10-8245-8aef930041d7 | -10.21135 | -48.21552 | 2025-07-31 04:10:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6732a558-956b-36cb-acf9-933745d5e706 | -8.95704 | -46.7475 | 2025-07-31 04:10:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 999eda40-d2ae-3227-bbd2-882e848db122 | -6.3902 | -53.32523 | 2025-07-31 04:10:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| aa006e91-2487-372d-adaa-2141afb4c7ad | -9.57387 | -43.89185 | 2025-07-31 04:10:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| bcf5703d-5807-3293-9485-6fd54bc62506 | -10.61902 | -45.24317 | 2025-07-31 04:10:00 | NPP-375D | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 0005c329-fe3a-3535-91a3-e36bb6ff6cd4 | -9.63212 | -43.85593 | 2025-07-31 04:10:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| bba6928a-a0cb-3f7e-8434-e4fd36b89a2b | -10.60847 | -45.26237 | 2025-07-31 04:10:00 | NPP-375D | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6bba5f48-d2b9-325c-9c77-49202d52f51c | -11.99176 | -46.70091 | 2025-07-31 04:10:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b75a26c8-dc09-3b27-b0fe-3672c7a41bcb | -6.41786 | -53.36424 | 2025-07-31 04:10:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| a45e8dd1-7f67-3fbf-bf53-8685dcc2f242 | -10.31825 | -54.15718 | 2025-07-31 04:10:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| fd01c007-5309-3d3a-9951-efd63c45f36f | -10.62258 | -45.24377 | 2025-07-31 04:10:00 | NPP-375D | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 80f849b6-b568-38fe-8166-8c5298a6373f | -12.62498 | -48.09401 | 2025-07-31 04:10:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c3419ce4-351b-362e-ae08-d5e07651ba9e | -7.58892 | -44.81023 | 2025-07-31 04:10:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 4cbe7a16-3e74-3544-83ed-ffee05e75dd5 | -10.95848 | -48.15683 | 2025-07-31 04:10:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ebe36f58-6750-3886-adf9-7ac7f802d210 | -7.32362 | -44.67358 | 2025-07-31 04:10:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| b279e341-4635-3a85-96f3-70d5fc8a9ce1 | -12.48944 | -44.76787 | 2025-07-31 04:10:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 2fcbf156-b443-3dac-b0cb-16d0108bee23 | -9.57227 | -43.88018 | 2025-07-31 04:10:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 5546204a-d5be-3432-aa85-fa6737c6a715 | -6.4169 | -53.36947 | 2025-07-31 04:10:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 20609ebe-892e-3e78-98b9-61af3a6ce26d | -10.23203 | -56.76923 | 2025-07-31 04:10:00 | NPP-375D | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c55f88b6-e8b4-313f-a0c6-fb1949608ea3 | -8.1721 | -45.01104 | 2025-07-31 04:10:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b78d5fcc-36c4-3f61-a7a3-4e435ce68c2a | -7.3441 | -44.64571 | 2025-07-31 04:10:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a7485266-4a37-36af-a69b-c1a34b3a1aef | -10.05116 | -46.54072 | 2025-07-31 04:10:00 | NPP-375D | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 29c865d9-d776-3f23-a611-13075a8e5d23 | -6.90338 | -52.87287 | 2025-07-31 04:10:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4d4cc412-d976-3538-9895-251c4e4588fc | -12.74151 | -47.00161 | 2025-07-31 04:10:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |


[Clique aqui para ver as próximas entradas](README10.md)
