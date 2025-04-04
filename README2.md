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
| 1ab7868a-fa1b-34ad-97a0-1c117dab5ed9 | -8.11084 | -43.1291 | 2025-04-04 03:55:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 7.6 |
| 1c82732b-61e7-31aa-81ef-27fe6aef56b0 | -15.492 | -39.81321 | 2025-04-04 03:55:00 | NOAA-21 | PAU BRASIL | BAHIA | Brasil | 2923902 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| d3783966-f0cd-3ab6-aa98-684e529536fc | -11.02083 | -45.24501 | 2025-04-04 03:55:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 058a5233-3750-3a80-aa21-46fc111e8bfd | -13.02613 | -45.08631 | 2025-04-04 03:55:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| baa3912c-5ea1-39ad-bbfe-cf769dc7752a | -8.72829 | -44.01986 | 2025-04-04 03:55:00 | NOAA-21 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 41032950-cac3-381f-ba80-4acc82dc259e | -9.35093 | -40.4769 | 2025-04-04 03:55:00 | NOAA-21 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 497c08a5-ead9-3739-868a-06789f602812 | -13.03825 | -45.08853 | 2025-04-04 03:55:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 73e20a4a-976e-375c-b35a-6ea13c4925f3 | -11.27834 | -40.98085 | 2025-04-04 03:55:00 | NOAA-21 | MORRO DO CHAPÉU | BAHIA | Brasil | 2921708 | 29 | 33 | nan | nan | nan | Caatinga | 4.6 |
| 31a3425c-b507-3c2d-8e75-0ffd1f1c862a | -13.02548 | -45.08995 | 2025-04-04 03:55:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 17836707-8d98-3108-aaa0-22a46a3f78f6 | -11.03043 | -44.42496 | 2025-04-04 03:55:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 02181581-30e2-3d96-a61b-c67c5a06f202 | -14.12676 | -47.66015 | 2025-04-04 03:55:00 | NOAA-21 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| feb3af30-a6e4-3f92-a38c-f56e1aa9adbf | -8.10698 | -43.12847 | 2025-04-04 03:55:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 6.1 |
| 606a30fa-9c4e-357c-bc63-9ae8b80fe625 | -13.43168 | -41.78646 | 2025-04-04 03:55:00 | NOAA-21 | RIO DE CONTAS | BAHIA | Brasil | 2926707 | 29 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 2d45593e-b76b-3f50-a40c-7104146cb6fb | -10.42245 | -39.44787 | 2025-04-04 03:55:00 | NOAA-21 | MONTE SANTO | BAHIA | Brasil | 2921500 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 7f01d580-224e-3b14-899a-27b5004ab34e | -12.50281 | -45.50525 | 2025-04-04 03:55:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 7539cf80-faed-3bef-b7e0-6b8a8bb259b7 | -11.27803 | -42.32922 | 2025-04-04 03:55:00 | NOAA-21 | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 3.2 |
| c68e598c-3828-32e3-97f7-089fb582d09a | -12.49545 | -47.47935 | 2025-04-04 03:55:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 31ad1f92-a43f-3ec6-9f30-00c43eed9188 | -13.0355 | -45.08051 | 2025-04-04 03:55:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 9bee63f3-75b2-3168-8e87-225216025be1 | -11.6419 | -37.88965 | 2025-04-04 03:55:00 | NOAA-21 | RIO REAL | BAHIA | Brasil | 2927002 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 8d1d66ee-77fa-3dd2-abf5-32774fba6dd4 | -8.1018 | -43.12545 | 2025-04-04 03:55:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 0eac3e0e-e874-30d7-83b7-9b551dbe23d7 | -15.57069 | -40.09778 | 2025-04-04 03:55:00 | NOAA-21 | ITARANTIM | BAHIA | Brasil | 2916807 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| d11a4fac-d08c-3f51-ad5d-c44caeac2c2c | -13.66951 | -44.05944 | 2025-04-04 03:55:00 | NOAA-21 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b9131741-8998-3445-9235-7c95ed9c2fc2 | -13.48379 | -44.03053 | 2025-04-04 03:55:00 | NOAA-21 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| fbd85de0-f7c5-3efa-b1a7-ae3864f592c6 | -12.27936 | -43.52575 | 2025-04-04 03:55:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7bd48dba-0306-3d8d-a181-8a448f4af38b | -13.03421 | -45.08778 | 2025-04-04 03:55:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2d207315-111c-35ab-8b53-8116e564531f | -10.69526 | -37.0505 | 2025-04-04 03:55:00 | NOAA-21 | ROSÁRIO DO CATETE | SERGIPE | Brasil | 2806107 | 28 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| b30de733-1e48-348e-8eb0-f2102e4703f8 | -13.03017 | -45.08704 | 2025-04-04 03:55:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 67b0a8ae-cdbd-331c-be26-7fb9cea0707c | -8.10311 | -43.12785 | 2025-04-04 03:55:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 6.1 |
| 932b06a9-f83d-3ccd-a00e-0488be01dd00 | -10.35004 | -38.47149 | 2025-04-04 03:55:00 | NOAA-21 | NOVO TRIUNFO | BAHIA | Brasil | 2923050 | 29 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 368320a9-c37b-3773-8d67-5896706ad6db | -11.28132 | -42.32863 | 2025-04-04 03:55:00 | NOAA-21 | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 2.7 |
| c45c1135-ec25-3fbe-a3c6-6c1af38bcfd3 | -8.11552 | -43.1249 | 2025-04-04 03:55:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 7.6 |
| 018097bf-215e-33fc-b331-0a08ddbd561c | -10.35336 | -38.47202 | 2025-04-04 03:55:00 | NOAA-21 | NOVO TRIUNFO | BAHIA | Brasil | 2923050 | 29 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 0953626a-5e69-3c03-aed5-42efe7ede38a | -17.83121 | -42.62657 | 2025-04-04 03:57:00 | NOAA-21 | ARICANDUVA | MINAS GERAIS | Brasil | 3104452 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 6d4f2dfa-892c-3c04-a6ac-ff21c60bba56 | -22.6759 | -42.85336 | 2025-04-04 03:57:00 | NOAA-21 | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| e07537d3-63b0-3f23-afbf-2a6c317c92fc | -21.6265 | -43.46586 | 2025-04-04 03:57:00 | NOAA-21 | JUIZ DE FORA | MINAS GERAIS | Brasil | 3136702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 691ee3d2-8c67-32ee-a19f-e8bf54b2c481 | -20.34967 | -40.3617 | 2025-04-04 03:57:00 | NOAA-21 | CARIACICA | ESPÍRITO SANTO | Brasil | 3201308 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 9a05ae74-d1c4-3fb5-9e7e-d8f2b2c6d3d2 | -17.83058 | -42.63037 | 2025-04-04 03:57:00 | NOAA-21 | ARICANDUVA | MINAS GERAIS | Brasil | 3104452 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| d0f9440f-90a5-3fe9-b2a3-a03086a11735 | -17.0362 | -40.15748 | 2025-04-04 03:57:00 | NOAA-21 | JUCURUÇU | BAHIA | Brasil | 2918456 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 1d97ec3c-7c15-3946-aa8f-6c85e6bfb2c4 | -17.09564 | -43.80596 | 2025-04-04 03:57:00 | NOAA-21 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e88f00ed-ec69-30a8-b2ec-ec2a08da7e92 | -17.67897 | -42.7401 | 2025-04-04 03:57:00 | NOAA-21 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 37c4a498-9153-3310-8e8b-176dd418ba87 | -16.48151 | -40.25161 | 2025-04-04 03:57:00 | NOAA-21 | SANTO ANTÔNIO DO JACINTO | MINAS GERAIS | Brasil | 3160306 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 95762647-d662-322e-8be3-1ca53c24ea6d | -19.44695 | -54.78399 | 2025-04-04 03:57:00 | NOAA-21 | SÃO GABRIEL DO OESTE | MATO GROSSO DO SUL | Brasil | 5007695 | 50 | 33 | nan | nan | nan | Cerrado | 6.2 |
| b7d1e4ef-d59e-366a-badc-44802005abbb | -20.7641 | -46.77046 | 2025-04-04 03:57:00 | NOAA-21 | ITAÚ DE MINAS | MINAS GERAIS | Brasil | 3133758 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| d98833ca-e19f-3dba-aaea-5bea97cb445c | -18.03924 | -39.92633 | 2025-04-04 03:57:00 | NOAA-21 | MUCURI | BAHIA | Brasil | 2922003 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 1448eda8-8282-3307-9a42-a7d60ee97ae3 | -21.62587 | -43.46972 | 2025-04-04 03:57:00 | NOAA-21 | JUIZ DE FORA | MINAS GERAIS | Brasil | 3136702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| f1463e7f-48e6-351e-a0ac-b40ba5a26b39 | -17.83459 | -42.62715 | 2025-04-04 03:57:00 | NOAA-21 | ARICANDUVA | MINAS GERAIS | Brasil | 3104452 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| 0797882d-e5e4-3357-a234-d0357afb1504 | -20.58047 | -56.03461 | 2025-04-04 03:57:00 | NOAA-21 | ANASTÁCIO | MATO GROSSO DO SUL | Brasil | 5000708 | 50 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 7dcdad4b-7bdc-3496-897d-582709068298 | -20.16281 | -47.32495 | 2025-04-04 03:57:00 | NOAA-21 | PEDREGULHO | SÃO PAULO | Brasil | 3537008 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| aced557a-470f-3f82-a583-a47073040609 | -17.67834 | -42.74392 | 2025-04-04 03:57:00 | NOAA-21 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| fb2967ec-86db-305e-86c8-f50756c87406 | -16.21591 | -43.74209 | 2025-04-04 03:57:00 | NOAA-21 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bc019258-ea1f-3ed9-8a3f-238d78a8f3a6 | -20.33165 | -46.16029 | 2025-04-04 03:57:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 86681af5-a883-37c4-8a94-e41871ed9625 | -16.68106 | -43.88588 | 2025-04-04 03:57:00 | NOAA-21 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 886f072f-97bd-38f4-a16f-c1c99b492c89 | -15.51286 | -42.61472 | 2025-04-04 03:57:00 | NOAA-21 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 51d348e2-ebde-36ba-8dcb-df2955bd8349 | -16.63694 | -43.3604 | 2025-04-04 03:57:00 | NOAA-21 | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6c804eb2-ae94-3817-a21b-d145fecddd8b | -16.04363 | -43.80835 | 2025-04-04 03:57:00 | NOAA-21 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 42413f87-3da1-3d2b-884e-1be4c7723b03 | -16.63276 | -43.36375 | 2025-04-04 03:57:00 | NOAA-21 | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fa82ba32-a112-3129-9476-bc5beb9341dd | -17.59548 | -43.19685 | 2025-04-04 03:57:00 | NOAA-21 | CARBONITA | MINAS GERAIS | Brasil | 3113503 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 66acb109-3925-3f8c-a281-29f4622d6513 | -22.67922 | -42.85398 | 2025-04-04 03:57:00 | NOAA-21 | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| acdb0a1c-a54b-3df8-8359-321ca4ac536f | -22.9011 | -43.75196 | 2025-04-04 03:57:00 | NOAA-21 | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 3bccca15-2f0f-32a7-a5bb-fbff1ea79e36 | -16.68328 | -43.8835 | 2025-04-04 03:57:00 | NOAA-21 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| c7de32ba-92d5-3444-8521-067113894224 | -17.83798 | -42.62774 | 2025-04-04 03:57:00 | NOAA-21 | ARICANDUVA | MINAS GERAIS | Brasil | 3104452 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| a3f724f7-d3ef-34e1-90bd-b44907b87fe7 | -20.57885 | -56.04121 | 2025-04-04 03:57:00 | NOAA-21 | ANASTÁCIO | MATO GROSSO DO SUL | Brasil | 5000708 | 50 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 11ded78f-deef-3327-b63d-f10452a65620 | -17.78005 | -42.80931 | 2025-04-04 03:57:00 | NOAA-21 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3d2ae042-2138-395f-806c-9b358bd8801a | -17.15513 | -44.79097 | 2025-04-04 03:57:00 | NOAA-21 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5a6426e9-4ef5-3888-8039-de68d2246cbe | -17.16258 | -44.79239 | 2025-04-04 03:57:00 | NOAA-21 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c8c22034-df20-3b3b-a902-fbd5d9291ccc | -17.15886 | -44.79167 | 2025-04-04 03:57:00 | NOAA-21 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0e1962ca-0495-36d8-ad7c-30948f3f0610 | -17.15431 | -44.79565 | 2025-04-04 03:57:00 | NOAA-21 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| fd2efa54-741f-366b-93dd-1b2d316c39cd | -19.44051 | -54.78196 | 2025-04-04 03:57:00 | NOAA-21 | SÃO GABRIEL DO OESTE | MATO GROSSO DO SUL | Brasil | 5007695 | 50 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 0d2f8b68-2984-3a37-8a62-5bdba5b14f9c | -19.43903 | -54.78823 | 2025-04-04 03:57:00 | NOAA-21 | RIO NEGRO | MATO GROSSO DO SUL | Brasil | 5007307 | 50 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 7e26f886-15f8-3e29-a5c5-1af1c1cc0037 | -17.15804 | -44.79637 | 2025-04-04 03:57:00 | NOAA-21 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 08eccae4-49d2-3c54-842c-f7d413103b35 | -15.76158 | -43.93507 | 2025-04-04 03:57:00 | NOAA-21 | VARZELÂNDIA | MINAS GERAIS | Brasil | 3170909 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8a49c14a-9740-3a99-afd8-1b98b66cb155 | -16.03353 | -40.81284 | 2025-04-04 03:57:00 | NOAA-21 | ALMENARA | MINAS GERAIS | Brasil | 3101706 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 37733697-640c-3958-941b-24cfc157c782 | -25.56748 | -49.36707 | 2025-04-04 04:00:00 | NOAA-21 | ARAUCÁRIA | PARANÁ | Brasil | 4101804 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 5aa4c147-0f38-3b9a-844d-42015f7cb2bd | -23.98709 | -48.91911 | 2025-04-04 04:00:00 | NOAA-21 | ITAPEVA | SÃO PAULO | Brasil | 3522406 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3dce7a7f-cf78-3487-8e56-57fed195e700 | -20.57907 | -56.03887 | 2025-04-04 04:00:00 | NOAA-21 | ANASTÁCIO | MATO GROSSO DO SUL | Brasil | 5000708 | 50 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 125f0645-931d-3f1c-85e8-78dc02f793a9 | -20.58075 | -56.0322 | 2025-04-04 04:00:00 | NOAA-21 | ANASTÁCIO | MATO GROSSO DO SUL | Brasil | 5000708 | 50 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 0a726157-6630-3a23-acfc-f1613f920645 | -8.10142 | -43.12438 | 2025-04-04 04:19:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 8655980b-ee3e-3ec3-b79c-6680d11fe215 | -6.539 | -43.09509 | 2025-04-04 04:19:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| d8b6cbb0-5288-3360-9a7a-ffb9eae4400a | -8.10769 | -43.12917 | 2025-04-04 04:19:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 44246857-cedc-3bbd-9e6e-29f928120df5 | -8.11169 | -43.12598 | 2025-04-04 04:19:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 4.5 |
| 865d4e22-4240-36b8-83e8-da56046b22f4 | -10.34654 | -38.47395 | 2025-04-04 04:19:00 | NPP-375D | NOVO TRIUNFO | BAHIA | Brasil | 2923050 | 29 | 33 | nan | nan | nan | Caatinga | 2.6 |
| d41834a3-12f4-3856-8148-9c2b91f4209c | -8.72739 | -44.01926 | 2025-04-04 04:19:00 | NPP-375D | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c064c7a2-776f-3f78-904a-271d0f31c25f | -8.10427 | -43.12864 | 2025-04-04 04:19:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| e3f2c914-b6f7-35ab-ae6d-a2764375afaf | -8.72684 | -44.02282 | 2025-04-04 04:19:00 | NPP-375D | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5ba2805b-8e56-3bea-8f31-6cb0ee89b5cd | -7.23056 | -44.7686 | 2025-04-04 04:19:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fa221365-eeac-3b7b-81a8-4951119c1b0c | -5.6325 | -44.32088 | 2025-04-04 04:19:00 | NPP-375D | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d03ec9d6-d1dc-3cd6-949f-fbf6cba654b2 | -10.35114 | -38.4747 | 2025-04-04 04:19:00 | NPP-375D | NOVO TRIUNFO | BAHIA | Brasil | 2923050 | 29 | 33 | nan | nan | nan | Caatinga | 2.6 |
| b15b2d30-6bcb-3bb7-8a90-7f7eaf126d52 | -8.10484 | -43.12491 | 2025-04-04 04:19:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 303dd072-ef98-30e5-96df-b0b38744be83 | -4.81788 | -42.98368 | 2025-04-04 04:19:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| e102cbd5-f69c-3a61-b830-7dca50cd46b9 | -10.35182 | -38.46991 | 2025-04-04 04:19:00 | NPP-375D | NOVO TRIUNFO | BAHIA | Brasil | 2923050 | 29 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 4512f256-af5c-33f9-80b2-515f9b29c3a7 | -5.94302 | -45.39685 | 2025-04-04 04:19:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| c2d506af-354d-3e65-a4c8-bb3c4cc7a1e5 | -9.52736 | -42.93774 | 2025-04-04 04:19:00 | NPP-375D | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 512deace-2fc4-3c5a-8df3-864a2eedd62f | -10.35005 | -38.47142 | 2025-04-04 04:19:00 | NPP-375D | NOVO TRIUNFO | BAHIA | Brasil | 2923050 | 29 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 4329d90e-ed0b-3ed2-9bc4-91293b713a03 | -2.62271 | -44.28661 | 2025-04-04 04:19:00 | NPP-375D | SÃO LUÍS | MARANHÃO | Brasil | 2111300 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8eb1a236-2db2-3f28-b1b5-6839e09fab1c | -8.10826 | -43.12545 | 2025-04-04 04:19:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 4.5 |
| d8853b14-45fa-3d14-83a0-a5164cd2fd38 | -5.02564 | -43.59994 | 2025-04-04 04:19:00 | NPP-375D | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7ec93ccc-755e-31d3-bce0-0730ad6172f8 | -5.02509 | -43.60342 | 2025-04-04 04:19:00 | NPP-375D | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 527f24d9-e210-33b2-8fb5-0b394a771e7e | -6.53843 | -43.09873 | 2025-04-04 04:19:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 42e03c93-1d34-343b-a6d8-c49498243da7 | -6.2963 | -45.26248 | 2025-04-04 04:19:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 869491fb-7185-3a84-93bc-38a0bd769f54 | -5.94637 | -45.39737 | 2025-04-04 04:19:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |


[Clique aqui para ver as próximas entradas](README3.md)
