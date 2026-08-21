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

## Dados Diários - Página 53

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| eb4b7e7a-a65b-3c16-a933-d48303f936cb | -19.86284 | -45.52791 | 2026-08-21 04:51:00 | NOAA-21 | LAGOA DA PRATA | MINAS GERAIS | Brasil | 3137205 | 31 | 33 | nan | nan | nan | Cerrado | 4.4 |
| a21e010c-bbdb-3c70-97c6-d389a9e306bd | -19.76024 | -57.98319 | 2026-08-21 04:51:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.5 |
| ccff150a-438e-3e53-8b66-f0f64abc49fd | -21.57533 | -43.47896 | 2026-08-21 04:51:00 | NOAA-21 | JUIZ DE FORA | MINAS GERAIS | Brasil | 3136702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| aa8e34cf-9288-321e-8734-22fcc0e55bb0 | -21.74459 | -48.56089 | 2026-08-21 04:51:00 | NOAA-21 | NOVA EUROPA | SÃO PAULO | Brasil | 3532900 | 35 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0299922b-ede0-3e18-970d-f9cac067fa65 | -20.31093 | -47.21505 | 2026-08-21 04:51:00 | NOAA-21 | CLARAVAL | MINAS GERAIS | Brasil | 3116407 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0800791f-00eb-3ffd-8000-5906b33a0c8e | -19.68509 | -42.06776 | 2026-08-21 04:51:00 | NOAA-21 | UBAPORANGA | MINAS GERAIS | Brasil | 3170057 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 01a13fb9-d587-39e1-896e-9d30f171df25 | -19.74555 | -57.98032 | 2026-08-21 04:51:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 48f116c4-f629-3ffc-9de6-c29cd5c0c52f | -17.95862 | -49.37616 | 2026-08-21 04:51:00 | NOAA-21 | GOIATUBA | GOIÁS | Brasil | 5209101 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 3ab2592a-d5bc-3c0e-81d3-7d224140a48f | -23.53822 | -47.31885 | 2026-08-21 04:51:00 | NOAA-21 | SOROCABA | SÃO PAULO | Brasil | 3552205 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 6a9172bc-1f55-3dd9-86da-8960186e91e2 | -19.73627 | -57.95231 | 2026-08-21 04:51:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 9963f2f3-1e39-3838-b6e8-4bc128f87ab7 | -19.73914 | -57.9576 | 2026-08-21 04:51:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| cca9d171-57b9-3351-8c16-6d787e75e356 | -19.74121 | -57.96747 | 2026-08-21 04:51:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.5 |
| 109957a3-86cf-39fd-a824-374943c3c6a9 | -20.7523 | -51.6661 | 2026-08-21 04:51:00 | NOAA-21 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 8a099ed2-bb92-38bb-8773-7d0db5400dd1 | -20.26038 | -46.76117 | 2026-08-21 04:51:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 911f34ac-76dd-393d-846a-330da17f1ad6 | -20.68454 | -45.26821 | 2026-08-21 04:51:00 | NOAA-21 | CANDEIAS | MINAS GERAIS | Brasil | 3112000 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 39e501eb-f233-384f-82f1-098d79eaff5d | -20.32079 | -42.74443 | 2026-08-21 04:51:00 | NOAA-21 | URUCÂNIA | MINAS GERAIS | Brasil | 3170503 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 973a8264-a936-3e42-a904-b893a3c70ade | -17.96308 | -49.37212 | 2026-08-21 04:51:00 | NOAA-21 | GOIATUBA | GOIÁS | Brasil | 5209101 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 97afb64a-9120-3479-8f9a-3273c0b607c0 | -19.74328 | -57.97735 | 2026-08-21 04:51:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 32e7a1e9-f718-3ad3-baf0-63a607dba4b5 | -19.74923 | -57.98103 | 2026-08-21 04:51:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 686c6e46-1a8b-3128-864e-312dc9e35ddd | -19.85321 | -43.87399 | 2026-08-21 04:51:00 | NOAA-21 | BELO HORIZONTE | MINAS GERAIS | Brasil | 3106200 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 6b658f6d-24c7-3ba3-9b4e-7db4b7c7675a | -19.66409 | -46.05168 | 2026-08-21 04:51:00 | NOAA-21 | CÓRREGO DANTA | MINAS GERAIS | Brasil | 3119807 | 31 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 9d67a06b-4e56-3bf8-9697-7cc1bb9ac406 | -18.03645 | -46.47013 | 2026-08-21 04:51:00 | NOAA-21 | PRESIDENTE OLEGÁRIO | MINAS GERAIS | Brasil | 3153400 | 31 | 33 | nan | nan | nan | Cerrado | 4.0 |
| df62ac9b-679a-3f68-b276-7334a40683f9 | -17.96244 | -49.37694 | 2026-08-21 04:51:00 | NOAA-21 | GOIATUBA | GOIÁS | Brasil | 5209101 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 016502a5-7dac-3f79-b960-35a2f5ce940b | -19.93275 | -46.08995 | 2026-08-21 04:51:00 | NOAA-21 | TAPIRAÍ | MINAS GERAIS | Brasil | 3168200 | 31 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 2e4e1928-feca-3fd3-9d30-40c24a82859b | -22.2944 | -51.8356 | 2026-08-21 04:51:00 | NOAA-21 | MIRANTE DO PARANAPANEMA | SÃO PAULO | Brasil | 3530201 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| 410593ec-3339-3109-a5c9-09d8629b93c6 | -18.9803 | -47.03277 | 2026-08-21 04:51:00 | NOAA-21 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 812da58e-35a4-32d3-98a9-1a3ae66e68f2 | -24.77328 | -49.53806 | 2026-08-21 04:51:00 | NOAA-21 | CERRO AZUL | PARANÁ | Brasil | 4105201 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| cd834e67-65cf-33ed-976b-1853bb552481 | -21.57994 | -43.47794 | 2026-08-21 04:51:00 | NOAA-21 | JUIZ DE FORA | MINAS GERAIS | Brasil | 3136702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 4582cb7a-a7fd-3396-9ca3-f8813d2a54ff | -19.73594 | -57.97591 | 2026-08-21 04:51:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.6 |
| eb33cd8b-1415-30a6-92be-4c1c8a67b5e7 | -17.35214 | -52.0548 | 2026-08-21 04:51:00 | NOAA-21 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d426a28c-0b06-36b0-b07d-6463318adafd | -22.37954 | -43.022 | 2026-08-21 04:51:00 | NOAA-21 | TERESÓPOLIS | RIO DE JANEIRO | Brasil | 3305802 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 226abd54-3554-3145-bf3c-37ccecc811e9 | -19.7529 | -57.98175 | 2026-08-21 04:51:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.8 |
| c1369ef5-a943-3e37-8985-1c541fb2fd64 | -20.67382 | -57.2008 | 2026-08-21 04:51:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| fb0203d2-ec3b-34c3-b2c6-f752c68e472c | -19.93087 | -46.08963 | 2026-08-21 04:51:00 | NOAA-21 | TAPIRAÍ | MINAS GERAIS | Brasil | 3168200 | 31 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 90b860b3-8609-3ffc-b99f-3bfa6dc28d74 | -19.7302 | -57.9653 | 2026-08-21 04:51:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 20.2 |
| e447845e-d4c4-320d-8e1c-ff2a08b54dc7 | -20.95524 | -47.19908 | 2026-08-21 04:51:00 | NOAA-21 | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 2a0bd124-2a9d-39c4-b5f9-f93fc7b4657f | -21.58121 | -43.47958 | 2026-08-21 04:51:00 | NOAA-21 | JUIZ DE FORA | MINAS GERAIS | Brasil | 3136702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 7a31a6f8-a8c9-3e72-a23c-b62fd4d4c596 | -19.72653 | -57.96458 | 2026-08-21 04:51:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.0 |
| c88323fb-fb77-32c0-99fa-d3dc7fab2d93 | -23.53209 | -47.31739 | 2026-08-21 04:51:00 | NOAA-21 | SOROCABA | SÃO PAULO | Brasil | 3552205 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| ad0e3d7e-9aec-30c1-9cce-b4308899e4c9 | -20.20481 | -41.56758 | 2026-08-21 04:51:00 | NOAA-21 | LAJINHA | MINAS GERAIS | Brasil | 3137700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 0f230a43-24cc-3f49-94b1-f4bf6d3e5706 | -17.95925 | -49.37137 | 2026-08-21 04:51:00 | NOAA-21 | GOIATUBA | GOIÁS | Brasil | 5209101 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| b2e415c3-37a2-3d14-8c52-98f205401426 | -18.55013 | -48.21363 | 2026-08-21 04:51:00 | NOAA-21 | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d11254e5-37eb-3b66-b6f3-68e31f50d957 | -20.67031 | -57.20014 | 2026-08-21 04:51:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 05397480-c2d4-31fe-83c3-f1b1598df1ce | -19.67022 | -46.04085 | 2026-08-21 04:51:00 | NOAA-21 | CÓRREGO DANTA | MINAS GERAIS | Brasil | 3119807 | 31 | 33 | nan | nan | nan | Cerrado | 6.4 |
| eb053989-6bff-38b6-88db-beb5206bf0ba | -17.78898 | -49.20499 | 2026-08-21 04:51:00 | NOAA-21 | MORRINHOS | GOIÁS | Brasil | 5213806 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ba97fba0-21f4-380a-8928-90cb59821d37 | -19.86252 | -45.5309 | 2026-08-21 04:51:00 | NOAA-21 | LAGOA DA PRATA | MINAS GERAIS | Brasil | 3137205 | 31 | 33 | nan | nan | nan | Cerrado | 7.6 |
| adeb9c4e-afb5-3de7-b55e-705ccb9f9ae4 | -19.68736 | -42.06849 | 2026-08-21 04:51:00 | NOAA-21 | UBAPORANGA | MINAS GERAIS | Brasil | 3170057 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| 3171d639-d1bf-3019-a318-91c11d98503b | -19.85512 | -43.87702 | 2026-08-21 04:51:00 | NOAA-21 | BELO HORIZONTE | MINAS GERAIS | Brasil | 3106200 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.1 |
| f86a5b66-bf0c-38c9-825d-6b59191acb18 | -19.06986 | -57.37258 | 2026-08-21 04:51:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| f7c7ba28-3456-3a40-8b31-bf1093ae1e1c | -20.43647 | -46.49313 | 2026-08-21 04:51:00 | NOAA-21 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e17d9782-bf66-3bc0-a449-9e5cc70e4daf | -23.53678 | -47.31815 | 2026-08-21 04:51:00 | NOAA-21 | SOROCABA | SÃO PAULO | Brasil | 3552205 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| 91d6d6e6-4ba7-3fe4-bd41-39931d5b1bf3 | -20.26088 | -46.75678 | 2026-08-21 04:51:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c5d4ddc1-4997-33af-990f-91a1b5e9758d | -20.25831 | -46.73756 | 2026-08-21 04:51:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9b835a1b-7d8b-332d-9a8c-220753a6e1ee | -18.6983 | -47.47188 | 2026-08-21 04:51:00 | NOAA-21 | MONTE CARMELO | MINAS GERAIS | Brasil | 3143104 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 02338a54-a6bb-3f33-8a23-c167b5c92522 | -19.66472 | -46.04592 | 2026-08-21 04:51:00 | NOAA-21 | CÓRREGO DANTA | MINAS GERAIS | Brasil | 3119807 | 31 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 52069414-ddf5-3353-a0c0-19a8daf4c785 | -19.7543 | -57.97952 | 2026-08-21 04:51:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 5edec68f-452d-3f60-9af5-792dd93799c6 | -20.68485 | -45.26505 | 2026-08-21 04:51:00 | NOAA-21 | CANDEIAS | MINAS GERAIS | Brasil | 3112000 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| a8019a1e-6334-3fd0-86ba-083682034e4d | -20.65651 | -46.19476 | 2026-08-21 04:51:00 | NOAA-21 | CAPITÓLIO | MINAS GERAIS | Brasil | 3112802 | 31 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 1622c00e-f405-3d45-a704-b6fc05c2888b | -23.53353 | -47.31804 | 2026-08-21 04:51:00 | NOAA-21 | SOROCABA | SÃO PAULO | Brasil | 3552205 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| ef3fa949-554e-3013-a3ad-81efb783c7e9 | -17.99506 | -49.39693 | 2026-08-21 04:51:00 | NOAA-21 | GOIATUBA | GOIÁS | Brasil | 5209101 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 79ad29d2-6047-384b-84d0-8bc3b92cf1e7 | -19.73961 | -57.97663 | 2026-08-21 04:51:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 010a5838-1268-3961-a5dc-40eadaa9ef19 | -22.62457 | -54.99844 | 2026-08-21 04:51:00 | NOAA-21 | CAARAPÓ | MATO GROSSO DO SUL | Brasil | 5002407 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 35a72b19-4269-361c-9aaf-273cca392c8b | -22.62126 | -54.99784 | 2026-08-21 04:51:00 | NOAA-21 | CAARAPÓ | MATO GROSSO DO SUL | Brasil | 5002407 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 8cd56971-b19f-3020-bfa6-97e7cabc284c | -20.05059 | -45.62257 | 2026-08-21 04:51:00 | NOAA-21 | LUZ | MINAS GERAIS | Brasil | 3138807 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e29366e2-1018-33d6-b40b-52d7769e72cc | -19.85282 | -43.8782 | 2026-08-21 04:51:00 | NOAA-21 | BELO HORIZONTE | MINAS GERAIS | Brasil | 3106200 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 6f6fe10f-dcb0-3c07-bc49-4531bcdb8dfa | -19.68471 | -42.07222 | 2026-08-21 04:51:00 | NOAA-21 | UBAPORANGA | MINAS GERAIS | Brasil | 3170057 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 7ae80700-100e-3d35-a843-b81b807324ea | -18.03241 | -46.46451 | 2026-08-21 04:51:00 | NOAA-21 | PRESIDENTE OLEGÁRIO | MINAS GERAIS | Brasil | 3153400 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c4746468-7358-37c7-8e84-c78beb3ab2ce | -21.32731 | -43.81008 | 2026-08-21 04:51:00 | NOAA-21 | ANTÔNIO CARLOS | MINAS GERAIS | Brasil | 3102902 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 78d77416-f530-3d6e-b5f0-42184179e191 | -20.75265 | -51.66374 | 2026-08-21 04:51:00 | NOAA-21 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 2992d204-2f21-30dc-9691-a32f56ba1ae3 | -20.65706 | -46.18945 | 2026-08-21 04:51:00 | NOAA-21 | CAPITÓLIO | MINAS GERAIS | Brasil | 3112802 | 31 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 6df6f68f-6994-3d08-a661-acfdbfbfcaf4 | -19.73387 | -57.96603 | 2026-08-21 04:51:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 20.2 |
| a483d80c-7abc-3ae1-a9c7-728c40861c79 | -20.83287 | -44.19559 | 2026-08-21 04:51:00 | NOAA-21 | RESENDE COSTA | MINAS GERAIS | Brasil | 3154200 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 97c42528-1b5a-3f43-833e-0929a5bffa1a | -21.50019 | -44.86006 | 2026-08-21 04:51:00 | NOAA-21 | INGAÍ | MINAS GERAIS | Brasil | 3130804 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 2bb5085b-4baf-3650-932e-c995fc2979d1 | -20.25616 | -46.75646 | 2026-08-21 04:51:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 858ab1d6-42c4-3392-8900-6be16e7b8141 | -19.73307 | -57.97061 | 2026-08-21 04:51:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 15.9 |
| d1bc16f5-14a7-3fcc-bf5b-14c5e39738ac | -20.1983 | -41.56717 | 2026-08-21 04:51:00 | NOAA-21 | LAJINHA | MINAS GERAIS | Brasil | 3137700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| b78ca816-9853-3c63-a8d1-608b9f5243a9 | -19.74695 | -57.97807 | 2026-08-21 04:51:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| f36f6260-b457-3b34-954e-422d73084a52 | -20.83326 | -44.19154 | 2026-08-21 04:51:00 | NOAA-21 | LAGOA DOURADA | MINAS GERAIS | Brasil | 3137403 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| a73f96f2-1092-3d2a-bf58-53d390f3e89d | -27.24152 | -48.77942 | 2026-08-21 04:53:00 | NOAA-21 | CANELINHA | SANTA CATARINA | Brasil | 4203709 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| a38e7013-4fa8-3577-94b3-979095e319f2 | -3.5407 | -48.1673 | 2026-08-21 05:00:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 49.8 |
| c6f63a68-6b94-3225-9613-8f4a05e23324 | -7.3603 | -45.8136 | 2026-08-21 05:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 115.0 |
| 33e7ca91-89e8-30e5-a399-24cd8b006c62 | -9.4071 | -60.417 | 2026-08-21 05:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 293.8 |
| 5a3d5d31-3cff-3dc0-abf1-b520cbd049ea | -13.3734 | -54.3779 | 2026-08-21 05:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 158.2 |
| fd46ed04-09f0-362f-998c-79edf4078f7b | -13.3923 | -54.3965 | 2026-08-21 05:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 72.1 |
| 0c03e963-9aa9-3d91-8167-24b012e18402 | -9.4257 | -60.416 | 2026-08-21 05:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 88.0 |
| d85481de-77af-3efc-aaf9-fabb1af9ac14 | -11.1747 | -54.0216 | 2026-08-21 05:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 66.9 |
| bee2fa90-bff8-3e1c-a7c9-597838cf4c75 | -6.8756 | -59.4171 | 2026-08-21 05:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 55.0 |
| 68b317d5-3e62-3c1e-b8bb-540b61da7dc4 | -7.3791 | -45.8119 | 2026-08-21 05:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 77.6 |
| c76922ef-8c29-3816-8650-f31317d9bf48 | -8.3718 | -62.697 | 2026-08-21 05:00:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 48.3 |
| aa058193-1776-32e5-8547-014573fbfc11 | -13.3926 | -54.3758 | 2026-08-21 05:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 275.5 |
| 3a3acdd4-1846-32db-b19c-d109b23f5d41 | -9.4069 | -60.4362 | 2026-08-21 05:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 77.3 |
| 75cffd24-42d5-3b1b-8aee-a48f97aec892 | -6.8755 | -59.4364 | 2026-08-21 05:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 69.0 |
| 96d80d63-2a0b-391f-9395-e3178eedb492 | -13.3929 | -54.3551 | 2026-08-21 05:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 126.5 |
| 65b26978-5e94-39c4-b5a2-9d0b00e81c6a | -13.4117 | -54.3737 | 2026-08-21 05:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 69.8 |
| b372ca10-8397-3f6b-8d42-ad9ad6d8ecbc | -8.3903 | -62.6963 | 2026-08-21 05:00:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 43.9 |
| 4d7cffb7-71c7-3399-a881-dbfd2ee18502 | -6.8939 | -59.4356 | 2026-08-21 05:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 45.7 |
| e32a6742-8167-373e-9d18-3755988f5028 | -13.3737 | -54.3572 | 2026-08-21 05:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 80.5 |
| c8937db3-56ab-3a5f-b381-d279500ce3f2 | -9.4259 | -60.3967 | 2026-08-21 05:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 63.5 |
| ff650169-27a7-3239-98e4-37a83790acda | -9.4072 | -60.3977 | 2026-08-21 05:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 177.1 |
| aa66300d-3b7e-36ba-a6f0-bac397a273fd | -6.2341 | -55.6109 | 2026-08-21 05:00:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 100.7 |


[Clique aqui para ver as próximas entradas](README54.md)
