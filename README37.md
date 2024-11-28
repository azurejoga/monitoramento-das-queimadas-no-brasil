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

## Dados Diários - Página 37

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| dc995f64-6191-3cd1-af20-776d363468c8 | -2.74122 | -46.11581 | 2024-11-28 03:59:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 85602658-9ad4-314f-b6df-e04b5034d08a | -1.32295 | -51.9339 | 2024-11-28 03:59:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| fbcd7014-5d49-376e-8377-a8f4f8106c30 | -3.5122 | -50.31374 | 2024-11-28 03:59:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 42121495-3ab3-3f61-a86e-a0aaa2e02249 | -3.08594 | -41.13925 | 2024-11-28 03:59:00 | NPP-375D | BARROQUINHA | CEARÁ | Brasil | 2302057 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| f20b1e58-c4c3-37ce-ac89-276ad0dc64c4 | -1.67144 | -52.48982 | 2024-11-28 03:59:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3fbc2d7f-7845-3053-a1c1-9c41b75060f1 | -2.47488 | -47.04344 | 2024-11-28 03:59:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6fdcad20-9e5b-3c83-ae1c-d869be12bb53 | -2.18485 | -52.1326 | 2024-11-28 03:59:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2a7493ca-6b8c-3733-9f9a-92d039922d67 | -2.17078 | -52.13617 | 2024-11-28 03:59:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 5aa3b1c1-5efa-3ef3-a598-c83a4708d791 | -3.04279 | -48.5189 | 2024-11-28 03:59:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 881d2020-adfe-3a58-9a1a-20e86edd481d | -2.05443 | -47.12114 | 2024-11-28 03:59:00 | NPP-375D | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4a972b3e-7e6d-396a-9db9-705c4aeb0b22 | -2.89108 | -51.58755 | 2024-11-28 03:59:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 866c1ca2-24f5-3187-a626-070e355f8c7f | -2.87525 | -46.85275 | 2024-11-28 03:59:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| c3b611d6-7c22-3cf3-b72f-816f5cfa1df5 | -6.17363 | -42.60865 | 2024-11-28 03:59:00 | NPP-375D | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 2c258cc7-8d5b-3f97-b489-e61d416ae2e2 | -3.27251 | -50.6215 | 2024-11-28 03:59:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 23c3177f-27c2-31d5-a35a-edeaec2c1638 | -5.49376 | -47.66282 | 2024-11-28 03:59:00 | NPP-375D | SÃO MIGUEL DO TOCANTINS | TOCANTINS | Brasil | 1720200 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9f587327-d4d4-3178-ae64-ef28c95ffcfb | -3.18031 | -48.43594 | 2024-11-28 03:59:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 82cd5851-158d-3965-b2e6-e9a96770d0bd | -3.36664 | -50.827 | 2024-11-28 03:59:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 8a8c28b0-2c32-3814-a28e-df1e8cf1e0e9 | -3.98502 | -46.65281 | 2024-11-28 03:59:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 464d9277-32ef-31b9-be8e-c30181e8184e | -3.59261 | -50.69535 | 2024-11-28 03:59:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 71eaa0cb-b7d8-3c38-b7cc-97d7a69f255d | -3.77602 | -44.11133 | 2024-11-28 03:59:00 | NPP-375D | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0ebe5f8e-ace1-34e0-91c2-2cbbb4e7d6be | -4.45397 | -45.89302 | 2024-11-28 03:59:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 008a0e6b-6aeb-3ec0-ad83-d371fd24a919 | -5.98186 | -45.37996 | 2024-11-28 03:59:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 4284f612-6b5f-3b32-814b-e9a131e3896f | -3.78014 | -50.1373 | 2024-11-28 03:59:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 246657aa-d30d-35b6-b5a2-c1c425d1522c | -3.27844 | -50.61207 | 2024-11-28 03:59:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f47f0698-440e-3fa5-9e3b-decbf2720296 | -1.68449 | -52.49918 | 2024-11-28 03:59:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| b106a6ad-2660-39f8-a757-5136dc6182f5 | -5.30124 | -44.43672 | 2024-11-28 03:59:00 | NPP-375D | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 20c5e759-4ad9-38ad-88bc-c8b73e41ab1c | -3.96435 | -48.0778 | 2024-11-28 03:59:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 1743166e-c2e8-31e8-8495-e73fca2a91e2 | -4.51737 | -45.8131 | 2024-11-28 03:59:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 89d3fdef-e158-34e2-8d1b-04d3fb5becd1 | -3.69123 | -51.37177 | 2024-11-28 03:59:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 06808163-8263-3d0c-b33c-3377ae3b01a7 | -6.46411 | -39.85149 | 2024-11-28 03:59:00 | NPP-375D | SABOEIRO | CEARÁ | Brasil | 2311900 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 233d492b-a061-353d-85b6-6862fafcf8d6 | -5.08599 | -45.98352 | 2024-11-28 03:59:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c6f16db9-7337-30b6-89fd-c93160bd776f | -4.08442 | -46.14432 | 2024-11-28 03:59:00 | NPP-375D | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 48374123-c956-3430-b5a9-4bf3f1e15d7c | -4.04431 | -48.33311 | 2024-11-28 03:59:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c43edabd-0799-3553-bea7-4ff4c06f2ec3 | -2.86776 | -46.80735 | 2024-11-28 03:59:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| faac09f4-9132-31f4-a17b-b74d10e0ec43 | -4.19694 | -48.56739 | 2024-11-28 03:59:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 54d76c7e-bba9-3229-8df7-9abf7bfba838 | -3.72229 | -50.18654 | 2024-11-28 03:59:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 194734c0-8658-3a90-8557-cbc8d37e4ceb | -6.92383 | -38.14027 | 2024-11-28 03:59:00 | NPP-375D | SÃO JOSÉ DA LAGOA TAPADA | PARAÍBA | Brasil | 2514206 | 25 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 2376d63c-26f7-3287-9e58-285bac20e3c2 | -2.86764 | -46.86824 | 2024-11-28 03:59:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 3ec26d27-1be0-3c66-a2ea-ef271233f4d1 | -2.84283 | -46.83633 | 2024-11-28 03:59:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 3737d9c1-e689-38d0-aa49-d9dcfc5d65ac | -2.31063 | -47.86348 | 2024-11-28 03:59:00 | NPP-375D | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 6f27458b-daf7-3303-b773-729f3c4bd8dd | -3.46791 | -50.53714 | 2024-11-28 03:59:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| c919e2cd-239c-3d3b-b515-3ecabb33335a | -5.0922 | -45.83847 | 2024-11-28 03:59:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b1283f12-83fe-3e05-85a3-c0f50546b56d | -2.84192 | -46.84174 | 2024-11-28 03:59:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 84d0c361-b0e5-358a-9055-60b1e7a35db7 | -2.79859 | -51.58973 | 2024-11-28 03:59:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5215094a-b47c-33c3-8028-7bd38ce6dbac | -3.73797 | -51.84143 | 2024-11-28 03:59:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c01d3985-20d5-3f6c-a7e3-a477bd25c257 | -2.53682 | -47.32587 | 2024-11-28 03:59:00 | NPP-375D | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c34115f2-e2a6-37cd-9223-7bcc2c9cdfae | -4.5102 | -42.07293 | 2024-11-28 03:59:00 | NPP-375D | BOQUEIRÃO DO PIAUÍ | PIAUÍ | Brasil | 2201945 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| fde54817-2fd8-389e-ae9a-736c7da0521a | -2.8587 | -46.8484 | 2024-11-28 03:59:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| f097892e-cf90-33e3-97f1-198b44d84bfc | -4.77205 | -44.42546 | 2024-11-28 03:59:00 | NPP-375D | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| f0fa5eea-6b78-3e6d-9166-d25317766030 | -2.87264 | -46.80812 | 2024-11-28 03:59:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| b4a9c565-b67b-31e9-810f-97518264887e | -4.73966 | -46.50703 | 2024-11-28 03:59:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 6.0 |
| ff496b00-54b6-3960-9431-42e0d4970190 | -3.50612 | -50.31264 | 2024-11-28 03:59:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2d81db68-4daf-3d07-b33d-be1519f81f96 | -6.86598 | -44.76476 | 2024-11-28 03:59:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 7d1c76a0-fe47-32a5-a07e-05ea920d9704 | -2.27454 | -46.37602 | 2024-11-28 03:59:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 7a3116e9-8bb1-3f01-b5f3-cf86ea221743 | -2.84401 | -46.84607 | 2024-11-28 03:59:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 1abd40b2-ec63-3e4b-8c9d-25198ac82c34 | -3.97706 | -46.72926 | 2024-11-28 03:59:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0cf51e59-251f-3266-aaa7-d4bd8a5df6c9 | -2.85064 | -46.83601 | 2024-11-28 03:59:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a55fc21f-e92e-3550-8c9d-eceb4863c095 | -3.48277 | -49.895 | 2024-11-28 03:59:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| fbd103ca-1d03-37fa-8152-56351c91c244 | -6.92325 | -38.14398 | 2024-11-28 03:59:00 | NPP-375D | SÃO JOSÉ DA LAGOA TAPADA | PARAÍBA | Brasil | 2514206 | 25 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 2eee8f9a-1e78-3c7e-ad80-e0606d6f05da | -2.16881 | -52.1429 | 2024-11-28 03:59:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 728677d4-a576-3798-831c-3cdae29e3624 | -2.63524 | -51.77897 | 2024-11-28 03:59:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 12979079-9ae0-32d8-bb80-8a99e8943246 | -6.90156 | -38.10267 | 2024-11-28 03:59:00 | NPP-375D | SÃO JOSÉ DA LAGOA TAPADA | PARAÍBA | Brasil | 2514206 | 25 | 33 | nan | nan | nan | Caatinga | 2.3 |
| c73ccf55-8cac-3486-aae1-31d269c68050 | -2.5161 | -45.19467 | 2024-11-28 03:59:00 | NPP-375D | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 781cce94-9eb1-3113-85b8-1c42f3e75268 | -6.09431 | -41.93956 | 2024-11-28 03:59:00 | NPP-375D | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| c13fccb9-e7d9-3260-b153-b98fe3a42afb | -3.37643 | -50.11184 | 2024-11-28 03:59:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e29fa267-2d8b-3552-a626-71c4843424b0 | -1.34923 | -51.99145 | 2024-11-28 03:59:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 1b48c8a9-9a23-3d89-96e6-52e6b9e96cd4 | -3.97851 | -46.98768 | 2024-11-28 03:59:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4eef8929-9e56-3eb0-8bc4-9156a9778cda | -3.98585 | -46.64789 | 2024-11-28 03:59:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 436de5ff-667c-3985-af95-24a8540d4dea | -6.23514 | -42.98409 | 2024-11-28 03:59:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| fc270140-cde0-3f63-9c97-e1969bbc09ee | -7.31387 | -35.19196 | 2024-11-28 03:59:00 | NPP-375D | PEDRAS DE FOGO | PARAÍBA | Brasil | 2511202 | 25 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| f908bb54-363c-383a-bd54-d1b7c8344374 | -6.23084 | -42.98766 | 2024-11-28 03:59:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 81fd7d84-966e-32b0-a721-16e51154fa5b | -2.8489 | -46.84687 | 2024-11-28 03:59:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 6343445d-a9f6-3839-9e43-6af2e09f4b4b | -6.93266 | -39.25517 | 2024-11-28 03:59:00 | NPP-375D | CARIRIAÇU | CEARÁ | Brasil | 2303204 | 23 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 1249b73e-42f7-33ed-ae14-1cd1325d53e3 | -3.74123 | -51.84314 | 2024-11-28 03:59:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 14744809-23ed-35d9-a70a-0d1050d7a850 | -6.33727 | -38.45565 | 2024-11-28 03:59:00 | NPP-375D | LUÍS GOMES | RIO GRANDE DO NORTE | Brasil | 2407005 | 24 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 828618a8-b6ee-3bcb-ba07-26931019e0d9 | -3.5791 | -50.32784 | 2024-11-28 03:59:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 752979bb-190b-33f3-b338-a1abaf9d0390 | -2.77841 | -48.58149 | 2024-11-28 03:59:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| af660c50-70fa-3550-8659-e8b8ea59c341 | -4.88062 | -43.3036 | 2024-11-28 03:59:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6a4c324b-2e78-3c31-8a53-aba45c29da5e | -4.00227 | -44.27746 | 2024-11-28 03:59:00 | NPP-375D | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8dbef5f9-7050-370d-b54c-50e0631116cd | -2.05396 | -47.12407 | 2024-11-28 03:59:00 | NPP-375D | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 86f36688-fe81-3244-b820-45e685593cd4 | -3.85997 | -40.70959 | 2024-11-28 03:59:00 | NPP-375D | MUCAMBO | CEARÁ | Brasil | 2309003 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 1fdc8d4b-d1ff-33a0-8a73-ebb6d220afa5 | -3.79285 | -50.13509 | 2024-11-28 03:59:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 338734ca-e7c7-30bc-ab51-a99eb3d0afae | -3.04825 | -48.51982 | 2024-11-28 03:59:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a7ba2f2e-3927-3dff-b9b1-0ad76c04a522 | -2.1697 | -52.14269 | 2024-11-28 03:59:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| aef16093-d673-3fed-9626-3dae0827947d | -5.4199 | -47.9168 | 2024-11-28 03:59:00 | NPP-375D | AUGUSTINÓPOLIS | TOCANTINS | Brasil | 1702554 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a2a402bb-a494-3824-a0b2-3e28375c4f3a | -3.35256 | -50.51561 | 2024-11-28 03:59:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 3645e8c5-6d71-3fd7-9ad8-433b888a3cf4 | -4.20709 | -45.29879 | 2024-11-28 03:59:00 | NPP-375D | VITORINO FREIRE | MARANHÃO | Brasil | 2113009 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| dc45af93-7ef2-3809-904a-fc43708ec33d | -3.49588 | -44.60878 | 2024-11-28 03:59:00 | NPP-375D | MIRANDA DO NORTE | MARANHÃO | Brasil | 2106755 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d5aa5511-3d47-3501-a5b7-5a046fb7bb06 | -3.86956 | -46.34126 | 2024-11-28 03:59:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 92f61db3-9814-3d5c-be24-eb93dab1885d | -3.07467 | -48.66705 | 2024-11-28 03:59:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 59d07363-4b70-3307-86d0-fca6732db57a | -2.3937 | -47.16515 | 2024-11-28 03:59:00 | NPP-375D | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| cda7ea85-5d49-3b74-811a-8a4ceb727e0a | -6.48372 | -42.80962 | 2024-11-28 03:59:00 | NPP-375D | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 93667f12-1afc-3236-bf88-7eff30d7c3e4 | -4.47795 | -46.36844 | 2024-11-28 03:59:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 008f5731-b96b-36c4-860d-f36ea12db188 | -3.69693 | -51.3731 | 2024-11-28 03:59:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 1b69501f-6842-310f-b2ef-ed1eaa993c32 | -3.05934 | -51.06314 | 2024-11-28 03:59:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 14d830a6-dee3-350d-b3ae-8505ffb53ef3 | -3.56107 | -46.33922 | 2024-11-28 03:59:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3dff548c-f0a0-3bb0-a077-89256d890954 | -1.65507 | -52.48006 | 2024-11-28 03:59:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b8f2b126-3f35-31ca-bb01-3db4d1be699a | -3.27414 | -50.61182 | 2024-11-28 03:59:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| a363f274-5de5-33f1-84c9-0ac18bed6937 | -9.00326 | -35.99626 | 2024-11-28 03:59:00 | NPP-375D | SÃO JOSÉ DA LAJE | ALAGOAS | Brasil | 2708303 | 27 | 33 | nan | nan | nan | Mata Atlântica | 8.9 |
| e2d3f8ae-986d-306f-9f46-2776ebc92fc0 | -3.3839 | -50.10411 | 2024-11-28 03:59:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |


[Clique aqui para ver as próximas entradas](README38.md)
