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

## Dados Diários - Página 28

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3226b244-1f9a-3eba-9615-c47fba7c16ab | -8.46736 | -54.67552 | 2026-09-03 04:40:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| a31826d2-c148-3c4e-857f-a2b93d70aefa | -9.62929 | -54.31196 | 2026-09-03 04:40:00 | NPP-375D | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 40c8cdbc-c81f-3fcd-8a7e-7798157fcc38 | -10.74458 | -50.61701 | 2026-09-03 04:40:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8c017219-18ad-381f-9ff7-7266112fcee0 | -12.09388 | -47.06114 | 2026-09-03 04:40:00 | NPP-375D | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| ab959d1f-e26d-3b07-aff0-65ca85db1298 | -10.99472 | -45.08693 | 2026-09-03 04:40:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 14.8 |
| f199aa63-e003-3710-8cee-82aba4f9dab9 | -11.3138 | -50.52225 | 2026-09-03 04:40:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 60aed657-d2eb-3a25-a1de-b430d88370ce | -11.30302 | -50.52037 | 2026-09-03 04:40:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 13.9 |
| 2c4c756b-0dbc-3413-beda-02709ab2889c | -9.61033 | -48.56198 | 2026-09-03 04:40:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 32dd7401-5959-35e3-a332-6ee4c71fdd41 | -10.56056 | -47.72378 | 2026-09-03 04:40:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| caa62994-d834-3ad7-b5d8-94b9229ecef9 | -10.24318 | -47.76292 | 2026-09-03 04:40:00 | NPP-375D | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d4a4f89e-b8a0-3435-930f-0e5f838ae3dd | -11.33327 | -50.53852 | 2026-09-03 04:40:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 4d4c9861-3588-38d7-b191-5db4ee7a0e0a | -12.16976 | -47.06926 | 2026-09-03 04:40:00 | NPP-375D | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ccbc9994-059c-3e5d-a992-07396233e378 | -10.34298 | -49.95811 | 2026-09-03 04:40:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a6035e60-0dc3-36f2-b83b-574653fb8dd9 | -8.46925 | -54.64914 | 2026-09-03 04:40:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 12fdbafd-9f36-3ac1-be4d-5f1fe08f7a10 | -10.89368 | -45.32067 | 2026-09-03 04:40:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 89e90b7d-cbdc-3022-b32f-63eee2f9bf08 | -11.28759 | -45.17766 | 2026-09-03 04:40:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 24b9749f-5117-3a94-8cb6-d6c66795ec8a | -8.46437 | -54.64836 | 2026-09-03 04:40:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 2e2dbff0-d777-355e-85fa-b8a4055f28cc | -12.40282 | -44.81402 | 2026-09-03 04:40:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e84c5727-2251-3865-b88d-34ca60a09196 | -8.47205 | -54.6488 | 2026-09-03 04:40:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 4b736768-7489-3a3a-b383-85e81a2e3ea7 | -11.33038 | -50.53372 | 2026-09-03 04:40:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| cf119f6c-344d-3ba9-95ea-e642ce7210f4 | -11.77825 | -48.84298 | 2026-09-03 04:40:00 | NPP-375D | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 32ba3789-b6e5-39fb-a91f-d54eee215641 | -12.39985 | -44.80933 | 2026-09-03 04:40:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 23ebe8c5-9762-30f8-9761-dfc909d01baf | -13.58502 | -47.87764 | 2026-09-03 04:40:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 03ee6fa4-994f-3a46-a28c-cb519fa29c35 | -10.28065 | -50.04719 | 2026-09-03 04:40:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8a0a5b12-9763-33aa-af1a-18edb6fa0a1c | -10.88795 | -45.31198 | 2026-09-03 04:40:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 4722c59f-26b8-3706-9aeb-4c5762980d7b | -11.29942 | -50.51974 | 2026-09-03 04:40:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 94dc7f19-417d-37db-b63f-585412ae5178 | -13.78525 | -49.72762 | 2026-09-03 04:40:00 | NPP-375D | AMARALINA | GOIÁS | Brasil | 5200829 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b1816c97-97e9-3b00-9579-3aeca36d8a47 | -10.89596 | -45.32886 | 2026-09-03 04:40:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3282c773-a5bb-3417-a8c8-f13f50d1f36c | -8.46729 | -54.65984 | 2026-09-03 04:40:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 27aff739-ca68-3053-b005-0a7f93f7ef54 | -12.14534 | -47.13812 | 2026-09-03 04:40:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| bec0ec44-7c61-35af-9202-d146c5d02419 | -9.97315 | -46.452 | 2026-09-03 04:40:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d8a303f0-75ef-3b00-8de7-404a981ad690 | -15.8948 | -47.67972 | 2026-09-03 04:40:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 378ffcbd-9067-38b7-945f-36d0a46114b7 | -11.33617 | -50.54332 | 2026-09-03 04:40:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| a1ddd705-0885-37b8-b939-93d4c703af16 | -10.48898 | -48.64524 | 2026-09-03 04:40:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 609dbe8e-f354-3b7e-841c-1f656ae59540 | -10.89023 | -45.32015 | 2026-09-03 04:40:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3bb5d7b1-5915-301e-baf2-b1f8c464610b | -10.87468 | -45.32941 | 2026-09-03 04:40:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 4ab5c2d9-4175-3823-83cc-0cd2609e4cef | -11.29166 | -45.17424 | 2026-09-03 04:40:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| f4b1afda-9a4c-37d7-902d-fa7223d3e347 | -8.44505 | -54.745 | 2026-09-03 04:40:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| dddf5271-8bc8-387c-b946-aa6e4929a0a6 | -9.70343 | -57.88626 | 2026-09-03 04:40:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b5fb352a-3689-3df5-9e3f-5dfe39805a51 | -11.3174 | -50.52287 | 2026-09-03 04:40:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 9d2c32b1-7607-3a28-b7d3-ba28ab9f4263 | -10.48408 | -51.32792 | 2026-09-03 04:40:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 88b00e41-d043-39ac-9c57-47457e6cd04c | -13.39205 | -51.35893 | 2026-09-03 04:40:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f52b98af-d3e4-3739-846b-91508d938896 | -11.3173 | -45.12251 | 2026-09-03 04:40:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 4e665702-c69f-30e1-a586-55be7c4232ff | -15.68384 | -45.90072 | 2026-09-03 04:40:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f88242d9-030a-3042-8295-a80207772c90 | -16.54194 | -49.56646 | 2026-09-03 04:40:00 | NPP-375D | TRINDADE | GOIÁS | Brasil | 5221403 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| afc55168-fa0e-3a1d-bdb6-69764764a529 | -12.09054 | -47.06059 | 2026-09-03 04:40:00 | NPP-375D | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 50a37ab0-5d6b-3983-a443-ee3ffc2058d0 | -11.28883 | -45.12179 | 2026-09-03 04:40:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 82fae3d2-970d-3b0c-b513-54a73612dad6 | -16.51817 | -47.73214 | 2026-09-03 04:40:00 | NPP-375D | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 771c319a-6698-3d5f-9880-72e692bd05c5 | -10.56558 | -47.71378 | 2026-09-03 04:40:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 3ffa670c-a65a-3796-97b2-066fbbc85e1e | -12.08888 | -47.07125 | 2026-09-03 04:40:00 | NPP-375D | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4e4a2fa2-7042-3698-9ebb-4a98d35520a8 | -11.24293 | -45.16642 | 2026-09-03 04:40:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 88ce4dc1-33b8-365f-ad88-6054ea909182 | -10.87472 | -45.30606 | 2026-09-03 04:40:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 2ba35489-ad8c-30fa-8fa6-c8bbdc742818 | -11.31599 | -50.53121 | 2026-09-03 04:40:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 13.5 |
| 8eeb0511-09db-31aa-8630-7f7c360fe7a9 | -11.31669 | -50.52704 | 2026-09-03 04:40:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 13.5 |
| a40bbfb4-6a03-3bc2-9dc1-9aed466287c4 | -15.67854 | -45.88749 | 2026-09-03 04:40:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c2fb42d7-0285-3631-98c7-fc6a42bbc4cd | -12.10444 | -47.0592 | 2026-09-03 04:40:00 | NPP-375D | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3f9e53f8-6b13-3376-ab17-70925a1b8056 | -10.91648 | -45.34678 | 2026-09-03 04:40:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| bf9d1074-d924-3078-860f-25b3f36ed2d9 | -11.33473 | -45.12537 | 2026-09-03 04:40:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a9c19955-b706-3a04-a430-9c6ca271863b | -13.38472 | -51.38004 | 2026-09-03 04:40:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 7.0 |
| c9a45f3e-a649-354c-9705-ce381a1b7870 | -13.37088 | -51.35059 | 2026-09-03 04:40:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6e5b61db-2a5f-3fea-a2fe-3d0727d2b9ba | -11.33547 | -50.5475 | 2026-09-03 04:40:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 3db8fe75-8a06-3c2d-b0df-880523c472c5 | -11.27831 | -45.16819 | 2026-09-03 04:40:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 222da883-b95a-375a-9e73-49ec9d17f815 | -14.95859 | -48.08828 | 2026-09-03 04:40:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3f8d035b-742d-3a33-9bca-e4bf7af79ee5 | -15.53458 | -45.91395 | 2026-09-03 04:40:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6f55f314-7ef0-3fc5-be26-471a0a21856f | -11.69076 | -46.7343 | 2026-09-03 04:40:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2ff07ccd-e791-31fa-9e59-0dbba10b3552 | -14.05223 | -48.40717 | 2026-09-03 04:40:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d9af69f7-75d4-355c-b68c-a073337f6135 | -13.58446 | -47.88118 | 2026-09-03 04:40:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 3c8fd88c-38a4-371b-ab24-bd24687c763b | -11.28593 | -45.11732 | 2026-09-03 04:40:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 4ec37899-87ab-39b2-b853-55788d746e13 | -13.39114 | -51.35718 | 2026-09-03 04:40:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0b69b9e9-58cf-30fe-a2d6-0ec988c8e109 | -10.99414 | -45.09082 | 2026-09-03 04:40:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 14.8 |
| eff02666-f9ca-342e-8ba7-c3c1bb6294a1 | -10.57167 | -47.71838 | 2026-09-03 04:40:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3089fc0b-370a-3d66-94f6-9cf50eeef3a6 | -11.33687 | -50.53915 | 2026-09-03 04:40:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 6a1b2af5-399e-31db-9e31-ea13bca25be0 | -10.18276 | -50.2686 | 2026-09-03 04:40:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 081ecbef-e238-3f09-8439-c98a12c2fdec | -14.0489 | -48.40661 | 2026-09-03 04:40:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e224a62d-e91c-32de-9a5c-71bd68cf5e31 | -13.41188 | -42.49107 | 2026-09-03 04:40:00 | NPP-375D | BOTUPORÃ | BAHIA | Brasil | 2904209 | 29 | 33 | nan | nan | nan | Caatinga | 5.6 |
| 0bfeaab2-a235-31c9-9d0d-ae25bfc5b61b | -9.63076 | -54.31479 | 2026-09-03 04:40:00 | NPP-375D | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 64457d4b-68fe-30bb-bea7-87a16c52ca1b | -10.35294 | -49.96395 | 2026-09-03 04:40:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 0a340b8d-476a-36cc-97c5-e1082f0b274e | -13.28435 | -48.84422 | 2026-09-03 04:40:00 | NPP-375D | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 922ef39d-2451-3429-8fd9-a8ad543ee026 | -14.21414 | -42.04301 | 2026-09-03 04:40:00 | NPP-375D | RIO DO ANTÔNIO | BAHIA | Brasil | 2926806 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 0c8d0f94-9441-3a93-b2ab-1884996607f8 | -17.63888 | -44.328 | 2026-09-03 04:40:00 | NPP-375D | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c82d86c4-fb89-3f05-bacd-bc31e97280e7 | -12.08777 | -47.0565 | 2026-09-03 04:40:00 | NPP-375D | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0f74b902-a4e6-35a3-80ab-b39a7ee1f33f | -9.62464 | -54.31102 | 2026-09-03 04:40:00 | NPP-375D | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 56ce6b3b-bb46-331d-8fc2-f3b24c68606f | -15.07994 | -51.45427 | 2026-09-03 04:40:00 | NPP-375D | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 452acc03-1027-37e7-bcd4-3fadf6b63daa | -10.98717 | -45.08972 | 2026-09-03 04:40:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 18.5 |
| 449144e8-c4f1-3ace-be29-c23fafbe1fcc | -8.46825 | -54.68197 | 2026-09-03 04:40:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 8b5fec4e-2b92-3fa1-8a9c-690c3fec2665 | -10.88567 | -45.3038 | 2026-09-03 04:40:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 38ad93df-9e56-39b6-8660-2fab0ee72244 | -10.56947 | -47.71081 | 2026-09-03 04:40:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 652e2ae2-c426-3048-8299-5d200b605f9c | -10.56445 | -47.72081 | 2026-09-03 04:40:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e21f7e8c-21ee-3af6-812a-92e18c825f09 | -10.87817 | -45.30658 | 2026-09-03 04:40:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.0 |
| f0a74204-1508-3b74-8378-8a6b3df40e56 | -16.32627 | -49.45473 | 2026-09-03 04:40:00 | NPP-375D | INHUMAS | GOIÁS | Brasil | 5210000 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 3cf33937-edae-3342-b609-d33417643b43 | -11.31889 | -50.53601 | 2026-09-03 04:40:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 7.0 |
| ffb8202a-f709-3d7c-841e-07bc05c94d4e | -10.99531 | -45.08303 | 2026-09-03 04:40:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 0d6b04c3-a7b7-348d-9f88-a497abfd24c3 | -12.4076 | -44.80635 | 2026-09-03 04:40:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| dc3eddac-b932-3062-9ac8-39871a47f9b8 | -11.31021 | -50.52162 | 2026-09-03 04:40:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| c2182178-60ae-3b67-8cd0-4f39a9a8e907 | -10.28352 | -50.05185 | 2026-09-03 04:40:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ea9dcd42-0d7a-3b3b-85a6-e121a689ea69 | -12.39925 | -44.81344 | 2026-09-03 04:40:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 3894dade-ec72-3fc1-b118-500ddcb72a6d | -12.0761 | -47.06555 | 2026-09-03 04:40:00 | NPP-375D | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 93f9bd20-40d8-30c4-b916-566838e7b8a7 | -8.46644 | -54.68078 | 2026-09-03 04:40:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 6c07bd98-dfc7-314b-97b3-a439b7ba40b8 | -12.08943 | -47.0677 | 2026-09-03 04:40:00 | NPP-375D | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 62153146-a520-3bce-b6e2-29765abd4bd3 | -10.57279 | -47.71135 | 2026-09-03 04:40:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |


[Clique aqui para ver as próximas entradas](README29.md)
