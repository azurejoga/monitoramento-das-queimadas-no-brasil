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

## Dados Diários - Página 34

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3e555b75-3c09-3014-8921-e6e4d322452d | -11.68392 | -44.43166 | 2025-09-26 04:44:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0d89e00d-8149-3d5b-bfea-8ee9317c1557 | -12.56251 | -45.85141 | 2025-09-26 04:44:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6c277996-2145-3f09-b89b-79f489c297b8 | -11.95589 | -47.87654 | 2025-09-26 04:44:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0bbe1ce9-6bd6-3835-9363-7baa3fdb5776 | -12.7345 | -46.82452 | 2025-09-26 04:44:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fb0a57a1-874e-3bb3-b07b-4e6e3c809a8c | -11.2401 | -45.5612 | 2025-09-26 04:44:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 11.2 |
| bca5b424-aab9-3345-9441-a06a12452d90 | -11.21786 | -45.56838 | 2025-09-26 04:44:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 177d08ab-cc7a-3b31-85a6-5891e3d13b52 | -14.10777 | -51.16875 | 2025-09-26 04:44:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 237aa15a-a6cf-3875-8a29-9de028786676 | -15.37835 | -48.60021 | 2025-09-26 04:44:00 | NPP-375D | COCALZINHO DE GOIÁS | GOIÁS | Brasil | 5205513 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c36f47ba-f01f-378c-865f-0c7aa566ca31 | -14.11936 | -51.20358 | 2025-09-26 04:44:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| af152d3e-231f-30c6-9d81-7dc773c326b0 | -15.90526 | -57.49325 | 2025-09-26 04:44:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9e347803-45f1-31c0-85dd-319402cc220f | -10.81033 | -45.38691 | 2025-09-26 04:44:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| fca24143-5a87-3593-b825-76e3866bd3c7 | -15.90342 | -59.3355 | 2025-09-26 04:44:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| de512f02-55d4-31f3-8bbf-52fe76b8207a | -11.23753 | -45.54993 | 2025-09-26 04:44:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 23.3 |
| d4c23b8a-08d1-34ca-9616-62afb91ee36b | -16.89846 | -47.97045 | 2025-09-26 04:44:00 | NPP-375D | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 529d8db7-2b82-3bc6-a8d9-231fe7741351 | -11.96112 | -47.88013 | 2025-09-26 04:44:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| a39af403-e619-36ad-8d79-78695ceeae00 | -11.222 | -45.57304 | 2025-09-26 04:44:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 10.0 |
| f2508deb-23a7-35f6-8bed-707f4959a31b | -15.90504 | -57.49142 | 2025-09-26 04:44:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 49f6ab34-8304-3e0d-97a3-86d9f92a2418 | -11.78791 | -44.91503 | 2025-09-26 04:44:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 85f56bab-f20a-344a-affd-43a98145d71f | -15.51566 | -50.43555 | 2025-09-26 04:44:00 | NPP-375D | FAINA | GOIÁS | Brasil | 5207535 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 838f3007-5bd2-3e35-806e-80d96d7a4872 | -15.02506 | -46.935 | 2025-09-26 04:44:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0d8e0e1d-e5b5-3e12-9b98-114350f4b502 | -15.12688 | -46.42117 | 2025-09-26 04:44:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| b0a2dc7f-891c-3ab7-b695-ae351199eef1 | -13.69551 | -51.15143 | 2025-09-26 04:44:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6b29bb69-d745-3fbf-a7a1-dec7db589b07 | -11.6078 | -44.4339 | 2025-09-26 04:44:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| badf0caa-1f2d-3733-9a7f-22bff710c3b7 | -11.06681 | -48.36042 | 2025-09-26 04:44:00 | NPP-375D | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b5ecfef6-7123-3584-93d0-270d0a5e3b4f | -14.59589 | -48.25559 | 2025-09-26 04:44:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| e27b4823-858a-3b9c-a739-73c077230a6f | -11.41302 | -43.51186 | 2025-09-26 04:44:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b8d56dcb-c9dc-3248-ba68-552530417992 | -15.36823 | -59.175 | 2025-09-26 04:44:00 | NPP-375D | VALE DE SÃO DOMINGOS | MATO GROSSO | Brasil | 5108352 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 11bb8702-491f-3dcb-9dcb-f05e8e357602 | -15.64032 | -48.84578 | 2025-09-26 04:44:00 | NPP-375D | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 7ffcfe5f-d87a-33f7-ae60-f364a987172f | -13.28045 | -50.69025 | 2025-09-26 04:44:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a992fad2-a804-30a0-839d-31a4ec871279 | -17.02821 | -52.2406 | 2025-09-26 04:44:00 | NPP-375D | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e054605a-68ab-38d6-b71c-68d07f851a2c | -11.01186 | -44.35277 | 2025-09-26 04:44:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 043e2e1e-64f0-3838-a0e7-bb29e31abaf3 | -11.95947 | -47.87711 | 2025-09-26 04:44:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0d678caa-d7e8-34e0-a467-dface481663b | -11.67777 | -44.44381 | 2025-09-26 04:44:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3d0a3a3f-18ea-3978-b987-b20a36244e7d | -11.78309 | -44.91864 | 2025-09-26 04:44:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 39fe3cfb-ff07-316c-9bbf-8d8cd8830cc2 | -11.24157 | -45.55051 | 2025-09-26 04:44:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 23.3 |
| 0efeea60-c019-3e24-9f14-85a1d9e90727 | -11.23655 | -45.55705 | 2025-09-26 04:44:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 84951cf6-6811-3404-9eba-bbe1c1f2d683 | -10.93027 | -44.29539 | 2025-09-26 04:44:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4568ae1b-fbea-3215-85d2-46ba702b0b90 | -15.51678 | -50.42828 | 2025-09-26 04:44:00 | NPP-375D | FAINA | GOIÁS | Brasil | 5207535 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 964ce1fd-a354-3ea1-b540-a93b46ca0e71 | -12.76963 | -47.50842 | 2025-09-26 04:44:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3e95f8a9-f9a5-3a2b-93da-e3cc1d541eea | -14.82487 | -45.40137 | 2025-09-26 04:44:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a7c08b7c-d43c-3b25-88fc-d0908fbf1574 | -12.13431 | -47.95573 | 2025-09-26 04:44:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c7892c2a-b7f8-3395-a36e-8020d37806ef | -12.84945 | -44.6875 | 2025-09-26 04:44:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 042c1744-7092-3e7a-9a17-13d28157dd64 | -13.85008 | -45.6165 | 2025-09-26 04:44:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5ee03acd-82df-3033-9ac8-3b08e40107fd | -16.1316 | -50.76232 | 2025-09-26 04:44:00 | NPP-375D | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a02432fd-8b64-392f-99d3-8ad318bfefc4 | -15.51531 | -45.91987 | 2025-09-26 04:44:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| dd3a0a71-23bc-383d-9dbc-e91a955e0b24 | -14.60075 | -48.2539 | 2025-09-26 04:44:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 31d31d3c-1f75-3e26-91ff-4606b6f05400 | -15.74499 | -59.5125 | 2025-09-26 04:44:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 62b2eca3-c959-3ba0-b88e-b68c714e2725 | -11.68475 | -44.45777 | 2025-09-26 04:44:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| fc58ab3e-c17e-3ad7-99d5-735729398422 | -11.62472 | -44.44065 | 2025-09-26 04:44:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 499d2a9e-25c8-35f3-841b-e5cf6d2ade93 | -11.21687 | -45.57523 | 2025-09-26 04:44:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| b1f31caa-2135-35f1-b727-2c21a8eae9a3 | -12.86871 | -44.68038 | 2025-09-26 04:44:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f57844fd-e863-3c14-8068-07797ecaeafd | -12.87576 | -44.69448 | 2025-09-26 04:44:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 9a63b9aa-941e-30ec-9aa0-3ab629578dbd | -10.31672 | -48.18447 | 2025-09-26 04:44:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 015356b0-55d6-38c6-a7b5-14e332ce8c0e | -10.54909 | -47.51671 | 2025-09-26 04:44:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 913a5413-c5d8-3adc-a649-e13d33f63cd1 | -11.2471 | -45.5404 | 2025-09-26 04:44:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 12.2 |
| d54caf95-f4d9-38ef-8d5f-9804c5ba7b78 | -13.24684 | -50.69248 | 2025-09-26 04:44:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e3cf1ab7-c17d-38c4-9796-e19b349fbeeb | -16.89837 | -47.97258 | 2025-09-26 04:44:00 | NPP-375D | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 11bf5b6d-3855-3721-b6f7-5d79252b812a | -12.13135 | -47.9511 | 2025-09-26 04:44:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9acc913c-1860-30cf-a0a0-759be85e473c | -11.67836 | -44.43956 | 2025-09-26 04:44:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ceb13935-6f3c-34e1-b4a1-abbdb22292ee | -14.03843 | -45.49208 | 2025-09-26 04:44:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| e3ee5243-67c3-3157-8ab9-385ec15124ef | -15.94037 | -59.49586 | 2025-09-26 04:44:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 30f376ad-b67e-37b7-ace5-de4570445d9c | -11.65381 | -46.85112 | 2025-09-26 04:44:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1a65088e-4503-30ec-bbf1-a40291e30a17 | -15.26777 | -46.4175 | 2025-09-26 04:44:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4ca4a917-c72e-3a66-998e-c7b96ec6e33f | -15.91682 | -57.49817 | 2025-09-26 04:44:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| cb353563-993f-3015-bb23-2cbdd4629a75 | -14.10556 | -51.16108 | 2025-09-26 04:44:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 81d877fa-34c8-3bde-8e0a-9ce3b89e8d2f | -12.84156 | -44.71246 | 2025-09-26 04:44:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c104b121-6f9d-332d-ad39-cd25f1e82ca6 | -15.33532 | -47.99214 | 2025-09-26 04:44:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 20a83e0d-672b-3647-a2dd-5b10b13194f3 | -15.25162 | -46.44534 | 2025-09-26 04:44:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4b02272c-4e06-3451-939e-93900c200f32 | -11.42208 | -44.9834 | 2025-09-26 04:44:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 5a5ad9ab-5b7d-307e-85d7-a0aeef954cb3 | -11.24462 | -45.55823 | 2025-09-26 04:44:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 0dc0bb96-ef74-3e55-af27-51207959c9d2 | -11.61597 | -44.4394 | 2025-09-26 04:44:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 30.1 |
| 7e040fd1-bbc0-34f9-a534-301585d95506 | -13.84225 | -45.61146 | 2025-09-26 04:44:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| dbceca84-6839-3b00-80a9-999bcb3afe39 | -15.9759 | -59.49195 | 2025-09-26 04:44:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8e582717-6410-34a4-aa92-2cdcc931655a | -13.8506 | -45.61263 | 2025-09-26 04:44:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| cf1bde56-fb44-364e-b8a6-697f57325213 | -10.48554 | -48.03977 | 2025-09-26 04:44:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8457657e-1b07-306f-ae2f-d24f3c1789fb | -15.27069 | -46.4262 | 2025-09-26 04:44:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 514a2775-1be7-343c-99da-bb1307639b7d | -12.56301 | -45.84783 | 2025-09-26 04:44:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 459f0783-7f79-3b53-90d1-b423358240d1 | -12.34079 | -47.99268 | 2025-09-26 04:44:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 57b29ce1-a4cd-39d0-b1a4-b7d17df5a2b3 | -14.57361 | -51.40595 | 2025-09-26 04:44:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 315389f7-ecb9-317d-a40e-2273d88cb7c8 | -15.99514 | -59.49504 | 2025-09-26 04:44:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| acc675a8-efc4-31ee-89ad-dc968bad63d9 | -11.05683 | -45.90196 | 2025-09-26 04:44:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1eb54020-e6e3-3a23-8bf3-e1d817307ccb | -15.38236 | -46.11329 | 2025-09-26 04:44:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c17cd30d-b01a-3a9f-aa69-4ae4bce709a8 | -11.42685 | -44.97976 | 2025-09-26 04:44:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4dbfbff8-a071-3bcd-b7eb-0132dce7023e | -11.65327 | -44.42732 | 2025-09-26 04:44:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| eaf1f83b-ef3b-3b2f-a7ab-09a5ff1ce4f7 | -15.92603 | -57.49546 | 2025-09-26 04:44:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 81ec13fb-d0af-38ef-9859-b7ecdf058e66 | -10.79106 | -45.37687 | 2025-09-26 04:44:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f63a5c06-b8d7-3163-a2f8-3b3ef547ce2b | -15.51229 | -50.43502 | 2025-09-26 04:44:00 | NPP-375D | FAINA | GOIÁS | Brasil | 5207535 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 1ba6ecfd-b505-30d1-87bf-1f59eba7bc5b | -15.36934 | -59.16873 | 2025-09-26 04:44:00 | NPP-375D | VALE DE SÃO DOMINGOS | MATO GROSSO | Brasil | 5108352 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 04668488-b592-34b6-b19d-3558e52b06bb | -12.17918 | -47.91168 | 2025-09-26 04:44:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ccbedb06-b4bb-30a4-9e8e-a577ffe74579 | -15.51396 | -50.4241 | 2025-09-26 04:44:00 | NPP-375D | FAINA | GOIÁS | Brasil | 5207535 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e009884c-7a69-35a4-b0b5-dbce1186cedf | -11.21069 | -47.8338 | 2025-09-26 04:44:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 4bf7c8b6-d083-3192-b943-a77ac36aceaf | -11.70062 | -44.4079 | 2025-09-26 04:44:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f0c0dba1-8201-3831-a67c-d2333dd5914d | -11.6661 | -44.4638 | 2025-09-26 04:44:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b8d67a7d-97f3-31cd-8e0b-adab21d05183 | -14.11001 | -51.1545 | 2025-09-26 04:44:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| eabd72cf-0973-384f-a074-80319be04b4e | -14.75987 | -48.35986 | 2025-09-26 04:44:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| dc6b8136-7216-3298-80cb-37e1037cb290 | -16.22157 | -48.80916 | 2025-09-26 04:44:00 | NPP-375D | ABADIÂNIA | GOIÁS | Brasil | 5200100 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| bb45511e-4c2c-3650-ab0c-598461e453bc | -15.52071 | -50.42514 | 2025-09-26 04:44:00 | NPP-375D | FAINA | GOIÁS | Brasil | 5207535 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 74aca716-a6bd-31a7-8583-ec49fb689c6d | -15.97708 | -59.48598 | 2025-09-26 04:44:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8ce12520-4dc2-3752-b882-d6fae7ffe48a | -15.74575 | -59.51748 | 2025-09-26 04:44:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| ae0cf9a8-38d3-335c-b48a-cdd98642144c | -13.8459 | -45.61592 | 2025-09-26 04:44:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |


[Clique aqui para ver as próximas entradas](README35.md)
