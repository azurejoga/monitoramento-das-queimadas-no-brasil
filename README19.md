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

## Dados Diários - Página 19

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6dfe6369-d6d1-32bc-a391-9d553cc26b2d | -18.96735 | -46.93253 | 2025-08-23 03:42:00 | NPP-375D | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f3f2dab7-3be3-33d6-bb1a-c694fbca65d1 | -20.09707 | -47.7629 | 2025-08-23 03:42:00 | NPP-375D | IGARAPAVA | SÃO PAULO | Brasil | 3520103 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c107de32-b391-352e-9361-61b0c00b2823 | -23.49453 | -45.99815 | 2025-08-23 03:42:00 | NPP-375D | GUARAREMA | SÃO PAULO | Brasil | 3518305 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 7777a818-205b-368e-8e55-01a69b15e6fe | -21.67625 | -49.05975 | 2025-08-23 03:42:00 | NPP-375D | BORBOREMA | SÃO PAULO | Brasil | 3507407 | 35 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 94d5e035-c473-382c-bc8c-1d9dd1d1103e | -23.49766 | -47.62896 | 2025-08-23 03:42:00 | NPP-375D | ARAÇOIABA DA SERRA | SÃO PAULO | Brasil | 3502903 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 5993aa76-351e-3dc3-8a93-0049c96260f7 | -22.90442 | -46.39636 | 2025-08-23 03:42:00 | NPP-375D | VARGEM | SÃO PAULO | Brasil | 3556354 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 8718e8a9-7482-3a0d-a350-362d40e10331 | -20.08458 | -47.76453 | 2025-08-23 03:42:00 | NPP-375D | IGARAPAVA | SÃO PAULO | Brasil | 3520103 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a4a55c44-c442-3b55-888c-0316336e5eb1 | -22.17489 | -43.28611 | 2025-08-23 03:42:00 | NPP-375D | PARAÍBA DO SUL | RIO DE JANEIRO | Brasil | 3303708 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 9b0b5829-69d9-3ffb-958b-1ba315b61dd0 | -22.90014 | -46.39178 | 2025-08-23 03:42:00 | NPP-375D | VARGEM | SÃO PAULO | Brasil | 3556354 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 5215aa9a-8142-312b-883e-113f0566fb42 | -20.28556 | -46.64572 | 2025-08-23 03:42:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f266a2b3-81a8-3ac2-bca8-798916bbb128 | -22.66078 | -46.91418 | 2025-08-23 03:42:00 | NPP-375D | SANTO ANTÔNIO DE POSSE | SÃO PAULO | Brasil | 3548005 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| e1327430-f5f5-31cf-94c5-c351a4639656 | -22.62848 | -47.44308 | 2025-08-23 03:42:00 | NPP-375D | LIMEIRA | SÃO PAULO | Brasil | 3526902 | 35 | 33 | nan | nan | nan | Cerrado | 8.9 |
| a3ef877e-8f49-3414-bed1-ebe742d64d1d | -22.47819 | -44.27375 | 2025-08-23 03:42:00 | NPP-375D | BARRA MANSA | RIO DE JANEIRO | Brasil | 3300407 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 0bdb117b-54c2-36ec-8116-f473854d845d | -20.28372 | -46.65437 | 2025-08-23 03:42:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| dddaf5f3-2d32-3a74-ae06-35d492c76ec4 | -20.35524 | -46.51553 | 2025-08-23 03:42:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 858052e7-a33f-3a70-989d-4d781cc43cbc | -22.17908 | -43.2871 | 2025-08-23 03:42:00 | NPP-375D | PARAÍBA DO SUL | RIO DE JANEIRO | Brasil | 3303708 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 47ec3e8e-f9e8-33b2-ba04-300a906ce062 | -22.47626 | -44.28326 | 2025-08-23 03:42:00 | NPP-375D | BARRA MANSA | RIO DE JANEIRO | Brasil | 3300407 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 2b692df7-2baf-3725-a26b-57b566b28360 | -22.90512 | -46.39311 | 2025-08-23 03:42:00 | NPP-375D | VARGEM | SÃO PAULO | Brasil | 3556354 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| d7b177ff-5651-3626-a600-69a909eb1a16 | -20.33714 | -46.54734 | 2025-08-23 03:42:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b9f53655-1fc4-3a89-bfce-3417aa912899 | -22.92369 | -43.50434 | 2025-08-23 03:42:00 | NPP-375D | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 78ee5382-54c8-3c6e-9cc4-f7b771071b85 | -22.15662 | -44.59766 | 2025-08-23 03:42:00 | NPP-375D | ALAGOA | MINAS GERAIS | Brasil | 3101300 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| ad52250f-f22b-36eb-8522-d044876bd78d | -20.28833 | -46.64164 | 2025-08-23 03:42:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e4a82f87-ac08-30bd-98af-0d551c67ec82 | -22.47181 | -44.28238 | 2025-08-23 03:42:00 | NPP-375D | BARRA MANSA | RIO DE JANEIRO | Brasil | 3300407 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 87750bda-e5af-3e39-8612-6a25208eba7e | -20.28015 | -46.65314 | 2025-08-23 03:42:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a88a5cb6-8f46-3c94-bcb0-4a098fbd3883 | -20.27391 | -46.6813 | 2025-08-23 03:42:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 79168332-af15-3a1f-a1bc-72a68a004d00 | -20.35634 | -46.53614 | 2025-08-23 03:42:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8c1f9dc7-81a2-3e27-87d3-d95b0f99c557 | -22.53481 | -43.72398 | 2025-08-23 03:42:00 | NPP-375D | MENDES | RIO DE JANEIRO | Brasil | 3302809 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| fe6729ea-4f0c-3e0d-8e9e-eaed71775085 | -22.63021 | -47.43543 | 2025-08-23 03:42:00 | NPP-375D | LIMEIRA | SÃO PAULO | Brasil | 3526902 | 35 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 2c7c10ea-a29b-39db-ab99-a1b43666ef2c | -21.67733 | -49.05508 | 2025-08-23 03:42:00 | NPP-375D | BORBOREMA | SÃO PAULO | Brasil | 3507407 | 35 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b53fd831-d3f4-3307-beec-173d904f9dc7 | -22.02834 | -44.09418 | 2025-08-23 03:42:00 | NPP-375D | SANTA RITA DE JACUTINGA | MINAS GERAIS | Brasil | 3159308 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 4de0c4c1-2440-3f24-afd6-15b974c985f5 | -23.49325 | -46.00404 | 2025-08-23 03:42:00 | NPP-375D | GUARAREMA | SÃO PAULO | Brasil | 3518305 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| ec50fd92-f5c9-38c3-91c3-76721191ed41 | -22.5357 | -43.71959 | 2025-08-23 03:42:00 | NPP-375D | MENDES | RIO DE JANEIRO | Brasil | 3302809 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 0389fca6-3b30-31e5-8660-26b090d05e37 | -22.66517 | -46.91909 | 2025-08-23 03:42:00 | NPP-375D | SANTO ANTÔNIO DE POSSE | SÃO PAULO | Brasil | 3548005 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| 4995c71b-22df-321f-a486-231a14bc95cc | -20.27476 | -42.83478 | 2025-08-23 03:42:00 | NPP-375D | SANTA CRUZ DO ESCALVADO | MINAS GERAIS | Brasil | 3157401 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 65786780-be18-3f88-9976-ab5351c00ddb | -20.10089 | -47.77292 | 2025-08-23 03:42:00 | NPP-375D | ARAMINA | SÃO PAULO | Brasil | 3503000 | 35 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2d519aca-71b5-34ab-830b-3b9282cfe13e | -20.44199 | -42.13294 | 2025-08-23 03:42:00 | NPP-375D | SÃO JOÃO DO MANHUAÇU | MINAS GERAIS | Brasil | 3162559 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| 8d96215d-66b7-3c59-a97f-52b039772e34 | -22.3058 | -43.1701 | 2025-08-23 03:42:00 | NPP-375D | AREAL | RIO DE JANEIRO | Brasil | 3300225 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 3222e73d-c127-3a93-8ffd-3777ea225b65 | -22.5305 | -43.72316 | 2025-08-23 03:42:00 | NPP-375D | MENDES | RIO DE JANEIRO | Brasil | 3302809 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| dbfa30ee-d267-31c7-bf87-baba52e3400e | -23.49153 | -47.63113 | 2025-08-23 03:42:00 | NPP-375D | ARAÇOIABA DA SERRA | SÃO PAULO | Brasil | 3502903 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 0d01d728-42d0-3d01-b2aa-c0a4db41fd4a | -20.34893 | -46.51889 | 2025-08-23 03:42:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 01e72027-4572-3e63-84c6-c71ee29a1b19 | -19.77835 | -45.65995 | 2025-08-23 03:42:00 | NPP-375D | LUZ | MINAS GERAIS | Brasil | 3138807 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 2280ecb7-201e-35bb-afeb-f9652c30fcd3 | -23.49844 | -47.62549 | 2025-08-23 03:42:00 | NPP-375D | ARAÇOIABA DA SERRA | SÃO PAULO | Brasil | 3502903 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| fb6f747d-f486-39fe-a33b-128a446baaee | -20.01357 | -46.43318 | 2025-08-23 03:42:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1930ceef-5440-3622-90e5-67f6ebaa2124 | -22.66593 | -46.91565 | 2025-08-23 03:42:00 | NPP-375D | SANTO ANTÔNIO DE POSSE | SÃO PAULO | Brasil | 3548005 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 0e873e31-fb17-393f-b83d-9b8c3427d4b2 | -20.35463 | -46.51836 | 2025-08-23 03:42:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| cea107cf-6389-3406-8a96-e2078b78f86f | -23.49235 | -47.62751 | 2025-08-23 03:42:00 | NPP-375D | ARAÇOIABA DA SERRA | SÃO PAULO | Brasil | 3502903 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| d374d9e6-1a76-3383-abf4-247857d0c6d0 | -20.28367 | -46.63727 | 2025-08-23 03:42:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 963ff24e-9038-37a0-a9a6-64eb97ba531a | -20.44543 | -42.13366 | 2025-08-23 03:42:00 | NPP-375D | SÃO JOÃO DO MANHUAÇU | MINAS GERAIS | Brasil | 3162559 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| d94f2373-75dd-3757-aa74-40e12e4732ad | -18.75697 | -46.68981 | 2025-08-23 03:42:00 | NPP-375D | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b6eabf7f-7162-3732-8543-0bcb24e95904 | -20.47563 | -42.04193 | 2025-08-23 03:42:00 | NPP-375D | LUISBURGO | MINAS GERAIS | Brasil | 3138674 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 106d9e4c-706f-3a27-bec4-a1f689a1a2c7 | -21.96172 | -45.59618 | 2025-08-23 03:42:00 | NPP-375D | SÃO GONÇALO DO SAPUCAÍ | MINAS GERAIS | Brasil | 3162005 | 31 | 33 | nan | nan | nan | Mata Atlântica | 12.3 |
| 6f2b66f8-6635-39ef-9981-f1c963489673 | -22.02996 | -44.09755 | 2025-08-23 03:42:00 | NPP-375D | SANTA RITA DE JACUTINGA | MINAS GERAIS | Brasil | 3159308 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| cd5a7fba-f116-36a9-a350-2e9566f49e66 | -20.28283 | -46.64107 | 2025-08-23 03:42:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 619742fc-c56a-3a59-9d1e-23942946ef9a | -20.27168 | -46.68422 | 2025-08-23 03:42:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7f4c30c5-0f7a-3b8c-a6b0-d265d4849ba5 | -20.30033 | -42.24083 | 2025-08-23 03:42:00 | NPP-375D | MATIPÓ | MINAS GERAIS | Brasil | 3140902 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 132db802-a536-3e7b-9af3-7cb5fdb5eb9b | -20.08774 | -47.75049 | 2025-08-23 03:42:00 | NPP-375D | IGARAPAVA | SÃO PAULO | Brasil | 3520103 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2e5994c1-e861-39d5-b6f4-c23e78058757 | -20.01101 | -46.43526 | 2025-08-23 03:42:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| acde51d5-6f14-3e50-81db-0a168e48e00c | -22.53353 | -43.72477 | 2025-08-23 03:42:00 | NPP-375D | MENDES | RIO DE JANEIRO | Brasil | 3302809 | 33 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| c3bc4fc3-9521-32ce-a151-3e4851355895 | -19.94827 | -47.48458 | 2025-08-23 03:42:00 | NPP-375D | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8fdecac2-e428-3e50-a5b6-415a1cf73206 | -20.44692 | -42.12594 | 2025-08-23 03:42:00 | NPP-375D | LUISBURGO | MINAS GERAIS | Brasil | 3138674 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| 7e79c0b1-462d-3f4c-934c-c8998f34249d | -22.4737 | -44.27304 | 2025-08-23 03:42:00 | NPP-375D | BARRA MANSA | RIO DE JANEIRO | Brasil | 3300407 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 75e4c64d-65fe-3be6-9ea7-b3137e8e5ff2 | -19.77903 | -45.65672 | 2025-08-23 03:42:00 | NPP-375D | LUZ | MINAS GERAIS | Brasil | 3138807 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 6a90f21e-e56d-3072-9b0a-93539c7e6225 | -19.68056 | -43.86916 | 2025-08-23 03:42:00 | NPP-375D | LAGOA SANTA | MINAS GERAIS | Brasil | 3137601 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ea766c10-0184-3b61-94be-130755caf1ba | -22.62812 | -47.44035 | 2025-08-23 03:42:00 | NPP-375D | LIMEIRA | SÃO PAULO | Brasil | 3526902 | 35 | 33 | nan | nan | nan | Cerrado | 6.8 |
| dec5656b-ac4a-37bd-91ef-4f2fd1766809 | -20.28922 | -46.6376 | 2025-08-23 03:42:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| cee90c55-62d8-312d-9da5-a3d81b74c5f6 | -20.3379 | -46.54386 | 2025-08-23 03:42:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 13758ed4-8416-35c5-9555-a65bb1f5391e | -20.22386 | -43.80029 | 2025-08-23 03:42:00 | NPP-375D | ITABIRITO | MINAS GERAIS | Brasil | 3131901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 6a330ab6-403c-3df3-8fd2-68522fe7ff85 | -23.10576 | -46.79939 | 2025-08-23 03:42:00 | NPP-375D | JUNDIAÍ | SÃO PAULO | Brasil | 3525904 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 19cac6bb-ffe2-3787-abf5-f20618f7266c | -22.62935 | -47.43922 | 2025-08-23 03:42:00 | NPP-375D | LIMEIRA | SÃO PAULO | Brasil | 3526902 | 35 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 17b9953a-4641-307c-966a-0dcf3b6653cb | -20.35397 | -46.5214 | 2025-08-23 03:42:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 13ce8c2c-eb38-3f80-aa44-5ad516b3614e | -19.38922 | -41.44362 | 2025-08-23 03:42:00 | NPP-375D | SANTA RITA DO ITUETO | MINAS GERAIS | Brasil | 3159506 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| b0719342-d6a7-354e-8c9c-047f8e8ac499 | -21.9665 | -45.59766 | 2025-08-23 03:42:00 | NPP-375D | SÃO GONÇALO DO SAPUCAÍ | MINAS GERAIS | Brasil | 3162005 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| b90e9cb4-2e85-3ed0-92d9-3e6f8fc6a675 | -23.10503 | -46.80267 | 2025-08-23 03:42:00 | NPP-375D | JUNDIAÍ | SÃO PAULO | Brasil | 3525904 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| bee74547-59b2-358b-853c-50b5404b6109 | -22.12354 | -41.38003 | 2025-08-23 03:42:00 | NPP-375D | QUISSAMÃ | RIO DE JANEIRO | Brasil | 3304151 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 53f0c3d3-02dd-3630-b42b-58bcda90ac8a | -17.59729 | -49.42521 | 2025-08-23 03:42:00 | NPP-375D | PONTALINA | GOIÁS | Brasil | 5217708 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 76a85d83-44fa-3287-9b0e-dbc44477bf78 | -19.38231 | -41.44613 | 2025-08-23 03:42:00 | NPP-375D | SANTA RITA DO ITUETO | MINAS GERAIS | Brasil | 3159506 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.5 |
| 34a33fcf-51c0-3104-815a-4a8931171e41 | -20.27459 | -46.67821 | 2025-08-23 03:42:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e47019fd-21a7-3eb8-bedf-7c2649c00af7 | -20.44404 | -42.12199 | 2025-08-23 03:42:00 | NPP-375D | LUISBURGO | MINAS GERAIS | Brasil | 3138674 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| c0324be6-2fc3-3138-a87d-8a77236214ae | -18.7515 | -46.68824 | 2025-08-23 03:42:00 | NPP-375D | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9b0492cf-a84b-38b1-8f4e-2f515bd9c4df | -22.22354 | -48.36132 | 2025-08-23 03:42:00 | NPP-375D | DOIS CÓRREGOS | SÃO PAULO | Brasil | 3514106 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b0bc23b7-88a8-371e-8931-bf01de6a9ed4 | -19.78411 | -45.65796 | 2025-08-23 03:42:00 | NPP-375D | LUZ | MINAS GERAIS | Brasil | 3138807 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 7540eb67-e0cd-3e2c-99ff-d1793618fcbf | -20.44602 | -42.13383 | 2025-08-23 03:42:00 | NPP-375D | SÃO JOÃO DO MANHUAÇU | MINAS GERAIS | Brasil | 3162559 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 7a12e5ef-8ed6-314a-aee8-b612feb03029 | -20.35717 | -46.53232 | 2025-08-23 03:42:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4c60bbb9-9078-3a03-b1e4-d16b0d165173 | -20.0867 | -47.75513 | 2025-08-23 03:42:00 | NPP-375D | IGARAPAVA | SÃO PAULO | Brasil | 3520103 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9c2be5c4-10b6-3ce1-93a4-1b31818e87ed | -19.38527 | -41.44281 | 2025-08-23 03:42:00 | NPP-375D | SANTA RITA DO ITUETO | MINAS GERAIS | Brasil | 3159506 | 31 | 33 | nan | nan | nan | Mata Atlântica | 14.9 |
| 55cd5141-e13d-3818-b6db-ba591490e030 | -19.43484 | -42.54482 | 2025-08-23 03:42:00 | NPP-375D | SANTANA DO PARAÍSO | MINAS GERAIS | Brasil | 3158953 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 7ac99ca0-92ce-372c-8abc-193745230a19 | -22.02557 | -44.09641 | 2025-08-23 03:42:00 | NPP-375D | SANTA RITA DE JACUTINGA | MINAS GERAIS | Brasil | 3159308 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 4653304d-936c-395b-8bc1-4cc934042ea5 | -20.09243 | -47.75656 | 2025-08-23 03:42:00 | NPP-375D | IGARAPAVA | SÃO PAULO | Brasil | 3520103 | 35 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c6ea2442-5973-35c6-aeef-60f85992fa02 | -23.49684 | -47.63258 | 2025-08-23 03:42:00 | NPP-375D | ARAÇOIABA DA SERRA | SÃO PAULO | Brasil | 3502903 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| e281835a-f790-3fcf-894d-95b3b13fcd37 | -22.64299 | -46.67113 | 2025-08-23 03:42:00 | NPP-375D | MONTE ALEGRE DO SUL | SÃO PAULO | Brasil | 3531209 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 5161887a-43f1-31bd-b431-f932c1c163c0 | -22.62727 | -47.44424 | 2025-08-23 03:42:00 | NPP-375D | LIMEIRA | SÃO PAULO | Brasil | 3526902 | 35 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 452a613f-3a17-3f36-8fcc-b8780301de49 | -22.1891 | -44.55543 | 2025-08-23 03:42:00 | NPP-375D | BOCAINA DE MINAS | MINAS GERAIS | Brasil | 3107208 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| c787a34f-4a85-37df-b098-fe0431d88357 | -20.34823 | -46.52213 | 2025-08-23 03:42:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8520b1df-2a2f-310d-8590-590057ad54bb | -20.00823 | -46.43204 | 2025-08-23 03:42:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 201f88d2-f297-3343-928e-324052520a41 | -20.08858 | -46.11938 | 2025-08-23 03:42:00 | NPP-375D | BAMBUÍ | MINAS GERAIS | Brasil | 3105103 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7a19241e-636b-3245-b005-679ffb93d448 | -23.63177 | -46.44012 | 2025-08-23 03:42:00 | NPP-375D | SÃO PAULO | SÃO PAULO | Brasil | 3550308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 58e6a3f2-bb96-3cc8-b91d-6524e979f041 | -22.53439 | -43.72038 | 2025-08-23 03:42:00 | NPP-375D | MENDES | RIO DE JANEIRO | Brasil | 3302809 | 33 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| 10c01ec2-4141-3d7e-9950-77e5919efa89 | -22.5124 | -47.31697 | 2025-08-23 03:42:00 | NPP-375D | LIMEIRA | SÃO PAULO | Brasil | 3526902 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 98b3368e-5e39-3943-bb81-5b0204d82a1f | -20.39308 | -45.4461 | 2025-08-23 03:42:00 | NPP-375D | FORMIGA | MINAS GERAIS | Brasil | 3126109 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| b9d0352b-c7db-33f0-9a07-e69a04941341 | -20.34754 | -46.5253 | 2025-08-23 03:42:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |


[Clique aqui para ver as próximas entradas](README20.md)
