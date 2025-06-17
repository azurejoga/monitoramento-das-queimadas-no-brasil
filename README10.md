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

## Dados Diários - Página 10

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c7608242-d1ae-3c8b-8900-b597b691a3cb | -23.33901 | -46.77164 | 2025-06-17 04:12:00 | NOAA-21 | CAIEIRAS | SÃO PAULO | Brasil | 3509007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 65caeded-ea66-33b7-98ae-cfa6d31f273c | -23.59329 | -47.43874 | 2025-06-17 04:12:00 | NOAA-21 | VOTORANTIM | SÃO PAULO | Brasil | 3557006 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 06a4f260-1bff-3f93-83d1-b15b4be4361c | -19.70033 | -47.01716 | 2025-06-17 04:12:00 | NOAA-21 | ARAXÁ | MINAS GERAIS | Brasil | 3104007 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2251000a-dd33-3587-b6af-2a4d364d97fd | -21.62706 | -43.46832 | 2025-06-17 04:12:00 | NOAA-21 | JUIZ DE FORA | MINAS GERAIS | Brasil | 3136702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 6a432070-093b-3e16-8bd3-692cc3f4a6e5 | -20.92263 | -49.09575 | 2025-06-17 04:12:00 | NOAA-21 | TABAPUÃ | SÃO PAULO | Brasil | 3552601 | 35 | 33 | nan | nan | nan | Mata Atlântica | 11.0 |
| 96b7b50c-c4c7-3539-8ab8-b25124ef01d2 | -21.06286 | -47.74215 | 2025-06-17 04:12:00 | NOAA-21 | JARDINÓPOLIS | SÃO PAULO | Brasil | 3525102 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cc6458a1-50b4-311c-9386-088829404da0 | -23.97557 | -48.88983 | 2025-06-17 04:12:00 | NOAA-21 | ITAPEVA | SÃO PAULO | Brasil | 3522406 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bd7b4ad9-1421-371d-b969-e01f99333953 | -18.64539 | -53.31709 | 2025-06-17 04:12:00 | NOAA-21 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d301da1a-401d-3972-9dc4-5b08f16c2e3b | -20.01313 | -44.18016 | 2025-06-17 04:12:00 | NOAA-21 | BETIM | MINAS GERAIS | Brasil | 3106705 | 31 | 33 | nan | nan | nan | Mata Atlântica | 20.5 |
| fa410051-f207-3ab7-a7fd-0be0a9b940ec | -20.2329 | -46.74107 | 2025-06-17 04:12:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 6e143f3a-a5ab-3d2c-a81d-9f38674f9484 | -20.23698 | -46.73762 | 2025-06-17 04:12:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| edc0b0a3-258d-3e12-875c-32c94482a16b | -19.69965 | -47.02113 | 2025-06-17 04:12:00 | NOAA-21 | ARAXÁ | MINAS GERAIS | Brasil | 3104007 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1d6da44b-8542-3dec-8ee8-3948e51619c8 | -19.54624 | -49.67635 | 2025-06-17 04:12:00 | NOAA-21 | CAMPINA VERDE | MINAS GERAIS | Brasil | 3111101 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 2ffd8321-ac2e-315e-9c3e-7b588504d450 | -20.99659 | -51.7942 | 2025-06-17 04:12:00 | NOAA-21 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 9484cf69-a0dc-3a1f-9976-bdc3e25e1058 | -21.56129 | -45.76438 | 2025-06-17 04:12:00 | NOAA-21 | PARAGUAÇU | MINAS GERAIS | Brasil | 3147204 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| d230e967-4305-383f-a5c3-b4ded240b546 | -22.95853 | -43.36037 | 2025-06-17 04:12:00 | NOAA-21 | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| fba974c7-8abf-3e03-8bf6-2dd93d2a7e3c | -20.55684 | -54.12354 | 2025-06-17 04:12:00 | NOAA-21 | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4746274a-cc77-35e0-adce-6d1bab1f9a4b | -20.00982 | -44.17959 | 2025-06-17 04:12:00 | NOAA-21 | BETIM | MINAS GERAIS | Brasil | 3106705 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 0624d9a1-45ea-31c6-8096-c92ef24e38fe | -22.77178 | -49.31333 | 2025-06-17 04:12:00 | NOAA-21 | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 7892161f-a9dd-3947-95a7-43cc64af3a31 | -23.52131 | -46.97602 | 2025-06-17 04:12:00 | NOAA-21 | ITAPEVI | SÃO PAULO | Brasil | 3522505 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| 41cb2318-8137-3a36-bb5a-ebe489829d33 | -19.97636 | -44.85694 | 2025-06-17 04:12:00 | NOAA-21 | SÃO GONÇALO DO PARÁ | MINAS GERAIS | Brasil | 3161809 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4db03ea9-b335-3b11-9039-a202953dbe0f | -20.01556 | -45.76223 | 2025-06-17 04:12:00 | NOAA-21 | IGUATAMA | MINAS GERAIS | Brasil | 3130309 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8eb01684-c09e-3a57-adea-e6a7a0c0db13 | -20.01277 | -45.76223 | 2025-06-17 04:12:00 | NOAA-21 | IGUATAMA | MINAS GERAIS | Brasil | 3130309 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c09ff922-63f3-39d9-9076-c506d2115e68 | -20.3103 | -45.58295 | 2025-06-17 04:12:00 | NOAA-21 | ARCOS | MINAS GERAIS | Brasil | 3104205 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| bbe7d38f-4acd-3b61-bd45-7fabfff06e2b | -23.38395 | -46.41604 | 2025-06-17 04:12:00 | NOAA-21 | GUARULHOS | SÃO PAULO | Brasil | 3518800 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 9cf268d9-b0dd-360e-ae79-3c14de32581a | -22.77095 | -49.31796 | 2025-06-17 04:12:00 | NOAA-21 | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 6.0 |
| b7bbba07-138c-3280-a3cf-98f1fb2d5d5d | -21.13296 | -47.8018 | 2025-06-17 04:12:00 | NOAA-21 | RIBEIRÃO PRETO | SÃO PAULO | Brasil | 3543402 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c7440756-21aa-3462-827b-ba55c6efee1d | -20.55178 | -54.12227 | 2025-06-17 04:12:00 | NOAA-21 | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 828e376e-5ebd-3e32-b43b-1a1cd647aad7 | -21.18113 | -43.97927 | 2025-06-17 04:12:00 | NOAA-21 | BARROSO | MINAS GERAIS | Brasil | 3105905 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 5a842eff-95c2-37de-ad4d-96c99b7ef3a7 | -22.75421 | -43.51589 | 2025-06-17 04:12:00 | NOAA-21 | NOVA IGUAÇU | RIO DE JANEIRO | Brasil | 3303500 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| c5fcb29d-f9a2-33c1-82a1-186dfbcf0376 | -22.54046 | -48.81244 | 2025-06-17 04:12:00 | NOAA-21 | MACATUBA | SÃO PAULO | Brasil | 3528007 | 35 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0de70f0b-76e5-371e-81e8-5d96cda34995 | -19.00707 | -52.08263 | 2025-06-17 04:12:00 | NOAA-21 | CASSILÂNDIA | MATO GROSSO DO SUL | Brasil | 5002902 | 50 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 47813c80-5e84-3438-93bd-182e53116871 | -20.47971 | -53.67693 | 2025-06-17 04:12:00 | NOAA-21 | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 255f77ad-49f0-354b-9ebb-d4a5c5502a1d | -21.97505 | -42.80293 | 2025-06-17 04:12:00 | NOAA-21 | SAPUCAIA | RIO DE JANEIRO | Brasil | 3305406 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 5e583368-0da9-3973-bc18-9d4cf3523085 | -21.42621 | -48.64048 | 2025-06-17 04:12:00 | NOAA-21 | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 63d57c57-c9d0-3eb0-8ad2-712b7d6423ab | -20.92634 | -49.09656 | 2025-06-17 04:12:00 | NOAA-21 | TABAPUÃ | SÃO PAULO | Brasil | 3552601 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 81ba88c0-d6e8-3698-b12b-560df9801f6b | -23.40511 | -46.55665 | 2025-06-17 04:12:00 | NOAA-21 | SÃO PAULO | SÃO PAULO | Brasil | 3550308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 20f768c5-3b35-344a-ab1e-3a22b2a578d0 | -8.07 | -43.1216 | 2025-06-17 04:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 68.6 |
| d2908456-191c-3177-9f94-f02617941fbb | -8.0703 | -43.0981 | 2025-06-17 04:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 72.6 |
| f540fbfb-730f-3be5-ba7f-662b4cc7f97c | -7.1932 | -43.20597 | 2025-06-17 04:34:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 15fed718-0565-3b2d-902c-7dcf0cd92092 | -7.72562 | -55.13993 | 2025-06-17 04:34:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 7ca39252-141e-32bf-8791-2cf0e4eac0b6 | -7.41388 | -49.37172 | 2025-06-17 04:34:00 | NPP-375D | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| aa06bf5f-0e53-3742-88a8-af4a0c9eafca | -7.1387 | -43.18076 | 2025-06-17 04:34:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 93e33f5f-91ef-3600-80f9-47b895c14b2c | -7.1432 | -43.18348 | 2025-06-17 04:34:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 77963839-5222-39c0-acbe-dae88d6729b4 | -8.70409 | -46.96262 | 2025-06-17 04:34:00 | NPP-375D | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8419051d-b053-32fc-8d60-eb6af2fd279c | -6.22108 | -43.33579 | 2025-06-17 04:34:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 671ea499-e47e-34a1-8320-f44cc833e52b | -7.26882 | -44.624 | 2025-06-17 04:34:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1705e75b-da6c-3401-b763-f4fe87350b83 | -6.29356 | -47.00508 | 2025-06-17 04:34:00 | NPP-375D | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| da4cd61f-ae4a-338f-90d6-08e79979d690 | -8.33981 | -48.44695 | 2025-06-17 04:34:00 | NPP-375D | BRASILÂNDIA DO TOCANTINS | TOCANTINS | Brasil | 1703602 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8fe9b1d7-5eed-378d-901c-0ea4dfd9f793 | -6.12669 | -42.52458 | 2025-06-17 04:34:00 | NPP-375D | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 458bada9-868e-3a20-aaf3-fa79a0b14910 | -7.23556 | -43.08608 | 2025-06-17 04:34:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| aa3dbc81-e6af-3657-9ed0-87c02ae2dc0f | -6.29411 | -47.00156 | 2025-06-17 04:34:00 | NPP-375D | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5f666ff2-8f1e-3621-8b5f-713433440978 | -9.41722 | -48.4146 | 2025-06-17 04:34:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 5d91f729-df81-3710-b039-89c36e1083ef | -4.37656 | -48.07166 | 2025-06-17 04:34:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 09fd7c80-423e-3509-ae38-71f59b1d5ee1 | -9.41279 | -48.42107 | 2025-06-17 04:34:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 33f89d5e-4eb6-34a6-920b-8014e8dd84bd | -9.39174 | -48.42488 | 2025-06-17 04:34:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d18e9696-6292-30ec-a597-61c60ece1954 | -8.61063 | -45.02897 | 2025-06-17 04:34:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 73bd3398-58e1-3b6f-8091-5d2ab16a0b88 | -8.33649 | -48.44642 | 2025-06-17 04:34:00 | NPP-375D | BRASILÂNDIA DO TOCANTINS | TOCANTINS | Brasil | 1703602 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 99a76ec7-3f87-3dac-8f3a-a9c413e75074 | -7.14193 | -43.18655 | 2025-06-17 04:34:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 93326191-5e2e-3df4-a5c1-af4c5960b397 | -6.2297 | -44.65739 | 2025-06-17 04:34:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a79dd85c-873c-373a-9a5c-ab28c2c38c37 | -6.84567 | -47.84324 | 2025-06-17 04:34:00 | NPP-375D | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 16f284a8-e16a-3905-b0b8-7fc4a087fd72 | -4.55081 | -48.02031 | 2025-06-17 04:34:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cea353c0-6ef7-3ad6-9e05-6395dff2c307 | -9.40946 | -48.42054 | 2025-06-17 04:34:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7371cfbb-b6c7-3373-8788-17917b860493 | -9.40449 | -48.4305 | 2025-06-17 04:34:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 13747ea0-5af3-306a-b5ce-f04b19891ae9 | -6.03617 | -44.04847 | 2025-06-17 04:34:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 06535bed-8e97-3700-87af-a667bb3de3ec | -7.23382 | -44.75945 | 2025-06-17 04:34:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| de513739-1f00-3a29-87bc-cf7323e9f953 | -6.84289 | -47.83924 | 2025-06-17 04:34:00 | NPP-375D | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| c4ea69d5-bafe-3cb6-9f6a-936aea6e8481 | -9.40281 | -48.41948 | 2025-06-17 04:34:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 3f409a28-80b3-3bb6-a137-bb4905bcaec6 | -7.1872 | -43.60013 | 2025-06-17 04:34:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9ed8eef2-fb1b-3c65-8236-c8883be52bf3 | -7.72092 | -55.13638 | 2025-06-17 04:34:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 742c488a-0038-3fdc-a918-1a6063dd5117 | -6.11843 | -42.52338 | 2025-06-17 04:34:00 | NPP-375D | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 7b281121-413a-3b3b-b52b-314b53ec9ad5 | -8.61125 | -45.0247 | 2025-06-17 04:34:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a4372b47-b5fc-3982-a630-33673614f7b3 | -6.29745 | -47.00209 | 2025-06-17 04:34:00 | NPP-375D | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 64c1c2f3-ffc9-3893-b442-595b492d4d82 | -6.12614 | -42.52822 | 2025-06-17 04:34:00 | NPP-375D | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 6e2506e5-e649-3471-b225-4e2e1a6b6b94 | -6.15488 | -48.06067 | 2025-06-17 04:34:00 | NPP-375D | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 68b6a154-4835-32e3-9e1c-8cb6049fc64e | -7.18275 | -43.60252 | 2025-06-17 04:34:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 107558ae-ed59-3cf0-a36d-2abdb021dc1e | -9.40504 | -48.42701 | 2025-06-17 04:34:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d0daea64-68fd-3ef9-8a5e-449a36c6ffab | -8.22017 | -45.58038 | 2025-06-17 04:34:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cbde917a-593b-39d1-8859-215809ba909b | -6.29301 | -47.00859 | 2025-06-17 04:34:00 | NPP-375D | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2eaffbea-93e4-3cbf-b037-5b80cf20d2c5 | -8.88281 | -48.52315 | 2025-06-17 04:34:00 | NPP-375D | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 56a16ad6-8ec8-3190-86bb-fd957b45f3c3 | -7.54508 | -45.64257 | 2025-06-17 04:34:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 922ee937-388a-34d1-a8ae-e123733eece4 | -8.963 | -47.96974 | 2025-06-17 04:34:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 41ef29db-ba1d-3c0b-8134-9f7a80bf7e8b | -6.84622 | -47.83976 | 2025-06-17 04:34:00 | NPP-375D | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 92b40206-175c-3094-b985-c2d3cfe86cc8 | -8.96633 | -47.97026 | 2025-06-17 04:34:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7d9303aa-5abd-3884-96a5-0ccefa6909bc | -6.28676 | -44.23024 | 2025-06-17 04:34:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e847fdfc-9700-30c6-9c1a-7246173104de | -7.24364 | -43.0873 | 2025-06-17 04:34:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.6 |
| 578dd02a-f643-3a00-a9e5-377feefe2cf1 | -7.25906 | -44.61348 | 2025-06-17 04:34:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| dc88d78d-dd03-31bd-842d-827367e83080 | -7.67551 | -44.57214 | 2025-06-17 04:34:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| cea8f5d9-8c92-3186-98a8-e854642915d0 | -7.25262 | -44.61432 | 2025-06-17 04:34:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 02f8ce3d-1ca3-3eaa-a861-df105eabc91f | -7.83689 | -46.88621 | 2025-06-17 04:34:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 61f56f3a-1479-355f-99e2-e71829e1a674 | -8.60074 | -48.05624 | 2025-06-17 04:34:00 | NPP-375D | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e5d116e8-d556-3284-bf98-402095a994dc | -6.03548 | -44.05301 | 2025-06-17 04:34:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| ee586de1-bf2b-337c-ad8b-5182ba020667 | -9.33226 | -47.83659 | 2025-06-17 04:34:00 | NPP-375D | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 33942790-aa05-3ba8-99e2-9037719a587f | -8.07598 | -43.11106 | 2025-06-17 04:34:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 32.7 |
| e1a5eb37-dfa8-34df-bb1b-5a1cc808a4ac | -8.61555 | -45.02094 | 2025-06-17 04:34:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a7671fa5-3499-3960-9a9c-a51e694ec743 | -3.772 | -41.60604 | 2025-06-17 04:34:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 00b85b78-dc13-3329-9928-6cd0d1c73dfb | -7.23256 | -43.07841 | 2025-06-17 04:34:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 0c81bbbf-469a-3392-a513-5b03d3dd60a8 | -2.45086 | -47.49797 | 2025-06-17 04:34:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 694d0c43-dbe0-3eed-9f0c-abedfeb41b6d | -7.24763 | -44.62233 | 2025-06-17 04:34:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bf9c5764-db2a-3c79-8c7c-05adf15f57f1 | -7.20429 | -45.35069 | 2025-06-17 04:34:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |


[Clique aqui para ver as próximas entradas](README11.md)
