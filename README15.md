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

## Dados Diários - Página 15

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 03ca5190-5ae8-36de-ae0b-72d77d199aa8 | -10.9737 | -44.52995 | 2024-11-19 03:29:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 03874098-7e24-32f5-b2f2-d450a6f012d1 | -9.24523 | -44.99824 | 2024-11-19 03:29:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 0941b5cb-8405-3aa1-8ac2-275b980d4d4d | -10.22942 | -36.3099 | 2024-11-19 03:29:00 | NPP-375D | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| f3c1e1ce-d3f7-391d-9d54-408d99e8fa87 | -9.25176 | -44.99956 | 2024-11-19 03:29:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 4.9 |
| daa704c6-fc09-3464-8ca8-28ef342bbb89 | -10.97597 | -44.44733 | 2024-11-19 03:29:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 34d88e73-023b-3c70-9524-ff5539acfb8a | -8.26521 | -44.03851 | 2024-11-19 03:29:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| dd02b4be-6556-3142-b9cb-3d50a29b876d | -10.40225 | -44.48319 | 2024-11-19 03:29:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9567e5a3-679e-3c05-89a2-9fa98faa7193 | -10.17802 | -36.35791 | 2024-11-19 03:29:00 | NPP-375D | PENEDO | ALAGOAS | Brasil | 2706703 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 5a425af2-e5c9-3db4-a5ad-432f57bcb346 | -10.69585 | -37.05083 | 2024-11-19 03:29:00 | NPP-375D | ROSÁRIO DO CATETE | SERGIPE | Brasil | 2806107 | 28 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| cd3aecb0-5fb1-30c0-8485-aa1939484ae2 | -12.27288 | -43.52658 | 2024-11-19 03:29:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ae86e017-3bb9-3982-a596-2277fec4184e | -8.26275 | -44.03468 | 2024-11-19 03:29:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 25356d49-e1c4-3ccc-935f-0fbd5aca26da | -10.14035 | -38.52 | 2024-11-19 03:29:00 | NPP-375D | JEREMOABO | BAHIA | Brasil | 2918100 | 29 | 33 | nan | nan | nan | Caatinga | 4.5 |
| c2fbab37-ca7e-3281-84bf-9d9f63ac65a0 | -12.27932 | -43.52385 | 2024-11-19 03:29:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 946e201a-6807-358d-b39f-0a43234f5c32 | -12.27366 | -43.52263 | 2024-11-19 03:29:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f9910e05-d22e-3336-981b-e51f91b6e231 | -11.87967 | -47.47122 | 2024-11-19 03:29:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 7.2 |
| d85c1c71-37bc-37f0-9ef2-9f5aac2d9f98 | -13.0085 | -40.18205 | 2024-11-19 03:29:00 | NPP-375D | IAÇU | BAHIA | Brasil | 2911907 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| f1c7091b-ec77-3cab-a45f-37dad7114ebb | -8.28119 | -44.02238 | 2024-11-19 03:29:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 09c0e1cd-66aa-3eea-afcf-fb61996ad950 | -10.13608 | -38.52385 | 2024-11-19 03:29:00 | NPP-375D | JEREMOABO | BAHIA | Brasil | 2918100 | 29 | 33 | nan | nan | nan | Caatinga | 6.4 |
| 37856486-7687-322d-9190-cd7313c49dd9 | -8.27889 | -44.01841 | 2024-11-19 03:29:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 46b7d472-8dd9-3e89-9767-30e46bfa0992 | -10.42183 | -44.48206 | 2024-11-19 03:29:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 6ce56eec-e58e-3ddf-8926-e18184a5d5a5 | -11.24584 | -44.65252 | 2024-11-19 03:29:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 34034cdf-3033-3b73-b88d-7d2c9c0e4263 | -11.87205 | -38.34821 | 2024-11-19 03:29:00 | NPP-375D | INHAMBUPE | BAHIA | Brasil | 2913705 | 29 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 1b9d3dc1-0bb6-3ac7-9550-a8eab45597bc | -9.439 | -40.40726 | 2024-11-19 03:29:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 2.5 |
| fbd8b290-019f-3c94-9968-cfcd9711affa | -9.26125 | -45.01036 | 2024-11-19 03:29:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 82d06536-5660-38bf-9be9-d958c59cad15 | -8.86876 | -40.78211 | 2024-11-19 03:29:00 | NPP-375D | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 084fdb72-03db-30f1-aae8-b1fccf02f4a2 | -10.82216 | -44.36586 | 2024-11-19 03:29:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 36a6d8f4-1ace-33f3-b5e3-11103c2a6e82 | -9.25043 | -44.99655 | 2024-11-19 03:29:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 2b47e887-bf92-33ec-9d2e-922a619d71cd | -9.25068 | -45.00515 | 2024-11-19 03:29:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 2b63ccc2-f9f7-394d-89be-c98ef7e2ba64 | -9.26373 | -45.00784 | 2024-11-19 03:29:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f1998b22-13db-3db6-8167-8a39ea2d2e5f | -8.26179 | -44.03964 | 2024-11-19 03:29:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6d85828a-9e3f-31bc-ac55-1a1e857fb134 | -8.25939 | -44.01851 | 2024-11-19 03:29:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3800d2ac-4d11-3d95-8cac-900efee7dcbe | -9.25829 | -45.0009 | 2024-11-19 03:29:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 3b7b74b7-8c64-3b62-a228-2296016298a2 | -10.14029 | -38.52478 | 2024-11-19 03:29:00 | NPP-375D | JEREMOABO | BAHIA | Brasil | 2918100 | 29 | 33 | nan | nan | nan | Caatinga | 6.4 |
| bcb72ea4-3aee-3a3e-83ae-4bfeb87ea5ad | -10.82124 | -44.37049 | 2024-11-19 03:29:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 385ec751-d6f6-3038-84ed-716bdead3c30 | -9.25583 | -45.00346 | 2024-11-19 03:29:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 9315e520-d107-3201-86d8-b91090afc07a | -10.97795 | -44.53292 | 2024-11-19 03:29:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| a033fd69-adf6-3f1f-a694-8812be43d633 | -23.9706 | -54.1372 | 2024-11-19 03:30:00 | GOES-16 | MUNDO NOVO | MATO GROSSO DO SUL | Brasil | 5005681 | 50 | 33 | nan | nan | nan | Mata Atlântica | 109.0 |
| 6bec4564-d2c3-37ff-8d7c-f0f23fbecb8b | -23.9917 | -54.1329 | 2024-11-19 03:30:00 | GOES-16 | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 67.8 |
| b3a4d5b1-8812-3ad5-8746-5930cd6f1290 | -23.9711 | -54.1148 | 2024-11-19 03:30:00 | GOES-16 | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 107.0 |
| 20f15a41-f11f-3e3b-9bd0-68cb31936ea7 | -8.2659 | -44.0348 | 2024-11-19 03:30:00 | GOES-16 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 123.4 |
| 391994cf-e123-3c8b-9d76-a61ad8661b4d | -13.2643 | -56.7947 | 2024-11-19 03:30:00 | GOES-16 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 56.4 |
| 61c27538-d29f-3278-8532-10552979d438 | -23.9494 | -54.1415 | 2024-11-19 03:30:00 | GOES-16 | MUNDO NOVO | MATO GROSSO DO SUL | Brasil | 5005681 | 50 | 33 | nan | nan | nan | Mata Atlântica | 65.6 |
| 98a25776-a7c8-369f-a4ed-f3f85128170f | -4.5429 | -48.0151 | 2024-11-19 03:30:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 90.5 |
| 857faed2-ed11-3a5d-a12e-354b88bb4288 | -4.5614 | -48.0141 | 2024-11-19 03:30:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 141.7 |
| bd29ccb5-0b5b-3864-8b6a-b63b13071964 | -2.4293 | -54.6216 | 2024-11-19 03:30:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 39.3 |
| f1bf2a86-24cc-38c4-ab7b-3dd39773467a | -4.1246 | -43.5833 | 2024-11-19 03:30:00 | GOES-16 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 70.9 |
| 7dba0a33-0d3f-36bf-acd2-1f00ee9ba5a3 | -1.5869 | -53.8134 | 2024-11-19 03:30:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 120.4 |
| 7411a143-bd7c-304f-8389-238d71812186 | -4.58 | -48.0132 | 2024-11-19 03:30:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 48.8 |
| 125c917f-15a6-3e69-af07-23440d6f2260 | -4.5616 | -47.9925 | 2024-11-19 03:30:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 48.2 |
| aa935b9b-bf62-3217-b6eb-933a3a5bee8e | -13.264 | -56.8149 | 2024-11-19 03:30:00 | GOES-16 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 89.2 |
| caf4d2c0-1dcc-3033-bfff-640a5bef1a01 | -23.95 | -54.1191 | 2024-11-19 03:30:00 | GOES-16 | MUNDO NOVO | MATO GROSSO DO SUL | Brasil | 5005681 | 50 | 33 | nan | nan | nan | Mata Atlântica | 104.6 |
| 24a5c97e-542b-3cef-88bf-c7f4b4ef8ebf | -10.9717 | -44.5342 | 2024-11-19 03:30:00 | GOES-16 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 75.4 |
| f92b7792-76f3-3fac-a753-b46d6748ec2a | -5.9788 | -45.3621 | 2024-11-19 03:30:00 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 121.4 |
| 75c55d46-d2db-3668-bd7b-3ec321da644d | -1.5869 | -53.7933 | 2024-11-19 03:30:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 109.1 |
| 158a6463-7264-377f-b269-2697b38e9f94 | -23.97 | -54.1595 | 2024-11-19 03:30:00 | GOES-16 | MUNDO NOVO | MATO GROSSO DO SUL | Brasil | 5005681 | 50 | 33 | nan | nan | nan | Mata Atlântica | 66.6 |
| 1aeef43b-a1bb-34cc-bd04-acbf0e6e17eb | -2.766 | -52.5959 | 2024-11-19 03:30:00 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 60.8 |
| 2658992a-3073-34fe-9bbe-630ac1d829b2 | -13.245 | -56.8167 | 2024-11-19 03:30:00 | GOES-16 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 64.5 |
| fce58bae-d6bc-3750-96d6-c8acdf33c0d9 | -20.10405 | -47.46623 | 2024-11-19 03:32:00 | NPP-375D | PEDREGULHO | SÃO PAULO | Brasil | 3537008 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fb24b1bb-ee34-3264-ae48-5794b268a858 | -20.10292 | -47.47115 | 2024-11-19 03:32:00 | NPP-375D | PEDREGULHO | SÃO PAULO | Brasil | 3537008 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| af34f5d0-41cd-36ac-acba-e6e0f288ffc9 | -15.37236 | -43.03812 | 2024-11-19 03:32:00 | NPP-375D | CATUTI | MINAS GERAIS | Brasil | 3115474 | 31 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 89622b41-05e2-3cbb-b2ba-8a9bc8cbb026 | -20.17982 | -40.22763 | 2024-11-19 03:32:00 | NPP-375D | SERRA | ESPÍRITO SANTO | Brasil | 3205002 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 8a0f96f5-a9df-3bd8-bf74-6f30ab5d6636 | -19.83854 | -40.08106 | 2024-11-19 03:32:00 | NPP-375D | ARACRUZ | ESPÍRITO SANTO | Brasil | 3200607 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 41566cb8-b490-37ad-85e0-4f14fe220ff9 | -22.3045 | -49.76691 | 2024-11-19 03:34:00 | NPP-375D | GARÇA | SÃO PAULO | Brasil | 3516705 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.7 |
| f9ed69ce-37ca-3c4f-b55a-9783b64eae03 | -22.30622 | -49.76017 | 2024-11-19 03:34:00 | NPP-375D | GARÇA | SÃO PAULO | Brasil | 3516705 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.7 |
| 11371d56-b8cf-3d1d-9854-f03fbeee898d | -22.31111 | -49.76913 | 2024-11-19 03:34:00 | NPP-375D | GARÇA | SÃO PAULO | Brasil | 3516705 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 1c992404-9d4a-313e-8395-79f07a20b186 | -22.67443 | -42.85484 | 2024-11-19 03:34:00 | NPP-375D | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 0030e7fb-fc46-3064-8ad4-7cd7585b6c82 | -22.30997 | -49.76826 | 2024-11-19 03:34:00 | NPP-375D | GARÇA | SÃO PAULO | Brasil | 3516705 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.2 |
| 9943f36c-b833-3bd1-9a7d-dad213cc72d1 | -22.67743 | -42.85761 | 2024-11-19 03:34:00 | NPP-375D | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| c7fb375b-e006-3513-ac89-4ce833523459 | -22.79059 | -41.98919 | 2024-11-19 03:34:00 | NPP-375D | ARMAÇÃO DOS BÚZIOS | RIO DE JANEIRO | Brasil | 3300233 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 823fb18b-cce2-3c0e-b1d4-3a2dac9243c4 | -22.30336 | -49.76603 | 2024-11-19 03:34:00 | NPP-375D | GARÇA | SÃO PAULO | Brasil | 3516705 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.2 |
| 0f4d9809-2d99-3b8c-a155-773114b12dd7 | -22.52206 | -47.68963 | 2024-11-19 03:34:00 | NPP-375D | CHARQUEADA | SÃO PAULO | Brasil | 3511706 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| a1a0d787-405a-3426-8483-c3fd55ff0641 | -22.67887 | -42.85594 | 2024-11-19 03:34:00 | NPP-375D | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 57af58b6-ab72-36b3-bcc1-402a9dcb22c9 | -4.5616 | -47.9925 | 2024-11-19 03:40:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 61.8 |
| f35c280c-f0d2-364e-853c-f472ae5fab98 | -23.97 | -54.1595 | 2024-11-19 03:40:00 | GOES-16 | MUNDO NOVO | MATO GROSSO DO SUL | Brasil | 5005681 | 50 | 33 | nan | nan | nan | Mata Atlântica | 73.6 |
| a3a26dfc-02c6-35fd-8344-f715cd28dd32 | -4.5614 | -48.0141 | 2024-11-19 03:40:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 153.6 |
| f4a20116-a91c-3a3f-9612-af68dc5ed9ee | -4.58 | -48.0132 | 2024-11-19 03:40:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 48.8 |
| ad85f822-bddc-3b17-be8b-4c5745cd2383 | -4.1182 | -51.0486 | 2024-11-19 03:40:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 39.5 |
| b4e02c10-1b29-35a3-a1de-146c580afb47 | -1.424 | -52.4368 | 2024-11-19 03:40:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 53.5 |
| d2e4df14-9023-32f3-aa22-ebc5aa69b6d0 | -3.5125 | -50.2343 | 2024-11-19 03:40:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 65.8 |
| 2e9ef140-527f-3726-b56c-0b647eaa51c8 | -4.5429 | -48.0151 | 2024-11-19 03:40:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 70.6 |
| aa82a65d-a6bc-3a6d-b352-ca75ff329479 | -23.9506 | -54.0968 | 2024-11-19 03:40:00 | GOES-16 | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 66.5 |
| 9227fba6-55d9-30e7-9806-5ad685328570 | -13.264 | -56.8149 | 2024-11-19 03:40:00 | GOES-16 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 69.5 |
| 29e74f46-7724-3a68-aa63-5c065f633e83 | -4.5613 | -48.0358 | 2024-11-19 03:40:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 46.6 |
| d903f785-bdde-30c1-a7dd-146020728694 | -23.95 | -54.1191 | 2024-11-19 03:40:00 | GOES-16 | MUNDO NOVO | MATO GROSSO DO SUL | Brasil | 5005681 | 50 | 33 | nan | nan | nan | Mata Atlântica | 101.0 |
| 76108e91-2c01-36af-b250-132e47d67873 | -4.1246 | -43.5833 | 2024-11-19 03:40:00 | GOES-16 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 63.1 |
| d82b6ce3-5bc7-39e9-9355-69f1b9ffe754 | -5.9788 | -45.3621 | 2024-11-19 03:40:00 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 99.4 |
| 818bf59c-0246-3d01-8445-1c087b958c6c | -4.1059 | -43.5843 | 2024-11-19 03:40:00 | GOES-16 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 60.4 |
| d087b977-a159-3dae-bd80-a246845a92dc | -1.5869 | -53.7933 | 2024-11-19 03:40:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 82.2 |
| fae1ad98-9d6d-3c15-8366-32e50f4745d5 | -23.9711 | -54.1148 | 2024-11-19 03:40:00 | GOES-16 | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 113.3 |
| baf7f439-da7a-3bc3-bfae-a3b791528fe1 | -1.5869 | -53.8134 | 2024-11-19 03:40:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 84.9 |
| b7cefac6-edb1-3c45-bc81-a9cc13a1ff55 | -23.9706 | -54.1372 | 2024-11-19 03:40:00 | GOES-16 | MUNDO NOVO | MATO GROSSO DO SUL | Brasil | 5005681 | 50 | 33 | nan | nan | nan | Mata Atlântica | 117.3 |
| a1bd11ff-6680-3d07-afb5-baa8ae2b5a9f | -10.9717 | -44.5342 | 2024-11-19 03:40:00 | GOES-16 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 67.1 |
| febd75f1-4b20-390c-b5dc-682780f2c551 | -4.1182 | -51.0486 | 2024-11-19 03:50:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 47.3 |
| f690e630-e2e5-3508-bf60-78337428043e | -23.9294 | -54.1011 | 2024-11-19 03:50:00 | GOES-16 | MUNDO NOVO | MATO GROSSO DO SUL | Brasil | 5005681 | 50 | 33 | nan | nan | nan | Mata Atlântica | 65.6 |
| f4aa6e65-6c20-3c93-8a95-409c2eee21d3 | -4.543 | -47.9934 | 2024-11-19 03:50:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 47.2 |
| 514b3d5d-9e02-366d-8d9b-9a5f5c1dd2fa | -4.1246 | -43.5833 | 2024-11-19 03:50:00 | GOES-16 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 63.7 |
| e1347734-ab43-3c3d-8960-32ee73a590b7 | -23.95 | -54.1191 | 2024-11-19 03:50:00 | GOES-16 | MUNDO NOVO | MATO GROSSO DO SUL | Brasil | 5005681 | 50 | 33 | nan | nan | nan | Mata Atlântica | 99.4 |
| 1ae9dcb2-bc2f-3835-8210-f2bc1cdcfb9c | -1.5869 | -53.8134 | 2024-11-19 03:50:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 95.1 |
| ccfa70e2-8b16-3a35-8bc4-11e750a2d97f | -23.9711 | -54.1148 | 2024-11-19 03:50:00 | GOES-16 | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 96.4 |
| 953547a7-6ef3-3fc3-a816-ab8a0de9fa98 | -5.9788 | -45.3621 | 2024-11-19 03:50:00 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 98.6 |


[Clique aqui para ver as próximas entradas](README16.md)
