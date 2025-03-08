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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0b709247-3bb8-3d12-9c4f-907b4589a1d8 | -20.72336 | -49.43265 | 2025-03-08 04:29:00 | NPP-375D | SÃO JOSÉ DO RIO PRETO | SÃO PAULO | Brasil | 3549805 | 35 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 950208b0-b5e6-38ac-879c-c31baf6069e6 | -20.02553 | -54.6155 | 2025-03-08 04:29:00 | NPP-375D | JARAGUARI | MATO GROSSO DO SUL | Brasil | 5004908 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d5f2b108-1b54-35c2-bf06-a1bbcb2ea625 | -20.72669 | -49.43324 | 2025-03-08 04:29:00 | NPP-375D | SÃO JOSÉ DO RIO PRETO | SÃO PAULO | Brasil | 3549805 | 35 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d567432d-4743-3190-8949-9a41885fd708 | -17.22764 | -52.81441 | 2025-03-08 04:29:00 | NPP-375D | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 0.3 |
| d4a3fcae-471d-3497-a43e-35fb7b8a184c | -16.89334 | -52.25343 | 2025-03-08 04:29:00 | NPP-375D | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| e31ed45a-28f6-331b-badd-f909b0470f0b | -20.05367 | -49.37435 | 2025-03-08 04:29:00 | NPP-375D | PAULO DE FARIA | SÃO PAULO | Brasil | 3536604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| fdfb19f7-8da3-38ff-96fc-96d1088a0c96 | -20.20781 | -45.52565 | 2025-03-08 04:29:00 | NPP-375D | ARCOS | MINAS GERAIS | Brasil | 3104205 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3a64a7a6-f23a-3242-8793-81d8c6fd1a21 | -17.09419 | -43.80359 | 2025-03-08 04:29:00 | NPP-375D | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 61a09d05-c0a9-38c4-ac95-bd0e101a5695 | -17.98064 | -47.21938 | 2025-03-08 04:29:00 | NPP-375D | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| edb3b0c3-350a-38b1-b2f9-6736ff01bda3 | -19.96764 | -44.21626 | 2025-03-08 04:29:00 | NPP-375D | BETIM | MINAS GERAIS | Brasil | 3106705 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 5b5d5ec4-8a40-387e-872e-2d435cbdbb4c | -21.25572 | -48.71205 | 2025-03-08 04:29:00 | NPP-375D | FERNANDO PRESTES | SÃO PAULO | Brasil | 3515608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| b951db30-1fd4-3e58-b5ef-0e3f9da1a539 | -21.19428 | -44.93679 | 2025-03-08 04:29:00 | NPP-375D | IJACI | MINAS GERAIS | Brasil | 3130408 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 0b8886d3-652f-3411-9ad6-004d0072af83 | -21.2585 | -48.71642 | 2025-03-08 04:29:00 | NPP-375D | FERNANDO PRESTES | SÃO PAULO | Brasil | 3515608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 8f02ba0b-9bd9-33d3-9004-00bce5af4775 | -21.25907 | -48.71265 | 2025-03-08 04:29:00 | NPP-375D | FERNANDO PRESTES | SÃO PAULO | Brasil | 3515608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 5caa276a-e9e6-32cf-aebe-d6e948778679 | -16.67906 | -43.88229 | 2025-03-08 04:29:00 | NPP-375D | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 83464ba1-a2b6-3da6-8a3b-fc54d60e99ea | -21.09753 | -50.56562 | 2025-03-08 04:29:00 | NPP-375D | ARAÇATUBA | SÃO PAULO | Brasil | 3502804 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 51c36261-57bd-3eb1-a787-9e0a74d9545a | -21.61502 | -48.4779 | 2025-03-08 04:29:00 | NPP-375D | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2b2ad74c-43f0-31da-852d-c2ca92696558 | -20.72279 | -49.43634 | 2025-03-08 04:29:00 | NPP-375D | SÃO JOSÉ DO RIO PRETO | SÃO PAULO | Brasil | 3549805 | 35 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 87a36232-5218-3fc7-9f75-4cc1e5ece761 | -20.59795 | -51.61124 | 2025-03-08 04:29:00 | NPP-375D | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 9e507a5e-7560-3733-b983-00adddde34b8 | -18.80138 | -51.62488 | 2025-03-08 04:29:00 | NPP-375D | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| db6adc19-42a7-35c3-9ca2-906772396384 | -18.80206 | -51.62086 | 2025-03-08 04:29:00 | NPP-375D | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 01b73620-adf7-31d0-9bef-9effcb5812c8 | -21.25515 | -48.71583 | 2025-03-08 04:29:00 | NPP-375D | FERNANDO PRESTES | SÃO PAULO | Brasil | 3515608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 7e56be3d-e6d8-3a77-a280-85244da34b6e | -21.61164 | -48.47731 | 2025-03-08 04:29:00 | NPP-375D | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 0.5 |
| fed93a7a-ef40-3033-ba78-437b3979782b | -21.6122 | -48.47348 | 2025-03-08 04:29:00 | NPP-375D | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 0.5 |
| af37cc62-5b40-34c6-a9e7-86db2f5b0b4c | -17.22388 | -52.81372 | 2025-03-08 04:29:00 | NPP-375D | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ab351a5c-1559-3d40-831e-0fa5ff5e3668 | -21.90411 | -42.92745 | 2025-03-08 04:29:00 | NPP-375D | CHIADOR | MINAS GERAIS | Brasil | 3116209 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 4e973a2f-cf59-3adb-b362-7383c62c93c5 | -20.76467 | -46.76819 | 2025-03-08 04:29:00 | NPP-375D | ITAÚ DE MINAS | MINAS GERAIS | Brasil | 3133758 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 48ddab49-9c3b-3295-a3fb-2b6a8fc81b87 | -16.28286 | -50.34823 | 2025-03-08 04:29:00 | NPP-375D | SANCLERLÂNDIA | GOIÁS | Brasil | 5219001 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0865060e-6863-3bc3-9309-6a1840689260 | -16.72786 | -49.36488 | 2025-03-08 04:29:00 | NPP-375D | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 43570679-c1a3-3240-976a-467403ed8ad6 | -21.41131 | -50.06963 | 2025-03-08 04:29:00 | NPP-375D | PENÁPOLIS | SÃO PAULO | Brasil | 3537305 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| dcbe9fb4-e84b-32fd-a960-c93cdca62286 | -20.04325 | -45.54959 | 2025-03-08 04:29:00 | NPP-375D | LAGOA DA PRATA | MINAS GERAIS | Brasil | 3137205 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 890563f5-4223-3365-92e2-04e3e5646d41 | -16.28349 | -50.34441 | 2025-03-08 04:29:00 | NPP-375D | SANCLERLÂNDIA | GOIÁS | Brasil | 5219001 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6a6f5320-c472-3b04-83b8-7b2e7e5acb51 | -19.59099 | -46.96034 | 2025-03-08 04:29:00 | NPP-375D | ARAXÁ | MINAS GERAIS | Brasil | 3104007 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 54f875cd-0eaf-3226-be39-b36c237b4af8 | -23.38949 | -51.96438 | 2025-03-08 04:31:00 | NPP-375D | MARINGÁ | PARANÁ | Brasil | 4115200 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 851131d3-81fb-3ca0-8ce2-6e95b1e7cdcc | -23.7347 | -53.2485 | 2025-03-08 04:31:00 | NPP-375D | UMUARAMA | PARANÁ | Brasil | 4128104 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| f3f3002f-1545-3171-a93b-16e1aeb046fb | -22.96884 | -47.45909 | 2025-03-08 04:31:00 | NPP-375D | CAPIVARI | SÃO PAULO | Brasil | 3510401 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 883c3674-57bf-31d4-bb9b-c3b7b9a00e1f | -23.45018 | -47.24852 | 2025-03-08 04:31:00 | NPP-375D | MAIRINQUE | SÃO PAULO | Brasil | 3528403 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 755636c0-2161-3b83-b4b9-8fb50f263add | -28.53845 | -51.82016 | 2025-03-08 04:31:00 | NPP-375D | SÃO DOMINGOS DO SUL | RIO GRANDE DO SUL | Brasil | 4318051 | 43 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 952785a6-0677-3a19-962e-8f3b974aaa3a | -22.75062 | -43.51686 | 2025-03-08 04:31:00 | NPP-375D | NOVA IGUAÇU | RIO DE JANEIRO | Brasil | 3303500 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| b72990f0-fe65-3530-a099-611e83489103 | -23.50587 | -47.19012 | 2025-03-08 04:31:00 | NPP-375D | MAIRINQUE | SÃO PAULO | Brasil | 3528403 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| cb4d6662-e800-37d6-851c-d2ebc9eda44f | -22.75168 | -43.50774 | 2025-03-08 04:31:00 | NPP-375D | NOVA IGUAÇU | RIO DE JANEIRO | Brasil | 3303500 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 84952f27-1410-3a86-9b82-5d62489b5613 | -21.08147 | -54.19159 | 2025-03-08 04:31:00 | NPP-375D | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a18cc700-718b-3498-aed2-41ab987a7380 | -23.33733 | -46.7716 | 2025-03-08 04:31:00 | NPP-375D | CAIEIRAS | SÃO PAULO | Brasil | 3509007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 626ed1d3-db1e-3804-8e07-3c82e286d278 | -23.73545 | -53.24423 | 2025-03-08 04:31:00 | NPP-375D | UMUARAMA | PARANÁ | Brasil | 4128104 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| d53ceda9-4958-35ca-a457-d95bf7759f3b | -21.87608 | -53.71601 | 2025-03-08 04:31:00 | NPP-375D | NOVA ANDRADINA | MATO GROSSO DO SUL | Brasil | 5006200 | 50 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 71d73d3e-b5f6-3362-aeb0-15a8b4b2ab83 | -22.67725 | -42.85417 | 2025-03-08 04:31:00 | NPP-375D | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 847ded99-274f-364a-b847-936301dd7951 | -22.78493 | -43.75898 | 2025-03-08 04:31:00 | NPP-375D | SEROPÉDICA | RIO DE JANEIRO | Brasil | 3305554 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 4340c3e6-7964-33a8-be10-0b83ad25e7ee | -23.59339 | -47.43898 | 2025-03-08 04:31:00 | NPP-375D | VOTORANTIM | SÃO PAULO | Brasil | 3557006 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 2f4433e8-eef9-32bf-909a-837763a3f7b2 | -22.67267 | -42.85362 | 2025-03-08 04:31:00 | NPP-375D | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 2be95817-d74d-3932-ab45-4d0d147e8537 | -27.08411 | -50.51153 | 2025-03-08 04:31:00 | NPP-375D | SANTA CECÍLIA | SANTA CATARINA | Brasil | 4215505 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 3bea67c0-2028-3454-af9c-4befbebcd31f | -27.10822 | -51.90996 | 2025-03-08 04:31:00 | NPP-375D | IRANI | SANTA CATARINA | Brasil | 4207809 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| b00016f5-a46a-369b-91fd-9416c87b4134 | -25.72708 | -50.78119 | 2025-03-08 04:31:00 | NPP-375D | RIO AZUL | PARANÁ | Brasil | 4122008 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 8a4ed6bb-9cc7-3398-acdc-359802411b27 | -30.37074 | -51.98166 | 2025-03-08 04:33:00 | NPP-375D | SÃO JERÔNIMO | RIO GRANDE DO SUL | Brasil | 4318408 | 43 | 33 | nan | nan | nan | Pampa | 21.8 |
| 50c2bc3c-f3d5-3125-becb-d2712db0984b | -30.52687 | -53.63035 | 2025-03-08 04:33:00 | NPP-375D | CAÇAPAVA DO SUL | RIO GRANDE DO SUL | Brasil | 4302808 | 43 | 33 | nan | nan | nan | Pampa | 2.8 |
| a7335f84-cc70-3d44-b4dc-4cfa76566634 | -30.37339 | -51.97751 | 2025-03-08 04:33:00 | NPP-375D | SÃO JERÔNIMO | RIO GRANDE DO SUL | Brasil | 4318408 | 43 | 33 | nan | nan | nan | Pampa | 28.2 |
| 1d531823-15f0-305a-aff3-4972ee35190a | -30.37262 | -51.96962 | 2025-03-08 04:33:00 | NPP-375D | SÃO JERÔNIMO | RIO GRANDE DO SUL | Brasil | 4318408 | 43 | 33 | nan | nan | nan | Pampa | 1.0 |
| dda0ab2a-ab7e-3f90-bf0f-013eb3871663 | -30.37276 | -51.98152 | 2025-03-08 04:33:00 | NPP-375D | SÃO JERÔNIMO | RIO GRANDE DO SUL | Brasil | 4318408 | 43 | 33 | nan | nan | nan | Pampa | 18.8 |
| 9c53dcab-6be3-30c5-bf52-e45fe765d69c | -29.90327 | -51.53948 | 2025-03-08 04:33:00 | NPP-375D | TRIUNFO | RIO GRANDE DO SUL | Brasil | 4322004 | 43 | 33 | nan | nan | nan | Pampa | 1.3 |
| dbd78bec-d6a9-3740-9b3c-667b8d262c36 | -30.32448 | -53.41762 | 2025-03-08 04:33:00 | NPP-375D | CAÇAPAVA DO SUL | RIO GRANDE DO SUL | Brasil | 4302808 | 43 | 33 | nan | nan | nan | Pampa | 3.0 |
| 0b08ae92-ad1d-3363-b7af-169dbc9a7413 | -30.37463 | -51.96947 | 2025-03-08 04:33:00 | NPP-375D | SÃO JERÔNIMO | RIO GRANDE DO SUL | Brasil | 4318408 | 43 | 33 | nan | nan | nan | Pampa | 7.6 |
| a9af6b79-0c2b-3b17-8968-d88add888d3e | -30.36867 | -51.97295 | 2025-03-08 04:33:00 | NPP-375D | SÃO JERÔNIMO | RIO GRANDE DO SUL | Brasil | 4318408 | 43 | 33 | nan | nan | nan | Pampa | 14.0 |
| 72bff6b3-03b8-30d6-94f7-18c898fdf3f8 | -30.37401 | -51.97349 | 2025-03-08 04:33:00 | NPP-375D | SÃO JERÔNIMO | RIO GRANDE DO SUL | Brasil | 4318408 | 43 | 33 | nan | nan | nan | Pampa | 28.2 |
| 60ddfeeb-eb9d-3e29-a79f-cc50ac252733 | -30.32784 | -53.41839 | 2025-03-08 04:33:00 | NPP-375D | CAÇAPAVA DO SUL | RIO GRANDE DO SUL | Brasil | 4302808 | 43 | 33 | nan | nan | nan | Pampa | 3.0 |
| f35e7ea2-d57c-3284-bbe1-a79e7c63a16d | -30.36804 | -51.97696 | 2025-03-08 04:33:00 | NPP-375D | SÃO JERÔNIMO | RIO GRANDE DO SUL | Brasil | 4318408 | 43 | 33 | nan | nan | nan | Pampa | 14.0 |
| 7fa16cd5-0acb-3e02-ba15-087a74e4eef7 | -30.91646 | -52.18451 | 2025-03-08 04:33:00 | NPP-375D | CRISTAL | RIO GRANDE DO SUL | Brasil | 4306056 | 43 | 33 | nan | nan | nan | Pampa | 1.2 |
| 31fa3cc5-d5e3-3371-b2e0-688d2ff13a43 | -30.52885 | -53.63942 | 2025-03-08 04:33:00 | NPP-375D | CAÇAPAVA DO SUL | RIO GRANDE DO SUL | Brasil | 4302808 | 43 | 33 | nan | nan | nan | Pampa | 2.9 |
| a1b3b4be-df83-3d54-9871-4d0b12948b38 | -30.37136 | -51.97765 | 2025-03-08 04:33:00 | NPP-375D | SÃO JERÔNIMO | RIO GRANDE DO SUL | Brasil | 4318408 | 43 | 33 | nan | nan | nan | Pampa | 14.0 |
| d1d443d7-df1f-30cc-a6ca-fa3102c8a7eb | -29.23953 | -53.67972 | 2025-03-08 04:33:00 | NPP-375D | JÚLIO DE CASTILHOS | RIO GRANDE DO SUL | Brasil | 4311205 | 43 | 33 | nan | nan | nan | Pampa | 0.6 |
| d2ccf043-ecd2-3c33-b271-820785f87bcf | -30.52618 | -53.63452 | 2025-03-08 04:33:00 | NPP-375D | CAÇAPAVA DO SUL | RIO GRANDE DO SUL | Brasil | 4302808 | 43 | 33 | nan | nan | nan | Pampa | 2.9 |
| 872cf83f-6510-3396-ac82-074dc6fad0d6 | -30.32715 | -53.42249 | 2025-03-08 04:33:00 | NPP-375D | CAÇAPAVA DO SUL | RIO GRANDE DO SUL | Brasil | 4302808 | 43 | 33 | nan | nan | nan | Pampa | 10.9 |
| c86fb7fe-6b9a-323b-9fb3-9ec4479ba5ca | -30.37199 | -51.97363 | 2025-03-08 04:33:00 | NPP-375D | SÃO JERÔNIMO | RIO GRANDE DO SUL | Brasil | 4318408 | 43 | 33 | nan | nan | nan | Pampa | 14.0 |
| ebc9b704-a94e-39c3-a451-92b777c56acf | -29.24336 | -52.31633 | 2025-03-08 04:33:00 | NPP-375D | PROGRESSO | RIO GRANDE DO SUL | Brasil | 4315156 | 43 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 5eaab6b5-b838-3c8f-8a1c-9426fd444e49 | -6.95812 | -43.01908 | 2025-03-08 04:50:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 9c0c976c-2846-3320-bbc3-6d7757f9f59a | -9.92917 | -59.90733 | 2025-03-08 04:50:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| d2dbadd2-74be-3ab1-992a-12295da7db1b | -6.96365 | -43.0199 | 2025-03-08 04:50:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| ee1a95e4-37a6-342d-839c-3d7ef0cd8596 | -10.98214 | -44.72577 | 2025-03-08 04:50:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| f66453bf-763a-3566-8926-583e29a6b16f | -6.96315 | -43.02345 | 2025-03-08 04:50:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 8667b328-c8c3-3d23-8d01-d016d9dfaa12 | -6.9692 | -43.02059 | 2025-03-08 04:50:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| f364931b-f981-3967-b447-d66417b30657 | -6.9697 | -43.01699 | 2025-03-08 04:50:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 5bb2e371-d444-31e3-808f-6574f1e883d1 | -11.798 | -46.65042 | 2025-03-08 04:50:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6749fe53-2559-3a0d-826f-4c1033337462 | -10.6601 | -44.40242 | 2025-03-08 04:50:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 230539c3-edb4-3ad8-80a8-48d5e5d49744 | -10.98173 | -44.72898 | 2025-03-08 04:50:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 35f2bf76-ddeb-3912-bde5-45c64c7e1496 | -6.96415 | -43.01628 | 2025-03-08 04:50:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| be77d018-a350-3efe-bf8d-ba09c665c083 | -10.66542 | -44.4031 | 2025-03-08 04:50:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b3b25e4a-7bd3-3558-adc0-8dd27e7312e2 | -9.92996 | -59.90291 | 2025-03-08 04:50:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 13f46acd-b55f-334f-b943-a42b474f46bc | -6.9687 | -43.02416 | 2025-03-08 04:50:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| cbff769f-028f-3017-a6c7-0e5f2123ccfb | -10.66052 | -44.39907 | 2025-03-08 04:50:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1e6426e2-1750-3883-8d4e-83116f612d8d | -6.95862 | -43.01546 | 2025-03-08 04:50:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 930cf6be-2087-3daa-9dd5-7e9959478c5a | -10.31614 | -48.64305 | 2025-03-08 04:50:00 | NOAA-20 | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7fb005af-57e8-39ca-bae1-9e52fdb45721 | -9.92555 | -59.90209 | 2025-03-08 04:50:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 05eae3a1-5959-3d00-8af5-d9eef584f414 | -10.665 | -44.40641 | 2025-03-08 04:50:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3b93869a-45ff-3bf5-8072-977a49aab225 | -12.90372 | -45.07165 | 2025-03-08 04:53:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 63dcd655-4a96-3d4e-bac6-7561a8b719d1 | -12.9033 | -45.0722 | 2025-03-08 04:53:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e11f3a66-c642-3e5c-b84b-5e32b03bde46 | -19.14634 | -47.09325 | 2025-03-08 04:53:00 | NOAA-20 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| dc98709d-d0fd-3582-bad5-ab7c2f04191c | -21.4371 | -57.26273 | 2025-03-08 04:53:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1ae5b244-594b-362e-bbf6-1ebfa2e33852 | -15.07679 | -48.94656 | 2025-03-08 04:53:00 | NOAA-20 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f15f1996-6145-33a5-9274-f690ab0e4278 | -14.57619 | -57.10584 | 2025-03-08 04:53:00 | NOAA-20 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bcb334f9-6ec5-3e75-b491-8f67908fc08f | -23.52872 | -55.44573 | 2025-03-08 04:53:00 | NOAA-20 | PARANHOS | MATO GROSSO DO SUL | Brasil | 5006358 | 50 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| d90ebf84-6967-30cd-9403-869c1e2295f8 | -12.59694 | -46.74252 | 2025-03-08 04:53:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4941e480-1182-3204-b63d-c310e9cf7500 | -22.67718 | -42.85858 | 2025-03-08 04:53:00 | NOAA-20 | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |


[Clique aqui para ver as próximas entradas](README5.md)
