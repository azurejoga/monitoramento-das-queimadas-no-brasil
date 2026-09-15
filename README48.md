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

## Dados Diários - Página 48

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 55063d65-01e7-37db-9c9f-cb992f1278e1 | -15.53466 | -41.78473 | 2026-09-15 04:34:00 | NOAA-20 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| 03d6f6e0-fd8c-34c6-bcbd-f2e36bffe170 | -13.62409 | -47.91613 | 2026-09-15 04:34:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 30415209-5da5-3069-b383-af6efab3a3fa | -13.32559 | -51.60779 | 2026-09-15 04:34:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1d79c073-2d5d-3a06-baf4-18758b7e5635 | -9.85606 | -46.00504 | 2026-09-15 04:34:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b76cad89-12f9-348b-be4a-ae65ceecd456 | -9.47676 | -45.46919 | 2026-09-15 04:34:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6dbcff9d-6dd9-3898-b985-87a95d01cc12 | -13.59374 | -47.91458 | 2026-09-15 04:34:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ed0ac4c5-54e8-3e28-a2ed-c965e2c7fa2a | -10.69432 | -54.1724 | 2026-09-15 04:34:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 0a166419-d188-3203-ab61-bbb0ad851394 | -14.20311 | -47.42601 | 2026-09-15 04:34:00 | NOAA-20 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 31.0 |
| c0cfe3d3-22a2-3766-bf79-bbb01477ffb9 | -8.53376 | -54.70662 | 2026-09-15 04:34:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d4a9b1b5-3317-35f2-afd3-7c9f0b23db9f | -13.60091 | -47.91214 | 2026-09-15 04:34:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d2981a6f-935e-3d5b-9cf3-577b4be047b6 | -10.4397 | -48.64795 | 2026-09-15 04:34:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 36237ecc-aee9-38b5-b809-212a80113c51 | -10.75674 | -44.82106 | 2026-09-15 04:34:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 2bad83e8-2b4f-3385-a408-dfc432b97aea | -10.67694 | -54.15396 | 2026-09-15 04:34:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bd4446a8-e362-3f33-b41b-f38cb0a0f5c4 | -10.9883 | -48.32011 | 2026-09-15 04:34:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 68ab005b-95ae-389a-8019-7f5c7598ccd7 | -9.35177 | -50.13689 | 2026-09-15 04:34:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 906eeaec-374d-3c12-9cec-e7084d57db52 | -10.0522 | -44.88938 | 2026-09-15 04:34:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 904a532e-a67d-3202-a6f6-7e53a9ea6a62 | -9.83345 | -55.20356 | 2026-09-15 04:34:00 | NOAA-20 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f8909c5b-056e-31b9-b00d-9592a1ca80cf | -13.43571 | -43.82315 | 2026-09-15 04:34:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 38b131eb-399c-39b9-825e-dd31f974e155 | -6.32125 | -59.99728 | 2026-09-15 04:34:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5b0763e5-d345-377b-b8c7-36b30bcc32a3 | -9.42348 | -49.55043 | 2026-09-15 04:34:00 | NOAA-20 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| dbb0e421-e732-325a-a252-7e8735ab49d9 | -12.15543 | -47.99053 | 2026-09-15 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 79960faf-f168-3e4f-b8f8-f08764644fe7 | -8.79673 | -50.49139 | 2026-09-15 04:34:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 2821324b-02d5-3be2-be5a-e2d59f0965ef | -14.66903 | -48.00711 | 2026-09-15 04:34:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 85f78a5a-5acf-3054-831e-d34ca97ef7cb | -14.67557 | -42.8485 | 2026-09-15 04:34:00 | NOAA-20 | SEBASTIÃO LARANJEIRAS | BAHIA | Brasil | 2930006 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 124ee488-0337-3262-9c8f-cdccac243f44 | -9.36064 | -50.19352 | 2026-09-15 04:34:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 845dd713-5f9d-3214-a658-d662353bd55f | -14.16208 | -47.40431 | 2026-09-15 04:34:00 | NOAA-20 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 69b40c88-b619-3081-9078-55ba0110c993 | -10.45734 | -51.23498 | 2026-09-15 04:34:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 857fca91-1141-3c87-b552-0f02b9eab07e | -10.67534 | -54.16297 | 2026-09-15 04:34:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bb821fce-b8fa-361d-877d-960a04ff35a4 | -15.04722 | -48.55887 | 2026-09-15 04:34:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4b6fedf1-a6ba-3561-821d-ba9f36e3718d | -10.02969 | -52.12379 | 2026-09-15 04:34:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8e1c6986-3383-3026-b7d3-cc29cd2f36da | -13.22815 | -51.65093 | 2026-09-15 04:34:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 6.2 |
| da312a45-5f3b-36a7-a123-c13fac157170 | -9.42711 | -50.10332 | 2026-09-15 04:34:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c411da1b-ff1b-374b-87ae-dea0f889579f | -15.44743 | -44.84541 | 2026-09-15 04:34:00 | NOAA-20 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| eac72fd1-e689-33fc-bc3a-ba432216c205 | -10.97658 | -48.32922 | 2026-09-15 04:34:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 706e3de0-697a-3288-911b-d2087104a0ff | -14.15984 | -47.39677 | 2026-09-15 04:34:00 | NOAA-20 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 16faa009-80d9-38ce-8286-523fc0f28885 | -10.75381 | -44.81655 | 2026-09-15 04:34:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 1e1aca11-5401-3e89-b813-cae6b00534e2 | -12.47454 | -41.40411 | 2026-09-15 04:34:00 | NOAA-20 | LENÇÓIS | BAHIA | Brasil | 2919306 | 29 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 36e2703a-ead2-3442-8814-1e2b8e568669 | -14.85909 | -48.13715 | 2026-09-15 04:34:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 7c0dcdf1-2afe-3d7f-8ffa-4c0045eac477 | -15.29055 | -42.79559 | 2026-09-15 04:34:00 | NOAA-20 | MONTE AZUL | MINAS GERAIS | Brasil | 3142908 | 31 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 7fadb8a1-51a0-3be4-a850-7527bda586d1 | -7.65481 | -49.50852 | 2026-09-15 04:34:00 | NOAA-20 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| da094308-9c62-3482-8d37-3e26f6579188 | -9.45589 | -56.7086 | 2026-09-15 04:34:00 | NOAA-20 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a6c6380e-f817-3d12-a7e0-23df8d85941b | -15.06263 | -48.56878 | 2026-09-15 04:34:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 156d98a9-b028-3730-a9a0-a17c1f5478ec | -15.29097 | -42.79245 | 2026-09-15 04:34:00 | NOAA-20 | MONTE AZUL | MINAS GERAIS | Brasil | 3142908 | 31 | 33 | nan | nan | nan | Cerrado | 5.2 |
| eb9a2332-d649-3a27-a777-c3143c8e1b2d | -10.58218 | -47.737 | 2026-09-15 04:34:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 245659bb-b1f7-39bb-ae41-613c9a6c8b78 | -14.76558 | -42.94584 | 2026-09-15 04:34:00 | NOAA-20 | ESPINOSA | MINAS GERAIS | Brasil | 3124302 | 31 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 756ced22-db28-3a1f-afbb-10cfcbaed261 | -11.81296 | -46.57869 | 2026-09-15 04:34:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8d167022-6bc1-3e28-ada9-270fa7818f48 | -11.13533 | -47.71941 | 2026-09-15 04:34:00 | NOAA-20 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| deaf8720-43f3-3917-a1bd-2ebb6a97d969 | -8.53858 | -54.70749 | 2026-09-15 04:34:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 49f9894c-71d6-3983-be2e-6b3ae40c13b5 | -11.88436 | -43.82108 | 2026-09-15 04:34:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 62.1 |
| 33a052c1-82ec-36bd-89c4-7aef0d7d52f7 | -10.23412 | -50.90688 | 2026-09-15 04:34:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| cbb95ef1-3e39-345d-9f90-18335b288fa9 | -9.57236 | -55.14359 | 2026-09-15 04:34:00 | NOAA-20 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1de92fc0-b725-3e12-8c0f-a4ad91ea0509 | -7.66674 | -49.5022 | 2026-09-15 04:34:00 | NOAA-20 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 16b2edcf-bce0-346b-acb0-d1c9e03c39dd | -10.95207 | -49.63607 | 2026-09-15 04:34:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 42ce1c33-dc5b-370a-8de8-03d48252c2fc | -15.04447 | -48.55476 | 2026-09-15 04:34:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d970cd86-59d3-3f39-a0ee-8a77ca19021d | -13.57442 | -47.90777 | 2026-09-15 04:34:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 34befaf3-f8b9-3cd1-bd21-04f19595805d | -11.88371 | -43.82566 | 2026-09-15 04:34:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 62.1 |
| 2d593816-1e63-3610-aa1d-6def21e9a317 | -13.57078 | -51.44908 | 2026-09-15 04:34:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 1523060d-fcb7-37b1-b860-9fa76a8d603c | -8.79521 | -45.90959 | 2026-09-15 04:34:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9e41c9a7-628d-3408-a459-e67ed2313757 | -9.45426 | -48.90966 | 2026-09-15 04:34:00 | NOAA-20 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| f04f3afb-7491-3481-9465-5bb70ec10652 | -15.07539 | -48.55265 | 2026-09-15 04:34:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 8d1e27cf-9cfb-3ea5-9ce6-99c656c39aa9 | -13.29428 | -51.29197 | 2026-09-15 04:34:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 73470a0c-e36c-39aa-89ae-0b6d504aaf91 | -14.19867 | -47.43267 | 2026-09-15 04:34:00 | NOAA-20 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 27b19c12-bd17-3b89-923b-d0c58c6a4f7d | -9.41641 | -50.1015 | 2026-09-15 04:34:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 22.8 |
| ed0d10be-80b3-3031-ae39-0ebcfd114fb1 | -11.79623 | -46.59818 | 2026-09-15 04:34:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b8f1bc19-4d14-3b5e-827e-dbbef0226c72 | -12.11934 | -44.20624 | 2026-09-15 04:34:00 | NOAA-20 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 135d096e-77fe-33f5-aac8-7e64b739c414 | -13.63572 | -47.88537 | 2026-09-15 04:34:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ae566cc6-ba1b-33ed-9ed8-e26a5ca25b1c | -13.77017 | -48.81309 | 2026-09-15 04:34:00 | NOAA-20 | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4f87155a-4627-3e55-917e-60848318641c | -15.046 | -48.58793 | 2026-09-15 04:34:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b1ae545e-b509-39c3-9505-c5d51f09469f | -15.03574 | -48.5239 | 2026-09-15 04:34:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3a8c6e51-48dc-32a0-8325-053830043aaf | -13.35639 | -51.71357 | 2026-09-15 04:34:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e5a6307e-4cc0-3ef2-bcde-eb59374917b2 | -9.13617 | -51.58489 | 2026-09-15 04:34:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2b6b06b5-e8ea-30bd-b9a8-209d650d4cab | -14.96089 | -47.52865 | 2026-09-15 04:34:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 90f60d43-8718-3b54-87c5-df031a31d7e4 | -11.77301 | -47.42365 | 2026-09-15 04:34:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c4523854-45aa-307d-b9f8-75575c800335 | -9.25701 | -48.54436 | 2026-09-15 04:34:00 | NOAA-20 | RIO DOS BOIS | TOCANTINS | Brasil | 1718709 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 22e15b0e-52c1-3e2c-89c0-3d0d11ffef77 | -9.41709 | -50.0974 | 2026-09-15 04:34:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 28.4 |
| 2790a06c-b81b-3423-9516-cdc7f2b0e174 | -13.39863 | -57.02628 | 2026-09-15 04:34:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6561a968-ab7c-389c-b157-82771463344a | -10.63178 | -48.71976 | 2026-09-15 04:34:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 44d59b84-81d5-3959-91cd-19986e1fe67f | -12.03096 | -47.81121 | 2026-09-15 04:34:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ae909da2-1210-33f4-b1ec-418737af6ae1 | -15.53915 | -41.78535 | 2026-09-15 04:34:00 | NOAA-20 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| 0fa9b762-ac79-3004-993c-71b9bd598652 | -15.98783 | -43.27792 | 2026-09-15 04:34:00 | NOAA-20 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 5fdfeb1d-4397-3c17-a999-fae2b9ab4e8c | -9.45654 | -56.70504 | 2026-09-15 04:34:00 | NOAA-20 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7111ccf4-2372-31e3-a400-ff3234081be3 | -8.80246 | -45.90711 | 2026-09-15 04:34:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ff435231-85d3-3f67-90ef-2b86bf100afd | -9.41285 | -50.10089 | 2026-09-15 04:34:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 22.8 |
| 8ec69721-fd7d-3ddd-bfec-394d46a2aa39 | -14.20701 | -47.42291 | 2026-09-15 04:34:00 | NOAA-20 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 12.9 |
| ccbd7fdf-6a17-38c6-add0-c25491149c5b | -15.59081 | -42.5699 | 2026-09-15 04:34:00 | NOAA-20 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 33.7 |
| 8661241a-27b1-3ef2-9c81-5ef4525762bb | -11.32862 | -47.67862 | 2026-09-15 04:34:00 | NOAA-20 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d7fccefb-390c-3acb-b431-72acb318ffa6 | -10.30704 | -45.30396 | 2026-09-15 04:34:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f1a48da4-9422-3bc0-b21a-764dac7f4bae | -10.6593 | -58.76473 | 2026-09-15 04:34:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2e8c8d3a-cec3-3bbc-93df-b13f5007e5b3 | -10.89913 | -51.56329 | 2026-09-15 04:34:00 | NOAA-20 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| f59eb436-bd8f-314a-ab83-c3d155578f94 | -15.05497 | -48.55286 | 2026-09-15 04:34:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 128b81cc-3afd-3e21-8a92-554dc08cb28a | -9.41149 | -50.10909 | 2026-09-15 04:34:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 32ec7911-37b1-3779-9a20-20c44d808ef1 | -11.24711 | -43.4487 | 2026-09-15 04:34:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 849b65e0-de04-3b72-9a1e-8f44ad21713f | -8.53989 | -54.70539 | 2026-09-15 04:34:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| fb062654-ba36-3422-9401-ce1436b6fa5d | -9.16188 | -49.99397 | 2026-09-15 04:34:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 22d9b751-b781-35bf-a7a1-563d7e315f93 | -10.99047 | -48.32784 | 2026-09-15 04:34:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5e0a7eb3-dc82-3815-8a3d-d71f74d56e55 | -9.45486 | -48.90602 | 2026-09-15 04:34:00 | NOAA-20 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 70febb23-653e-34d8-87fb-6542a535b7aa | -9.35983 | -50.17639 | 2026-09-15 04:34:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4fe0dd30-09c0-344e-a311-3c83e3afd5bc | -9.31668 | -44.35371 | 2026-09-15 04:34:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3eb02894-44e5-3c1b-a997-90a604d6fb26 | -10.88908 | -47.79412 | 2026-09-15 04:34:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6ea5be52-1dad-360c-b48d-a3c5241f0278 | -11.81129 | -46.58949 | 2026-09-15 04:34:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |


[Clique aqui para ver as próximas entradas](README49.md)
